"""
AgentMath L1LP Question Generator
Topic: Shape and Space
Learning Outcomes: 2.18 - 2.21
Version: 1.0

Generates 600 questions (50 per level × 12 levels) for the L1LP strand.
Focus: Position words, movement words, 2D shapes, 3D shapes, sorting shapes, describing shapes.

Level Structure:
- Levels 1-4 (Foundation): 90% visual, 2-3 options
- Levels 5-8 (Developing): 80% visual, 3-4 options  
- Levels 9-12 (Progressing/Consolidating): 70% visual, 4 options
"""

import sqlite3
import random
import json
import math
from datetime import datetime

# Configuration
TOPIC = 'shape_and_space'
MODE = 'l1lp'
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12
DATABASE_PATH = 'instance/mathquiz.db'

# Accessible colour palette
COLOURS = {
    'red': '#E74C3C',
    'blue': '#3498DB',
    'green': '#27AE60',
    'yellow': '#F1C40F',
    'orange': '#E67E22',
    'purple': '#9B59B6'
}

COLOUR_NAMES = list(COLOURS.keys())

# =============================================================================
# SVG GENERATION FUNCTIONS - 2D SHAPES
# =============================================================================

def svg_circle(x, y, size=60, colour='#3498DB', stroke='#2980B9'):
    """Generate a circle"""
    return f'<circle cx="{x + size//2}" cy="{y + size//2}" r="{size//2 - 2}" fill="{colour}" stroke="{stroke}" stroke-width="2"/>'

def svg_square(x, y, size=60, colour='#E74C3C', stroke='#C0392B'):
    """Generate a square"""
    return f'<rect x="{x + 2}" y="{y + 2}" width="{size - 4}" height="{size - 4}" fill="{colour}" stroke="{stroke}" stroke-width="2"/>'

def svg_rectangle(x, y, width=80, height=50, colour='#27AE60', stroke='#1E8449'):
    """Generate a rectangle"""
    return f'<rect x="{x + 2}" y="{y + 2}" width="{width - 4}" height="{height - 4}" fill="{colour}" stroke="{stroke}" stroke-width="2"/>'

def svg_triangle(x, y, size=60, colour='#F1C40F', stroke='#D4AC0D'):
    """Generate a triangle"""
    points = f"{x + size//2},{y + 2} {x + 2},{y + size - 2} {x + size - 2},{y + size - 2}"
    return f'<polygon points="{points}" fill="{colour}" stroke="{stroke}" stroke-width="2"/>'

def svg_oval(x, y, width=70, height=45, colour='#9B59B6', stroke='#7D3C98'):
    """Generate an oval"""
    return f'<ellipse cx="{x + width//2}" cy="{y + height//2}" rx="{width//2 - 2}" ry="{height//2 - 2}" fill="{colour}" stroke="{stroke}" stroke-width="2"/>'

def svg_diamond(x, y, size=60, colour='#E67E22', stroke='#CA6F1E'):
    """Generate a diamond (rotated square)"""
    cx, cy = x + size//2, y + size//2
    half = size//2 - 4
    points = f"{cx},{y + 4} {x + size - 4},{cy} {cx},{y + size - 4} {x + 4},{cy}"
    return f'<polygon points="{points}" fill="{colour}" stroke="{stroke}" stroke-width="2"/>'

def svg_star(x, y, size=60, colour='#F1C40F', stroke='#D4AC0D'):
    """Generate a star"""
    cx, cy = x + size//2, y + size//2
    points = []
    for i in range(5):
        angle_outer = (i * 72 - 90) * math.pi / 180
        angle_inner = ((i * 72) + 36 - 90) * math.pi / 180
        r_outer = size//2 - 4
        r_inner = size//4
        points.append(f"{cx + r_outer * math.cos(angle_outer)},{cy + r_outer * math.sin(angle_outer)}")
        points.append(f"{cx + r_inner * math.cos(angle_inner)},{cy + r_inner * math.sin(angle_inner)}")
    return f'<polygon points="{" ".join(points)}" fill="{colour}" stroke="{stroke}" stroke-width="2"/>'

def svg_heart(x, y, size=60, colour='#E74C3C', stroke='#C0392B'):
    """Generate a heart"""
    scale = size / 50
    return f'''<g transform="translate({x},{y}) scale({scale})">
        <path d="M25,45 L5,25 C0,20 0,8 12,8 C18,8 25,14 25,20 C25,14 32,8 38,8 C50,8 50,20 45,25 Z" 
              fill="{colour}" stroke="{stroke}" stroke-width="2"/>
    </g>'''

# =============================================================================
# SVG GENERATION FUNCTIONS - 3D SHAPES
# =============================================================================

def svg_sphere(x, y, size=60, colour='#3498DB'):
    """Generate a sphere (ball)"""
    return f'''<g transform="translate({x},{y})">
        <circle cx="{size//2}" cy="{size//2}" r="{size//2 - 2}" fill="{colour}"/>
        <ellipse cx="{size//3}" cy="{size//3}" rx="{size//6}" ry="{size//8}" fill="white" opacity="0.4"/>
    </g>'''

def svg_cube(x, y, size=60, colour='#E74C3C'):
    """Generate a cube (box)"""
    offset = size // 4
    # Front face
    front = f'<rect x="{x}" y="{y + offset}" width="{size - offset}" height="{size - offset}" fill="{colour}" stroke="#333" stroke-width="1"/>'
    # Top face
    top_points = f"{x},{y + offset} {x + offset},{y} {x + size},{y} {x + size - offset},{y + offset}"
    top = f'<polygon points="{top_points}" fill="{COLOURS["orange"]}" stroke="#333" stroke-width="1"/>'
    # Side face
    side_points = f"{x + size - offset},{y + offset} {x + size},{y} {x + size},{y + size - offset} {x + size - offset},{y + size}"
    side = f'<polygon points="{side_points}" fill="{COLOURS["yellow"]}" stroke="#333" stroke-width="1"/>'
    return front + top + side

def svg_cylinder(x, y, size=60, colour='#27AE60'):
    """Generate a cylinder (can)"""
    width = size * 0.8
    height = size
    cx = x + size//2
    # Body
    body = f'<rect x="{x + size//10}" y="{y + size//6}" width="{width}" height="{height * 0.7}" fill="{colour}" stroke="#333" stroke-width="1"/>'
    # Top ellipse
    top = f'<ellipse cx="{cx}" cy="{y + size//6}" rx="{width//2}" ry="{size//8}" fill="{COLOURS["green"]}" stroke="#333" stroke-width="1"/>'
    # Bottom ellipse (partial)
    bottom = f'<ellipse cx="{cx}" cy="{y + size//6 + height * 0.7}" rx="{width//2}" ry="{size//8}" fill="{colour}" stroke="#333" stroke-width="1"/>'
    return body + bottom + top

def svg_cone(x, y, size=60, colour='#F1C40F'):
    """Generate a cone"""
    cx = x + size//2
    # Triangle body
    points = f"{cx},{y + 5} {x + 5},{y + size - 10} {x + size - 5},{y + size - 10}"
    body = f'<polygon points="{points}" fill="{colour}" stroke="#333" stroke-width="1"/>'
    # Base ellipse
    base = f'<ellipse cx="{cx}" cy="{y + size - 10}" rx="{size//2 - 5}" ry="{size//8}" fill="{COLOURS["orange"]}" stroke="#333" stroke-width="1"/>'
    return body + base

def svg_pyramid(x, y, size=60, colour='#9B59B6'):
    """Generate a pyramid"""
    cx = x + size//2
    # Front face
    front_points = f"{cx},{y + 5} {x + 5},{y + size - 5} {x + size - 5},{y + size - 5}"
    front = f'<polygon points="{front_points}" fill="{colour}" stroke="#333" stroke-width="1"/>'
    # Side faces indicated by lines
    line = f'<line x1="{cx}" y1="{y + 5}" x2="{cx}" y2="{y + size - 5}" stroke="#333" stroke-width="1"/>'
    return front + line

# =============================================================================
# SVG HELPER FUNCTIONS
# =============================================================================

def get_2d_shape_svg(shape, x, y, size=60, colour=None):
    """Get SVG for a 2D shape"""
    default_colours = {
        'circle': '#3498DB',
        'square': '#E74C3C', 
        'triangle': '#F1C40F',
        'rectangle': '#27AE60',
        'oval': '#9B59B6',
        'diamond': '#E67E22',
        'star': '#F1C40F',
        'heart': '#E74C3C'
    }
    
    c = colour or default_colours.get(shape, '#3498DB')
    
    if shape == 'circle':
        return svg_circle(x, y, size, c)
    elif shape == 'square':
        return svg_square(x, y, size, c)
    elif shape == 'triangle':
        return svg_triangle(x, y, size, c)
    elif shape == 'rectangle':
        return svg_rectangle(x, y, size + 20, size - 10, c)
    elif shape == 'oval':
        return svg_oval(x, y, size + 10, size - 15, c)
    elif shape == 'diamond':
        return svg_diamond(x, y, size, c)
    elif shape == 'star':
        return svg_star(x, y, size, c)
    elif shape == 'heart':
        return svg_heart(x, y, size, c)
    return svg_circle(x, y, size, c)

def get_3d_shape_svg(shape, x, y, size=60, colour=None):
    """Get SVG for a 3D shape"""
    default_colours = {
        'sphere': '#3498DB',
        'cube': '#E74C3C',
        'cylinder': '#27AE60',
        'cone': '#F1C40F',
        'pyramid': '#9B59B6'
    }
    
    c = colour or default_colours.get(shape, '#3498DB')
    
    if shape == 'sphere' or shape == 'ball':
        return svg_sphere(x, y, size, c)
    elif shape == 'cube' or shape == 'box':
        return svg_cube(x, y, size, c)
    elif shape == 'cylinder' or shape == 'can':
        return svg_cylinder(x, y, size, c)
    elif shape == 'cone':
        return svg_cone(x, y, size, c)
    elif shape == 'pyramid':
        return svg_pyramid(x, y, size, c)
    return svg_sphere(x, y, size, c)

def create_svg_wrapper(content, width=400, height=180):
    """Wrap SVG content"""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background: white;">{content}</svg>'

def create_position_scene(position, obj_type='ball'):
    """Create SVG showing position relationship"""
    width, height = 350, 180
    svg_content = ''
    
    # Reference object (box/table)
    box_x, box_y = 140, 80
    box_w, box_h = 80, 50
    svg_content += f'<rect x="{box_x}" y="{box_y}" width="{box_w}" height="{box_h}" fill="#8B4513" stroke="#5D3A1A" stroke-width="2" rx="3"/>'
    svg_content += f'<text x="{box_x + box_w//2}" y="{box_y + box_h + 20}" text-anchor="middle" font-size="12" fill="#333">box</text>'
    
    # Position the ball based on position word
    ball_size = 30
    if position == 'on':
        ball_x, ball_y = box_x + box_w//2 - ball_size//2, box_y - ball_size
    elif position == 'under':
        ball_x, ball_y = box_x + box_w//2 - ball_size//2, box_y + box_h + 10
    elif position == 'in':
        ball_x, ball_y = box_x + box_w//2 - ball_size//2, box_y + 10
    elif position == 'beside' or position == 'next to':
        ball_x, ball_y = box_x + box_w + 20, box_y + box_h//2 - ball_size//2
    elif position == 'behind':
        ball_x, ball_y = box_x - ball_size - 10, box_y - 10
        svg_content += f'<circle cx="{ball_x + ball_size//2}" cy="{ball_y + ball_size//2}" r="{ball_size//2}" fill="#3498DB" opacity="0.5"/>'
        svg_content += f'<text x="{175}" y="{30}" text-anchor="middle" font-size="14" fill="#333">The ball is {position} the box</text>'
        return create_svg_wrapper(svg_content, width, height)
    elif position == 'in front of':
        ball_x, ball_y = box_x + box_w + 30, box_y + box_h//2 - ball_size//2
    else:
        ball_x, ball_y = box_x + box_w//2 - ball_size//2, box_y - ball_size
    
    svg_content += f'<circle cx="{ball_x + ball_size//2}" cy="{ball_y + ball_size//2}" r="{ball_size//2}" fill="#3498DB"/>'
    svg_content += f'<text x="{175}" y="{30}" text-anchor="middle" font-size="14" fill="#333">The ball is {position} the box</text>'
    
    return create_svg_wrapper(svg_content, width, height)

def create_movement_scene(direction):
    """Create SVG showing movement direction"""
    width, height = 350, 150
    svg_content = ''
    
    # Arrow showing direction
    cx, cy = 175, 75
    arrow_len = 50
    
    if direction == 'up':
        svg_content += f'<line x1="{cx}" y1="{cy + arrow_len//2}" x2="{cx}" y2="{cy - arrow_len//2}" stroke="#27AE60" stroke-width="8"/>'
        svg_content += f'<polygon points="{cx},{cy - arrow_len//2 - 10} {cx - 15},{cy - arrow_len//2 + 10} {cx + 15},{cy - arrow_len//2 + 10}" fill="#27AE60"/>'
    elif direction == 'down':
        svg_content += f'<line x1="{cx}" y1="{cy - arrow_len//2}" x2="{cx}" y2="{cy + arrow_len//2}" stroke="#E74C3C" stroke-width="8"/>'
        svg_content += f'<polygon points="{cx},{cy + arrow_len//2 + 10} {cx - 15},{cy + arrow_len//2 - 10} {cx + 15},{cy + arrow_len//2 - 10}" fill="#E74C3C"/>'
    elif direction == 'left':
        svg_content += f'<line x1="{cx + arrow_len//2}" y1="{cy}" x2="{cx - arrow_len//2}" y2="{cy}" stroke="#3498DB" stroke-width="8"/>'
        svg_content += f'<polygon points="{cx - arrow_len//2 - 10},{cy} {cx - arrow_len//2 + 10},{cy - 15} {cx - arrow_len//2 + 10},{cy + 15}" fill="#3498DB"/>'
    elif direction == 'right':
        svg_content += f'<line x1="{cx - arrow_len//2}" y1="{cy}" x2="{cx + arrow_len//2}" y2="{cy}" stroke="#9B59B6" stroke-width="8"/>'
        svg_content += f'<polygon points="{cx + arrow_len//2 + 10},{cy} {cx + arrow_len//2 - 10},{cy - 15} {cx + arrow_len//2 - 10},{cy + 15}" fill="#9B59B6"/>'
    elif direction == 'forward':
        svg_content += f'<ellipse cx="{cx}" cy="{cy}" rx="30" ry="15" fill="none" stroke="#F1C40F" stroke-width="4"/>'
        svg_content += f'<polygon points="{cx + 30},{cy} {cx + 45},{cy - 10} {cx + 45},{cy + 10}" fill="#F1C40F"/>'
    elif direction == 'backward':
        svg_content += f'<ellipse cx="{cx}" cy="{cy}" rx="30" ry="15" fill="none" stroke="#E67E22" stroke-width="4"/>'
        svg_content += f'<polygon points="{cx - 30},{cy} {cx - 45},{cy - 10} {cx - 45},{cy + 10}" fill="#E67E22"/>'
    
    svg_content += f'<text x="{cx}" y="{140}" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">{direction.upper()}</text>'
    
    return create_svg_wrapper(svg_content, width, height)

# =============================================================================
# QUESTION GENERATORS BY LEVEL
# =============================================================================

def generate_level_1_questions():
    """Level 1: Position Words - in, on, under (2 options)"""
    questions = []
    
    positions = ['on', 'under', 'in']
    
    for i in range(QUESTIONS_PER_LEVEL):
        correct_pos = random.choice(positions)
        wrong_pos = random.choice([p for p in positions if p != correct_pos])
        
        svg = create_position_scene(correct_pos)
        
        options = [correct_pos.title(), wrong_pos.title()]
        random.shuffle(options)
        
        questions.append({
            'question_text': 'Where is the ball?',
            'options': json.dumps(options),
            'correct_answer': correct_pos.title(),
            'explanation': f'The ball is {correct_pos} the box!',
            'visual_data': svg
        })
    
    return questions

def generate_level_2_questions():
    """Level 2: Movement Words - up, down, left, right (2-3 options)"""
    questions = []
    
    directions = ['up', 'down', 'left', 'right']
    
    for i in range(QUESTIONS_PER_LEVEL):
        correct_dir = random.choice(directions)
        wrong_dirs = [d for d in directions if d != correct_dir]
        
        svg = create_movement_scene(correct_dir)
        
        if i % 2 == 0:
            options = [correct_dir.title(), wrong_dirs[0].title()]
        else:
            options = [correct_dir.title(), wrong_dirs[0].title(), wrong_dirs[1].title()]
        random.shuffle(options)
        
        questions.append({
            'question_text': 'Which direction is the arrow pointing?',
            'options': json.dumps(options),
            'correct_answer': correct_dir.title(),
            'explanation': f'The arrow is pointing {correct_dir}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_3_questions():
    """Level 3: Circle & Square - Recognise basic shapes (3 options)"""
    questions = []
    
    shapes = ['circle', 'square']
    
    for i in range(QUESTIONS_PER_LEVEL):
        target_shape = random.choice(shapes)
        colour = random.choice(list(COLOURS.values()))
        
        svg_content = get_2d_shape_svg(target_shape, 170, 50, 80, colour)
        svg = create_svg_wrapper(svg_content)
        
        options = ['Circle', 'Square', 'Triangle']
        random.shuffle(options)
        
        if target_shape == 'circle':
            explanation = 'This is a circle - it\'s perfectly round with no corners!'
        else:
            explanation = 'This is a square - it has 4 equal sides and 4 corners!'
        
        questions.append({
            'question_text': 'What shape is this?',
            'options': json.dumps(options),
            'correct_answer': target_shape.title(),
            'explanation': explanation,
            'visual_data': svg
        })
    
    return questions

def generate_level_4_questions():
    """Level 4: Triangle & Rectangle - More 2D shapes (3 options)"""
    questions = []
    
    shapes = ['triangle', 'rectangle']
    
    for i in range(QUESTIONS_PER_LEVEL):
        target_shape = random.choice(shapes)
        colour = random.choice(list(COLOURS.values()))
        
        svg_content = get_2d_shape_svg(target_shape, 160, 50, 80, colour)
        svg = create_svg_wrapper(svg_content)
        
        options = ['Triangle', 'Rectangle', 'Circle']
        random.shuffle(options)
        
        if target_shape == 'triangle':
            explanation = 'This is a triangle - it has 3 sides and 3 corners!'
        else:
            explanation = 'This is a rectangle - it has 4 sides and 4 corners, with 2 long sides and 2 short sides!'
        
        questions.append({
            'question_text': 'What shape is this?',
            'options': json.dumps(options),
            'correct_answer': target_shape.title(),
            'explanation': explanation,
            'visual_data': svg
        })
    
    return questions

def generate_level_5_questions():
    """Level 5: Shapes Around Us - Real-world shape recognition (4 options)"""
    questions = []
    
    real_world_shapes = [
        ('circle', 'wheel', 'A wheel is a circle!'),
        ('circle', 'clock face', 'A clock face is a circle!'),
        ('circle', 'pizza', 'A pizza is a circle!'),
        ('square', 'window', 'Many windows are squares!'),
        ('square', 'cracker', 'A cracker is often a square!'),
        ('rectangle', 'door', 'A door is a rectangle!'),
        ('rectangle', 'book', 'A book is a rectangle!'),
        ('rectangle', 'phone', 'A phone is a rectangle!'),
        ('triangle', 'roof', 'A roof is often a triangle shape!'),
        ('triangle', 'pizza slice', 'A pizza slice is a triangle!'),
        ('triangle', 'sail', 'A sail can be a triangle!')
    ]
    
    for i in range(QUESTIONS_PER_LEVEL):
        shape, obj, explanation = random.choice(real_world_shapes)
        
        svg_content = f'<text x="200" y="70" text-anchor="middle" font-size="18" fill="#333">What shape is a</text>'
        svg_content += f'<text x="200" y="100" text-anchor="middle" font-size="24" font-weight="bold" fill="#3498DB">{obj}</text>'
        svg_content += f'<text x="200" y="130" text-anchor="middle" font-size="18" fill="#333">?</text>'
        svg = create_svg_wrapper(svg_content)
        
        options = ['Circle', 'Square', 'Triangle', 'Rectangle']
        random.shuffle(options)
        
        questions.append({
            'question_text': f'What shape is a {obj}?',
            'options': json.dumps(options),
            'correct_answer': shape.title(),
            'explanation': explanation,
            'visual_data': svg
        })
    
    return questions

def generate_level_6_questions():
    """Level 6: 3D Shapes Intro - Flat vs Solid (4 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        if i % 2 == 0:
            # Show 3D shape, ask if flat or solid
            shapes_3d = ['sphere', 'cube', 'cylinder']
            shape = random.choice(shapes_3d)
            
            svg_content = get_3d_shape_svg(shape, 160, 50, 70)
            svg = create_svg_wrapper(svg_content)
            
            options = ['Solid (3D)', 'Flat (2D)', 'Not sure', 'Neither']
            
            questions.append({
                'question_text': 'Is this shape flat or solid?',
                'options': json.dumps(options),
                'correct_answer': 'Solid (3D)',
                'explanation': f'This is a {shape} - it\'s solid (3D). You can hold it in your hand!',
                'visual_data': svg
            })
        else:
            # Show 2D shape, ask if flat or solid
            shapes_2d = ['circle', 'square', 'triangle']
            shape = random.choice(shapes_2d)
            
            svg_content = get_2d_shape_svg(shape, 165, 50, 70)
            svg = create_svg_wrapper(svg_content)
            
            options = ['Flat (2D)', 'Solid (3D)', 'Not sure', 'Neither']
            
            questions.append({
                'question_text': 'Is this shape flat or solid?',
                'options': json.dumps(options),
                'correct_answer': 'Flat (2D)',
                'explanation': f'This is a {shape} - it\'s flat (2D). It\'s like a drawing!',
                'visual_data': svg
            })
    
    return questions

def generate_level_7_questions():
    """Level 7: Ball, Box, Can - Name 3D shapes (4 options)"""
    questions = []
    
    shape_info = [
        ('sphere', 'Ball', 'This is a sphere - like a ball! It\'s round all over.'),
        ('cube', 'Box', 'This is a cube - like a box! It has 6 square faces.'),
        ('cylinder', 'Can', 'This is a cylinder - like a can! It\'s round with flat ends.')
    ]
    
    for i in range(QUESTIONS_PER_LEVEL):
        shape, common_name, explanation = random.choice(shape_info)
        
        svg_content = get_3d_shape_svg(shape, 160, 50, 70)
        svg = create_svg_wrapper(svg_content)
        
        options = ['Ball (Sphere)', 'Box (Cube)', 'Can (Cylinder)', 'Cone']
        random.shuffle(options)
        
        correct = f'{common_name} ({shape.title()})'
        
        questions.append({
            'question_text': 'What 3D shape is this?',
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': explanation,
            'visual_data': svg
        })
    
    return questions

def generate_level_8_questions():
    """Level 8: Sorting Shapes - Sort by properties (4 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        sort_type = random.choice(['corners', 'sides', 'curved'])
        
        if sort_type == 'corners':
            # Which has 3 corners?
            svg_content = get_2d_shape_svg('circle', 50, 60, 50)
            svg_content += get_2d_shape_svg('square', 130, 60, 50)
            svg_content += get_2d_shape_svg('triangle', 210, 60, 50)
            svg_content += get_2d_shape_svg('rectangle', 280, 60, 50)
            svg = create_svg_wrapper(svg_content)
            
            corners = random.choice([3, 4, 0])
            if corners == 3:
                correct = 'Triangle'
                question = 'Which shape has 3 corners?'
            elif corners == 4:
                correct = random.choice(['Square', 'Rectangle'])
                question = 'Which shape has 4 corners?'
            else:
                correct = 'Circle'
                question = 'Which shape has NO corners?'
            
            options = ['Circle', 'Square', 'Triangle', 'Rectangle']
            random.shuffle(options)
            
        elif sort_type == 'sides':
            svg_content = get_2d_shape_svg('triangle', 80, 60, 55)
            svg_content += get_2d_shape_svg('square', 180, 60, 55)
            svg_content += get_2d_shape_svg('circle', 280, 60, 55)
            svg = create_svg_wrapper(svg_content)
            
            sides = random.choice([3, 4])
            if sides == 3:
                correct = 'Triangle'
                question = 'Which shape has 3 sides?'
            else:
                correct = 'Square'
                question = 'Which shape has 4 sides?'
            
            options = ['Triangle', 'Square', 'Circle', 'Star']
            random.shuffle(options)
            
        else:  # curved
            svg_content = get_2d_shape_svg('circle', 80, 60, 55)
            svg_content += get_2d_shape_svg('oval', 175, 65, 55)
            svg_content += get_2d_shape_svg('square', 280, 60, 55)
            svg = create_svg_wrapper(svg_content)
            
            question = 'Which shapes have curved edges?'
            correct = 'Circle and Oval'
            options = ['Circle and Oval', 'Square only', 'All of them', 'None of them']
            random.shuffle(options)
        
        questions.append({
            'question_text': question,
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': f'{correct} is correct!',
            'visual_data': svg
        })
    
    return questions

def generate_level_9_questions():
    """Level 9: Shapes in Life - Connect shapes to objects (4 options)"""
    questions = []
    
    shape_objects = {
        'circle': ['clock', 'wheel', 'pizza', 'coin', 'plate'],
        'square': ['window', 'tile', 'cracker', 'dice face', 'sticky note'],
        'rectangle': ['door', 'book', 'phone', 'TV screen', 'envelope'],
        'triangle': ['roof', 'pizza slice', 'yield sign', 'tent', 'sandwich half'],
        'sphere': ['ball', 'orange', 'globe', 'marble', 'bubble'],
        'cube': ['dice', 'box', 'ice cube', 'sugar cube', 'building block'],
        'cylinder': ['can', 'glass', 'candle', 'roll of paper', 'battery']
    }
    
    for i in range(QUESTIONS_PER_LEVEL):
        shape = random.choice(list(shape_objects.keys()))
        obj = random.choice(shape_objects[shape])
        
        # Show the shape
        if shape in ['sphere', 'cube', 'cylinder']:
            svg_content = get_3d_shape_svg(shape, 160, 50, 70)
        else:
            svg_content = get_2d_shape_svg(shape, 165, 50, 70)
        svg = create_svg_wrapper(svg_content)
        
        # Get wrong answers
        wrong_objects = []
        for s, objs in shape_objects.items():
            if s != shape:
                wrong_objects.extend(objs)
        
        options = [obj.title()] + [o.title() for o in random.sample(wrong_objects, 3)]
        random.shuffle(options)
        
        questions.append({
            'question_text': f'Which real object is shaped like this {shape}?',
            'options': json.dumps(options),
            'correct_answer': obj.title(),
            'explanation': f'A {obj} is shaped like a {shape}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_10_questions():
    """Level 10: Sides & Corners - Count shape properties (4 options)"""
    questions = []
    
    shape_properties = {
        'circle': {'sides': 0, 'corners': 0},
        'triangle': {'sides': 3, 'corners': 3},
        'square': {'sides': 4, 'corners': 4},
        'rectangle': {'sides': 4, 'corners': 4},
        'pentagon': {'sides': 5, 'corners': 5},
        'hexagon': {'sides': 6, 'corners': 6}
    }
    
    for i in range(QUESTIONS_PER_LEVEL):
        shape = random.choice(['circle', 'triangle', 'square', 'rectangle'])
        prop = random.choice(['sides', 'corners'])
        correct_count = shape_properties[shape][prop]
        
        svg_content = get_2d_shape_svg(shape, 165, 50, 70)
        svg = create_svg_wrapper(svg_content)
        
        if correct_count == 0:
            options = ['0', '1', '2', '4']
        else:
            options = [str(correct_count), str(correct_count + 1), str(correct_count - 1), str(correct_count + 2)]
            options = list(set(options))
            while len(options) < 4:
                options.append(str(random.randint(1, 6)))
            options = options[:4]
        random.shuffle(options)
        
        questions.append({
            'question_text': f'How many {prop} does this {shape} have?',
            'options': json.dumps(options),
            'correct_answer': str(correct_count),
            'explanation': f'A {shape} has {correct_count} {prop}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_11_questions():
    """Level 11: Describing Shapes - Use words to describe (4 options)"""
    questions = []
    
    descriptions = [
        ('circle', 'round', 'A circle is round with no corners!'),
        ('circle', 'no corners', 'A circle has no corners - it\'s curved all the way around!'),
        ('square', '4 equal sides', 'A square has 4 equal sides!'),
        ('square', '4 corners', 'A square has 4 corners!'),
        ('triangle', '3 sides', 'A triangle has 3 sides!'),
        ('triangle', '3 corners', 'A triangle has 3 corners!'),
        ('rectangle', '2 long and 2 short sides', 'A rectangle has 2 long sides and 2 short sides!'),
        ('sphere', 'round like a ball', 'A sphere is round like a ball - no flat parts!'),
        ('cube', '6 square faces', 'A cube has 6 square faces!'),
        ('cylinder', 'round with flat ends', 'A cylinder is round with 2 flat circular ends!')
    ]
    
    for i in range(QUESTIONS_PER_LEVEL):
        shape, desc, explanation = random.choice(descriptions)
        
        if shape in ['sphere', 'cube', 'cylinder']:
            svg_content = get_3d_shape_svg(shape, 160, 50, 70)
        else:
            svg_content = get_2d_shape_svg(shape, 165, 50, 70)
        svg = create_svg_wrapper(svg_content)
        
        # Create wrong descriptions
        wrong_descs = [d[1] for d in descriptions if d[0] != shape]
        wrong_options = random.sample(wrong_descs, 3)
        
        options = [desc] + wrong_options
        random.shuffle(options)
        
        questions.append({
            'question_text': f'Which describes this {shape}?',
            'options': json.dumps(options),
            'correct_answer': desc,
            'explanation': explanation,
            'visual_data': svg
        })
    
    return questions

def generate_level_12_questions():
    """Level 12: Shape Challenge - Mixed shape problems (4 options)"""
    questions = []
    
    challenge_types = ['identify_2d', 'identify_3d', 'count_property', 'real_world', 'position', 'compare']
    
    for i in range(QUESTIONS_PER_LEVEL):
        c_type = challenge_types[i % len(challenge_types)]
        
        if c_type == 'identify_2d':
            shapes = ['circle', 'square', 'triangle', 'rectangle']
            shape = random.choice(shapes)
            colour = random.choice(list(COLOURS.values()))
            
            svg_content = get_2d_shape_svg(shape, 165, 50, 70, colour)
            svg = create_svg_wrapper(svg_content)
            
            options = [s.title() for s in shapes]
            random.shuffle(options)
            
            questions.append({
                'question_text': 'What shape is this?',
                'options': json.dumps(options),
                'correct_answer': shape.title(),
                'explanation': f'This is a {shape}!',
                'visual_data': svg
            })
            
        elif c_type == 'identify_3d':
            shapes = ['sphere', 'cube', 'cylinder']
            shape = random.choice(shapes)
            
            svg_content = get_3d_shape_svg(shape, 160, 50, 70)
            svg = create_svg_wrapper(svg_content)
            
            common_names = {'sphere': 'Ball', 'cube': 'Box', 'cylinder': 'Can'}
            options = [f'{common_names[s]} ({s.title()})' for s in shapes] + ['Cone']
            random.shuffle(options)
            
            correct = f'{common_names[shape]} ({shape.title()})'
            
            questions.append({
                'question_text': 'What 3D shape is this?',
                'options': json.dumps(options),
                'correct_answer': correct,
                'explanation': f'This is a {shape}!',
                'visual_data': svg
            })
            
        elif c_type == 'count_property':
            shape = random.choice(['triangle', 'square', 'rectangle'])
            prop = random.choice(['sides', 'corners'])
            counts = {'triangle': 3, 'square': 4, 'rectangle': 4}
            correct = counts[shape]
            
            svg_content = get_2d_shape_svg(shape, 165, 50, 70)
            svg = create_svg_wrapper(svg_content)
            
            options = [str(correct), str(correct+1), str(correct-1), '0']
            random.shuffle(options)
            
            questions.append({
                'question_text': f'How many {prop} does this shape have?',
                'options': json.dumps(options),
                'correct_answer': str(correct),
                'explanation': f'This {shape} has {correct} {prop}!',
                'visual_data': svg
            })
            
        elif c_type == 'real_world':
            pairs = [('circle', 'pizza'), ('square', 'window'), ('rectangle', 'door'), ('triangle', 'roof')]
            shape, obj = random.choice(pairs)
            
            svg_content = f'<text x="200" y="90" text-anchor="middle" font-size="20" fill="#333">{obj.title()}</text>'
            svg = create_svg_wrapper(svg_content)
            
            options = ['Circle', 'Square', 'Rectangle', 'Triangle']
            random.shuffle(options)
            
            questions.append({
                'question_text': f'What shape is a {obj}?',
                'options': json.dumps(options),
                'correct_answer': shape.title(),
                'explanation': f'A {obj} is a {shape} shape!',
                'visual_data': svg
            })
            
        elif c_type == 'position':
            positions = ['on', 'under', 'beside']
            pos = random.choice(positions)
            
            svg = create_position_scene(pos)
            
            options = ['On', 'Under', 'Beside', 'In']
            random.shuffle(options)
            
            questions.append({
                'question_text': 'Where is the ball?',
                'options': json.dumps(options),
                'correct_answer': pos.title(),
                'explanation': f'The ball is {pos} the box!',
                'visual_data': svg
            })
            
        else:  # compare
            shape1 = random.choice(['circle', 'square'])
            shape2 = random.choice(['triangle', 'rectangle'])
            
            svg_content = get_2d_shape_svg(shape1, 100, 60, 60)
            svg_content += get_2d_shape_svg(shape2, 240, 60, 60)
            svg = create_svg_wrapper(svg_content)
            
            corners1 = 0 if shape1 == 'circle' else 4
            corners2 = 3 if shape2 == 'triangle' else 4
            
            if corners1 + corners2 <= 4:
                question = 'How many corners in total?'
                correct = str(corners1 + corners2)
            else:
                question = 'Which shape has more corners?'
                correct = shape1.title() if corners1 > corners2 else shape2.title()
            
            options = [correct, str(corners1), str(corners2), 'Same']
            options = list(set(options))[:4]
            random.shuffle(options)
            
            questions.append({
                'question_text': question,
                'options': json.dumps(options),
                'correct_answer': correct,
                'explanation': f'The answer is {correct}!',
                'visual_data': svg
            })
    
    return questions

# =============================================================================
# MAIN GENERATION AND DATABASE FUNCTIONS
# =============================================================================

def generate_all_questions():
    """Generate all questions for all levels"""
    all_questions = []
    
    generators = [
        (1, generate_level_1_questions),
        (2, generate_level_2_questions),
        (3, generate_level_3_questions),
        (4, generate_level_4_questions),
        (5, generate_level_5_questions),
        (6, generate_level_6_questions),
        (7, generate_level_7_questions),
        (8, generate_level_8_questions),
        (9, generate_level_9_questions),
        (10, generate_level_10_questions),
        (11, generate_level_11_questions),
        (12, generate_level_12_questions),
    ]
    
    for level, generator in generators:
        print(f"  Generating Level {level}...")
        questions = generator()
        for q in questions:
            q['level'] = level
            q['topic'] = TOPIC
            q['mode'] = MODE
        all_questions.extend(questions)
        print(f"    ✓ {len(questions)} questions generated")
    
    return all_questions

def validate_questions(questions):
    """Validate all questions before insertion"""
    print(f"\nValidating {len(questions)} questions...")
    
    errors = []
    for i, q in enumerate(questions):
        required = ['question_text', 'options', 'correct_answer', 'level', 'topic', 'mode']
        for field in required:
            if field not in q or not q[field]:
                errors.append(f"Question {i}: Missing {field}")
        
        try:
            options = json.loads(q['options'])
            if q['correct_answer'] not in options:
                errors.append(f"Question {i}: Correct answer '{q['correct_answer']}' not in options {options}")
        except:
            errors.append(f"Question {i}: Invalid options JSON")
    
    if errors:
        print(f"  ✗ Found {len(errors)} errors:")
        for e in errors[:10]:
            print(f"    - {e}")
        if len(errors) > 10:
            print(f"    ... and {len(errors) - 10} more")
        return False
    
    print(f"  ✓ All questions valid")
    return True

def insert_questions(questions):
    """Insert questions into database"""
    print(f"\nInserting {len(questions)} questions into database...")
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        DELETE FROM questions_adaptive 
        WHERE topic = ? AND mode = ?
    ''', (TOPIC, MODE))
    deleted = cursor.rowcount
    print(f"  Removed {deleted} existing questions")
    
    inserted = 0
    for q in questions:
        try:
            cursor.execute('''
                INSERT INTO questions_adaptive 
                (topic, mode, difficulty_level, question_text, options, correct_answer, explanation, visual_data)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                q['topic'],
                q['mode'],
                q['level'],
                q['question_text'],
                q['options'],
                q['correct_answer'],
                q.get('explanation', ''),
                q.get('visual_data', '')
            ))
            inserted += 1
        except Exception as e:
            print(f"  Error inserting question: {e}")
    
    conn.commit()
    conn.close()
    
    print(f"  ✓ Inserted {inserted} questions")
    return inserted

def verify_insertion():
    """Verify questions were inserted correctly"""
    print(f"\nVerifying insertion...")
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT difficulty_level, COUNT(*) 
        FROM questions_adaptive 
        WHERE topic = ? AND mode = ?
        GROUP BY difficulty_level
        ORDER BY difficulty_level
    ''', (TOPIC, MODE))
    
    results = cursor.fetchall()
    conn.close()
    
    print(f"\n  Questions per level:")
    total = 0
    for level, count in results:
        status = "✓" if count == QUESTIONS_PER_LEVEL else "✗"
        print(f"    Level {level}: {count} {status}")
        total += count
    
    print(f"\n  Total: {total} questions")
    expected = QUESTIONS_PER_LEVEL * TOTAL_LEVELS
    if total == expected:
        print(f"  ✓ Perfect! Expected {expected}, got {total}")
    else:
        print(f"  ✗ Mismatch! Expected {expected}, got {total}")
    
    return total == expected

# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print(f"AgentMath L1LP Question Generator")
    print(f"Topic: {TOPIC}")
    print(f"Mode: {MODE}")
    print("=" * 60)
    
    print(f"\nGenerating questions...")
    questions = generate_all_questions()
    
    if not validate_questions(questions):
        print("\n✗ Validation failed. Aborting.")
        exit(1)
    
    insert_questions(questions)
    success = verify_insertion()
    
    print("\n" + "=" * 60)
    if success:
        print("✓ COMPLETE! All questions generated successfully.")
    else:
        print("✗ INCOMPLETE. Please check errors above.")
    print("=" * 60)
