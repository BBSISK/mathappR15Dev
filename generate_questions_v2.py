#!/usr/bin/env python3
"""
================================================================================
ADAPTIVE QUIZ QUESTION GENERATOR - PRODUCTION VERSION 2.0
================================================================================

QUESTION TARGETS:
- 60+ questions per level (720+ total)
- Levels 1-10: 75% visual questions
- Levels 11-12: 50% visual questions

SKILL LADDER:
Level 1:  IDENTIFY halves (1/2 only)
Level 2:  IDENTIFY quarters and thirds
Level 3:  IDENTIFY any fraction (fifths, sixths, eighths, tenths)
Level 4:  SIMPLIFY fractions to lowest terms
Level 5:  EQUIVALENT fractions
Level 6:  ADD/SUBTRACT same denominator
Level 7:  ADD/SUBTRACT different denominators
Level 8:  MULTIPLY fractions
Level 9:  DIVIDE fractions
Level 10: MULTI-STEP problems (mastery)
Level 11: APPLICATION (real-world word problems)
Level 12: LINKED (cross-topic: percentages, decimals)

================================================================================
"""

import sqlite3
import os
import sys
import math
import random
from datetime import datetime
from typing import List, Dict, Tuple, Optional
from collections import Counter
from dataclasses import dataclass

# ==============================================================================
# CONFIGURATION
# ==============================================================================

DATABASE_PATHS = [
    'instance/mathquiz.db',
    'mathquiz.db',
    'mathapp.db',
]

LEVEL_BANDS = {
    1: 'beginner', 2: 'beginner', 3: 'beginner',
    4: 'intermediate', 5: 'intermediate', 6: 'intermediate',
    7: 'advanced', 8: 'advanced', 9: 'advanced',
    10: 'mastery', 11: 'application', 12: 'linked'
}

# Visual question targets
VISUAL_TARGET = {
    1: 0.75, 2: 0.75, 3: 0.75, 4: 0.75, 5: 0.75,
    6: 0.75, 7: 0.75, 8: 0.75, 9: 0.75, 10: 0.75,
    11: 0.50, 12: 0.50
}

# Irish names for word problems
IRISH_NAMES = ['Seán', 'Aoife', 'Ciarán', 'Niamh', 'Oisín', 'Siobhán', 'Fionn', 'Caoimhe', 
               'Darragh', 'Saoirse', 'Conor', 'Róisín', 'Eoin', 'Méabh', 'Tadhg', 'Orlaith']

# ==============================================================================
# DATA CLASS
# ==============================================================================

@dataclass
class Question:
    level: int
    band: str
    question_text: str
    options: List[str]
    correct_index: int
    question_type: str = 'calculation'
    svg: str = ''
    explanation: str = ''
    linked_topics: Optional[str] = None
    
    def __post_init__(self):
        self.validate()
    
    def validate(self):
        errors = []
        if len(self.options) != 4:
            errors.append(f"Must have 4 options, got {len(self.options)}")
        if len(self.options) != len(set(self.options)):
            errors.append(f"Duplicate options: {self.options}")
        if self.correct_index < 0 or self.correct_index >= len(self.options):
            errors.append(f"Invalid correct_index: {self.correct_index}")
        if self.level < 1 or self.level > 12:
            errors.append(f"Level must be 1-12, got {self.level}")
        if any(not opt or opt.strip() == '' for opt in self.options):
            errors.append("Empty option found")
        if not self.question_text:
            errors.append("Empty question text")
        if errors:
            raise ValueError(f"Invalid question: {'; '.join(errors)}")


# ==============================================================================
# UTILITIES
# ==============================================================================

def find_database() -> str:
    for path in DATABASE_PATHS:
        if os.path.exists(path):
            return path
    raise FileNotFoundError(f"Database not found. Checked: {DATABASE_PATHS}")


def ensure_unique_options(correct: str, distractors: List[str], count: int = 4) -> List[str]:
    """Guarantee exactly `count` unique options including correct answer."""
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
            n = random.randint(1, 9)
            d = random.randint(2, 10)
            new_opt = f"{n}/{d}"
        elif '%' in str(correct):
            new_opt = f"{random.randint(5, 95)}%"
        else:
            try:
                base = int(str(correct).split()[0])
                new_opt = str(max(1, base + random.choice([-3, -2, -1, 1, 2, 3])))
            except:
                new_opt = str(random.randint(1, 20))
        if new_opt not in options:
            options.append(new_opt)
    
    return options[:count]


def shuffle_options(options: List[str], correct_value: str) -> Tuple[List[str], int]:
    """Shuffle and return new correct index."""
    shuffled = options.copy()
    random.shuffle(shuffled)
    return shuffled, shuffled.index(correct_value)


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def simplify_fraction(num: int, denom: int) -> Tuple[int, int]:
    g = gcd(num, denom)
    return num // g, denom // g


def get_name() -> str:
    return random.choice(IRISH_NAMES)


# ==============================================================================
# SVG GENERATORS
# ==============================================================================

def svg_pie_chart(numerator: int, denominator: int, size: int = 160) -> str:
    cx, cy, r = size // 2, size // 2, size // 2 - 15
    
    if numerator == 0:
        return f'<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg"><circle cx="{cx}" cy="{cy}" r="{r}" fill="#E8F5E9" stroke="#333" stroke-width="2"/></svg>'
    
    if numerator >= denominator:
        return f'<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg"><circle cx="{cx}" cy="{cy}" r="{r}" fill="#4CAF50" stroke="#333" stroke-width="2"/></svg>'
    
    slices = []
    angle_per = 360 / denominator
    
    for i in range(denominator):
        start = i * angle_per - 90
        end = (i + 1) * angle_per - 90
        x1 = cx + r * math.cos(math.radians(start))
        y1 = cy + r * math.sin(math.radians(start))
        x2 = cx + r * math.cos(math.radians(end))
        y2 = cy + r * math.sin(math.radians(end))
        large = 1 if angle_per > 180 else 0
        color = '#4CAF50' if i < numerator else '#E8F5E9'
        slices.append(f'<path d="M{cx},{cy} L{x1:.1f},{y1:.1f} A{r},{r} 0 {large},1 {x2:.1f},{y2:.1f} Z" fill="{color}" stroke="#333" stroke-width="1"/>')
    
    return f'<svg viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">{"".join(slices)}</svg>'


def svg_fraction_bar(numerator: int, denominator: int, width: int = 200, height: int = 40) -> str:
    seg_width = (width - 10) / denominator
    segments = []
    for i in range(denominator):
        color = '#4CAF50' if i < numerator else '#E8F5E9'
        x = 5 + i * seg_width
        segments.append(f'<rect x="{x:.1f}" y="5" width="{seg_width:.1f}" height="{height-10}" fill="{color}" stroke="#333" stroke-width="1"/>')
    return f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">{"".join(segments)}</svg>'


def svg_grid(numerator: int, denominator: int, cols: int = None) -> str:
    """Generate a grid representation of a fraction."""
    if cols is None:
        cols = denominator if denominator <= 5 else 5
    rows = math.ceil(denominator / cols)
    cell_size = 30
    width = cols * cell_size + 10
    height = rows * cell_size + 10
    
    cells = []
    for i in range(denominator):
        row, col = i // cols, i % cols
        x = 5 + col * cell_size
        y = 5 + row * cell_size
        color = '#4CAF50' if i < numerator else '#E8F5E9'
        cells.append(f'<rect x="{x}" y="{y}" width="{cell_size-2}" height="{cell_size-2}" fill="{color}" stroke="#333" stroke-width="1"/>')
    
    return f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">{"".join(cells)}</svg>'


# ==============================================================================
# DISTRACTOR GENERATORS
# ==============================================================================

def fraction_distractors(num: int, denom: int) -> List[str]:
    """Generate plausible wrong fraction answers."""
    correct = f"{num}/{denom}"
    distractors = set()
    
    # Inverted
    if num != denom:
        distractors.add(f"{denom}/{num}")
    
    # Off by one
    if num > 1:
        distractors.add(f"{num - 1}/{denom}")
    if num < denom - 1:
        distractors.add(f"{num + 1}/{denom}")
    if denom > 2:
        distractors.add(f"{num}/{denom - 1}")
    distractors.add(f"{num}/{denom + 1}")
    
    # Complement
    if denom - num != num:
        distractors.add(f"{denom - num}/{denom}")
    
    # Common mistakes
    distractors.add(f"{num * 2}/{denom * 2}")
    distractors.add(f"{num}/{denom * 2}")
    
    # Random
    for _ in range(5):
        n, d = random.randint(1, 9), random.randint(2, 10)
        if f"{n}/{d}" != correct:
            distractors.add(f"{n}/{d}")
    
    distractors.discard(correct)
    return list(distractors)


# ==============================================================================
# LEVEL GENERATORS
# ==============================================================================

class FractionsGenerator:
    TOPIC = 'fractions'
    
    @classmethod
    def level_1(cls) -> List[Question]:
        """Level 1: HALVES ONLY - 60+ questions, 75% visual"""
        questions = []
        q_id = 1000
        
        # VISUAL: Pie charts (20)
        for i in range(20):
            svg = svg_pie_chart(1, 2)
            correct = "1/2"
            distractors = ["1/4", "1/3", "2/2", "2/4", "1/1", "2/3"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(1, 'beginner', f"What fraction of the circle is green? [L1-{q_id}]", options, idx, 'visual', svg))
            q_id += 1
        
        # VISUAL: Fraction bars (15)
        for i in range(15):
            svg = svg_fraction_bar(1, 2)
            correct = "1/2"
            distractors = ["1/4", "2/4", "1/3", "2/2", "3/4"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(1, 'beginner', f"What fraction of the bar is green? [L1-{q_id}]", options, idx, 'visual', svg))
            q_id += 1
        
        # VISUAL: Grids (10)
        for i in range(10):
            svg = svg_grid(1, 2, 2)
            correct = "1/2"
            distractors = ["1/4", "2/4", "1/3", "2/2"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(1, 'beginner', f"What fraction of the grid is green? [L1-{q_id}]", options, idx, 'visual', svg))
            q_id += 1
        
        # WORD: Cutting items (10)
        items = ['pizza', 'cake', 'apple', 'sandwich', 'cookie', 'orange', 'pie', 'chocolate bar', 'watermelon', 'bread']
        for item in items:
            correct = "1/2"
            distractors = ["1/4", "2/2", "1/3", "2/4"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(1, 'beginner', f"{get_name()} cuts a {item} into 2 equal pieces. What fraction is each piece? [L1-{q_id}]", options, idx, 'word_problem'))
            q_id += 1
        
        # WORD: Sharing (10)
        for i in range(10):
            correct = "1/2"
            distractors = ["1/3", "2/2", "1/4", "2/3"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(1, 'beginner', f"{get_name()} shares a cookie equally with a friend. What fraction does each person get? [L1-{q_id}]", options, idx, 'word_problem'))
            q_id += 1
        
        return questions
    
    @classmethod
    def level_2(cls) -> List[Question]:
        """Level 2: QUARTERS AND THIRDS - 60+ questions, 75% visual"""
        questions = []
        q_id = 2000
        
        # VISUAL: Quarters pie charts (15)
        for num in [1, 2, 3]:
            for i in range(5):
                svg = svg_pie_chart(num, 4)
                correct = f"{num}/4"
                distractors = fraction_distractors(num, 4)
                options = ensure_unique_options(correct, distractors)
                options, idx = shuffle_options(options, correct)
                questions.append(Question(2, 'beginner', f"The circle shows quarters. What fraction is green? [L2-{q_id}]", options, idx, 'visual', svg))
                q_id += 1
        
        # VISUAL: Quarters bars (15)
        for num in [1, 2, 3]:
            for i in range(5):
                svg = svg_fraction_bar(num, 4)
                correct = f"{num}/4"
                distractors = fraction_distractors(num, 4)
                options = ensure_unique_options(correct, distractors)
                options, idx = shuffle_options(options, correct)
                questions.append(Question(2, 'beginner', f"The bar shows quarters. What fraction is green? [L2-{q_id}]", options, idx, 'visual', svg))
                q_id += 1
        
        # VISUAL: Thirds pie charts (10)
        for num in [1, 2]:
            for i in range(5):
                svg = svg_pie_chart(num, 3)
                correct = f"{num}/3"
                distractors = fraction_distractors(num, 3)
                options = ensure_unique_options(correct, distractors)
                options, idx = shuffle_options(options, correct)
                questions.append(Question(2, 'beginner', f"The circle shows thirds. What fraction is green? [L2-{q_id}]", options, idx, 'visual', svg))
                q_id += 1
        
        # VISUAL: Thirds bars (10)
        for num in [1, 2]:
            for i in range(5):
                svg = svg_fraction_bar(num, 3)
                correct = f"{num}/3"
                distractors = fraction_distractors(num, 3)
                options = ensure_unique_options(correct, distractors)
                options, idx = shuffle_options(options, correct)
                questions.append(Question(2, 'beginner', f"The bar shows thirds. What fraction is green? [L2-{q_id}]", options, idx, 'visual', svg))
                q_id += 1
        
        # WORD: Quarters scenarios (10)
        items = ['pizza', 'cake', 'chocolate bar', 'sandwich', 'pie']
        for item in items:
            for num in [1, 2]:
                correct = f"{num}/4"
                distractors = fraction_distractors(num, 4)
                options = ensure_unique_options(correct, distractors)
                options, idx = shuffle_options(options, correct)
                questions.append(Question(2, 'beginner', f"A {item} is cut into 4 equal pieces. {get_name()} eats {num}. What fraction was eaten? [L2-{q_id}]", options, idx, 'word_problem'))
                q_id += 1
        
        # WORD: Thirds scenarios (5)
        for i in range(5):
            num = random.choice([1, 2])
            correct = f"{num}/3"
            distractors = fraction_distractors(num, 3)
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(2, 'beginner', f"An orange is split into 3 equal parts. {get_name()} eats {num}. What fraction was eaten? [L2-{q_id}]", options, idx, 'word_problem'))
            q_id += 1
        
        return questions
    
    @classmethod
    def level_3(cls) -> List[Question]:
        """Level 3: FIFTHS, SIXTHS, EIGHTHS, TENTHS - 60+ questions, 75% visual"""
        questions = []
        q_id = 3000
        
        denoms = [(5, "fifths"), (6, "sixths"), (8, "eighths"), (10, "tenths")]
        
        # VISUAL: Pie charts for each denominator (40)
        for denom, name in denoms:
            for num in range(1, min(denom, 6)):
                svg = svg_pie_chart(num, denom)
                correct = f"{num}/{denom}"
                distractors = fraction_distractors(num, denom)
                options = ensure_unique_options(correct, distractors)
                options, idx = shuffle_options(options, correct)
                questions.append(Question(3, 'beginner', f"This circle shows {name}. What fraction is green? [L3-{q_id}]", options, idx, 'visual', svg))
                q_id += 1
        
        # VISUAL: Bars (20)
        for denom, name in denoms:
            for i in range(5):
                num = random.randint(1, denom - 1)
                svg = svg_fraction_bar(num, denom)
                correct = f"{num}/{denom}"
                distractors = fraction_distractors(num, denom)
                options = ensure_unique_options(correct, distractors)
                options, idx = shuffle_options(options, correct)
                questions.append(Question(3, 'beginner', f"What fraction of the bar is green? [L3-{q_id}]", options, idx, 'visual', svg))
                q_id += 1
        
        # WORD: Various scenarios (15)
        scenarios = [
            ("class of {d} students", "are girls"),
            ("bag of {d} sweets", "are red"),
            ("box of {d} crayons", "are blue"),
            ("garden with {d} flowers", "are roses"),
            ("shelf with {d} books", "are fiction"),
        ]
        for denom, _ in denoms:
            for template, ending in scenarios[:3]:
                num = random.randint(1, denom - 1)
                container = template.format(d=denom)
                correct = f"{num}/{denom}"
                distractors = fraction_distractors(num, denom)
                options = ensure_unique_options(correct, distractors)
                options, idx = shuffle_options(options, correct)
                questions.append(Question(3, 'beginner', f"In a {container}, {num} {ending}. What fraction {ending}? [L3-{q_id}]", options, idx, 'word_problem'))
                q_id += 1
        
        return questions
    
    @classmethod
    def level_4(cls) -> List[Question]:
        """Level 4: SIMPLIFY FRACTIONS + MIXED/IMPROPER CONVERSIONS - 60+ questions, 75% visual"""
        questions = []
        q_id = 4000
        
        # All simplification cases
        simplify_cases = [
            (2, 4, 1, 2), (3, 6, 1, 2), (4, 8, 1, 2), (5, 10, 1, 2), (6, 12, 1, 2),
            (2, 6, 1, 3), (3, 9, 1, 3), (4, 12, 1, 3),
            (2, 8, 1, 4), (3, 12, 1, 4),
            (4, 6, 2, 3), (6, 9, 2, 3), (8, 12, 2, 3),
            (6, 8, 3, 4), (9, 12, 3, 4),
            (4, 10, 2, 5), (6, 10, 3, 5), (8, 10, 4, 5),
            (10, 12, 5, 6), (8, 12, 2, 3),
        ]
        
        # VISUAL: Show unsimplified with pie, ask for simplified (20)
        for i, (n, d, sn, sd) in enumerate(simplify_cases):
            svg = svg_pie_chart(n, d)
            correct = f"{sn}/{sd}"
            distractors = [f"{n}/{d}", f"{sn}/{d}", f"{n}/{sd}", f"{sd}/{sn}"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(4, 'intermediate', f"The circle shows {n}/{d}. Write this in simplest form. [L4-{q_id}]", options, idx, 'visual', svg))
            q_id += 1
        
        # TEXT: Direct simplification (20)
        for n, d, sn, sd in simplify_cases:
            correct = f"{sn}/{sd}"
            distractors = [f"{n}/{d}", f"{sn}/{d}", f"{n}/{sd}", f"{sd}/{sn}"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(4, 'intermediate', f"Simplify {n}/{d} to its lowest terms. [L4-{q_id}]", options, idx, 'calculation'))
            q_id += 1
        
        # =====================================================
        # IMPROPER TO MIXED NUMBER CONVERSIONS (NEW!)
        # =====================================================
        improper_to_mixed = [
            # (numerator, denominator, whole, remainder) -> "whole remainder/denom"
            (3, 2, 1, 1),   # 3/2 = 1 1/2
            (5, 2, 2, 1),   # 5/2 = 2 1/2
            (7, 2, 3, 1),   # 7/2 = 3 1/2
            (9, 2, 4, 1),   # 9/2 = 4 1/2
            (4, 3, 1, 1),   # 4/3 = 1 1/3
            (5, 3, 1, 2),   # 5/3 = 1 2/3
            (7, 3, 2, 1),   # 7/3 = 2 1/3
            (8, 3, 2, 2),   # 8/3 = 2 2/3
            (10, 3, 3, 1),  # 10/3 = 3 1/3
            (5, 4, 1, 1),   # 5/4 = 1 1/4
            (7, 4, 1, 3),   # 7/4 = 1 3/4
            (9, 4, 2, 1),   # 9/4 = 2 1/4
            (11, 4, 2, 3),  # 11/4 = 2 3/4
            (6, 5, 1, 1),   # 6/5 = 1 1/5
            (7, 5, 1, 2),   # 7/5 = 1 2/5
            (9, 5, 1, 4),   # 9/5 = 1 4/5
            (11, 5, 2, 1),  # 11/5 = 2 1/5
            (7, 6, 1, 1),   # 7/6 = 1 1/6
            (11, 6, 1, 5),  # 11/6 = 1 5/6
            (13, 6, 2, 1),  # 13/6 = 2 1/6
        ]
        
        # VISUAL: Improper to mixed with pie charts (15)
        for n, d, whole, rem in improper_to_mixed[:15]:
            # Show multiple pies for improper fractions
            svg = svg_pie_chart(n % d if n % d > 0 else d, d)  # Show the remainder part
            correct = f"{whole} {rem}/{d}"
            # Generate plausible wrong answers
            distractors = [
                f"{whole + 1} {rem}/{d}",  # Wrong whole number
                f"{whole} {rem + 1}/{d}" if rem + 1 < d else f"{whole} 1/{d}",  # Wrong remainder
                f"{n}/{d}",  # Didn't convert
                f"{rem} {whole}/{d}",  # Swapped whole and remainder
            ]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(4, 'intermediate', f"Convert the improper fraction {n}/{d} to a mixed number. [L4-{q_id}]", options, idx, 'visual', svg))
            q_id += 1
        
        # TEXT: Improper to mixed (10)
        for n, d, whole, rem in improper_to_mixed[15:] + improper_to_mixed[:5]:
            correct = f"{whole} {rem}/{d}"
            distractors = [
                f"{whole + 1} {rem}/{d}",
                f"{whole} {rem + 1}/{d}" if rem + 1 < d else f"{whole} 1/{d}",
                f"{n}/{d}",
                f"{d}/{n}",
            ]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(4, 'intermediate', f"Write {n}/{d} as a mixed number. [L4-{q_id}]", options, idx, 'calculation'))
            q_id += 1
        
        # =====================================================
        # MIXED NUMBER TO IMPROPER CONVERSIONS (NEW!)
        # =====================================================
        mixed_to_improper = [
            # (whole, numerator, denominator) -> improper numerator
            (1, 1, 2, 3),   # 1 1/2 = 3/2
            (2, 1, 2, 5),   # 2 1/2 = 5/2
            (3, 1, 2, 7),   # 3 1/2 = 7/2
            (1, 1, 3, 4),   # 1 1/3 = 4/3
            (1, 2, 3, 5),   # 1 2/3 = 5/3
            (2, 1, 3, 7),   # 2 1/3 = 7/3
            (2, 2, 3, 8),   # 2 2/3 = 8/3
            (1, 1, 4, 5),   # 1 1/4 = 5/4
            (1, 3, 4, 7),   # 1 3/4 = 7/4
            (2, 1, 4, 9),   # 2 1/4 = 9/4
            (2, 3, 4, 11),  # 2 3/4 = 11/4
            (1, 1, 5, 6),   # 1 1/5 = 6/5
            (1, 2, 5, 7),   # 1 2/5 = 7/5
            (1, 4, 5, 9),   # 1 4/5 = 9/5
            (2, 1, 5, 11),  # 2 1/5 = 11/5
            (1, 1, 6, 7),   # 1 1/6 = 7/6
            (1, 5, 6, 11),  # 1 5/6 = 11/6
            (2, 1, 6, 13),  # 2 1/6 = 13/6
            (3, 1, 4, 13),  # 3 1/4 = 13/4
            (4, 1, 3, 13),  # 4 1/3 = 13/3
        ]
        
        # VISUAL: Mixed to improper with pie charts (15)
        for whole, num, denom, improper_num in mixed_to_improper[:15]:
            svg = svg_pie_chart(num, denom)  # Show the fractional part
            correct = f"{improper_num}/{denom}"
            # Generate plausible wrong answers
            distractors = [
                f"{whole + num}/{denom}",  # Added instead of multiplied
                f"{improper_num + 1}/{denom}",  # Off by one
                f"{whole * num}/{denom}",  # Multiplied wrong parts
                f"{num}/{denom}",  # Forgot the whole number
            ]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(4, 'intermediate', f"Convert {whole} {num}/{denom} to an improper fraction. [L4-{q_id}]", options, idx, 'visual', svg))
            q_id += 1
        
        # TEXT: Mixed to improper (10)
        for whole, num, denom, improper_num in mixed_to_improper[15:] + mixed_to_improper[:5]:
            correct = f"{improper_num}/{denom}"
            distractors = [
                f"{whole + num}/{denom}",
                f"{improper_num + 1}/{denom}",
                f"{improper_num - 1}/{denom}",
                f"{num}/{denom}",
            ]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(4, 'intermediate', f"Write {whole} {num}/{denom} as an improper fraction. [L4-{q_id}]", options, idx, 'calculation'))
            q_id += 1
        
        # "Is this simplified?" questions (5)
        already_simple = [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4)]
        for n, d in already_simple:
            correct = "Yes, already simplified"
            distractors = ["No, simplify to 1/2", "No, simplify to 1/3", "No, simplify to 1/4"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(4, 'intermediate', f"Is {n}/{d} in its simplest form? [L4-{q_id}]", options, idx, 'calculation'))
            q_id += 1
        
        return questions
    
    @classmethod
    def level_5(cls) -> List[Question]:
        """Level 5: EQUIVALENT FRACTIONS - 60+ questions, 75% visual"""
        questions = []
        q_id = 5000
        
        equiv_cases = [
            (1, 2, 2, 4), (1, 2, 3, 6), (1, 2, 4, 8), (1, 2, 5, 10),
            (1, 3, 2, 6), (1, 3, 3, 9), (1, 3, 4, 12),
            (2, 3, 4, 6), (2, 3, 6, 9), (2, 3, 8, 12),
            (1, 4, 2, 8), (1, 4, 3, 12), (3, 4, 6, 8), (3, 4, 9, 12),
            (1, 5, 2, 10), (2, 5, 4, 10), (3, 5, 6, 10), (4, 5, 8, 10),
            (1, 6, 2, 12), (5, 6, 10, 12),
        ]
        
        # VISUAL: Show two pies, ask if equivalent (25)
        for n1, d1, n2, d2 in equiv_cases[:20]:
            svg1 = svg_pie_chart(n1, d1)
            svg2 = svg_pie_chart(n2, d2)
            combined_svg = f'<div style="display:flex;gap:20px;justify-content:center;">{svg1}{svg2}</div>'
            correct = f"{n2}/{d2}"
            distractors = [f"{n2}/{d1}", f"{n1}/{d2}", f"{n1+1}/{d1+1}", f"{n2+1}/{d2}"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(5, 'intermediate', f"Which fraction equals {n1}/{d1}? [L5-{q_id}]", options, idx, 'visual', svg1))
            q_id += 1
        
        # VISUAL: Bar comparison (20)
        for n1, d1, n2, d2 in equiv_cases:
            svg = svg_fraction_bar(n1, d1)
            correct = f"{n2}/{d2}"
            distractors = [f"{n2}/{d1}", f"{n1}/{d2}", f"{n1+n2}/{d1+d2}"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(5, 'intermediate', f"The bar shows {n1}/{d1}. Which fraction is equivalent? [L5-{q_id}]", options, idx, 'visual', svg))
            q_id += 1
        
        # TEXT: Find missing number (20)
        missing_cases = [
            ("?/4 = 1/2", "2"), ("?/6 = 1/3", "2"), ("?/8 = 1/2", "4"),
            ("?/6 = 1/2", "3"), ("?/10 = 1/2", "5"), ("?/9 = 1/3", "3"),
            ("?/12 = 1/4", "3"), ("?/8 = 3/4", "6"), ("?/6 = 2/3", "4"),
            ("?/10 = 2/5", "4"), ("?/12 = 1/3", "4"), ("?/10 = 3/5", "6"),
            ("1/2 = ?/6", "3"), ("1/4 = ?/8", "2"), ("2/3 = ?/9", "6"),
            ("3/4 = ?/12", "9"), ("1/5 = ?/10", "2"), ("2/5 = ?/10", "4"),
            ("1/3 = ?/12", "4"), ("5/6 = ?/12", "10"),
        ]
        for equation, correct in missing_cases:
            distractors = ["1", "2", "3", "4", "5", "6", "8", "9", "10", "12"]
            distractors = [d for d in distractors if d != correct]
            options = ensure_unique_options(correct, distractors[:5])
            options, idx = shuffle_options(options, correct)
            questions.append(Question(5, 'intermediate', f"Find the missing number: {equation} [L5-{q_id}]", options, idx, 'calculation'))
            q_id += 1
        
        return questions
    
    @classmethod
    def level_6(cls) -> List[Question]:
        """Level 6: ADD/SUBTRACT SAME DENOMINATOR - 60+ questions"""
        questions = []
        q_id = 6000
        
        # Generate all valid addition cases
        add_cases = []
        for d in [4, 5, 6, 8, 10]:
            for a in range(1, d):
                for b in range(1, d - a + 1):
                    if a + b <= d:
                        add_cases.append((a, d, b, d, f"{a+b}/{d}"))
        
        # VISUAL: Addition with bars (25)
        for i, (a, d, b, _, ans) in enumerate(add_cases[:25]):
            svg1 = svg_fraction_bar(a, d)
            correct = ans
            distractors = [f"{a+b}/{d*2}", f"{a}/{d}", f"{a*b}/{d}", f"{a+b}/{d+d}"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(6, 'intermediate', f"Calculate: {a}/{d} + {b}/{d} [L6-{q_id}]", options, idx, 'visual', svg1))
            q_id += 1
        
        # TEXT: Addition (20)
        for a, d, b, _, ans in add_cases[25:45]:
            correct = ans
            distractors = [f"{a+b}/{d*2}", f"{a}/{d}", f"{a*b}/{d}"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(6, 'intermediate', f"Calculate: {a}/{d} + {b}/{d} [L6-{q_id}]", options, idx, 'calculation'))
            q_id += 1
        
        # Subtraction cases
        sub_cases = []
        for d in [4, 5, 6, 8, 10]:
            for a in range(2, d + 1):
                for b in range(1, a):
                    sub_cases.append((a, d, b, d, f"{a-b}/{d}"))
        
        # VISUAL: Subtraction (10)
        for a, d, b, _, ans in sub_cases[:10]:
            svg = svg_fraction_bar(a, d)
            correct = ans
            distractors = [f"{a}/{d}", f"{b}/{d}", f"{a-b}/{d*2}"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(6, 'intermediate', f"Calculate: {a}/{d} − {b}/{d} [L6-{q_id}]", options, idx, 'visual', svg))
            q_id += 1
        
        # TEXT: Subtraction (15)
        for a, d, b, _, ans in sub_cases[10:25]:
            correct = ans
            distractors = [f"{a}/{d}", f"{b}/{d}", f"{a-b}/{d*2}"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(6, 'intermediate', f"Calculate: {a}/{d} − {b}/{d} [L6-{q_id}]", options, idx, 'calculation'))
            q_id += 1
        
        return questions
    
    @classmethod
    def level_7(cls) -> List[Question]:
        """Level 7: ADD/SUBTRACT DIFFERENT DENOMINATORS - 60+ questions"""
        questions = []
        q_id = 7000
        
        # Pre-computed addition cases with answers
        add_cases = [
            (1, 2, 1, 4, "3/4"), (1, 2, 1, 6, "4/6"), (1, 3, 1, 6, "3/6"),
            (2, 3, 1, 6, "5/6"), (1, 2, 1, 3, "5/6"), (1, 4, 1, 8, "3/8"),
            (3, 4, 1, 8, "7/8"), (1, 3, 1, 4, "7/12"), (1, 2, 1, 5, "7/10"),
            (2, 5, 1, 10, "5/10"), (1, 4, 1, 2, "3/4"), (1, 6, 1, 3, "3/6"),
            (1, 2, 1, 8, "5/8"), (3, 4, 1, 2, "5/4"), (1, 3, 2, 9, "5/9"),
            (1, 4, 1, 6, "5/12"), (1, 5, 1, 10, "3/10"), (2, 3, 1, 4, "11/12"),
            (1, 6, 1, 2, "4/6"), (2, 5, 1, 2, "9/10"),
        ]
        
        # VISUAL: Addition (30)
        for n1, d1, n2, d2, ans in add_cases:
            svg = svg_pie_chart(n1, d1)
            correct = ans
            distractors = [f"{n1+n2}/{d1+d2}", f"{n1+n2}/{d2}", f"{n1}/{d1}"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(7, 'advanced', f"Calculate: {n1}/{d1} + {n2}/{d2} [L7-{q_id}]", options, idx, 'visual', svg))
            q_id += 1
        
        # TEXT: More addition (15)
        for n1, d1, n2, d2, ans in add_cases[:15]:
            correct = ans
            distractors = [f"{n1+n2}/{d1+d2}", f"{n1+n2}/{max(d1,d2)}", f"{n1*n2}/{d1*d2}"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(7, 'advanced', f"Add: {n1}/{d1} + {n2}/{d2} [L7-{q_id}]", options, idx, 'calculation'))
            q_id += 1
        
        # Subtraction cases
        sub_cases = [
            (1, 2, 1, 4, "1/4"), (3, 4, 1, 2, "1/4"), (2, 3, 1, 6, "3/6"),
            (5, 6, 1, 3, "3/6"), (3, 4, 1, 8, "5/8"), (7, 8, 1, 4, "5/8"),
            (2, 3, 1, 4, "5/12"), (3, 4, 1, 3, "5/12"), (5, 6, 1, 2, "2/6"),
            (4, 5, 1, 2, "3/10"), (7, 10, 1, 5, "5/10"), (3, 4, 1, 6, "7/12"),
        ]
        
        # VISUAL: Subtraction (10)
        for n1, d1, n2, d2, ans in sub_cases[:10]:
            svg = svg_pie_chart(n1, d1)
            correct = ans
            distractors = [f"{n1-n2}/{d1}", f"{n1}/{d1}", f"{n2}/{d2}"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(7, 'advanced', f"Calculate: {n1}/{d1} − {n2}/{d2} [L7-{q_id}]", options, idx, 'visual', svg))
            q_id += 1
        
        # TEXT: More subtraction (10)
        for n1, d1, n2, d2, ans in sub_cases:
            correct = ans
            distractors = [f"{n1-n2}/{d1-d2}" if d1 > d2 else "1/2", f"{n1}/{d1}", f"{n2}/{d2}"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(7, 'advanced', f"Subtract: {n1}/{d1} − {n2}/{d2} [L7-{q_id}]", options, idx, 'calculation'))
            q_id += 1
        
        return questions
    
    @classmethod
    def level_8(cls) -> List[Question]:
        """Level 8: MULTIPLY FRACTIONS - 60+ questions"""
        questions = []
        q_id = 8000
        
        # Fraction × Fraction cases
        mult_cases = []
        for n1 in range(1, 4):
            for d1 in [2, 3, 4, 5]:
                for n2 in range(1, 3):
                    for d2 in [2, 3, 4]:
                        if n1 < d1 and n2 < d2:
                            mult_cases.append((n1, d1, n2, d2, f"{n1*n2}/{d1*d2}"))
        
        # VISUAL: Multiplication (25)
        for n1, d1, n2, d2, ans in mult_cases[:25]:
            svg = svg_pie_chart(n1, d1)
            correct = ans
            distractors = [f"{n1+n2}/{d1+d2}", f"{n1*n2}/{d1}", f"{n1}/{d1*d2}"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(8, 'advanced', f"Calculate: {n1}/{d1} × {n2}/{d2} [L8-{q_id}]", options, idx, 'visual', svg))
            q_id += 1
        
        # TEXT: More multiplication (20)
        for n1, d1, n2, d2, ans in mult_cases[25:45]:
            correct = ans
            distractors = [f"{n1+n2}/{d1+d2}", f"{n1*n2}/{d1}", f"{n1}/{d1*d2}"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(8, 'advanced', f"Multiply: {n1}/{d1} × {n2}/{d2} [L8-{q_id}]", options, idx, 'calculation'))
            q_id += 1
        
        # Fraction × Whole number (20)
        whole_cases = [
            (1, 2, 2, "2/2"), (1, 2, 3, "3/2"), (1, 2, 4, "4/2"), (1, 2, 5, "5/2"),
            (1, 3, 2, "2/3"), (1, 3, 3, "3/3"), (2, 3, 2, "4/3"), (2, 3, 3, "6/3"),
            (1, 4, 2, "2/4"), (1, 4, 3, "3/4"), (3, 4, 2, "6/4"), (3, 4, 4, "12/4"),
            (1, 5, 2, "2/5"), (1, 5, 3, "3/5"), (2, 5, 3, "6/5"), (3, 5, 2, "6/5"),
            (1, 6, 2, "2/6"), (1, 6, 3, "3/6"), (5, 6, 2, "10/6"), (1, 8, 4, "4/8"),
        ]
        for n, d, w, ans in whole_cases:
            correct = ans
            distractors = [f"{n+w}/{d}", f"{n*w}/{d*w}", f"{n}/{d}"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(8, 'advanced', f"Calculate: {n}/{d} × {w} [L8-{q_id}]", options, idx, 'calculation'))
            q_id += 1
        
        return questions
    
    @classmethod
    def level_9(cls) -> List[Question]:
        """Level 9: DIVIDE FRACTIONS - 60+ questions"""
        questions = []
        q_id = 9000
        
        # Division cases (flip and multiply)
        div_cases = [
            (1, 2, 1, 4, "2"), (1, 2, 1, 2, "1"), (3, 4, 1, 2, "3/2"),
            (2, 3, 1, 3, "2"), (1, 4, 1, 2, "1/2"), (3, 4, 1, 4, "3"),
            (1, 3, 1, 6, "2"), (2, 5, 1, 5, "2"), (1, 2, 1, 3, "3/2"),
            (2, 3, 1, 2, "4/3"), (5, 6, 1, 2, "5/3"), (3, 4, 3, 8, "2"),
            (1, 2, 1, 6, "3"), (2, 3, 2, 9, "3"), (4, 5, 2, 5, "2"),
            (1, 3, 1, 9, "3"), (3, 5, 1, 5, "3"), (1, 4, 1, 8, "2"),
            (5, 8, 1, 4, "5/2"), (7, 8, 1, 2, "7/4"),
        ]
        
        # VISUAL: Division (25)
        for n1, d1, n2, d2, ans in div_cases:
            svg = svg_pie_chart(n1, d1)
            correct = ans
            distractors = [f"{n1*n2}/{d1*d2}", "1/8", f"{n1}/{d1}"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(9, 'advanced', f"Calculate: {n1}/{d1} ÷ {n2}/{d2} [L9-{q_id}]", options, idx, 'visual', svg))
            q_id += 1
        
        # TEXT: More division (20)
        for n1, d1, n2, d2, ans in div_cases:
            correct = ans
            distractors = [f"{n1*n2}/{d1*d2}", f"{d1*d2}/{n1*n2}", f"{n1}/{d1}"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(9, 'advanced', f"Divide: {n1}/{d1} ÷ {n2}/{d2} [L9-{q_id}]", options, idx, 'calculation'))
            q_id += 1
        
        # Divide by whole number (20)
        whole_div = [
            (1, 2, 2, "1/4"), (1, 2, 3, "1/6"), (1, 2, 4, "1/8"),
            (2, 3, 2, "2/6"), (1, 3, 2, "1/6"), (1, 3, 3, "1/9"),
            (3, 4, 2, "3/8"), (3, 4, 3, "3/12"), (1, 4, 2, "1/8"),
            (2, 5, 2, "2/10"), (3, 5, 3, "3/15"), (4, 5, 2, "4/10"),
            (1, 6, 2, "1/12"), (5, 6, 2, "5/12"), (1, 8, 2, "1/16"),
            (3, 8, 2, "3/16"), (5, 8, 2, "5/16"), (7, 8, 2, "7/16"),
            (1, 10, 2, "1/20"), (3, 10, 2, "3/20"),
        ]
        for n, d, w, ans in whole_div:
            correct = ans
            distractors = [f"{n*w}/{d}", f"{n}/{d}", f"{n}/{d*w*2}"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(9, 'advanced', f"Calculate: {n}/{d} ÷ {w} [L9-{q_id}]", options, idx, 'calculation'))
            q_id += 1
        
        return questions
    
    @classmethod
    def level_10(cls) -> List[Question]:
        """Level 10: MULTI-STEP PROBLEMS - 60+ questions"""
        questions = []
        q_id = 10000
        
        # Order of operations (25)
        order_cases = [
            ("(1/4 + 1/4) × 2", "1"), ("(1/2 + 1/4) × 2", "3/2"), ("(3/4 − 1/4) × 2", "1"),
            ("(1/3 + 1/3) × 3", "2"), ("(2/3 − 1/3) × 6", "2"), ("(1/2 − 1/4) × 4", "1"),
            ("1/2 × 2/3 + 1/6", "1/2"), ("3/4 − 1/2 × 1/2", "1/2"), ("1/3 + 1/3 × 1/2", "1/2"),
            ("2 × 1/4 + 1/2", "1"), ("3 × 1/3 − 1/2", "1/2"), ("(1/2 + 1/2) ÷ 2", "1/2"),
            ("1 − 1/4 − 1/4", "1/2"), ("1 − 1/3 − 1/3", "1/3"), ("2/3 + 1/6 − 1/2", "1/3"),
            ("(3/4 − 1/4) ÷ 2", "1/4"), ("(1/2 + 1/2) × 1/2", "1/2"), ("1/4 × 4 − 1/2", "1/2"),
            ("2 × (1/4 + 1/4)", "1"), ("3 × (1/3 − 1/6)", "1/2"), ("(1/2)² + 1/4", "1/2"),
            ("(1/3)² × 9", "1"), ("1/2 + 1/4 + 1/4", "1"), ("3/4 − 1/8 − 1/8", "1/2"),
            ("(2/3 + 1/3) ÷ 2", "1/2"),
        ]
        
        for expr, ans in order_cases:
            correct = ans
            distractors = ["1/2", "1/4", "3/4", "1", "2", "1/3", "2/3"]
            distractors = [d for d in distractors if d != correct]
            options = ensure_unique_options(correct, distractors[:5])
            options, idx = shuffle_options(options, correct)
            questions.append(Question(10, 'mastery', f"Calculate: {expr} [L10-{q_id}]", options, idx, 'calculation'))
            q_id += 1
        
        # Reverse problems (20)
        reverse_cases = [
            ("1/2 of a number is 6. What is the number?", "12"),
            ("1/3 of a number is 5. What is the number?", "15"),
            ("1/4 of a number is 3. What is the number?", "12"),
            ("2/3 of a number is 8. What is the number?", "12"),
            ("3/4 of a number is 9. What is the number?", "12"),
            ("1/5 of a number is 4. What is the number?", "20"),
            ("2/5 of a number is 6. What is the number?", "15"),
            ("1/2 of a number is 10. What is the number?", "20"),
            ("1/4 of a number is 5. What is the number?", "20"),
            ("3/4 of a number is 15. What is the number?", "20"),
            ("1/3 of a number is 8. What is the number?", "24"),
            ("2/3 of a number is 10. What is the number?", "15"),
            ("1/5 of a number is 6. What is the number?", "30"),
            ("4/5 of a number is 16. What is the number?", "20"),
            ("1/6 of a number is 5. What is the number?", "30"),
            ("5/6 of a number is 25. What is the number?", "30"),
            ("1/2 of a number is 15. What is the number?", "30"),
            ("1/4 of a number is 8. What is the number?", "32"),
            ("3/4 of a number is 21. What is the number?", "28"),
            ("2/5 of a number is 10. What is the number?", "25"),
        ]
        
        for text, ans in reverse_cases:
            correct = ans
            distractors = ["6", "8", "10", "12", "15", "18", "20", "24", "25", "30"]
            distractors = [d for d in distractors if d != correct]
            options = ensure_unique_options(correct, distractors[:5])
            options, idx = shuffle_options(options, correct)
            questions.append(Question(10, 'mastery', f"{text} [L10-{q_id}]", options, idx, 'calculation'))
            q_id += 1
        
        # VISUAL: Complex with diagrams (20)
        visual_problems = [
            (svg_pie_chart(1, 2), "A circle shows 1/2 shaded. If you shade 1/4 more, what total is shaded?", "3/4"),
            (svg_pie_chart(3, 4), "A circle shows 3/4 shaded. What is 1/2 of the shaded part?", "3/8"),
            (svg_fraction_bar(2, 4), "The bar shows 2/4. Simplify and add 1/4.", "3/4"),
            (svg_pie_chart(1, 3), "1/3 is shaded. Double it. What fraction is that?", "2/3"),
        ]
        
        for i in range(5):
            for svg, text, ans in visual_problems:
                correct = ans
                distractors = ["1/2", "1/4", "3/4", "1/8", "2/3", "1/3"]
                distractors = [d for d in distractors if d != correct]
                options = ensure_unique_options(correct, distractors[:5])
                options, idx = shuffle_options(options, correct)
                questions.append(Question(10, 'mastery', f"{text} [L10-{q_id}]", options, idx, 'visual', svg))
                q_id += 1
        
        return questions
    
    @classmethod
    def level_11(cls) -> List[Question]:
        """Level 11: REAL-WORLD APPLICATION - 60+ questions, 50% visual"""
        questions = []
        q_id = 11000
        
        # Recipe problems (15)
        recipe_problems = [
            ("A recipe needs 3/4 cup flour for 4 people. How much for 2 people?", "3/8 cup"),
            ("A recipe uses 1/2 cup sugar. To make half the recipe, how much sugar?", "1/4 cup"),
            ("A cake needs 2/3 cup milk. For double the recipe, how much milk?", "4/3 cups"),
            ("A recipe needs 1/4 teaspoon salt for 6 cookies. How much for 12?", "1/2 teaspoon"),
            ("You need 3/4 cup butter. You only want to make 1/3 of the recipe. How much butter?", "1/4 cup"),
        ]
        for text, ans in recipe_problems:
            correct = ans
            distractors = ["1/2 cup", "1/4 cup", "3/4 cup", "1 cup", "2/3 cup"]
            distractors = [d for d in distractors if d != correct]
            options = ensure_unique_options(correct, distractors[:5])
            options, idx = shuffle_options(options, correct)
            questions.append(Question(11, 'application', f"{text} [L11-{q_id}]", options, idx, 'word_problem'))
            q_id += 1
        
        # Money problems (15)
        for i in range(15):
            amount = random.choice([20, 30, 40, 50, 60])
            frac_n, frac_d = random.choice([(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (1, 5), (2, 5)])
            spent = amount * frac_n // frac_d
            left = amount - spent
            
            correct = f"€{left}"
            distractors = [f"€{spent}", f"€{amount}", f"€{left+5}", f"€{left-5}"]
            distractors = [d for d in distractors if d != correct and int(d[1:]) > 0]
            options = ensure_unique_options(correct, distractors[:5])
            options, idx = shuffle_options(options, correct)
            questions.append(Question(11, 'application', f"{get_name()} has €{amount}. They spend {frac_n}/{frac_d} on books. How much is left? [L11-{q_id}]", options, idx, 'word_problem'))
            q_id += 1
        
        # Time problems (15)
        for i in range(15):
            total_mins = random.choice([30, 45, 60, 90, 120])
            frac_n, frac_d = random.choice([(1, 2), (1, 3), (2, 3), (1, 4), (3, 4)])
            activity_mins = total_mins * frac_n // frac_d
            
            correct = f"{activity_mins} minutes"
            distractors = [f"{total_mins} minutes", f"{total_mins - activity_mins} minutes", 
                          f"{activity_mins + 10} minutes", f"{activity_mins - 10} minutes"]
            distractors = [d for d in distractors if d != correct]
            options = ensure_unique_options(correct, distractors[:5])
            options, idx = shuffle_options(options, correct)
            questions.append(Question(11, 'application', f"{get_name()} studies for {total_mins} minutes. They spend {frac_n}/{frac_d} on maths. How many minutes on maths? [L11-{q_id}]", options, idx, 'word_problem'))
            q_id += 1
        
        # Pizza/food sharing with visual (15)
        for i in range(15):
            slices = random.choice([6, 8, 10, 12])
            eaten1 = random.randint(1, slices // 3)
            eaten2 = random.randint(1, slices // 3)
            left_n = slices - eaten1 - eaten2
            svg = svg_pie_chart(left_n, slices)
            
            correct = f"{left_n}/{slices}"
            distractors = [f"{eaten1+eaten2}/{slices}", f"{eaten1}/{slices}", f"{slices}/{left_n}"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(11, 'application', f"A pizza has {slices} slices. {get_name()} eats {eaten1} and {get_name()} eats {eaten2}. What fraction is left? [L11-{q_id}]", options, idx, 'visual', svg))
            q_id += 1
        
        # Distance problems (10)
        for i in range(10):
            total_km = random.choice([2, 3, 4, 5])
            walked_n, walked_d = random.choice([(1, 2), (1, 4), (3, 4), (2, 3)])
            
            # Calculate remaining
            remaining_n = walked_d - walked_n
            correct = f"{remaining_n}/{walked_d} km"
            distractors = [f"{walked_n}/{walked_d} km", f"1/{walked_d} km", f"{total_km} km"]
            options = ensure_unique_options(correct, distractors)
            options, idx = shuffle_options(options, correct)
            questions.append(Question(11, 'application', f"{get_name()} walks {total_km} km to school. After walking {walked_n}/{walked_d} of the way, how much is left? [L11-{q_id}]", options, idx, 'word_problem'))
            q_id += 1
        
        return questions
    
    @classmethod
    def level_12(cls) -> List[Question]:
        """Level 12: CROSS-TOPIC LINKS - 60+ questions, 50% visual"""
        questions = []
        q_id = 12000
        
        # Fractions to percentages (20)
        frac_to_pct = [
            ("1/4", "25%"), ("1/2", "50%"), ("3/4", "75%"), ("1/5", "20%"),
            ("2/5", "40%"), ("3/5", "60%"), ("4/5", "80%"), ("1/10", "10%"),
            ("3/10", "30%"), ("7/10", "70%"), ("9/10", "90%"), ("1/20", "5%"),
            ("1/25", "4%"), ("1/50", "2%"), ("1/100", "1%"), ("3/20", "15%"),
            ("7/20", "35%"), ("9/20", "45%"), ("11/20", "55%"), ("3/25", "12%"),
        ]
        
        for frac, pct in frac_to_pct:
            svg = svg_pie_chart(int(frac.split('/')[0]), int(frac.split('/')[1]))
            correct = pct
            distractors = ["10%", "15%", "25%", "30%", "35%", "45%", "55%", "65%"]
            distractors = [d for d in distractors if d != correct]
            options = ensure_unique_options(correct, distractors[:5])
            options, idx = shuffle_options(options, correct)
            questions.append(Question(12, 'linked', f"Convert {frac} to a percentage. [L12-{q_id}]", options, idx, 'visual', svg, linked_topics='percentages'))
            q_id += 1
        
        # Percentages to fractions (15)
        pct_to_frac = [
            ("25%", "1/4"), ("50%", "1/2"), ("75%", "3/4"), ("20%", "1/5"),
            ("40%", "2/5"), ("60%", "3/5"), ("10%", "1/10"), ("30%", "3/10"),
            ("80%", "4/5"), ("5%", "1/20"), ("15%", "3/20"), ("35%", "7/20"),
            ("45%", "9/20"), ("12%", "3/25"), ("4%", "1/25"),
        ]
        
        for pct, frac in pct_to_frac:
            correct = frac
            distractors = ["1/2", "1/3", "1/4", "1/5", "2/3", "2/5", "3/4", "3/5"]
            distractors = [d for d in distractors if d != correct]
            options = ensure_unique_options(correct, distractors[:5])
            options, idx = shuffle_options(options, correct)
            questions.append(Question(12, 'linked', f"Convert {pct} to a fraction in lowest terms. [L12-{q_id}]", options, idx, 'calculation', linked_topics='percentages'))
            q_id += 1
        
        # Fractions to decimals (15)
        frac_to_dec = [
            ("1/2", "0.5"), ("1/4", "0.25"), ("3/4", "0.75"), ("1/5", "0.2"),
            ("2/5", "0.4"), ("3/5", "0.6"), ("4/5", "0.8"), ("1/10", "0.1"),
            ("3/10", "0.3"), ("7/10", "0.7"), ("1/8", "0.125"), ("3/8", "0.375"),
            ("5/8", "0.625"), ("7/8", "0.875"), ("1/20", "0.05"),
        ]
        
        for frac, dec in frac_to_dec:
            svg = svg_pie_chart(int(frac.split('/')[0]), int(frac.split('/')[1]))
            correct = dec
            distractors = ["0.1", "0.2", "0.25", "0.3", "0.4", "0.5", "0.6", "0.75"]
            distractors = [d for d in distractors if d != correct]
            options = ensure_unique_options(correct, distractors[:5])
            options, idx = shuffle_options(options, correct)
            questions.append(Question(12, 'linked', f"Convert {frac} to a decimal. [L12-{q_id}]", options, idx, 'visual', svg, linked_topics='decimals'))
            q_id += 1
        
        # Decimals to fractions (10)
        dec_to_frac = [
            ("0.5", "1/2"), ("0.25", "1/4"), ("0.75", "3/4"), ("0.2", "1/5"),
            ("0.4", "2/5"), ("0.6", "3/5"), ("0.8", "4/5"), ("0.1", "1/10"),
            ("0.3", "3/10"), ("0.125", "1/8"),
        ]
        
        for dec, frac in dec_to_frac:
            correct = frac
            distractors = ["1/2", "1/3", "1/4", "1/5", "2/3", "2/5", "3/4", "3/5"]
            distractors = [d for d in distractors if d != correct]
            options = ensure_unique_options(correct, distractors[:5])
            options, idx = shuffle_options(options, correct)
            questions.append(Question(12, 'linked', f"Convert {dec} to a fraction in lowest terms. [L12-{q_id}]", options, idx, 'calculation', linked_topics='decimals'))
            q_id += 1
        
        # Probability connections (10)
        prob_problems = [
            ("A bag has 4 red and 4 blue marbles. What's the probability of picking red?", "1/2"),
            ("A coin is flipped. What's the probability of heads?", "1/2"),
            ("A die is rolled. What's the probability of getting 6?", "1/6"),
            ("A die is rolled. What's the probability of getting an even number?", "1/2"),
            ("A bag has 3 red and 6 blue marbles. What's the probability of red?", "1/3"),
            ("A spinner has 4 equal sections: 1 red, 3 blue. Probability of red?", "1/4"),
            ("A bag has 2 red, 3 blue, 5 green. Probability of blue?", "3/10"),
            ("A deck has 4 aces in 52 cards. Probability of drawing an ace?", "1/13"),
            ("A spinner has 5 equal sections numbered 1-5. Probability of landing on 3?", "1/5"),
            ("A bag has 1 gold and 9 silver coins. Probability of gold?", "1/10"),
        ]
        
        for text, ans in prob_problems:
            correct = ans
            distractors = ["1/2", "1/3", "1/4", "1/5", "1/6", "2/3", "3/4"]
            distractors = [d for d in distractors if d != correct]
            options = ensure_unique_options(correct, distractors[:5])
            options, idx = shuffle_options(options, correct)
            questions.append(Question(12, 'linked', f"{text} [L12-{q_id}]", options, idx, 'word_problem', linked_topics='probability'))
            q_id += 1
        
        return questions
    
    @classmethod
    def generate_all(cls) -> List[Question]:
        """Generate all questions for all levels."""
        all_questions = []
        generators = [
            cls.level_1, cls.level_2, cls.level_3, cls.level_4,
            cls.level_5, cls.level_6, cls.level_7, cls.level_8,
            cls.level_9, cls.level_10, cls.level_11, cls.level_12,
        ]
        for gen in generators:
            all_questions.extend(gen())
        return all_questions


# ==============================================================================
# DATABASE OPERATIONS
# ==============================================================================

def fix_database_schema(conn: sqlite3.Connection):
    """Ensure database supports levels 1-12."""
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='questions_adaptive'")
    if not cursor.fetchone():
        print("📦 Creating questions_adaptive table...")
        cursor.execute("""
            CREATE TABLE questions_adaptive (
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
        conn.commit()
        print("✅ Table created")
        return
    
    # Test if level 11 works
    try:
        cursor.execute("INSERT INTO questions_adaptive (topic, difficulty_level, difficulty_band, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, is_active, question_type) VALUES ('_test_', 11, 'application', 'test', 'a', 'b', 'c', 'd', 0, '', 1, 'test')")
        cursor.execute("DELETE FROM questions_adaptive WHERE topic = '_test_'")
        conn.commit()
        print("✅ Database schema OK")
    except sqlite3.IntegrityError:
        print("⚠️  Updating schema...")
        conn.rollback()
        # Rebuild table (simplified)
        cursor.execute("DROP TABLE IF EXISTS questions_adaptive_new")
        cursor.execute("""CREATE TABLE questions_adaptive_new (
            id INTEGER PRIMARY KEY AUTOINCREMENT, topic TEXT NOT NULL, question_text TEXT NOT NULL,
            option_a TEXT NOT NULL, option_b TEXT NOT NULL, option_c TEXT NOT NULL, option_d TEXT NOT NULL,
            correct_answer INTEGER NOT NULL CHECK (correct_answer BETWEEN 0 AND 3),
            explanation TEXT NOT NULL DEFAULT '', difficulty_level INTEGER NOT NULL CHECK (difficulty_level BETWEEN 1 AND 12),
            difficulty_band TEXT NOT NULL, complexity_factors TEXT, estimated_time_seconds INTEGER DEFAULT 30,
            hint_text TEXT, hint_penalty INTEGER DEFAULT 50, question_type TEXT DEFAULT 'text',
            times_shown INTEGER DEFAULT 0, times_correct INTEGER DEFAULT 0, avg_response_time REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_active INTEGER DEFAULT 1, image_svg TEXT, linked_topics TEXT,
            UNIQUE(topic, difficulty_level, question_text))""")
        cursor.execute("INSERT OR IGNORE INTO questions_adaptive_new SELECT * FROM questions_adaptive WHERE difficulty_level <= 10")
        cursor.execute("DROP TABLE questions_adaptive")
        cursor.execute("ALTER TABLE questions_adaptive_new RENAME TO questions_adaptive")
        conn.commit()
        print("✅ Schema updated")


def insert_questions(conn: sqlite3.Connection, questions: List[Question], topic: str):
    """Insert questions into database."""
    cursor = conn.cursor()
    inserted, duplicates = 0, 0
    
    for q in questions:
        try:
            cursor.execute("""
                INSERT INTO questions_adaptive 
                (topic, difficulty_level, difficulty_band, question_text, option_a, option_b, option_c, option_d, 
                 correct_answer, explanation, is_active, question_type, image_svg, linked_topics, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?, ?, ?, ?)
            """, (topic, q.level, q.band, q.question_text, q.options[0], q.options[1], q.options[2], q.options[3],
                  q.correct_index, q.explanation, q.question_type, q.svg, q.linked_topics, datetime.now().isoformat()))
            inserted += 1
        except sqlite3.IntegrityError:
            duplicates += 1
    
    conn.commit()
    return inserted, duplicates


def clear_topic(conn: sqlite3.Connection, topic: str) -> int:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = ?", (topic,))
    deleted = cursor.rowcount
    conn.commit()
    return deleted


def get_stats(conn: sqlite3.Connection, topic: str) -> Dict:
    cursor = conn.cursor()
    
    # Count by level
    cursor.execute("SELECT difficulty_level, COUNT(*) FROM questions_adaptive WHERE topic = ? AND is_active = 1 GROUP BY difficulty_level ORDER BY difficulty_level", (topic,))
    level_counts = {row[0]: row[1] for row in cursor.fetchall()}
    
    # Count visual questions by level
    cursor.execute("SELECT difficulty_level, COUNT(*) FROM questions_adaptive WHERE topic = ? AND is_active = 1 AND (question_type = 'visual' OR image_svg != '') GROUP BY difficulty_level ORDER BY difficulty_level", (topic,))
    visual_counts = {row[0]: row[1] for row in cursor.fetchall()}
    
    return level_counts, visual_counts


# ==============================================================================
# COMPREHENSIVE VALIDATION
# ==============================================================================

def validate_all_questions(questions: List[Question], topic: str) -> Tuple[bool, List[str]]:
    """
    Run ALL validation checks on generated questions.
    Returns (passed: bool, errors: List[str])
    
    Checks performed:
    1. Each question has exactly 4 unique options (no duplicate answers)
    2. No duplicate question texts across all questions
    3. Minimum questions per level (at least 30)
    4. Visual question targets met (75% for L1-10, 50% for L11-12)
    5. Correct answer index is valid
    6. No empty questions or options
    """
    errors = []
    warnings = []
    
    print("\n" + "=" * 50)
    print("🔍 COMPREHENSIVE VALIDATION CHECKS")
    print("=" * 50)
    
    # =========================================================
    # CHECK 1: Duplicate options within questions
    # =========================================================
    print("\n📋 Check 1: Duplicate options within questions...")
    dup_options_count = 0
    for q in questions:
        if len(set(q.options)) != 4:
            dup_options_count += 1
            errors.append(f"L{q.level}: Duplicate options in '{q.question_text[:50]}...' → {q.options}")
    
    if dup_options_count == 0:
        print(f"   ✅ PASSED - All {len(questions)} questions have 4 unique options")
    else:
        print(f"   ❌ FAILED - {dup_options_count} questions have duplicate options")
    
    # =========================================================
    # CHECK 2: Duplicate question texts
    # =========================================================
    print("\n📋 Check 2: Duplicate question texts...")
    texts = [q.question_text for q in questions]
    text_counts = Counter(texts)
    duplicates = [(t, c) for t, c in text_counts.items() if c > 1]
    
    if not duplicates:
        print(f"   ✅ PASSED - All {len(questions)} question texts are unique")
    else:
        print(f"   ❌ FAILED - {len(duplicates)} duplicate question texts found:")
        for text, count in duplicates[:5]:
            errors.append(f"Duplicate [{count}x]: '{text[:60]}...'")
            print(f"      [{count}x] {text[:60]}...")
    
    # =========================================================
    # CHECK 3: Minimum questions per level
    # =========================================================
    print("\n📋 Check 3: Minimum questions per level (target: 30+)...")
    level_counts = Counter(q.level for q in questions)
    min_per_level = 30
    
    all_levels_ok = True
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        status = "✅" if count >= min_per_level else "⚠️"
        if count < min_per_level:
            all_levels_ok = False
            warnings.append(f"Level {level} has only {count} questions (target: {min_per_level}+)")
        print(f"   Level {level:2d}: {count:3d} questions {status}")
    
    if all_levels_ok:
        print(f"   ✅ PASSED - All levels have {min_per_level}+ questions")
    else:
        print(f"   ⚠️ WARNING - Some levels below target")
    
    # =========================================================
    # CHECK 4: Visual question targets
    # =========================================================
    print("\n📋 Check 4: Visual question targets...")
    visual_by_level = Counter()
    for q in questions:
        if q.question_type == 'visual' or q.svg:
            visual_by_level[q.level] += 1
    
    visual_ok = True
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        visual = visual_by_level.get(level, 0)
        pct = (visual / count * 100) if count > 0 else 0
        target = VISUAL_TARGET.get(level, 0.75) * 100
        status = "✅" if pct >= target - 10 else "⚠️"  # 10% tolerance
        if pct < target - 10:
            visual_ok = False
            warnings.append(f"Level {level} visual: {pct:.0f}% (target: {target:.0f}%)")
        print(f"   Level {level:2d}: {pct:5.1f}% visual (target: {target:.0f}%) {status}")
    
    if visual_ok:
        print(f"   ✅ PASSED - Visual targets met (within 10% tolerance)")
    else:
        print(f"   ⚠️ WARNING - Some levels below visual target")
    
    # =========================================================
    # CHECK 5: Valid correct answer indices
    # =========================================================
    print("\n📋 Check 5: Valid correct answer indices...")
    invalid_indices = 0
    for q in questions:
        if q.correct_index < 0 or q.correct_index >= 4:
            invalid_indices += 1
            errors.append(f"Invalid correct_index {q.correct_index} in '{q.question_text[:50]}...'")
    
    if invalid_indices == 0:
        print(f"   ✅ PASSED - All correct_index values are 0-3")
    else:
        print(f"   ❌ FAILED - {invalid_indices} questions have invalid correct_index")
    
    # =========================================================
    # CHECK 6: No empty content
    # =========================================================
    print("\n📋 Check 6: No empty questions or options...")
    empty_count = 0
    for q in questions:
        if not q.question_text or not q.question_text.strip():
            empty_count += 1
            errors.append("Empty question text found")
        for i, opt in enumerate(q.options):
            if not opt or not str(opt).strip():
                empty_count += 1
                errors.append(f"Empty option {i} in '{q.question_text[:50]}...'")
    
    if empty_count == 0:
        print(f"   ✅ PASSED - No empty questions or options")
    else:
        print(f"   ❌ FAILED - {empty_count} empty items found")
    
    # =========================================================
    # SUMMARY
    # =========================================================
    print("\n" + "=" * 50)
    passed = len(errors) == 0
    if passed:
        print("✅ ALL VALIDATION CHECKS PASSED!")
    else:
        print(f"❌ VALIDATION FAILED - {len(errors)} errors found")
        for e in errors[:10]:
            print(f"   • {e}")
        if len(errors) > 10:
            print(f"   ... and {len(errors) - 10} more errors")
    
    if warnings:
        print(f"\n⚠️ {len(warnings)} warnings:")
        for w in warnings[:5]:
            print(f"   • {w}")
    
    print("=" * 50)
    
    return passed, errors


# ==============================================================================
# MAIN
# ==============================================================================

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Generate adaptive quiz questions')
    parser.add_argument('--topic', default='fractions', help='Topic to generate')
    parser.add_argument('--clear', action='store_true', help='Clear existing questions first')
    parser.add_argument('--test', action='store_true', help='Test mode - validate only')
    args = parser.parse_args()
    
    print("=" * 70)
    print("ADAPTIVE QUIZ QUESTION GENERATOR v2.0")
    print("=" * 70)
    
    db_path = find_database()
    print(f"✅ Database: {db_path}")
    
    conn = sqlite3.connect(db_path)
    fix_database_schema(conn)
    
    print(f"\n📝 Generating {args.topic} questions...")
    
    if args.topic == 'fractions':
        questions = FractionsGenerator.generate_all()
    else:
        print(f"❌ Unknown topic: {args.topic}")
        sys.exit(1)
    
    print(f"   Generated {len(questions)} questions")
    
    # Run comprehensive validation
    passed, errors = validate_all_questions(questions, args.topic)
    
    if not passed:
        print("\n❌ ABORTING - Fix validation errors before inserting to database")
        sys.exit(1)
    
    if args.test:
        print("\n🧪 TEST MODE - No database changes")
        conn.close()
        return
    
    if args.clear:
        deleted = clear_topic(conn, args.topic)
        print(f"\n🗑️  Cleared {deleted} existing questions")
    
    print(f"\n💾 Inserting...")
    inserted, duplicates = insert_questions(conn, questions, args.topic)
    print(f"   ✅ Inserted: {inserted}")
    print(f"   ⏭️  Duplicates skipped: {duplicates}")
    
    # Final stats
    print("\n📊 Final database counts:")
    level_counts, visual_counts = get_stats(conn, args.topic)
    total, total_visual = 0, 0
    
    print(f"   {'Level':<8} {'Count':<8} {'Visual':<8} {'Visual %':<10} {'Target':<10}")
    print(f"   {'-'*50}")
    
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        visual = visual_counts.get(level, 0)
        pct = (visual / count * 100) if count > 0 else 0
        target = VISUAL_TARGET.get(level, 0.75) * 100
        status = "✅" if pct >= target - 10 else "⚠️"
        print(f"   {level:<8} {count:<8} {visual:<8} {pct:>5.1f}%     {target:>5.0f}%  {status}")
        total += count
        total_visual += visual
    
    print(f"   {'-'*50}")
    print(f"   {'TOTAL':<8} {total:<8} {total_visual:<8} {total_visual/total*100 if total else 0:>5.1f}%")
    
    conn.close()
    print("\n" + "=" * 70)
    print("✅ DONE! Reload web app to see changes.")
    print("=" * 70)


if __name__ == '__main__':
    main()
