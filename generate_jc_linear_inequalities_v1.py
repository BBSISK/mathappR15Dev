#!/usr/bin/env python3
"""
AgentMath - Linear Inequalities Question Generator
SEC Junior Cycle Aligned - JC Exam Mode

Based on SEC Papers 2022-2025:
- 2022 OL Q8(d-e): Temperature inequalities, interpretation & number line
- 2023 HL Q1(a-b): Rounding inequalities (18°C shown, find actual range)
- 2022 HL Q4(a): Solve 2x − 3 ≥ 5 where x ∈ ℤ, show on number line
- 2023 HL Q4(d): Solve 3x + 2 < 14 where x ∈ ℕ
- 2024 HL Q11(c): Graph x < 2 (x∈ℤ), x ≤ 3 (x∈ℕ), −2 < x ≤ 4 (x∈ℝ)

Level Structure:
  L1-3:   Foundation (75% visual)
  L4-6:   Ordinary (75% visual)
  L7-9:   Higher (75% visual)
  L10-12: Application/Mastery (L10: 75%, L11-12: 50%)

Target: 600 questions (50 per level)
"""

import random
import sqlite3
import os

# ============================================================
# CONFIGURATION
# ============================================================

TOPIC = 'linear_inequalities'
MODE = 'jc_exam'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'

# Irish names for word problems
IRISH_NAMES = ['Aoife', 'Cian', 'Niamh', 'Oisín', 'Saoirse', 'Conor', 'Róisín', 'Seán', 
               'Ciara', 'Darragh', 'Éabha', 'Fionn', 'Gráinne', 'Liam', 'Meadhbh', 'Tadhg',
               'Áine', 'Cillian', 'Orlaith', 'Pádraig', 'Sinéad', 'Eoin', 'Caoimhe', 'Declan']

# Irish places
IRISH_PLACES = ['Dublin', 'Cork', 'Galway', 'Limerick', 'Waterford', 'Kilkenny', 
                'Sligo', 'Wexford', 'Donegal', 'Kerry', 'Clare', 'Mayo']

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_unique_wrong_numbers(correct_val, exclude_list, count=3):
    """Generate unique wrong number options"""
    exclude_set = set(exclude_list) | {correct_val}
    wrong = set()
    
    # Try nearby values first
    candidates = [correct_val + 1, correct_val - 1, correct_val + 2, correct_val - 2,
                  correct_val * 2, correct_val + 3, correct_val - 3, correct_val + 5]
    
    for c in candidates:
        if c not in exclude_set and len(wrong) < count:
            wrong.add(c)
    
    # Fill remaining with random values
    while len(wrong) < count:
        w = random.randint(-10, 20)
        if w not in exclude_set and w not in wrong:
            wrong.add(w)
    
    return [str(w) for w in list(wrong)[:count]]

def ensure_unique_options(correct, wrong_opts):
    """Ensure all 4 options are unique, return None if can't make unique"""
    options = [correct] + list(wrong_opts)[:3]
    if len(set(options)) != 4:
        return None
    return options

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

def generate_number_line_svg(min_val, max_val, inequality_type, value, domain='R', show_solution=True):
    """
    Generate SVG number line for inequality visualization
    
    inequality_type: 'lt' (<), 'le' (≤), 'gt' (>), 'ge' (≥)
    domain: 'R' (real), 'Z' (integer), 'N' (natural)
    """
    width = 300
    height = 60
    margin = 30
    line_y = 35
    
    # Calculate scale
    range_val = max_val - min_val
    if range_val == 0:
        range_val = 1
    scale = (width - 2 * margin) / range_val
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    
    # Background
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#f8fafc" rx="5"/>'
    
    # Number line
    svg += f'<line x1="{margin}" y1="{line_y}" x2="{width - margin}" y2="{line_y}" stroke="#374151" stroke-width="2"/>'
    
    # Arrows at ends
    svg += f'<polygon points="{margin-5},{line_y} {margin+5},{line_y-5} {margin+5},{line_y+5}" fill="#374151"/>'
    svg += f'<polygon points="{width-margin+5},{line_y} {width-margin-5},{line_y-5} {width-margin-5},{line_y+5}" fill="#374151"/>'
    
    # Tick marks and labels
    for i in range(min_val, max_val + 1):
        x = margin + (i - min_val) * scale
        svg += f'<line x1="{x}" y1="{line_y - 5}" x2="{x}" y2="{line_y + 5}" stroke="#374151" stroke-width="1.5"/>'
        svg += f'<text x="{x}" y="{line_y + 18}" text-anchor="middle" font-size="10" fill="#374151">{i}</text>'
    
    if show_solution:
        value_x = margin + (value - min_val) * scale
        
        # Draw the solution region
        if inequality_type in ['lt', 'le']:
            # Shade to the left
            svg += f'<line x1="{margin}" y1="{line_y}" x2="{value_x}" y2="{line_y}" stroke="#3b82f6" stroke-width="4"/>'
        else:  # gt, ge
            # Shade to the right
            svg += f'<line x1="{value_x}" y1="{line_y}" x2="{width - margin}" y2="{line_y}" stroke="#3b82f6" stroke-width="4"/>'
        
        # Draw the endpoint circle (filled for ≤/≥, hollow for </> )
        if inequality_type in ['le', 'ge']:
            svg += f'<circle cx="{value_x}" cy="{line_y}" r="6" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>'
        else:
            svg += f'<circle cx="{value_x}" cy="{line_y}" r="6" fill="white" stroke="#3b82f6" stroke-width="2"/>'
        
        # For integers/naturals, show dots
        if domain in ['Z', 'N']:
            start = min_val if inequality_type in ['lt', 'le'] else value
            end = value if inequality_type in ['lt', 'le'] else max_val
            
            if domain == 'N':
                start = max(1, start)
            
            for i in range(start, end + 1):
                if inequality_type == 'lt' and i >= value:
                    continue
                if inequality_type == 'le' and i > value:
                    continue
                if inequality_type == 'gt' and i <= value:
                    continue
                if inequality_type == 'ge' and i < value:
                    continue
                    
                dot_x = margin + (i - min_val) * scale
                svg += f'<circle cx="{dot_x}" cy="{line_y}" r="4" fill="#22c55e" stroke="#15803d" stroke-width="1"/>'
    
    svg += '</svg>'
    return svg

def generate_compound_inequality_svg(min_val, max_val, left_val, right_val, left_inclusive, right_inclusive, domain='R'):
    """Generate SVG for compound inequalities like -2 < x ≤ 4"""
    width = 300
    height = 60
    margin = 30
    line_y = 35
    
    range_val = max_val - min_val
    if range_val == 0:
        range_val = 1
    scale = (width - 2 * margin) / range_val
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#f8fafc" rx="5"/>'
    
    # Number line
    svg += f'<line x1="{margin}" y1="{line_y}" x2="{width - margin}" y2="{line_y}" stroke="#374151" stroke-width="2"/>'
    
    # Arrows
    svg += f'<polygon points="{margin-5},{line_y} {margin+5},{line_y-5} {margin+5},{line_y+5}" fill="#374151"/>'
    svg += f'<polygon points="{width-margin+5},{line_y} {width-margin-5},{line_y-5} {width-margin-5},{line_y+5}" fill="#374151"/>'
    
    # Tick marks
    for i in range(min_val, max_val + 1):
        x = margin + (i - min_val) * scale
        svg += f'<line x1="{x}" y1="{line_y - 5}" x2="{x}" y2="{line_y + 5}" stroke="#374151" stroke-width="1.5"/>'
        svg += f'<text x="{x}" y="{line_y + 18}" text-anchor="middle" font-size="10" fill="#374151">{i}</text>'
    
    # Shaded region
    left_x = margin + (left_val - min_val) * scale
    right_x = margin + (right_val - min_val) * scale
    svg += f'<line x1="{left_x}" y1="{line_y}" x2="{right_x}" y2="{line_y}" stroke="#3b82f6" stroke-width="4"/>'
    
    # Left endpoint
    if left_inclusive:
        svg += f'<circle cx="{left_x}" cy="{line_y}" r="6" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>'
    else:
        svg += f'<circle cx="{left_x}" cy="{line_y}" r="6" fill="white" stroke="#3b82f6" stroke-width="2"/>'
    
    # Right endpoint
    if right_inclusive:
        svg += f'<circle cx="{right_x}" cy="{line_y}" r="6" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>'
    else:
        svg += f'<circle cx="{right_x}" cy="{line_y}" r="6" fill="white" stroke="#3b82f6" stroke-width="2"/>'
    
    svg += '</svg>'
    return svg

def generate_blank_number_line_svg(min_val, max_val):
    """Generate blank number line for questions asking students to identify"""
    width = 300
    height = 60
    margin = 30
    line_y = 35
    
    range_val = max_val - min_val
    if range_val == 0:
        range_val = 1
    scale = (width - 2 * margin) / range_val
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}">'
    svg += f'<rect x="0" y="0" width="{width}" height="{height}" fill="#f8fafc" rx="5"/>'
    
    # Number line
    svg += f'<line x1="{margin}" y1="{line_y}" x2="{width - margin}" y2="{line_y}" stroke="#374151" stroke-width="2"/>'
    
    # Arrows
    svg += f'<polygon points="{margin-5},{line_y} {margin+5},{line_y-5} {margin+5},{line_y+5}" fill="#374151"/>'
    svg += f'<polygon points="{width-margin+5},{line_y} {width-margin-5},{line_y-5} {width-margin-5},{line_y+5}" fill="#374151"/>'
    
    # Tick marks
    for i in range(min_val, max_val + 1):
        x = margin + (i - min_val) * scale
        svg += f'<line x1="{x}" y1="{line_y - 5}" x2="{x}" y2="{line_y + 5}" stroke="#374151" stroke-width="1.5"/>'
        svg += f'<text x="{x}" y="{line_y + 18}" text-anchor="middle" font-size="10" fill="#374151">{i}</text>'
    
    svg += '</svg>'
    return svg

def generate_thermometer_svg(temp, min_temp=30, max_temp=45):
    """Generate thermometer visual for temperature inequalities"""
    width = 80
    height = 150
    
    # Calculate fill level
    temp = max(min_temp, min(max_temp, temp))  # Clamp temp
    fill_pct = (temp - min_temp) / (max_temp - min_temp)
    fill_height = int(90 * fill_pct)
    
    svg = f'''<svg viewBox="0 0 {width} {height}" width="{width}">
        <rect x="0" y="0" width="{width}" height="{height}" fill="#f0f9ff" rx="5"/>
        
        <!-- Thermometer outline -->
        <rect x="30" y="15" width="20" height="100" rx="10" fill="#e5e7eb" stroke="#9ca3af" stroke-width="2"/>
        <circle cx="40" cy="125" r="18" fill="#e5e7eb" stroke="#9ca3af" stroke-width="2"/>
        
        <!-- Mercury -->
        <rect x="34" y="{105 - fill_height}" width="12" height="{fill_height + 10}" fill="#ef4444"/>
        <circle cx="40" cy="125" r="14" fill="#ef4444"/>
        
        <!-- Temperature reading -->
        <text x="40" y="{height - 5}" text-anchor="middle" font-size="12" font-weight="bold" fill="#dc2626">{temp}°C</text>
        
        <!-- Scale markers -->
        <text x="60" y="25" font-size="8" fill="#6b7280">{max_temp}°</text>
        <text x="60" y="70" font-size="8" fill="#6b7280">{(max_temp+min_temp)//2}°</text>
        <text x="60" y="110" font-size="8" fill="#6b7280">{min_temp}°</text>
    </svg>'''
    return svg

def generate_context_visual_svg(context, value, comparison):
    """Generate context-based visuals for word problems"""
    if context == 'age':
        svg = f'''<svg viewBox="0 0 200 70" width="200">
            <rect x="5" y="5" width="190" height="60" rx="8" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
            <text x="100" y="28" text-anchor="middle" font-size="11" fill="#92400e">Age Restriction</text>
            <text x="100" y="48" text-anchor="middle" font-size="14" font-weight="bold" fill="#b45309">{comparison} {value} years</text>
        </svg>'''
    elif context == 'height':
        svg = f'''<svg viewBox="0 0 200 70" width="200">
            <rect x="5" y="5" width="190" height="60" rx="8" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>
            <text x="100" y="28" text-anchor="middle" font-size="11" fill="#1e40af">Height Requirement</text>
            <text x="100" y="48" text-anchor="middle" font-size="14" font-weight="bold" fill="#1d4ed8">{comparison} {value} cm</text>
        </svg>'''
    elif context == 'speed':
        svg = f'''<svg viewBox="0 0 200 70" width="200">
            <rect x="5" y="5" width="190" height="60" rx="8" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>
            <text x="100" y="28" text-anchor="middle" font-size="11" fill="#991b1b">Speed Limit</text>
            <text x="100" y="48" text-anchor="middle" font-size="14" font-weight="bold" fill="#dc2626">{comparison} {value} km/h</text>
        </svg>'''
    elif context == 'temperature':
        svg = f'''<svg viewBox="0 0 200 70" width="200">
            <rect x="5" y="5" width="190" height="60" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
            <text x="100" y="28" text-anchor="middle" font-size="11" fill="#065f46">Temperature Range</text>
            <text x="100" y="48" text-anchor="middle" font-size="14" font-weight="bold" fill="#047857">{comparison} {value}°C</text>
        </svg>'''
    else:
        svg = f'''<svg viewBox="0 0 200 70" width="200">
            <rect x="5" y="5" width="190" height="60" rx="8" fill="#f3e8ff" stroke="#a855f7" stroke-width="2"/>
            <text x="100" y="28" text-anchor="middle" font-size="11" fill="#6b21a8">Constraint</text>
            <text x="100" y="48" text-anchor="middle" font-size="14" font-weight="bold" fill="#7c3aed">{comparison} {value}</text>
        </svg>'''
    return svg

# ============================================================
# LEVEL 1: Understanding Inequality Symbols
# Foundation level - 75% visual
# ============================================================

def generate_level_1(num_questions=50):
    """Level 1: Understanding inequality symbols (<, >, ≤, ≥)"""
    questions = []
    used_questions = set()
    
    symbols = [
        ('<', 'less than', 'is smaller than'),
        ('>', 'greater than', 'is bigger than'),
        ('≤', 'less than or equal to', 'is at most'),
        ('≥', 'greater than or equal to', 'is at least')
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 10:
        attempts += 1
        
        q_type = random.choice(['symbol_to_words', 'words_to_symbol', 'true_false', 'compare_numbers'])
        
        if q_type == 'symbol_to_words':
            symbol, meaning1, meaning2 = random.choice(symbols)
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            while b == a:
                b = random.randint(1, 20)
            
            question_text = f"What does the symbol '{symbol}' mean in mathematics?"
            correct = meaning1.capitalize()
            wrong_opts = [m[1].capitalize() for s, m, _ in symbols if s != symbol][:3]
            
            # Visual showing the symbol
            visual = f'''<svg viewBox="0 0 120 60" width="120">
                <rect x="5" y="5" width="110" height="50" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
                <text x="60" y="40" text-anchor="middle" font-size="28" font-weight="bold" fill="#1d4ed8">{symbol}</text>
            </svg>'''
            
            explanation = f"The symbol '{symbol}' means '{meaning1}' or '{meaning2}'."
            
        elif q_type == 'words_to_symbol':
            symbol, meaning1, meaning2 = random.choice(symbols)
            phrase = random.choice([meaning1, meaning2])
            
            question_text = f"Which symbol means '{phrase}'?"
            correct = symbol
            wrong_opts = [s for s, _, _ in symbols if s != symbol]
            
            visual = f'''<svg viewBox="0 0 200 60" width="200">
                <rect x="5" y="5" width="190" height="50" rx="8" fill="#f0fdf4" stroke="#22c55e" stroke-width="2"/>
                <text x="100" y="38" text-anchor="middle" font-size="14" fill="#166534">"{phrase}"</text>
            </svg>'''
            
            explanation = f"'{phrase.capitalize()}' is written as '{symbol}' in mathematics."
            
        elif q_type == 'true_false':
            a = random.randint(1, 15)
            b = random.randint(1, 15)
            while b == a:
                b = random.randint(1, 15)
            
            symbol, _, _ = random.choice(symbols)
            
            # Determine if statement is true
            if symbol == '<':
                is_true = a < b
            elif symbol == '>':
                is_true = a > b
            elif symbol == '≤':
                is_true = a <= b
            else:  # ≥
                is_true = a >= b
            
            question_text = f"Is the statement '{a} {symbol} {b}' true or false?"
            correct = "True" if is_true else "False"
            wrong_opts = ["False" if is_true else "True", "Cannot determine", "Only sometimes"]
            
            visual = f'''<svg viewBox="0 0 150 60" width="150">
                <rect x="5" y="5" width="140" height="50" rx="8" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
                <text x="75" y="40" text-anchor="middle" font-size="18" font-weight="bold" fill="#b45309">{a} {symbol} {b}</text>
            </svg>'''
            
            symbol_idx = [s for s, _, _ in symbols].index(symbol)
            explanation = f"{a} {symbol} {b} is {correct.lower()} because {a} {'is' if is_true else 'is not'} {symbols[symbol_idx][1]} {b}."
            
        else:  # compare_numbers
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            while b == a:
                b = random.randint(1, 20)
            
            question_text = f"Which symbol correctly completes: {a} ___ {b}?"
            
            if a < b:
                correct = "<"
                explanation = f"Since {a} is less than {b}, we write {a} < {b}."
            else:
                correct = ">"
                explanation = f"Since {a} is greater than {b}, we write {a} > {b}."
            
            wrong_opts = ["=", "≠", "≥" if a < b else "≤"]
            
            visual = f'''<svg viewBox="0 0 180 60" width="180">
                <rect x="5" y="5" width="170" height="50" rx="8" fill="#ede9fe" stroke="#8b5cf6" stroke-width="2"/>
                <text x="50" y="40" text-anchor="middle" font-size="20" font-weight="bold" fill="#5b21b6">{a}</text>
                <text x="90" y="40" text-anchor="middle" font-size="20" fill="#7c3aed">?</text>
                <text x="130" y="40" text-anchor="middle" font-size="20" font-weight="bold" fill="#5b21b6">{b}</text>
            </svg>'''
        
        q_key = f"{q_type}_{question_text}"
        if q_key in used_questions or question_text in used_questions:
            continue
        
        used_questions.add(q_key)
        used_questions.add(question_text)
        
        options = [correct] + wrong_opts[:3]
        if len(set(options)) != 4:
            continue
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 2: Reading Inequalities from Number Lines
# Foundation level - 75% visual
# ============================================================

def generate_level_2(num_questions=50):
    """Level 2: Reading inequalities from number lines"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 10:
        attempts += 1
        
        value = random.randint(-3, 7)
        ineq_type = random.choice(['lt', 'le', 'gt', 'ge'])
        
        q_style = random.choice(['read_inequality', 'identify_endpoint', 'identify_direction'])
        
        min_val = value - 4
        max_val = value + 4
        
        symbol_map = {'lt': '<', 'le': '≤', 'gt': '>', 'ge': '≥'}
        symbol = symbol_map[ineq_type]
        
        if q_style == 'read_inequality':
            question_text = f"Which inequality is shown on this number line? (boundary at {value})"
            visual = generate_number_line_svg(min_val, max_val, ineq_type, value, 'R', True)
            
            correct = f"x {symbol} {value}"
            
            # Generate wrong options
            wrong_symbols = [s for s in ['<', '≤', '>', '≥'] if s != symbol]
            wrong_opts = [f"x {wrong_symbols[0]} {value}", 
                         f"x {wrong_symbols[1]} {value}", 
                         f"x {symbol} {value + 1}"]
            
            explanation = f"The number line shows all values {'less than' if ineq_type in ['lt', 'le'] else 'greater than'}{' or equal to' if ineq_type in ['le', 'ge'] else ''} {value}. The {'filled' if ineq_type in ['le', 'ge'] else 'hollow'} circle means {value} is {'included' if ineq_type in ['le', 'ge'] else 'not included'}."
            
        elif q_style == 'identify_endpoint':
            question_text = f"What is the boundary value in this inequality showing x {symbol} ___?"
            visual = generate_number_line_svg(min_val, max_val, ineq_type, value, 'R', True)
            
            correct = str(value)
            wrong_opts = [str(value - 1), str(value + 1), str(value + 2)]
            
            explanation = f"The boundary value is {value}, shown by the circle on the number line."
            
        else:  # identify_direction
            question_text = f"For x {symbol} {value}, which direction does the shading go?"
            visual = generate_number_line_svg(min_val, max_val, ineq_type, value, 'R', True)
            
            if ineq_type in ['lt', 'le']:
                correct = "Left (towards smaller numbers)"
                wrong_opts = ["Right (towards larger numbers)", "Both directions", "Neither direction"]
            else:
                correct = "Right (towards larger numbers)"
                wrong_opts = ["Left (towards smaller numbers)", "Both directions", "Neither direction"]
            
            explanation = f"For x {symbol} {value}, the solution includes all values {'less than' if ineq_type in ['lt', 'le'] else 'greater than'} {value}, so shading goes {'left' if ineq_type in ['lt', 'le'] else 'right'}."
        
        q_key = f"{q_style}_{ineq_type}_{value}"
        if q_key in used_questions or question_text in used_questions:
            continue
        
        used_questions.add(q_key)
        used_questions.add(question_text)
        
        options = [correct] + wrong_opts[:3]
        if len(set(options)) != 4:
            continue
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 3: Real-World Inequality Interpretation
# Foundation level - 75% visual (SEC 2022 OL Q8 style)
# ============================================================

def generate_level_3(num_questions=50):
    """Level 3: Interpreting real-world inequalities"""
    questions = []
    used_questions = set()
    
    contexts = [
        ('temperature', '°C', 'T', [(35, 'hypothermia'), (36, 'low'), (37, 'normal'), (38, 'fever'), (40, 'high fever')]),
        ('age', ' years', 'A', [(12, 'child'), (13, 'teenager'), (18, 'adult'), (65, 'senior')]),
        ('speed', ' km/h', 'S', [(30, 'school zone'), (50, 'town'), (80, 'regional'), (120, 'motorway')]),
        ('height', ' cm', 'H', [(100, 'toddler ride'), (120, 'small ride'), (140, 'all rides')])
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 10:
        attempts += 1
        
        context, unit, var, thresholds = random.choice(contexts)
        threshold, description = random.choice(thresholds)
        
        q_style = random.choice(['inequality_to_words', 'words_to_inequality', 'complete_table', 'interpret_range'])
        
        if q_style == 'inequality_to_words':
            ineq_type = random.choice(['lt', 'gt', 'le', 'ge'])
            symbol_map = {'lt': '<', 'le': '≤', 'gt': '>', 'ge': '≥'}
            symbol = symbol_map[ineq_type]
            
            question_text = f"What does {var} {symbol} {threshold} mean in words?"
            
            word_map = {
                'lt': f'{context.capitalize()} is less than {threshold}{unit}',
                'le': f'{context.capitalize()} is at most {threshold}{unit}',
                'gt': f'{context.capitalize()} is greater than {threshold}{unit}',
                'ge': f'{context.capitalize()} is at least {threshold}{unit}'
            }
            
            correct = word_map[ineq_type]
            wrong_opts = [word_map[k] for k in word_map if k != ineq_type]
            
            visual = generate_context_visual_svg(context, f"{threshold}{unit}", symbol)
            explanation = f"{var} {symbol} {threshold} means the {context} is {word_map[ineq_type].split('is ')[1]}."
            
        elif q_style == 'words_to_inequality':
            ineq_type = random.choice(['lt', 'gt', 'le', 'ge'])
            symbol_map = {'lt': '<', 'le': '≤', 'gt': '>', 'ge': '≥'}
            
            word_phrases = {
                'lt': f'The {context} must be below {threshold}{unit}',
                'le': f'The {context} must not exceed {threshold}{unit}',
                'gt': f'The {context} must be above {threshold}{unit}',
                'ge': f'The {context} must be at least {threshold}{unit}'
            }
            
            phrase = word_phrases[ineq_type]
            question_text = f"'{phrase}' - Write this as an inequality."
            
            correct = f"{var} {symbol_map[ineq_type]} {threshold}"
            wrong_opts = [f"{var} {symbol_map[k]} {threshold}" for k in symbol_map if k != ineq_type]
            
            visual = generate_context_visual_svg(context, f"{threshold}{unit}", "?")
            explanation = f"'{phrase}' is written as {correct}."
            
        elif q_style == 'complete_table':
            if context == 'temperature':
                question_text = f"Complete: {var} > {threshold} means '________________'"
                correct = f"Temperature is greater than {threshold}°C"
                wrong_opts = [
                    f"Temperature is less than {threshold}°C",
                    f"Temperature equals {threshold}°C",
                    f"Temperature is at most {threshold}°C"
                ]
                visual = generate_thermometer_svg(threshold + 2)
            else:
                question_text = f"Complete: {var} ≥ {threshold} means '________________'"
                correct = f"{context.capitalize()} is at least {threshold}{unit}"
                wrong_opts = [
                    f"{context.capitalize()} is less than {threshold}{unit}",
                    f"{context.capitalize()} is exactly {threshold}{unit}",
                    f"{context.capitalize()} is below {threshold}{unit}"
                ]
                visual = generate_context_visual_svg(context, f"{threshold}{unit}", "≥")
            
            explanation = f"The symbol '>' means 'greater than' and '≥' means 'greater than or equal to' (at least)."
            
        else:  # interpret_range
            low = threshold - random.randint(2, 5)
            high = threshold + random.randint(2, 5)
            
            question_text = f"What does {low} < {var} < {high} tell us about the {context}?"
            correct = f"{context.capitalize()} is between {low}{unit} and {high}{unit}"
            wrong_opts = [
                f"{context.capitalize()} is less than {low}{unit}",
                f"{context.capitalize()} is greater than {high}{unit}",
                f"{context.capitalize()} equals {low}{unit} or {high}{unit}"
            ]
            
            visual = generate_compound_inequality_svg(low - 2, high + 2, low, high, False, False)
            explanation = f"{low} < {var} < {high} means the {context} is strictly between {low}{unit} and {high}{unit}, not including the endpoints."
        
        q_key = f"{q_style}_{context}_{threshold}_{ineq_type if 'ineq_type' in dir() else ''}"
        if q_key in used_questions or question_text in used_questions:
            continue
        
        used_questions.add(q_key)
        used_questions.add(question_text)
        
        options = [correct] + wrong_opts[:3]
        if len(set(options)) != 4:
            continue
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 4: Graphing Simple Inequalities (x ∈ ℝ)
# Ordinary level - 75% visual
# ============================================================

def generate_level_4(num_questions=50):
    """Level 4: Graphing simple inequalities on number line (x ∈ ℝ)"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 10:
        attempts += 1
        
        value = random.randint(-5, 8)
        ineq_type = random.choice(['lt', 'le', 'gt', 'ge'])
        symbol_map = {'lt': '<', 'le': '≤', 'gt': '>', 'ge': '≥'}
        symbol = symbol_map[ineq_type]
        
        q_style = random.choice(['which_graph', 'describe_graph', 'endpoint_type', 'match_inequality'])
        
        min_val = value - 4
        max_val = value + 4
        
        if q_style == 'which_graph':
            question_text = f"Which description matches the graph of x {symbol} {value}?"
            visual = generate_number_line_svg(min_val, max_val, ineq_type, value, 'R', True)
            
            correct = f"Shading {'left' if ineq_type in ['lt', 'le'] else 'right'}, {'filled' if ineq_type in ['le', 'ge'] else 'hollow'} circle at {value}"
            
            opposite_dir = 'right' if ineq_type in ['lt', 'le'] else 'left'
            opposite_circle = 'hollow' if ineq_type in ['le', 'ge'] else 'filled'
            
            wrong_opts = [
                f"Shading {opposite_dir}, {'filled' if ineq_type in ['le', 'ge'] else 'hollow'} circle at {value}",
                f"Shading {'left' if ineq_type in ['lt', 'le'] else 'right'}, {opposite_circle} circle at {value}",
                f"Shading {opposite_dir}, {opposite_circle} circle at {value}"
            ]
            
            explanation = f"For x {symbol} {value}: shade {'left (smaller values)' if ineq_type in ['lt', 'le'] else 'right (larger values)'}, use {'filled' if ineq_type in ['le', 'ge'] else 'hollow'} circle because {value} is {'included' if ineq_type in ['le', 'ge'] else 'not included'}."
            
        elif q_style == 'describe_graph':
            question_text = f"How would you graph x {symbol} {value} on a number line?"
            visual = generate_blank_number_line_svg(min_val, max_val)
            
            correct = f"{'Filled' if ineq_type in ['le', 'ge'] else 'Hollow'} circle at {value}, shade {'left' if ineq_type in ['lt', 'le'] else 'right'}"
            
            wrong_opts = [
                f"{'Hollow' if ineq_type in ['le', 'ge'] else 'Filled'} circle at {value}, shade {'left' if ineq_type in ['lt', 'le'] else 'right'}",
                f"{'Filled' if ineq_type in ['le', 'ge'] else 'Hollow'} circle at {value}, shade {'right' if ineq_type in ['lt', 'le'] else 'left'}",
                f"{'Hollow' if ineq_type in ['le', 'ge'] else 'Filled'} circle at {value}, shade {'right' if ineq_type in ['lt', 'le'] else 'left'}"
            ]
            
            explanation = f"Use a {'filled (solid)' if ineq_type in ['le', 'ge'] else 'hollow (open)'} circle at {value} because '{symbol}' {'includes' if ineq_type in ['le', 'ge'] else 'excludes'} the endpoint. Shade {'left' if ineq_type in ['lt', 'le'] else 'right'} for {'less than' if ineq_type in ['lt', 'le'] else 'greater than'}."
            
        elif q_style == 'endpoint_type':
            question_text = f"For x {symbol} {value}, what type of circle should be at {value}?"
            visual = generate_number_line_svg(min_val, max_val, ineq_type, value, 'R', True)
            
            correct = "Filled (solid) circle" if ineq_type in ['le', 'ge'] else "Hollow (open) circle"
            wrong_opts = [
                "Hollow (open) circle" if ineq_type in ['le', 'ge'] else "Filled (solid) circle",
                "No circle needed",
                "A cross mark"
            ]
            
            explanation = f"For '{symbol}' use a {'filled' if ineq_type in ['le', 'ge'] else 'hollow'} circle. Filled means the value is included (≤ or ≥), hollow means excluded (< or >)."
            
        else:  # match_inequality
            question_text = f"Match this graph (boundary at {value}) to the correct inequality:"
            visual = generate_number_line_svg(min_val, max_val, ineq_type, value, 'R', True)
            
            correct = f"x {symbol} {value}"
            flip_map = {'lt': 'gt', 'gt': 'lt', 'le': 'ge', 'ge': 'le'}
            incl_map = {'lt': 'le', 'le': 'lt', 'gt': 'ge', 'ge': 'gt'}
            wrong_opts = [
                f"x {symbol_map[flip_map[ineq_type]]} {value}",
                f"x {symbol_map[incl_map[ineq_type]]} {value}",
                f"x {symbol} {value + 1}"
            ]
            
            explanation = f"The graph shows {'left' if ineq_type in ['lt', 'le'] else 'right'} shading with {'filled' if ineq_type in ['le', 'ge'] else 'hollow'} circle at {value}, so x {symbol} {value}."
        
        q_key = f"{q_style}_{ineq_type}_{value}"
        if q_key in used_questions or question_text in used_questions:
            continue
        
        used_questions.add(q_key)
        used_questions.add(question_text)
        
        options = [correct] + wrong_opts[:3]
        if len(set(options)) != 4:
            continue
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 5: Graphing with Domain Restrictions (x ∈ ℤ, x ∈ ℕ)
# Ordinary level - 75% visual (SEC 2024 HL Q11(c) style)
# ============================================================

def generate_level_5(num_questions=50):
    """Level 5: Graphing with integer/natural number restrictions"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 10:
        attempts += 1
        
        value = random.randint(1, 6)
        ineq_type = random.choice(['lt', 'le', 'gt', 'ge'])
        domain = random.choice(['Z', 'N'])
        symbol_map = {'lt': '<', 'le': '≤', 'gt': '>', 'ge': '≥'}
        symbol = symbol_map[ineq_type]
        
        domain_name = 'integers (ℤ)' if domain == 'Z' else 'natural numbers (ℕ)'
        domain_symbol = 'ℤ' if domain == 'Z' else 'ℕ'
        
        q_style = random.choice(['list_solutions', 'count_solutions', 'identify_domain', 'graph_domain'])
        
        min_val = -3 if domain == 'Z' else 0
        max_val = value + 4
        
        # Calculate actual solutions
        if ineq_type == 'lt':
            if domain == 'Z':
                solutions = [i for i in range(min_val, value)]
            else:
                solutions = [i for i in range(1, value)]
        elif ineq_type == 'le':
            if domain == 'Z':
                solutions = [i for i in range(min_val, value + 1)]
            else:
                solutions = [i for i in range(1, value + 1)]
        elif ineq_type == 'gt':
            solutions = [i for i in range(value + 1, max_val + 1)]
            if domain == 'N':
                solutions = [s for s in solutions if s >= 1]
        else:  # ge
            if domain == 'N' and value < 1:
                solutions = [i for i in range(1, max_val + 1)]
            else:
                solutions = [i for i in range(max(value, 1 if domain == 'N' else value), max_val + 1)]
        
        solutions = solutions[:6]
        
        if q_style == 'list_solutions':
            question_text = f"List solutions to x {symbol} {value}, where x ∈ {domain_symbol}:"
            visual = generate_number_line_svg(min_val, max_val, ineq_type, value, domain, True)
            
            if solutions:
                correct = ', '.join(map(str, sorted(solutions)[:5])) + ('...' if len(solutions) > 5 else '')
            else:
                correct = "No solutions"
            
            if solutions:
                w1 = solutions + [value] if ineq_type in ['lt', 'gt'] else [s for s in solutions if s != value]
                w2 = [s + 1 for s in solutions]
                w3 = [s - 1 for s in solutions if s - 1 >= (1 if domain == 'N' else min_val)]
            else:
                w1 = [value]
                w2 = [value + 1]
                w3 = [value - 1] if value > 0 else [1]
            
            wrong_opts = [
                ', '.join(map(str, sorted(w1)[:5])) if w1 else "No solutions",
                ', '.join(map(str, sorted(w2)[:5])) if w2 else "No solutions",
                ', '.join(map(str, sorted(w3)[:5])) if w3 else "No solutions"
            ]
            
            explanation = f"For x {symbol} {value} where x ∈ {domain_symbol}: {correct}."
            
        elif q_style == 'count_solutions':
            question_text = f"How many solutions does x {symbol} {value}, x ∈ {domain_symbol}, have between {min_val} and {max_val}?"
            visual = generate_number_line_svg(min_val, max_val, ineq_type, value, domain, True)
            
            correct = str(len(solutions))
            wrong_opts = [str(len(solutions) + 1), str(max(0, len(solutions) - 1)), str(len(solutions) + 2)]
            
            explanation = f"Count the {domain_name} satisfying x {symbol} {value}: there are {len(solutions)} solutions."
            
        elif q_style == 'identify_domain':
            question_text = f"This graph shows x {symbol} {value} with dots. What is the domain?"
            visual = generate_number_line_svg(min_val if domain == 'Z' else 0, max_val, ineq_type, value, domain, True)
            
            correct = f"x ∈ {domain_symbol} ({domain_name})"
            other_domain = 'ℕ' if domain == 'Z' else 'ℤ'
            other_name = 'natural numbers (ℕ)' if domain == 'Z' else 'integers (ℤ)'
            
            wrong_opts = [
                f"x ∈ ℝ (real numbers)",
                f"x ∈ {other_domain} ({other_name})",
                "x ∈ ℚ (rational numbers)"
            ]
            
            explanation = f"The dots show discrete values, indicating {domain_name}."
            
        else:  # graph_domain
            question_text = f"How should x {symbol} {value}, x ∈ {domain_symbol}, be graphed?"
            visual = generate_blank_number_line_svg(min_val if domain == 'Z' else 0, max_val)
            
            correct = f"Individual dots at each {domain_name[:-1]} satisfying the inequality"
            wrong_opts = [
                "A continuous line/ray",
                "A shaded region with no dots",
                "Only the endpoint marked"
            ]
            
            explanation = f"For discrete domains ({domain_symbol}), use individual dots, not a continuous line."
        
        q_key = f"{q_style}_{domain}_{ineq_type}_{value}"
        if q_key in used_questions or question_text in used_questions:
            continue
        
        used_questions.add(q_key)
        used_questions.add(question_text)
        
        options = [correct] + wrong_opts[:3]
        if len(set(options)) != 4:
            continue
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 6: Solving One-Step Inequalities
# Ordinary level - 75% visual
# ============================================================

def generate_level_6(num_questions=50):
    """Level 6: Solving one-step inequalities"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 10:
        attempts += 1
        
        ineq_type = random.choice(['lt', 'le', 'gt', 'ge'])
        symbol_map = {'lt': '<', 'le': '≤', 'gt': '>', 'ge': '≥'}
        symbol = symbol_map[ineq_type]
        
        op_type = random.choice(['add', 'subtract', 'multiply', 'divide'])
        
        if op_type == 'add':
            a = random.randint(2, 10)
            solution = random.randint(-5, 10)
            b = solution + a
            
            question_text = f"Solve: x + {a} {symbol} {b}"
            correct = f"x {symbol} {solution}"
            wrong_opts = [f"x {symbol} {solution + a}", f"x {symbol} {solution - 1}", f"x {symbol} {b}"]
            explanation = f"x + {a} {symbol} {b}\\nSubtract {a}: x {symbol} {solution}"
            
        elif op_type == 'subtract':
            a = random.randint(2, 10)
            solution = random.randint(-5, 15)
            b = solution - a
            
            question_text = f"Solve: x - {a} {symbol} {b}"
            correct = f"x {symbol} {solution}"
            wrong_opts = [f"x {symbol} {solution - a}", f"x {symbol} {b}", f"x {symbol} {solution + 1}"]
            explanation = f"x - {a} {symbol} {b}\\nAdd {a}: x {symbol} {solution}"
            
        elif op_type == 'multiply':
            a = random.randint(2, 5)
            solution = random.randint(1, 10)
            b = a * solution
            
            question_text = f"Solve: {a}x {symbol} {b}"
            correct = f"x {symbol} {solution}"
            wrong_opts = [f"x {symbol} {b}", f"x {symbol} {a * solution + 1}", f"x {symbol} {solution - 1}"]
            explanation = f"{a}x {symbol} {b}\\nDivide by {a}: x {symbol} {solution}"
            
        else:  # divide
            a = random.randint(2, 5)
            b = random.randint(1, 8)
            solution = a * b
            
            question_text = f"Solve: x/{a} {symbol} {b}"
            correct = f"x {symbol} {solution}"
            wrong_opts = [f"x {symbol} {b}", f"x {symbol} {solution + a}", f"x {symbol} {solution - a}"]
            explanation = f"x/{a} {symbol} {b}\\nMultiply by {a}: x {symbol} {solution}"
        
        if random.random() < 0.75:
            min_val = solution - 4
            max_val = solution + 4
            visual = generate_number_line_svg(min_val, max_val, ineq_type, solution, 'R', True)
        else:
            visual = None
        
        q_key = f"{op_type}_{ineq_type}_{question_text}"
        if q_key in used_questions or question_text in used_questions:
            continue
        
        used_questions.add(q_key)
        used_questions.add(question_text)
        
        options = [correct] + wrong_opts[:3]
        if len(set(options)) != 4:
            continue
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 7: Solving Two-Step Inequalities
# Higher level - 75% visual (SEC 2022 HL Q4(a) style)
# ============================================================

def generate_level_7(num_questions=50):
    """Level 7: Solving two-step inequalities (SEC style)"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 10:
        attempts += 1
        
        ineq_type = random.choice(['lt', 'le', 'gt', 'ge'])
        symbol_map = {'lt': '<', 'le': '≤', 'gt': '>', 'ge': '≥'}
        symbol = symbol_map[ineq_type]
        
        a = random.randint(2, 5)
        b = random.randint(1, 10)
        solution = random.randint(-3, 8)
        
        style = random.choice(['ax_plus_b', 'ax_minus_b'])
        
        if style == 'ax_plus_b':
            c = a * solution + b
            question_text = f"Solve: {a}x + {b} {symbol} {c}"
            explanation = f"{a}x + {b} {symbol} {c}\\nSubtract {b}: {a}x {symbol} {c - b}\\nDivide by {a}: x {symbol} {solution}"
        else:
            c = a * solution - b
            question_text = f"Solve: {a}x - {b} {symbol} {c}"
            explanation = f"{a}x - {b} {symbol} {c}\\nAdd {b}: {a}x {symbol} {c + b}\\nDivide by {a}: x {symbol} {solution}"
        
        correct = f"x {symbol} {solution}"
        wrong_opts = [f"x {symbol} {solution + 1}", f"x {symbol} {solution - 1}", f"x {symbol} {a * solution}"]
        
        domain = random.choice([None, 'Z', 'N'])
        if domain:
            domain_symbol = 'ℤ' if domain == 'Z' else 'ℕ'
            question_text += f", where x ∈ {domain_symbol}"
        
        if random.random() < 0.75:
            min_val = solution - 4
            max_val = solution + 4
            visual = generate_number_line_svg(min_val, max_val, ineq_type, solution, domain if domain else 'R', True)
        else:
            visual = None
        
        q_key = f"{style}_{ineq_type}_{a}_{b}_{solution}_{domain}"
        if q_key in used_questions or question_text in used_questions:
            continue
        
        used_questions.add(q_key)
        used_questions.add(question_text)
        
        options = [correct] + wrong_opts[:3]
        if len(set(options)) != 4:
            continue
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 8: Compound Inequalities
# Higher level - 75% visual (SEC 2024 HL Q11(c) style)
# ============================================================

def generate_level_8(num_questions=50):
    """Level 8: Compound inequalities"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 10:
        attempts += 1
        
        left_val = random.randint(-5, 3)
        right_val = left_val + random.randint(3, 7)
        
        left_inclusive = random.choice([True, False])
        right_inclusive = random.choice([True, False])
        
        left_symbol = '≤' if left_inclusive else '<'
        right_symbol = '≤' if right_inclusive else '<'
        
        domain = random.choice(['R', 'Z'])
        domain_symbol = {'R': 'ℝ', 'Z': 'ℤ'}[domain]
        
        q_style = random.choice(['read_inequality', 'count_integers', 'interpret_meaning', 'graph_compound'])
        
        if q_style == 'read_inequality':
            question_text = f"What inequality is shown? (x ∈ {domain_symbol})"
            visual = generate_compound_inequality_svg(left_val - 2, right_val + 2, left_val, right_val, left_inclusive, right_inclusive, domain)
            
            correct = f"{left_val} {left_symbol} x {right_symbol} {right_val}"
            wrong_opts = [
                f"{left_val} {'≤' if not left_inclusive else '<'} x {right_symbol} {right_val}",
                f"{left_val} {left_symbol} x {'≤' if not right_inclusive else '<'} {right_val}",
                f"{left_val - 1} {left_symbol} x {right_symbol} {right_val + 1}"
            ]
            
            explanation = f"{'Filled' if left_inclusive else 'Hollow'} circle at {left_val}, {'filled' if right_inclusive else 'hollow'} at {right_val}."
            
        elif q_style == 'count_integers':
            question_text = f"How many integers satisfy {left_val} {left_symbol} x {right_symbol} {right_val}?"
            visual = generate_compound_inequality_svg(left_val - 2, right_val + 2, left_val, right_val, left_inclusive, right_inclusive, 'Z')
            
            start = left_val if left_inclusive else left_val + 1
            end = right_val if right_inclusive else right_val - 1
            count = max(0, end - start + 1)
            
            correct = str(count)
            wrong_opts = [str(count + 1), str(max(0, count - 1)), str(count + 2)]
            
            explanation = f"Integers from {start} to {end} = {count}."
            
        elif q_style == 'interpret_meaning':
            question_text = f"What does {left_val} {left_symbol} x {right_symbol} {right_val} mean?"
            visual = generate_compound_inequality_svg(left_val - 2, right_val + 2, left_val, right_val, left_inclusive, right_inclusive)
            
            left_word = "at least" if left_inclusive else "greater than"
            right_word = "at most" if right_inclusive else "less than"
            
            correct = f"x is {left_word} {left_val} AND {right_word} {right_val}"
            wrong_opts = [
                f"x is {left_word} {left_val} OR {right_word} {right_val}",
                f"x equals {left_val} or {right_val}",
                f"x is outside the range {left_val} to {right_val}"
            ]
            
            explanation = f"Compound inequality: x must satisfy BOTH conditions (AND)."
            
        else:  # graph_compound
            question_text = f"Describe how to graph {left_val} {left_symbol} x {right_symbol} {right_val}:"
            visual = generate_blank_number_line_svg(left_val - 2, right_val + 2)
            
            left_circle = "filled" if left_inclusive else "hollow"
            right_circle = "filled" if right_inclusive else "hollow"
            
            correct = f"{left_circle.capitalize()} at {left_val}, {right_circle} at {right_val}, shade between"
            wrong_opts = [
                f"{'Hollow' if left_inclusive else 'Filled'} at {left_val}, {right_circle} at {right_val}, shade between",
                f"{left_circle.capitalize()} at {left_val}, {'hollow' if right_inclusive else 'filled'} at {right_val}, shade between",
                f"{left_circle.capitalize()} at {left_val}, {right_circle} at {right_val}, shade outside"
            ]
            
            explanation = f"Use {left_circle} circle at {left_val}, {right_circle} at {right_val}, shade between."
        
        q_key = f"{q_style}_{left_val}_{right_val}_{left_inclusive}_{right_inclusive}_{domain}"
        if q_key in used_questions or question_text in used_questions:
            continue
        
        used_questions.add(q_key)
        used_questions.add(question_text)
        
        options = [correct] + wrong_opts[:3]
        if len(set(options)) != 4:
            continue
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 9: Inequalities with Negative Coefficients
# Higher level - 75% visual
# ============================================================

def generate_level_9(num_questions=50):
    """Level 9: Inequalities with negative coefficients (flip rule)"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 10:
        attempts += 1
        
        ineq_type = random.choice(['lt', 'le', 'gt', 'ge'])
        symbol_map = {'lt': '<', 'le': '≤', 'gt': '>', 'ge': '≥'}
        flip_map = {'lt': 'gt', 'le': 'ge', 'gt': 'lt', 'ge': 'le'}
        symbol = symbol_map[ineq_type]
        flipped_symbol = symbol_map[flip_map[ineq_type]]
        
        q_style = random.choice(['solve_negative', 'explain_flip', 'two_step_negative'])
        
        if q_style == 'solve_negative':
            a = random.randint(2, 5)
            solution = random.randint(-5, 5)
            b = -a * solution
            
            question_text = f"Solve: -{a}x {symbol} {b}"
            correct = f"x {flipped_symbol} {solution}"
            wrong_opts = [f"x {symbol} {solution}", f"x {flipped_symbol} {-solution}", f"x {symbol} {-solution}"]
            explanation = f"-{a}x {symbol} {b}\\nDivide by -{a} (FLIP!): x {flipped_symbol} {solution}"
            
            visual = generate_number_line_svg(solution - 4, solution + 4, flip_map[ineq_type], solution, 'R', True)
            
        elif q_style == 'explain_flip':
            question_text = "When do you flip the inequality sign?"
            correct = "When multiplying or dividing by a negative number"
            wrong_opts = ["When adding a negative number", "When subtracting from both sides", "Never"]
            
            visual = f'''<svg viewBox="0 0 280 80" width="280">
                <rect x="5" y="5" width="270" height="70" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
                <text x="140" y="30" text-anchor="middle" font-size="12" font-weight="bold" fill="#dc2626">⚠️ FLIP RULE</text>
                <text x="140" y="50" text-anchor="middle" font-size="10" fill="#991b1b">-2x &lt; 6  →  x &gt; -3</text>
                <text x="140" y="68" text-anchor="middle" font-size="9" fill="#b91c1c">(Divide by -2, flip &lt; to &gt;)</text>
            </svg>'''
            
            explanation = "When dividing or multiplying by a NEGATIVE, flip the inequality sign."
            
        else:  # two_step_negative
            a = random.randint(2, 4)
            b = random.randint(5, 15)
            solution = random.randint(-3, 5)
            c = b - a * solution
            
            question_text = f"Solve: {b} - {a}x {symbol} {c}"
            correct = f"x {flipped_symbol} {solution}"
            wrong_opts = [f"x {symbol} {solution}", f"x {flipped_symbol} {-solution}", f"x {symbol} {(b - c) // a if a != 0 else 0}"]
            explanation = f"{b} - {a}x {symbol} {c}\\nSubtract {b}: -{a}x {symbol} {c - b}\\nDivide by -{a} (FLIP!): x {flipped_symbol} {solution}"
            
            visual = generate_number_line_svg(solution - 4, solution + 4, flip_map[ineq_type], solution, 'R', True)
        
        q_key = f"{q_style}_{ineq_type}_{question_text[:40]}"
        if q_key in used_questions or question_text in used_questions:
            continue
        
        used_questions.add(q_key)
        used_questions.add(question_text)
        
        options = [correct] + wrong_opts[:3]
        if len(set(options)) != 4:
            continue
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 10: Word Problems with Inequalities
# Application level - 75% visual
# ============================================================

def generate_level_10(num_questions=50):
    """Level 10: Word problems with inequalities"""
    questions = []
    used_questions = set()
    
    problem_types = ['budget', 'age_restriction', 'height_ride', 'temperature', 'speed_limit']
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 10:
        attempts += 1
        
        p_type = random.choice(problem_types)
        name = random.choice(IRISH_NAMES)
        
        if p_type == 'budget':
            budget = random.randint(50, 200)
            item_cost = random.randint(5, 20)
            fixed_cost = random.randint(10, 30)
            max_items = (budget - fixed_cost) // item_cost
            
            question_text = f"{name} has €{budget}. Membership costs €{fixed_cost}, games cost €{item_cost} each. What inequality shows max games (g)?"
            correct = f"{item_cost}g + {fixed_cost} ≤ {budget}"
            wrong_opts = [f"{item_cost}g + {fixed_cost} ≥ {budget}", f"{item_cost}g - {fixed_cost} ≤ {budget}", f"{item_cost}g ≤ {budget}"]
            
            visual = f'''<svg viewBox="0 0 250 80" width="250">
                <rect x="5" y="5" width="240" height="70" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
                <text x="125" y="25" text-anchor="middle" font-size="11" fill="#065f46">Budget: €{budget}</text>
                <text x="125" y="45" text-anchor="middle" font-size="10" fill="#047857">Membership: €{fixed_cost} | Games: €{item_cost}</text>
                <text x="125" y="65" text-anchor="middle" font-size="10" font-weight="bold" fill="#059669">Max games: {max_items}</text>
            </svg>'''
            
            explanation = f"Total cost = {item_cost}g + {fixed_cost} ≤ {budget}"
            
        elif p_type == 'age_restriction':
            min_age = random.choice([12, 13, 15, 16, 18])
            
            question_text = f"A film is rated {min_age}+. Write an inequality for allowed ages (a)."
            correct = f"a ≥ {min_age}"
            wrong_opts = [f"a > {min_age}", f"a ≤ {min_age}", f"a < {min_age}"]
            
            visual = generate_context_visual_svg('age', min_age, '≥')
            explanation = f"'{min_age}+' means at least {min_age}, so a ≥ {min_age}."
            
        elif p_type == 'height_ride':
            min_height = random.choice([100, 110, 120, 130, 140])
            
            question_text = f"A ride requires minimum height {min_height} cm. Write the inequality for allowed heights (h)."
            correct = f"h ≥ {min_height}"
            wrong_opts = [f"h > {min_height}", f"h ≤ {min_height}", f"h = {min_height}"]
            
            visual = generate_context_visual_svg('height', min_height, 'at least')
            explanation = f"'At least {min_height} cm' means h ≥ {min_height}."
            
        elif p_type == 'temperature':
            low_temp = random.randint(15, 25)
            high_temp = low_temp + random.randint(5, 15)
            
            question_text = f"Temperature T must be between {low_temp}°C and {high_temp}°C inclusive. Write the inequality."
            correct = f"{low_temp} ≤ T ≤ {high_temp}"
            wrong_opts = [f"{low_temp} < T < {high_temp}", f"T ≤ {high_temp}", f"T ≥ {low_temp}"]
            
            visual = generate_compound_inequality_svg(low_temp - 5, high_temp + 5, low_temp, high_temp, True, True)
            explanation = f"'Between, inclusive' means {low_temp} ≤ T ≤ {high_temp}."
            
        else:  # speed_limit
            limit = random.choice([30, 50, 60, 80, 100, 120])
            
            question_text = f"Speed limit is {limit} km/h. Write inequality for legal speeds (s)."
            correct = f"s ≤ {limit}"
            wrong_opts = [f"s < {limit}", f"s ≥ {limit}", f"s = {limit}"]
            
            visual = generate_context_visual_svg('speed', limit, 'max')
            explanation = f"Speed limit {limit} means s ≤ {limit} (can equal the limit)."
        
        q_key = f"{p_type}_{question_text[:40]}"
        if q_key in used_questions or question_text in used_questions:
            continue
        
        used_questions.add(q_key)
        used_questions.add(question_text)
        
        options = [correct] + wrong_opts[:3]
        if len(set(options)) != 4:
            continue
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 11: Rounding & Tolerance Inequalities
# Application level - 50% visual (SEC 2023 HL Q1 style)
# ============================================================

def generate_level_11(num_questions=50):
    """Level 11: Rounding and tolerance inequalities (SEC style)"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 10:
        attempts += 1
        
        q_type = random.choice(['rounding_range', 'tolerance', 'measurement_error', 'significant_figures'])
        
        if q_type == 'rounding_range':
            displayed = random.randint(10, 30)
            name = random.choice(IRISH_NAMES)
            
            question_text = f"{name}'s thermometer shows {displayed}°C (nearest whole). Write inequality for actual temperature t."
            correct = f"{displayed - 0.5} ≤ t < {displayed + 0.5}"
            wrong_opts = [f"{displayed - 1} ≤ t ≤ {displayed + 1}", f"{displayed - 0.5} < t < {displayed + 0.5}", f"{displayed} ≤ t ≤ {displayed + 1}"]
            
            visual = generate_thermometer_svg(displayed) if random.random() < 0.5 else None
            explanation = f"Rounded to nearest whole: {displayed - 0.5} ≤ t < {displayed + 0.5}"
            
        elif q_type == 'tolerance':
            target = random.randint(50, 200)
            tolerance = random.choice([0.5, 1, 2, 5])
            
            question_text = f"A part must be {target} mm ± {tolerance} mm. Write inequality for acceptable length (L)."
            correct = f"{target - tolerance} ≤ L ≤ {target + tolerance}"
            wrong_opts = [f"{target - tolerance} < L < {target + tolerance}", f"L = {target} ± {tolerance}", f"|L - {target}| > {tolerance}"]
            
            visual = None
            explanation = f"{target} ± {tolerance} means {target - tolerance} ≤ L ≤ {target + tolerance}."
            
        elif q_type == 'measurement_error':
            measured = random.randint(10, 50)
            precision = random.choice([1, 2])
            half_precision = precision / 2
            
            question_text = f"Length measured as {measured} cm to nearest {precision} cm. What's the range for actual length (x)?"
            correct = f"{measured - half_precision} ≤ x < {measured + half_precision}"
            wrong_opts = [f"{measured - precision} ≤ x ≤ {measured + precision}", f"{measured - half_precision} < x < {measured + half_precision}", f"x = {measured}"]
            
            visual = None
            explanation = f"Nearest {precision} cm means error ± {half_precision} cm."
            
        else:  # significant_figures
            displayed = random.randint(2, 9) * 10
            
            question_text = f"Distance recorded as {displayed} m (to nearest 10 m). Write inequality for actual distance d."
            correct = f"{displayed - 5} ≤ d < {displayed + 5}"
            wrong_opts = [f"{displayed - 10} ≤ d ≤ {displayed + 10}", f"{displayed - 5} < d < {displayed + 5}", f"d = {displayed}"]
            
            visual = None
            explanation = f"Nearest 10 m means error bound ± 5 m."
        
        q_key = f"{q_type}_{question_text[:40]}"
        if q_key in used_questions or question_text in used_questions:
            continue
        
        used_questions.add(q_key)
        used_questions.add(question_text)
        
        options = [correct] + wrong_opts[:3]
        if len(set(options)) != 4:
            continue
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 12: Multi-step & Cross-topic Applications
# Mastery level - 50% visual
# ============================================================

def generate_level_12(num_questions=50):
    """Level 12: Multi-step and cross-topic inequality problems"""
    questions = []
    used_questions = set()
    
    problem_types = ['area_constraint', 'profit_analysis', 'combined_inequalities', 'optimization', 'algebraic_complex']
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 10:
        attempts += 1
        
        p_type = random.choice(problem_types)
        name = random.choice(IRISH_NAMES)
        
        if p_type == 'area_constraint':
            width = random.randint(3, 8)
            min_area = random.randint(30, 60)
            min_length = (min_area + width - 1) // width  # Ceiling division
            
            question_text = f"Rectangle width = {width} m, area must be at least {min_area} m². What inequality for length (L)?"
            correct = f"L ≥ {min_length}"
            wrong_opts = [f"L ≥ {min_area}", f"L ≤ {min_length}", f"L > {min_area // width}"]
            
            visual = f'''<svg viewBox="0 0 200 100" width="200">
                <rect x="20" y="20" width="160" height="60" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>
                <text x="100" y="55" text-anchor="middle" font-size="12" fill="#1d4ed8">Area ≥ {min_area} m²</text>
                <text x="100" y="90" text-anchor="middle" font-size="10" fill="#6b7280">Width = {width} m</text>
            </svg>'''
            
            explanation = f"Area = {width}L ≥ {min_area}, so L ≥ {min_area}/{width} ≈ {min_length}"
            
        elif p_type == 'profit_analysis':
            fixed_cost = random.randint(100, 500)
            cost_per = random.randint(5, 15)
            price_per = cost_per + random.randint(5, 15)
            break_even = fixed_cost // (price_per - cost_per)
            
            question_text = f"Fixed costs €{fixed_cost}, each item costs €{cost_per} to make, sells for €{price_per}. How many (n) for profit?"
            correct = f"n > {break_even}"
            wrong_opts = [f"n ≥ {break_even}", f"n > {fixed_cost // price_per}", f"n ≥ {fixed_cost}"]
            
            visual = None
            explanation = f"Profit = {price_per}n - {fixed_cost} - {cost_per}n = {price_per - cost_per}n - {fixed_cost} > 0, so n > {break_even}"
            
        elif p_type == 'combined_inequalities':
            a = random.randint(2, 4)
            b = random.randint(5, 15)
            c = random.randint(10, 30)
            
            sol1 = b // a
            sol2 = c // a
            if sol1 > sol2:
                sol1, sol2 = sol2, sol1
            
            question_text = f"Find integers satisfying both {a}x > {b} AND {a}x < {c}."
            
            lower = sol1 + 1
            upper = sol2 - 1 if (a * sol2) >= c else sol2
            int_solutions = list(range(lower, upper + 1))
            
            if int_solutions:
                correct = ", ".join(map(str, int_solutions[:5]))
            else:
                correct = "No solutions"
            
            wrong_opts = [
                ", ".join(map(str, [i + 1 for i in int_solutions[:4]])) if int_solutions else "0, 1, 2",
                ", ".join(map(str, [i - 1 for i in int_solutions[:4]])) if int_solutions else "1, 2, 3",
                "All integers"
            ]
            
            visual = None
            explanation = f"{b}/{a} < x < {c}/{a}, integers: {correct}"
            
        elif p_type == 'optimization':
            rate = random.randint(10, 25)
            fixed = random.randint(20, 50)
            budget = random.randint(100, 200)
            max_hours = (budget - fixed) // rate
            
            question_text = f"{name} charges €{fixed} callout + €{rate}/hour. Budget €{budget}. Max hours (h)?"
            correct = f"h ≤ {max_hours}"
            wrong_opts = [f"h ≤ {budget // rate}", f"h < {max_hours}", f"h ≤ {max_hours + 1}"]
            
            visual = None
            explanation = f"{fixed} + {rate}h ≤ {budget}, so h ≤ {max_hours}"
            
        else:  # algebraic_complex
            a = random.randint(2, 4)
            b = random.randint(1, 5)
            c = random.randint(1, 3)
            d = random.randint(6, 15)
            
            coeff = a - c
            const = d - b
            
            if coeff > 0:
                solution = const / coeff
                correct = f"x > {solution:.1f}" if solution != int(solution) else f"x > {int(solution)}"
            elif coeff < 0:
                solution = const / coeff
                correct = f"x < {solution:.1f}" if solution != int(solution) else f"x < {int(solution)}"
            else:
                correct = "No solution" if const > 0 else "All real numbers"
                solution = 0
            
            question_text = f"Solve: {a}x + {b} > {c}x + {d}"
            wrong_opts = [f"x < {abs(solution):.0f}" if coeff > 0 else f"x > {abs(solution):.0f}", f"x > {const}", f"x = {solution:.0f}"]
            
            visual = None
            explanation = f"{a}x + {b} > {c}x + {d} → {a-c}x > {d-b} → {correct}"
        
        q_key = f"{p_type}_{question_text[:40]}"
        if q_key in used_questions or question_text in used_questions:
            continue
        
        used_questions.add(q_key)
        used_questions.add(question_text)
        
        options = [correct] + wrong_opts[:3]
        if len(set(options)) != 4:
            continue
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# MAIN GENERATION AND DATABASE FUNCTIONS
# ============================================================

def generate_all_questions():
    """Generate all questions for all levels"""
    all_questions = []
    
    level_functions = [
        (1, generate_level_1, "Understanding Symbols"),
        (2, generate_level_2, "Reading Number Lines"),
        (3, generate_level_3, "Real-World Interpretation"),
        (4, generate_level_4, "Graphing (x ∈ ℝ)"),
        (5, generate_level_5, "Graphing (x ∈ ℤ, ℕ)"),
        (6, generate_level_6, "One-Step Solving"),
        (7, generate_level_7, "Two-Step Solving"),
        (8, generate_level_8, "Compound Inequalities"),
        (9, generate_level_9, "Negative Coefficients"),
        (10, generate_level_10, "Word Problems"),
        (11, generate_level_11, "Rounding & Tolerance"),
        (12, generate_level_12, "Multi-step Applications")
    ]
    
    for level, gen_func, description in level_functions:
        print(f"Generating Level {level}: {description}...")
        questions = gen_func(QUESTIONS_PER_LEVEL)
        
        for q in questions:
            q['topic'] = TOPIC
            q['difficulty'] = level
            q['mode'] = MODE
            
            if level <= 3:
                q['difficulty_band'] = 'foundation'
            elif level <= 6:
                q['difficulty_band'] = 'ordinary'
            elif level <= 9:
                q['difficulty_band'] = 'higher'
            else:
                q['difficulty_band'] = 'mastery'
        
        all_questions.extend(questions)
        print(f"  Generated {len(questions)} questions")
    
    return all_questions

def validate_questions(questions):
    """Validate all generated questions"""
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    
    errors = []
    level_counts = {}
    level_visuals = {}
    
    for q in questions:
        level = q['difficulty']
        level_counts[level] = level_counts.get(level, 0) + 1
        
        if q.get('image_svg'):
            level_visuals[level] = level_visuals.get(level, 0) + 1
        
        options = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(options)) != 4:
            errors.append(f"Level {level}: Duplicate options in '{q['question_text'][:30]}...'")
        
        if not q.get('explanation'):
            errors.append(f"Level {level}: Missing explanation")
    
    level_names = [
        "Understanding Symbols", "Reading Number Lines", "Real-World Interpretation",
        "Graphing (x ∈ ℝ)", "Graphing (x ∈ ℤ, ℕ)", "One-Step Solving",
        "Two-Step Solving", "Compound Inequalities", "Negative Coefficients",
        "Word Problems", "Rounding & Tolerance", "Multi-step Applications"
    ]
    
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        visual_count = level_visuals.get(level, 0)
        visual_pct = (visual_count / count * 100) if count > 0 else 0
        status = "✓" if count >= QUESTIONS_PER_LEVEL else "✗"
        print(f"Level {level:2}: {count:2}/{QUESTIONS_PER_LEVEL} | Visual: {visual_pct:5.1f}% | {status} {level_names[level-1]}")
    
    print("=" * 60)
    print(f"Total Questions: {len(questions)}")
    print(f"Total Errors: {len(errors)}")
    
    if errors:
        print("\nFirst 5 errors:")
        for err in errors[:5]:
            print(f"  - {err}")
    
    print("=" * 60)
    
    return len(errors) == 0

def insert_questions(questions, db_path=DB_PATH):
    """Insert questions into database"""
    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}")
        return False
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = ? AND mode = ?", (TOPIC, MODE))
    deleted = cursor.rowcount
    print(f"Deleted {deleted} existing {TOPIC} questions in {MODE} mode")
    
    inserted = 0
    errors = 0
    
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
            print(f"Error inserting: {e}")
            errors += 1
    
    conn.commit()
    conn.close()
    
    print(f"✓ Inserted {inserted} questions")
    if errors:
        print(f"✗ {errors} errors occurred")
    
    return errors == 0

if __name__ == "__main__":
    print("=" * 60)
    print("LINEAR INEQUALITIES - JC EXAM QUESTION GENERATOR")
    print("=" * 60)
    print(f"Topic: {TOPIC}")
    print(f"Mode: {MODE}")
    print(f"Questions per level: {QUESTIONS_PER_LEVEL}")
    print(f"Total target: {QUESTIONS_PER_LEVEL * 12}")
    print("=" * 60 + "\n")
    
    all_questions = generate_all_questions()
    is_valid = validate_questions(all_questions)
    
    if not is_valid:
        print("\n⚠ Validation found issues. Review before inserting.")
    
    print("=" * 60)
    
    response = input("Insert questions into database? (y/n): ")
    if response.lower() == 'y':
        success = insert_questions(all_questions)
        if success:
            print("\n✅ All questions inserted successfully!")
        else:
            print("\n⚠ Some questions failed to insert.")
    else:
        print("Skipped database insertion.")
    
    print("\nDone!")
