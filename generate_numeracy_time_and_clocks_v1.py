#!/usr/bin/env python3
"""
AgentMath - Time & Clocks Question Generator (Numeracy Strand)
Irish Primary Curriculum Aligned

Target Audience: 5th/6th Class (ages 10-12)
Mode: numeracy

Level Structure:
  L1-3:   Foundation - Reading clocks, o'clock/half past, quarter past/to
  L4-6:   Developing - 5-minute intervals, 24-hour time, digital/analogue
  L7-9:   Proficient - Time calculations, elapsed time, word problems
  L10-12: Advanced - Complex calculations, timetables, mastery

Target: 600 questions (50 per level)
"""

import random
import sqlite3

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'time_and_clocks'
MODE = 'numeracy'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'

IRISH_NAMES = [
    'Aoife', 'Cian', 'Niamh', 'Oisín', 'Saoirse', 'Conor',
    'Siobhán', 'Seán', 'Caoimhe', 'Darragh', 'Róisín', 'Fionn',
    'Emma', 'Jack', 'Sophie', 'Liam', 'Grace', 'Adam'
]

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_difficulty_band(level):
    if level <= 3:
        return 'foundation'
    elif level <= 6:
        return 'developing'
    elif level <= 9:
        return 'proficient'
    else:
        return 'advanced'

def make_options(correct, wrong_list):
    correct_str = str(correct)
    unique_wrong = []
    for w in wrong_list:
        w_str = str(w)
        if w_str != correct_str and w_str not in unique_wrong:
            unique_wrong.append(w_str)
    
    options = [correct_str] + unique_wrong[:3]
    
    fallback_idx = 1
    while len(set(options)) < 4:
        options.append(f"Option {fallback_idx}")
        fallback_idx += 1
    
    options = list(dict.fromkeys(options))[:4]
    random.shuffle(options)
    correct_idx = options.index(correct_str)
    return options, correct_idx

def format_12hr(hour, minute):
    """Format time in 12-hour format"""
    period = "am" if hour < 12 else "pm"
    display_hour = hour if hour <= 12 else hour - 12
    if display_hour == 0:
        display_hour = 12
    return f"{display_hour}:{minute:02d} {period}"

def format_24hr(hour, minute):
    """Format time in 24-hour format"""
    return f"{hour:02d}:{minute:02d}"

def generate_clock_svg(hour, minute, show_digital=False):
    """Generate SVG of an analogue clock"""
    import math
    
    # Calculate hand positions
    hour_angle = (hour % 12 + minute / 60) * 30 - 90
    minute_angle = minute * 6 - 90
    
    hour_rad = math.radians(hour_angle)
    minute_rad = math.radians(minute_angle)
    
    # Hand endpoints
    hour_x = 60 + 25 * math.cos(hour_rad)
    hour_y = 60 + 25 * math.sin(hour_rad)
    minute_x = 60 + 38 * math.cos(minute_rad)
    minute_y = 60 + 38 * math.sin(minute_rad)
    
    svg = f'''<svg viewBox="0 0 120 {'140' if show_digital else '120'}" xmlns="http://www.w3.org/2000/svg">
    <style>
        .face {{ fill: #f9fafb; stroke: #374151; stroke-width: 3; }}
        .center {{ fill: #374151; }}
        .hour-hand {{ stroke: #1f2937; stroke-width: 4; stroke-linecap: round; }}
        .minute-hand {{ stroke: #10b981; stroke-width: 3; stroke-linecap: round; }}
        .tick {{ stroke: #6b7280; }}
        .number {{ font-size: 10px; fill: #374151; text-anchor: middle; dominant-baseline: middle; }}
        .digital {{ font-size: 14px; fill: #1f2937; text-anchor: middle; font-weight: bold; }}
    </style>
    <circle cx="60" cy="60" r="50" class="face"/>'''
    
    # Hour markers
    for i in range(12):
        angle = math.radians(i * 30 - 90)
        x1 = 60 + 42 * math.cos(angle)
        y1 = 60 + 42 * math.sin(angle)
        x2 = 60 + 48 * math.cos(angle)
        y2 = 60 + 48 * math.sin(angle)
        svg += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="tick" stroke-width="2"/>'
        
        # Numbers
        num_x = 60 + 35 * math.cos(angle)
        num_y = 60 + 35 * math.sin(angle)
        num = 12 if i == 0 else i
        svg += f'<text x="{num_x}" y="{num_y}" class="number">{num}</text>'
    
    # Hands
    svg += f'<line x1="60" y1="60" x2="{hour_x}" y2="{hour_y}" class="hour-hand"/>'
    svg += f'<line x1="60" y1="60" x2="{minute_x}" y2="{minute_y}" class="minute-hand"/>'
    svg += '<circle cx="60" cy="60" r="4" class="center"/>'
    
    if show_digital:
        time_str = format_12hr(hour, minute)
        svg += f'<text x="60" y="130" class="digital">{time_str}</text>'
    
    svg += '</svg>'
    return svg

def add_time(hour, minute, add_hours, add_minutes):
    """Add time and return new hour, minute"""
    total_minutes = hour * 60 + minute + add_hours * 60 + add_minutes
    new_hour = (total_minutes // 60) % 24
    new_minute = total_minutes % 60
    return new_hour, new_minute

def subtract_time(hour, minute, sub_hours, sub_minutes):
    """Subtract time and return new hour, minute"""
    total_minutes = hour * 60 + minute - sub_hours * 60 - sub_minutes
    if total_minutes < 0:
        total_minutes += 24 * 60
    new_hour = (total_minutes // 60) % 24
    new_minute = total_minutes % 60
    return new_hour, new_minute

def time_difference(h1, m1, h2, m2):
    """Calculate difference between two times in minutes"""
    total1 = h1 * 60 + m1
    total2 = h2 * 60 + m2
    diff = abs(total2 - total1)
    return diff // 60, diff % 60

# ============================================================
# LEVEL 1: O'Clock Times (Foundation)
# ============================================================

def generate_level_1():
    """Level 1: O'Clock Times"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            hour = random.randint(1, 12)
            q_type = random.choice(['read', 'identify', 'write', 'word'])
            
            if q_type == 'read':
                q_text = f"What time does the clock show?"
                correct = f"{hour} o'clock"
                wrong = [f"{(hour % 12) + 1} o'clock", f"{hour - 1 if hour > 1 else 12} o'clock", f"half past {hour}"]
                explanation = f"Step 1: The short hand points to {hour}. Step 2: The long hand points to 12. Step 3: It's {hour} o'clock. ✓"
                image_svg = generate_clock_svg(hour, 0)
                
            elif q_type == 'identify':
                q_text = f"Which clock shows {hour} o'clock?"
                correct = f"Clock with hour hand on {hour}, minute hand on 12"
                wrong = [f"Clock showing {hour}:30", f"Clock showing {(hour % 12) + 1}:00", f"Clock showing {hour}:15"]
                explanation = f"Step 1: At {hour} o'clock, the minute hand is on 12 and hour hand is on {hour}. ✓"
                image_svg = generate_clock_svg(hour, 0)
                
            elif q_type == 'write':
                q_text = f"Write {hour} o'clock in digital format."
                correct = f"{hour}:00"
                wrong = [f"{hour}:30", f"{hour}:15", f"{(hour % 12) + 1}:00"]
                explanation = f"Step 1: {hour} o'clock = {hour}:00 in digital. ✓"
                image_svg = None
                
            else:  # word
                name = random.choice(IRISH_NAMES)
                q_text = f"{name}'s clock shows the hour hand on {hour} and the minute hand on 12. What time is it?"
                correct = f"{hour} o'clock"
                wrong = [f"half past {hour}", f"{hour}:30", f"{(hour % 12) + 1} o'clock"]
                explanation = f"Step 1: Minute hand on 12 means o'clock. Step 2: Hour hand on {hour}. Answer: {hour} o'clock. ✓"
                image_svg = None
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': image_svg,
                'difficulty': 1,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 2: Half Past (Foundation)
# ============================================================

def generate_level_2():
    """Level 2: Half Past Times"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            hour = random.randint(1, 12)
            q_type = random.choice(['read', 'digital', 'identify', 'word'])
            
            if q_type == 'read':
                q_text = f"What time does the clock show?"
                correct = f"half past {hour}"
                wrong = [f"{hour} o'clock", f"quarter past {hour}", f"half past {(hour % 12) + 1}"]
                explanation = f"Step 1: The long hand points to 6 (30 minutes). Step 2: The short hand is past {hour}. Step 3: It's half past {hour}. ✓"
                image_svg = generate_clock_svg(hour, 30)
                
            elif q_type == 'digital':
                q_text = f"Write 'half past {hour}' in digital format."
                correct = f"{hour}:30"
                wrong = [f"{hour}:00", f"{hour}:15", f"{hour}:45"]
                explanation = f"Step 1: Half past = 30 minutes. Step 2: Half past {hour} = {hour}:30. ✓"
                image_svg = None
                
            elif q_type == 'identify':
                q_text = f"At half past the hour, where does the minute hand point?"
                correct = "6"
                wrong = ["12", "3", "9"]
                explanation = f"Step 1: Half past = 30 minutes. Step 2: The minute hand points to 6. ✓"
                image_svg = generate_clock_svg(hour, 30)
                
            else:  # word
                name = random.choice(IRISH_NAMES)
                q_text = f"{name} has lunch at half past {hour}. What is this in digital time?"
                correct = f"{hour}:30"
                wrong = [f"{hour}:00", f"{hour}:15", f"{(hour % 12) + 1}:30"]
                explanation = f"Step 1: Half past {hour} = {hour}:30. ✓"
                image_svg = None
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': image_svg,
                'difficulty': 2,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 3: Quarter Past and Quarter To (Foundation)
# ============================================================

def generate_level_3():
    """Level 3: Quarter Past and Quarter To"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            hour = random.randint(1, 12)
            time_type = random.choice(['quarter_past', 'quarter_to'])
            
            if time_type == 'quarter_past':
                minute = 15
                time_word = f"quarter past {hour}"
                next_hour = hour
            else:
                minute = 45
                next_hour = (hour % 12) + 1
                time_word = f"quarter to {next_hour}"
            
            q_type = random.choice(['read', 'digital', 'identify', 'word', 'convert', 'compare'])
            
            if q_type == 'read':
                q_text = f"What time does the clock show?"
                correct = time_word
                if time_type == 'quarter_past':
                    wrong = [f"quarter to {(hour % 12) + 1}", f"half past {hour}", f"{hour} o'clock"]
                else:
                    wrong = [f"quarter past {hour}", f"half past {hour}", f"{next_hour} o'clock"]
                explanation = f"Step 1: Minute hand on {'3' if minute == 15 else '9'}. Step 2: It's {time_word}. ✓"
                image_svg = generate_clock_svg(hour, minute)
                
            elif q_type == 'digital':
                q_text = f"Write '{time_word}' in digital format."
                if time_type == 'quarter_past':
                    correct = f"{hour}:15"
                    wrong = [f"{hour}:45", f"{hour}:30", f"{hour}:00"]
                else:
                    correct = f"{hour}:45"
                    wrong = [f"{next_hour}:15", f"{hour}:30", f"{next_hour}:00"]
                explanation = f"Step 1: Quarter past = :15, Quarter to = :45. Step 2: {time_word} = {correct}. ✓"
                image_svg = None
                
            elif q_type == 'identify':
                if time_type == 'quarter_past':
                    q_text = f"At quarter past {hour}, where does the minute hand point?"
                else:
                    q_text = f"At quarter to {next_hour}, where does the minute hand point?"
                correct = "3" if minute == 15 else "9"
                wrong = ["12", "6", "3" if minute == 45 else "9"]
                explanation = f"Step 1: {'Quarter past points to 3' if minute == 15 else 'Quarter to points to 9'}. ✓"
                image_svg = generate_clock_svg(hour, minute)
                
            elif q_type == 'word':
                name = random.choice(IRISH_NAMES)
                activity = random.choice(['school', 'football', 'dinner', 'homework'])
                q_text = f"{name} has {activity} at {time_word}. What is this in digital time?"
                if time_type == 'quarter_past':
                    correct = f"{hour}:15"
                    wrong = [f"{hour}:45", f"{hour}:30", f"{hour}:00"]
                else:
                    correct = f"{hour}:45"
                    wrong = [f"{hour}:15", f"{hour}:30", f"{next_hour}:00"]
                explanation = f"Step 1: {time_word} = {correct}. ✓"
                image_svg = None
                
            elif q_type == 'convert':
                if time_type == 'quarter_past':
                    q_text = f"How many minutes past {hour} is quarter past {hour}?"
                    correct = "15 minutes"
                    wrong = ["30 minutes", "45 minutes", "20 minutes"]
                else:
                    q_text = f"How many minutes until {next_hour} o'clock is quarter to {next_hour}?"
                    correct = "15 minutes"
                    wrong = ["30 minutes", "45 minutes", "20 minutes"]
                explanation = f"Step 1: Quarter = 1/4 of an hour = 15 minutes. ✓"
                image_svg = None
                
            else:  # compare
                other_hour = random.choice([h for h in range(1, 13) if h != hour])
                q_text = f"Which is later: quarter past {hour} or quarter to {other_hour}?"
                time1_mins = hour * 60 + 15
                time2_mins = (other_hour - 1) * 60 + 45
                if time1_mins > time2_mins:
                    correct = f"Quarter past {hour}"
                elif time2_mins > time1_mins:
                    correct = f"Quarter to {other_hour}"
                else:
                    correct = "Same time"
                wrong = [f"Quarter past {hour}" if time1_mins <= time2_mins else f"Quarter to {other_hour}", "Same time" if time1_mins != time2_mins else f"Quarter past {hour}", "Cannot tell"]
                explanation = f"Step 1: Quarter past {hour} = {hour}:15. Quarter to {other_hour} = {other_hour - 1}:45. ✓"
                image_svg = None
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': image_svg,
                'difficulty': 3,
                'difficulty_band': 'foundation',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 4: 5-Minute Intervals (Developing)
# ============================================================

def generate_level_4():
    """Level 4: Reading time in 5-minute intervals"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            hour = random.randint(1, 12)
            minute = random.choice([5, 10, 20, 25, 35, 40, 50, 55])
            
            q_type = random.choice(['read', 'digital', 'minutes'])
            
            if q_type == 'read':
                q_text = f"What time does the clock show?"
                correct = f"{hour}:{minute:02d}"
                wrong = [f"{hour}:{(minute + 5) % 60:02d}", f"{hour}:{(minute - 5) % 60:02d}", f"{(hour % 12) + 1}:{minute:02d}"]
                explanation = f"Step 1: Hour hand near {hour}. Step 2: Minute hand at {minute} minutes. Step 3: Time is {hour}:{minute:02d}. ✓"
                image_svg = generate_clock_svg(hour, minute)
                
            elif q_type == 'digital':
                # Convert words to digital
                if minute <= 30:
                    time_word = f"{minute} minutes past {hour}"
                else:
                    next_hour = (hour % 12) + 1
                    mins_to = 60 - minute
                    time_word = f"{mins_to} minutes to {next_hour}"
                
                q_text = f"Write '{time_word}' in digital format."
                correct = f"{hour}:{minute:02d}"
                wrong = [f"{hour}:{(minute + 10) % 60:02d}", f"{(hour % 12) + 1}:{minute:02d}", f"{hour}:{(60 - minute):02d}"]
                explanation = f"Step 1: {time_word} = {hour}:{minute:02d}. ✓"
                image_svg = None
                
            else:  # minutes
                q_text = f"How many minutes past {hour} is {hour}:{minute:02d}?"
                correct = f"{minute} minutes"
                wrong = [f"{minute + 5} minutes", f"{minute - 5} minutes", f"{60 - minute} minutes"]
                explanation = f"Step 1: {hour}:{minute:02d} means {minute} minutes past {hour}. ✓"
                image_svg = generate_clock_svg(hour, minute)
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': image_svg,
                'difficulty': 4,
                'difficulty_band': 'developing',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 5: 24-Hour Time (Developing)
# ============================================================

def generate_level_5():
    """Level 5: 24-Hour Time"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            hour_24 = random.randint(0, 23)
            minute = random.choice([0, 15, 30, 45])
            
            # Convert to 12-hour
            if hour_24 == 0:
                hour_12 = 12
                period = "am"
            elif hour_24 < 12:
                hour_12 = hour_24
                period = "am"
            elif hour_24 == 12:
                hour_12 = 12
                period = "pm"
            else:
                hour_12 = hour_24 - 12
                period = "pm"
            
            q_type = random.choice(['to_12', 'to_24', 'identify', 'word'])
            
            if q_type == 'to_12':
                q_text = f"Convert {hour_24:02d}:{minute:02d} to 12-hour time."
                correct = f"{hour_12}:{minute:02d} {period}"
                wrong_period = "pm" if period == "am" else "am"
                wrong = [f"{hour_12}:{minute:02d} {wrong_period}", f"{hour_24}:{minute:02d}", f"{(hour_12 % 12) + 1}:{minute:02d} {period}"]
                explanation = f"Step 1: {hour_24:02d}:{minute:02d} is {'afternoon/evening' if hour_24 >= 12 else 'morning'}. Step 2: = {hour_12}:{minute:02d} {period}. ✓"
                image_svg = None
                
            elif q_type == 'to_24':
                q_text = f"Convert {hour_12}:{minute:02d} {period} to 24-hour time."
                correct = f"{hour_24:02d}:{minute:02d}"
                wrong = [f"{(hour_24 + 12) % 24:02d}:{minute:02d}", f"{hour_12:02d}:{minute:02d}", f"{(hour_24 - 1) % 24:02d}:{minute:02d}"]
                explanation = f"Step 1: {hour_12}:{minute:02d} {period} = {hour_24:02d}:{minute:02d} in 24-hour time. ✓"
                image_svg = None
                
            elif q_type == 'identify':
                q_text = f"Is {hour_24:02d}:{minute:02d} in the morning (am) or afternoon/evening (pm)?"
                correct = period
                wrong = ["pm" if period == "am" else "am", "midnight", "noon"]
                explanation = f"Step 1: Hours 00-11 are am, 12-23 are pm. Step 2: {hour_24:02d}:{minute:02d} is {period}. ✓"
                image_svg = None
                
            else:  # word
                name = random.choice(IRISH_NAMES)
                q_text = f"{name}'s train leaves at {hour_24:02d}:{minute:02d}. What time is this in 12-hour format?"
                correct = f"{hour_12}:{minute:02d} {period}"
                wrong_period = "pm" if period == "am" else "am"
                wrong = [f"{hour_12}:{minute:02d} {wrong_period}", f"{hour_24}:{minute:02d}", f"{(hour_12 % 12) + 1}:{minute:02d} {period}"]
                explanation = f"Step 1: {hour_24:02d}:{minute:02d} = {hour_12}:{minute:02d} {period}. ✓"
                image_svg = None
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': image_svg,
                'difficulty': 5,
                'difficulty_band': 'developing',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 6: Time Units and Conversions (Developing)
# ============================================================

def generate_level_6():
    """Level 6: Time Units - seconds, minutes, hours, days"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 30
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            q_type = random.choice(['min_to_sec', 'hour_to_min', 'day_to_hour', 'mixed', 'weeks', 'reverse', 'word', 'compare'])
            
            if q_type == 'min_to_sec':
                minutes = random.randint(1, 10)
                seconds = minutes * 60
                
                q_text = f"How many seconds are in {minutes} minute{'s' if minutes > 1 else ''}?"
                correct = f"{seconds} seconds"
                wrong = [f"{seconds + 60} seconds", f"{minutes} seconds", f"{seconds - 60} seconds" if seconds > 60 else f"{seconds + 120} seconds"]
                explanation = f"Step 1: 1 minute = 60 seconds. Step 2: {minutes} minutes = {minutes} × 60 = {seconds} seconds. ✓"
                
            elif q_type == 'hour_to_min':
                hours = random.randint(1, 5)
                minutes = hours * 60
                
                q_text = f"How many minutes are in {hours} hour{'s' if hours > 1 else ''}?"
                correct = f"{minutes} minutes"
                wrong = [f"{minutes + 60} minutes", f"{hours} minutes", f"{minutes - 30} minutes" if minutes > 30 else f"{minutes + 90} minutes"]
                explanation = f"Step 1: 1 hour = 60 minutes. Step 2: {hours} hours = {hours} × 60 = {minutes} minutes. ✓"
                
            elif q_type == 'day_to_hour':
                days = random.randint(1, 7)
                hours = days * 24
                
                q_text = f"How many hours are in {days} day{'s' if days > 1 else ''}?"
                correct = f"{hours} hours"
                wrong = [f"{hours + 12} hours", f"{days * 12} hours", f"{hours - 24} hours" if hours > 24 else f"{hours + 48} hours"]
                explanation = f"Step 1: 1 day = 24 hours. Step 2: {days} days = {days} × 24 = {hours} hours. ✓"
                
            elif q_type == 'mixed':
                hours = random.randint(1, 4)
                mins = random.choice([10, 15, 20, 30, 45])
                total_mins = hours * 60 + mins
                
                q_text = f"How many minutes in total is {hours} hour{'s' if hours > 1 else ''} and {mins} minutes?"
                correct = f"{total_mins} minutes"
                wrong = [f"{total_mins + 15} minutes", f"{hours * 60} minutes", f"{mins} minutes"]
                explanation = f"Step 1: {hours} hours = {hours * 60} minutes. Step 2: {hours * 60} + {mins} = {total_mins} minutes. ✓"
                
            elif q_type == 'weeks':
                weeks = random.randint(1, 4)
                days = weeks * 7
                
                q_text = f"How many days are in {weeks} week{'s' if weeks > 1 else ''}?"
                correct = f"{days} days"
                wrong = [f"{days + 7} days", f"{weeks * 5} days", f"{days - 7} days" if days > 7 else f"{days + 14} days"]
                explanation = f"Step 1: 1 week = 7 days. Step 2: {weeks} weeks = {weeks} × 7 = {days} days. ✓"
                
            elif q_type == 'reverse':
                # Converting back to larger units
                variant = random.choice(['sec_to_min', 'min_to_hr'])
                if variant == 'sec_to_min':
                    minutes = random.randint(2, 10)
                    seconds = minutes * 60
                    q_text = f"How many minutes is {seconds} seconds?"
                    correct = f"{minutes} minutes"
                    wrong = [f"{minutes + 1} minutes", f"{seconds} minutes", f"{minutes - 1} minutes" if minutes > 1 else f"{minutes + 2} minutes"]
                    explanation = f"Step 1: {seconds} ÷ 60 = {minutes} minutes. ✓"
                else:
                    hours = random.randint(1, 4)
                    minutes = hours * 60
                    q_text = f"How many hours is {minutes} minutes?"
                    correct = f"{hours} hours"
                    wrong = [f"{hours + 1} hours", f"{minutes} hours", f"{hours - 1} hours" if hours > 1 else f"{hours + 2} hours"]
                    explanation = f"Step 1: {minutes} ÷ 60 = {hours} hours. ✓"
                
            elif q_type == 'word':
                name = random.choice(IRISH_NAMES)
                variant = random.choice(['movie', 'journey', 'game'])
                if variant == 'movie':
                    hours = random.randint(1, 2)
                    mins = random.choice([30, 45])
                    total = hours * 60 + mins
                    q_text = f"A movie is {hours} hour{'s' if hours > 1 else ''} and {mins} minutes long. How many minutes is that?"
                    correct = f"{total} minutes"
                    wrong = [f"{total + 15} minutes", f"{hours * 60} minutes", f"{mins} minutes"]
                elif variant == 'journey':
                    minutes = random.choice([90, 120, 150])
                    hours = minutes // 60
                    rem = minutes % 60
                    q_text = f"{name}'s journey takes {minutes} minutes. How many hours and minutes is that?"
                    correct = f"{hours} hr {rem} min" if rem > 0 else f"{hours} hours"
                    wrong = [f"{hours + 1} hr", f"{minutes} min", f"{hours} hr {rem + 15} min" if rem > 0 else f"{hours - 1} hr 60 min"]
                else:
                    halves = random.randint(2, 4)
                    minutes = halves * 45
                    q_text = f"A football match has {halves} halves of 45 minutes each. Total playing time?"
                    correct = f"{minutes} minutes"
                    wrong = [f"{minutes + 45} minutes", f"45 minutes", f"{minutes - 45} minutes"]
                explanation = f"Step 1: Calculate total time. Answer: {correct}. ✓"
                
            else:  # compare
                unit1 = random.choice([60, 120, 180])  # seconds
                unit2 = unit1 // 60  # minutes
                
                q_text = f"Which is longer: {unit1} seconds or {unit2 + 1} minutes?"
                correct = f"{unit2 + 1} minutes"
                wrong = [f"{unit1} seconds", "Same length", "Cannot tell"]
                explanation = f"Step 1: {unit1} seconds = {unit2} minutes. {unit2 + 1} minutes is longer. ✓"
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 6,
                'difficulty_band': 'developing',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 7: Adding Time (Proficient)
# ============================================================

def generate_level_7():
    """Level 7: Adding Time"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            start_hour = random.randint(8, 14)
            start_min = random.choice([0, 15, 30, 45])
            add_hours = random.randint(0, 3)
            add_mins = random.choice([15, 30, 45, 60])
            
            end_hour, end_min = add_time(start_hour, start_min, add_hours, add_mins)
            
            q_type = random.choice(['basic', 'word', 'journey'])
            
            if q_type == 'basic':
                q_text = f"What time is {add_hours} hour{'s' if add_hours != 1 else ''} and {add_mins} minutes after {start_hour}:{start_min:02d}?"
                correct = f"{end_hour}:{end_min:02d}"
                wrong = [f"{end_hour}:{(end_min + 15) % 60:02d}", f"{start_hour + add_hours}:{start_min:02d}", f"{end_hour - 1}:{end_min:02d}"]
                explanation = f"Step 1: Start at {start_hour}:{start_min:02d}. Step 2: Add {add_hours}h {add_mins}m. Step 3: End at {end_hour}:{end_min:02d}. ✓"
                
            elif q_type == 'word':
                name = random.choice(IRISH_NAMES)
                duration = add_hours * 60 + add_mins
                q_text = f"{name} starts homework at {start_hour}:{start_min:02d}. It takes {duration} minutes. When do they finish?"
                correct = f"{end_hour}:{end_min:02d}"
                wrong = [f"{end_hour}:{(end_min + 15) % 60:02d}", f"{start_hour}:{start_min:02d}", f"{end_hour + 1}:{end_min:02d}"]
                explanation = f"Step 1: {start_hour}:{start_min:02d} + {duration} minutes = {end_hour}:{end_min:02d}. ✓"
                
            else:  # journey
                q_text = f"A bus leaves at {start_hour}:{start_min:02d}. The journey takes {add_hours} hour{'s' if add_hours != 1 else ''} {add_mins} minutes. Arrival time?"
                correct = f"{end_hour}:{end_min:02d}"
                wrong = [f"{end_hour + 1}:{end_min:02d}", f"{start_hour}:{start_min:02d}", f"{end_hour}:{(end_min + 30) % 60:02d}"]
                explanation = f"Step 1: Depart {start_hour}:{start_min:02d}. Step 2: Journey {add_hours}h {add_mins}m. Step 3: Arrive {end_hour}:{end_min:02d}. ✓"
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 7,
                'difficulty_band': 'proficient',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 8: Elapsed Time (Proficient)
# ============================================================

def generate_level_8():
    """Level 8: Calculating Elapsed Time"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            start_hour = random.randint(8, 12)
            start_min = random.choice([0, 15, 30, 45])
            end_hour = random.randint(start_hour + 1, 17)
            end_min = random.choice([0, 15, 30, 45])
            
            diff_hours, diff_mins = time_difference(start_hour, start_min, end_hour, end_min)
            
            q_type = random.choice(['basic', 'word', 'school'])
            
            if q_type == 'basic':
                q_text = f"How long is it from {start_hour}:{start_min:02d} to {end_hour}:{end_min:02d}?"
                if diff_mins == 0:
                    correct = f"{diff_hours} hour{'s' if diff_hours != 1 else ''}"
                else:
                    correct = f"{diff_hours} hour{'s' if diff_hours != 1 else ''} {diff_mins} minutes"
                wrong = [f"{diff_hours + 1} hours", f"{diff_hours} hours {diff_mins + 15} minutes", f"{diff_hours - 1} hours {diff_mins} minutes"]
                explanation = f"Step 1: From {start_hour}:{start_min:02d} to {end_hour}:{end_min:02d}. Step 2: Duration = {correct}. ✓"
                
            elif q_type == 'word':
                name = random.choice(IRISH_NAMES)
                q_text = f"{name} started reading at {start_hour}:{start_min:02d} and stopped at {end_hour}:{end_min:02d}. How long did they read?"
                if diff_mins == 0:
                    correct = f"{diff_hours} hour{'s' if diff_hours != 1 else ''}"
                else:
                    correct = f"{diff_hours} hour{'s' if diff_hours != 1 else ''} {diff_mins} minutes"
                wrong = [f"{diff_hours + 1} hours", f"{diff_mins} minutes", f"{diff_hours} hours"]
                explanation = f"Step 1: {end_hour}:{end_min:02d} - {start_hour}:{start_min:02d} = {correct}. ✓"
                
            else:  # school
                q_text = f"School starts at {start_hour}:{start_min:02d} and finishes at {end_hour}:{end_min:02d}. How long is the school day?"
                if diff_mins == 0:
                    correct = f"{diff_hours} hours"
                else:
                    correct = f"{diff_hours} hours {diff_mins} minutes"
                wrong = [f"{diff_hours + 1} hours", f"{diff_hours - 1} hours", f"{diff_hours} hours {diff_mins + 30} minutes"]
                explanation = f"Step 1: {end_hour}:{end_min:02d} - {start_hour}:{start_min:02d} = {correct}. ✓"
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 8,
                'difficulty_band': 'proficient',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 9: Time Word Problems (Proficient)
# ============================================================

def generate_level_9():
    """Level 9: Time Word Problems"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            problem_type = random.randint(1, 4)
            name = random.choice(IRISH_NAMES)
            
            if problem_type == 1:
                # Before/after
                event_hour = random.randint(10, 16)
                event_min = random.choice([0, 30])
                before_mins = random.choice([15, 30, 45])
                
                arrival_hour, arrival_min = subtract_time(event_hour, event_min, 0, before_mins)
                
                q_text = f"{name} needs to arrive {before_mins} minutes before their {event_hour}:{event_min:02d} appointment. When should they arrive?"
                correct = f"{arrival_hour}:{arrival_min:02d}"
                wrong = [f"{event_hour}:{event_min:02d}", f"{arrival_hour}:{(arrival_min + 15) % 60:02d}", f"{arrival_hour + 1}:{arrival_min:02d}"]
                explanation = f"Step 1: {event_hour}:{event_min:02d} - {before_mins} minutes = {arrival_hour}:{arrival_min:02d}. ✓"
                
            elif problem_type == 2:
                # Multiple activities
                start = random.randint(9, 11)
                act1 = 45
                act2 = 30
                total = act1 + act2
                end_hour, end_min = add_time(start, 0, 0, total)
                
                q_text = f"{name} starts at {start}:00. They do maths for {act1} minutes and reading for {act2} minutes. When do they finish?"
                correct = f"{end_hour}:{end_min:02d}"
                wrong = [f"{start + 1}:00", f"{end_hour}:{(end_min + 15) % 60:02d}", f"{start}:{total:02d}"]
                explanation = f"Step 1: Total time = {total} minutes. Step 2: {start}:00 + {total} min = {end_hour}:{end_min:02d}. ✓"
                
            elif problem_type == 3:
                # Break calculation
                total_time = random.choice([90, 120, 150])
                break_time = random.choice([15, 20, 30])
                work_time = total_time - break_time
                
                q_text = f"A class lasts {total_time} minutes including a {break_time} minute break. How long is the actual class time?"
                correct = f"{work_time} minutes"
                wrong = [f"{total_time} minutes", f"{work_time + 10} minutes", f"{break_time} minutes"]
                explanation = f"Step 1: {total_time} - {break_time} = {work_time} minutes of class. ✓"
                
            else:
                # Time zones (simple)
                dublin_hour = random.randint(10, 16)
                diff = random.choice([1, 5, 8])
                other_hour = (dublin_hour + diff) % 24
                
                city = "London" if diff == 1 else "New York" if diff == 5 else "Tokyo"
                
                q_text = f"When it's {dublin_hour}:00 in Dublin, it's {diff} hour{'s' if diff != 1 else ''} {'later' if diff > 0 else 'earlier'} in {city}. What time is it in {city}?"
                correct = f"{other_hour}:00"
                wrong = [f"{dublin_hour}:00", f"{(other_hour + 1) % 24}:00", f"{(dublin_hour - diff) % 24}:00"]
                explanation = f"Step 1: {dublin_hour}:00 + {diff} hours = {other_hour}:00. ✓"
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 9,
                'difficulty_band': 'proficient',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 10: Complex Time Calculations (Advanced)
# ============================================================

def generate_level_10():
    """Level 10: Complex Time Calculations"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            problem_type = random.randint(1, 4)
            name = random.choice(IRISH_NAMES)
            
            if problem_type == 1:
                # Working backwards
                end_hour = random.randint(14, 18)
                end_min = random.choice([0, 30])
                duration_hours = random.randint(1, 3)
                duration_mins = random.choice([15, 30, 45])
                
                start_hour, start_min = subtract_time(end_hour, end_min, duration_hours, duration_mins)
                
                q_text = f"{name} finished a {duration_hours} hour {duration_mins} minute film at {end_hour}:{end_min:02d}. When did it start?"
                correct = f"{start_hour}:{start_min:02d}"
                wrong = [f"{end_hour}:{end_min:02d}", f"{start_hour + 1}:{start_min:02d}", f"{start_hour}:{(start_min + 30) % 60:02d}"]
                explanation = f"Step 1: {end_hour}:{end_min:02d} - {duration_hours}h {duration_mins}m = {start_hour}:{start_min:02d}. ✓"
                
            elif problem_type == 2:
                # Multiple segments
                leave_home = random.randint(7, 8)
                walk_mins = random.choice([15, 20, 25])
                wait_mins = random.choice([5, 10])
                bus_mins = random.choice([20, 25, 30])
                total = walk_mins + wait_mins + bus_mins
                
                arrive_hour, arrive_min = add_time(leave_home, 0, 0, total)
                
                q_text = f"{name} leaves home at {leave_home}:00. Walks {walk_mins} min, waits {wait_mins} min, bus takes {bus_mins} min. When arrive at school?"
                correct = f"{arrive_hour}:{arrive_min:02d}"
                wrong = [f"{arrive_hour}:{(arrive_min + 15) % 60:02d}", f"{leave_home + 1}:00", f"{arrive_hour - 1}:{arrive_min:02d}"]
                explanation = f"Step 1: Total journey = {total} minutes. Step 2: Arrive at {arrive_hour}:{arrive_min:02d}. ✓"
                
            elif problem_type == 3:
                # Comparison
                alice_start = 9
                alice_end = 12
                alice_break = 30
                bob_start = 10
                bob_end = 13
                bob_break = 45
                
                alice_work = (alice_end - alice_start) * 60 - alice_break
                bob_work = (bob_end - bob_start) * 60 - bob_break
                diff = abs(alice_work - bob_work)
                
                q_text = f"Alice works {alice_start}:00-{alice_end}:00 with {alice_break} min break. Bob works {bob_start}:00-{bob_end}:00 with {bob_break} min break. Who works longer and by how much?"
                longer = "Alice" if alice_work > bob_work else "Bob"
                correct = f"{longer} by {diff} minutes"
                wrong = [f"{'Bob' if longer == 'Alice' else 'Alice'} by {diff} minutes", f"Same time", f"{longer} by {diff + 15} minutes"]
                explanation = f"Step 1: Alice = {alice_work} min, Bob = {bob_work} min. Step 2: {longer} works {diff} min more. ✓"
                
            else:
                # Days and hours
                total_hours = random.randint(30, 60)
                days = total_hours // 24
                remaining_hours = total_hours % 24
                
                q_text = f"A project takes {total_hours} hours. How many complete days and hours is that?"
                correct = f"{days} days {remaining_hours} hours"
                wrong = [f"{days + 1} days", f"{days} days", f"{days - 1} days {remaining_hours + 24} hours"]
                explanation = f"Step 1: {total_hours} ÷ 24 = {days} remainder {remaining_hours}. Step 2: = {days} days {remaining_hours} hours. ✓"
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 10,
                'difficulty_band': 'advanced',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 11: Timetables (Advanced)
# ============================================================

def generate_level_11():
    """Level 11: Reading and Using Timetables"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            problem_type = random.randint(1, 4)
            
            if problem_type == 1:
                # Bus timetable
                buses = [
                    (8, 15), (8, 45), (9, 15), (9, 45), (10, 15)
                ]
                current_hour = random.choice([8, 9])
                current_min = random.randint(20, 40)
                
                # Find next bus
                next_bus = None
                for h, m in buses:
                    if h > current_hour or (h == current_hour and m > current_min):
                        next_bus = (h, m)
                        break
                
                if next_bus:
                    q_text = f"Bus times: 8:15, 8:45, 9:15, 9:45, 10:15. It's now {current_hour}:{current_min:02d}. When is the next bus?"
                    correct = f"{next_bus[0]}:{next_bus[1]:02d}"
                    wrong = [f"{buses[0][0]}:{buses[0][1]:02d}", f"{current_hour}:{current_min:02d}", f"10:15"]
                    explanation = f"Step 1: Current time is {current_hour}:{current_min:02d}. Step 2: Next bus after this is {correct}. ✓"
                else:
                    continue
                    
            elif problem_type == 2:
                # Journey time from timetable
                depart = (9, 30)
                arrive = (10, 45)
                journey_mins = (arrive[0] - depart[0]) * 60 + (arrive[1] - depart[1])
                
                q_text = f"A train departs at {depart[0]}:{depart[1]:02d} and arrives at {arrive[0]}:{arrive[1]:02d}. How long is the journey?"
                correct = f"{journey_mins // 60} hour{'s' if journey_mins >= 120 else ''} {journey_mins % 60} minutes"
                wrong = [f"2 hours", f"1 hour", f"1 hour 30 minutes"]
                explanation = f"Step 1: {arrive[0]}:{arrive[1]:02d} - {depart[0]}:{depart[1]:02d} = {journey_mins} minutes = {correct}. ✓"
                
            elif problem_type == 3:
                # Frequency
                first_bus = 7
                frequency = random.choice([15, 20, 30])
                num_buses = random.randint(3, 5)
                last_bus_hour = first_bus + (num_buses * frequency) // 60
                last_bus_min = (num_buses * frequency) % 60
                
                q_text = f"Buses run every {frequency} minutes starting at {first_bus}:00. What time is the {num_buses + 1}{'st' if num_buses == 0 else 'nd' if num_buses == 1 else 'rd' if num_buses == 2 else 'th'} bus?"
                correct = f"{last_bus_hour}:{last_bus_min:02d}"
                wrong = [f"{first_bus}:{frequency:02d}", f"{last_bus_hour}:{(last_bus_min + frequency) % 60:02d}", f"{first_bus + num_buses}:00"]
                explanation = f"Step 1: {num_buses} × {frequency} = {num_buses * frequency} minutes after {first_bus}:00 = {correct}. ✓"
                
            else:
                # Waiting time
                current = (9, 20)
                next_train = (9, 45)
                wait = (next_train[0] - current[0]) * 60 + (next_train[1] - current[1])
                
                q_text = f"It's {current[0]}:{current[1]:02d}. The next train is at {next_train[0]}:{next_train[1]:02d}. How long to wait?"
                correct = f"{wait} minutes"
                wrong = [f"{wait + 15} minutes", f"{wait - 10} minutes", f"1 hour"]
                explanation = f"Step 1: {next_train[0]}:{next_train[1]:02d} - {current[0]}:{current[1]:02d} = {wait} minutes wait. ✓"
            
            if q_text in used:
                continue
            used.add(q_text)
            
            options, correct_idx = make_options(correct, wrong)
            if len(set(options)) != 4:
                continue
            
            questions.append({
                'question_text': q_text,
                'option_a': options[0],
                'option_b': options[1],
                'option_c': options[2],
                'option_d': options[3],
                'correct_idx': correct_idx,
                'explanation': explanation,
                'image_svg': None,
                'difficulty': 11,
                'difficulty_band': 'advanced',
                'topic': TOPIC,
                'mode': MODE
            })
            
        except Exception as e:
            continue
    
    return questions

# ============================================================
# LEVEL 12: Mastery Challenge (Advanced)
# ============================================================

def generate_level_12():
    """Level 12: Mastery Challenge"""
    questions = []
    used = set()
    attempts = 0
    max_attempts = QUESTIONS_PER_LEVEL * 20
    
    generators = [generate_level_9, generate_level_10, generate_level_11]
    
    while len(questions) < QUESTIONS_PER_LEVEL and attempts < max_attempts:
        attempts += 1
        
        try:
            gen = random.choice(generators)
            source_questions = gen()
            
            if source_questions:
                q = random.choice(source_questions)
                q_text = q['question_text']
                
                if q_text in used:
                    continue
                used.add(q_text)
                
                q['difficulty'] = 12
                q['difficulty_band'] = 'advanced'
                questions.append(q)
                
        except Exception as e:
            continue
    
    return questions

# ============================================================
# VALIDATION & DATABASE
# ============================================================

def validate_questions(questions):
    errors = []
    level_counts = {}
    
    for i, q in enumerate(questions):
        level = q['difficulty']
        level_counts[level] = level_counts.get(level, 0) + 1
        
        if q['mode'] != 'numeracy':
            errors.append(f"Level {level} Q{i}: Wrong mode")
        
        options = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(options)) != 4:
            errors.append(f"Level {level} Q{i}: Duplicate options")
    
    print("\n" + "="*60)
    print("VALIDATION - Time & Clocks")
    print("="*60)
    
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        status = "✓" if count >= QUESTIONS_PER_LEVEL else "✗"
        print(f"Level {level:2}: {count:2}/{QUESTIONS_PER_LEVEL} {status}")
    
    print("="*60)
    print(f"Total: {len(questions)} | Errors: {len(errors)}")
    
    return len(errors)

def insert_questions(questions):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = ? AND mode = ?", (TOPIC, MODE))
    print(f"Deleted {cursor.rowcount} existing questions")
    
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
                q['question_text'], q['option_a'], q['option_b'],
                q['option_c'], q['option_d'], q['correct_idx'],
                q['topic'], q['difficulty'], q['difficulty_band'],
                q['mode'], q['explanation'], q.get('image_svg')
            ))
            inserted += 1
        except Exception as e:
            print(f"Insert error: {e}")
    
    conn.commit()
    conn.close()
    print(f"Inserted {inserted} questions")

def main():
    print("="*60)
    print("AgentMath - Time & Clocks Generator")
    print("Numeracy Strand | Target: 600 questions")
    print("="*60)
    
    all_questions = []
    
    generators = [
        (1, "O'Clock Times", generate_level_1),
        (2, "Half Past", generate_level_2),
        (3, "Quarter Past/To", generate_level_3),
        (4, "5-Minute Intervals", generate_level_4),
        (5, "24-Hour Time", generate_level_5),
        (6, "Time Units", generate_level_6),
        (7, "Adding Time", generate_level_7),
        (8, "Elapsed Time", generate_level_8),
        (9, "Word Problems", generate_level_9),
        (10, "Complex Calculations", generate_level_10),
        (11, "Timetables", generate_level_11),
        (12, "Mastery Challenge", generate_level_12),
    ]
    
    for level, name, gen_func in generators:
        print(f"Generating Level {level}: {name}...")
        questions = gen_func()
        print(f"  Generated {len(questions)} questions")
        all_questions.extend(questions)
    
    validate_questions(all_questions)
    
    response = input("\nInsert into database? (y/n): ").strip().lower()
    if response == 'y':
        insert_questions(all_questions)
        print("\n✓ Done!")

if __name__ == "__main__":
    main()
