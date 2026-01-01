#!/usr/bin/env python3
"""
SETS & VENN DIAGRAMS - Adaptive Quiz Question Generator
========================================================
Topic: sets
Strand: Statistics and Probability
Target: 200+ questions, 75%+ visual

Visual Design Specs:
- Minimum font size: 14px (labels), 16px (numbers)
- High contrast colors
- Clear, legible text
- Diagram size: 280-350px
"""

import sqlite3
import random
import math
from datetime import datetime

DB_PATH = 'instance/mathquiz.db'

# ============================================================
# SVG GENERATORS - VENN DIAGRAMS & SETS
# ============================================================

def svg_venn_2_circles(a_only_elements, intersection_elements, b_only_elements, 
                        label_a='A', label_b='B', size=320, show_universal=True):
    """
    Two-circle Venn diagram with elements displayed
    Elements should be lists of numbers/strings
    """
    cx1, cx2 = size * 0.35, size * 0.65
    cy = size * 0.5
    r = size * 0.28
    
    svg = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
    
    # Universal set background
    if show_universal:
        svg += f'<rect x="10" y="10" width="{size-20}" height="{size-20}" fill="#f8fafc" stroke="#94a3b8" stroke-width="2" rx="8"/>'
        svg += f'<text x="25" y="35" font-size="16" fill="#64748b" font-weight="bold">U</text>'
    
    # Circle A (purple, semi-transparent)
    svg += f'<circle cx="{cx1}" cy="{cy}" r="{r}" fill="#8b5cf6" fill-opacity="0.3" stroke="#7c3aed" stroke-width="3"/>'
    
    # Circle B (green, semi-transparent)
    svg += f'<circle cx="{cx2}" cy="{cy}" r="{r}" fill="#22c55e" fill-opacity="0.3" stroke="#16a34a" stroke-width="3"/>'
    
    # Labels outside circles
    svg += f'<text x="{cx1 - r - 5}" y="{cy - r - 10}" font-size="18" fill="#7c3aed" font-weight="bold" text-anchor="middle">{label_a}</text>'
    svg += f'<text x="{cx2 + r + 5}" y="{cy - r - 10}" font-size="18" fill="#16a34a" font-weight="bold" text-anchor="middle">{label_b}</text>'
    
    # Elements in A only (left side of left circle)
    a_only_x = cx1 - r * 0.45
    for i, elem in enumerate(a_only_elements[:4]):
        y_offset = (i - len(a_only_elements[:4])/2 + 0.5) * 28
        svg += f'<text x="{a_only_x}" y="{cy + y_offset}" font-size="18" fill="#1e293b" text-anchor="middle" font-weight="500">{elem}</text>'
    
    # Elements in intersection (middle)
    int_x = (cx1 + cx2) / 2
    for i, elem in enumerate(intersection_elements[:4]):
        y_offset = (i - len(intersection_elements[:4])/2 + 0.5) * 28
        svg += f'<text x="{int_x}" y="{cy + y_offset}" font-size="18" fill="#1e293b" text-anchor="middle" font-weight="600">{elem}</text>'
    
    # Elements in B only (right side of right circle)
    b_only_x = cx2 + r * 0.45
    for i, elem in enumerate(b_only_elements[:4]):
        y_offset = (i - len(b_only_elements[:4])/2 + 0.5) * 28
        svg += f'<text x="{b_only_x}" y="{cy + y_offset}" font-size="18" fill="#1e293b" text-anchor="middle" font-weight="500">{elem}</text>'
    
    svg += '</svg>'
    return svg


def svg_venn_2_numbers(n_a_only, n_intersection, n_b_only, label_a='A', label_b='B', size=320):
    """
    Two-circle Venn diagram with COUNT numbers in each region
    """
    cx1, cx2 = size * 0.35, size * 0.65
    cy = size * 0.5
    r = size * 0.28
    
    svg = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
    
    # Universal set background
    svg += f'<rect x="10" y="10" width="{size-20}" height="{size-20}" fill="#f8fafc" stroke="#94a3b8" stroke-width="2" rx="8"/>'
    svg += f'<text x="25" y="35" font-size="16" fill="#64748b" font-weight="bold">U</text>'
    
    # Circle A
    svg += f'<circle cx="{cx1}" cy="{cy}" r="{r}" fill="#8b5cf6" fill-opacity="0.25" stroke="#7c3aed" stroke-width="3"/>'
    
    # Circle B
    svg += f'<circle cx="{cx2}" cy="{cy}" r="{r}" fill="#22c55e" fill-opacity="0.25" stroke="#16a34a" stroke-width="3"/>'
    
    # Labels
    svg += f'<text x="{cx1 - r - 5}" y="{cy - r - 10}" font-size="18" fill="#7c3aed" font-weight="bold" text-anchor="middle">{label_a}</text>'
    svg += f'<text x="{cx2 + r + 5}" y="{cy - r - 10}" font-size="18" fill="#16a34a" font-weight="bold" text-anchor="middle">{label_b}</text>'
    
    # Numbers in regions (large, bold)
    # A only
    svg += f'<text x="{cx1 - r*0.45}" y="{cy + 8}" font-size="28" fill="#7c3aed" text-anchor="middle" font-weight="bold">{n_a_only}</text>'
    
    # Intersection
    svg += f'<text x="{(cx1+cx2)/2}" y="{cy + 8}" font-size="28" fill="#1e293b" text-anchor="middle" font-weight="bold">{n_intersection}</text>'
    
    # B only
    svg += f'<text x="{cx2 + r*0.45}" y="{cy + 8}" font-size="28" fill="#16a34a" text-anchor="middle" font-weight="bold">{n_b_only}</text>'
    
    svg += '</svg>'
    return svg


def svg_venn_2_shaded(shade_region, label_a='A', label_b='B', size=320):
    """
    Two-circle Venn diagram with a region shaded
    shade_region: 'A_only', 'B_only', 'intersection', 'union', 'A_complement', 'B_complement'
    """
    cx1, cx2 = size * 0.35, size * 0.65
    cy = size * 0.5
    r = size * 0.28
    
    svg = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
    svg += '<defs>'
    
    # Clip paths for precise shading
    svg += f'<clipPath id="clipA"><circle cx="{cx1}" cy="{cy}" r="{r}"/></clipPath>'
    svg += f'<clipPath id="clipB"><circle cx="{cx2}" cy="{cy}" r="{r}"/></clipPath>'
    svg += f'<clipPath id="clipAB"><circle cx="{cx1}" cy="{cy}" r="{r}"/><circle cx="{cx2}" cy="{cy}" r="{r}"/></clipPath>'
    svg += '</defs>'
    
    # Universal set background
    svg += f'<rect x="10" y="10" width="{size-20}" height="{size-20}" fill="#f8fafc" stroke="#94a3b8" stroke-width="2" rx="8"/>'
    
    # Shading based on region
    shade_color = '#fbbf24'  # Yellow for shading
    
    if shade_region == 'A_only':
        # A minus intersection
        svg += f'<circle cx="{cx1}" cy="{cy}" r="{r}" fill="{shade_color}"/>'
        svg += f'<circle cx="{cx2}" cy="{cy}" r="{r}" fill="#f8fafc"/>'
        svg += f'<circle cx="{cx1}" cy="{cy}" r="{r}" fill="none" stroke="#7c3aed" stroke-width="3"/>'
        svg += f'<circle cx="{cx2}" cy="{cy}" r="{r}" fill="none" stroke="#16a34a" stroke-width="3"/>'
    
    elif shade_region == 'B_only':
        svg += f'<circle cx="{cx2}" cy="{cy}" r="{r}" fill="{shade_color}"/>'
        svg += f'<circle cx="{cx1}" cy="{cy}" r="{r}" fill="#f8fafc"/>'
        svg += f'<circle cx="{cx1}" cy="{cy}" r="{r}" fill="none" stroke="#7c3aed" stroke-width="3"/>'
        svg += f'<circle cx="{cx2}" cy="{cy}" r="{r}" fill="none" stroke="#16a34a" stroke-width="3"/>'
    
    elif shade_region == 'intersection':
        # Draw both circles, then shade intersection
        svg += f'<circle cx="{cx1}" cy="{cy}" r="{r}" fill="#f8fafc" stroke="#7c3aed" stroke-width="3"/>'
        svg += f'<circle cx="{cx2}" cy="{cy}" r="{r}" fill="#f8fafc" stroke="#16a34a" stroke-width="3"/>'
        # Intersection using clip
        svg += f'<g clip-path="url(#clipA)"><circle cx="{cx2}" cy="{cy}" r="{r}" fill="{shade_color}"/></g>'
        svg += f'<circle cx="{cx1}" cy="{cy}" r="{r}" fill="none" stroke="#7c3aed" stroke-width="3"/>'
        svg += f'<circle cx="{cx2}" cy="{cy}" r="{r}" fill="none" stroke="#16a34a" stroke-width="3"/>'
    
    elif shade_region == 'union':
        svg += f'<circle cx="{cx1}" cy="{cy}" r="{r}" fill="{shade_color}" stroke="#7c3aed" stroke-width="3"/>'
        svg += f'<circle cx="{cx2}" cy="{cy}" r="{r}" fill="{shade_color}" stroke="#16a34a" stroke-width="3"/>'
    
    elif shade_region == 'A_complement':
        # Everything except A
        svg += f'<rect x="10" y="10" width="{size-20}" height="{size-20}" fill="{shade_color}" rx="8"/>'
        svg += f'<circle cx="{cx1}" cy="{cy}" r="{r}" fill="#f8fafc" stroke="#7c3aed" stroke-width="3"/>'
        svg += f'<circle cx="{cx2}" cy="{cy}" r="{r}" fill="none" stroke="#16a34a" stroke-width="3"/>'
        # Re-shade B only part
        svg += f'<circle cx="{cx2}" cy="{cy}" r="{r}" fill="{shade_color}"/>'
        svg += f'<g clip-path="url(#clipA)"><circle cx="{cx2}" cy="{cy}" r="{r}" fill="#f8fafc"/></g>'
        svg += f'<circle cx="{cx1}" cy="{cy}" r="{r}" fill="none" stroke="#7c3aed" stroke-width="3"/>'
        svg += f'<circle cx="{cx2}" cy="{cy}" r="{r}" fill="none" stroke="#16a34a" stroke-width="3"/>'
    
    else:
        # Default - just outlines
        svg += f'<circle cx="{cx1}" cy="{cy}" r="{r}" fill="none" stroke="#7c3aed" stroke-width="3"/>'
        svg += f'<circle cx="{cx2}" cy="{cy}" r="{r}" fill="none" stroke="#16a34a" stroke-width="3"/>'
    
    # Labels
    svg += f'<text x="{cx1 - r - 5}" y="{cy - r - 10}" font-size="18" fill="#7c3aed" font-weight="bold" text-anchor="middle">{label_a}</text>'
    svg += f'<text x="{cx2 + r + 5}" y="{cy - r - 10}" font-size="18" fill="#16a34a" font-weight="bold" text-anchor="middle">{label_b}</text>'
    svg += f'<text x="25" y="35" font-size="16" fill="#64748b" font-weight="bold">U</text>'
    
    svg += '</svg>'
    return svg


def svg_venn_3_circles(regions, labels=['A', 'B', 'C'], size=350):
    """
    Three-circle Venn diagram with numbers in regions
    regions: dict with keys 'a_only', 'b_only', 'c_only', 'ab', 'ac', 'bc', 'abc'
    """
    cx = size / 2
    cy = size / 2
    r = size * 0.22
    offset = r * 0.7
    
    # Circle centers forming a triangle
    c1 = (cx - offset * 0.6, cy - offset * 0.3)  # A - top left
    c2 = (cx + offset * 0.6, cy - offset * 0.3)  # B - top right  
    c3 = (cx, cy + offset * 0.6)                  # C - bottom
    
    svg = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
    
    # Universal set
    svg += f'<rect x="10" y="10" width="{size-20}" height="{size-20}" fill="#f8fafc" stroke="#94a3b8" stroke-width="2" rx="8"/>'
    svg += f'<text x="25" y="35" font-size="14" fill="#64748b" font-weight="bold">U</text>'
    
    # Circles
    svg += f'<circle cx="{c1[0]}" cy="{c1[1]}" r="{r}" fill="#8b5cf6" fill-opacity="0.2" stroke="#7c3aed" stroke-width="2"/>'
    svg += f'<circle cx="{c2[0]}" cy="{c2[1]}" r="{r}" fill="#22c55e" fill-opacity="0.2" stroke="#16a34a" stroke-width="2"/>'
    svg += f'<circle cx="{c3[0]}" cy="{c3[1]}" r="{r}" fill="#f97316" fill-opacity="0.2" stroke="#ea580c" stroke-width="2"/>'
    
    # Labels
    svg += f'<text x="{c1[0] - r}" y="{c1[1] - r}" font-size="16" fill="#7c3aed" font-weight="bold">{labels[0]}</text>'
    svg += f'<text x="{c2[0] + r - 10}" y="{c2[1] - r}" font-size="16" fill="#16a34a" font-weight="bold">{labels[1]}</text>'
    svg += f'<text x="{c3[0]}" y="{c3[1] + r + 20}" font-size="16" fill="#ea580c" font-weight="bold" text-anchor="middle">{labels[2]}</text>'
    
    # Numbers in regions (approximate positions)
    # A only
    if 'a_only' in regions:
        svg += f'<text x="{c1[0] - r*0.5}" y="{c1[1]}" font-size="20" fill="#1e293b" text-anchor="middle" font-weight="bold">{regions["a_only"]}</text>'
    
    # B only
    if 'b_only' in regions:
        svg += f'<text x="{c2[0] + r*0.5}" y="{c2[1]}" font-size="20" fill="#1e293b" text-anchor="middle" font-weight="bold">{regions["b_only"]}</text>'
    
    # C only
    if 'c_only' in regions:
        svg += f'<text x="{c3[0]}" y="{c3[1] + r*0.5}" font-size="20" fill="#1e293b" text-anchor="middle" font-weight="bold">{regions["c_only"]}</text>'
    
    # A ∩ B only
    if 'ab' in regions:
        svg += f'<text x="{cx}" y="{c1[1] - r*0.1}" font-size="18" fill="#1e293b" text-anchor="middle" font-weight="bold">{regions["ab"]}</text>'
    
    # A ∩ C only
    if 'ac' in regions:
        svg += f'<text x="{c1[0] + r*0.3}" y="{cy + r*0.2}" font-size="18" fill="#1e293b" text-anchor="middle" font-weight="bold">{regions["ac"]}</text>'
    
    # B ∩ C only
    if 'bc' in regions:
        svg += f'<text x="{c2[0] - r*0.3}" y="{cy + r*0.2}" font-size="18" fill="#1e293b" text-anchor="middle" font-weight="bold">{regions["bc"]}</text>'
    
    # A ∩ B ∩ C
    if 'abc' in regions:
        svg += f'<text x="{cx}" y="{cy + 8}" font-size="18" fill="#1e293b" text-anchor="middle" font-weight="bold">{regions["abc"]}</text>'
    
    svg += '</svg>'
    return svg


def svg_set_notation(elements, set_name='A', size=300):
    """
    Visual representation of a set with elements listed
    Properly positions closing brace next to elements
    """
    # Calculate width based on content
    elem_str = ', '.join(str(e) for e in elements[:8])
    
    # Estimate text width (approximately 12px per character for size 20 font)
    set_name_width = 45  # "A =" takes about 45px
    brace_width = 20     # Each brace takes about 20px
    elem_width = len(elem_str) * 12  # Elements
    padding = 40         # Left and right padding
    
    # Calculate total width needed
    content_width = set_name_width + brace_width + elem_width + brace_width + padding
    width = max(200, min(content_width + 20, size))  # Clamp between 200 and size
    height = 80
    
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
    
    # Set bracket/box - size to fit content
    box_width = content_width - 10
    svg += f'<rect x="15" y="15" width="{box_width}" height="50" fill="#f0fdf4" stroke="#22c55e" stroke-width="3" rx="10"/>'
    
    # Set name (A =)
    svg += f'<text x="25" y="48" font-size="22" fill="#16a34a" font-weight="bold">{set_name} =</text>'
    
    # Opening brace
    open_brace_x = 25 + set_name_width
    svg += f'<text x="{open_brace_x}" y="50" font-size="26" fill="#374151" font-weight="bold">{{</text>'
    
    # Elements
    elem_x = open_brace_x + 22
    svg += f'<text x="{elem_x}" y="48" font-size="20" fill="#1e293b" font-weight="500">{elem_str}</text>'
    
    # Closing brace - position right after elements
    close_brace_x = elem_x + elem_width + 5
    svg += f'<text x="{close_brace_x}" y="50" font-size="26" fill="#374151" font-weight="bold">}}</text>'
    
    svg += '</svg>'
    return svg


def svg_element_question(element, set_elements, set_name='A', size=280):
    """
    Visual showing a set and asking if element is in it
    """
    svg = f'<svg width="{size}" height="150" viewBox="0 0 {size} 150">'
    
    # The element in question (highlighted)
    svg += f'<circle cx="50" cy="40" r="30" fill="#fef3c7" stroke="#f59e0b" stroke-width="3"/>'
    svg += f'<text x="50" y="48" font-size="24" fill="#92400e" text-anchor="middle" font-weight="bold">{element}</text>'
    
    # Arrow
    svg += f'<text x="95" y="45" font-size="24" fill="#64748b">→</text>'
    
    # The set
    svg += f'<ellipse cx="190" cy="80" rx="70" ry="50" fill="#ede9fe" stroke="#8b5cf6" stroke-width="3"/>'
    svg += f'<text x="190" y="35" font-size="18" fill="#7c3aed" text-anchor="middle" font-weight="bold">{set_name}</text>'
    
    # Elements in set
    elem_str = ', '.join(str(e) for e in set_elements[:5])
    svg += f'<text x="190" y="85" font-size="16" fill="#1e293b" text-anchor="middle" font-weight="500">{elem_str}</text>'
    
    svg += '</svg>'
    return svg


# ============================================================
# QUESTION GENERATORS
# ============================================================

def generate_beginner_questions():
    """Levels 1-3: Basic set concepts"""
    questions = []
    
    # Type 1: Count elements in a set
    sets_data = [
        ([1, 3, 5, 7], 'A'),
        ([2, 4, 6], 'B'),
        ([1, 2, 3, 4, 5], 'C'),
        ([10, 20, 30, 40], 'P'),
        ([5, 10, 15], 'Q'),
    ]
    
    for level in range(1, 4):
        for elements, name in sets_data:
            svg = svg_set_notation(elements, name)
            count = len(elements)
            
            questions.append({
                'level': level, 'band': 'beginner',
                'question': f'How many elements are in set {name}?',
                'options': [str(count), str(count+1), str(count-1), str(count+2)],
                'correct': str(count),
                'svg': svg, 'type': 'visual'
            })
    
    # Type 2: Is element in set?
    element_checks = [
        (3, [1, 2, 3, 4, 5], True),
        (7, [1, 2, 3, 4, 5], False),
        (10, [5, 10, 15, 20], True),
        (12, [5, 10, 15, 20], False),
        (4, [2, 4, 6, 8], True),
    ]
    
    for level in range(1, 4):
        for elem, set_elems, is_in in element_checks:
            svg = svg_element_question(elem, set_elems)
            correct = 'Yes' if is_in else 'No'
            
            questions.append({
                'level': level, 'band': 'beginner',
                'question': f'Is {elem} an element of this set?',
                'options': ['Yes', 'No', 'Maybe', 'Cannot tell'],
                'correct': correct,
                'svg': svg, 'type': 'visual'
            })
    
    # Type 3: Simple 2-circle Venn - identify elements
    for level in range(1, 4):
        venn_data = [
            ([1, 3], [5], [7, 9], 'A', 'B'),
            ([2, 4], [6], [8, 10], 'P', 'Q'),
            (['a', 'b'], ['c'], ['d', 'e'], 'X', 'Y'),
        ]
        
        for a_only, inter, b_only, la, lb in venn_data:
            svg = svg_venn_2_circles(a_only, inter, b_only, la, lb)
            
            # Question: What's in A only?
            correct_a = ', '.join(str(x) for x in a_only)
            questions.append({
                'level': level, 'band': 'beginner',
                'question': f'Which elements are in {la} only (not in {lb})?',
                'options': [correct_a, ', '.join(str(x) for x in inter), 
                           ', '.join(str(x) for x in b_only), ', '.join(str(x) for x in a_only + inter)],
                'correct': correct_a,
                'svg': svg, 'type': 'visual'
            })
            
            # Question: What's in the intersection?
            correct_int = ', '.join(str(x) for x in inter)
            questions.append({
                'level': level, 'band': 'beginner',
                'question': f'Which elements are in both {la} and {lb}?',
                'options': [correct_int, correct_a, ', '.join(str(x) for x in b_only), 'None'],
                'correct': correct_int,
                'svg': svg, 'type': 'visual'
            })
    
    # Type 4: Text questions - set notation
    notation_qs = [
        ('What does {1, 2, 3} represent?', 'A set with elements 1, 2, 3', 
         ['A set with elements 1, 2, 3', 'The number 123', 'Three separate numbers', 'A sequence']),
        ('What does ∈ mean?', 'is an element of',
         ['is an element of', 'is equal to', 'is not in', 'is greater than']),
        ('If A = {2, 4, 6}, what is #(A)?', '3',
         ['3', '6', '12', '2']),
        ('What does #(A) mean?', 'The number of elements in set A',
         ['The number of elements in set A', 'A times A', 'A squared', 'The hashtag of A']),
        ('What does A\\B mean?', 'Elements in A but not in B',
         ['Elements in A but not in B', 'A divided by B', 'A times B', 'Elements in both A and B']),
    ]
    
    for level in range(1, 4):
        for q, correct, options in notation_qs:
            questions.append({
                'level': level, 'band': 'beginner',
                'question': q,
                'options': options,
                'correct': correct,
                'svg': None, 'type': 'text'
            })
    
    return questions


def generate_intermediate_questions():
    """Levels 4-6: Union, intersection, complement"""
    questions = []
    
    # Type 1: Venn with numbers - find totals
    for level in range(4, 7):
        venn_configs = [
            (5, 3, 4, 'A', 'B'),  # A only, intersection, B only
            (7, 2, 6, 'P', 'Q'),
            (4, 5, 3, 'X', 'Y'),
            (8, 4, 6, 'M', 'N'),
            (3, 6, 5, 'A', 'B'),
        ]
        
        for a_only, inter, b_only, la, lb in venn_configs:
            svg = svg_venn_2_numbers(a_only, inter, b_only, la, lb)
            
            n_a = a_only + inter
            n_b = inter + b_only
            n_union = a_only + inter + b_only
            
            # #(A) question
            questions.append({
                'level': level, 'band': 'intermediate',
                'question': f'From the Venn diagram, what is #({la})?',
                'options': [str(n_a), str(a_only), str(n_union), str(inter)],
                'correct': str(n_a),
                'svg': svg, 'type': 'visual'
            })
            
            # #(A ∪ B) question
            questions.append({
                'level': level, 'band': 'intermediate',
                'question': f'From the Venn diagram, what is #({la} ∪ {lb})?',
                'options': [str(n_union), str(n_a + n_b), str(inter), str(a_only + b_only)],
                'correct': str(n_union),
                'svg': svg, 'type': 'visual'
            })
            
            # #(A ∩ B) question
            questions.append({
                'level': level, 'band': 'intermediate',
                'question': f'From the Venn diagram, what is #({la} ∩ {lb})?',
                'options': [str(inter), str(n_union), str(a_only), str(b_only)],
                'correct': str(inter),
                'svg': svg, 'type': 'visual'
            })
            
            # #(A\B) question - A without B
            questions.append({
                'level': level, 'band': 'intermediate',
                'question': f'From the Venn diagram, what is #({la}\\{lb})? (elements in {la} but not in {lb})',
                'options': [str(a_only), str(inter), str(n_a), str(b_only)],
                'correct': str(a_only),
                'svg': svg, 'type': 'visual'
            })
    
    # Type 2: Identify shaded region
    for level in range(4, 7):
        shade_configs = [
            ('intersection', 'A ∩ B'),
            ('union', 'A ∪ B'),
            ('A_only', 'A\\B (A without B)'),
            ('B_only', 'B\\A (B without A)'),
        ]
        
        for shade, correct in shade_configs:
            svg = svg_venn_2_shaded(shade)
            
            questions.append({
                'level': level, 'band': 'intermediate',
                'question': 'What does the shaded region represent?',
                'options': ['A ∩ B', 'A ∪ B', 'A\\B (A without B)', 'B\\A (B without A)'],
                'correct': correct,
                'svg': svg, 'type': 'visual'
            })
    
    # Type 3: Union/intersection with actual elements
    for level in range(4, 7):
        set_pairs = [
            ({1, 2, 3, 4}, {3, 4, 5, 6}),
            ({2, 4, 6, 8}, {1, 2, 3, 4}),
            ({5, 10, 15}, {10, 15, 20}),
        ]
        
        for set_a, set_b in set_pairs:
            a_only = sorted(set_a - set_b)
            b_only = sorted(set_b - set_a)
            inter = sorted(set_a & set_b)
            union = sorted(set_a | set_b)
            
            svg = svg_venn_2_circles(a_only, inter, b_only)
            
            # Intersection question
            inter_str = '{' + ', '.join(map(str, inter)) + '}'
            questions.append({
                'level': level, 'band': 'intermediate',
                'question': 'From the Venn diagram, what is A ∩ B?',
                'options': [inter_str, '{' + ', '.join(map(str, union)) + '}',
                           '{' + ', '.join(map(str, a_only)) + '}',
                           '{' + ', '.join(map(str, b_only)) + '}'],
                'correct': inter_str,
                'svg': svg, 'type': 'visual'
            })
    
    # Type 4: Text - definitions
    definitions = [
        ('A ∪ B means:', 'A union B (elements in A or B or both)',
         ['A union B (elements in A or B or both)', 'A intersection B', 'A without B', 'A complement']),
        ('A ∩ B means:', 'A intersection B (elements in both A and B)',
         ['A intersection B (elements in both A and B)', 'A union B', 'Elements only in A', 'Elements only in B']),
        ("A' means:", 'The complement of A (elements NOT in A)',
         ['The complement of A (elements NOT in A)', 'A squared', 'A union B', 'A intersection B']),
        ('A\\B means:', 'A without B (elements in A but not in B)',
         ['A without B (elements in A but not in B)', 'A divided by B', 'A intersection B', 'A union B']),
        ('#(A) means:', 'The cardinal number (count of elements) in A',
         ['The cardinal number (count of elements) in A', 'A times A', 'A squared', 'The hashtag of A']),
    ]
    
    for level in range(4, 7):
        for q, correct, options in definitions:
            questions.append({
                'level': level, 'band': 'intermediate',
                'question': q,
                'options': options,
                'correct': correct,
                'svg': None, 'type': 'text'
            })
    
    return questions


def generate_advanced_questions():
    """Levels 7-9: 3-circle Venn, complex problems"""
    questions = []
    
    # Type 1: 3-circle Venn diagrams
    for level in range(7, 10):
        regions_configs = [
            {'a_only': 4, 'b_only': 3, 'c_only': 5, 'ab': 2, 'ac': 1, 'bc': 3, 'abc': 1},
            {'a_only': 6, 'b_only': 4, 'c_only': 3, 'ab': 3, 'ac': 2, 'bc': 2, 'abc': 2},
            {'a_only': 5, 'b_only': 5, 'c_only': 5, 'ab': 2, 'ac': 2, 'bc': 2, 'abc': 1},
        ]
        
        for regions in regions_configs:
            svg = svg_venn_3_circles(regions)
            
            n_a = regions['a_only'] + regions['ab'] + regions['ac'] + regions['abc']
            n_b = regions['b_only'] + regions['ab'] + regions['bc'] + regions['abc']
            n_c = regions['c_only'] + regions['ac'] + regions['bc'] + regions['abc']
            total = sum(regions.values())
            
            # #(A) question
            questions.append({
                'level': level, 'band': 'advanced',
                'question': 'From the 3-circle Venn diagram, what is #(A)?',
                'options': [str(n_a), str(regions['a_only']), str(total), str(n_b)],
                'correct': str(n_a),
                'svg': svg, 'type': 'visual'
            })
            
            # Total elements
            questions.append({
                'level': level, 'band': 'advanced',
                'question': 'What is the total number of elements shown?',
                'options': [str(total), str(total + 2), str(total - 2), str(n_a + n_b + n_c)],
                'correct': str(total),
                'svg': svg, 'type': 'visual'
            })
            
            # Elements in exactly one set
            exactly_one = regions['a_only'] + regions['b_only'] + regions['c_only']
            questions.append({
                'level': level, 'band': 'advanced',
                'question': 'How many elements are in exactly one set?',
                'options': [str(exactly_one), str(total), str(regions['abc']), str(exactly_one + regions['abc'])],
                'correct': str(exactly_one),
                'svg': svg, 'type': 'visual'
            })
            
            # A\B question for 3-circle
            a_without_b = regions['a_only'] + regions['ac']
            questions.append({
                'level': level, 'band': 'advanced',
                'question': 'From the diagram, what is #(A\\B)? (elements in A but not in B)',
                'options': [str(a_without_b), str(n_a), str(regions['a_only']), str(regions['ab'])],
                'correct': str(a_without_b),
                'svg': svg, 'type': 'visual'
            })
    
    # Type 2: Formula-based 2-circle problems
    for level in range(7, 10):
        problems = [
            (20, 15, 8, 27),  # #(A)=20, #(B)=15, #(A∩B)=8, #(A∪B)=27
            (25, 18, 10, 33),
            (30, 20, 12, 38),
        ]
        
        for n_a, n_b, n_int, n_union in problems:
            svg = svg_venn_2_numbers(n_a - n_int, n_int, n_b - n_int)
            
            questions.append({
                'level': level, 'band': 'advanced',
                'question': f'If #(A) = {n_a} and #(B) = {n_b} and #(A ∩ B) = {n_int}, what is #(A ∪ B)?',
                'options': [str(n_union), str(n_a + n_b), str(n_a + n_b - n_int*2), str(n_int)],
                'correct': str(n_union),
                'svg': svg, 'type': 'visual'
            })
            
            # Reverse question - find intersection
            questions.append({
                'level': level, 'band': 'advanced',
                'question': f'If #(A) = {n_a}, #(B) = {n_b}, and #(A ∪ B) = {n_union}, what is #(A ∩ B)?',
                'options': [str(n_int), str(n_a - n_int), str(n_b - n_int), str(n_union - n_a)],
                'correct': str(n_int),
                'svg': svg, 'type': 'visual'
            })
    
    # Type 3: Text - word problems
    word_problems = [
        ('In a class of 30, 18 play football, 15 play rugby, and 8 play both. How many play neither?',
         '5', ['5', '8', '3', '0']),
        ('If #(U) = 50 and #(A) = 30, what is #(A\')?',
         '20', ['20', '30', '50', '80']),
        ('If #(A) = 12 and #(A ∩ B) = 5, what is #(A\\B)?',
         '7', ['7', '5', '12', '17']),
    ]
    
    for level in range(7, 10):
        for q, correct, options in word_problems:
            questions.append({
                'level': level, 'band': 'advanced',
                'question': q,
                'options': options,
                'correct': correct,
                'svg': None, 'type': 'text'
            })
    
    return questions


def generate_mastery_questions():
    """Level 10: Complex problems"""
    questions = []
    
    # Complex 3-circle problems
    regions = {'a_only': 8, 'b_only': 6, 'c_only': 7, 'ab': 4, 'ac': 3, 'bc': 5, 'abc': 2}
    svg = svg_venn_3_circles(regions)
    
    # Various complex questions
    questions.append({
        'level': 10, 'band': 'advanced',
        'question': 'From the diagram, what is #(A ∩ B) but NOT in C? (i.e., #((A ∩ B)\\C))',
        'options': ['4', '2', '6', '5'],
        'correct': '4',
        'svg': svg, 'type': 'visual'
    })
    
    questions.append({
        'level': 10, 'band': 'advanced',
        'question': 'How many elements are in exactly two sets?',
        'options': ['12', '10', '14', '8'],
        'correct': '12',  # ab + ac + bc = 4 + 3 + 5 = 12
        'svg': svg, 'type': 'visual'
    })
    
    questions.append({
        'level': 10, 'band': 'advanced',
        'question': 'What is #(A\\(B ∪ C))? (elements in A only)',
        'options': ['8', '15', '4', '2'],
        'correct': '8',
        'svg': svg, 'type': 'visual'
    })
    
    # Formula application
    questions.append({
        'level': 10, 'band': 'advanced',
        'question': '#(A ∪ B) = #(A) + #(B) - #(A ∩ B). If #(A) = 45, #(B) = 35, #(A ∪ B) = 60, find #(A ∩ B).',
        'options': ['20', '15', '25', '10'],
        'correct': '20',
        'svg': None, 'type': 'text'
    })
    
    questions.append({
        'level': 10, 'band': 'advanced',
        'question': 'In a survey, 80 people were asked about pets. 45 have dogs, 35 have cats, 10 have both. How many have neither?',
        'options': ['10', '0', '15', '20'],
        'correct': '10',
        'svg': None, 'type': 'text'
    })
    
    questions.append({
        'level': 10, 'band': 'advanced',
        'question': 'If #(A) = 25, #(B) = 20, and #(A\\B) = 15, what is #(A ∩ B)?',
        'options': ['10', '15', '5', '20'],
        'correct': '10',
        'svg': None, 'type': 'text'
    })
    
    questions.append({
        'level': 10, 'band': 'advanced',
        'question': 'If U = {1,2,3,4,5,6,7,8,9,10}, A = {2,4,6,8,10}, what is #(A\')?',
        'options': ['5', '10', '0', '15'],
        'correct': '5',
        'svg': None, 'type': 'text'
    })
    
    return questions


# ============================================================
# DATABASE OPERATIONS
# ============================================================

def insert_questions(questions, topic='sets'):
    """Insert questions using INSERT OR IGNORE"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    inserted = 0
    skipped = 0
    
    for q in questions:
        options = q['options']
        correct_letter = 'A'
        for i, opt in enumerate(options):
            if opt == q['correct']:
                correct_letter = ['A', 'B', 'C', 'D'][i]
                break
        
        try:
            cursor.execute('''
                INSERT OR IGNORE INTO questions_adaptive 
                (topic, question_text, option_a, option_b, option_c, option_d, 
                 correct_answer, explanation, difficulty_level, difficulty_band,
                 question_type, image_svg, is_active, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?)
            ''', (
                topic,
                q['question'],
                options[0] if len(options) > 0 else '',
                options[1] if len(options) > 1 else '',
                options[2] if len(options) > 2 else '',
                options[3] if len(options) > 3 else '',
                correct_letter,
                '',
                q['level'],
                q['band'],
                q['type'],
                q.get('svg'),
                datetime.now().isoformat()
            ))
            if cursor.rowcount > 0:
                inserted += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"Error: {e}")
            skipped += 1
    
    conn.commit()
    conn.close()
    return inserted, skipped


def show_stats():
    """Show statistics for Sets topic"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("SETS & VENN DIAGRAMS - QUESTION STATISTICS")
    print("="*60)
    
    cursor.execute("""
        SELECT difficulty_level, question_type, COUNT(*) 
        FROM questions_adaptive 
        WHERE topic='sets' AND is_active=1
        GROUP BY difficulty_level, question_type
        ORDER BY difficulty_level
    """)
    
    results = cursor.fetchall()
    if not results:
        print("\nNo questions found for 'sets' topic")
        conn.close()
        return
    
    # Summary
    cursor.execute("""
        SELECT COUNT(*), 
               SUM(CASE WHEN question_type='visual' THEN 1 ELSE 0 END)
        FROM questions_adaptive WHERE topic='sets' AND is_active=1
    """)
    total, visual = cursor.fetchone()
    
    print(f"\nTotal Questions: {total}")
    print(f"Visual: {visual} ({visual/total*100:.1f}%)" if total else "")
    print(f"Text: {total - visual} ({(total-visual)/total*100:.1f}%)" if total else "")
    
    if visual/total >= 0.75 if total else False:
        print("\n✅ 75% visual target ACHIEVED!")
    else:
        needed = int(total * 0.75) - visual if total else 0
        print(f"\n⚠️  Need {needed} more visual questions for 75%")
    
    print("\nBreakdown by level:")
    current_level = None
    for level, qtype, count in results:
        if level != current_level:
            print(f"\n  Level {level}:")
            current_level = level
        print(f"    {qtype}: {count}")
    
    conn.close()


def main():
    print("="*60)
    print("SETS & VENN DIAGRAMS - QUESTION GENERATOR")
    print("="*60)
    print("\nFollowing Phase Plan for Topic Addition...")
    
    print("\n📝 Phase 3: Generating questions...")
    
    print("\n  Generating Beginner (Levels 1-3)...")
    beginner = generate_beginner_questions()
    ins, skip = insert_questions(beginner)
    print(f"    Added {ins} questions ({skip} duplicates)")
    
    print("\n  Generating Intermediate (Levels 4-6)...")
    intermediate = generate_intermediate_questions()
    ins, skip = insert_questions(intermediate)
    print(f"    Added {ins} questions ({skip} duplicates)")
    
    print("\n  Generating Advanced (Levels 7-9)...")
    advanced = generate_advanced_questions()
    ins, skip = insert_questions(advanced)
    print(f"    Added {ins} questions ({skip} duplicates)")
    
    print("\n  Generating Mastery (Level 10)...")
    mastery = generate_mastery_questions()
    ins, skip = insert_questions(mastery)
    print(f"    Added {ins} questions ({skip} duplicates)")
    
    print("\n📊 Phase 4: Verifying insertion...")
    show_stats()
    
    print("\n" + "="*60)
    print("NEXT STEPS:")
    print("="*60)
    print("""
1. Update student_app.html - add Sets to adaptiveTopics:
   
   'Statistics and Probability': [
       { key: 'probability', title: 'Probability', icon: 'fa-dice' },
       { key: 'sets', title: 'Sets & Venn Diagrams', icon: 'fa-circle-nodes' }
   ],

2. Upload student_app.html to PythonAnywhere

3. Reload web app

4. Test the Sets topic!
""")
    print("✅ Question generation complete!")


if __name__ == '__main__':
    main()
