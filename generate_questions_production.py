#!/usr/bin/env python3
"""
================================================================================
ADAPTIVE QUIZ QUESTION GENERATOR - PRODUCTION VERSION
================================================================================

This is the MASTER generator template for all topics. It includes:

1. GUARANTEED UNIQUE OPTIONS - Validated before insertion
2. PROPER SKILL PROGRESSION - Each level introduces new cognitive demand
3. REUSABLE PATTERNS - Template for any topic
4. FULL VALIDATION - No bad data enters the database
5. COMPREHENSIVE TESTING - Verify before deploy

USAGE:
    python3 generate_questions_production.py --topic fractions
    python3 generate_questions_production.py --topic fractions --clear
    python3 generate_questions_production.py --topic fractions --test

Author: AgentMath System
Version: 1.0.0
================================================================================
"""

import sqlite3
import os
import sys
import math
import random
from datetime import datetime
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from abc import ABC, abstractmethod


# ==============================================================================
# CONFIGURATION
# ==============================================================================

DATABASE_PATHS = [
    'instance/mathquiz.db',
    'mathquiz.db',
    'mathapp.db',
]

# Difficulty bands by level
LEVEL_BANDS = {
    1: 'beginner', 2: 'beginner', 3: 'beginner',
    4: 'intermediate', 5: 'intermediate', 6: 'intermediate',
    7: 'advanced', 8: 'advanced', 9: 'advanced',
    10: 'mastery', 11: 'application', 12: 'linked'
}


# ==============================================================================
# DATA CLASSES
# ==============================================================================

@dataclass
class Question:
    """Represents a single question with full validation"""
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
        """Validate question on creation"""
        self.validate()
    
    def validate(self):
        """Ensure question meets all requirements"""
        errors = []
        
        # Must have exactly 4 options
        if len(self.options) != 4:
            errors.append(f"Must have exactly 4 options, got {len(self.options)}")
        
        # All options must be unique
        if len(self.options) != len(set(self.options)):
            duplicates = [o for o in self.options if self.options.count(o) > 1]
            errors.append(f"Duplicate options found: {duplicates}")
        
        # Correct index must be valid
        if self.correct_index < 0 or self.correct_index >= len(self.options):
            errors.append(f"Invalid correct_index: {self.correct_index}")
        
        # Level must be 1-12
        if self.level < 1 or self.level > 12:
            errors.append(f"Level must be 1-12, got {self.level}")
        
        # No empty options
        if any(not opt or opt.strip() == '' for opt in self.options):
            errors.append("Empty option found")
        
        # No empty question text
        if not self.question_text or self.question_text.strip() == '':
            errors.append("Empty question text")
        
        if errors:
            raise ValueError(f"Invalid question: {'; '.join(errors)}\nQuestion: {self.question_text}\nOptions: {self.options}")


# ==============================================================================
# UTILITY FUNCTIONS
# ==============================================================================

def find_database() -> str:
    """Find the database file"""
    for path in DATABASE_PATHS:
        if os.path.exists(path):
            return path
    raise FileNotFoundError(f"Database not found. Checked: {DATABASE_PATHS}")


def ensure_unique_options(correct: str, distractors: List[str], count: int = 4) -> List[str]:
    """
    CRITICAL FUNCTION: Guarantee exactly `count` unique options including correct answer.
    
    This is the key fix for the duplicate options bug.
    """
    # Start with correct answer
    options = [str(correct)]
    
    # Add distractors, skipping duplicates
    for d in distractors:
        d_str = str(d)
        if d_str not in options:
            options.append(d_str)
        if len(options) >= count:
            break
    
    # If still need more, generate random ones
    attempts = 0
    while len(options) < count and attempts < 100:
        attempts += 1
        
        # Generate based on correct answer type
        if '/' in str(correct):
            # Fraction - generate random fraction
            n = random.randint(1, 9)
            d = random.randint(2, 10)
            new_opt = f"{n}/{d}"
        elif '%' in str(correct):
            # Percentage
            new_opt = f"{random.randint(5, 95)}%"
        elif '.' in str(correct):
            # Decimal
            new_opt = f"{random.uniform(0.1, 0.9):.2f}"
        else:
            # Integer or text - try nearby integers
            try:
                base = int(str(correct).split()[0])
                offset = random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
                new_opt = str(max(1, base + offset))
            except:
                new_opt = str(random.randint(1, 20))
        
        if new_opt not in options:
            options.append(new_opt)
    
    if len(options) < count:
        raise ValueError(f"Could not generate {count} unique options for correct={correct}")
    
    return options[:count]


def shuffle_with_correct_index(options: List[str], correct_value: str) -> Tuple[List[str], int]:
    """Shuffle options and return new correct index"""
    shuffled = options.copy()
    random.shuffle(shuffled)
    correct_index = shuffled.index(correct_value)
    return shuffled, correct_index


def gcd(a: int, b: int) -> int:
    """Greatest common divisor"""
    while b:
        a, b = b, a % b
    return a


def simplify_fraction(num: int, denom: int) -> Tuple[int, int]:
    """Reduce fraction to lowest terms"""
    g = gcd(num, denom)
    return num // g, denom // g


# ==============================================================================
# SVG GENERATORS
# ==============================================================================

def svg_pie_chart(numerator: int, denominator: int, size: int = 160) -> str:
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


def svg_fraction_bar(numerator: int, denominator: int, width: int = 200, height: int = 40) -> str:
    """Generate a fraction bar SVG"""
    segment_width = (width - 10) / denominator
    
    segments = []
    for i in range(denominator):
        color = '#4CAF50' if i < numerator else '#E8F5E9'
        x = 5 + i * segment_width
        segments.append(f'<rect x="{x:.1f}" y="5" width="{segment_width:.1f}" height="{height-10}" fill="{color}" stroke="#333" stroke-width="1"/>')
    
    return f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">{''.join(segments)}</svg>'''


# ==============================================================================
# FRACTIONS QUESTION GENERATORS
# ==============================================================================

class FractionsGenerator:
    """
    Generates fractions questions with proper skill progression.
    
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
    """
    
    TOPIC = 'fractions'
    
    @staticmethod
    def generate_distractors_fraction(correct_num: int, correct_denom: int) -> List[str]:
        """Generate plausible wrong fraction answers"""
        correct = f"{correct_num}/{correct_denom}"
        distractors = set()
        
        # Inverted
        if correct_num != correct_denom:
            distractors.add(f"{correct_denom}/{correct_num}")
        
        # Off by one numerator
        if correct_num > 1:
            distractors.add(f"{correct_num - 1}/{correct_denom}")
        if correct_num < correct_denom - 1:
            distractors.add(f"{correct_num + 1}/{correct_denom}")
        
        # Off by one denominator
        if correct_denom > 2:
            distractors.add(f"{correct_num}/{correct_denom - 1}")
        distractors.add(f"{correct_num}/{correct_denom + 1}")
        
        # Complement
        if correct_denom - correct_num != correct_num:
            distractors.add(f"{correct_denom - correct_num}/{correct_denom}")
        
        # Unsimplified
        distractors.add(f"{correct_num * 2}/{correct_denom * 2}")
        
        # Random valid fractions
        for _ in range(5):
            n = random.randint(1, 9)
            d = random.randint(2, 10)
            if f"{n}/{d}" != correct:
                distractors.add(f"{n}/{d}")
        
        distractors.discard(correct)
        return list(distractors)
    
    @classmethod
    def level_1(cls) -> List[Question]:
        """Level 1: HALVES ONLY - The simplest fraction"""
        questions = []
        
        # Visual: Pie charts showing 1/2
        for i in range(10):
            svg = svg_pie_chart(1, 2)
            correct = "1/2"
            distractors = ["1/4", "1/3", "2/2", "2/4", "1/1"]
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=1, band='beginner',
                question_text=f"What fraction of the circle is green? [L1-P{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='visual', svg=svg
            ))
        
        # Visual: Fraction bars showing 1/2
        for i in range(8):
            svg = svg_fraction_bar(1, 2)
            correct = "1/2"
            distractors = ["1/4", "2/4", "1/3", "2/2"]
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=1, band='beginner',
                question_text=f"What fraction of the bar is green? [L1-B{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='visual', svg=svg
            ))
        
        # Word problems
        items = ['pizza', 'cake', 'apple', 'sandwich', 'cookie', 'orange', 'pie', 'chocolate bar']
        names = ['Seán', 'Aoife', 'Ciarán', 'Niamh', 'Oisín', 'Siobhán', 'Fionn', 'Caoimhe']
        
        for i, (item, name) in enumerate(zip(items, names)):
            correct = "1/2"
            distractors = ["1/4", "2/2", "1/3", "2/4"]
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=1, band='beginner',
                question_text=f"{name} cuts a {item} into 2 equal pieces. What fraction is each piece? [L1-W{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='word_problem'
            ))
        
        return questions
    
    @classmethod
    def level_2(cls) -> List[Question]:
        """Level 2: QUARTERS AND THIRDS"""
        questions = []
        
        # Quarters - all variations
        for num in [1, 2, 3]:
            svg = svg_pie_chart(num, 4)
            correct = f"{num}/4"
            distractors = cls.generate_distractors_fraction(num, 4)
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=2, band='beginner',
                question_text=f"The circle is divided into quarters. What fraction is green? [L2-Q{num}]",
                options=options, correct_index=correct_idx,
                question_type='visual', svg=svg
            ))
            
            # Bar version
            svg_bar = svg_fraction_bar(num, 4)
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=2, band='beginner',
                question_text=f"The bar shows quarters. What fraction is green? [L2-QB{num}]",
                options=options, correct_index=correct_idx,
                question_type='visual', svg=svg_bar
            ))
        
        # Thirds - all variations
        for num in [1, 2]:
            svg = svg_pie_chart(num, 3)
            correct = f"{num}/3"
            distractors = cls.generate_distractors_fraction(num, 3)
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=2, band='beginner',
                question_text=f"The circle is divided into thirds. What fraction is green? [L2-T{num}]",
                options=options, correct_index=correct_idx,
                question_type='visual', svg=svg
            ))
            
            # Bar version
            svg_bar = svg_fraction_bar(num, 3)
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=2, band='beginner',
                question_text=f"The bar shows thirds. What fraction is green? [L2-TB{num}]",
                options=options, correct_index=correct_idx,
                question_type='visual', svg=svg_bar
            ))
        
        # Word problems
        word_problems = [
            ("A pizza is cut into 4 equal slices. Seán eats 1 slice.", 1, 4),
            ("A cake is divided into 4 pieces. Aoife takes 2 pieces.", 2, 4),
            ("A chocolate bar has 4 sections. Ciarán eats 3 sections.", 3, 4),
            ("An orange is split into 3 equal parts. Niamh eats 1 part.", 1, 3),
            ("A pie is cut into 3 slices. Oisín eats 2 slices.", 2, 3),
        ]
        
        for i, (text, num, denom) in enumerate(word_problems):
            correct = f"{num}/{denom}"
            distractors = cls.generate_distractors_fraction(num, denom)
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=2, band='beginner',
                question_text=f"{text} What fraction was eaten? [L2-W{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='word_problem'
            ))
        
        return questions
    
    @classmethod
    def level_3(cls) -> List[Question]:
        """Level 3: ANY FRACTION (fifths, sixths, eighths, tenths)"""
        questions = []
        
        # Generate for each denominator
        denominators = [
            (5, "fifths"), (6, "sixths"), (8, "eighths"), (10, "tenths")
        ]
        
        for denom, name in denominators:
            for num in range(1, min(denom, 5)):  # 1 to 4 for each
                svg = svg_pie_chart(num, denom)
                correct = f"{num}/{denom}"
                distractors = cls.generate_distractors_fraction(num, denom)
                options = ensure_unique_options(correct, distractors)
                options, correct_idx = shuffle_with_correct_index(options, correct)
                
                questions.append(Question(
                    level=3, band='beginner',
                    question_text=f"This circle shows {name}. What fraction is green? [L3-{name[0].upper()}{num}]",
                    options=options, correct_index=correct_idx,
                    question_type='visual', svg=svg
                ))
        
        # Fraction bar versions
        for denom, name in denominators:
            num = random.randint(1, denom - 1)
            svg = svg_fraction_bar(num, denom)
            correct = f"{num}/{denom}"
            distractors = cls.generate_distractors_fraction(num, denom)
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=3, band='beginner',
                question_text=f"What fraction of the bar is green? [L3-Bar{denom}]",
                options=options, correct_index=correct_idx,
                question_type='visual', svg=svg
            ))
        
        return questions
    
    @classmethod
    def level_4(cls) -> List[Question]:
        """Level 4: SIMPLIFY FRACTIONS - New skill!"""
        questions = []
        
        # All unique simplification problems
        simplify_cases = [
            (2, 4, 1, 2), (3, 6, 1, 2), (4, 8, 1, 2), (5, 10, 1, 2),
            (2, 6, 1, 3), (3, 9, 1, 3), (4, 12, 1, 3),
            (2, 8, 1, 4), (3, 12, 1, 4),
            (4, 6, 2, 3), (6, 9, 2, 3), (8, 12, 2, 3),
            (6, 8, 3, 4), (9, 12, 3, 4),
            (4, 10, 2, 5), (6, 10, 3, 5),
            (6, 12, 1, 2), (8, 12, 2, 3), (10, 12, 5, 6),
        ]
        
        for i, (n, d, sn, sd) in enumerate(simplify_cases):
            correct = f"{sn}/{sd}"
            # Specific distractors for simplification
            distractors = [
                f"{n}/{d}",      # Unsimplified (common mistake)
                f"{sn}/{d}",    # Only simplified numerator
                f"{n}/{sd}",    # Only simplified denominator
                f"{sd}/{sn}" if sn != sd else f"{sn+1}/{sd}",  # Inverted
            ]
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=4, band='intermediate',
                question_text=f"Simplify {n}/{d} to its lowest terms [L4-S{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='calculation'
            ))
        
        return questions
    
    @classmethod
    def level_5(cls) -> List[Question]:
        """Level 5: EQUIVALENT FRACTIONS"""
        questions = []
        
        # Find equivalent fractions
        equiv_cases = [
            (1, 2, 2, 4), (1, 2, 3, 6), (1, 2, 4, 8), (1, 2, 5, 10),
            (1, 3, 2, 6), (1, 3, 3, 9), (2, 3, 4, 6), (2, 3, 6, 9),
            (1, 4, 2, 8), (1, 4, 3, 12), (3, 4, 6, 8), (3, 4, 9, 12),
            (1, 5, 2, 10), (2, 5, 4, 10), (3, 5, 6, 10),
        ]
        
        for i, (n1, d1, n2, d2) in enumerate(equiv_cases):
            correct = f"{n2}/{d2}"
            distractors = [
                f"{n2}/{d1}",       # Only multiplied numerator
                f"{n1}/{d2}",       # Only multiplied denominator
                f"{n1+1}/{d1+1}",   # Added instead of multiplied
                f"{n2+1}/{d2}",     # Close but wrong
            ]
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=5, band='intermediate',
                question_text=f"Which fraction is equivalent to {n1}/{d1}? [L5-E{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='calculation'
            ))
        
        # Missing number problems
        missing_cases = [
            ("?/4 = 1/2", "2", ["1", "3", "4"]),
            ("?/6 = 1/3", "2", ["1", "3", "6"]),
            ("?/8 = 1/2", "4", ["2", "3", "8"]),
            ("?/6 = 1/2", "3", ["2", "4", "6"]),
            ("?/10 = 1/2", "5", ["2", "4", "10"]),
            ("?/9 = 1/3", "3", ["1", "6", "9"]),
            ("?/12 = 1/4", "3", ["2", "4", "12"]),
            ("?/8 = 3/4", "6", ["3", "4", "8"]),
        ]
        
        for i, (equation, correct, wrongs) in enumerate(missing_cases):
            options = ensure_unique_options(correct, wrongs)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=5, band='intermediate',
                question_text=f"Find the missing number: {equation} [L5-M{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='calculation'
            ))
        
        return questions
    
    @classmethod
    def level_6(cls) -> List[Question]:
        """Level 6: ADD/SUBTRACT - SAME DENOMINATOR"""
        questions = []
        
        # Addition
        add_cases = [
            (1, 4, 2, 4, "3/4"), (1, 4, 1, 4, "2/4"), (2, 5, 2, 5, "4/5"),
            (1, 6, 2, 6, "3/6"), (2, 6, 3, 6, "5/6"), (1, 8, 3, 8, "4/8"),
            (3, 8, 2, 8, "5/8"), (2, 10, 3, 10, "5/10"), (4, 10, 3, 10, "7/10"),
        ]
        
        for i, (n1, d, n2, _, correct) in enumerate(add_cases):
            distractors = [
                f"{n1+n2}/{d*2}",  # Added denominators too
                f"{n1}/{d}",       # Forgot second fraction
                f"{n1*n2}/{d}",    # Multiplied instead
            ]
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=6, band='intermediate',
                question_text=f"Calculate: {n1}/{d} + {n2}/{d} [L6-A{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='calculation'
            ))
        
        # Subtraction
        sub_cases = [
            (3, 4, 1, 4, "2/4"), (3, 4, 2, 4, "1/4"),
            (4, 5, 2, 5, "2/5"), (5, 6, 2, 6, "3/6"),
            (7, 8, 3, 8, "4/8"), (5, 8, 2, 8, "3/8"),
            (9, 10, 4, 10, "5/10"), (7, 10, 3, 10, "4/10"),
        ]
        
        for i, (n1, d, n2, _, correct) in enumerate(sub_cases):
            distractors = [
                f"{n1}/{d}",       # Forgot to subtract
                f"{n2}/{d}",       # Gave subtrahend
                f"{n1-n2}/{d*2}",  # Wrong denominator
            ]
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=6, band='intermediate',
                question_text=f"Calculate: {n1}/{d} − {n2}/{d} [L6-S{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='calculation'
            ))
        
        return questions
    
    @classmethod
    def level_7(cls) -> List[Question]:
        """Level 7: ADD/SUBTRACT - DIFFERENT DENOMINATORS"""
        questions = []
        
        # These require finding LCD
        add_cases = [
            (1, 2, 1, 4, "3/4"),
            (1, 2, 1, 6, "4/6"),
            (1, 3, 1, 6, "3/6"),
            (2, 3, 1, 6, "5/6"),
            (1, 2, 1, 3, "5/6"),
            (1, 4, 1, 8, "3/8"),
            (3, 4, 1, 8, "7/8"),
            (1, 3, 1, 4, "7/12"),
            (1, 2, 1, 5, "7/10"),
            (2, 5, 1, 10, "5/10"),
        ]
        
        for i, (n1, d1, n2, d2, correct) in enumerate(add_cases):
            distractors = [
                f"{n1+n2}/{d1+d2}",  # Added both
                f"{n1+n2}/{d2}",     # Wrong denominator
                f"{n1}/{d1}",        # First fraction only
            ]
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=7, band='advanced',
                question_text=f"Calculate: {n1}/{d1} + {n2}/{d2} [L7-A{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='calculation'
            ))
        
        # Subtraction with different denominators
        sub_cases = [
            (1, 2, 1, 4, "1/4"),
            (3, 4, 1, 2, "1/4"),
            (2, 3, 1, 6, "3/6"),
            (5, 6, 1, 3, "3/6"),
            (3, 4, 1, 8, "5/8"),
            (7, 8, 1, 4, "5/8"),
        ]
        
        for i, (n1, d1, n2, d2, correct) in enumerate(sub_cases):
            distractors = [
                f"{n1-n2}/{d1}",     # Wrong method
                f"{n1-n2}/{d2}",     # Wrong method
                f"{n1}/{d1}",        # Didn't subtract
            ]
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=7, band='advanced',
                question_text=f"Calculate: {n1}/{d1} − {n2}/{d2} [L7-S{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='calculation'
            ))
        
        return questions
    
    @classmethod
    def level_8(cls) -> List[Question]:
        """Level 8: MULTIPLY FRACTIONS"""
        questions = []
        
        mult_cases = [
            (1, 2, 1, 2, "1/4"), (1, 2, 1, 3, "1/6"), (1, 2, 1, 4, "1/8"),
            (1, 2, 2, 3, "2/6"), (1, 2, 3, 4, "3/8"),
            (1, 3, 1, 3, "1/9"), (1, 3, 2, 3, "2/9"),
            (2, 3, 1, 2, "2/6"), (2, 3, 3, 4, "6/12"),
            (1, 4, 1, 2, "1/8"), (3, 4, 1, 2, "3/8"),
            (3, 4, 2, 3, "6/12"),
        ]
        
        for i, (n1, d1, n2, d2, correct) in enumerate(mult_cases):
            distractors = [
                f"{n1+n2}/{d1+d2}",  # Added instead
                f"{n1*n2}/{d1}",     # Wrong denominator
                f"{n1}/{d1*d2}",     # Wrong numerator
            ]
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=8, band='advanced',
                question_text=f"Calculate: {n1}/{d1} × {n2}/{d2} [L8-M{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='calculation'
            ))
        
        # Fraction × whole number
        whole_cases = [
            (1, 2, 3, "3/2"), (1, 2, 4, "4/2"), (1, 3, 2, "2/3"),
            (2, 3, 3, "6/3"), (1, 4, 2, "2/4"), (3, 4, 2, "6/4"),
            (1, 5, 3, "3/5"), (2, 5, 4, "8/5"),
        ]
        
        for i, (n, d, w, correct) in enumerate(whole_cases):
            distractors = [
                f"{n+w}/{d}",     # Added instead
                f"{n*w}/{d*w}",   # Multiplied denominator too
                f"{n}/{d}",       # Unchanged
            ]
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=8, band='advanced',
                question_text=f"Calculate: {n}/{d} × {w} [L8-W{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='calculation'
            ))
        
        return questions
    
    @classmethod
    def level_9(cls) -> List[Question]:
        """Level 9: DIVIDE FRACTIONS (flip and multiply)"""
        questions = []
        
        div_cases = [
            (1, 2, 1, 4, "2"),
            (1, 2, 1, 2, "1"),
            (3, 4, 1, 2, "3/2"),
            (2, 3, 1, 3, "2"),
            (1, 4, 1, 2, "1/2"),
            (3, 4, 1, 4, "3"),
            (1, 3, 1, 6, "2"),
            (2, 5, 1, 5, "2"),
            (1, 2, 1, 3, "3/2"),
            (2, 3, 1, 2, "4/3"),
            (5, 6, 1, 2, "5/3"),
        ]
        
        for i, (n1, d1, n2, d2, correct) in enumerate(div_cases):
            distractors = [
                f"{n1*n2}/{d1*d2}",  # Multiplied instead of dividing
                "1/8",               # Common wrong answer
                f"{n1}/{d1}",        # First fraction unchanged
            ]
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=9, band='advanced',
                question_text=f"Calculate: {n1}/{d1} ÷ {n2}/{d2} [L9-D{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='calculation'
            ))
        
        # Divide by whole number
        whole_div = [
            (1, 2, 2, "1/4"), (1, 2, 3, "1/6"),
            (2, 3, 2, "2/6"), (3, 4, 3, "3/12"),
            (1, 3, 2, "1/6"), (4, 5, 2, "4/10"),
        ]
        
        for i, (n, d, w, correct) in enumerate(whole_div):
            distractors = [
                f"{n*w}/{d}",       # Multiplied instead
                f"{n}/{d}",         # Unchanged
                f"{n}/{d*w*2}",     # Way off
            ]
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=9, band='advanced',
                question_text=f"Calculate: {n}/{d} ÷ {w} [L9-W{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='calculation'
            ))
        
        return questions
    
    @classmethod
    def level_10(cls) -> List[Question]:
        """Level 10: MULTI-STEP PROBLEMS (Mastery)"""
        questions = []
        
        # Order of operations
        order_cases = [
            ("(1/4 + 1/4) × 2", "1", ["1/2", "1/4", "2/4"]),
            ("(1/2 + 1/4) × 2", "3/2", ["3/4", "1", "5/4"]),
            ("(3/4 − 1/4) × 2", "1", ["1/2", "3/4", "2"]),
            ("(1/3 + 1/3) × 3", "2", ["1", "2/3", "3"]),
            ("1/2 × 2/3 + 1/6", "1/2", ["1/3", "2/3", "5/6"]),
            ("2 × 1/4 + 1/2", "1", ["3/4", "1/2", "5/4"]),
            ("1 − 1/4 − 1/4", "1/2", ["1/4", "3/4", "0"]),
            ("3/4 − 1/2 × 1/2", "1/2", ["1/4", "3/4", "1"]),
        ]
        
        for i, (expr, correct, wrongs) in enumerate(order_cases):
            options = ensure_unique_options(correct, wrongs)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=10, band='mastery',
                question_text=f"Calculate: {expr} [L10-O{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='calculation'
            ))
        
        # Reverse problems
        reverse_cases = [
            ("1/2 of a number is 6. What is the number?", "12", ["6", "3", "8"]),
            ("1/3 of a number is 5. What is the number?", "15", ["5", "8", "10"]),
            ("1/4 of a number is 3. What is the number?", "12", ["3", "6", "9"]),
            ("2/3 of a number is 8. What is the number?", "12", ["8", "10", "16"]),
            ("3/4 of a number is 9. What is the number?", "12", ["9", "6", "15"]),
        ]
        
        for i, (text, correct, wrongs) in enumerate(reverse_cases):
            options = ensure_unique_options(correct, wrongs)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=10, band='mastery',
                question_text=f"{text} [L10-R{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='calculation'
            ))
        
        return questions
    
    @classmethod
    def level_11(cls) -> List[Question]:
        """Level 11: APPLICATION (Real-world problems)"""
        questions = []
        
        problems = [
            ("A recipe for 4 people uses 3/4 cup flour. How much for 2 people?", "3/8 cup", ["3/4 cup", "1/2 cup", "6/8 cup"]),
            ("Aoife has €60. She spends 1/3 on books. How much is left?", "€40", ["€20", "€30", "€45"]),
            ("Seán studies for 90 minutes. He spends 2/3 on maths. How many minutes?", "60 minutes", ["30 minutes", "45 minutes", "80 minutes"]),
            ("A pizza is cut into 8 slices. Ciarán eats 3/8 and Niamh eats 2/8. What fraction is left?", "3/8", ["5/8", "1/8", "6/8"]),
            ("A tank is 1/4 full. You add enough to make it 3/4 full. What fraction did you add?", "1/2", ["1/4", "3/4", "2/4"]),
            ("Oisín reads 2/5 of a book on Monday and 1/5 on Tuesday. What fraction is left?", "2/5", ["3/5", "1/5", "4/5"]),
            ("A class has 30 students. 2/3 are girls. How many boys?", "10", ["20", "15", "12"]),
            ("Siobhán cycles 3/4 km to school. If she's cycled 1/2 km, how much is left?", "1/4 km", ["1/2 km", "3/4 km", "2/4 km"]),
        ]
        
        for i, (text, correct, wrongs) in enumerate(problems):
            options = ensure_unique_options(correct, wrongs)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=11, band='application',
                question_text=f"{text} [L11-{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='word_problem'
            ))
        
        return questions
    
    @classmethod
    def level_12(cls) -> List[Question]:
        """Level 12: LINKED (Cross-topic connections)"""
        questions = []
        
        # Fractions to percentages
        frac_to_pct = [
            ("1/4", "25%"), ("1/2", "50%"), ("3/4", "75%"),
            ("1/5", "20%"), ("2/5", "40%"), ("3/5", "60%"),
            ("1/10", "10%"), ("3/10", "30%"), ("4/5", "80%"),
        ]
        
        for i, (frac, correct) in enumerate(frac_to_pct):
            distractors = ["10%", "15%", "45%", "35%", "55%"]
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=12, band='linked',
                question_text=f"Convert {frac} to a percentage [L12-P{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='calculation',
                linked_topics='percentages'
            ))
        
        # Fractions to decimals
        frac_to_dec = [
            ("1/2", "0.5"), ("1/4", "0.25"), ("3/4", "0.75"),
            ("1/5", "0.2"), ("2/5", "0.4"), ("1/10", "0.1"),
        ]
        
        for i, (frac, correct) in enumerate(frac_to_dec):
            distractors = ["0.14", "0.33", "0.6", "0.15", "0.45"]
            options = ensure_unique_options(correct, distractors)
            options, correct_idx = shuffle_with_correct_index(options, correct)
            
            questions.append(Question(
                level=12, band='linked',
                question_text=f"Convert {frac} to a decimal [L12-D{i+1}]",
                options=options, correct_index=correct_idx,
                question_type='calculation',
                linked_topics='decimals'
            ))
        
        return questions
    
    @classmethod
    def generate_all(cls) -> List[Question]:
        """Generate all questions for all levels"""
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
    """Ensure database supports levels 1-12"""
    cursor = conn.cursor()
    
    # Check if table exists
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
        print("✅ Table created with levels 1-12 support")
        return
    
    # Try inserting level 11 to test constraint
    try:
        cursor.execute("""
            INSERT INTO questions_adaptive 
            (topic, difficulty_level, difficulty_band, question_text,
             option_a, option_b, option_c, option_d, correct_answer,
             explanation, is_active, question_type)
            VALUES ('_schema_test_', 11, 'application', 'test', 'a', 'b', 'c', 'd', 0, '', 1, 'test')
        """)
        cursor.execute("DELETE FROM questions_adaptive WHERE topic = '_schema_test_'")
        conn.commit()
        print("✅ Database schema OK (supports levels 1-12)")
        return
    except sqlite3.IntegrityError:
        print("⚠️  Updating database schema for levels 1-12...")
        conn.rollback()
    
    # Rebuild table with new constraint
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
    
    # Copy existing data (for levels 1-10)
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
    print("✅ Database schema updated")


def insert_questions(conn: sqlite3.Connection, questions: List[Question], topic: str):
    """Insert questions into database with full validation"""
    cursor = conn.cursor()
    inserted = 0
    duplicates = 0
    errors = 0
    
    for q in questions:
        try:
            cursor.execute("""
                INSERT INTO questions_adaptive 
                (topic, difficulty_level, difficulty_band, question_text,
                 option_a, option_b, option_c, option_d, correct_answer,
                 explanation, is_active, question_type, image_svg, linked_topics, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?, ?, ?, ?)
            """, (
                topic,
                q.level,
                q.band,
                q.question_text,
                q.options[0],
                q.options[1],
                q.options[2],
                q.options[3],
                q.correct_index,
                q.explanation,
                q.question_type,
                q.svg,
                q.linked_topics,
                datetime.now().isoformat()
            ))
            inserted += 1
        except sqlite3.IntegrityError:
            duplicates += 1
        except Exception as e:
            errors += 1
            print(f"  ❌ Error inserting: {e}")
    
    conn.commit()
    return inserted, duplicates, errors


def clear_topic(conn: sqlite3.Connection, topic: str) -> int:
    """Clear all questions for a topic"""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = ?", (topic,))
    deleted = cursor.rowcount
    conn.commit()
    return deleted


def get_stats(conn: sqlite3.Connection, topic: str) -> Dict:
    """Get question statistics for a topic"""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT difficulty_level, COUNT(*) 
        FROM questions_adaptive 
        WHERE topic = ? AND is_active = 1
        GROUP BY difficulty_level
        ORDER BY difficulty_level
    """, (topic,))
    
    return {row[0]: row[1] for row in cursor.fetchall()}


# ==============================================================================
# MAIN
# ==============================================================================

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate adaptive quiz questions')
    parser.add_argument('--topic', default='fractions', help='Topic to generate')
    parser.add_argument('--clear', action='store_true', help='Clear existing questions first')
    parser.add_argument('--test', action='store_true', help='Test mode - validate but don\'t insert')
    args = parser.parse_args()
    
    print("=" * 70)
    print("ADAPTIVE QUIZ QUESTION GENERATOR - PRODUCTION VERSION")
    print("=" * 70)
    
    # Find database
    try:
        db_path = find_database()
        print(f"✅ Database: {db_path}")
    except FileNotFoundError as e:
        print(f"❌ {e}")
        sys.exit(1)
    
    conn = sqlite3.connect(db_path)
    
    # Fix schema if needed
    fix_database_schema(conn)
    
    # Generate questions
    print(f"\n📝 Generating {args.topic} questions...")
    
    if args.topic == 'fractions':
        questions = FractionsGenerator.generate_all()
    else:
        print(f"❌ Unknown topic: {args.topic}")
        sys.exit(1)
    
    print(f"   Generated {len(questions)} questions")
    
    # Validate all questions
    print("\n🔍 Validating questions...")
    valid = 0
    invalid = 0
    for q in questions:
        try:
            q.validate()
            valid += 1
        except ValueError as e:
            invalid += 1
            print(f"   ❌ {e}")
    
    print(f"   ✅ {valid} valid, ❌ {invalid} invalid")
    
    if invalid > 0:
        print("\n⚠️  Fix invalid questions before inserting!")
        sys.exit(1)
    
    if args.test:
        print("\n🧪 TEST MODE - No changes made to database")
        conn.close()
        return
    
    # Clear existing if requested
    if args.clear:
        deleted = clear_topic(conn, args.topic)
        print(f"\n🗑️  Cleared {deleted} existing {args.topic} questions")
    
    # Insert questions
    print(f"\n💾 Inserting questions...")
    inserted, duplicates, errors = insert_questions(conn, questions, args.topic)
    print(f"   ✅ Inserted: {inserted}")
    print(f"   ⏭️  Duplicates skipped: {duplicates}")
    if errors > 0:
        print(f"   ❌ Errors: {errors}")
    
    # Show final stats
    print("\n📊 Final question counts:")
    stats = get_stats(conn, args.topic)
    total = 0
    for level in range(1, 13):
        count = stats.get(level, 0)
        total += count
        band = LEVEL_BANDS.get(level, 'unknown')
        print(f"   Level {level:2d} ({band:12s}): {count:3d} questions")
    print(f"   {'─' * 35}")
    print(f"   TOTAL: {total} questions")
    
    conn.close()
    
    print("\n" + "=" * 70)
    print("✅ DONE! Reload web app to see changes.")
    print("=" * 70)


if __name__ == '__main__':
    main()
