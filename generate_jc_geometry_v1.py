#!/usr/bin/env python3
"""
AgentMath - Geometry Generator v1
Junior Cycle Mathematics - SEC Aligned (2022-2025)

12 Levels based on actual SEC exam questions:
1. Naming Shapes & Properties - Foundation
2. Angle Sum of Triangle - Foundation
3. Properties of Quadrilaterals - Foundation
4. Angles with Parallel Lines - Ordinary
5. Symmetry & Transformations - Ordinary
6. Basic Constructions - Ordinary
7. Pythagoras Theorem - Higher
8. Similar Triangles - Higher
9. Scale Drawings - Higher
10. Circle Properties - Mastery
11. Advanced Constructions - Mastery
12. Problem Solving & Proofs - Mastery

SEC References:
- JC 2022-2025 OL/HL papers
- Angle sum of triangle, parallel lines, constructions
- Similar triangles, scale drawings, transformations
"""

import random
import math

TOPIC = "geometry"
MODE = "jc_exam"
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12


# Visual SVG generators
def triangle_svg(angles=None, labels=None, show_right_angle=False):
    """Draw a triangle with optional angle labels"""
    svg = '''<svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg">
    <rect width="200" height="160" fill="#f0f9ff"/>
    '''
    
    # Triangle vertices
    points = "30,130 170,130 100,30"
    svg += f'<polygon points="{points}" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>'
    
    # Labels
    if labels:
        svg += f'<text x="20" y="145" font-size="14" fill="#1e293b">{labels[0]}</text>'
        svg += f'<text x="170" y="145" font-size="14" fill="#1e293b">{labels[1]}</text>'
        svg += f'<text x="95" y="25" font-size="14" fill="#1e293b">{labels[2]}</text>'
    
    # Angles
    if angles:
        svg += f'<text x="45" y="120" font-size="12" fill="#dc2626">{angles[0]}°</text>'
        svg += f'<text x="140" y="120" font-size="12" fill="#dc2626">{angles[1]}°</text>'
        svg += f'<text x="90" y="50" font-size="12" fill="#dc2626">{angles[2]}°</text>'
    
    if show_right_angle:
        svg += '<rect x="160" y="120" width="10" height="10" fill="none" stroke="#1e293b" stroke-width="1"/>'
    
    svg += '</svg>'
    return svg


def quadrilateral_svg(shape_type, angles=None):
    """Draw various quadrilaterals"""
    svg = '''<svg viewBox="0 0 200 150" xmlns="http://www.w3.org/2000/svg">
    <rect width="200" height="150" fill="#fef3c7"/>
    '''
    
    if shape_type == 'rectangle':
        svg += '<rect x="30" y="30" width="140" height="90" fill="#fde68a" stroke="#f59e0b" stroke-width="2"/>'
        # Right angle marks
        for x, y in [(30, 30), (160, 30), (30, 110), (160, 110)]:
            svg += f'<rect x="{x}" y="{y}" width="10" height="10" fill="none" stroke="#1e293b" stroke-width="1"/>'
    elif shape_type == 'parallelogram':
        svg += '<polygon points="50,120 30,40 150,40 170,120" fill="#fde68a" stroke="#f59e0b" stroke-width="2"/>'
    elif shape_type == 'square':
        svg += '<rect x="50" y="30" width="100" height="100" fill="#fde68a" stroke="#f59e0b" stroke-width="2"/>'
    elif shape_type == 'rhombus':
        svg += '<polygon points="100,20 170,75 100,130 30,75" fill="#fde68a" stroke="#f59e0b" stroke-width="2"/>'
    elif shape_type == 'trapezium':
        svg += '<polygon points="50,120 30,40 170,40 150,120" fill="#fde68a" stroke="#f59e0b" stroke-width="2"/>'
    elif shape_type == 'kite':
        svg += '<polygon points="100,20 160,70 100,130 40,70" fill="#fde68a" stroke="#f59e0b" stroke-width="2"/>'
    
    if angles:
        svg += f'<text x="40" y="55" font-size="11" fill="#dc2626">{angles[0]}°</text>'
        svg += f'<text x="145" y="55" font-size="11" fill="#dc2626">{angles[1]}°</text>'
    
    svg += '</svg>'
    return svg


def parallel_lines_svg(angles=None):
    """Draw parallel lines cut by a transversal"""
    svg = '''<svg viewBox="0 0 220 150" xmlns="http://www.w3.org/2000/svg">
    <rect width="220" height="150" fill="#ecfdf5"/>
    
    <!-- Parallel lines -->
    <line x1="20" y1="50" x2="200" y2="50" stroke="#059669" stroke-width="2"/>
    <line x1="20" y1="100" x2="200" y2="100" stroke="#059669" stroke-width="2"/>
    
    <!-- Transversal -->
    <line x1="60" y1="20" x2="160" y2="130" stroke="#3b82f6" stroke-width="2"/>
    
    <!-- Arrows for parallel -->
    <text x="180" y="45" font-size="12" fill="#059669">→</text>
    <text x="180" y="95" font-size="12" fill="#059669">→</text>
    '''
    
    if angles:
        svg += f'<text x="95" y="45" font-size="12" fill="#dc2626">{angles[0]}°</text>'
        svg += f'<text x="115" y="115" font-size="12" fill="#dc2626">{angles[1]}°</text>'
    
    svg += '</svg>'
    return svg


def symmetry_svg(shape_type):
    """Draw shapes with lines of symmetry"""
    svg = '''<svg viewBox="0 0 200 150" xmlns="http://www.w3.org/2000/svg">
    <rect width="200" height="150" fill="#fdf4ff"/>
    '''
    
    if shape_type == 'rectangle':
        svg += '<rect x="40" y="40" width="120" height="70" fill="#e9d5ff" stroke="#9333ea" stroke-width="2"/>'
        svg += '<line x1="100" y1="30" x2="100" y2="120" stroke="#dc2626" stroke-width="1" stroke-dasharray="5,5"/>'
        svg += '<line x1="30" y1="75" x2="170" y2="75" stroke="#dc2626" stroke-width="1" stroke-dasharray="5,5"/>'
    elif shape_type == 'equilateral':
        svg += '<polygon points="100,30 40,120 160,120" fill="#e9d5ff" stroke="#9333ea" stroke-width="2"/>'
        svg += '<line x1="100" y1="30" x2="100" y2="120" stroke="#dc2626" stroke-width="1" stroke-dasharray="5,5"/>'
    elif shape_type == 'isosceles':
        svg += '<polygon points="100,30 50,120 150,120" fill="#e9d5ff" stroke="#9333ea" stroke-width="2"/>'
        svg += '<line x1="100" y1="30" x2="100" y2="120" stroke="#dc2626" stroke-width="1" stroke-dasharray="5,5"/>'
    elif shape_type == 'square':
        svg += '<rect x="50" y="30" width="100" height="100" fill="#e9d5ff" stroke="#9333ea" stroke-width="2"/>'
        svg += '<line x1="100" y1="20" x2="100" y2="140" stroke="#dc2626" stroke-width="1" stroke-dasharray="5,5"/>'
        svg += '<line x1="40" y1="80" x2="160" y2="80" stroke="#dc2626" stroke-width="1" stroke-dasharray="5,5"/>'
    
    svg += '</svg>'
    return svg


def construction_svg(construction_type):
    """Visual for geometric constructions"""
    svg = '''<svg viewBox="0 0 220 120" xmlns="http://www.w3.org/2000/svg">
    <rect width="220" height="120" fill="#f0fdf4"/>
    '''
    
    if construction_type == '60_angle':
        svg += '<line x1="30" y1="90" x2="190" y2="90" stroke="#1e293b" stroke-width="2"/>'
        svg += '<line x1="30" y1="90" x2="110" y2="20" stroke="#1e293b" stroke-width="2"/>'
        svg += '<path d="M 50 90 A 20 20 0 0 1 40 75" fill="none" stroke="#dc2626" stroke-width="1"/>'
        svg += '<text x="55" y="80" font-size="12" fill="#dc2626">60°</text>'
        svg += '<circle cx="30" cy="90" r="60" fill="none" stroke="#3b82f6" stroke-width="1" stroke-dasharray="3,3"/>'
    elif construction_type == 'perpendicular_bisector':
        svg += '<line x1="40" y1="60" x2="180" y2="60" stroke="#1e293b" stroke-width="2"/>'
        svg += '<line x1="110" y1="20" x2="110" y2="100" stroke="#dc2626" stroke-width="2" stroke-dasharray="5,5"/>'
        svg += '<circle cx="40" cy="60" r="50" fill="none" stroke="#3b82f6" stroke-width="1" stroke-dasharray="3,3"/>'
        svg += '<circle cx="180" cy="60" r="50" fill="none" stroke="#3b82f6" stroke-width="1" stroke-dasharray="3,3"/>'
        svg += '<text x="35" y="75" font-size="10" fill="#1e293b">A</text>'
        svg += '<text x="175" y="75" font-size="10" fill="#1e293b">B</text>'
    elif construction_type == 'equilateral':
        svg += '<line x1="40" y1="100" x2="180" y2="100" stroke="#1e293b" stroke-width="2"/>'
        svg += '<line x1="40" y1="100" x2="110" y2="20" stroke="#1e293b" stroke-width="2"/>'
        svg += '<line x1="180" y1="100" x2="110" y2="20" stroke="#1e293b" stroke-width="2"/>'
        svg += '<circle cx="40" cy="100" r="70" fill="none" stroke="#3b82f6" stroke-width="1" stroke-dasharray="3,3" opacity="0.5"/>'
        svg += '<circle cx="180" cy="100" r="70" fill="none" stroke="#3b82f6" stroke-width="1" stroke-dasharray="3,3" opacity="0.5"/>'
    
    svg += '</svg>'
    return svg


def similar_triangles_svg():
    """Draw two similar triangles"""
    svg = '''<svg viewBox="0 0 280 130" xmlns="http://www.w3.org/2000/svg">
    <rect width="280" height="130" fill="#fef3c7"/>
    
    <!-- Larger triangle -->
    <polygon points="20,110 100,110 60,30" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>
    <text x="15" y="120" font-size="10" fill="#1e293b">A</text>
    <text x="95" y="120" font-size="10" fill="#1e293b">B</text>
    <text x="55" y="25" font-size="10" fill="#1e293b">C</text>
    
    <!-- Smaller triangle -->
    <polygon points="160,110 220,110 190,50" fill="#fde68a" stroke="#f59e0b" stroke-width="2"/>
    <text x="155" y="120" font-size="10" fill="#1e293b">D</text>
    <text x="215" y="120" font-size="10" fill="#1e293b">E</text>
    <text x="185" y="45" font-size="10" fill="#1e293b">F</text>
    
    <text x="120" y="75" font-size="14" fill="#64748b">~</text>
    </svg>'''
    return svg


def pythagoras_svg(a, b, c):
    """Draw right triangle for Pythagoras"""
    svg = f'''<svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg">
    <rect width="200" height="160" fill="#ecfdf5"/>
    
    <!-- Right triangle -->
    <polygon points="30,130 170,130 170,40" fill="#d1fae5" stroke="#059669" stroke-width="2"/>
    
    <!-- Right angle mark -->
    <rect x="160" y="120" width="10" height="10" fill="none" stroke="#1e293b" stroke-width="1"/>
    
    <!-- Labels -->
    <text x="90" y="145" font-size="14" fill="#1e293b">{a}</text>
    <text x="175" y="90" font-size="14" fill="#1e293b">{b}</text>
    <text x="85" y="80" font-size="14" fill="#dc2626">{c}</text>
    </svg>'''
    return svg


def scale_drawing_svg():
    """Visual for scale drawings"""
    svg = '''<svg viewBox="0 0 240 120" xmlns="http://www.w3.org/2000/svg">
    <rect width="240" height="120" fill="#f0f9ff"/>
    
    <!-- Small rectangle (drawing) -->
    <rect x="20" y="40" width="60" height="40" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>
    <text x="40" y="65" font-size="10" fill="#1e293b">6 cm</text>
    <text x="5" y="65" font-size="10" fill="#1e293b">4 cm</text>
    
    <!-- Arrow -->
    <text x="95" y="65" font-size="16" fill="#64748b">→</text>
    
    <!-- Large rectangle (actual) -->
    <rect x="120" y="20" width="100" height="80" fill="#fde68a" stroke="#f59e0b" stroke-width="2"/>
    <text x="155" y="65" font-size="10" fill="#1e293b">?</text>
    
    <text x="20" y="100" font-size="10" fill="#059669">Scale 1:5</text>
    </svg>'''
    return svg


def circle_svg(show_parts=None):
    """Draw circle with labeled parts"""
    svg = '''<svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg">
    <rect width="200" height="160" fill="#fdf4ff"/>
    
    <circle cx="100" cy="80" r="60" fill="#f3e8ff" stroke="#9333ea" stroke-width="2"/>
    <circle cx="100" cy="80" r="2" fill="#1e293b"/>
    '''
    
    if show_parts:
        if 'radius' in show_parts:
            svg += '<line x1="100" y1="80" x2="160" y2="80" stroke="#dc2626" stroke-width="2"/>'
            svg += '<text x="125" y="75" font-size="10" fill="#dc2626">radius</text>'
        if 'diameter' in show_parts:
            svg += '<line x1="40" y1="80" x2="160" y2="80" stroke="#3b82f6" stroke-width="2"/>'
            svg += '<text x="85" y="95" font-size="10" fill="#3b82f6">diameter</text>'
        if 'chord' in show_parts:
            svg += '<line x1="55" y1="50" x2="145" y2="110" stroke="#059669" stroke-width="2"/>'
            svg += '<text x="110" y="65" font-size="10" fill="#059669">chord</text>'
    
    svg += '</svg>'
    return svg


def make_options(correct, wrong_set):
    """Create 4 unique options with correct answer included"""
    correct_str = str(correct)
    wrong_list = [str(w) for w in wrong_set if str(w) != correct_str]
    random.shuffle(wrong_list)
    
    options = [correct_str] + wrong_list[:3]
    
    while len(options) < 4:
        if isinstance(correct, (int, float)):
            wrong = correct + random.choice([-2, -1, 1, 2]) * random.randint(1, 5)
        else:
            wrong = f"Option {random.randint(1, 99)}"
        if str(wrong) not in options:
            options.append(str(wrong))
    
    random.shuffle(options)
    correct_idx = options.index(correct_str)
    return options, correct_idx


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


# Level 1: Naming Shapes & Properties
def gen_level_1(n=50):
    """Foundation: Identify and name basic shapes"""
    qs = []
    used = set()
    
    for _ in range(n * 40):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['identify', 'sides', 'properties', 'angles_name', 'classify', 'angles_count', 'regular'])
        
        if qtype == 'identify':
            shapes = [
                ('triangle', 3, 'A shape with 3 sides'),
                ('quadrilateral', 4, 'A shape with 4 sides'),
                ('pentagon', 5, 'A shape with 5 sides'),
                ('hexagon', 6, 'A shape with 6 sides'),
                ('heptagon', 7, 'A shape with 7 sides'),
                ('octagon', 8, 'A shape with 8 sides'),
                ('nonagon', 9, 'A shape with 9 sides'),
                ('decagon', 10, 'A shape with 10 sides'),
            ]
            name, sides, desc = random.choice(shapes)
            txt = f"What is the name of a polygon with {sides} sides?"
            ans = name.capitalize()
            wrongs = {s[0].capitalize() for s in shapes if s[0] != name}
            vis = triangle_svg() if sides == 3 else quadrilateral_svg('rectangle')
            exp = f"A polygon with {sides} sides is called a {name}"
            
        elif qtype == 'sides':
            shapes = [
                ('Triangle', 3),
                ('Quadrilateral', 4),
                ('Pentagon', 5),
                ('Hexagon', 6),
                ('Heptagon', 7),
                ('Octagon', 8),
                ('Nonagon', 9),
                ('Decagon', 10),
            ]
            name, sides = random.choice(shapes)
            txt = f"How many sides does a {name.lower()} have?"
            ans = str(sides)
            wrongs = {str(sides + 1), str(sides - 1) if sides > 3 else "2", str(sides + 2), str(sides * 2)}
            vis = triangle_svg() if sides == 3 else quadrilateral_svg('rectangle')
            exp = f"A {name.lower()} has {sides} sides"
            
        elif qtype == 'properties':
            props = [
                ('square', '4 equal sides and 4 right angles'),
                ('rectangle', '4 right angles and opposite sides equal'),
                ('rhombus', '4 equal sides (but angles not necessarily 90°)'),
                ('parallelogram', 'opposite sides parallel and equal'),
                ('trapezium', 'exactly one pair of parallel sides'),
                ('kite', 'two pairs of adjacent sides equal'),
            ]
            name, desc = random.choice(props)
            txt = f"Which shape has: {desc}?"
            ans = name.capitalize()
            wrongs = {p[0].capitalize() for p in props if p[0] != name}
            vis = quadrilateral_svg(name if name in ['square', 'rectangle', 'rhombus', 'parallelogram', 'trapezium', 'kite'] else 'rectangle')
            exp = f"A {name} has {desc}"
            
        elif qtype == 'angles_name':
            angle_types = [
                ('acute', 'less than 90°', random.randint(10, 89)),
                ('right', 'exactly 90°', 90),
                ('obtuse', 'between 90° and 180°', random.randint(91, 179)),
                ('straight', 'exactly 180°', 180),
                ('reflex', 'between 180° and 360°', random.randint(181, 359)),
            ]
            name, desc, val = random.choice(angle_types)
            txt = f"An angle of {val}° is called:"
            ans = f"{name.capitalize()} angle"
            wrongs = {f"{a[0].capitalize()} angle" for a in angle_types if a[0] != name}
            vis = triangle_svg(angles=[min(val, 60), 60, 60])
            exp = f"An angle of {val}° ({desc}) is called a {name} angle"
            
        elif qtype == 'classify':
            triangles = [
                ('equilateral', 'all sides equal'),
                ('isosceles', 'two sides equal'),
                ('scalene', 'no sides equal'),
                ('right-angled', 'one angle is 90°'),
                ('acute-angled', 'all angles less than 90°'),
                ('obtuse-angled', 'one angle greater than 90°'),
            ]
            name, desc = random.choice(triangles)
            txt = f"A triangle with {desc} is called:"
            ans = f"{name.capitalize()} triangle"
            wrongs = {f"{t[0].capitalize()} triangle" for t in triangles if t[0] != name}
            vis = triangle_svg()
            exp = f"A triangle with {desc} is called a {name} triangle"
            
        elif qtype == 'angles_count':
            shapes = [
                ('triangle', 3),
                ('quadrilateral', 4),
                ('pentagon', 5),
                ('hexagon', 6),
            ]
            name, angles = random.choice(shapes)
            txt = f"How many angles does a {name} have?"
            ans = str(angles)
            wrongs = {str(angles + 1), str(angles - 1) if angles > 3 else "2", str(angles + 2), str(angles * 2)}
            vis = triangle_svg() if angles == 3 else quadrilateral_svg('rectangle')
            exp = f"A {name} has {angles} angles (same as the number of sides)"
            
        else:  # regular
            shapes = [
                ('regular pentagon', 5, 108),
                ('regular hexagon', 6, 120),
                ('regular octagon', 8, 135),
            ]
            name, sides, angle = random.choice(shapes)
            txt = f"Each interior angle of a {name} is:"
            ans = f"{angle}°"
            wrongs = {f"{angle + 10}°", f"{angle - 10}°", f"{180}°", f"{90}°"}
            vis = quadrilateral_svg('rectangle')
            exp = f"Interior angle of {name} = (({sides}-2) × 180°) ÷ {sides} = {angle}°"
        
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


# Level 2: Angle Sum of Triangle
def gen_level_2(n=50):
    """Foundation: Angles in a triangle sum to 180°"""
    qs = []
    used = set()
    
    for _ in range(n * 25):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['find_third', 'rule', 'isosceles', 'equilateral', 'right_triangle'])
        
        if qtype == 'find_third':
            # SEC style: Two angles given, find third
            a1 = random.randint(30, 80)
            a2 = random.randint(30, 80)
            while a1 + a2 >= 170:
                a2 = random.randint(30, 80)
            a3 = 180 - a1 - a2
            txt = f"A triangle has angles of {a1}° and {a2}°. Find the third angle."
            ans = f"{a3}°"
            wrongs = {f"{a3 + 10}°", f"{a3 - 10}°", f"{180 - a1}°", f"{a1 + a2}°"}
            vis = triangle_svg(angles=[a1, a2, '?'])
            exp = f"Angles in a triangle sum to 180°. Third angle = 180° - {a1}° - {a2}° = {a3}°"
            
        elif qtype == 'rule':
            txt = "What do the angles in any triangle add up to?"
            ans = "180°"
            wrongs = {"90°", "360°", "270°", "100°"}
            vis = triangle_svg(angles=[60, 60, 60])
            exp = "The angle sum of any triangle is 180°"
            
        elif qtype == 'isosceles':
            base_angle = random.choice([40, 50, 55, 65, 70, 75])
            apex = 180 - 2 * base_angle
            txt = f"An isosceles triangle has two equal angles of {base_angle}°. Find the third angle."
            ans = f"{apex}°"
            wrongs = {f"{base_angle}°", f"{180 - base_angle}°", f"{apex + 10}°", f"{apex - 10}°"}
            vis = triangle_svg(angles=[base_angle, base_angle, '?'])
            exp = f"Third angle = 180° - {base_angle}° - {base_angle}° = {apex}°"
            
        elif qtype == 'equilateral':
            txt = "What is the size of each angle in an equilateral triangle?"
            ans = "60°"
            wrongs = {"90°", "45°", "120°", "30°"}
            vis = triangle_svg(angles=[60, 60, 60])
            exp = "All angles equal: 180° ÷ 3 = 60°"
            
        else:  # right_triangle
            other = random.choice([30, 35, 40, 45, 50, 55, 60])
            third = 90 - other
            txt = f"A right-angled triangle has one angle of {other}°. Find the third angle."
            ans = f"{third}°"
            wrongs = {f"{90 - third}°", f"{180 - other}°", f"{other}°", f"{third + 10}°"}
            vis = triangle_svg(angles=[90, other, '?'], show_right_angle=True)
            exp = f"Right angle = 90°. Third angle = 180° - 90° - {other}° = {third}°"
        
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


# Level 3: Properties of Quadrilaterals
def gen_level_3(n=50):
    """Foundation: Properties of squares, rectangles, parallelograms"""
    qs = []
    used = set()
    
    for _ in range(n * 40):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['angle_sum', 'rectangle_angles', 'parallelogram', 'identify_property', 'diagonal', 'find_angle', 'true_false'])
        
        if qtype == 'angle_sum':
            txt = "What do the angles in any quadrilateral add up to?"
            ans = "360°"
            wrongs = {"180°", "270°", "450°", "90°"}
            vis = quadrilateral_svg('rectangle')
            exp = "The angle sum of any quadrilateral is 360°"
            
        elif qtype == 'rectangle_angles':
            txt = "All angles in a rectangle are:"
            ans = "90° (right angles)"
            wrongs = {"60°", "45°", "180°", "Equal but not 90°"}
            vis = quadrilateral_svg('rectangle')
            exp = "A rectangle has 4 right angles (90° each)"
            
        elif qtype == 'parallelogram':
            a1 = random.choice([55, 60, 65, 70, 75, 80, 85, 100, 105, 110, 115, 120, 125])
            a2 = 180 - a1
            variant = random.choice(['opposite', 'adjacent', 'all_four'])
            if variant == 'opposite':
                txt = f"In a parallelogram, one angle is {a1}°. What is the opposite angle?"
                ans = f"{a1}°"
                wrongs = {f"{a2}°", f"{180 - a1}°", f"{360 - a1}°", f"{a1 + 10}°"}
                exp = f"Opposite angles in a parallelogram are equal: {a1}°"
            elif variant == 'adjacent':
                txt = f"In a parallelogram, one angle is {a1}°. What is an adjacent angle?"
                ans = f"{a2}°"
                wrongs = {f"{a1}°", f"{360 - a1}°", f"{a2 + 10}°", f"{90}°"}
                exp = f"Adjacent angles in a parallelogram add to 180°: {a2}°"
            else:
                txt = f"In a parallelogram, one angle is {a1}°. What are the four angles?"
                ans = f"{a1}°, {a2}°, {a1}°, {a2}°"
                wrongs = {f"{a1}°, {a1}°, {a1}°, {a1}°", f"{90}°, {90}°, {90}°, {90}°", 
                         f"{a1}°, {a1}°, {a2}°, {a2}°", f"{a2}°, {a2}°, {a2}°, {a2}°"}
                exp = f"Opposite angles equal, adjacent angles supplementary: {a1}°, {a2}°, {a1}°, {a2}°"
            vis = quadrilateral_svg('parallelogram', angles=[a1, a2])
            
        elif qtype == 'identify_property':
            props = [
                ('square', 'All sides equal AND all angles 90°'),
                ('rectangle', 'Opposite sides equal AND all angles 90°'),
                ('rhombus', 'All sides equal but angles NOT all 90°'),
                ('parallelogram', 'Opposite sides parallel and equal'),
                ('trapezium', 'Exactly one pair of parallel sides'),
                ('kite', 'Two pairs of adjacent equal sides'),
            ]
            name, prop = random.choice(props)
            txt = f"Which property describes a {name}?"
            ans = prop
            wrongs = {p[1] for p in props if p[0] != name}
            vis = quadrilateral_svg(name if name in ['square', 'rectangle', 'rhombus', 'parallelogram', 'trapezium', 'kite'] else 'rectangle')
            exp = f"A {name} has: {prop}"
            
        elif qtype == 'diagonal':
            shapes = [
                ('square', 'equal and bisect at right angles'),
                ('rectangle', 'equal and bisect each other'),
                ('rhombus', 'bisect at right angles but not equal'),
                ('parallelogram', 'bisect each other'),
                ('kite', 'one bisects the other at right angles'),
            ]
            name, diag = random.choice(shapes)
            txt = f"The diagonals of a {name}:"
            ans = diag.capitalize()
            wrongs = {s[1].capitalize() for s in shapes if s[0] != name}
            vis = quadrilateral_svg(name if name in ['square', 'rectangle', 'rhombus', 'parallelogram', 'kite'] else 'rectangle')
            exp = f"In a {name}, the diagonals {diag}"
            
        elif qtype == 'find_angle':
            # Three angles given, find fourth
            a1 = random.randint(70, 100)
            a2 = random.randint(70, 100)
            a3 = random.randint(70, 100)
            a4 = 360 - a1 - a2 - a3
            if a4 > 0 and a4 < 180:
                txt = f"A quadrilateral has angles {a1}°, {a2}°, and {a3}°. Find the fourth angle."
                ans = f"{a4}°"
                wrongs = {f"{a4 + 10}°", f"{a4 - 10}°", f"{180 - a4}°", f"{90}°"}
                vis = quadrilateral_svg('trapezium')
                exp = f"Fourth angle = 360° - {a1}° - {a2}° - {a3}° = {a4}°"
            else:
                continue
                
        else:  # true_false
            statements = [
                ("A square is a special type of rectangle", True),
                ("A rectangle is a special type of parallelogram", True),
                ("All parallelograms are rectangles", False),
                ("A rhombus has all sides equal", True),
                ("All quadrilaterals have parallel sides", False),
                ("A square is also a rhombus", True),
            ]
            statement, is_true = random.choice(statements)
            txt = f"True or False: {statement}"
            ans = "True" if is_true else "False"
            wrongs = {"True", "False", "Sometimes", "Cannot determine"}
            vis = quadrilateral_svg('square' if 'square' in statement.lower() else 'rectangle')
            exp = f"{statement} - {ans}"
        
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


# Level 4: Angles with Parallel Lines
def gen_level_4(n=50):
    """Ordinary: Corresponding, alternate, co-interior angles"""
    qs = []
    used = set()
    
    for _ in range(n * 25):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['corresponding', 'alternate', 'co_interior', 'identify', 'calculate'])
        
        if qtype == 'corresponding':
            angle = random.randint(40, 140)
            txt = f"Two parallel lines are cut by a transversal. One angle is {angle}°. What is the corresponding angle?"
            ans = f"{angle}°"
            wrongs = {f"{180 - angle}°", f"{90 - angle}°" if angle < 90 else f"{angle - 90}°", f"{angle + 10}°", f"{360 - angle}°"}
            vis = parallel_lines_svg(angles=[angle, angle])
            exp = f"Corresponding angles are equal: {angle}°"
            
        elif qtype == 'alternate':
            angle = random.randint(40, 140)
            txt = f"Two parallel lines are cut by a transversal. One angle is {angle}°. What is the alternate angle?"
            ans = f"{angle}°"
            wrongs = {f"{180 - angle}°", f"{angle + 10}°", f"{angle - 10}°", f"{90}°"}
            vis = parallel_lines_svg(angles=[angle, angle])
            exp = f"Alternate angles are equal: {angle}°"
            
        elif qtype == 'co_interior':
            angle = random.randint(40, 140)
            other = 180 - angle
            txt = f"Two parallel lines are cut by a transversal. One co-interior angle is {angle}°. Find the other."
            ans = f"{other}°"
            wrongs = {f"{angle}°", f"{360 - angle}°", f"{other + 10}°", f"{90}°"}
            vis = parallel_lines_svg(angles=[angle, other])
            exp = f"Co-interior angles add to 180°: {other}°"
            
        elif qtype == 'identify':
            angle_types = [
                ('corresponding', 'are equal (F-shape)'),
                ('alternate', 'are equal (Z-shape)'),
                ('co-interior', 'add to 180° (C-shape or U-shape)'),
            ]
            name, rule = random.choice(angle_types)
            txt = f"When parallel lines are cut by a transversal, {name} angles:"
            ans = rule.capitalize()
            wrongs = {a[1].capitalize() for a in angle_types if a[0] != name}
            wrongs.add("Are always 90°")
            vis = parallel_lines_svg()
            exp = f"{name.capitalize()} angles {rule}"
            
        else:  # calculate - SEC style
            given = random.randint(40, 85)
            # Find angle using combination of rules
            txt = f"Lines l and k are parallel. Angle a = {given}°. Find angle b on the other parallel line (alternate to a)."
            ans = f"{given}°"
            wrongs = {f"{180 - given}°", f"{given + 10}°", f"{90}°", f"{360 - given}°"}
            vis = parallel_lines_svg(angles=[given, '?'])
            exp = f"Alternate angles are equal, so b = {given}°"
        
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


# Level 5: Symmetry & Transformations
def gen_level_5(n=50):
    """Ordinary: Line symmetry, rotational symmetry, transformations"""
    qs = []
    used = set()
    
    for _ in range(n * 40):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['lines_of_symmetry', 'rotational', 'rotation_angle', 'reflection', 'identify', 'rotation_image', 'central_symmetry'])
        
        if qtype == 'lines_of_symmetry':
            shapes = [
                ('square', 4),
                ('rectangle', 2),
                ('equilateral triangle', 3),
                ('isosceles triangle', 1),
                ('regular hexagon', 6),
                ('regular pentagon', 5),
                ('parallelogram', 0),
                ('rhombus', 2),
                ('scalene triangle', 0),
                ('kite', 1),
            ]
            name, lines = random.choice(shapes)
            txt = f"How many lines of symmetry does a {name} have?"
            ans = str(lines)
            wrongs = {str(lines + 1) if isinstance(lines, int) else "1", 
                     str(max(0, lines - 1)),
                     str(lines + 2) if isinstance(lines, int) else "2", 
                     str(lines + 3) if lines < 3 else "1"}
            vis = symmetry_svg('square' if 'square' in name else ('equilateral' if 'equilateral' in name else 'rectangle'))
            exp = f"A {name} has {lines} line(s) of symmetry"
            
        elif qtype == 'rotational':
            shapes = [
                ('square', 4),
                ('rectangle', 2),
                ('equilateral triangle', 3),
                ('regular hexagon', 6),
                ('parallelogram', 2),
                ('regular pentagon', 5),
                ('rhombus', 2),
            ]
            name, order = random.choice(shapes)
            txt = f"What is the order of rotational symmetry of a {name}?"
            ans = str(order)
            wrongs = {str(order + 1), str(max(1, order - 1)), str(order + 2), "1"}
            vis = symmetry_svg('square' if 'square' in name else 'rectangle')
            exp = f"A {name} has rotational symmetry of order {order}"
            
        elif qtype == 'rotation_angle':
            angles = [90, 180, 270, 360]
            angle = random.choice(angles)
            direction = random.choice(['clockwise', 'anticlockwise'])
            txt = f"A shape is rotated {angle}° {direction} about a point. How many right angles is this?"
            ans = str(angle // 90)
            wrongs = {str(angle // 90 + 1), str(max(0, angle // 90 - 1)), str(angle // 45), "5"}
            vis = symmetry_svg('square')
            exp = f"{angle}° = {angle // 90} right angle(s)"
            
        elif qtype == 'reflection':
            txt = "When a shape is reflected in a mirror line:"
            ans = "The image is the same distance from the line as the original"
            wrongs = {"The image is rotated", "The image changes size", "The image moves parallel to the line", "The shape disappears"}
            vis = symmetry_svg('rectangle')
            exp = "Reflection creates a mirror image equidistant from the line"
            
        elif qtype == 'identify':
            transformations = [
                ('reflection', 'flips the shape over a line'),
                ('rotation', 'turns the shape around a point'),
                ('translation', 'slides the shape without turning'),
                ('enlargement', 'changes the size of the shape'),
            ]
            name, desc = random.choice(transformations)
            txt = f"Which transformation {desc}?"
            ans = name.capitalize()
            wrongs = {t[0].capitalize() for t in transformations if t[0] != name}
            vis = symmetry_svg('square')
            exp = f"{name.capitalize()} {desc}"
            
        elif qtype == 'rotation_image':
            # SEC style: point rotation
            original = random.choice(['A', 'B', 'C', 'P', 'Q'])
            angle = random.choice([90, 180, 270])
            direction = random.choice(['clockwise', 'anticlockwise'])
            txt = f"Point {original} is rotated {angle}° {direction} about the origin. What transformation is this?"
            ans = f"Rotation of {angle}° {direction}"
            wrongs = {f"Rotation of {angle}° {'anticlockwise' if direction == 'clockwise' else 'clockwise'}",
                     f"Reflection in the x-axis", f"Translation", f"Rotation of {180 if angle != 180 else 90}°"}
            vis = symmetry_svg('square')
            exp = f"This is a rotation of {angle}° {direction} about the origin"
            
        else:  # central_symmetry
            txt = "Central symmetry in a point P means:"
            ans = "Every point maps to a point the same distance from P but on the opposite side"
            wrongs = {"Reflection in a horizontal line through P", "Rotation of 90° about P",
                     "Translation by vector P", "The shape stays in the same place"}
            vis = symmetry_svg('rectangle')
            exp = "Central symmetry = rotation of 180° about the centre point"
        
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


# Level 6: Basic Constructions
def gen_level_6(n=50):
    """Ordinary: Construct angles, triangles using compass and ruler"""
    qs = []
    used = set()
    
    for _ in range(n * 40):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['60_angle', 'equilateral', 'bisector', 'perpendicular', 'steps', 'tools', '90_angle', 'triangle_sas'])
        
        if qtype == '60_angle':
            txt = "To construct an angle of 60° using compass and ruler, you need to construct:"
            ans = "An equilateral triangle (all angles 60°)"
            wrongs = {"A right angle and bisect it", "A square", "Two parallel lines", "A circle"}
            vis = construction_svg('60_angle')
            exp = "An equilateral triangle has all angles = 60°"
            
        elif qtype == 'equilateral':
            side_len = random.randint(4, 10)
            txt = f"To construct an equilateral triangle with side {side_len} cm, the compass should be set to:"
            ans = f"{side_len} cm"
            wrongs = {f"{side_len // 2} cm", f"{side_len * 2} cm", f"{side_len + 2} cm", "Any length"}
            vis = construction_svg('equilateral')
            exp = f"All sides equal, so compass radius = {side_len} cm"
            
        elif qtype == 'bisector':
            angle = random.choice([40, 60, 80, 100, 120])
            half = angle // 2
            txt = f"An angle of {angle}° is bisected. Each new angle measures:"
            ans = f"{half}°"
            wrongs = {f"{angle}°", f"{half + 10}°", f"{half - 5}°" if half > 5 else f"{half + 5}°", f"{180 - half}°"}
            vis = construction_svg('60_angle')
            exp = f"Bisecting {angle}° gives two angles of {half}° each"
            
        elif qtype == 'perpendicular':
            txt = "A perpendicular bisector of a line segment:"
            ans = "Passes through the midpoint at 90°"
            wrongs = {"Passes through one end at 90°", "Is parallel to the line", "Touches the line at any point", "Bisects without being perpendicular"}
            vis = construction_svg('perpendicular_bisector')
            exp = "Perpendicular bisector: through midpoint, at right angles"
            
        elif qtype == 'steps':
            constructions = [
                ("perpendicular bisector", "Draw arcs from both endpoints with the same radius, then connect the intersections"),
                ("60° angle", "Draw an arc from the vertex, then an arc of the same radius from where it crosses the line"),
                ("angle bisector", "Draw an arc from the vertex, then equal arcs from where it crosses both arms"),
                ("equilateral triangle", "Set compass to the base length, draw arcs from both ends of the base"),
            ]
            name, steps = random.choice(constructions)
            txt = f"What is the key step in constructing a {name}?"
            ans = steps
            wrongs = {c[1] for c in constructions if c[0] != name}
            vis = construction_svg('perpendicular_bisector' if 'bisector' in name else '60_angle')
            exp = f"To construct a {name}: {steps}"
            
        elif qtype == 'tools':
            txt = "Which tools are allowed for geometric constructions in the Junior Cert?"
            ans = "Compass and straight edge (ruler without measurements)"
            wrongs = {"Protractor and ruler", "Set square only", "Any measuring tools", "Calculator and ruler"}
            vis = construction_svg('equilateral')
            exp = "Only compass and straight edge are allowed for pure constructions"
            
        elif qtype == '90_angle':
            txt = "To construct a 90° angle, you can:"
            ans = "Construct a 60° angle, then bisect a 30° angle from it to add"
            wrongs = {"Use a protractor", "Draw a square", "It cannot be done with compass and ruler", "Draw any two lines"}
            vis = construction_svg('perpendicular_bisector')
            exp = "Alternatively: construct perpendicular bisector of a line segment"
            
        else:  # triangle_sas
            # SEC OL style: Construct triangle SAS
            side1 = random.randint(5, 10)
            angle = random.choice([40, 50, 60, 70, 80])
            side2 = random.randint(4, 8)
            txt = f"To construct triangle ABC with |AB| = {side1} cm, ∠CAB = {angle}°, |AC| = {side2} cm, you first:"
            ans = f"Draw AB = {side1} cm, construct {angle}° at A, mark C at {side2} cm from A"
            wrongs = {f"Draw any triangle and measure", f"Start with the {angle}° angle", 
                     f"Draw a circle of radius {side1} cm", f"Use trial and error"}
            vis = construction_svg('equilateral')
            exp = f"SAS construction: draw base, construct angle, measure second side"
        
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


# Level 7: Pythagoras Theorem
def gen_level_7(n=50):
    """Higher: Find missing sides using Pythagoras"""
    qs = []
    used = set()
    
    # Pythagorean triples
    triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (6, 8, 10), (9, 12, 15), (12, 16, 20)]
    
    for _ in range(n * 25):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['find_hyp', 'find_side', 'identify', 'check', 'word_problem'])
        
        if qtype == 'find_hyp':
            a, b, c = random.choice(triples)
            mult = random.choice([1, 2])
            a, b, c = a * mult, b * mult, c * mult
            txt = f"Find the hypotenuse of a right-angled triangle with sides {a} cm and {b} cm."
            ans = f"{c} cm"
            wrongs = {f"{a + b} cm", f"{c + 1} cm", f"{c - 1} cm", f"{int(math.sqrt(a*a + b*b) + 2)} cm"}
            vis = pythagoras_svg(f"{a} cm", f"{b} cm", "?")
            exp = f"c² = a² + b² = {a}² + {b}² = {a*a} + {b*b} = {c*c}. c = {c} cm"
            
        elif qtype == 'find_side':
            a, b, c = random.choice(triples)
            mult = random.choice([1, 2])
            a, b, c = a * mult, b * mult, c * mult
            txt = f"A right-angled triangle has hypotenuse {c} cm and one side {a} cm. Find the other side."
            ans = f"{b} cm"
            wrongs = {f"{c - a} cm", f"{b + 1} cm", f"{b - 1} cm", f"{a} cm"}
            vis = pythagoras_svg(f"{a} cm", "?", f"{c} cm")
            exp = f"b² = c² - a² = {c}² - {a}² = {c*c} - {a*a} = {b*b}. b = {b} cm"
            
        elif qtype == 'identify':
            txt = "In a right-angled triangle, the hypotenuse is:"
            ans = "The longest side, opposite the right angle"
            wrongs = {"The shortest side", "Any side with the right angle", "Always horizontal", "The base"}
            vis = pythagoras_svg("a", "b", "c (hyp)")
            exp = "The hypotenuse is always opposite the 90° angle and is the longest side"
            
        elif qtype == 'check':
            a, b, c = random.choice(triples[:4])
            is_right = random.choice([True, False])
            if not is_right:
                c = c + 1
            txt = f"Can a triangle with sides {a}, {b}, and {c} be right-angled?"
            if is_right:
                ans = f"Yes, because {a}² + {b}² = {c}²"
                wrongs = {"No, the sides are too different", "Yes, because sides are consecutive", "No, it's isosceles"}
            else:
                ans = f"No, because {a}² + {b}² ≠ {c}²"
                wrongs = {f"Yes, because {a}² + {b}² = {c}²", "Yes, all triangles can be", "Cannot determine"}
            vis = pythagoras_svg(str(a), str(b), str(c))
            exp = f"{a}² + {b}² = {a*a + b*b}, {c}² = {c*c}. " + ("Equal, so right-angled" if is_right else "Not equal, so not right-angled")
            
        else:  # word_problem
            a, b, c = random.choice(triples[:3])
            mult = random.randint(1, 3)
            a, b, c = a * mult, b * mult, c * mult
            contexts = [
                (f"A ladder {c}m long leans against a wall. The base is {a}m from the wall. How high up the wall does it reach?", b),
                (f"A rectangular field is {a}m by {b}m. What is the length of the diagonal?", c),
            ]
            context, answer = random.choice(contexts)
            txt = context
            ans = f"{answer}m"
            wrongs = {f"{answer + 1}m", f"{answer - 1}m", f"{a + b}m", f"{c}m" if answer != c else f"{a}m"}
            vis = pythagoras_svg(f"{a}m", "?", f"{c}m") if answer == b else pythagoras_svg(f"{a}m", f"{b}m", "?")
            exp = f"Using Pythagoras: answer = {answer}m"
        
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


# Level 8: Similar Triangles
def gen_level_8(n=50):
    """Higher: Identify and use similar triangles"""
    qs = []
    used = set()
    
    for _ in range(n * 25):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['find_side', 'ratio', 'identify', 'scale_factor', 'area_ratio'])
        
        if qtype == 'find_side':
            # SEC style: Given corresponding sides, find missing
            scale = random.choice([2, 3, 4, 5])
            small_side = random.randint(3, 8)
            large_side = small_side * scale
            other_small = random.randint(4, 10)
            other_large = other_small * scale
            txt = f"Triangles ABC and DEF are similar. |AB| = {small_side} cm, |DE| = {large_side} cm, |BC| = {other_small} cm. Find |EF|."
            ans = f"{other_large} cm"
            wrongs = {f"{other_small} cm", f"{other_large + small_side} cm", f"{other_large - 2} cm", f"{other_small * 2} cm"}
            vis = similar_triangles_svg()
            exp = f"Scale factor = {large_side}/{small_side} = {scale}. |EF| = {other_small} × {scale} = {other_large} cm"
            
        elif qtype == 'ratio':
            scale = random.choice([2, 3, 4])
            s1, s2 = random.randint(3, 6), random.randint(3, 6) * scale
            txt = f"Two similar triangles have corresponding sides {s1} cm and {s2} cm. What is the scale factor?"
            ans = f"{s2 // s1}" if s2 % s1 == 0 else f"{s2}/{s1}"
            wrongs = {f"{s1}", f"{s2}", f"{s1 + s2}", f"{abs(s2 - s1)}"}
            vis = similar_triangles_svg()
            exp = f"Scale factor = {s2} ÷ {s1} = {s2 // s1 if s2 % s1 == 0 else f'{s2}/{s1}'}"
            
        elif qtype == 'identify':
            txt = "Two triangles are similar if:"
            ans = "All corresponding angles are equal"
            wrongs = {"All sides are equal", "They have the same area", "One side is equal", "They are congruent"}
            vis = similar_triangles_svg()
            exp = "Similar triangles have equal angles but proportional (not equal) sides"
            
        elif qtype == 'scale_factor':
            sf = random.choice([2, 3, 4, 5])
            side = random.randint(4, 10)
            txt = f"A triangle is enlarged by scale factor {sf}. If one side was {side} cm, what is it now?"
            ans = f"{side * sf} cm"
            wrongs = {f"{side + sf} cm", f"{side * sf - 1} cm", f"{side} cm", f"{side * sf + 2} cm"}
            vis = similar_triangles_svg()
            exp = f"New length = {side} × {sf} = {side * sf} cm"
            
        else:  # area_ratio
            sf = random.choice([2, 3])
            area1 = random.randint(10, 20)
            area2 = area1 * sf * sf
            txt = f"Two similar triangles have scale factor {sf}. If the smaller has area {area1} cm², find the larger area."
            ans = f"{area2} cm²"
            wrongs = {f"{area1 * sf} cm²", f"{area1 + sf} cm²", f"{area2 - area1} cm²", f"{area1} cm²"}
            vis = similar_triangles_svg()
            exp = f"Area ratio = (scale factor)² = {sf}² = {sf*sf}. Larger area = {area1} × {sf*sf} = {area2} cm²"
        
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


# Level 9: Scale Drawings
def gen_level_9(n=50):
    """Higher: Work with scale drawings"""
    qs = []
    used = set()
    
    for _ in range(n * 25):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['drawing_to_actual', 'actual_to_drawing', 'scale_ratio', 'perimeter', 'interpret'])
        
        if qtype == 'drawing_to_actual':
            # SEC style: Given scale, find actual distance
            scales = [(1, 5), (1, 10), (1, 50), (1, 100), (1, 200)]
            s1, s2 = random.choice(scales)
            drawing = random.randint(3, 15)
            actual = drawing * s2 // s1
            units = random.choice([('cm', 'm', 100), ('cm', 'cm', 1)])
            txt = f"A scale drawing uses scale 1:{s2}. A length of {drawing} cm on the drawing represents what actual length?"
            ans = f"{actual} cm" if units[2] == 1 else f"{actual / 100} m"
            wrongs = {f"{drawing} cm", f"{actual + 10} cm" if units[2] == 1 else f"{(actual + 10) / 100} m",
                     f"{drawing * 2} cm" if units[2] == 1 else f"{drawing * 2 / 100} m", f"{s2} cm"}
            vis = scale_drawing_svg()
            exp = f"Actual = Drawing × Scale = {drawing} × {s2} = {actual} cm"
            
        elif qtype == 'actual_to_drawing':
            scales = [(1, 10), (1, 20), (1, 50), (1, 100)]
            s1, s2 = random.choice(scales)
            actual = random.choice([50, 100, 150, 200, 300, 400, 500])
            drawing = actual // s2
            txt = f"Using scale 1:{s2}, how long should a {actual} cm actual length be drawn?"
            ans = f"{drawing} cm"
            wrongs = {f"{actual} cm", f"{drawing + 1} cm", f"{drawing * 2} cm", f"{s2} cm"}
            vis = scale_drawing_svg()
            exp = f"Drawing = Actual ÷ Scale = {actual} ÷ {s2} = {drawing} cm"
            
        elif qtype == 'scale_ratio':
            drawing = random.choice([2, 4, 5, 8, 10])
            actual = drawing * random.choice([5, 10, 20, 25, 50])
            txt = f"A drawing shows a {actual} m wall as {drawing} cm. What is the scale?"
            ratio = actual * 100 // drawing  # Convert m to cm
            ans = f"1:{ratio}"
            wrongs = {f"1:{ratio // 2}", f"1:{ratio * 2}", f"{drawing}:{actual}", f"1:{actual}"}
            vis = scale_drawing_svg()
            exp = f"Scale = Drawing:Actual = {drawing}:{actual * 100} = 1:{ratio}"
            
        elif qtype == 'perimeter':
            # SEC style: Find actual perimeter
            scale = random.choice([50, 100, 200])
            draw_l, draw_w = random.randint(4, 8), random.randint(3, 6)
            actual_l, actual_w = draw_l * scale, draw_w * scale
            perimeter = 2 * (actual_l + actual_w)
            txt = f"A rectangular garden is drawn as {draw_l} cm × {draw_w} cm with scale 1:{scale}. Find the actual perimeter."
            ans = f"{perimeter} cm" if scale < 100 else f"{perimeter / 100} m"
            wrongs = {f"{2 * (draw_l + draw_w)} cm", f"{perimeter // 2} cm" if scale < 100 else f"{perimeter / 200} m",
                     f"{actual_l * actual_w} cm²", f"{perimeter + 100} cm" if scale < 100 else f"{(perimeter + 100) / 100} m"}
            vis = scale_drawing_svg()
            exp = f"Actual L = {draw_l} × {scale} = {actual_l}. Actual W = {draw_w} × {scale} = {actual_w}. Perimeter = 2({actual_l} + {actual_w}) = {perimeter}"
            
        else:  # interpret
            txt = "A scale of 1:200 means:"
            ans = "1 cm on the drawing represents 200 cm (2 m) in real life"
            wrongs = {"200 cm on the drawing represents 1 cm in real life", 
                     "The drawing is 200 times larger than actual",
                     "1 m represents 200 m", "The scale cannot be determined"}
            vis = scale_drawing_svg()
            exp = "1:200 means multiply drawing measurements by 200 to get actual"
        
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


# Level 10: Circle Properties
def gen_level_10(n=50):
    """Mastery: Circle terminology and basic theorems"""
    qs = []
    used = set()
    
    for _ in range(n * 40):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['terminology', 'diameter_radius', 'angle_semicircle', 'tangent', 'chord', 'circumference', 'area', 'arc'])
        
        if qtype == 'terminology':
            terms = [
                ('radius', 'A line from the centre to the circumference'),
                ('diameter', 'A line through the centre, touching both sides of the circle'),
                ('chord', 'A line joining two points on the circumference (not through centre)'),
                ('tangent', 'A line that touches the circle at exactly one point'),
                ('arc', 'Part of the circumference of a circle'),
                ('sector', 'A "pizza slice" shape bounded by two radii and an arc'),
                ('segment', 'Region between a chord and an arc'),
                ('circumference', 'The perimeter (distance around) a circle'),
            ]
            name, defn = random.choice(terms)
            txt = f"What is the {name} of a circle?"
            ans = defn
            wrongs = {t[1] for t in terms if t[0] != name}
            vis = circle_svg(show_parts=[name] if name in ['radius', 'diameter', 'chord'] else None)
            exp = f"The {name} is: {defn}"
            
        elif qtype == 'diameter_radius':
            r = random.randint(2, 20)
            variant = random.choice(['r_to_d', 'd_to_r', 'r_to_c', 'd_to_c'])
            if variant == 'r_to_d':
                txt = f"A circle has radius {r} cm. What is the diameter?"
                ans = f"{r * 2} cm"
                wrongs = {f"{r} cm", f"{r * 3} cm", f"{r + 2} cm", f"{r * 2 + 1} cm"}
                exp = f"Diameter = 2 × radius = 2 × {r} = {r * 2} cm"
            elif variant == 'd_to_r':
                d = r * 2
                txt = f"A circle has diameter {d} cm. What is the radius?"
                ans = f"{r} cm"
                wrongs = {f"{d} cm", f"{r + 1} cm", f"{r - 1} cm" if r > 1 else f"{r + 2} cm", f"{d + r} cm"}
                exp = f"Radius = diameter ÷ 2 = {d} ÷ 2 = {r} cm"
            elif variant == 'r_to_c':
                txt = f"A circle has radius {r} cm. What is the circumference? (Use π)"
                ans = f"2π × {r} = {2*r}π cm"
                wrongs = {f"π × {r} = {r}π cm", f"π × {r*r} = {r*r}π cm²", f"2 × {r} = {2*r} cm", f"{r}² = {r*r} cm"}
                exp = f"Circumference = 2πr = 2π × {r} = {2*r}π cm"
            else:
                d = r * 2
                txt = f"A circle has diameter {d} cm. What is the circumference? (Use π)"
                ans = f"π × {d} = {d}π cm"
                wrongs = {f"2π × {d} = {2*d}π cm", f"π × {r} = {r}π cm", f"{d} cm", f"π × {d*d} cm²"}
                exp = f"Circumference = πd = π × {d} = {d}π cm"
            vis = circle_svg(show_parts=['radius', 'diameter'])
            
        elif qtype == 'angle_semicircle':
            txt = "The angle in a semicircle (angle at circumference, diameter as base) is always:"
            ans = "90°"
            wrongs = {"180°", "60°", "45°", "120°"}
            vis = circle_svg(show_parts=['diameter'])
            exp = "The angle in a semicircle is always 90° (Thales' theorem)"
            
        elif qtype == 'tangent':
            variant = random.choice(['angle', 'property', 'from_point'])
            if variant == 'angle':
                txt = "The angle between a tangent and the radius at the point of contact is:"
                ans = "90°"
                wrongs = {"180°", "60°", "45°", "0°"}
                exp = "A tangent is perpendicular to the radius at the point of contact"
            elif variant == 'property':
                txt = "A tangent to a circle:"
                ans = "Touches the circle at exactly one point"
                wrongs = {"Passes through the centre", "Cuts the circle at two points", "Is always horizontal", "Is the same as a chord"}
                exp = "A tangent touches (but doesn't cross) the circle at one point"
            else:
                txt = "Two tangents drawn from an external point to a circle:"
                ans = "Are equal in length"
                wrongs = {"Are parallel", "Are perpendicular", "Have different lengths", "Pass through the centre"}
                exp = "Tangents from an external point to a circle are equal in length"
            vis = circle_svg()
            
        elif qtype == 'chord':
            variant = random.choice(['bisector', 'equal', 'longest'])
            if variant == 'bisector':
                txt = "The perpendicular from the centre of a circle to a chord:"
                ans = "Bisects the chord"
                wrongs = {"Is parallel to the chord", "Equals the chord length", "Passes through the circumference only", "Has no special property"}
                exp = "A perpendicular from the centre bisects any chord"
            elif variant == 'equal':
                txt = "Equal chords in a circle are:"
                ans = "The same distance from the centre"
                wrongs = {"Different distances from the centre", "Always parallel", "Always perpendicular", "On the same side"}
                exp = "Equal chords are equidistant from the centre"
            else:
                txt = "The longest chord in any circle is:"
                ans = "The diameter"
                wrongs = {"The radius", "Any chord through the centre", "The tangent", "The arc"}
                exp = "The diameter is the longest chord (passes through centre)"
            vis = circle_svg(show_parts=['chord'])
            
        elif qtype == 'circumference':
            r = random.randint(3, 10)
            txt = f"Find the circumference of a circle with radius {r} cm. Give your answer in terms of π."
            ans = f"{2*r}π cm"
            wrongs = {f"{r}π cm", f"{r*r}π cm²", f"{2*r} cm", f"{r*r*2}π cm"}
            vis = circle_svg(show_parts=['radius'])
            exp = f"C = 2πr = 2 × π × {r} = {2*r}π cm"
            
        elif qtype == 'area':
            r = random.randint(2, 8)
            txt = f"Find the area of a circle with radius {r} cm. Give your answer in terms of π."
            ans = f"{r*r}π cm²"
            wrongs = {f"{2*r}π cm", f"{r}π cm²", f"{2*r*r}π cm²", f"{r*r} cm²"}
            vis = circle_svg(show_parts=['radius'])
            exp = f"A = πr² = π × {r}² = {r*r}π cm²"
            
        else:  # arc
            txt = "An arc is:"
            ans = "Part of the circumference of a circle"
            wrongs = {"Part of the area of a circle", "A straight line across the circle", "The whole circumference", "A line from centre to edge"}
            vis = circle_svg()
            exp = "An arc is a portion of the circle's circumference"
        
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


# Level 11: Advanced Constructions
def gen_level_11(n=50):
    """Mastery: Divide line segments, perpendiculars, more complex constructions"""
    qs = []
    used = set()
    
    for _ in range(n * 50):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['divide_line', 'perpendicular_point', 'angle_bisector', 'parallel', 'circumcircle', 
                              'incircle', 'centroid', 'altitude', 'orthocentre', 'locus', 'angle_construct',
                              'euler_line', 'nine_point', 'congruence_construct'])
        
        if qtype == 'divide_line':
            parts = random.choice([2, 3, 4, 5, 6, 7])
            txt = f"To divide a line segment into {parts} equal parts using construction:"
            ans = f"Draw a ray at an angle, mark {parts} equal lengths, connect last mark to endpoint, draw parallels"
            wrongs = {"Use a ruler to measure", f"Bisect the line {parts} times", 
                     "Draw a circle", "Use a protractor"}
            vis = construction_svg('perpendicular_bisector')
            exp = f"Use parallel lines to divide into {parts} equal parts without measuring"
            
        elif qtype == 'perpendicular_point':
            variant = random.choice(['on_line', 'off_line', 'method'])
            if variant == 'on_line':
                txt = "To construct a perpendicular to a line at a point ON the line:"
                ans = "Draw equal arcs on both sides of the point, then arcs from those points to find intersection above"
                wrongs = {"Use a set square", "Draw a circle centered on the point",
                         "It cannot be done exactly", "Draw any line through the point"}
            elif variant == 'off_line':
                txt = "To construct a perpendicular to a line through a point NOT on the line:"
                ans = "Draw arcs from the point to create two points on the line, then construct perpendicular bisector"
                wrongs = {"Draw a line at 90° by estimation", "Use the corner of a page",
                         "It cannot be done with compass and ruler", "Draw a circle centered on the point"}
            else:
                txt = "The compass-and-ruler construction for a perpendicular relies on:"
                ans = "Creating equidistant points and using the perpendicular bisector property"
                wrongs = {"Measuring 90° with a protractor", "Drawing a square first",
                         "Using a set square", "Trial and error"}
            vis = construction_svg('perpendicular_bisector')
            exp = "Arc method creates equidistant points to work from"
            
        elif qtype == 'angle_bisector':
            angle = random.choice([20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 140, 160])
            txt = f"To bisect an angle of {angle}° using compass and ruler, each resulting angle will be:"
            ans = f"{angle // 2}°"
            wrongs = {f"{angle}°", f"{angle // 2 + 5}°", f"{90 - angle // 2}°" if angle < 180 else f"{angle - 90}°", f"{180 - angle}°"}
            vis = construction_svg('60_angle')
            exp = f"Bisecting {angle}° gives two angles of {angle // 2}° each"
            
        elif qtype == 'parallel':
            method = random.choice(['corresponding', 'alternate', 'general'])
            if method == 'corresponding':
                txt = "To construct a parallel line using corresponding angles, you:"
                ans = "Copy an angle from the given line to the new point using the transversal"
                wrongs = {"Draw any line through the point", "Use only a ruler",
                         "It requires a protractor", "Draw a perpendicular first"}
            elif method == 'alternate':
                txt = "To construct a parallel line using alternate angles, you:"
                ans = "Create equal alternate angles on opposite sides of the transversal"
                wrongs = {"Measure with a protractor", "Draw a circle",
                         "It cannot be done", "Draw multiple perpendiculars"}
            else:
                txt = "To construct a line parallel to a given line through a point:"
                ans = "Use corresponding angles - copy an angle at the point equal to one on the given line"
                wrongs = {"Draw any line through the point", "Use a set square only",
                         "It cannot be done exactly", "Draw a perpendicular first, then another perpendicular"}
            vis = parallel_lines_svg()
            exp = "Equal corresponding or alternate angles guarantee parallel lines"
            
        elif qtype == 'circumcircle':
            aspect = random.choice(['passes', 'centre', 'construct'])
            if aspect == 'passes':
                txt = "The circumcircle of a triangle:"
                ans = "Passes through all three vertices"
                wrongs = {"Passes through the midpoints of the sides", "Only touches two vertices", "Passes through the centroid", "Has its centre at a vertex"}
            elif aspect == 'centre':
                txt = "The centre of the circumcircle of a triangle is found at:"
                ans = "The intersection of the perpendicular bisectors of the sides"
                wrongs = {"The intersection of the medians", "The intersection of the altitudes",
                         "The intersection of the angle bisectors", "The midpoint of the longest side"}
            else:
                txt = "To construct the circumcircle of a triangle:"
                ans = "Find where the perpendicular bisectors of two sides meet, then draw circle through a vertex"
                wrongs = {"Draw a circle touching all three sides", "Find the centroid first",
                         "Use trial and error", "It cannot be done exactly"}
            vis = triangle_svg()
            exp = "The circumcircle passes through all three vertices; its centre is where perpendicular bisectors meet"
            
        elif qtype == 'incircle':
            aspect = random.choice(['touches', 'centre', 'radius'])
            if aspect == 'touches':
                txt = "The incircle of a triangle:"
                ans = "Touches all three sides and has its centre at the intersection of angle bisectors"
                wrongs = {"Passes through all three vertices", "Has its centre at a vertex", 
                         "Touches only one side", "Has its centre at the midpoint of the longest side"}
            elif aspect == 'centre':
                txt = "The centre of the incircle (incentre) is found at:"
                ans = "The intersection of the angle bisectors"
                wrongs = {"The intersection of the perpendicular bisectors", "The intersection of the medians",
                         "The intersection of the altitudes", "The centroid"}
            else:
                txt = "The radius of the incircle is:"
                ans = "The perpendicular distance from the incentre to any side"
                wrongs = {"The distance to a vertex", "Half the shortest side",
                         "The same as the circumradius", "One third of the perimeter"}
            vis = triangle_svg()
            exp = "The incircle touches all three sides; its centre is where angle bisectors meet"
            
        elif qtype == 'centroid':
            aspect = random.choice(['definition', 'property', 'ratio'])
            if aspect == 'definition':
                txt = "The centroid of a triangle is found by:"
                ans = "Finding the intersection of the medians (lines from vertices to midpoints of opposite sides)"
                wrongs = {"Finding the intersection of the perpendicular bisectors", 
                         "Finding the intersection of the altitudes",
                         "Finding the intersection of the angle bisectors",
                         "Finding the midpoint of the longest side"}
            elif aspect == 'property':
                txt = "The centroid of a triangle:"
                ans = "Is the centre of mass (balance point) of the triangle"
                wrongs = {"Is equidistant from all vertices", "Is equidistant from all sides",
                         "Lies outside the triangle", "Is at a vertex"}
            else:
                txt = "Each median is divided by the centroid in the ratio:"
                ans = "2:1 from vertex to midpoint"
                wrongs = {"1:1 (equal parts)", "3:1 from vertex to midpoint",
                         "1:2 from vertex to midpoint", "Varies for each median"}
            vis = triangle_svg()
            exp = "The centroid is where the three medians meet, dividing each median 2:1"
            
        elif qtype == 'altitude':
            aspect = random.choice(['definition', 'orthocentre', 'acute_obtuse'])
            if aspect == 'definition':
                txt = "An altitude of a triangle is:"
                ans = "A perpendicular line from a vertex to the opposite side (or its extension)"
                wrongs = {"A line from vertex to midpoint of opposite side",
                         "The longest side of the triangle",
                         "A line bisecting an angle",
                         "Always inside the triangle"}
            elif aspect == 'orthocentre':
                txt = "The orthocentre is:"
                ans = "The point where all three altitudes meet"
                wrongs = {"The point where all three medians meet",
                         "The point where all three angle bisectors meet",
                         "The centre of the circumcircle",
                         "Always inside the triangle"}
            else:
                txt = "In an obtuse triangle, the orthocentre lies:"
                ans = "Outside the triangle"
                wrongs = {"Inside the triangle", "On a vertex", "At the centre", "On the longest side"}
            vis = triangle_svg()
            exp = "An altitude is perpendicular to a side, drawn from the opposite vertex"
            
        elif qtype == 'orthocentre':
            txt = "The orthocentre of a triangle is found at:"
            ans = "The intersection of the three altitudes"
            wrongs = {"The intersection of the three medians",
                     "The intersection of the angle bisectors",
                     "The intersection of the perpendicular bisectors",
                     "The centre of the inscribed circle"}
            vis = triangle_svg()
            exp = "The orthocentre is where all three altitudes meet"
            
        elif qtype == 'locus':
            loci = [
                ("all points equidistant from two fixed points", "the perpendicular bisector of the line joining them"),
                ("all points equidistant from two lines", "the angle bisectors of the lines"),
                ("all points a fixed distance from a point", "a circle centred on that point"),
                ("all points a fixed distance from a line", "two lines parallel to the given line"),
            ]
            condition, answer = random.choice(loci)
            txt = f"The locus of {condition} is:"
            ans = answer.capitalize()
            wrongs = {l[1].capitalize() for l in loci if l[1] != answer}
            vis = construction_svg('perpendicular_bisector')
            exp = f"The locus of {condition} is {answer}"
            
        else:  # angle_construct
            angles = [(30, "Bisect 60°"), (45, "Bisect 90°"), (15, "Bisect 30°"), 
                     (90, "Construct perpendicular"), (120, "Construct 60° and double it")]
            angle, method = random.choice(angles)
            txt = f"To construct an angle of exactly {angle}° using compass and ruler:"
            ans = method
            wrongs = {a[1] for a in angles if a[0] != angle}
            wrongs.add("Use a protractor")
            vis = construction_svg('60_angle')
            exp = f"{angle}° can be constructed by: {method}"
        
        if qtype == 'euler_line':
            txt = "The Euler line of a triangle passes through:"
            ans = "The circumcentre, centroid, and orthocentre"
            wrongs = {"The incentre and circumcentre only", "All four triangle centres",
                     "The three vertices", "The midpoints of the sides"}
            vis = triangle_svg()
            exp = "The Euler line connects circumcentre, centroid, and orthocentre (but NOT incentre)"
        
        elif qtype == 'nine_point':
            txt = "The nine-point circle of a triangle passes through:"
            ans = "The midpoints of the sides, feet of altitudes, and midpoints from vertices to orthocentre"
            wrongs = {"The three vertices only", "The incentre and circumcentre",
                     "Just the midpoints of the sides", "The centroid and orthocentre"}
            vis = triangle_svg()
            exp = "The nine-point circle passes through 9 significant points of any triangle"
        
        elif qtype == 'congruence_construct':
            conditions = [
                ("SSS", "three sides"),
                ("SAS", "two sides and the included angle"),
                ("ASA", "two angles and the included side"),
                ("AAS", "two angles and a non-included side"),
            ]
            name, desc = random.choice(conditions)
            txt = f"To construct a triangle congruent to another using {name}, you need:"
            ans = f"Measurements of {desc}"
            wrongs = {f"Measurements of {c[1]}" for c in conditions if c[0] != name}
            vis = triangle_svg()
            exp = f"{name} congruence requires {desc}"
        
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


# Level 12: Problem Solving & Proofs
def gen_level_12(n=50):
    """Mastery: Multi-step problems, justify answers"""
    qs = []
    used = set()
    
    for _ in range(n * 25):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['external_angle', 'similar_proof', 'congruent', 'multi_step', 'justify'])
        
        if qtype == 'external_angle':
            # SEC style: External angle theorem
            a1 = random.randint(30, 70)
            a2 = random.randint(30, 70)
            ext = a1 + a2
            txt = f"In a triangle, two interior angles are {a1}° and {a2}°. What is the exterior angle adjacent to the third angle?"
            ans = f"{ext}°"
            wrongs = {f"{180 - ext}°", f"{a1}°", f"{a2}°", f"{180 - a1 - a2}°"}
            vis = triangle_svg(angles=[a1, a2, '?'])
            exp = f"External angle = sum of non-adjacent interior angles = {a1}° + {a2}° = {ext}°"
            
        elif qtype == 'similar_proof':
            txt = "To prove two triangles are similar, you can show that:"
            ans = "Two pairs of corresponding angles are equal (AA)"
            wrongs = {"One pair of sides is equal", "They have equal perimeters",
                     "One angle is equal", "They have the same area"}
            vis = similar_triangles_svg()
            exp = "AA (Angle-Angle) is sufficient to prove similarity"
            
        elif qtype == 'congruent':
            conditions = [
                ('SSS', 'Three sides equal'),
                ('SAS', 'Two sides and the included angle equal'),
                ('ASA', 'Two angles and the included side equal'),
                ('RHS', 'Right angle, hypotenuse, and one side equal'),
            ]
            name, desc = random.choice(conditions)
            txt = f"The congruence condition {name} means:"
            ans = desc
            wrongs = {c[1] for c in conditions if c[0] != name}
            vis = triangle_svg()
            exp = f"{name}: {desc}"
            
        elif qtype == 'multi_step':
            # Multi-step angle problem
            a1 = random.randint(35, 55)
            # Isosceles with parallel line
            txt = f"Triangle ABC is isosceles with AB = AC. Angle BAC = {a1}°. Line DE is parallel to BC. Find angle ADE."
            base_angle = (180 - a1) // 2
            ans = f"{base_angle}°"
            wrongs = {f"{a1}°", f"{180 - base_angle}°", f"{base_angle + 10}°", f"{90}°"}
            vis = triangle_svg(angles=[a1, base_angle, base_angle])
            exp = f"Base angles = (180° - {a1}°) ÷ 2 = {base_angle}°. ADE = ABC (corresponding) = {base_angle}°"
            
        else:  # justify
            txt = "Why can't a triangle have two obtuse angles?"
            ans = "Two obtuse angles would sum to more than 180°, but angles in a triangle sum to exactly 180°"
            wrongs = {"Triangles must have at least one right angle", "Obtuse angles don't fit in triangles",
                     "It would make the triangle too large", "Triangles can have two obtuse angles"}
            vis = triangle_svg()
            exp = "Each obtuse angle > 90°, so two would give > 180°, which is impossible in a triangle"
        
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
        
        required = ['question_text', 'option_a', 'option_b', 'option_c', 'option_d', 
                   'correct_idx', 'explanation', 'level', 'topic', 'mode']
        for field in required:
            if field not in q or q[field] is None:
                errors.append(f"L{level}: Missing {field}")
        
        opts = [q.get('option_a'), q.get('option_b'), q.get('option_c'), q.get('option_d')]
        if len(set(opts)) != 4:
            errors.append(f"L{level}: Non-unique options: {opts}")
        
        if q.get('image_svg'):
            visual_counts[level] += 1
    
    return errors, level_counts, visual_counts


def print_summary(errors, level_counts, visual_counts):
    """Print validation summary"""
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    
    for level in range(1, 13):
        count = level_counts[level]
        vis_pct = (visual_counts[level] / count * 100) if count > 0 else 0
        status = "✓" if count >= QUESTIONS_PER_LEVEL else "✗"
        bar = "█" * (count // 2) + " " * (25 - count // 2)
        print(f"Level {level:2}: [{bar}] {count}/{QUESTIONS_PER_LEVEL} | Vis: {vis_pct:.0f}% | {status}")
    
    print("=" * 60)
    print(f"Total Errors: {len(errors)}")
    if errors[:10]:
        for e in errors[:10]:
            print(f"  - {e}")


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
        print("Database not found.")
        return False
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = ?", (TOPIC,))
    deleted = cursor.rowcount
    print(f"Deleted {deleted} existing {TOPIC} questions")
    conn.commit()
    
    inserted = 0
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
            print(f"Insert error: {e}")
    
    conn.commit()
    conn.close()
    print(f"Inserted {inserted} questions")
    return True


if __name__ == "__main__":
    print("=" * 60)
    print("AgentMath - Geometry Generator v1")
    print("=" * 60)
    
    qs = generate_all()
    errors, level_counts, visual_counts = validate(qs)
    print_summary(errors, level_counts, visual_counts)
    
    print("\n" + "=" * 60)
    response = input("Insert? (y/n): ").strip().lower()
    if response == 'y':
        insert_to_db(qs)
    else:
        print("Cancelled.")
