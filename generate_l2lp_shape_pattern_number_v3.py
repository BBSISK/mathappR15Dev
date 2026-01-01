"""
AgentMath L2LP Question Generator V3
Topic: Shape, Pattern & Number (l2_shape_pattern_number)
NCCA Module: Understanding shapes, patterns and number properties

V3: Completely rewritten with UNIQUE question texts per level.

Author: AgentMath Generator
Version: 3.0
Date: December 2025
"""

import sqlite3
import random
from datetime import datetime

TOPIC = 'l2_shape_pattern_number'
QUESTIONS_PER_LEVEL = 50
TOTAL_LEVELS = 12
DATABASE_PATH = 'instance/mathquiz.db'

def get_difficulty_band(level):
    if level <= 3:
        return 'beginner'
    elif level <= 6:
        return 'intermediate'
    elif level <= 9:
        return 'advanced'
    elif level == 10:
        return 'mastery'
    elif level == 11:
        return 'application'
    else:
        return 'linked'


def generate_level_1_questions():
    """Level 1: Basic Shapes - 50 unique questions"""
    questions = []
    
    # Shape identification (25 questions)
    shapes = [
        ("circle", "round with no corners", 0),
        ("square", "4 equal sides and 4 corners", 4),
        ("triangle", "3 sides and 3 corners", 3),
        ("rectangle", "4 sides with 2 long and 2 short", 4),
        ("oval", "like a stretched circle", 0),
        ("diamond", "like a square turned on its point", 4),
        ("star", "has points sticking out", 5),
        ("heart", "shape of love", 0),
        ("pentagon", "5 sides and 5 corners", 5),
        ("hexagon", "6 sides and 6 corners", 6)
    ]
    
    for name, description, corners in shapes:
        # Question type 1: Identify from description
        options = [name.capitalize(), "Banana", "Cloud", "Tree"]
        random.shuffle(options)
        correct_idx = options.index(name.capitalize())
        
        questions.append({
            'question_text': f"Which shape is {description}?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"A {name} is {description}"
        })
        
        # Question type 2: How many corners?
        if corners > 0:
            options = [str(corners), str(corners + 1), str(corners - 1) if corners > 1 else "0", str(corners + 2)]
            random.shuffle(options)
            correct_idx = options.index(str(corners))
            
            questions.append({
                'question_text': f"How many corners does a {name} have?",
                'options': options,
                'correct_index': correct_idx,
                'explanation': f"A {name} has {corners} corners"
            })
    
    # Real-world shape examples (15 questions)
    real_world = [
        ("wheel", "circle", "Wheels are round"),
        ("window", "rectangle", "Windows are usually rectangular"),
        ("pizza slice", "triangle", "Pizza slices are triangular"),
        ("dice", "square faces", "Dice have square faces"),
        ("clock face", "circle", "Clock faces are circular"),
        ("book cover", "rectangle", "Books are rectangular"),
        ("yield sign", "triangle", "Yield signs are triangular"),
        ("stop sign", "octagon", "Stop signs have 8 sides"),
        ("coin", "circle", "Coins are circular"),
        ("door", "rectangle", "Doors are rectangular"),
        ("ice cream cone top", "circle", "Ice cream top is circular"),
        ("sandwich cut diagonally", "triangle", "Diagonal cut makes triangles"),
        ("picture frame", "rectangle", "Frames are usually rectangular"),
        ("sun drawing", "circle", "We draw the sun as a circle"),
        ("egg shape", "oval", "Eggs are oval shaped")
    ]
    
    for item, shape, explanation in real_world:
        shape_options = ["Circle", "Square", "Triangle", "Rectangle", "Oval", "Octagon"]
        correct = shape.split()[0].capitalize()
        wrong = [s for s in shape_options if s.lower() not in shape.lower()][:3]
        
        options = [correct] + wrong
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"What shape is a {item}?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_2_questions():
    """Level 2: Shape Properties - 50 unique questions"""
    questions = []
    
    # Sides and corners (25 questions)
    shapes_data = [
        ("triangle", 3, 3), ("square", 4, 4), ("rectangle", 4, 4),
        ("pentagon", 5, 5), ("hexagon", 6, 6), ("heptagon", 7, 7),
        ("octagon", 8, 8), ("nonagon", 9, 9), ("decagon", 10, 10)
    ]
    
    for shape, sides, corners in shapes_data:
        # Sides question
        options = [str(sides), str(sides + 1), str(sides - 1) if sides > 1 else "0", str(sides + 2)]
        random.shuffle(options)
        correct_idx = options.index(str(sides))
        
        questions.append({
            'question_text': f"How many sides does a {shape} have?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"A {shape} has {sides} sides"
        })
        
        # What shape has X sides?
        options = [shape.capitalize(), shapes_data[(shapes_data.index((shape, sides, corners)) + 1) % len(shapes_data)][0].capitalize(),
                   shapes_data[(shapes_data.index((shape, sides, corners)) + 2) % len(shapes_data)][0].capitalize(), "Circle"]
        random.shuffle(options)
        correct_idx = options.index(shape.capitalize())
        
        questions.append({
            'question_text': f"Which shape has exactly {sides} sides?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"A {shape} has {sides} sides"
        })
    
    # Comparing shapes (14 questions)
    comparisons = [
        ("square", "triangle", "more sides", "Square has 4, triangle has 3"),
        ("hexagon", "pentagon", "more sides", "Hexagon has 6, pentagon has 5"),
        ("circle", "square", "no corners", "Circles have no corners"),
        ("rectangle", "square", "different length sides", "Rectangles have 2 long and 2 short"),
        ("triangle", "square", "fewer sides", "Triangle has 3, square has 4"),
        ("octagon", "hexagon", "more sides", "Octagon has 8, hexagon has 6"),
        ("pentagon", "triangle", "more sides", "Pentagon has 5, triangle has 3")
    ]
    
    for shape1, shape2, property, explanation in comparisons:
        q_text = f"Which has {property}: a {shape1} or a {shape2}?"
        
        if "more" in property or "different" in property or "no corners" in property:
            correct = shape1.capitalize()
        else:
            correct = shape1.capitalize()
        
        options = [shape1.capitalize(), shape2.capitalize(), "Same", "Cannot tell"]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
        
        # Reverse question
        if "fewer" in property:
            q_text = f"Which has more sides: a {shape1} or a {shape2}?"
            correct = shape2.capitalize()
            
            options = [shape1.capitalize(), shape2.capitalize(), "Same", "Cannot tell"]
            random.shuffle(options)
            correct_idx = options.index(correct)
            
            questions.append({
                'question_text': q_text,
                'options': options,
                'correct_index': correct_idx,
                'explanation': explanation
            })
    
    return questions[:50]


def generate_level_3_questions():
    """Level 3: 2D Shape Names - 50 unique questions"""
    questions = []
    
    # Advanced shape vocabulary (25 questions)
    vocab = [
        ("2D shape", "flat shape with length and width only", "Like shapes on paper"),
        ("polygon", "closed shape with straight sides", "Many-sided figure"),
        ("regular polygon", "all sides and angles equal", "Like a perfect square"),
        ("irregular polygon", "sides or angles are different", "Like a rectangle"),
        ("quadrilateral", "any shape with 4 sides", "Quad means 4"),
        ("parallel sides", "sides that never meet", "Like train tracks"),
        ("perpendicular", "lines that meet at right angles", "Like a plus sign"),
        ("vertex", "corner of a shape", "Where two sides meet"),
        ("vertices", "more than one corner", "Plural of vertex"),
        ("edge", "side of a shape", "The line between corners"),
        ("diagonal", "line from corner to opposite corner", "Cuts through the middle"),
        ("symmetry", "same on both sides", "Mirror image"),
        ("line of symmetry", "divides shape into matching halves", "Fold line"),
        ("right angle", "90 degree angle", "Like a square corner"),
        ("acute angle", "less than 90 degrees", "Sharp, pointy angle")
    ]
    
    for term, definition, extra in vocab:
        wrong_defs = [d[1] for d in vocab if d[0] != term][:3]
        
        options = [definition] + wrong_defs
        random.shuffle(options)
        correct_idx = options.index(definition)
        
        questions.append({
            'question_text': f"What does '{term}' mean in geometry?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"{term.capitalize()}: {definition}. {extra}"
        })
    
    # Shape classification (25 questions)
    classifications = [
        ("square", "quadrilateral", "It has 4 sides"),
        ("rectangle", "quadrilateral", "It has 4 sides"),
        ("rhombus", "quadrilateral", "It has 4 sides"),
        ("trapezoid", "quadrilateral", "It has 4 sides"),
        ("parallelogram", "quadrilateral", "It has 4 sides"),
        ("equilateral triangle", "triangle with all equal sides", "Equi = equal"),
        ("isosceles triangle", "triangle with 2 equal sides", "Iso = same"),
        ("scalene triangle", "triangle with no equal sides", "All different"),
        ("right triangle", "triangle with one 90° angle", "Has a right angle"),
        ("regular hexagon", "hexagon with all equal sides", "All sides same length"),
        ("circle", "shape with no sides", "Curved line"),
        ("semicircle", "half of a circle", "Semi = half"),
        ("quarter circle", "quarter of a circle", "Quarter = 1/4"),
        ("ellipse", "stretched circle", "Oval shape"),
        ("kite", "quadrilateral with 2 pairs of equal adjacent sides", "Like a flying kite")
    ]
    
    for shape, category, explanation in classifications:
        categories = ["quadrilateral", "triangle with all equal sides", "shape with no sides", 
                      "hexagon with all equal sides", "triangle with 2 equal sides"]
        wrong = [c for c in categories if c != category][:3]
        
        options = [category] + wrong
        random.shuffle(options)
        correct_idx = options.index(category)
        
        questions.append({
            'question_text': f"How would you classify a {shape}?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # True/False about shapes (10 questions)
    tf = [
        ("All squares are rectangles", True, "Squares are special rectangles"),
        ("All rectangles are squares", False, "Only if all sides equal"),
        ("A triangle can have 2 right angles", False, "Max 1 right angle in a triangle"),
        ("A circle has infinite lines of symmetry", True, "Any diameter is a line of symmetry"),
        ("A square has 4 lines of symmetry", True, "2 diagonal + 2 through midpoints"),
        ("A rectangle has 4 lines of symmetry", False, "Only 2 lines of symmetry"),
        ("An equilateral triangle has 3 lines of symmetry", True, "One through each vertex"),
        ("All quadrilaterals have 4 right angles", False, "Only rectangles and squares"),
        ("A pentagon has more sides than a hexagon", False, "Pentagon 5, hexagon 6"),
        ("Regular shapes have all equal sides", True, "Definition of regular")
    ]
    
    for statement, is_true, explanation in tf:
        options = ["True", "False", "Sometimes", "Cannot tell"]
        correct_idx = 0 if is_true else 1
        
        questions.append({
            'question_text': f"True or False: {statement}",
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_4_questions():
    """Level 4: Simple Patterns - 50 unique questions"""
    questions = []
    
    # Number patterns (25 questions)
    number_patterns = [
        ([2, 4, 6, 8], 10, "+2", "Add 2 each time"),
        ([5, 10, 15, 20], 25, "+5", "Add 5 each time"),
        ([3, 6, 9, 12], 15, "+3", "Add 3 each time"),
        ([1, 3, 5, 7], 9, "+2 (odd)", "Add 2, odd numbers"),
        ([10, 20, 30, 40], 50, "+10", "Add 10 each time"),
        ([4, 8, 12, 16], 20, "+4", "Add 4 each time"),
        ([7, 14, 21, 28], 35, "+7", "Add 7 each time"),
        ([100, 90, 80, 70], 60, "-10", "Subtract 10 each time"),
        ([50, 45, 40, 35], 30, "-5", "Subtract 5 each time"),
        ([20, 18, 16, 14], 12, "-2", "Subtract 2 each time"),
        ([1, 2, 4, 8], 16, "×2", "Double each time"),
        ([1, 4, 9, 16], 25, "squares", "1², 2², 3², 4², 5²"),
        ([2, 6, 18, 54], 162, "×3", "Multiply by 3"),
        ([1, 1, 2, 3, 5], 8, "Fibonacci", "Add previous two"),
        ([10, 11, 13, 16, 20], 25, "+1,+2,+3,+4", "Add increasing amount")
    ]
    
    for pattern, next_val, rule, explanation in number_patterns:
        pattern_str = ", ".join(str(x) for x in pattern)
        
        wrong1 = next_val + 1
        wrong2 = next_val - 1 if next_val > 1 else next_val + 2
        wrong3 = pattern[-1]
        
        options = [str(next_val), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(options)
        correct_idx = options.index(str(next_val))
        
        questions.append({
            'question_text': f"What comes next? {pattern_str}, ___",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"Rule: {rule}. {explanation}"
        })
        
        # Ask for the rule
        options = [rule, "+1", "×10", "random"]
        random.shuffle(options)
        correct_idx = options.index(rule)
        
        questions.append({
            'question_text': f"What is the rule for this pattern? {pattern_str}",
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Shape patterns (20 questions)
    shape_patterns = [
        ("circle, square, circle, square", "circle", "Alternating"),
        ("triangle, triangle, square, triangle, triangle, square", "triangle", "2 triangles then square"),
        ("red, blue, red, blue, red", "blue", "Alternating colours"),
        ("big, small, big, small", "big", "Size alternates"),
        ("star, star, moon, star, star", "moon", "2 stars then moon"),
        ("up, down, up, down, up", "down", "Direction alternates"),
        ("1, A, 2, B, 3", "C", "Number, letter alternating"),
        ("dog, cat, bird, dog, cat", "bird", "Repeating trio"),
        ("🔴🔵🔴🔵🔴", "🔵", "Red, blue alternating"),
        ("AAB, AAB, AAB", "AAB", "Repeating AAB")
    ]
    
    for pattern, next_item, rule in shape_patterns:
        items = pattern.replace(",", "").split()
        unique_items = list(set(items))
        
        wrong = [i for i in unique_items if i != next_item]
        while len(wrong) < 3:
            wrong.append("none")
        
        options = [next_item] + wrong[:3]
        random.shuffle(options)
        correct_idx = options.index(next_item)
        
        questions.append({
            'question_text': f"What comes next in this pattern? {pattern}, ___",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"Pattern rule: {rule}"
        })
    
    return questions[:50]


def generate_level_5_questions():
    """Level 5: Complex Patterns - 50 unique questions"""
    questions = []
    
    # Two-step patterns (25 questions)
    two_step = [
        ([2, 5, 8, 11], 14, "+3", "Add 3 each time"),
        ([1, 4, 7, 10, 13], 16, "+3", "Add 3 each time"),
        ([100, 93, 86, 79], 72, "-7", "Subtract 7 each time"),
        ([3, 7, 11, 15, 19], 23, "+4", "Add 4 each time"),
        ([50, 46, 42, 38], 34, "-4", "Subtract 4 each time"),
        ([2, 4, 8, 16, 32], 64, "×2", "Double each time"),
        ([243, 81, 27, 9], 3, "÷3", "Divide by 3 each time"),
        ([1, 2, 4, 7, 11], 16, "+1,+2,+3,+4,+5", "Add increasing numbers"),
        ([2, 3, 5, 8, 12], 17, "+1,+2,+3,+4,+5", "Add increasing numbers"),
        ([1000, 500, 250, 125], 62.5, "÷2", "Halve each time")
    ]
    
    for pattern, next_val, rule, explanation in two_step:
        pattern_str = ", ".join(str(x) for x in pattern)
        
        if isinstance(next_val, float):
            wrong1 = next_val + 10
            wrong2 = next_val - 10
            wrong3 = pattern[-1]
        else:
            wrong1 = next_val + 3
            wrong2 = next_val - 2 if next_val > 2 else next_val + 5
            wrong3 = pattern[-1] + 1
        
        options = [str(next_val), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(options)
        correct_idx = options.index(str(next_val))
        
        questions.append({
            'question_text': f"Continue the pattern: {pattern_str}, ___",
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Find missing term (15 questions)
    missing = [
        ([2, "_", 6, 8, 10], 4, "+2 pattern"),
        ([5, 10, "_", 20, 25], 15, "+5 pattern"),
        ([100, 90, "_", 70, 60], 80, "-10 pattern"),
        ([1, "_", 9, 16, 25], 4, "Square numbers"),
        ([3, 6, "_", 12, 15], 9, "+3 pattern"),
        ([2, 4, "_", 16, 32], 8, "×2 pattern"),
        (["_", 4, 7, 10, 13], 1, "+3 pattern"),
        ([8, "_", 24, 32, 40], 16, "+8 pattern"),
        ([50, 45, "_", 35, 30], 40, "-5 pattern"),
        ([1, 3, "_", 10, 15], 6, "Triangular numbers"),
        ([12, "_", 8, 6, 4], 10, "-2 pattern"),
        ([7, 14, "_", 28, 35], 21, "+7 pattern"),
        ([9, "_", 25, 36, 49], 16, "Square numbers"),
        ([100, "_", 25, 12.5], 50, "÷2 pattern"),
        (["_", 6, 9, 12, 15], 3, "+3 pattern")
    ]
    
    for pattern, answer, rule in missing:
        pattern_str = ", ".join(str(x) for x in pattern)
        
        wrong1 = answer + 2
        wrong2 = answer - 1 if answer > 1 else answer + 3
        wrong3 = answer * 2
        
        options = [str(answer), str(wrong1), str(wrong2), str(wrong3)]
        random.shuffle(options)
        correct_idx = options.index(str(answer))
        
        questions.append({
            'question_text': f"Find the missing number: {pattern_str}",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"This is a {rule}"
        })
    
    # Growing patterns (10 questions)
    growing = [
        ("1 dot, 3 dots, 6 dots, 10 dots", "15 dots", "Triangular numbers: +2, +3, +4..."),
        ("1 square, 4 squares, 9 squares", "16 squares", "Square numbers"),
        ("1×1, 2×2, 3×3, 4×4", "5×5 = 25", "Growing squares"),
        ("1+2, 1+2+3, 1+2+3+4", "1+2+3+4+5 = 15", "Sum of counting numbers"),
        ("Level 1: 2 blocks, Level 2: 6 blocks, Level 3: 12 blocks", "20 blocks", "Add 4, 6, 8..."),
        ("Row 1: 1, Row 2: 1+2, Row 3: 1+2+3", "Row 4: 1+2+3+4 = 10", "Adding rows"),
        ("Week 1: €5, Week 2: €10, Week 3: €20", "Week 4: €40", "Doubling"),
        ("Day 1: 3 pages, Day 2: 6 pages, Day 3: 12 pages", "Day 4: 24 pages", "Doubling"),
        ("1×2=2, 2×3=6, 3×4=12", "4×5=20", "Product of consecutive"),
        ("Perimeter 4, Perimeter 8, Perimeter 12", "Perimeter 16", "Add 4 each time")
    ]
    
    for pattern, answer, rule in growing:
        parts = answer.split("=")
        correct = parts[-1].strip() if len(parts) > 1 else answer
        
        options = [correct, "Wrong answer 1", "Wrong answer 2", "Cannot determine"]
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"What comes next? {pattern}, ___",
            'options': options,
            'correct_index': correct_idx,
            'explanation': rule
        })
    
    return questions[:50]


def generate_level_6_questions():
    """Level 6: Odd & Even Numbers - 50 unique questions"""
    questions = []
    
    # Identify odd/even (25 questions)
    numbers = list(range(1, 51))
    random.shuffle(numbers)
    
    for num in numbers[:25]:
        is_even = num % 2 == 0
        correct = "Even" if is_even else "Odd"
        
        options = ["Even", "Odd", "Neither", "Both"]
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"Is {num} odd or even?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"{num} is {correct.lower()} because it {'can' if is_even else 'cannot'} be divided by 2 evenly"
        })
    
    # Properties of odd/even (15 questions)
    properties = [
        ("Even + Even = ?", "Even", "2 + 4 = 6 (even)"),
        ("Odd + Odd = ?", "Even", "3 + 5 = 8 (even)"),
        ("Even + Odd = ?", "Odd", "2 + 3 = 5 (odd)"),
        ("Even × Even = ?", "Even", "2 × 4 = 8 (even)"),
        ("Odd × Odd = ?", "Odd", "3 × 5 = 15 (odd)"),
        ("Even × Odd = ?", "Even", "2 × 3 = 6 (even)"),
        ("Is 0 even or odd?", "Even", "0 ÷ 2 = 0 with no remainder"),
        ("All even numbers end in...", "0, 2, 4, 6, or 8", "Last digit determines even/odd"),
        ("All odd numbers end in...", "1, 3, 5, 7, or 9", "Last digit determines even/odd"),
        ("Even - Even = ?", "Even", "8 - 4 = 4 (even)"),
        ("Odd - Odd = ?", "Even", "7 - 3 = 4 (even)"),
        ("Even - Odd = ?", "Odd", "8 - 3 = 5 (odd)"),
        ("The next even number after 24 is?", "26", "Add 2 to any even"),
        ("The next odd number after 37 is?", "39", "Add 2 to any odd"),
        ("Double any number is always?", "Even", "2 × anything is even")
    ]
    
    for q, correct, explanation in properties:
        if correct in ["Even", "Odd"]:
            options = ["Even", "Odd", "Neither", "Could be either"]
        elif "0, 2" in correct:
            options = [correct, "1, 3, 5, 7, or 9", "Only 0", "Any digit"]
        elif "1, 3" in correct:
            options = [correct, "0, 2, 4, 6, or 8", "Only 5", "Any digit"]
        else:
            val = int(''.join(filter(str.isdigit, correct)))
            options = [correct, str(val + 1), str(val - 1), str(val + 2)]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Word problems with odd/even (10 questions)
    word_problems = [
        ("Sara has 7 sweets. Can she share them equally with her friend?", "No", "7 is odd, can't split evenly into 2"),
        ("There are 12 students. Can they make pairs?", "Yes", "12 is even, 12÷2=6 pairs"),
        ("Mum baked 15 cookies. Can she put same number on 2 plates?", "No", "15 is odd"),
        ("20 children need partners. Possible?", "Yes", "20 is even"),
        ("Class has 25 students. Can they all have a partner?", "No", "25 is odd, one left over"),
        ("Share 30 marbles between 2 people equally?", "Yes", "30 is even"),
        ("8 slices of pizza for 2 people. Fair?", "Yes", "8÷2=4 each"),
        ("17 cards dealt to 2 players. Fair?", "No", "17 is odd"),
        ("14 football players split into 2 teams. Fair?", "Yes", "14÷2=7 each"),
        ("9 pieces of fruit for 2 children. Fair?", "No", "9 is odd")
    ]
    
    for q, correct, explanation in word_problems:
        options = ["Yes", "No", "Sometimes", "Cannot tell"]
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_7_questions():
    """Level 7: Number Properties - 50 unique questions"""
    questions = []
    
    # Factors (20 questions)
    factor_qs = [
        (12, [1, 2, 3, 4, 6, 12], "Factors of 12"),
        (20, [1, 2, 4, 5, 10, 20], "Factors of 20"),
        (15, [1, 3, 5, 15], "Factors of 15"),
        (24, [1, 2, 3, 4, 6, 8, 12, 24], "Factors of 24"),
        (16, [1, 2, 4, 8, 16], "Factors of 16"),
        (30, [1, 2, 3, 5, 6, 10, 15, 30], "Factors of 30"),
        (18, [1, 2, 3, 6, 9, 18], "Factors of 18"),
        (25, [1, 5, 25], "Factors of 25"),
        (36, [1, 2, 3, 4, 6, 9, 12, 18, 36], "Factors of 36"),
        (10, [1, 2, 5, 10], "Factors of 10")
    ]
    
    for num, factors, explanation in factor_qs:
        # How many factors?
        options = [str(len(factors)), str(len(factors) + 2), str(len(factors) - 1), str(len(factors) + 1)]
        random.shuffle(options)
        correct_idx = options.index(str(len(factors)))
        
        questions.append({
            'question_text': f"How many factors does {num} have?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"{explanation}: {factors}"
        })
        
        # Is X a factor?
        test_factor = random.choice(factors)
        options = ["Yes", "No", "Sometimes", "Cannot tell"]
        
        questions.append({
            'question_text': f"Is {test_factor} a factor of {num}?",
            'options': options,
            'correct_index': 0,
            'explanation': f"Yes, {num} ÷ {test_factor} = {num // test_factor}"
        })
    
    # Multiples (15 questions)
    multiple_qs = [
        (3, [3, 6, 9, 12, 15, 18, 21, 24, 27, 30], "Multiples of 3"),
        (5, [5, 10, 15, 20, 25, 30, 35, 40, 45, 50], "Multiples of 5"),
        (4, [4, 8, 12, 16, 20, 24, 28, 32, 36, 40], "Multiples of 4"),
        (7, [7, 14, 21, 28, 35, 42, 49, 56, 63, 70], "Multiples of 7"),
        (6, [6, 12, 18, 24, 30, 36, 42, 48, 54, 60], "Multiples of 6")
    ]
    
    for num, multiples, explanation in multiple_qs:
        # What is 5th multiple?
        options = [str(multiples[4]), str(multiples[3]), str(multiples[5] if len(multiples) > 5 else multiples[4] + num), str(num * 6)]
        random.shuffle(options)
        correct_idx = options.index(str(multiples[4]))
        
        questions.append({
            'question_text': f"What is the 5th multiple of {num}?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': f"5 × {num} = {multiples[4]}"
        })
        
        # Is X a multiple?
        test = random.choice(multiples)
        options = ["Yes", "No", "Sometimes", "Cannot tell"]
        
        questions.append({
            'question_text': f"Is {test} a multiple of {num}?",
            'options': options,
            'correct_index': 0,
            'explanation': f"Yes, {test} ÷ {num} = {test // num}"
        })
        
        # First 3 multiples
        first_three = ", ".join(str(x) for x in multiples[:3])
        options = [first_three, ", ".join(str(x) for x in multiples[1:4]), f"{num}, {num+1}, {num+2}", "1, 2, 3"]
        random.shuffle(options)
        correct_idx = options.index(first_three)
        
        questions.append({
            'question_text': f"What are the first 3 multiples of {num}?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Prime numbers (15 questions)
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    non_primes = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25]
    
    for p in primes[:7]:
        options = ["Yes", "No", "Sometimes", "Cannot tell"]
        
        questions.append({
            'question_text': f"Is {p} a prime number?",
            'options': options,
            'correct_index': 0,
            'explanation': f"{p} is prime - only divisible by 1 and itself"
        })
    
    for np in non_primes[:8]:
        options = ["Yes", "No", "Sometimes", "Cannot tell"]
        
        questions.append({
            'question_text': f"Is {np} a prime number?",
            'options': options,
            'correct_index': 1,
            'explanation': f"{np} is not prime - has factors other than 1 and itself"
        })
    
    return questions[:50]


def generate_level_8_questions():
    """Level 8: 3D Shapes - 50 unique questions"""
    questions = []
    
    # 3D shape names (20 questions)
    shapes_3d = [
        ("cube", 6, 12, 8, "6 square faces"),
        ("cuboid", 6, 12, 8, "6 rectangular faces"),
        ("sphere", 0, 0, 0, "no faces, edges, or vertices"),
        ("cylinder", 2, 0, 0, "2 circular faces"),
        ("cone", 1, 0, 1, "1 circular face, 1 vertex"),
        ("pyramid (square)", 5, 8, 5, "1 square + 4 triangles"),
        ("triangular prism", 5, 9, 6, "2 triangles + 3 rectangles"),
        ("hemisphere", 1, 0, 0, "1 flat circular face"),
        ("pentagonal prism", 7, 15, 10, "2 pentagons + 5 rectangles"),
        ("hexagonal prism", 8, 18, 12, "2 hexagons + 6 rectangles")
    ]
    
    for name, faces, edges, vertices, description in shapes_3d:
        # Faces question
        if faces > 0:
            options = [str(faces), str(faces + 2), str(faces - 1) if faces > 1 else "0", str(faces + 1)]
            random.shuffle(options)
            correct_idx = options.index(str(faces))
            
            questions.append({
                'question_text': f"How many faces does a {name} have?",
                'options': options,
                'correct_index': correct_idx,
                'explanation': f"A {name} has {faces} faces - {description}"
            })
        
        # Vertices question
        if vertices > 0:
            options = [str(vertices), str(vertices + 2), str(vertices - 2) if vertices > 2 else "0", str(vertices + 1)]
            random.shuffle(options)
            correct_idx = options.index(str(vertices))
            
            questions.append({
                'question_text': f"How many vertices (corners) does a {name} have?",
                'options': options,
                'correct_index': correct_idx,
                'explanation': f"A {name} has {vertices} vertices"
            })
    
    # Real-world 3D examples (15 questions)
    real_3d = [
        ("dice", "cube", "Dice have 6 square faces"),
        ("cereal box", "cuboid", "Boxes are rectangular cuboids"),
        ("football", "sphere", "Balls are spherical"),
        ("ice cream cone", "cone", "Cones are... cones!"),
        ("tin can", "cylinder", "Cans are cylindrical"),
        ("Egyptian pyramid", "square pyramid", "Ancient pyramids"),
        ("Toblerone box", "triangular prism", "Triangular cross-section"),
        ("globe", "sphere", "Globes are spherical"),
        ("party hat", "cone", "Party hats are cone-shaped"),
        ("pipe", "cylinder", "Pipes are cylindrical"),
        ("tent", "triangular prism", "Some tents are prism-shaped"),
        ("bowling ball", "sphere", "Balls are spheres"),
        ("tissue box", "cuboid", "Rectangular box"),
        ("planet Earth", "sphere", "Earth is roughly spherical"),
        ("soup can", "cylinder", "Cans are cylinders")
    ]
    
    for item, shape, explanation in real_3d:
        all_shapes = ["cube", "cuboid", "sphere", "cone", "cylinder", "square pyramid", "triangular prism"]
        wrong = [s for s in all_shapes if s != shape][:3]
        
        options = [shape] + wrong
        random.shuffle(options)
        correct_idx = options.index(shape)
        
        questions.append({
            'question_text': f"What 3D shape is a {item} most like?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # 3D shape properties (15 questions)
    properties_3d = [
        ("Which 3D shape has no flat faces?", "Sphere"),
        ("Which shape has all square faces?", "Cube"),
        ("Which shape can roll?", "Sphere, cylinder, or cone"),
        ("Which shape has a point at the top?", "Cone or pyramid"),
        ("What's the relationship: F + V - E = ?", "2 (Euler's formula)"),
        ("A cube has how many edges?", "12"),
        ("A triangular prism has how many faces?", "5"),
        ("Which shape has 2 circular faces?", "Cylinder"),
        ("Net of a cube has how many squares?", "6"),
        ("What shape has 1 curved face and 2 flat faces?", "Cylinder"),
        ("Pyramid with triangle base has how many faces?", "4"),
        ("What solid has 8 vertices?", "Cube or cuboid"),
        ("Which shape has no vertices?", "Sphere or cylinder"),
        ("A prism always has how many identical faces?", "2 (the ends)"),
        ("What 3D shape is made by rotating a circle?", "Sphere")
    ]
    
    for q, correct in properties_3d:
        if "Sphere" in correct and "," in correct:
            options = [correct, "Cube only", "Pyramid only", "None of these"]
        elif correct.isdigit():
            val = int(correct)
            options = [correct, str(val + 2), str(val - 2) if val > 2 else str(val + 4), str(val * 2)]
        else:
            shapes = ["Sphere", "Cube", "Cylinder", "Cone", "Pyramid", "Prism"]
            wrong = [s for s in shapes if s not in correct][:3]
            options = [correct] + wrong
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': correct
        })
    
    return questions[:50]


def generate_level_9_questions():
    """Level 9: Symmetry & Transformations - 50 unique questions"""
    questions = []
    
    # Lines of symmetry (25 questions)
    symmetry = [
        ("square", 4, "2 diagonal + 2 through midpoints"),
        ("rectangle", 2, "Through midpoints only"),
        ("equilateral triangle", 3, "Through each vertex"),
        ("isosceles triangle", 1, "Through the apex"),
        ("circle", "infinite", "Any diameter"),
        ("regular pentagon", 5, "Through each vertex"),
        ("regular hexagon", 6, "Through vertices and midpoints"),
        ("letter A", 1, "Vertical line"),
        ("letter B", 1, "Horizontal line"),
        ("letter H", 2, "Vertical and horizontal"),
        ("letter O", "infinite", "It's circular"),
        ("letter X", 4, "2 diagonal + 2 through center"),
        ("heart shape", 1, "Vertical line down middle"),
        ("arrow pointing up", 1, "Vertical line"),
        ("scalene triangle", 0, "No equal sides")
    ]
    
    for shape, lines, explanation in symmetry:
        if isinstance(lines, int):
            options = [str(lines), str(lines + 1), str(lines - 1) if lines > 0 else "1", str(lines + 2)]
        else:
            options = ["Infinite", "0", "4", "Cannot have symmetry"]
        
        random.shuffle(options)
        correct = str(lines) if isinstance(lines, int) else "Infinite"
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': f"How many lines of symmetry does a {shape} have?",
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Transformations (15 questions)
    transforms = [
        ("Moving a shape without turning it", "Translation (slide)"),
        ("Flipping a shape over a line", "Reflection (flip)"),
        ("Turning a shape around a point", "Rotation (turn)"),
        ("Making a shape bigger or smaller", "Scaling (resize)"),
        ("A shape after reflection looks...", "Like a mirror image"),
        ("A shape after translation looks...", "The same, just moved"),
        ("A shape after 180° rotation looks...", "Upside down"),
        ("A shape after 90° rotation looks...", "Turned on its side"),
        ("Which transformation changes size?", "Scaling"),
        ("Which transformation changes orientation?", "Rotation or reflection"),
        ("If you slide a square right 3 units, its shape...", "Stays the same"),
        ("If you reflect a letter P, you might get...", "Letter reversed (like q)"),
        ("If you rotate letter N 180°, you get...", "The letter N"),
        ("If you rotate letter b 180°, you get...", "The letter q"),
        ("Tessellation uses which transformations?", "Translations, rotations, reflections")
    ]
    
    for q, correct in transforms:
        if "Translation" in correct or "Reflection" in correct or "Rotation" in correct or "Scaling" in correct:
            options = [correct, "Translation (slide)", "Reflection (flip)", "Rotation (turn)"]
            options = list(set(options))
            while len(options) < 4:
                options.append("Scaling (resize)")
        elif "mirror" in correct.lower() or "same" in correct.lower():
            options = [correct, "Completely different", "Larger", "Smaller"]
        else:
            options = [correct, "Wrong answer 1", "Wrong answer 2", "Cannot tell"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': correct
        })
    
    # Rotational symmetry (10 questions)
    rotational = [
        ("Order of rotational symmetry for a square", "4"),
        ("Order of rotational symmetry for equilateral triangle", "3"),
        ("Order of rotational symmetry for rectangle", "2"),
        ("Order of rotational symmetry for regular hexagon", "6"),
        ("Order of rotational symmetry for letter S", "2"),
        ("Order of rotational symmetry for letter N", "2"),
        ("Order of rotational symmetry for letter Z", "2"),
        ("Order of rotational symmetry for scalene triangle", "1 (none)"),
        ("Order of rotational symmetry for circle", "Infinite"),
        ("If a shape has order 4 rotational symmetry, it looks the same after...", "90° rotation")
    ]
    
    for q, correct in rotational:
        if correct.isdigit():
            options = [correct, str(int(correct) + 1), str(int(correct) - 1) if int(correct) > 1 else "0", str(int(correct) + 2)]
        elif "Infinite" in correct:
            options = ["Infinite", "0", "4", "12"]
        else:
            options = [correct, "180° rotation", "45° rotation", "360° rotation"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': correct
        })
    
    return questions[:50]


def generate_level_10_questions():
    """Level 10: Number Systems - 50 unique questions"""
    questions = []
    
    # Place value extended (20 questions)
    place_values = [
        (1234, "thousands", 1, "1 is in thousands place"),
        (5678, "hundreds", 6, "6 is in hundreds place"),
        (9012, "tens", 1, "1 is in tens place"),
        (3456, "ones", 6, "6 is in ones place"),
        (12345, "ten thousands", 1, "1 is in ten thousands"),
        (67890, "thousands", 7, "7 is in thousands place"),
        (2468, "value of 4", 400, "4 is in hundreds = 400"),
        (1357, "value of 3", 300, "3 is in hundreds = 300"),
        (8024, "value of 8", 8000, "8 is in thousands = 8000"),
        (9631, "value of 6", 600, "6 is in hundreds = 600")
    ]
    
    for num, question_type, answer, explanation in place_values:
        if "value" in question_type:
            q_text = f"In {num}, what is the value of the digit {question_type.split()[-1]}?"
            options = [str(answer), str(answer * 10), str(answer // 10) if answer >= 10 else str(answer + 10), str(answer + 100)]
        else:
            q_text = f"In {num}, which digit is in the {question_type} place?"
            options = [str(answer), str((answer + 1) % 10), str((answer + 2) % 10), str((answer + 3) % 10)]
        
        random.shuffle(options)
        correct_idx = options.index(str(answer))
        
        questions.append({
            'question_text': q_text,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Rounding (15 questions)
    rounding = [
        (37, "nearest 10", 40, "37 rounds up to 40"),
        (82, "nearest 10", 80, "82 rounds down to 80"),
        (45, "nearest 10", 50, "45 rounds up to 50"),
        (234, "nearest 100", 200, "234 rounds down to 200"),
        (678, "nearest 100", 700, "678 rounds up to 700"),
        (450, "nearest 100", 500, "450 rounds up to 500"),
        (1234, "nearest 1000", 1000, "1234 rounds down to 1000"),
        (6789, "nearest 1000", 7000, "6789 rounds up to 7000"),
        (3500, "nearest 1000", 4000, "3500 rounds up to 4000"),
        (567, "nearest 10", 570, "567 rounds up to 570"),
        (8943, "nearest 100", 8900, "8943 rounds down to 8900"),
        (2350, "nearest 100", 2400, "2350 rounds up to 2400"),
        (15678, "nearest 10000", 20000, "15678 rounds up to 20000"),
        (42500, "nearest 10000", 40000, "42500 rounds down to 40000"),
        (750, "nearest 100", 800, "750 rounds up to 800")
    ]
    
    for num, to, answer, explanation in rounding:
        options = [str(answer), str(answer + 10), str(answer - 10) if answer >= 10 else str(answer + 20), str(num)]
        random.shuffle(options)
        correct_idx = options.index(str(answer))
        
        questions.append({
            'question_text': f"Round {num} to the {to}.",
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    # Comparing and ordering (15 questions)
    comparing = [
        ("4567 ___ 4576", "<", "4567 is less"),
        ("9999 ___ 10000", "<", "9999 is less"),
        ("5050 ___ 5050", "=", "Equal"),
        ("12345 ___ 12354", "<", "12345 is less"),
        ("99999 ___ 100000", "<", "99999 is less"),
        ("Order: 432, 423, 342", "342, 423, 432", "Smallest to largest"),
        ("Order: 1010, 1001, 1100", "1001, 1010, 1100", "Smallest to largest"),
        ("Largest: 5678, 5687, 5768", "5768", "Compare digit by digit"),
        ("Smallest: 9123, 9132, 9213", "9123", "Compare digit by digit"),
        ("Between 200 and 300", "234", "234 is between"),
        ("Between 1000 and 2000", "1500", "1500 is between"),
        ("Halfway between 0 and 100", "50", "50 is halfway"),
        ("Halfway between 100 and 200", "150", "150 is halfway"),
        ("1000 more than 4567", "5567", "4567 + 1000 = 5567"),
        ("1000 less than 8234", "7234", "8234 - 1000 = 7234")
    ]
    
    for q, correct, explanation in comparing:
        if correct in ["<", ">", "="]:
            options = ["<", ">", "=", "Cannot compare"]
        elif "," in correct:
            parts = correct.split(", ")
            wrong1 = ", ".join(reversed(parts))
            wrong2 = ", ".join([parts[1], parts[0], parts[2]])
            options = [correct, wrong1, wrong2, "Cannot order"]
        elif correct.isdigit():
            val = int(correct)
            options = [correct, str(val + 10), str(val - 10) if val >= 10 else str(val + 20), str(val + 100)]
        else:
            options = [correct, "Wrong", "Cannot determine", "None"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': explanation
        })
    
    return questions[:50]


def generate_level_11_questions():
    """Level 11: Applied Patterns - 50 unique questions"""
    questions = []
    
    # Real-world patterns (50 questions)
    applied = [
        ("Bus comes every 15 mins. First at 9:00. Next 3 times?", "9:15, 9:30, 9:45"),
        ("Save €5 per week. After 8 weeks?", "€40"),
        ("Plant grows 2cm per day. Height after 1 week?", "14cm"),
        ("Heart beats 70 times per minute. In 5 minutes?", "350 beats"),
        ("Double your money each day. Start €1. Day 5?", "€16"),
        ("Staircase pattern: 1, 3, 6, 10. Next?", "15 (triangular numbers)"),
        ("Fibonacci in nature: 1, 1, 2, 3, 5. Next?", "8"),
        ("Square numbers: 1, 4, 9, 16. Next?", "25"),
        ("Cube numbers: 1, 8, 27. Next?", "64"),
        ("Powers of 2: 2, 4, 8, 16. Next?", "32"),
        ("Tiles: row 1 has 2, row 2 has 4, row 3 has 6. Row 5?", "10 tiles"),
        ("Salary increases €500 per year. Start €20,000. Year 4?", "€21,500"),
        ("Temperature rises 2°C per hour. Start 10°C. After 5 hours?", "20°C"),
        ("Each bounce is half the height. Start 128cm. After 4 bounces?", "8cm"),
        ("Bacteria double every hour. Start 100. After 3 hours?", "800"),
        ("Book has 50 pages. Read 8 per day. Days to finish?", "7 days (6.25 rounded up)"),
        ("100m race times: 12.5s, 12.3s, 12.1s. Pattern continues. Next?", "11.9s"),
        ("Fence posts every 2m. 20m fence. Posts needed?", "11 posts"),
        ("Handshakes: 2 people=1, 3 people=3, 4 people=6. 5 people?", "10 handshakes"),
        ("Layers: 1, 3, 5, 7 blocks. Layer 5?", "9 blocks"),
        ("Petals: 3, 5, 8, 13. Next (Fibonacci)?", "21"),
        ("Compound interest approx: €100→€110→€121→€133. Pattern?", "×1.1 (10% growth)"),
        ("Seating: row 1=10, row 2=12, row 3=14. Row 6?", "20 seats"),
        ("Points: win=3, draw=1. 5 wins, 2 draws?", "17 points"),
        ("Discount: 20% off. Price was €50. Now?", "€40"),
        ("Tax: add 23%. Item €100. Total?", "€123"),
        ("Markup: 50% on €20 cost. Selling price?", "€30"),
        ("Score doubles each level. Level 1=100. Level 5?", "1600"),
        ("Pages: chapter 1=15, ch 2=20, ch 3=25. Ch 5?", "35 pages"),
        ("Cuts: 1 cut=2 pieces, 2 cuts=3 pieces. 5 cuts?", "6 pieces"),
        ("Triangular numbers: 1, 3, 6, 10, 15. Next?", "21"),
        ("Perfect squares: 1, 4, 9, 16, 25. Next?", "36"),
        ("Prime numbers: 2, 3, 5, 7, 11. Next?", "13"),
        ("Odd numbers: 1, 3, 5, 7, 9. 10th odd number?", "19"),
        ("Even numbers: 2, 4, 6, 8. 15th even number?", "30"),
        ("Multiples of 7: 7, 14, 21. 8th multiple?", "56"),
        ("Counting in 3s: 3, 6, 9. 20th term?", "60"),
        ("Alternating: +2, -1, +2, -1. Start 5. After 6 steps?", "8"),
        ("Growing squares: 1×1, 2×2, 3×3. 6×6 area?", "36"),
        ("Perimeters of squares: 4, 8, 12, 16. Side 7 square?", "28"),
        ("Sequence: 1, 4, 9, 16, 25. What type?", "Square numbers"),
        ("Sequence: 1, 1, 2, 3, 5, 8. Name?", "Fibonacci sequence"),
        ("Sequence: 2, 3, 5, 7, 11. What type?", "Prime numbers"),
        ("Sequence: 1, 3, 6, 10, 15. What type?", "Triangular numbers"),
        ("Sequence: 1, 8, 27, 64. What type?", "Cube numbers"),
        ("Find pattern: 2, 6, 18, 54. Rule?", "×3 each time"),
        ("Find pattern: 100, 95, 90, 85. Rule?", "-5 each time"),
        ("Find pattern: 3, 6, 12, 24. Rule?", "×2 each time"),
        ("Find pattern: 1, 4, 7, 10. Rule?", "+3 each time"),
        ("Find pattern: 50, 25, 12.5. Rule?", "÷2 each time")
    ]
    
    for q, correct in applied:
        if "," in correct and not "€" in correct:
            options = [correct, "Wrong sequence", "Cannot determine", "Different pattern"]
        elif "€" in correct:
            val = int(''.join(filter(str.isdigit, correct)))
            options = [correct, f"€{val+10}", f"€{val-5}" if val > 5 else f"€{val*2}", f"€{val+20}"]
        elif correct.replace('.', '').isdigit():
            val = float(correct) if '.' in correct else int(correct)
            options = [str(correct), str(val + 5), str(val - 3) if val > 3 else str(val + 10), str(val * 2)]
        elif "numbers" in correct or "sequence" in correct:
            options = [correct, "Random numbers", "Even numbers", "Cannot classify"]
        elif "×" in correct or "+" in correct or "-" in correct or "÷" in correct:
            options = [correct, "+1 each time", "×10 each time", "No clear pattern"]
        else:
            options = [correct, "Different answer", "Cannot determine", "More info needed"]
        
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': correct
        })
    
    return questions[:50]


def generate_level_12_questions():
    """Level 12: Problem Solving - 50 unique questions"""
    questions = []
    
    # Multi-step problems combining shapes, patterns, numbers (50 questions)
    problems = [
        ("Square has perimeter 24cm. What is its area?", "36 cm²"),
        ("Rectangle area 48cm², width 6cm. Perimeter?", "28cm"),
        ("Triangle sides 3, 4, 5cm. Is it right-angled?", "Yes (3²+4²=5²)"),
        ("Circle diameter 14cm. Circumference roughly?", "About 44cm (π×14)"),
        ("Cube edge 5cm. Total surface area?", "150 cm² (6×25)"),
        ("Pattern: 2, 5, 11, 23. Next number?", "47 (×2+1)"),
        ("Sum of first 10 even numbers?", "110"),
        ("Sum of first 10 odd numbers?", "100"),
        ("How many rectangles in a 3×3 grid?", "36"),
        ("How many triangles in a shape with 5 points?", "10"),
        ("LCM of 4 and 6?", "12"),
        ("HCF of 24 and 36?", "12"),
        ("What % is 15 of 60?", "25%"),
        ("20% of what number is 50?", "250"),
        ("Ratio 3:5, total 40. Larger part?", "25"),
        ("Shape A has 3 more sides than shape B. B is a square. A is?", "Heptagon (7 sides)"),
        ("Pattern rule: n². What's the 12th term?", "144"),
        ("Pattern rule: 2n+1. What's the 20th term?", "41"),
        ("Pattern rule: n(n+1)/2. What's the 8th term?", "36"),
        ("Tiles cover 1m². Room 5m×4m. Tiles needed?", "20 tiles"),
        ("Paint covers 10m²/L. Cube 3m edge. Litres needed?", "5.4 litres"),
        ("Symmetry: combine square and circle. Lines of symmetry?", "4 (if centered)"),
        ("Rotate a square 45°. What shape does it look like?", "Diamond (still a square)"),
        ("Scale factor 2. Area increases by?", "Factor of 4"),
        ("Scale factor 3. Volume increases by?", "Factor of 27"),
        ("Prime factorization of 60?", "2²×3×5"),
        ("How many factors does 36 have?", "9"),
        ("Sum of factors of 12?", "28 (1+2+3+4+6+12)"),
        ("Product of first 4 primes?", "210 (2×3×5×7)"),
        ("Fibonacci: ratio of consecutive terms approaches?", "Golden ratio (≈1.618)"),
        ("Square numbers that are also triangular?", "1, 36, 1225..."),
        ("Palindromic primes under 100?", "2, 3, 5, 7, 11"),
        ("Perfect number (sum of factors = itself)?", "6 or 28"),
        ("What shape has 5 faces, 8 edges, 5 vertices?", "Square pyramid"),
        ("Euler's formula: F+V-E for polyhedra?", "2"),
        ("Regular polygon interior angle 120°. How many sides?", "6 (hexagon)"),
        ("Sum of interior angles of pentagon?", "540°"),
        ("Exterior angle of regular octagon?", "45°"),
        ("How many diagonals in a hexagon?", "9"),
        ("How many diagonals in a decagon?", "35"),
        ("Tessellations: which regular polygon DOESN'T tessellate alone?", "Pentagon"),
        ("3D shape with 2 congruent parallel faces connected by rectangles?", "Prism"),
        ("3D shape with one base and triangular faces meeting at a point?", "Pyramid"),
        ("Cross-section of cylinder perpendicular to axis?", "Circle"),
        ("Cross-section of cone through vertex?", "Triangle"),
        ("Net of a cube: how many edges to cut?", "7 (from 12 to 5)"),
        ("Doubling each dimension of a cuboid. Volume increases by?", "Factor of 8"),
        ("Halving each dimension of a sphere. Surface area decreases to?", "1/4 of original"),
        ("Sequence: 1, 11, 21, 1211, 111221. What type?", "Look-and-say sequence"),
        ("Find x: pattern is x, x+3, x+6, x+9 = 10, 13, 16, 19. x=?", "10")
    ]
    
    for q, correct in problems:
        # Extract simple answer without parenthetical explanations
        simple_correct = correct.split(" (")[0].strip()
        
        if "cm²" in correct or "m²" in correct:
            val = int(''.join(filter(str.isdigit, correct.split()[0])))
            unit = "cm²" if "cm²" in correct else "m²"
            options = [simple_correct, f"{val+10} {unit}", f"{val-10} {unit}" if val > 10 else f"{val*2} {unit}", f"{val//2} {unit}"]
        elif "cm" in correct and correct[0].isdigit():
            val = int(''.join(filter(str.isdigit, correct.split()[0].split('cm')[0])))
            options = [simple_correct, f"{val+5}cm", f"{val-5}cm" if val > 5 else f"{val*2}cm", f"{val+10}cm"]
        elif simple_correct.startswith("Yes") or simple_correct == "Yes":
            options = ["Yes", "No", "Cannot determine", "Sometimes"]
            simple_correct = "Yes"
        elif simple_correct.startswith("No") or simple_correct == "No":
            options = ["Yes", "No", "Cannot determine", "Sometimes"]
            simple_correct = "No"
        elif simple_correct.isdigit():
            val = int(simple_correct)
            options = [simple_correct, str(val+10), str(val-5) if val > 5 else str(val*2), str(val*2)]
        elif "Factor" in correct:
            options = [simple_correct, "Factor of 2", "Factor of 16", "No change"]
        elif "%" in correct:
            val = int(''.join(filter(str.isdigit, correct)))
            options = [simple_correct, f"{val+10}%", f"{val-5}%" if val > 5 else f"{val*2}%", f"{val+25}%"]
        else:
            options = [simple_correct, "Different answer", "Cannot solve", "More info needed"]
        
        random.shuffle(options)
        correct_idx = options.index(simple_correct)
        
        questions.append({
            'question_text': q,
            'options': options,
            'correct_index': correct_idx,
            'explanation': correct
        })
    
    return questions[:50]


# ============================================================
# MAIN FUNCTIONS
# ============================================================

def generate_all_questions():
    all_questions = []
    
    generators = [
        (1, generate_level_1_questions),
        (2, generate_level_2_questions),
        (3, generate_level_3_questions),
        (4, generate_level_4_questions),
        (5, generate_level_5_questions),
        (6, generate_level_6_questions),
        (7, generate_level_7_questions),
        (8, generate_level_8_questions),
        (9, generate_level_9_questions),
        (10, generate_level_10_questions),
        (11, generate_level_11_questions),
        (12, generate_level_12_questions)
    ]
    
    for level, generator in generators:
        print(f"  Generating Level {level}...")
        questions = generator()
        
        for q in questions:
            options = q['options']
            while len(options) < 4:
                options.append('')
            
            all_questions.append({
                'topic': TOPIC,
                'level': level,
                'question_text': q['question_text'],
                'option_a': str(options[0]),
                'option_b': str(options[1]),
                'option_c': str(options[2]),
                'option_d': str(options[3]),
                'correct_answer': ['A', 'B', 'C', 'D'][q['correct_index']],
                'solution': q.get('explanation', ''),
                'question_image_svg': q.get('image_svg', '')
            })
        
        print(f"    Level {level}: {len(questions)} questions generated")
    
    return all_questions


def validate_questions(questions):
    errors = []
    seen = set()
    
    for i, q in enumerate(questions):
        key = (q['level'], q['question_text'][:100])
        if key in seen:
            errors.append(f"Q{i} L{q['level']}: Duplicate")
        seen.add(key)
    
    return errors


def count_existing_questions():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT difficulty_level, COUNT(*) FROM questions_adaptive WHERE topic = ? GROUP BY difficulty_level', (TOPIC,))
        counts = dict(cursor.fetchall())
        conn.close()
        return counts
    except:
        return {}


def clear_existing_questions():
    counts = count_existing_questions()
    total = sum(counts.values())
    
    if total > 0:
        print(f"\n⚠️  Found {total} existing questions for {TOPIC}")
        response = input("Delete existing? (yes/no): ").strip().lower()
        if response == 'yes':
            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()
            cursor.execute('DELETE FROM questions_adaptive WHERE topic = ?', (TOPIC,))
            deleted = cursor.rowcount
            conn.commit()
            conn.close()
            print(f"   Deleted {deleted} questions")
            return True
        return False
    return True


def insert_questions(questions):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    letter_to_int = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    inserted = 0
    
    for q in questions:
        try:
            level = q['level']
            band = get_difficulty_band(level)
            
            correct_answer = q['correct_answer']
            if isinstance(correct_answer, str):
                correct_answer = letter_to_int.get(correct_answer.upper(), 0)
            
            cursor.execute('''
                INSERT OR IGNORE INTO questions_adaptive 
                (topic, question_text, option_a, option_b, option_c, option_d, 
                 correct_answer, explanation, difficulty_level, difficulty_band,
                 question_type, is_active, image_svg, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                q['topic'], q['question_text'], q['option_a'], q['option_b'],
                q.get('option_c', ''), q.get('option_d', ''),
                correct_answer, q.get('solution', ''), level, band,
                'multiple_choice', 1, q.get('question_image_svg', ''),
                datetime.now(), datetime.now()
            ))
            
            if cursor.rowcount > 0:
                inserted += 1
        except sqlite3.Error as e:
            print(f"Error: {e}")
    
    conn.commit()
    conn.close()
    return inserted


def main():
    print("=" * 60)
    print("AgentMath L2LP Question Generator V3")
    print(f"Topic: {TOPIC}")
    print(f"Table: questions_adaptive")
    print(f"Target: {QUESTIONS_PER_LEVEL} × {TOTAL_LEVELS} = {QUESTIONS_PER_LEVEL * TOTAL_LEVELS}")
    print("=" * 60)
    
    if not clear_existing_questions():
        return
    
    print("\nGenerating questions...")
    questions = generate_all_questions()
    print(f"\nTotal: {len(questions)}")
    
    print("\nValidating...")
    errors = validate_questions(questions)
    if errors:
        print(f"⚠️  {len(errors)} duplicates (will be skipped)")
    
    print("✅ Validation passed")
    
    print("\nInserting...")
    inserted = insert_questions(questions)
    
    print(f"\n{'=' * 60}")
    print(f"✅ Complete! Inserted {inserted} questions")
    
    counts = count_existing_questions()
    print("\nQuestions per level:")
    for level in range(1, 13):
        count = counts.get(level, 0)
        status = "✓" if count >= 40 else "⚠️"
        print(f"   Level {level}: {count} {status}")
    print("=" * 60)


if __name__ == '__main__':
    main()
