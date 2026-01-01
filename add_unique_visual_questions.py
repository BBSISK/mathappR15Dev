#!/usr/bin/env python3
"""
ADD MORE UNIQUE VISUAL QUESTIONS
Specifically for Fractions and Percentages to hit 75% target
Uses varied question wording to avoid UNIQUE constraint conflicts
"""

import sqlite3
import random
import math
from datetime import datetime

DB_PATH = 'instance/mathquiz.db'

def get_db():
    return sqlite3.connect(DB_PATH)

# ============================================================
# SVG GENERATORS
# ============================================================

def svg_pie_chart(num_shaded, total_slices, size=200, start_from='top'):
    """Pie chart with shaded slices - varied starting positions"""
    cx, cy, r = size//2, size//2, size//2 - 10
    angle_per_slice = 360 / total_slices
    
    # Vary starting angle for visual variety
    offset = {'top': -90, 'right': 0, 'bottom': 90, 'left': 180}[start_from]
    
    svg = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
    
    for i in range(total_slices):
        start_angle = i * angle_per_slice + offset
        end_angle = (i + 1) * angle_per_slice + offset
        
        start_rad = math.radians(start_angle)
        end_rad = math.radians(end_angle)
        
        x1 = cx + r * math.cos(start_rad)
        y1 = cy + r * math.sin(start_rad)
        x2 = cx + r * math.cos(end_rad)
        y2 = cy + r * math.sin(end_rad)
        
        large_arc = 1 if angle_per_slice > 180 else 0
        color = '#8b5cf6' if i < num_shaded else '#e5e7eb'
        
        path = f'M {cx},{cy} L {x1},{y1} A {r},{r} 0 {large_arc},1 {x2},{y2} Z'
        svg += f'<path d="{path}" fill="{color}" stroke="#374151" stroke-width="2"/>'
    
    svg += f'<circle cx="{cx}" cy="{cy}" r="4" fill="#374151"/>'
    svg += '</svg>'
    return svg


def svg_rectangle_parts(num_shaded, total_parts, orientation='horizontal'):
    """Rectangle divided into parts"""
    if orientation == 'horizontal':
        width, height = 280, 60
        part_w = (width - 20) / total_parts
        part_h = height - 20
    else:
        width, height = 80, 240
        part_w = width - 20
        part_h = (height - 20) / total_parts
    
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
    
    for i in range(total_parts):
        if orientation == 'horizontal':
            x, y = 10 + i * part_w, 10
            w, h = part_w, part_h
        else:
            x, y = 10, 10 + (total_parts - 1 - i) * part_h
            w, h = part_w, part_h
        
        color = '#8b5cf6' if i < num_shaded else '#f3f4f6'
        svg += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}" stroke="#374151" stroke-width="1"/>'
    
    svg += '</svg>'
    return svg


def svg_square_grid(rows, cols, shaded, cell_size=35):
    """Square grid with shaded cells"""
    width = cols * cell_size + 20
    height = rows * cell_size + 20
    
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
    
    count = 0
    for r in range(rows):
        for c in range(cols):
            x = 10 + c * cell_size
            y = 10 + r * cell_size
            color = '#8b5cf6' if count < shaded else '#f3f4f6'
            svg += f'<rect x="{x}" y="{y}" width="{cell_size-2}" height="{cell_size-2}" fill="{color}" stroke="#374151" stroke-width="1" rx="2"/>'
            count += 1
    
    svg += '</svg>'
    return svg


def svg_circle_set(total, shaded, size=200):
    """Set of circles, some shaded"""
    cols = min(5, total)
    rows = (total + cols - 1) // cols
    r = 20
    gap = 10
    width = cols * (2*r + gap) + 20
    height = rows * (2*r + gap) + 20
    
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
    
    count = 0
    for row in range(rows):
        for col in range(cols):
            if count >= total:
                break
            cx = 10 + r + col * (2*r + gap)
            cy = 10 + r + row * (2*r + gap)
            color = '#8b5cf6' if count < shaded else '#e5e7eb'
            svg += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" stroke="#374151" stroke-width="2"/>'
            count += 1
    
    svg += '</svg>'
    return svg


def svg_chocolate_bar(rows, cols, eaten, cell_size=25):
    """Chocolate bar with pieces eaten (for fractions)"""
    width = cols * cell_size + 20
    height = rows * cell_size + 40
    
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
    
    # Chocolate bar background
    svg += f'<rect x="10" y="10" width="{cols*cell_size}" height="{rows*cell_size}" fill="#8B4513" stroke="#5D3A1A" stroke-width="2" rx="3"/>'
    
    count = 0
    for r in range(rows):
        for c in range(cols):
            x = 10 + c * cell_size
            y = 10 + r * cell_size
            if count < eaten:
                # Eaten piece - show empty
                svg += f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" fill="#f3f4f6" stroke="#d1d5db" stroke-width="1"/>'
            else:
                # Remaining chocolate
                svg += f'<rect x="{x+2}" y="{y+2}" width="{cell_size-4}" height="{cell_size-4}" fill="#D2691E" stroke="#8B4513" stroke-width="1" rx="2"/>'
            count += 1
    
    svg += '</svg>'
    return svg


def svg_pizza(total_slices, eaten, size=180):
    """Pizza with slices eaten"""
    cx, cy, r = size//2, size//2, size//2 - 15
    angle_per = 360 / total_slices
    
    svg = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
    
    # Pizza base
    svg += f'<circle cx="{cx}" cy="{cy}" r="{r+5}" fill="#F4A460" stroke="#8B4513" stroke-width="3"/>'
    
    for i in range(total_slices):
        start = i * angle_per - 90
        end = (i + 1) * angle_per - 90
        
        x1 = cx + r * math.cos(math.radians(start))
        y1 = cy + r * math.sin(math.radians(start))
        x2 = cx + r * math.cos(math.radians(end))
        y2 = cy + r * math.sin(math.radians(end))
        
        large = 1 if angle_per > 180 else 0
        
        if i < eaten:
            # Eaten - show empty plate
            color = '#f5f5f5'
        else:
            # Pizza slice with cheese
            color = '#FFD700'
        
        path = f'M {cx},{cy} L {x1},{y1} A {r},{r} 0 {large},1 {x2},{y2} Z'
        svg += f'<path d="{path}" fill="{color}" stroke="#8B4513" stroke-width="2"/>'
        
        # Add pepperoni to uneaten slices
        if i >= eaten:
            mid = (start + end) / 2
            px = cx + r * 0.5 * math.cos(math.radians(mid))
            py = cy + r * 0.5 * math.sin(math.radians(mid))
            svg += f'<circle cx="{px}" cy="{py}" r="6" fill="#CD5C5C"/>'
    
    svg += '</svg>'
    return svg


def svg_tank_fill(percentage, width=100, height=180):
    """Water tank showing fill level"""
    fill_height = (height - 40) * percentage / 100
    
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
    
    # Tank outline
    svg += f'<rect x="15" y="20" width="{width-30}" height="{height-40}" fill="#e5e7eb" stroke="#374151" stroke-width="3" rx="5"/>'
    
    # Water fill
    if fill_height > 0:
        svg += f'<rect x="18" y="{20 + (height-40) - fill_height}" width="{width-36}" height="{fill_height}" fill="#60a5fa" rx="3"/>'
    
    # Measurement lines
    for i in range(1, 10):
        y = 20 + (height - 40) * (10 - i) / 10
        svg += f'<line x1="10" y1="{y}" x2="15" y2="{y}" stroke="#374151" stroke-width="1"/>'
    
    svg += '</svg>'
    return svg


def svg_progress_circle(percentage, size=150):
    """Circular progress indicator"""
    cx, cy, r = size//2, size//2, size//2 - 15
    circumference = 2 * math.pi * r
    dash = circumference * percentage / 100
    
    svg = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
    
    # Background circle
    svg += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#e5e7eb" stroke-width="12"/>'
    
    # Progress arc
    svg += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#8b5cf6" stroke-width="12" stroke-dasharray="{dash} {circumference}" transform="rotate(-90 {cx} {cy})"/>'
    
    # Percentage text
    svg += f'<text x="{cx}" y="{cy+8}" text-anchor="middle" font-size="24" fill="#374151" font-weight="bold">?</text>'
    
    svg += '</svg>'
    return svg


def svg_jar_balls(total, colored, color='red', size=150):
    """Jar with colored balls"""
    svg = f'<svg width="{size}" height="{size+30}" viewBox="0 0 {size} {size+30}">'
    
    # Jar
    svg += f'<path d="M 30 30 L 25 {size} Q 25 {size+20} {size//2} {size+20} Q {size-25} {size+20} {size-25} {size} L {size-30} 30 Z" fill="#e0f2fe" stroke="#0ea5e9" stroke-width="2"/>'
    svg += f'<ellipse cx="{size//2}" cy="30" rx="{size//2-30}" ry="10" fill="#bae6fd" stroke="#0ea5e9" stroke-width="2"/>'
    
    # Balls
    ball_colors = {'red': '#ef4444', 'blue': '#3b82f6', 'green': '#22c55e', 'yellow': '#fbbf24'}
    positions = [(45, 130), (75, 125), (105, 130), (55, 100), (95, 100), (75, 80), (60, 60), (90, 60)]
    
    for i in range(min(total, len(positions))):
        x, y = positions[i]
        c = ball_colors.get(color, '#ef4444') if i < colored else '#9ca3af'
        svg += f'<circle cx="{x}" cy="{y}" r="12" fill="{c}" stroke="#374151" stroke-width="1"/>'
        svg += f'<circle cx="{x-3}" cy="{y-3}" r="3" fill="white" opacity="0.5"/>'
    
    svg += '</svg>'
    return svg


# ============================================================
# QUESTION GENERATORS - VARIED WORDING
# ============================================================

def generate_fraction_questions_v2():
    """Generate fraction questions with varied wording"""
    questions = []
    
    # Pie chart variations with different wordings
    pie_wordings = [
        "What fraction of the shape is coloured?",
        "What fraction of this circle is purple?",
        "Look at the diagram. What fraction is shaded?",
        "What part of the circle is filled in?",
        "Express the shaded area as a fraction.",
    ]
    
    for level in range(1, 11):
        band = 'beginner' if level <= 3 else ('intermediate' if level <= 6 else 'advanced')
        
        denoms = [2,3,4] if level <= 3 else ([4,5,6,8] if level <= 6 else [6,8,10,12])
        starts = ['top', 'right', 'bottom', 'left']
        
        for denom in denoms:
            for num in range(1, denom):
                for wording in random.sample(pie_wordings, 2):
                    start = random.choice(starts)
                    svg = svg_pie_chart(num, denom, start_from=start)
                    correct = f'{num}/{denom}'
                    
                    options = [correct, f'{denom-num}/{denom}', f'{num}/{denom+1}', f'{num+1}/{denom}' if num+1<denom else f'1/{denom}']
                    
                    questions.append({
                        'level': level, 'band': band,
                        'question': wording,
                        'options': options[:4], 'correct': correct,
                        'svg': svg, 'type': 'visual'
                    })
    
    # Rectangle/bar variations
    bar_wordings = [
        "What fraction of the bar is shaded?",
        "What fraction of this rectangle is coloured?",
        "Look at the strip. What fraction is purple?",
        "What part of this shape is filled?",
    ]
    
    for level in range(1, 11):
        band = 'beginner' if level <= 3 else ('intermediate' if level <= 6 else 'advanced')
        denoms = [2,3,4,5] if level <= 3 else ([5,6,8,10] if level <= 6 else [8,10,12])
        
        for denom in denoms:
            for num in range(1, denom):
                orient = random.choice(['horizontal', 'vertical'])
                svg = svg_rectangle_parts(num, denom, orient)
                correct = f'{num}/{denom}'
                wording = random.choice(bar_wordings)
                
                questions.append({
                    'level': level, 'band': band,
                    'question': wording,
                    'options': [correct, f'{denom-num}/{denom}', f'{num}/{denom+2}', f'{num+1}/{denom}' if num+1<denom else f'1/{denom}'],
                    'correct': correct, 'svg': svg, 'type': 'visual'
                })
    
    # Circle sets
    for level in range(1, 11):
        band = 'beginner' if level <= 3 else ('intermediate' if level <= 6 else 'advanced')
        totals = [3,4,5] if level <= 3 else ([6,8,10] if level <= 6 else [8,10,12])
        
        for total in totals:
            for shaded in range(1, total):
                svg = svg_circle_set(total, shaded)
                correct = f'{shaded}/{total}'
                
                questions.append({
                    'level': level, 'band': band,
                    'question': f'What fraction of the circles is shaded?',
                    'options': [correct, f'{total-shaded}/{total}', f'{shaded}/{total+1}', f'{shaded+1}/{total}' if shaded+1<total else f'1/{total}'],
                    'correct': correct, 'svg': svg, 'type': 'visual'
                })
    
    # Pizza fractions
    pizza_wordings = [
        "What fraction of the pizza has been eaten?",
        "What fraction of the pizza is left?",
    ]
    
    for level in range(1, 8):
        band = 'beginner' if level <= 3 else 'intermediate'
        
        for total in [4, 6, 8]:
            for eaten in range(1, total):
                svg = svg_pizza(total, eaten)
                
                # Eaten version
                questions.append({
                    'level': level, 'band': band,
                    'question': 'What fraction of the pizza has been eaten?',
                    'options': [f'{eaten}/{total}', f'{total-eaten}/{total}', f'{eaten}/{total+1}', f'1/{total}'],
                    'correct': f'{eaten}/{total}', 'svg': svg, 'type': 'visual'
                })
                
                # Remaining version
                questions.append({
                    'level': level, 'band': band,
                    'question': 'What fraction of the pizza is left?',
                    'options': [f'{total-eaten}/{total}', f'{eaten}/{total}', f'{total-eaten}/{total+1}', f'1/{total}'],
                    'correct': f'{total-eaten}/{total}', 'svg': svg, 'type': 'visual'
                })
    
    # Chocolate bar fractions
    for level in range(2, 9):
        band = 'beginner' if level <= 3 else ('intermediate' if level <= 6 else 'advanced')
        
        for rows, cols in [(2, 4), (2, 5), (3, 4)]:
            total = rows * cols
            for eaten in range(1, total):
                svg = svg_chocolate_bar(rows, cols, eaten)
                
                questions.append({
                    'level': level, 'band': band,
                    'question': 'What fraction of the chocolate bar has been eaten?',
                    'options': [f'{eaten}/{total}', f'{total-eaten}/{total}', f'{eaten}/{total+1}', f'1/{total}'],
                    'correct': f'{eaten}/{total}', 'svg': svg, 'type': 'visual'
                })
    
    # Grid fractions
    for level in range(1, 11):
        band = 'beginner' if level <= 3 else ('intermediate' if level <= 6 else 'advanced')
        
        grids = [(2,3), (2,4), (3,3)] if level <= 3 else ([(3,4), (2,5), (4,4)] if level <= 6 else [(3,5), (4,5), (5,5)])
        
        for rows, cols in grids:
            total = rows * cols
            for shaded in range(1, min(total, 8)):
                svg = svg_square_grid(rows, cols, shaded)
                correct = f'{shaded}/{total}'
                
                questions.append({
                    'level': level, 'band': band,
                    'question': 'What fraction of the grid is shaded?',
                    'options': [correct, f'{total-shaded}/{total}', f'{shaded}/{total+1}', f'{shaded+1}/{total}'],
                    'correct': correct, 'svg': svg, 'type': 'visual'
                })
    
    return questions


def generate_percentage_questions_v2():
    """Generate percentage questions with varied visuals"""
    questions = []
    
    # Tank fill levels
    for level in range(1, 11):
        band = 'beginner' if level <= 3 else ('intermediate' if level <= 6 else 'advanced')
        
        percentages = [10,20,25,50,75] if level <= 3 else ([15,30,35,40,45,55,60,65,70,80,85] if level <= 6 else [5,12,18,22,28,33,38,42,48,52,58,62,67,72,78,83,88,92])
        
        for pct in percentages:
            svg = svg_tank_fill(pct)
            
            questions.append({
                'level': level, 'band': band,
                'question': 'What percentage of the tank is filled with water?',
                'options': [f'{pct}%', f'{pct+10}%', f'{100-pct}%', f'{pct-10}%' if pct>=10 else f'{pct+15}%'],
                'correct': f'{pct}%', 'svg': svg, 'type': 'visual'
            })
    
    # Progress circles
    for level in range(1, 11):
        band = 'beginner' if level <= 3 else ('intermediate' if level <= 6 else 'advanced')
        
        percentages = [25,50,75] if level <= 3 else ([10,20,30,40,60,70,80,90] if level <= 6 else [15,35,45,55,65,85])
        
        for pct in percentages:
            svg = svg_progress_circle(pct)
            
            questions.append({
                'level': level, 'band': band,
                'question': 'What percentage does the progress circle show?',
                'options': [f'{pct}%', f'{pct+10}%', f'{100-pct}%', f'{pct+5}%'],
                'correct': f'{pct}%', 'svg': svg, 'type': 'visual'
            })
    
    # Grid shading with percentage
    grid_wordings = [
        "What percentage of the squares is shaded?",
        "What percentage of this grid is coloured?",
        "What percentage of the grid is purple?",
    ]
    
    for level in range(1, 11):
        band = 'beginner' if level <= 3 else ('intermediate' if level <= 6 else 'advanced')
        
        # 10x10 grid = easy percentages
        for pct in [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95]:
            svg = svg_square_grid(10, 10, pct, 18)
            wording = random.choice(grid_wordings)
            
            questions.append({
                'level': level, 'band': band,
                'question': wording,
                'options': [f'{pct}%', f'{pct+5}%', f'{100-pct}%', f'{pct-5}%' if pct>=5 else f'{pct+10}%'],
                'correct': f'{pct}%', 'svg': svg, 'type': 'visual'
            })
    
    # 5x4 = 20 grid (multiples of 5%)
    for level in range(4, 11):
        band = 'intermediate' if level <= 6 else 'advanced'
        
        for shaded in range(1, 20):
            pct = shaded * 5
            svg = svg_square_grid(5, 4, shaded, 30)
            
            questions.append({
                'level': level, 'band': band,
                'question': 'What percentage of this 5×4 grid is shaded?',
                'options': [f'{pct}%', f'{pct+5}%', f'{100-pct}%', f'{pct+10}%'],
                'correct': f'{pct}%', 'svg': svg, 'type': 'visual'
            })
    
    # Jar with balls for percentage
    for level in range(3, 11):
        band = 'beginner' if level <= 3 else ('intermediate' if level <= 6 else 'advanced')
        
        configs = [(4, 1), (4, 2), (4, 3), (5, 2), (5, 3), (8, 2), (8, 4), (8, 6)]
        
        for total, colored in configs:
            pct = int(colored / total * 100)
            svg = svg_jar_balls(total, colored)
            
            questions.append({
                'level': level, 'band': band,
                'question': f'What percentage of the balls are red?',
                'options': [f'{pct}%', f'{100-pct}%', f'{pct+10}%', f'{pct+25}%'],
                'correct': f'{pct}%', 'svg': svg, 'type': 'visual'
            })
    
    return questions


# ============================================================
# DATABASE
# ============================================================

def insert_questions(questions, topic):
    """Insert using INSERT OR IGNORE to skip duplicates"""
    conn = get_db()
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
                q['svg'],
                datetime.now().isoformat()
            ))
            if cursor.rowcount > 0:
                inserted += 1
            else:
                skipped += 1
        except Exception as e:
            skipped += 1
    
    conn.commit()
    conn.close()
    return inserted, skipped


def show_stats():
    """Show stats for BETA topics only"""
    conn = get_db()
    cursor = conn.cursor()
    
    print("\n" + "="*60)
    print("BETA TOPICS VISUAL QUESTION STATISTICS")
    print("="*60)
    
    cursor.execute("""
        SELECT topic,
               COUNT(*) as total,
               SUM(CASE WHEN question_type = 'visual' THEN 1 ELSE 0 END) as visual
        FROM questions_adaptive
        WHERE is_active = 1 AND topic IN ('fractions', 'percentages', 'probability')
        GROUP BY topic
    """)
    
    grand_total = 0
    grand_visual = 0
    
    for topic, total, visual in cursor.fetchall():
        pct = (visual / total * 100) if total > 0 else 0
        status = "✅" if pct >= 75 else "⚠️"
        print(f"\n{topic}:")
        print(f"  Total: {total}, Visual: {visual} ({pct:.1f}%) {status}")
        grand_total += total
        grand_visual += visual
    
    if grand_total > 0:
        overall_pct = grand_visual / grand_total * 100
        print(f"\n{'='*40}")
        print(f"OVERALL: {grand_visual}/{grand_total} = {overall_pct:.1f}% visual")
        if overall_pct >= 75:
            print("✅ 75% TARGET ACHIEVED!")
        else:
            needed = int(grand_total * 0.75) - grand_visual
            print(f"⚠️  Need {needed} more visual questions")
    
    conn.close()


def main():
    print("="*60)
    print("ADDING MORE UNIQUE VISUAL QUESTIONS")
    print("="*60)
    
    print("\n📊 Generating varied Fractions visuals...")
    fractions = generate_fraction_questions_v2()
    ins, skip = insert_questions(fractions, 'fractions')
    print(f"   Added {ins} new questions ({skip} duplicates skipped)")
    
    print("\n📊 Generating varied Percentages visuals...")
    percentages = generate_percentage_questions_v2()
    ins, skip = insert_questions(percentages, 'percentages')
    print(f"   Added {ins} new questions ({skip} duplicates skipped)")
    
    show_stats()
    print("\n✅ Done!")


if __name__ == '__main__':
    main()
