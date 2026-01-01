#!/usr/bin/env python3
"""
AgentMath - Simultaneous Equations Topic Generator v1
SEC Junior Cycle Mathematics - Adaptive Quiz System

Generates 600 questions (50 per level x 12 levels) for Simultaneous Equations topic.
Aligned with SEC Junior Cycle Mathematics Specification.

Level Structure:
  Level 1:  Understanding Systems - Visual Introduction (Foundation) - 75% visual
  Level 2:  Solving by Inspection/Tables (Foundation) - 75% visual
  Level 3:  Graphical Method Introduction (Foundation) - 75% visual
  Level 4:  Elimination - Same Coefficients (Ordinary)
  Level 5:  Elimination - Multiplying One Equation (Ordinary)
  Level 6:  Elimination - Multiplying Both Equations (Ordinary)
  Level 7:  Substitution Method - Simple (Higher)
  Level 8:  Substitution Method - Rearranging Required (Higher)
  Level 9:  Choosing the Best Method (Higher)
  Level 10: Word Problems - Setting Up Equations (Mastery)
  Level 11: Word Problems - Complete Solutions (Mastery)
  Level 12: Complex Applications & Problem Solving (Mastery)

SEC Reference Questions:
  - 2022 HL Q8: Solve simultaneous equations using elimination
  - 2023 HL Q7: Solve using substitution method
  - 2024 OL Q11: Form and solve simultaneous equations from word problem
  - 2024 HL Q9: Complex simultaneous equation application
  - 2025 OL Q8: Two equations, two unknowns

Author: AgentMath Generator
Version: 1.0
"""

import random
import sqlite3
import os

TOPIC = 'simultaneous_equations'
MODE = 'jc_exam'
QUESTIONS_PER_LEVEL = 50

IRISH_NAMES = ['Aoife', 'Ciara', 'Niamh', 'Saoirse', 'Orla', 'Siobhan', 'Aisling', 'Roisin',
               'Cian', 'Sean', 'Oisin', 'Conor', 'Liam', 'Darragh', 'Fionn', 'Eoin',
               'Caoimhe', 'Grainne', 'Maeve', 'Declan', 'Padraig', 'Tadhg', 'Cathal', 'Rory']

IRISH_PLACES = ['Dublin', 'Cork', 'Galway', 'Limerick', 'Waterford', 'Kilkenny', 'Sligo', 'Wexford']

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_unique_wrong_numbers(correct_val, exclude_vals, count=3):
    """Generate unique wrong number options avoiding correct and excluded values"""
    wrong = set()
    exclude_set = set(exclude_vals) if isinstance(exclude_vals, (list, tuple)) else {exclude_vals}
    exclude_set.add(correct_val)
    
    # Try nearby values first
    candidates = [correct_val + 1, correct_val - 1, correct_val + 2, correct_val - 2,
                  correct_val * 2, abs(correct_val) + 3]
    for c in candidates:
        if c > 0 and c not in exclude_set and c not in wrong and len(wrong) < count:
            wrong.add(c)
    
    # Fill with random if needed
    while len(wrong) < count:
        w = random.randint(1, max(15, correct_val + 5))
        if w not in exclude_set and w not in wrong:
            wrong.add(w)
    
    return [str(w) for w in list(wrong)[:count]]

def ensure_unique_options(correct, wrong_opts):
    """Ensure all 4 options are unique, return None if can't make unique"""
    options = [correct] + list(wrong_opts)[:3]
    if len(set(options)) != 4:
        return None
    return options

def make_options(correct, wrong_list):
    """Create 4 unique options with correct answer included"""
    correct_str = str(correct)
    # Filter out any wrong options that match the correct answer
    unique_wrong = [str(w) for w in wrong_list if str(w) != correct_str]
    # Remove duplicates from wrong list
    seen = set()
    unique_wrong = [w for w in unique_wrong if not (w in seen or seen.add(w))]
    
    options = [correct_str] + unique_wrong[:3]
    
    # If we don't have 4 unique options, generate more
    counter = 1
    while len(options) < 4:
        if '(' in correct_str and ',' in correct_str:
            # It's a coordinate pair, generate alternative coordinate
            filler = f"({counter + 10}, {counter + 5})"
        elif correct_str.isdigit() or (correct_str.startswith('-') and correct_str[1:].isdigit()):
            # It's a number
            filler = str(int(correct_str) + counter * 2)
        else:
            filler = f"Option {counter}"
        
        if filler not in options:
            options.append(filler)
        counter += 1
    
    random.shuffle(options)
    correct_idx = options.index(correct_str)
    return options, correct_idx


# ============================================================
# SVG GENERATORS - Visual representations for equations
# ============================================================

def generate_system_svg(eq1, eq2, highlight_var=None):
    """Generate visual for a system of two equations with bracket"""
    color1 = "#3b82f6"  # Blue
    color2 = "#8b5cf6"  # Purple
    svg = f'''<svg viewBox="0 0 220 80" width="220">
        <path d="M 15 10 Q 5 40 15 70" fill="none" stroke="#374151" stroke-width="2.5"/>
        <text x="30" y="32" font-size="15" fill="{color1}" font-weight="bold">{eq1}</text>
        <text x="30" y="60" font-size="15" fill="{color2}" font-weight="bold">{eq2}</text>
    </svg>'''
    return svg

def generate_elimination_step_svg(eq1, eq2, operation, result):
    """Generate visual showing elimination step"""
    svg = f'''<svg viewBox="0 0 280 100" width="280">
        <text x="20" y="25" font-size="13" fill="#3b82f6" font-weight="bold">{eq1}</text>
        <text x="20" y="50" font-size="13" fill="#8b5cf6" font-weight="bold">{eq2}</text>
        <text x="200" y="37" font-size="12" fill="#dc2626" font-weight="bold">{operation}</text>
        <line x1="20" y1="60" x2="180" y2="60" stroke="#374151" stroke-width="1"/>
        <text x="20" y="80" font-size="14" fill="#059669" font-weight="bold">{result}</text>
    </svg>'''
    return svg

def generate_substitution_svg(eq1, eq2, sub_expr):
    """Generate visual showing substitution step"""
    svg = f'''<svg viewBox="0 0 280 100" width="280">
        <text x="20" y="25" font-size="12" fill="#6b7280">From equation 1:</text>
        <text x="20" y="45" font-size="14" fill="#3b82f6" font-weight="bold">{eq1}</text>
        <text x="20" y="70" font-size="12" fill="#6b7280">Substitute into equation 2:</text>
        <text x="20" y="90" font-size="13" fill="#8b5cf6" font-weight="bold">{sub_expr}</text>
    </svg>'''
    return svg

def generate_graph_intersection_svg(x_sol, y_sol, eq1_label, eq2_label):
    """Generate visual showing two lines intersecting"""
    # Scale for display
    cx = 100 + x_sol * 15
    cy = 70 - y_sol * 10
    # Ensure within bounds
    cx = max(40, min(180, cx))
    cy = max(20, min(100, cy))
    
    svg = f'''<svg viewBox="0 0 220 120" width="220">
        <!-- Axes -->
        <line x1="30" y1="100" x2="200" y2="100" stroke="#9ca3af" stroke-width="1.5"/>
        <line x1="30" y1="10" x2="30" y2="100" stroke="#9ca3af" stroke-width="1.5"/>
        <text x="205" y="105" font-size="10" fill="#6b7280">x</text>
        <text x="25" y="8" font-size="10" fill="#6b7280">y</text>
        
        <!-- Line 1 (blue) -->
        <line x1="30" y1="90" x2="190" y2="30" stroke="#3b82f6" stroke-width="2"/>
        <text x="175" y="25" font-size="9" fill="#3b82f6">{eq1_label}</text>
        
        <!-- Line 2 (purple) -->
        <line x1="30" y1="40" x2="190" y2="85" stroke="#8b5cf6" stroke-width="2"/>
        <text x="175" y="95" font-size="9" fill="#8b5cf6">{eq2_label}</text>
        
        <!-- Intersection point -->
        <circle cx="{cx}" cy="{cy}" r="6" fill="#ef4444" stroke="white" stroke-width="2"/>
        <text x="{cx + 10}" y="{cy - 5}" font-size="10" fill="#dc2626" font-weight="bold">({x_sol}, {y_sol})</text>
    </svg>'''
    return svg

def generate_table_check_svg(x_val, y_val, eq1_check, eq2_check):
    """Generate visual showing table/check of solution"""
    svg = f'''<svg viewBox="0 0 260 90" width="260">
        <rect x="10" y="10" width="240" height="70" rx="8" fill="#f0fdf4" stroke="#22c55e" stroke-width="2"/>
        <text x="130" y="30" text-anchor="middle" font-size="12" fill="#166534" font-weight="bold">Check: x = {x_val}, y = {y_val}</text>
        <text x="30" y="55" font-size="11" fill="#3b82f6">Eq 1: {eq1_check} ✓</text>
        <text x="30" y="75" font-size="11" fill="#8b5cf6">Eq 2: {eq2_check} ✓</text>
    </svg>'''
    return svg

def generate_word_problem_svg(context, var1, var2):
    """Generate visual for word problem setup"""
    svg = f'''<svg viewBox="0 0 280 80" width="280">
        <rect x="5" y="5" width="270" height="70" rx="8" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
        <text x="140" y="25" text-anchor="middle" font-size="11" fill="#92400e" font-weight="bold">{context}</text>
        <text x="140" y="50" text-anchor="middle" font-size="12" fill="#1e40af">Let {var1} and {var2}</text>
        <text x="140" y="68" text-anchor="middle" font-size="10" fill="#6b7280">Form two equations</text>
    </svg>'''
    return svg

def generate_coins_svg(coin1_name, coin1_count, coin2_name, coin2_count):
    """Generate visual for coin/money problems"""
    svg = f'''<svg viewBox="0 0 280 70" width="280">
        <rect x="5" y="5" width="130" height="60" rx="8" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
        <text x="70" y="25" text-anchor="middle" font-size="11" fill="#92400e">{coin1_name}</text>
        <text x="70" y="45" text-anchor="middle" font-size="16" fill="#1e40af" font-weight="bold">{coin1_count}</text>
        
        <rect x="145" y="5" width="130" height="60" rx="8" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>
        <text x="210" y="25" text-anchor="middle" font-size="11" fill="#1e40af">{coin2_name}</text>
        <text x="210" y="45" text-anchor="middle" font-size="16" fill="#3b82f6" font-weight="bold">{coin2_count}</text>
    </svg>'''
    return svg

# ============================================================
# LEVEL 1: Understanding Systems - Visual Introduction
# Foundation level - 75% visual questions
# ============================================================

def generate_level_1(num_questions=50):
    """Level 1: Understanding Systems - Visual Introduction"""
    questions = []
    used_questions = set()
    
    question_types = [
        "identify_solution",
        "check_solution", 
        "count_equations",
        "identify_variables",
        "matching_system"
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 4:
        attempts += 1
        q_type = random.choice(question_types)
        
        # Generate simple integer solutions
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        
        # Generate coefficients for equations
        a1 = random.randint(1, 4)
        b1 = random.randint(1, 4)
        c1 = a1 * x + b1 * y
        
        a2 = random.randint(1, 4)
        b2 = random.randint(1, 4)
        # Ensure different equation
        while a1 * b2 == a2 * b1:  # Avoid parallel lines
            a2 = random.randint(1, 4)
            b2 = random.randint(1, 4)
        c2 = a2 * x + b2 * y
        
        eq1 = f"{a1}x + {b1}y = {c1}"
        eq2 = f"{a2}x + {b2}y = {c2}"
        
        # Ensure x and y are different enough
        while abs(x - y) < 2:
            y = random.randint(1, 8)
        
        if q_type == "identify_solution":
            question_text = f"For {eq1} and {eq2}, which point is the solution?"
            visual = generate_system_svg(eq1, eq2)
            
            correct = f"({x}, {y})"
            wrong_opts = [f"({y}, {x})", f"({x + 2}, {y - 1})", f"({x - 2}, {y + 1})"]
            
            explanation = f"Substituting x = {x}, y = {y}:\\nEq 1: {a1}({x}) + {b1}({y}) = {a1*x} + {b1*y} = {c1} ✓\\nEq 2: {a2}({x}) + {b2}({y}) = {a2*x} + {b2*y} = {c2} ✓"
            
        elif q_type == "check_solution":
            # Give a solution and ask if it works
            works = random.choice([True, False])
            if works:
                test_x, test_y = x, y
                question_text = f"For {eq1} and {eq2}: does ({test_x}, {test_y}) satisfy both?"
                correct = "Yes, it satisfies both"
            else:
                test_x = x + random.choice([-2, 2])
                test_y = y
                question_text = f"For {eq1} and {eq2}: does ({test_x}, {test_y}) satisfy both?"
                correct = "No, it does not satisfy both"
            
            visual = generate_system_svg(eq1, eq2)
            wrong_opts = ["Yes, it satisfies both" if not works else "No, it does not satisfy both",
                         "Only satisfies the first equation",
                         "Only satisfies the second equation"]
            
            check1 = a1 * test_x + b1 * test_y
            check2 = a2 * test_x + b2 * test_y
            explanation = f"Check ({test_x}, {test_y}):\\nEq 1: {a1}({test_x}) + {b1}({test_y}) = {check1} {'= ' + str(c1) + ' ✓' if check1 == c1 else '≠ ' + str(c1) + ' ✗'}\\nEq 2: {a2}({test_x}) + {b2}({test_y}) = {check2} {'= ' + str(c2) + ' ✓' if check2 == c2 else '≠ ' + str(c2) + ' ✗'}"
            
        elif q_type == "count_equations":
            question_text = f"The system {eq1} and {eq2} has how many equations?"
            visual = generate_system_svg(eq1, eq2)
            correct = "2"
            wrong_opts = ["1", "3", "4"]
            explanation = "A system of simultaneous equations has 2 or more equations that must be solved together. To find 2 unknowns (x and y), we need at least 2 equations."
            
        elif q_type == "identify_variables":
            question_text = f"In the system {eq1} and {eq2}, what are the unknowns?"
            visual = generate_system_svg(eq1, eq2)
            correct = "x and y"
            wrong_opts = [f"{c1} and {c2}", f"{a1} and {b1}", "Only x"]
            explanation = f"The variables are the letters we need to find values for. In this system, x and y are unknowns. The numbers ({a1}, {b1}, {c1}, etc.) are coefficients and constants."
            
        else:  # matching_system
            question_text = f"Which system has solution x = {x}, y = {y}?"
            visual = None  # No visual for this one
            
            # Correct system
            correct = f"{eq1} and {eq2}"
            
            # Wrong systems (different solutions)
            x2, y2 = x + 2, y + 2
            w_c1 = a1 * x2 + b1 * y2
            w_c2 = a2 * x2 + b2 * y2
            wrong1 = f"{a1}x + {b1}y = {w_c1} and {a2}x + {b2}y = {w_c2}"
            
            x3, y3 = x - 2, y + 1
            w_c3 = a1 * x3 + b1 * y3
            w_c4 = a2 * x3 + b2 * y3
            wrong2 = f"{a1}x + {b1}y = {w_c3} and {a2}x + {b2}y = {w_c4}"
            
            wrong3 = f"{a1}x + {b1}y = {c1 + 5} and {a2}x + {b2}y = {c2 + 3}"
            wrong_opts = [wrong1, wrong2, wrong3]
            explanation = f"Substitute x = {x}, y = {y} into each system to check which gives true statements for both equations."
        
        q_key = f"{q_type}_{eq1}_{eq2}"
        if q_key in used_questions:
            continue
        
        # Also check for unique question_text
        if question_text in used_questions:
            continue
        
        used_questions.add(q_key)
        used_questions.add(question_text)
        
        options = ensure_unique_options(correct, wrong_opts)
        if options is None:
            continue
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 2: Solving by Inspection/Tables
# Foundation level - 75% visual questions
# ============================================================

def generate_level_2(num_questions=50):
    """Level 2: Solving by Inspection/Tables"""
    questions = []
    used_questions = set()
    question_counter = 0
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 6:
        attempts += 1
        
        # Simple solutions for inspection - ensure x != y and good separation
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        while y == x or abs(x - y) < 2:
            y = random.randint(1, 8)
        
        # Simple coefficients
        eq_type = random.choice(['simple', 'one_coeff', 'x_plus_y'])
        
        if eq_type == 'simple':
            # x + y = ? and x - y = ? (when x > y)
            if x <= y:
                x, y = y + 1, x
            sum_val = x + y
            diff_val = x - y
            eq1 = f"x + y = {sum_val}"
            eq2 = f"x - y = {diff_val}"
            explanation = f"From x + y = {sum_val} and x - y = {diff_val}:\\nAdding: 2x = {sum_val + diff_val}, so x = {x}\\nThen y = {sum_val} - {x} = {y}"
            
        elif eq_type == 'one_coeff':
            # x + 2y = ? and x + y = ?
            c1 = x + 2 * y
            c2 = x + y
            eq1 = f"x + 2y = {c1}"
            eq2 = f"x + y = {c2}"
            explanation = f"Subtracting Eq 2 from Eq 1:\\n(x + 2y) - (x + y) = {c1} - {c2}\\ny = {y}\\nThen x = {c2} - {y} = {x}"
            
        else:  # x_plus_y
            # 2x + y = ? and x + y = ?
            c1 = 2 * x + y
            c2 = x + y
            eq1 = f"2x + y = {c1}"
            eq2 = f"x + y = {c2}"
            explanation = f"Subtracting Eq 2 from Eq 1:\\n(2x + y) - (x + y) = {c1} - {c2}\\nx = {x}\\nThen y = {c2} - {x} = {y}"
        
        q_style = random.choice(['find_x', 'find_y', 'find_both', 'table_check'])
        
        # Generate unique wrong options
        def get_unique_wrong_numbers(correct_val, other_val, count=3):
            """Generate unique wrong options avoiding correct and other value"""
            wrong = set()
            candidates = [correct_val + 1, correct_val - 1, correct_val + 2, correct_val - 2, 
                          other_val + 1, other_val - 1, correct_val * 2, abs(correct_val - other_val)]
            for c in candidates:
                if c > 0 and c != correct_val and c != other_val and len(wrong) < count:
                    wrong.add(c)
            while len(wrong) < count:
                w = random.randint(1, 15)
                if w != correct_val and w != other_val:
                    wrong.add(w)
            return list(wrong)[:count]
        
        question_counter += 1
        
        if q_style == 'find_x':
            question_text = f"Find the value of x:\n{eq1}\n{eq2}"
            correct = str(x)
            wrong_nums = get_unique_wrong_numbers(x, y)
            wrong_opts = [str(w) for w in wrong_nums]
        elif q_style == 'find_y':
            question_text = f"Find the value of y:\n{eq1}\n{eq2}"
            correct = str(y)
            wrong_nums = get_unique_wrong_numbers(y, x)
            wrong_opts = [str(w) for w in wrong_nums]
        elif q_style == 'find_both':
            question_text = f"Solve this system:\n{eq1}\n{eq2}"
            correct = f"x = {x}, y = {y}"
            # Ensure unique wrong options
            w1 = f"x = {y}, y = {x}" if x != y else f"x = {x+1}, y = {y+1}"
            w2 = f"x = {x + 2}, y = {max(1, y - 1)}"
            w3 = f"x = {max(1, x - 1)}, y = {y + 2}"
            wrong_opts = [w1, w2, w3]
        else:  # table_check
            question_text = f"Use inspection to solve:\n{eq1}\n{eq2}"
            correct = f"x = {x}, y = {y}"
            w1 = f"x = {x + 1}, y = {y + 1}"
            w2 = f"x = {max(1, x - 1)}, y = {max(1, y - 1)}" if (x > 1 and y > 1 and (x-1 != y-1 or x-1 != x)) else f"x = {x + 2}, y = {y}"
            w3 = f"x = {y}, y = {x}" if x != y else f"x = {x + 3}, y = {y + 3}"
            wrong_opts = [w1, w2, w3]
        
        visual = generate_system_svg(eq1, eq2)
        
        q_key = f"{eq1}_{eq2}_{q_style}_{x}_{y}"
        if q_key in used_questions:
            continue
        used_questions.add(q_key)
        
        # Ensure all options are unique
        options = [correct] + wrong_opts[:3]
        if len(set(options)) != 4:
            # Try to fix duplicate options
            unique_opts = list(set(options))
            while len(unique_opts) < 4:
                if correct.isdigit():
                    new_val = int(correct) + len(unique_opts) + random.randint(2, 5)
                    new_opt = str(new_val)
                else:
                    new_opt = f"x = {random.randint(1,10)}, y = {random.randint(1,10)}"
                if new_opt not in unique_opts:
                    unique_opts.append(new_opt)
            options = unique_opts[:4]
            
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 3: Graphical Method Introduction
# Foundation level - 75% visual questions
# ============================================================

def generate_level_3(num_questions=50):
    """Level 3: Graphical Method Introduction"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 8:
        attempts += 1
        
        # Solutions that display nicely on a graph - ensure x != y
        x = random.randint(1, 5)
        y = random.randint(1, 5)
        while y == x:
            y = random.randint(1, 5)
        
        # Create equations with nice graph representations
        a1, b1 = random.randint(1, 3), random.randint(1, 3)
        c1 = a1 * x + b1 * y
        
        a2, b2 = random.randint(1, 3), random.randint(1, 3)
        while a1 * b2 == a2 * b1:  # Avoid parallel
            a2 = random.randint(1, 3)
        c2 = a2 * x + b2 * y
        
        eq1 = f"{a1}x + {b1}y = {c1}"
        eq2 = f"{a2}x + {b2}y = {c2}"
        
        q_style = random.choice(['intersection', 'read_coords', 'meaning', 'verify_graph'])
        
        if q_style == 'intersection':
            question_text = f"At what point do the two lines intersect?\n{eq1}\n{eq2}"
            visual = generate_graph_intersection_svg(x, y, "Line 1", "Line 2")
            correct = f"({x}, {y})"
            # Ensure unique wrong options
            w1 = f"({y}, {x})" if x != y else f"({x+2}, {y+2})"
            w2 = f"({x + 1}, {y})" if x + 1 != y else f"({x + 2}, {y})"
            w3 = f"({x}, {y + 1})" if y + 1 != x else f"({x}, {y + 2})"
            wrong_opts = [w1, w2, w3]
            explanation = f"The intersection point is where both lines cross. Reading from the graph: ({x}, {y}). This point satisfies both equations."
            
        elif q_style == 'read_coords':
            question_text = f"The solution to a system is where the lines intersect. What is the x-coordinate of the solution?\n{eq1}\n{eq2}"
            visual = generate_graph_intersection_svg(x, y, eq1[:10], eq2[:10])
            correct = str(x)
            # Ensure unique wrong options
            wrong_set = set()
            for v in [y, x + 1, x - 1 if x > 1 else x + 2, x + 2, y + 1, y - 1 if y > 1 else y + 2]:
                if v != x and v > 0:
                    wrong_set.add(str(v))
            wrong_opts = list(wrong_set)[:3]
            while len(wrong_opts) < 3:
                wrong_opts.append(str(x + len(wrong_opts) + 2))
            explanation = f"The intersection point is ({x}, {y}). The x-coordinate is {x}."
            
        elif q_style == 'meaning':
            question_text = f"For {eq1} and {eq2}: what does the intersection point represent?"
            visual = generate_graph_intersection_svg(x, y, "Eq 1", "Eq 2")
            correct = "The solution that satisfies both equations"
            wrong_opts = ["The average of both equations", "The point where y = 0", "The point where x = 0"]
            explanation = "The intersection point is the (x, y) pair that makes both equations true simultaneously. It's the solution to the system."
            
        else:  # verify_graph
            question_text = f"A graph shows intersection at ({x}, {y}). Which system could this solve?"
            visual = generate_graph_intersection_svg(x, y, "", "")
            correct = f"{eq1} and {eq2}"
            
            # Create wrong systems
            wx, wy = x + 1, y + 1
            w_c1 = a1 * wx + b1 * wy
            w_c2 = a2 * wx + b2 * wy
            wrong_opts = [
                f"{a1}x + {b1}y = {w_c1} and {a2}x + {b2}y = {w_c2}",
                f"{a1}x + {b1}y = {c1 + 2} and {a2}x + {b2}y = {c2}",
                f"{a1}x + {b1}y = {c1} and {a2}x + {b2}y = {c2 + 3}"
            ]
            explanation = f"Substitute ({x}, {y}) into each system. Only the correct answer gives true statements for both equations."
        
        q_key = f"{q_style}_{x}_{y}_{eq1}_{eq2}"
        if q_key in used_questions:
            continue
        
        # Also check for unique question_text
        if question_text in used_questions:
            continue
        
        used_questions.add(q_key)
        used_questions.add(question_text)
        
        # Ensure all options are unique
        options = [correct] + wrong_opts[:3]
        if len(set(options)) != 4:
            continue  # Skip if duplicate options
            
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 4: Elimination - Same Coefficients
# Ordinary level
# ============================================================

def generate_level_4(num_questions=50):
    """Level 4: Elimination - Same Coefficients"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 4:
        attempts += 1
        
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        
        # Create equations where one coefficient is the same
        style = random.choice(['same_x', 'same_y', 'same_x_sub', 'same_y_sub'])
        
        if style == 'same_x':
            # Same x coefficient, add to eliminate
            a = random.randint(1, 4)
            b1 = random.randint(1, 4)
            b2 = -b1  # Opposite y coefficients
            c1 = a * x + b1 * y
            c2 = a * x + b2 * y
            eq1 = f"{a}x + {b1}y = {c1}"
            eq2 = f"{a}x - {b1}y = {c2}"
            operation = "Add equations"
            result_eq = f"{2*a}x = {c1 + c2}"
            explanation = f"Adding equations:\\n{a}x + {b1}y + {a}x - {b1}y = {c1} + {c2}\\n{2*a}x = {c1 + c2}\\nx = {x}\\nSubstitute: y = {y}"
            
        elif style == 'same_y':
            # Same y coefficient, subtract to eliminate
            a1 = random.randint(2, 5)
            a2 = random.randint(1, 4)
            if a1 == a2:
                a2 = a1 + 1
            b = random.randint(1, 4)
            c1 = a1 * x + b * y
            c2 = a2 * x + b * y
            eq1 = f"{a1}x + {b}y = {c1}"
            eq2 = f"{a2}x + {b}y = {c2}"
            operation = "Subtract equations"
            result_eq = f"{a1 - a2}x = {c1 - c2}"
            explanation = f"Subtracting Eq 2 from Eq 1:\\n({a1}x + {b}y) - ({a2}x + {b}y) = {c1} - {c2}\\n{a1 - a2}x = {c1 - c2}\\nx = {x}\\nSubstitute: y = {y}"
            
        elif style == 'same_x_sub':
            # Same x coefficient, subtract
            a = random.randint(2, 4)
            b1 = random.randint(2, 4)
            b2 = random.randint(1, 3)
            if b1 == b2:
                b2 = b1 + 1
            c1 = a * x + b1 * y
            c2 = a * x + b2 * y
            eq1 = f"{a}x + {b1}y = {c1}"
            eq2 = f"{a}x + {b2}y = {c2}"
            operation = "Subtract equations"
            result_eq = f"{b1 - b2}y = {c1 - c2}"
            explanation = f"Subtracting Eq 2 from Eq 1:\\n{b1 - b2}y = {c1 - c2}\\ny = {y}\\nSubstitute back: x = {x}"
            
        else:  # same_y_sub
            a1 = random.randint(2, 5)
            a2 = random.randint(1, 4)
            b = random.randint(1, 4)
            c1 = a1 * x + b * y
            c2 = a2 * x - b * y
            eq1 = f"{a1}x + {b}y = {c1}"
            eq2 = f"{a2}x - {b}y = {c2}"
            operation = "Add equations"
            result_eq = f"{a1 + a2}x = {c1 + c2}"
            explanation = f"Adding equations eliminates y:\\n{a1 + a2}x = {c1 + c2}\\nx = {x}\\nSubstitute: y = {y}"
        
        q_style = random.choice(['solve_x', 'solve_y', 'solve_both', 'identify_operation'])
        
        # Ensure x and y are different enough
        while abs(x - y) < 2:
            y = random.randint(1, 10)
        
        if q_style == 'solve_x':
            question_text = f"Given {eq1} and {eq2}, solve for x using elimination:"
            correct = str(x)
            wrong_opts = get_unique_wrong_numbers(x, [y])
        elif q_style == 'solve_y':
            question_text = f"Given {eq1} and {eq2}, solve for y using elimination:"
            correct = str(y)
            wrong_opts = get_unique_wrong_numbers(y, [x])
        elif q_style == 'solve_both':
            question_text = f"Solve using elimination: {eq1} and {eq2}"
            correct = f"x = {x}, y = {y}"
            wrong_opts = [f"x = {y}, y = {x}", f"x = {x + 2}, y = {y - 2}", f"x = {x - 2}, y = {y + 2}"]
        else:  # identify_operation
            question_text = f"For {eq1} and {eq2}, what operation eliminates a variable?"
            correct = operation
            if "Add" in operation:
                wrong_opts = ["Subtract equations", "Multiply by 2", "Divide both"]
            else:
                wrong_opts = ["Add equations", "Multiply by 2", "Divide both"]
        
        visual = generate_system_svg(eq1, eq2)
        
        q_key = f"{eq1}_{eq2}_{q_style}"
        if q_key in used_questions:
            continue
        used_questions.add(q_key)
        
        options = ensure_unique_options(correct, wrong_opts)
        if options is None:
            continue
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 5: Elimination - Multiplying One Equation
# Ordinary level
# ============================================================

def generate_level_5(num_questions=50):
    """Level 5: Elimination - Multiplying One Equation"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 4:
        attempts += 1
        
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        
        # Create equations where multiplying one makes coefficients match
        multiplier = random.randint(2, 3)
        
        style = random.choice(['mult_first', 'mult_second'])
        
        if style == 'mult_first':
            # Multiply first equation
            a1 = random.randint(1, 3)
            b1 = random.randint(1, 3)
            a2 = a1 * multiplier
            b2 = random.randint(1, 4)
            if b1 == b2:
                b2 = b1 + 1
        else:
            # Multiply second equation
            a1 = random.randint(2, 4) * multiplier
            b1 = random.randint(1, 4)
            a2 = random.randint(2, 4)
            b2 = random.randint(1, 3)
            
        c1 = a1 * x + b1 * y
        c2 = a2 * x + b2 * y
        
        eq1 = f"{a1}x + {b1}y = {c1}"
        eq2 = f"{a2}x + {b2}y = {c2}"
        
        if style == 'mult_first':
            mult_eq = f"Multiply Eq 1 by {multiplier}: {a1*multiplier}x + {b1*multiplier}y = {c1*multiplier}"
            explanation = f"{mult_eq}\\nNow coefficients of x match.\\nSubtract to eliminate x:\\n{b1*multiplier - b2}y = {c1*multiplier - c2}\\ny = {y}\\nSubstitute: x = {x}"
        else:
            mult_eq = f"Multiply Eq 2 by {multiplier}: {a2*multiplier}x + {b2*multiplier}y = {c2*multiplier}"
            explanation = f"{mult_eq}\\nNow coefficients of x match.\\nSubtract to eliminate x:\\n{b1 - b2*multiplier}y = {c1 - c2*multiplier}\\ny = {y}\\nSubstitute: x = {x}"
        
        q_style = random.choice(['solve_both', 'find_multiplier', 'solve_x', 'solve_y'])
        
        # Ensure x and y are different enough
        while abs(x - y) < 2:
            y = random.randint(1, 8)
        
        if q_style == 'solve_both':
            question_text = f"Solve {eq1} and {eq2} using elimination:"
            correct = f"x = {x}, y = {y}"
            wrong_opts = [f"x = {y}, y = {x}", f"x = {x + 2}, y = {y - 1}", f"x = {x - 1}, y = {y + 2}"]
        elif q_style == 'find_multiplier':
            question_text = f"For {eq1} and {eq2}: to eliminate x, multiply {'Eq 1' if style == 'mult_first' else 'Eq 2'} by?"
            correct = str(multiplier)
            wrong_opts = get_unique_wrong_numbers(multiplier, [])
        elif q_style == 'solve_x':
            question_text = f"For {eq1} and {eq2}, solve for x:"
            correct = str(x)
            wrong_opts = get_unique_wrong_numbers(x, [y])
        else:
            question_text = f"For {eq1} and {eq2}, solve for y:"
            correct = str(y)
            wrong_opts = get_unique_wrong_numbers(y, [x])
        
        visual = generate_system_svg(eq1, eq2)
        
        q_key = f"{eq1}_{eq2}_{q_style}"
        if q_key in used_questions:
            continue
        used_questions.add(q_key)
        
        options = ensure_unique_options(correct, wrong_opts)
        if options is None:
            continue
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 6: Elimination - Multiplying Both Equations
# Ordinary level
# ============================================================

def generate_level_6(num_questions=50):
    """Level 6: Elimination - Multiplying Both Equations"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 4:
        attempts += 1
        
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        
        # Coefficients that require multiplying both equations
        # Ensure they're not already matching and not multiples
        valid = False
        inner_attempts = 0
        while not valid and inner_attempts < 50:
            inner_attempts += 1
            a1 = random.randint(2, 4)
            b1 = random.randint(2, 4)
            a2 = random.randint(2, 4)
            b2 = random.randint(2, 4)
            
            # Check conditions: different coefficients, not multiples of each other
            if a1 != a2 and b1 != b2 and a1 % a2 != 0 and a2 % a1 != 0:
                valid = True
        
        if not valid:
            continue
            
        c1 = a1 * x + b1 * y
        c2 = a2 * x + b2 * y
        
        eq1 = f"{a1}x + {b1}y = {c1}"
        eq2 = f"{a2}x + {b2}y = {c2}"
        
        # Find LCM for elimination
        import math
        lcm_a = (a1 * a2) // math.gcd(a1, a2)
        m1 = lcm_a // a1
        m2 = lcm_a // a2
        
        explanation = f"Multiply Eq 1 by {m1}: {a1*m1}x + {b1*m1}y = {c1*m1}\\nMultiply Eq 2 by {m2}: {a2*m2}x + {b2*m2}y = {c2*m2}\\nSubtract to eliminate x:\\n{b1*m1 - b2*m2}y = {c1*m1 - c2*m2}\\ny = {y}\\nSubstitute: x = {x}"
        
        q_style = random.choice(['solve_both', 'multipliers', 'solve_x', 'solve_y'])
        
        # Ensure x and y are different enough
        while abs(x - y) < 2:
            y = random.randint(1, 7)
        
        if q_style == 'solve_both':
            question_text = f"Solve {eq1} and {eq2} by elimination:"
            correct = f"x = {x}, y = {y}"
            wrong_opts = [f"x = {y}, y = {x}", f"x = {x + 2}, y = {y - 1}", f"x = {x - 1}, y = {y + 2}"]
        elif q_style == 'multipliers':
            question_text = f"For {eq1} and {eq2}, to eliminate x multiply equations by:"
            correct = f"{m1} and {m2}"
            wrong_opts = [f"{m2} and {m1}", f"{m1 + 1} and {m2 - 1}" if m2 > 1 else f"{m1 + 1} and {m2 + 1}", f"{a1} and {a2}"]
        elif q_style == 'solve_x':
            question_text = f"For {eq1} and {eq2}, solve for x:"
            correct = str(x)
            wrong_opts = get_unique_wrong_numbers(x, [y])
        else:
            question_text = f"For {eq1} and {eq2}, solve for y:"
            correct = str(y)
            wrong_opts = get_unique_wrong_numbers(y, [x])
        
        visual = generate_system_svg(eq1, eq2)
        
        q_key = f"{eq1}_{eq2}_{q_style}"
        if q_key in used_questions:
            continue
        used_questions.add(q_key)
        
        options = ensure_unique_options(correct, wrong_opts)
        if options is None:
            continue
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 7: Substitution Method - Simple
# Higher level
# ============================================================

def generate_level_7(num_questions=50):
    """Level 7: Substitution Method - Simple"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 4:
        attempts += 1
        
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        
        # Create equations where one is already solved for a variable
        style = random.choice(['y_equals', 'x_equals'])
        
        if style == 'y_equals':
            # y = mx + c form
            m = random.randint(1, 3)
            c = y - m * x
            eq1 = f"y = {m}x + {c}" if c >= 0 else f"y = {m}x - {-c}"
            
            a = random.randint(1, 3)
            b = random.randint(1, 3)
            c2 = a * x + b * y
            eq2 = f"{a}x + {b}y = {c2}"
            
            sub_expr = f"{a}x + {b}({m}x + {c}) = {c2}" if c >= 0 else f"{a}x + {b}({m}x - {-c}) = {c2}"
            explanation = f"Substitute y = {m}x + {c} into Eq 2:\\n{sub_expr}\\n{a}x + {b*m}x + {b*c} = {c2}\\n{a + b*m}x = {c2 - b*c}\\nx = {x}\\nThen y = {m}({x}) + {c} = {y}"
            
        else:  # x_equals
            m = random.randint(1, 3)
            c = x - m * y
            eq1 = f"x = {m}y + {c}" if c >= 0 else f"x = {m}y - {-c}"
            
            a = random.randint(1, 3)
            b = random.randint(1, 3)
            c2 = a * x + b * y
            eq2 = f"{a}x + {b}y = {c2}"
            
            sub_expr = f"{a}({m}y + {c}) + {b}y = {c2}" if c >= 0 else f"{a}({m}y - {-c}) + {b}y = {c2}"
            explanation = f"Substitute x = {m}y + {c} into Eq 2:\\n{sub_expr}\\n{a*m}y + {a*c} + {b}y = {c2}\\n{a*m + b}y = {c2 - a*c}\\ny = {y}\\nThen x = {m}({y}) + {c} = {x}"
        
        q_style = random.choice(['solve_both', 'solve_x', 'solve_y', 'substitute'])
        
        # Ensure x and y are different enough
        while abs(x - y) < 2:
            y = random.randint(1, 8)
        
        if q_style == 'solve_both':
            question_text = f"Solve {eq1} and {eq2} using substitution:"
            correct = f"x = {x}, y = {y}"
            wrong_opts = [f"x = {y}, y = {x}", f"x = {x + 2}, y = {y - 1}", f"x = {x - 1}, y = {y + 2}"]
        elif q_style == 'solve_x':
            question_text = f"For {eq1} and {eq2}, solve for x:"
            correct = str(x)
            wrong_opts = get_unique_wrong_numbers(x, [y])
        elif q_style == 'solve_y':
            question_text = f"For {eq1} and {eq2}, solve for y:"
            correct = str(y)
            wrong_opts = get_unique_wrong_numbers(y, [x])
        else:  # substitute
            question_text = f"For {eq1} and {eq2}, what expression do you substitute?"
            if style == 'y_equals':
                correct = f"y = {m}x + {c}" if c >= 0 else f"y = {m}x - {-c}"
            else:
                correct = f"x = {m}y + {c}" if c >= 0 else f"x = {m}y - {-c}"
            wrong_opts = [f"x = {c}", f"y = {c}", f"x + y = {x + y}"]
        
        visual = generate_system_svg(eq1, eq2)
        
        q_key = f"{eq1}_{eq2}_{q_style}"
        if q_key in used_questions:
            continue
        used_questions.add(q_key)
        
        options = ensure_unique_options(correct, wrong_opts)
        if options is None:
            continue
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 8: Substitution Method - Rearranging Required
# Higher level
# ============================================================

def generate_level_8(num_questions=50):
    """Level 8: Substitution Method - Rearranging Required"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 4:
        attempts += 1
        
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        
        # Create equations where neither is pre-solved
        a1 = random.randint(1, 2)
        b1 = random.randint(1, 3)
        c1 = a1 * x + b1 * y
        
        a2 = random.randint(2, 4)
        b2 = random.randint(1, 3)
        c2 = a2 * x + b2 * y
        
        # Ensure different equations
        while a1 * b2 == a2 * b1:
            a2 = random.randint(2, 4)
        
        eq1 = f"{a1}x + {b1}y = {c1}"
        eq2 = f"{a2}x + {b2}y = {c2}"
        
        # Rearrange eq1 to solve for x
        # a1*x = c1 - b1*y
        # x = (c1 - b1*y) / a1
        
        if a1 == 1:
            rearranged = f"x = {c1} - {b1}y"
            explanation = f"From Eq 1: x = {c1} - {b1}y\\nSubstitute into Eq 2:\\n{a2}({c1} - {b1}y) + {b2}y = {c2}\\n{a2*c1} - {a2*b1}y + {b2}y = {c2}\\n{b2 - a2*b1}y = {c2 - a2*c1}\\ny = {y}\\nThen x = {c1} - {b1}({y}) = {x}"
        else:
            rearranged = f"{a1}x = {c1} - {b1}y"
            explanation = f"From Eq 1: {a1}x = {c1} - {b1}y, so x = ({c1} - {b1}y)/{a1}\\nSubstitute into Eq 2 and solve.\\nSolution: x = {x}, y = {y}"
        
        q_style = random.choice(['solve_both', 'rearrange', 'solve_x', 'solve_y'])
        
        # Ensure x and y are different enough
        while abs(x - y) < 2:
            y = random.randint(1, 7)
        
        if q_style == 'solve_both':
            question_text = f"Solve {eq1} and {eq2} using substitution:"
            correct = f"x = {x}, y = {y}"
            wrong_opts = [f"x = {y}, y = {x}", f"x = {x + 2}, y = {y - 1}", f"x = {x - 1}, y = {y + 2}"]
        elif q_style == 'rearrange':
            question_text = f"For {eq1}, rearrange to make x the subject:"
            correct = rearranged
            wrong_opts = [f"x = {c1} + {b1}y", f"x = {b1}y - {c1}", f"y = {c1} - {a1}x"]
        elif q_style == 'solve_x':
            question_text = f"For {eq1} and {eq2}, solve for x:"
            correct = str(x)
            wrong_opts = get_unique_wrong_numbers(x, [y])
        else:
            question_text = f"For {eq1} and {eq2}, solve for y:"
            correct = str(y)
            wrong_opts = get_unique_wrong_numbers(y, [x])
        
        visual = generate_system_svg(eq1, eq2)
        
        q_key = f"{eq1}_{eq2}_{q_style}_{x}_{y}"
        if q_key in used_questions:
            continue
        
        # Also check for unique question_text
        if question_text in used_questions:
            continue
        
        used_questions.add(q_key)
        used_questions.add(question_text)
        
        options = ensure_unique_options(correct, wrong_opts)
        if options is None:
            continue
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 9: Choosing the Best Method
# Higher level
# ============================================================

def generate_level_9(num_questions=50):
    """Level 9: Choosing the Best Method"""
    questions = []
    used_questions = set()
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 8:
        attempts += 1
        
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        
        # Create different equation styles to test method choice
        method_type = random.choice(['elimination_obvious', 'substitution_obvious', 'either_works', 'identify_method'])
        
        if method_type == 'elimination_obvious':
            # Equations with same coefficient - elimination best
            a = random.randint(1, 3)
            b1 = random.randint(1, 4)
            b2 = random.randint(1, 4)
            if b1 == b2:
                b2 = b1 + 1
            c1 = a * x + b1 * y
            c2 = a * x + b2 * y
            eq1 = f"{a}x + {b1}y = {c1}"
            eq2 = f"{a}x + {b2}y = {c2}"
            best_method = "Elimination"
            reason = "Both equations have the same x coefficient"
            explanation = f"Elimination is best because both equations have {a}x.\\nSubtract: {b1 - b2}y = {c1 - c2}\\ny = {y}, then x = {x}"
            
        elif method_type == 'substitution_obvious':
            # One equation already solved for a variable
            m = random.randint(1, 2)
            c = y - m * x
            eq1 = f"y = {m}x + {c}" if c >= 0 else f"y = {m}x - {-c}"
            a = random.randint(1, 3)
            b = random.randint(1, 3)
            c2 = a * x + b * y
            eq2 = f"{a}x + {b}y = {c2}"
            best_method = "Substitution"
            reason = "One equation is already solved for y"
            explanation = f"Substitution is best because y is already isolated.\\nSubstitute y = {m}x + {c} into Eq 2.\\nSolution: x = {x}, y = {y}"
            
        else:  # either_works or identify_method
            a1, b1 = random.randint(1, 3), random.randint(1, 3)
            a2, b2 = random.randint(1, 3), random.randint(1, 3)
            c1 = a1 * x + b1 * y
            c2 = a2 * x + b2 * y
            eq1 = f"{a1}x + {b1}y = {c1}"
            eq2 = f"{a2}x + {b2}y = {c2}"
            best_method = "Either method"
            reason = "No obvious advantage to either method"
            explanation = f"Both methods work. Using elimination or substitution:\\nSolution: x = {x}, y = {y}"
        
        q_style = random.choice(['solve', 'choose_method', 'explain_choice'])
        
        # Ensure x and y are different enough
        while abs(x - y) < 2:
            y = random.randint(1, 8)
        
        if q_style == 'solve':
            question_text = f"Solve {eq1} and {eq2} efficiently:"
            correct = f"x = {x}, y = {y}"
            wrong_opts = [f"x = {y}, y = {x}", f"x = {x + 2}, y = {y - 1}", f"x = {x - 1}, y = {y + 2}"]
        elif q_style == 'choose_method':
            question_text = f"For {eq1} and {eq2}, which method is best?"
            correct = best_method
            if best_method == "Elimination":
                wrong_opts = ["Substitution", "Graphical method", "Trial and error"]
            elif best_method == "Substitution":
                wrong_opts = ["Elimination", "Graphical method", "Trial and error"]
            else:
                wrong_opts = ["Only elimination works", "Only substitution works", "Graphical only"]
                correct = "Both methods work equally"
        else:  # explain_choice
            question_text = f"For {eq1} and {eq2}: why is {best_method.lower()} efficient?"
            correct = reason
            wrong_opts = ["The coefficients are all prime", "The constants are even", "The variables are alphabetical"]
        
        visual = generate_system_svg(eq1, eq2)
        
        q_key = f"{eq1}_{eq2}_{q_style}_{method_type}"
        if q_key in used_questions:
            continue
        used_questions.add(q_key)
        
        options = ensure_unique_options(correct, wrong_opts)
        if options is None:
            continue
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 10: Word Problems - Setting Up Equations
# Mastery level
# ============================================================

def generate_level_10(num_questions=50):
    """Level 10: Word Problems - Setting Up Equations"""
    questions = []
    used_questions = set()
    
    problem_types = [
        'age', 'money', 'tickets', 'perimeter', 'mixture'
    ]
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 4:
        attempts += 1
        
        p_type = random.choice(problem_types)
        name1 = random.choice(IRISH_NAMES)
        name2 = random.choice([n for n in IRISH_NAMES if n != name1])
        
        if p_type == 'age':
            # Age problems
            age1 = random.randint(10, 25)
            age2 = random.randint(8, 20)
            sum_ages = age1 + age2
            diff_ages = abs(age1 - age2)
            
            question_text = f"{name1} and {name2}'s ages add up to {sum_ages}. {name1} is {diff_ages} years older than {name2}. What equations represent this?"
            
            correct = f"x + y = {sum_ages} and x - y = {diff_ages}"
            wrong_opts = [
                f"x + y = {sum_ages} and x + y = {diff_ages}",
                f"x - y = {sum_ages} and x + y = {diff_ages}",
                f"xy = {sum_ages} and x/y = {diff_ages}"
            ]
            explanation = f"Let x = {name1}'s age, y = {name2}'s age\\nSum: x + y = {sum_ages}\\nDifference: x - y = {diff_ages} (since {name1} is older)"
            visual = generate_word_problem_svg("Age Problem", "x = " + name1 + "'s age", "y = " + name2 + "'s age")
            
        elif p_type == 'money':
            # Coin/money problems
            num_coins1 = random.randint(5, 15)
            num_coins2 = random.randint(5, 15)
            total_coins = num_coins1 + num_coins2
            val1, val2 = 50, 20  # 50c and 20c coins
            total_value = num_coins1 * val1 + num_coins2 * val2
            
            question_text = f"A jar has {total_coins} coins (50c and 20c coins only). The total value is €{total_value/100:.2f}. What equations represent this?"
            
            correct = f"x + y = {total_coins} and 50x + 20y = {total_value}"
            wrong_opts = [
                f"x + y = {total_value} and 50x + 20y = {total_coins}",
                f"x - y = {total_coins} and 50x + 20y = {total_value}",
                f"x + y = {total_coins} and x + y = {total_value}"
            ]
            explanation = f"Let x = number of 50c coins, y = number of 20c coins\\nTotal coins: x + y = {total_coins}\\nTotal value (in cents): 50x + 20y = {total_value}"
            visual = generate_coins_svg("50c coins", "x", "20c coins", "y")
            
        elif p_type == 'tickets':
            # Ticket problems
            adult_price = random.randint(8, 15)
            child_price = random.randint(4, 7)
            num_adults = random.randint(3, 10)
            num_children = random.randint(5, 15)
            total_people = num_adults + num_children
            total_cost = num_adults * adult_price + num_children * child_price
            
            question_text = f"At a cinema, adult tickets cost €{adult_price} and child tickets cost €{child_price}. {total_people} people spent €{total_cost} total. What equations represent this?"
            
            correct = f"x + y = {total_people} and {adult_price}x + {child_price}y = {total_cost}"
            wrong_opts = [
                f"x + y = {total_cost} and {adult_price}x + {child_price}y = {total_people}",
                f"x - y = {total_people} and {adult_price}x + {child_price}y = {total_cost}",
                f"{adult_price}x + {child_price}y = {total_people} and x + y = {total_cost}"
            ]
            explanation = f"Let x = adults, y = children\\nTotal people: x + y = {total_people}\\nTotal cost: {adult_price}x + {child_price}y = {total_cost}"
            visual = generate_word_problem_svg("Cinema Tickets", "x = adults", "y = children")
            
        elif p_type == 'perimeter':
            # Rectangle perimeter
            length = random.randint(8, 20)
            width = random.randint(4, 12)
            perimeter = 2 * (length + width)
            diff = length - width
            
            question_text = f"A rectangle has perimeter {perimeter} cm. The length is {diff} cm more than the width. What equations represent this?"
            
            correct = f"2x + 2y = {perimeter} and x - y = {diff}"
            wrong_opts = [
                f"x + y = {perimeter} and x - y = {diff}",
                f"2x + 2y = {perimeter} and x + y = {diff}",
                f"xy = {perimeter} and x - y = {diff}"
            ]
            explanation = f"Let x = length, y = width\\nPerimeter: 2x + 2y = {perimeter}\\nLength is {diff} more: x - y = {diff}"
            visual = generate_word_problem_svg("Rectangle Problem", "x = length", "y = width")
            
        else:  # mixture
            # Mixture problems
            kg1 = random.randint(2, 8)
            kg2 = random.randint(2, 8)
            total_kg = kg1 + kg2
            price1 = random.randint(3, 6)
            price2 = random.randint(7, 12)
            total_cost = kg1 * price1 + kg2 * price2
            
            question_text = f"A shop mixes {total_kg} kg of two types of coffee. Type A costs €{price1}/kg and Type B costs €{price2}/kg. Total cost is €{total_cost}. What equations represent this?"
            
            correct = f"x + y = {total_kg} and {price1}x + {price2}y = {total_cost}"
            wrong_opts = [
                f"x + y = {total_cost} and {price1}x + {price2}y = {total_kg}",
                f"x - y = {total_kg} and {price1}x + {price2}y = {total_cost}",
                f"x + y = {total_kg} and {price1}x - {price2}y = {total_cost}"
            ]
            explanation = f"Let x = kg of Type A, y = kg of Type B\\nTotal weight: x + y = {total_kg}\\nTotal cost: {price1}x + {price2}y = {total_cost}"
            visual = generate_word_problem_svg("Mixture Problem", "x = kg Type A", "y = kg Type B")
        
        q_key = f"{p_type}_{question_text[:40]}"
        if q_key in used_questions:
            continue
        used_questions.add(q_key)
        
        options = [correct] + wrong_opts[:3]
        # Skip if any duplicate options
        if len(set(options)) != 4:
            continue
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 11: Word Problems - Complete Solutions
# Mastery level
# ============================================================

def generate_level_11(num_questions=50):
    """Level 11: Word Problems - Complete Solutions"""
    questions = []
    used_questions = set()
    
    problem_types = ['age', 'money', 'tickets', 'speed', 'work']
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 8:
        attempts += 1
        
        p_type = random.choice(problem_types)
        name1 = random.choice(IRISH_NAMES)
        name2 = random.choice([n for n in IRISH_NAMES if n != name1])
        
        if p_type == 'age':
            age1 = random.randint(12, 30)
            age2 = random.randint(8, 20)
            if age1 <= age2:
                age1, age2 = age2 + 2, age1
            sum_ages = age1 + age2
            diff_ages = age1 - age2
            
            question_text = f"{name1} and {name2}'s ages add up to {sum_ages}. {name1} is {diff_ages} years older. How old is {name2}?"
            correct = str(age2)
            wrong_opts = [str(age1), str(age2 + 2), str(age2 - 2) if age2 > 2 else str(age2 + 3)]
            explanation = f"x + y = {sum_ages} and x - y = {diff_ages}\\nAdding: 2x = {sum_ages + diff_ages}, x = {age1}\\nSo y = {sum_ages} - {age1} = {age2}"
            visual = generate_word_problem_svg("Age Problem", "x = " + name1, "y = " + name2)
            
        elif p_type == 'money':
            num_5 = random.randint(4, 12)
            num_2 = random.randint(6, 15)
            total_coins = num_5 + num_2
            total_value = num_5 * 5 + num_2 * 2
            
            question_text = f"A piggy bank has {total_coins} coins (€5 and €2 coins). Total value is €{total_value}. How many €5 coins are there?"
            correct = str(num_5)
            wrong_opts = [str(num_2), str(num_5 + 2), str(num_5 - 2) if num_5 > 2 else str(num_5 + 3)]
            explanation = f"x + y = {total_coins} and 5x + 2y = {total_value}\\nMultiply Eq 1 by 2: 2x + 2y = {2*total_coins}\\nSubtract: 3x = {total_value - 2*total_coins}\\nx = {num_5} (€5 coins)"
            visual = generate_coins_svg("€5 coins", "x", "€2 coins", "y")
            
        elif p_type == 'tickets':
            adult_price = random.randint(10, 18)
            child_price = random.randint(5, 9)
            num_adults = random.randint(4, 12)
            num_children = random.randint(6, 15)
            total_people = num_adults + num_children
            total_cost = num_adults * adult_price + num_children * child_price
            
            question_text = f"Adult tickets cost €{adult_price}, child tickets €{child_price}. {total_people} people paid €{total_cost} total. How many adults went?"
            correct = str(num_adults)
            wrong_opts = [str(num_children), str(num_adults + 2), str(num_adults - 2) if num_adults > 2 else str(num_adults + 3)]
            explanation = f"x + y = {total_people} and {adult_price}x + {child_price}y = {total_cost}\\nUsing elimination: x = {num_adults} adults"
            visual = generate_word_problem_svg("Ticket Sales", f"Adult = €{adult_price}", f"Child = €{child_price}")
            
        elif p_type == 'speed':
            speed1 = random.randint(40, 80)
            speed2 = random.randint(50, 90)
            if speed1 >= speed2:
                speed1, speed2 = speed2 - 10, speed1
            diff_speed = speed2 - speed1
            sum_speed = speed1 + speed2
            
            question_text = f"Two cars travel towards each other. Their combined speed is {sum_speed} km/h. One is {diff_speed} km/h faster. What is the slower car's speed?"
            correct = str(speed1)
            wrong_opts = [str(speed2), str(speed1 + 5), str(speed1 - 5) if speed1 > 5 else str(speed1 + 10)]
            explanation = f"x + y = {sum_speed} and y - x = {diff_speed}\\nAdding: 2y = {sum_speed + diff_speed}, y = {speed2}\\nSo x = {sum_speed} - {speed2} = {speed1} km/h"
            visual = generate_word_problem_svg("Speed Problem", "x = slower car", "y = faster car")
            
        else:  # work
            rate1 = random.randint(2, 6)
            rate2 = random.randint(3, 8)
            if rate1 == rate2:
                rate2 = rate1 + 1
            sum_rate = rate1 + rate2
            diff_rate = abs(rate1 - rate2)
            
            question_text = f"{name1} and {name2} together paint {sum_rate} rooms per day. {name1} paints {diff_rate} {'more' if rate1 > rate2 else 'fewer'} rooms than {name2}. How many does {name2} paint?"
            correct = str(rate2)
            wrong_opts = [str(rate1), str(rate2 + 1), str(rate2 - 1) if rate2 > 1 else str(rate2 + 2)]
            explanation = f"x + y = {sum_rate} and x - y = {diff_rate if rate1 > rate2 else -diff_rate}\\nSolving: {name2} paints {rate2} rooms/day"
            visual = generate_word_problem_svg("Work Rate", f"x = {name1}", f"y = {name2}")
        
        q_key = f"{p_type}_{question_text[:40]}"
        if q_key in used_questions:
            continue
        used_questions.add(q_key)
        
        options = [correct] + wrong_opts[:3]
        # Skip if any duplicate options
        if len(set(options)) != 4:
            continue
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# LEVEL 12: Complex Applications & Problem Solving
# Mastery level
# ============================================================

def generate_level_12(num_questions=50):
    """Level 12: Complex Applications & Problem Solving"""
    questions = []
    used_questions = set()
    
    problem_types = ['investment', 'mixture_percent', 'distance_time', 'break_even', 'supply_demand']
    
    attempts = 0
    while len(questions) < num_questions and attempts < num_questions * 8:
        attempts += 1
        
        p_type = random.choice(problem_types)
        place = random.choice(IRISH_PLACES)
        name = random.choice(IRISH_NAMES)
        
        if p_type == 'investment':
            # Investment at different rates
            total_invest = random.choice([5000, 8000, 10000, 12000])
            rate1 = random.randint(3, 5)
            rate2 = random.randint(6, 9)
            amount1 = random.randint(2, 6) * 1000
            amount2 = total_invest - amount1
            total_interest = int(amount1 * rate1 / 100 + amount2 * rate2 / 100)
            
            question_text = f"{name} invests €{total_invest} in two accounts. One pays {rate1}% and another pays {rate2}%. Total annual interest is €{total_interest}. How much is in the {rate1}% account?"
            correct = f"€{amount1}"
            wrong_opts = [f"€{amount2}", f"€{amount1 + 1000}", f"€{amount1 - 1000}" if amount1 > 1000 else f"€{amount1 + 2000}"]
            explanation = f"x + y = {total_invest} and 0.0{rate1}x + 0.0{rate2}y = {total_interest}\\nSolving gives x = €{amount1} at {rate1}%"
            visual = generate_word_problem_svg("Investment", f"{rate1}% account = x", f"{rate2}% account = y")
            
        elif p_type == 'mixture_percent':
            # Mixing solutions of different concentrations
            vol1 = random.randint(20, 50)
            vol2 = random.randint(30, 60)
            conc1 = random.randint(10, 30)
            conc2 = random.randint(40, 70)
            total_vol = vol1 + vol2
            final_conc = (vol1 * conc1 + vol2 * conc2) // total_vol
            
            question_text = f"Mixing {total_vol}ml of two solutions. One is {conc1}% acid, another is {conc2}% acid. Final mixture is {final_conc}% acid. How much of the {conc1}% solution is used?"
            correct = f"{vol1}ml"
            wrong_opts = [f"{vol2}ml", f"{vol1 + 10}ml", f"{vol1 - 10}ml" if vol1 > 10 else f"{vol1 + 15}ml"]
            explanation = f"x + y = {total_vol} and {conc1}x + {conc2}y = {final_conc}({total_vol})\\nSolving gives x = {vol1}ml of {conc1}% solution"
            visual = generate_word_problem_svg("Mixture Problem", f"{conc1}% solution = x", f"{conc2}% solution = y")
            
        elif p_type == 'distance_time':
            # Meeting in the middle
            dist = random.choice([120, 150, 180, 200, 240])
            speed1 = random.randint(40, 60)
            speed2 = random.randint(50, 80)
            time = dist // (speed1 + speed2) if (speed1 + speed2) > 0 else 2
            if time < 1:
                time = 2
                dist = time * (speed1 + speed2)
            
            question_text = f"Two cars start {dist}km apart and drive towards each other. Car A travels at {speed1}km/h and Car B at {speed2}km/h. How far does Car A travel before they meet?"
            dist_a = speed1 * time
            correct = f"{dist_a}km"
            wrong_opts = [f"{speed2 * time}km", f"{dist_a + 10}km", f"{dist_a - 10}km" if dist_a > 10 else f"{dist_a + 20}km"]
            explanation = f"Time to meet: {dist}/({speed1}+{speed2}) = {time} hours\\nCar A travels: {speed1} × {time} = {dist_a}km"
            visual = generate_word_problem_svg(f"{place} to {random.choice([p for p in IRISH_PLACES if p != place])}", f"Car A: {speed1}km/h", f"Car B: {speed2}km/h")
            
        elif p_type == 'break_even':
            # Cost and revenue break-even
            fixed_cost = random.choice([200, 300, 500, 800])
            var_cost = random.randint(5, 15)
            price = var_cost + random.randint(5, 15)
            break_even = fixed_cost // (price - var_cost)
            
            question_text = f"A business has fixed costs of €{fixed_cost}. Each item costs €{var_cost} to make and sells for €{price}. How many items to break even?"
            correct = str(break_even)
            wrong_opts = [str(break_even + 5), str(break_even - 5) if break_even > 5 else str(break_even + 10), str(fixed_cost // price)]
            explanation = f"Cost: C = {fixed_cost} + {var_cost}x\\nRevenue: R = {price}x\\nBreak-even when C = R:\\n{fixed_cost} + {var_cost}x = {price}x\\n{fixed_cost} = {price - var_cost}x\\nx = {break_even} items"
            visual = generate_word_problem_svg("Break-Even Analysis", f"Cost = {fixed_cost} + {var_cost}x", f"Revenue = {price}x")
            
        else:  # supply_demand
            # Supply and demand equilibrium
            # Demand: p = a - bq, Supply: p = c + dq
            q_eq = random.randint(10, 30)
            p_eq = random.randint(15, 40)
            b = random.randint(1, 3)
            a = p_eq + b * q_eq
            d = random.randint(1, 2)
            c = p_eq - d * q_eq
            if c < 0:
                c = 0
                d = p_eq // q_eq if q_eq > 0 else 1
            
            question_text = f"Demand: p = {a} - {b}q. Supply: p = {c} + {d}q. Find the equilibrium quantity."
            correct = str(q_eq)
            wrong_opts = [str(p_eq), str(q_eq + 5), str(q_eq - 5) if q_eq > 5 else str(q_eq + 10)]
            explanation = f"At equilibrium, demand = supply:\\n{a} - {b}q = {c} + {d}q\\n{a - c} = {b + d}q\\nq = {q_eq} units"
            visual = generate_word_problem_svg("Supply & Demand", f"Demand: p = {a} - {b}q", f"Supply: p = {c} + {d}q")
        
        q_key = f"{p_type}_{question_text[:40]}"
        if q_key in used_questions:
            continue
        used_questions.add(q_key)
        
        options = [correct] + wrong_opts[:3]
        # Skip if any duplicate options
        if len(set(options)) != 4:
            continue
        random.shuffle(options)
        correct_idx = options.index(correct)
        
        questions.append({
            'question_text': question_text,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': explanation,
            'image_svg': visual
        })
    
    return questions

# ============================================================
# MAIN GENERATION AND DATABASE FUNCTIONS
# ============================================================

def generate_all_questions():
    """Generate all questions for all levels"""
    all_questions = []
    
    generators = [
        (1, generate_level_1, "Understanding Systems"),
        (2, generate_level_2, "Solving by Inspection"),
        (3, generate_level_3, "Graphical Method"),
        (4, generate_level_4, "Elimination - Same Coefficients"),
        (5, generate_level_5, "Elimination - Multiply One"),
        (6, generate_level_6, "Elimination - Multiply Both"),
        (7, generate_level_7, "Substitution - Simple"),
        (8, generate_level_8, "Substitution - Rearranging"),
        (9, generate_level_9, "Choosing Best Method"),
        (10, generate_level_10, "Word Problems - Setup"),
        (11, generate_level_11, "Word Problems - Solve"),
        (12, generate_level_12, "Complex Applications"),
    ]
    
    for level, generator, name in generators:
        print(f"Generating Level {level}: {name}...")
        questions = generator(QUESTIONS_PER_LEVEL)
        
        # Assign difficulty band
        if level <= 3:
            band = "foundation"
        elif level <= 6:
            band = "ordinary"
        elif level <= 9:
            band = "higher"
        else:
            band = "mastery"
        
        for q in questions:
            q['topic'] = TOPIC
            q['difficulty'] = level
            q['difficulty_band'] = band
            q['mode'] = MODE
        
        all_questions.extend(questions)
        print(f"  Generated {len(questions)} questions")
    
    return all_questions

def validate_questions(questions):
    """Validate all generated questions"""
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    
    errors = []
    level_counts = {}
    level_visuals = {}
    
    for q in questions:
        level = q['difficulty']
        level_counts[level] = level_counts.get(level, 0) + 1
        
        if q.get('image_svg'):
            level_visuals[level] = level_visuals.get(level, 0) + 1
        
        # Check for duplicate options
        options = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(options)) != 4:
            errors.append(f"Level {level}: Duplicate options in '{q['question_text'][:30]}...'")
        
        # Check for missing explanation
        if not q.get('explanation'):
            errors.append(f"Level {level}: Missing explanation")
    
    # Print summary
    level_names = [
        "Understanding Systems", "Solving by Inspection", "Graphical Method",
        "Elimination - Same Coeff", "Elimination - Mult One", "Elimination - Mult Both",
        "Substitution - Simple", "Substitution - Rearrange", "Choosing Method",
        "Word Problems - Setup", "Word Problems - Solve", "Complex Applications"
    ]
    
    for level in range(1, 13):
        count = level_counts.get(level, 0)
        visual_count = level_visuals.get(level, 0)
        visual_pct = (visual_count / count * 100) if count > 0 else 0
        status = "✓" if count >= QUESTIONS_PER_LEVEL else "✗"
        print(f"Level {level:2}: {count:2}/{QUESTIONS_PER_LEVEL} | Visual: {visual_pct:5.1f}% | {status} {level_names[level-1]}")
    
    print("=" * 60)
    print(f"Total Questions: {len(questions)}")
    print(f"Total Errors: {len(errors)}")
    
    if errors:
        print("\nFirst 5 errors:")
        for err in errors[:5]:
            print(f"  - {err}")
    
    print("=" * 60)
    
    return len(errors) == 0

def test_single_insert(db_path):
    """Test inserting ONE question before bulk insert"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    test_sql = """
        INSERT INTO questions_adaptive 
        (question_text, option_a, option_b, option_c, option_d,
         correct_answer, topic, difficulty_level, difficulty_band, 
         mode, explanation, image_svg, is_active)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
    """
    
    try:
        cursor.execute(test_sql, (
            "TEST_QUESTION_DELETE_ME", "A", "B", "C", "D",
            0, "test_topic", 1, "foundation", "jc_exam", "Test", None
        ))
        cursor.execute("DELETE FROM questions_adaptive WHERE question_text = 'TEST_QUESTION_DELETE_ME'")
        conn.commit()
        conn.close()
        print("✓ Database schema validated - test insert successful")
        return True
    except Exception as e:
        conn.close()
        print(f"✗ DATABASE SCHEMA ERROR: {e}")
        print("  Check column names match questions_adaptive table!")
        return False

def insert_into_database(questions):
    """Insert questions into the database"""
    db_path = 'instance/mathquiz.db'
    
    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}")
        return False
    
    if not test_single_insert(db_path):
        print("ABORTING: Fix schema errors before bulk insert!")
        return False
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Delete existing questions for this topic and mode
    cursor.execute("DELETE FROM questions_adaptive WHERE topic = ? AND mode = ?", (TOPIC, MODE))
    deleted = cursor.rowcount
    print(f"Deleted {deleted} existing {TOPIC} questions in {MODE} mode")
    
    inserted = 0
    errors = 0
    
    for q in questions:
        try:
            cursor.execute('''
                INSERT INTO questions_adaptive 
                (question_text, option_a, option_b, option_c, option_d,
                 correct_answer, topic, difficulty_level, difficulty_band,
                 mode, explanation, image_svg, is_active)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                q['question_text'],
                q['option_a'], q['option_b'], q['option_c'], q['option_d'],
                q['correct_idx'], q['topic'], q['difficulty'], q['difficulty_band'],
                q['mode'], q['explanation'], q.get('image_svg', ''), 1
            ))
            inserted += 1
        except Exception as e:
            errors += 1
            if errors <= 5:
                print(f"Error inserting: {e}")
    
    conn.commit()
    conn.close()
    
    print(f"\n✓ Inserted {inserted} questions")
    if errors > 0:
        print(f"✗ {errors} errors occurred")
    
    return errors == 0

# ============================================================
# MAIN ENTRY POINT
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("AgentMath - Simultaneous Equations Topic Generator v1")
    print("SEC Junior Cycle Mathematics - Adaptive Quiz System")
    print("Generating 600 questions (50 per level × 12 levels)")
    print("=" * 60)
    
    # Generate all questions
    questions = generate_all_questions()
    
    # Validate
    valid = validate_questions(questions)
    
    if not valid:
        print("\n⚠ Validation found issues. Review before inserting.")
    
    # Prompt for database insertion
    print("\n" + "=" * 60)
    response = input("Insert questions into database? (y/n): ")
    
    if response.lower() == 'y':
        success = insert_into_database(questions)
        if success:
            print("\n" + "=" * 60)
            print("✓ SUCCESS! All questions inserted.")
            print("=" * 60)
        else:
            print("\n⚠ Some questions failed to insert. Check errors above.")
    else:
        print("Skipped database insertion.")
