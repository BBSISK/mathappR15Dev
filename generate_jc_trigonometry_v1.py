#!/usr/bin/env python3
"""
AgentMath - Trigonometry Generator v1
Junior Cycle Mathematics - SEC Aligned

12 Levels:
1. Identifying Sides (Opposite, Adjacent, Hypotenuse) - Foundation
2. Understanding Trig Ratios (SOH CAH TOA) - Foundation
3. Calculator Skills (sin, cos, tan values) - Foundation
4. Finding Sides Using Trig Ratios - Ordinary
5. Finding Angles Using Inverse Trig - Ordinary
6. Mixed Problems (Sides and Angles) - Ordinary
7. Angles of Elevation and Depression - Higher
8. Multi-Step Problems - Higher
9. Pythagoras & Trigonometry Combined - Higher
10. Bearings and Navigation - Mastery
11. Area of Triangle (½absinC) - Mastery
12. Problem Solving & Applications - Mastery

SEC References:
- 2022-2025 OL/HL: Right-angled triangle problems
- SOH CAH TOA applications
- Angles of elevation/depression
- Real-world context problems
"""

import random
import math

TOPIC = "trigonometry"
MODE = "jc_exam"
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12

# Visual SVG generators
def right_triangle_svg(base=4, height=3, labels=None, angle_label=None, show_right_angle=True):
    """Generate right-angled triangle SVG with labels"""
    # Scale for display
    scale = 30
    margin = 40
    
    width = base * scale + margin * 2
    height_px = height * scale + margin * 2
    
    # Triangle points: right angle at bottom-left
    p1 = (margin, height_px - margin)  # Bottom-left (right angle)
    p2 = (margin + base * scale, height_px - margin)  # Bottom-right
    p3 = (margin, height_px - margin - height * scale)  # Top-left
    
    svg = f'''<svg viewBox="0 0 {width} {height_px}" xmlns="http://www.w3.org/2000/svg">
    <rect width="{width}" height="{height_px}" fill="#f0f9ff"/>
    '''
    
    # Draw triangle
    svg += f'''<polygon points="{p1[0]},{p1[1]} {p2[0]},{p2[1]} {p3[0]},{p3[1]}" 
               fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>'''
    
    # Right angle marker
    if show_right_angle:
        size = 12
        svg += f'''<path d="M {p1[0]+size} {p1[1]} L {p1[0]+size} {p1[1]-size} L {p1[0]} {p1[1]-size}" 
                   fill="none" stroke="#0284c7" stroke-width="1.5"/>'''
    
    # Angle arc at bottom-right (the angle we're usually working with)
    if angle_label:
        arc_r = 20
        svg += f'''<path d="M {p2[0]-arc_r} {p2[1]} A {arc_r} {arc_r} 0 0 0 {p2[0]-arc_r*0.7} {p2[1]-arc_r*0.7}" 
                   fill="none" stroke="#dc2626" stroke-width="2"/>'''
        svg += f'''<text x="{p2[0]-arc_r-15}" y="{p2[1]-10}" font-size="14" fill="#dc2626" font-weight="bold">{angle_label}</text>'''
    
    # Labels
    if labels:
        # Hypotenuse (slanted side)
        if 'hyp' in labels:
            mid_x = (p2[0] + p3[0]) / 2 + 10
            mid_y = (p2[1] + p3[1]) / 2
            svg += f'''<text x="{mid_x}" y="{mid_y}" font-size="13" fill="#7c3aed" font-weight="bold">{labels['hyp']}</text>'''
        
        # Opposite (vertical side)
        if 'opp' in labels:
            svg += f'''<text x="{p1[0]-25}" y="{(p1[1]+p3[1])/2}" font-size="13" fill="#059669" font-weight="bold">{labels['opp']}</text>'''
        
        # Adjacent (horizontal side)
        if 'adj' in labels:
            svg += f'''<text x="{(p1[0]+p2[0])/2}" y="{p1[1]+20}" font-size="13" fill="#0284c7" font-weight="bold">{labels['adj']}</text>'''
    
    svg += '</svg>'
    return svg


def elevation_depression_svg(scenario='elevation'):
    """Generate angle of elevation/depression diagram"""
    svg = '''<svg viewBox="0 0 250 180" xmlns="http://www.w3.org/2000/svg">
    <rect width="250" height="180" fill="#f0fdf4"/>
    '''
    
    if scenario == 'elevation':
        # Ground
        svg += '<line x1="20" y1="140" x2="230" y2="140" stroke="#65a30d" stroke-width="3"/>'
        # Person
        svg += '<circle cx="40" cy="125" r="8" fill="#f59e0b"/>'
        svg += '<line x1="40" y1="133" x2="40" y2="140" stroke="#f59e0b" stroke-width="2"/>'
        # Building/object
        svg += '<rect x="180" y="40" width="40" height="100" fill="#6b7280"/>'
        # Line of sight
        svg += '<line x1="40" y1="125" x2="200" y2="50" stroke="#dc2626" stroke-width="2" stroke-dasharray="5,3"/>'
        # Horizontal reference
        svg += '<line x1="40" y1="125" x2="150" y2="125" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="3,3"/>'
        # Angle arc
        svg += '<path d="M 70 125 A 30 30 0 0 0 60 110" fill="none" stroke="#dc2626" stroke-width="2"/>'
        svg += '<text x="75" y="118" font-size="11" fill="#dc2626" font-weight="bold">θ</text>'
        svg += '<text x="80" y="170" font-size="12" fill="#1e293b">Angle of Elevation</text>'
    else:
        # Cliff top
        svg += '<rect x="20" y="40" width="60" height="100" fill="#a3a3a3"/>'
        svg += '<line x1="20" y1="140" x2="230" y2="140" stroke="#65a30d" stroke-width="3"/>'
        # Person on top
        svg += '<circle cx="70" cy="30" r="6" fill="#f59e0b"/>'
        svg += '<line x1="70" y1="36" x2="70" y2="40" stroke="#f59e0b" stroke-width="2"/>'
        # Object below
        svg += '<circle cx="190" cy="135" r="8" fill="#3b82f6"/>'
        # Line of sight
        svg += '<line x1="70" y1="35" x2="190" y2="130" stroke="#dc2626" stroke-width="2" stroke-dasharray="5,3"/>'
        # Horizontal reference
        svg += '<line x1="70" y1="35" x2="180" y2="35" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="3,3"/>'
        # Angle arc
        svg += '<path d="M 100 35 A 30 30 0 0 1 95 55" fill="none" stroke="#dc2626" stroke-width="2"/>'
        svg += '<text x="105" y="50" font-size="11" fill="#dc2626" font-weight="bold">θ</text>'
        svg += '<text x="80" y="170" font-size="12" fill="#1e293b">Angle of Depression</text>'
    
    svg += '</svg>'
    return svg


def sohcahtoa_svg():
    """Visual showing SOH CAH TOA"""
    svg = '''<svg viewBox="0 0 220 120" xmlns="http://www.w3.org/2000/svg">
    <rect width="220" height="120" fill="#fef3c7"/>
    
    <text x="110" y="25" font-size="14" fill="#1e293b" text-anchor="middle" font-weight="bold">SOH CAH TOA</text>
    
    <text x="20" y="55" font-size="13" fill="#dc2626" font-weight="bold">Sin θ = </text>
    <text x="75" y="55" font-size="12" fill="#1e293b">Opp / Hyp</text>
    
    <text x="20" y="80" font-size="13" fill="#059669" font-weight="bold">Cos θ = </text>
    <text x="75" y="80" font-size="12" fill="#1e293b">Adj / Hyp</text>
    
    <text x="20" y="105" font-size="13" fill="#7c3aed" font-weight="bold">Tan θ = </text>
    <text x="75" y="105" font-size="12" fill="#1e293b">Opp / Adj</text>
    
    </svg>'''
    return svg


def bearing_svg(bearing, distance=None):
    """Generate compass/bearing diagram"""
    svg = '''<svg viewBox="0 0 180 180" xmlns="http://www.w3.org/2000/svg">
    <rect width="180" height="180" fill="#f0f9ff"/>
    '''
    
    cx, cy = 90, 90
    r = 60
    
    # Compass circle
    svg += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#94a3b8" stroke-width="2"/>'
    
    # Cardinal directions
    svg += f'<text x="{cx}" y="{cy-r-5}" font-size="14" fill="#1e293b" text-anchor="middle" font-weight="bold">N</text>'
    svg += f'<text x="{cx}" y="{cy+r+15}" font-size="14" fill="#1e293b" text-anchor="middle">S</text>'
    svg += f'<text x="{cx+r+10}" y="{cy+5}" font-size="14" fill="#1e293b" text-anchor="middle">E</text>'
    svg += f'<text x="{cx-r-10}" y="{cy+5}" font-size="14" fill="#1e293b" text-anchor="middle">W</text>'
    
    # North line
    svg += f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-r+10}" stroke="#64748b" stroke-width="1.5"/>'
    
    # Bearing line
    angle_rad = math.radians(bearing)
    end_x = cx + (r - 5) * math.sin(angle_rad)
    end_y = cy - (r - 5) * math.cos(angle_rad)
    svg += f'<line x1="{cx}" y1="{cy}" x2="{end_x}" y2="{end_y}" stroke="#dc2626" stroke-width="2.5"/>'
    svg += f'<circle cx="{end_x}" cy="{end_y}" r="4" fill="#dc2626"/>'
    
    # Bearing arc
    arc_r = 25
    arc_end_x = cx + arc_r * math.sin(angle_rad)
    arc_end_y = cy - arc_r * math.cos(angle_rad)
    large_arc = 1 if bearing > 180 else 0
    svg += f'<path d="M {cx} {cy-arc_r} A {arc_r} {arc_r} 0 {large_arc} 1 {arc_end_x} {arc_end_y}" fill="none" stroke="#3b82f6" stroke-width="2"/>'
    
    # Bearing label
    svg += f'<text x="{cx}" y="175" font-size="12" fill="#dc2626" text-anchor="middle" font-weight="bold">{bearing:03d}°</text>'
    
    svg += '</svg>'
    return svg


def make_options(correct, wrong_set):
    """Create 4 unique options with correct answer included"""
    wrong_list = [w for w in wrong_set if w != correct]
    random.shuffle(wrong_list)
    
    options = [correct] + wrong_list[:3]
    while len(options) < 4:
        if isinstance(correct, (int, float)):
            wrong = round(correct + random.choice([-2, -1, 1, 2]) * random.uniform(0.5, 1.5), 1)
            wrong = str(wrong)
        else:
            wrong = str(random.randint(1, 20))
        if wrong not in options and str(wrong) != str(correct):
            options.append(str(wrong))
    
    random.shuffle(options)
    correct_str = str(correct)
    correct_idx = options.index(correct_str) if correct_str in options else 0
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


# Level 1: Identifying Sides
def gen_level_1(n=50):
    """Foundation: Identify opposite, adjacent, hypotenuse relative to angle"""
    qs = []
    used = set()
    
    angles = ['A', 'B', 'θ', 'α', 'x', 'P', 'Q', 'R', 'M', 'N']
    
    for _ in range(n * 30):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['identify_hyp', 'identify_opp', 'identify_adj', 'which_side', 'label_side', 'true_false', 'property'])
        angle = random.choice(angles)
        
        # Generate side lengths for display
        a = random.randint(3, 12)
        b = random.randint(3, 12)
        c = round(math.sqrt(a**2 + b**2), 1)
        
        if qtype == 'identify_hyp':
            variant = random.randint(1, 5)
            if variant == 1:
                txt = f"In a right-angled triangle, which side is the hypotenuse?"
                ans = "The longest side, opposite the right angle"
                wrongs = {"The shortest side", "The side next to the angle", "The vertical side", "The base"}
            elif variant == 2:
                txt = f"The hypotenuse of a right triangle is always..."
                ans = "The longest side"
                wrongs = {"The shortest side", "The base", "The vertical side", "The opposite side"}
            elif variant == 3:
                txt = f"Which side is opposite the 90° angle?"
                ans = "The hypotenuse"
                wrongs = {"The opposite", "The adjacent", "The base", "The vertical side"}
            elif variant == 4:
                txt = f"In a right triangle with sides {a}, {b}, and {c}, which is the hypotenuse?"
                ans = str(c)
                wrongs = {str(a), str(b), str(a+b), str(round(c+1,1))}
            else:
                txt = f"The side that doesn't touch the right angle is called the..."
                ans = "Hypotenuse"
                wrongs = {"Opposite", "Adjacent", "Base", "Height"}
            labels = {'opp': str(a), 'adj': str(b), 'hyp': str(c)}
            exp = "The hypotenuse is always the longest side, opposite the 90° angle"
            
        elif qtype == 'identify_opp':
            variant = random.randint(1, 3)
            if variant == 1:
                txt = f"Relative to angle {angle}, which side is the OPPOSITE?"
                ans = "The side across from the angle"
                wrongs = {"The side next to the angle", "The hypotenuse", "The base", "The shortest side"}
            elif variant == 2:
                txt = f"The opposite side relative to angle {angle} is..."
                ans = "Across from the angle, not touching it"
                wrongs = {"Next to the angle", "The longest side", "The hypotenuse", "Touching the angle"}
            else:
                txt = f"Which side does NOT touch angle {angle}?"
                ans = "The opposite side"
                wrongs = {"The adjacent side", "The hypotenuse", "Both sides touch it", "The base"}
            labels = {'opp': 'OPP', 'adj': 'ADJ', 'hyp': 'HYP'}
            exp = f"The opposite side is directly across from angle {angle}, not touching it"
            
        elif qtype == 'identify_adj':
            variant = random.randint(1, 3)
            if variant == 1:
                txt = f"Relative to angle {angle}, which side is the ADJACENT?"
                ans = "The side next to the angle (not hypotenuse)"
                wrongs = {"The side across from the angle", "The hypotenuse", "The longest side", "The opposite side"}
            elif variant == 2:
                txt = f"The adjacent side relative to angle {angle}..."
                ans = "Touches the angle but isn't the hypotenuse"
                wrongs = {"Is across from the angle", "Is the longest side", "Doesn't touch the angle", "Is always horizontal"}
            else:
                txt = f"Which side touches angle {angle} but is NOT the hypotenuse?"
                ans = "The adjacent side"
                wrongs = {"The opposite side", "The base only", "The height only", "Both non-hypotenuse sides"}
            labels = {'opp': 'OPP', 'adj': 'ADJ', 'hyp': 'HYP'}
            exp = f"The adjacent side touches angle {angle} and is not the hypotenuse"
            
        elif qtype == 'which_side':
            side_type = random.choice(['opposite', 'adjacent', 'hypotenuse'])
            marker = random.choice(['?', 'x', 'y', 'p'])
            if side_type == 'opposite':
                labels = {'opp': marker, 'adj': str(b), 'hyp': str(c)}
                txt = f"The side marked '{marker}' is the _____ relative to angle {angle}."
                ans = "Opposite"
            elif side_type == 'adjacent':
                labels = {'opp': str(a), 'adj': marker, 'hyp': str(c)}
                txt = f"The side marked '{marker}' is the _____ relative to angle {angle}."
                ans = "Adjacent"
            else:
                labels = {'opp': str(a), 'adj': str(b), 'hyp': marker}
                txt = f"The side marked '{marker}' is the _____."
                ans = "Hypotenuse"
            wrongs = {"Opposite", "Adjacent", "Hypotenuse", "Base", "Height"}
            exp = f"The side is the {ans.lower()}" + (" - longest side opposite the right angle" if ans == "Hypotenuse" else f" relative to angle {angle}")
            
        elif qtype == 'label_side':
            position = random.choice(['vertical', 'horizontal', 'slanted'])
            if position == 'vertical':
                txt = f"In the triangle, the vertical side is the _____ relative to the bottom angle."
                ans = "Opposite"
            elif position == 'horizontal':
                txt = f"In the triangle, the horizontal side (base) is the _____ relative to the bottom angle."
                ans = "Adjacent"
            else:
                txt = f"In the triangle, the slanted side connecting the other two is the _____."
                ans = "Hypotenuse"
            wrongs = {"Opposite", "Adjacent", "Hypotenuse", "Base", "Height"}
            labels = {'opp': str(a), 'adj': str(b), 'hyp': str(c)}
            exp = f"The {position} side is the {ans.lower()}"
            
        elif qtype == 'true_false':
            statements = [
                ("The hypotenuse is always the longest side.", "True"),
                ("The opposite side touches the angle.", "False"),
                ("The adjacent side is next to the angle.", "True"),
                ("Any side can be the hypotenuse.", "False"),
                ("The hypotenuse is opposite the right angle.", "True"),
                ("The adjacent side is always horizontal.", "False"),
                ("Every right triangle has exactly one hypotenuse.", "True"),
                ("The opposite and adjacent depend on which angle you choose.", "True"),
            ]
            statement = random.choice(statements)
            txt = f"True or False: {statement[0]}"
            ans = statement[1]
            wrongs = {"True", "False", "Sometimes", "Depends on the triangle"}
            labels = {'opp': 'O', 'adj': 'A', 'hyp': 'H'}
            exp = f"{statement[0]} → {ans}"
            
        else:  # property
            props = [
                (f"How many sides does a right-angled triangle have?", "3"),
                (f"The right angle in a right triangle measures...", "90°"),
                (f"The sum of the other two angles in a right triangle is...", "90°"),
            ]
            prop = random.choice(props)
            txt = prop[0]
            ans = prop[1]
            wrongs = {"2", "3", "4", "90°", "180°", "45°", "60°"}
            labels = {'opp': str(a), 'adj': str(b), 'hyp': str(c)}
            exp = f"{txt} {ans}"
        
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
            'image_svg': right_triangle_svg(b, a, labels, angle)
        })
    
    return qs


# Level 2: Understanding Trig Ratios
def gen_level_2(n=50):
    """Foundation: Know SOH CAH TOA definitions"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['sin_def', 'cos_def', 'tan_def', 'which_ratio', 'formula'])
        
        if qtype == 'sin_def':
            txt = "What is the formula for sin θ?"
            ans = "Opposite / Hypotenuse"
            wrongs = {"Adjacent / Hypotenuse", "Opposite / Adjacent", "Hypotenuse / Opposite", "Adjacent / Opposite"}
            exp = "SOH: Sin = Opposite / Hypotenuse"
            
        elif qtype == 'cos_def':
            txt = "What is the formula for cos θ?"
            ans = "Adjacent / Hypotenuse"
            wrongs = {"Opposite / Hypotenuse", "Opposite / Adjacent", "Hypotenuse / Adjacent", "Hypotenuse / Opposite"}
            exp = "CAH: Cos = Adjacent / Hypotenuse"
            
        elif qtype == 'tan_def':
            txt = "What is the formula for tan θ?"
            ans = "Opposite / Adjacent"
            wrongs = {"Adjacent / Opposite", "Opposite / Hypotenuse", "Adjacent / Hypotenuse", "Hypotenuse / Opposite"}
            exp = "TOA: Tan = Opposite / Adjacent"
            
        elif qtype == 'which_ratio':
            opp = random.randint(3, 8)
            adj = random.randint(3, 8)
            hyp = round(math.sqrt(opp**2 + adj**2), 1)
            
            ratio = random.choice(['sin', 'cos', 'tan'])
            if ratio == 'sin':
                txt = f"If opposite = {opp} and hypotenuse = {hyp}, which ratio can you find directly?"
                ans = "sin θ"
            elif ratio == 'cos':
                txt = f"If adjacent = {adj} and hypotenuse = {hyp}, which ratio can you find directly?"
                ans = "cos θ"
            else:
                txt = f"If opposite = {opp} and adjacent = {adj}, which ratio can you find directly?"
                ans = "tan θ"
            wrongs = {"sin θ", "cos θ", "tan θ", "None of these"}
            exp = f"With these sides, you can calculate {ans} directly"
            
        else:  # formula
            scenario = random.choice(['find_opp', 'find_adj', 'find_hyp'])
            if scenario == 'find_opp':
                txt = "To find the opposite side when you know the angle and hypotenuse, use:"
                ans = "Opposite = Hypotenuse × sin θ"
                wrongs = {"Opposite = Hypotenuse × cos θ", "Opposite = Hypotenuse / sin θ", "Opposite = Adjacent × tan θ"}
            elif scenario == 'find_adj':
                txt = "To find the adjacent side when you know the angle and hypotenuse, use:"
                ans = "Adjacent = Hypotenuse × cos θ"
                wrongs = {"Adjacent = Hypotenuse × sin θ", "Adjacent = Hypotenuse / cos θ", "Adjacent = Opposite × tan θ"}
            else:
                txt = "To find the hypotenuse when you know the angle and opposite, use:"
                ans = "Hypotenuse = Opposite / sin θ"
                wrongs = {"Hypotenuse = Opposite × sin θ", "Hypotenuse = Opposite / cos θ", "Hypotenuse = Adjacent / tan θ"}
            exp = f"Rearranging SOH CAH TOA gives: {ans}"
        
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
            'image_svg': sohcahtoa_svg()
        })
    
    return qs


# Level 3: Calculator Skills
def gen_level_3(n=50):
    """Foundation: Use calculator for trig values"""
    qs = []
    used = set()
    
    all_angles = list(range(5, 86, 5))  # 5, 10, 15, ... 85
    
    for _ in range(n * 20):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['sin_value', 'cos_value', 'tan_value', 'inverse_sin', 'inverse_cos', 'inverse_tan'])
        angle = random.choice(all_angles)
        
        if qtype == 'sin_value':
            val = round(math.sin(math.radians(angle)), 2)
            txt = f"What is sin({angle}°)? (Round to 2 decimal places)"
            ans = str(val)
            wrongs = {str(round(val + 0.1, 2)), str(round(val - 0.1, 2)), 
                     str(round(math.cos(math.radians(angle)), 2)), str(round(abs(val - 0.15), 2))}
            exp = f"sin({angle}°) = {val}"
            
        elif qtype == 'cos_value':
            val = round(math.cos(math.radians(angle)), 2)
            txt = f"What is cos({angle}°)? (Round to 2 decimal places)"
            ans = str(val)
            wrongs = {str(round(val + 0.1, 2)), str(round(val - 0.1, 2)), 
                     str(round(math.sin(math.radians(angle)), 2)), str(round(abs(val - 0.15), 2))}
            exp = f"cos({angle}°) = {val}"
            
        elif qtype == 'tan_value':
            if angle >= 85:
                angle = 80  # Avoid very large tan values
            val = round(math.tan(math.radians(angle)), 2)
            txt = f"What is tan({angle}°)? (Round to 2 decimal places)"
            ans = str(val)
            wrongs = {str(round(val + 0.2, 2)), str(round(val - 0.2, 2)), 
                     str(round(val * 1.5, 2)), str(round(val * 0.6, 2))}
            exp = f"tan({angle}°) = {val}"
            
        elif qtype == 'inverse_sin':
            val = round(math.sin(math.radians(angle)), 2)
            txt = f"If sin(θ) = {val}, find θ (to nearest degree)"
            ans = f"{angle}°"
            wrongs = {f"{angle+5}°", f"{angle-5}°", f"{90-angle}°", f"{angle+10}°"}
            exp = f"θ = sin⁻¹({val}) = {angle}°"
            
        elif qtype == 'inverse_cos':
            val = round(math.cos(math.radians(angle)), 2)
            txt = f"If cos(θ) = {val}, find θ (to nearest degree)"
            ans = f"{angle}°"
            wrongs = {f"{angle+5}°", f"{angle-5}°", f"{90-angle}°", f"{angle+10}°"}
            exp = f"θ = cos⁻¹({val}) = {angle}°"
            
        else:  # inverse_tan
            if angle >= 85:
                angle = 75
            val = round(math.tan(math.radians(angle)), 2)
            txt = f"If tan(θ) = {val}, find θ (to nearest degree)"
            ans = f"{angle}°"
            wrongs = {f"{angle+5}°", f"{angle-5}°", f"{90-angle}°", f"{angle+10}°"}
            exp = f"θ = tan⁻¹({val}) = {angle}°"
        
        key = txt
        if key in used:
            continue
        used.add(key)
        
        opts, idx = make_options(ans, wrongs)
        
        # Simple triangle visual
        labels = {'opp': 'opp', 'adj': 'adj', 'hyp': 'hyp'}
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': right_triangle_svg(4, 3, labels, f"{angle}°")
        })
    
    return qs


# Level 4: Finding Sides Using Trig Ratios
def gen_level_4(n=50):
    """Ordinary: Calculate unknown sides"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
        
        angle = random.choice([30, 35, 40, 45, 50, 55, 60])
        known = random.randint(5, 15)
        
        scenario = random.choice(['find_opp_from_hyp', 'find_adj_from_hyp', 'find_opp_from_adj', 'find_adj_from_opp'])
        
        if scenario == 'find_opp_from_hyp':
            # opp = hyp × sin(θ)
            opp = round(known * math.sin(math.radians(angle)), 1)
            txt = f"In a right triangle, the hypotenuse is {known} cm and angle θ = {angle}°. Find the opposite side."
            ans = str(opp)
            labels = {'opp': '?', 'adj': '', 'hyp': str(known)}
            exp = f"opp = hyp × sin({angle}°) = {known} × {round(math.sin(math.radians(angle)), 3)} = {opp} cm"
            
        elif scenario == 'find_adj_from_hyp':
            # adj = hyp × cos(θ)
            adj = round(known * math.cos(math.radians(angle)), 1)
            txt = f"In a right triangle, the hypotenuse is {known} cm and angle θ = {angle}°. Find the adjacent side."
            ans = str(adj)
            labels = {'opp': '', 'adj': '?', 'hyp': str(known)}
            exp = f"adj = hyp × cos({angle}°) = {known} × {round(math.cos(math.radians(angle)), 3)} = {adj} cm"
            
        elif scenario == 'find_opp_from_adj':
            # opp = adj × tan(θ)
            opp = round(known * math.tan(math.radians(angle)), 1)
            txt = f"In a right triangle, the adjacent side is {known} cm and angle θ = {angle}°. Find the opposite side."
            ans = str(opp)
            labels = {'opp': '?', 'adj': str(known), 'hyp': ''}
            exp = f"opp = adj × tan({angle}°) = {known} × {round(math.tan(math.radians(angle)), 3)} = {opp} cm"
            
        else:  # find_adj_from_opp
            # adj = opp / tan(θ)
            adj = round(known / math.tan(math.radians(angle)), 1)
            txt = f"In a right triangle, the opposite side is {known} cm and angle θ = {angle}°. Find the adjacent side."
            ans = str(adj)
            labels = {'opp': str(known), 'adj': '?', 'hyp': ''}
            exp = f"adj = opp / tan({angle}°) = {known} / {round(math.tan(math.radians(angle)), 3)} = {adj} cm"
        
        key = txt
        if key in used:
            continue
        used.add(key)
        
        ans_val = float(ans)
        wrongs = {str(round(ans_val + 1, 1)), str(round(ans_val - 1, 1)), 
                 str(round(ans_val * 1.2, 1)), str(round(ans_val * 0.8, 1))}
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': right_triangle_svg(4, 3, labels, f"{angle}°")
        })
    
    return qs


# Level 5: Finding Angles Using Inverse Trig
def gen_level_5(n=50):
    """Ordinary: Calculate unknown angles using sin⁻¹, cos⁻¹, tan⁻¹"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
        
        # Generate sides that give nice angles
        target_angle = random.choice([30, 35, 40, 45, 50, 55, 60])
        hyp = random.randint(8, 15)
        opp = round(hyp * math.sin(math.radians(target_angle)), 1)
        adj = round(hyp * math.cos(math.radians(target_angle)), 1)
        
        scenario = random.choice(['sin_inverse', 'cos_inverse', 'tan_inverse'])
        
        if scenario == 'sin_inverse':
            ratio = round(opp / hyp, 3)
            angle = round(math.degrees(math.asin(ratio)))
            txt = f"In a right triangle, opposite = {opp} and hypotenuse = {hyp}. Find angle θ."
            labels = {'opp': str(opp), 'adj': '', 'hyp': str(hyp)}
            exp = f"sin θ = {opp}/{hyp} = {ratio}. θ = sin⁻¹({ratio}) = {angle}°"
            
        elif scenario == 'cos_inverse':
            ratio = round(adj / hyp, 3)
            angle = round(math.degrees(math.acos(ratio)))
            txt = f"In a right triangle, adjacent = {adj} and hypotenuse = {hyp}. Find angle θ."
            labels = {'opp': '', 'adj': str(adj), 'hyp': str(hyp)}
            exp = f"cos θ = {adj}/{hyp} = {ratio}. θ = cos⁻¹({ratio}) = {angle}°"
            
        else:  # tan_inverse
            ratio = round(opp / adj, 3)
            angle = round(math.degrees(math.atan(ratio)))
            txt = f"In a right triangle, opposite = {opp} and adjacent = {adj}. Find angle θ."
            labels = {'opp': str(opp), 'adj': str(adj), 'hyp': ''}
            exp = f"tan θ = {opp}/{adj} = {ratio}. θ = tan⁻¹({ratio}) = {angle}°"
        
        key = txt
        if key in used:
            continue
        used.add(key)
        
        ans = f"{angle}°"
        wrongs = {f"{angle+5}°", f"{angle-5}°", f"{90-angle}°", f"{angle+10}°"}
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': right_triangle_svg(4, 3, labels, 'θ')
        })
    
    return qs


# Level 6: Mixed Problems
def gen_level_6(n=50):
    """Ordinary: Mixed sides and angles problems"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['two_step_side', 'find_both', 'choose_ratio'])
        
        if qtype == 'two_step_side':
            angle = random.choice([30, 40, 45, 50, 60])
            hyp = random.randint(10, 20)
            opp = round(hyp * math.sin(math.radians(angle)), 1)
            adj = round(hyp * math.cos(math.radians(angle)), 1)
            
            txt = f"A right triangle has hypotenuse {hyp} cm and angle {angle}°. Find both the opposite and adjacent sides."
            ans = f"Opp = {opp}, Adj = {adj}"
            wrongs = {f"Opp = {adj}, Adj = {opp}", f"Opp = {opp+1}, Adj = {adj+1}", 
                     f"Opp = {round(opp*1.1,1)}, Adj = {round(adj*0.9,1)}"}
            labels = {'opp': '?', 'adj': '?', 'hyp': str(hyp)}
            exp = f"opp = {hyp} × sin({angle}°) = {opp}. adj = {hyp} × cos({angle}°) = {adj}"
            
        elif qtype == 'find_both':
            a = random.randint(3, 6)
            b = random.randint(4, 8)
            c = round(math.sqrt(a**2 + b**2), 1)
            angle = round(math.degrees(math.atan(a/b)))
            
            txt = f"A right triangle has opposite = {a} and adjacent = {b}. Find the angle θ and hypotenuse."
            ans = f"θ = {angle}°, hyp = {c}"
            wrongs = {f"θ = {90-angle}°, hyp = {c}", f"θ = {angle}°, hyp = {a+b}", 
                     f"θ = {angle+5}°, hyp = {c+1}"}
            labels = {'opp': str(a), 'adj': str(b), 'hyp': '?'}
            exp = f"tan θ = {a}/{b}, so θ = {angle}°. Hyp = √({a}² + {b}²) = {c}"
            
        else:  # choose_ratio
            opp = random.randint(3, 8)
            adj = random.randint(4, 10)
            hyp = round(math.sqrt(opp**2 + adj**2), 1)
            
            target = random.choice(['angle', 'missing_side'])
            if target == 'angle':
                txt = f"You know opposite = {opp} and adjacent = {adj}. Which ratio should you use to find angle θ?"
                ans = "tan θ = opp/adj"
                wrongs = {"sin θ = opp/hyp", "cos θ = adj/hyp", "tan θ = adj/opp"}
            else:
                txt = f"You know angle θ = 40° and hypotenuse = {hyp}. To find the opposite, which formula?"
                ans = "opp = hyp × sin θ"
                wrongs = {"opp = hyp × cos θ", "opp = hyp / sin θ", "opp = hyp × tan θ"}
            labels = {'opp': str(opp), 'adj': str(adj), 'hyp': str(hyp)}
            exp = f"Choose the ratio that uses the sides you know: {ans}"
        
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
            'image_svg': right_triangle_svg(4, 3, labels, 'θ')
        })
    
    return qs


# Level 7: Angles of Elevation and Depression
def gen_level_7(n=50):
    """Higher: Real-world elevation and depression problems"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
        
        scenario = random.choice(['elevation', 'depression', 'elevation', 'depression'])
        angle = random.choice([25, 30, 35, 40, 45, 50, 55, 60])
        distance = random.randint(20, 100)
        
        if scenario == 'elevation':
            contexts = [
                (f"A person stands {distance}m from a building. The angle of elevation to the top is {angle}°. Find the height of the building.", 
                 distance, angle, 'height'),
                (f"From a point {distance}m from the base of a tower, the angle of elevation to the top is {angle}°. Find the tower's height.",
                 distance, angle, 'height'),
                (f"A ladder leans against a wall at an angle of {angle}° to the ground. If the base is {distance}m from the wall, how high up the wall does it reach?",
                 distance, angle, 'height')
            ]
            txt, d, a, find = random.choice(contexts)
            height = round(d * math.tan(math.radians(a)), 1)
            ans = f"{height} m"
            labels = {'opp': '?', 'adj': str(d), 'hyp': ''}
            exp = f"height = {d} × tan({a}°) = {d} × {round(math.tan(math.radians(a)), 3)} = {height} m"
            vis = elevation_depression_svg('elevation')
            
        else:  # depression
            height = random.randint(20, 80)
            contexts = [
                (f"From the top of a {height}m cliff, the angle of depression to a boat is {angle}°. How far is the boat from the base of the cliff?",
                 height, angle, 'distance'),
                (f"A lighthouse is {height}m tall. The angle of depression to a ship is {angle}°. Find the distance from the lighthouse to the ship.",
                 height, angle, 'distance')
            ]
            txt, h, a, find = random.choice(contexts)
            dist = round(h / math.tan(math.radians(a)), 1)
            ans = f"{dist} m"
            labels = {'opp': str(h), 'adj': '?', 'hyp': ''}
            exp = f"distance = {h} / tan({a}°) = {h} / {round(math.tan(math.radians(a)), 3)} = {dist} m"
            vis = elevation_depression_svg('depression')
        
        key = txt
        if key in used:
            continue
        used.add(key)
        
        ans_val = float(ans.split()[0])
        wrongs = {f"{round(ans_val + 5, 1)} m", f"{round(ans_val - 5, 1)} m", 
                 f"{round(ans_val * 1.2, 1)} m", f"{round(ans_val * 0.8, 1)} m"}
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': vis
        })
    
    return qs


# Level 8: Multi-Step Problems
def gen_level_8(n=50):
    """Higher: Problems requiring multiple calculations"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['find_third_side', 'two_triangles', 'perimeter'])
        
        if qtype == 'find_third_side':
            angle = random.choice([30, 40, 45, 50, 60])
            hyp = random.randint(10, 20)
            opp = round(hyp * math.sin(math.radians(angle)), 1)
            adj = round(hyp * math.cos(math.radians(angle)), 1)
            
            txt = f"A right triangle has hypotenuse {hyp} cm and one angle of {angle}°. Find the perimeter."
            perimeter = round(hyp + opp + adj, 1)
            ans = f"{perimeter} cm"
            labels = {'opp': '?', 'adj': '?', 'hyp': str(hyp)}
            exp = f"opp = {hyp}×sin({angle}°) = {opp}. adj = {hyp}×cos({angle}°) = {adj}. P = {hyp}+{opp}+{adj} = {perimeter}"
            
        elif qtype == 'two_triangles':
            angle1 = 30
            angle2 = 60
            base = random.randint(10, 20)
            h = round(base * math.tan(math.radians(angle1)), 1)
            
            txt = f"A triangular plot has a base of {base}m. One corner makes a {angle1}° angle with the horizontal. Find the height."
            ans = f"{h} m"
            labels = {'opp': '?', 'adj': str(base), 'hyp': ''}
            exp = f"height = {base} × tan({angle1}°) = {h} m"
            
        else:  # perimeter
            a = random.randint(5, 10)
            b = random.randint(6, 12)
            c = round(math.sqrt(a**2 + b**2), 1)
            
            txt = f"A right triangle has legs of {a} cm and {b} cm. Find its perimeter."
            perimeter = round(a + b + c, 1)
            ans = f"{perimeter} cm"
            labels = {'opp': str(a), 'adj': str(b), 'hyp': '?'}
            exp = f"hyp = √({a}² + {b}²) = √{a**2 + b**2} = {c}. P = {a}+{b}+{c} = {perimeter}"
        
        key = txt
        if key in used:
            continue
        used.add(key)
        
        ans_val = float(ans.split()[0])
        wrongs = {f"{round(ans_val + 2, 1)} cm", f"{round(ans_val - 2, 1)} cm", 
                 f"{round(ans_val + 5, 1)} cm", f"{round(ans_val - 5, 1)} cm"}
        if 'm' in ans:
            wrongs = {w.replace('cm', 'm') for w in wrongs}
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': right_triangle_svg(4, 3, labels, 'θ')
        })
    
    return qs


# Level 9: Pythagoras & Trigonometry Combined
def gen_level_9(n=50):
    """Higher: Using both Pythagoras and trig together"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['find_angle_pythag', 'verify_right', 'combined'])
        
        if qtype == 'find_angle_pythag':
            # Give two sides, find hyp with Pythagoras, then angle with trig
            a = random.randint(3, 8)
            b = random.randint(4, 10)
            c = round(math.sqrt(a**2 + b**2), 1)
            angle = round(math.degrees(math.atan(a/b)))
            
            txt = f"A right triangle has legs of {a} cm and {b} cm. Find angle θ (opposite the {a} cm side)."
            ans = f"{angle}°"
            labels = {'opp': str(a), 'adj': str(b), 'hyp': ''}
            exp = f"tan θ = {a}/{b} = {round(a/b, 3)}. θ = tan⁻¹({round(a/b, 3)}) = {angle}°"
            
        elif qtype == 'verify_right':
            # Check if given sides form right triangle
            a, b, c = random.choice([(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17)])
            multiplier = random.choice([1, 2])
            a, b, c = a * multiplier, b * multiplier, c * multiplier
            
            txt = f"Do sides {a}, {b}, {c} form a right-angled triangle?"
            angle = 45  # Default for SVG
            if a**2 + b**2 == c**2:
                ans = "Yes"
                exp = f"{a}² + {b}² = {a**2} + {b**2} = {a**2 + b**2} = {c}² ✓"
            else:
                ans = "No"
                exp = f"{a}² + {b}² = {a**2 + b**2} ≠ {c}² = {c**2}"
            wrongs = {"Yes", "No", "Cannot determine", "Need more information"}
            labels = {'opp': str(a), 'adj': str(b), 'hyp': str(c)}
            
        else:  # combined
            angle = random.choice([30, 45, 60])
            side = random.randint(5, 12)
            
            if angle == 30:
                hyp = side * 2
                other = round(side * math.sqrt(3), 1)
            elif angle == 45:
                hyp = round(side * math.sqrt(2), 1)
                other = side
            else:  # 60
                hyp = round(side * 2 / math.sqrt(3), 1)
                other = round(side / math.sqrt(3), 1)
            
            txt = f"In a right triangle with angle {angle}°, the side opposite is {side} cm. Find the hypotenuse."
            hyp_calc = round(side / math.sin(math.radians(angle)), 1)
            ans = f"{hyp_calc} cm"
            labels = {'opp': str(side), 'adj': '', 'hyp': '?'}
            exp = f"sin({angle}°) = {side}/hyp. hyp = {side}/sin({angle}°) = {hyp_calc} cm"
        
        key = txt
        if key in used:
            continue
        used.add(key)
        
        if '°' in str(ans):
            ans_val = int(ans.replace('°', ''))
            wrongs = {f"{ans_val+5}°", f"{ans_val-5}°", f"{90-ans_val}°", f"{ans_val+10}°"}
        elif 'cm' in str(ans):
            ans_val = float(ans.split()[0])
            wrongs = {f"{round(ans_val+1, 1)} cm", f"{round(ans_val-1, 1)} cm", 
                     f"{round(ans_val*1.2, 1)} cm", f"{round(ans_val*0.8, 1)} cm"}
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': right_triangle_svg(4, 3, labels, f"{angle}°" if 'angle' in txt else 'θ')
        })
    
    return qs


# Level 10: Bearings and Navigation
def gen_level_10(n=50):
    """Mastery: Three-figure bearings and navigation problems"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['identify_bearing', 'back_bearing', 'distance_bearing', 'direction'])
        
        if qtype == 'identify_bearing':
            bearing = random.choice([30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330])
            txt = f"What direction is a bearing of {bearing:03d}°?"
            
            if bearing == 0 or bearing == 360:
                ans = "North"
            elif 0 < bearing < 90:
                ans = "North-East"
            elif bearing == 90:
                ans = "East"
            elif 90 < bearing < 180:
                ans = "South-East"
            elif bearing == 180:
                ans = "South"
            elif 180 < bearing < 270:
                ans = "South-West"
            elif bearing == 270:
                ans = "West"
            else:
                ans = "North-West"
            
            wrongs = {"North", "North-East", "East", "South-East", "South", "South-West", "West", "North-West"}
            exp = f"Bearing {bearing:03d}° is measured clockwise from North → {ans}"
            vis = bearing_svg(bearing)
            
        elif qtype == 'back_bearing':
            bearing = random.choice([30, 45, 60, 90, 120, 150])
            back = bearing + 180
            txt = f"A ship sails on a bearing of {bearing:03d}°. What is the back bearing (return journey)?"
            ans = f"{back:03d}°"
            wrongs = {f"{(bearing + 90) % 360:03d}°", f"{(360 - bearing):03d}°", 
                     f"{bearing:03d}°", f"{(bearing + 270) % 360:03d}°"}
            exp = f"Back bearing = {bearing} + 180 = {back}°"
            vis = bearing_svg(bearing)
            
        elif qtype == 'distance_bearing':
            bearing = random.choice([30, 45, 60])
            distance = random.randint(10, 50)
            
            # Calculate N-S and E-W components
            north = round(distance * math.cos(math.radians(bearing)), 1)
            east = round(distance * math.sin(math.radians(bearing)), 1)
            
            component = random.choice(['north', 'east'])
            if component == 'north':
                txt = f"A plane flies {distance} km on bearing {bearing:03d}°. How far north has it traveled?"
                ans = f"{north} km"
                exp = f"North = {distance} × cos({bearing}°) = {north} km"
            else:
                txt = f"A plane flies {distance} km on bearing {bearing:03d}°. How far east has it traveled?"
                ans = f"{east} km"
                exp = f"East = {distance} × sin({bearing}°) = {east} km"
            
            wrongs = {f"{round(float(ans.split()[0]) + 3, 1)} km", f"{round(float(ans.split()[0]) - 3, 1)} km",
                     f"{distance} km", f"{round(float(ans.split()[0]) * 0.8, 1)} km"}
            vis = bearing_svg(bearing)
            
        else:  # direction
            directions = [
                ("North", 0), ("North-East", 45), ("East", 90), ("South-East", 135),
                ("South", 180), ("South-West", 225), ("West", 270), ("North-West", 315)
            ]
            direction, bearing = random.choice(directions)
            txt = f"What is the three-figure bearing for {direction}?"
            ans = f"{bearing:03d}°"
            wrongs = {f"{(bearing + 90) % 360:03d}°", f"{(bearing + 180) % 360:03d}°", 
                     f"{(bearing + 45) % 360:03d}°", f"{(360 - bearing) % 360:03d}°"}
            exp = f"{direction} = {bearing:03d}° (measured clockwise from North)"
            vis = bearing_svg(bearing)
        
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


# Level 11: Area of Triangle (½absinC)
def gen_level_11(n=50):
    """Mastery: Calculate area using ½absinC"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['basic_area', 'find_side', 'find_angle', 'compare'])
        
        if qtype == 'basic_area':
            a = random.randint(5, 12)
            b = random.randint(6, 14)
            C = random.choice([30, 45, 60, 90, 120])
            
            area = round(0.5 * a * b * math.sin(math.radians(C)), 1)
            txt = f"Find the area of a triangle with sides {a} cm and {b} cm, and included angle {C}°."
            ans = f"{area} cm²"
            labels = {'opp': str(a), 'adj': str(b), 'hyp': ''}
            exp = f"Area = ½ × {a} × {b} × sin({C}°) = ½ × {a} × {b} × {round(math.sin(math.radians(C)), 3)} = {area} cm²"
            
        elif qtype == 'find_side':
            area = random.randint(20, 50)
            b = random.randint(5, 10)
            C = random.choice([30, 45, 60, 90])
            
            # Area = ½ab sinC → a = 2×Area / (b × sinC)
            a = round(2 * area / (b * math.sin(math.radians(C))), 1)
            txt = f"A triangle has area {area} cm², one side {b} cm, and included angle {C}°. Find the other side."
            ans = f"{a} cm"
            labels = {'opp': '?', 'adj': str(b), 'hyp': ''}
            exp = f"a = 2 × {area} / ({b} × sin({C}°)) = {2*area} / {round(b * math.sin(math.radians(C)), 2)} = {a} cm"
            
        elif qtype == 'find_angle':
            a = random.randint(6, 10)
            b = random.randint(7, 12)
            area = random.randint(15, 35)
            
            # sinC = 2×Area / (a×b)
            sinC = min(1, 2 * area / (a * b))  # Cap at 1
            C = round(math.degrees(math.asin(sinC)))
            
            txt = f"A triangle has sides {a} cm and {b} cm with area {area} cm². Find the included angle."
            ans = f"{C}°"
            labels = {'opp': str(a), 'adj': str(b), 'hyp': ''}
            exp = f"sin C = 2 × {area} / ({a} × {b}) = {round(sinC, 3)}. C = sin⁻¹({round(sinC, 3)}) = {C}°"
            
        else:  # compare
            a = random.randint(5, 8)
            b = random.randint(6, 10)
            C1, C2 = 30, 60
            
            area1 = round(0.5 * a * b * math.sin(math.radians(C1)), 1)
            area2 = round(0.5 * a * b * math.sin(math.radians(C2)), 1)
            
            txt = f"Two triangles have sides {a} cm and {b} cm. One has angle {C1}°, the other {C2}°. Which has larger area?"
            ans = f"The {C2}° triangle"
            wrongs = {f"The {C1}° triangle", "Same area", "Cannot determine", "Need more info"}
            labels = {'opp': str(a), 'adj': str(b), 'hyp': ''}
            exp = f"Area₁ = {area1} cm², Area₂ = {area2} cm². {C2}° gives larger area."
            
            opts, idx = make_options(ans, wrongs)
            qs.append({
                'question_text': txt,
                'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
                'correct_idx': idx,
                'explanation': exp,
                'image_svg': right_triangle_svg(4, 3, labels, 'C')
            })
            continue
        
        key = txt
        if key in used:
            continue
        used.add(key)
        
        if '°' in str(ans):
            val = int(ans.replace('°', ''))
            wrongs = {f"{val+10}°", f"{val-10}°", f"{90-val}°", f"{180-val}°"}
        elif 'cm²' in str(ans):
            val = float(ans.split()[0])
            wrongs = {f"{round(val+5, 1)} cm²", f"{round(val-5, 1)} cm²", 
                     f"{round(val*1.3, 1)} cm²", f"{round(val*0.7, 1)} cm²"}
        elif 'cm' in str(ans):
            val = float(ans.split()[0])
            wrongs = {f"{round(val+2, 1)} cm", f"{round(val-2, 1)} cm", 
                     f"{round(val*1.2, 1)} cm", f"{round(val*0.8, 1)} cm"}
        
        opts, idx = make_options(ans, wrongs)
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': right_triangle_svg(4, 3, labels, 'C')
        })
    
    return qs


# Level 12: Problem Solving & Applications
def gen_level_12(n=50):
    """Mastery: Complex real-world applications"""
    qs = []
    used = set()
    
    for _ in range(n * 10):
        if len(qs) >= n:
            break
        
        qtype = random.choice(['shadow', 'ramp', 'roof', 'surveying', 'flight'])
        
        if qtype == 'shadow':
            height = random.randint(5, 15)
            angle = random.choice([30, 40, 45, 50, 60])
            shadow = round(height / math.tan(math.radians(angle)), 1)
            
            txt = f"A {height}m tall tree casts a shadow. The angle of elevation of the sun is {angle}°. How long is the shadow?"
            ans = f"{shadow} m"
            exp = f"tan({angle}°) = {height}/shadow. Shadow = {height}/tan({angle}°) = {shadow} m"
            
        elif qtype == 'ramp':
            length = random.randint(3, 8)
            angle = random.choice([10, 15, 20, 25, 30])
            rise = round(length * math.sin(math.radians(angle)), 2)
            
            txt = f"A wheelchair ramp is {length}m long and makes an angle of {angle}° with the ground. What is the vertical rise?"
            ans = f"{rise} m"
            exp = f"rise = {length} × sin({angle}°) = {rise} m"
            
        elif qtype == 'roof':
            base = random.randint(6, 12)
            angle = random.choice([25, 30, 35, 40, 45])
            height = round((base/2) * math.tan(math.radians(angle)), 1)
            
            txt = f"A roof spans {base}m. If the roof makes an angle of {angle}° with the horizontal, what is the height of the peak?"
            ans = f"{height} m"
            exp = f"Half base = {base/2}m. Height = {base/2} × tan({angle}°) = {height} m"
            
        elif qtype == 'surveying':
            d1 = random.randint(40, 80)
            angle1 = random.choice([30, 35, 40])
            angle2 = random.choice([50, 55, 60])
            
            # Simple case: moving closer
            h = round(d1 * math.tan(math.radians(angle1)), 1)
            
            txt = f"From {d1}m away, the angle of elevation to a cliff top is {angle1}°. Find the cliff height."
            ans = f"{h} m"
            exp = f"h = {d1} × tan({angle1}°) = {h} m"
            
        else:  # flight
            altitude = random.randint(500, 2000)
            angle = random.choice([20, 25, 30, 35])
            ground_dist = round(altitude / math.tan(math.radians(angle)), 0)
            
            txt = f"A plane at {altitude}m altitude begins descent at {angle}° to horizontal. How far will it travel horizontally to land?"
            ans = f"{int(ground_dist)} m"
            exp = f"tan({angle}°) = {altitude}/distance. Distance = {altitude}/tan({angle}°) = {int(ground_dist)} m"
        
        key = txt
        if key in used:
            continue
        used.add(key)
        
        ans_val = float(ans.split()[0])
        wrongs = {f"{round(ans_val * 1.2, 1)} m", f"{round(ans_val * 0.8, 1)} m", 
                 f"{round(ans_val + 5, 1)} m", f"{round(ans_val - 5, 1)} m"}
        
        opts, idx = make_options(ans, wrongs)
        
        labels = {'opp': 'h', 'adj': 'd', 'hyp': ''}
        qs.append({
            'question_text': txt,
            'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3],
            'correct_idx': idx,
            'explanation': exp,
            'image_svg': elevation_depression_svg('elevation')
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
    print("AgentMath - Trigonometry Generator v1")
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
