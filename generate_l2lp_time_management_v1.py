"""
AgentMath L2LP Question Generator
Topic: Time & Timetables (l2_time_management)
NCCA Module: Understanding and managing time

Generates 600 questions (50 per level × 12 levels) for the L2LP strand.
High visual percentage with SVG graphics for accessibility.

Author: AgentMath Generator
Version: 1.0
Date: December 2025
"""

import sqlite3
import random
import math
from datetime import datetime

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'l2_time_management'
MODE = 'adaptive'
DIFFICULTY = 'adaptive'
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12
DATABASE_PATH = 'instance/mathquiz.db'

# Visual percentage targets by level
def get_visual_percentage(level):
    if level <= 3:
        return 85  # Foundation - maximum visual support
    elif level <= 6:
        return 75  # Developing - high visual support
    elif level <= 9:
        return 65  # Progressing - moderate visual support
    else:
        return 55  # Consolidating - building text confidence

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
    'clock_face': '#fefefe',
    'clock_border': '#1f2937'
}

# ============================================================
# SVG GENERATION FUNCTIONS
# ============================================================

def generate_analogue_clock_svg(hours, minutes):
    """Generate SVG of an analogue clock showing specific time"""
    # Normalize hours to 12-hour format
    hours = hours % 12
    
    # Calculate angles (12 o'clock is 0 degrees, clockwise)
    # Hour hand: 360/12 = 30 degrees per hour, plus minute contribution
    hour_angle = (hours * 30) + (minutes * 0.5) - 90
    # Minute hand: 360/60 = 6 degrees per minute
    minute_angle = (minutes * 6) - 90
    
    # Convert to radians for calculation
    hour_rad = math.radians(hour_angle)
    minute_rad = math.radians(minute_angle)
    
    # Hand endpoints (hour hand shorter)
    hour_x = 100 + 40 * math.cos(hour_rad)
    hour_y = 100 + 40 * math.sin(hour_rad)
    minute_x = 100 + 60 * math.cos(minute_rad)
    minute_y = 100 + 60 * math.sin(minute_rad)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
        <!-- Clock face -->
        <circle cx="100" cy="100" r="90" fill="{COLOURS['clock_face']}" stroke="{COLOURS['clock_border']}" stroke-width="4"/>
        
        <!-- Hour markers -->'''
    
    # Add hour markers
    for i in range(12):
        angle = math.radians(i * 30 - 90)
        inner_r = 75
        outer_r = 85
        x1 = 100 + inner_r * math.cos(angle)
        y1 = 100 + inner_r * math.sin(angle)
        x2 = 100 + outer_r * math.cos(angle)
        y2 = 100 + outer_r * math.sin(angle)
        width = 3 if i % 3 == 0 else 1
        svg += f'\n        <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{COLOURS["dark"]}" stroke-width="{width}"/>'
    
    # Add numbers
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        x = 100 + 65 * math.cos(angle)
        y = 100 + 65 * math.sin(angle) + 6
        svg += f'\n        <text x="{x:.1f}" y="{y:.1f}" font-size="16" font-family="Arial" fill="{COLOURS["dark"]}" text-anchor="middle">{i}</text>'
    
    svg += f'''
        <!-- Hour hand (thick, short) -->
        <line x1="100" y1="100" x2="{hour_x:.1f}" y2="{hour_y:.1f}" stroke="{COLOURS['dark']}" stroke-width="6" stroke-linecap="round"/>
        
        <!-- Minute hand (thin, long) -->
        <line x1="100" y1="100" x2="{minute_x:.1f}" y2="{minute_y:.1f}" stroke="{COLOURS['dark']}" stroke-width="3" stroke-linecap="round"/>
        
        <!-- Center dot -->
        <circle cx="100" cy="100" r="6" fill="{COLOURS['dark']}"/>
    </svg>'''
    
    return svg


def generate_digital_clock_svg(hours, minutes, format_24=False):
    """Generate SVG of a digital clock display"""
    if format_24:
        time_str = f"{hours:02d}:{minutes:02d}"
    else:
        period = "AM" if hours < 12 else "PM"
        display_hours = hours % 12
        if display_hours == 0:
            display_hours = 12
        time_str = f"{display_hours}:{minutes:02d}"
        
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100">
        <rect x="10" y="10" width="180" height="80" fill="{COLOURS['dark']}" rx="10"/>
        <rect x="15" y="15" width="170" height="70" fill="#1a1a2e" rx="8"/>
        <text x="100" y="65" font-size="40" font-family="Courier New, monospace" fill="#00ff00" text-anchor="middle" font-weight="bold">{time_str}</text>'''
    
    if not format_24:
        svg += f'\n        <text x="170" y="45" font-size="16" font-family="Arial" fill="#00ff00" text-anchor="middle">{period}</text>'
    
    svg += '\n    </svg>'
    return svg


def generate_time_instrument_svg(instrument_type):
    """Generate SVG of different time-telling instruments"""
    if instrument_type == 'watch':
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 160">
            <!-- Watch strap top -->
            <rect x="35" y="5" width="50" height="40" fill="#8B4513" rx="5"/>
            <!-- Watch face -->
            <circle cx="60" cy="80" r="45" fill="{COLOURS['clock_face']}" stroke="#C0C0C0" stroke-width="4"/>
            <circle cx="60" cy="80" r="40" fill="{COLOURS['clock_face']}" stroke="{COLOURS['dark']}" stroke-width="2"/>
            <!-- Simple clock hands -->
            <line x1="60" y1="80" x2="60" y2="50" stroke="{COLOURS['dark']}" stroke-width="2"/>
            <line x1="60" y1="80" x2="80" y2="80" stroke="{COLOURS['dark']}" stroke-width="3"/>
            <circle cx="60" cy="80" r="3" fill="{COLOURS['dark']}"/>
            <!-- Watch strap bottom -->
            <rect x="35" y="120" width="50" height="35" fill="#8B4513" rx="5"/>
        </svg>'''
    elif instrument_type == 'phone':
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 180">
            <rect x="10" y="5" width="80" height="170" fill="{COLOURS['dark']}" rx="15"/>
            <rect x="15" y="25" width="70" height="130" fill="#87CEEB"/>
            <text x="50" y="90" font-size="24" font-family="Arial" fill="{COLOURS['dark']}" text-anchor="middle" font-weight="bold">10:30</text>
            <circle cx="50" cy="165" r="8" fill="{COLOURS['grey']}" stroke="{COLOURS['dark']}" stroke-width="1"/>
        </svg>'''
    elif instrument_type == 'wall_clock':
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 150">
            <circle cx="75" cy="75" r="70" fill="#8B4513"/>
            <circle cx="75" cy="75" r="62" fill="{COLOURS['clock_face']}" stroke="{COLOURS['dark']}" stroke-width="2"/>
            <line x1="75" y1="75" x2="75" y2="35" stroke="{COLOURS['dark']}" stroke-width="3"/>
            <line x1="75" y1="75" x2="100" y2="75" stroke="{COLOURS['dark']}" stroke-width="4"/>
            <circle cx="75" cy="75" r="4" fill="{COLOURS['dark']}"/>
            <text x="75" y="28" font-size="12" fill="{COLOURS['dark']}" text-anchor="middle">12</text>
            <text x="75" y="128" font-size="12" fill="{COLOURS['dark']}" text-anchor="middle">6</text>
            <text x="125" y="80" font-size="12" fill="{COLOURS['dark']}" text-anchor="middle">3</text>
            <text x="25" y="80" font-size="12" fill="{COLOURS['dark']}" text-anchor="middle">9</text>
        </svg>'''
    elif instrument_type == 'sundial':
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 100">
            <ellipse cx="75" cy="70" rx="65" ry="25" fill="#C0C0C0" stroke="{COLOURS['dark']}" stroke-width="2"/>
            <polygon points="75,20 80,70 70,70" fill="{COLOURS['dark']}"/>
            <text x="75" y="95" font-size="10" fill="{COLOURS['dark']}" text-anchor="middle">Sundial</text>
        </svg>'''
    else:  # timer/hourglass
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 150">
            <rect x="20" y="5" width="60" height="10" fill="#8B4513"/>
            <rect x="20" y="135" width="60" height="10" fill="#8B4513"/>
            <polygon points="25,15 75,15 60,75 75,135 25,135 40,75" fill="#87CEEB" stroke="{COLOURS['dark']}" stroke-width="2"/>
            <ellipse cx="50" cy="110" rx="20" ry="15" fill="#F4D03F"/>
        </svg>'''
    
    return svg


def generate_calendar_svg(month, day, year=2025):
    """Generate SVG of a calendar page"""
    months = ['', 'January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 180">
        <!-- Calendar frame -->
        <rect x="10" y="10" width="130" height="160" fill="{COLOURS['white']}" stroke="{COLOURS['dark']}" stroke-width="2" rx="5"/>
        <!-- Red header -->
        <rect x="10" y="10" width="130" height="40" fill="{COLOURS['red']}" rx="5"/>
        <rect x="10" y="35" width="130" height="15" fill="{COLOURS['red']}"/>
        <!-- Month name -->
        <text x="75" y="38" font-size="16" font-family="Arial" fill="{COLOURS['white']}" text-anchor="middle" font-weight="bold">{months[month]}</text>
        <!-- Day number -->
        <text x="75" y="120" font-size="60" font-family="Arial" fill="{COLOURS['dark']}" text-anchor="middle" font-weight="bold">{day}</text>
        <!-- Year -->
        <text x="75" y="155" font-size="14" font-family="Arial" fill="{COLOURS['grey']}" text-anchor="middle">{year}</text>
    </svg>'''
    return svg


def generate_timetable_svg(times, activities, title="Timetable"):
    """Generate SVG of a simple timetable"""
    height = 60 + len(times) * 35
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 {height}">
        <rect width="300" height="{height}" fill="{COLOURS['light_grey']}"/>
        <!-- Title -->
        <rect x="10" y="10" width="280" height="30" fill="{COLOURS['blue']}" rx="3"/>
        <text x="150" y="32" font-size="14" font-family="Arial" fill="{COLOURS['white']}" text-anchor="middle" font-weight="bold">{title}</text>
        <!-- Headers -->
        <rect x="10" y="45" width="80" height="25" fill="{COLOURS['grey']}"/>
        <rect x="95" y="45" width="195" height="25" fill="{COLOURS['grey']}"/>
        <text x="50" y="63" font-size="12" font-family="Arial" fill="{COLOURS['white']}" text-anchor="middle">Time</text>
        <text x="192" y="63" font-size="12" font-family="Arial" fill="{COLOURS['white']}" text-anchor="middle">Activity</text>
    '''
    
    y = 75
    for time, activity in zip(times, activities):
        svg += f'''
        <rect x="10" y="{y}" width="80" height="30" fill="{COLOURS['white']}" stroke="{COLOURS['grey']}" stroke-width="1"/>
        <rect x="95" y="{y}" width="195" height="30" fill="{COLOURS['white']}" stroke="{COLOURS['grey']}" stroke-width="1"/>
        <text x="50" y="{y+20}" font-size="11" font-family="Arial" fill="{COLOURS['dark']}" text-anchor="middle">{time}</text>
        <text x="192" y="{y+20}" font-size="11" font-family="Arial" fill="{COLOURS['dark']}" text-anchor="middle">{activity}</text>'''
        y += 30
    
    svg += '\n    </svg>'
    return svg


def generate_bus_timetable_svg(route, stops, times):
    """Generate SVG of a bus timetable"""
    height = 80 + len(stops) * 30
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 {height}">
        <rect width="280" height="{height}" fill="{COLOURS['light_grey']}"/>
        <!-- Header -->
        <rect x="5" y="5" width="270" height="35" fill="{COLOURS['green']}" rx="3"/>
        <text x="140" y="28" font-size="14" font-family="Arial" fill="{COLOURS['white']}" text-anchor="middle" font-weight="bold">🚌 Route {route}</text>
        <!-- Column headers -->
        <rect x="5" y="45" width="130" height="25" fill="{COLOURS['dark']}"/>
        <rect x="140" y="45" width="135" height="25" fill="{COLOURS['dark']}"/>
        <text x="70" y="62" font-size="11" font-family="Arial" fill="{COLOURS['white']}" text-anchor="middle">Stop</text>
        <text x="207" y="62" font-size="11" font-family="Arial" fill="{COLOURS['white']}" text-anchor="middle">Departs</text>
    '''
    
    y = 75
    for stop, time in zip(stops, times):
        svg += f'''
        <rect x="5" y="{y}" width="130" height="28" fill="{COLOURS['white']}" stroke="{COLOURS['grey']}" stroke-width="1"/>
        <rect x="140" y="{y}" width="135" height="28" fill="{COLOURS['white']}" stroke="{COLOURS['grey']}" stroke-width="1"/>
        <text x="70" y="{y+18}" font-size="10" font-family="Arial" fill="{COLOURS['dark']}" text-anchor="middle">{stop}</text>
        <text x="207" y="{y+18}" font-size="11" font-family="Arial" fill="{COLOURS['dark']}" text-anchor="middle" font-weight="bold">{time}</text>'''
        y += 28
    
    svg += '\n    </svg>'
    return svg


# ============================================================
# QUESTION GENERATORS BY LEVEL
# ============================================================

def generate_level_1_questions():
    """Level 1: Time Instruments (Foundation)
    NCCA LO: a - Recognise different instruments for telling the time
    """
    questions = []
    
    # Type 1: Identify time-telling instruments (20 questions)
    instruments = [
        ('watch', 'A watch', 'tells the time on your wrist'),
        ('phone', 'A phone', 'shows the time on its screen'),
        ('wall_clock', 'A wall clock', 'hangs on the wall to show time'),
        ('sundial', 'A sundial', 'uses the sun to tell time'),
        ('timer', 'An hourglass', 'measures time with sand'),
    ]
    
    question_templates = [
        "Which of these can tell the time?",
        "What is this instrument used for?",
        "This object helps us know the time. What is it?",
        "What can you use this for?",
    ]
    
    for i in range(20):
        inst_type, name, purpose = instruments[i % len(instruments)]
        template = question_templates[i % len(question_templates)]
        
        if "Which" in template:
            correct = name
            distractors = ["A book", "A chair", "A cup", "A pencil"]
        else:
            correct = "To tell the time"
            distractors = ["To cook food", "To read books", "To play music", "To make calls"]
        
        distractors = random.sample(distractors, 3)
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"{template} (Look at the picture)",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{name} {purpose}.",
            'question_image_svg': generate_time_instrument_svg(inst_type)
        })
    
    # Type 2: Match instrument to description (15 questions)
    descriptions = [
        ("You wear this on your wrist to see the time", "watch", "A watch"),
        ("This hangs on a wall and has hands that move", "wall_clock", "A wall clock"),
        ("You can check this to see the time on its screen", "phone", "A phone"),
        ("This ancient device uses the sun's shadow", "sundial", "A sundial"),
        ("Sand falls through this to measure time", "timer", "An hourglass"),
    ]
    
    for i in range(15):
        desc, inst_type, correct = descriptions[i % len(descriptions)]
        other_names = [d[2] for d in descriptions if d[2] != correct]
        distractors = random.sample(other_names, 3)
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"{desc}. What is it?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{correct} - {desc.lower()}.",
            'question_image_svg': generate_time_instrument_svg(inst_type)
        })
    
    # Type 3: Yes/No - Can this tell time? (15 questions)
    can_tell_time = [
        ("clock", True, "wall_clock"),
        ("watch", True, "watch"),
        ("phone", True, "phone"),
    ]
    
    for i in range(15):
        item, tells_time, svg_type = can_tell_time[i % len(can_tell_time)]
        
        if tells_time:
            correct = "Yes"
            solution = f"A {item} can tell you what time it is."
        else:
            correct = "No"
            solution = f"A {item} cannot tell you the time."
        
        options = ["Yes", "No", "Sometimes", "Only at night"]
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Can a {item} tell you the time?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': solution,
            'question_image_svg': generate_time_instrument_svg(svg_type)
        })
    
    return questions


def generate_level_2_questions():
    """Level 2: Analogue Clocks (Foundation)
    NCCA LOs: b, g - Identify times on analogue clock, key times of day
    """
    questions = []
    
    # Type 1: O'clock times (20 questions)
    for i in range(20):
        hour = random.randint(1, 12)
        
        correct = f"{hour} o'clock"
        distractors = []
        for h in [hour - 1, hour + 1, hour + 6]:
            h = ((h - 1) % 12) + 1
            if f"{h} o'clock" != correct:
                distractors.append(f"{h} o'clock")
        distractors = distractors[:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        templates = [
            f"What time does this clock show?",
            f"Read the clock. What time is it?",
            f"Look at the clock hands. What is the time?",
        ]
        
        questions.append({
            'question_text': templates[i % 3],
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The short hand points to {hour} and the long hand points to 12. It is {hour} o'clock.",
            'question_image_svg': generate_analogue_clock_svg(hour, 0)
        })
    
    # Type 2: Half past times (15 questions)
    for i in range(15):
        hour = random.randint(1, 12)
        
        correct = f"Half past {hour}"
        distractors = [f"{hour} o'clock", f"Half past {(hour % 12) + 1}", f"Quarter past {hour}"]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"What time is shown on the clock?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The long hand points to 6 (half past) and the short hand is between {hour} and {(hour % 12) + 1}. It is half past {hour}.",
            'question_image_svg': generate_analogue_clock_svg(hour, 30)
        })
    
    # Type 3: Key times of day (15 questions)
    key_times = [
        (7, 0, "breakfast time", "morning"),
        (9, 0, "school starting", "morning"),
        (12, 0, "lunch time", "midday"),
        (3, 0, "school ending", "afternoon"),
        (6, 0, "dinner time", "evening"),
        (8, 0, "bedtime", "night"),
    ]
    
    for i in range(15):
        hour, minute, activity, period = key_times[i % len(key_times)]
        
        correct = f"{hour} o'clock"
        distractors = ["3 o'clock", "6 o'clock", "10 o'clock"]
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"This clock shows {activity} in the {period}. What time is it?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{activity.capitalize()} is usually around {hour} o'clock in the {period}.",
            'question_image_svg': generate_analogue_clock_svg(hour, minute)
        })
    
    return questions


def generate_level_3_questions():
    """Level 3: Digital Clocks (Foundation)
    NCCA LO: c - Read the time from a digital clock
    """
    questions = []
    
    # Type 1: Read digital o'clock (15 questions)
    for i in range(15):
        hour = random.randint(1, 12)
        
        correct = f"{hour} o'clock"
        distractors = []
        for h in [(hour % 12) + 1, ((hour + 5) % 12) + 1, ((hour + 8) % 12) + 1]:
            distractors.append(f"{h} o'clock")
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"What time does this digital clock show?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The display shows {hour}:00 which means {hour} o'clock.",
            'question_image_svg': generate_digital_clock_svg(hour, 0)
        })
    
    # Type 2: Read digital with minutes (20 questions)
    common_minutes = [15, 30, 45]
    
    for i in range(20):
        hour = random.randint(1, 12)
        minutes = random.choice(common_minutes)
        
        if minutes == 30:
            correct = f"Half past {hour}"
            time_display = f"{hour}:30"
        elif minutes == 15:
            correct = f"Quarter past {hour}"
            time_display = f"{hour}:15"
        else:  # 45
            next_hour = (hour % 12) + 1
            correct = f"Quarter to {next_hour}"
            time_display = f"{hour}:45"
        
        distractors = [f"{hour} o'clock", f"Half past {(hour % 12) + 1}", f"{hour}:{minutes:02d}"]
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Read this digital clock. What time is shown?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The display shows {time_display}. This is {correct}.",
            'question_image_svg': generate_digital_clock_svg(hour, minutes)
        })
    
    # Type 3: Match analogue to digital (15 questions)
    for i in range(15):
        hour = random.randint(1, 12)
        minutes = random.choice([0, 30])
        
        correct = f"{hour}:{minutes:02d}"
        distractors = [f"{(hour % 12) + 1}:{minutes:02d}", 
                      f"{hour}:{(minutes + 30) % 60:02d}",
                      f"{((hour + 5) % 12) + 1}:00"]
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Which digital time matches this analogue clock?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The analogue clock shows {hour}:{minutes:02d}.",
            'question_image_svg': generate_analogue_clock_svg(hour, minutes)
        })
    
    return questions


def generate_level_4_questions():
    """Level 4: 12 and 24 Hour Time (Developing)
    NCCA LOs: d, e - 12/24 hour formats, a.m. and p.m.
    """
    questions = []
    
    # Type 1: AM or PM? (15 questions)
    activities = [
        ("eating breakfast", "morning", "AM"),
        ("at school", "morning", "AM"),
        ("eating lunch", "midday", "PM"),
        ("after school", "afternoon", "PM"),
        ("eating dinner", "evening", "PM"),
        ("going to bed", "night", "PM"),
        ("waking up", "morning", "AM"),
        ("watching evening TV", "evening", "PM"),
    ]
    
    for i in range(15):
        activity, period, correct = activities[i % len(activities)]
        
        options = ["AM", "PM", "Both", "Neither"]
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"You are {activity}. Is it AM or PM?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{activity.capitalize()} happens in the {period}, which is {correct}.",
            'question_image_svg': ''
        })
    
    # Type 2: Convert 12-hour to 24-hour (20 questions)
    conversions = [
        (9, "AM", 9, "09:00"),
        (10, "AM", 10, "10:00"),
        (11, "AM", 11, "11:00"),
        (12, "PM", 12, "12:00"),
        (1, "PM", 13, "13:00"),
        (2, "PM", 14, "14:00"),
        (3, "PM", 15, "15:00"),
        (4, "PM", 16, "16:00"),
        (5, "PM", 17, "17:00"),
        (6, "PM", 18, "18:00"),
        (7, "PM", 19, "19:00"),
        (8, "PM", 20, "20:00"),
        (9, "PM", 21, "21:00"),
        (12, "AM", 0, "00:00"),
    ]
    
    for i in range(20):
        hour_12, period, hour_24, display = conversions[i % len(conversions)]
        
        correct = display
        distractors = [f"{(hour_24 + 2) % 24:02d}:00", 
                      f"{(hour_24 - 2) % 24:02d}:00",
                      f"{hour_12:02d}:00"]
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"What is {hour_12} {period} in 24-hour time?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{hour_12} {period} in 24-hour time is {display}.",
            'question_image_svg': generate_digital_clock_svg(hour_24, 0, format_24=True)
        })
    
    # Type 3: Convert 24-hour to 12-hour (15 questions)
    for i in range(15):
        hour_12, period, hour_24, display = conversions[i % len(conversions)]
        
        correct = f"{hour_12} {period}"
        distractors = [f"{(hour_12 % 12) + 1} {period}",
                      f"{hour_12} {'AM' if period == 'PM' else 'PM'}",
                      f"{hour_24} o'clock"]
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"What is {display} in 12-hour time?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{display} (24-hour) is {hour_12} {period} (12-hour).",
            'question_image_svg': generate_digital_clock_svg(hour_24, 0, format_24=True)
        })
    
    return questions


def generate_level_5_questions():
    """Level 5: Time Language (Developing)
    NCCA LO: f - Use language related to time in different settings
    """
    questions = []
    
    # Type 1: Time vocabulary (20 questions)
    vocab = [
        ("How long is 60 seconds?", "1 minute", ["1 hour", "1 day", "1 second"]),
        ("How long is 60 minutes?", "1 hour", ["1 minute", "1 day", "1 second"]),
        ("How long is 24 hours?", "1 day", ["1 hour", "1 week", "1 minute"]),
        ("How many days in a week?", "7", ["5", "10", "12"]),
        ("How many months in a year?", "12", ["10", "7", "52"]),
        ("How many weeks in a year?", "52", ["12", "7", "365"]),
        ("What comes after Monday?", "Tuesday", ["Wednesday", "Sunday", "Friday"]),
        ("What comes before Saturday?", "Friday", ["Sunday", "Thursday", "Monday"]),
        ("Which month comes after March?", "April", ["May", "February", "June"]),
        ("Which month comes before December?", "November", ["October", "January", "September"]),
    ]
    
    for i in range(20):
        question, correct, distractors = vocab[i % len(vocab)]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The answer is {correct}.",
            'question_image_svg': ''
        })
    
    # Type 2: Time of day vocabulary (15 questions)
    times_of_day = [
        ("When does the sun come up?", "Morning", "sunrise"),
        ("When do most people eat lunch?", "Midday", "noon"),
        ("When does it start getting dark?", "Evening", "sunset"),
        ("When do most people sleep?", "Night", "bedtime"),
        ("When do you usually wake up for school?", "Morning", "early"),
        ("3 PM is in the...", "Afternoon", "after lunch"),
        ("9 AM is in the...", "Morning", "before lunch"),
        ("8 PM is in the...", "Evening", "after dinner"),
    ]
    
    for i in range(15):
        question, correct, hint = times_of_day[i % len(times_of_day)]
        distractors = ["Morning", "Afternoon", "Evening", "Night"]
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The answer is {correct} ({hint}).",
            'question_image_svg': ''
        })
    
    # Type 3: Relative time terms (15 questions)
    relative = [
        ("The day before today is called...", "Yesterday", ["Tomorrow", "Today", "Next week"]),
        ("The day after today is called...", "Tomorrow", ["Yesterday", "Today", "Last week"]),
        ("7 days from now is...", "Next week", ["Tomorrow", "Yesterday", "Next month"]),
        ("7 days ago was...", "Last week", ["Next week", "Yesterday", "Tomorrow"]),
        ("In 30 days it will be...", "Next month", ["Tomorrow", "Next week", "Next year"]),
    ]
    
    for i in range(15):
        question, correct, distractors = relative[i % len(relative)]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{correct} - {question.lower().replace('...', '')}.",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_6_questions():
    """Level 6: Units of Time (Developing)
    NCCA LO: h - Seconds/minutes/hours/days/weeks/months relationships
    """
    questions = []
    
    # Type 1: Time conversions (25 questions)
    conversions = [
        ("How many seconds in 1 minute?", 60, "seconds", [30, 100, 45]),
        ("How many minutes in 1 hour?", 60, "minutes", [30, 100, 45]),
        ("How many hours in 1 day?", 24, "hours", [12, 48, 60]),
        ("How many days in 1 week?", 7, "days", [5, 10, 14]),
        ("How many days in 2 weeks?", 14, "days", [7, 21, 10]),
        ("How many weeks in 1 month (about)?", 4, "weeks", [2, 7, 12]),
        ("How many months in 1 year?", 12, "months", [10, 52, 7]),
        ("How many minutes in half an hour?", 30, "minutes", [15, 60, 45]),
        ("How many hours in half a day?", 12, "hours", [6, 24, 8]),
        ("How many seconds in half a minute?", 30, "seconds", [15, 60, 45]),
    ]
    
    for i in range(25):
        question, correct, unit, dist_vals = conversions[i % len(conversions)]
        
        correct_str = str(correct)
        distractors = [str(d) for d in dist_vals]
        
        options = [correct_str] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct_str)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"There are {correct} {unit}.",
            'question_image_svg': ''
        })
    
    # Type 2: Which is longer? (15 questions)
    comparisons = [
        ("1 hour or 30 minutes", "1 hour", "1 hour = 60 minutes > 30 minutes"),
        ("1 day or 20 hours", "1 day", "1 day = 24 hours > 20 hours"),
        ("1 week or 5 days", "1 week", "1 week = 7 days > 5 days"),
        ("2 hours or 100 minutes", "2 hours", "2 hours = 120 minutes > 100 minutes"),
        ("1 month or 3 weeks", "1 month", "1 month ≈ 4 weeks > 3 weeks"),
        ("90 seconds or 1 minute", "90 seconds", "90 seconds > 1 minute (60 seconds)"),
        ("half an hour or 20 minutes", "Half an hour", "30 minutes > 20 minutes"),
    ]
    
    for i in range(15):
        comparison, correct, explanation = comparisons[i % len(comparisons)]
        parts = comparison.split(" or ")
        distractors = [parts[1] if correct == parts[0] else parts[0], 
                      "They are equal", "Cannot tell"]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Which is longer: {comparison}?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': explanation,
            'question_image_svg': ''
        })
    
    # Type 3: Order of time units (10 questions)
    orderings = [
        ("Shortest to longest: hour, minute, day", "minute, hour, day"),
        ("Shortest to longest: week, day, month", "day, week, month"),
        ("Longest to shortest: year, week, day", "year, week, day"),
        ("Shortest to longest: second, minute, hour", "second, minute, hour"),
    ]
    
    for i in range(10):
        question, correct = orderings[i % len(orderings)]
        
        # Generate distractors by shuffling
        parts = correct.split(", ")
        distractors = []
        for _ in range(3):
            shuffled = parts.copy()
            random.shuffle(shuffled)
            d = ", ".join(shuffled)
            if d != correct and d not in distractors:
                distractors.append(d)
        while len(distractors) < 3:
            distractors.append(", ".join(reversed(parts)))
        distractors = distractors[:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The correct order is: {correct}.",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_7_questions():
    """Level 7: Timelines & Timetables (Progressing)
    NCCA LOs: i, j - Interpret and use timelines/timetables
    """
    questions = []
    
    # Type 1: Read simple timetable (25 questions)
    school_activities = [
        (["9:00", "10:00", "11:00", "12:00", "1:00"], 
         ["Assembly", "Maths", "English", "Lunch", "Art"],
         "School Day"),
    ]
    
    for i in range(25):
        times = ["9:00", "10:00", "11:00", "12:00", "1:00", "2:00"]
        activities = ["Assembly", "Maths", "English", "Lunch", "Art", "P.E."]
        
        # Pick a random question type
        q_type = i % 5
        
        if q_type == 0:  # What happens at X time?
            idx = random.randint(0, len(times) - 1)
            correct = activities[idx]
            question = f"Look at the timetable. What happens at {times[idx]}?"
            distractors = [a for a in activities if a != correct][:3]
        elif q_type == 1:  # What time is X?
            idx = random.randint(0, len(activities) - 1)
            correct = times[idx]
            question = f"Look at the timetable. What time is {activities[idx]}?"
            distractors = [t for t in times if t != correct][:3]
        elif q_type == 2:  # What comes after X?
            idx = random.randint(0, len(activities) - 2)
            correct = activities[idx + 1]
            question = f"What activity comes after {activities[idx]}?"
            distractors = [a for a in activities if a != correct][:3]
        elif q_type == 3:  # What comes before X?
            idx = random.randint(1, len(activities) - 1)
            correct = activities[idx - 1]
            question = f"What activity comes before {activities[idx]}?"
            distractors = [a for a in activities if a != correct][:3]
        else:  # How many activities before lunch?
            lunch_idx = activities.index("Lunch")
            correct = str(lunch_idx)
            question = "How many activities are there before Lunch?"
            distractors = [str(lunch_idx - 1), str(lunch_idx + 1), str(lunch_idx + 2)]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"According to the timetable, {correct}.",
            'question_image_svg': generate_timetable_svg(times, activities, "School Timetable")
        })
    
    # Type 2: Daily routine timeline (15 questions)
    routine_times = ["7:00", "8:00", "9:00", "12:30", "3:30", "6:00", "9:00"]
    routine_activities = ["Wake up", "Breakfast", "School starts", "Lunch", "School ends", "Dinner", "Bedtime"]
    
    for i in range(15):
        idx = random.randint(0, len(routine_times) - 1)
        q_type = i % 3
        
        if q_type == 0:
            correct = routine_activities[idx]
            question = f"What usually happens at {routine_times[idx]}?"
            distractors = [a for a in routine_activities if a != correct][:3]
        elif q_type == 1:
            correct = routine_times[idx]
            question = f"What time is {routine_activities[idx]}?"
            distractors = [t for t in routine_times if t != correct][:3]
        else:
            if idx < len(routine_activities) - 1:
                correct = routine_activities[idx + 1]
                question = f"What comes after {routine_activities[idx]}?"
            else:
                correct = routine_activities[idx - 1]
                question = f"What comes before {routine_activities[idx]}?"
            distractors = [a for a in routine_activities if a != correct][:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"In a typical daily routine, {correct}.",
            'question_image_svg': generate_timetable_svg(routine_times, routine_activities, "Daily Routine")
        })
    
    # Type 3: Bus timetable (10 questions)
    for i in range(10):
        stops = ["City Centre", "Main Street", "School Road", "Park Avenue", "Shopping Centre"]
        base_time = random.randint(8, 16)
        times = [f"{base_time}:00", f"{base_time}:10", f"{base_time}:18", f"{base_time}:25", f"{base_time}:35"]
        route = random.randint(15, 99)
        
        stop_idx = random.randint(0, len(stops) - 1)
        correct = times[stop_idx]
        question = f"When does the bus leave {stops[stop_idx]}?"
        distractors = [t for t in times if t != correct][:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The bus leaves {stops[stop_idx]} at {correct}.",
            'question_image_svg': generate_bus_timetable_svg(route, stops, times)
        })
    
    return questions


def generate_level_8_questions():
    """Level 8: Calculating Time (Progressing)
    NCCA LO: k - Calculate and interpret passage of time
    """
    questions = []
    
    # Type 1: Time elapsed - simple hours (20 questions)
    for i in range(20):
        start_hour = random.randint(8, 16)
        duration = random.randint(1, 4)
        end_hour = start_hour + duration
        
        correct = f"{duration} hour{'s' if duration > 1 else ''}"
        distractors = [f"{duration + 1} hours", f"{duration - 1} hour{'s' if duration > 1 else ''}", f"{duration + 2} hours"]
        distractors = [d for d in distractors if d != correct and "0 hour" not in d and "-" not in d][:3]
        while len(distractors) < 3:
            distractors.append(f"{random.randint(1, 5)} hours")
        
        options = [correct] + distractors[:3]
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        templates = [
            f"A film starts at {start_hour}:00 and ends at {end_hour}:00. How long is it?",
            f"You arrive at {start_hour}:00 and leave at {end_hour}:00. How long were you there?",
            f"School starts at {start_hour}:00 and break is at {end_hour}:00. How long until break?",
        ]
        
        questions.append({
            'question_text': templates[i % 3],
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"From {start_hour}:00 to {end_hour}:00 is {duration} hour{'s' if duration > 1 else ''}.",
            'question_image_svg': ''
        })
    
    # Type 2: Time elapsed with minutes (15 questions)
    for i in range(15):
        start_hour = random.randint(9, 15)
        start_min = random.choice([0, 15, 30])
        duration_min = random.choice([15, 30, 45, 60])
        
        end_min = start_min + duration_min
        end_hour = start_hour
        if end_min >= 60:
            end_min -= 60
            end_hour += 1
        
        if duration_min == 60:
            correct = "1 hour"
        elif duration_min < 60:
            correct = f"{duration_min} minutes"
        
        distractors = ["15 minutes", "30 minutes", "45 minutes", "1 hour"]
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"From {start_hour}:{start_min:02d} to {end_hour}:{end_min:02d}, how much time passes?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"From {start_hour}:{start_min:02d} to {end_hour}:{end_min:02d} is {correct}.",
            'question_image_svg': ''
        })
    
    # Type 3: What time will it be? (15 questions)
    for i in range(15):
        start_hour = random.randint(9, 18)
        add_hours = random.randint(1, 3)
        end_hour = start_hour + add_hours
        
        correct = f"{end_hour}:00"
        distractors = [f"{end_hour - 1}:00", f"{end_hour + 1}:00", f"{start_hour}:00"]
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"It is {start_hour}:00 now. What time will it be in {add_hours} hour{'s' if add_hours > 1 else ''}?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{start_hour}:00 + {add_hours} hour{'s' if add_hours > 1 else ''} = {correct}.",
            'question_image_svg': generate_analogue_clock_svg(start_hour, 0)
        })
    
    return questions


def generate_level_9_questions():
    """Level 9: Time Management Skills (Progressing)
    NCCA LOs: l, m, n - Time management, sequence events, estimate time
    """
    questions = []
    
    # Type 1: Allow enough time (20 questions)
    scenarios = [
        ("The bus comes at 8:30. It takes 15 minutes to walk to the bus stop. What time should you leave home?", "8:15", ["8:30", "8:00", "8:45"]),
        ("School starts at 9:00. It takes 20 minutes to get ready. What time should you wake up?", "8:40", ["9:00", "8:20", "9:20"]),
        ("The film starts at 7:00. It takes 30 minutes to get there. What time should you leave?", "6:30", ["7:00", "6:00", "7:30"]),
        ("Dinner is at 6:00. It takes 45 minutes to cook. What time should you start?", "5:15", ["6:00", "5:45", "5:00"]),
        ("The train leaves at 10:15. It takes 10 minutes to buy a ticket. What time should you arrive?", "10:05", ["10:15", "10:00", "10:25"]),
    ]
    
    for i in range(20):
        question, correct, distractors = scenarios[i % len(scenarios)]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"You should start/leave at {correct} to have enough time.",
            'question_image_svg': ''
        })
    
    # Type 2: Estimate time for activities (15 questions)
    estimates = [
        ("How long does it take to brush your teeth?", "2 minutes", ["2 hours", "30 minutes", "30 seconds"]),
        ("How long does it take to watch a film?", "2 hours", ["2 minutes", "10 hours", "30 seconds"]),
        ("How long does it take to boil an egg?", "10 minutes", ["10 seconds", "2 hours", "1 second"]),
        ("How long is a school day?", "6 hours", ["6 minutes", "1 hour", "24 hours"]),
        ("How long does it take to eat lunch?", "30 minutes", ["30 seconds", "3 hours", "5 seconds"]),
        ("How long does it take to walk 1 km?", "10-15 minutes", ["1 minute", "2 hours", "5 seconds"]),
        ("How long does a football match last?", "90 minutes", ["9 minutes", "9 hours", "90 seconds"]),
    ]
    
    for i in range(15):
        question, correct, distractors = estimates[i % len(estimates)]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"This typically takes about {correct}.",
            'question_image_svg': ''
        })
    
    # Type 3: Sequence daily activities (15 questions)
    sequences = [
        ("What should you do first in the morning?", "Wake up", ["Eat dinner", "Go to bed", "Watch TV"]),
        ("What comes after getting dressed?", "Eating breakfast", ["Sleeping", "Taking a shower", "Going to bed"]),
        ("Before leaving for school, you should...", "Pack your bag", ["Go to sleep", "Eat dinner", "Watch a film"]),
        ("After school, you usually...", "Go home", ["Wake up", "Eat breakfast", "Start school"]),
        ("Before bed, you should...", "Brush your teeth", ["Eat breakfast", "Go to school", "Wake up"]),
    ]
    
    for i in range(15):
        question, correct, distractors = sequences[i % len(sequences)]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The correct answer is: {correct}.",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_10_questions():
    """Level 10: Daily Routines (Consolidating)
    NCCA LOs: m, o - Sequence events, undertake activity within time
    """
    questions = []
    
    # Type 1: Plan a morning routine (20 questions)
    morning_tasks = [
        ("shower", 15),
        ("get dressed", 10),
        ("eat breakfast", 20),
        ("brush teeth", 3),
        ("pack bag", 5),
        ("walk to bus stop", 10),
    ]
    
    for i in range(20):
        # Pick 3-4 random tasks
        num_tasks = random.randint(3, 4)
        selected = random.sample(morning_tasks, num_tasks)
        total_time = sum(t[1] for t in selected)
        
        task_names = [t[0] for t in selected]
        task_times = [f"{t[1]} min" for t in selected]
        
        correct = f"{total_time} minutes"
        distractors = [f"{total_time + 10} minutes", f"{total_time - 10} minutes", f"{total_time + 20} minutes"]
        distractors = [d for d in distractors if d != correct and int(d.split()[0]) > 0][:3]
        while len(distractors) < 3:
            distractors.append(f"{random.randint(20, 60)} minutes")
        
        options = [correct] + distractors[:3]
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        task_list = ", ".join([f"{t[0]} ({t[1]} min)" for t in selected])
        
        questions.append({
            'question_text': f"You need to: {task_list}. How long will this take in total?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"Adding the times: {' + '.join([str(t[1]) for t in selected])} = {total_time} minutes.",
            'question_image_svg': ''
        })
    
    # Type 2: Will you be on time? (15 questions)
    for i in range(15):
        need_time = random.randint(30, 60)
        have_time = need_time + random.choice([-15, -10, -5, 0, 5, 10, 15])
        
        if have_time >= need_time:
            correct = "Yes"
            solution = f"You have {have_time} minutes and need {need_time} minutes. You have enough time!"
        else:
            correct = "No"
            solution = f"You have {have_time} minutes but need {need_time} minutes. You need {need_time - have_time} more minutes."
        
        options = ["Yes", "No", "Maybe", "Cannot tell"]
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"You have {have_time} minutes. Your tasks will take {need_time} minutes. Will you be on time?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': solution,
            'question_image_svg': ''
        })
    
    # Type 3: Order of activities (15 questions)
    activity_orders = [
        ("Put these in order: eat breakfast, wake up, get dressed", "wake up, get dressed, eat breakfast"),
        ("Put these in order: go to bed, eat dinner, brush teeth", "eat dinner, brush teeth, go to bed"),
        ("Put these in order: arrive at school, leave home, pack bag", "pack bag, leave home, arrive at school"),
        ("Put these in order: eat lunch, morning classes, afternoon classes", "morning classes, eat lunch, afternoon classes"),
    ]
    
    for i in range(15):
        question, correct = activity_orders[i % len(activity_orders)]
        
        parts = correct.split(", ")
        distractors = []
        for _ in range(3):
            shuffled = parts.copy()
            random.shuffle(shuffled)
            d = ", ".join(shuffled)
            if d != correct and d not in distractors:
                distractors.append(d)
        while len(distractors) < 3:
            distractors.append(", ".join(reversed(parts)))
        
        options = [correct] + distractors[:3]
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The correct order is: {correct}.",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_11_questions():
    """Level 11: Calendars & Planning (Consolidating)
    NCCA LOs: p, s - Use calendars, date formats, forward planning
    """
    questions = []
    
    # Type 1: Read calendar dates (20 questions)
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    
    for i in range(20):
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        
        q_type = i % 4
        
        if q_type == 0:
            correct = months[month - 1]
            question = f"What month is shown on this calendar?"
            distractors = random.sample([m for m in months if m != correct], 3)
        elif q_type == 1:
            correct = str(day)
            question = f"What day of the month is shown?"
            distractors = [str(day + 1), str(day - 1), str(day + 10)]
            distractors = [d for d in distractors if int(d) > 0 and int(d) <= 31][:3]
        elif q_type == 2:
            correct = f"{day}/{month}/2025"
            question = f"Write this date in DD/MM/YYYY format."
            distractors = [f"{month}/{day}/2025", f"{day}/{month + 1}/2025", f"{day + 1}/{month}/2025"]
        else:
            correct = f"{day} {months[month - 1]} 2025"
            question = f"Write this date in words."
            distractors = [f"{day + 1} {months[month - 1]} 2025", 
                         f"{day} {months[(month) % 12]} 2025",
                         f"{month} {months[month - 1]} 2025"]
        
        while len(distractors) < 3:
            distractors.append(f"{random.randint(1, 28)}/{random.randint(1, 12)}/2025")
        
        options = [correct] + distractors[:3]
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The answer is {correct}.",
            'question_image_svg': generate_calendar_svg(month, day)
        })
    
    # Type 2: Days until event (15 questions)
    for i in range(15):
        days_until = random.randint(3, 14)
        event = random.choice(["birthday party", "doctor appointment", "school trip", "concert", "exam"])
        
        correct = f"{days_until} days"
        distractors = [f"{days_until + 1} days", f"{days_until - 1} days", f"{days_until + 7} days"]
        distractors = [d for d in distractors if d != correct and int(d.split()[0]) > 0][:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': f"Today is the 1st. Your {event} is on the {1 + days_until}th. How many days until the {event}?",
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"From the 1st to the {1 + days_until}th is {days_until} days.",
            'question_image_svg': ''
        })
    
    # Type 3: Date format conversions (15 questions)
    formats = [
        ("15/03/2025", "15 March 2025", "DD/MM/YYYY to words"),
        ("22/07/2025", "22 July 2025", "DD/MM/YYYY to words"),
        ("01/12/2025", "1 December 2025", "DD/MM/YYYY to words"),
        ("30/09/2025", "30 September 2025", "DD/MM/YYYY to words"),
    ]
    
    for i in range(15):
        numeric, written, desc = formats[i % len(formats)]
        
        q_type = i % 2
        if q_type == 0:
            question = f"Write {numeric} in words."
            correct = written
            distractors = ["15 July 2025", "22 March 2025", "1 September 2025"]
        else:
            question = f"Write '{written}' in DD/MM/YYYY format."
            correct = numeric
            distractors = ["03/15/2025", "2025/03/15", "15-03-2025"]
        
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"{numeric} = {written}",
            'question_image_svg': ''
        })
    
    return questions


def generate_level_12_questions():
    """Level 12: Journey Planning (Consolidating)
    NCCA LOs: q, r - Transport timetables, plan entire day including journey
    """
    questions = []
    
    # Type 1: Bus journey calculations (20 questions)
    for i in range(20):
        depart_hour = random.randint(8, 14)
        depart_min = random.choice([0, 15, 30, 45])
        journey_min = random.choice([15, 20, 25, 30, 35, 40, 45])
        
        arrive_min = depart_min + journey_min
        arrive_hour = depart_hour
        if arrive_min >= 60:
            arrive_min -= 60
            arrive_hour += 1
        
        q_type = i % 4
        
        if q_type == 0:
            correct = f"{arrive_hour}:{arrive_min:02d}"
            question = f"The bus leaves at {depart_hour}:{depart_min:02d}. The journey takes {journey_min} minutes. What time will you arrive?"
            distractors = [f"{arrive_hour}:{(arrive_min + 15) % 60:02d}", 
                         f"{arrive_hour - 1}:{arrive_min:02d}",
                         f"{arrive_hour}:{(arrive_min + 30) % 60:02d}"]
        elif q_type == 1:
            correct = f"{journey_min} minutes"
            question = f"The bus leaves at {depart_hour}:{depart_min:02d} and arrives at {arrive_hour}:{arrive_min:02d}. How long is the journey?"
            distractors = [f"{journey_min + 10} minutes", f"{journey_min - 10} minutes", f"{journey_min + 15} minutes"]
            distractors = [d for d in distractors if int(d.split()[0]) > 0]
        elif q_type == 2:
            walk_time = 10
            leave_home_min = depart_min - walk_time
            leave_home_hour = depart_hour
            if leave_home_min < 0:
                leave_home_min += 60
                leave_home_hour -= 1
            correct = f"{leave_home_hour}:{leave_home_min:02d}"
            question = f"The bus leaves at {depart_hour}:{depart_min:02d}. It takes 10 minutes to walk to the stop. What time should you leave home?"
            distractors = [f"{depart_hour}:{depart_min:02d}", 
                         f"{leave_home_hour}:{(leave_home_min + 5) % 60:02d}",
                         f"{leave_home_hour}:{(leave_home_min - 5) % 60:02d}"]
        else:
            correct = "Check the timetable"
            question = f"How do you find out when the next bus to town leaves?"
            distractors = ["Guess the time", "Wait all day", "Don't take the bus"]
        
        while len(distractors) < 3:
            distractors.append(f"{random.randint(8, 18)}:{random.choice([0, 15, 30, 45]):02d}")
        
        options = [correct] + distractors[:3]
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The answer is {correct}.",
            'question_image_svg': ''
        })
    
    # Type 2: Plan a day trip (15 questions)
    trips = [
        {
            'destination': 'Dublin Zoo',
            'bus_time': '9:00',
            'journey': 45,
            'arrive': '9:45',
            'open': '10:00',
            'activities': 3,
            'activity_time': 60,
            'lunch': '12:00',
            'leave': '15:00',
            'home': '15:45'
        },
    ]
    
    trip = trips[0]
    
    for i in range(15):
        q_type = i % 5
        
        if q_type == 0:
            correct = trip['arrive']
            question = f"The bus to {trip['destination']} leaves at {trip['bus_time']} and takes {trip['journey']} minutes. What time will you arrive?"
            distractors = ["10:00", "9:30", "10:15"]
        elif q_type == 1:
            correct = f"{trip['activity_time'] * trip['activities']} minutes"
            question = f"You plan to do {trip['activities']} activities, each taking {trip['activity_time']} minutes. How long will the activities take?"
            distractors = ["120 minutes", "60 minutes", "240 minutes"]
        elif q_type == 2:
            correct = trip['home']
            question = f"You leave {trip['destination']} at {trip['leave']}. The journey home takes {trip['journey']} minutes. What time will you get home?"
            distractors = ["15:30", "16:00", "15:15"]
        elif q_type == 3:
            total_hours = 6
            correct = f"{total_hours} hours"
            question = f"You arrive at {trip['arrive']} and leave at {trip['leave']}. How long is your visit?"
            distractors = ["5 hours", "7 hours", "4 hours"]
        else:
            correct = "Before the zoo opens"
            question = f"You arrive at {trip['arrive']} and the zoo opens at {trip['open']}. Will you have to wait?"
            distractors = ["No waiting needed", "You'll miss the opening", "The zoo is closed"]
        
        distractors = [d for d in distractors if d != correct][:3]
        
        options = [correct] + distractors
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The answer is {correct}.",
            'question_image_svg': ''
        })
    
    # Type 3: Multiple transport connections (15 questions)
    for i in range(15):
        bus1_depart = f"{random.randint(8, 10)}:{random.choice([0, 15, 30]):02d}"
        bus1_journey = random.choice([20, 25, 30])
        wait_time = random.choice([5, 10, 15])
        bus2_journey = random.choice([15, 20, 25])
        
        # Calculate times
        h1, m1 = map(int, bus1_depart.split(':'))
        m1 += bus1_journey
        if m1 >= 60:
            m1 -= 60
            h1 += 1
        bus1_arrive = f"{h1}:{m1:02d}"
        
        m1 += wait_time
        if m1 >= 60:
            m1 -= 60
            h1 += 1
        bus2_depart = f"{h1}:{m1:02d}"
        
        m1 += bus2_journey
        if m1 >= 60:
            m1 -= 60
            h1 += 1
        final_arrive = f"{h1}:{m1:02d}"
        
        total_time = bus1_journey + wait_time + bus2_journey
        
        q_type = i % 3
        
        if q_type == 0:
            correct = final_arrive
            question = f"Bus 1 leaves at {bus1_depart} ({bus1_journey} min). You wait {wait_time} min, then Bus 2 takes {bus2_journey} min. What time do you arrive?"
            distractors = [f"{h1}:{(m1 + 10) % 60:02d}", f"{h1 - 1}:{m1:02d}", f"{h1}:{(m1 + 20) % 60:02d}"]
        elif q_type == 1:
            correct = f"{total_time} minutes"
            question = f"Bus 1 takes {bus1_journey} min. You wait {wait_time} min. Bus 2 takes {bus2_journey} min. What is the total journey time?"
            distractors = [f"{total_time + 10} minutes", f"{total_time - 10} minutes", f"{bus1_journey + bus2_journey} minutes"]
        else:
            correct = bus2_depart
            question = f"Bus 1 arrives at {bus1_arrive}. You wait {wait_time} minutes. What time does Bus 2 leave?"
            distractors = [bus1_arrive, f"{h1}:{(m1 + 5) % 60:02d}", f"{h1}:{(m1 - 5) % 60:02d}"]
        
        distractors = [d for d in distractors if d != correct][:3]
        while len(distractors) < 3:
            distractors.append(f"{random.randint(9, 12)}:{random.choice([0, 15, 30, 45]):02d}")
        
        options = [correct] + distractors[:3]
        while len(options) < 4: options.append(str(random.randint(1, 99)))
        random.shuffle(options)
        correct_letter = ['A', 'B', 'C', 'D'][options.index(correct)]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_answer': correct_letter,
            'solution': f"The answer is {correct}.",
            'question_image_svg': ''
        })
    
    return questions


# ============================================================
# MAIN GENERATION FUNCTIONS
# ============================================================

def generate_all_questions():
    """Generate all questions for all levels"""
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
        
        # Ensure exactly 50 questions per level
        if len(questions) < QUESTIONS_PER_LEVEL:
            print(f"    Warning: Level {level} has only {len(questions)} questions")
        elif len(questions) > QUESTIONS_PER_LEVEL:
            questions = questions[:QUESTIONS_PER_LEVEL]
        
        for q in questions:
            q['level'] = level
            q['topic'] = TOPIC
            q['difficulty'] = DIFFICULTY
        
        all_questions.extend(questions)
        print(f"    Level {level}: {len(questions)} questions generated")
    
    return all_questions


def validate_questions(questions):
    """Validate all questions before insertion"""
    errors = []
    
    for i, q in enumerate(questions):
        if not q.get('question_text'):
            errors.append(f"Q{i+1}: Missing question_text")
        
        if not q.get('correct_answer') in ['A', 'B', 'C', 'D']:
            errors.append(f"Q{i+1}: Invalid correct_answer: {q.get('correct_answer')}")
        
        if not q.get('option_a'):
            errors.append(f"Q{i+1}: Missing option_a")
        
        if not q.get('option_b'):
            errors.append(f"Q{i+1}: Missing option_b")
        
        correct = q.get('correct_answer', '')
        if correct:
            correct_option = q.get(f'option_{correct.lower()}', '')
            if not correct_option:
                errors.append(f"Q{i+1}: Correct answer {correct} but option is empty")
    
    # Check for duplicates (visual questions with same text are OK if SVG differs)
    seen_text_only = set()
    seen_visual = {}
    
    for i, q in enumerate(questions):
        text = q['question_text']
        svg = q.get('question_image_svg', '')
        
        if svg:
            svg_hash = hash(svg)
            if text in seen_visual:
                if svg_hash in seen_visual[text]:
                    errors.append(f"Duplicate question found: '{text[:50]}...'")
                else:
                    seen_visual[text].add(svg_hash)
            else:
                seen_visual[text] = {svg_hash}
        else:
            if text in seen_text_only:
                errors.append(f"Duplicate question found: '{text[:50]}...'")
            seen_text_only.add(text)
    
    return errors


def count_existing_questions():
    """Count existing questions for this topic"""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT level, COUNT(*) FROM questions WHERE topic = ? GROUP BY level', (TOPIC,))
        counts = dict(cursor.fetchall())
        conn.close()
        return counts
    except:
        return {}


def clear_existing_questions():
    """Clear existing questions for this topic"""
    counts = count_existing_questions()
    total = sum(counts.values())
    
    if total > 0:
        print(f"\n⚠️  Found {total} existing questions for {TOPIC}")
        response = input("Delete existing questions? (yes/no): ").strip().lower()
        if response == 'yes':
            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()
            cursor.execute('DELETE FROM questions WHERE topic = ?', (TOPIC,))
            deleted = cursor.rowcount
            conn.commit()
            conn.close()
            print(f"   Deleted {deleted} questions")
            return True
        else:
            print("   Keeping existing questions")
            return False
    return True


def insert_questions(questions):
    """Insert questions into database"""
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
                q['topic'], 
                q['difficulty'], 
                q['level'],
                q['question_text'], 
                q['option_a'], 
                q['option_b'], 
                q.get('option_c', ''), 
                q.get('option_d', ''),
                q['correct_answer'], 
                q.get('solution', ''),
                q.get('question_image_svg', '')
            ))
            inserted += 1
        except sqlite3.Error as e:
            print(f"Error inserting question: {e}")
            print(f"Question: {q['question_text'][:50]}...")
    
    conn.commit()
    conn.close()
    return inserted


def main():
    """Main entry point"""
    print("=" * 60)
    print("AgentMath L2LP Question Generator")
    print(f"Topic: {TOPIC}")
    print(f"Target: {QUESTIONS_PER_LEVEL} questions × {TOTAL_LEVELS} levels = {QUESTIONS_PER_LEVEL * TOTAL_LEVELS} total")
    print("=" * 60)
    
    if not clear_existing_questions():
        print("\nAborting to preserve existing questions.")
        return
    
    print("\nGenerating questions...")
    questions = generate_all_questions()
    
    print(f"\nTotal questions generated: {len(questions)}")
    
    print("\nValidating questions...")
    errors = validate_questions(questions)
    
    critical_errors = [e for e in errors if 'Duplicate' not in e]
    duplicate_warnings = [e for e in errors if 'Duplicate' in e]
    
    if critical_errors:
        print(f"\n❌ Found {len(critical_errors)} critical errors:")
        for error in critical_errors[:10]:
            print(f"   - {error}")
        response = input("\nContinue anyway? (yes/no): ").strip().lower()
        if response != 'yes':
            print("Aborting.")
            return
    
    if duplicate_warnings:
        print(f"\n⚠️  Found {len(duplicate_warnings)} duplicate warnings (non-blocking)")
    
    if not critical_errors and not duplicate_warnings:
        print("✅ All questions validated successfully!")
    
    print("\nInserting questions into database...")
    inserted = insert_questions(questions)
    
    print(f"\n✅ Successfully inserted {inserted} questions!")
    
    # Summary
    print("\nQuestions per level:")
    level_counts = {}
    for q in questions:
        level = q['level']
        level_counts[level] = level_counts.get(level, 0) + 1
    
    for level in sorted(level_counts.keys()):
        print(f"   Level {level}: {level_counts[level]} questions")
    
    print("\nVisual question check:")
    for level in range(1, 13):
        level_qs = [q for q in questions if q['level'] == level]
        visual_count = sum(1 for q in level_qs if q.get('question_image_svg'))
        visual_pct = (visual_count / len(level_qs) * 100) if level_qs else 0
        target = get_visual_percentage(level)
        status = "✅" if visual_pct >= target - 15 else "⚠️"
        print(f"   Level {level}: {visual_pct:.0f}% visual (target: {target}%) {status}")


if __name__ == '__main__':
    main()
