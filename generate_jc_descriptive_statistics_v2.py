#!/usr/bin/env python3
"""
AgentMath - Descriptive Statistics Question Generator
SEC-Aligned for Irish Junior Cycle Mathematics

Version: 2.0
Date: December 2025
Author: Barry (ICT Coordinator, Palmerstown Community School)

CHANGELOG v2.0:
- FIXED: Stem-and-leaf mode questions now generate UNIMODAL data only
- FIXED: Frequency table SVG clipping - increased height and padding
- FIXED: Frequency table text size increased for accessibility (12-14px)
- IMPROVED: Better validation for single-mode datasets
- IMPROVED: Larger, more readable frequency tables

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
    """
    Generate an SVG frequency table - V2 with LARGER TEXT and NO CLIPPING
    
    Changes from v1:
    - Increased row_height from 24 to 32 for better spacing
    - Increased font sizes from 10-11 to 12-14 for accessibility
    - Added more bottom padding to prevent clipping
    - Wider table (260px vs 220px) for better readability
    """
    width = 260  # Increased from 220
    row_height = 32  # Increased from 24
    header_height = 36  # Slightly taller header
    
    # Calculate height with extra padding at bottom
    num_rows = len(values)
    table_content_height = header_height + (num_rows * row_height)
    title_space = 28 if title else 0
    bottom_padding = 20  # Extra padding to prevent clipping
    
    height = title_space + table_content_height + bottom_padding + 10
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#ffffff"/>'
    
    title_y = 0
    if title:
        svg += f'<text x="{width/2}" y="20" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e293b">{title}</text>'
        title_y = 28
    
    # Table positioning
    table_x = 15
    table_width = width - 30
    table_y = title_y + 8
    col_divider_x = table_x + table_width // 2
    
    # Table border
    total_table_height = header_height + (num_rows * row_height)
    svg += f'<rect x="{table_x}" y="{table_y}" width="{table_width}" height="{total_table_height}" fill="none" stroke="#94a3b8" stroke-width="2" rx="4"/>'
    
    # Header background
    svg += f'<rect x="{table_x}" y="{table_y}" width="{table_width}" height="{header_height}" fill="#e2e8f0" rx="4"/>'
    svg += f'<rect x="{table_x}" y="{table_y + header_height - 4}" width="{table_width}" height="4" fill="#e2e8f0"/>'
    
    # Header text - LARGER FONT SIZE (14px)
    svg += f'<text x="{table_x + table_width//4}" y="{table_y + header_height//2 + 5}" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e293b">{x_label}</text>'
    svg += f'<text x="{table_x + 3*table_width//4}" y="{table_y + header_height//2 + 5}" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e293b">Frequency</text>'
    
    # Column divider line
    svg += f'<line x1="{col_divider_x}" y1="{table_y}" x2="{col_divider_x}" y2="{table_y + total_table_height}" stroke="#94a3b8" stroke-width="1"/>'
    
    # Header/data separator line
    svg += f'<line x1="{table_x}" y1="{table_y + header_height}" x2="{table_x + table_width}" y2="{table_y + header_height}" stroke="#94a3b8" stroke-width="1"/>'
    
    # Data rows - LARGER FONT SIZE (13px for values, 14px bold for frequencies)
    for i, (val, freq) in enumerate(zip(values, frequencies)):
        row_y = table_y + header_height + (i * row_height)
        
        # Alternating row background
        if i % 2 == 0:
            svg += f'<rect x="{table_x + 1}" y="{row_y + 1}" width="{table_width - 2}" height="{row_height - 1}" fill="#f8fafc"/>'
        
        # Row separator line (except for last row)
        if i < num_rows - 1:
            svg += f'<line x1="{table_x}" y1="{row_y + row_height}" x2="{table_x + table_width}" y2="{row_y + row_height}" stroke="#e2e8f0" stroke-width="1"/>'
        
        # Value text - centered in left column
        text_y = row_y + (row_height // 2) + 5
        svg += f'<text x="{table_x + table_width//4}" y="{text_y}" text-anchor="middle" font-size="13" fill="#1e293b">{val}</text>'
        
        # Frequency text - centered in right column, bold blue
        svg += f'<text x="{table_x + 3*table_width//4}" y="{text_y}" text-anchor="middle" font-size="14" font-weight="bold" fill="#2563eb">{freq}</text>'
    
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
    """
    Generate an SVG stem-and-leaf diagram - V2 with improved sizing
    
    Changes from v1:
    - Slightly larger font sizes
    - Better spacing
    """
    # Organize data
    stems = {}
    for val in sorted(data):
        stem = val // 10
        leaf = val % 10
        if stem not in stems:
            stems[stem] = []
        stems[stem].append(leaf)
    
    width = 220  # Slightly wider
    row_height = 24  # Slightly more spacing
    height = 70 + len(stems) * row_height
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#ffffff"/>'
    
    if title:
        svg += f'<text x="{width/2}" y="20" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">{title}</text>'
    
    # Header
    svg += f'<text x="45" y="42" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">Stem</text>'
    svg += f'<text x="140" y="42" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">Leaf</text>'
    
    # Dividing line
    svg += f'<line x1="80" y1="28" x2="80" y2="{height-15}" stroke="#94a3b8" stroke-width="2"/>'
    
    # Data rows
    for i, stem in enumerate(sorted(stems.keys())):
        y = 65 + i * row_height
        leaves = ' '.join(str(l) for l in sorted(stems[stem]))
        svg += f'<text x="45" y="{y}" text-anchor="middle" font-size="13" fill="#1e293b">{stem}</text>'
        svg += f'<text x="90" y="{y}" font-size="13" fill="#3b82f6" font-family="monospace">{leaves}</text>'
    
    # Key
    svg += f'<text x="10" y="{height-5}" font-size="10" fill="#64748b">Key: 3|5 means 35</text>'
    
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
    
    width = 300  # Wider for better readability
    row_height = 24
    num_stems = max_stem - min_stem + 1
    height = 90 + num_stems * row_height
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#ffffff"/>'
    
    # Titles
    if title_left:
        svg += f'<text x="75" y="20" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e293b">{title_left}</text>'
    if title_right:
        svg += f'<text x="225" y="20" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e293b">{title_right}</text>'
    
    # Column headers
    svg += f'<text x="75" y="48" text-anchor="middle" font-size="10" fill="#64748b">Leaf</text>'
    svg += f'<text x="150" y="48" text-anchor="middle" font-size="10" fill="#64748b">Stem</text>'
    svg += f'<text x="225" y="48" text-anchor="middle" font-size="10" fill="#64748b">Leaf</text>'
    
    # Dividing lines
    svg += f'<line x1="130" y1="38" x2="130" y2="{height-20}" stroke="#94a3b8" stroke-width="1"/>'
    svg += f'<line x1="170" y1="38" x2="170" y2="{height-20}" stroke="#94a3b8" stroke-width="1"/>'
    
    # Data rows
    for i, stem in enumerate(range(min_stem, max_stem + 1)):
        y = 70 + i * row_height
        
        # Left leaves (reversed order, right-aligned)
        left_leaves = ' '.join(str(l) for l in sorted(stems_left[stem], reverse=True))
        svg += f'<text x="125" y="{y}" text-anchor="end" font-size="12" fill="#3b82f6" font-family="monospace">{left_leaves}</text>'
        
        # Stem
        svg += f'<text x="150" y="{y}" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">{stem}</text>'
        
        # Right leaves
        right_leaves = ' '.join(str(l) for l in sorted(stems_right[stem]))
        svg += f'<text x="175" y="{y}" font-size="12" fill="#22c55e" font-family="monospace">{right_leaves}</text>'
    
    # Key
    svg += f'<text x="10" y="{height-5}" font-size="9" fill="#64748b">Key: 5 3|4 means 35 (left) and 34 (right)</text>'
    
    svg += '</svg>'
    return svg


def generate_data_table_svg(headers, rows, title=""):
    """Generate a simple data table SVG"""
    col_width = 55  # Slightly wider
    width = len(headers) * col_width + 20
    row_height = 28  # Taller rows
    height = 45 + (len(rows) + 1) * row_height
    
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#ffffff"/>'
    
    if title:
        svg += f'<text x="{width/2}" y="18" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e293b">{title}</text>'
    
    table_y = 30
    
    # Header row
    svg += f'<rect x="10" y="{table_y}" width="{width-20}" height="{row_height}" fill="#e2e8f0"/>'
    for i, header in enumerate(headers):
        x = 10 + i * col_width + col_width/2
        svg += f'<text x="{x}" y="{table_y + 18}" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e293b">{header}</text>'
    
    # Data rows
    for r, row in enumerate(rows):
        y = table_y + (r + 1) * row_height
        if r % 2 == 0:
            svg += f'<rect x="10" y="{y}" width="{width-20}" height="{row_height}" fill="#f8fafc"/>'
        for i, cell in enumerate(row):
            x = 10 + i * col_width + col_width/2
            svg += f'<text x="{x}" y="{y + 18}" text-anchor="middle" font-size="10" fill="#1e293b">{cell}</text>'
    
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


def is_unimodal(data):
    """Check if dataset has exactly one mode"""
    if not data:
        return False
    counts = Counter(data)
    max_count = max(counts.values())
    modes = [val for val, count in counts.items() if count == max_count]
    return len(modes) == 1


def generate_unimodal_data(n, min_val=10, max_val=99, mode_frequency=None):
    """
    Generate a dataset that is guaranteed to have exactly ONE mode.
    
    This is V2's key fix for stem-and-leaf mode questions.
    
    Args:
        n: number of data points
        min_val: minimum value
        max_val: maximum value
        mode_frequency: how many times the mode should appear (default: calculated)
    
    Returns:
        tuple: (data, mode_value)
    """
    # Ensure the mode appears more times than any other value
    if mode_frequency is None:
        # Mode should appear at least 2 times, and more than n // distinct_values
        mode_frequency = max(3, n // 4 + 1)
    
    # Pick a mode value
    mode_val = random.randint(min_val + 5, max_val - 5)
    
    # Start with the mode appearing mode_frequency times
    data = [mode_val] * mode_frequency
    
    # Fill the rest with values that appear LESS than mode_frequency
    remaining = n - mode_frequency
    available_values = [v for v in range(min_val, max_val + 1) if v != mode_val]
    
    # Track how many times each non-mode value has been used
    value_counts = {v: 0 for v in available_values}
    max_non_mode_frequency = mode_frequency - 1  # Non-mode values can appear at most this many times
    
    for _ in range(remaining):
        # Filter to values that can still be added
        valid_values = [v for v in available_values if value_counts[v] < max_non_mode_frequency]
        if not valid_values:
            # If all values are at max, just pick any (still won't exceed mode)
            valid_values = available_values
        
        chosen = random.choice(valid_values)
        data.append(chosen)
        value_counts[chosen] += 1
    
    random.shuffle(data)
    
    # Verify it's unimodal
    assert is_unimodal(data), f"Generated data is not unimodal: {Counter(data)}"
    
    return data, mode_val


def generate_unique_options(correct, num_options=4, option_type='int', min_val=None, max_val=None):
    """Generate unique answer options including the correct answer"""
    options = [correct]
    
    # Determine range for distractors
    if min_val is None:
        min_val = max(0, correct - 20) if option_type == 'int' else max(0, correct - 10)
    if max_val is None:
        max_val = correct + 20 if option_type == 'int' else correct + 10
    
    attempts = 0
    while len(options) < num_options and attempts < 100:
        attempts += 1
        
        if option_type == 'int':
            # Generate integer distractors
            offset = random.choice([-3, -2, -1, 1, 2, 3, -5, 5, -10, 10])
            distractor = int(correct) + offset
        else:
            # Generate float distractors
            offset = random.choice([-2.5, -2, -1.5, -1, -0.5, 0.5, 1, 1.5, 2, 2.5])
            distractor = round(correct + offset, 1)
        
        if distractor not in options and distractor >= min_val:
            if max_val is None or distractor <= max_val:
                options.append(distractor)
    
    # Fill remaining slots if needed
    while len(options) < num_options:
        if option_type == 'int':
            distractor = random.randint(int(min_val), int(max_val))
        else:
            distractor = round(random.uniform(min_val, max_val), 1)
        if distractor not in options:
            options.append(distractor)
    
    random.shuffle(options)
    correct_idx = options.index(correct)
    
    return options, correct_idx


def format_number(n):
    """Format number for display (remove unnecessary decimals)"""
    if isinstance(n, float):
        if n == int(n):
            return str(int(n))
        return str(round(n, 2))
    return str(n)


# ==================== LEVEL GENERATORS ====================

def generate_level_1():
    """
    Level 1: Reading Data (tally, pictogram, bar chart)
    Foundation level - 100% visual
    SEC Style: Reading and interpreting basic charts
    """
    questions = []
    
    # Type 1: Tally charts (17 questions)
    for i in range(17):
        items = random.sample(['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple'], 4)
        values = [random.randint(3, 12) for _ in items]
        
        q_type = random.choice(['total', 'most', 'least', 'specific'])
        
        if q_type == 'total':
            correct = sum(values)
            question = "The tally chart shows favourite colours. How many people were surveyed in total?"
            explanation = f"Add all frequencies: {' + '.join(map(str, values))} = {correct}"
        elif q_type == 'most':
            correct = items[values.index(max(values))]
            question = "The tally chart shows favourite colours. Which colour is most popular?"
            options = items.copy()
            random.shuffle(options)
            correct_idx = options.index(correct)
            explanation = f"The highest frequency is {max(values)}, which is {correct}."
        elif q_type == 'least':
            correct = items[values.index(min(values))]
            question = "The tally chart shows favourite colours. Which colour is least popular?"
            options = items.copy()
            random.shuffle(options)
            correct_idx = options.index(correct)
            explanation = f"The lowest frequency is {min(values)}, which is {correct}."
        else:
            idx = random.randint(0, len(items) - 1)
            correct = values[idx]
            question = f"The tally chart shows favourite colours. How many chose {items[idx]}?"
            explanation = f"Read the tally for {items[idx]}: {correct}"
        
        if q_type not in ['most', 'least']:
            options, correct_idx = generate_unique_options(correct, min_val=1)
            options = [str(o) for o in options]
        
        svg = generate_tally_chart_svg(items, values, title="Favourite Colours")
        
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
    
    # Type 2: Pictograms (17 questions)
    for i in range(17):
        days = random.sample(DAYS[:5], 4)  # Weekdays
        values = [random.randint(2, 8) for _ in days]
        context = random.choice(['books sold', 'ice creams sold', 'pizzas made', 'cakes baked'])
        
        q_type = random.choice(['total', 'difference', 'specific'])
        
        if q_type == 'total':
            correct = sum(values)
            question = f"The pictogram shows {context} each day. What is the total for all days?"
            explanation = f"Total = {' + '.join(map(str, values))} = {correct}"
        elif q_type == 'difference':
            max_day = days[values.index(max(values))]
            min_day = days[values.index(min(values))]
            correct = max(values) - min(values)
            question = f"The pictogram shows {context}. How many more were sold on {max_day} than {min_day}?"
            explanation = f"Difference = {max(values)} - {min(values)} = {correct}"
        else:
            idx = random.randint(0, len(days) - 1)
            correct = values[idx]
            question = f"The pictogram shows {context}. How many on {days[idx]}?"
            explanation = f"Count the symbols for {days[idx]}: {correct}"
        
        options, correct_idx = generate_unique_options(correct, min_val=0)
        options = [str(o) for o in options]
        
        svg = generate_pictogram_svg(days, values, title=context.title())
        
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
    
    # Type 3: Bar charts (16 questions)
    for i in range(16):
        categories = random.sample(['Maths', 'English', 'Irish', 'Science', 'History', 'Art'], 4)
        values = [random.randint(5, 20) for _ in categories]
        
        q_type = random.choice(['total', 'highest', 'compare'])
        
        if q_type == 'total':
            correct = sum(values)
            question = "The bar chart shows test scores. What is the total of all scores?"
            explanation = f"Total = {' + '.join(map(str, values))} = {correct}"
        elif q_type == 'highest':
            correct = categories[values.index(max(values))]
            question = "The bar chart shows test scores. Which subject has the highest score?"
            options = categories.copy()
            random.shuffle(options)
            correct_idx = options.index(correct)
            explanation = f"The tallest bar is {correct} with {max(values)} marks."
        else:
            idx = random.randint(0, len(categories) - 1)
            correct = values[idx]
            question = f"The bar chart shows test scores. What was the score for {categories[idx]}?"
            explanation = f"Read the height of the {categories[idx]} bar: {correct}"
        
        if q_type != 'highest':
            options, correct_idx = generate_unique_options(correct, min_val=0)
            options = [str(o) for o in options]
        
        svg = generate_bar_chart_svg(categories, values, title="Test Scores")
        
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
    SEC Style: "Find the mode" - OL Q5, Q6
    """
    questions = []
    
    for i in range(50):
        # Generate data with clear single mode
        n = random.randint(7, 12)
        mode_val = random.randint(3, 15)
        mode_freq = random.randint(3, 4)
        
        # Create data ensuring clear mode
        data = [mode_val] * mode_freq
        other_vals = [v for v in range(mode_val - 5, mode_val + 6) if v != mode_val and v > 0]
        
        while len(data) < n:
            val = random.choice(other_vals)
            if data.count(val) < mode_freq - 1:  # Ensure no ties
                data.append(val)
        
        random.shuffle(data)
        correct = mode_val
        
        context = random.choice(['shoe sizes', 'goals scored', 'test marks', 'ages', 'pets owned'])
        
        if i < 40:  # 80% visual
            labels = random.sample(PEOPLE_NAMES, n) if n <= len(PEOPLE_NAMES) else [f"P{j+1}" for j in range(n)]
            question = f"Find the mode of these {context}:\n{', '.join(map(str, data))}"
            svg = generate_bar_chart_svg(labels, data, title=f"{context.title()}")
        else:
            question = f"The {context} were: {', '.join(map(str, data))}. What is the mode?"
            svg = None
        
        options, correct_idx = generate_unique_options(correct, min_val=min(data), max_val=max(data))
        options = [str(o) for o in options]
        
        explanation = f"Mode = most frequent value\n"
        counts = Counter(data)
        for val, count in sorted(counts.items()):
            marker = " ← appears most often" if val == mode_val else ""
            explanation += f"  {val} appears {count} times{marker}\n"
        explanation += f"Mode = {correct}"
        
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
    
    return questions


def generate_level_3():
    """
    Level 3: Range from Lists & Tables
    Foundation level - 75% visual
    SEC Style: "Find the range" - OL Q5, Q6
    """
    questions = []
    
    for i in range(50):
        n = random.randint(6, 10)
        min_val = random.randint(5, 20)
        range_val = random.randint(10, 25)
        max_val = min_val + range_val
        
        # Generate data with specific range
        data = [min_val, max_val]
        while len(data) < n:
            data.append(random.randint(min_val, max_val))
        random.shuffle(data)
        
        correct = range_val
        
        context = random.choice(['temperatures (°C)', 'heights (cm)', 'weights (kg)', 'prices (€)', 'times (min)'])
        
        if i < 40:  # 80% visual
            labels = random.sample(DAYS, n) if n <= 7 else [f"D{j+1}" for j in range(n)]
            question = f"Find the range of these {context}:\n{', '.join(map(str, data))}"
            svg = generate_bar_chart_svg(labels, data, title=context.title())
        else:
            question = f"The {context} were: {', '.join(map(str, data))}. Calculate the range."
            svg = None
        
        options, correct_idx = generate_unique_options(correct, min_val=1)
        options = [str(o) for o in options]
        
        explanation = f"Range = Maximum - Minimum\n"
        explanation += f"Maximum = {max(data)}\n"
        explanation += f"Minimum = {min(data)}\n"
        explanation += f"Range = {max(data)} - {min(data)} = {correct}"
        
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
    
    return questions


def generate_level_4():
    """
    Level 4: Median (odd number of values)
    Ordinary level - 75% visual
    SEC Style: Finding median with odd datasets
    """
    questions = []
    
    for i in range(50):
        # Generate odd-sized dataset (5, 7, 9, or 11 values)
        n = random.choice([5, 7, 9, 11])
        
        base = random.randint(10, 30)
        data = [base + random.randint(-10, 10) for _ in range(n)]
        
        sorted_data = sorted(data)
        correct = sorted_data[n // 2]
        
        context = random.choice(['marks', 'ages', 'heights (cm)', 'distances (km)'])
        
        if i < 38:  # 75% visual
            question = f"Find the median of these {n} {context}:\n{', '.join(map(str, data))}"
            labels = [f"V{j+1}" for j in range(n)]
            svg = generate_bar_chart_svg(labels, data, title=context.title())
        else:
            name = random.choice(PEOPLE_NAMES)
            question = f"{name} recorded {n} {context}: {', '.join(map(str, data))}. Find the median."
            svg = None
        
        options, correct_idx = generate_unique_options(correct, min_val=min(data), max_val=max(data))
        options = [str(o) for o in options]
        
        explanation = f"To find the median with {n} (odd) values:\n"
        explanation += f"1. Arrange in order: {', '.join(map(str, sorted_data))}\n"
        explanation += f"2. Find the middle value (position {n//2 + 1})\n"
        explanation += f"3. Median = {correct}"
        
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
        # Generate 5-7 values for the frequency table
        num_values = random.randint(5, 7)
        start_val = random.randint(0, 2)
        values = list(range(start_val, start_val + num_values))
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
        # Generate frequency table with 5-6 values
        num_values = random.randint(5, 6)
        start_val = random.randint(0, 2)
        values = list(range(start_val, start_val + num_values))
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
    
    V2 FIX: Mode questions now use GUARANTEED UNIMODAL data
    """
    questions = []
    
    for i in range(50):
        q_type = random.choice(['median', 'range', 'mode', 'count', 'smallest', 'largest'])
        
        context = random.choice(['test scores', 'ages', 'heights (cm)', 'reaction times (ms)'])
        
        # For MODE questions, generate UNIMODAL data (V2 FIX)
        if q_type == 'mode':
            n = random.randint(10, 16)
            data, mode_val = generate_unimodal_data(n, min_val=20, max_val=80)
            sorted_data = sorted(data)
            correct = mode_val
            
            question = f"The stem-and-leaf diagram shows {context} for {n} students. Find the mode."
            options, correct_idx = generate_unique_options(correct, min_val=min(data), max_val=max(data))
            
            counts = Counter(data)
            max_count = counts[mode_val]
            explanation = f"Mode = most frequent value\n"
            explanation += f"Looking at the leaves, {correct} appears {max_count} times (most frequent).\n"
            explanation += f"Mode = {correct}"
        
        else:
            # For other question types, generate regular data
            n = random.randint(10, 18)
            base = random.randint(30, 60)
            data = [base + random.randint(-20, 20) for _ in range(n)]
            data = [max(10, min(99, d)) for d in data]  # Keep 2-digit
            sorted_data = sorted(data)
            
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
    SEC Style: "Which measure best represents..." - HL Q2
    """
    questions = []
    
    for i in range(50):
        q_type = random.choice(['outlier_mean', 'skewed', 'typical', 'comparison'])
        
        if q_type == 'outlier_mean':
            # Dataset with outlier - median better
            base_data = [random.randint(15, 25) for _ in range(7)]
            outlier = random.choice([random.randint(70, 90), random.randint(1, 5)])
            data = base_data + [outlier]
            random.shuffle(data)
            
            mean_val = sum(data) / len(data)
            median_val = calculate_median(data)
            
            correct = 'Median'
            question = f"The data set is: {', '.join(map(str, data))}.\nWhich average best represents the data?"
            options = ['Mean', 'Median', 'Mode', 'Range']
            random.shuffle(options)
            correct_idx = options.index(correct)
            
            explanation = f"Mean = {format_number(mean_val)}, Median = {format_number(median_val)}\n"
            explanation += f"The outlier ({outlier}) pulls the mean {'up' if outlier > 30 else 'down'}.\n"
            explanation += f"Median is not affected by outliers, so it better represents the typical value."
        
        elif q_type == 'skewed':
            # Skewed dataset
            data = sorted([random.randint(10, 20) for _ in range(6)] + [random.randint(35, 50) for _ in range(2)])
            
            mean_val = sum(data) / len(data)
            median_val = calculate_median(data)
            
            correct = 'Median'
            question = f"Salaries in €000s: {', '.join(map(str, data))}.\nWhich average is most appropriate?"
            options = ['Mean', 'Median', 'Mode', 'Range']
            random.shuffle(options)
            correct_idx = options.index(correct)
            
            explanation = f"Mean = {format_number(mean_val)}, Median = {format_number(median_val)}\n"
            explanation += f"The data is skewed by high values.\n"
            explanation += f"Median better represents the typical salary."
        
        elif q_type == 'typical':
            # Modal data - mode best
            sizes = ['S', 'M', 'L', 'XL']
            frequencies = [random.randint(5, 15) for _ in sizes]
            max_freq_idx = frequencies.index(max(frequencies))
            
            correct = 'Mode'
            question = f"T-shirt sizes sold: S({frequencies[0]}), M({frequencies[1]}), L({frequencies[2]}), XL({frequencies[3]}).\nWhich measure should the shop use to decide what to stock more of?"
            options = ['Mean', 'Median', 'Mode', 'Range']
            random.shuffle(options)
            correct_idx = options.index(correct)
            
            explanation = f"For categorical data like sizes, mode is most useful.\n"
            explanation += f"Mode = {sizes[max_freq_idx]} (sold {max(frequencies)} times)\n"
            explanation += f"The shop should stock more size {sizes[max_freq_idx]}."
        
        else:  # comparison
            # Compare two datasets
            data1 = [random.randint(40, 60) for _ in range(8)]
            data2 = [random.randint(35, 75) for _ in range(8)]
            
            mean1 = sum(data1) / len(data1)
            mean2 = sum(data2) / len(data2)
            range1 = max(data1) - min(data1)
            range2 = max(data2) - min(data2)
            
            if abs(mean1 - mean2) < 3:
                # Similar means, different ranges
                correct = f"Class {'A' if range1 < range2 else 'B'}"
                question = f"Class A scores: {', '.join(map(str, data1))}.\nClass B scores: {', '.join(map(str, data2))}.\nWhich class was more consistent?"
                explanation = f"Class A: Mean = {format_number(mean1)}, Range = {range1}\n"
                explanation += f"Class B: Mean = {format_number(mean2)}, Range = {range2}\n"
                explanation += f"Smaller range = more consistent. {correct} is more consistent."
            else:
                correct = f"Class {'A' if mean1 > mean2 else 'B'}"
                question = f"Class A scores: {', '.join(map(str, data1))}.\nClass B scores: {', '.join(map(str, data2))}.\nWhich class performed better on average?"
                explanation = f"Class A: Mean = {format_number(mean1)}\n"
                explanation += f"Class B: Mean = {format_number(mean2)}\n"
                explanation += f"Higher mean = better average performance. {correct} performed better."
            
            options = ['Class A', 'Class B', 'Both the same', 'Cannot tell']
            random.shuffle(options)
            correct_idx = options.index(correct)
        
        svg = None if i >= 25 else generate_bar_chart_svg([str(j) for j in range(len(data))], data) if 'data' in dir() and q_type != 'typical' else None
        
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
    
    return questions


def generate_level_12():
    """
    Level 12: Problem Solving & Back-to-back Stem-and-Leaf
    Higher/Mastery level - 50% visual
    SEC Style: HL Q4 style problems, back-to-back comparison
    """
    questions = []
    
    # Type 1: Back-to-back stem-and-leaf (20 questions)
    for i in range(20):
        # Generate two related datasets
        base = random.randint(40, 60)
        data_a = [base + random.randint(-15, 10) for _ in range(random.randint(10, 14))]
        data_b = [base + random.randint(-10, 15) for _ in range(random.randint(10, 14))]
        data_a = [max(20, min(90, d)) for d in data_a]
        data_b = [max(20, min(90, d)) for d in data_b]
        
        context = random.choice([('Class A', 'Class B'), ('Boys', 'Girls'), ('Morning', 'Afternoon'), ('Team X', 'Team Y')])
        
        q_type = random.choice(['compare_median', 'compare_range', 'compare_mean', 'which_better'])
        
        median_a = calculate_median(data_a)
        median_b = calculate_median(data_b)
        mean_a = calculate_mean(data_a)
        mean_b = calculate_mean(data_b)
        range_a = calculate_range(data_a)
        range_b = calculate_range(data_b)
        
        if q_type == 'compare_median':
            correct = round(abs(median_a - median_b), 1)
            if correct == int(correct):
                correct = int(correct)
            question = f"The back-to-back stem-and-leaf shows scores for {context[0]} and {context[1]}. Find the difference between the medians."
            options, correct_idx = generate_unique_options(correct, option_type='float' if isinstance(correct, float) else 'int', min_val=0)
            explanation = f"{context[0]} median = {format_number(median_a)}\n"
            explanation += f"{context[1]} median = {format_number(median_b)}\n"
            explanation += f"Difference = |{format_number(median_a)} - {format_number(median_b)}| = {format_number(correct)}"
        
        elif q_type == 'compare_range':
            correct = abs(range_a - range_b)
            question = f"The back-to-back stem-and-leaf shows scores. Find the difference between the ranges."
            options, correct_idx = generate_unique_options(correct, min_val=0)
            explanation = f"{context[0]} range = {range_a}\n"
            explanation += f"{context[1]} range = {range_b}\n"
            explanation += f"Difference = |{range_a} - {range_b}| = {correct}"
        
        elif q_type == 'compare_mean':
            correct = round(abs(mean_a - mean_b), 1)
            question = f"The diagram shows results for {context[0]} and {context[1]}. Find the difference between the means (to 1 d.p.)."
            options, correct_idx = generate_unique_options(correct, option_type='float', min_val=0)
            explanation = f"{context[0]} mean = {format_number(mean_a)}\n"
            explanation += f"{context[1]} mean = {format_number(mean_b)}\n"
            explanation += f"Difference = |{format_number(mean_a)} - {format_number(mean_b)}| = {format_number(correct)}"
        
        else:  # which_better
            better = context[0] if mean_a > mean_b else context[1]
            correct = better
            question = f"The back-to-back stem-and-leaf shows test scores. Which group performed better overall?"
            options = [context[0], context[1], 'Both the same', 'Cannot determine']
            random.shuffle(options)
            correct_idx = options.index(correct)
            explanation = f"{context[0]} mean = {format_number(mean_a)}\n"
            explanation += f"{context[1]} mean = {format_number(mean_b)}\n"
            explanation += f"{correct} has the higher mean, so performed better overall."
        
        if q_type != 'which_better':
            options = [format_number(o) for o in options]
        
        svg = generate_back_to_back_stem_leaf_svg(data_a, data_b, context[0], context[1])
        
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
    
    # Type 2: Problem solving - find missing value (15 questions)
    for i in range(15):
        # Given mean, find missing value
        n = random.randint(4, 6)
        target_mean = random.randint(10, 25)
        
        # Generate n-1 known values
        known_values = [target_mean + random.randint(-5, 5) for _ in range(n - 1)]
        
        # Calculate what the missing value should be
        required_sum = target_mean * n
        missing = required_sum - sum(known_values)
        
        # Ensure missing value is reasonable
        if missing < 0:
            known_values = [v - 5 for v in known_values]
            missing = required_sum - sum(known_values)
        
        correct = missing
        
        context = random.choice(['test score', 'number of points', 'temperature', 'height (cm)'])
        question = f"The mean of {n} {context}s is {target_mean}. If {n-1} of them are {', '.join(map(str, known_values))}, find the missing value."
        
        options, correct_idx = generate_unique_options(correct, min_val=0)
        options = [str(o) for o in options]
        
        explanation = f"Mean = Sum ÷ Count\n"
        explanation += f"{target_mean} = Sum ÷ {n}\n"
        explanation += f"Sum = {target_mean} × {n} = {required_sum}\n"
        explanation += f"Known values sum = {' + '.join(map(str, known_values))} = {sum(known_values)}\n"
        explanation += f"Missing value = {required_sum} - {sum(known_values)} = {correct}"
        
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
    
    # Type 3: Effect of adding/removing value (15 questions)
    for i in range(15):
        n = random.randint(5, 8)
        data = [random.randint(10, 30) for _ in range(n)]
        original_mean = sum(data) / n
        
        q_type = random.choice(['add_value', 'remove_value', 'change_value'])
        
        if q_type == 'add_value':
            new_value = random.randint(15, 35)
            new_mean = (sum(data) + new_value) / (n + 1)
            correct = round(new_mean, 1)
            
            question = f"The mean of {', '.join(map(str, data))} is {format_number(original_mean)}. If {new_value} is added, what is the new mean?"
            
            explanation = f"New sum = {sum(data)} + {new_value} = {sum(data) + new_value}\n"
            explanation += f"New count = {n} + 1 = {n + 1}\n"
            explanation += f"New mean = {sum(data) + new_value} ÷ {n + 1} = {format_number(new_mean)}"
        
        elif q_type == 'remove_value':
            removed_idx = random.randint(0, n - 1)
            removed_val = data[removed_idx]
            remaining = [d for j, d in enumerate(data) if j != removed_idx]
            new_mean = sum(remaining) / len(remaining)
            correct = round(new_mean, 1)
            
            question = f"The mean of {', '.join(map(str, data))} is {format_number(original_mean)}. If {removed_val} is removed, what is the new mean?"
            
            explanation = f"New sum = {sum(data)} - {removed_val} = {sum(remaining)}\n"
            explanation += f"New count = {n} - 1 = {n - 1}\n"
            explanation += f"New mean = {sum(remaining)} ÷ {n - 1} = {format_number(new_mean)}"
        
        else:  # change_value
            change_idx = random.randint(0, n - 1)
            old_val = data[change_idx]
            new_val = old_val + random.choice([-5, -3, 3, 5, 10])
            new_sum = sum(data) - old_val + new_val
            new_mean = new_sum / n
            correct = round(new_mean, 1)
            
            question = f"The mean of {n} values is {format_number(original_mean)}. If one value changes from {old_val} to {new_val}, what is the new mean?"
            
            explanation = f"Change in sum = {new_val} - {old_val} = {new_val - old_val}\n"
            explanation += f"New sum = {sum(data)} + ({new_val - old_val}) = {new_sum}\n"
            explanation += f"New mean = {new_sum} ÷ {n} = {format_number(new_mean)}"
        
        options, correct_idx = generate_unique_options(correct, option_type='float', min_val=0)
        options = [format_number(o) for o in options]
        
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
    """Validate all generated questions"""
    errors = []
    warnings = []
    
    for i, q in enumerate(questions):
        # Check required fields
        required = ['question_text', 'option_a', 'option_b', 'option_c', 'option_d', 
                    'correct_idx', 'topic', 'difficulty', 'explanation']
        for field in required:
            if field not in q or q[field] is None or q[field] == '':
                errors.append(f"Q{i+1} (L{q.get('difficulty', '?')}): Missing {field}")
        
        # Check correct_idx is valid
        if q.get('correct_idx') not in [0, 1, 2, 3]:
            errors.append(f"Q{i+1} (L{q.get('difficulty', '?')}): Invalid correct_idx: {q.get('correct_idx')}")
        
        # Check for duplicate options
        options = [q.get('option_a'), q.get('option_b'), q.get('option_c'), q.get('option_d')]
        if len(set(str(o) for o in options)) < 4:
            warnings.append(f"Q{i+1} (L{q.get('difficulty', '?')}): Duplicate options detected")
        
        # Check explanation length
        if q.get('explanation') and len(q['explanation']) < 20:
            warnings.append(f"Q{i+1} (L{q.get('difficulty', '?')}): Short explanation")
    
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
    print("🎓 AgentMath - Descriptive Statistics Generator V2")
    print("=" * 60)
    print(f"Topic: {TOPIC}")
    print(f"Target: {QUESTIONS_PER_LEVEL} questions × 12 levels = 600 total")
    print()
    print("V2 FIXES:")
    print("  ✓ Stem-and-leaf MODE questions: guaranteed unimodal data")
    print("  ✓ Frequency tables: no clipping, increased height/padding")
    print("  ✓ Frequency table text: larger font sizes (12-14px)")
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
