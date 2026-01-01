#!/usr/bin/env python3
"""
Delete and regenerate spinner questions with correct colors
"""

import sqlite3
import math
from datetime import datetime

DB_PATH = 'instance/mathquiz.db'

def svg_spinner(sections, size=180):
    """Spinner with colors matching labels"""
    cx, cy, r = size//2, size//2, size//2 - 15
    n = len(sections)
    angle_per = 360 / n
    
    color_map = {
        'R': '#ef4444', 'Red': '#ef4444', 'red': '#ef4444',
        'B': '#3b82f6', 'Blue': '#3b82f6', 'blue': '#3b82f6',
        'G': '#22c55e', 'Green': '#22c55e', 'green': '#22c55e',
        'Y': '#fbbf24', 'Yellow': '#fbbf24', 'yellow': '#fbbf24',
        'P': '#a855f7', 'Purple': '#a855f7', 'purple': '#a855f7',
        'O': '#f97316', 'Orange': '#f97316', 'orange': '#f97316',
        '1': '#ef4444', '2': '#3b82f6', '3': '#22c55e', 
        '4': '#fbbf24', '5': '#a855f7', '6': '#f97316',
        'A': '#ef4444', 'C': '#22c55e',
    }
    fallback = ['#ef4444', '#3b82f6', '#22c55e', '#fbbf24', '#a855f7', '#f97316', '#14b8a6', '#ec4899']
    
    svg = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
    
    for i, label in enumerate(sections):
        start = i * angle_per - 90
        end = (i + 1) * angle_per - 90
        mid = (start + end) / 2
        
        x1 = cx + r * math.cos(math.radians(start))
        y1 = cy + r * math.sin(math.radians(start))
        x2 = cx + r * math.cos(math.radians(end))
        y2 = cy + r * math.sin(math.radians(end))
        
        large = 1 if angle_per > 180 else 0
        color = color_map.get(str(label), fallback[i % len(fallback)])
        
        path = f'M {cx},{cy} L {x1},{y1} A {r},{r} 0 {large},1 {x2},{y2} Z'
        svg += f'<path d="{path}" fill="{color}" stroke="#374151" stroke-width="2"/>'
        
        lr = r * 0.6
        lx = cx + lr * math.cos(math.radians(mid))
        ly = cy + lr * math.sin(math.radians(mid))
        svg += f'<text x="{lx}" y="{ly}" text-anchor="middle" dominant-baseline="middle" font-size="12" fill="white" font-weight="bold">{label}</text>'
    
    svg += f'<circle cx="{cx}" cy="{cy}" r="6" fill="#374151"/>'
    svg += '</svg>'
    return svg


def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Delete old spinner questions
    cursor.execute("""
        DELETE FROM questions_adaptive 
        WHERE question_text LIKE '%spinner%'
    """)
    deleted = cursor.rowcount
    print(f"🗑️  Deleted {deleted} old spinner questions")
    
    conn.commit()
    
    # Regenerate spinner questions with correct colors
    spinner_questions = []
    
    # 4-section color spinner
    for level in range(1, 11):
        band = 'beginner' if level <= 3 else ('intermediate' if level <= 6 else 'advanced')
        
        sections = ['Red', 'Blue', 'Green', 'Yellow']
        svg = svg_spinner(sections)
        
        for target in sections:
            spinner_questions.append({
                'level': level,
                'band': band,
                'question': f'This spinner has 4 equal sections. What is the probability of landing on {target}?',
                'options': ['1/4', '1/2', '1/3', '1/6'],
                'correct': '1/4',
                'svg': svg
            })
    
    # 2 Red, 2 Blue spinner (probability 1/2)
    for level in range(2, 8):
        band = 'beginner' if level <= 3 else 'intermediate'
        
        sections = ['Red', 'Red', 'Blue', 'Blue']
        svg = svg_spinner(sections)
        
        spinner_questions.append({
            'level': level,
            'band': band,
            'question': 'This spinner has 4 equal sections: 2 Red and 2 Blue. What is the probability of landing on Red?',
            'options': ['1/2', '1/4', '2/3', '3/4'],
            'correct': '1/2',
            'svg': svg
        })
    
    # 6-section numbered spinner
    for level in range(4, 11):
        band = 'intermediate' if level <= 6 else 'advanced'
        
        sections = ['1', '2', '3', '4', '5', '6']
        svg = svg_spinner(sections)
        
        spinner_questions.append({
            'level': level,
            'band': band,
            'question': 'This spinner has 6 equal sections numbered 1-6. What is the probability of landing on an even number?',
            'options': ['1/2', '1/3', '1/6', '2/3'],
            'correct': '1/2',
            'svg': svg
        })
        
        spinner_questions.append({
            'level': level,
            'band': band,
            'question': 'This spinner has 6 equal sections numbered 1-6. What is the probability of landing on a number greater than 4?',
            'options': ['1/3', '1/2', '1/6', '2/3'],
            'correct': '1/3',
            'svg': svg
        })
    
    # 3 Red, 2 Blue, 1 Green spinner
    for level in range(4, 11):
        band = 'intermediate' if level <= 6 else 'advanced'
        
        sections = ['Red', 'Red', 'Red', 'Blue', 'Blue', 'Green']
        svg = svg_spinner(sections)
        
        spinner_questions.append({
            'level': level,
            'band': band,
            'question': 'This spinner has 6 equal sections: 3 Red, 2 Blue, and 1 Green. What is the probability of landing on Red?',
            'options': ['1/2', '1/3', '1/6', '2/3'],
            'correct': '1/2',
            'svg': svg
        })
        
        spinner_questions.append({
            'level': level,
            'band': band,
            'question': 'This spinner has 6 equal sections: 3 Red, 2 Blue, and 1 Green. What is the probability of landing on Blue?',
            'options': ['1/3', '1/2', '1/6', '2/6'],
            'correct': '1/3',
            'svg': svg
        })
    
    # 8-section spinner
    for level in range(6, 11):
        band = 'intermediate' if level <= 6 else 'advanced'
        
        sections = ['Red', 'Red', 'Blue', 'Blue', 'Green', 'Green', 'Yellow', 'Yellow']
        svg = svg_spinner(sections)
        
        spinner_questions.append({
            'level': level,
            'band': band,
            'question': 'This spinner has 8 equal sections: 2 of each color (Red, Blue, Green, Yellow). What is the probability of landing on Red?',
            'options': ['1/4', '1/8', '1/2', '2/8'],
            'correct': '1/4',
            'svg': svg
        })
    
    # Insert new spinner questions
    inserted = 0
    for q in spinner_questions:
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
                'probability',
                q['question'],
                options[0], options[1], options[2], options[3],
                correct_letter,
                '',
                q['level'],
                q['band'],
                'visual',
                q['svg'],
                datetime.now().isoformat()
            ))
            if cursor.rowcount > 0:
                inserted += 1
        except Exception as e:
            print(f"Error: {e}")
    
    conn.commit()
    conn.close()
    
    print(f"✅ Added {inserted} new spinner questions with correct colors")


if __name__ == '__main__':
    main()
