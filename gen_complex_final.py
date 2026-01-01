#!/usr/bin/env python3
"""LC OL Complex Numbers - 600 Questions - Final"""
import random

TOPIC_ID = 'lc_ol_complex'
STRAND_ID = 11

LEVEL_CONFIG = {
    1: ("Introduction to i", "Foundation"),
    2: ("Complex Number Form", "Foundation"),
    3: ("Real and Imaginary Parts", "Foundation"),
    4: ("Adding Complex Numbers", "Developing"),
    5: ("Subtracting Complex Numbers", "Developing"),
    6: ("Multiplying by Real Numbers", "Developing"),
    7: ("Multiplying Complex Numbers", "Proficient"),
    8: ("Complex Conjugate", "Proficient"),
    9: ("Dividing Complex Numbers", "Proficient"),
    10: ("Argand Diagram", "Advanced"),
    11: ("Modulus of Complex Numbers", "Advanced"),
    12: ("SEC Exam Style", "Advanced"),
}

def shuffle_options(correct, distractors):
    options = [correct] + distractors[:3]
    random.shuffle(options)
    return options, options.index(correct)

def gen_level(level):
    qs = []
    
    if level == 1:  # Powers of i, square roots
        qs.append(("What is i?", "√(-1)", ["√1", "-1", "1"], "i = √(-1)."))
        qs.append(("i² = ?", "-1", ["1", "i", "-i"], "i² = -1."))
        qs.append(("i³ = ?", "-i", ["i", "1", "-1"], "i³ = -i."))
        qs.append(("i⁴ = ?", "1", ["-1", "i", "-i"], "i⁴ = 1."))
        for n in range(5, 45):
            r = n % 4
            ans = ["1", "i", "-1", "-i"][r]
            qs.append((f"i^{n} = ?", ans, ["1", "-1", "i", "-i"], f"i^{n} mod 4 = {r}."))
            if len(qs) >= 48: break
        for n in [4,9,16,25,36,49,64,81,100,121,144]:
            r = int(n**0.5)
            qs.append((f"√(-{n}) = ?", f"{r}i", [f"-{r}i", str(r), str(-r)], f"= {r}i."))
            if len(qs) >= 50: break
                
    elif level == 2:  # Complex form
        qs.append(("Standard form?", "a + bi", ["ai + b", "a - bi", "ab"], "a + bi."))
        for a in range(-6, 7):
            for b in range(1, 7):
                z = f"{a} + {b}i" if a >= 0 else f"{a} + {b}i"
                qs.append((f"Is {z} complex?", "Yes", ["No", "Real only", "Imaginary only"], "Yes."))
                if len(qs) >= 50: break
            if len(qs) >= 50: break
                
    elif level == 3:  # Real and imaginary parts
        for a in range(-8, 9):
            for b in range(-8, 9):
                if a != 0 and b != 0 and len(qs) < 25:
                    z = f"{a}+{b}i" if b > 0 else f"{a}-{-b}i"
                    qs.append((f"Re({z}) = ?", str(a), [str(b), str(-a), str(a+b)], f"Re = {a}."))
        for a in range(-8, 9):
            for b in range(-8, 9):
                if a != 0 and b != 0 and len(qs) < 50:
                    z = f"{a}+{b}i" if b > 0 else f"{a}-{-b}i"
                    qs.append((f"Im({z}) = ?", str(b), [str(a), str(-b), f"{b}i"], f"Im = {b}."))
                    
    elif level == 4:  # Adding
        qs.append(("How add complex?", "Add real, add imaginary", ["Multiply", "Cross multiply", "Divide"], "(a+bi)+(c+di)=(a+c)+(b+d)i."))
        for a1 in range(1, 10):
            for b1 in range(1, 8):
                a2, b2 = (a1 % 5) + 1, (b1 % 4) + 1
                ar, br = a1+a2, b1+b2
                qs.append((f"({a1}+{b1}i)+({a2}+{b2}i)=?", f"{ar}+{br}i", [f"{ar}-{br}i", f"{br}+{ar}i", f"{ar+br}"], f"= {ar}+{br}i."))
                if len(qs) >= 50: break
            if len(qs) >= 50: break
                
    elif level == 5:  # Subtracting
        qs.append(("How subtract complex?", "Subtract real, subtract imaginary", ["Add", "Multiply", "Divide"], "(a+bi)-(c+di)=(a-c)+(b-d)i."))
        for a1 in range(4, 14):
            for b1 in range(4, 12):
                a2, b2 = (a1 % 3) + 1, (b1 % 3) + 1
                ar, br = a1-a2, b1-b2
                qs.append((f"({a1}+{b1}i)-({a2}+{b2}i)=?", f"{ar}+{br}i", [f"{a1+a2}+{b1+b2}i", f"{ar}-{br}i", f"{br}+{ar}i"], f"= {ar}+{br}i."))
                if len(qs) >= 50: break
            if len(qs) >= 50: break
                
    elif level == 6:  # Multiply by real
        qs.append(("k(a+bi) = ?", "ka + kbi", ["k+a+bi", "ka+bi", "a+kbi"], "Multiply both parts."))
        for k in range(2, 12):
            for a, b in [(1,2),(2,3),(3,1),(1,4),(2,1),(4,2),(3,2),(1,5),(2,4),(3,3),(4,1),(1,3)]:
                ar, br = k*a, k*b
                qs.append((f"{k}({a}+{b}i) = ?", f"{ar}+{br}i", [f"{ar}-{br}i", f"{a}+{br}i", f"{ar}+{b}i"], f"= {ar}+{br}i."))
                if len(qs) >= 50: break
            if len(qs) >= 50: break
                
    elif level == 7:  # Multiply complex
        qs.append(("Method for (a+bi)(c+di)?", "FOIL, then i²=-1", ["Add parts", "Multiply corresponding", "Divide"], "FOIL and i²=-1."))
        products = [((1,2),(3,1),(1,7)),((2,1),(1,3),(-1,7)),((1,1),(2,2),(0,4)),((3,1),(2,1),(5,5)),
                   ((2,3),(1,1),(-1,5)),((1,2),(1,2),(-3,4)),((2,1),(2,1),(3,4)),((1,3),(1,3),(-8,6)),
                   ((2,2),(3,1),(4,8)),((3,2),(2,3),(0,13)),((4,1),(1,2),(2,9)),((1,4),(2,1),(-2,9))]
        for (a1,b1),(a2,b2),(ar,br) in products:
            ans = f"{ar}+{br}i" if ar!=0 else f"{br}i"
            if ar!=0 and br<0: ans = f"{ar}-{-br}i"
            qs.append((f"({a1}+{b1}i)({a2}+{b2}i)=?", ans, [f"{a1*a2}+{b1*b2}i", f"{-ar}+{br}i", f"{br}+{ar}i"], f"FOIL: {ans}."))
        for a, b in [(2,3),(3,4),(1,5),(4,2),(5,1),(2,2),(3,1),(1,2),(4,3),(2,4),(3,3),(5,2),(1,4),(2,1),(4,4),(6,1),(1,6),(5,3),(3,5),(2,5),(5,2),(7,1),(1,7),(6,2),(2,6),(4,5),(5,4),(3,6),(6,3),(7,2),(2,7),(8,1),(1,8),(4,1),(1,1),(2,2),(3,3)]:
            result = a*a + b*b
            qs.append((f"({a}+{b}i)({a}-{b}i)=?", str(result), [f"{result}i", str(a*a-b*b), f"{2*a*b}i"], f"= a²+b² = {result}."))
            if len(qs) >= 50: break
            
    elif level == 8:  # Conjugate
        qs.append(("Conjugate of a+bi?", "a-bi", ["a+bi", "-a+bi", "-a-bi"], "Change sign of imaginary."))
        qs.append(("Conjugate notation?", "z̄ or z*", ["z²", "|z|", "1/z"], "z̄ (z-bar)."))
        for a in range(-6, 7):
            for b in range(1, 7):
                z = f"{a}+{b}i"
                conj = f"{a}-{b}i"
                qs.append((f"Conjugate of {z}?", conj, [z, f"{-a}+{b}i", f"{-a}-{b}i"], f"= {conj}."))
                if len(qs) >= 30: break
            if len(qs) >= 30: break
        for a, b in [(2,3),(3,4),(1,2),(4,3),(5,2),(2,1),(3,1),(1,1),(2,2),(4,1),(1,3),(3,2),(5,1),(2,4),(4,2),(1,4),(3,3),(5,3),(2,5),(4,4)]:
            result = a*a + b*b
            qs.append((f"({a}+{b}i)×conjugate=?", str(result), [f"{result}i", str(2*a*b), str(a*a-b*b)], f"z×z̄ = {result}."))
            if len(qs) >= 50: break
            
    elif level == 9:  # Division
        qs.append(("To divide complex?", "Multiply by conjugate of denominator", ["Divide parts", "Add parts", "Subtract"], "Makes denominator real."))
        for a, b, k in [(6,4,2),(9,3,3),(8,4,4),(10,5,5),(6,9,3),(8,12,4),(12,6,2),(15,10,5),(4,8,2),(9,6,3),(12,8,4),(18,6,6),(14,7,7),(16,8,8),(20,10,10),(24,12,12),(18,12,6),(21,14,7),(16,4,4),(20,15,5)]:
            ar, br = a//k, b//k
            qs.append((f"({a}+{b}i)÷{k}=?", f"{ar}+{br}i", [f"{a}+{br}i", f"{ar}+{b}i", f"{ar+br}i"], f"= {ar}+{br}i."))
            if len(qs) >= 28: break
        for a, b in [(3,4),(2,5),(4,1),(1,3),(5,2),(6,1),(2,3),(3,2),(4,3),(1,6),(7,2),(2,7),(5,3),(3,5),(8,1),(1,8),(6,2),(2,6),(4,5),(5,4),(9,2),(2,9),(7,3),(3,7),(6,4),(4,6),(8,3),(3,8),(7,4),(4,7)]:
            ar, br = b, -a
            ans = f"{ar}-{-br}i" if br < 0 else f"{ar}+{br}i"
            qs.append((f"({a}+{b}i)÷i=?", ans, [f"{a}+{b}i", f"-{a}-{b}i", f"{a}i+{b}"], f"= {ans}."))
            if len(qs) >= 50: break
            
    elif level == 10:  # Argand
        qs.append(("What is Argand diagram?", "Graph of complex numbers", ["Calculation", "Equation", "Formula"], "Plots on complex plane."))
        qs.append(("Argand axes?", "Real (horiz), Imaginary (vert)", ["x and y", "Both real", "Both imag"], "Real=horiz, Imag=vert."))
        for a in range(-7, 8):
            for b in range(-7, 8):
                if (a != 0 or b != 0) and len(qs) < 50:
                    z = f"{a}+{b}i" if b >= 0 else f"{a}-{-b}i"
                    if b == 0: z = str(a)
                    if a == 0: z = f"{b}i"
                    qs.append((f"Coords for {z}?", f"({a},{b})", [f"({b},{a})", f"({-a},{b})", f"({a},{-b})"], f"→ ({a},{b})."))
                    
    elif level == 11:  # Modulus
        qs.append(("|a+bi| = ?", "√(a²+b²)", ["a+b", "a²+b²", "|a|+|b|"], "|z| = √(a²+b²)."))
        qs.append(("Modulus notation?", "|z|", ["z̄", "z²", "1/z"], "Absolute value."))
        for a, b, r in [(3,4,5),(5,12,13),(6,8,10),(8,6,10),(4,3,5),(12,5,13),(8,15,17),(15,8,17),(9,12,15),(12,9,15),(7,24,25),(24,7,25),(20,21,29),(21,20,29),(9,40,41)]:
            qs.append((f"|{a}+{b}i|=?", str(r), [str(a+b), str(a*a+b*b), str(r+1)], f"|z| = {r}."))
            if len(qs) >= 20: break
        for a in range(1, 14):
            qs.append((f"|{a}|=?", str(a), [f"{a}i", str(-a), "0"], f"|{a}| = {a}."))
            if len(qs) >= 32: break
        for b in range(1, 14):
            qs.append((f"|{b}i|=?", str(b), [f"-{b}", str(-b), "0"], f"|{b}i| = {b}."))
            if len(qs) >= 48: break
        for a, b in [(-3,4),(3,-4),(-3,-4),(-5,12),(5,-12),(-4,3),(4,-3),(-6,8)]:
            r = int((a*a+b*b)**0.5)
            z = f"{a}+{b}i" if b >= 0 else f"{a}-{-b}i"
            qs.append((f"|{z}|=?", str(r), [str(-r), str(abs(a)+abs(b)), str(abs(a-b))], f"|z| = {r}."))
            if len(qs) >= 50: break
            
    elif level == 12:  # SEC style
        for n in [15,23,32,47,100,101,102,103,200,201,50,51,99,17,29,33,44,55,66,77]:
            r = n % 4
            ans = ["1","i","-1","-i"][r]
            qs.append((f"i^{n}=?", ans, ["1","-1","i","-i"], f"mod 4 = {r}."))
            if len(qs) >= 26: break
        for a, b in [(3,4),(5,12),(8,6),(6,8),(8,15),(15,8),(9,12),(12,9),(4,3),(12,5),(5,12),(7,24)]:
            r = int((a*a+b*b)**0.5)
            qs.append((f"|{a}+{b}i|=?", str(r), [str(a+b), str(a*a+b*b), str(r+1)], f"|z| = {r}."))
            if len(qs) >= 36: break
        for a, b in [(2,3),(4,1),(3,4),(5,2),(1,6),(7,3),(2,5),(4,4),(6,2),(3,5),(8,1),(2,7),(1,1),(3,3),(5,5),(6,1),(1,2),(2,2),(4,2)]:
            qs.append((f"Conjugate of {a}+{b}i?", f"{a}-{b}i", [f"{a}+{b}i", f"-{a}+{b}i", f"-{a}-{b}i"], f"= {a}-{b}i."))
            if len(qs) >= 50: break
    
    return qs[:50]

def generate_all():
    all_q = []
    for level in range(1, 13):
        raw = gen_level(level)
        name, band = LEVEL_CONFIG[level]
        qs = []
        for item in raw:
            text, correct, dists, exp = item
            opts, idx = shuffle_options(correct, dists)
            qs.append({'text': text, 'opts': opts, 'idx': idx, 'exp': exp, 'level': level, 'band': band})
        all_q.extend(qs)
        print(f"Level {level:2d}: {len(qs):3d} - {name}")
    return all_q

def generate_sql(questions):
    lines = [
        "-- LC OL Complex Numbers - 600 Questions",
        f"-- Total: {len(questions)}",
        "",
        f"INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)",
        f"VALUES ('{TOPIC_ID}', 'Complex Numbers', {STRAND_ID}, '🔢', 14, 1);",
        "",
        f"DELETE FROM questions_adaptive WHERE topic = '{TOPIC_ID}';",
        "",
    ]
    for q in questions:
        txt = q['text'].replace("'", "''")
        a = q['opts'][0].replace("'", "''") if isinstance(q['opts'][0], str) else str(q['opts'][0])
        b = q['opts'][1].replace("'", "''") if isinstance(q['opts'][1], str) else str(q['opts'][1])
        c = q['opts'][2].replace("'", "''") if isinstance(q['opts'][2], str) else str(q['opts'][2])
        d = q['opts'][3].replace("'", "''") if isinstance(q['opts'][3], str) else str(q['opts'][3])
        exp = q['exp'].replace("'", "''")
        sql = f"INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode) VALUES ('{TOPIC_ID}', '{txt}', '{a}', '{b}', '{c}', '{d}', {q['idx']}, '{exp}', {q['level']}, '{q['band']}', 'adaptive');"
        lines.append(sql)
    lines.append("")
    lines.append(f"SELECT COUNT(*) as total FROM questions_adaptive WHERE topic = '{TOPIC_ID}';")
    return '\n'.join(lines)

if __name__ == "__main__":
    print("="*60)
    print("LC OL Complex Numbers - 600 Questions")
    print("="*60 + "\n")
    questions = generate_all()
    print(f"\nTotal: {len(questions)}\n")
    sql = generate_sql(questions)
    with open('lc_ol_complex_600.sql', 'w') as f:
        f.write(sql)
    print(f"Saved: lc_ol_complex_600.sql ({len(sql):,} chars)")
