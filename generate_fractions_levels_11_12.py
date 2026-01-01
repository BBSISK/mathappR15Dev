#!/usr/bin/env python3
"""
Example: Level 11-12 Question Generators for Fractions
======================================================

This shows the pattern for creating Application (L11) and Linked Topics (L12) questions.

Level 11 - Application:
  - Real-life word problems
  - Irish context (€, local references)
  - Multi-step problem solving
  - 50% visual target

Level 12 - Linked Topics:
  - Cross-topic integration
  - Requires Level 8+ in linked topics
  - stored with linked_topics field
  - 50% visual target
"""

import random
from datetime import datetime
import sqlite3
import math
import os

# Check multiple possible database locations
POSSIBLE_PATHS = [
    'mathapp.db',
    'instance/mathquiz.db',
    'mathquiz.db',
]

DB_PATH = None

def find_db():
    """Find the database file"""
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
# SVG GENERATORS FOR WORD PROBLEMS
# ============================================================

def generate_recipe_svg(original, people_original, people_new):
    """Generate a recipe card visual"""
    return f'''<svg viewBox="0 0 280 180" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="260" height="160" rx="10" fill="#FFF8E7" stroke="#D4A574" stroke-width="2"/>
        <text x="140" y="35" text-anchor="middle" font-size="16" font-weight="bold" fill="#8B4513">🍳 Recipe Card</text>
        <line x1="30" y1="45" x2="250" y2="45" stroke="#D4A574" stroke-width="1"/>
        <text x="30" y="70" font-size="13" fill="#5D4037">Original recipe: {people_original} people</text>
        <text x="30" y="95" font-size="13" fill="#5D4037">Flour needed: {original} cups</text>
        <line x1="30" y1="110" x2="250" y2="110" stroke="#D4A574" stroke-dasharray="5,5"/>
        <text x="30" y="135" font-size="14" font-weight="bold" fill="#2E7D32">Cooking for: {people_new} people</text>
        <text x="30" y="158" font-size="13" fill="#5D4037">How much flour?</text>
    </svg>'''


def generate_shopping_svg(original_price, discount_pct):
    """Generate a shop price tag visual"""
    sale_price = original_price * (1 - discount_pct/100)
    return f'''<svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg">
        <rect x="10" y="10" width="180" height="140" rx="8" fill="#FFEBEE" stroke="#E53935" stroke-width="2"/>
        <polygon points="180,10 200,30 180,30" fill="#E53935"/>
        <circle cx="185" cy="20" r="6" fill="white"/>
        <text x="100" y="45" text-anchor="middle" font-size="14" fill="#B71C1C">🏷️ SALE!</text>
        <text x="100" y="75" text-anchor="middle" font-size="12" fill="#666">Was: €{original_price:.2f}</text>
        <line x1="60" y1="72" x2="140" y2="72" stroke="#E53935" stroke-width="2"/>
        <text x="100" y="105" text-anchor="middle" font-size="20" font-weight="bold" fill="#2E7D32">{discount_pct}% OFF</text>
        <text x="100" y="135" text-anchor="middle" font-size="11" fill="#666">What's the sale price?</text>
    </svg>'''


def generate_fraction_to_percent_svg(numerator, denominator):
    """Generate visual showing fraction to percentage conversion"""
    percentage = (numerator / denominator) * 100
    angle = percentage * 3.6
    large_arc = 1 if percentage > 50 else 0
    
    rad = math.radians(angle - 90)
    x = 80 + 50 * math.cos(rad)
    y = 80 + 50 * math.sin(rad)
    
    return f'''<svg viewBox="0 0 280 160" xmlns="http://www.w3.org/2000/svg">
        <!-- Fraction side -->
        <rect x="10" y="20" width="100" height="120" rx="8" fill="#E3F2FD" stroke="#1976D2" stroke-width="2"/>
        <text x="60" y="55" text-anchor="middle" font-size="28" font-weight="bold" fill="#1565C0">{numerator}</text>
        <line x1="30" y1="70" x2="90" y2="70" stroke="#1565C0" stroke-width="3"/>
        <text x="60" y="105" text-anchor="middle" font-size="28" font-weight="bold" fill="#1565C0">{denominator}</text>
        
        <!-- Arrow -->
        <text x="140" y="85" text-anchor="middle" font-size="24" fill="#666">→</text>
        
        <!-- Percentage pie chart -->
        <circle cx="210" cy="80" r="50" fill="#E8F5E9" stroke="#4CAF50" stroke-width="2"/>
        <path d="M210,80 L210,30 A50,50 0 {large_arc},1 {x:.1f},{y:.1f} Z" fill="#4CAF50"/>
        <text x="210" y="150" text-anchor="middle" font-size="14" fill="#2E7D32">= ?%</text>
    </svg>'''


def generate_probability_fraction_svg(favorable, total):
    """Generate visual showing probability as fraction"""
    return f'''<svg viewBox="0 0 280 140" xmlns="http://www.w3.org/2000/svg">
        <!-- Bag of marbles -->
        <ellipse cx="70" cy="100" rx="50" ry="20" fill="#8D6E63"/>
        <path d="M20,100 Q20,40 70,40 Q120,40 120,100" fill="#A1887F" stroke="#6D4C41" stroke-width="2"/>
        <circle cx="45" cy="70" r="10" fill="#F44336"/>
        <circle cx="70" cy="75" r="10" fill="#2196F3"/>
        <circle cx="95" cy="70" r="10" fill="#F44336"/>
        <circle cx="55" cy="55" r="10" fill="#2196F3"/>
        <circle cx="85" cy="55" r="10" fill="#2196F3"/>
        
        <!-- Text -->
        <text x="70" y="130" text-anchor="middle" font-size="11" fill="#5D4037">{favorable} red, {total-favorable} blue</text>
        
        <!-- Arrow and question -->
        <text x="150" y="75" font-size="20" fill="#666">→</text>
        
        <!-- Fraction box -->
        <rect x="180" y="30" width="90" height="80" rx="8" fill="#FFF3E0" stroke="#FF9800" stroke-width="2"/>
        <text x="225" y="60" text-anchor="middle" font-size="14" fill="#E65100">P(red) = ?</text>
        <text x="225" y="95" text-anchor="middle" font-size="12" fill="#666">as a fraction</text>
    </svg>'''


# ============================================================
# LEVEL 11: APPLICATION QUESTIONS (Real-Life Word Problems)
# ============================================================

def generate_level_11_fractions():
    """
    Level 11: Application - Real-life fraction word problems
    Multi-step, requires identifying which operation to use
    """
    questions = []
    
    # Type 1: Recipe scaling
    for _ in range(15):
        # Original recipe
        num = random.choice([1, 2, 3])
        denom = random.choice([2, 3, 4])
        original_people = random.choice([4, 6])
        new_people = random.choice([2, 3, 8, 9, 12])
        
        # Calculate answer
        scale_factor = new_people / original_people
        result_num = num * new_people
        result_denom = denom * original_people
        
        # Simplify
        from math import gcd
        g = gcd(result_num, result_denom)
        result_num //= g
        result_denom //= g
        
        if result_denom == 1:
            correct = str(result_num)
        else:
            correct = f"{result_num}/{result_denom}"
        
        # Generate distractors
        distractors = [
            f"{num}/{denom}",  # Original amount (didn't scale)
            f"{num * new_people}/{denom}",  # Only multiplied numerator
            f"{num}/{denom * original_people}",  # Wrong operation
        ]
        
        options = [correct] + [d for d in distractors if d != correct][:3]
        while len(options) < 4:
            fake_num = random.randint(1, 10)
            fake_denom = random.randint(2, 8)
            fake = f"{fake_num}/{fake_denom}"
            if fake not in options:
                options.append(fake)
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        svg = generate_recipe_svg(f"{num}/{denom}", original_people, new_people)
        
        questions.append({
            'question': f"A recipe for {original_people} people needs {num}/{denom} cups of flour. Áine is cooking for {new_people} people. How much flour does she need?",
            'options': options,
            'correct': correct_idx,
            'level': 11,
            'band': 'application',
            'type': 'visual',
            'svg': svg,
            'linked_topics': None
        })
    
    # Type 2: Time/Distance problems
    for _ in range(10):
        hours_num = random.choice([1, 2, 3])
        hours_denom = random.choice([2, 3, 4])
        distance = random.randint(5, 20)
        
        # Calculate speed = distance / time
        speed_num = distance * hours_denom
        speed_denom = hours_num
        
        from math import gcd
        g = gcd(speed_num, speed_denom)
        speed_num //= g
        speed_denom //= g
        
        if speed_denom == 1:
            correct = f"{speed_num} km/h"
        else:
            correct = f"{speed_num}/{speed_denom} km/h"
        
        # Generate distractors
        distractors = [
            f"{distance * hours_num}/{hours_denom} km/h",
            f"{distance + hours_num} km/h",
            f"{distance - hours_num} km/h" if distance > hours_num else f"{distance + 2} km/h"
        ]
        
        options = [correct] + [d for d in distractors if d != correct][:3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question': f"Seán cycles {distance} km in {hours_num}/{hours_denom} of an hour. What is his average speed?",
            'options': options,
            'correct': correct_idx,
            'level': 11,
            'band': 'application',
            'type': 'word_problem',
            'svg': '',
            'linked_topics': None
        })
    
    # Type 3: Multi-step fraction of amount
    for _ in range(15):
        total = random.choice([24, 30, 36, 40, 48, 60])
        frac1_num = random.choice([1, 2])
        frac1_denom = random.choice([3, 4, 6])
        frac2_num = random.choice([1, 2])
        frac2_denom = random.choice([2, 3, 4])
        
        # First group
        group1 = (total * frac1_num) // frac1_denom
        # Second group is fraction of remainder
        remainder = total - group1
        group2 = (remainder * frac2_num) // frac2_denom
        # Rest
        rest = remainder - group2
        
        correct = str(rest)
        
        distractors = [
            str(group1),
            str(group2),
            str(total - group1)
        ]
        
        options = [correct] + [d for d in distractors if d != correct][:3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question': f"A class has {total} students. {frac1_num}/{frac1_denom} of them play football. Of the rest, {frac2_num}/{frac2_denom} play hurling. How many play neither sport?",
            'options': options,
            'correct': correct_idx,
            'level': 11,
            'band': 'application',
            'type': 'word_problem',
            'svg': '',
            'linked_topics': None
        })
    
    return questions


# ============================================================
# LEVEL 12: LINKED TOPICS (Cross-Topic Integration)
# ============================================================

def generate_level_12_fractions():
    """
    Level 12: Linked Topics - Cross-topic integration
    These questions link fractions to other topics.
    User needs Level 8+ in linked topics to access these.
    """
    questions = []
    
    # ----------------------------------------
    # Link: Fractions ↔ Percentages
    # ----------------------------------------
    for _ in range(20):
        denom = random.choice([2, 4, 5, 8, 10, 20, 25])
        num = random.randint(1, denom - 1)
        
        from math import gcd
        g = gcd(num, denom)
        num_simplified = num // g
        denom_simplified = denom // g
        
        percentage = (num / denom) * 100
        
        if percentage == int(percentage):
            correct = f"{int(percentage)}%"
        else:
            correct = f"{percentage:.1f}%"
        
        # Distractors
        distractors = [
            f"{int(num_simplified * 10)}%",  # Common mistake
            f"{denom}%",
            f"{int(100 / denom)}%"
        ]
        
        options = [correct] + [d for d in distractors if d != correct][:3]
        while len(options) < 4:
            options.append(f"{random.randint(1, 99)}%")
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        svg = generate_fraction_to_percent_svg(num_simplified, denom_simplified)
        
        questions.append({
            'question': f"Express {num_simplified}/{denom_simplified} as a percentage.",
            'options': options,
            'correct': correct_idx,
            'level': 12,
            'band': 'linked',
            'type': 'visual',
            'svg': svg,
            'linked_topics': 'percentages'  # IMPORTANT: Specifies linked topic
        })
    
    # ----------------------------------------
    # Link: Fractions ↔ Probability
    # ----------------------------------------
    for _ in range(15):
        total = random.choice([10, 12, 15, 20])
        favorable = random.randint(2, total - 2)
        
        from math import gcd
        g = gcd(favorable, total)
        frac_num = favorable // g
        frac_denom = total // g
        
        correct = f"{frac_num}/{frac_denom}"
        
        # Distractors
        other = total - favorable
        g2 = gcd(other, total)
        complement = f"{other // g2}/{total // g2}"
        
        distractors = [
            complement,  # P(not event)
            f"{favorable}/{total}",  # Unsimplified (if different)
            f"{frac_denom}/{frac_num}" if frac_num < frac_denom else f"1/{frac_denom}"  # Inverted
        ]
        
        options = [correct] + [d for d in distractors if d != correct][:3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        svg = generate_probability_fraction_svg(favorable, total)
        
        questions.append({
            'question': f"A bag contains {favorable} red and {total - favorable} blue marbles. One is picked at random. Express P(red) as a fraction in lowest terms.",
            'options': options,
            'correct': correct_idx,
            'level': 12,
            'band': 'linked',
            'type': 'visual',
            'svg': svg,
            'linked_topics': 'probability'  # IMPORTANT: Specifies linked topic
        })
    
    # ----------------------------------------
    # Link: Fractions ↔ Decimals
    # ----------------------------------------
    for _ in range(15):
        denom = random.choice([2, 4, 5, 8, 10, 20])
        num = random.randint(1, denom - 1)
        
        decimal = num / denom
        correct = f"{decimal:.2f}".rstrip('0').rstrip('.')
        if '.' not in correct:
            correct = correct + ".0"
        
        # Distractors - common decimal conversion errors
        distractors = [
            f"{num}.{denom}",  # Wrong interpretation
            f"0.{num}{denom}",  # Concatenation error
            f"{decimal + 0.1:.2f}".rstrip('0').rstrip('.')  # Off by 0.1
        ]
        
        options = [correct] + [d for d in distractors if d != correct][:3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question': f"Convert {num}/{denom} to a decimal.",
            'options': options,
            'correct': correct_idx,
            'level': 12,
            'band': 'linked',
            'type': 'calculation',
            'svg': '',
            'linked_topics': 'decimals'  # IMPORTANT: Specifies linked topic
        })
    
    # ----------------------------------------
    # Link: Fractions ↔ Percentages + Probability (Multiple links!)
    # ----------------------------------------
    for _ in range(10):
        total = random.choice([20, 25, 40, 50])
        favorable = random.randint(4, total // 2)
        
        percentage = (favorable / total) * 100
        correct = f"{int(percentage)}%"
        
        distractors = [
            f"{favorable}%",
            f"{100 - int(percentage)}%",
            f"{int(percentage / 2)}%"
        ]
        
        options = [correct] + [d for d in distractors if d != correct][:3]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question': f"In a survey of {total} students, {favorable} prefer maths. If a student is chosen at random, what is the probability (as a percentage) that they prefer maths?",
            'options': options,
            'correct': correct_idx,
            'level': 12,
            'band': 'linked',
            'type': 'word_problem',
            'svg': '',
            'linked_topics': 'percentages,probability'  # MULTIPLE linked topics!
        })
    
    return questions


# ============================================================
# DATABASE INSERTION
# ============================================================

def insert_questions(topic, questions):
    """Insert questions into database"""
    conn = get_db()
    cursor = conn.cursor()
    inserted = 0
    
    for q in questions:
        options = q['options']
        
        try:
            cursor.execute('''
                INSERT INTO questions_adaptive 
                (topic, question_text, option_a, option_b, option_c, option_d, 
                 correct_answer, explanation, difficulty_level, difficulty_band,
                 question_type, image_svg, linked_topics, is_active, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?)
            ''', (
                topic,
                q['question'],
                options[0] if len(options) > 0 else '',
                options[1] if len(options) > 1 else '',
                options[2] if len(options) > 2 else '',
                options[3] if len(options) > 3 else '',
                q['correct'],
                '',  # explanation
                q['level'],
                q['band'],
                q['type'],
                q.get('svg', ''),
                q.get('linked_topics', None),  # NEW: linked_topics field
                datetime.now().isoformat()
            ))
            inserted += 1
        except sqlite3.IntegrityError:
            pass  # Duplicate - skip
        except Exception as e:
            print(f"Error inserting question: {e}")
    
    conn.commit()
    conn.close()
    return inserted


def generate_all():
    """Generate Level 11-12 questions for Fractions"""
    print("=" * 60)
    print("Generating Level 11-12 Questions for Fractions")
    print("=" * 60)
    
    # Level 11
    level_11 = generate_level_11_fractions()
    print(f"\nLevel 11 (Application): Generated {len(level_11)} questions")
    inserted_11 = insert_questions('fractions', level_11)
    print(f"  Inserted: {inserted_11} new questions")
    
    # Level 12
    level_12 = generate_level_12_fractions()
    print(f"\nLevel 12 (Linked Topics): Generated {len(level_12)} questions")
    
    # Count by linked topic
    by_link = {}
    for q in level_12:
        link = q.get('linked_topics', 'none')
        by_link[link] = by_link.get(link, 0) + 1
    print(f"  By linked topic: {by_link}")
    
    inserted_12 = insert_questions('fractions', level_12)
    print(f"  Inserted: {inserted_12} new questions")
    
    # Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Total Level 11 inserted: {inserted_11}")
    print(f"Total Level 12 inserted: {inserted_12}")
    print(f"\nLevel 12 Unlock Requirements:")
    print(f"  - Level 8+ in fractions (primary)")
    for link in by_link:
        if link and link != 'none':
            topics = link.split(',')
            print(f"  - Level 8+ in {', '.join(topics)} (for those questions)")


def show_stats():
    """Show current question statistics"""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT difficulty_level, difficulty_band, COUNT(*) 
        FROM questions_adaptive 
        WHERE topic = 'fractions' AND is_active = 1
        GROUP BY difficulty_level, difficulty_band
        ORDER BY difficulty_level
    """)
    
    print("\nFractions Questions by Level:")
    print("-" * 40)
    for row in cursor.fetchall():
        print(f"  Level {row[0]:2d} ({row[1]:12s}): {row[2]:3d} questions")
    
    # Level 12 breakdown
    cursor.execute("""
        SELECT linked_topics, COUNT(*) 
        FROM questions_adaptive 
        WHERE topic = 'fractions' AND difficulty_level = 12 AND is_active = 1
        GROUP BY linked_topics
    """)
    
    results = cursor.fetchall()
    if results:
        print("\nLevel 12 by Linked Topics:")
        for row in results:
            print(f"  → {row[0] or 'none'}: {row[1]} questions")
    
    conn.close()


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--stats':
        show_stats()
    else:
        generate_all()
        print("\n")
        show_stats()
