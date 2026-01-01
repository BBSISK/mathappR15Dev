"""
AgentMath L1LP Question Generator
Topic: Time
Learning Outcomes: 2.26 - 2.29
Version: 1.0

Generates 600 questions (50 per level × 12 levels) for the L1LP strand.
Focus: Morning/night, times of day, days of week, daily routines, seasons, o'clock times, before/after, timers, visual timetables.

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
TOPIC = 'time'
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
    'purple': '#9B59B6',
    'pink': '#FF69B4',
    'grey': '#7F8C8D'
}

# Days of the week
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Seasons
SEASONS = ['Spring', 'Summer', 'Autumn', 'Winter']

# =============================================================================
# SVG GENERATION FUNCTIONS
# =============================================================================

def create_svg_wrapper(content, width=400, height=180):
    """Wrap SVG content"""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background: white;">{content}</svg>'

def svg_sun(x, y, size=60):
    """Generate a sun"""
    cx, cy = x + size//2, y + size//2
    rays = ''
    for i in range(8):
        angle = i * 45 * math.pi / 180
        x1 = cx + (size//3) * math.cos(angle)
        y1 = cy + (size//3) * math.sin(angle)
        x2 = cx + (size//2) * math.cos(angle)
        y2 = cy + (size//2) * math.sin(angle)
        rays += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#F1C40F" stroke-width="3"/>'
    
    return f'{rays}<circle cx="{cx}" cy="{cy}" r="{size//3}" fill="#F1C40F"/>'

def svg_moon(x, y, size=60):
    """Generate a crescent moon"""
    cx, cy = x + size//2, y + size//2
    return f'''<g>
        <circle cx="{cx}" cy="{cy}" r="{size//3}" fill="#F4D03F"/>
        <circle cx="{cx + size//6}" cy="{cy - size//8}" r="{size//4}" fill="white"/>
    </g>'''

def svg_stars(x, y, width=100, height=60):
    """Generate scattered stars"""
    stars = ''
    for i in range(5):
        sx = x + random.randint(10, width - 10)
        sy = y + random.randint(10, height - 10)
        size = random.randint(3, 6)
        stars += f'<polygon points="{sx},{sy-size} {sx+size//2},{sy+size//2} {sx-size//2},{sy+size//2}" fill="#F4D03F"/>'
    return stars

def svg_clock(x, y, size=80, hour=12, minute=0):
    """Generate an analog clock showing a specific time"""
    cx, cy = x + size//2, y + size//2
    radius = size//2 - 5
    
    # Clock face
    face = f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="white" stroke="#333" stroke-width="3"/>'
    
    # Hour markers
    markers = ''
    for i in range(12):
        angle = (i * 30 - 90) * math.pi / 180
        x1 = cx + (radius - 8) * math.cos(angle)
        y1 = cy + (radius - 8) * math.sin(angle)
        x2 = cx + (radius - 3) * math.cos(angle)
        y2 = cy + (radius - 3) * math.sin(angle)
        markers += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#333" stroke-width="2"/>'
    
    # Hour numbers (12, 3, 6, 9)
    numbers = ''
    number_positions = [(12, 0, -radius + 15), (3, radius - 15, 5), (6, 0, radius - 10), (9, -radius + 15, 5)]
    for num, dx, dy in number_positions:
        numbers += f'<text x="{cx + dx}" y="{cy + dy}" text-anchor="middle" font-size="12" font-weight="bold" fill="#333">{num}</text>'
    
    # Hour hand
    hour_angle = ((hour % 12) * 30 + minute * 0.5 - 90) * math.pi / 180
    hour_len = radius * 0.5
    hx = cx + hour_len * math.cos(hour_angle)
    hy = cy + hour_len * math.sin(hour_angle)
    hour_hand = f'<line x1="{cx}" y1="{cy}" x2="{hx}" y2="{hy}" stroke="#333" stroke-width="4" stroke-linecap="round"/>'
    
    # Minute hand
    minute_angle = (minute * 6 - 90) * math.pi / 180
    minute_len = radius * 0.7
    mx = cx + minute_len * math.cos(minute_angle)
    my = cy + minute_len * math.sin(minute_angle)
    minute_hand = f'<line x1="{cx}" y1="{cy}" x2="{mx}" y2="{my}" stroke="#E74C3C" stroke-width="3" stroke-linecap="round"/>'
    
    # Center dot
    center = f'<circle cx="{cx}" cy="{cy}" r="4" fill="#333"/>'
    
    return face + markers + numbers + hour_hand + minute_hand + center

def svg_digital_clock(x, y, hour, minute=0):
    """Generate a digital clock display"""
    time_str = f'{hour}:{minute:02d}'
    return f'''<g transform="translate({x},{y})">
        <rect x="0" y="0" width="80" height="45" fill="#1a1a1a" rx="5"/>
        <text x="40" y="32" text-anchor="middle" font-size="24" font-family="monospace" fill="#00FF00">{time_str}</text>
    </g>'''

def svg_morning_scene():
    """Generate a morning scene"""
    svg = ''
    # Sky gradient (light blue)
    svg += f'<rect x="0" y="0" width="400" height="120" fill="#87CEEB"/>'
    # Sun
    svg += svg_sun(300, 20, 50)
    # Ground
    svg += f'<rect x="0" y="120" width="400" height="60" fill="#90EE90"/>'
    # House
    svg += f'<rect x="50" y="70" width="80" height="50" fill="#DEB887"/>'
    svg += f'<polygon points="50,70 90,40 130,70" fill="#8B4513"/>'
    # Person waking
    svg += f'<circle cx="250" cy="100" r="15" fill="#FFDAB9"/>'
    svg += f'<text x="250" y="140" text-anchor="middle" font-size="10">Good morning!</text>'
    return create_svg_wrapper(svg)

def svg_night_scene():
    """Generate a night scene"""
    svg = ''
    # Sky (dark blue)
    svg += f'<rect x="0" y="0" width="400" height="120" fill="#1a1a2e"/>'
    # Moon
    svg += svg_moon(300, 15, 40)
    # Stars
    svg += svg_stars(50, 20, 200, 80)
    # Ground (dark)
    svg += f'<rect x="0" y="120" width="400" height="60" fill="#2d4a3e"/>'
    # House with light in window
    svg += f'<rect x="50" y="70" width="80" height="50" fill="#4a4a4a"/>'
    svg += f'<polygon points="50,70 90,40 130,70" fill="#333"/>'
    svg += f'<rect x="70" y="85" width="20" height="20" fill="#F1C40F"/>'
    # Bed icon
    svg += f'<text x="250" y="100" text-anchor="middle" font-size="30">🛏️</text>'
    svg += f'<text x="250" y="140" text-anchor="middle" font-size="10">Good night!</text>'
    return create_svg_wrapper(svg)

def svg_season_scene(season):
    """Generate a scene for each season"""
    svg = ''
    
    if season == 'Spring':
        svg += f'<rect x="0" y="0" width="400" height="120" fill="#87CEEB"/>'
        svg += f'<rect x="0" y="120" width="400" height="60" fill="#90EE90"/>'
        # Flowers
        for i in range(5):
            x = 50 + i * 70
            svg += f'<circle cx="{x}" cy="140" r="10" fill="#FF69B4"/>'
            svg += f'<circle cx="{x}" cy="140" r="4" fill="#F1C40F"/>'
            svg += f'<rect x="{x-2}" y="150" width="4" height="15" fill="#27AE60"/>'
        svg += f'<text x="200" y="30" text-anchor="middle" font-size="16" fill="#333">🌸 Spring 🌷</text>'
        
    elif season == 'Summer':
        svg += f'<rect x="0" y="0" width="400" height="100" fill="#87CEEB"/>'
        svg += svg_sun(320, 10, 50)
        svg += f'<rect x="0" y="100" width="400" height="80" fill="#F4D03F"/>'  # Beach
        svg += f'<rect x="0" y="140" width="400" height="40" fill="#3498DB"/>'  # Sea
        svg += f'<text x="200" y="30" text-anchor="middle" font-size="16" fill="#333">☀️ Summer 🏖️</text>'
        
    elif season == 'Autumn':
        svg += f'<rect x="0" y="0" width="400" height="120" fill="#B0C4DE"/>'
        svg += f'<rect x="0" y="120" width="400" height="60" fill="#8B7355"/>'
        # Falling leaves
        colours = ['#E74C3C', '#E67E22', '#F1C40F', '#D35400']
        for i in range(8):
            x = random.randint(30, 370)
            y = random.randint(40, 100)
            svg += f'<ellipse cx="{x}" cy="{y}" rx="8" ry="5" fill="{random.choice(colours)}"/>'
        # Tree with few leaves
        svg += f'<rect x="180" y="80" width="20" height="50" fill="#8B4513"/>'
        svg += f'<circle cx="190" cy="60" r="30" fill="#D35400"/>'
        svg += f'<text x="200" y="30" text-anchor="middle" font-size="16" fill="#333">🍂 Autumn 🍁</text>'
        
    else:  # Winter
        svg += f'<rect x="0" y="0" width="400" height="120" fill="#B0C4DE"/>'
        svg += f'<rect x="0" y="120" width="400" height="60" fill="white"/>'
        # Snowflakes
        for i in range(10):
            x = random.randint(30, 370)
            y = random.randint(30, 110)
            svg += f'<text x="{x}" y="{y}" font-size="12" fill="#ADD8E6">❄</text>'
        # Snowman
        svg += f'<circle cx="200" cy="140" r="20" fill="white" stroke="#333"/>'
        svg += f'<circle cx="200" cy="110" r="15" fill="white" stroke="#333"/>'
        svg += f'<circle cx="200" cy="85" r="10" fill="white" stroke="#333"/>'
        svg += f'<text x="200" y="30" text-anchor="middle" font-size="16" fill="#333">❄️ Winter ⛄</text>'
    
    return create_svg_wrapper(svg)

def svg_timer(x, y, seconds_left=30, total=60):
    """Generate a visual timer"""
    cx, cy = x + 40, y + 40
    radius = 35
    
    # Background circle
    bg = f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="#ecf0f1" stroke="#bdc3c7" stroke-width="3"/>'
    
    # Progress arc
    progress = seconds_left / total
    if progress > 0:
        angle = progress * 360
        end_angle = (90 - angle) * math.pi / 180
        large_arc = 1 if angle > 180 else 0
        
        start_x = cx
        start_y = cy - radius
        end_x = cx + radius * math.sin(angle * math.pi / 180)
        end_y = cy - radius * math.cos(angle * math.pi / 180)
        
        arc = f'<path d="M{cx},{cy} L{start_x},{start_y} A{radius},{radius} 0 {large_arc},1 {end_x},{end_y} Z" fill="#3498DB"/>'
    else:
        arc = ''
    
    # Center text
    text = f'<text x="{cx}" y="{cy + 5}" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">{seconds_left}</text>'
    
    return bg + arc + text

def svg_timetable(activities):
    """Generate a visual timetable"""
    svg = ''
    svg += f'<text x="200" y="25" text-anchor="middle" font-size="14" font-weight="bold" fill="#333">Today\'s Schedule</text>'
    
    colours = [COLOURS['blue'], COLOURS['green'], COLOURS['orange'], COLOURS['purple']]
    
    for i, (time, activity) in enumerate(activities):
        y = 45 + i * 35
        svg += f'<rect x="30" y="{y}" width="340" height="30" fill="{colours[i % len(colours)]}" opacity="0.3" rx="5"/>'
        svg += f'<text x="50" y="{y + 20}" font-size="12" fill="#333">{time}</text>'
        svg += f'<text x="130" y="{y + 20}" font-size="12" fill="#333">{activity}</text>'
    
    return create_svg_wrapper(svg)

# =============================================================================
# QUESTION GENERATORS BY LEVEL
# =============================================================================

def generate_level_1_questions():
    """Level 1: Morning & Night - Day vs night (2 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        if i % 2 == 0:
            # Morning scene
            svg = svg_morning_scene()
            question = 'Is this morning or night?'
            correct = 'Morning'
        else:
            # Night scene
            svg = svg_night_scene()
            question = 'Is this morning or night?'
            correct = 'Night'
        
        options = ['Morning', 'Night']
        random.shuffle(options)
        
        questions.append({
            'question_text': question,
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': f'This is {correct.lower()}! You can tell by the {"sun" if correct == "Morning" else "moon and stars"}.',
            'visual_data': svg
        })
    
    return questions

def generate_level_2_questions():
    """Level 2: Times of Day - Morning, afternoon, evening, night (2-3 options)"""
    questions = []
    
    times_of_day = [
        ('morning', '☀️ Sun rising, breakfast time', 'The sun is up and it\'s time for breakfast!'),
        ('afternoon', '🌤️ Sun high, lunchtime', 'The sun is high in the sky, it\'s after lunch!'),
        ('evening', '🌅 Sun setting, dinner time', 'The sun is going down, it\'s dinner time!'),
        ('night', '🌙 Moon and stars, bedtime', 'The moon is out, it\'s time for bed!')
    ]
    
    for i in range(QUESTIONS_PER_LEVEL):
        time_name, visual_desc, explanation = random.choice(times_of_day)
        
        svg_content = f'<text x="200" y="80" text-anchor="middle" font-size="24">{visual_desc.split()[0]}</text>'
        svg_content += f'<text x="200" y="110" text-anchor="middle" font-size="14" fill="#666">{" ".join(visual_desc.split()[1:])}</text>'
        svg = create_svg_wrapper(svg_content)
        
        if i % 2 == 0:
            options = ['Morning', 'Night', 'Afternoon']
        else:
            options = ['Morning', 'Afternoon', 'Evening']
        
        if time_name.title() not in options:
            options[0] = time_name.title()
        
        random.shuffle(options)
        
        questions.append({
            'question_text': 'What time of day is this?',
            'options': json.dumps(options),
            'correct_answer': time_name.title(),
            'explanation': explanation,
            'visual_data': svg
        })
    
    return questions

def generate_level_3_questions():
    """Level 3: Days of the Week - Learn day names (3 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        day_idx = i % 7
        day = DAYS[day_idx]
        
        if i % 3 == 0:
            # What day is today?
            svg_content = f'<rect x="100" y="50" width="200" height="80" fill="#3498DB" rx="10"/>'
            svg_content += f'<text x="200" y="100" text-anchor="middle" font-size="24" fill="white" font-weight="bold">{day}</text>'
            svg = create_svg_wrapper(svg_content)
            
            question = f'What day is shown?'
            correct = day
            wrong_days = [d for d in DAYS if d != day]
            options = [day] + random.sample(wrong_days, 2)
            
        elif i % 3 == 1:
            # What day comes after?
            next_day = DAYS[(day_idx + 1) % 7]
            
            svg_content = f'<text x="200" y="70" text-anchor="middle" font-size="18" fill="#333">Today is {day}</text>'
            svg_content += f'<text x="200" y="110" text-anchor="middle" font-size="16" fill="#666">Tomorrow is...?</text>'
            svg = create_svg_wrapper(svg_content)
            
            question = f'What day comes AFTER {day}?'
            correct = next_day
            wrong_days = [d for d in DAYS if d != next_day]
            options = [next_day] + random.sample(wrong_days, 2)
            
        else:
            # What day comes before?
            prev_day = DAYS[(day_idx - 1) % 7]
            
            svg_content = f'<text x="200" y="70" text-anchor="middle" font-size="18" fill="#333">Today is {day}</text>'
            svg_content += f'<text x="200" y="110" text-anchor="middle" font-size="16" fill="#666">Yesterday was...?</text>'
            svg = create_svg_wrapper(svg_content)
            
            question = f'What day comes BEFORE {day}?'
            correct = prev_day
            wrong_days = [d for d in DAYS if d != prev_day]
            options = [prev_day] + random.sample(wrong_days, 2)
        
        random.shuffle(options)
        
        questions.append({
            'question_text': question,
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': f'{correct} is correct!',
            'visual_data': svg
        })
    
    return questions

def generate_level_4_questions():
    """Level 4: Daily Routines - Order activities (3 options)"""
    questions = []
    
    routines = [
        ('wake up', 'morning', '🌅'),
        ('eat breakfast', 'morning', '🥣'),
        ('go to school', 'morning', '🏫'),
        ('eat lunch', 'afternoon', '🍽️'),
        ('play outside', 'afternoon', '⚽'),
        ('eat dinner', 'evening', '🍝'),
        ('brush teeth', 'evening', '🪥'),
        ('go to bed', 'night', '🛏️')
    ]
    
    for i in range(QUESTIONS_PER_LEVEL):
        activity, time_of_day, emoji = random.choice(routines)
        
        svg_content = f'<text x="200" y="70" text-anchor="middle" font-size="40">{emoji}</text>'
        svg_content += f'<text x="200" y="120" text-anchor="middle" font-size="18" fill="#333">{activity.title()}</text>'
        svg = create_svg_wrapper(svg_content)
        
        question = f'When do you usually {activity}?'
        correct = time_of_day.title()
        options = ['Morning', 'Afternoon', 'Night']
        if correct == 'Evening':
            options = ['Morning', 'Evening', 'Night']
        
        random.shuffle(options)
        
        questions.append({
            'question_text': question,
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': f'We usually {activity} in the {time_of_day}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_5_questions():
    """Level 5: Seasons - Identify seasons (4 options)"""
    questions = []
    
    season_facts = {
        'Spring': ['flowers bloom', 'baby animals', 'rain showers', 'getting warmer'],
        'Summer': ['hot weather', 'long days', 'beach time', 'school holidays'],
        'Autumn': ['leaves fall', 'getting cooler', 'back to school', 'harvest time'],
        'Winter': ['cold weather', 'short days', 'snow possible', 'Christmas time']
    }
    
    for i in range(QUESTIONS_PER_LEVEL):
        season = SEASONS[i % 4]
        
        svg = svg_season_scene(season)
        
        if i % 2 == 0:
            question = 'What season is shown?'
            correct = season
        else:
            fact = random.choice(season_facts[season])
            svg_content = f'<text x="200" y="80" text-anchor="middle" font-size="16" fill="#333">In this season:</text>'
            svg_content += f'<text x="200" y="110" text-anchor="middle" font-size="14" fill="#666">{fact}</text>'
            svg = create_svg_wrapper(svg_content)
            
            question = f'Which season has "{fact}"?'
            correct = season
        
        options = SEASONS.copy()
        random.shuffle(options)
        
        questions.append({
            'question_text': question,
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': f'This is {season}!',
            'visual_data': svg
        })
    
    return questions

def generate_level_6_questions():
    """Level 6: Special Events - Holidays and celebrations (4 options)"""
    questions = []
    
    events = [
        ('Christmas', 'Winter', '🎄', 'December'),
        ('Easter', 'Spring', '🐰', 'March or April'),
        ('Halloween', 'Autumn', '🎃', 'October'),
        ('Summer holidays', 'Summer', '🏖️', 'July and August'),
        ('St Patrick\'s Day', 'Spring', '☘️', 'March'),
        ('New Year', 'Winter', '🎆', 'January')
    ]
    
    for i in range(QUESTIONS_PER_LEVEL):
        event, season, emoji, month = random.choice(events)
        
        svg_content = f'<text x="200" y="70" text-anchor="middle" font-size="40">{emoji}</text>'
        svg_content += f'<text x="200" y="110" text-anchor="middle" font-size="18" fill="#333">{event}</text>'
        svg = create_svg_wrapper(svg_content)
        
        if i % 2 == 0:
            question = f'What season is {event} in?'
            correct = season
            options = SEASONS.copy()
        else:
            question = f'When is {event}?'
            correct = month
            months = ['January', 'March', 'July and August', 'October', 'December', 'March or April']
            options = [month] + random.sample([m for m in months if m != month], 3)
        
        random.shuffle(options)
        
        questions.append({
            'question_text': question,
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': f'{event} is in {season} ({month})!',
            'visual_data': svg
        })
    
    return questions

def generate_level_7_questions():
    """Level 7: O'Clock Times - Read hour times on clock (4 options)"""
    questions = []
    
    for i in range(QUESTIONS_PER_LEVEL):
        hour = random.randint(1, 12)
        
        svg_content = svg_clock(160, 40, 80, hour, 0)
        svg = create_svg_wrapper(svg_content)
        
        question = 'What time does the clock show?'
        correct = f"{hour} o'clock"
        
        # Generate wrong answers
        wrong_hours = [h for h in range(1, 13) if h != hour]
        wrong_options = [f"{h} o'clock" for h in random.sample(wrong_hours, 3)]
        
        options = [correct] + wrong_options
        random.shuffle(options)
        
        questions.append({
            'question_text': question,
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': f'The clock shows {hour} o\'clock! The short hand points to {hour}.',
            'visual_data': svg
        })
    
    return questions

def generate_level_8_questions():
    """Level 8: Before and After - Time sequence (4 options)"""
    questions = []
    
    time_sequences = [
        ('breakfast', 'lunch', 'Breakfast comes BEFORE lunch'),
        ('lunch', 'dinner', 'Lunch comes BEFORE dinner'),
        ('morning', 'afternoon', 'Morning comes BEFORE afternoon'),
        ('afternoon', 'evening', 'Afternoon comes BEFORE evening'),
        ('evening', 'night', 'Evening comes BEFORE night'),
        ('Monday', 'Tuesday', 'Monday comes BEFORE Tuesday'),
        ('Friday', 'Saturday', 'Friday comes BEFORE Saturday'),
        ('Spring', 'Summer', 'Spring comes BEFORE Summer')
    ]
    
    for i in range(QUESTIONS_PER_LEVEL):
        first, second, explanation = random.choice(time_sequences)
        
        svg_content = f'<text x="100" y="80" text-anchor="middle" font-size="16" fill="#3498DB">{first.title()}</text>'
        svg_content += f'<text x="200" y="80" text-anchor="middle" font-size="24" fill="#333">→</text>'
        svg_content += f'<text x="300" y="80" text-anchor="middle" font-size="16" fill="#E74C3C">{second.title()}</text>'
        svg = create_svg_wrapper(svg_content)
        
        if i % 2 == 0:
            question = f'What comes BEFORE {second}?'
            correct = first.title()
            # Generate options based on type
            if first in DAYS:
                options = random.sample(DAYS, 4)
            elif first in SEASONS:
                options = SEASONS.copy()
            else:
                options = [first.title(), second.title(), 'Night', 'Morning']
        else:
            question = f'What comes AFTER {first}?'
            correct = second.title()
            if second in DAYS:
                options = random.sample(DAYS, 4)
            elif second in SEASONS:
                options = SEASONS.copy()
            else:
                options = [first.title(), second.title(), 'Night', 'Morning']
        
        if correct not in options:
            options[0] = correct
        random.shuffle(options)
        
        questions.append({
            'question_text': question,
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': explanation,
            'visual_data': svg
        })
    
    return questions

def generate_level_9_questions():
    """Level 9: Using Timers - Understand waiting (4 options)"""
    questions = []
    
    timer_scenarios = [
        ('brushing teeth', 2, 'minutes'),
        ('washing hands', 20, 'seconds'),
        ('waiting for toast', 3, 'minutes'),
        ('counting to 10', 10, 'seconds'),
        ('baking cookies', 15, 'minutes'),
        ('boiling an egg', 5, 'minutes')
    ]
    
    for i in range(QUESTIONS_PER_LEVEL):
        activity, duration, unit = random.choice(timer_scenarios)
        
        if i % 3 == 0:
            # Which takes longer?
            short_activity = ('washing hands', 20, 'seconds')
            long_activity = ('baking cookies', 15, 'minutes')
            
            svg_content = f'<text x="100" y="70" text-anchor="middle" font-size="14">A: {short_activity[0]}</text>'
            svg_content += f'<text x="100" y="90" text-anchor="middle" font-size="12" fill="#666">({short_activity[1]} {short_activity[2]})</text>'
            svg_content += f'<text x="300" y="70" text-anchor="middle" font-size="14">B: {long_activity[0]}</text>'
            svg_content += f'<text x="300" y="90" text-anchor="middle" font-size="12" fill="#666">({long_activity[1]} {long_activity[2]})</text>'
            svg = create_svg_wrapper(svg_content)
            
            question = 'Which takes LONGER?'
            correct = 'B'
            options = ['A', 'B', 'Same time', 'Cannot tell']
            
        elif i % 3 == 1:
            # Is this a long or short time?
            if duration <= 30 and unit == 'seconds':
                correct = 'Short time'
            elif duration <= 5 and unit == 'minutes':
                correct = 'Short time'
            else:
                correct = 'Long time'
            
            svg_content = f'<text x="200" y="70" text-anchor="middle" font-size="16">{activity.title()}</text>'
            svg_content += f'<text x="200" y="100" text-anchor="middle" font-size="20" fill="#3498DB">{duration} {unit}</text>'
            svg = create_svg_wrapper(svg_content)
            
            question = f'Is {duration} {unit} a long or short time?'
            options = ['Short time', 'Long time', 'Medium time', 'Very long time']
            
        else:
            # Timer reading
            seconds = random.choice([10, 20, 30, 45, 60])
            
            svg_content = svg_timer(160, 50, seconds, 60)
            svg = create_svg_wrapper(svg_content)
            
            question = 'How many seconds are left on the timer?'
            correct = str(seconds)
            options = [str(seconds), str(seconds + 10), str(seconds - 10) if seconds > 10 else '5', str(60)]
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

def generate_level_10_questions():
    """Level 10: Waiting & Turns - Patience and sequence (4 options)"""
    questions = []
    
    scenarios = [
        {
            'situation': 'Queue at the shop',
            'people': ['Amy', 'Ben', 'Cat', 'Dan'],
            'question': 'Who is FIRST in the queue?',
            'answer_idx': 0
        },
        {
            'situation': 'Taking turns on the swing',
            'people': ['Ella', 'Finn', 'Grace', 'Harry'],
            'question': 'Who is LAST to get a turn?',
            'answer_idx': 3
        },
        {
            'situation': 'Waiting for the bus',
            'people': ['Ivy', 'Jack', 'Kate', 'Leo'],
            'question': 'Who is SECOND in line?',
            'answer_idx': 1
        }
    ]
    
    for i in range(QUESTIONS_PER_LEVEL):
        scenario = scenarios[i % len(scenarios)]
        
        svg_content = f'<text x="200" y="30" text-anchor="middle" font-size="14" font-weight="bold">{scenario["situation"]}</text>'
        
        for j, person in enumerate(scenario['people']):
            x = 60 + j * 90
            svg_content += f'<circle cx="{x}" cy="80" r="20" fill="{list(COLOURS.values())[j]}"/>'
            svg_content += f'<text x="{x}" y="120" text-anchor="middle" font-size="12">{person}</text>'
            svg_content += f'<text x="{x}" y="140" text-anchor="middle" font-size="10" fill="#666">{j + 1}</text>'
        
        svg = create_svg_wrapper(svg_content)
        
        correct = scenario['people'][scenario['answer_idx']]
        options = scenario['people'].copy()
        random.shuffle(options)
        
        questions.append({
            'question_text': scenario['question'],
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': f'{correct} is the answer!',
            'visual_data': svg
        })
    
    return questions

def generate_level_11_questions():
    """Level 11: Visual Timetables - Read simple schedules (4 options)"""
    questions = []
    
    sample_schedules = [
        [('9:00', 'Circle Time'), ('10:00', 'Maths'), ('11:00', 'Break'), ('12:00', 'Lunch')],
        [('9:00', 'Assembly'), ('10:00', 'Reading'), ('11:00', 'Art'), ('12:00', 'Lunch')],
        [('2:00', 'Music'), ('3:00', 'PE'), ('3:30', 'Home Time'), ('', '')]
    ]
    
    for i in range(QUESTIONS_PER_LEVEL):
        schedule = random.choice(sample_schedules[:2])  # Use full schedules
        
        svg = svg_timetable(schedule)
        
        if i % 3 == 0:
            # What happens at X time?
            time_slot = random.choice(schedule)
            question = f'What happens at {time_slot[0]}?'
            correct = time_slot[1]
            options = [s[1] for s in schedule]
            
        elif i % 3 == 1:
            # What time is X?
            time_slot = random.choice(schedule)
            question = f'What time is {time_slot[1]}?'
            correct = time_slot[0]
            options = [s[0] for s in schedule]
            
        else:
            # What comes after X?
            idx = random.randint(0, len(schedule) - 2)
            question = f'What comes AFTER {schedule[idx][1]}?'
            correct = schedule[idx + 1][1]
            options = [s[1] for s in schedule]
        
        random.shuffle(options)
        
        questions.append({
            'question_text': question,
            'options': json.dumps(options),
            'correct_answer': correct,
            'explanation': f'{correct} is correct!',
            'visual_data': svg
        })
    
    return questions

def generate_level_12_questions():
    """Level 12: Time Challenge - Mixed time problems (4 options)"""
    questions = []
    
    challenge_types = ['clock', 'day', 'season', 'routine', 'sequence', 'timetable']
    
    for i in range(QUESTIONS_PER_LEVEL):
        c_type = challenge_types[i % len(challenge_types)]
        
        if c_type == 'clock':
            hour = random.randint(1, 12)
            svg_content = svg_clock(160, 40, 80, hour, 0)
            svg = create_svg_wrapper(svg_content)
            
            correct = f"{hour} o'clock"
            wrong = [f"{h} o'clock" for h in random.sample([h for h in range(1, 13) if h != hour], 3)]
            options = [correct] + wrong
            random.shuffle(options)
            
            questions.append({
                'question_text': 'What time is it?',
                'options': json.dumps(options),
                'correct_answer': correct,
                'explanation': f'It\'s {hour} o\'clock!',
                'visual_data': svg
            })
            
        elif c_type == 'day':
            day_idx = random.randint(0, 6)
            day = DAYS[day_idx]
            next_day = DAYS[(day_idx + 1) % 7]
            
            svg_content = f'<text x="200" y="90" text-anchor="middle" font-size="20" fill="#333">Today is {day}</text>'
            svg = create_svg_wrapper(svg_content)
            
            question = 'What day is TOMORROW?'
            correct = next_day
            options = random.sample(DAYS, 4)
            if correct not in options:
                options[0] = correct
            random.shuffle(options)
            
            questions.append({
                'question_text': question,
                'options': json.dumps(options),
                'correct_answer': correct,
                'explanation': f'After {day} comes {next_day}!',
                'visual_data': svg
            })
            
        elif c_type == 'season':
            season = random.choice(SEASONS)
            svg = svg_season_scene(season)
            
            options = SEASONS.copy()
            random.shuffle(options)
            
            questions.append({
                'question_text': 'What season is this?',
                'options': json.dumps(options),
                'correct_answer': season,
                'explanation': f'This is {season}!',
                'visual_data': svg
            })
            
        elif c_type == 'routine':
            activities = [
                ('wake up', 'Morning'),
                ('eat lunch', 'Afternoon'),
                ('eat dinner', 'Evening'),
                ('go to bed', 'Night')
            ]
            activity, time = random.choice(activities)
            
            svg_content = f'<text x="200" y="90" text-anchor="middle" font-size="18">When do you {activity}?</text>'
            svg = create_svg_wrapper(svg_content)
            
            options = ['Morning', 'Afternoon', 'Evening', 'Night']
            random.shuffle(options)
            
            questions.append({
                'question_text': f'When do you {activity}?',
                'options': json.dumps(options),
                'correct_answer': time,
                'explanation': f'We {activity} in the {time.lower()}!',
                'visual_data': svg
            })
            
        elif c_type == 'sequence':
            pairs = [
                ('breakfast', 'lunch'),
                ('Monday', 'Tuesday'),
                ('Spring', 'Summer'),
                ('morning', 'afternoon')
            ]
            first, second = random.choice(pairs)
            
            svg_content = f'<text x="200" y="90" text-anchor="middle" font-size="18">{first.title()} → ?</text>'
            svg = create_svg_wrapper(svg_content)
            
            if first in [d.lower() for d in DAYS]:
                options = DAYS[:4]
            elif first in [s.lower() for s in SEASONS]:
                options = SEASONS
            else:
                options = [second.title(), first.title(), 'Night', 'Evening']
            
            random.shuffle(options)
            
            questions.append({
                'question_text': f'What comes AFTER {first}?',
                'options': json.dumps(options),
                'correct_answer': second.title(),
                'explanation': f'{second.title()} comes after {first}!',
                'visual_data': svg
            })
            
        else:  # timetable
            schedule = [('9:00', 'Maths'), ('10:00', 'English'), ('11:00', 'Break'), ('12:00', 'Lunch')]
            svg = svg_timetable(schedule)
            
            time_slot = random.choice(schedule)
            question = f'What happens at {time_slot[0]}?'
            correct = time_slot[1]
            options = [s[1] for s in schedule]
            random.shuffle(options)
            
            questions.append({
                'question_text': question,
                'options': json.dumps(options),
                'correct_answer': correct,
                'explanation': f'{correct} happens at {time_slot[0]}!',
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
