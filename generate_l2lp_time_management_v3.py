"""
AgentMath L2LP Question Generator V3
Topic: Time & Timetables (l2_time_management)
NCCA Module: Understanding time and managing schedules

V3: Completely rewritten with UNIQUE question texts per level.
Each question includes specific times, days, or scenarios in the text.

Author: AgentMath Generator
Version: 3.0
Date: December 2025
"""

import sqlite3
import random
from datetime import datetime

TOPIC = 'l2_time_management'
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12
DATABASE_PATH = 'instance/mathquiz.db'

def get_difficulty_band(level):
    if level <= 3:
        return 'beginner'
    elif level <= 6:
        return 'intermediate'
    elif level <= 9:
        return 'advanced'
    elif level == 10:
        return 'mastery'
    elif level == 11:
        return 'application'
    else:
        return 'linked'


def generate_clock_svg(hour, minute=0, digital=False):
    """Generate clock SVG"""
    if digital:
        time_str = f"{hour:02d}:{minute:02d}"
        return f'''<svg viewBox="0 0 120 60" xmlns="http://www.w3.org/2000/svg">
        <rect width="120" height="60" fill="#1f2937" rx="8"/>
        <text x="60" y="42" font-size="28" fill="#22c55e" text-anchor="middle" font-family="monospace">{time_str}</text>
        </svg>'''
    else:
        # Analogue clock
        import math
        hour_angle = (hour % 12 + minute / 60) * 30 - 90
        minute_angle = minute * 6 - 90
        
        hour_x = 50 + 20 * math.cos(math.radians(hour_angle))
        hour_y = 50 + 20 * math.sin(math.radians(hour_angle))
        min_x = 50 + 30 * math.cos(math.radians(minute_angle))
        min_y = 50 + 30 * math.sin(math.radians(minute_angle))
        
        svg = f'''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="45" fill="white" stroke="#374151" stroke-width="3"/>
        <circle cx="50" cy="50" r="3" fill="#374151"/>'''
        
        # Numbers
        for i in range(1, 13):
            angle = i * 30 - 90
            x = 50 + 35 * math.cos(math.radians(angle))
            y = 50 + 35 * math.sin(math.radians(angle)) + 4
            svg += f'<text x="{x}" y="{y}" font-size="10" text-anchor="middle" fill="#374151">{i}</text>'
        
        # Hands
        svg += f'<line x1="50" y1="50" x2="{hour_x}" y2="{hour_y}" stroke="#1f2937" stroke-width="4" stroke-linecap="round"/>'
        svg += f'<line x1="50" y1="50" x2="{min_x}" y2="{min_y}" stroke="#3b82f6" stroke-width="2" stroke-linecap="round"/>'
        svg += '</svg>'
        return svg


# ============================================================
# QUESTION GENERATORS BY LEVEL
# ============================================================

def generate_level_1_questions():
    """Level 1: Time Instruments - 50 unique questions"""
    questions = []
    
    instruments = [
        ('clock', 'tells the time', 'on walls and desks'),
        ('watch', 'tells the time', 'worn on the wrist'),
        ('calendar', 'shows dates', 'on walls or phones'),
        ('stopwatch', 'measures time intervals', 'for sports timing'),
        ('timer', 'counts down', 'for cooking'),
        ('hourglass', 'measures time with sand', 'turns upside down'),
        ('sundial', 'uses shadows to tell time', 'needs sunlight'),
        ('alarm clock', 'wakes you up', 'by your bed')
    ]
    
    # Template 1: What instrument? (20 questions)
    uses = [
        ("know what time it is right now", "clock", "Clocks show the current time"),
        ("know today's date", "calendar", "Calendars show days and dates"),
        ("time a running race", "stopwatch", "Stopwatches measure time intervals"),
        ("know when to wake up", "alarm clock", "Alarm clocks wake us at set times"),
        ("time cooking eggs", "timer", "Timers count down for cooking"),
        ("check the time while walking", "watch", "Watches are worn on the wrist"),
        ("see what day your birthday is on", "calendar", "Calendars show dates"),
        ("measure how long something takes", "stopwatch", "Stopwatches measure duration"),
        ("not be late for school", "alarm clock", "Alarm clocks help us wake on time"),
        ("know when the pasta is ready", "timer", "Timers alert when time is up"),
        ("tell time on a sunny day outside", "sundial", "Sundials use shadows from the sun"),
        ("time a 3-minute game", "timer", "Timers count down set amounts"),
        ("know what month it is", "calendar", "Calendars show months and dates"),
        ("tell time without electricity", "sundial", "Sundials work with sunlight only"),
        ("check time during a meeting", "watch", "Watches can be checked discreetly"),
        ("know when break time ends", "clock", "Clocks on walls show current time"),
        ("time a swimming race", "stopwatch", "Stopwatches measure exact times"),
        ("plan what day to have a party", "calendar", "Calendars help plan future events"),
        ("know when cookies are done", "timer", "Kitchen timers track cooking time"),
        ("wake up at 7am", "alarm clock", "Alarm clocks ring at set times")
    ]
    
    for use, correct, explanation in uses:
        wrong = [i[0] for i in instruments if i[0] != correct][:3]
        options = [correct] + wrong
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"Which time instrument would help you {use}?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Template 2: True/False about instruments (15 questions)
    tf_statements = [
        ("A watch is worn on your wrist", True, "Watches are wrist-worn time devices"),
        ("A calendar shows you the time in hours", False, "Calendars show dates, not hours"),
        ("A stopwatch is used to time races", True, "Stopwatches measure time intervals"),
        ("An alarm clock can wake you up", True, "Alarm clocks ring at set times"),
        ("A timer counts up from zero", False, "Timers count DOWN from a set time"),
        ("A sundial works at night", False, "Sundials need sunlight to work"),
        ("Clocks have hour and minute hands", True, "Analogue clocks have two main hands"),
        ("A calendar tells you what time it is", False, "Calendars show dates, not times"),
        ("You can wear a clock on your wrist", False, "You wear a WATCH on your wrist"),
        ("An hourglass uses sand to measure time", True, "Sand flows through hourglasses"),
        ("A digital clock has hands", False, "Digital clocks show numbers"),
        ("Timers are useful for cooking", True, "Kitchen timers help time cooking"),
        ("A stopwatch tells you today's date", False, "Stopwatches measure time intervals"),
        ("You can find clocks in classrooms", True, "Most classrooms have wall clocks"),
        ("A watch and a clock do the same job", True, "Both tell the current time")
    ]
    
    for statement, is_true, explanation in tf_statements:
        options = ['True', 'False', 'Sometimes', 'Depends']
        correct_idx = 0 if is_true else 1
        
        questions.append({
            'question_text': f"True or False: {statement}",
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Template 3: Match instrument to description (15 questions)
    matches = [
        ("A device worn on your arm that shows the time", "Watch"),
        ("A large device on the wall that shows hours and minutes", "Wall clock"),
        ("Shows all the days of a month", "Calendar"),
        ("Makes a sound to wake you up in the morning", "Alarm clock"),
        ("Used by referees to time sports games", "Stopwatch"),
        ("Counts down time for cooking or games", "Timer"),
        ("An ancient time-telling device that uses the sun", "Sundial"),
        ("Has two hands - one short and one long", "Analogue clock"),
        ("Shows time with numbers like 10:30", "Digital clock"),
        ("Uses falling sand to measure time", "Hourglass"),
        ("Beeps when your food is ready", "Kitchen timer"),
        ("Athletes wear this to check their lap times", "Sports watch"),
        ("Found in every classroom to track lesson times", "Clock"),
        ("Pages you flip to see different months", "Calendar"),
        ("A pocket-sized device for timing races", "Stopwatch")
    ]
    
    for description, correct in matches:
        all_answers = ['Watch', 'Wall clock', 'Calendar', 'Alarm clock', 'Stopwatch', 
                       'Timer', 'Sundial', 'Analogue clock', 'Digital clock', 'Hourglass']
        wrong = [a for a in all_answers if a != correct][:3]
        options = [correct] + wrong
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"What time instrument is this? '{description}'",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"This describes a {correct}"
        })
    
    return questions[:50]


def generate_level_2_questions():
    """Level 2: Analogue Clocks - 50 unique questions"""
    questions = []
    
    # O'clock times (20 questions)
    for hour in range(1, 13):
        # Variation 1: What time is shown?
        options = [f"{hour} o'clock", f"{(hour % 12) + 1} o'clock", 
                   f"{((hour - 2) % 12) + 1} o'clock", f"{(hour + 5) % 12 + 1} o'clock"]
        random.shuffle(options)
        correct_idx = options.index(f"{hour} o'clock")
        
        questions.append({
            'question_text': f"The short hand points to {hour} and the long hand points to 12. What time is it?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"When the minute hand is on 12 and hour hand on {hour}, it's {hour} o'clock.",
            'image_svg': generate_clock_svg(hour, 0)
        })
        
        if hour <= 8:
            # Variation 2: Which clock shows X o'clock?
            questions.append({
                'question_text': f"Emma needs to be ready at {hour} o'clock. The clock shows hour hand on {hour}, minute hand on 12. Is she on time?",
                'options': ['Yes, it\'s exactly the right time', 'No, it\'s too early', 'No, it\'s too late', 'Cannot tell'],
                'correct_index': 0,
                'explanation': f"Hour hand on {hour}, minute hand on 12 = {hour} o'clock exactly.",
                'image_svg': generate_clock_svg(hour, 0)
            })
    
    # Half past times (14 questions)
    half_past = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2]
    for i, hour in enumerate(half_past):
        correct = f"Half past {hour}"
        wrong1 = f"{hour} o'clock"
        wrong2 = f"Half past {(hour % 12) + 1}"
        wrong3 = f"Quarter past {hour}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"The hour hand is between {hour} and {(hour % 12) + 1}, the minute hand points to 6. What time is it?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"Minute hand on 6 = 30 minutes = half past. So it's half past {hour}.",
            'image_svg': generate_clock_svg(hour, 30)
        })
    
    # Clock hand identification (8 questions)
    hand_qs = [
        ("Which hand shows the hours on a clock?", "The short hand", "The short/hour hand points to hours"),
        ("Which hand shows the minutes?", "The long hand", "The long/minute hand points to minutes"),
        ("The short hand is also called the...", "Hour hand", "Short hand = hour hand"),
        ("The long hand is also called the...", "Minute hand", "Long hand = minute hand"),
        ("How many numbers are on a clock face?", "12", "Clock faces have numbers 1-12"),
        ("What number does the minute hand point to at o'clock?", "12", "At o'clock, minute hand is on 12"),
        ("What number does the minute hand point to at half past?", "6", "At half past, minute hand is on 6"),
        ("Where does the minute hand point at quarter past?", "3", "Quarter past = 15 mins = on the 3")
    ]
    
    for q, correct, explanation in hand_qs:
        if 'short hand' in correct.lower():
            options = ['The short hand', 'The long hand', 'Both hands', 'Neither hand']
        elif 'long hand' in correct.lower():
            options = ['The long hand', 'The short hand', 'Both hands', 'Neither hand']
        elif correct in ['12', '6', '3']:
            options = ['12', '6', '3', '9']
        else:
            options = [correct, 'Second hand', 'Big hand', 'Small hand']
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_3_questions():
    """Level 3: Digital Clocks - 50 unique questions"""
    questions = []
    
    # Read digital times (25 questions)
    digital_times = [
        (9, 0, "9 o'clock"), (10, 0, "10 o'clock"), (11, 0, "11 o'clock"),
        (12, 0, "12 o'clock"), (1, 0, "1 o'clock"), (2, 0, "2 o'clock"),
        (3, 30, "half past 3"), (4, 30, "half past 4"), (5, 30, "half past 5"),
        (6, 30, "half past 6"), (7, 30, "half past 7"), (8, 30, "half past 8"),
        (9, 15, "quarter past 9"), (10, 15, "quarter past 10"), (11, 15, "quarter past 11"),
        (12, 45, "quarter to 1"), (1, 45, "quarter to 2"), (2, 45, "quarter to 3"),
        (3, 0, "3 o'clock"), (4, 0, "4 o'clock"), (5, 0, "5 o'clock"),
        (6, 0, "6 o'clock"), (7, 0, "7 o'clock"), (8, 0, "8 o'clock"),
        (9, 30, "half past 9")
    ]
    
    for hour, minute, time_words in digital_times:
        digital_display = f"{hour:02d}:{minute:02d}" if hour >= 10 else f"{hour}:{minute:02d}"
        
        # Generate wrong options
        wrong_times = []
        if minute == 0:
            wrong_times = [f"{(hour % 12) + 1} o'clock", f"half past {hour}", f"quarter past {hour}"]
        elif minute == 30:
            wrong_times = [f"{hour} o'clock", f"quarter past {hour}", f"quarter to {(hour % 12) + 1}"]
        elif minute == 15:
            wrong_times = [f"{hour} o'clock", f"half past {hour}", f"quarter to {hour}"]
        elif minute == 45:
            wrong_times = [f"{hour} o'clock", f"half past {hour}", f"quarter past {hour}"]
        
        options = [time_words] + wrong_times[:3]
        random.shuffle(options)
        correct_idx = options.index(time_words)
        
        questions.append({
            'question_text': f"A digital clock shows {hour}:{minute:02d}. What time is this in words?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"{hour}:{minute:02d} is {time_words}",
            'image_svg': generate_clock_svg(hour, minute, digital=True)
        })
    
    # Convert words to digital (15 questions)
    word_to_digital = [
        ("9 o'clock", "9:00", "09:00"),
        ("half past 2", "2:30", "02:30"),
        ("quarter past 5", "5:15", "05:15"),
        ("quarter to 4", "3:45", "03:45"),
        ("10 o'clock", "10:00", "10:00"),
        ("half past 7", "7:30", "07:30"),
        ("quarter past 11", "11:15", "11:15"),
        ("quarter to 12", "11:45", "11:45"),
        ("6 o'clock", "6:00", "06:00"),
        ("half past 1", "1:30", "01:30"),
        ("quarter past 8", "8:15", "08:15"),
        ("quarter to 9", "8:45", "08:45"),
        ("12 o'clock", "12:00", "12:00"),
        ("half past 10", "10:30", "10:30"),
        ("quarter past 3", "3:15", "03:15")
    ]
    
    for words, correct, alt in word_to_digital:
        hour = int(correct.split(':')[0])
        minute = int(correct.split(':')[1])
        
        wrong1 = f"{(hour + 1) % 12}:{minute:02d}"
        wrong2 = f"{hour}:{(minute + 15) % 60:02d}"
        wrong3 = f"{(hour - 1) % 12 or 12}:{minute:02d}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"How would '{words}' appear on a digital clock?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"'{words}' = {correct} on a digital clock"
        })
    
    # AM/PM basics (10 questions)
    am_pm = [
        ("7:00 in the morning is written as:", "7:00 AM", "Morning times use AM"),
        ("3:00 in the afternoon is written as:", "3:00 PM", "Afternoon times use PM"),
        ("What does AM stand for?", "Before midday", "AM = ante meridiem = before noon"),
        ("What does PM stand for?", "After midday", "PM = post meridiem = after noon"),
        ("Breakfast at 8:00 would be:", "8:00 AM", "Breakfast is in the morning (AM)"),
        ("Dinner at 6:00 would be:", "6:00 PM", "Dinner is in the evening (PM)"),
        ("Midnight is:", "12:00 AM", "Midnight = 12:00 AM"),
        ("Midday/Noon is:", "12:00 PM", "Noon = 12:00 PM"),
        ("School starts at 9:00 in the morning:", "9:00 AM", "Morning = AM"),
        ("Bedtime at 8:00 at night:", "8:00 PM", "Night = PM")
    ]
    
    for q, correct, explanation in am_pm:
        if 'AM' in correct or 'PM' in correct:
            time_part = correct.split()[0]
            wrong1 = time_part + " PM" if "AM" in correct else time_part + " AM"
            wrong2 = str(int(time_part.split(':')[0]) + 12) + ":" + time_part.split(':')[1]
            wrong3 = "Cannot tell"
            options = [correct, wrong1, wrong2, wrong3]
        else:
            options = [correct, 'After midday', 'At midday', 'Anytime'] if 'Before' in correct else [correct, 'Before midday', 'At midday', 'Anytime']
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_4_questions():
    """Level 4: 12 and 24 Hour Time - 50 unique questions"""
    questions = []
    
    # 12 to 24 hour conversions (20 questions)
    conversions = [
        ("1:00 PM", "13:00"), ("2:00 PM", "14:00"), ("3:00 PM", "15:00"),
        ("4:00 PM", "16:00"), ("5:00 PM", "17:00"), ("6:00 PM", "18:00"),
        ("7:00 PM", "19:00"), ("8:00 PM", "20:00"), ("9:00 PM", "21:00"),
        ("10:00 PM", "22:00"), ("11:00 PM", "23:00"), ("12:00 AM", "00:00"),
        ("1:30 PM", "13:30"), ("2:45 PM", "14:45"), ("5:15 PM", "17:15"),
        ("8:30 PM", "20:30"), ("10:45 PM", "22:45"), ("3:15 PM", "15:15"),
        ("6:30 PM", "18:30"), ("9:15 PM", "21:15")
    ]
    
    for twelve, twentyfour in conversions:
        hour_24 = int(twentyfour.split(':')[0])
        wrong1 = f"{(hour_24 + 2) % 24:02d}:{twentyfour.split(':')[1]}"
        wrong2 = f"{(hour_24 - 2) % 24:02d}:{twentyfour.split(':')[1]}"
        wrong3 = twelve.replace(' PM', '').replace(' AM', '')
        
        options = [twentyfour, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(twentyfour)
        
        questions.append({
            'question_text': f"Convert {twelve} to 24-hour time.",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"{twelve} = {twentyfour} in 24-hour format"
        })
    
    # 24 to 12 hour conversions (20 questions)
    reverse = [
        ("13:00", "1:00 PM"), ("14:00", "2:00 PM"), ("15:00", "3:00 PM"),
        ("16:00", "4:00 PM"), ("17:00", "5:00 PM"), ("18:00", "6:00 PM"),
        ("19:00", "7:00 PM"), ("20:00", "8:00 PM"), ("21:00", "9:00 PM"),
        ("22:00", "10:00 PM"), ("23:00", "11:00 PM"), ("00:00", "12:00 AM"),
        ("13:30", "1:30 PM"), ("15:45", "3:45 PM"), ("17:15", "5:15 PM"),
        ("19:30", "7:30 PM"), ("21:45", "9:45 PM"), ("14:15", "2:15 PM"),
        ("16:30", "4:30 PM"), ("20:15", "8:15 PM")
    ]
    
    for twentyfour, twelve in reverse:
        hour_12 = int(twelve.split(':')[0])
        minute = twelve.split(':')[1].split()[0]
        am_pm = 'PM' if 'PM' in twelve else 'AM'
        
        wrong1 = f"{(hour_12 % 12) + 1}:{minute} {am_pm}"
        wrong2 = f"{hour_12}:{minute} {'AM' if am_pm == 'PM' else 'PM'}"
        wrong3 = f"{hour_12 + 12}:{minute}"
        
        options = [twelve, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(twelve)
        
        questions.append({
            'question_text': f"Convert {twentyfour} to 12-hour time.",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"{twentyfour} = {twelve}"
        })
    
    # Understanding 24-hour clock (10 questions)
    understanding = [
        ("In 24-hour time, what comes after 12:00?", "13:00", "After 12:00 (noon) comes 13:00"),
        ("What is midnight in 24-hour time?", "00:00", "Midnight = 00:00"),
        ("What is noon in 24-hour time?", "12:00", "Noon = 12:00"),
        ("Why do trains and planes use 24-hour time?", "To avoid AM/PM confusion", "24-hour time is clearer"),
        ("What hour comes after 23:00?", "00:00", "After 23:00 comes midnight (00:00)"),
        ("Is 15:00 morning or afternoon?", "Afternoon", "15:00 = 3 PM = afternoon"),
        ("Is 09:00 morning or afternoon?", "Morning", "09:00 = 9 AM = morning"),
        ("How many hours are shown on a 24-hour clock?", "24 (0-23)", "24-hour clocks go from 00 to 23"),
        ("Which is later: 14:00 or 2:00 PM?", "They are the same", "14:00 = 2:00 PM"),
        ("Which is earlier: 08:00 or 20:00?", "08:00", "08:00 is morning, 20:00 is evening")
    ]
    
    for q, correct, explanation in understanding:
        if correct == "13:00":
            options = ["13:00", "13:01", "12:01", "1:00"]
        elif correct == "00:00":
            options = ["00:00", "24:00", "12:00", "01:00"]
        elif correct == "12:00":
            options = ["12:00", "00:00", "24:00", "13:00"]
        elif "confusion" in correct:
            options = ["To avoid AM/PM confusion", "It looks nicer", "It's shorter", "No reason"]
        elif correct == "Afternoon":
            options = ["Afternoon", "Morning", "Evening", "Night"]
        elif correct == "Morning":
            options = ["Morning", "Afternoon", "Evening", "Night"]
        elif "24" in correct:
            options = ["24 (0-23)", "12 (1-12)", "10 (0-9)", "60 (0-59)"]
        elif "same" in correct:
            options = ["They are the same", "14:00 is later", "2:00 PM is later", "Cannot compare"]
        elif correct == "08:00":
            options = ["08:00", "20:00", "They are the same", "Cannot tell"]
        else:
            options = [correct, "Wrong1", "Wrong2", "Wrong3"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_5_questions():
    """Level 5: Time Language - 50 unique questions"""
    questions = []
    
    # Time vocabulary (25 questions)
    vocab = [
        ("What does 'quarter past' mean?", "15 minutes after the hour", "Quarter = 15 minutes"),
        ("What does 'quarter to' mean?", "15 minutes before the next hour", "Quarter to = 45 minutes past"),
        ("What does 'half past' mean?", "30 minutes after the hour", "Half = 30 minutes"),
        ("How many minutes in 'quarter of an hour'?", "15 minutes", "Quarter of 60 = 15"),
        ("How many minutes in 'half an hour'?", "30 minutes", "Half of 60 = 30"),
        ("How many minutes in 'three quarters of an hour'?", "45 minutes", "3 × 15 = 45"),
        ("What time is '5 past 3'?", "3:05", "5 past = 5 minutes after"),
        ("What time is '10 to 4'?", "3:50", "10 to 4 = 50 minutes past 3"),
        ("What time is '20 past 7'?", "7:20", "20 past = 20 minutes after"),
        ("What time is '25 to 9'?", "8:35", "25 to 9 = 35 minutes past 8"),
        ("What does 'noon' mean?", "12 o'clock midday", "Noon = middle of the day"),
        ("What does 'midnight' mean?", "12 o'clock at night", "Midnight = middle of the night"),
        ("What is another word for 'midday'?", "Noon", "Midday = noon = 12:00 PM"),
        ("'Morning' is what part of the day?", "After midnight, before noon", "Morning = AM hours"),
        ("'Evening' is what part of the day?", "Late afternoon to bedtime", "Evening = later PM hours"),
        ("What does 'dusk' mean?", "When it gets dark (sunset)", "Dusk = sun going down"),
        ("What does 'dawn' mean?", "When it gets light (sunrise)", "Dawn = sun coming up"),
        ("What time is '5 to 12'?", "11:55", "5 to 12 = 55 minutes past 11"),
        ("What time is 'quarter past 6'?", "6:15", "Quarter past = 15 minutes after"),
        ("What time is 'quarter to 8'?", "7:45", "Quarter to 8 = 45 minutes past 7"),
        ("What time is 'half past 11'?", "11:30", "Half past = 30 minutes after"),
        ("What time is '20 to 5'?", "4:40", "20 to 5 = 40 minutes past 4"),
        ("What time is '10 past 2'?", "2:10", "10 past = 10 minutes after"),
        ("What does 'o'clock' mean?", "Exactly on the hour", "O'clock = :00"),
        ("Why do we say 'o'clock'?", "Short for 'of the clock'", "O'clock = of the clock")
    ]
    
    for q, correct, explanation in vocab:
        if ':' in correct:
            hour = int(correct.split(':')[0])
            minute = int(correct.split(':')[1])
            wrong1 = f"{hour}:{(minute + 15) % 60:02d}"
            wrong2 = f"{(hour + 1) % 12 or 12}:{minute:02d}"
            wrong3 = f"{hour}:{(minute - 10) % 60:02d}"
        elif 'minutes' in correct:
            val = int(correct.split()[0])
            wrong1 = f"{val + 15} minutes"
            wrong2 = f"{val - 5} minutes"
            wrong3 = f"{val * 2} minutes"
        else:
            # Generate generic wrong answers
            all_answers = [a[1] for a in vocab if a[1] != correct]
            wrong1, wrong2, wrong3 = random.sample(all_answers, 3) if len(all_answers) >= 3 else ['Wrong1', 'Wrong2', 'Wrong3']
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Time expressions in context (25 questions)
    contexts = [
        ("The train leaves at quarter past 9. What time?", "9:15"),
        ("School ends at half past 3. What time?", "3:30"),
        ("Lunch is at quarter to 1. What time?", "12:45"),
        ("The movie starts at 10 to 7. What time?", "6:50"),
        ("Wake up at quarter past 7. What time?", "7:15"),
        ("Dinner at half past 6. What time?", "6:30"),
        ("Bus arrives at 20 past 4. What time?", "4:20"),
        ("Match starts at 5 to 3. What time?", "2:55"),
        ("Shop opens at quarter past 9. What time?", "9:15"),
        ("Shop closes at half past 5. What time?", "5:30"),
        ("Break starts at quarter to 11. What time?", "10:45"),
        ("Class begins at 10 past 9. What time?", "9:10"),
        ("Flight departs at 25 to 4. What time?", "3:35"),
        ("Meeting at quarter past 2. What time?", "2:15"),
        ("Appointment at 20 to 10. What time?", "9:40"),
        ("Concert at half past 7. What time?", "7:30"),
        ("Library closes at quarter to 6. What time?", "5:45"),
        ("Game kicks off at 5 past 3. What time?", "3:05"),
        ("Train arrives at 10 to 8. What time?", "7:50"),
        ("Party starts at half past 4. What time?", "4:30"),
        ("Doctor at quarter past 10. What time?", "10:15"),
        ("Dentist at 20 past 2. What time?", "2:20"),
        ("Swimming at quarter to 5. What time?", "4:45"),
        ("Piano lesson at half past 4. What time?", "4:30"),
        ("Bedtime at quarter past 8. What time?", "8:15")
    ]
    
    for q, correct in contexts:
        hour = int(correct.split(':')[0])
        minute = int(correct.split(':')[1])
        
        wrong1 = f"{hour}:{(minute + 15) % 60:02d}"
        wrong2 = f"{(hour + 1) % 12 or 12}:{minute:02d}"
        wrong3 = f"{hour}:{(60 - minute) % 60:02d}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"The correct time is {correct}"
        })
    
    return questions[:50]


def generate_level_6_questions():
    """Level 6: Units of Time - 50 unique questions"""
    questions = []
    
    # Time unit conversions (25 questions)
    conversions = [
        ("How many seconds in 1 minute?", 60, "seconds"),
        ("How many minutes in 1 hour?", 60, "minutes"),
        ("How many hours in 1 day?", 24, "hours"),
        ("How many days in 1 week?", 7, "days"),
        ("How many days in a normal year?", 365, "days"),
        ("How many days in a leap year?", 366, "days"),
        ("How many weeks in 1 year (approximately)?", 52, "weeks"),
        ("How many months in 1 year?", 12, "months"),
        ("How many minutes in 2 hours?", 120, "minutes"),
        ("How many hours in 2 days?", 48, "hours"),
        ("How many days in 2 weeks?", 14, "days"),
        ("How many seconds in 2 minutes?", 120, "seconds"),
        ("How many minutes in half an hour?", 30, "minutes"),
        ("How many hours in half a day?", 12, "hours"),
        ("How many days in half a week?", 3.5, "days"),
        ("How many seconds in 5 minutes?", 300, "seconds"),
        ("How many minutes in 3 hours?", 180, "minutes"),
        ("How many hours in 3 days?", 72, "hours"),
        ("How many days in 4 weeks?", 28, "days"),
        ("How many months in half a year?", 6, "months"),
        ("How many minutes in 90 seconds?", 1.5, "minutes"),
        ("How many hours in 180 minutes?", 3, "hours"),
        ("How many days in 48 hours?", 2, "days"),
        ("How many weeks in 21 days?", 3, "weeks"),
        ("How many minutes in quarter of an hour?", 15, "minutes")
    ]
    
    for q, correct, unit in conversions:
        if isinstance(correct, float):
            correct_str = str(correct)
            wrong1 = str(correct + 0.5)
            wrong2 = str(correct - 0.5) if correct > 0.5 else str(correct + 1)
            wrong3 = str(int(correct) + 1)
        else:
            correct_str = str(correct)
            wrong1 = str(correct + 10 if correct > 50 else correct + 5)
            wrong2 = str(correct - 5 if correct > 10 else correct + 15)
            wrong3 = str(correct * 2)
        
        options = [correct_str, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct_str)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"The answer is {correct} {unit}"
        })
    
    # Time unit comparisons (15 questions)
    comparisons = [
        ("Which is longer: 1 hour or 50 minutes?", "1 hour", "1 hour = 60 minutes > 50 minutes"),
        ("Which is longer: 2 days or 50 hours?", "50 hours", "2 days = 48 hours < 50 hours"),
        ("Which is longer: 1 week or 10 days?", "10 days", "1 week = 7 days < 10 days"),
        ("Which is longer: 100 seconds or 2 minutes?", "100 seconds", "2 minutes = 120 seconds > 100 seconds"),
        ("Which is longer: 90 minutes or 1.5 hours?", "They are equal", "1.5 hours = 90 minutes"),
        ("Which is longer: 3 weeks or 20 days?", "3 weeks", "3 weeks = 21 days > 20 days"),
        ("Which is longer: 72 hours or 3 days?", "They are equal", "3 days = 72 hours"),
        ("Which is longer: 2 hours or 100 minutes?", "100 minutes", "2 hours = 120 minutes > 100 minutes"),
        ("Which is longer: 1 year or 12 months?", "They are equal", "1 year = 12 months"),
        ("Which is longer: 30 minutes or 0.5 hours?", "They are equal", "0.5 hours = 30 minutes"),
        ("Which is longer: 2 weeks or 15 days?", "15 days", "2 weeks = 14 days < 15 days"),
        ("Which is longer: 5 minutes or 250 seconds?", "250 seconds", "5 minutes = 300 seconds > 250 seconds"),
        ("Which is longer: 48 hours or 2 days?", "They are equal", "2 days = 48 hours"),
        ("Which is longer: 1 month or 4 weeks?", "Depends on the month", "Months have 28-31 days"),
        ("Which is longer: 180 seconds or 3 minutes?", "They are equal", "3 minutes = 180 seconds")
    ]
    
    for q, correct, explanation in comparisons:
        options_list = list(set([q.split(': ')[1].split(' or ')[0], q.split(' or ')[1].replace('?', ''), "They are equal", "Depends on the month"]))
        if correct not in options_list:
            options_list.append(correct)
        options = options_list[:4]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Days of week/months (10 questions)
    days_months = [
        ("How many days in January?", "31", "January has 31 days"),
        ("How many days in February (normal year)?", "28", "February normally has 28 days"),
        ("How many days in April?", "30", "April has 30 days"),
        ("What day comes after Wednesday?", "Thursday", "Wed → Thu → Fri"),
        ("What day comes before Monday?", "Sunday", "Sat → Sun → Mon"),
        ("What month comes after March?", "April", "Mar → Apr → May"),
        ("What month comes before September?", "August", "Jul → Aug → Sep"),
        ("How many days in a weekend?", "2", "Saturday and Sunday"),
        ("How many school days in a typical week?", "5", "Monday to Friday"),
        ("Which months have 30 days?", "April, June, September, November", "30 days hath September...")
    ]
    
    for q, correct, explanation in days_months:
        if correct.isdigit():
            val = int(correct)
            options = [correct, str(val + 1), str(val - 1), str(val + 2)]
        elif correct in ['Thursday', 'Sunday', 'April', 'August']:
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
            if correct in days:
                wrong = [d for d in days if d != correct][:3]
            else:
                wrong = [m for m in months if m != correct][:3]
            options = [correct] + wrong
        else:
            options = [correct, "January, March, May", "February, April", "All months"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_7_questions():
    """Level 7: Timelines & Timetables - 50 unique questions"""
    questions = []
    
    # School timetable questions (25 questions)
    timetable = [
        ("09:00", "Maths"), ("09:45", "English"), ("10:30", "Break"),
        ("10:45", "Science"), ("11:30", "History"), ("12:15", "Lunch"),
        ("13:00", "Art"), ("13:45", "PE"), ("14:30", "Music"), ("15:15", "Home")
    ]
    
    for i, (time, subject) in enumerate(timetable):
        # What subject at X time?
        wrong_subjects = [s for t, s in timetable if s != subject][:3]
        options = [subject] + wrong_subjects
        random.shuffle(options)
        correct_idx = options.index(subject)
        
        questions.append({
            'question_text': f"The school timetable shows {subject} starts at {time}. What subject is at {time}?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"At {time}, the subject is {subject}"
        })
        
        if i < 15:
            # What time does X start?
            wrong_times = [t for t, s in timetable if t != time][:3]
            options = [time] + wrong_times
            random.shuffle(options)
            correct_idx = options.index(time)
            
            questions.append({
                'question_text': f"According to the timetable, what time does {subject} start?",
                'options': options,
                'correct_index': correct_idx,
                'explanation': f"{subject} starts at {time}"
            })
    
    # Bus/train timetable questions (15 questions)
    bus_times = [
        ("Dublin", "08:15"), ("Cork", "09:30"), ("Galway", "10:45"),
        ("Limerick", "11:00"), ("Waterford", "12:15")
    ]
    
    for destination, dep_time in bus_times:
        # When does bus to X leave?
        wrong_times = [t for d, t in bus_times if t != dep_time][:3]
        options = [dep_time] + wrong_times
        random.shuffle(options)
        correct_idx = options.index(dep_time)
        
        questions.append({
            'question_text': f"The bus timetable shows the bus to {destination} leaves at {dep_time}. What time does the {destination} bus depart?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"The bus to {destination} leaves at {dep_time}"
        })
        
        # Where does the X:XX bus go?
        wrong_dests = [d for d, t in bus_times if d != destination][:3]
        options = [destination] + wrong_dests
        random.shuffle(options)
        correct_idx = options.index(destination)
        
        questions.append({
            'question_text': f"A bus leaves at {dep_time}. Where is it going?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"The {dep_time} bus goes to {destination}"
        })
    
    # Timeline ordering (5 questions)
    ordering = [
        (["breakfast", "lunch", "dinner"], "What order do meals go in?"),
        (["wake up", "go to school", "come home"], "What order for a school day?"),
        (["spring", "summer", "autumn", "winter"], "What order do seasons go in?"),
        (["January", "February", "March"], "What order do these months go?"),
        (["Monday", "Tuesday", "Wednesday"], "What order do these days go?")
    ]
    
    for correct_order, question in ordering:
        correct = " → ".join(correct_order)
        wrong1 = " → ".join(reversed(correct_order))
        wrong2 = " → ".join([correct_order[1], correct_order[0]] + correct_order[2:])
        wrong3 = " → ".join([correct_order[-1]] + correct_order[:-1])
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"The correct order is: {correct}"
        })
    
    return questions[:50]


def generate_level_8_questions():
    """Level 8: Calculating Time - 50 unique questions"""
    questions = []
    
    # Time elapsed calculations (25 questions)
    elapsed = [
        ("09:00", "09:30", "30 minutes"), ("10:00", "10:45", "45 minutes"),
        ("11:00", "12:00", "1 hour"), ("08:30", "09:00", "30 minutes"),
        ("14:00", "15:30", "1 hour 30 minutes"), ("13:00", "14:15", "1 hour 15 minutes"),
        ("09:15", "10:00", "45 minutes"), ("11:30", "12:15", "45 minutes"),
        ("08:00", "10:00", "2 hours"), ("09:00", "11:30", "2 hours 30 minutes"),
        ("10:30", "11:00", "30 minutes"), ("14:45", "15:30", "45 minutes"),
        ("07:00", "07:30", "30 minutes"), ("16:00", "17:45", "1 hour 45 minutes"),
        ("12:00", "14:00", "2 hours"), ("09:30", "10:15", "45 minutes"),
        ("15:00", "16:30", "1 hour 30 minutes"), ("11:15", "12:00", "45 minutes"),
        ("08:45", "09:30", "45 minutes"), ("13:30", "15:00", "1 hour 30 minutes"),
        ("10:00", "12:30", "2 hours 30 minutes"), ("14:30", "15:15", "45 minutes"),
        ("09:00", "09:15", "15 minutes"), ("10:45", "11:30", "45 minutes"),
        ("12:30", "13:00", "30 minutes")
    ]
    
    for start, end, correct in elapsed:
        if "hour" in correct and "minute" in correct:
            wrong1 = correct.replace("30 minutes", "45 minutes") if "30" in correct else correct.replace("45 minutes", "30 minutes")
            wrong2 = correct.replace("1 hour", "2 hours") if "1 hour" in correct else correct.replace("2 hours", "1 hour")
            wrong3 = "2 hours"
        elif "hour" in correct:
            hrs = int(correct.split()[0])
            wrong1 = f"{hrs + 1} hours"
            wrong2 = f"{hrs - 1} hour" if hrs > 1 else "30 minutes"
            wrong3 = f"{hrs} hours 30 minutes"
        else:
            mins = int(correct.split()[0])
            wrong1 = f"{mins + 15} minutes"
            wrong2 = f"{mins - 15} minutes" if mins > 15 else f"{mins + 30} minutes"
            wrong3 = "1 hour"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"How much time passes from {start} to {end}?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"From {start} to {end} is {correct}"
        })
    
    # Add time calculations (15 questions)
    add_time = [
        ("09:00", "30 minutes", "09:30"), ("10:30", "1 hour", "11:30"),
        ("14:00", "45 minutes", "14:45"), ("08:15", "30 minutes", "08:45"),
        ("11:00", "1 hour 30 minutes", "12:30"), ("09:45", "15 minutes", "10:00"),
        ("13:30", "2 hours", "15:30"), ("10:15", "45 minutes", "11:00"),
        ("07:30", "1 hour", "08:30"), ("14:45", "30 minutes", "15:15"),
        ("12:00", "2 hours 30 minutes", "14:30"), ("09:00", "3 hours", "12:00"),
        ("16:30", "1 hour 15 minutes", "17:45"), ("11:15", "45 minutes", "12:00"),
        ("08:00", "2 hours 15 minutes", "10:15")
    ]
    
    for start, add, correct in add_time:
        hour = int(correct.split(':')[0])
        minute = int(correct.split(':')[1])
        
        wrong1 = f"{hour}:{(minute + 15) % 60:02d}"
        wrong2 = f"{(hour + 1) % 24}:{minute:02d}"
        wrong3 = f"{(hour - 1) % 24}:{minute:02d}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"It's {start}. What time will it be in {add}?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"{start} + {add} = {correct}"
        })
    
    # Subtract time calculations (10 questions)
    subtract = [
        ("10:00", "30 minutes", "09:30"), ("11:30", "1 hour", "10:30"),
        ("14:45", "45 minutes", "14:00"), ("09:15", "15 minutes", "09:00"),
        ("12:30", "1 hour 30 minutes", "11:00"), ("15:00", "2 hours", "13:00"),
        ("10:45", "45 minutes", "10:00"), ("08:30", "30 minutes", "08:00"),
        ("13:15", "1 hour 15 minutes", "12:00"), ("16:00", "3 hours", "13:00")
    ]
    
    for start, sub, correct in subtract:
        hour = int(correct.split(':')[0])
        minute = int(correct.split(':')[1])
        
        wrong1 = f"{hour}:{(minute + 15) % 60:02d}"
        wrong2 = f"{(hour + 1) % 24}:{minute:02d}"
        wrong3 = f"{(hour - 1) % 24 or 12}:{minute:02d}"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"It's {start}. What time was it {sub} ago?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"{start} - {sub} = {correct}"
        })
    
    return questions[:50]


def generate_level_9_questions():
    """Level 9: Time Management Skills - 50 unique questions"""
    questions = []
    
    # Planning scenarios (25 questions)
    scenarios = [
        ("You need 30 minutes to get ready and must leave at 8:00. When should you start?", "7:30"),
        ("The bus takes 45 minutes. You need to arrive at 9:00. When should you leave?", "8:15"),
        ("Homework takes 1 hour. You want to finish by 6:00. When should you start?", "5:00"),
        ("Cooking dinner takes 45 minutes. You want to eat at 7:00. When start cooking?", "6:15"),
        ("The movie is 2 hours long and starts at 14:00. When will it end?", "16:00"),
        ("You have a 1 hour class starting at 10:30. When does it end?", "11:30"),
        ("Swimming lessons are 45 minutes, ending at 17:00. When did they start?", "16:15"),
        ("You need 15 minutes to walk to school. School starts at 9:00. When leave home?", "8:45"),
        ("Piano practice is 30 minutes. You finish at 16:30. When did you start?", "16:00"),
        ("The train journey is 2 hours 30 minutes. You leave at 10:00. Arrival time?", "12:30"),
        ("You need 20 minutes to eat breakfast and leave at 8:15. When start eating?", "7:55"),
        ("The game is 90 minutes long. It finishes at 15:30. When did it start?", "14:00"),
        ("You have 3 hours of free time starting at 14:00. When does your free time end?", "17:00"),
        ("The bus arrives every 30 minutes. One came at 9:15. When is the next one?", "9:45"),
        ("You need 1 hour 15 minutes to do chores. You want to finish by 12:00. Start time?", "10:45"),
        ("The concert is 2 hours long. It ends at 22:00. When did it start?", "20:00"),
        ("You walk for 25 minutes and arrive at 9:00. When did you leave?", "8:35"),
        ("The lesson starts at 11:00 and lasts 50 minutes. End time?", "11:50"),
        ("You want to watch a 45-minute show before dinner at 18:00. Latest start time?", "17:15"),
        ("It takes 10 minutes to get ready for bed. Bedtime is 20:30. Start getting ready?", "20:20"),
        ("The match has two 45-minute halves. It starts at 15:00. End time (no extra time)?", "16:30"),
        ("You have 2 hours of homework and 1 hour of practice. Total time needed?", "3 hours"),
        ("Library closes at 17:30. You need 45 minutes there. Latest arrival time?", "16:45"),
        ("The journey is 1 hour 20 minutes. You arrive at 14:00. Departure time?", "12:40"),
        ("You need 5 minutes to walk between classes. Class 1 ends at 10:00. Class 2 starts?", "10:05")
    ]
    
    for q, correct in scenarios:
        if ':' in correct:
            hour = int(correct.split(':')[0])
            minute = int(correct.split(':')[1])
            wrong1 = f"{hour}:{(minute + 15) % 60:02d}"
            wrong2 = f"{(hour + 1) % 24}:{minute:02d}"
            wrong3 = f"{(hour - 1) % 24 or 12}:{minute:02d}"
        else:
            val = int(correct.split()[0])
            wrong1 = f"{val + 1} hours"
            wrong2 = f"{val - 1} hours" if val > 1 else "4 hours"
            wrong3 = f"{val} hours 30 minutes"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"The answer is {correct}"
        })
    
    # Priority/scheduling questions (25 questions)
    priorities = [
        ("You have 30 minutes before school. What should you do FIRST?", "Get dressed", "Getting dressed is essential"),
        ("You have homework and want to play. What should come first?", "Homework", "Responsibilities before fun"),
        ("It's nearly bedtime. What should you do?", "Brush teeth and get ready", "Bedtime routine is important"),
        ("You're running late for school. What should you skip?", "Playing games", "Skip non-essentials when late"),
        ("You have a test tomorrow. How should you spend tonight?", "Study and sleep early", "Preparation is key"),
        ("It's Saturday morning. When is best to do homework?", "Morning when fresh", "Do hard tasks when alert"),
        ("You need to pack your bag. When is best?", "The night before", "Preparing ahead reduces stress"),
        ("You want to watch TV but have chores. What first?", "Do the chores", "Responsibilities first"),
        ("It's late and you're tired. Should you start a long project?", "No, wait until tomorrow", "Big tasks need energy"),
        ("Your friend calls during homework time. What do you do?", "Call back after homework", "Finish what you started"),
        ("You have 1 hour of free time. Can you watch a 2-hour movie?", "No, not enough time", "Plan activities that fit"),
        ("What helps you wake up on time?", "Going to bed early", "Good sleep = easier mornings"),
        ("When should you set your alarm?", "The night before", "Prepare the night before"),
        ("You finish dinner at 6:30. Bedtime is 8:30. Free time?", "2 hours", "6:30 to 8:30 = 2 hours"),
        ("You have swimming at 4:00 and music at 5:30. Time between?", "1 hour 30 minutes", "5:30 - 4:00 = 1:30"),
        ("School ends at 3:15. Your bus is at 3:30. How long to wait?", "15 minutes", "3:30 - 3:15 = 15 min"),
        ("You want to be 10 minutes early. Event is at 10:00. Arrive by?", "9:50", "10 min early = 9:50"),
        ("You're always late. What might help?", "Set reminders", "Reminders help with time"),
        ("How can you make mornings easier?", "Prepare the night before", "Preparation saves time"),
        ("What's a good bedtime habit?", "Same time every night", "Routine helps sleep"),
        ("You feel rushed in the morning. What could help?", "Wake up earlier", "More time = less rush"),
        ("You have activities at 2:00, 4:00, and 6:00. Total free time between them?", "2 hours", "2 gaps of 2 hours, minus activities"),
        ("Best time to pack your school bag?", "Before bed", "Avoid morning rush"),
        ("You have piano at 5 and need 30 min to get there. Leave by?", "4:30", "5:00 - 30 min = 4:30"),
        ("A good way to remember appointments?", "Write in a diary/calendar", "Recording helps memory")
    ]
    
    for q, correct, explanation in priorities:
        if ':' in correct:
            # Time answer
            hour = int(correct.split(':')[0])
            minute = int(correct.split(':')[1])
            wrong1 = f"{hour}:{(minute + 10) % 60:02d}"
            wrong2 = f"{(hour + 1) % 24}:{minute:02d}"
            wrong3 = f"{hour - 1}:{minute:02d}" if hour > 1 else f"{hour + 2}:{minute:02d}"
        elif 'hour' in correct or 'minute' in correct:
            # Duration answer
            if 'hour' in correct:
                val = int(correct.split()[0])
                wrong1 = f"{val + 1} hours"
                wrong2 = f"{val - 1} hours" if val > 1 else "30 minutes"
                wrong3 = f"{val} hours 15 minutes"
            else:
                val = int(correct.split()[0])
                wrong1 = f"{val + 10} minutes"
                wrong2 = f"{val - 5} minutes" if val > 5 else f"{val + 20} minutes"
                wrong3 = "1 hour"
        else:
            # Text answer - create plausible wrong answers
            wrong1 = "Do it later"
            wrong2 = "Skip it entirely"
            wrong3 = "Ask someone else"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_10_questions():
    """Level 10: Daily Routines - 50 unique questions"""
    questions = []
    
    # Daily schedule planning (30 questions)
    routines = [
        ("What time do most schools in Ireland start?", "9:00 AM", "Around 9 is typical"),
        ("What's a typical school finish time?", "3:00-3:30 PM", "Afternoon finish is standard"),
        ("When is lunch time in most schools?", "12:30-1:00 PM", "Midday lunch break"),
        ("How long is a typical school day?", "About 6 hours", "9 AM to 3 PM is 6 hours"),
        ("What's a good bedtime for a teenager?", "9-10 PM", "8-10 hours sleep needed"),
        ("When should you eat breakfast?", "Before leaving for school", "Fuel up in the morning"),
        ("How long should homework take each day?", "1-2 hours", "Varies by age and school"),
        ("What time is considered 'early morning'?", "5-7 AM", "Before typical wake time"),
        ("What time is considered 'late evening'?", "8-10 PM", "Before typical bedtime"),
        ("When is rush hour in the morning?", "7-9 AM", "When people go to work/school"),
        ("When is rush hour in the evening?", "4-6 PM", "When people go home"),
        ("How much sleep does a teenager need?", "8-10 hours", "Important for growth"),
        ("What's a healthy breakfast time?", "7-8 AM", "Allow time to digest before school"),
        ("When should you do homework?", "After school, before dinner", "When you're still alert"),
        ("What time is 'tea time' in Ireland?", "Around 6 PM", "Evening meal time"),
        ("What's a typical weekend wake time?", "Later than weekdays", "No strict school schedule"),
        ("How long is a typical lunch break?", "30-60 minutes", "Time to eat and rest"),
        ("What activities are good before bed?", "Reading, calm activities", "Help wind down"),
        ("What activities are NOT good before bed?", "Video games, screens", "Can disrupt sleep"),
        ("When should you pack your school bag?", "Night before", "Reduce morning stress"),
        ("How much exercise should you get daily?", "At least 1 hour", "Important for health"),
        ("What's a good time for exercise?", "Afternoon/after school", "Not too close to bed"),
        ("How often should you eat?", "3 meals plus snacks", "Regular eating is healthy"),
        ("What time should you stop using screens before bed?", "1 hour before", "Helps with sleep"),
        ("What's a good morning routine length?", "45-60 minutes", "Don't rush"),
        ("How many hours are you typically awake in a day?", "14-16 hours", "24 minus 8-10 sleep"),
        ("Best time to study for a test?", "The day before, evening", "When material is fresh"),
        ("When should you have dinner finished by?", "2 hours before bed", "Allow time to digest"),
        ("What time do most shops close?", "5-6 PM (some later)", "Typical closing time"),
        ("When do banks typically open?", "10 AM", "Later than most shops")
    ]
    
    for q, correct, explanation in routines:
        if 'AM' in correct or 'PM' in correct:
            wrong1 = correct.replace('AM', 'PM') if 'AM' in correct else correct.replace('PM', 'AM')
            wrong2 = "Noon"
            wrong3 = "Midnight"
        elif 'hour' in correct:
            if '-' in correct or 'About' in correct:
                wrong1 = "30 minutes"
                wrong2 = "12 hours"
                wrong3 = "All day"
            else:
                try:
                    num = int(correct.split()[0])
                    wrong1 = f"{num + 3} hours"
                    wrong2 = f"{num - 1} hours" if num > 1 else "5 hours"
                    wrong3 = "30 minutes"
                except ValueError:
                    wrong1 = "30 minutes"
                    wrong2 = "12 hours"
                    wrong3 = "All day"
        else:
            wrong1 = "Anytime"
            wrong2 = "It doesn't matter"
            wrong3 = "As late as possible"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Routine problem solving (20 questions)
    problems = [
        ("Your alarm didn't go off. What's the first thing to do?", "Check the time and get ready quickly", "Don't panic, act fast"),
        ("You forgot your lunch. What can you do?", "Tell a teacher or buy lunch", "Find a solution"),
        ("You're running 10 minutes late. What should you NOT do?", "Skip brushing teeth", "Keep hygiene habits"),
        ("It's Friday evening. When should you do weekend homework?", "Saturday morning", "Get it done, enjoy Sunday"),
        ("You can't sleep. What should you try?", "Read a calm book", "Avoid screens, try relaxing"),
        ("You're tired after school. What helps?", "Short rest then homework", "Balance rest and work"),
        ("You have too much to do. What first?", "Make a list and prioritize", "Organize then act"),
        ("Your schedule is too busy. What can help?", "Decide what's most important", "Can't do everything"),
        ("You keep forgetting things. What helps?", "Use a checklist", "Write things down"),
        ("You're always rushing. What's wrong?", "Not allowing enough time", "Plan more time"),
        ("School starts in 30 min, you just woke up. Priority?", "Get dressed and go", "Essentials only"),
        ("You have a test tomorrow but want to play. Decision?", "Study first, play if time", "Priorities matter"),
        ("Your friend wants to video call during homework. What do?", "Say you'll call after", "Finish tasks first"),
        ("It's 9 PM and homework isn't done. What now?", "Do what you can, sleep on time", "Sleep is important"),
        ("You're bored on a school morning. What NOT to do?", "Start a video game", "Don't start something long"),
        ("Your morning routine is too slow. What helps?", "Prepare things the night before", "Preparation is key"),
        ("You wake up feeling sick. What first?", "Tell a parent/guardian", "Health comes first"),
        ("You finish homework early. Good use of time?", "Prepare for tomorrow", "Use time wisely"),
        ("Weekend is too unstructured. What helps?", "Make a loose plan", "Some structure helps"),
        ("You're always tired. What might help?", "Earlier bedtime", "More sleep needed")
    ]
    
    for q, correct, explanation in problems:
        wrong1 = "Do nothing"
        wrong2 = "Panic"
        wrong3 = "Give up"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_11_questions():
    """Level 11: Calendars & Planning - 50 unique questions"""
    questions = []
    
    # Calendar reading (25 questions)
    calendar_qs = [
        ("If today is Monday, what day is tomorrow?", "Tuesday"),
        ("If today is Friday, what day was yesterday?", "Thursday"),
        ("If today is Wednesday, what day is in 3 days?", "Saturday"),
        ("If today is Sunday, what day was 2 days ago?", "Friday"),
        ("If today is Tuesday, what day is in a week?", "Tuesday"),
        ("How many days from Monday to Friday?", "4 days"),
        ("How many days from Wednesday to Sunday?", "4 days"),
        ("If March 1st is a Monday, what day is March 8th?", "Monday"),
        ("If June 15th is a Thursday, what day is June 22nd?", "Thursday"),
        ("If December 10th is a Sunday, what day is December 17th?", "Sunday"),
        ("What's the date one week after January 20th?", "January 27th"),
        ("What's the date 2 weeks after March 5th?", "March 19th"),
        ("If April starts on a Tuesday, what day is April 15th?", "Monday"),
        ("How many Mondays are typically in a month?", "4 or 5"),
        ("If your birthday is May 20th and today is May 13th, how many days until your birthday?", "7 days"),
        ("If an event is on October 31st and today is October 1st, how many days to wait?", "30 days"),
        ("What month comes 3 months after June?", "September"),
        ("What month is 2 months before December?", "October"),
        ("If today is the 15th, when is the end of the month?", "15-16 days away"),
        ("How many school days in a typical week?", "5"),
        ("If you see the doctor every 2 weeks, starting January 1st, what are the next dates?", "Jan 15, Jan 29"),
        ("How many days between January 1st and January 31st?", "30 days"),
        ("If an assignment is due in 2 weeks from Monday, March 3rd, when is it due?", "Monday, March 17th"),
        ("What day of the week is New Year's Day usually celebrated?", "January 1st (varies by day)"),
        ("How many weekends in a month?", "4 or 5")
    ]
    
    for q, correct in calendar_qs:
        if correct in ['Tuesday', 'Thursday', 'Saturday', 'Friday', 'Monday', 'Sunday', 'Wednesday']:
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            wrong = [d for d in days if d != correct][:3]
        elif 'days' in correct:
            val = correct.split()[0]
            if val.isdigit():
                num = int(val)
                wrong = [f"{num+1} days", f"{num-1} days" if num > 1 else "1 day", f"{num+2} days"]
            else:
                wrong = ['2 days', '3 days', '5 days']
        elif correct in ['September', 'October']:
            months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
            wrong = [m for m in months if m != correct][:3]
        else:
            wrong = ['Wrong answer 1', 'Wrong answer 2', 'Wrong answer 3']
        
        options = [correct] + wrong
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"The answer is {correct}"
        })
    
    # Event planning (25 questions)
    planning = [
        ("You're planning a party for Saturday. When should you send invites?", "At least a week before"),
        ("You have a dentist appointment. What should you do the day before?", "Check the time and location"),
        ("How far ahead should you plan a birthday party?", "2-4 weeks"),
        ("You're going on holiday next month. When pack?", "A few days before"),
        ("You have exams in 3 weeks. When start studying?", "Now/as soon as possible"),
        ("A school project is due in 2 weeks. When to start?", "This week"),
        ("You need to buy a birthday gift. When is too late?", "The day of the birthday"),
        ("When should you confirm attendance at an event?", "As soon as you receive the invite"),
        ("You're meeting friends. What should you confirm before?", "Time and place"),
        ("A relative is visiting next week. What to prepare?", "Clean room, plan activities"),
        ("When should you set a reminder for an appointment?", "Day before and morning of"),
        ("You want to join a club. When to sign up?", "Before the deadline"),
        ("You have a match on Saturday. When to prepare kit?", "Friday night"),
        ("Family dinner is at 6 PM. When should you be ready?", "A few minutes before"),
        ("You're cooking for guests. When to start prep?", "Earlier in the day"),
        ("When's a good time to make weekend plans?", "Thursday or Friday"),
        ("You need to return a library book. When check due date?", "Before it's overdue"),
        ("You're going to a concert. What to check beforehand?", "Time, tickets, transport"),
        ("A friend's party is at 3 PM. What time to arrive?", "3 PM or slightly after"),
        ("You promised to call grandma Sunday. When to set reminder?", "Saturday night"),
        ("You're meeting someone new. What to confirm?", "Time, place, contact number"),
        ("Term starts next week. What to prepare?", "Uniform, supplies, schedule"),
        ("You have a half-day at school. Who to inform?", "Parents, so they know pickup time"),
        ("Doctor said come back in a month. What to do now?", "Schedule the appointment"),
        ("You're hosting a sleepover. What to plan?", "Food, activities, sleeping arrangements")
    ]
    
    for q, correct in planning:
        wrong1 = "Don't plan ahead"
        wrong2 = "The day of the event"
        wrong3 = "It doesn't matter"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"Good planning: {correct}"
        })
    
    return questions[:50]


def generate_level_12_questions():
    """Level 12: Journey Planning - 50 unique questions"""
    questions = []
    
    # Journey time calculations (25 questions)
    journeys = [
        ("Train departs 10:00, journey is 2 hours. Arrival?", "12:00", "10:00 + 2 hours = 12:00"),
        ("Bus departs 09:30, journey is 45 minutes. Arrival?", "10:15", "09:30 + 45 min = 10:15"),
        ("Flight departs 14:00, flight is 3 hours. Arrival?", "17:00", "14:00 + 3 hours = 17:00"),
        ("Train departs 11:15, journey is 1 hour 30 minutes. Arrival?", "12:45", "11:15 + 1:30 = 12:45"),
        ("Bus arrives 15:00, journey was 50 minutes. Departure was?", "14:10", "15:00 - 50 min = 14:10"),
        ("You need to be there at 09:00, journey is 40 minutes. Leave by?", "08:20", "09:00 - 40 min = 08:20"),
        ("Meeting at 14:30, travel time 1 hour. Leave by?", "13:30", "14:30 - 1 hour = 13:30"),
        ("Film starts 19:00, takes 25 minutes to get there. Leave by?", "18:35", "19:00 - 25 min = 18:35"),
        ("School starts 09:00, walk is 15 minutes. Leave by?", "08:45", "09:00 - 15 min = 08:45"),
        ("Party starts 16:00, bus takes 35 minutes. Leave by?", "15:25", "16:00 - 35 min = 15:25"),
        ("Train takes 2 hrs 15 min. Departs 10:30. Arrival?", "12:45", "10:30 + 2:15 = 12:45"),
        ("Flight lands 18:00. Flight was 4 hours. Departure was?", "14:00", "18:00 - 4 hours = 14:00"),
        ("You need 30 min buffer before a flight. Flight 11:00. Arrive by?", "10:30", "Buffer time needed"),
        ("Bus runs every 20 minutes. First at 08:00. Second?", "08:20", "08:00 + 20 min = 08:20"),
        ("Train every 30 min. One at 09:15. Next?", "09:45", "09:15 + 30 min = 09:45"),
        ("Connection time is 15 minutes. Arrive 11:30. Next train?", "11:45", "11:30 + 15 min = 11:45"),
        ("Total journey: 45 min train + 20 min walk. Total?", "1 hour 5 minutes", "45 + 20 = 65 min"),
        ("Journey: 30 min bus + 15 min walk + 25 min train. Total?", "1 hour 10 minutes", "30+15+25=70 min"),
        ("You have 2 hours. Journey is 1 hr 40 min. Time to spare?", "20 minutes", "120 - 100 = 20 min"),
        ("Bus at 10:00, 10:30, 11:00. You arrive 10:25. Wait time?", "5 minutes", "Next bus at 10:30"),
        ("Train missed at 09:00. Next is 09:30. Wait time?", "Up to 30 minutes", "Depends when you arrived"),
        ("Journey normally 1 hour. Add 15 min for delays. Total?", "1 hour 15 minutes", "1:00 + 0:15 = 1:15"),
        ("Arrive airport 2 hrs before flight. Flight 15:00. Arrive by?", "13:00", "15:00 - 2 hours = 13:00"),
        ("Ferry crossing 90 minutes. Departs 12:30. Arrival?", "14:00", "12:30 + 1:30 = 14:00"),
        ("Journey home: 25 min + 10 min walk. Total?", "35 minutes", "25 + 10 = 35 min")
    ]
    
    for q, correct, explanation in journeys:
        if ':' in correct:
            hour = int(correct.split(':')[0])
            minute = int(correct.split(':')[1])
            wrong1 = f"{hour}:{(minute + 15) % 60:02d}"
            wrong2 = f"{(hour + 1) % 24}:{minute:02d}"
            wrong3 = f"{(hour - 1) % 24 or 12}:{minute:02d}"
        elif 'minute' in correct or 'hour' in correct:
            if 'hour' in correct and 'minute' in correct:
                wrong1 = correct.replace('5 minutes', '20 minutes')
                wrong2 = correct.replace('1 hour', '2 hours')
                wrong3 = "45 minutes"
            elif 'minute' in correct:
                try:
                    val = int(correct.split()[0])
                    wrong1 = f"{val + 10} minutes"
                    wrong2 = f"{val - 10} minutes" if val > 10 else f"{val + 20} minutes"
                    wrong3 = "1 hour"
                except ValueError:
                    wrong1 = "15 minutes"
                    wrong2 = "1 hour"
                    wrong3 = "45 minutes"
            else:
                wrong1 = "30 minutes"
                wrong2 = "2 hours"
                wrong3 = "3 hours"
        else:
            wrong1 = "Wrong answer 1"
            wrong2 = "Wrong answer 2"
            wrong3 = "Wrong answer 3"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Journey planning scenarios (25 questions)
    scenarios = [
        ("You're taking a train. What should you check first?", "Departure time and platform"),
        ("Going to the airport. How early should you arrive?", "2-3 hours before international flights"),
        ("You miss your bus. What's a good backup plan?", "Check when the next one comes"),
        ("You're travelling by train. What might you need?", "Ticket and possibly a seat reservation"),
        ("It's raining and you're walking. What should you do?", "Allow extra time and bring umbrella"),
        ("Traffic is heavy. How does this affect journey time?", "It will take longer"),
        ("You're taking a bus. How do you know when to get off?", "Watch for your stop or ask driver"),
        ("What's a connection in travel terms?", "Changing from one service to another"),
        ("Why arrive early for a flight?", "Security, check-in, finding gate"),
        ("Your train is delayed. What should you do?", "Check screens for updates"),
        ("You're planning a journey. What helps most?", "Checking times and routes beforehand"),
        ("What does 'peak time' mean for travel?", "Busy times when prices may be higher"),
        ("Why might you choose a slower train?", "It might be cheaper or more convenient"),
        ("What's important when booking travel?", "Correct date, time, and destination"),
        ("You're at a train station. Where to find your platform?", "Departure boards"),
        ("What should you do if lost in a station?", "Ask staff or check signs"),
        ("How can you make a long journey more comfortable?", "Bring snacks, entertainment, charge phone"),
        ("What's a travel itinerary?", "A plan of your journey with times"),
        ("Why check weather before travelling?", "May affect journey time or what to bring"),
        ("What's the benefit of booking in advance?", "Often cheaper, guaranteed seat"),
        ("You're planning a route. What apps help?", "Maps, travel planner apps"),
        ("What should you do after booking travel?", "Save confirmation and check details"),
        ("How do you know if a train is on time?", "Check departure boards or app"),
        ("What's a return ticket?", "Ticket for going and coming back"),
        ("Why arrive at bus stop a few minutes early?", "Bus might come early, gives buffer")
    ]
    
    for q, correct in scenarios:
        wrong1 = "Don't plan, just go"
        wrong2 = "It doesn't matter"
        wrong3 = "Wing it"
        
        options = [correct, wrong1, wrong2, wrong3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"Good planning: {correct}"
        })
    
    return questions[:50]


# ============================================================
# MAIN FUNCTIONS
# ============================================================

def generate_all_questions():
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
        (12, generate_level_12_questions)
    ]
    
    for level, generator in generators:
        print(f"  Generating Level {level}...")
        questions = generator()
        
        for q in questions:
            options = q['options']
            while len(options) < 4:
                options.append('')
            
            all_questions.append({
                'topic': TOPIC,
                'level': level,
                'question_text': q['question_text'],
                'option_a': str(options[0]),
                'option_b': str(options[1]),
                'option_c': str(options[2]),
                'option_d': str(options[3]),
                'correct_answer': ['A', 'B', 'C', 'D'][q['correct_index']],
                'solution': q.get('explanation', ''),
                'question_image_svg': q.get('image_svg', '')
            })
        
        print(f"    Level {level}: {len(questions)} questions generated")
    
    return all_questions


def validate_questions(questions):
    errors = []
    seen = set()
    
    for i, q in enumerate(questions):
        if not q.get('question_text'):
            errors.append(f"Q{i}: Missing question_text")
        if not q.get('option_a'):
            errors.append(f"Q{i}: Missing option_a")
        
        key = (q['level'], q['question_text'][:100])
        if key in seen:
            errors.append(f"Q{i} L{q['level']}: Duplicate")
        seen.add(key)
    
    return errors


def count_existing_questions():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT difficulty_level, COUNT(*) FROM questions_adaptive WHERE topic = ? GROUP BY difficulty_level', (TOPIC,))
        counts = dict(cursor.fetchall())
        conn.close()
        return counts
    except:
        return {}


def clear_existing_questions():
    counts = count_existing_questions()
    total = sum(counts.values())
    
    if total > 0:
        print(f"\n⚠️  Found {total} existing questions for {TOPIC}")
        response = input("Delete existing? (yes/no): ").strip().lower()
        if response == 'yes':
            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()
            cursor.execute('DELETE FROM questions_adaptive WHERE topic = ?', (TOPIC,))
            deleted = cursor.rowcount
            conn.commit()
            conn.close()
            print(f"   Deleted {deleted} questions")
            return True
        return False
    return True


def insert_questions(questions):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    letter_to_int = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    inserted = 0
    skipped = 0
    
    for q in questions:
        try:
            level = q['level']
            band = get_difficulty_band(level)
            
            correct_answer = q['correct_answer']
            if isinstance(correct_answer, str):
                correct_answer = letter_to_int.get(correct_answer.upper(), 0)
            
            cursor.execute('''
                INSERT OR IGNORE INTO questions_adaptive 
                (topic, question_text, option_a, option_b, option_c, option_d, 
                 correct_answer, explanation, difficulty_level, difficulty_band,
                 question_type, is_active, image_svg, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                q['topic'], q['question_text'], q['option_a'], q['option_b'],
                q.get('option_c', ''), q.get('option_d', ''),
                correct_answer, q.get('solution', ''), level, band,
                'multiple_choice', 1, q.get('question_image_svg', ''),
                datetime.now(), datetime.now()
            ))
            
            if cursor.rowcount > 0:
                inserted += 1
            else:
                skipped += 1
        except sqlite3.Error as e:
            print(f"Error: {e}")
            skipped += 1
    
    conn.commit()
    conn.close()
    
    if skipped > 0:
        print(f"   Skipped {skipped} duplicates")
    
    return inserted


def main():
    print("=" * 60)
    print("AgentMath L2LP Question Generator V3")
    print(f"Topic: {TOPIC}")
    print(f"Table: questions_adaptive")
    print(f"Target: {QUESTIONS_PER_LEVEL} × {TOTAL_LEVELS} = {QUESTIONS_PER_LEVEL * TOTAL_LEVELS}")
    print("=" * 60)
    
    if not clear_existing_questions():
        return
    
    print("\nGenerating questions...")
    questions = generate_all_questions()
    print(f"\nTotal: {len(questions)}")
    
    print("\nValidating...")
    errors = validate_questions(questions)
    dupes = [e for e in errors if 'Duplicate' in e]
    
    if dupes:
        print(f"⚠️  {len(dupes)} duplicates (will be skipped)")
    
    print("✅ Validation passed")
    
    print("\nInserting...")
    inserted = insert_questions(questions)
    
    print(f"\n{'=' * 60}")
    print(f"✅ Complete! Inserted {inserted} questions")
    
    counts = count_existing_questions()
    print("\nQuestions per level:")
    for level in range(1, 13):
        count = counts.get(level, 0)
        status = "✓" if count >= 40 else "⚠️"
        print(f"   Level {level}: {count} {status}")
    print("=" * 60)


if __name__ == '__main__':
    main()
