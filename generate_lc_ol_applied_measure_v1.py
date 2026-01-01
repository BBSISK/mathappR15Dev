#!/usr/bin/env python3
"""
LC Ordinary Level Applied Measure Question Generator
Target: Irish Leaving Certificate Ordinary Level
Structure: 12 difficulty levels, 50 questions each = 600 questions
Topic ID: lc_ol_applied_measure

Covers: Unit conversions, scale drawings, speed/distance/time, rates, compound measures
"""

import random
from math import gcd

# Configuration
STRAND_ID = 11  # LC Ordinary Level strand
TOPIC_ID = "lc_ol_applied_measure"
DISPLAY_NAME = "Applied Measure"
QUESTIONS_PER_LEVEL = 50
MODE = "lc_ol"

def generate_level_1():
    """Level 1: Basic Unit Conversions - Length (cm/m/km)"""
    questions = []
    
    # Type 1: cm to m (15 questions)
    for _ in range(15):
        cm = random.randint(100, 999)
        m = cm / 100
        correct = f"{m} m"
        
        distractors = [
            f"{cm * 100} m",
            f"{cm / 10} m",
            f"{cm * 10} m"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {cm} cm to metres.",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{cm} cm ÷ 100 = {m} m"
        })
    
    # Type 2: m to cm (10 questions)
    for _ in range(10):
        m = round(random.uniform(1.5, 9.9), 1)
        cm = m * 100
        correct = f"{int(cm)} cm"
        
        distractors = [
            f"{int(m * 10)} cm",
            f"{int(m * 1000)} cm",
            f"{int(cm / 10)} cm"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {m} m to centimetres.",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{m} m × 100 = {int(cm)} cm"
        })
    
    # Type 3: m to km (10 questions)
    for _ in range(10):
        m = random.randint(1, 9) * 1000 + random.randint(0, 9) * 100
        km = m / 1000
        correct = f"{km} km"
        
        distractors = [
            f"{m * 1000} km",
            f"{m / 100} km",
            f"{km * 10} km"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {m} m to kilometres.",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{m} m ÷ 1000 = {km} km"
        })
    
    # Type 4: km to m (15 questions)
    for _ in range(15):
        km = round(random.uniform(0.5, 9.5), 1)
        m = km * 1000
        correct = f"{int(m)} m"
        
        distractors = [
            f"{int(km * 100)} m",
            f"{int(km * 10)} m",
            f"{int(m * 10)} m"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {km} km to metres.",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{km} km × 1000 = {int(m)} m"
        })
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_2():
    """Level 2: Basic Unit Conversions - Mass and Capacity"""
    questions = []
    
    # Type 1: g to kg (12 questions)
    for _ in range(12):
        g = random.randint(1, 9) * 1000 + random.randint(0, 9) * 100
        kg = g / 1000
        correct = f"{kg} kg"
        
        distractors = [
            f"{g * 1000} kg",
            f"{g / 100} kg",
            f"{kg * 10} kg"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {g} g to kilograms.",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{g} g ÷ 1000 = {kg} kg"
        })
    
    # Type 2: kg to g (12 questions)
    for _ in range(12):
        kg = round(random.uniform(0.5, 9.5), 1)
        g = kg * 1000
        correct = f"{int(g)} g"
        
        distractors = [
            f"{int(kg * 100)} g",
            f"{int(kg * 10)} g",
            f"{int(g * 10)} g"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {kg} kg to grams.",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{kg} kg × 1000 = {int(g)} g"
        })
    
    # Type 3: ml to litres (13 questions)
    for _ in range(13):
        ml = random.randint(1, 9) * 1000 + random.randint(0, 9) * 100
        litres = ml / 1000
        correct = f"{litres} L"
        
        distractors = [
            f"{ml * 1000} L",
            f"{ml / 100} L",
            f"{litres * 10} L"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {ml} ml to litres.",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{ml} ml ÷ 1000 = {litres} L"
        })
    
    # Type 4: litres to ml (13 questions)
    for _ in range(13):
        litres = round(random.uniform(0.5, 9.5), 1)
        ml = litres * 1000
        correct = f"{int(ml)} ml"
        
        distractors = [
            f"{int(litres * 100)} ml",
            f"{int(litres * 10)} ml",
            f"{int(ml * 10)} ml"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {litres} litres to millilitres.",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{litres} L × 1000 = {int(ml)} ml"
        })
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_3():
    """Level 3: Time Conversions and Calculations"""
    questions = []
    
    # Type 1: Minutes to hours (10 questions)
    for _ in range(10):
        mins = random.choice([30, 45, 60, 90, 120, 150, 180, 210, 240, 300])
        hours = mins / 60
        if hours == int(hours):
            correct = f"{int(hours)} hours"
        else:
            correct = f"{hours} hours"
        
        distractors = [
            f"{mins / 100} hours",
            f"{mins * 60} hours",
            f"{hours + 1} hours"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {mins} minutes to hours.",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{mins} minutes ÷ 60 = {hours} hours"
        })
    
    # Type 2: Hours and minutes to minutes (10 questions)
    for _ in range(10):
        hours = random.randint(1, 5)
        mins = random.randint(1, 5) * 10
        total_mins = hours * 60 + mins
        correct = f"{total_mins} minutes"
        
        distractors = [
            f"{hours * 100 + mins} minutes",
            f"{hours + mins} minutes",
            f"{total_mins + 60} minutes"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {hours} hours {mins} minutes to minutes.",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{hours} × 60 + {mins} = {total_mins} minutes"
        })
    
    # Type 3: Seconds to minutes (10 questions)
    for _ in range(10):
        secs = random.choice([60, 120, 180, 240, 300, 360, 420, 480, 540, 600])
        mins = secs // 60
        correct = f"{mins} minutes"
        
        distractors = [
            f"{secs / 100} minutes",
            f"{secs} minutes",
            f"{mins * 10} minutes"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {secs} seconds to minutes.",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{secs} seconds ÷ 60 = {mins} minutes"
        })
    
    # Type 4: Time calculations (20 questions)
    start_times = ["09:00", "09:30", "10:00", "10:15", "11:00", "11:30", "12:00", "13:00", "14:00", "14:30"]
    durations = [30, 45, 60, 75, 90, 105, 120, 150, 180]
    
    for _ in range(20):
        start = random.choice(start_times)
        duration = random.choice(durations)
        
        start_h, start_m = map(int, start.split(":"))
        end_m = start_m + duration
        end_h = start_h + end_m // 60
        end_m = end_m % 60
        
        correct = f"{end_h:02d}:{end_m:02d}"
        
        # Wrong answers
        wrong1_h = end_h
        wrong1_m = (end_m + 30) % 60
        if end_m + 30 >= 60:
            wrong1_h += 1
            
        wrong2_h = end_h - 1 if end_h > start_h else end_h + 1
        wrong2_m = end_m
        
        wrong3_h = end_h
        wrong3_m = start_m
        
        distractors = [
            f"{wrong1_h:02d}:{wrong1_m:02d}",
            f"{wrong2_h:02d}:{wrong2_m:02d}",
            f"{wrong3_h:02d}:{wrong3_m:02d}"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"A meeting starts at {start} and lasts {duration} minutes. What time does it end?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{start} + {duration} minutes = {correct}"
        })
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_4():
    """Level 4: Speed, Distance, Time - Basic Calculations"""
    questions = []
    
    # Type 1: Find distance (d = s × t) (17 questions)
    for _ in range(17):
        speed = random.choice([40, 50, 60, 70, 80, 90, 100])
        time = random.choice([1, 2, 3, 4, 5])
        distance = speed * time
        
        correct = f"{distance} km"
        distractors = [
            f"{speed + time} km",
            f"{speed} km",
            f"{distance + speed} km"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"A car travels at {speed} km/h for {time} hours. How far does it travel?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"Distance = Speed × Time = {speed} × {time} = {distance} km"
        })
    
    # Type 2: Find time (t = d ÷ s) (17 questions)
    for _ in range(17):
        speed = random.choice([40, 50, 60, 80, 100])
        time = random.choice([1, 2, 3, 4, 5])
        distance = speed * time
        
        correct = f"{time} hours"
        distractors = [
            f"{distance / 10} hours",
            f"{time + 1} hours",
            f"{speed / 10} hours"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"A car travels {distance} km at {speed} km/h. How long does the journey take?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"Time = Distance ÷ Speed = {distance} ÷ {speed} = {time} hours"
        })
    
    # Type 3: Find speed (s = d ÷ t) (16 questions)
    for _ in range(16):
        speed = random.choice([30, 40, 50, 60, 70, 80, 90, 100])
        time = random.choice([2, 3, 4, 5])
        distance = speed * time
        
        correct = f"{speed} km/h"
        distractors = [
            f"{distance + time} km/h",
            f"{distance} km/h",
            f"{speed + 10} km/h"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"A car travels {distance} km in {time} hours. What is its average speed?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"Speed = Distance ÷ Time = {distance} ÷ {time} = {speed} km/h"
        })
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_5():
    """Level 5: Scale Drawings - Reading Scales"""
    questions = []
    
    # Type 1: Scale 1:100 (12 questions)
    for _ in range(12):
        drawing_cm = random.randint(3, 15)
        actual_m = drawing_cm  # 1:100 means 1cm = 1m
        
        correct = f"{actual_m} m"
        distractors = [
            f"{drawing_cm * 10} m",
            f"{drawing_cm / 10} m",
            f"{drawing_cm * 100} m"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"On a 1:100 scale drawing, a wall measures {drawing_cm} cm. What is the actual length?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"1:100 scale: {drawing_cm} cm × 100 = {drawing_cm * 100} cm = {actual_m} m"
        })
    
    # Type 2: Scale 1:50 (12 questions)
    for _ in range(12):
        drawing_cm = random.randint(4, 20)
        actual_cm = drawing_cm * 50
        actual_m = actual_cm / 100
        
        correct = f"{actual_m} m"
        distractors = [
            f"{drawing_cm} m",
            f"{actual_m * 10} m",
            f"{actual_m / 2} m"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"On a 1:50 scale drawing, a room measures {drawing_cm} cm. What is the actual length?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"1:50 scale: {drawing_cm} cm × 50 = {actual_cm} cm = {actual_m} m"
        })
    
    # Type 3: Scale 1:200 (13 questions)
    for _ in range(13):
        drawing_cm = random.randint(2, 10)
        actual_m = drawing_cm * 2  # 1:200 means 1cm = 2m
        
        correct = f"{actual_m} m"
        distractors = [
            f"{drawing_cm} m",
            f"{actual_m * 10} m",
            f"{drawing_cm * 100} m"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"On a 1:200 scale drawing, a building measures {drawing_cm} cm. What is the actual length?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"1:200 scale: {drawing_cm} cm × 200 = {drawing_cm * 200} cm = {actual_m} m"
        })
    
    # Type 4: Find drawing length from actual (13 questions)
    for _ in range(13):
        actual_m = random.randint(3, 12)
        scale = random.choice([100, 200])
        drawing_cm = actual_m * 100 / scale
        
        correct = f"{drawing_cm} cm"
        distractors = [
            f"{actual_m} cm",
            f"{drawing_cm * 10} cm",
            f"{actual_m * scale / 100} cm"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"A room is {actual_m} m long. How long is it on a 1:{scale} scale drawing?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"Drawing length = {actual_m} m ÷ {scale} = {actual_m * 100} cm ÷ {scale} = {drawing_cm} cm"
        })
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_6():
    """Level 6: Area Conversions"""
    questions = []
    
    # Type 1: cm² to m² (12 questions)
    for _ in range(12):
        cm2 = random.choice([10000, 20000, 50000, 100000, 150000, 200000])
        m2 = cm2 / 10000
        
        correct = f"{m2} m²"
        distractors = [
            f"{cm2 / 100} m²",
            f"{cm2 / 1000} m²",
            f"{m2 * 10} m²"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {cm2:,} cm² to m².",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{cm2:,} cm² ÷ 10,000 = {m2} m²"
        })
    
    # Type 2: m² to cm² (12 questions)
    for _ in range(12):
        m2 = random.choice([1, 2, 3, 4, 5, 0.5, 1.5, 2.5])
        cm2 = int(m2 * 10000)
        
        correct = f"{cm2:,} cm²"
        distractors = [
            f"{int(m2 * 100):,} cm²",
            f"{int(m2 * 1000):,} cm²",
            f"{cm2 * 10:,} cm²"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {m2} m² to cm².",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{m2} m² × 10,000 = {cm2:,} cm²"
        })
    
    # Type 3: m² to hectares (13 questions)
    for _ in range(13):
        m2 = random.choice([10000, 20000, 50000, 100000, 150000, 200000, 500000])
        ha = m2 / 10000
        
        correct = f"{ha} ha"
        distractors = [
            f"{m2 / 1000} ha",
            f"{m2 / 100} ha",
            f"{ha * 10} ha"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {m2:,} m² to hectares.",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{m2:,} m² ÷ 10,000 = {ha} ha"
        })
    
    # Type 4: hectares to m² (13 questions)
    for _ in range(13):
        ha = random.choice([1, 2, 3, 5, 10, 0.5, 1.5, 2.5])
        m2 = int(ha * 10000)
        
        correct = f"{m2:,} m²"
        distractors = [
            f"{int(ha * 100):,} m²",
            f"{int(ha * 1000):,} m²",
            f"{m2 * 10:,} m²"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {ha} hectares to m².",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{ha} ha × 10,000 = {m2:,} m²"
        })
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_7():
    """Level 7: Volume Conversions"""
    questions = []
    
    # Type 1: cm³ to litres (12 questions)
    for _ in range(12):
        cm3 = random.choice([500, 1000, 1500, 2000, 2500, 3000, 5000, 10000])
        litres = cm3 / 1000
        
        correct = f"{litres} L"
        distractors = [
            f"{cm3 / 100} L",
            f"{cm3 / 10} L",
            f"{litres * 10} L"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {cm3:,} cm³ to litres.",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{cm3:,} cm³ ÷ 1,000 = {litres} L"
        })
    
    # Type 2: litres to cm³ (12 questions)
    for _ in range(12):
        litres = random.choice([1, 2, 3, 5, 10, 0.5, 1.5, 2.5])
        cm3 = int(litres * 1000)
        
        correct = f"{cm3:,} cm³"
        distractors = [
            f"{int(litres * 100):,} cm³",
            f"{int(litres * 10):,} cm³",
            f"{cm3 * 10:,} cm³"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {litres} litres to cm³.",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{litres} L × 1,000 = {cm3:,} cm³"
        })
    
    # Type 3: m³ to litres (13 questions)
    for _ in range(13):
        m3 = random.choice([1, 2, 3, 5, 0.5, 0.1, 0.2, 0.25])
        litres = m3 * 1000
        
        correct = f"{int(litres):,} L"
        distractors = [
            f"{int(m3 * 100):,} L",
            f"{int(m3 * 10):,} L",
            f"{int(litres * 10):,} L"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {m3} m³ to litres.",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{m3} m³ × 1,000 = {int(litres):,} L"
        })
    
    # Type 4: litres to m³ (13 questions)
    for _ in range(13):
        litres = random.choice([1000, 2000, 5000, 500, 250, 100, 2500, 750])
        m3 = litres / 1000
        
        correct = f"{m3} m³"
        distractors = [
            f"{litres / 100} m³",
            f"{litres / 10} m³",
            f"{m3 * 10} m³"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {litres:,} litres to m³.",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{litres:,} L ÷ 1,000 = {m3} m³"
        })
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_8():
    """Level 8: Speed with Mixed Units"""
    questions = []
    
    # Type 1: km/h to m/s (12 questions)
    for _ in range(12):
        kmh = random.choice([36, 54, 72, 90, 108, 126, 144])
        ms = kmh / 3.6
        
        correct = f"{ms:.0f} m/s"
        distractors = [
            f"{kmh * 3.6:.0f} m/s",
            f"{kmh / 10:.1f} m/s",
            f"{ms * 2:.0f} m/s"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {kmh} km/h to m/s.",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{kmh} km/h ÷ 3.6 = {ms:.0f} m/s"
        })
    
    # Type 2: m/s to km/h (12 questions)
    for _ in range(12):
        ms = random.choice([5, 10, 15, 20, 25, 30, 35, 40])
        kmh = ms * 3.6
        
        correct = f"{kmh:.0f} km/h"
        distractors = [
            f"{ms / 3.6:.1f} km/h",
            f"{ms * 10:.0f} km/h",
            f"{kmh / 2:.0f} km/h"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Convert {ms} m/s to km/h.",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{ms} m/s × 3.6 = {kmh:.0f} km/h"
        })
    
    # Type 3: Distance in metres, time in seconds (13 questions)
    for _ in range(13):
        distance_m = random.choice([100, 200, 400, 500, 800, 1000])
        time_s = random.choice([10, 20, 25, 40, 50, 100])
        speed_ms = distance_m / time_s
        
        correct = f"{speed_ms:.0f} m/s"
        distractors = [
            f"{distance_m + time_s:.0f} m/s",
            f"{time_s / distance_m * 100:.1f} m/s",
            f"{speed_ms * 2:.0f} m/s"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"A runner covers {distance_m} m in {time_s} seconds. What is their speed in m/s?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"Speed = {distance_m} ÷ {time_s} = {speed_ms:.0f} m/s"
        })
    
    # Type 4: Time in minutes, need to convert (13 questions)
    for _ in range(13):
        speed_kmh = random.choice([60, 80, 100, 120])
        time_min = random.choice([30, 45, 60, 90, 120])
        time_h = time_min / 60
        distance = speed_kmh * time_h
        
        correct = f"{distance:.0f} km"
        distractors = [
            f"{speed_kmh * time_min:.0f} km",
            f"{distance / 2:.0f} km",
            f"{speed_kmh + time_min:.0f} km"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"A car travels at {speed_kmh} km/h for {time_min} minutes. How far does it travel?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"Time = {time_min} min = {time_h} hours. Distance = {speed_kmh} × {time_h} = {distance:.0f} km"
        })
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_9():
    """Level 9: Rates and Unit Rates"""
    questions = []
    
    # Type 1: Price per unit (12 questions)
    items = ["apples", "oranges", "pens", "notebooks", "bottles of water", "packets of crisps"]
    for _ in range(12):
        item = random.choice(items)
        quantity = random.choice([4, 5, 6, 8, 10, 12])
        total_price = quantity * random.choice([1.50, 2.00, 2.50, 3.00])
        unit_price = total_price / quantity
        
        correct = f"€{unit_price:.2f}"
        distractors = [
            f"€{total_price:.2f}",
            f"€{unit_price * 2:.2f}",
            f"€{total_price / 2:.2f}"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"{quantity} {item} cost €{total_price:.2f}. What is the price per {item[:-1] if item.endswith('s') else item}?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"€{total_price:.2f} ÷ {quantity} = €{unit_price:.2f}"
        })
    
    # Type 2: Fuel consumption (12 questions)
    for _ in range(12):
        litres = random.choice([30, 40, 50, 60])
        km = litres * random.choice([10, 12, 15])
        consumption = km / litres
        
        correct = f"{consumption:.0f} km/L"
        distractors = [
            f"{litres / km * 100:.1f} km/L",
            f"{consumption * 2:.0f} km/L",
            f"{km:.0f} km/L"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"A car uses {litres} litres of fuel to travel {km} km. What is its fuel efficiency?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{km} km ÷ {litres} L = {consumption:.0f} km/L"
        })
    
    # Type 3: Work rate (13 questions)
    for _ in range(13):
        items = random.choice([10, 12, 15, 20, 24, 30])
        hours = random.choice([2, 3, 4, 5])
        rate = items / hours
        
        correct = f"{rate:.0f} per hour"
        distractors = [
            f"{items:.0f} per hour",
            f"{hours:.0f} per hour",
            f"{rate * 2:.0f} per hour"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"A worker completes {items} tasks in {hours} hours. What is their work rate?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"{items} tasks ÷ {hours} hours = {rate:.0f} per hour"
        })
    
    # Type 4: Best value comparison (13 questions)
    for _ in range(13):
        item = random.choice(["juice", "cereal", "rice", "pasta"])
        
        # Option A
        size_a = random.choice([500, 750, 1000])
        price_a = round(size_a / 1000 * random.uniform(2, 4), 2)
        rate_a = price_a / (size_a / 1000)
        
        # Option B (make one clearly better)
        size_b = size_a + random.choice([250, 500])
        if random.random() > 0.5:
            price_b = round(price_a * 1.3, 2)  # A is better
            better = "A"
        else:
            price_b = round(price_a * 1.1, 2)  # B is better (more for slightly more)
            rate_b = price_b / (size_b / 1000)
            if rate_b < rate_a:
                better = "B"
            else:
                better = "A"
        
        correct = f"Option {better}"
        options = ["Option A", "Option B", "Same value", "Cannot determine"]
        options.remove(correct)
        
        questions.append({
            "question_text": f"Option A: {size_a}ml of {item} for €{price_a:.2f}. Option B: {size_b}ml for €{price_b:.2f}. Which is better value?",
            "correct_answer": correct,
            "distractor1": options[0],
            "distractor2": options[1],
            "distractor3": options[2],
            "explanation": f"Compare price per ml to find best value. {correct} is better."
        })
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_10():
    """Level 10: Scale Drawings - Area Calculations"""
    questions = []
    
    # Type 1: Area from scale drawing 1:100 (17 questions)
    for _ in range(17):
        length_cm = random.randint(4, 10)
        width_cm = random.randint(3, 8)
        
        # 1:100 means 1cm = 1m
        actual_length = length_cm
        actual_width = width_cm
        actual_area = actual_length * actual_width
        
        correct = f"{actual_area} m²"
        distractors = [
            f"{length_cm * width_cm / 10} m²",
            f"{actual_area * 100} m²",
            f"{actual_area * 10} m²"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"A room is {length_cm} cm × {width_cm} cm on a 1:100 scale drawing. What is its actual area?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"Actual: {actual_length} m × {actual_width} m = {actual_area} m²"
        })
    
    # Type 2: Area from scale drawing 1:200 (17 questions)
    for _ in range(17):
        length_cm = random.randint(3, 8)
        width_cm = random.randint(2, 6)
        
        # 1:200 means 1cm = 2m
        actual_length = length_cm * 2
        actual_width = width_cm * 2
        actual_area = actual_length * actual_width
        
        correct = f"{actual_area} m²"
        distractors = [
            f"{length_cm * width_cm * 2} m²",
            f"{actual_area / 4} m²",
            f"{length_cm * width_cm} m²"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"A garden is {length_cm} cm × {width_cm} cm on a 1:200 scale drawing. What is its actual area?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"Actual: {actual_length} m × {actual_width} m = {actual_area} m²"
        })
    
    # Type 3: Area from scale drawing 1:50 (16 questions)
    for _ in range(16):
        length_cm = random.randint(6, 16)
        width_cm = random.randint(4, 12)
        
        # 1:50 means 1cm = 0.5m
        actual_length = length_cm * 0.5
        actual_width = width_cm * 0.5
        actual_area = actual_length * actual_width
        
        correct = f"{actual_area} m²"
        distractors = [
            f"{length_cm * width_cm} m²",
            f"{actual_area * 4} m²",
            f"{actual_area / 2} m²"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"A floor plan shows a room as {length_cm} cm × {width_cm} cm at 1:50 scale. What is the actual area?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"Actual: {actual_length} m × {actual_width} m = {actual_area} m²"
        })
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_11():
    """Level 11: Compound Measures and Multi-Step Problems"""
    questions = []
    
    # Type 1: Density calculations (12 questions)
    for _ in range(12):
        mass = random.choice([100, 200, 300, 500, 1000])
        volume = random.choice([50, 100, 200, 250, 500])
        density = mass / volume
        
        correct = f"{density} g/cm³"
        distractors = [
            f"{volume / mass:.2f} g/cm³",
            f"{mass + volume} g/cm³",
            f"{density * 10} g/cm³"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"An object has mass {mass} g and volume {volume} cm³. What is its density?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"Density = Mass ÷ Volume = {mass} ÷ {volume} = {density} g/cm³"
        })
    
    # Type 2: Population density (12 questions)
    for _ in range(12):
        population = random.choice([10000, 20000, 50000, 100000, 200000])
        area = random.choice([50, 100, 200, 500, 1000])
        density = population / area
        
        correct = f"{int(density)} people/km²"
        distractors = [
            f"{int(area / population * 10000)} people/km²",
            f"{int(density * 10)} people/km²",
            f"{int(density / 10)} people/km²"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"A town has population {population:,} and area {area} km². What is the population density?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"Density = {population:,} ÷ {area} = {int(density)} people/km²"
        })
    
    # Type 3: Two-part journey problems (13 questions)
    for _ in range(13):
        speed1 = random.choice([40, 50, 60])
        time1 = random.choice([1, 2])
        speed2 = random.choice([70, 80, 90])
        time2 = random.choice([1, 2, 3])
        
        dist1 = speed1 * time1
        dist2 = speed2 * time2
        total_dist = dist1 + dist2
        total_time = time1 + time2
        avg_speed = total_dist / total_time
        
        correct = f"{avg_speed:.0f} km/h"
        distractors = [
            f"{(speed1 + speed2) / 2:.0f} km/h",
            f"{total_dist:.0f} km/h",
            f"{avg_speed + 10:.0f} km/h"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"A car travels at {speed1} km/h for {time1} hour(s), then {speed2} km/h for {time2} hour(s). What is the average speed?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"Total distance = {total_dist} km, Total time = {total_time} h. Average = {avg_speed:.0f} km/h"
        })
    
    # Type 4: Pressure calculations (13 questions)
    for _ in range(13):
        force = random.choice([100, 200, 500, 1000, 2000])
        area = random.choice([2, 4, 5, 10, 20])
        pressure = force / area
        
        correct = f"{int(pressure)} N/m²"
        distractors = [
            f"{force * area} N/m²",
            f"{int(area / force * 1000)} N/m²",
            f"{int(pressure * 10)} N/m²"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"A force of {force} N acts on an area of {area} m². What is the pressure?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"Pressure = Force ÷ Area = {force} ÷ {area} = {int(pressure)} N/m²"
        })
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_12():
    """Level 12: Mastery Challenge - Complex Applied Measure Problems"""
    questions = []
    
    # Type 1: Scale drawings with area and perimeter (12 questions)
    for _ in range(12):
        scale = random.choice([100, 200])
        length_cm = random.randint(5, 10)
        width_cm = random.randint(3, 7)
        
        # Calculate actual dimensions
        if scale == 100:
            actual_l = length_cm  # metres
            actual_w = width_cm
        else:  # 1:200
            actual_l = length_cm * 2
            actual_w = width_cm * 2
        
        actual_area = actual_l * actual_w
        
        correct = f"{actual_area} m²"
        distractors = [
            f"{length_cm * width_cm} m²",
            f"{actual_area * scale} m²",
            f"{actual_area // 2} m²"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"A room is {length_cm} cm × {width_cm} cm on a 1:{scale} drawing. What is its actual area?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"Actual: {actual_l} m × {actual_w} m = {actual_area} m²"
        })
    
    # Type 2: Multi-step speed problems (12 questions)
    for _ in range(12):
        dist_km = random.choice([120, 150, 180, 200, 240])
        speed_kmh = random.choice([60, 80, 100])
        time_h = dist_km / speed_kmh
        time_min = int(time_h * 60)
        
        correct = f"{time_min} minutes"
        distractors = [
            f"{int(time_h)} minutes",
            f"{time_min + 60} minutes",
            f"{dist_km} minutes"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"How long (in minutes) to travel {dist_km} km at {speed_kmh} km/h?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"Time = {dist_km} ÷ {speed_kmh} = {time_h} hours = {time_min} minutes"
        })
    
    # Type 3: Volume and capacity problems (13 questions)
    for _ in range(13):
        length = random.choice([20, 30, 40, 50])
        width = random.choice([10, 15, 20, 25])
        height = random.choice([10, 15, 20])
        
        volume_cm3 = length * width * height
        litres = volume_cm3 / 1000
        
        correct = f"{litres} L"
        distractors = [
            f"{volume_cm3} L",
            f"{litres * 10} L",
            f"{litres / 10} L"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"A tank is {length} cm × {width} cm × {height} cm. What is its capacity in litres?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"Volume = {volume_cm3} cm³ = {litres} L"
        })
    
    # Type 4: Combined rate problems (13 questions)
    for _ in range(13):
        rate1 = random.choice([10, 12, 15])
        rate2 = random.choice([8, 10, 12])
        hours = random.choice([3, 4, 5, 6])
        
        total = (rate1 + rate2) * hours
        
        correct = f"{total}"
        distractors = [
            f"{rate1 * hours}",
            f"{rate2 * hours}",
            f"{(rate1 + rate2) * hours * 2}"
        ]
        random.shuffle(distractors)
        
        questions.append({
            "question_text": f"Worker A produces {rate1} items/hour, Worker B produces {rate2} items/hour. How many items do they produce together in {hours} hours?",
            "correct_answer": correct,
            "distractor1": distractors[0],
            "distractor2": distractors[1],
            "distractor3": distractors[2],
            "explanation": f"Combined rate = {rate1 + rate2}/hour. Total = {rate1 + rate2} × {hours} = {total}"
        })
    
    random.shuffle(questions)
    return questions[:QUESTIONS_PER_LEVEL]


def generate_all_questions():
    """Generate all questions for all levels."""
    all_questions = []
    
    generators = [
        (1, generate_level_1, "Length Conversions"),
        (2, generate_level_2, "Mass and Capacity"),
        (3, generate_level_3, "Time Conversions"),
        (4, generate_level_4, "Speed Distance Time"),
        (5, generate_level_5, "Scale Drawings - Reading"),
        (6, generate_level_6, "Area Conversions"),
        (7, generate_level_7, "Volume Conversions"),
        (8, generate_level_8, "Speed Mixed Units"),
        (9, generate_level_9, "Rates and Unit Rates"),
        (10, generate_level_10, "Scale - Area"),
        (11, generate_level_11, "Compound Measures"),
        (12, generate_level_12, "Mastery Challenge"),
    ]
    
    for level, generator, name in generators:
        questions = generator()
        for q in questions:
            q['level'] = level
            q['level_name'] = name
        all_questions.extend(questions)
        print(f"Level {level} ({name}): {len(questions)} questions")
    
    return all_questions


def generate_sql(questions):
    """Generate SQL statements for database insertion."""
    sql_statements = []
    
    sql_statements.append(f"""
-- LC Ordinary Level Applied Measure
-- Strand ID: {STRAND_ID} (LC Ordinary Level)
-- Total Questions: {len(questions)}
-- Structure: 12 levels × 50 questions = 600 questions

-- Insert topic
INSERT OR REPLACE INTO topics (topic_id, strand_id, display_name, description, sort_order, is_active, mode, is_visible)
VALUES ('{TOPIC_ID}', {STRAND_ID}, '{DISPLAY_NAME}', 'Applied Measure for LC Ordinary Level - 12 progressive difficulty levels', 7, 1, '{MODE}', 1);

-- Delete existing questions for this topic
DELETE FROM questions_adaptive WHERE topic = '{TOPIC_ID}';

-- Insert questions
""")
    
    for i, q in enumerate(questions):
        q_text = q['question_text'].replace("'", "''")
        correct = q['correct_answer'].replace("'", "''")
        d1 = q['distractor1'].replace("'", "''")
        d2 = q['distractor2'].replace("'", "''")
        d3 = q['distractor3'].replace("'", "''")
        explanation = q['explanation'].replace("'", "''")
        level_name = q['level_name'].replace("'", "''")
        
        sql = f"""INSERT INTO questions_adaptive (topic, difficulty_level, question_text, correct_answer, distractor1, distractor2, distractor3, explanation, level_name)
VALUES ('{TOPIC_ID}', {q['level']}, '{q_text}', '{correct}', '{d1}', '{d2}', '{d3}', '{explanation}', '{level_name}');"""
        sql_statements.append(sql)
    
    return '\n'.join(sql_statements)


def main():
    """Main function to generate questions and SQL."""
    print("=" * 60)
    print("LC Ordinary Level Applied Measure Question Generator")
    print("=" * 60)
    
    questions = generate_all_questions()
    
    print(f"\nTotal questions generated: {len(questions)}")
    
    sql = generate_sql(questions)
    
    sql_filename = "lc_ol_applied_measure_complete.sql"
    with open(sql_filename, 'w') as f:
        f.write(sql)
    
    print(f"\nSQL file saved: {sql_filename}")
    print(f"File size: {len(sql):,} characters")
    
    print("\n" + "=" * 60)
    print("Summary by Level:")
    print("=" * 60)
    for level in range(1, 13):
        level_qs = [q for q in questions if q['level'] == level]
        if level_qs:
            print(f"Level {level:2d}: {len(level_qs):3d} questions - {level_qs[0]['level_name']}")
    
    return questions, sql


if __name__ == "__main__":
    main()
