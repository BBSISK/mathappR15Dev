#!/usr/bin/env python3
"""
AgentMath - Descriptive Statistics Question Generator
SEC-Aligned for Irish Junior Cycle Mathematics

Version: 1.0
Date: December 2025
Author: Barry (ICT Coordinator, Palmerstown Community School)

Generates 600 questions (50 per level × 12 levels)
- Levels 1-10: 75% visual/contextual
- Levels 11-12: 50% visual/contextual
- All questions include step-by-step explanations

Level Structure:
  1: Reading Data (tally, pictogram, bar chart)
  2: Mode from Lists & Tables
  3: Range from Lists & Tables
  4: Median (odd datasets)
  5: Median (even datasets)
  6: Mean (simple averages)
  7: Frequency Tables (reading & creating)
  8: Mean from Frequency Tables
  9: Histograms & Grouped Data
  10: Stem-and-Leaf Diagrams
  11: Comparing Measures / Which is better?
  12: Problem Solving & Back-to-back Stem-and-Leaf

SEC Question Sources:
  - 2022 OL Q6: Range, mode, median, mean from table
  - 2023 OL Q4: Histogram, grouped data, median interval
  - 2024 OL Q5: Frequency table, bar chart, mode, range, mean
  - 2025 OL Q3: Histogram, grouped data
  - 2025 OL Q6(b): Find missing values given mode, median, range
  - 2022-2025 HL: Stem-and-leaf, back-to-back, comparison
"""

import sqlite3
import random
from collections import Counter

# ==================== CONFIGURATION ====================
TOPIC = 'descriptive_statistics'
QUESTIONS_PER_LEVEL = 50
DB_PATH = 'instance/mathquiz.db'  # Adjust for PythonAnywhere if needed

# Difficulty bands matching methodology
BANDS = {
    1: 'foundation', 2: 'foundation', 3: 'foundation',
    4: 'ordinary', 5: 'ordinary', 6: 'ordinary',
    7: 'ordinary', 8: 'ordinary',
    9: 'higher', 10: 'higher', 11: 'higher', 12: 'higher'
}

# ==================== CONTEXT DATA ====================
# Real-world contexts for engaging questions
CONTEXTS = {
    'sports': ['goals scored', 'points scored', 'matches won', 'races completed'],
    'school': ['test scores', 'books read', 'homework marks', 'attendance days'],
    'weather': ['temperatures (°C)', 'rainfall (mm)', 'sunny days', 'wind speed (km/h)'],
    'shopping': ['items sold', 'customers served', 'prices (€)', 'sales (€)'],
    'transport': ['journey times (min)', 'distances (km)', 'passengers', 'trips made'],
    'food': ['calories', 'portions sold', 'ingredients (g)', 'orders taken'],
    'animals': ['weights (kg)', 'heights (cm)', 'ages (years)', 'speeds (km/h)'],
    'technology': ['downloads', 'screen time (min)', 'messages sent', 'battery (%)']
}

PEOPLE_NAMES = ['Emma', 'Liam', 'Aoife', 'Cian', 'Sophie', 'Jack', 'Niamh', 'Sean', 
                'Grace', 'Conor', 'Ella', 'Dylan', 'Ava', 'Oisin', 'Mia', 'Fionn',
                'Sarah', 'James', 'Katie', 'Ryan', 'Lucy', 'Adam', 'Holly', 'Ben']

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# ==================== SVG GENERATORS ====================

def generate_bar_chart_svg(labels, values, title="", color='#3b82f6'):
    """Generate an SVG bar chart"""
    width = 280
    height = 180
    margin = {'top': 30, 'right': 20, 'bottom': 40, 'left': 40}
    chart_width = width - margin['left'] - margin['right']
    chart_height = height - margin['top'] - margin['bottom']
    
    max_val = max(values) if values else 1
    bar_width = chart_width / len(values) * 0.7
    gap = chart_width / len(values) * 0.3
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#f8fafc"/>'
    
    # Title
    if title:
        svg += f'<text x="{width/2}" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">{title}</text>'
    
    # Y-axis
    svg += f'<line x1="{margin["left"]}" y1="{margin["top"]}" x2="{margin["left"]}" y2="{height-margin["bottom"]}" stroke="#94a3b8" stroke-width="1"/>'
    
    # X-axis
    svg += f'<line x1="{margin["left"]}" y1="{height-margin["bottom"]}" x2="{width-margin["right"]}" y2="{height-margin["bottom"]}" stroke="#94a3b8" stroke-width="1"/>'
    
    # Bars and labels
    for i, (label, value) in enumerate(zip(labels, values)):
        bar_height = (value / max_val) * chart_height if max_val > 0 else 0
        x = margin['left'] + i * (bar_width + gap) + gap/2
        y = height - margin['bottom'] - bar_height
        
        svg += f'<rect x="{x}" y="{y}" width="{bar_width}" height="{bar_height}" fill="{color}" rx="2"/>'
        svg += f'<text x="{x + bar_width/2}" y="{height - margin["bottom"] + 15}" text-anchor="middle" font-size="9" fill="#64748b">{label}</text>'
        svg += f'<text x="{x + bar_width/2}" y="{y - 5}" text-anchor="middle" font-size="9" fill="#1e293b">{value}</text>'
    
    svg += '</svg>'
    return svg


def generate_pictogram_svg(labels, values, symbol='●', title=""):
    """Generate an SVG pictogram (each symbol = 1 unit)"""
    width = 280
    row_height = 25
    height = 40 + len(labels) * row_height
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#f8fafc"/>'
    
    if title:
        svg += f'<text x="{width/2}" y="18" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e293b">{title}</text>'
    
    for i, (label, value) in enumerate(zip(labels, values)):
        y = 35 + i * row_height
        svg += f'<text x="10" y="{y}" font-size="10" fill="#1e293b">{label}</text>'
        
        # Draw symbols
        symbols = symbol * min(value, 15)  # Cap at 15 for display
        if value > 15:
            symbols += '...'
        svg += f'<text x="80" y="{y}" font-size="12" fill="#3b82f6">{symbols}</text>'
        svg += f'<text x="260" y="{y}" font-size="10" fill="#64748b">({value})</text>'
    
    svg += '</svg>'
    return svg


def generate_tally_chart_svg(labels, values, title=""):
    """Generate an SVG tally chart"""
    width = 260
    row_height = 28
    height = 50 + len(labels) * row_height
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#ffffff" stroke="#e2e8f0"/>'
    
    if title:
        svg += f'<text x="{width/2}" y="18" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e293b">{title}</text>'
    
    # Header row
    svg += f'<rect x="0" y="28" width="{width}" height="22" fill="#f1f5f9"/>'
    svg += f'<text x="50" y="43" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e293b">Item</text>'
    svg += f'<text x="150" y="43" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e293b">Tally</text>'
    svg += f'<text x="230" y="43" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e293b">Total</text>'
    
    for i, (label, value) in enumerate(zip(labels, values)):
        y = 65 + i * row_height
        
        # Row background
        if i % 2 == 0:
            svg += f'<rect x="0" y="{y-15}" width="{width}" height="{row_height}" fill="#f8fafc"/>'
        
        svg += f'<text x="50" y="{y}" text-anchor="middle" font-size="10" fill="#1e293b">{label}</text>'
        
        # Tally marks
        tally = ''
        full_groups = value // 5
        remainder = value % 5
        for g in range(min(full_groups, 3)):  # Max 3 groups for display
            tally += '||||̷ '  # 5 marks with strikethrough
        if full_groups > 3:
            tally += '... '
        tally += '|' * remainder
        
        svg += f'<text x="150" y="{y}" text-anchor="middle" font-size="11" fill="#3b82f6" font-family="monospace">{tally}</text>'
        svg += f'<text x="230" y="{y}" text-anchor="middle" font-size="10" fill="#1e293b">{value}</text>'
    
    svg += '</svg>'
    return svg


def generate_frequency_table_svg(values, frequencies, title="", x_label="Value"):
    """Generate an SVG frequency table"""
    width = 220
    row_height = 24
    height = 50 + (len(values) + 1) * row_height
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#ffffff"/>'
    
    if title:
        svg += f'<text x="{width/2}" y="18" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e293b">{title}</text>'
    
    # Table border
    table_y = 30
    table_height = (len(values) + 1) * row_height
    svg += f'<rect x="10" y="{table_y}" width="200" height="{table_height}" fill="none" stroke="#cbd5e1" stroke-width="1"/>'
    
    # Header
    svg += f'<rect x="10" y="{table_y}" width="200" height="{row_height}" fill="#e2e8f0"/>'
    svg += f'<line x1="110" y1="{table_y}" x2="110" y2="{table_y + table_height}" stroke="#cbd5e1"/>'
    svg += f'<text x="60" y="{table_y + 16}" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e293b">{x_label}</text>'
    svg += f'<text x="160" y="{table_y + 16}" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e293b">Frequency</text>'
    
    # Data rows
    for i, (val, freq) in enumerate(zip(values, frequencies)):
        y = table_y + (i + 1) * row_height
        svg += f'<line x1="10" y1="{y}" x2="210" y2="{y}" stroke="#e2e8f0"/>'
        svg += f'<text x="60" y="{y + 16}" text-anchor="middle" font-size="10" fill="#1e293b">{val}</text>'
        svg += f'<text x="160" y="{y + 16}" text-anchor="middle" font-size="10" fill="#3b82f6">{freq}</text>'
    
    svg += '</svg>'
    return svg


def generate_histogram_svg(intervals, frequencies, title=""):
    """Generate an SVG histogram for grouped data"""
    width = 300
    height = 200
    margin = {'top': 35, 'right': 20, 'bottom': 50, 'left': 45}
    chart_width = width - margin['left'] - margin['right']
    chart_height = height - margin['top'] - margin['bottom']
    
    max_freq = max(frequencies) if frequencies else 1
    bar_width = chart_width / len(frequencies)
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#f8fafc"/>'
    
    if title:
        svg += f'<text x="{width/2}" y="20" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e293b">{title}</text>'
    
    # Y-axis
    svg += f'<line x1="{margin["left"]}" y1="{margin["top"]}" x2="{margin["left"]}" y2="{height-margin["bottom"]}" stroke="#64748b" stroke-width="1"/>'
    
    # X-axis  
    svg += f'<line x1="{margin["left"]}" y1="{height-margin["bottom"]}" x2="{width-margin["right"]}" y2="{height-margin["bottom"]}" stroke="#64748b" stroke-width="1"/>'
    
    # Y-axis label
    svg += f'<text x="15" y="{height/2}" text-anchor="middle" font-size="9" fill="#64748b" transform="rotate(-90, 15, {height/2})">Frequency</text>'
    
    # Y-axis ticks
    for i in range(5):
        y_val = max_freq * i / 4
        y_pos = height - margin['bottom'] - (chart_height * i / 4)
        svg += f'<text x="{margin["left"]-5}" y="{y_pos+3}" text-anchor="end" font-size="8" fill="#64748b">{int(y_val)}</text>'
        svg += f'<line x1="{margin["left"]}" y1="{y_pos}" x2="{margin["left"]+3}" y2="{y_pos}" stroke="#64748b"/>'
    
    # Bars (touching - histogram style)
    for i, (interval, freq) in enumerate(zip(intervals, frequencies)):
        bar_height = (freq / max_freq) * chart_height if max_freq > 0 else 0
        x = margin['left'] + i * bar_width
        y = height - margin['bottom'] - bar_height
        
        svg += f'<rect x="{x}" y="{y}" width="{bar_width}" height="{bar_height}" fill="#3b82f6" stroke="#1e40af" stroke-width="1"/>'
        
        # X-axis labels (intervals)
        svg += f'<text x="{x + bar_width/2}" y="{height - margin["bottom"] + 12}" text-anchor="middle" font-size="7" fill="#64748b">{interval}</text>'
    
    svg += '</svg>'
    return svg


def generate_stem_leaf_svg(data, title=""):
    """Generate an SVG stem-and-leaf diagram"""
    # Organize data
    stems = {}
    for val in sorted(data):
        stem = val // 10
        leaf = val % 10
        if stem not in stems:
            stems[stem] = []
        stems[stem].append(leaf)
    
    width = 200
    row_height = 22
    height = 60 + len(stems) * row_height
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#ffffff"/>'
    
    if title:
        svg += f'<text x="{width/2}" y="18" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e293b">{title}</text>'
    
    # Header
    svg += f'<text x="40" y="40" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e293b">Stem</text>'
    svg += f'<text x="130" y="40" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e293b">Leaf</text>'
    
    # Dividing line
    svg += f'<line x1="70" y1="28" x2="70" y2="{height-10}" stroke="#94a3b8" stroke-width="1"/>'
    
    # Data rows
    for i, stem in enumerate(sorted(stems.keys())):
        y = 60 + i * row_height
        leaves = ' '.join(str(l) for l in sorted(stems[stem]))
        svg += f'<text x="40" y="{y}" text-anchor="middle" font-size="11" fill="#1e293b">{stem}</text>'
        svg += f'<text x="80" y="{y}" font-size="11" fill="#3b82f6" font-family="monospace">{leaves}</text>'
    
    # Key
    svg += f'<text x="10" y="{height-5}" font-size="8" fill="#64748b">Key: 3|5 means 35</text>'
    
    svg += '</svg>'
    return svg


def generate_back_to_back_stem_leaf_svg(data_left, data_right, title_left="", title_right=""):
    """Generate back-to-back stem-and-leaf diagram"""
    # Organize both datasets
    all_data = data_left + data_right
    min_stem = min(d // 10 for d in all_data)
    max_stem = max(d // 10 for d in all_data)
    
    stems_left = {s: [] for s in range(min_stem, max_stem + 1)}
    stems_right = {s: [] for s in range(min_stem, max_stem + 1)}
    
    for val in data_left:
        stems_left[val // 10].append(val % 10)
    for val in data_right:
        stems_right[val // 10].append(val % 10)
    
    width = 280
    row_height = 22
    num_stems = max_stem - min_stem + 1
    height = 80 + num_stems * row_height
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#ffffff"/>'
    
    # Titles
    if title_left:
        svg += f'<text x="70" y="18" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e293b">{title_left}</text>'
    if title_right:
        svg += f'<text x="210" y="18" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e293b">{title_right}</text>'
    
    # Column headers
    svg += f'<text x="70" y="45" text-anchor="middle" font-size="9" fill="#64748b">Leaf</text>'
    svg += f'<text x="140" y="45" text-anchor="middle" font-size="9" fill="#64748b">Stem</text>'
    svg += f'<text x="210" y="45" text-anchor="middle" font-size="9" fill="#64748b">Leaf</text>'
    
    # Dividing lines
    svg += f'<line x1="120" y1="35" x2="120" y2="{height-20}" stroke="#94a3b8" stroke-width="1"/>'
    svg += f'<line x1="160" y1="35" x2="160" y2="{height-20}" stroke="#94a3b8" stroke-width="1"/>'
    
    # Data rows
    for i, stem in enumerate(range(min_stem, max_stem + 1)):
        y = 65 + i * row_height
        
        # Left leaves (reversed order, right-aligned)
        left_leaves = ' '.join(str(l) for l in sorted(stems_left[stem], reverse=True))
        svg += f'<text x="115" y="{y}" text-anchor="end" font-size="11" fill="#3b82f6" font-family="monospace">{left_leaves}</text>'
        
        # Stem
        svg += f'<text x="140" y="{y}" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e293b">{stem}</text>'
        
        # Right leaves
        right_leaves = ' '.join(str(l) for l in sorted(stems_right[stem]))
        svg += f'<text x="165" y="{y}" font-size="11" fill="#22c55e" font-family="monospace">{right_leaves}</text>'
    
    # Key
    svg += f'<text x="10" y="{height-5}" font-size="8" fill="#64748b">Key: 5 3|4 means 35 (left) and 34 (right)</text>'
    
    svg += '</svg>'
    return svg


def generate_data_table_svg(headers, rows, title=""):
    """Generate a simple data table SVG"""
    col_width = 50
    width = len(headers) * col_width + 20
    row_height = 24
    height = 40 + (len(rows) + 1) * row_height
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#ffffff"/>'
    
    if title:
        svg += f'<text x="{width/2}" y="18" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e293b">{title}</text>'
    
    table_y = 28
    
    # Header row
    svg += f'<rect x="10" y="{table_y}" width="{width-20}" height="{row_height}" fill="#e2e8f0"/>'
    for i, header in enumerate(headers):
        x = 10 + i * col_width + col_width/2
        svg += f'<text x="{x}" y="{table_y + 16}" text-anchor="middle" font-size="9" font-weight="bold" fill="#1e293b">{header}</text>'
    
    # Data rows
    for r, row in enumerate(rows):
        y = table_y + (r + 1) * row_height
        if r % 2 == 0:
            svg += f'<rect x="10" y="{y}" width="{width-20}" height="{row_height}" fill="#f8fafc"/>'
        for i, cell in enumerate(row):
            x = 10 + i * col_width + col_width/2
            svg += f'<text x="{x}" y="{y + 16}" text-anchor="middle" font-size="9" fill="#1e293b">{cell}</text>'
    
    # Border
    svg += f'<rect x="10" y="{table_y}" width="{width-20}" height="{(len(rows)+1)*row_height}" fill="none" stroke="#cbd5e1"/>'
    
    # Column lines
    for i in range(1, len(headers)):
        x = 10 + i * col_width
        svg += f'<line x1="{x}" y1="{table_y}" x2="{x}" y2="{table_y + (len(rows)+1)*row_height}" stroke="#e2e8f0"/>'
    
    svg += '</svg>'
    return svg


# ==================== HELPER FUNCTIONS ====================

def calculate_mean(data):
    """Calculate mean of a dataset"""
    return sum(data) / len(data) if data else 0


def calculate_median(data):
    """Calculate median of a dataset"""
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n == 0:
        return 0
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2


def calculate_mode(data):
    """Calculate mode of a dataset (returns list if multiple modes)"""
    if not data:
        return []
    counts = Counter(data)
    max_count = max(counts.values())
    modes = [val for val, count in counts.items() if count == max_count]
    return sorted(modes)


def calculate_range(data):
    """Calculate range of a dataset"""
    return max(data) - min(data) if data else 0


def generate_unique_options(correct, num_options=4, option_type='int', min_val=None, max_val=None):
    """Generate unique answer options including the correct answer"""
    options = [correct]
    attempts = 0
    max_attempts = 100
    
    while len(options) < num_options and attempts < max_attempts:
        attempts += 1
        
        if option_type == 'int':
            # Generate plausible wrong answers near the correct one
            offset = random.choice([-3, -2, -1, 1, 2, 3, -4, 4, -5, 5])
            wrong = correct + offset
            if min_val is not None:
                wrong = max(min_val, wrong)
            if max_val is not None:
                wrong = min(max_val, wrong)
        elif option_type == 'float':
            offset = random.choice([-2.5, -2, -1.5, -1, -0.5, 0.5, 1, 1.5, 2, 2.5])
            wrong = round(correct + offset, 1)
            if min_val is not None:
                wrong = max(min_val, wrong)
        else:
            wrong = correct + random.randint(-5, 5)
        
        if wrong not in options and wrong != correct:
            options.append(wrong)
    
    # Ensure we have exactly 4 options
    while len(options) < num_options:
        if option_type == 'float':
            wrong = round(correct + random.uniform(-5, 5), 1)
        else:
            wrong = correct + random.randint(-10, 10)
        if wrong not in options:
            options.append(wrong)
    
    random.shuffle(options)
    correct_idx = options.index(correct)
    
    return options, correct_idx


def format_number(n):
    """Format number for display (remove .0 from whole numbers)"""
    if isinstance(n, float) and n == int(n):
        return str(int(n))
    elif isinstance(n, float):
        return str(round(n, 2))
    return str(n)


# ==================== LEVEL GENERATORS ====================

def generate_level_1():
    """
    Level 1: Reading Data (tally charts, pictograms, bar charts)
    Foundation level - 75% visual
    SEC Style: Basic data reading from charts
    """
    questions = []
    
    # Type 1: Reading from bar charts (20 questions)
    for i in range(20):
        context = random.choice(list(CONTEXTS.keys()))
        data_type = random.choice(CONTEXTS[context])
        
        if context in ['sports', 'school']:
            labels = random.sample(DAYS[:5], 4)  # Weekdays
        else:
            labels = random.sample(['A', 'B', 'C', 'D', 'E'], 4)
        
        values = [random.randint(2, 15) for _ in range(4)]
        
        # Question types
        q_type = random.choice(['highest', 'lowest', 'total', 'specific'])
        
        if q_type == 'highest':
            max_idx = values.index(max(values))
            correct = labels[max_idx]
            question = f"The bar chart shows {data_type} for different {['days', 'categories'][context not in ['sports', 'school']]}. Which had the highest value?"
            options = labels.copy()
            random.shuffle(options)
            correct_idx = options.index(correct)
            explanation = f"Looking at the bar chart, {correct} has the tallest bar with a value of {max(values)}. This is the highest."
        
        elif q_type == 'lowest':
            min_idx = values.index(min(values))
            correct = labels[min_idx]
            question = f"The bar chart shows {data_type}. Which had the lowest value?"
            options = labels.copy()
            random.shuffle(options)
            correct_idx = options.index(correct)
            explanation = f"Looking at the bar chart, {correct} has the shortest bar with a value of {min(values)}. This is the lowest."
        
        elif q_type == 'total':
            correct = sum(values)
            question = f"The bar chart shows {data_type}. What is the total?"
            options, correct_idx = generate_unique_options(correct, min_val=1)
            options = [str(o) for o in options]
            explanation = f"Add all the values: {' + '.join(map(str, values))} = {correct}"
        
        else:  # specific
            idx = random.randint(0, len(labels)-1)
            correct = values[idx]
            question = f"The bar chart shows {data_type}. What is the value for {labels[idx]}?"
            options, correct_idx = generate_unique_options(correct, min_val=0)
            options = [str(o) for o in options]
            explanation = f"Reading from the bar chart, the bar for {labels[idx]} shows a value of {correct}."
        
        svg = generate_bar_chart_svg(labels, values, title=data_type.title())
        
        questions.append({
            'question_text': question,
            'option_a': str(options[0]),
            'option_b': str(options[1]),
            'option_c': str(options[2]),
            'option_d': str(options[3]),
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 1,
            'difficulty_band': BANDS[1],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': svg
        })
    
    # Type 2: Reading from tally charts (15 questions)
    for i in range(15):
        items = random.sample(['Red', 'Blue', 'Green', 'Yellow', 'Orange'], 4)
        values = [random.randint(3, 12) for _ in range(4)]
        
        q_type = random.choice(['total', 'most', 'specific', 'difference'])
        
        if q_type == 'total':
            correct = sum(values)
            question = "The tally chart shows favourite colours. How many people were surveyed in total?"
            options, correct_idx = generate_unique_options(correct, min_val=1)
            explanation = f"Add all frequencies: {' + '.join(map(str, values))} = {correct}"
        
        elif q_type == 'most':
            max_idx = values.index(max(values))
            correct = items[max_idx]
            question = "The tally chart shows favourite colours. Which colour was most popular?"
            options = items.copy()
            random.shuffle(options)
            correct_idx = options.index(correct)
            explanation = f"{correct} has the most tally marks ({max(values)}), so it is the most popular."
        
        elif q_type == 'specific':
            idx = random.randint(0, 3)
            correct = values[idx]
            question = f"The tally chart shows favourite colours. How many people chose {items[idx]}?"
            options, correct_idx = generate_unique_options(correct, min_val=0)
            explanation = f"Count the tally marks for {items[idx]}: there are {correct} marks."
        
        else:  # difference
            idx1, idx2 = random.sample(range(4), 2)
            correct = abs(values[idx1] - values[idx2])
            question = f"The tally chart shows favourite colours. What is the difference between {items[idx1]} and {items[idx2]}?"
            options, correct_idx = generate_unique_options(correct, min_val=0)
            explanation = f"Difference = |{values[idx1]} - {values[idx2]}| = {correct}"
        
        svg = generate_tally_chart_svg(items, values, title="Favourite Colours")
        options = [str(o) for o in options]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 1,
            'difficulty_band': BANDS[1],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': svg
        })
    
    # Type 3: Reading from pictograms (15 questions)
    for i in range(15):
        names = random.sample(PEOPLE_NAMES, 4)
        values = [random.randint(2, 8) for _ in range(4)]
        data_type = random.choice(['books read', 'goals scored', 'stars earned', 'stickers collected'])
        
        q_type = random.choice(['total', 'who_most', 'how_many', 'combined'])
        
        if q_type == 'total':
            correct = sum(values)
            question = f"The pictogram shows {data_type} by different students. What is the total?"
            options, correct_idx = generate_unique_options(correct, min_val=1)
            explanation = f"Add all values: {' + '.join(map(str, values))} = {correct}"
        
        elif q_type == 'who_most':
            max_idx = values.index(max(values))
            correct = names[max_idx]
            question = f"The pictogram shows {data_type}. Who had the most?"
            options = names.copy()
            random.shuffle(options)
            correct_idx = options.index(correct)
            explanation = f"{correct} has the most symbols ({max(values)}), so they had the most {data_type}."
        
        elif q_type == 'how_many':
            idx = random.randint(0, 3)
            correct = values[idx]
            question = f"The pictogram shows {data_type}. How many did {names[idx]} have?"
            options, correct_idx = generate_unique_options(correct, min_val=0)
            explanation = f"Count the symbols for {names[idx]}: there are {correct}."
        
        else:  # combined
            idx1, idx2 = random.sample(range(4), 2)
            correct = values[idx1] + values[idx2]
            question = f"The pictogram shows {data_type}. How many did {names[idx1]} and {names[idx2]} have together?"
            options, correct_idx = generate_unique_options(correct, min_val=1)
            explanation = f"{names[idx1]} + {names[idx2]} = {values[idx1]} + {values[idx2]} = {correct}"
        
        svg = generate_pictogram_svg(names, values, symbol='★', title=data_type.title())
        options = [str(o) for o in options]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 1,
            'difficulty_band': BANDS[1],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_2():
    """
    Level 2: Mode from Lists & Tables
    Foundation level - 75% visual
    SEC Style: "Find the mode" from datasets
    """
    questions = []
    
    # Type 1: Mode from simple lists with visual (25 questions)
    for i in range(25):
        # Create dataset with clear mode
        base_values = list(range(1, 8))
        mode_value = random.choice(base_values)
        data = [mode_value] * random.randint(3, 5)  # Mode appears 3-5 times
        
        # Add other values (appearing less frequently)
        for v in base_values:
            if v != mode_value:
                data.extend([v] * random.randint(1, 2))
        
        random.shuffle(data)
        data = data[:random.randint(8, 12)]  # Limit size
        
        # Ensure mode is unique
        counts = Counter(data)
        mode_count = counts[mode_value]
        for v in counts:
            if v != mode_value and counts[v] >= mode_count:
                # Remove some to ensure unique mode
                while counts[v] >= mode_count:
                    data.remove(v)
                    counts[v] -= 1
        
        correct = mode_value
        context = random.choice(['test scores', 'shoe sizes', 'ages', 'number of pets', 'goals scored'])
        
        question = f"Find the mode of the following {context}:\n{', '.join(map(str, data))}"
        options, correct_idx = generate_unique_options(correct, min_val=min(data), max_val=max(data))
        
        counts = Counter(data)
        explanation = f"The mode is the most frequent value.\nCounting each value:\n"
        for v in sorted(set(data)):
            explanation += f"  {v} appears {counts[v]} time(s)\n"
        explanation += f"The mode is {correct} (appears {counts[correct]} times - the most)."
        
        # Create frequency table visual
        unique_vals = sorted(set(data))
        freqs = [counts[v] for v in unique_vals]
        svg = generate_frequency_table_svg(unique_vals, freqs, title=context.title())
        options = [str(o) for o in options]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 2,
            'difficulty_band': BANDS[2],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': svg
        })
    
    # Type 2: Mode from frequency tables (15 questions)
    for i in range(15):
        values = list(range(random.randint(1, 3), random.randint(6, 9)))
        frequencies = [random.randint(2, 8) for _ in values]
        
        # Ensure unique mode
        max_freq = max(frequencies)
        mode_idx = frequencies.index(max_freq)
        for j in range(len(frequencies)):
            if j != mode_idx and frequencies[j] == max_freq:
                frequencies[j] -= 1
        
        correct = values[frequencies.index(max(frequencies))]
        context = random.choice(['number of siblings', 'hours of sleep', 'books read', 'cinema visits'])
        
        question = f"The frequency table shows {context} for a group of students. What is the mode?"
        options, correct_idx = generate_unique_options(correct, min_val=min(values), max_val=max(values))
        
        explanation = f"The mode is the value with the highest frequency.\n"
        for v, f in zip(values, frequencies):
            marker = " ← highest" if f == max(frequencies) else ""
            explanation += f"  {v}: frequency {f}{marker}\n"
        explanation += f"The mode is {correct} (frequency = {max(frequencies)})."
        
        svg = generate_frequency_table_svg(values, frequencies, title=context.title())
        options = [str(o) for o in options]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 2,
            'difficulty_band': BANDS[2],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': svg
        })
    
    # Type 3: Mode word problems (10 questions)
    for i in range(10):
        name = random.choice(PEOPLE_NAMES)
        context_data = [
            ('dice rolls', list(range(1, 7)), 'dice'),
            ('spelling test scores', list(range(5, 11)), 'test'),
            ('number of messages received', list(range(0, 8)), 'messages'),
        ]
        context, possible_vals, ctx_word = random.choice(context_data)
        
        mode_val = random.choice(possible_vals)
        data = [mode_val] * random.randint(4, 6)
        for v in possible_vals:
            if v != mode_val:
                data.extend([v] * random.randint(1, 3))
        random.shuffle(data)
        data = data[:10]
        
        # Ensure unique mode
        counts = Counter(data)
        if counts[mode_val] <= max(c for v, c in counts.items() if v != mode_val):
            data.append(mode_val)
            data.append(mode_val)
        
        correct = mode_val
        question = f"{name} recorded their {context} over several days: {', '.join(map(str, data))}. What is the mode?"
        options, correct_idx = generate_unique_options(correct, min_val=min(data), max_val=max(data))
        
        counts = Counter(data)
        explanation = f"Mode = most frequent value.\n"
        explanation += f"Frequency count: "
        explanation += ', '.join([f"{v}:{counts[v]}" for v in sorted(set(data))])
        explanation += f"\nThe mode is {correct} (appears most often)."
        
        options = [str(o) for o in options]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 2,
            'difficulty_band': BANDS[2],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': None
        })
    
    return questions


def generate_level_3():
    """
    Level 3: Range from Lists & Tables
    Foundation level - 75% visual
    SEC Style: "Find the range" - OL Q5/Q6
    """
    questions = []
    
    # Type 1: Range from simple lists (20 questions)
    for i in range(20):
        min_val = random.randint(1, 20)
        max_val = min_val + random.randint(5, 25)
        
        # Generate data between min and max
        data = [min_val, max_val]
        for _ in range(random.randint(4, 8)):
            data.append(random.randint(min_val, max_val))
        random.shuffle(data)
        
        correct = max_val - min_val
        context = random.choice(['temperatures (°C)', 'test scores', 'heights (cm)', 'ages', 'prices (€)'])
        
        question = f"Find the range of the following {context}:\n{', '.join(map(str, data))}"
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        explanation = f"Range = Maximum - Minimum\n"
        explanation += f"Maximum = {max_val}\n"
        explanation += f"Minimum = {min_val}\n"
        explanation += f"Range = {max_val} - {min_val} = {correct}"
        
        # Create bar chart visual
        labels = [f"D{j+1}" for j in range(len(data))]
        svg = generate_bar_chart_svg(labels, data, title=context.title())
        options = [str(o) for o in options]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 3,
            'difficulty_band': BANDS[3],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': svg
        })
    
    # Type 2: Range from tables (20 questions)
    for i in range(20):
        names = random.sample(PEOPLE_NAMES, 5)
        min_val = random.randint(10, 50)
        max_val = min_val + random.randint(10, 30)
        
        values = [min_val, max_val]
        for _ in range(3):
            values.append(random.randint(min_val, max_val))
        random.shuffle(values)
        
        correct = max_val - min_val
        context = random.choice(['scores', 'heights (cm)', 'times (sec)', 'distances (m)'])
        
        question = f"The table shows {context} for 5 students. Find the range."
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        explanation = f"Range = Maximum - Minimum\n"
        explanation += f"From the table: Maximum = {max_val}, Minimum = {min_val}\n"
        explanation += f"Range = {max_val} - {min_val} = {correct}"
        
        # Create table visual
        headers = ['Name'] + names
        rows = [[context.split()[0].title()] + values]
        svg = generate_data_table_svg(['Name', context.title()], [[n, v] for n, v in zip(names, values)])
        options = [str(o) for o in options]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 3,
            'difficulty_band': BANDS[3],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': svg
        })
    
    # Type 3: Range word problems (10 questions)
    for i in range(10):
        scenarios = [
            ("The temperatures in Dublin last week were", "°C", (-2, 15)),
            ("A shop recorded daily sales of", "items", (20, 80)),
            ("Journey times to school were", "minutes", (5, 35)),
            ("Heights of plants in a garden are", "cm", (10, 45)),
        ]
        
        context, unit, (lo, hi) = random.choice(scenarios)
        min_val = random.randint(lo, lo + 5)
        max_val = random.randint(hi - 5, hi)
        
        data = [min_val, max_val]
        for _ in range(random.randint(3, 5)):
            data.append(random.randint(min_val, max_val))
        random.shuffle(data)
        
        correct = max_val - min_val
        data_str = ', '.join([f"{d}{unit}" if unit != 'items' else str(d) for d in data])
        
        question = f"{context}: {data_str}. Calculate the range."
        options, correct_idx = generate_unique_options(correct, min_val=1)
        
        explanation = f"Range = Highest - Lowest\n"
        explanation += f"Highest = {max_val}{unit if unit != 'items' else ''}\n"
        explanation += f"Lowest = {min_val}{unit if unit != 'items' else ''}\n"
        explanation += f"Range = {max_val} - {min_val} = {correct}{unit if unit != 'items' else ''}"
        
        options = [str(o) for o in options]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 3,
            'difficulty_band': BANDS[3],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': None
        })
    
    return questions


def generate_level_4():
    """
    Level 4: Median (odd number of values)
    Ordinary level - 75% visual
    SEC Style: "Find the median" - OL Q6
    """
    questions = []
    
    for i in range(50):
        # Generate odd-sized dataset (5, 7, 9, or 11 values)
        n = random.choice([5, 7, 9, 11])
        
        # Generate data ensuring variety
        base = random.randint(1, 20)
        data = [base + random.randint(0, 20) for _ in range(n)]
        
        sorted_data = sorted(data)
        median_pos = n // 2
        correct = sorted_data[median_pos]
        
        context = random.choice(['test scores', 'ages', 'heights (cm)', 'weights (kg)', 'prices (€)'])
        
        # Vary question format
        if i < 25:
            # With visual
            question = f"Find the median of these {n} {context}:\n{', '.join(map(str, data))}"
            
            # Create frequency table or bar chart
            if random.random() < 0.5:
                labels = [f"V{j+1}" for j in range(n)]
                svg = generate_bar_chart_svg(labels, data, title=f"{context.title()}")
            else:
                unique_vals = sorted(set(data))
                counts = Counter(data)
                freqs = [counts[v] for v in unique_vals]
                svg = generate_frequency_table_svg(unique_vals, freqs, title=context.title())
        else:
            # Word problem style
            name = random.choice(PEOPLE_NAMES)
            question = f"{name} recorded {n} {context}: {', '.join(map(str, data))}. What is the median?"
            svg = None
        
        options, correct_idx = generate_unique_options(correct, min_val=min(data), max_val=max(data))
        
        explanation = f"To find the median:\n"
        explanation += f"1. Arrange in order: {', '.join(map(str, sorted_data))}\n"
        explanation += f"2. With {n} values, the median is the {median_pos + 1}th value (middle)\n"
        explanation += f"3. Median = {correct}"
        
        options = [str(o) for o in options]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 4,
            'difficulty_band': BANDS[4],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_5():
    """
    Level 5: Median (even number of values - average of two middle)
    Ordinary level - 75% visual
    SEC Style: Finding median with even datasets
    """
    questions = []
    
    for i in range(50):
        # Generate even-sized dataset (6, 8, 10, or 12 values)
        n = random.choice([6, 8, 10, 12])
        
        base = random.randint(1, 20)
        data = [base + random.randint(0, 20) for _ in range(n)]
        
        sorted_data = sorted(data)
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        correct = (mid1 + mid2) / 2
        
        context = random.choice(['scores', 'temperatures (°C)', 'waiting times (min)', 'distances (km)'])
        
        if i < 38:  # 75% visual
            question = f"Find the median of these {n} {context}:\n{', '.join(map(str, data))}"
            labels = [f"D{j+1}" for j in range(n)]
            svg = generate_bar_chart_svg(labels, data, title=context.title())
        else:
            name = random.choice(PEOPLE_NAMES)
            question = f"{name}'s {n} {context} were: {', '.join(map(str, data))}. Calculate the median."
            svg = None
        
        # Format correct answer
        if correct == int(correct):
            correct_display = int(correct)
        else:
            correct_display = correct
        
        options, correct_idx = generate_unique_options(correct, option_type='float', min_val=min(data))
        options = [format_number(o) for o in options]
        
        explanation = f"To find the median with {n} (even) values:\n"
        explanation += f"1. Arrange in order: {', '.join(map(str, sorted_data))}\n"
        explanation += f"2. Find the two middle values (positions {n//2} and {n//2 + 1})\n"
        explanation += f"3. Middle values: {mid1} and {mid2}\n"
        explanation += f"4. Median = ({mid1} + {mid2}) ÷ 2 = {mid1 + mid2} ÷ 2 = {format_number(correct)}"
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 5,
            'difficulty_band': BANDS[5],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_6():
    """
    Level 6: Mean (simple averages)
    Ordinary level - 75% visual
    SEC Style: "Work out the mean" - OL Q5, Q6
    """
    questions = []
    
    for i in range(50):
        # Generate dataset for clean mean calculations
        n = random.choice([4, 5, 6, 8, 10])
        
        # Create data that gives reasonable mean
        target_mean = random.randint(5, 25)
        data = [target_mean + random.randint(-5, 5) for _ in range(n)]
        
        # Adjust last value to get cleaner mean if possible
        current_sum = sum(data)
        if current_sum % n != 0:
            adjustment = n - (current_sum % n)
            if adjustment <= 5:
                data[-1] += adjustment
        
        total = sum(data)
        correct = total / n
        
        context = random.choice(['test scores', 'ages', 'heights (cm)', 'daily steps (thousands)', 'hours worked'])
        
        if i < 38:  # 75% visual
            question = f"Calculate the mean of these {n} {context}:\n{', '.join(map(str, data))}"
            labels = random.sample(PEOPLE_NAMES, n) if n <= 8 else [f"D{j+1}" for j in range(n)]
            svg = generate_bar_chart_svg(labels, data, title=f"Mean {context.title()}")
        else:
            names_sample = random.sample(PEOPLE_NAMES, n) if n <= 8 else [f"Student {j+1}" for j in range(n)]
            question = f"The {context} for {n} people were: {', '.join(map(str, data))}. Find the mean."
            svg = None
        
        # Format answer
        if correct == int(correct):
            correct_display = int(correct)
            options, correct_idx = generate_unique_options(int(correct), min_val=1)
        else:
            correct_display = round(correct, 1)
            options, correct_idx = generate_unique_options(correct, option_type='float', min_val=1)
        
        options = [format_number(o) for o in options]
        
        explanation = f"Mean = Sum ÷ Count\n"
        explanation += f"Sum = {' + '.join(map(str, data))} = {total}\n"
        explanation += f"Count = {n}\n"
        explanation += f"Mean = {total} ÷ {n} = {format_number(correct)}"
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 6,
            'difficulty_band': BANDS[6],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_7():
    """
    Level 7: Frequency Tables (reading & creating)
    Ordinary level - 75% visual
    SEC Style: "Complete the frequency table" - OL Q5
    """
    questions = []
    
    # Type 1: Reading frequency tables (25 questions)
    for i in range(25):
        values = list(range(random.randint(0, 2), random.randint(5, 8)))
        frequencies = [random.randint(2, 10) for _ in values]
        total_freq = sum(frequencies)
        
        context = random.choice(['number of pets', 'siblings', 'goals scored', 'absences', 'books read'])
        
        q_type = random.choice(['total', 'most_common', 'how_many', 'at_least'])
        
        if q_type == 'total':
            correct = total_freq
            question = f"The frequency table shows {context}. How many people were surveyed?"
            explanation = f"Total = sum of all frequencies\n"
            explanation += f"Total = {' + '.join(map(str, frequencies))} = {correct}"
        
        elif q_type == 'most_common':
            max_freq = max(frequencies)
            correct = values[frequencies.index(max_freq)]
            question = f"The frequency table shows {context}. What is the most common value?"
            explanation = f"Find the value with highest frequency.\n"
            explanation += f"Highest frequency is {max_freq}, which corresponds to value {correct}."
        
        elif q_type == 'how_many':
            idx = random.randint(0, len(values) - 1)
            correct = frequencies[idx]
            question = f"The frequency table shows {context}. How many people have exactly {values[idx]}?"
            explanation = f"Read the frequency for value {values[idx]}.\n"
            explanation += f"Frequency = {correct}"
        
        else:  # at_least
            threshold = random.choice(values[1:]) if len(values) > 1 else values[0]
            correct = sum(f for v, f in zip(values, frequencies) if v >= threshold)
            question = f"The frequency table shows {context}. How many have {threshold} or more?"
            explanation = f"Add frequencies for values ≥ {threshold}:\n"
            parts = [f"{f}" for v, f in zip(values, frequencies) if v >= threshold]
            explanation += f"{' + '.join(parts)} = {correct}"
        
        options, correct_idx = generate_unique_options(correct, min_val=0)
        options = [str(o) for o in options]
        
        svg = generate_frequency_table_svg(values, frequencies, title=context.title())
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 7,
            'difficulty_band': BANDS[7],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': svg
        })
    
    # Type 2: Creating/completing frequency tables (25 questions)
    for i in range(25):
        # Generate raw data
        values_range = list(range(random.randint(1, 3), random.randint(6, 9)))
        raw_data = []
        for _ in range(random.randint(15, 25)):
            raw_data.append(random.choice(values_range))
        
        counts = Counter(raw_data)
        
        # Pick one value to find frequency for
        target_val = random.choice(list(counts.keys()))
        correct = counts[target_val]
        
        context = random.choice(['shoe sizes', 'dice rolls', 'quiz scores', 'family sizes'])
        
        question = f"The data shows {context}:\n{', '.join(map(str, raw_data))}\n\nWhat is the frequency for {target_val}?"
        
        options, correct_idx = generate_unique_options(correct, min_val=0)
        options = [str(o) for o in options]
        
        explanation = f"Count how many times {target_val} appears in the data.\n"
        explanation += f"Going through the list: {target_val} appears {correct} times."
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 7,
            'difficulty_band': BANDS[7],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': None
        })
    
    return questions


def generate_level_8():
    """
    Level 8: Mean from Frequency Tables
    Ordinary level - 75% visual
    SEC Style: Calculate mean using Σfx ÷ Σf
    """
    questions = []
    
    for i in range(50):
        # Generate frequency table
        values = list(range(random.randint(0, 2), random.randint(5, 8)))
        frequencies = [random.randint(2, 8) for _ in values]
        
        # Calculate mean
        fx_sum = sum(v * f for v, f in zip(values, frequencies))
        f_sum = sum(frequencies)
        correct = fx_sum / f_sum
        
        context = random.choice(['number of children', 'cars per household', 'days absent', 
                                 'books borrowed', 'goals per match'])
        
        if i < 38:  # 75% visual
            question = f"The frequency table shows {context} for {f_sum} families. Calculate the mean."
            svg = generate_frequency_table_svg(values, frequencies, title=context.title(), x_label=context.split()[0].title())
        else:
            # Text-only format with table in question
            table_str = " | ".join([f"{v}:{f}" for v, f in zip(values, frequencies)])
            question = f"For {context}, the data is (value:frequency): {table_str}. Find the mean."
            svg = None
        
        # Round appropriately
        if correct == int(correct):
            options, correct_idx = generate_unique_options(int(correct), min_val=0)
        else:
            correct = round(correct, 2)
            options, correct_idx = generate_unique_options(correct, option_type='float', min_val=0)
        
        options = [format_number(o) for o in options]
        
        explanation = f"Mean from frequency table = Σ(f × x) ÷ Σf\n\n"
        explanation += "Calculate f × x for each value:\n"
        for v, f in zip(values, frequencies):
            explanation += f"  {v} × {f} = {v * f}\n"
        explanation += f"\nΣ(f × x) = {fx_sum}\n"
        explanation += f"Σf = {f_sum}\n"
        explanation += f"Mean = {fx_sum} ÷ {f_sum} = {format_number(fx_sum / f_sum)}"
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 8,
            'difficulty_band': BANDS[8],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_9():
    """
    Level 9: Histograms & Grouped Data
    Higher level - 75% visual
    SEC Style: "Complete the histogram", "Which interval contains median?" - OL Q3, Q4
    """
    questions = []
    
    # Common interval patterns
    interval_patterns = [
        [(0, 10), (10, 20), (20, 30), (30, 40), (40, 50)],
        [(0, 5), (5, 10), (10, 15), (15, 20), (20, 25)],
        [(0, 20), (20, 40), (40, 60), (60, 80), (80, 100)],
        [(10, 20), (20, 30), (30, 40), (40, 50), (50, 60)],
    ]
    
    for i in range(50):
        intervals_bounds = random.choice(interval_patterns)
        intervals = [f"{a}-{b}" for a, b in intervals_bounds]
        frequencies = [random.randint(3, 15) for _ in intervals]
        total = sum(frequencies)
        
        context = random.choice(['journey times (min)', 'test scores', 'ages', 'waiting times (min)', 'distances (km)'])
        
        q_type = random.choice(['total', 'median_interval', 'modal_class', 'proportion'])
        
        if q_type == 'total':
            correct = total
            question = f"The histogram shows {context}. How many items of data are there in total?"
            options, correct_idx = generate_unique_options(correct, min_val=10)
            explanation = f"Total = sum of all frequencies\n"
            explanation += f"Total = {' + '.join(map(str, frequencies))} = {correct}"
        
        elif q_type == 'median_interval':
            # Find which interval contains median
            median_pos = (total + 1) / 2
            cumulative = 0
            median_interval_idx = 0
            for idx, f in enumerate(frequencies):
                cumulative += f
                if cumulative >= median_pos:
                    median_interval_idx = idx
                    break
            
            correct = intervals[median_interval_idx]
            question = f"The histogram shows {context} for {total} people. Which interval contains the median?"
            
            # Create 4 options including the correct one
            other_intervals = [iv for iv in intervals if iv != correct]
            wrong_options = random.sample(other_intervals, 3)
            options = [correct] + wrong_options
            random.shuffle(options)
            correct_idx = options.index(correct)
            
            explanation = f"Median position = ({total} + 1) ÷ 2 = {median_pos}\n"
            explanation += "Cumulative frequencies:\n"
            cum = 0
            for interval, f in zip(intervals, frequencies):
                cum += f
                marker = " ← median is here" if cum >= median_pos and cum - f < median_pos else ""
                explanation += f"  {interval}: {cum}{marker}\n"
            explanation += f"Median is in interval {correct}"
        
        elif q_type == 'modal_class':
            max_freq = max(frequencies)
            correct = intervals[frequencies.index(max_freq)]
            question = f"The histogram shows {context}. What is the modal class?"
            
            # Create 4 options including the correct one
            other_intervals = [iv for iv in intervals if iv != correct]
            wrong_options = random.sample(other_intervals, 3)
            options = [correct] + wrong_options
            random.shuffle(options)
            correct_idx = options.index(correct)
            
            explanation = f"Modal class = interval with highest frequency\n"
            for interval, f in zip(intervals, frequencies):
                marker = " ← highest" if f == max_freq else ""
                explanation += f"  {interval}: {f}{marker}\n"
            explanation += f"Modal class is {correct}"
            options = [str(o) for o in options]
        
        else:  # proportion
            idx = random.randint(0, len(intervals) - 1)
            correct = frequencies[idx]
            question = f"The histogram shows {context}. How many are in the {intervals[idx]} interval?"
            options, correct_idx = generate_unique_options(correct, min_val=0)
            explanation = f"Read the frequency for interval {intervals[idx]} from the histogram.\n"
            explanation += f"Frequency = {correct}"
            options = [str(o) for o in options]
        svg = generate_histogram_svg(intervals, frequencies, title=context.title())
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 9,
            'difficulty_band': BANDS[9],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_10():
    """
    Level 10: Stem-and-Leaf Diagrams
    Higher level - 75% visual
    SEC Style: "Find the median" from stem-and-leaf - HL Q2
    """
    questions = []
    
    for i in range(50):
        # Generate data for stem-and-leaf
        n = random.randint(10, 18)
        base = random.randint(20, 50)
        data = [base + random.randint(-15, 25) for _ in range(n)]
        data = [max(10, min(99, d)) for d in data]  # Keep 2-digit
        
        sorted_data = sorted(data)
        
        q_type = random.choice(['median', 'range', 'mode', 'count', 'smallest', 'largest'])
        
        context = random.choice(['test scores', 'ages', 'heights (cm)', 'reaction times (ms)'])
        
        if q_type == 'median':
            if n % 2 == 1:
                correct = sorted_data[n // 2]
            else:
                correct = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
            question = f"The stem-and-leaf diagram shows {context} for {n} students. Find the median."
            
            if correct == int(correct):
                options, correct_idx = generate_unique_options(int(correct), min_val=min(data), max_val=max(data))
            else:
                options, correct_idx = generate_unique_options(correct, option_type='float', min_val=min(data))
            
            explanation = f"With {n} values, "
            if n % 2 == 1:
                explanation += f"median is the {n//2 + 1}th value.\n"
                explanation += f"Ordered: {', '.join(map(str, sorted_data))}\n"
                explanation += f"Median = {format_number(correct)}"
            else:
                explanation += f"median is average of {n//2}th and {n//2 + 1}th values.\n"
                explanation += f"Middle values: {sorted_data[n//2 - 1]} and {sorted_data[n//2]}\n"
                explanation += f"Median = ({sorted_data[n//2 - 1]} + {sorted_data[n//2]}) ÷ 2 = {format_number(correct)}"
        
        elif q_type == 'range':
            correct = max(data) - min(data)
            question = f"The stem-and-leaf diagram shows {context}. Find the range."
            options, correct_idx = generate_unique_options(correct, min_val=1)
            explanation = f"Range = Maximum - Minimum\n"
            explanation += f"Maximum = {max(data)}, Minimum = {min(data)}\n"
            explanation += f"Range = {max(data)} - {min(data)} = {correct}"
        
        elif q_type == 'mode':
            counts = Counter(data)
            max_count = max(counts.values())
            modes = [v for v, c in counts.items() if c == max_count]
            correct = modes[0]
            question = f"The stem-and-leaf diagram shows {context}. Find the mode."
            options, correct_idx = generate_unique_options(correct, min_val=min(data), max_val=max(data))
            explanation = f"Mode = most frequent value\n"
            explanation += f"{correct} appears {max_count} times (most frequent)."
        
        elif q_type == 'count':
            correct = n
            question = f"The stem-and-leaf diagram shows {context}. How many values are shown?"
            options, correct_idx = generate_unique_options(correct, min_val=5, max_val=25)
            explanation = f"Count all the leaves in the diagram.\n"
            explanation += f"Total number of values = {correct}"
        
        elif q_type == 'smallest':
            correct = min(data)
            question = f"The stem-and-leaf diagram shows {context}. What is the smallest value?"
            options, correct_idx = generate_unique_options(correct, min_val=min(data)-10, max_val=min(data)+10)
            explanation = f"Look at the first stem with leaves.\n"
            explanation += f"Smallest value = {correct}"
        
        else:  # largest
            correct = max(data)
            question = f"The stem-and-leaf diagram shows {context}. What is the largest value?"
            options, correct_idx = generate_unique_options(correct, min_val=max(data)-10, max_val=max(data)+10)
            explanation = f"Look at the last stem with leaves.\n"
            explanation += f"Largest value = {correct}"
        
        options = [format_number(o) for o in options]
        svg = generate_stem_leaf_svg(data, title=context.title())
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 10,
            'difficulty_band': BANDS[10],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': svg
        })
    
    return questions


def generate_level_11():
    """
    Level 11: Comparing Measures / Which is better?
    Higher level - 50% visual
    SEC Style: "Which is a better measure - mean or median? Justify" - HL Q2
    """
    questions = []
    
    # Type 1: Which measure is better? (25 questions)
    for i in range(25):
        # Create dataset with or without outlier
        has_outlier = random.choice([True, False])
        
        if has_outlier:
            # Data with outlier - median is better
            base = random.randint(15, 35)
            data = [base + random.randint(-5, 5) for _ in range(7)]
            outlier = base + random.choice([-30, 40, 45, 50])
            data.append(outlier)
            random.shuffle(data)
            
            mean_val = calculate_mean(data)
            median_val = calculate_median(data)
            
            correct = "Median"
            wrong_measure = "Mean"
            reason = f"The outlier ({outlier}) pulls the mean ({format_number(round(mean_val, 1))}) away from the typical values. The median ({format_number(median_val)}) better represents the typical value."
        else:
            # Symmetric data - mean is fine
            base = random.randint(20, 40)
            data = [base + random.randint(-8, 8) for _ in range(8)]
            
            mean_val = calculate_mean(data)
            median_val = calculate_median(data)
            
            # For symmetric data, either could be correct - but we'll accept mean
            correct = "Mean"
            wrong_measure = "Median"
            reason = f"The data has no extreme outliers. Mean ({format_number(round(mean_val, 1))}) and median ({format_number(median_val)}) are similar, so mean gives a good representation."
        
        context = random.choice(['salaries (€000s)', 'house prices (€000s)', 'test scores', 'ages'])
        
        question = f"Data: {', '.join(map(str, data))}\n\nWhich is a better measure of the typical {context.split()[0]} - the mean or the median?"
        
        options = ["Mean", "Median", "Mode", "Range"]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        explanation = f"Mean = {format_number(round(mean_val, 1))}\n"
        explanation += f"Median = {format_number(median_val)}\n\n"
        explanation += reason
        
        if i < 13:  # 50% visual
            labels = [f"D{j+1}" for j in range(len(data))]
            svg = generate_bar_chart_svg(labels, data, title=context.title())
        else:
            svg = None
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 11,
            'difficulty_band': BANDS[11],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': svg
        })
    
    # Type 2: Comparing two datasets (25 questions)
    for i in range(25):
        # Generate two datasets
        data1 = [random.randint(40, 70) for _ in range(8)]
        data2 = [random.randint(35, 75) for _ in range(8)]
        
        mean1 = calculate_mean(data1)
        mean2 = calculate_mean(data2)
        range1 = calculate_range(data1)
        range2 = calculate_range(data2)
        
        q_type = random.choice(['higher_mean', 'higher_range', 'more_consistent', 'better_overall'])
        
        if q_type == 'higher_mean':
            correct = "Class A" if mean1 > mean2 else "Class B"
            question = "Two classes took a test.\nClass A: " + ', '.join(map(str, data1)) + "\nClass B: " + ', '.join(map(str, data2)) + "\n\nWhich class had a higher mean score?"
            explanation = f"Class A mean = {format_number(round(mean1, 1))}\n"
            explanation += f"Class B mean = {format_number(round(mean2, 1))}\n"
            explanation += f"{correct} has the higher mean."
        
        elif q_type == 'higher_range':
            correct = "Class A" if range1 > range2 else "Class B"
            question = "Two classes took a test.\nClass A: " + ', '.join(map(str, data1)) + "\nClass B: " + ', '.join(map(str, data2)) + "\n\nWhich class had a higher range?"
            explanation = f"Class A range = {range1}\n"
            explanation += f"Class B range = {range2}\n"
            explanation += f"{correct} has the higher range."
        
        elif q_type == 'more_consistent':
            correct = "Class A" if range1 < range2 else "Class B"
            question = "Two classes took a test.\nClass A: " + ', '.join(map(str, data1)) + "\nClass B: " + ', '.join(map(str, data2)) + "\n\nWhich class had more consistent results?"
            explanation = f"Consistency is measured by range (smaller = more consistent).\n"
            explanation += f"Class A range = {range1}\n"
            explanation += f"Class B range = {range2}\n"
            explanation += f"{correct} is more consistent (smaller range)."
        
        else:  # better_overall
            # Better = higher mean AND lower range (or just higher mean)
            if mean1 > mean2:
                correct = "Class A"
            else:
                correct = "Class B"
            question = "Two classes took a test.\nClass A: " + ', '.join(map(str, data1)) + "\nClass B: " + ', '.join(map(str, data2)) + "\n\nWhich class performed better overall (higher average)?"
            explanation = f"Compare means:\n"
            explanation += f"Class A mean = {format_number(round(mean1, 1))}\n"
            explanation += f"Class B mean = {format_number(round(mean2, 1))}\n"
            explanation += f"{correct} performed better (higher mean)."
        
        options = ["Class A", "Class B", "Same", "Cannot tell"]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 11,
            'difficulty_band': BANDS[11],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': None
        })
    
    return questions


def generate_level_12():
    """
    Level 12: Problem Solving & Back-to-back Stem-and-Leaf
    Mastery level - 50% visual
    SEC Style: HL Q4 - Back-to-back, effect on mean, finding missing values
    """
    questions = []
    
    # Type 1: Back-to-back stem-and-leaf (15 questions)
    for i in range(15):
        # Generate two related datasets
        n1 = random.randint(10, 14)
        n2 = random.randint(10, 14)
        
        base1 = random.randint(40, 55)
        base2 = random.randint(45, 60)
        
        data1 = [base1 + random.randint(-15, 20) for _ in range(n1)]
        data2 = [base2 + random.randint(-15, 20) for _ in range(n2)]
        
        data1 = [max(20, min(80, d)) for d in data1]
        data2 = [max(20, min(80, d)) for d in data2]
        
        mean1 = calculate_mean(data1)
        mean2 = calculate_mean(data2)
        median1 = calculate_median(data1)
        median2 = calculate_median(data2)
        
        q_type = random.choice(['compare_median', 'compare_mean', 'which_better', 'range_compare'])
        
        if q_type == 'compare_median':
            correct = "Art" if median1 > median2 else "Business"
            question = f"The back-to-back stem-and-leaf shows scores in Art (left) and Business (right) for students. Which subject had a higher median?"
            explanation = f"Art median = {format_number(median1)}\n"
            explanation += f"Business median = {format_number(median2)}\n"
            explanation += f"{correct} has the higher median."
        
        elif q_type == 'compare_mean':
            diff = abs(mean1 - mean2)
            correct = round(diff, 1)
            question = f"The back-to-back stem-and-leaf shows Art (left) and Business (right) scores. What is the difference between the two means (to 1 d.p.)?"
            options, correct_idx = generate_unique_options(correct, option_type='float', min_val=0)
            explanation = f"Art mean = {format_number(round(mean1, 1))}\n"
            explanation += f"Business mean = {format_number(round(mean2, 1))}\n"
            explanation += f"Difference = |{format_number(round(mean1, 1))} - {format_number(round(mean2, 1))}| = {format_number(correct)}"
        
        elif q_type == 'which_better':
            correct = "Art" if mean1 > mean2 else "Business"
            question = f"The back-to-back stem-and-leaf shows Art (left) and Business (right) scores. In which subject did students perform better on average?"
            explanation = f"Compare means:\n"
            explanation += f"Art mean = {format_number(round(mean1, 1))}\n"
            explanation += f"Business mean = {format_number(round(mean2, 1))}\n"
            explanation += f"Students performed better in {correct}."
        
        else:  # range_compare
            range1 = calculate_range(data1)
            range2 = calculate_range(data2)
            correct = "Art" if range1 > range2 else "Business"
            question = f"The back-to-back stem-and-leaf shows Art (left) and Business (right) scores. Which subject had a greater range?"
            explanation = f"Art range = {range1}\n"
            explanation += f"Business range = {range2}\n"
            explanation += f"{correct} has the greater range."
        
        if q_type not in ['compare_mean']:
            options = ["Art", "Business", "Same", "Cannot tell"]
            random.shuffle(options)
            correct_idx = options.index(correct)
        
        options = [format_number(o) if isinstance(o, (int, float)) else o for o in options]
        svg = generate_back_to_back_stem_leaf_svg(data1, data2, "Art", "Business")
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 12,
            'difficulty_band': BANDS[12],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': svg
        })
    
    # Type 2: Effect on mean (15 questions) - SEC 2025 HL style
    for i in range(15):
        n = random.randint(8, 12)
        data = [random.randint(40, 70) for _ in range(n)]
        old_mean = calculate_mean(data)
        
        # New value that changes mean
        new_mean_target = old_mean + random.choice([-2, -1, 1, 2])
        new_value = int(new_mean_target * (n + 1) - sum(data))
        new_value = max(0, min(100, new_value))
        
        # Calculate actual new mean
        actual_new_mean = (sum(data) + new_value) / (n + 1)
        
        q_type = random.choice(['find_new_value', 'effect_on_mean', 'keeps_mean_same'])
        
        # Add visual for first 8 questions (to reach 50% overall)
        if i < 8:
            labels = [f"S{j+1}" for j in range(n)]
            svg = generate_bar_chart_svg(labels, data, title="Test Scores")
        else:
            svg = None
        
        if q_type == 'find_new_value':
            target_mean = round(old_mean + random.choice([1, 2, -1, -2]), 0)
            correct = int(target_mean * (n + 1) - sum(data))
            question = f"The mean of {n} scores is {format_number(round(old_mean, 1))}. What score must the {n+1}th student get to make the new mean exactly {int(target_mean)}?"
            options, correct_idx = generate_unique_options(correct, min_val=0, max_val=100)
            explanation = f"Current sum = {sum(data)} (mean {format_number(round(old_mean, 1))} × {n})\n"
            explanation += f"New sum needed = {int(target_mean)} × {n+1} = {int(target_mean * (n + 1))}\n"
            explanation += f"New score needed = {int(target_mean * (n + 1))} - {sum(data)} = {correct}"
        
        elif q_type == 'effect_on_mean':
            new_score = random.randint(50, 90)
            new_mean = (sum(data) + new_score) / (n + 1)
            if new_mean > old_mean:
                correct = "Increase"
            elif new_mean < old_mean:
                correct = "Decrease"
            else:
                correct = "Stay the same"
            question = f"The mean of {n} test scores is {format_number(round(old_mean, 1))}. If a student scoring {new_score} joins, will the mean increase, decrease, or stay the same?"
            options = ["Increase", "Decrease", "Stay the same", "Cannot tell"]
            random.shuffle(options)
            correct_idx = options.index(correct)
            explanation = f"Old mean = {format_number(round(old_mean, 1))}\n"
            explanation += f"New score ({new_score}) is {'above' if new_score > old_mean else 'below'} the old mean.\n"
            explanation += f"New mean = {format_number(round(new_mean, 1))}\n"
            explanation += f"The mean will {correct.lower()}."
        
        else:  # keeps_mean_same
            correct = int(round(old_mean))
            question = f"The mean of {n} scores is {format_number(round(old_mean, 1))}. What score would the {n+1}th student need to keep the mean approximately the same?"
            options, correct_idx = generate_unique_options(correct, min_val=0, max_val=100)
            explanation = f"To keep the mean the same, the new value must equal the current mean.\n"
            explanation += f"Current mean ≈ {format_number(round(old_mean, 1))}\n"
            explanation += f"New student needs approximately {correct}."
        
        options = [str(o) for o in options]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 12,
            'difficulty_band': BANDS[12],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': svg
        })
    
    # Type 3: Find missing values given statistics - SEC 2025 OL Q6(b) style
    for i in range(20):
        # Create puzzle: given mode, median, range, find missing values
        # 5 numbers from smallest to largest with some missing
        
        mode_val = random.randint(2, 8)
        range_val = random.randint(8, 15)
        smallest = random.randint(1, 5)
        largest = smallest + range_val
        
        # Create sequence with mode appearing twice
        middle_val = random.randint(smallest + 2, largest - 2)
        
        # For odd count, median is middle
        # Arrange: smallest, mode, median, mode_or_other, largest
        # Let's use: smallest, mode, median, x, largest where mode appears at positions that work
        
        data = sorted([smallest, mode_val, middle_val, mode_val, largest])
        median_val = data[2]  # Middle of 5
        
        # Verify mode
        counts = Counter(data)
        if counts[mode_val] < 2 or any(c > counts[mode_val] for v, c in counts.items() if v != mode_val):
            # Adjust
            data = [smallest, mode_val, mode_val, mode_val + 2, largest]
            median_val = data[2]
        
        # Pick which value to find
        hide_idx = random.choice([1, 2, 3])
        correct = data[hide_idx]
        
        shown = data.copy()
        shown[hide_idx] = '?'
        
        question = f"Five numbers in order: {', '.join(map(str, shown))}\nMode = {mode_val}, Median = {median_val}, Range = {range_val}\n\nFind the missing number."
        options, correct_idx = generate_unique_options(correct, min_val=smallest, max_val=largest)
        
        explanation = f"The five numbers in order are: {', '.join(map(str, data))}\n"
        explanation += f"• Range = {largest} - {smallest} = {range_val} ✓\n"
        explanation += f"• Median (middle) = {median_val} ✓\n"
        explanation += f"• Mode (most frequent) = {mode_val} ✓\n"
        explanation += f"Missing number = {correct}"
        
        options = [str(o) for o in options]
        
        questions.append({
            'question_text': question,
            'option_a': options[0],
            'option_b': options[1],
            'option_c': options[2],
            'option_d': options[3],
            'correct_idx': correct_idx,
            'topic': TOPIC,
            'difficulty': 12,
            'difficulty_band': BANDS[12],
            'mode': 'jc_exam',
            'explanation': explanation,
            'image_svg': None
        })
    
    return questions


# ==================== VALIDATION ====================

def validate_questions(questions):
    """Validate all questions meet requirements"""
    errors = []
    warnings = []
    
    for i, q in enumerate(questions):
        # Check unique options
        opts = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(opts)) != 4:
            errors.append(f"Q{i+1} L{q['difficulty']}: Duplicate options - {opts}")
        
        # Check explanation exists and has substance
        if not q.get('explanation') or len(q['explanation']) < 20:
            errors.append(f"Q{i+1} L{q['difficulty']}: Missing/short explanation")
        
        # Check correct_idx valid
        if q['correct_idx'] not in [0, 1, 2, 3]:
            errors.append(f"Q{i+1} L{q['difficulty']}: Invalid correct_idx {q['correct_idx']}")
        
        # Check required fields
        for field in ['question_text', 'topic', 'difficulty', 'difficulty_band', 'mode']:
            if not q.get(field):
                errors.append(f"Q{i+1}: Missing field '{field}'")
    
    # Check questions per level
    level_counts = {}
    for q in questions:
        level = q['difficulty']
        level_counts[level] = level_counts.get(level, 0) + 1
    
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        if count < QUESTIONS_PER_LEVEL:
            warnings.append(f"Level {level}: Only {count} questions (need {QUESTIONS_PER_LEVEL})")
        elif count > QUESTIONS_PER_LEVEL:
            warnings.append(f"Level {level}: {count} questions (expected {QUESTIONS_PER_LEVEL})")
    
    return errors, warnings


def print_validation_summary(questions):
    """Print validation summary"""
    print("\n" + "=" * 60)
    print("📊 VALIDATION SUMMARY")
    print("=" * 60)
    
    # Questions per level
    level_counts = {}
    for q in questions:
        level = q['difficulty']
        level_counts[level] = level_counts.get(level, 0) + 1
    
    print("\n📈 Questions per Level:")
    total = 0
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        total += count
        band = BANDS[level]
        bar = '█' * (count // 5) + '░' * ((QUESTIONS_PER_LEVEL - count) // 5)
        status = '✅' if count >= QUESTIONS_PER_LEVEL else '❌'
        print(f"   Level {level:2d} ({band:10s}): {bar} {count:2d} {status}")
    
    print(f"\n📊 Total Questions: {total}")
    
    # Visual ratio check
    for level in range(1, 13):
        level_qs = [q for q in questions if q['difficulty'] == level]
        visual_count = sum(1 for q in level_qs if q.get('image_svg'))
        visual_pct = (visual_count / len(level_qs) * 100) if level_qs else 0
        expected = 75 if level <= 10 else 50
        status = '✅' if visual_pct >= expected - 10 else '⚠️'
        if level in [1, 6, 10, 12]:  # Sample levels
            print(f"   Level {level} visual: {visual_pct:.0f}% (target: {expected}%) {status}")
    
    # Run validation
    errors, warnings = validate_questions(questions)
    
    if errors:
        print(f"\n❌ ERRORS ({len(errors)}):")
        for e in errors[:10]:  # Show first 10
            print(f"   {e}")
        if len(errors) > 10:
            print(f"   ... and {len(errors) - 10} more errors")
    else:
        print("\n✅ No validation errors!")
    
    if warnings:
        print(f"\n⚠️ WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"   {w}")
    
    return len(errors) == 0


# ==================== DATABASE INSERTION ====================

def insert_questions(questions, db_path):
    """Insert questions into database with proper handling"""
    
    # Step 1: Deduplicate
    seen = set()
    unique_questions = []
    for q in questions:
        key = (q['topic'], q['difficulty'], q['question_text'][:100])
        if key not in seen:
            seen.add(key)
            unique_questions.append(q)
    
    if len(unique_questions) < len(questions):
        print(f"⚠️ Removed {len(questions) - len(unique_questions)} duplicate questions")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Step 2: Check existing
    cursor.execute("SELECT topic, COUNT(*) FROM questions_adaptive GROUP BY topic")
    existing = cursor.fetchall()
    if existing:
        print(f"📁 Existing topics: {[(r[0], r[1]) for r in existing]}")
    
    # Step 3: Delete existing for this topic
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = ?", (TOPIC,))
    deleted = cursor.rowcount
    conn.commit()
    print(f"🗑️ Deleted {deleted} existing questions for '{TOPIC}'")
    
    # Step 4: Insert new questions
    insert_sql = """
        INSERT INTO questions_adaptive 
        (question_text, option_a, option_b, option_c, option_d,
         correct_answer, topic, difficulty_level, difficulty_band, mode,
         explanation, image_svg, is_active)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
    """
    
    inserted = 0
    errors = 0
    for q in unique_questions:
        try:
            cursor.execute(insert_sql, (
                q['question_text'],
                q['option_a'],
                q['option_b'],
                q['option_c'],
                q['option_d'],
                q['correct_idx'],  # Maps to correct_answer
                q['topic'],
                q['difficulty'],   # Maps to difficulty_level
                q['difficulty_band'],
                q['mode'],
                q['explanation'],
                q.get('image_svg')
            ))
            inserted += 1
        except Exception as e:
            errors += 1
            if errors <= 5:
                print(f"   ⚠️ Error L{q['difficulty']}: {str(e)[:60]}")
    
    conn.commit()
    conn.close()
    
    print(f"✅ Inserted {inserted} questions, {errors} errors")
    return inserted, errors


# ==================== MAIN ====================

def main():
    """Main function to generate and insert questions"""
    print("=" * 60)
    print("🎓 AgentMath - Descriptive Statistics Generator")
    print("=" * 60)
    print(f"Topic: {TOPIC}")
    print(f"Target: {QUESTIONS_PER_LEVEL} questions × 12 levels = 600 total")
    print()
    
    all_questions = []
    
    # Generate questions for each level
    generators = [
        generate_level_1,
        generate_level_2,
        generate_level_3,
        generate_level_4,
        generate_level_5,
        generate_level_6,
        generate_level_7,
        generate_level_8,
        generate_level_9,
        generate_level_10,
        generate_level_11,
        generate_level_12,
    ]
    
    for level, generator in enumerate(generators, 1):
        print(f"Generating Level {level}...", end=" ")
        try:
            questions = generator()
            all_questions.extend(questions)
            print(f"✓ {len(questions)} questions")
        except Exception as e:
            print(f"✗ Error: {e}")
            import traceback
            traceback.print_exc()
    
    # Validate
    is_valid = print_validation_summary(all_questions)
    
    if not is_valid:
        print("\n⚠️ Validation failed. Fix errors before inserting.")
        response = input("Continue anyway? (y/N): ").strip().lower()
        if response != 'y':
            print("Aborted.")
            return
    
    # Insert into database
    print("\n" + "=" * 60)
    print("💾 DATABASE INSERTION")
    print("=" * 60)
    print(f"Database: {DB_PATH}")
    
    response = input("Insert questions into database? (y/N): ").strip().lower()
    if response == 'y':
        try:
            inserted, errors = insert_questions(all_questions, DB_PATH)
            print(f"\n🎉 Complete! {inserted} questions added to database.")
        except Exception as e:
            print(f"\n❌ Database error: {e}")
            import traceback
            traceback.print_exc()
    else:
        print("Skipped database insertion.")
    
    # Verification query
    print("\n📋 Verification SQL:")
    print(f"""
    SELECT difficulty_level, COUNT(*) as count,
           COUNT(CASE WHEN explanation != '' THEN 1 END) as with_explanation
    FROM questions_adaptive 
    WHERE topic = '{TOPIC}' AND mode = 'jc_exam'
    GROUP BY difficulty_level
    ORDER BY difficulty_level;
    """)


if __name__ == "__main__":
    main()
