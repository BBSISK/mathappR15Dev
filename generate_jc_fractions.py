"""
JC Exam Style Fractions Question Generator
Based on SEC Junior Cycle Ordinary Level analysis (2022-2025)

Key SEC Patterns Identified:
- 2022 Q10(a): Adding fractions with different denominators (2/3 + 5/7)
- "Simplest form" explicitly required
- 5-mark allocation typical
- Recent shift toward contextual/applied questions

Levels:
1-4: Foundation (visual, same denominator, simplifying)
5-6: Core Ordinary Level (different denominator add/subtract) ← SEC Q10(a) style
7-8: Ordinary Level (multiply/divide, mixed numbers)
9-10: Higher/stretch (word problems, multi-step)
11-12: Higher Level (algebraic, complex multi-step)

Run: python generate_jc_fractions.py
"""

import sqlite3
import random
from math import gcd
import os

DB_PATH = 'instance/mathquiz.db'

def simplify_fraction(num, den):
    """Return simplified fraction as tuple"""
    if den == 0:
        return (num, 1)
    common = gcd(abs(num), abs(den))
    return (num // common, den // common)

def lcm(a, b):
    """Least common multiple"""
    return abs(a * b) // gcd(a, b)

def fraction_to_mixed(num, den):
    """Convert improper fraction to mixed number string"""
    if abs(num) < den:
        n, d = simplify_fraction(num, den)
        return f"{n}/{d}"
    whole = num // den
    remainder = num % den
    if remainder == 0:
        return str(whole)
    n, d = simplify_fraction(remainder, den)
    return f"{whole} {n}/{d}"

def generate_svg_pie_fraction(num, den, size=120):
    """Generate SVG pie chart showing a fraction"""
    import math
    cx, cy, r = size//2, size//2, size//2 - 10
    
    svg = f'<svg width="{size}" height="{size}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#e0e0e0" stroke="#333" stroke-width="2"/>'
    
    # Draw filled segments
    for i in range(num):
        start_angle = (i / den) * 2 * math.pi - math.pi/2
        end_angle = ((i + 1) / den) * 2 * math.pi - math.pi/2
        
        x1 = cx + r * math.cos(start_angle)
        y1 = cy + r * math.sin(start_angle)
        x2 = cx + r * math.cos(end_angle)
        y2 = cy + r * math.sin(end_angle)
        
        large_arc = 1 if (end_angle - start_angle) > math.pi else 0
        
        svg += f'<path d="M{cx},{cy} L{x1:.1f},{y1:.1f} A{r},{r} 0 {large_arc},1 {x2:.1f},{y2:.1f} Z" fill="#4CAF50" stroke="#333" stroke-width="1"/>'
    
    # Draw segment lines
    for i in range(den):
        angle = (i / den) * 2 * math.pi - math.pi/2
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        svg += f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#333" stroke-width="1"/>'
    
    svg += '</svg>'
    return svg


def generate_level_questions(level):
    """Generate questions for a specific level - correct_answer is 0-3 (index)"""
    questions = []
    
    if level == 1:
        # Foundation: Identify fractions from visuals
        fractions = [(1,2), (1,3), (2,3), (1,4), (3,4), (2,5), (3,5)]
        for num, den in fractions:
            svg = generate_svg_pie_fraction(num, den)
            
            answer = f"{num}/{den}"
            options = [answer]
            distractors = [f"{den}/{num}", f"{num}/{den+1}", f"{num+1}/{den}"]
            for d in distractors:
                if d not in options:
                    options.append(d)
            options = options[:4]
            random.shuffle(options)
            correct = options.index(answer)  # Returns 0, 1, 2, or 3
            
            questions.append({
                'question': f"What fraction of this shape is shaded?",
                'options': options,
                'correct': correct,
                'explanation': f"There are {den} equal parts and {num} are shaded, so the fraction is {num}/{den}.",
                'svg': svg,
                'type': 'visual'
            })
    
    elif level == 2:
        # Foundation: Simplify fractions
        pairs = [(2,4), (3,6), (4,8), (2,6), (3,9), (4,12), (5,10), (6,8), (4,6), (6,9)]
        for num, den in pairs:
            sn, sd = simplify_fraction(num, den)
            
            answer = f"{sn}/{sd}"
            options = [answer]
            distractors = [f"{num}/{den}", f"{num//2 if num%2==0 else num}/{den}", f"{sn}/{sd+1}"]
            for d in distractors:
                if d not in options and d != f"{num}/{den}":
                    options.append(d)
            while len(options) < 4:
                options.append(f"{sn+1}/{sd+1}")
            options = options[:4]
            random.shuffle(options)
            correct = options.index(answer)
            
            questions.append({
                'question': f"Write {num}/{den} in its simplest form.",
                'options': options,
                'correct': correct,
                'explanation': f"Divide both {num} and {den} by their HCF ({gcd(num,den)}) to get {sn}/{sd}.",
                'svg': None,
                'type': 'simplify'
            })
    
    elif level == 3:
        # Foundation: Add fractions with SAME denominator
        for den in [4, 5, 6, 8, 10]:
            for _ in range(2):
                num1 = random.randint(1, den-2)
                num2 = random.randint(1, den-1-num1)
                result_num = num1 + num2
                sn, sd = simplify_fraction(result_num, den)
                
                answer = str(sn) if sd == 1 else f"{sn}/{sd}"
                
                options = [answer]
                distractors = [
                    f"{num1+num2}/{den+den}",
                    f"{result_num}/{den}" if answer != f"{result_num}/{den}" else f"{result_num+1}/{den}",
                    f"{sn+1}/{sd}" if sd != 1 else str(sn+1)
                ]
                for d in distractors:
                    if d not in options:
                        options.append(d)
                options = options[:4]
                random.shuffle(options)
                correct = options.index(answer)
                
                questions.append({
                    'question': f"Calculate {num1}/{den} + {num2}/{den}. Give your answer in simplest form.",
                    'options': options,
                    'correct': correct,
                    'explanation': f"{num1}/{den} + {num2}/{den} = {result_num}/{den} = {answer}",
                    'svg': None,
                    'type': 'add_same'
                })
    
    elif level == 4:
        # Foundation: Subtract fractions with SAME denominator
        for den in [4, 5, 6, 8, 10]:
            for _ in range(2):
                num1 = random.randint(3, den-1)
                num2 = random.randint(1, num1-1)
                result_num = num1 - num2
                sn, sd = simplify_fraction(result_num, den)
                
                answer = f"{sn}/{sd}" if sd != 1 else str(sn)
                
                options = [answer]
                distractors = [
                    f"{result_num}/{den}" if answer != f"{result_num}/{den}" else f"{result_num+1}/{den}",
                    f"{result_num}/{den+1}",
                    f"{sn+1}/{sd}" if sd != 1 else str(max(1, sn-1))
                ]
                for d in distractors:
                    if d not in options:
                        options.append(d)
                while len(options) < 4:
                    options.append(f"{sn}/{sd+1}")
                options = options[:4]
                random.shuffle(options)
                correct = options.index(answer)
                
                questions.append({
                    'question': f"Calculate {num1}/{den} − {num2}/{den}. Give your answer in simplest form.",
                    'options': options,
                    'correct': correct,
                    'explanation': f"{num1}/{den} − {num2}/{den} = {result_num}/{den} = {answer}",
                    'svg': None,
                    'type': 'subtract_same'
                })
    
    elif level == 5:
        # ★ CORE SEC ORDINARY LEVEL - Add fractions with DIFFERENT denominators
        pairs = [
            (1,2, 1,3), (1,2, 1,4), (1,3, 1,4), (2,3, 1,4), (1,2, 2,5),
            (2,3, 3,4), (1,3, 2,5), (3,4, 1,5), (2,5, 1,3), (1,4, 2,3),
            (2,3, 5,7), (3,4, 2,5), (1,6, 1,4), (2,5, 3,10), (1,3, 1,6)
        ]
        
        for n1, d1, n2, d2 in pairs:
            common_den = lcm(d1, d2)
            new_n1 = n1 * (common_den // d1)
            new_n2 = n2 * (common_den // d2)
            result_num = new_n1 + new_n2
            sn, sd = simplify_fraction(result_num, common_den)
            
            answer = str(sn) if sd == 1 else f"{sn}/{sd}"
            
            options = [answer]
            distractors = [
                f"{n1+n2}/{d1+d2}",
                f"{result_num}/{common_den}" if answer != f"{result_num}/{common_den}" else f"{result_num+1}/{common_den}",
                f"{n1+n2}/{max(d1,d2)}"
            ]
            for d in distractors:
                if d not in options:
                    options.append(d)
            options = options[:4]
            random.shuffle(options)
            correct = options.index(answer)
            
            questions.append({
                'question': f"Write {n1}/{d1} + {n2}/{d2} as a single fraction in its simplest form.",
                'options': options,
                'correct': correct,
                'explanation': f"LCD = {common_den}. {n1}/{d1} = {new_n1}/{common_den}, {n2}/{d2} = {new_n2}/{common_den}. Sum = {result_num}/{common_den} = {answer}",
                'svg': None,
                'type': 'add_different'
            })
    
    elif level == 6:
        # ★ SEC ORDINARY LEVEL - Subtract fractions with DIFFERENT denominators
        pairs = [
            (3,4, 1,2), (2,3, 1,4), (5,6, 1,3), (3,4, 2,5), (4,5, 1,2),
            (5,6, 1,4), (7,8, 1,2), (2,3, 1,6), (5,8, 1,4), (3,5, 1,3),
            (7,10, 2,5), (5,6, 3,8), (4,5, 3,10), (7,8, 2,3), (9,10, 3,5)
        ]
        
        for n1, d1, n2, d2 in pairs:
            common_den = lcm(d1, d2)
            new_n1 = n1 * (common_den // d1)
            new_n2 = n2 * (common_den // d2)
            result_num = new_n1 - new_n2
            
            if result_num <= 0:
                continue
                
            sn, sd = simplify_fraction(result_num, common_den)
            answer = f"{sn}/{sd}" if sd != 1 else str(sn)
            
            options = [answer]
            distractors = [
                f"{abs(n1-n2)}/{abs(d1-d2)}" if d1 != d2 else f"{n1-n2}/{d1}",
                f"{result_num}/{common_den}" if answer != f"{result_num}/{common_den}" else f"{result_num+1}/{common_den}",
                f"{abs(n1-n2)}/{max(d1,d2)}"
            ]
            for d in distractors:
                if d not in options and '/0' not in d:
                    options.append(d)
            while len(options) < 4:
                options.append(f"{sn+1}/{sd}")
            options = options[:4]
            random.shuffle(options)
            correct = options.index(answer)
            
            questions.append({
                'question': f"Write {n1}/{d1} − {n2}/{d2} as a single fraction in its simplest form.",
                'options': options,
                'correct': correct,
                'explanation': f"LCD = {common_den}. {n1}/{d1} = {new_n1}/{common_den}, {n2}/{d2} = {new_n2}/{common_den}. Difference = {result_num}/{common_den} = {answer}",
                'svg': None,
                'type': 'subtract_different'
            })
    
    elif level == 7:
        # Ordinary Level: Multiply fractions
        pairs = [
            (1,2, 1,3), (2,3, 3,4), (1,4, 2,5), (3,5, 5,6), (2,3, 1,2),
            (3,4, 4,5), (2,5, 5,8), (1,3, 3,7), (4,5, 1,2), (2,7, 7,8),
            (3,8, 2,3), (5,6, 3,5), (1,4, 4,9), (2,9, 3,4), (5,7, 7,10)
        ]
        
        for n1, d1, n2, d2 in pairs:
            result_num = n1 * n2
            result_den = d1 * d2
            sn, sd = simplify_fraction(result_num, result_den)
            
            answer = f"{sn}/{sd}" if sd != 1 else str(sn)
            
            options = [answer]
            distractors = [
                f"{n1*n2}/{d1*d2}" if answer != f"{n1*n2}/{d1*d2}" else f"{n1*n2+1}/{d1*d2}",
                f"{n1+n2}/{d1+d2}",
                f"{n1*d2}/{d1*n2}"
            ]
            for d in distractors:
                if d not in options:
                    options.append(d)
            options = options[:4]
            random.shuffle(options)
            correct = options.index(answer)
            
            questions.append({
                'question': f"Calculate {n1}/{d1} × {n2}/{d2}. Give your answer in simplest form.",
                'options': options,
                'correct': correct,
                'explanation': f"{n1}/{d1} × {n2}/{d2} = {result_num}/{result_den} = {answer}",
                'svg': None,
                'type': 'multiply'
            })
    
    elif level == 8:
        # Ordinary Level: Divide fractions
        pairs = [
            (1,2, 1,4), (2,3, 1,3), (3,4, 1,2), (1,3, 2,3), (2,5, 1,5),
            (3,4, 3,8), (5,6, 1,3), (2,3, 4,9), (1,2, 3,4), (4,5, 2,5),
            (5,8, 1,4), (3,5, 6,10), (7,8, 7,16), (2,9, 1,3), (5,6, 5,12)
        ]
        
        for n1, d1, n2, d2 in pairs:
            result_num = n1 * d2
            result_den = d1 * n2
            sn, sd = simplify_fraction(result_num, result_den)
            
            answer = f"{sn}/{sd}" if sd != 1 else str(sn)
            
            options = [answer]
            distractors = [
                f"{n1*n2}/{d1*d2}",
                f"{n1}/{d1*n2}",
                f"{d1*n2}/{n1*d2}"
            ]
            for d in distractors:
                if d not in options:
                    options.append(d)
            options = options[:4]
            random.shuffle(options)
            correct = options.index(answer)
            
            questions.append({
                'question': f"Calculate {n1}/{d1} ÷ {n2}/{d2}. Give your answer in simplest form.",
                'options': options,
                'correct': correct,
                'explanation': f"{n1}/{d1} ÷ {n2}/{d2} = {n1}/{d1} × {d2}/{n2} = {result_num}/{result_den} = {answer}",
                'svg': None,
                'type': 'divide'
            })
    
    elif level == 9:
        # Higher/Stretch: Mixed numbers addition
        problems = [
            (1, 1,2, 2, 1,4),
            (2, 1,3, 1, 1,2),
            (1, 3,4, 2, 1,3),
            (3, 1,5, 1, 2,5),
            (2, 2,3, 1, 5,6),
            (1, 1,4, 3, 1,2),
            (2, 3,8, 1, 1,4),
            (1, 5,6, 2, 1,3),
        ]
        
        for w1, n1, d1, w2, n2, d2 in problems:
            imp1 = w1 * d1 + n1
            imp2 = w2 * d2 + n2
            common_den = lcm(d1, d2)
            new_n1 = imp1 * (common_den // d1)
            new_n2 = imp2 * (common_den // d2)
            result_num = new_n1 + new_n2
            
            answer = fraction_to_mixed(result_num, common_den)
            
            options = [answer]
            wrong1 = fraction_to_mixed(result_num - common_den, common_den)
            wrong2 = fraction_to_mixed(result_num + common_den, common_den)
            wrong3 = f"{w1+w2} {n1+n2}/{d1+d2}" if d1+d2 > 0 else str(w1+w2+1)
            
            for d in [wrong1, wrong2, wrong3]:
                if d not in options and d:
                    options.append(d)
            while len(options) < 4:
                options.append(fraction_to_mixed(result_num + 2, common_den))
            options = options[:4]
            random.shuffle(options)
            correct = options.index(answer)
            
            questions.append({
                'question': f"Calculate {w1} {n1}/{d1} + {w2} {n2}/{d2}. Give your answer as a mixed number in simplest form.",
                'options': options,
                'correct': correct,
                'explanation': "Convert to improper fractions, find common denominator, add, then convert back to mixed number.",
                'svg': None,
                'type': 'mixed_add'
            })
    
    elif level == 10:
        # Higher/Stretch: Word problems with fractions
        word_problems = [
            {
                'question': "A recipe needs 2/3 cup of flour. If you want to make 1½ times the recipe, how much flour do you need?",
                'answer': "1",
                'distractors': ["2/3", "1/2", "5/6"]
            },
            {
                'question': "Sarah walked 3/4 km to school and 2/5 km to the shop. How far did she walk in total?",
                'answer': "1 3/20",
                'distractors': ["5/9", "1 1/5", "1 1/4"]
            },
            {
                'question': "A tank is 5/6 full. After using 1/4 of the tank, what fraction remains?",
                'answer': "7/12",
                'distractors': ["4/2", "1/2", "2/3"]
            },
            {
                'question': "If 3/5 of a class are girls, and 1/4 of the girls wear glasses, what fraction of the class are girls wearing glasses?",
                'answer': "3/20",
                'distractors': ["4/9", "1/5", "17/20"]
            },
            {
                'question': "A piece of rope is 7/8 m long. How many pieces of 1/4 m can be cut from it?",
                'answer': "3 1/2",
                'distractors': ["3", "4", "7/32"]
            },
        ]
        
        for wp in word_problems:
            options = [wp['answer']] + wp['distractors']
            random.shuffle(options)
            correct = options.index(wp['answer'])
            
            questions.append({
                'question': wp['question'],
                'options': options,
                'correct': correct,
                'explanation': "Identify the operation needed, then calculate with fractions.",
                'svg': None,
                'type': 'word_problem'
            })
    
    elif level == 11:
        # Higher Level: Multi-step problems
        multi_step = [
            {
                'question': "Calculate (1/2 + 1/3) × 3/5. Give your answer in simplest form.",
                'answer': "1/2",
                'distractors': ["5/6", "3/10", "1/3"]
            },
            {
                'question': "Calculate (3/4 − 1/3) ÷ 5/12. Give your answer in simplest form.",
                'answer': "1",
                'distractors': ["5/12", "25/144", "12/5"]
            },
            {
                'question': "Calculate 2/3 of (1/2 + 3/4). Give your answer in simplest form.",
                'answer': "5/6",
                'distractors': ["1/2", "7/12", "11/12"]
            },
            {
                'question': "If x = 3/4 and y = 2/3, calculate (x + y) × (x − y).",
                'answer': "17/144",
                'distractors': ["1/12", "5/12", "1/2"]
            },
            {
                'question': "Calculate 1/2 + 1/3 + 1/4. Give your answer in simplest form.",
                'answer': "1 1/12",
                'distractors': ["3/9", "1", "13/12"]
            },
        ]
        
        for ms in multi_step:
            options = [ms['answer']] + ms['distractors']
            random.shuffle(options)
            correct = options.index(ms['answer'])
            
            questions.append({
                'question': ms['question'],
                'options': options,
                'correct': correct,
                'explanation': "Follow order of operations (BIMDAS) when solving multi-step fraction problems.",
                'svg': None,
                'type': 'multi_step'
            })
    
    elif level == 12:
        # Higher Level: Cross-topic (fractions ↔ percentages, decimals)
        cross_topic = [
            {
                'question': "Express 3/8 as a percentage.",
                'answer': "37.5%",
                'distractors': ["37%", "38%", "0.375%"]
            },
            {
                'question': "What fraction is equivalent to 0.125?",
                'answer': "1/8",
                'distractors': ["1/125", "125/1000", "1/4"]
            },
            {
                'question': "If 40% of a number is 24, what is 3/4 of that number?",
                'answer': "45",
                'distractors': ["48", "40", "36"]
            },
            {
                'question': "Write 2.75 as a mixed number in simplest form.",
                'answer': "2 3/4",
                'distractors': ["2 75/100", "2 7/10", "275/100"]
            },
            {
                'question': "What is 5/6 as a recurring decimal?",
                'answer': "0.833...",
                'distractors': ["0.83", "0.856", "0.8"]
            },
        ]
        
        for ct in cross_topic:
            options = [ct['answer']] + ct['distractors']
            random.shuffle(options)
            correct = options.index(ct['answer'])
            
            questions.append({
                'question': ct['question'],
                'options': options,
                'correct': correct,
                'explanation': "Convert between fractions, decimals, and percentages as needed.",
                'svg': None,
                'type': 'cross_topic'
            })
    
    return questions


def insert_questions(cursor, questions, level):
    """Insert questions into database"""
    count = 0
    
    # Determine difficulty band
    if level <= 4:
        band = 'foundation'
    elif level <= 8:
        band = 'ordinary'
    else:
        band = 'higher'
    
    for q in questions:
        try:
            cursor.execute("""
                INSERT INTO questions_adaptive 
                (topic, difficulty_level, difficulty_band, question_text, 
                 option_a, option_b, option_c, option_d, correct_answer, 
                 explanation, image_svg, question_type, is_active, mode)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, 'jc_exam')
            """, (
                'fractions',
                level,
                band,
                q['question'],
                q['options'][0],
                q['options'][1],
                q['options'][2],
                q['options'][3] if len(q['options']) > 3 else '',
                q['correct'],  # Now numeric 0-3
                q['explanation'],
                q['svg'],
                q['type']
            ))
            count += 1
        except Exception as e:
            print(f"   ⚠️ Error inserting question: {e}")
    
    return count


def main():
    print("=" * 60)
    print("JC Exam Style Fractions Question Generator")
    print("Based on SEC Ordinary Level Analysis (2022-2025)")
    print("=" * 60)
    
    if not os.path.exists(DB_PATH):
        print(f"❌ Database not found at {DB_PATH}")
        return
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check if mode column exists
    cursor.execute("PRAGMA table_info(questions_adaptive)")
    columns = [col[1] for col in cursor.fetchall()]
    if 'mode' not in columns:
        print("❌ 'mode' column not found. Run add_question_mode_column.py first.")
        conn.close()
        return
    
    # Clear existing jc_exam fractions questions
    cursor.execute("""
        DELETE FROM questions_adaptive 
        WHERE topic = 'fractions' AND mode = 'jc_exam'
    """)
    deleted = cursor.rowcount
    print(f"🗑️ Cleared {deleted} existing JC Exam fractions questions")
    
    total_inserted = 0
    
    print("\n📝 Generating questions by level:")
    print("-" * 40)
    
    for level in range(1, 13):
        questions = generate_level_questions(level)
        count = insert_questions(cursor, questions, level)
        
        band = 'Foundation' if level <= 4 else ('Ordinary' if level <= 8 else 'Higher')
        star = '★' if level in [5, 6] else ' '
        print(f"   Level {level:2d} ({band:10s}): {count:3d} questions {star}")
        total_inserted += count
    
    conn.commit()
    
    print("-" * 40)
    print(f"✅ Total inserted: {total_inserted} JC Exam questions")
    
    # Summary by band
    cursor.execute("""
        SELECT difficulty_band, COUNT(*) 
        FROM questions_adaptive 
        WHERE topic = 'fractions' AND mode = 'jc_exam'
        GROUP BY difficulty_band
    """)
    print("\n📊 Questions by difficulty band:")
    for band, count in cursor.fetchall():
        print(f"   {band}: {count}")
    
    conn.close()
    print("\n✅ Generation complete!")
    print("\n💡 Levels 5-6 (★) directly match SEC Ordinary Level Q10(a) style")


if __name__ == "__main__":
    main()
