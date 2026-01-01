"""
AgentMath L1LP Question Generator
Topic: Time
Learning Outcomes: 2.26 - 2.29
Version: 2.0 - Updated for actual database schema
"""

import sqlite3
import random
import math

TOPIC = 'time'
MODE = 'l1lp'
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12
DATABASE_PATH = 'instance/mathquiz.db'

DIFFICULTY_BANDS = {
    1: 'Foundation', 2: 'Foundation', 3: 'Foundation', 4: 'Foundation',
    5: 'Developing', 6: 'Developing', 7: 'Developing', 8: 'Developing',
    9: 'Progressing', 10: 'Progressing', 11: 'Consolidating', 12: 'Consolidating'
}

COLOURS = {'red': '#E74C3C', 'blue': '#3498DB', 'green': '#27AE60', 'yellow': '#F1C40F', 'orange': '#E67E22', 'purple': '#9B59B6'}
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
SEASONS = ['Spring', 'Summer', 'Autumn', 'Winter']

def create_svg_wrapper(content, width=400, height=180):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background: white;">{content}</svg>'

def svg_sun(x, y, size=60):
    cx, cy = x + size//2, y + size//2
    rays = ''
    for i in range(8):
        angle = i * 45 * math.pi / 180
        x1, y1 = cx + (size//3) * math.cos(angle), cy + (size//3) * math.sin(angle)
        x2, y2 = cx + (size//2) * math.cos(angle), cy + (size//2) * math.sin(angle)
        rays += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#F1C40F" stroke-width="3"/>'
    return f'{rays}<circle cx="{cx}" cy="{cy}" r="{size//3}" fill="#F1C40F"/>'

def svg_moon(x, y, size=60):
    cx, cy = x + size//2, y + size//2
    return f'<circle cx="{cx}" cy="{cy}" r="{size//3}" fill="#F4D03F"/><circle cx="{cx + size//6}" cy="{cy - size//8}" r="{size//4}" fill="white"/>'

def svg_clock(x, y, size=80, hour=12, minute=0):
    cx, cy = x + size//2, y + size//2
    r = size//2 - 5
    face = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="white" stroke="#333" stroke-width="3"/>'
    markers = ''
    for i in range(12):
        angle = (i * 30 - 90) * math.pi / 180
        x1, y1 = cx + (r - 8) * math.cos(angle), cy + (r - 8) * math.sin(angle)
        x2, y2 = cx + (r - 3) * math.cos(angle), cy + (r - 3) * math.sin(angle)
        markers += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#333" stroke-width="2"/>'
    nums = ''
    for n, dx, dy in [(12, 0, -r + 15), (3, r - 15, 5), (6, 0, r - 10), (9, -r + 15, 5)]:
        nums += f'<text x="{cx + dx}" y="{cy + dy}" text-anchor="middle" font-size="12" font-weight="bold">{n}</text>'
    h_angle = ((hour % 12) * 30 + minute * 0.5 - 90) * math.pi / 180
    hx, hy = cx + r * 0.5 * math.cos(h_angle), cy + r * 0.5 * math.sin(h_angle)
    h_hand = f'<line x1="{cx}" y1="{cy}" x2="{hx}" y2="{hy}" stroke="#333" stroke-width="4" stroke-linecap="round"/>'
    m_angle = (minute * 6 - 90) * math.pi / 180
    mx, my = cx + r * 0.7 * math.cos(m_angle), cy + r * 0.7 * math.sin(m_angle)
    m_hand = f'<line x1="{cx}" y1="{cy}" x2="{mx}" y2="{my}" stroke="#E74C3C" stroke-width="3" stroke-linecap="round"/>'
    center = f'<circle cx="{cx}" cy="{cy}" r="4" fill="#333"/>'
    return face + markers + nums + h_hand + m_hand + center

def svg_morning_scene():
    svg = f'<rect x="0" y="0" width="400" height="120" fill="#87CEEB"/>'
    svg += svg_sun(300, 20, 50)
    svg += f'<rect x="0" y="120" width="400" height="60" fill="#90EE90"/>'
    svg += f'<rect x="50" y="70" width="80" height="50" fill="#DEB887"/>'
    svg += f'<polygon points="50,70 90,40 130,70" fill="#8B4513"/>'
    svg += f'<text x="250" y="100" text-anchor="middle" font-size="12">Good morning!</text>'
    return create_svg_wrapper(svg)

def svg_night_scene():
    svg = f'<rect x="0" y="0" width="400" height="120" fill="#1a1a2e"/>'
    svg += svg_moon(300, 15, 40)
    for i in range(5):
        sx, sy = random.randint(50, 250), random.randint(20, 80)
        svg += f'<text x="{sx}" y="{sy}" font-size="10" fill="#F4D03F">★</text>'
    svg += f'<rect x="0" y="120" width="400" height="60" fill="#2d4a3e"/>'
    svg += f'<rect x="50" y="70" width="80" height="50" fill="#4a4a4a"/>'
    svg += f'<polygon points="50,70 90,40 130,70" fill="#333"/>'
    svg += f'<rect x="70" y="85" width="20" height="20" fill="#F1C40F"/>'
    svg += f'<text x="250" y="100" text-anchor="middle" font-size="12" fill="white">Good night!</text>'
    return create_svg_wrapper(svg)

def svg_season_scene(season):
    svg = ''
    if season == 'Spring':
        svg = f'<rect x="0" y="0" width="400" height="120" fill="#87CEEB"/><rect x="0" y="120" width="400" height="60" fill="#90EE90"/>'
        for i in range(5):
            x = 50 + i * 70
            svg += f'<circle cx="{x}" cy="140" r="10" fill="#FF69B4"/><circle cx="{x}" cy="140" r="4" fill="#F1C40F"/><rect x="{x-2}" y="150" width="4" height="15" fill="#27AE60"/>'
        svg += f'<text x="200" y="30" text-anchor="middle" font-size="16">🌸 Spring 🌷</text>'
    elif season == 'Summer':
        svg = f'<rect x="0" y="0" width="400" height="100" fill="#87CEEB"/>'
        svg += svg_sun(320, 10, 50)
        svg += f'<rect x="0" y="100" width="400" height="80" fill="#F4D03F"/><rect x="0" y="140" width="400" height="40" fill="#3498DB"/>'
        svg += f'<text x="200" y="30" text-anchor="middle" font-size="16">☀️ Summer 🏖️</text>'
    elif season == 'Autumn':
        svg = f'<rect x="0" y="0" width="400" height="120" fill="#B0C4DE"/><rect x="0" y="120" width="400" height="60" fill="#8B7355"/>'
        cols = ['#E74C3C', '#E67E22', '#F1C40F', '#D35400']
        for i in range(8):
            x, y = random.randint(30, 370), random.randint(40, 100)
            svg += f'<ellipse cx="{x}" cy="{y}" rx="8" ry="5" fill="{random.choice(cols)}"/>'
        svg += f'<rect x="180" y="80" width="20" height="50" fill="#8B4513"/><circle cx="190" cy="60" r="30" fill="#D35400"/>'
        svg += f'<text x="200" y="30" text-anchor="middle" font-size="16">🍂 Autumn 🍁</text>'
    else:
        svg = f'<rect x="0" y="0" width="400" height="120" fill="#B0C4DE"/><rect x="0" y="120" width="400" height="60" fill="white"/>'
        for i in range(10):
            x, y = random.randint(30, 370), random.randint(30, 110)
            svg += f'<text x="{x}" y="{y}" font-size="12" fill="#ADD8E6">❄</text>'
        svg += f'<circle cx="200" cy="140" r="20" fill="white" stroke="#333"/><circle cx="200" cy="110" r="15" fill="white" stroke="#333"/><circle cx="200" cy="85" r="10" fill="white" stroke="#333"/>'
        svg += f'<text x="200" y="30" text-anchor="middle" font-size="16">❄️ Winter ⛄</text>'
    return create_svg_wrapper(svg)

def svg_timetable(activities):
    svg = f'<text x="200" y="25" text-anchor="middle" font-size="14" font-weight="bold">Today\'s Schedule</text>'
    cols = [COLOURS['blue'], COLOURS['green'], COLOURS['orange'], COLOURS['purple']]
    for i, (time, activity) in enumerate(activities):
        y = 45 + i * 35
        svg += f'<rect x="30" y="{y}" width="340" height="30" fill="{cols[i % len(cols)]}" opacity="0.3" rx="5"/>'
        svg += f'<text x="50" y="{y + 20}" font-size="12">{time}</text>'
        svg += f'<text x="130" y="{y + 20}" font-size="12">{activity}</text>'
    return create_svg_wrapper(svg)

# Track question numbers for uniqueness
_question_counter = {}

def make_question(question_text, options, correct_answer, explanation, svg, level):
    global _question_counter
    # Make question_text unique by adding counter
    key = (level, question_text)
    if key not in _question_counter:
        _question_counter[key] = 0
    _question_counter[key] += 1
    
    # Only add number if there are duplicates
    if _question_counter[key] > 1:
        question_text = f"{question_text} (#{_question_counter[key]})"
    
    while len(options) < 4:
        options.append("")
    options = options[:4]
    try:
        correct_index = options.index(correct_answer)
    except ValueError:
        options[0] = correct_answer
        correct_index = 0
    return {'question_text': question_text, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_answer': correct_index,
            'explanation': explanation, 'image_svg': svg, 'difficulty_band': DIFFICULTY_BANDS[level],
            'question_type': 'visual' if svg else 'text'}

def generate_level_1_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        if i % 2 == 0:
            svg, correct = svg_morning_scene(), 'Morning'
        else:
            svg, correct = svg_night_scene(), 'Night'
        options = ['Morning', 'Night', '', '']
        random.shuffle(options[:2])
        questions.append(make_question('Is this morning or night?', options, correct, f'This is {correct.lower()}!', svg, 1))
    return questions

def generate_level_2_questions():
    questions = []
    times = [('morning', '☀️ Sun rising, breakfast time'), ('afternoon', '🌤️ Sun high, lunchtime'),
             ('evening', '🌅 Sun setting, dinner time'), ('night', '🌙 Moon and stars, bedtime')]
    for i in range(QUESTIONS_PER_LEVEL):
        time_name, desc = random.choice(times)
        svg_c = f'<text x="200" y="80" text-anchor="middle" font-size="24">{desc.split()[0]}</text>'
        svg_c += f'<text x="200" y="110" text-anchor="middle" font-size="14" fill="#666">{" ".join(desc.split()[1:])}</text>'
        svg = create_svg_wrapper(svg_c)
        opts = ['Morning', 'Afternoon', 'Evening'] if i % 2 == 0 else ['Morning', 'Night', 'Evening']
        if time_name.title() not in opts:
            opts[0] = time_name.title()
        opts.append('')
        random.shuffle(opts[:3])
        questions.append(make_question('What time of day is this?', opts, time_name.title(), f'This is {time_name}!', svg, 2))
    return questions

def generate_level_3_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        day_idx = i % 7
        day = DAYS[day_idx]
        if i % 3 == 0:
            svg_c = f'<rect x="100" y="50" width="200" height="80" fill="#3498DB" rx="10"/><text x="200" y="100" text-anchor="middle" font-size="24" fill="white" font-weight="bold">{day}</text>'
            svg = create_svg_wrapper(svg_c)
            question, correct = 'What day is shown?', day
            wrong = [d for d in DAYS if d != day]
            options = [day] + random.sample(wrong, 2) + ['']
        elif i % 3 == 1:
            next_day = DAYS[(day_idx + 1) % 7]
            svg_c = f'<text x="200" y="70" text-anchor="middle" font-size="18">Today is {day}</text><text x="200" y="110" text-anchor="middle" font-size="16" fill="#666">Tomorrow is...?</text>'
            svg = create_svg_wrapper(svg_c)
            question, correct = f'What day comes AFTER {day}?', next_day
            wrong = [d for d in DAYS if d != next_day]
            options = [next_day] + random.sample(wrong, 2) + ['']
        else:
            prev_day = DAYS[(day_idx - 1) % 7]
            svg_c = f'<text x="200" y="70" text-anchor="middle" font-size="18">Today is {day}</text><text x="200" y="110" text-anchor="middle" font-size="16" fill="#666">Yesterday was...?</text>'
            svg = create_svg_wrapper(svg_c)
            question, correct = f'What day comes BEFORE {day}?', prev_day
            wrong = [d for d in DAYS if d != prev_day]
            options = [prev_day] + random.sample(wrong, 2) + ['']
        random.shuffle(options[:3])
        questions.append(make_question(question, options, correct, f'{correct} is correct!', svg, 3))
    return questions

def generate_level_4_questions():
    questions = []
    routines = [('wake up', 'morning', '🌅'), ('eat breakfast', 'morning', '🥣'), ('go to school', 'morning', '🏫'),
                ('eat lunch', 'afternoon', '🍽️'), ('play outside', 'afternoon', '⚽'), ('eat dinner', 'evening', '🍝'),
                ('brush teeth', 'evening', '🪥'), ('go to bed', 'night', '🛏️')]
    for i in range(QUESTIONS_PER_LEVEL):
        activity, time, emoji = random.choice(routines)
        svg_c = f'<text x="200" y="70" text-anchor="middle" font-size="40">{emoji}</text><text x="200" y="120" text-anchor="middle" font-size="18">{activity.title()}</text>'
        svg = create_svg_wrapper(svg_c)
        options = ['Morning', 'Afternoon', 'Night', ''] if time != 'evening' else ['Morning', 'Evening', 'Night', '']
        correct = time.title()
        random.shuffle(options[:3])
        questions.append(make_question(f'When do you usually {activity}?', options, correct, f'We usually {activity} in the {time}!', svg, 4))
    return questions

def generate_level_5_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        season = SEASONS[i % 4]
        svg = svg_season_scene(season)
        options = SEASONS.copy()
        random.shuffle(options)
        questions.append(make_question('What season is shown?', options, season, f'This is {season}!', svg, 5))
    return questions

def generate_level_6_questions():
    questions = []
    events = [('Christmas', 'Winter', 'December'), ('Easter', 'Spring', 'March or April'), ('Halloween', 'Autumn', 'October'),
              ('Summer holidays', 'Summer', 'July and August'), ("St Patrick's Day", 'Spring', 'March')]
    for i in range(QUESTIONS_PER_LEVEL):
        event, season, month = random.choice(events)
        emojis = {'Christmas': '🎄', 'Easter': '🐰', 'Halloween': '🎃', 'Summer holidays': '🏖️', "St Patrick's Day": '☘️'}
        svg_c = f'<text x="200" y="70" text-anchor="middle" font-size="40">{emojis.get(event, "📅")}</text><text x="200" y="110" text-anchor="middle" font-size="18">{event}</text>'
        svg = create_svg_wrapper(svg_c)
        if i % 2 == 0:
            question, correct = f'What season is {event} in?', season
            options = SEASONS.copy()
        else:
            question, correct = f'When is {event}?', month
            months = ['January', 'March', 'July and August', 'October', 'December', 'March or April']
            options = [month] + random.sample([m for m in months if m != month], 3)
        random.shuffle(options)
        questions.append(make_question(question, options, correct, f'{event} is in {season} ({month})!', svg, 6))
    return questions

def generate_level_7_questions():
    questions = []
    for i in range(QUESTIONS_PER_LEVEL):
        hour = random.randint(1, 12)
        svg_c = svg_clock(160, 40, 80, hour, 0)
        svg = create_svg_wrapper(svg_c)
        correct = f"{hour} o'clock"
        wrong = [f"{h} o'clock" for h in random.sample([h for h in range(1, 13) if h != hour], 3)]
        options = [correct] + wrong
        random.shuffle(options)
        questions.append(make_question('What time does the clock show?', options, correct, f'The clock shows {hour} o\'clock!', svg, 7))
    return questions

def generate_level_8_questions():
    questions = []
    seqs = [('breakfast', 'lunch'), ('lunch', 'dinner'), ('morning', 'afternoon'), ('afternoon', 'evening'),
            ('evening', 'night'), ('Monday', 'Tuesday'), ('Friday', 'Saturday'), ('Spring', 'Summer')]
    for i in range(QUESTIONS_PER_LEVEL):
        first, second = random.choice(seqs)
        svg_c = f'<text x="100" y="80" text-anchor="middle" font-size="16" fill="#3498DB">{first.title()}</text>'
        svg_c += f'<text x="200" y="80" text-anchor="middle" font-size="24">→</text>'
        svg_c += f'<text x="300" y="80" text-anchor="middle" font-size="16" fill="#E74C3C">{second.title()}</text>'
        svg = create_svg_wrapper(svg_c)
        if i % 2 == 0:
            question, correct = f'What comes BEFORE {second}?', first.title()
            if first in [d.lower() for d in DAYS]: options = DAYS[:4]
            elif first in [s.lower() for s in SEASONS]: options = SEASONS
            else: options = [first.title(), second.title(), 'Night', 'Morning']
        else:
            question, correct = f'What comes AFTER {first}?', second.title()
            if second in [d.lower() for d in DAYS]: options = DAYS[:4]
            elif second in [s.lower() for s in SEASONS]: options = SEASONS
            else: options = [first.title(), second.title(), 'Night', 'Evening']
        if correct not in options: options[0] = correct
        random.shuffle(options)
        questions.append(make_question(question, options, correct, f'{correct} is the answer!', svg, 8))
    return questions

def generate_level_9_questions():
    questions = []
    scenarios = [('brushing teeth', 2, 'minutes'), ('washing hands', 20, 'seconds'), ('waiting for toast', 3, 'minutes'),
                 ('baking cookies', 15, 'minutes'), ('boiling an egg', 5, 'minutes')]
    for i in range(QUESTIONS_PER_LEVEL):
        activity, duration, unit = random.choice(scenarios)
        if i % 3 == 0:
            short, long = ('washing hands', 20, 'seconds'), ('baking cookies', 15, 'minutes')
            svg_c = f'<text x="100" y="70" text-anchor="middle" font-size="14">A: {short[0]}</text><text x="100" y="90" text-anchor="middle" font-size="12" fill="#666">({short[1]} {short[2]})</text>'
            svg_c += f'<text x="300" y="70" text-anchor="middle" font-size="14">B: {long[0]}</text><text x="300" y="90" text-anchor="middle" font-size="12" fill="#666">({long[1]} {long[2]})</text>'
            svg = create_svg_wrapper(svg_c)
            question, correct = 'Which takes LONGER?', 'B'
            options = ['A', 'B', 'Same time', 'Cannot tell']
        elif i % 3 == 1:
            correct = 'Short time' if (duration <= 30 and unit == 'seconds') or (duration <= 5 and unit == 'minutes') else 'Long time'
            svg_c = f'<text x="200" y="70" text-anchor="middle" font-size="16">{activity.title()}</text><text x="200" y="100" text-anchor="middle" font-size="20" fill="#3498DB">{duration} {unit}</text>'
            svg = create_svg_wrapper(svg_c)
            question = f'Is {duration} {unit} a long or short time?'
            options = ['Short time', 'Long time', 'Medium time', 'Very long time']
        else:
            seconds = random.choice([10, 20, 30, 45, 60])
            svg_c = f'<circle cx="200" cy="80" r="40" fill="#ecf0f1" stroke="#bdc3c7" stroke-width="3"/><text x="200" y="85" text-anchor="middle" font-size="20" font-weight="bold">{seconds}</text>'
            svg = create_svg_wrapper(svg_c)
            question, correct = 'How many seconds are left on the timer?', str(seconds)
            options = list(set([str(seconds), str(seconds + 10), str(seconds - 10) if seconds > 10 else '5', '60']))[:4]
        random.shuffle(options)
        questions.append(make_question(question, options, correct, f'{correct} is the answer!', svg, 9))
    return questions

def generate_level_10_questions():
    questions = []
    scenarios = [
        {'situation': 'Queue at the shop', 'people': ['Amy', 'Ben', 'Cat', 'Dan'], 'question': 'Who is FIRST in the queue?', 'answer_idx': 0},
        {'situation': 'Taking turns on the swing', 'people': ['Ella', 'Finn', 'Grace', 'Harry'], 'question': 'Who is LAST to get a turn?', 'answer_idx': 3},
        {'situation': 'Waiting for the bus', 'people': ['Ivy', 'Jack', 'Kate', 'Leo'], 'question': 'Who is SECOND in line?', 'answer_idx': 1}
    ]
    for i in range(QUESTIONS_PER_LEVEL):
        scenario = scenarios[i % len(scenarios)]
        svg_c = f'<text x="200" y="30" text-anchor="middle" font-size="14" font-weight="bold">{scenario["situation"]}</text>'
        cols = list(COLOURS.values())
        for j, person in enumerate(scenario['people']):
            x = 60 + j * 90
            svg_c += f'<circle cx="{x}" cy="80" r="20" fill="{cols[j]}"/><text x="{x}" y="120" text-anchor="middle" font-size="12">{person}</text><text x="{x}" y="140" text-anchor="middle" font-size="10" fill="#666">{j + 1}</text>'
        svg = create_svg_wrapper(svg_c)
        correct = scenario['people'][scenario['answer_idx']]
        options = scenario['people'].copy()
        random.shuffle(options)
        questions.append(make_question(scenario['question'], options, correct, f'{correct} is the answer!', svg, 10))
    return questions

def generate_level_11_questions():
    questions = []
    schedules = [
        [('9:00', 'Circle Time'), ('10:00', 'Maths'), ('11:00', 'Break'), ('12:00', 'Lunch')],
        [('9:00', 'Assembly'), ('10:00', 'Reading'), ('11:00', 'Art'), ('12:00', 'Lunch')]
    ]
    for i in range(QUESTIONS_PER_LEVEL):
        schedule = random.choice(schedules)
        svg = svg_timetable(schedule)
        if i % 3 == 0:
            time_slot = random.choice(schedule)
            question, correct = f'What happens at {time_slot[0]}?', time_slot[1]
            options = [s[1] for s in schedule]
        elif i % 3 == 1:
            time_slot = random.choice(schedule)
            question, correct = f'What time is {time_slot[1]}?', time_slot[0]
            options = [s[0] for s in schedule]
        else:
            idx = random.randint(0, len(schedule) - 2)
            question, correct = f'What comes AFTER {schedule[idx][1]}?', schedule[idx + 1][1]
            options = [s[1] for s in schedule]
        random.shuffle(options)
        questions.append(make_question(question, options, correct, f'{correct} is correct!', svg, 11))
    return questions

def generate_level_12_questions():
    questions = []
    types = ['clock', 'day', 'season', 'routine', 'sequence', 'timetable']
    for i in range(QUESTIONS_PER_LEVEL):
        t = types[i % len(types)]
        if t == 'clock':
            hour = random.randint(1, 12)
            svg_c = svg_clock(160, 40, 80, hour, 0)
            svg = create_svg_wrapper(svg_c)
            correct = f"{hour} o'clock"
            wrong = [f"{h} o'clock" for h in random.sample([h for h in range(1, 13) if h != hour], 3)]
            options = [correct] + wrong
            random.shuffle(options)
            questions.append(make_question('What time is it?', options, correct, f'It\'s {hour} o\'clock!', svg, 12))
        elif t == 'day':
            day_idx = random.randint(0, 6)
            day, next_day = DAYS[day_idx], DAYS[(day_idx + 1) % 7]
            svg_c = f'<text x="200" y="90" text-anchor="middle" font-size="20">Today is {day}</text>'
            svg = create_svg_wrapper(svg_c)
            options = random.sample(DAYS, 4)
            if next_day not in options: options[0] = next_day
            random.shuffle(options)
            questions.append(make_question('What day is TOMORROW?', options, next_day, f'After {day} comes {next_day}!', svg, 12))
        elif t == 'season':
            season = random.choice(SEASONS)
            svg = svg_season_scene(season)
            options = SEASONS.copy()
            random.shuffle(options)
            questions.append(make_question('What season is this?', options, season, f'This is {season}!', svg, 12))
        elif t == 'routine':
            activities = [('wake up', 'Morning'), ('eat lunch', 'Afternoon'), ('eat dinner', 'Evening'), ('go to bed', 'Night')]
            activity, time = random.choice(activities)
            svg_c = f'<text x="200" y="90" text-anchor="middle" font-size="18">When do you {activity}?</text>'
            svg = create_svg_wrapper(svg_c)
            options = ['Morning', 'Afternoon', 'Evening', 'Night']
            random.shuffle(options)
            questions.append(make_question(f'When do you {activity}?', options, time, f'We {activity} in the {time.lower()}!', svg, 12))
        elif t == 'sequence':
            pairs = [('breakfast', 'lunch'), ('Monday', 'Tuesday'), ('Spring', 'Summer'), ('morning', 'afternoon')]
            first, second = random.choice(pairs)
            svg_c = f'<text x="200" y="90" text-anchor="middle" font-size="18">{first.title()} → ?</text>'
            svg = create_svg_wrapper(svg_c)
            if first.lower() in [d.lower() for d in DAYS]: options = DAYS[:4]
            elif first.lower() in [s.lower() for s in SEASONS]: options = SEASONS
            else: options = [second.title(), first.title(), 'Night', 'Evening']
            random.shuffle(options)
            questions.append(make_question(f'What comes AFTER {first}?', options, second.title(), f'{second.title()} comes after {first}!', svg, 12))
        else:
            schedule = [('9:00', 'Maths'), ('10:00', 'English'), ('11:00', 'Break'), ('12:00', 'Lunch')]
            svg = svg_timetable(schedule)
            time_slot = random.choice(schedule)
            question, correct = f'What happens at {time_slot[0]}?', time_slot[1]
            options = [s[1] for s in schedule]
            random.shuffle(options)
            questions.append(make_question(question, options, correct, f'{correct} happens at {time_slot[0]}!', svg, 12))
    return questions

def generate_all_questions():
    global _question_counter
    _question_counter = {}  # Reset counter
    all_q = []
    gens = [(1, generate_level_1_questions), (2, generate_level_2_questions), (3, generate_level_3_questions),
            (4, generate_level_4_questions), (5, generate_level_5_questions), (6, generate_level_6_questions),
            (7, generate_level_7_questions), (8, generate_level_8_questions), (9, generate_level_9_questions),
            (10, generate_level_10_questions), (11, generate_level_11_questions), (12, generate_level_12_questions)]
    for level, gen in gens:
        print(f"  Generating Level {level}...")
        questions = gen()
        for q in questions:
            q['level'] = level
            q['topic'] = TOPIC
            q['mode'] = MODE
        all_q.extend(questions)
        print(f"    ✓ {len(questions)} questions generated")
    return all_q

def validate_questions(questions):
    print(f"\nValidating {len(questions)} questions...")
    errors = []
    for i, q in enumerate(questions):
        for f in ['question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer', 'level', 'topic', 'mode']:
            if f not in q: errors.append(f"Q{i}: Missing {f}")
        if 'correct_answer' in q and (not isinstance(q['correct_answer'], int) or q['correct_answer'] < 0 or q['correct_answer'] > 3):
            errors.append(f"Q{i}: bad correct_answer")
    if errors:
        for e in errors[:10]: print(f"    - {e}")
        return False
    print(f"  ✓ All valid")
    return True

def insert_questions(questions):
    print(f"\nInserting {len(questions)} questions...")
    conn = sqlite3.connect(DATABASE_PATH)
    cur = conn.cursor()
    cur.execute('DELETE FROM questions_adaptive WHERE topic = ? AND mode = ?', (TOPIC, MODE))
    print(f"  Removed {cur.rowcount} existing")
    ins = 0
    for q in questions:
        try:
            cur.execute('''INSERT INTO questions_adaptive (topic, mode, difficulty_level, difficulty_band, question_text,
                option_a, option_b, option_c, option_d, correct_answer, explanation, image_svg, question_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (q['topic'], q['mode'], q['level'], q['difficulty_band'], q['question_text'],
                 q['option_a'], q['option_b'], q['option_c'], q['option_d'], q['correct_answer'],
                 q.get('explanation', ''), q.get('image_svg', ''), q.get('question_type', 'visual')))
            ins += 1
        except Exception as e:
            print(f"  Error: {e}")
    conn.commit()
    conn.close()
    print(f"  ✓ Inserted {ins}")
    return ins

def verify_insertion():
    print(f"\nVerifying...")
    conn = sqlite3.connect(DATABASE_PATH)
    cur = conn.cursor()
    cur.execute('SELECT difficulty_level, COUNT(*) FROM questions_adaptive WHERE topic = ? AND mode = ? GROUP BY difficulty_level', (TOPIC, MODE))
    results = cur.fetchall()
    conn.close()
    total = sum(c for _, c in results)
    for lvl, cnt in results:
        print(f"    Level {lvl}: {cnt} {'✓' if cnt == QUESTIONS_PER_LEVEL else '✗'}")
    expected = QUESTIONS_PER_LEVEL * TOTAL_LEVELS
    print(f"\n  Total: {total} {'✓' if total == expected else '✗'}")
    return total == expected

if __name__ == '__main__':
    print("=" * 60)
    print(f"AgentMath L1LP Generator - {TOPIC}")
    print("=" * 60)
    questions = generate_all_questions()
    if not validate_questions(questions):
        exit(1)
    insert_questions(questions)
    verify_insertion()
    print("=" * 60)
    print("✓ COMPLETE!")
