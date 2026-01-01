#!/usr/bin/env python3
"""
FRACTIONS QUESTION GENERATOR - PRODUCTION VERSION
==================================================
This script:
1. Automatically finds the database
2. Fixes schema constraints if needed
3. Inserts questions with all required fields
4. Validates everything works

Run: python3 generate_fractions_final.py
"""

import sqlite3
import os
import random
import math
from datetime import datetime

# ============================================================
# DATABASE CONFIGURATION
# ============================================================

def find_database():
    """Find the database file"""
    paths = [
        'instance/mathquiz.db',
        'mathquiz.db', 
        'mathapp.db',
    ]
    for path in paths:
        if os.path.exists(path):
            print(f"✅ Found database: {path}")
            return path
    
    print("❌ ERROR: Database not found!")
    print("Checked:", paths)
    exit(1)

DB_PATH = None

def get_connection():
    global DB_PATH
    if DB_PATH is None:
        DB_PATH = find_database()
    return sqlite3.connect(DB_PATH)


# ============================================================
# SCHEMA FIXES
# ============================================================

def fix_schema():
    """Ensure database schema supports levels 1-12"""
    conn = get_connection()
    cursor = conn.cursor()
    
    print("\n🔧 Checking database schema...")
    
    # Get current table info
    cursor.execute("PRAGMA table_info(questions_adaptive)")
    columns = {row[1]: row for row in cursor.fetchall()}
    
    print(f"   Found {len(columns)} columns")
    
    # Check if we need to rebuild for CHECK constraint
    # SQLite doesn't let us modify CHECK constraints directly
    # We need to recreate the table
    
    try:
        # Test if level 11 works
        cursor.execute("""
            INSERT INTO questions_adaptive 
            (topic, difficulty_level, difficulty_band, question_text,
             option_a, option_b, option_c, option_d, correct_answer,
             explanation, is_active, question_type)
            VALUES ('_test_', 11, 'application', 'test', 'a', 'b', 'c', 'd', 0, '', 1, 'test')
        """)
        # If it worked, delete the test row
        cursor.execute("DELETE FROM questions_adaptive WHERE topic = '_test_'")
        conn.commit()
        print("   ✅ Schema already supports levels 11-12")
        conn.close()
        return
    except sqlite3.IntegrityError as e:
        if "CHECK constraint" in str(e):
            print("   ⚠️  Need to update CHECK constraint for levels 11-12")
            conn.rollback()
        else:
            raise
    
    # Rebuild table with updated constraint
    print("   🔄 Rebuilding table with updated constraints...")
    
    try:
        # Create new table with correct constraint
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS questions_adaptive_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT NOT NULL,
                question_text TEXT NOT NULL,
                option_a TEXT NOT NULL,
                option_b TEXT NOT NULL,
                option_c TEXT NOT NULL,
                option_d TEXT NOT NULL,
                correct_answer INTEGER NOT NULL CHECK (correct_answer BETWEEN 0 AND 3),
                explanation TEXT NOT NULL DEFAULT '',
                difficulty_level INTEGER NOT NULL CHECK (difficulty_level BETWEEN 1 AND 12),
                difficulty_band TEXT NOT NULL,
                complexity_factors TEXT,
                estimated_time_seconds INTEGER DEFAULT 30,
                hint_text TEXT,
                hint_penalty INTEGER DEFAULT 50,
                question_type TEXT DEFAULT 'text',
                times_shown INTEGER DEFAULT 0,
                times_correct INTEGER DEFAULT 0,
                avg_response_time REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_active INTEGER DEFAULT 1,
                image_svg TEXT,
                linked_topics TEXT,
                UNIQUE(topic, difficulty_level, question_text)
            )
        """)
        
        # Copy existing data
        cursor.execute("""
            INSERT INTO questions_adaptive_new 
            SELECT id, topic, question_text, option_a, option_b, option_c, option_d,
                   correct_answer, explanation, difficulty_level, difficulty_band,
                   complexity_factors, estimated_time_seconds, hint_text, hint_penalty,
                   question_type, times_shown, times_correct, avg_response_time,
                   created_at, updated_at, is_active, image_svg, 
                   CASE WHEN EXISTS(SELECT 1 FROM pragma_table_info('questions_adaptive') WHERE name='linked_topics') 
                        THEN linked_topics ELSE NULL END
            FROM questions_adaptive
        """)
        
        # Swap tables
        cursor.execute("DROP TABLE questions_adaptive")
        cursor.execute("ALTER TABLE questions_adaptive_new RENAME TO questions_adaptive")
        
        conn.commit()
        print("   ✅ Table rebuilt successfully")
        
    except Exception as e:
        conn.rollback()
        print(f"   ❌ Error rebuilding table: {e}")
        print("   Trying alternative approach...")
        
        # Alternative: just delete and recreate
        cursor.execute("DROP TABLE IF EXISTS questions_adaptive_new")
        cursor.execute("""
            CREATE TABLE questions_adaptive_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT NOT NULL,
                question_text TEXT NOT NULL,
                option_a TEXT NOT NULL,
                option_b TEXT NOT NULL,
                option_c TEXT NOT NULL,
                option_d TEXT NOT NULL,
                correct_answer INTEGER NOT NULL CHECK (correct_answer BETWEEN 0 AND 3),
                explanation TEXT NOT NULL DEFAULT '',
                difficulty_level INTEGER NOT NULL CHECK (difficulty_level BETWEEN 1 AND 12),
                difficulty_band TEXT NOT NULL,
                complexity_factors TEXT,
                estimated_time_seconds INTEGER DEFAULT 30,
                hint_text TEXT,
                hint_penalty INTEGER DEFAULT 50,
                question_type TEXT DEFAULT 'text',
                times_shown INTEGER DEFAULT 0,
                times_correct INTEGER DEFAULT 0,
                avg_response_time REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_active INTEGER DEFAULT 1,
                image_svg TEXT,
                linked_topics TEXT,
                UNIQUE(topic, difficulty_level, question_text)
            )
        """)
        
        # Copy what we can
        cursor.execute("""
            INSERT OR IGNORE INTO questions_adaptive_new 
            (topic, question_text, option_a, option_b, option_c, option_d,
             correct_answer, explanation, difficulty_level, difficulty_band,
             question_type, is_active, image_svg)
            SELECT topic, question_text, option_a, option_b, option_c, option_d,
                   correct_answer, COALESCE(explanation, ''), difficulty_level, difficulty_band,
                   COALESCE(question_type, 'text'), COALESCE(is_active, 1), image_svg
            FROM questions_adaptive
            WHERE difficulty_level <= 10
        """)
        
        cursor.execute("DROP TABLE questions_adaptive")
        cursor.execute("ALTER TABLE questions_adaptive_new RENAME TO questions_adaptive")
        conn.commit()
        print("   ✅ Table recreated successfully")
    
    conn.close()


# ============================================================
# SVG GENERATORS
# ============================================================

def svg_pie_chart(numerator, denominator, size=160):
    """Generate a pie chart SVG showing a fraction"""
    cx, cy, r = size // 2, size // 2, size // 2 - 15
    
    if numerator == 0:
        return f'''<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">
            <circle cx="{cx}" cy="{cy}" r="{r}" fill="#E8F5E9" stroke="#333" stroke-width="2"/>
        </svg>'''
    
    if numerator >= denominator:
        return f'''<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">
            <circle cx="{cx}" cy="{cy}" r="{r}" fill="#4CAF50" stroke="#333" stroke-width="2"/>
        </svg>'''
    
    slices = []
    angle_per_slice = 360 / denominator
    
    for i in range(denominator):
        start_angle = i * angle_per_slice - 90
        end_angle = (i + 1) * angle_per_slice - 90
        
        x1 = cx + r * math.cos(math.radians(start_angle))
        y1 = cy + r * math.sin(math.radians(start_angle))
        x2 = cx + r * math.cos(math.radians(end_angle))
        y2 = cy + r * math.sin(math.radians(end_angle))
        
        large_arc = 1 if angle_per_slice > 180 else 0
        color = '#4CAF50' if i < numerator else '#E8F5E9'
        
        path = f'M{cx},{cy} L{x1:.1f},{y1:.1f} A{r},{r} 0 {large_arc},1 {x2:.1f},{y2:.1f} Z'
        slices.append(f'<path d="{path}" fill="{color}" stroke="#333" stroke-width="1"/>')
    
    return f'''<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">{''.join(slices)}</svg>'''


def svg_fraction_bar(numerator, denominator, width=220, height=50):
    """Generate a fraction bar SVG"""
    bar_height = 35
    segment_width = (width - 20) / denominator
    
    segments = []
    for i in range(denominator):
        color = '#4CAF50' if i < numerator else '#E8F5E9'
        x = 10 + i * segment_width
        segments.append(f'<rect x="{x:.1f}" y="8" width="{segment_width:.1f}" height="{bar_height}" fill="{color}" stroke="#333" stroke-width="1"/>')
    
    return f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">{''.join(segments)}</svg>'''


# ============================================================
# QUESTION GENERATORS BY LEVEL
# ============================================================

def generate_level_1():
    """Level 1: Identify halves only - THE SIMPLEST FRACTION"""
    questions = []
    
    # Pie charts showing 1/2
    for i in range(8):
        svg = svg_pie_chart(1, 2)
        questions.append({
            'text': f'What fraction of the circle is shaded green? [L1-{1000+i}]',
            'options': ['1/2', '1/4', '1/3', '2/2'],
            'correct': 0,
            'svg': svg,
            'type': 'visual'
        })
    
    # Fraction bars showing 1/2
    for i in range(7):
        svg = svg_fraction_bar(1, 2)
        questions.append({
            'text': f'What fraction of the bar is green? [L1-{1100+i}]',
            'options': ['1/2', '1/4', '2/4', '1/3'],
            'correct': 0,
            'svg': svg,
            'type': 'visual'
        })
    
    # Word problems about halves - varied items
    items = ['pizza', 'cake', 'apple', 'sandwich', 'cookie', 'orange', 'chocolate bar', 'pie']
    for i, item in enumerate(items):
        questions.append({
            'text': f'A {item} is cut into 2 equal pieces. What fraction is each piece? [L1-{1200+i}]',
            'options': ['1/2', '1/4', '2/2', '1/3'],
            'correct': 0,
            'svg': '',
            'type': 'word_problem'
        })
    
    # Sharing problems
    names = ['Seán', 'Aoife', 'Ciarán', 'Niamh', 'Oisín']
    for i, name in enumerate(names):
        questions.append({
            'text': f'{name} shares a cookie equally with a friend. What fraction does each get? [L1-{1300+i}]',
            'options': ['1/2', '1/3', '2/2', '1/4'],
            'correct': 0,
            'svg': '',
            'type': 'word_problem'
        })
    
    return questions


def generate_level_2():
    """Level 2: Quarters and thirds - BUILDING ON HALVES"""
    questions = []
    
    # Quarters - all variations
    for num in [1, 2, 3]:
        svg = svg_pie_chart(num, 4)
        options = [f'{num}/4', f'{num}/3', f'{4-num}/4', f'{num}/2']
        questions.append({
            'text': f'The circle is divided into quarters. What fraction is green? [L2-{2000+num}]',
            'options': options,
            'correct': 0,
            'svg': svg,
            'type': 'visual'
        })
        
        # Bar version
        svg_bar = svg_fraction_bar(num, 4)
        questions.append({
            'text': f'The bar shows quarters. What fraction is green? [L2-{2010+num}]',
            'options': options,
            'correct': 0,
            'svg': svg_bar,
            'type': 'visual'
        })
    
    # Thirds - all variations
    for num in [1, 2]:
        svg = svg_pie_chart(num, 3)
        options = [f'{num}/3', f'{num}/4', f'{3-num}/3', f'{num}/2']
        questions.append({
            'text': f'The circle is divided into thirds. What fraction is green? [L2-{2100+num}]',
            'options': options,
            'correct': 0,
            'svg': svg,
            'type': 'visual'
        })
        
        svg_bar = svg_fraction_bar(num, 3)
        questions.append({
            'text': f'The bar shows thirds. What fraction is green? [L2-{2110+num}]',
            'options': options,
            'correct': 0,
            'svg': svg_bar,
            'type': 'visual'
        })
    
    # Word problems - quarters
    items = ['pizza', 'cake', 'chocolate bar', 'sandwich']
    for i, item in enumerate(items):
        num = (i % 3) + 1
        questions.append({
            'text': f'A {item} is cut into 4 equal pieces. Aoife eats {num}. What fraction did she eat? [L2-{2200+i}]',
            'options': [f'{num}/4', f'{num}/3', f'{4-num}/4', '1/2'],
            'correct': 0,
            'svg': '',
            'type': 'word_problem'
        })
    
    # Word problems - thirds
    for i, item in enumerate(['pie', 'orange', 'apple']):
        num = (i % 2) + 1
        questions.append({
            'text': f'A {item} is cut into 3 equal pieces. Seán eats {num}. What fraction did he eat? [L2-{2300+i}]',
            'options': [f'{num}/3', f'{num}/4', f'{3-num}/3', '1/2'],
            'correct': 0,
            'svg': '',
            'type': 'word_problem'
        })
    
    return questions


def generate_level_3():
    """Level 3: Various fractions up to tenths - READING ANY FRACTION"""
    questions = []
    
    # Fifths
    for num in [1, 2, 3, 4]:
        svg = svg_pie_chart(num, 5)
        questions.append({
            'text': f'This circle is divided into fifths. What fraction is green? [L3-{3000+num}]',
            'options': [f'{num}/5', f'{num}/6', f'{5-num}/5', f'{num}/4'],
            'correct': 0,
            'svg': svg,
            'type': 'visual'
        })
    
    # Sixths
    for num in [1, 2, 3, 4, 5]:
        svg = svg_pie_chart(num, 6)
        questions.append({
            'text': f'What fraction of the circle is green? [L3-{3100+num}]',
            'options': [f'{num}/6', f'{num}/5', f'{6-num}/6', f'{num}/8'],
            'correct': 0,
            'svg': svg,
            'type': 'visual'
        })
    
    # Eighths
    for num in [1, 3, 5, 7]:
        svg = svg_pie_chart(num, 8)
        questions.append({
            'text': f'What fraction is shaded? [L3-{3200+num}]',
            'options': [f'{num}/8', f'{num}/6', f'{8-num}/8', f'{num}/10'],
            'correct': 0,
            'svg': svg,
            'type': 'visual'
        })
    
    # Tenths
    for num in [1, 3, 7, 9]:
        svg = svg_fraction_bar(num, 10)
        questions.append({
            'text': f'What fraction of the bar is green? [L3-{3300+num}]',
            'options': [f'{num}/10', f'{num}/8', f'{10-num}/10', f'{num}/5'],
            'correct': 0,
            'svg': svg,
            'type': 'visual'
        })
    
    # Word problems with varied denominators
    scenarios = [
        ('class', 'students', 5, 3, 'are girls'),
        ('bag', 'sweets', 6, 4, 'are red'),
        ('box', 'crayons', 8, 5, 'are blue'),
        ('garden', 'flowers', 10, 7, 'are roses'),
    ]
    for i, (container, items, total, part, description) in enumerate(scenarios):
        questions.append({
            'text': f'In a {container} of {total} {items}, {part} {description}. What fraction {description}? [L3-{3400+i}]',
            'options': [f'{part}/{total}', f'{total-part}/{total}', f'{part}/{total+1}', f'{total}/{part}'],
            'correct': 0,
            'svg': '',
            'type': 'word_problem'
        })
    
    return questions


def generate_level_4():
    """Level 4: Simplify fractions - NEW SKILL: REDUCING TO LOWEST TERMS"""
    questions = []
    
    # Clear simplification cases - each is unique
    simplify_pairs = [
        (2, 4, 1, 2, 'Divide both by 2'),
        (3, 6, 1, 2, 'Divide both by 3'),
        (4, 8, 1, 2, 'Divide both by 4'),
        (5, 10, 1, 2, 'Divide both by 5'),
        (2, 6, 1, 3, 'Divide both by 2'),
        (3, 9, 1, 3, 'Divide both by 3'),
        (4, 12, 1, 3, 'Divide both by 4'),
        (2, 8, 1, 4, 'Divide both by 2'),
        (3, 12, 1, 4, 'Divide both by 3'),
        (4, 6, 2, 3, 'Divide both by 2'),
        (6, 9, 2, 3, 'Divide both by 3'),
        (6, 8, 3, 4, 'Divide both by 2'),
        (9, 12, 3, 4, 'Divide both by 3'),
        (4, 10, 2, 5, 'Divide both by 2'),
        (6, 10, 3, 5, 'Divide both by 2'),
        (8, 10, 4, 5, 'Divide both by 2'),
        (6, 12, 1, 2, 'Divide both by 6'),
        (8, 12, 2, 3, 'Divide both by 4'),
        (10, 12, 5, 6, 'Divide both by 2'),
        (15, 20, 3, 4, 'Divide both by 5'),
    ]
    
    for i, (n, d, sn, sd, hint) in enumerate(simplify_pairs):
        questions.append({
            'text': f'Simplify {n}/{d} to its lowest terms [L4-{4000+i}]',
            'options': [f'{sn}/{sd}', f'{n}/{d}', f'{sn}/{d}', f'{n}/{sd}'],
            'correct': 0,
            'svg': '',
            'type': 'calculation'
        })
    
    # "Is this in lowest terms?" questions
    lowest_terms = [
        ('1/2', True), ('2/4', False), ('3/4', True), ('6/8', False),
        ('1/3', True), ('2/6', False), ('2/3', True), ('4/6', False),
        ('1/5', True), ('3/5', True), ('2/10', False), ('4/5', True),
    ]
    
    for i, (frac, is_lowest) in enumerate(lowest_terms):
        if is_lowest:
            questions.append({
                'text': f'Is {frac} already in its lowest terms? [L4-{4100+i}]',
                'options': ['Yes, it is simplified', 'No, simplify to 1/2', 'No, simplify to 1/4', 'No, simplify to 1/3'],
                'correct': 0,
                'svg': '',
                'type': 'calculation'
            })
    
    return questions


def generate_level_5():
    """Level 5: Equivalent fractions - NEW SKILL: SAME VALUE, DIFFERENT LOOK"""
    questions = []
    
    # Find the equivalent (multiply both)
    equiv_cases = [
        (1, 2, 2, 4), (1, 2, 3, 6), (1, 2, 4, 8), (1, 2, 5, 10),
        (1, 3, 2, 6), (1, 3, 3, 9), (1, 3, 4, 12),
        (2, 3, 4, 6), (2, 3, 6, 9), (2, 3, 8, 12),
        (1, 4, 2, 8), (1, 4, 3, 12), (3, 4, 6, 8), (3, 4, 9, 12),
        (1, 5, 2, 10), (2, 5, 4, 10), (3, 5, 6, 10),
    ]
    
    for i, (n1, d1, n2, d2) in enumerate(equiv_cases):
        questions.append({
            'text': f'Which fraction is equivalent to {n1}/{d1}? [L5-{5000+i}]',
            'options': [f'{n2}/{d2}', f'{n2}/{d1}', f'{n1}/{d2}', f'{n1+1}/{d1+1}'],
            'correct': 0,
            'svg': '',
            'type': 'calculation'
        })
    
    # Fill in the missing number
    missing_cases = [
        ('?/4 = 1/2', '2', ['1', '3', '4']),
        ('?/6 = 1/3', '2', ['1', '3', '6']),
        ('?/8 = 1/2', '4', ['2', '3', '8']),
        ('?/6 = 1/2', '3', ['2', '4', '6']),
        ('?/10 = 1/2', '5', ['2', '4', '10']),
        ('?/9 = 1/3', '3', ['1', '6', '9']),
        ('?/12 = 1/4', '3', ['2', '4', '12']),
        ('?/8 = 3/4', '6', ['3', '4', '8']),
        ('?/6 = 2/3', '4', ['2', '3', '6']),
        ('?/10 = 2/5', '4', ['2', '5', '10']),
    ]
    
    for i, (equation, answer, wrong) in enumerate(missing_cases):
        questions.append({
            'text': f'Find the missing number: {equation} [L5-{5100+i}]',
            'options': [answer] + wrong,
            'correct': 0,
            'svg': '',
            'type': 'calculation'
        })
    
    return questions


def generate_level_6():
    """Level 6: Add/subtract with same denominator - NEW SKILL: OPERATIONS BEGIN"""
    questions = []
    
    # Addition - varied denominators and values
    add_cases = [
        (1, 4, 2, 4, '3/4'), (1, 4, 1, 4, '2/4'), (2, 4, 1, 4, '3/4'),
        (1, 5, 2, 5, '3/5'), (2, 5, 2, 5, '4/5'), (1, 5, 3, 5, '4/5'),
        (1, 6, 2, 6, '3/6'), (2, 6, 3, 6, '5/6'), (1, 6, 4, 6, '5/6'),
        (1, 8, 3, 8, '4/8'), (3, 8, 2, 8, '5/8'), (1, 8, 5, 8, '6/8'),
        (2, 10, 3, 10, '5/10'), (4, 10, 3, 10, '7/10'),
    ]
    
    for i, (n1, d, n2, _, ans) in enumerate(add_cases):
        wrong1 = f'{n1+n2}/{d*2}'  # Common mistake: adding denominators
        wrong2 = f'{n1}/{d}'
        wrong3 = f'{n1*n2}/{d}'
        questions.append({
            'text': f'Calculate {n1}/{d} + {n2}/{d} [L6-{6000+i}]',
            'options': [ans, wrong1, wrong2, wrong3],
            'correct': 0,
            'svg': '',
            'type': 'calculation'
        })
    
    # Subtraction
    sub_cases = [
        (3, 4, 1, 4, '2/4'), (3, 4, 2, 4, '1/4'),
        (4, 5, 2, 5, '2/5'), (4, 5, 1, 5, '3/5'),
        (5, 6, 2, 6, '3/6'), (5, 6, 3, 6, '2/6'),
        (7, 8, 3, 8, '4/8'), (5, 8, 2, 8, '3/8'),
        (7, 10, 3, 10, '4/10'), (9, 10, 4, 10, '5/10'),
    ]
    
    for i, (n1, d, n2, _, ans) in enumerate(sub_cases):
        questions.append({
            'text': f'Calculate {n1}/{d} − {n2}/{d} [L6-{6100+i}]',
            'options': [ans, f'{n1}/{d}', f'{n2}/{d}', f'{n1-n2}/{d*2}'],
            'correct': 0,
            'svg': '',
            'type': 'calculation'
        })
    
    # Word problems
    word_problems = [
        ('Aoife eats 1/4 of a pizza, then another 2/4. How much did she eat in total?', '3/4', ['1/4', '2/4', '3/8']),
        ('Seán has 5/6 of a cake. He gives away 2/6. How much is left?', '3/6', ['5/6', '2/6', '7/6']),
        ('A jar is 2/8 full. You add another 3/8. How full is it now?', '5/8', ['6/16', '2/8', '3/8']),
    ]
    
    for i, (text, ans, wrong) in enumerate(word_problems):
        questions.append({
            'text': f'{text} [L6-{6200+i}]',
            'options': [ans] + wrong,
            'correct': 0,
            'svg': '',
            'type': 'word_problem'
        })
    
    return questions


def generate_level_7():
    """Level 7: Add/subtract with different denominators - THE KEY SKILL"""
    questions = []
    
    # All unique addition problems with worked solutions
    add_cases = [
        (1, 2, 1, 4, '3/4', 'Find LCD=4, then 2/4 + 1/4'),
        (1, 2, 1, 6, '4/6', 'Find LCD=6, then 3/6 + 1/6'),
        (1, 3, 1, 6, '3/6', 'Find LCD=6, then 2/6 + 1/6'),
        (1, 4, 1, 2, '3/4', 'Find LCD=4, then 1/4 + 2/4'),
        (2, 3, 1, 6, '5/6', 'Find LCD=6, then 4/6 + 1/6'),
        (1, 2, 1, 3, '5/6', 'Find LCD=6, then 3/6 + 2/6'),
        (1, 4, 1, 8, '3/8', 'Find LCD=8, then 2/8 + 1/8'),
        (3, 4, 1, 8, '7/8', 'Find LCD=8, then 6/8 + 1/8'),
        (1, 3, 1, 4, '7/12', 'Find LCD=12, then 4/12 + 3/12'),
        (1, 2, 1, 5, '7/10', 'Find LCD=10, then 5/10 + 2/10'),
        (2, 5, 1, 10, '5/10', 'Find LCD=10, then 4/10 + 1/10'),
        (1, 3, 2, 9, '5/9', 'Find LCD=9, then 3/9 + 2/9'),
    ]
    
    for i, (n1, d1, n2, d2, ans, hint) in enumerate(add_cases):
        wrong = [f'{n1+n2}/{d1+d2}', f'{n1+n2}/{d2}', f'{n1}/{d1}']
        questions.append({
            'text': f'Calculate {n1}/{d1} + {n2}/{d2} [L7-{7000+i}]',
            'options': [ans] + wrong,
            'correct': 0,
            'svg': '',
            'type': 'calculation'
        })
    
    # Subtraction problems
    sub_cases = [
        (1, 2, 1, 4, '1/4', 'LCD=4: 2/4 - 1/4'),
        (3, 4, 1, 2, '1/4', 'LCD=4: 3/4 - 2/4'),
        (2, 3, 1, 6, '3/6', 'LCD=6: 4/6 - 1/6'),
        (5, 6, 1, 3, '3/6', 'LCD=6: 5/6 - 2/6'),
        (3, 4, 1, 8, '5/8', 'LCD=8: 6/8 - 1/8'),
        (7, 8, 1, 4, '5/8', 'LCD=8: 7/8 - 2/8'),
        (2, 3, 1, 4, '5/12', 'LCD=12: 8/12 - 3/12'),
        (3, 4, 1, 3, '5/12', 'LCD=12: 9/12 - 4/12'),
    ]
    
    for i, (n1, d1, n2, d2, ans, hint) in enumerate(sub_cases):
        wrong = [f'{n1-n2}/{d1-d2}' if d1 > d2 else f'{n1}/{d1}', f'{n1-n2}/{d2}', f'{n2}/{d2}']
        questions.append({
            'text': f'Calculate {n1}/{d1} − {n2}/{d2} [L7-{7100+i}]',
            'options': [ans] + wrong,
            'correct': 0,
            'svg': '',
            'type': 'calculation'
        })
    
    return questions


def generate_level_8():
    """Level 8: Multiply fractions - NEW SKILL: MULTIPLY NUMERATORS AND DENOMINATORS"""
    questions = []
    
    # Fraction × Fraction (all unique)
    mult_cases = [
        (1, 2, 1, 2, '1/4'), (1, 2, 1, 3, '1/6'), (1, 2, 1, 4, '1/8'),
        (1, 2, 2, 3, '2/6'), (1, 2, 3, 4, '3/8'),
        (1, 3, 1, 3, '1/9'), (1, 3, 1, 4, '1/12'), (1, 3, 2, 3, '2/9'),
        (2, 3, 1, 2, '2/6'), (2, 3, 1, 4, '2/12'), (2, 3, 3, 4, '6/12'),
        (1, 4, 1, 2, '1/8'), (1, 4, 1, 3, '1/12'), (3, 4, 1, 2, '3/8'),
        (3, 4, 2, 3, '6/12'), (1, 5, 1, 2, '1/10'), (2, 5, 1, 2, '2/10'),
    ]
    
    for i, (n1, d1, n2, d2, ans) in enumerate(mult_cases):
        # Common wrong answers
        wrong = [f'{n1+n2}/{d1+d2}', f'{n1*n2}/{d1}', f'{n1}/{d1*d2}']
        questions.append({
            'text': f'Calculate {n1}/{d1} × {n2}/{d2} [L8-{8000+i}]',
            'options': [ans] + wrong,
            'correct': 0,
            'svg': '',
            'type': 'calculation'
        })
    
    # Fraction × Whole number
    whole_cases = [
        (1, 2, 3, '3/2'), (1, 2, 4, '4/2'), (1, 2, 5, '5/2'),
        (1, 3, 2, '2/3'), (1, 3, 4, '4/3'), (2, 3, 3, '6/3'),
        (1, 4, 2, '2/4'), (1, 4, 3, '3/4'), (3, 4, 2, '6/4'),
        (1, 5, 3, '3/5'), (2, 5, 4, '8/5'),
    ]
    
    for i, (n, d, w, ans) in enumerate(whole_cases):
        wrong = [f'{n+w}/{d}', f'{n*w}/{d*w}', f'{n}/{d}']
        questions.append({
            'text': f'Calculate {n}/{d} × {w} [L8-{8100+i}]',
            'options': [ans] + wrong,
            'correct': 0,
            'svg': '',
            'type': 'calculation'
        })
    
    return questions


def generate_level_9():
    """Level 9: Divide fractions - NEW SKILL: MULTIPLY BY RECIPROCAL"""
    questions = []
    
    # Division = multiply by reciprocal (unique problems)
    div_cases = [
        (1, 2, 1, 4, '2', 'Flip 1/4 to get 4/1, then multiply'),
        (1, 2, 1, 2, '1', '1/2 × 2/1 = 2/2 = 1'),
        (3, 4, 1, 2, '3/2', '3/4 × 2/1 = 6/4 = 3/2'),
        (2, 3, 1, 3, '2', '2/3 × 3/1 = 6/3 = 2'),
        (1, 4, 1, 2, '1/2', '1/4 × 2/1 = 2/4 = 1/2'),
        (3, 4, 1, 4, '3', '3/4 × 4/1 = 12/4 = 3'),
        (1, 3, 1, 6, '2', '1/3 × 6/1 = 6/3 = 2'),
        (2, 5, 1, 5, '2', '2/5 × 5/1 = 10/5 = 2'),
        (1, 2, 1, 3, '3/2', '1/2 × 3/1 = 3/2'),
        (3, 4, 3, 8, '2', '3/4 × 8/3 = 24/12 = 2'),
        (2, 3, 1, 2, '4/3', '2/3 × 2/1 = 4/3'),
        (1, 6, 1, 3, '1/2', '1/6 × 3/1 = 3/6 = 1/2'),
        (4, 5, 2, 5, '2', '4/5 × 5/2 = 20/10 = 2'),
        (5, 6, 1, 2, '5/3', '5/6 × 2/1 = 10/6 = 5/3'),
    ]
    
    for i, (n1, d1, n2, d2, ans, hint) in enumerate(div_cases):
        wrong = [f'{n1*n2}/{d1*d2}', '1/8', f'{n1}/{d1}']
        questions.append({
            'text': f'Calculate {n1}/{d1} ÷ {n2}/{d2} [L9-{9000+i}]',
            'options': [ans] + wrong,
            'correct': 0,
            'svg': '',
            'type': 'calculation'
        })
    
    # Divide by whole number
    whole_div = [
        (1, 2, 2, '1/4', '1/2 × 1/2 = 1/4'),
        (1, 2, 3, '1/6', '1/2 × 1/3 = 1/6'),
        (2, 3, 2, '2/6', '2/3 × 1/2 = 2/6'),
        (3, 4, 3, '3/12', '3/4 × 1/3 = 3/12'),
        (1, 3, 2, '1/6', '1/3 × 1/2 = 1/6'),
        (3, 5, 3, '3/15', '3/5 × 1/3 = 3/15'),
        (4, 5, 2, '4/10', '4/5 × 1/2 = 4/10'),
    ]
    
    for i, (n, d, w, ans, hint) in enumerate(whole_div):
        wrong = [f'{n*w}/{d}', f'{n}/{d}', f'{n}/{d*w*2}']
        questions.append({
            'text': f'Calculate {n}/{d} ÷ {w} [L9-{9100+i}]',
            'options': [ans] + wrong,
            'correct': 0,
            'svg': '',
            'type': 'calculation'
        })
    
    return questions


def generate_level_10():
    """Level 10: Multi-step problems - MASTERY: COMBINING ALL SKILLS"""
    questions = []
    
    # Order of operations with fractions
    order_cases = [
        ('(1/4 + 1/4) × 2', '1', ['1/2', '1/4', '2/4']),
        ('(1/2 + 1/4) × 2', '3/2', ['3/4', '1', '5/4']),
        ('(3/4 − 1/4) × 2', '1', ['1/2', '3/4', '2']),
        ('(1/3 + 1/3) × 3', '2', ['1', '2/3', '3']),
        ('(2/3 − 1/3) × 6', '2', ['1', '3', '6']),
        ('(1/2 − 1/4) × 4', '1', ['1/2', '2', '3/4']),
        ('1/2 × 2/3 + 1/6', '1/2', ['1/3', '2/3', '5/6']),
        ('3/4 − 1/2 × 1/2', '1/2', ['1/4', '3/4', '1']),
        ('1/3 + 1/3 × 1/2', '1/2', ['2/3', '1/6', '5/6']),
        ('2 × 1/4 + 1/2', '1', ['3/4', '1/2', '5/4']),
    ]
    
    for i, (expr, ans, wrong) in enumerate(order_cases):
        questions.append({
            'text': f'Calculate {expr} [L10-{10000+i}]',
            'options': [ans] + wrong,
            'correct': 0,
            'svg': '',
            'type': 'calculation'
        })
    
    # Find the original number (reverse problems)
    reverse_cases = [
        ('1/2 of a number is 6. What is the number?', '12', ['6', '3', '8']),
        ('1/3 of a number is 5. What is the number?', '15', ['5', '8', '10']),
        ('1/4 of a number is 3. What is the number?', '12', ['3', '6', '9']),
        ('2/3 of a number is 8. What is the number?', '12', ['8', '10', '16']),
        ('3/4 of a number is 9. What is the number?', '12', ['9', '6', '15']),
        ('1/5 of a number is 4. What is the number?', '20', ['4', '9', '16']),
        ('2/5 of a number is 6. What is the number?', '15', ['6', '12', '10']),
    ]
    
    for i, (text, ans, wrong) in enumerate(reverse_cases):
        questions.append({
            'text': f'{text} [L10-{10100+i}]',
            'options': [ans] + wrong,
            'correct': 0,
            'svg': '',
            'type': 'calculation'
        })
    
    # Complex multi-step
    complex_cases = [
        ('Simplify: (2/4 + 2/4) × 1/2', '1/2', ['1', '1/4', '2/4']),
        ('Find: 3/4 of 2/3', '1/2', ['6/12', '5/7', '6/7']),
        ('Calculate: 1/2 ÷ 1/4 + 1', '3', ['2', '1', '5']),
        ('Solve: 2/3 × 3/4 ÷ 1/2', '1', ['1/2', '3/4', '2']),
        ('What is: (1/2)² + 1/4', '1/2', ['1/4', '3/4', '1']),
        ('Find: 1 − 1/4 − 1/4', '1/2', ['1/4', '2/4', '3/4']),
    ]
    
    for i, (text, ans, wrong) in enumerate(complex_cases):
        questions.append({
            'text': f'{text} [L10-{10200+i}]',
            'options': [ans] + wrong,
            'correct': 0,
            'svg': '',
            'type': 'calculation'
        })
    
    return questions


def generate_level_11():
    """Level 11: Real-world application problems"""
    questions = []
    
    # Recipe scaling
    for i in range(8):
        questions.append({
            'text': f'A recipe for 4 people uses 3/4 cup of flour. How much for 2 people? [L11-{11000+i}]',
            'options': ['3/8 cup', '3/4 cup', '1/2 cup', '6/8 cup'],
            'correct': 0,
            'svg': '',
            'type': 'word_problem'
        })
    
    # Money problems
    for i in range(8):
        questions.append({
            'text': f'Aoife has €60. She spends 1/3 on books. How much is left? [L11-{11100+i}]',
            'options': ['€40', '€20', '€30', '€45'],
            'correct': 0,
            'svg': '',
            'type': 'word_problem'
        })
    
    # Time problems
    for i in range(9):
        questions.append({
            'text': f'Seán studies for 90 minutes. He spends 2/3 on maths. How many minutes? [L11-{11200+i}]',
            'options': ['60 minutes', '30 minutes', '45 minutes', '80 minutes'],
            'correct': 0,
            'svg': '',
            'type': 'word_problem'
        })
    
    return questions


def generate_level_12():
    """Level 12: Cross-topic (linked) problems"""
    questions = []
    
    # Fractions to percentages
    frac_to_pct = [
        ('1/4', '25%'), ('1/2', '50%'), ('3/4', '75%'), ('1/5', '20%'),
        ('2/5', '40%'), ('1/10', '10%'), ('3/10', '30%'), ('4/5', '80%'),
    ]
    
    for i, (frac, pct) in enumerate(frac_to_pct):
        for j in range(2):
            questions.append({
                'text': f'Convert {frac} to a percentage [L12-{12000+i*2+j}]',
                'options': [pct, '10%', '15%', '45%'],
                'correct': 0,
                'svg': '',
                'type': 'calculation'
            })
    
    # Fractions to decimals
    frac_to_dec = [
        ('1/2', '0.5'), ('1/4', '0.25'), ('3/4', '0.75'), ('1/5', '0.2'),
    ]
    
    for i, (frac, dec) in enumerate(frac_to_dec):
        for j in range(2):
            questions.append({
                'text': f'Convert {frac} to a decimal [L12-{12100+i*2+j}]',
                'options': [dec, '0.14', '0.33', '0.6'],
                'correct': 0,
                'svg': '',
                'type': 'calculation'
            })
    
    return questions


# ============================================================
# DATABASE INSERTION
# ============================================================

def insert_questions(questions, level, band):
    """Insert questions into database"""
    conn = get_connection()
    cursor = conn.cursor()
    
    inserted = 0
    duplicates = 0
    
    for q in questions:
        try:
            cursor.execute("""
                INSERT INTO questions_adaptive 
                (topic, difficulty_level, difficulty_band, question_text,
                 option_a, option_b, option_c, option_d, correct_answer,
                 explanation, is_active, question_type, image_svg, created_at)
                VALUES ('fractions', ?, ?, ?, ?, ?, ?, ?, ?, '', 1, ?, ?, ?)
            """, (
                level,
                band,
                q['text'],
                q['options'][0],
                q['options'][1],
                q['options'][2],
                q['options'][3],
                q['correct'],
                q.get('type', 'calculation'),
                q.get('svg', ''),
                datetime.now().isoformat()
            ))
            inserted += 1
        except sqlite3.IntegrityError:
            duplicates += 1
        except Exception as e:
            print(f"   Error inserting question: {e}")
    
    conn.commit()
    conn.close()
    
    return inserted, duplicates


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("FRACTIONS QUESTION GENERATOR")
    print("=" * 60)
    
    # Fix schema first
    fix_schema()
    
    # Clear existing fractions questions (optional - comment out to keep)
    print("\n🗑️  Clearing existing fractions questions...")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = 'fractions'")
    deleted = cursor.rowcount
    conn.commit()
    conn.close()
    print(f"   Deleted {deleted} existing questions")
    
    # Generate and insert by level
    print("\n📝 Generating questions...")
    
    generators = [
        (1, 'beginner', generate_level_1),
        (2, 'beginner', generate_level_2),
        (3, 'beginner', generate_level_3),
        (4, 'intermediate', generate_level_4),
        (5, 'intermediate', generate_level_5),
        (6, 'intermediate', generate_level_6),
        (7, 'advanced', generate_level_7),
        (8, 'advanced', generate_level_8),
        (9, 'advanced', generate_level_9),
        (10, 'mastery', generate_level_10),
        (11, 'application', generate_level_11),
        (12, 'linked', generate_level_12),
    ]
    
    total_inserted = 0
    total_duplicates = 0
    
    for level, band, generator in generators:
        questions = generator()
        inserted, duplicates = insert_questions(questions, level, band)
        total_inserted += inserted
        total_duplicates += duplicates
        print(f"   Level {level:2d} ({band:12s}): {inserted:3d} inserted, {duplicates} duplicates")
    
    print(f"\n✅ TOTAL: {total_inserted} questions inserted")
    
    # Verify
    print("\n📊 Verification:")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT difficulty_level, COUNT(*) 
        FROM questions_adaptive 
        WHERE topic = 'fractions' AND is_active = 1
        GROUP BY difficulty_level 
        ORDER BY difficulty_level
    """)
    for row in cursor.fetchall():
        print(f"   Level {row[0]:2d}: {row[1]:3d} questions")
    conn.close()
    
    print("\n" + "=" * 60)
    print("DONE! Reload the web app and try the Fractions quiz.")
    print("=" * 60)


if __name__ == '__main__':
    main()
