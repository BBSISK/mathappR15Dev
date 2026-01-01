#!/usr/bin/env python3
"""
VISUAL QUESTION GENERATOR
=========================
Generates mathematically verified questions WITH SVG graphics.
Visual learning for fractions, percentages, probability, and more.

Usage:
    python question_generator_visual.py

This creates engaging visual questions that students can see and interact with.
"""

import sqlite3
import random
import math

# Database path
DB_PATH = 'instance/mathquiz.db'

# Track generated questions to avoid duplicates
_generated_questions = set()


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def ensure_image_column():
    """Add image_svg column if it doesn't exist"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Check if column exists
    cursor.execute("PRAGMA table_info(questions_adaptive)")
    columns = [row[1] for row in cursor.fetchall()]
    
    if 'image_svg' not in columns:
        cursor.execute("ALTER TABLE questions_adaptive ADD COLUMN image_svg TEXT")
        conn.commit()
        print("✓ Added image_svg column to questions_adaptive")
    else:
        print("✓ image_svg column already exists")
    
    conn.close()


def smart_number(val, max_decimals=2):
    """Format number - show decimals only if needed"""
    if val == int(val):
        return str(int(val))
    formatted = f"{val:.{max_decimals}f}".rstrip('0').rstrip('.')
    return formatted


def simplify_fraction(num, den):
    """Simplify a fraction and return as string"""
    if den == 0:
        return "undefined"
    g = math.gcd(abs(num), abs(den))
    num, den = num // g, den // g
    if den < 0:
        num, den = -num, -den
    if den == 1:
        return str(num)
    return f"{num}/{den}"


def save_visual_question(topic, level, question_text, options, correct_index, explanation, image_svg, question_type='visual'):
    """Save a visual question to the database"""
    global _generated_questions
    
    # Create unique key
    key = (topic, level, question_text, image_svg[:100] if image_svg else '')
    if key in _generated_questions:
        return False
    
    conn = get_db()
    cursor = conn.cursor()
    
    if level <= 3:
        band = 'beginner'
    elif level <= 7:
        band = 'intermediate'
    else:
        band = 'advanced'
    
    try:
        cursor.execute("""
            INSERT INTO questions_adaptive 
            (topic, question_text, option_a, option_b, option_c, option_d,
             correct_answer, explanation, difficulty_level, difficulty_band,
             question_type, image_svg, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
        """, (
            topic,
            question_text,
            options[0],
            options[1],
            options[2],
            options[3],
            correct_index,
            explanation,
            level,
            band,
            question_type,
            image_svg
        ))
        conn.commit()
        _generated_questions.add(key)
        conn.close()
        return True
    except Exception as e:
        conn.close()
        return False


def shuffle_options(correct, distractors):
    """Shuffle options and return (options_list, correct_index)"""
    options = [correct] + list(distractors)[:3]
    random.shuffle(options)
    correct_index = options.index(correct)
    return options, correct_index


# =============================================================================
# SVG GENERATORS
# =============================================================================

def svg_pie_chart(numerator, denominator, size=200, colors=None):
    """
    Generate SVG pie chart showing a fraction.
    
    Args:
        numerator: Number of shaded segments
        denominator: Total number of segments
        size: Width/height of SVG
        colors: Tuple of (shaded_color, unshaded_color)
    """
    if colors is None:
        colors = ('#8b5cf6', '#e5e7eb')  # Purple and gray
    
    shaded_color, unshaded_color = colors
    cx, cy = size // 2, size // 2
    radius = size // 2 - 10
    
    svg_parts = [f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">']
    
    # Background circle
    svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="{unshaded_color}" stroke="#9ca3af" stroke-width="2"/>')
    
    if numerator > 0 and numerator <= denominator:
        # Draw shaded segments
        angle_per_segment = 360 / denominator
        
        for i in range(numerator):
            start_angle = -90 + (i * angle_per_segment)
            end_angle = start_angle + angle_per_segment
            
            # Convert to radians
            start_rad = math.radians(start_angle)
            end_rad = math.radians(end_angle)
            
            # Calculate arc points
            x1 = cx + radius * math.cos(start_rad)
            y1 = cy + radius * math.sin(start_rad)
            x2 = cx + radius * math.cos(end_rad)
            y2 = cy + radius * math.sin(end_rad)
            
            # Large arc flag
            large_arc = 1 if angle_per_segment > 180 else 0
            
            # Create pie slice path
            path = f'M {cx},{cy} L {x1},{y1} A {radius},{radius} 0 {large_arc},1 {x2},{y2} Z'
            svg_parts.append(f'<path d="{path}" fill="{shaded_color}" stroke="#7c3aed" stroke-width="1"/>')
    
    # Draw segment lines
    for i in range(denominator):
        angle = -90 + (i * 360 / denominator)
        rad = math.radians(angle)
        x = cx + radius * math.cos(rad)
        y = cy + radius * math.sin(rad)
        svg_parts.append(f'<line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="#6b7280" stroke-width="1.5"/>')
    
    # Center dot
    svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="#374151"/>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def svg_bar_model(numerator, denominator, width=280, height=60, colors=None):
    """
    Generate SVG bar model showing a fraction.
    
    Args:
        numerator: Number of shaded parts
        denominator: Total number of parts
        width: Width of bar
        height: Height of bar
        colors: Tuple of (shaded_color, unshaded_color)
    """
    if colors is None:
        colors = ('#3b82f6', '#e5e7eb')  # Blue and gray
    
    shaded_color, unshaded_color = colors
    padding = 10
    bar_width = width - 2 * padding
    bar_height = height - 2 * padding
    segment_width = bar_width / denominator
    
    svg_parts = [f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    
    # Draw each segment
    for i in range(denominator):
        x = padding + i * segment_width
        color = shaded_color if i < numerator else unshaded_color
        svg_parts.append(f'<rect x="{x}" y="{padding}" width="{segment_width}" height="{bar_height}" fill="{color}" stroke="#6b7280" stroke-width="1.5"/>')
    
    # Outer border
    svg_parts.append(f'<rect x="{padding}" y="{padding}" width="{bar_width}" height="{bar_height}" fill="none" stroke="#374151" stroke-width="2"/>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def svg_progress_bar(percentage, width=280, height=50):
    """
    Generate SVG progress bar showing a percentage.
    """
    padding = 10
    bar_width = width - 2 * padding
    bar_height = 30
    filled_width = bar_width * percentage / 100
    
    svg_parts = [f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    
    # Background
    svg_parts.append(f'<rect x="{padding}" y="{padding}" width="{bar_width}" height="{bar_height}" rx="5" fill="#e5e7eb" stroke="#9ca3af" stroke-width="1"/>')
    
    # Filled portion
    if percentage > 0:
        svg_parts.append(f'<rect x="{padding}" y="{padding}" width="{filled_width}" height="{bar_height}" rx="5" fill="#10b981"/>')
    
    # Percentage markers
    for pct in [25, 50, 75]:
        x = padding + bar_width * pct / 100
        svg_parts.append(f'<line x1="{x}" y1="{padding}" x2="{x}" y2="{padding + bar_height}" stroke="#9ca3af" stroke-width="1" stroke-dasharray="2,2"/>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def svg_price_tag(original_price, discount_percent=None, sale_price=None, width=200, height=120):
    """
    Generate SVG price tag for percentage questions.
    """
    svg_parts = [f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    
    # Tag shape
    svg_parts.append(f'''
        <path d="M 20,10 L {width-10},10 L {width-10},{height-10} L 20,{height-10} L 5,{height//2} Z" 
              fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
        <circle cx="25" cy="{height//2}" r="6" fill="white" stroke="#f59e0b" stroke-width="2"/>
    ''')
    
    if discount_percent:
        # Show discount badge
        svg_parts.append(f'''
            <circle cx="{width-35}" cy="35" r="28" fill="#ef4444"/>
            <text x="{width-35}" y="32" text-anchor="middle" fill="white" font-size="12" font-weight="bold">{discount_percent}%</text>
            <text x="{width-35}" y="46" text-anchor="middle" fill="white" font-size="10" font-weight="bold">OFF</text>
        ''')
        # Original price (crossed out)
        svg_parts.append(f'''
            <text x="{width//2 - 10}" y="{height//2 - 5}" text-anchor="middle" fill="#9ca3af" font-size="16" text-decoration="line-through">€{original_price}</text>
        ''')
        if sale_price:
            svg_parts.append(f'''
                <text x="{width//2 - 10}" y="{height//2 + 25}" text-anchor="middle" fill="#059669" font-size="24" font-weight="bold">€{smart_number(sale_price)}</text>
            ''')
        else:
            svg_parts.append(f'''
                <text x="{width//2 - 10}" y="{height//2 + 25}" text-anchor="middle" fill="#059669" font-size="24" font-weight="bold">?</text>
            ''')
    else:
        # Just show original price
        svg_parts.append(f'''
            <text x="{width//2}" y="{height//2 + 10}" text-anchor="middle" fill="#374151" font-size="28" font-weight="bold">€{original_price}</text>
        ''')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def svg_dice(value, size=80):
    """Generate SVG dice showing a value 1-6"""
    svg_parts = [f'<svg width="{size}" height="{size}" viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">']
    
    # Dice body
    svg_parts.append('<rect x="5" y="5" width="70" height="70" rx="10" fill="white" stroke="#374151" stroke-width="3"/>')
    
    # Dot positions based on value
    dot_positions = {
        1: [(40, 40)],
        2: [(25, 25), (55, 55)],
        3: [(25, 25), (40, 40), (55, 55)],
        4: [(25, 25), (55, 25), (25, 55), (55, 55)],
        5: [(25, 25), (55, 25), (40, 40), (25, 55), (55, 55)],
        6: [(25, 20), (55, 20), (25, 40), (55, 40), (25, 60), (55, 60)]
    }
    
    for x, y in dot_positions.get(value, []):
        svg_parts.append(f'<circle cx="{x}" cy="{y}" r="7" fill="#1f2937"/>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def svg_spinner(sections, colors=None, size=200):
    """
    Generate SVG spinner with colored sections.
    
    Args:
        sections: List of section labels (e.g., ['Red', 'Blue', 'Green', 'Yellow'])
        colors: List of colors for sections
        size: Size of spinner
    """
    if colors is None:
        colors = ['#ef4444', '#3b82f6', '#22c55e', '#eab308', '#8b5cf6', '#f97316', '#ec4899', '#14b8a6']
    
    cx, cy = size // 2, size // 2
    radius = size // 2 - 15
    num_sections = len(sections)
    angle_per_section = 360 / num_sections
    
    svg_parts = [f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">']
    
    # Draw sections
    for i, label in enumerate(sections):
        start_angle = -90 + (i * angle_per_section)
        end_angle = start_angle + angle_per_section
        
        start_rad = math.radians(start_angle)
        end_rad = math.radians(end_angle)
        
        x1 = cx + radius * math.cos(start_rad)
        y1 = cy + radius * math.sin(start_rad)
        x2 = cx + radius * math.cos(end_rad)
        y2 = cy + radius * math.sin(end_rad)
        
        large_arc = 1 if angle_per_section > 180 else 0
        color = colors[i % len(colors)]
        
        path = f'M {cx},{cy} L {x1},{y1} A {radius},{radius} 0 {large_arc},1 {x2},{y2} Z'
        svg_parts.append(f'<path d="{path}" fill="{color}" stroke="white" stroke-width="2"/>')
        
        # Add label
        mid_angle = math.radians(start_angle + angle_per_section / 2)
        label_x = cx + (radius * 0.6) * math.cos(mid_angle)
        label_y = cy + (radius * 0.6) * math.sin(mid_angle)
        svg_parts.append(f'<text x="{label_x}" y="{label_y}" text-anchor="middle" dominant-baseline="middle" fill="white" font-size="12" font-weight="bold">{label}</text>')
    
    # Center circle
    svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="12" fill="#374151" stroke="white" stroke-width="2"/>')
    
    # Pointer
    svg_parts.append(f'<polygon points="{cx},{cy - radius - 8} {cx - 8},{cy - radius + 5} {cx + 8},{cy - radius + 5}" fill="#374151" stroke="white" stroke-width="1"/>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def svg_coin_grid(num_heads, num_tails, cols=5):
    """Generate grid of coins showing heads/tails"""
    total = num_heads + num_tails
    rows = math.ceil(total / cols)
    width = cols * 45 + 10
    height = rows * 45 + 10
    
    svg_parts = [f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    
    coins = ['H'] * num_heads + ['T'] * num_tails
    random.shuffle(coins)
    
    for i, coin in enumerate(coins):
        row = i // cols
        col = i % cols
        x = 25 + col * 45
        y = 25 + row * 45
        
        if coin == 'H':
            svg_parts.append(f'<circle cx="{x}" cy="{y}" r="18" fill="#fbbf24" stroke="#d97706" stroke-width="2"/>')
            svg_parts.append(f'<text x="{x}" y="{y + 5}" text-anchor="middle" fill="#92400e" font-size="14" font-weight="bold">H</text>')
        else:
            svg_parts.append(f'<circle cx="{x}" cy="{y}" r="18" fill="#9ca3af" stroke="#6b7280" stroke-width="2"/>')
            svg_parts.append(f'<text x="{x}" y="{y + 5}" text-anchor="middle" fill="#374151" font-size="14" font-weight="bold">T</text>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


def svg_shape_grid(shaded, total, shape='circle', cols=5):
    """Generate grid of shapes with some shaded"""
    rows = math.ceil(total / cols)
    width = cols * 50 + 20
    height = rows * 50 + 20
    
    svg_parts = [f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    
    for i in range(total):
        row = i // cols
        col = i % cols
        x = 30 + col * 50
        y = 30 + row * 50
        
        fill = '#8b5cf6' if i < shaded else '#e5e7eb'
        stroke = '#7c3aed' if i < shaded else '#9ca3af'
        
        if shape == 'circle':
            svg_parts.append(f'<circle cx="{x}" cy="{y}" r="18" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
        elif shape == 'square':
            svg_parts.append(f'<rect x="{x - 16}" y="{y - 16}" width="32" height="32" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
        elif shape == 'star':
            # Simple 5-point star
            points = []
            for j in range(10):
                angle = math.radians(-90 + j * 36)
                r = 18 if j % 2 == 0 else 8
                px = x + r * math.cos(angle)
                py = y + r * math.sin(angle)
                points.append(f"{px},{py}")
            svg_parts.append(f'<polygon points="{" ".join(points)}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
    
    svg_parts.append('</svg>')
    return '\n'.join(svg_parts)


# =============================================================================
# VISUAL FRACTIONS QUESTIONS
# =============================================================================

def generate_visual_fractions():
    """Generate visual fraction questions"""
    print("\n🥧 Generating Visual Fractions...")
    count = 0
    target_per_level = 15
    
    # Level 1-2: Identify fraction from pie chart
    for level in [1, 2]:
        generated = 0
        attempts = 0
        while generated < target_per_level and attempts < 200:
            attempts += 1
            
            if level == 1:
                denominator = random.choice([2, 3, 4])
            else:
                denominator = random.choice([4, 5, 6, 8])
            
            numerator = random.randint(1, denominator - 1)
            
            svg = svg_pie_chart(numerator, denominator)
            question = "What fraction of the circle is shaded?"
            correct = simplify_fraction(numerator, denominator)
            explanation = f"There are {denominator} equal parts in total, and {numerator} are shaded. So the fraction is {numerator}/{denominator}"
            if correct != f"{numerator}/{denominator}":
                explanation += f" = {correct}"
            
            # Generate distractors
            distractors = []
            distractors.append(simplify_fraction(denominator - numerator, denominator))  # Complement
            distractors.append(simplify_fraction(numerator, denominator + 1))
            distractors.append(simplify_fraction(numerator + 1, denominator))
            distractors = [d for d in distractors if d != correct][:3]
            while len(distractors) < 3:
                distractors.append(simplify_fraction(numerator + len(distractors) + 1, denominator + 1))
            
            options, correct_idx = shuffle_options(correct, distractors)
            if save_visual_question('fractions', level, question, options, correct_idx, explanation, svg):
                generated += 1
                count += 1
    
    # Level 3-4: Identify fraction from bar model
    for level in [3, 4]:
        generated = 0
        attempts = 0
        while generated < target_per_level and attempts < 200:
            attempts += 1
            
            if level == 3:
                denominator = random.choice([4, 5, 6])
            else:
                denominator = random.choice([6, 8, 10, 12])
            
            numerator = random.randint(1, denominator - 1)
            
            svg = svg_bar_model(numerator, denominator)
            question = "What fraction of the bar is shaded blue?"
            correct = simplify_fraction(numerator, denominator)
            explanation = f"The bar is divided into {denominator} equal parts, with {numerator} shaded. The fraction is {numerator}/{denominator}"
            if correct != f"{numerator}/{denominator}":
                explanation += f" = {correct}"
            
            distractors = []
            distractors.append(simplify_fraction(denominator - numerator, denominator))
            distractors.append(f"{numerator}/{denominator + 2}")
            distractors.append(f"{numerator + 1}/{denominator}")
            distractors = [d for d in distractors if d != correct][:3]
            while len(distractors) < 3:
                distractors.append(f"{numerator + len(distractors)}/{denominator + len(distractors)}")
            
            options, correct_idx = shuffle_options(correct, distractors)
            if save_visual_question('fractions', level, question, options, correct_idx, explanation, svg):
                generated += 1
                count += 1
    
    # Level 5-6: Shape grid fractions
    for level in [5, 6]:
        generated = 0
        attempts = 0
        while generated < target_per_level and attempts < 200:
            attempts += 1
            
            if level == 5:
                total = random.choice([6, 8, 10])
            else:
                total = random.choice([10, 12, 15])
            
            shaded = random.randint(1, total - 1)
            shape = random.choice(['circle', 'square', 'star'])
            
            svg = svg_shape_grid(shaded, total, shape)
            question = f"What fraction of the shapes are shaded purple?"
            correct = simplify_fraction(shaded, total)
            explanation = f"There are {total} shapes in total, and {shaded} are shaded. The fraction is {shaded}/{total}"
            if correct != f"{shaded}/{total}":
                explanation += f" = {correct}"
            
            distractors = []
            distractors.append(simplify_fraction(total - shaded, total))
            distractors.append(simplify_fraction(shaded + 1, total))
            distractors.append(simplify_fraction(shaded, total + 2))
            distractors = [d for d in distractors if d != correct][:3]
            while len(distractors) < 3:
                distractors.append(simplify_fraction(shaded + len(distractors) + 1, total + 1))
            
            options, correct_idx = shuffle_options(correct, distractors)
            if save_visual_question('fractions', level, question, options, correct_idx, explanation, svg):
                generated += 1
                count += 1
    
    print(f"   ✓ Generated {count} visual fraction questions")
    return count


# =============================================================================
# VISUAL PERCENTAGES QUESTIONS
# =============================================================================

def generate_visual_percentages():
    """Generate visual percentage questions"""
    print("\n💯 Generating Visual Percentages...")
    count = 0
    target_per_level = 15
    
    # Level 1-2: Read percentage from progress bar
    for level in [1, 2]:
        generated = 0
        attempts = 0
        while generated < target_per_level and attempts < 200:
            attempts += 1
            
            if level == 1:
                percentage = random.choice([25, 50, 75, 100])
            else:
                percentage = random.choice([10, 20, 30, 40, 60, 70, 80, 90])
            
            svg = svg_progress_bar(percentage)
            question = "What percentage of the bar is filled?"
            correct = f"{percentage}%"
            explanation = f"The bar shows {percentage}% filled (green portion)."
            
            distractors = [f"{percentage + 10}%", f"{max(0, percentage - 10)}%", f"{100 - percentage}%"]
            distractors = [d for d in distractors if d != correct][:3]
            while len(distractors) < 3:
                distractors.append(f"{percentage + (len(distractors) + 1) * 15}%")
            
            options, correct_idx = shuffle_options(correct, distractors)
            if save_visual_question('percentages', level, question, options, correct_idx, explanation, svg):
                generated += 1
                count += 1
    
    # Level 3-4: Price tag with discount - find sale price
    for level in [3, 4]:
        generated = 0
        attempts = 0
        while generated < target_per_level and attempts < 200:
            attempts += 1
            
            if level == 3:
                discount = random.choice([10, 20, 25, 50])
                original = random.choice([20, 40, 50, 100])
            else:
                discount = random.choice([15, 25, 30, 40])
                original = random.choice([30, 60, 80, 120, 150])
            
            sale_price = original * (100 - discount) / 100
            
            svg = svg_price_tag(original, discount_percent=discount)
            question = "What is the sale price after the discount?"
            correct = f"€{smart_number(sale_price)}"
            explanation = f"Discount = {discount}% of €{original} = €{smart_number(original * discount / 100)}\nSale price = €{original} - €{smart_number(original * discount / 100)} = €{smart_number(sale_price)}"
            
            distractors = [
                f"€{smart_number(original * discount / 100)}",  # Just the discount
                f"€{smart_number(sale_price + 5)}",
                f"€{smart_number(max(1, sale_price - 5))}"
            ]
            distractors = [d for d in distractors if d != correct][:3]
            while len(distractors) < 3:
                distractors.append(f"€{smart_number(sale_price + (len(distractors) + 1) * 3)}")
            
            options, correct_idx = shuffle_options(correct, distractors)
            if save_visual_question('percentages', level, question, options, correct_idx, explanation, svg):
                generated += 1
                count += 1
    
    # Level 5-6: Price tag - find the discount percentage
    for level in [5, 6]:
        generated = 0
        attempts = 0
        while generated < target_per_level and attempts < 200:
            attempts += 1
            
            if level == 5:
                discount = random.choice([10, 20, 25, 50])
                original = random.choice([40, 50, 100, 200])
            else:
                discount = random.choice([15, 20, 25, 30, 40])
                original = random.choice([60, 80, 120, 150])
            
            sale_price = original * (100 - discount) / 100
            
            svg = svg_price_tag(original, sale_price=sale_price)
            question = f"An item was €{original}, now €{smart_number(sale_price)}. What is the discount percentage?"
            correct = f"{discount}%"
            explanation = f"Discount = €{original} - €{smart_number(sale_price)} = €{smart_number(original - sale_price)}\nPercentage = €{smart_number(original - sale_price)} ÷ €{original} × 100 = {discount}%"
            
            distractors = [f"{discount + 5}%", f"{max(5, discount - 5)}%", f"{discount + 10}%"]
            distractors = [d for d in distractors if d != correct][:3]
            while len(distractors) < 3:
                distractors.append(f"{discount + (len(distractors) + 1) * 10}%")
            
            options, correct_idx = shuffle_options(correct, distractors)
            if save_visual_question('percentages', level, question, options, correct_idx, explanation, svg):
                generated += 1
                count += 1
    
    print(f"   ✓ Generated {count} visual percentage questions")
    return count


# =============================================================================
# VISUAL PROBABILITY QUESTIONS
# =============================================================================

def generate_visual_probability():
    """Generate visual probability questions"""
    print("\n🎲 Generating Visual Probability...")
    count = 0
    target_per_level = 15
    
    # Level 1-2: Dice probability
    for level in [1, 2]:
        generated = 0
        attempts = 0
        while generated < target_per_level and attempts < 200:
            attempts += 1
            
            if level == 1:
                # Simple: probability of specific number
                target = random.randint(1, 6)
                svg = svg_dice(target)
                question = f"If you roll a fair dice, what is the probability of getting a {target}?"
                correct = "1/6"
                explanation = f"A fair dice has 6 equally likely outcomes. Getting a {target} is 1 out of 6 possibilities, so the probability is 1/6."
            else:
                # Slightly harder: greater than or less than
                threshold = random.choice([2, 3, 4, 5])
                comparison = random.choice(['greater than', 'less than'])
                
                if comparison == 'greater than':
                    favorable = 6 - threshold
                else:
                    favorable = threshold - 1
                
                svg = svg_dice(random.randint(1, 6))  # Show random dice
                question = f"What is the probability of rolling {comparison} {threshold} on a fair dice?"
                correct = simplify_fraction(favorable, 6)
                explanation = f"Numbers {comparison} {threshold}: there are {favorable} such outcomes out of 6. Probability = {favorable}/6"
                if correct != f"{favorable}/6":
                    explanation += f" = {correct}"
            
            distractors = []
            if level == 1:
                distractors = ["1/3", "1/2", "2/6"]
            else:
                distractors.append(simplify_fraction(6 - favorable, 6))
                distractors.append(simplify_fraction(favorable + 1, 6))
                distractors.append(simplify_fraction(max(1, favorable - 1), 6))
            distractors = [d for d in distractors if d != correct][:3]
            while len(distractors) < 3:
                distractors.append(f"{len(distractors) + 1}/6")
            
            options, correct_idx = shuffle_options(correct, distractors)
            if save_visual_question('probability', level, question, options, correct_idx, explanation, svg):
                generated += 1
                count += 1
    
    # Level 3-4: Spinner probability
    for level in [3, 4]:
        generated = 0
        attempts = 0
        while generated < target_per_level and attempts < 200:
            attempts += 1
            
            if level == 3:
                sections = random.choice([
                    ['Red', 'Blue', 'Green', 'Yellow'],
                    ['A', 'B', 'C', 'D'],
                    ['1', '2', '3', '4']
                ])
            else:
                sections = random.choice([
                    ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple'],
                    ['A', 'B', 'C', 'D', 'E', 'F'],
                    ['1', '2', '3', '4', '5', '6', '7', '8']
                ])
            
            target = random.choice(sections)
            num_sections = len(sections)
            
            svg = svg_spinner(sections)
            question = f"If the spinner is fair, what is the probability of landing on {target}?"
            correct = simplify_fraction(1, num_sections)
            explanation = f"The spinner has {num_sections} equal sections. The probability of landing on {target} is 1/{num_sections}"
            if correct != f"1/{num_sections}":
                explanation += f" = {correct}"
            
            distractors = [
                simplify_fraction(2, num_sections),
                simplify_fraction(1, num_sections + 2),
                simplify_fraction(1, num_sections - 1) if num_sections > 2 else "1/2"
            ]
            distractors = [d for d in distractors if d != correct][:3]
            while len(distractors) < 3:
                distractors.append(f"1/{num_sections + len(distractors) + 1}")
            
            options, correct_idx = shuffle_options(correct, distractors)
            if save_visual_question('probability', level, question, options, correct_idx, explanation, svg):
                generated += 1
                count += 1
    
    # Level 5-6: Coin grid probability
    for level in [5, 6]:
        generated = 0
        attempts = 0
        while generated < target_per_level and attempts < 200:
            attempts += 1
            
            if level == 5:
                total = random.choice([8, 10])
            else:
                total = random.choice([10, 12, 15])
            
            heads = random.randint(2, total - 2)
            tails = total - heads
            
            svg = svg_coin_grid(heads, tails)
            target = random.choice(['heads', 'tails'])
            favorable = heads if target == 'heads' else tails
            
            question = f"If you pick one coin at random, what is the probability of getting {target}?"
            correct = simplify_fraction(favorable, total)
            explanation = f"There are {favorable} {target} out of {total} coins. Probability = {favorable}/{total}"
            if correct != f"{favorable}/{total}":
                explanation += f" = {correct}"
            
            distractors = [
                simplify_fraction(total - favorable, total),
                simplify_fraction(favorable + 1, total),
                simplify_fraction(favorable, total + 2)
            ]
            distractors = [d for d in distractors if d != correct][:3]
            while len(distractors) < 3:
                distractors.append(simplify_fraction(favorable + len(distractors) + 1, total + 1))
            
            options, correct_idx = shuffle_options(correct, distractors)
            if save_visual_question('probability', level, question, options, correct_idx, explanation, svg):
                generated += 1
                count += 1
    
    print(f"   ✓ Generated {count} visual probability questions")
    return count


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 60)
    print("VISUAL QUESTION GENERATOR")
    print("SVG Graphics for Engaging Maths Learning")
    print("=" * 60)
    
    # Ensure database has image_svg column
    ensure_image_column()
    
    total = 0
    
    total += generate_visual_fractions()
    total += generate_visual_percentages()
    total += generate_visual_probability()
    
    print("\n" + "=" * 60)
    print(f"COMPLETE! Generated {total} visual questions with SVG graphics")
    print("=" * 60)
    
    # Show summary
    conn = get_db()
    cursor = conn.cursor()
    
    print("\nVisual questions per topic:")
    cursor.execute("""
        SELECT topic, COUNT(*) 
        FROM questions_adaptive 
        WHERE image_svg IS NOT NULL AND image_svg != ''
        GROUP BY topic
    """)
    for topic, cnt in cursor.fetchall():
        print(f"  {topic}: {cnt} visual questions")
    
    conn.close()


if __name__ == '__main__':
    main()
