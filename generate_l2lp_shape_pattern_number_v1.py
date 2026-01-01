"""
AgentMath L2LP Question Generator
Topic: Shape, Pattern & Number (l2_shape_pattern_number)
NCCA Module: Understanding shapes, patterns and number properties

Generates 600 questions (50 per level × 12 levels) for the L2LP strand.
High visual percentage with SVG graphics for accessibility.

Author: AgentMath Generator
Version: 1.0
Date: December 2025
"""

import sqlite3
import random
import math

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'l2_shape_pattern_number'
MODE = 'adaptive'
DIFFICULTY = 'adaptive'
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12
DATABASE_PATH = 'instance/mathquiz.db'

def get_visual_percentage(level):
    if level <= 3:
        return 85
    elif level <= 6:
        return 75
    elif level <= 9:
        return 65
    else:
        return 55

# ============================================================
# COLOUR PALETTE
# ============================================================

COLOURS = {
    'orange': '#f97316',
    'red': '#dc2626',
    'blue': '#3b82f6',
    'green': '#22c55e',
    'yellow': '#eab308',
    'purple': '#8b5cf6',
    'grey': '#6b7280',
    'dark': '#1f2937',
    'white': '#ffffff',
    'light_grey': '#f3f4f6',
    'pink': '#ec4899'
}

# ============================================================
# SVG GENERATION FUNCTIONS
# ============================================================

def generate_shape_svg(shape_type, colour=None, size=80):
    """Generate SVG of a 2D shape"""
    if colour is None:
        colour = random.choice([COLOURS['blue'], COLOURS['green'], COLOURS['orange'], COLOURS['purple']])
    
    cx, cy = 100, 100
    
    if shape_type == 'circle':
        shape = f'<circle cx="{cx}" cy="{cy}" r="{size//2}" fill="{colour}"/>'
        name = "Circle"
    elif shape_type == 'square':
        x, y = cx - size//2, cy - size//2
        shape = f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="{colour}"/>'
        name = "Square"
    elif shape_type == 'rectangle':
        w, h = size, size // 2
        shape = f'<rect x="{cx - w//2}" y="{cy - h//2}" width="{w}" height="{h}" fill="{colour}"/>'
        name = "Rectangle"
    elif shape_type == 'triangle':
        points = f"{cx},{cy - size//2} {cx - size//2},{cy + size//2} {cx + size//2},{cy + size//2}"
        shape = f'<polygon points="{points}" fill="{colour}"/>'
        name = "Triangle"
    elif shape_type == 'pentagon':
        points = []
        for i in range(5):
            angle = math.radians(i * 72 - 90)
            px = cx + (size//2) * math.cos(angle)
            py = cy + (size//2) * math.sin(angle)
            points.append(f"{px:.1f},{py:.1f}")
        shape = f'<polygon points="{" ".join(points)}" fill="{colour}"/>'
        name = "Pentagon"
    elif shape_type == 'hexagon':
        points = []
        for i in range(6):
            angle = math.radians(i * 60 - 90)
            px = cx + (size//2) * math.cos(angle)
            py = cy + (size//2) * math.sin(angle)
            points.append(f"{px:.1f},{py:.1f}")
        shape = f'<polygon points="{" ".join(points)}" fill="{colour}"/>'
        name = "Hexagon"
    elif shape_type == 'oval':
        shape = f'<ellipse cx="{cx}" cy="{cy}" rx="{size//2}" ry="{size//3}" fill="{colour}"/>'
        name = "Oval"
    elif shape_type == 'diamond':
        points = f"{cx},{cy - size//2} {cx + size//2},{cy} {cx},{cy + size//2} {cx - size//2},{cy}"
        shape = f'<polygon points="{points}" fill="{colour}"/>'
        name = "Diamond"
    else:
        shape = f'<circle cx="{cx}" cy="{cy}" r="{size//2}" fill="{colour}"/>'
        name = "Circle"
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
        <rect width="200" height="200" fill="{COLOURS['light_grey']}"/>
        {shape}
    </svg>'''
    
    return svg, name


def generate_3d_shape_svg(shape_type):
    """Generate SVG of a 3D shape"""
    colour = COLOURS['blue']
    
    if shape_type == 'cube':
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
            <rect width="200" height="200" fill="{COLOURS['light_grey']}"/>
            <!-- Front face -->
            <rect x="50" y="70" width="70" height="70" fill="{colour}" stroke="{COLOURS['dark']}" stroke-width="2"/>
            <!-- Top face -->
            <polygon points="50,70 80,40 150,40 120,70" fill="{COLOURS['green']}" stroke="{COLOURS['dark']}" stroke-width="2"/>
            <!-- Side face -->
            <polygon points="120,70 150,40 150,110 120,140" fill="{COLOURS['purple']}" stroke="{COLOURS['dark']}" stroke-width="2"/>
        </svg>'''
        name = "Cube"
    elif shape_type == 'sphere':
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
            <rect width="200" height="200" fill="{COLOURS['light_grey']}"/>
            <defs>
                <radialGradient id="sphereGrad" cx="30%" cy="30%">
                    <stop offset="0%" style="stop-color:#87CEEB"/>
                    <stop offset="100%" style="stop-color:{colour}"/>
                </radialGradient>
            </defs>
            <circle cx="100" cy="100" r="60" fill="url(#sphereGrad)" stroke="{COLOURS['dark']}" stroke-width="2"/>
        </svg>'''
        name = "Sphere"
    elif shape_type == 'cylinder':
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
            <rect width="200" height="200" fill="{COLOURS['light_grey']}"/>
            <rect x="50" y="60" width="100" height="80" fill="{colour}" stroke="{COLOURS['dark']}" stroke-width="2"/>
            <ellipse cx="100" cy="60" rx="50" ry="20" fill="{COLOURS['green']}" stroke="{COLOURS['dark']}" stroke-width="2"/>
            <ellipse cx="100" cy="140" rx="50" ry="20" fill="{colour}" stroke="{COLOURS['dark']}" stroke-width="2"/>
        </svg>'''
        name = "Cylinder"
    elif shape_type == 'cone':
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
            <rect width="200" height="200" fill="{COLOURS['light_grey']}"/>
            <polygon points="100,30 50,150 150,150" fill="{colour}" stroke="{COLOURS['dark']}" stroke-width="2"/>
            <ellipse cx="100" cy="150" rx="50" ry="20" fill="{COLOURS['green']}" stroke="{COLOURS['dark']}" stroke-width="2"/>
        </svg>'''
        name = "Cone"
    elif shape_type == 'pyramid':
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
            <rect width="200" height="200" fill="{COLOURS['light_grey']}"/>
            <!-- Front face -->
            <polygon points="100,30 50,150 150,150" fill="{colour}" stroke="{COLOURS['dark']}" stroke-width="2"/>
            <!-- Right face -->
            <polygon points="100,30 150,150 130,120" fill="{COLOURS['purple']}" stroke="{COLOURS['dark']}" stroke-width="2"/>
        </svg>'''
        name = "Pyramid"
    elif shape_type == 'cuboid':
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
            <rect width="200" height="200" fill="{COLOURS['light_grey']}"/>
            <!-- Front face -->
            <rect x="40" y="80" width="90" height="60" fill="{colour}" stroke="{COLOURS['dark']}" stroke-width="2"/>
            <!-- Top face -->
            <polygon points="40,80 70,50 160,50 130,80" fill="{COLOURS['green']}" stroke="{COLOURS['dark']}" stroke-width="2"/>
            <!-- Side face -->
            <polygon points="130,80 160,50 160,110 130,140" fill="{COLOURS['purple']}" stroke="{COLOURS['dark']}" stroke-width="2"/>
        </svg>'''
        name = "Cuboid"
    else:
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
            <rect width="200" height="200" fill="{COLOURS['light_grey']}"/>
            <circle cx="100" cy="100" r="60" fill="{colour}"/>
        </svg>'''
        name = "Sphere"
    
    return svg, name


def generate_pattern_svg(pattern_elements, repeat_count=4):
    """Generate SVG showing a repeating pattern"""
    element_width = 50
    total_width = element_width * len(pattern_elements) * repeat_count + 20
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {min(400, total_width)} 80">
        <rect width="{min(400, total_width)}" height="80" fill="{COLOURS['light_grey']}"/>
    '''
    
    x = 10
    for _ in range(repeat_count):
        for element in pattern_elements:
            shape, colour = element
            if shape == 'circle':
                svg += f'<circle cx="{x + 20}" cy="40" r="18" fill="{colour}"/>'
            elif shape == 'square':
                svg += f'<rect x="{x + 5}" y="25" width="30" height="30" fill="{colour}"/>'
            elif shape == 'triangle':
                svg += f'<polygon points="{x + 20},22 {x + 5},55 {x + 35},55" fill="{colour}"/>'
            elif shape == 'star':
                svg += f'<text x="{x + 20}" y="50" font-size="30" text-anchor="middle" fill="{colour}">★</text>'
            x += element_width
    
    svg += '</svg>'
    return svg


def generate_number_pattern_svg(numbers):
    """Generate SVG showing a number sequence"""
    box_width = 50
    total_width = box_width * len(numbers) + 20
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_width} 80">
        <rect width="{total_width}" height="80" fill="{COLOURS['light_grey']}"/>
    '''
    
    x = 10
    for i, num in enumerate(numbers):
        fill = COLOURS['blue'] if num != '?' else COLOURS['orange']
        svg += f'''
            <rect x="{x}" y="15" width="45" height="50" fill="{fill}" rx="5"/>
            <text x="{x + 22}" y="50" font-size="24" font-family="Arial" fill="{COLOURS['white']}" text-anchor="middle" font-weight="bold">{num}</text>
        '''
        x += box_width
    
    svg += '</svg>'
    return svg


def generate_symmetry_svg(shape_type, show_line=True):
    """Generate SVG showing symmetry"""
    svg, name = generate_shape_svg(shape_type, COLOURS['blue'], 100)
    
    if show_line:
        # Add line of symmetry
        svg = svg.replace('</svg>', f'''
            <line x1="100" y1="30" x2="100" y2="170" stroke="{COLOURS['red']}" stroke-width="3" stroke-dasharray="8,4"/>
            <text x="100" y="190" font-size="12" fill="{COLOURS['dark']}" text-anchor="middle">Line of Symmetry</text>
        </svg>''')
    
    return svg


def generate_fraction_svg(numerator, denominator, filled=None):
    """Generate SVG showing a fraction visually"""
    if filled is None:
        filled = numerator
    
    if denominator <= 4:
        # Use a circle divided into parts
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
            <rect width="200" height="200" fill="{COLOURS['light_grey']}"/>
        '''
        
        for i in range(denominator):
            angle_start = (i * 360 / denominator) - 90
            angle_end = ((i + 1) * 360 / denominator) - 90
            
            x1 = 100 + 60 * math.cos(math.radians(angle_start))
            y1 = 100 + 60 * math.sin(math.radians(angle_start))
            x2 = 100 + 60 * math.cos(math.radians(angle_end))
            y2 = 100 + 60 * math.sin(math.radians(angle_end))
            
            large_arc = 1 if 360 / denominator > 180 else 0
            colour = COLOURS['blue'] if i < filled else COLOURS['light_grey']
            
            svg += f'<path d="M100,100 L{x1:.1f},{y1:.1f} A60,60 0 {large_arc},1 {x2:.1f},{y2:.1f} Z" fill="{colour}" stroke="{COLOURS["dark"]}" stroke-width="2"/>'
        
        svg += f'''
            <text x="100" y="180" font-size="20" fill="{COLOURS['dark']}" text-anchor="middle" font-weight="bold">{numerator}/{denominator}</text>
        </svg>'''
    else:
        # Use a bar divided into parts
        bar_width = 160
        part_width = bar_width / denominator
        
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 150">
            <rect width="200" height="150" fill="{COLOURS['light_grey']}"/>
        '''
        
        for i in range(denominator):
            x = 20 + i * part_width
            colour = COLOURS['blue'] if i < filled else COLOURS['white']
            svg += f'<rect x="{x:.1f}" y="40" width="{part_width:.1f}" height="50" fill="{colour}" stroke="{COLOURS["dark"]}" stroke-width="1"/>'
        
        svg += f'''
            <text x="100" y="120" font-size="20" fill="{COLOURS['dark']}" text-anchor="middle" font-weight="bold">{numerator}/{denominator}</text>
        </svg>'''
    
    return svg


def generate_multiplication_array_svg(rows, cols):
    """Generate SVG showing multiplication as an array"""
    dot_size = 15
    spacing = 25
    margin = 20
    
    width = cols * spacing + margin * 2
    height = rows * spacing + margin * 2 + 30
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
        <rect width="{width}" height="{height}" fill="{COLOURS['light_grey']}"/>
    '''
    
    for r in range(rows):
        for c in range(cols):
            x = margin + c * spacing + spacing // 2
            y = margin + r * spacing + spacing // 2
            svg += f'<circle cx="{x}" cy="{y}" r="{dot_size//2}" fill="{COLOURS["blue"]}"/>'
    
    svg += f'''
        <text x="{width//2}" y="{height - 10}" font-size="14" fill="{COLOURS['dark']}" text-anchor="middle">{rows} × {cols} = {rows * cols}</text>
    </svg>'''
    
    return svg


# ============================================================
# QUESTION GENERATORS BY LEVEL
# ============================================================

def generate_level_1_questions():
    """Level 1: 2D Shapes (Foundation)
    NCCA LO: Sa - Name and describe properties of common 2D shapes
    """
    questions = []
    
    shapes_2d = ['circle', 'square', 'rectangle', 'triangle']
    
    # Type 1: Identify shape name (25 questions)
    for i in range(25):
        shape = shapes_2d[i % len(shapes_2d)]
        svg, name = generate_shape_svg(shape)
        
        correct = name
        distractors = [s.capitalize() for s in shapes_2d if s != shape][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        templates = [
            "What shape is this?",
            "Name this shape.",
            "What is this shape called?",
        ]
        
        questions.append({
            'question_text': templates[i % 3],
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"This is a {name}.",
            'question_image_svg': svg
        })
    
    # Type 2: Shape properties (15 questions)
    properties = [
        ("circle", "no corners", "A circle is round with no corners."),
        ("square", "4 equal sides", "A square has 4 equal sides."),
        ("rectangle", "4 sides, 2 long and 2 short", "A rectangle has 4 sides."),
        ("triangle", "3 sides", "A triangle has 3 sides."),
        ("square", "4 corners", "A square has 4 corners."),
        ("triangle", "3 corners", "A triangle has 3 corners."),
    ]
    
    for i in range(15):
        shape, correct, explanation = properties[i % len(properties)]
        svg, name = generate_shape_svg(shape)
        
        question = f"What is true about this {name.lower()}?"
        distractors = ["5 sides", "No sides", "Round like a ball"]
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        while len(options) < 4:
            options.append("None of these")
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': explanation,
            'question_image_svg': svg
        })
    
    # Type 3: Count sides/corners (10 questions)
    for i in range(10):
        shape = shapes_2d[i % len(shapes_2d)]
        svg, name = generate_shape_svg(shape)
        
        sides = {'circle': 0, 'square': 4, 'rectangle': 4, 'triangle': 3}
        correct = str(sides[shape])
        
        q_type = i % 2
        if q_type == 0:
            question = f"How many sides does this {name.lower()} have?"
        else:
            question = f"How many corners does this {name.lower()} have?"
        
        distractors = ['2', '3', '4', '5', '6']
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"A {name.lower()} has {correct} sides/corners.",
            'question_image_svg': svg
        })
    
    return questions


def generate_level_2_questions():
    """Level 2: 3D Shapes (Foundation)
    NCCA LO: Sb - Name and describe common 3D shapes
    """
    questions = []
    
    shapes_3d = ['cube', 'sphere', 'cylinder', 'cone', 'pyramid', 'cuboid']
    
    # Type 1: Identify 3D shape (25 questions)
    for i in range(25):
        shape = shapes_3d[i % len(shapes_3d)]
        svg, name = generate_3d_shape_svg(shape)
        
        correct = name
        distractors = [s.capitalize() for s in shapes_3d if s != shape][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': "What 3D shape is this?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"This is a {name}.",
            'question_image_svg': svg
        })
    
    # Type 2: Real-world 3D shapes (15 questions)
    real_world = [
        ("dice", "Cube", "A dice is shaped like a cube."),
        ("ball", "Sphere", "A ball is shaped like a sphere."),
        ("tin can", "Cylinder", "A tin can is shaped like a cylinder."),
        ("ice cream cone", "Cone", "An ice cream cone is cone-shaped."),
        ("Egyptian pyramid", "Pyramid", "The pyramids are pyramid-shaped."),
        ("cereal box", "Cuboid", "A cereal box is a cuboid."),
        ("orange", "Sphere", "An orange is shaped like a sphere."),
        ("toilet roll", "Cylinder", "A toilet roll is a cylinder."),
    ]
    
    for i in range(15):
        item, correct, explanation = real_world[i % len(real_world)]
        
        question = f"What 3D shape is a {item}?"
        distractors = [s.capitalize() for s in shapes_3d if s.capitalize() != correct][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': explanation,
            'question_image_svg': ''
        })
    
    # Type 3: 3D shape properties (10 questions)
    properties_3d = [
        ("cube", "6 flat faces", "A cube has 6 square faces."),
        ("sphere", "no flat faces", "A sphere is completely round."),
        ("cylinder", "2 circular faces", "A cylinder has 2 circular ends."),
        ("cone", "1 circular face", "A cone has 1 circular base."),
        ("pyramid", "triangular faces", "A pyramid has triangular sides."),
    ]
    
    for i in range(10):
        shape, correct, explanation = properties_3d[i % len(properties_3d)]
        svg, name = generate_3d_shape_svg(shape)
        
        question = f"What is true about a {name.lower()}?"
        distractors = ["no faces", "10 faces", "all round"]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': explanation,
            'question_image_svg': svg
        })
    
    return questions


def generate_level_3_questions():
    """Level 3: Simple Patterns (Foundation)
    NCCA LO: Sc - Recognise and describe repeating patterns
    """
    questions = []
    
    # Type 1: Continue the pattern (25 questions)
    patterns = [
        ([('circle', COLOURS['red']), ('circle', COLOURS['blue'])], 'Red circle'),
        ([('square', COLOURS['green']), ('square', COLOURS['yellow'])], 'Green square'),
        ([('circle', COLOURS['red']), ('square', COLOURS['red'])], 'Red circle'),
        ([('triangle', COLOURS['blue']), ('circle', COLOURS['blue'])], 'Blue triangle'),
    ]
    
    for i in range(25):
        pattern, next_item = patterns[i % len(patterns)]
        
        question = "What comes next in the pattern?"
        distractors = ['Blue square', 'Red triangle', 'Green circle', 'Yellow square']
        distractors = [d for d in distractors if d != next_item][:3]
        
        options = [next_item] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(next_item)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The pattern repeats, so next is: {next_item}",
            'question_image_svg': generate_pattern_svg(pattern, 3)
        })
    
    # Type 2: Describe the pattern (15 questions)
    for i in range(15):
        pattern_type = i % 3
        
        if pattern_type == 0:
            pattern = [('circle', COLOURS['red']), ('circle', COLOURS['blue'])]
            correct = "Colours alternate"
            description = "red, blue, red, blue..."
        elif pattern_type == 1:
            pattern = [('circle', COLOURS['red']), ('square', COLOURS['red'])]
            correct = "Shapes alternate"
            description = "circle, square, circle, square..."
        else:
            pattern = [('circle', COLOURS['red']), ('circle', COLOURS['red']), ('square', COLOURS['blue'])]
            correct = "Two circles, then a square"
            description = "circle, circle, square repeats"
        
        distractors = ["All the same", "Random order", "Gets bigger"]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': "How would you describe this pattern?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The pattern is: {description}",
            'question_image_svg': generate_pattern_svg(pattern, 2)
        })
    
    # Type 3: Find the missing item (10 questions)
    for i in range(10):
        pattern = [('circle', COLOURS['red']), ('square', COLOURS['blue'])]
        missing_pos = random.choice([1, 2, 3])
        
        correct = "Square" if missing_pos % 2 == 0 else "Circle"
        distractors = ["Triangle", "Star", "Diamond"]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Position {missing_pos} is missing. What shape should go there?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Following the pattern, position {missing_pos} should be a {correct}.",
            'question_image_svg': generate_pattern_svg(pattern, 2)
        })
    
    return questions


def generate_level_4_questions():
    """Level 4: Number Patterns (Developing)
    NCCA LO: Sd - Recognise and continue simple number patterns
    """
    questions = []
    
    # Type 1: Continue counting patterns (20 questions)
    for i in range(20):
        pattern_type = i % 4
        
        if pattern_type == 0:  # Count by 1s
            start = random.randint(1, 10)
            numbers = [start + j for j in range(5)]
            step = 1
        elif pattern_type == 1:  # Count by 2s
            start = random.choice([2, 4, 6, 8, 10])
            numbers = [start + j * 2 for j in range(5)]
            step = 2
        elif pattern_type == 2:  # Count by 5s
            start = random.choice([5, 10, 15])
            numbers = [start + j * 5 for j in range(5)]
            step = 5
        else:  # Count by 10s
            start = random.choice([10, 20, 30])
            numbers = [start + j * 10 for j in range(5)]
            step = 10
        
        display = [str(n) for n in numbers[:4]] + ['?']
        correct = str(numbers[4])
        
        distractors = [str(numbers[4] + step), str(numbers[4] - step), str(numbers[4] + 1)]
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': "What number comes next?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The pattern goes up by {step} each time. {numbers[3]} + {step} = {numbers[4]}",
            'question_image_svg': generate_number_pattern_svg(display)
        })
    
    # Type 2: Identify the rule (15 questions)
    rules = [
        ([2, 4, 6, 8, 10], "Add 2 each time", 2),
        ([5, 10, 15, 20, 25], "Add 5 each time", 5),
        ([10, 20, 30, 40, 50], "Add 10 each time", 10),
        ([1, 3, 5, 7, 9], "Add 2 each time (odd numbers)", 2),
        ([3, 6, 9, 12, 15], "Add 3 each time", 3),
    ]
    
    for i in range(15):
        numbers, correct, step = rules[i % len(rules)]
        display = [str(n) for n in numbers]
        
        distractors = ["Add 1 each time", "Subtract 2 each time", "Multiply by 2"]
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': "What is the rule for this pattern?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Each number increases by {step}.",
            'question_image_svg': generate_number_pattern_svg(display)
        })
    
    # Type 3: Find missing number in pattern (15 questions)
    for i in range(15):
        step = random.choice([2, 3, 5, 10])
        start = random.randint(1, 5) * step
        numbers = [start + j * step for j in range(5)]
        
        missing_pos = random.randint(1, 3)
        display = [str(n) if j != missing_pos else '?' for j, n in enumerate(numbers)]
        correct = str(numbers[missing_pos])
        
        distractors = [str(numbers[missing_pos] + step), str(numbers[missing_pos] - step), str(numbers[missing_pos] + 1)]
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': "Find the missing number in the pattern.",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The pattern adds {step} each time. The missing number is {numbers[missing_pos]}.",
            'question_image_svg': generate_number_pattern_svg(display)
        })
    
    return questions


def generate_level_5_questions():
    """Level 5: Symmetry (Developing)
    NCCA LO: Se - Identify shapes and lines with symmetry
    """
    questions = []
    
    symmetric_shapes = ['circle', 'square', 'rectangle', 'triangle']
    
    # Type 1: Does it have symmetry? (20 questions)
    symmetry_facts = [
        ('circle', True, "A circle has infinite lines of symmetry."),
        ('square', True, "A square has 4 lines of symmetry."),
        ('rectangle', True, "A rectangle has 2 lines of symmetry."),
        ('triangle', True, "An equilateral triangle has 3 lines of symmetry."),
    ]
    
    for i in range(20):
        shape, has_symmetry, explanation = symmetry_facts[i % len(symmetry_facts)]
        
        correct = "Yes" if has_symmetry else "No"
        options = ["Yes", "No", "Sometimes", "Cannot tell"]
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Does this shape have a line of symmetry?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': explanation,
            'question_image_svg': generate_symmetry_svg(shape)
        })
    
    # Type 2: What is symmetry? (15 questions)
    symmetry_qs = [
        ("What does 'symmetrical' mean?", "Both halves match", "Symmetrical means identical on both sides of a line."),
        ("A line of symmetry divides a shape into...", "Two matching halves", "The line creates a mirror image."),
        ("If you fold along the line of symmetry...", "Both sides match", "Folding shows the matching halves."),
        ("How many lines of symmetry does a square have?", "4", "A square can be folded 4 different ways."),
        ("Which letter has a line of symmetry: A or F?", "A", "The letter A is symmetrical vertically."),
    ]
    
    for i in range(15):
        question, correct, explanation = symmetry_qs[i % len(symmetry_qs)]
        
        distractors = ["Different sizes", "Random shapes", "No match"]
        if correct.isdigit():
            distractors = ["2", "6", "0"]
            distractors = [d for d in distractors if d != correct]
        
        options = [correct] + distractors[:3]
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': explanation,
            'question_image_svg': ''
        })
    
    # Type 3: Compare symmetry (15 questions)
    for i in range(15):
        shape1 = random.choice(symmetric_shapes)
        shape2 = random.choice(symmetric_shapes)
        
        symmetry_count = {'circle': 'infinite', 'square': '4', 'rectangle': '2', 'triangle': '3'}
        
        question = f"Which has more lines of symmetry: a {shape1} or a {shape2}?"
        
        if shape1 == 'circle' or (symmetry_count[shape1] > symmetry_count[shape2]):
            correct = shape1.capitalize()
        elif shape2 == 'circle' or (symmetry_count[shape2] > symmetry_count[shape1]):
            correct = shape2.capitalize()
        else:
            correct = "They have the same"
        
        options = [shape1.capitalize(), shape2.capitalize(), "They have the same", "Neither has symmetry"]
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"A {shape1} has {symmetry_count[shape1]} lines, a {shape2} has {symmetry_count[shape2]} lines.",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_6_questions():
    """Level 6: More 2D Shapes (Developing)
    NCCA LO: Sf - Name and identify pentagon, hexagon, oval, diamond
    """
    questions = []
    
    shapes = ['pentagon', 'hexagon', 'oval', 'diamond']
    
    # Type 1: Identify extended shapes (25 questions)
    for i in range(25):
        shape = shapes[i % len(shapes)]
        svg, name = generate_shape_svg(shape)
        
        correct = name
        all_shapes = ['Pentagon', 'Hexagon', 'Oval', 'Diamond', 'Circle', 'Square']
        distractors = [s for s in all_shapes if s != correct][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': "What shape is this?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"This is a {name}.",
            'question_image_svg': svg
        })
    
    # Type 2: Count sides (15 questions)
    sides = {'pentagon': 5, 'hexagon': 6, 'oval': 0, 'diamond': 4}
    
    for i in range(15):
        shape = shapes[i % len(shapes)]
        svg, name = generate_shape_svg(shape)
        
        correct = str(sides[shape])
        distractors = ['3', '4', '5', '6', '8']
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"How many sides does a {name.lower()} have?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"A {name.lower()} has {sides[shape]} sides.",
            'question_image_svg': svg
        })
    
    # Type 3: Shape meanings (10 questions)
    meanings = [
        ("pentagon", "5 sides", "Penta means 5 in Greek."),
        ("hexagon", "6 sides", "Hexa means 6 in Greek."),
        ("oval", "egg-shaped", "Oval means egg-shaped."),
        ("diamond", "4 sides, tilted square", "A diamond is like a tilted square."),
    ]
    
    for i in range(10):
        shape, correct, explanation = meanings[i % len(meanings)]
        
        distractors = ["3 sides", "7 sides", "round"]
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"A {shape} has:",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': explanation,
            'question_image_svg': ''
        })
    
    return questions


def generate_level_7_questions():
    """Level 7: Odd and Even Numbers (Progressing)
    NCNA LO: Sg - Identify and describe odd/even numbers
    """
    questions = []
    
    # Type 1: Is it odd or even? (25 questions)
    for i in range(25):
        number = random.randint(1, 50)
        is_even = number % 2 == 0
        
        correct = "Even" if is_even else "Odd"
        options = ["Even", "Odd", "Neither", "Both"]
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Is {number} odd or even?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{number} is {correct.lower()} because it {'can' if is_even else 'cannot'} be divided by 2 evenly.",
            'question_image_svg': ''
        })
    
    # Type 2: What makes a number even/odd? (15 questions)
    even_odd_facts = [
        ("even", "ends in 0, 2, 4, 6, or 8", "Even numbers can be split into 2 equal groups."),
        ("odd", "ends in 1, 3, 5, 7, or 9", "Odd numbers have 1 left over when split in 2."),
        ("even", "can be divided by 2 evenly", "2, 4, 6, 8, 10... are all even."),
        ("odd", "has a remainder of 1 when divided by 2", "1, 3, 5, 7, 9... are all odd."),
    ]
    
    for i in range(15):
        num_type, correct, explanation = even_odd_facts[i % len(even_odd_facts)]
        
        question = f"An {num_type} number..."
        distractors = ["ends in 7 only", "cannot be counted", "is always less than 10"]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': explanation,
            'question_image_svg': ''
        })
    
    # Type 3: Find all even/odd in a list (10 questions)
    for i in range(10):
        numbers = random.sample(range(1, 20), 5)
        find_type = "even" if i % 2 == 0 else "odd"
        
        found = [n for n in numbers if (n % 2 == 0) == (find_type == "even")]
        correct = ", ".join(str(n) for n in sorted(found)) if found else "None"
        
        # Create distractors
        wrong = [n for n in numbers if n not in found]
        distractors = [
            ", ".join(str(n) for n in sorted(wrong[:2])) if len(wrong) >= 2 else "All of them",
            "All of them",
            "None",
        ]
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        while len(options) < 4:
            options.append(str(random.randint(1, 20)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Which of these are {find_type}: {', '.join(str(n) for n in numbers)}?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The {find_type} numbers are: {correct}",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_8_questions():
    """Level 8: Fractions (Progressing)
    NCCA LO: Sh - Simple fractions: half, quarter, third
    """
    questions = []
    
    # Type 1: Identify fractions from pictures (25 questions)
    fractions = [(1, 2), (1, 4), (2, 4), (3, 4), (1, 3), (2, 3)]
    
    for i in range(25):
        num, denom = fractions[i % len(fractions)]
        
        correct = f"{num}/{denom}"
        distractors = [f"{n}/{d}" for n, d in fractions if (n, d) != (num, denom)][:3]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': "What fraction is shaded?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{num} out of {denom} parts are shaded = {num}/{denom}",
            'question_image_svg': generate_fraction_svg(num, denom)
        })
    
    # Type 2: Fraction vocabulary (15 questions)
    vocab = [
        ("half", "1/2", "2 equal parts"),
        ("quarter", "1/4", "4 equal parts"),
        ("third", "1/3", "3 equal parts"),
        ("three quarters", "3/4", "3 out of 4 parts"),
        ("two thirds", "2/3", "2 out of 3 parts"),
    ]
    
    for i in range(15):
        word, fraction, meaning = vocab[i % len(vocab)]
        
        q_type = i % 2
        if q_type == 0:
            question = f"What fraction is 'one {word}'?"
            correct = fraction
            distractors = [v[1] for v in vocab if v[1] != fraction][:3]
        else:
            question = f"{fraction} means the shape is divided into:"
            correct = meaning
            distractors = ["1 equal part", "10 equal parts", "no parts"]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"One {word} = {fraction}, which means {meaning}.",
            'question_image_svg': ''
        })
    
    # Type 3: Fraction of a number (10 questions)
    for i in range(10):
        whole = random.choice([4, 6, 8, 10, 12])
        fraction_type = random.choice(['half', 'quarter', 'third'])
        
        if fraction_type == 'half':
            correct = str(whole // 2)
            question = f"What is half of {whole}?"
        elif fraction_type == 'quarter' and whole % 4 == 0:
            correct = str(whole // 4)
            question = f"What is a quarter of {whole}?"
        else:
            whole = random.choice([6, 9, 12])
            correct = str(whole // 3)
            question = f"What is a third of {whole}?"
        
        distractors = [str(int(correct) + 1), str(int(correct) - 1), str(int(correct) * 2)]
        distractors = [d for d in distractors if d != correct and int(d) > 0][:3]
        
        options = [correct] + distractors
        while len(options) < 4:
            options.append(str(random.randint(1, 10)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{question} Answer: {correct}",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_9_questions():
    """Level 9: Multiplication Concepts (Progressing)
    NCCA LO: Si - Understand multiplication as repeated addition
    """
    questions = []
    
    # Type 1: Multiplication as arrays (20 questions)
    for i in range(20):
        rows = random.randint(2, 5)
        cols = random.randint(2, 5)
        total = rows * cols
        
        correct = str(total)
        distractors = [str(total + 1), str(total - 1), str(rows + cols)]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"How many dots in total? ({rows} rows × {cols} columns)",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{rows} × {cols} = {total}",
            'question_image_svg': generate_multiplication_array_svg(rows, cols)
        })
    
    # Type 2: Repeated addition (15 questions)
    for i in range(15):
        groups = random.randint(2, 5)
        items = random.randint(2, 6)
        total = groups * items
        
        addition = " + ".join([str(items)] * groups)
        
        q_type = i % 2
        if q_type == 0:
            question = f"What is {addition}?"
            correct = str(total)
            distractors = [str(total + items), str(total - items), str(groups + items)]
        else:
            question = f"{groups} groups of {items} = ?"
            correct = str(total)
            distractors = [str(total + 1), str(total - 1), str(groups * 2)]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{groups} × {items} = {total} (or {addition} = {total})",
            'question_image_svg': ''
        })
    
    # Type 3: Real-world multiplication (15 questions)
    scenarios = [
        (3, 4, "legs", "chairs", "How many legs on 3 chairs (4 legs each)?"),
        (5, 2, "eyes", "people", "How many eyes do 5 people have in total?"),
        (4, 5, "fingers", "hands", "How many fingers on 4 hands?"),
        (2, 6, "eggs", "boxes", "How many eggs in 2 boxes of 6?"),
        (3, 7, "days", "weeks", "How many days in 3 weeks?"),
    ]
    
    for i in range(15):
        groups, items, item_name, group_name, question = scenarios[i % len(scenarios)]
        total = groups * items
        
        correct = str(total)
        distractors = [str(total + items), str(total - items), str(groups + items)]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{groups} × {items} = {total} {item_name}",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_10_questions():
    """Level 10: Division Concepts (Consolidating)
    NCCA LO: Sj - Understand division as sharing
    """
    questions = []
    
    # Type 1: Equal sharing (20 questions)
    for i in range(20):
        total = random.choice([6, 8, 10, 12, 15, 18, 20])
        groups = random.choice([2, 3, 4, 5])
        while total % groups != 0:
            total = random.choice([6, 8, 10, 12, 15, 18, 20])
        
        each = total // groups
        
        correct = str(each)
        distractors = [str(each + 1), str(each - 1), str(total)]
        distractors = [d for d in distractors if int(d) > 0][:3]
        
        options = [correct] + distractors
        while len(options) < 4:
            options.append(str(random.randint(1, 10)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Share {total} sweets equally between {groups} friends. How many does each get?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{total} ÷ {groups} = {each} each",
            'question_image_svg': ''
        })
    
    # Type 2: Division as grouping (15 questions)
    for i in range(15):
        total = random.choice([10, 12, 15, 16, 18, 20])
        group_size = random.choice([2, 3, 4, 5])
        while total % group_size != 0:
            total = random.choice([10, 12, 15, 16, 18, 20])
        
        groups = total // group_size
        
        correct = str(groups)
        distractors = [str(groups + 1), str(groups - 1), str(total)]
        distractors = [d for d in distractors if int(d) > 0][:3]
        
        options = [correct] + distractors
        while len(options) < 4:
            options.append(str(random.randint(1, 10)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"You have {total} pencils. You put {group_size} in each box. How many boxes do you need?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{total} ÷ {group_size} = {groups} boxes",
            'question_image_svg': ''
        })
    
    # Type 3: Division facts (15 questions)
    for i in range(15):
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        product = a * b
        
        q_type = i % 2
        if q_type == 0:
            question = f"{product} ÷ {a} = ?"
            correct = str(b)
        else:
            question = f"{product} ÷ {b} = ?"
            correct = str(a)
        
        distractors = [str(int(correct) + 1), str(int(correct) - 1), str(product)]
        distractors = [d for d in distractors if int(d) > 0][:3]
        
        options = [correct] + distractors
        while len(options) < 4:
            options.append(str(random.randint(1, 10)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{question.replace(' = ?', '')} = {correct}",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_11_questions():
    """Level 11: Number Properties (Consolidating)
    NCCA LO: Sk - Describe properties: factors, multiples
    """
    questions = []
    
    # Type 1: What is a multiple? (20 questions)
    for i in range(20):
        base = random.randint(2, 10)
        multiplier = random.randint(2, 10)
        multiple = base * multiplier
        
        q_type = i % 3
        
        if q_type == 0:
            question = f"Is {multiple} a multiple of {base}?"
            correct = "Yes"
            options = ["Yes", "No", "Sometimes", "Cannot tell"]
            solution = f"{multiple} = {base} × {multiplier}, so yes."
        elif q_type == 1:
            non_multiple = multiple + 1
            question = f"Is {non_multiple} a multiple of {base}?"
            correct = "No"
            options = ["Yes", "No", "Sometimes", "Cannot tell"]
            solution = f"{non_multiple} ÷ {base} has a remainder, so no."
        else:
            question = f"What is the 3rd multiple of {base}?"
            correct = str(base * 3)
            distractors = [str(base * 2), str(base * 4), str(base + 3)]
            options = [correct] + distractors
            random.shuffle(options)
            solution = f"Multiples of {base}: {base}, {base*2}, {base*3}..."
        
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': solution,
            'question_image_svg': ''
        })
    
    # Type 2: What is a factor? (15 questions)
    factor_facts = [
        (12, [1, 2, 3, 4, 6, 12]),
        (10, [1, 2, 5, 10]),
        (8, [1, 2, 4, 8]),
        (15, [1, 3, 5, 15]),
        (20, [1, 2, 4, 5, 10, 20]),
    ]
    
    for i in range(15):
        number, factors = factor_facts[i % len(factor_facts)]
        test_num = random.choice(factors) if i % 2 == 0 else number + 1
        
        if test_num in factors:
            correct = "Yes"
            solution = f"{number} ÷ {test_num} = {number // test_num} with no remainder."
        else:
            correct = "No"
            solution = f"{number} ÷ {test_num} has a remainder."
        
        question = f"Is {test_num} a factor of {number}?"
        options = ["Yes", "No", "Sometimes", "Cannot tell"]
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': solution,
            'question_image_svg': ''
        })
    
    # Type 3: Find factors/multiples (15 questions)
    for i in range(15):
        number = random.choice([6, 8, 10, 12])
        
        q_type = i % 2
        if q_type == 0:
            question = f"List the first 4 multiples of {number}:"
            multiples = [number * j for j in range(1, 5)]
            correct = ", ".join(str(m) for m in multiples)
            wrong1 = ", ".join(str(m + 1) for m in multiples)
            wrong2 = ", ".join(str(number + j) for j in range(1, 5))
            distractors = [wrong1, wrong2, f"{number}, {number}, {number}, {number}"]
        else:
            question = f"Which of these is a factor of {number}?"
            factor = random.choice([f for f in [1, 2, 3, 4, 5, 6] if number % f == 0])
            correct = str(factor)
            non_factors = [n for n in range(2, 10) if number % n != 0]
            distractors = [str(n) for n in random.sample(non_factors, min(3, len(non_factors)))]
        
        options = [correct] + distractors[:3]
        while len(options) < 4:
            options.append("None")
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Answer: {correct}",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_12_questions():
    """Level 12: Problem Solving with Shapes & Numbers (Consolidating)
    NCCA LO: Sl - Apply knowledge to real-world problems
    """
    questions = []
    
    # Type 1: Shape problems (15 questions)
    shape_problems = [
        ("A stop sign is what shape?", "Hexagon", ["Square", "Circle", "Triangle"]),
        ("How many sides do 3 triangles have in total?", "9", ["6", "12", "3"]),
        ("A square has 4 sides. How many sides do 5 squares have?", "20", ["15", "25", "9"]),
        ("If you cut a square in half diagonally, what shape do you get?", "Triangle", ["Rectangle", "Circle", "Square"]),
        ("How many corners do 2 rectangles have in total?", "8", ["6", "4", "10"]),
    ]
    
    for i in range(15):
        question, correct, distractors = shape_problems[i % len(shape_problems)]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Answer: {correct}",
            'question_image_svg': ''
        })
    
    # Type 2: Pattern and sequence problems (20 questions)
    for i in range(20):
        problem_type = i % 4
        
        if problem_type == 0:
            # Tile pattern
            tiles_per_row = random.randint(4, 8)
            rows = random.randint(3, 6)
            total = tiles_per_row * rows
            question = f"A floor has {rows} rows of tiles. Each row has {tiles_per_row} tiles. How many tiles in total?"
            correct = str(total)
            distractors = [str(total + tiles_per_row), str(tiles_per_row + rows), str(total - rows)]
        elif problem_type == 1:
            # Stacking pattern
            bottom = random.randint(5, 8)
            levels = 3
            total = sum(bottom - i for i in range(levels))
            question = f"Blocks are stacked with {bottom} on bottom, {bottom-1} on next, {bottom-2} on top. How many total?"
            correct = str(total)
            distractors = [str(total + 1), str(bottom * 3), str(total - 1)]
        elif problem_type == 2:
            # Fence posts
            sections = random.randint(4, 8)
            posts = sections + 1
            question = f"A fence has {sections} sections. Each section needs a post at each end. How many posts are needed?"
            correct = str(posts)
            distractors = [str(sections), str(sections * 2), str(posts + 1)]
        else:
            # Handshakes
            people = random.choice([3, 4, 5])
            handshakes = (people * (people - 1)) // 2
            question = f"If {people} people each shake hands once with everyone, how many handshakes?"
            correct = str(handshakes)
            distractors = [str(people), str(people * 2), str(handshakes + 1)]
        
        distractors = [d for d in distractors if d != correct][:3]
        options = [correct] + distractors
        while len(options) < 4:
            options.append(str(random.randint(5, 30)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Answer: {correct}",
            'question_image_svg': ''
        })
    
    # Type 3: Number reasoning (15 questions)
    for i in range(15):
        reason_type = i % 3
        
        if reason_type == 0:
            # Odd + Even
            question = "If you add an odd number and an even number, the result is:"
            correct = "Always odd"
            distractors = ["Always even", "Sometimes odd", "Cannot tell"]
        elif reason_type == 1:
            # Even + Even
            question = "If you add two even numbers, the result is:"
            correct = "Always even"
            distractors = ["Always odd", "Sometimes odd", "Cannot tell"]
        else:
            # Odd + Odd
            question = "If you add two odd numbers, the result is:"
            correct = "Always even"
            distractors = ["Always odd", "Sometimes even", "Cannot tell"]
        
        options = [correct] + distractors
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Answer: {correct}",
            'question_image_svg': ''
        })
    
    return questions


# ============================================================
# MAIN FUNCTIONS
# ============================================================

def generate_all_questions():
    all_questions = []
    
    generators = [
        generate_level_1_questions,
        generate_level_2_questions,
        generate_level_3_questions,
        generate_level_4_questions,
        generate_level_5_questions,
        generate_level_6_questions,
        generate_level_7_questions,
        generate_level_8_questions,
        generate_level_9_questions,
        generate_level_10_questions,
        generate_level_11_questions,
        generate_level_12_questions,
    ]
    
    for level, generator in enumerate(generators, 1):
        print(f"  Generating Level {level}...")
        questions = generator()
        
        if len(questions) > QUESTIONS_PER_LEVEL:
            questions = questions[:QUESTIONS_PER_LEVEL]
        
        for q in questions:
            q['level'] = level
            q['topic'] = TOPIC
            q['difficulty'] = DIFFICULTY
        
        all_questions.extend(questions)
        print(f"    Level {level}: {len(questions)} questions generated")
    
    return all_questions


def validate_questions(questions):
    errors = []
    for i, q in enumerate(questions):
        if not q.get('question_text'):
            errors.append(f"Q{i+1}: Missing question_text")
        if not q.get('correct_answer') in ['A', 'B', 'C', 'D']:
            errors.append(f"Q{i+1}: Invalid correct_answer")
    
    seen_text = set()
    seen_visual = {}
    for q in questions:
        text = q['question_text']
        svg = q.get('question_image_svg', '')
        if svg:
            if text in seen_visual:
                if hash(svg) in seen_visual[text]:
                    errors.append(f"Duplicate: '{text[:50]}...'")
                else:
                    seen_visual[text].add(hash(svg))
            else:
                seen_visual[text] = {hash(svg)}
        else:
            if text in seen_text:
                errors.append(f"Duplicate: '{text[:50]}...'")
            seen_text.add(text)
    
    return errors


def clear_existing_questions():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM questions WHERE topic = ?', (TOPIC,))
        count = cursor.fetchone()[0]
        conn.close()
        
        if count > 0:
            print(f"\n⚠️  Found {count} existing questions for {TOPIC}")
            response = input("Delete existing? (yes/no): ").strip().lower()
            if response == 'yes':
                conn = sqlite3.connect(DATABASE_PATH)
                cursor = conn.cursor()
                cursor.execute('DELETE FROM questions WHERE topic = ?', (TOPIC,))
                conn.commit()
                conn.close()
                print(f"   Deleted {count} questions")
                return True
            return False
    except:
        pass
    return True


def insert_questions(questions):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    inserted = 0
    for q in questions:
        try:
            cursor.execute('''
                INSERT INTO questions 
                (topic, difficulty, level, question_text, option_a, option_b, option_c, option_d, 
                 correct_answer, explanation, question_image_svg)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                q['topic'], q['difficulty'], q['level'],
                q['question_text'], q['option_a'], q['option_b'], 
                q.get('option_c', ''), q.get('option_d', ''),
                q['correct_answer'], q.get('solution', ''),
                q.get('question_image_svg', '')
            ))
            inserted += 1
        except sqlite3.Error as e:
            print(f"Error: {e}")
    
    conn.commit()
    conn.close()
    return inserted


def main():
    print("=" * 60)
    print("AgentMath L2LP Question Generator")
    print(f"Topic: {TOPIC}")
    print(f"Target: {QUESTIONS_PER_LEVEL} × {TOTAL_LEVELS} = {QUESTIONS_PER_LEVEL * TOTAL_LEVELS}")
    print("=" * 60)
    
    if not clear_existing_questions():
        return
    
    print("\nGenerating questions...")
    questions = generate_all_questions()
    print(f"\nTotal: {len(questions)}")
    
    print("\nValidating...")
    errors = validate_questions(questions)
    critical = [e for e in errors if 'Duplicate' not in e]
    
    if critical:
        print(f"❌ {len(critical)} critical errors")
        return
    
    print("✅ Validation passed")
    
    print("\nInserting...")
    inserted = insert_questions(questions)
    print(f"✅ Inserted {inserted} questions!")
    
    print("\nSummary:")
    for level in range(1, 13):
        count = sum(1 for q in questions if q['level'] == level)
        visual = sum(1 for q in questions if q['level'] == level and q.get('question_image_svg'))
        pct = (visual / count * 100) if count else 0
        print(f"  Level {level}: {count} questions, {pct:.0f}% visual")


if __name__ == '__main__':
    main()
