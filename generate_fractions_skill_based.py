#!/usr/bin/env python3
"""
FRACTIONS: Skill-Based Question Generator
==========================================
Each level introduces a NEW SKILL, creating clear progression.

SKILL LADDER:
  Level 1:  IDENTIFY - Recognize halves (1/2 only)
  Level 2:  IDENTIFY - Quarters and thirds  
  Level 3:  IDENTIFY - Any unit fraction up to 1/10
  Level 4:  SIMPLIFY - Reduce fractions to lowest terms
  Level 5:  EQUIVALENT - Find equivalent fractions
  Level 6:  ADD/SUBTRACT - Same denominator
  Level 7:  ADD/SUBTRACT - Different denominators
  Level 8:  MULTIPLY - Fraction × Fraction
  Level 9:  DIVIDE - Fraction ÷ Fraction
  Level 10: MULTI-STEP - Combined operations
  Level 11: APPLICATION - Real-world word problems
  Level 12: LINKED - Cross-topic (%, decimals, probability)

Visual Target: 75% for L1-10, 50% for L11-12
"""

import sqlite3
import random
import math
import os
from datetime import datetime
from math import gcd

# Database auto-detection
POSSIBLE_PATHS = ['mathapp.db', 'instance/mathquiz.db', 'mathquiz.db']
DB_PATH = None

def find_db():
    for path in POSSIBLE_PATHS:
        if os.path.exists(path):
            return path
    print("ERROR: Database not found!")
    exit(1)

def get_db():
    global DB_PATH
    if DB_PATH is None:
        DB_PATH = find_db()
        print(f"Using database: {DB_PATH}")
    return sqlite3.connect(DB_PATH)


# ============================================================
# SKILL DEFINITIONS - What each level teaches
# ============================================================

SKILL_DESCRIPTIONS = {
    1: "Identify halves - recognize when something is split in two equal parts",
    2: "Identify quarters and thirds - recognize 1/4, 2/4, 3/4, 1/3, 2/3",
    3: "Identify any fraction - read fractions up to tenths",
    4: "Simplify fractions - reduce to lowest terms (e.g., 4/8 = 1/2)",
    5: "Equivalent fractions - find fractions with same value",
    6: "Add/subtract fractions - same denominator only",
    7: "Add/subtract fractions - different denominators",
    8: "Multiply fractions - fraction × fraction and fraction × whole",
    9: "Divide fractions - using reciprocal method",
    10: "Multi-step problems - combine multiple operations",
    11: "Real-world application - word problems in context",
    12: "Cross-topic links - fractions with %, decimals, probability"
}


# ============================================================
# SVG GENERATORS
# ============================================================

def svg_pie_chart(numerator, denominator, size=160, label=None):
    """Generate pie chart SVG"""
    cx, cy, r = size//2, size//2, size//2 - 15
    
    if numerator == 0:
        return f'''<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">
            <circle cx="{cx}" cy="{cy}" r="{r}" fill="#E8F5E9" stroke="#333" stroke-width="2"/>
            <text x="{cx}" y="{size-5}" text-anchor="middle" font-size="11" fill="#666">{label or ''}</text>
        </svg>'''
    
    if numerator == denominator:
        return f'''<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">
            <circle cx="{cx}" cy="{cy}" r="{r}" fill="#4CAF50" stroke="#333" stroke-width="2"/>
            <text x="{cx}" y="{size-5}" text-anchor="middle" font-size="11" fill="#666">{label or ''}</text>
        </svg>'''
    
    slices = []
    angle_per_slice = 360 / denominator
    
    for i in range(denominator):
        start_angle = i * angle_per_slice - 90
        end_angle = (i + 1) * angle_per_slice - 90
        
        start_rad = math.radians(start_angle)
        end_rad = math.radians(end_angle)
        
        x1 = cx + r * math.cos(start_rad)
        y1 = cy + r * math.sin(start_rad)
        x2 = cx + r * math.cos(end_rad)
        y2 = cy + r * math.sin(end_rad)
        
        large_arc = 1 if angle_per_slice > 180 else 0
        color = '#4CAF50' if i < numerator else '#E8F5E9'
        
        path = f'M{cx},{cy} L{x1:.1f},{y1:.1f} A{r},{r} 0 {large_arc},1 {x2:.1f},{y2:.1f} Z'
        slices.append(f'<path d="{path}" fill="{color}" stroke="#333" stroke-width="1"/>')
    
    return f'''<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">
        {''.join(slices)}
        <text x="{cx}" y="{size-3}" text-anchor="middle" font-size="11" fill="#666">{label or ''}</text>
    </svg>'''


def svg_fraction_bar(numerator, denominator, width=220, height=50):
    """Generate fraction bar SVG"""
    bar_height = 35
    segment_width = (width - 20) / denominator
    
    segments = []
    for i in range(denominator):
        color = '#4CAF50' if i < numerator else '#E8F5E9'
        x = 10 + i * segment_width
        segments.append(f'<rect x="{x:.1f}" y="8" width="{segment_width:.1f}" height="{bar_height}" fill="{color}" stroke="#333" stroke-width="1"/>')
    
    return f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
        {''.join(segments)}
    </svg>'''


def svg_fraction_operation(num1, denom1, num2, denom2, operator):
    """Generate visual for fraction operation"""
    width = 320
    height = 80
    
    return f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
        <!-- First fraction -->
        <rect x="20" y="15" width="60" height="50" rx="5" fill="#E3F2FD" stroke="#1976D2" stroke-width="2"/>
        <text x="50" y="35" text-anchor="middle" font-size="18" font-weight="bold" fill="#1565C0">{num1}</text>
        <line x1="30" y1="42" x2="70" y2="42" stroke="#1565C0" stroke-width="2"/>
        <text x="50" y="60" text-anchor="middle" font-size="18" font-weight="bold" fill="#1565C0">{denom1}</text>
        
        <!-- Operator -->
        <text x="110" y="48" text-anchor="middle" font-size="24" font-weight="bold" fill="#333">{operator}</text>
        
        <!-- Second fraction -->
        <rect x="140" y="15" width="60" height="50" rx="5" fill="#FFF3E0" stroke="#F57C00" stroke-width="2"/>
        <text x="170" y="35" text-anchor="middle" font-size="18" font-weight="bold" fill="#EF6C00">{num2}</text>
        <line x1="150" y1="42" x2="190" y2="42" stroke="#EF6C00" stroke-width="2"/>
        <text x="170" y="60" text-anchor="middle" font-size="18" font-weight="bold" fill="#EF6C00">{denom2}</text>
        
        <!-- Equals -->
        <text x="230" y="48" text-anchor="middle" font-size="24" font-weight="bold" fill="#333">=</text>
        
        <!-- Answer box -->
        <rect x="260" y="15" width="50" height="50" rx="5" fill="#E8F5E9" stroke="#4CAF50" stroke-width="2"/>
        <text x="285" y="48" text-anchor="middle" font-size="20" font-weight="bold" fill="#2E7D32">?</text>
    </svg>'''


def svg_simplify(num, denom):
    """Generate visual for simplification"""
    return f'''<svg viewBox="0 0 280 70" xmlns="http://www.w3.org/2000/svg">
        <!-- Original fraction -->
        <rect x="20" y="10" width="70" height="50" rx="5" fill="#FFEBEE" stroke="#E53935" stroke-width="2"/>
        <text x="55" y="30" text-anchor="middle" font-size="18" font-weight="bold" fill="#C62828">{num}</text>
        <line x1="30" y1="37" x2="80" y2="37" stroke="#C62828" stroke-width="2"/>
        <text x="55" y="55" text-anchor="middle" font-size="18" font-weight="bold" fill="#C62828">{denom}</text>
        
        <!-- Arrow -->
        <text x="120" y="42" text-anchor="middle" font-size="18" fill="#666">→ simplify →</text>
        
        <!-- Answer box -->
        <rect x="190" y="10" width="70" height="50" rx="5" fill="#E8F5E9" stroke="#4CAF50" stroke-width="2"/>
        <text x="225" y="42" text-anchor="middle" font-size="20" font-weight="bold" fill="#2E7D32">?</text>
    </svg>'''


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def simplify_fraction(num, denom):
    """Return simplified fraction as tuple"""
    g = gcd(num, denom)
    return num // g, denom // g


def make_unique_options(correct, distractors, count=4):
    """Ensure exactly count unique options"""
    options = [str(correct)]
    
    for d in distractors:
        d_str = str(d)
        if d_str not in options:
            options.append(d_str)
        if len(options) >= count:
            break
    
    # Generate more if needed
    attempts = 0
    while len(options) < count and attempts < 100:
        attempts += 1
        if '/' in str(correct):
            n, d = random.randint(1, 10), random.randint(2, 12)
            new_opt = f"{n}/{d}"
        else:
            try:
                base = int(str(correct).split()[0])
                new_opt = str(base + random.choice([-3, -2, -1, 1, 2, 3]))
            except:
                new_opt = str(random.randint(1, 20))
        if new_opt not in options and new_opt != str(correct):
            options.append(new_opt)
    
    return options[:count]


def fraction_distractors(correct_num, correct_denom):
    """Generate plausible wrong answers for a fraction"""
    correct = f"{correct_num}/{correct_denom}"
    distractors = []
    
    # Inverted
    if correct_num != correct_denom:
        distractors.append(f"{correct_denom}/{correct_num}")
    
    # Off by one
    if correct_num > 1:
        distractors.append(f"{correct_num - 1}/{correct_denom}")
    distractors.append(f"{correct_num + 1}/{correct_denom}")
    
    # Different denominator
    distractors.append(f"{correct_num}/{correct_denom + 1}")
    if correct_denom > 2:
        distractors.append(f"{correct_num}/{correct_denom - 1}")
    
    # Unsimplified/differently simplified
    distractors.append(f"{correct_num * 2}/{correct_denom * 2}")
    
    # Filter out correct and invalid
    distractors = [d for d in distractors if d != correct]
    return distractors


# ============================================================
# LEVEL 1: IDENTIFY HALVES
# ============================================================

def generate_level_1():
    """Level 1: Identify halves only - the simplest fraction concept"""
    questions = []
    
    # Type 1: Is this shape showing one half? (pie charts)
    for _ in range(20):
        num = random.choice([1, 1, 1, 0, 2])  # Mostly 1/2, sometimes 0 or 2
        svg = svg_pie_chart(num, 2, label="Circle")
        
        if num == 1:
            correct = "Yes, this shows 1/2"
            q_text = "Does the shaded part show one half (1/2)?"
        elif num == 0:
            correct = "No, nothing is shaded"
            q_text = "Does the shaded part show one half (1/2)?"
        else:
            correct = "No, this shows the whole circle"
            q_text = "Does the shaded part show one half (1/2)?"
        
        options = ["Yes, this shows 1/2", "No, nothing is shaded", "No, this shows the whole circle", "No, this shows 1/4"]
        
        questions.append({
            'level': 1, 'band': 'beginner', 'type': 'visual',
            'question': f'{q_text} [L1-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    # Type 2: Which shape shows 1/2? (choose from multiple)
    for _ in range(15):
        svg = svg_pie_chart(1, 2, label="Which is 1/2?")
        correct = "1/2"
        options = make_unique_options(correct, ["1/4", "1/3", "2/2", "0/2"], 4)
        random.shuffle(options)
        
        questions.append({
            'level': 1, 'band': 'beginner', 'type': 'visual',
            'question': f'The circle is cut in half. One half is shaded. Write this as a fraction: [L1-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    # Type 3: Fraction bar halves
    for _ in range(15):
        svg = svg_fraction_bar(1, 2)
        correct = "1/2"
        options = make_unique_options(correct, ["1/4", "2/4", "1/3"], 4)
        random.shuffle(options)
        
        questions.append({
            'level': 1, 'band': 'beginner', 'type': 'visual',
            'question': f'What fraction of the bar is green? [L1-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    return questions


# ============================================================
# LEVEL 2: QUARTERS AND THIRDS
# ============================================================

def generate_level_2():
    """Level 2: Identify quarters and thirds"""
    questions = []
    
    # Quarters
    for num in [1, 2, 3]:
        for _ in range(5):
            svg = svg_pie_chart(num, 4, label="Quarters")
            correct = f"{num}/4"
            options = make_unique_options(correct, fraction_distractors(num, 4), 4)
            random.shuffle(options)
            
            questions.append({
                'level': 2, 'band': 'beginner', 'type': 'visual',
                'question': f'This circle is cut into 4 equal parts (quarters). What fraction is shaded? [L2-{random.randint(1000,9999)}]',
                'options': options, 'correct': options.index(correct), 'svg': svg
            })
    
    # Thirds
    for num in [1, 2]:
        for _ in range(5):
            svg = svg_pie_chart(num, 3, label="Thirds")
            correct = f"{num}/3"
            options = make_unique_options(correct, fraction_distractors(num, 3), 4)
            random.shuffle(options)
            
            questions.append({
                'level': 2, 'band': 'beginner', 'type': 'visual',
                'question': f'This circle is cut into 3 equal parts (thirds). What fraction is shaded? [L2-{random.randint(1000,9999)}]',
                'options': options, 'correct': options.index(correct), 'svg': svg
            })
    
    # Fraction bars
    for denom, name in [(3, "thirds"), (4, "quarters")]:
        for num in range(1, denom):
            for _ in range(3):
                svg = svg_fraction_bar(num, denom)
                correct = f"{num}/{denom}"
                options = make_unique_options(correct, fraction_distractors(num, denom), 4)
                random.shuffle(options)
                
                questions.append({
                    'level': 2, 'band': 'beginner', 'type': 'visual',
                    'question': f'The bar is divided into {name}. What fraction is green? [L2-{random.randint(1000,9999)}]',
                    'options': options, 'correct': options.index(correct), 'svg': svg
                })
    
    return questions


# ============================================================
# LEVEL 3: ANY FRACTION UP TO TENTHS
# ============================================================

def generate_level_3():
    """Level 3: Identify any fraction with denominators 2-10"""
    questions = []
    
    for denom in [5, 6, 8, 10]:
        for _ in range(6):
            num = random.randint(1, denom - 1)
            svg = svg_pie_chart(num, denom)
            correct = f"{num}/{denom}"
            options = make_unique_options(correct, fraction_distractors(num, denom), 4)
            random.shuffle(options)
            
            questions.append({
                'level': 3, 'band': 'beginner', 'type': 'visual',
                'question': f'What fraction of the circle is shaded? [L3-{random.randint(1000,9999)}]',
                'options': options, 'correct': options.index(correct), 'svg': svg
            })
    
    # Fraction bars
    for denom in [5, 6, 8, 10]:
        for _ in range(4):
            num = random.randint(1, denom - 1)
            svg = svg_fraction_bar(num, denom)
            correct = f"{num}/{denom}"
            options = make_unique_options(correct, fraction_distractors(num, denom), 4)
            random.shuffle(options)
            
            questions.append({
                'level': 3, 'band': 'beginner', 'type': 'visual',
                'question': f'What fraction of the bar is green? [L3-{random.randint(1000,9999)}]',
                'options': options, 'correct': options.index(correct), 'svg': svg
            })
    
    return questions


# ============================================================
# LEVEL 4: SIMPLIFY FRACTIONS
# ============================================================

def generate_level_4():
    """Level 4: Reduce fractions to lowest terms"""
    questions = []
    
    # Clear simplification cases
    simplify_cases = [
        (2, 4, 1, 2), (2, 6, 1, 3), (3, 6, 1, 2), (4, 8, 1, 2),
        (3, 9, 1, 3), (4, 12, 1, 3), (6, 8, 3, 4), (4, 6, 2, 3),
        (2, 8, 1, 4), (5, 10, 1, 2), (6, 9, 2, 3), (4, 10, 2, 5),
        (6, 12, 1, 2), (8, 12, 2, 3), (9, 12, 3, 4), (3, 12, 1, 4)
    ]
    
    for orig_num, orig_denom, simp_num, simp_denom in simplify_cases:
        svg = svg_simplify(orig_num, orig_denom)
        correct = f"{simp_num}/{simp_denom}"
        
        # Distractors: unsimplified, partially simplified, wrong
        distractors = [
            f"{orig_num}/{orig_denom}",  # Unchanged
            f"{simp_num}/{orig_denom}",  # Wrong
            f"{orig_num}/{simp_denom}",  # Wrong
            f"{simp_denom}/{simp_num}" if simp_num != simp_denom else f"{simp_num+1}/{simp_denom}"  # Inverted
        ]
        
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 4, 'band': 'intermediate', 'type': 'visual',
            'question': f'Simplify {orig_num}/{orig_denom} to its lowest terms: [L4-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    # Text-only simplification
    for _ in range(15):
        multiplier = random.randint(2, 4)
        simp_num = random.randint(1, 4)
        simp_denom = random.choice([2, 3, 4, 5])
        if simp_num >= simp_denom:
            simp_num = simp_denom - 1
        
        orig_num = simp_num * multiplier
        orig_denom = simp_denom * multiplier
        
        correct = f"{simp_num}/{simp_denom}"
        distractors = [f"{orig_num}/{orig_denom}", f"{simp_num}/{orig_denom}", f"{orig_num}/{simp_denom}"]
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 4, 'band': 'intermediate', 'type': 'calculation',
            'question': f'Write {orig_num}/{orig_denom} in its simplest form: [L4-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    return questions


# ============================================================
# LEVEL 5: EQUIVALENT FRACTIONS
# ============================================================

def generate_level_5():
    """Level 5: Find equivalent fractions"""
    questions = []
    
    # Find the equivalent
    for _ in range(25):
        base_num = random.randint(1, 3)
        base_denom = random.choice([2, 3, 4, 5])
        if base_num >= base_denom:
            base_num = base_denom - 1
        
        multiplier = random.randint(2, 4)
        eq_num = base_num * multiplier
        eq_denom = base_denom * multiplier
        
        correct = f"{eq_num}/{eq_denom}"
        
        # Wrong answers: different multipliers
        distractors = [
            f"{eq_num}/{base_denom}",  # Only multiplied numerator
            f"{base_num}/{eq_denom}",  # Only multiplied denominator
            f"{eq_num + 1}/{eq_denom}",
            f"{base_num * (multiplier + 1)}/{base_denom * multiplier}"  # Mismatched
        ]
        
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 5, 'band': 'intermediate', 'type': 'calculation',
            'question': f'Which fraction is equivalent to {base_num}/{base_denom}? [L5-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    # Fill in the blank: ?/12 = 1/4
    for _ in range(15):
        base_num = random.randint(1, 3)
        base_denom = random.choice([2, 3, 4])
        multiplier = random.choice([2, 3, 4])
        
        new_denom = base_denom * multiplier
        new_num = base_num * multiplier
        
        correct = str(new_num)
        distractors = [str(new_num + 1), str(new_num - 1) if new_num > 1 else "1", str(base_num), str(new_denom)]
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 5, 'band': 'intermediate', 'type': 'calculation',
            'question': f'Find the missing number: ?/{new_denom} = {base_num}/{base_denom} [L5-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    return questions


# ============================================================
# LEVEL 6: ADD/SUBTRACT - SAME DENOMINATOR
# ============================================================

def generate_level_6():
    """Level 6: Add and subtract fractions with same denominator"""
    questions = []
    
    # Addition
    for _ in range(20):
        denom = random.choice([4, 5, 6, 8])
        num1 = random.randint(1, denom // 2)
        num2 = random.randint(1, denom // 2)
        result_num = num1 + num2
        
        simp_num, simp_denom = simplify_fraction(result_num, denom)
        
        if simp_denom == 1:
            correct = str(simp_num)
        else:
            correct = f"{simp_num}/{simp_denom}"
        
        svg = svg_fraction_operation(num1, denom, num2, denom, '+')
        
        distractors = [
            f"{num1 + num2}/{denom * 2}",  # Added denominators
            f"{num1}/{denom}",  # Forgot to add
            f"{result_num}/{denom}"  # Unsimplified
        ]
        
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 6, 'band': 'intermediate', 'type': 'visual',
            'question': f'Calculate {num1}/{denom} + {num2}/{denom} (simplify if possible): [L6-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    # Subtraction
    for _ in range(15):
        denom = random.choice([4, 5, 6, 8])
        num1 = random.randint(denom // 2 + 1, denom - 1)
        num2 = random.randint(1, num1 - 1)
        result_num = num1 - num2
        
        simp_num, simp_denom = simplify_fraction(result_num, denom)
        correct = f"{simp_num}/{simp_denom}"
        
        svg = svg_fraction_operation(num1, denom, num2, denom, '−')
        
        distractors = [f"{result_num}/{denom}", f"{num1}/{denom}", f"{num2}/{denom}"]
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 6, 'band': 'intermediate', 'type': 'visual',
            'question': f'Calculate {num1}/{denom} − {num2}/{denom}: [L6-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    return questions


# ============================================================
# LEVEL 7: ADD/SUBTRACT - DIFFERENT DENOMINATORS
# ============================================================

def generate_level_7():
    """Level 7: Add and subtract with different denominators"""
    questions = []
    
    # Related denominators (one is multiple of other)
    pairs = [(2, 4), (2, 6), (3, 6), (4, 8), (3, 9), (5, 10), (2, 8), (4, 12)]
    
    for _ in range(20):
        d1, d2 = random.choice(pairs)
        num1 = random.randint(1, d1 - 1)
        num2 = random.randint(1, d2 // 2)
        
        # Convert to common denominator
        common_d = d2
        new_num1 = num1 * (d2 // d1)
        result_num = new_num1 + num2
        
        simp_num, simp_denom = simplify_fraction(result_num, common_d)
        
        if simp_denom == 1:
            correct = str(simp_num)
        else:
            correct = f"{simp_num}/{simp_denom}"
        
        svg = svg_fraction_operation(num1, d1, num2, d2, '+')
        
        distractors = [
            f"{num1 + num2}/{d1 + d2}",  # Added both nums and denoms
            f"{num1 + num2}/{d2}",  # Didn't convert first fraction
            f"{result_num}/{common_d}"  # Unsimplified
        ]
        
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 7, 'band': 'advanced', 'type': 'visual',
            'question': f'Calculate {num1}/{d1} + {num2}/{d2} (simplify your answer): [L7-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    # Subtraction with different denominators
    for _ in range(15):
        d1, d2 = random.choice(pairs)
        # Ensure subtraction gives positive result
        num1 = random.randint(d1 // 2 + 1, d1 - 1) if d1 > 2 else 1
        num2 = random.randint(1, d2 // 3) if d2 > 3 else 1
        
        common_d = d2
        new_num1 = num1 * (d2 // d1)
        if new_num1 <= num2:
            new_num1, num2 = num2 + 1, 1
        result_num = new_num1 - num2
        
        simp_num, simp_denom = simplify_fraction(result_num, common_d)
        correct = f"{simp_num}/{simp_denom}"
        
        svg = svg_fraction_operation(num1, d1, num2, d2, '−')
        
        distractors = [f"{num1 - num2}/{d1}", f"{result_num}/{common_d}", f"{new_num1}/{common_d}"]
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 7, 'band': 'advanced', 'type': 'visual',
            'question': f'Calculate {num1}/{d1} − {num2}/{d2}: [L7-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    return questions


# ============================================================
# LEVEL 8: MULTIPLY FRACTIONS
# ============================================================

def generate_level_8():
    """Level 8: Multiply fractions"""
    questions = []
    
    # Fraction × Fraction
    for _ in range(20):
        num1 = random.randint(1, 4)
        denom1 = random.choice([2, 3, 4, 5])
        num2 = random.randint(1, 3)
        denom2 = random.choice([2, 3, 4])
        
        if num1 >= denom1:
            num1 = denom1 - 1
        if num2 >= denom2:
            num2 = denom2 - 1
        
        result_num = num1 * num2
        result_denom = denom1 * denom2
        
        simp_num, simp_denom = simplify_fraction(result_num, result_denom)
        
        if simp_denom == 1:
            correct = str(simp_num)
        else:
            correct = f"{simp_num}/{simp_denom}"
        
        svg = svg_fraction_operation(num1, denom1, num2, denom2, '×')
        
        distractors = [
            f"{num1 * num2}/{denom1 + denom2}",  # Added denoms
            f"{num1 + num2}/{denom1 * denom2}",  # Added nums
            f"{result_num}/{result_denom}"  # Unsimplified
        ]
        
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 8, 'band': 'advanced', 'type': 'visual',
            'question': f'Calculate {num1}/{denom1} × {num2}/{denom2}: [L8-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    # Fraction × Whole number
    for _ in range(15):
        num = random.randint(1, 3)
        denom = random.choice([2, 3, 4, 5])
        whole = random.randint(2, 5)
        
        result_num = num * whole
        simp_num, simp_denom = simplify_fraction(result_num, denom)
        
        if simp_num >= simp_denom:
            whole_part = simp_num // simp_denom
            remainder = simp_num % simp_denom
            if remainder == 0:
                correct = str(whole_part)
            else:
                correct = f"{whole_part} {remainder}/{simp_denom}"
        else:
            correct = f"{simp_num}/{simp_denom}"
        
        distractors = [
            f"{num * whole}/{denom}",
            f"{num + whole}/{denom}",
            str(num * whole)
        ]
        
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 8, 'band': 'advanced', 'type': 'calculation',
            'question': f'Calculate {num}/{denom} × {whole}: [L8-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    return questions


# ============================================================
# LEVEL 9: DIVIDE FRACTIONS
# ============================================================

def generate_level_9():
    """Level 9: Divide fractions using reciprocal method"""
    questions = []
    
    for _ in range(25):
        num1 = random.randint(1, 4)
        denom1 = random.choice([2, 3, 4, 5])
        num2 = random.randint(1, 3)
        denom2 = random.choice([2, 3, 4])
        
        if num1 >= denom1:
            num1 = denom1 - 1
        if num2 >= denom2:
            num2 = denom2 - 1
        
        # Divide = multiply by reciprocal
        result_num = num1 * denom2
        result_denom = denom1 * num2
        
        simp_num, simp_denom = simplify_fraction(result_num, result_denom)
        
        if simp_denom == 1:
            correct = str(simp_num)
        else:
            correct = f"{simp_num}/{simp_denom}"
        
        svg = svg_fraction_operation(num1, denom1, num2, denom2, '÷')
        
        distractors = [
            f"{num1 * num2}/{denom1 * denom2}",  # Multiplied instead
            f"{result_denom}/{result_num}" if result_denom != result_num else f"{simp_num + 1}/{simp_denom}",  # Inverted
            f"{num1 * denom2}/{denom1}"  # Partial calculation
        ]
        
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 9, 'band': 'advanced', 'type': 'visual',
            'question': f'Calculate {num1}/{denom1} ÷ {num2}/{denom2}: [L9-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': svg
        })
    
    # Divide by whole number
    for _ in range(15):
        num = random.randint(2, 6)
        denom = random.choice([3, 4, 5, 6])
        divisor = random.randint(2, 3)
        
        result_num = num
        result_denom = denom * divisor
        
        simp_num, simp_denom = simplify_fraction(result_num, result_denom)
        correct = f"{simp_num}/{simp_denom}"
        
        distractors = [
            f"{num * divisor}/{denom}",  # Multiplied instead
            f"{num}/{denom}",  # Unchanged
            f"{num}/{denom * divisor}"  # Unsimplified
        ]
        
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 9, 'band': 'advanced', 'type': 'calculation',
            'question': f'Calculate {num}/{denom} ÷ {divisor}: [L9-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    return questions


# ============================================================
# LEVEL 10: MULTI-STEP PROBLEMS
# ============================================================

def generate_level_10():
    """Level 10: Combined operations - the ultimate fraction challenge"""
    questions = []
    
    # (a/b + c/b) × n
    for _ in range(15):
        denom = random.choice([4, 6, 8])
        num1 = random.randint(1, denom // 2)
        num2 = random.randint(1, denom // 2)
        multiplier = random.randint(2, 3)
        
        sum_num = num1 + num2
        result_num = sum_num * multiplier
        
        simp_num, simp_denom = simplify_fraction(result_num, denom)
        
        if simp_denom == 1:
            correct = str(simp_num)
        elif simp_num > simp_denom:
            whole = simp_num // simp_denom
            rem = simp_num % simp_denom
            correct = f"{whole} {rem}/{simp_denom}" if rem > 0 else str(whole)
        else:
            correct = f"{simp_num}/{simp_denom}"
        
        distractors = [
            f"{sum_num}/{denom}",  # Forgot to multiply
            f"{num1 * multiplier}/{denom}",  # Only multiplied first
            f"{result_num}/{denom}"  # Unsimplified
        ]
        
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 10, 'band': 'mastery', 'type': 'calculation',
            'question': f'Calculate ({num1}/{denom} + {num2}/{denom}) × {multiplier}: [L10-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    # Reverse problems: find the original
    for _ in range(15):
        result = random.choice([6, 8, 9, 10, 12, 15])
        frac_num = random.randint(2, 4)
        frac_denom = random.choice([3, 4, 5, 6])
        if frac_num >= frac_denom:
            frac_num = frac_denom - 1
        
        original = (result * frac_denom) // frac_num
        
        correct = str(original)
        distractors = [
            str(result),
            str(original + frac_denom),
            str(original - frac_num) if original > frac_num else str(original + 1)
        ]
        
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 10, 'band': 'mastery', 'type': 'calculation',
            'question': f'{frac_num}/{frac_denom} of a number equals {result}. What is the number? [L10-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    # a/b × c/d + e/f
    for _ in range(10):
        # Keep numbers manageable
        a, b = random.randint(1, 2), random.choice([2, 3])
        c, d = random.randint(1, 2), random.choice([2, 3])
        e, f = random.randint(1, 2), 6
        
        # Calculate a/b × c/d
        mult_num = a * c
        mult_denom = b * d
        
        # Add e/f - use common denominator
        common_d = mult_denom * f // gcd(mult_denom, f)
        term1 = mult_num * (common_d // mult_denom)
        term2 = e * (common_d // f)
        result_num = term1 + term2
        
        simp_num, simp_denom = simplify_fraction(result_num, common_d)
        
        if simp_denom == 1:
            correct = str(simp_num)
        else:
            correct = f"{simp_num}/{simp_denom}"
        
        distractors = [
            f"{mult_num}/{mult_denom}",  # Just multiplication
            f"{a * c + e}/{b * d + f}",  # Wrong method
            f"{result_num}/{common_d}"  # Unsimplified
        ]
        
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 10, 'band': 'mastery', 'type': 'calculation',
            'question': f'Calculate {a}/{b} × {c}/{d} + {e}/{f}: [L10-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': ''
        })
    
    return questions


# ============================================================
# LEVEL 11: APPLICATION (Real-World)
# ============================================================

def generate_level_11():
    """Level 11: Real-world application problems"""
    questions = []
    
    # Recipe scaling
    for _ in range(12):
        orig_cups_num = random.randint(1, 3)
        orig_cups_denom = random.choice([2, 3, 4])
        orig_serves = random.choice([4, 6])
        new_serves = random.choice([2, 3, 8, 9, 12])
        
        # Scale factor
        scale_num = new_serves
        scale_denom = orig_serves
        
        result_num = orig_cups_num * scale_num
        result_denom = orig_cups_denom * scale_denom
        
        simp_num, simp_denom = simplify_fraction(result_num, result_denom)
        
        if simp_denom == 1:
            correct = f"{simp_num} cups"
        elif simp_num > simp_denom:
            whole = simp_num // simp_denom
            rem = simp_num % simp_denom
            correct = f"{whole} {rem}/{simp_denom} cups" if rem > 0 else f"{whole} cups"
        else:
            correct = f"{simp_num}/{simp_denom} cups"
        
        distractors = [
            f"{orig_cups_num}/{orig_cups_denom} cups",
            f"{result_num}/{result_denom} cups",
            f"{simp_num + 1}/{simp_denom} cups"
        ]
        
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 11, 'band': 'application', 'type': 'word_problem',
            'question': f'A recipe for {orig_serves} people needs {orig_cups_num}/{orig_cups_denom} cups of flour. Áine is baking for {new_serves} people. How much flour does she need? [L11-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': '',
            'linked_topics': None
        })
    
    # Money/budget problems
    for _ in range(10):
        total = random.choice([60, 80, 100, 120])
        frac1_num = random.randint(1, 2)
        frac1_denom = random.choice([3, 4, 5])
        
        spent1 = (total * frac1_num) // frac1_denom
        remaining = total - spent1
        
        correct = f"€{remaining}"
        distractors = [f"€{spent1}", f"€{total}", f"€{remaining + 10}"]
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 11, 'band': 'application', 'type': 'word_problem',
            'question': f'Seán has €{total}. He spends {frac1_num}/{frac1_denom} of it on books. How much money does he have left? [L11-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': '',
            'linked_topics': None
        })
    
    # Time problems
    for _ in range(10):
        total_mins = random.choice([60, 90, 120])
        frac_num = random.randint(1, 3)
        frac_denom = random.choice([3, 4, 6])
        
        part_mins = (total_mins * frac_num) // frac_denom
        
        correct = f"{part_mins} minutes"
        distractors = [
            f"{total_mins - part_mins} minutes",
            f"{total_mins} minutes",
            f"{part_mins + 15} minutes"
        ]
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        task = random.choice(["homework", "reading", "practice"])
        
        questions.append({
            'level': 11, 'band': 'application', 'type': 'word_problem',
            'question': f'Ciarán spends {total_mins} minutes on {task}. He spends {frac_num}/{frac_denom} of this time on maths. How many minutes is that? [L11-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': '',
            'linked_topics': None
        })
    
    # Multi-step real world
    for _ in range(8):
        total = random.choice([36, 48, 60])
        frac1 = (1, 3)
        frac2 = (1, 2)
        
        group1 = (total * frac1[0]) // frac1[1]
        remainder = total - group1
        group2 = (remainder * frac2[0]) // frac2[1]
        rest = remainder - group2
        
        correct = str(rest)
        distractors = [str(group1), str(group2), str(remainder)]
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 11, 'band': 'application', 'type': 'word_problem',
            'question': f'A class has {total} students. {frac1[0]}/{frac1[1]} are absent. Of those present, {frac2[0]}/{frac2[1]} are girls. How many boys are present? [L11-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': '',
            'linked_topics': None
        })
    
    return questions


# ============================================================
# LEVEL 12: LINKED TOPICS
# ============================================================

def generate_level_12():
    """Level 12: Cross-topic integration"""
    questions = []
    
    # Fractions ↔ Percentages
    for _ in range(15):
        denom = random.choice([2, 4, 5, 10, 20, 25])
        num = random.randint(1, denom - 1)
        
        simp_num, simp_denom = simplify_fraction(num, denom)
        percentage = (num / denom) * 100
        
        if percentage == int(percentage):
            correct = f"{int(percentage)}%"
        else:
            correct = f"{percentage:.1f}%"
        
        distractors = [
            f"{simp_num * 10}%",
            f"{denom}%",
            f"{int(100 / denom)}%"
        ]
        
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 12, 'band': 'linked', 'type': 'calculation',
            'question': f'Convert {simp_num}/{simp_denom} to a percentage: [L12-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': '',
            'linked_topics': 'percentages'
        })
    
    # Fractions ↔ Decimals
    for _ in range(15):
        denom = random.choice([2, 4, 5, 8, 10, 20])
        num = random.randint(1, denom - 1)
        
        decimal = num / denom
        correct = f"{decimal:.2f}".rstrip('0').rstrip('.')
        if '.' not in correct:
            correct += ".0"
        
        distractors = [
            f"{num}.{denom}",
            f"0.{num}{denom}",
            f"{decimal + 0.1:.2f}".rstrip('0').rstrip('.')
        ]
        
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 12, 'band': 'linked', 'type': 'calculation',
            'question': f'Convert {num}/{denom} to a decimal: [L12-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': '',
            'linked_topics': 'decimals'
        })
    
    # Fractions ↔ Probability
    for _ in range(10):
        total = random.choice([10, 12, 15, 20])
        favorable = random.randint(2, total - 2)
        
        simp_num, simp_denom = simplify_fraction(favorable, total)
        correct = f"{simp_num}/{simp_denom}"
        
        distractors = [
            f"{total - favorable}/{total}",
            f"{favorable}/{total}",
            f"{simp_denom}/{simp_num}" if simp_num != simp_denom else f"{simp_num + 1}/{simp_denom}"
        ]
        
        options = make_unique_options(correct, distractors, 4)
        random.shuffle(options)
        
        questions.append({
            'level': 12, 'band': 'linked', 'type': 'word_problem',
            'question': f'A bag has {favorable} red and {total - favorable} blue marbles. One is picked at random. Write P(red) as a simplified fraction: [L12-{random.randint(1000,9999)}]',
            'options': options, 'correct': options.index(correct), 'svg': '',
            'linked_topics': 'probability'
        })
    
    return questions


# ============================================================
# DATABASE INSERTION
# ============================================================

def insert_questions(questions):
    """Insert questions into database"""
    conn = get_db()
    cursor = conn.cursor()
    inserted = 0
    duplicates = 0
    
    # Check if linked_topics column exists
    cursor.execute("PRAGMA table_info(questions_adaptive)")
    columns = [col[1] for col in cursor.fetchall()]
    has_linked_topics = 'linked_topics' in columns
    
    for q in questions:
        options = q['options']
        
        try:
            if has_linked_topics:
                cursor.execute('''
                    INSERT INTO questions_adaptive 
                    (topic, question_text, option_a, option_b, option_c, option_d, 
                     correct_answer, explanation, difficulty_level, difficulty_band,
                     question_type, image_svg, linked_topics, is_active, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?)
                ''', (
                    'fractions',
                    q['question'],
                    str(options[0]) if len(options) > 0 else '',
                    str(options[1]) if len(options) > 1 else '',
                    str(options[2]) if len(options) > 2 else '',
                    str(options[3]) if len(options) > 3 else '',
                    q['correct'],
                    '',
                    q['level'],
                    q['band'],
                    q['type'],
                    q.get('svg', ''),
                    q.get('linked_topics'),
                    datetime.now().isoformat()
                ))
            else:
                # Fallback without linked_topics column
                cursor.execute('''
                    INSERT INTO questions_adaptive 
                    (topic, question_text, option_a, option_b, option_c, option_d, 
                     correct_answer, explanation, difficulty_level, difficulty_band,
                     question_type, image_svg, is_active, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?)
                ''', (
                    'fractions',
                    q['question'],
                    str(options[0]) if len(options) > 0 else '',
                    str(options[1]) if len(options) > 1 else '',
                    str(options[2]) if len(options) > 2 else '',
                    str(options[3]) if len(options) > 3 else '',
                    q['correct'],
                    '',
                    q['level'],
                    q['band'],
                    q['type'],
                    q.get('svg', ''),
                    datetime.now().isoformat()
                ))
            inserted += 1
        except sqlite3.IntegrityError:
            duplicates += 1
        except Exception as e:
            print(f"Error: {e}")
    
    conn.commit()
    conn.close()
    return inserted, duplicates


# ============================================================
# MAIN
# ============================================================

def generate_all():
    """Generate all questions with clear skill progression"""
    print("=" * 70)
    print("FRACTIONS: Skill-Based Question Generator")
    print("=" * 70)
    print("\nSKILL LADDER:")
    for level, desc in SKILL_DESCRIPTIONS.items():
        print(f"  Level {level:2d}: {desc}")
    print()
    
    generators = [
        (1, generate_level_1, "IDENTIFY halves"),
        (2, generate_level_2, "IDENTIFY quarters/thirds"),
        (3, generate_level_3, "IDENTIFY any fraction"),
        (4, generate_level_4, "SIMPLIFY fractions"),
        (5, generate_level_5, "EQUIVALENT fractions"),
        (6, generate_level_6, "ADD/SUBTRACT same denom"),
        (7, generate_level_7, "ADD/SUBTRACT diff denom"),
        (8, generate_level_8, "MULTIPLY fractions"),
        (9, generate_level_9, "DIVIDE fractions"),
        (10, generate_level_10, "MULTI-STEP problems"),
        (11, generate_level_11, "APPLICATION"),
        (12, generate_level_12, "LINKED TOPICS"),
    ]
    
    total_inserted = 0
    total_duplicates = 0
    
    for level, generator, skill in generators:
        questions = generator()
        inserted, duplicates = insert_questions(questions)
        total_inserted += inserted
        total_duplicates += duplicates
        print(f"Level {level:2d} ({skill:25s}): Generated {len(questions):3d} → Inserted {inserted:3d} (dupes: {duplicates})")
    
    print(f"\n{'='*70}")
    print(f"TOTAL: Inserted {total_inserted} questions (skipped {total_duplicates} duplicates)")
    print(f"{'='*70}")


def show_stats():
    """Show current statistics"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT difficulty_level, difficulty_band, COUNT(*) 
        FROM questions_adaptive 
        WHERE topic = 'fractions' AND is_active = 1
        GROUP BY difficulty_level
        ORDER BY difficulty_level
    """)
    
    print("\n" + "=" * 60)
    print("Current Fractions Question Bank")
    print("=" * 60)
    print(f"{'Level':<8} {'Skill':<30} {'Count':<8}")
    print("-" * 60)
    
    for row in cursor.fetchall():
        level, band, count = row
        skill = SKILL_DESCRIPTIONS.get(level, "Unknown")[:28]
        print(f"Level {level:<2} {skill:<30} {count:<8}")
    
    conn.close()


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--stats':
        show_stats()
    else:
        generate_all()
        print()
        show_stats()
