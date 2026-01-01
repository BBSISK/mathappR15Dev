#!/usr/bin/env python3
"""
AgentMath - Speed, Distance, Time Question Generator
SEC Junior Cycle Aligned - JC Exam Mode

Based on SEC Papers 2022-2025:
- 2022 OL Q3(b): Farah swims 250m in 5 mins. Average speed in m/min.
- 2022 HL Q10: Rachel runs from home - when 8km? Brendan catches up?
- 2023 HL Q8(c)(ii): Flight 360km in 45 mins. Speed in km/h.
- 2024 OL Q4: 60km in 45 mins by car. Speed in km/h.
- 2025 OL Q13(a): Tadhg cycles 3km in 10 mins. Speed in km/h.
- 2025 OL Q13(b): Distance-time graph interpretation.

Level Structure:
  L1-3:   Foundation (basic formula, simple calculations)
  L4-6:   Ordinary (unit conversions, time in minutes)
  L7-9:   Higher (graphs, multi-step, meeting problems)
  L10-12: Application/Mastery (complex problems, real-world)

Target: 600 questions (50 per level)
"""

import random
import sqlite3
import os
from decimal import Decimal, ROUND_HALF_UP

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'speed_distance_time'
MODE = 'jc_exam'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'

# Irish names for word problems
IRISH_NAMES = ['Aoife', 'Cian', 'Niamh', 'Oisín', 'Saoirse', 'Conor', 'Róisín', 'Seán', 
               'Ciara', 'Darragh', 'Éabha', 'Fionn', 'Gráinne', 'Liam', 'Meadhbh', 'Tadhg',
               'Áine', 'Cillian', 'Orlaith', 'Pádraig', 'Sinéad', 'Eoin', 'Caoimhe', 'Declan',
               'Rachel', 'Brendan', 'Farah', 'Emma', 'Jack', 'Sophie', 'Dylan', 'Katie']

# Irish places
IRISH_TOWNS = ['Dublin', 'Cork', 'Galway', 'Limerick', 'Waterford', 'Kilkenny', 
               'Sligo', 'Tralee', 'Athlone', 'Dundalk', 'Drogheda', 'Wexford']

# Transport modes
TRANSPORT = ['car', 'bus', 'train', 'bike', 'walk', 'run', 'cycle', 'drive']

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def round_val(value, decimals=2):
    """Round to specified decimal places"""
    return float(Decimal(str(value)).quantize(Decimal(f'0.{"0"*decimals}'), rounding=ROUND_HALF_UP))

def format_speed(value, unit='km/h'):
    """Format speed with unit"""
    rounded = round_val(value)
    if rounded == int(rounded):
        return f"{int(rounded)} {unit}"
    return f"{rounded} {unit}"

def format_distance(value, unit='km'):
    """Format distance with unit"""
    rounded = round_val(value)
    if rounded == int(rounded):
        return f"{int(rounded)} {unit}"
    return f"{rounded} {unit}"

def format_time_hours(hours):
    """Format time in hours and minutes"""
    if hours == int(hours):
        return f"{int(hours)} hour{'s' if hours != 1 else ''}"
    
    whole_hours = int(hours)
    mins = round((hours - whole_hours) * 60)
    
    if whole_hours == 0:
        return f"{mins} minutes"
    elif mins == 0:
        return f"{whole_hours} hour{'s' if whole_hours != 1 else ''}"
    else:
        return f"{whole_hours} hour{'s' if whole_hours != 1 else ''} {mins} minutes"

def mins_to_hours(mins):
    """Convert minutes to hours as decimal"""
    return mins / 60

def get_unique_wrong(correct_val, count=3, format_func=str):
    """Generate unique wrong options"""
    wrong = set()
    
    candidates = [
        correct_val * 1.5, correct_val * 2, correct_val / 2,
        correct_val + 5, correct_val - 5, correct_val + 10,
        correct_val * 0.8, correct_val * 1.2, correct_val + 2,
        correct_val - 2, correct_val * 3, correct_val / 3
    ]
    
    for c in candidates:
        if c > 0 and round_val(c) != round_val(correct_val) and len(wrong) < count:
            wrong.add(round_val(c))
    
    while len(wrong) < count:
        w = round_val(random.uniform(max(1, correct_val * 0.3), correct_val * 3))
        if w > 0 and w != round_val(correct_val) and w not in wrong:
            wrong.add(w)
    
    return [format_func(w) for w in list(wrong)[:count]]

def make_options(correct, wrong_list):
    """Create 4 unique options with correct answer included"""
    correct_str = str(correct)
    unique_wrong = [str(w) for w in wrong_list if str(w) != correct_str]
    seen = set()
    unique_wrong = [w for w in unique_wrong if not (w in seen or seen.add(w))]
    
    options = [correct_str] + unique_wrong[:3]
    
    counter = 1
    while len(set(options)) < 4:
        new_opt = f"Option {counter}"
        if new_opt not in options:
            options.append(new_opt)
        counter += 1
    
    options = list(dict.fromkeys(options))[:4]
    random.shuffle(options)
    correct_idx = options.index(correct_str)
    
    return options, correct_idx

# ============================================================
# SVG GENERATORS
# ============================================================

def generate_formula_triangle_svg():
    """Generate the Speed-Distance-Time triangle"""
    width = 200
    height = 160
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#e8f5e9" stroke="#4caf50" stroke-width="2" rx="8"/>'
    
    # Triangle
    svg += f'<polygon points="100,20 30,130 170,130" fill="none" stroke="#2e7d32" stroke-width="3"/>'
    
    # Horizontal line dividing top from bottom
    svg += f'<line x1="50" y1="85" x2="150" y2="85" stroke="#2e7d32" stroke-width="2"/>'
    
    # Vertical line in bottom section
    svg += f'<line x1="100" y1="85" x2="100" y2="130" stroke="#2e7d32" stroke-width="2"/>'
    
    # Labels
    svg += f'<text x="100" y="60" text-anchor="middle" font-size="16" fill="#1b5e20" font-weight="bold">D</text>'
    svg += f'<text x="70" y="115" text-anchor="middle" font-size="16" fill="#1b5e20" font-weight="bold">S</text>'
    svg += f'<text x="130" y="115" text-anchor="middle" font-size="16" fill="#1b5e20" font-weight="bold">T</text>'
    
    # Formula text
    svg += f'<text x="100" y="150" text-anchor="middle" font-size="10" fill="#666">D = S × T | S = D ÷ T | T = D ÷ S</text>'
    
    svg += '</svg>'
    return svg

def generate_journey_svg(distance, time_str, speed=None):
    """Generate a journey visualization"""
    width = 280
    height = 80
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#e3f2fd" stroke="#1976d2" stroke-width="2" rx="8"/>'
    
    # Start point
    svg += f'<circle cx="40" cy="40" r="12" fill="#4caf50"/>'
    svg += f'<text x="40" y="44" text-anchor="middle" font-size="10" fill="white">A</text>'
    
    # End point
    svg += f'<circle cx="240" cy="40" r="12" fill="#f44336"/>'
    svg += f'<text x="240" y="44" text-anchor="middle" font-size="10" fill="white">B</text>'
    
    # Arrow line
    svg += f'<line x1="55" y1="40" x2="220" y2="40" stroke="#1976d2" stroke-width="3"/>'
    svg += f'<polygon points="225,40 215,35 215,45" fill="#1976d2"/>'
    
    # Distance label
    svg += f'<text x="140" y="35" text-anchor="middle" font-size="12" fill="#0d47a1" font-weight="bold">{distance}</text>'
    
    # Time label
    svg += f'<text x="140" y="55" text-anchor="middle" font-size="11" fill="#666">Time: {time_str}</text>'
    
    # Speed if provided
    if speed:
        svg += f'<text x="140" y="72" text-anchor="middle" font-size="10" fill="#4caf50">Speed: {speed}</text>'
    
    svg += '</svg>'
    return svg

def generate_distance_time_graph_svg(points, labels=None):
    """Generate a distance-time graph"""
    width = 280
    height = 200
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#fff8e1" stroke="#ff9800" stroke-width="2" rx="5"/>'
    
    # Graph area
    graph_left = 50
    graph_bottom = 170
    graph_width = 210
    graph_height = 140
    
    # Axes
    svg += f'<line x1="{graph_left}" y1="{graph_bottom}" x2="{graph_left + graph_width}" y2="{graph_bottom}" stroke="#333" stroke-width="2"/>'
    svg += f'<line x1="{graph_left}" y1="{graph_bottom}" x2="{graph_left}" y2="{graph_bottom - graph_height}" stroke="#333" stroke-width="2"/>'
    
    # Axis labels
    svg += f'<text x="{graph_left + graph_width/2}" y="190" text-anchor="middle" font-size="11" fill="#333">Time</text>'
    svg += f'<text x="15" y="{graph_bottom - graph_height/2}" text-anchor="middle" font-size="11" fill="#333" transform="rotate(-90, 15, {graph_bottom - graph_height/2})">Distance</text>'
    
    # Grid lines
    for i in range(1, 5):
        y = graph_bottom - (i * graph_height / 4)
        svg += f'<line x1="{graph_left}" y1="{y}" x2="{graph_left + graph_width}" y2="{y}" stroke="#ddd" stroke-width="1"/>'
    
    # Plot points and lines
    if points:
        max_x = max(p[0] for p in points)
        max_y = max(p[1] for p in points)
        
        scaled_points = []
        for x, y in points:
            sx = graph_left + (x / max_x) * graph_width if max_x > 0 else graph_left
            sy = graph_bottom - (y / max_y) * graph_height if max_y > 0 else graph_bottom
            scaled_points.append((sx, sy))
        
        # Draw lines
        for i in range(len(scaled_points) - 1):
            svg += f'<line x1="{scaled_points[i][0]}" y1="{scaled_points[i][1]}" x2="{scaled_points[i+1][0]}" y2="{scaled_points[i+1][1]}" stroke="#1976d2" stroke-width="2"/>'
        
        # Draw points
        for sx, sy in scaled_points:
            svg += f'<circle cx="{sx}" cy="{sy}" r="4" fill="#1976d2"/>'
    
    svg += '</svg>'
    return svg

def generate_two_journeys_svg(person1, speed1, person2, speed2, start_diff=None):
    """Generate visualization of two people travelling"""
    width = 280
    height = 100
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#fce4ec" stroke="#e91e63" stroke-width="2" rx="8"/>'
    
    # Person 1
    svg += f'<text x="20" y="30" font-size="11" fill="#333">{person1}:</text>'
    svg += f'<text x="80" y="30" font-size="11" fill="#1976d2" font-weight="bold">{speed1}</text>'
    
    # Person 2
    svg += f'<text x="20" y="55" font-size="11" fill="#333">{person2}:</text>'
    svg += f'<text x="80" y="55" font-size="11" fill="#e91e63" font-weight="bold">{speed2}</text>'
    
    if start_diff:
        svg += f'<text x="20" y="80" font-size="10" fill="#666">{start_diff}</text>'
    
    # Simple race visual
    svg += f'<line x1="170" y1="25" x2="260" y2="25" stroke="#1976d2" stroke-width="3"/>'
    svg += f'<circle cx="175" cy="25" r="5" fill="#1976d2"/>'
    
    svg += f'<line x1="170" y1="50" x2="240" y2="50" stroke="#e91e63" stroke-width="3"/>'
    svg += f'<circle cx="175" cy="50" r="5" fill="#e91e63"/>'
    
    svg += '</svg>'
    return svg

# ============================================================
# LEVEL 1: Understanding the Formula (Foundation)
# ============================================================

def generate_level_1():
    """Understanding Speed = Distance ÷ Time"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 25
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(['formula_identify', 'units_match', 'concept', 'simple_speed', 'simple_identify', 'true_false', 'which_faster'])
        
        try:
            if q_type == 'formula_identify':
                formulas = [
                    ("Speed", "Distance ÷ Time", ["Distance × Time", "Time ÷ Distance", "Distance + Time"]),
                    ("Distance", "Speed × Time", ["Speed ÷ Time", "Speed + Time", "Time ÷ Speed"]),
                    ("Time", "Distance ÷ Speed", ["Distance × Speed", "Speed ÷ Distance", "Distance + Speed"])
                ]
                formula = random.choice(formulas)
                
                q_text = f"What is the formula to calculate {formula[0]}?"
                correct = formula[1]
                wrong = formula[2]
                
                visual = generate_formula_triangle_svg()
                explanation = f"From the triangle: {formula[0]} = {formula[1]}"
                
            elif q_type == 'units_match':
                units = [
                    ("km/h", "kilometres per hour", ["kilometres per minute", "metres per hour", "miles per second"]),
                    ("m/s", "metres per second", ["metres per hour", "miles per second", "kilometres per second"]),
                    ("km", "kilometres", ["km/h", "hours", "m/s"]),
                    ("hours", "time measurement", ["speed measurement", "distance measurement", "km/h"])
                ]
                unit = random.choice(units)
                
                q_text = f"What does '{unit[0]}' measure or mean?"
                correct = unit[1]
                wrong = unit[2]
                
                visual = None
                explanation = f"'{unit[0]}' means {unit[1]}."
                
            elif q_type == 'concept':
                concepts = [
                    ("If you travel further in the same time, your speed is...", "faster", ["slower", "the same", "zero"]),
                    ("If you travel the same distance in less time, your speed is...", "faster", ["slower", "the same", "zero"]),
                    ("What does 'average speed' mean?", "Total distance ÷ Total time", ["Top speed reached", "Speed at the start", "Speed at the end"]),
                    ("A car travels 100 km in 2 hours. It travels...", "50 km each hour on average", ["100 km each hour", "200 km each hour", "25 km each hour"])
                ]
                concept = random.choice(concepts)
                
                q_text = concept[0]
                correct = concept[1]
                wrong = concept[2]
                
                visual = None
                explanation = f"{concept[0]} {concept[1]}"
                
            elif q_type == 'simple_speed':
                distance = random.choice([10, 20, 30, 40, 50, 60, 80, 100])
                time = random.choice([1, 2, 4, 5])
                speed = distance / time
                
                q_text = f"A car travels {distance} km in {time} hour{'s' if time > 1 else ''}.\\nWhat is its speed?"
                correct = f"{int(speed)} km/h"
                wrong = [f"{int(speed * 2)} km/h", f"{int(speed / 2)} km/h", f"{int(speed + 10)} km/h"]
                
                visual = generate_journey_svg(f"{distance} km", f"{time} hour{'s' if time > 1 else ''}")
                explanation = f"Speed = Distance ÷ Time = {distance} ÷ {time} = {int(speed)} km/h"
                
            elif q_type == 'simple_identify':
                scenarios = [
                    ("60 km/h", "speed", ["distance", "time", "acceleration"]),
                    ("150 km", "distance", ["speed", "time", "velocity"]),
                    ("3 hours", "time", ["speed", "distance", "rate"]),
                    ("25 m/s", "speed", ["distance", "time", "length"])
                ]
                scenario = random.choice(scenarios)
                
                q_text = f"What type of measurement is '{scenario[0]}'?"
                correct = scenario[1]
                wrong = scenario[2]
                
                visual = None
                explanation = f"'{scenario[0]}' is a measurement of {scenario[1]}."
            
            elif q_type == 'true_false':
                statements = [
                    ("A car going 80 km/h is faster than one going 60 km/h", "True", ["False", "Cannot tell", "Same speed"]),
                    ("Speed tells you how far you travel", "False", ["True", "Sometimes", "Always"]),
                    ("If two cars travel the same distance, the faster one takes less time", "True", ["False", "Same time", "Cannot tell"]),
                    ("km/h and m/s are both units of speed", "True", ["False", "Only km/h", "Only m/s"]),
                    ("To find speed, you multiply distance by time", "False", ["True", "Sometimes", "Usually"])
                ]
                statement = random.choice(statements)
                
                q_text = f"True or False: {statement[0]}"
                correct = statement[1]
                wrong = statement[2]
                
                visual = None
                explanation = f"The answer is {statement[1]}."
            
            elif q_type == 'which_faster':
                speed1 = random.choice([30, 40, 50, 60])
                speed2 = speed1 + random.choice([10, 15, 20, 25])
                
                name1, name2 = random.sample(IRISH_NAMES, 2)
                
                q_text = f"{name1} travels at {speed1} km/h. {name2} travels at {speed2} km/h.\\nWho is going faster?"
                correct = name2
                wrong = [name1, "Same speed", "Cannot tell"]
                
                visual = None
                explanation = f"{name2} is faster: {speed2} km/h > {speed1} km/h"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{correct}_{q_text[:30]}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 1,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 2: Finding Speed (Foundation)
# ============================================================

def generate_level_2():
    """Calculate Speed given Distance and Time (whole hours)"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 15
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            name = random.choice(IRISH_NAMES)
            transport = random.choice(['car', 'bus', 'train', 'bike'])
            
            # Nice numbers that divide evenly
            time_hours = random.choice([1, 2, 3, 4, 5])
            speed = random.choice([20, 25, 30, 40, 50, 60, 80, 100, 120])
            distance = speed * time_hours
            
            town1, town2 = random.sample(IRISH_TOWNS, 2)
            
            q_text = f"{name} travels from {town1} to {town2} by {transport}.\\nThe distance is {distance} km and it takes {time_hours} hour{'s' if time_hours > 1 else ''}.\\nWhat is the average speed?"
            
            correct = f"{speed} km/h"
            wrong = [f"{speed + 10} km/h", f"{speed - 10} km/h", f"{speed * 2} km/h"]
            
            visual = generate_journey_svg(f"{distance} km", f"{time_hours} hour{'s' if time_hours > 1 else ''}")
            explanation = f"Speed = Distance ÷ Time\\n= {distance} km ÷ {time_hours} hours\\n= {speed} km/h"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"speed_{distance}_{time_hours}_{name}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 2,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 3: Finding Distance and Time (Foundation)
# ============================================================

def generate_level_3():
    """Calculate Distance or Time (whole numbers)"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 15
    
    question_types = ['find_distance', 'find_time']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            
            if q_type == 'find_distance':
                speed = random.choice([30, 40, 50, 60, 80, 100])
                time_hours = random.choice([1, 2, 3, 4, 5])
                distance = speed * time_hours
                
                q_text = f"{name} drives at {speed} km/h for {time_hours} hour{'s' if time_hours > 1 else ''}.\\nHow far do they travel?"
                
                correct = f"{distance} km"
                wrong = [f"{distance + 20} km", f"{distance - 20} km", f"{speed} km"]
                
                visual = generate_journey_svg("? km", f"{time_hours} hour{'s' if time_hours > 1 else ''}", f"{speed} km/h")
                explanation = f"Distance = Speed × Time\\n= {speed} km/h × {time_hours} hours\\n= {distance} km"
                
            else:  # find_time
                speed = random.choice([30, 40, 50, 60, 80, 100])
                time_hours = random.choice([1, 2, 3, 4, 5])
                distance = speed * time_hours
                
                q_text = f"{name} needs to travel {distance} km. They travel at {speed} km/h.\\nHow long does the journey take?"
                
                correct = f"{time_hours} hour{'s' if time_hours > 1 else ''}"
                wrong = [f"{time_hours + 1} hours", f"{time_hours + 2} hours", f"{time_hours * 2} hours"]
                
                visual = generate_journey_svg(f"{distance} km", "? hours", f"{speed} km/h")
                explanation = f"Time = Distance ÷ Speed\\n= {distance} km ÷ {speed} km/h\\n= {time_hours} hour{'s' if time_hours > 1 else ''}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{distance}_{speed}_{name}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 3,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 4: Time in Minutes (Ordinary)
# ============================================================

def generate_level_4():
    """Speed calculations with time in minutes - SEC 2024 OL Q4 style"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 15
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            name = random.choice(IRISH_NAMES)
            
            # SEC 2024 OL Q4 style: 60 km in 45 minutes
            time_mins = random.choice([15, 20, 30, 40, 45, 50])
            time_hours = time_mins / 60
            
            # Choose speed that gives nice answer
            speed = random.choice([40, 48, 60, 72, 80, 90, 100, 120])
            distance = round_val(speed * time_hours)
            
            transport = random.choice(['car', 'bus', 'taxi', 'train'])
            
            q_text = f"It takes {time_mins} minutes to travel {distance} km by {transport}.\\nWork out the average speed in km/hour."
            
            correct = f"{speed} km/h"
            wrong_vals = [speed * 0.75, speed * 1.5, distance]
            wrong = [f"{int(w)} km/h" for w in wrong_vals]
            
            visual = generate_journey_svg(f"{distance} km", f"{time_mins} minutes")
            explanation = f"SEC 2024 OL Q4 style!\\nConvert {time_mins} minutes to hours: {time_mins} ÷ 60 = {time_hours} hours\\nSpeed = Distance ÷ Time\\n= {distance} ÷ {time_hours}\\n= {speed} km/h"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"mins_{distance}_{time_mins}_{name}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 4,
                'difficulty_band': 'ordinary',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 5: Different Units (Ordinary)
# ============================================================

def generate_level_5():
    """Speed in m/min or m/s - SEC 2022 OL Q3(b) style"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 15
    
    question_types = ['m_per_min', 'm_per_sec', 'convert_units']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            
            if q_type == 'm_per_min':
                # SEC 2022 OL Q3(b) style: 250m in 5 minutes
                distance_m = random.choice([200, 250, 300, 400, 500, 600, 800, 1000])
                time_mins = random.choice([4, 5, 8, 10])
                speed = distance_m / time_mins
                
                activity = random.choice(['swims', 'walks', 'jogs', 'runs'])
                
                q_text = f"{name} {activity} {distance_m} m in {time_mins} minutes.\\nWork out the average speed in metres per minute."
                
                correct = f"{int(speed)} m/min"
                wrong = [f"{int(speed * 2)} m/min", f"{int(speed / 2)} m/min", f"{int(speed + 10)} m/min"]
                
                visual = generate_journey_svg(f"{distance_m} m", f"{time_mins} minutes")
                explanation = f"SEC 2022 OL Q3(b) style!\\nSpeed = Distance ÷ Time\\n= {distance_m} m ÷ {time_mins} min\\n= {int(speed)} m/min"
                
            elif q_type == 'm_per_sec':
                distance_m = random.choice([100, 200, 400, 800])
                time_secs = random.choice([10, 20, 25, 40, 50, 100])
                speed = distance_m / time_secs
                
                activity = random.choice(['sprints', 'runs', 'cycles'])
                
                q_text = f"{name} {activity} {distance_m} m in {time_secs} seconds.\\nWhat is the average speed in m/s?"
                
                correct = f"{round_val(speed)} m/s"
                wrong = [f"{round_val(speed * 2)} m/s", f"{round_val(speed / 2)} m/s", f"{round_val(speed + 2)} m/s"]
                
                visual = generate_journey_svg(f"{distance_m} m", f"{time_secs} seconds")
                explanation = f"Speed = Distance ÷ Time\\n= {distance_m} m ÷ {time_secs} s\\n= {round_val(speed)} m/s"
                
            else:  # convert_units
                speed_kmh = random.choice([36, 54, 72, 90, 108])
                speed_ms = speed_kmh / 3.6
                
                q_text = f"A car travels at {speed_kmh} km/h.\\nWhat is this speed in metres per second?\\n(Hint: divide by 3.6)"
                
                correct = f"{round_val(speed_ms)} m/s"
                wrong = [f"{round_val(speed_ms * 2)} m/s", f"{round_val(speed_ms * 3.6)} m/s", f"{round_val(speed_kmh)} m/s"]
                
                visual = None
                explanation = f"To convert km/h to m/s, divide by 3.6:\\n{speed_kmh} ÷ 3.6 = {round_val(speed_ms)} m/s"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{distance_m if 'distance_m' in dir() else speed_kmh}_{name}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 5,
                'difficulty_band': 'ordinary',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 6: Time Calculations with Minutes (Ordinary)
# ============================================================

def generate_level_6():
    """Find time answers in hours and minutes"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 15
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            name = random.choice(IRISH_NAMES)
            
            # Create times that give nice hour:minute answers
            speed = random.choice([40, 50, 60, 80, 100, 120])
            time_mins = random.choice([30, 45, 90, 120, 150])
            time_hours = time_mins / 60
            distance = round_val(speed * time_hours)
            
            town1, town2 = random.sample(IRISH_TOWNS, 2)
            
            q_text = f"{name} drives {distance} km from {town1} to {town2} at {speed} km/h.\\nHow long does the journey take?"
            
            hours = int(time_hours)
            mins = int((time_hours - hours) * 60)
            
            if hours == 0:
                correct = f"{mins} minutes"
            elif mins == 0:
                correct = f"{hours} hour{'s' if hours > 1 else ''}"
            else:
                correct = f"{hours} hour{'s' if hours > 1 else ''} {mins} minutes"
            
            wrong = [
                f"{hours + 1} hours" if mins == 0 else f"{hours + 1} hour{'s' if hours > 0 else ''} {mins} minutes",
                f"{time_mins} minutes",
                f"{int(time_mins * 1.5)} minutes"
            ]
            
            visual = generate_journey_svg(f"{distance} km", "?", f"{speed} km/h")
            explanation = f"Time = Distance ÷ Speed\\n= {distance} ÷ {speed}\\n= {time_hours} hours\\n= {correct}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"time_{distance}_{speed}_{name}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 6,
                'difficulty_band': 'ordinary',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 7: Flight/Journey Problems (Higher)
# ============================================================

def generate_level_7():
    """Flight problems - SEC 2023 HL Q8(c)(ii) style"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 15
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            name = random.choice(IRISH_NAMES)
            
            # SEC 2023 HL Q8(c)(ii): 360 km in 45 mins
            time_mins = random.choice([30, 40, 45, 50, 60, 75, 90])
            time_hours = time_mins / 60
            
            # Flight speeds typically 400-900 km/h
            speed = random.choice([400, 480, 500, 540, 600, 720, 800])
            distance = round_val(speed * time_hours)
            
            irish_airports = ['Dublin', 'Cork', 'Shannon', 'Knock', 'Kerry']
            uk_airports = ['London', 'Manchester', 'Birmingham', 'Edinburgh', 'Glasgow']
            
            airport1 = random.choice(irish_airports)
            airport2 = random.choice(uk_airports)
            
            q_text = f"{name} flies from {airport1} to {airport2}.\\nThe distance is {distance} km and the flight takes {time_mins} minutes.\\nWork out the average speed in km/hour."
            
            correct = f"{speed} km/h"
            wrong = [f"{int(speed * 0.75)} km/h", f"{int(speed * 1.5)} km/h", f"{int(distance)} km/h"]
            
            visual = generate_journey_svg(f"{distance} km", f"{time_mins} min flight")
            explanation = f"SEC 2023 HL Q8(c)(ii) style!\\nConvert time: {time_mins} mins = {time_mins}/60 = {round_val(time_hours, 3)} hours\\nSpeed = {distance} ÷ {round_val(time_hours, 3)} = {speed} km/h"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"flight_{distance}_{time_mins}_{name}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 7,
                'difficulty_band': 'higher',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 8: Cycling/Running - SEC 2025 OL style (Higher)
# ============================================================

def generate_level_8():
    """Cycling/Running problems with short times - SEC 2025 OL Q13 style"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 15
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            name = random.choice(IRISH_NAMES)
            
            # SEC 2025 OL Q13(a): 3 km in 10 minutes
            activity = random.choice(['cycles', 'runs', 'jogs', 'walks'])
            
            time_mins = random.choice([5, 10, 12, 15, 20, 30])
            time_hours = time_mins / 60
            
            # Realistic speeds for activity
            if activity == 'cycles':
                speed = random.choice([12, 15, 18, 20, 24, 30])
            elif activity in ['runs', 'jogs']:
                speed = random.choice([8, 10, 12, 15])
            else:
                speed = random.choice([4, 5, 6])
            
            distance = round_val(speed * time_hours)
            
            destination = random.choice(['school', 'football training', 'the shop', 'work', 'the park', 'a friend\'s house'])
            
            q_text = f"{name} {activity} {distance} km to {destination}.\\nIt takes {time_mins} minutes.\\nWork out the average speed in km/hour."
            
            correct = f"{speed} km/h"
            wrong = [f"{int(speed * 1.5)} km/h", f"{int(speed * 0.5)} km/h", f"{int(distance * 6)} km/h"]
            
            visual = generate_journey_svg(f"{distance} km", f"{time_mins} minutes")
            explanation = f"SEC 2025 OL Q13(a) style!\\nTime in hours: {time_mins} ÷ 60 = {round_val(time_hours, 3)} hours\\nSpeed = {distance} ÷ {round_val(time_hours, 3)} = {speed} km/h"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"activity_{distance}_{time_mins}_{activity}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 8,
                'difficulty_band': 'higher',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 9: Two-Part Journeys (Higher)
# ============================================================

def generate_level_9():
    """Average speed for journeys with different speeds"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 15
    
    question_types = ['total_distance', 'total_time', 'average_speed']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            
            if q_type == 'total_distance':
                speed1 = random.choice([40, 50, 60])
                time1 = random.choice([1, 2])
                speed2 = random.choice([80, 100, 120])
                time2 = random.choice([1, 2])
                
                dist1 = speed1 * time1
                dist2 = speed2 * time2
                total = dist1 + dist2
                
                q_text = f"{name} drives at {speed1} km/h for {time1} hour{'s' if time1 > 1 else ''}, then at {speed2} km/h for {time2} hour{'s' if time2 > 1 else ''}.\\nWhat is the total distance travelled?"
                
                correct = f"{total} km"
                wrong = [f"{dist1} km", f"{dist2} km", f"{total + 50} km"]
                
                visual = None
                explanation = f"Part 1: {speed1} × {time1} = {dist1} km\\nPart 2: {speed2} × {time2} = {dist2} km\\nTotal: {dist1} + {dist2} = {total} km"
                
            elif q_type == 'total_time':
                speed = random.choice([50, 60, 80, 100])
                dist1 = random.choice([50, 60, 80, 100])
                dist2 = random.choice([40, 50, 60, 80])
                
                time1 = dist1 / speed
                time2 = dist2 / speed
                total_time = time1 + time2
                total_mins = int(total_time * 60)
                
                q_text = f"{name} travels {dist1} km, stops for lunch, then travels another {dist2} km.\\nThey travel at {speed} km/h for both parts.\\nWhat is the total driving time?"
                
                hours = int(total_time)
                mins = int((total_time - hours) * 60)
                if mins == 0:
                    correct = f"{hours} hours"
                else:
                    correct = f"{hours} hour{'s' if hours > 1 else ''} {mins} minutes"
                
                wrong = [f"{hours + 1} hours", f"{total_mins} minutes", f"{int(total_time * 2)} hours"]
                
                visual = None
                explanation = f"Time 1: {dist1} ÷ {speed} = {round_val(time1)} hours\\nTime 2: {dist2} ÷ {speed} = {round_val(time2)} hours\\nTotal: {round_val(total_time)} hours = {correct}"
                
            else:  # average_speed
                dist1 = random.choice([60, 80, 100])
                dist2 = dist1  # Same distance each way for simpler calculation
                speed1 = random.choice([40, 50, 60])
                speed2 = random.choice([80, 100, 120])
                
                time1 = dist1 / speed1
                time2 = dist2 / speed2
                total_dist = dist1 + dist2
                total_time = time1 + time2
                avg_speed = round_val(total_dist / total_time)
                
                q_text = f"{name} drives {dist1} km to work at {speed1} km/h.\\nThey return the same way at {speed2} km/h.\\nWhat is the average speed for the whole journey?"
                
                correct = f"{avg_speed} km/h"
                # Common mistake: average of speeds
                wrong_avg = (speed1 + speed2) / 2
                wrong = [f"{int(wrong_avg)} km/h", f"{speed1} km/h", f"{speed2} km/h"]
                
                visual = None
                explanation = f"Total distance: {total_dist} km\\nTime out: {dist1}÷{speed1} = {round_val(time1)} h\\nTime back: {dist2}÷{speed2} = {round_val(time2)} h\\nTotal time: {round_val(total_time)} h\\nAverage = {total_dist} ÷ {round_val(total_time)} = {avg_speed} km/h\\n(Note: NOT {int(wrong_avg)} km/h - can't just average the speeds!)"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{q_text[:40]}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 9,
                'difficulty_band': 'higher',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 10: Catching Up Problems (Application)
# ============================================================

def generate_level_10():
    """SEC 2022 HL Q10 style - catching up problems"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    question_types = ['when_distance', 'catch_up_time', 'meeting_point']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name1 = random.choice(IRISH_NAMES)
            name2 = random.choice([n for n in IRISH_NAMES if n != name1])
            
            if q_type == 'when_distance':
                # SEC 2022 HL Q10(a) style: At 09:20 she is 5km from home, when 8km?
                speed = random.choice([12, 15, 18, 20])  # Running/cycling speed km/h
                
                time1_mins = random.choice([15, 20, 30])
                dist1 = speed * (time1_mins / 60)
                
                dist2 = random.choice([6, 8, 10, 12])
                while dist2 <= dist1:
                    dist2 += 2
                
                time2_mins = (dist2 / speed) * 60
                extra_mins = time2_mins - time1_mins
                
                start_hour = 9
                start_min = 0
                check_min = start_min + time1_mins
                
                final_min = start_min + time2_mins
                final_hour = start_hour + int(final_min // 60)
                final_min = int(final_min % 60)
                
                q_text = f"{name1} leaves home at 09:00 running at constant speed.\\nAt 09:{time1_mins:02d} they are {dist1} km from home.\\nAt what time will they be {dist2} km from home?"
                
                correct = f"{final_hour:02d}:{final_min:02d}"
                wrong = [f"09:{int(time2_mins):02d}", f"{final_hour:02d}:{(final_min+10)%60:02d}", f"10:{final_min:02d}"]
                
                visual = generate_two_journeys_svg(name1, f"{speed} km/h", "", "", f"Started 09:00")
                explanation = f"Speed = {dist1} km ÷ {time1_mins/60} h = {speed} km/h\\nTime for {dist2} km = {dist2} ÷ {speed} = {time2_mins/60} hours = {int(time2_mins)} mins\\nTime: 09:00 + {int(time2_mins)} mins = {correct}"
                
            elif q_type == 'catch_up_time':
                # Two people, one starts later but faster
                speed1 = random.choice([10, 12, 15])
                speed2 = random.choice([15, 18, 20, 24])
                while speed2 <= speed1:
                    speed2 += 3
                
                head_start_mins = random.choice([10, 15, 20])
                head_start_dist = speed1 * (head_start_mins / 60)
                
                # Time to catch up: head_start_dist / (speed2 - speed1)
                catch_up_hours = head_start_dist / (speed2 - speed1)
                catch_up_mins = catch_up_hours * 60
                
                q_text = f"{name1} starts running at {speed1} km/h.\\n{name2} starts {head_start_mins} minutes later at {speed2} km/h.\\nHow long after {name2} starts will they catch up?"
                
                correct = f"{int(catch_up_mins)} minutes"
                wrong = [f"{int(catch_up_mins * 1.5)} minutes", f"{int(catch_up_mins * 0.5)} minutes", f"{head_start_mins} minutes"]
                
                visual = generate_two_journeys_svg(name1, f"{speed1} km/h", name2, f"{speed2} km/h", f"{name2} starts {head_start_mins} min later")
                explanation = f"{name1}'s head start: {speed1} × {head_start_mins}/60 = {round_val(head_start_dist)} km\\nClosing speed: {speed2} - {speed1} = {speed2-speed1} km/h\\nTime to catch: {round_val(head_start_dist)} ÷ {speed2-speed1} = {round_val(catch_up_hours)} h = {int(catch_up_mins)} mins"
                
            else:  # meeting_point
                speed1 = random.choice([40, 50, 60])
                speed2 = random.choice([50, 60, 80])
                total_dist = random.choice([100, 120, 150, 180])
                
                # They meet when d1 + d2 = total, and t1 = t2
                # speed1 * t + speed2 * t = total
                # t = total / (speed1 + speed2)
                meet_time = total_dist / (speed1 + speed2)
                meet_dist = speed1 * meet_time
                
                town1, town2 = random.sample(IRISH_TOWNS, 2)
                
                q_text = f"{name1} leaves {town1} travelling to {town2} at {speed1} km/h.\\n{name2} leaves {town2} at the same time travelling to {town1} at {speed2} km/h.\\nThe towns are {total_dist} km apart. How far from {town1} do they meet?"
                
                correct = f"{round_val(meet_dist)} km"
                wrong = [f"{round_val(total_dist - meet_dist)} km", f"{round_val(total_dist / 2)} km", f"{round_val(meet_dist * 1.5)} km"]
                
                visual = None
                explanation = f"Combined speed: {speed1} + {speed2} = {speed1+speed2} km/h\\nTime to meet: {total_dist} ÷ {speed1+speed2} = {round_val(meet_time)} hours\\n{name1}'s distance: {speed1} × {round_val(meet_time)} = {round_val(meet_dist)} km from {town1}"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{name1}_{name2}_{speed1 if 'speed1' in dir() else 0}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 10,
                'difficulty_band': 'application',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 11: Distance-Time Graphs (Application)
# ============================================================

def generate_level_11():
    """Distance-Time Graph interpretation - SEC 2025 OL Q13(b) style"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    question_types = ['total_time', 'stationary_time', 'faster_section', 'read_distance', 'calculate_speed']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            
            # Generate graph data
            outward_time = random.choice([10, 15, 20])
            stationary_time = random.choice([30, 45, 60])
            return_time = random.choice([10, 15, 20, 25])
            max_distance = random.choice([3, 4, 5, 6])
            
            total_time = outward_time + stationary_time + return_time
            
            points = [
                (0, 0),
                (outward_time, max_distance),
                (outward_time + stationary_time, max_distance),
                (total_time, 0)
            ]
            
            if q_type == 'total_time':
                q_text = f"Look at the distance-time graph.\\n{name} cycles from home and back.\\nHow long was {name} away from home in total?"
                
                correct = f"{total_time} minutes"
                wrong = [f"{outward_time + return_time} minutes", f"{stationary_time} minutes", f"{total_time + 10} minutes"]
                
                explanation = f"SEC 2025 OL Q13(b)(i) style!\\nTotal time = from start to returning home\\n= {total_time} minutes"
                
            elif q_type == 'stationary_time':
                q_text = f"The graph shows {name}'s journey.\\nHow long was {name} stationary (not moving)?"
                
                correct = f"{stationary_time} minutes"
                wrong = [f"{outward_time} minutes", f"{return_time} minutes", f"{total_time} minutes"]
                
                explanation = f"SEC 2025 OL Q13(b)(ii) style!\\nStationary = horizontal section (distance not changing)\\n= {stationary_time} minutes"
                
            elif q_type == 'faster_section':
                outward_speed = max_distance / (outward_time / 60)
                return_speed = max_distance / (return_time / 60)
                
                if outward_speed > return_speed:
                    correct = "Going (outward journey)"
                    explanation = f"Outward: {max_distance} km in {outward_time} min = {round_val(outward_speed)} km/h\\nReturn: {max_distance} km in {return_time} min = {round_val(return_speed)} km/h\\nOutward is faster (steeper line)"
                else:
                    correct = "Returning (homeward journey)"
                    explanation = f"Outward: {max_distance} km in {outward_time} min = {round_val(outward_speed)} km/h\\nReturn: {max_distance} km in {return_time} min = {round_val(return_speed)} km/h\\nReturn is faster (steeper line)"
                
                q_text = f"Was {name} quicker going to the destination or returning home?\\nGive a reason."
                wrong = ["Same speed both ways", "Cannot tell from graph", "Returning (homeward journey)" if "Going" in correct else "Going (outward journey)"]
                
            elif q_type == 'read_distance':
                q_text = f"From the graph, what was the maximum distance {name} reached from home?"
                
                correct = f"{max_distance} km"
                wrong = [f"{max_distance + 1} km", f"{max_distance - 1} km", f"{max_distance * 2} km"]
                
                explanation = f"Read the highest point on the graph = {max_distance} km"
                
            else:  # calculate_speed
                outward_speed = max_distance / (outward_time / 60)
                
                q_text = f"The graph shows {name} cycling {max_distance} km in {outward_time} minutes for the outward journey.\\nWhat was the speed in km/h?"
                
                correct = f"{round_val(outward_speed)} km/h"
                wrong = [f"{round_val(outward_speed * 0.5)} km/h", f"{round_val(outward_speed * 2)} km/h", f"{max_distance} km/h"]
                
                explanation = f"Speed = Distance ÷ Time\\n= {max_distance} ÷ ({outward_time}/60)\\n= {max_distance} ÷ {round_val(outward_time/60, 3)}\\n= {round_val(outward_speed)} km/h"
            
            visual = generate_distance_time_graph_svg(points)
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{total_time}_{max_distance}_{random.randint(1,100)}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': visual,
                'difficulty': 11,
                'difficulty_band': 'application',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 12: Complex Real-World Problems (Mastery)
# ============================================================

def generate_level_12():
    """Complex multi-step speed/distance/time problems"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 25
    
    question_types = ['arrival_time', 'required_speed', 'fuel_calculation', 'delay_problem']
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        q_type = random.choice(question_types)
        
        try:
            name = random.choice(IRISH_NAMES)
            
            if q_type == 'arrival_time':
                distance = random.choice([150, 180, 200, 240, 300])
                speed = random.choice([60, 80, 100, 120])
                start_time = random.choice(['08:00', '09:30', '10:00', '14:00'])
                
                journey_hours = distance / speed
                journey_mins = int(journey_hours * 60)
                
                start_h, start_m = map(int, start_time.split(':'))
                total_mins = start_h * 60 + start_m + journey_mins
                arr_h = total_mins // 60
                arr_m = total_mins % 60
                
                q_text = f"{name} leaves at {start_time} to drive {distance} km.\\nThey travel at an average speed of {speed} km/h.\\nAt what time will they arrive?"
                
                correct = f"{arr_h:02d}:{arr_m:02d}"
                wrong = [f"{arr_h:02d}:{(arr_m+30)%60:02d}", f"{(arr_h+1)%24:02d}:{arr_m:02d}", f"{arr_h:02d}:{(arr_m-15)%60:02d}"]
                
                visual = None
                explanation = f"Journey time: {distance} ÷ {speed} = {round_val(journey_hours)} hours = {journey_mins} minutes\\nStart: {start_time}\\nArrival: {correct}"
                
            elif q_type == 'required_speed':
                distance = random.choice([100, 120, 150, 180])
                available_time_mins = random.choice([90, 120, 150, 180])
                available_hours = available_time_mins / 60
                required_speed = distance / available_hours
                
                q_text = f"{name} needs to travel {distance} km in {available_time_mins} minutes.\\nWhat average speed must they maintain?"
                
                correct = f"{round_val(required_speed)} km/h"
                wrong = [f"{round_val(required_speed * 0.75)} km/h", f"{round_val(required_speed * 1.5)} km/h", f"{distance} km/h"]
                
                visual = None
                explanation = f"Time in hours: {available_time_mins} ÷ 60 = {round_val(available_hours)} hours\\nRequired speed: {distance} ÷ {round_val(available_hours)} = {round_val(required_speed)} km/h"
                
            elif q_type == 'fuel_calculation':
                distance = random.choice([200, 250, 300, 400])
                fuel_efficiency = random.choice([8, 10, 12, 15])  # L per 100km
                
                fuel_needed = (distance / 100) * fuel_efficiency
                
                q_text = f"{name} plans a journey of {distance} km.\\nTheir car uses {fuel_efficiency} litres per 100 km.\\nHow much fuel will they need?"
                
                correct = f"{round_val(fuel_needed)} litres"
                wrong = [f"{round_val(fuel_needed * 0.5)} litres", f"{round_val(fuel_needed * 2)} litres", f"{fuel_efficiency} litres"]
                
                visual = None
                explanation = f"Fuel = (Distance ÷ 100) × Consumption\\n= ({distance} ÷ 100) × {fuel_efficiency}\\n= {round_val(fuel_needed)} litres"
                
            else:  # delay_problem
                original_speed = random.choice([80, 100, 120])
                distance = random.choice([200, 240, 300])
                delay_mins = random.choice([15, 20, 30])
                
                original_time_h = distance / original_speed
                new_time_h = original_time_h - (delay_mins / 60)
                new_speed = round_val(distance / new_time_h)
                
                q_text = f"{name} normally drives {distance} km at {original_speed} km/h.\\nToday they left {delay_mins} minutes late.\\nWhat speed must they average to arrive at the same time?"
                
                correct = f"{new_speed} km/h"
                wrong = [f"{original_speed} km/h", f"{round_val(new_speed * 0.9)} km/h", f"{round_val(new_speed * 1.1)} km/h"]
                
                visual = None
                explanation = f"Normal time: {distance} ÷ {original_speed} = {round_val(original_time_h)} hours\\nTime available: {round_val(original_time_h)} - {delay_mins/60} = {round_val(new_time_h)} hours\\nRequired speed: {distance} ÷ {round_val(new_time_h)} = {new_speed} km/h"
            
            options, correct_idx = make_options(correct, wrong)
            
            q_key = f"{q_type}_{q_text[:40]}_{random.randint(1,100)}"
            if q_key in used or len(set(options)) != 4:
                continue
            used.add(q_key)
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 12,
                'difficulty_band': 'mastery',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# VALIDATION
# ============================================================

def validate_questions(questions):
    """Validate generated questions"""
    errors = []
    level_counts = {}
    level_visuals = {}
    
    for q in questions:
        level = q['difficulty']
        level_counts[level] = level_counts.get(level, 0) + 1
        
        if level not in level_visuals:
            level_visuals[level] = {'total': 0, 'visual': 0}
        level_visuals[level]['total'] += 1
        if q.get('image_svg'):
            level_visuals[level]['visual'] += 1
        
        options = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(options)) != 4:
            errors.append(f"Level {level}: Duplicate options")
        
        if not q.get('explanation'):
            errors.append(f"Level {level}: Missing explanation")
    
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    
    level_names = {
        1: "Understanding Formula",
        2: "Finding Speed",
        3: "Finding Distance/Time",
        4: "Time in Minutes",
        5: "Different Units (m/s)",
        6: "Time in Hours & Mins",
        7: "Flight Problems",
        8: "Cycling/Running",
        9: "Two-Part Journeys",
        10: "Catching Up",
        11: "Distance-Time Graphs",
        12: "Complex Problems"
    }
    
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        visual_pct = 0
        if level in level_visuals and level_visuals[level]['total'] > 0:
            visual_pct = (level_visuals[level]['visual'] / level_visuals[level]['total']) * 100
        
        status = "✓" if count == QUESTIONS_PER_LEVEL else "✗"
        name = level_names.get(level, "Unknown")
        print(f"Level {level:2}: {count:2}/{QUESTIONS_PER_LEVEL} | Visual: {visual_pct:5.1f}% | {status} {name}")
    
    print("=" * 60)
    print(f"Total Questions: {len(questions)}")
    print(f"Total Errors: {len(errors)}")
    print("=" * 60)
    
    return len(errors)

# ============================================================
# DATABASE INSERTION
# ============================================================

def insert_questions(questions):
    """Insert questions into database"""
    if not os.path.exists(DB_PATH):
        print(f"Database not found at {DB_PATH}")
        return False
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        DELETE FROM questions_adaptive 
        WHERE topic = ? AND mode = ?
    """, (TOPIC, MODE))
    
    deleted = cursor.rowcount
    print(f"Deleted {deleted} existing {TOPIC} questions")
    
    inserted = 0
    for q in questions:
        try:
            cursor.execute("""
                INSERT INTO questions_adaptive 
                (question_text, option_a, option_b, option_c, option_d,
                 correct_answer, topic, difficulty_level, difficulty_band,
                 mode, explanation, image_svg, is_active)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
            """, (
                q['question_text'], q['option_a'], q['option_b'], q['option_c'], q['option_d'],
                q['correct_idx'], q['topic'], q['difficulty'], q['difficulty_band'],
                q['mode'], q['explanation'], q.get('image_svg')
            ))
            inserted += 1
        except Exception as e:
            print(f"Error: {e}")
    
    conn.commit()
    conn.close()
    print(f"Inserted {inserted} questions")
    return True

# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("SPEED, DISTANCE, TIME - JC EXAM QUESTION GENERATOR")
    print("=" * 60)
    print(f"Topic: {TOPIC}")
    print(f"Mode: {MODE}")
    print(f"Target: {QUESTIONS_PER_LEVEL * 12} questions")
    print("=" * 60)
    
    all_questions = []
    
    generators = [
        (1, "Understanding Formula", generate_level_1),
        (2, "Finding Speed", generate_level_2),
        (3, "Finding Distance/Time", generate_level_3),
        (4, "Time in Minutes", generate_level_4),
        (5, "Different Units (m/s)", generate_level_5),
        (6, "Time in Hours & Mins", generate_level_6),
        (7, "Flight Problems", generate_level_7),
        (8, "Cycling/Running", generate_level_8),
        (9, "Two-Part Journeys", generate_level_9),
        (10, "Catching Up", generate_level_10),
        (11, "Distance-Time Graphs", generate_level_11),
        (12, "Complex Problems", generate_level_12),
    ]
    
    for level, name, generator in generators:
        print(f"\nGenerating Level {level}: {name}...")
        questions = generator()
        print(f"  Generated {len(questions)} questions")
        all_questions.extend(questions)
    
    validate_questions(all_questions)
    
    print("=" * 60)
    response = input("Insert into database? (y/n): ").strip().lower()
    
    if response == 'y':
        insert_questions(all_questions)
        print("\n✓ Done!")
    else:
        print("Skipped.")

if __name__ == "__main__":
    main()
