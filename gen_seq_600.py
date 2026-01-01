#!/usr/bin/env python3
"""
LC Ordinary Level Sequences - GUARANTEED 600 Questions
======================================================
50 questions per level × 12 levels = 600 questions
"""

import random

TOPIC_ID = 'lc_ol_sequences'
STRAND_ID = 11

LEVEL_CONFIG = {
    1: ("Recognising Patterns", "Foundation"),
    2: ("Finding Common Difference", "Foundation"),
    3: ("Next Terms", "Foundation"),
    4: ("Tₙ Formula Basics", "Developing"),
    5: ("Using Tₙ Formula", "Developing"),
    6: ("Finding n", "Developing"),
    7: ("Sum Formula Sₙ", "Proficient"),
    8: ("Applied Sequences", "Proficient"),
    9: ("Working Backwards", "Proficient"),
    10: ("Complex Applications", "Advanced"),
    11: ("Proof & Reasoning", "Advanced"),
    12: ("SEC Exam Style", "Advanced"),
}

def shuffle_options(correct, distractors):
    options = [correct] + distractors[:3]
    random.shuffle(options)
    return options, options.index(correct)

def generate_level_1():
    """Recognising Patterns"""
    questions = []
    
    # Is it arithmetic? YES - various a and d values
    for a in [1, 2, 3, 4, 5, 7, 10, 12, 15, 20]:
        for d in [2, 3, 4, 5, 6, 7]:
            seq = f"{a}, {a+d}, {a+2*d}, {a+3*d}, ..."
            opts, idx = shuffle_options("Yes", ["No", "Cannot tell", "Sometimes"])
            questions.append({
                'text': f"Is {seq} an arithmetic sequence?",
                'opts': opts, 'idx': idx,
                'exp': f"Yes. d = {d}."
            })
            if len(questions) >= 20:
                break
        if len(questions) >= 20:
            break
    
    # Decreasing sequences
    for a in [50, 40, 30, 25, 20]:
        for d in [3, 4, 5, 6]:
            seq = f"{a}, {a-d}, {a-2*d}, {a-3*d}, ..."
            opts, idx = shuffle_options("Yes", ["No", "Cannot tell", "Only if positive"])
            questions.append({
                'text': f"Is {seq} an arithmetic sequence?",
                'opts': opts, 'idx': idx,
                'exp': f"Yes. d = -{d}."
            })
            if len(questions) >= 30:
                break
        if len(questions) >= 30:
            break
    
    # NOT arithmetic
    non_arith = [
        ("2, 4, 8, 16", "geometric ×2"), ("1, 4, 9, 16", "squares"),
        ("3, 9, 27, 81", "geometric ×3"), ("1, 1, 2, 3, 5", "Fibonacci"),
        ("1, 8, 27, 64", "cubes"), ("2, 6, 18, 54", "geometric ×3"),
    ]
    for seq, reason in non_arith:
        opts, idx = shuffle_options("No", ["Yes", "Cannot tell", "Sometimes"])
        questions.append({
            'text': f"Is {seq}, ... an arithmetic sequence?",
            'opts': opts, 'idx': idx,
            'exp': f"No. This is {reason}."
        })
    
    # Find first term
    for a in range(1, 15):
        d = random.randint(3, 7)
        seq = f"{a}, {a+d}, {a+2*d}, {a+3*d}"
        opts, idx = shuffle_options(str(a), [str(a+d), str(d), str(a+1)])
        questions.append({
            'text': f"What is the first term of: {seq}, ...?",
            'opts': opts, 'idx': idx,
            'exp': f"First term a = {a}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_2():
    """Finding Common Difference"""
    questions = []
    
    # Positive d
    for a in range(1, 15):
        for d in range(2, 9):
            seq = f"{a}, {a+d}, {a+2*d}, {a+3*d}"
            opts, idx = shuffle_options(str(d), [str(d+1), str(d-1), str(d+2)])
            questions.append({
                'text': f"Find d for: {seq}, ...",
                'opts': opts, 'idx': idx,
                'exp': f"d = {a+d} - {a} = {d}."
            })
            if len(questions) >= 25:
                break
        if len(questions) >= 25:
            break
    
    # Negative d
    for a in [30, 40, 50, 60, 80, 100]:
        for d in [2, 3, 4, 5, 6, 7, 8]:
            seq = f"{a}, {a-d}, {a-2*d}, {a-3*d}"
            opts, idx = shuffle_options(str(-d), [str(d), str(-d-1), str(-d+1)])
            questions.append({
                'text': f"Find d for: {seq}, ...",
                'opts': opts, 'idx': idx,
                'exp': f"d = {a-d} - {a} = {-d}."
            })
            if len(questions) >= 40:
                break
        if len(questions) >= 40:
            break
    
    # Given T1 and T2
    for a in range(2, 12):
        d = random.randint(3, 8)
        t2 = a + d
        opts, idx = shuffle_options(str(d), [str(d+1), str(d-1), str(a)])
        questions.append({
            'text': f"T₁ = {a}, T₂ = {t2}. Find d.",
            'opts': opts, 'idx': idx,
            'exp': f"d = {t2} - {a} = {d}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_3():
    """Next Terms"""
    questions = []
    
    # Find next term - increasing
    for a in range(1, 12):
        for d in range(2, 8):
            t4 = a + 3*d
            t5 = a + 4*d
            seq = f"{a}, {a+d}, {a+2*d}, {t4}"
            opts, idx = shuffle_options(str(t5), [str(t5+1), str(t5-1), str(t5+d)])
            questions.append({
                'text': f"Next term: {seq}, __",
                'opts': opts, 'idx': idx,
                'exp': f"d = {d}. Next = {t4} + {d} = {t5}."
            })
            if len(questions) >= 25:
                break
        if len(questions) >= 25:
            break
    
    # Decreasing
    for a in [40, 50, 60, 70, 80]:
        for d in [3, 4, 5, 6]:
            t4 = a - 3*d
            t5 = a - 4*d
            seq = f"{a}, {a-d}, {a-2*d}, {t4}"
            opts, idx = shuffle_options(str(t5), [str(t5+1), str(t5-1), str(t5+d)])
            questions.append({
                'text': f"Next term: {seq}, __",
                'opts': opts, 'idx': idx,
                'exp': f"d = -{d}. Next = {t4} - {d} = {t5}."
            })
            if len(questions) >= 40:
                break
        if len(questions) >= 40:
            break
    
    # Given a and d, write sequence
    for a in range(1, 12):
        d = random.randint(2, 6)
        ans = f"{a}, {a+d}, {a+2*d}, {a+3*d}"
        opts, idx = shuffle_options(ans, [f"{a}, {a+1}, {a+2}, {a+3}", f"{d}, {2*d}, {3*d}, {4*d}", f"{a+d}, {a+2*d}, {a+3*d}, {a+4*d}"])
        questions.append({
            'text': f"Write first 4 terms: a = {a}, d = {d}.",
            'opts': opts, 'idx': idx,
            'exp': f"Start at {a}, add {d}: {ans}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_4():
    """Tₙ Formula Basics"""
    questions = []
    
    # Formula recognition
    opts, idx = shuffle_options("Tₙ = a + (n-1)d", ["Tₙ = a + nd", "Tₙ = an + d", "Tₙ = a × dⁿ"])
    questions.append({
        'text': "Formula for nth term of arithmetic sequence?",
        'opts': opts, 'idx': idx,
        'exp': "Tₙ = a + (n-1)d."
    })
    
    # Find T5
    for a in range(1, 12):
        for d in range(2, 7):
            t5 = a + 4*d
            opts, idx = shuffle_options(str(t5), [str(t5+1), str(t5-1), str(t5+d)])
            questions.append({
                'text': f"Find T₅: a = {a}, d = {d}.",
                'opts': opts, 'idx': idx,
                'exp': f"T₅ = {a} + 4×{d} = {t5}."
            })
            if len(questions) >= 20:
                break
        if len(questions) >= 20:
            break
    
    # Find T10
    for a in range(1, 10):
        for d in range(2, 5):
            t10 = a + 9*d
            opts, idx = shuffle_options(str(t10), [str(t10+d), str(t10-d), str(t10+1)])
            questions.append({
                'text': f"Find T₁₀: a = {a}, d = {d}.",
                'opts': opts, 'idx': idx,
                'exp': f"T₁₀ = {a} + 9×{d} = {t10}."
            })
            if len(questions) >= 35:
                break
        if len(questions) >= 35:
            break
    
    # From sequence find T6
    for a in range(2, 12):
        for d in range(3, 7):
            t6 = a + 5*d
            seq = f"{a}, {a+d}, {a+2*d}, ..."
            opts, idx = shuffle_options(str(t6), [str(t6+1), str(t6-1), str(t6+d)])
            questions.append({
                'text': f"For {seq}, find T₆.",
                'opts': opts, 'idx': idx,
                'exp': f"a={a}, d={d}. T₆ = {a}+5×{d} = {t6}."
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    # Find T8
    for a in range(1, 8):
        for d in range(2, 5):
            t8 = a + 7*d
            opts, idx = shuffle_options(str(t8), [str(t8+1), str(t8-1), str(t8+d)])
            questions.append({
                'text': f"Find T₈: a = {a}, d = {d}.",
                'opts': opts, 'idx': idx,
                'exp': f"T₈ = {a} + 7×{d} = {t8}."
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_5():
    """Using Tₙ Formula - larger n"""
    questions = []
    
    # T20
    for a in range(1, 8):
        for d in range(2, 5):
            t20 = a + 19*d
            opts, idx = shuffle_options(str(t20), [str(t20+d), str(t20-d), str(t20+1)])
            questions.append({
                'text': f"Find T₂₀: a = {a}, d = {d}.",
                'opts': opts, 'idx': idx,
                'exp': f"T₂₀ = {a} + 19×{d} = {t20}."
            })
            if len(questions) >= 15:
                break
        if len(questions) >= 15:
            break
    
    # T15
    for a in range(2, 8):
        for d in range(3, 6):
            t15 = a + 14*d
            opts, idx = shuffle_options(str(t15), [str(t15+d), str(t15-d), str(t15+1)])
            questions.append({
                'text': f"Find T₁₅: a = {a}, d = {d}.",
                'opts': opts, 'idx': idx,
                'exp': f"T₁₅ = {a} + 14×{d} = {t15}."
            })
            if len(questions) >= 28:
                break
        if len(questions) >= 28:
            break
    
    # T100
    for a in range(1, 6):
        for d in range(1, 4):
            t100 = a + 99*d
            opts, idx = shuffle_options(str(t100), [str(t100+1), str(t100-1), str(t100+d)])
            questions.append({
                'text': f"Find T₁₀₀: a = {a}, d = {d}.",
                'opts': opts, 'idx': idx,
                'exp': f"T₁₀₀ = {a} + 99×{d} = {t100}."
            })
            if len(questions) >= 40:
                break
        if len(questions) >= 40:
            break
    
    # Various n
    for a in range(2, 8):
        for d in range(2, 5):
            for n in [12, 18, 25, 30]:
                tn = a + (n-1)*d
                opts, idx = shuffle_options(str(tn), [str(tn+d), str(tn-d), str(tn+1)])
                questions.append({
                    'text': f"Find T{n}: a = {a}, d = {d}.",
                    'opts': opts, 'idx': idx,
                    'exp': f"T{n} = {a} + {n-1}×{d} = {tn}."
                })
                if len(questions) >= 50:
                    break
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_6():
    """Finding n"""
    questions = []
    
    # Which term equals X?
    for a in range(2, 8):
        for d in range(2, 5):
            for n in range(8, 18):
                tn = a + (n-1)*d
                opts, idx = shuffle_options(str(n), [str(n+1), str(n-1), str(n+2)])
                questions.append({
                    'text': f"a = {a}, d = {d}. Which term equals {tn}?",
                    'opts': opts, 'idx': idx,
                    'exp': f"{tn} = {a} + (n-1)×{d} → n = {n}."
                })
                if len(questions) >= 30:
                    break
            if len(questions) >= 30:
                break
        if len(questions) >= 30:
            break
    
    # Is X a term? YES
    for a in range(3, 8):
        for d in range(3, 6):
            n = random.randint(6, 12)
            tn = a + (n-1)*d
            ans = f"Yes, T{n}"
            opts, idx = shuffle_options(ans, ["No", f"Yes, T{n+1}", f"Yes, T{n-1}"])
            questions.append({
                'text': f"Is {tn} a term in a={a}, d={d}?",
                'opts': opts, 'idx': idx,
                'exp': f"Yes, T{n}."
            })
            if len(questions) >= 42:
                break
        if len(questions) >= 42:
            break
    
    # Is X a term? NO
    for a in range(2, 6):
        for d in range(4, 7):
            val = a + random.randint(5, 10)*d + 1
            opts, idx = shuffle_options("No", [f"Yes, T{random.randint(5,10)}", f"Yes, T{random.randint(3,8)}", "Cannot tell"])
            questions.append({
                'text': f"Is {val} a term in a={a}, d={d}?",
                'opts': opts, 'idx': idx,
                'exp': f"No. {val} = {a} + (n-1)×{d} gives non-integer n."
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_7():
    """Sum Formula Sₙ"""
    questions = []
    
    # Formula
    opts, idx = shuffle_options("Sₙ = n/2[2a + (n-1)d]", ["Sₙ = n(a + d)", "Sₙ = an + d", "Sₙ = n²d"])
    questions.append({
        'text': "Formula for sum of n terms of AP?",
        'opts': opts, 'idx': idx,
        'exp': "Sₙ = n/2[2a + (n-1)d]."
    })
    
    # Calculate Sn
    for a in range(1, 6):
        for d in range(2, 4):
            for n in range(5, 12):
                sn = n * (2*a + (n-1)*d) // 2
                opts, idx = shuffle_options(str(sn), [str(sn+10), str(sn-10), str(sn+n)])
                questions.append({
                    'text': f"Find S{n}: a = {a}, d = {d}.",
                    'opts': opts, 'idx': idx,
                    'exp': f"S{n} = {n}/2[2×{a}+{n-1}×{d}] = {sn}."
                })
                if len(questions) >= 30:
                    break
            if len(questions) >= 30:
                break
        if len(questions) >= 30:
            break
    
    # Sum of natural numbers
    for n in [10, 15, 20, 25, 30, 50, 100]:
        sn = n * (n + 1) // 2
        opts, idx = shuffle_options(str(sn), [str(sn+n), str(sn-n), str(n*n)])
        questions.append({
            'text': f"Sum of first {n} positive integers?",
            'opts': opts, 'idx': idx,
            'exp': f"{n}×{n+1}/2 = {sn}."
        })
    
    # From sequence
    for a in range(2, 7):
        for d in range(3, 5):
            for n in range(6, 10):
                sn = n * (2*a + (n-1)*d) // 2
                seq = f"{a}, {a+d}, {a+2*d}, ..."
                opts, idx = shuffle_options(str(sn), [str(sn+10), str(sn-10), str(sn+n)])
                questions.append({
                    'text': f"Find S{n} for: {seq}",
                    'opts': opts, 'idx': idx,
                    'exp': f"a={a}, d={d}. S{n} = {sn}."
                })
                if len(questions) >= 50:
                    break
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_8():
    """Applied Sequences"""
    questions = []
    
    # Salary
    for start in [25000, 28000, 30000, 32000, 35000, 40000]:
        for inc in [1000, 1500, 2000, 2500]:
            for year in [5, 8, 10, 12]:
                tn = start + (year-1)*inc
                ans = f"€{tn:,}"
                opts, idx = shuffle_options(ans, [f"€{tn+inc:,}", f"€{tn-inc:,}", f"€{start+year*inc:,}"])
                questions.append({
                    'text': f"Start €{start:,}, +€{inc:,}/year. Year {year} salary?",
                    'opts': opts, 'idx': idx,
                    'exp': f"T{year} = {start}+{year-1}×{inc} = {tn}."
                })
                if len(questions) >= 20:
                    break
            if len(questions) >= 20:
                break
        if len(questions) >= 20:
            break
    
    # Seating/stacking
    for front in [10, 12, 15, 18, 20]:
        for d in [2, 3, 4]:
            for n in [8, 10, 12, 15]:
                tn = front + (n-1)*d
                opts, idx = shuffle_options(str(tn), [str(tn+d), str(tn-d), str(tn+1)])
                questions.append({
                    'text': f"Row 1: {front} seats, +{d}/row. Row {n}?",
                    'opts': opts, 'idx': idx,
                    'exp': f"T{n} = {front}+{n-1}×{d} = {tn}."
                })
                if len(questions) >= 35:
                    break
            if len(questions) >= 35:
                break
        if len(questions) >= 35:
            break
    
    # Total seating
    for front in [12, 15, 18, 20]:
        for d in [2, 3]:
            for rows in [10, 12, 15]:
                sn = rows * (2*front + (rows-1)*d) // 2
                opts, idx = shuffle_options(str(sn), [str(sn+10), str(sn-10), str(sn+rows)])
                questions.append({
                    'text': f"Theatre: {front} in row 1, +{d}/row. Total in {rows} rows?",
                    'opts': opts, 'idx': idx,
                    'exp': f"S{rows} = {sn}."
                })
                if len(questions) >= 50:
                    break
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_9():
    """Working Backwards"""
    questions = []
    
    # Given Tn and d, find a
    for d in range(2, 5):
        for n in range(8, 14):
            a = random.randint(2, 8)
            tn = a + (n-1)*d
            opts, idx = shuffle_options(str(a), [str(a+1), str(a-1), str(a+d)])
            questions.append({
                'text': f"T{n} = {tn}, d = {d}. Find a.",
                'opts': opts, 'idx': idx,
                'exp': f"a = {tn} - {n-1}×{d} = {a}."
            })
            if len(questions) >= 18:
                break
        if len(questions) >= 18:
            break
    
    # Given Tn and a, find d
    for a in range(2, 7):
        for n in range(8, 12):
            d = random.randint(2, 5)
            tn = a + (n-1)*d
            opts, idx = shuffle_options(str(d), [str(d+1), str(d-1), str(d+2)])
            questions.append({
                'text': f"a = {a}, T{n} = {tn}. Find d.",
                'opts': opts, 'idx': idx,
                'exp': f"d = ({tn}-{a})/{n-1} = {d}."
            })
            if len(questions) >= 32:
                break
        if len(questions) >= 32:
            break
    
    # Two terms given
    for a in range(2, 8):
        d = random.randint(2, 5)
        n1, n2 = 3, 7
        t1, t2 = a + (n1-1)*d, a + (n2-1)*d
        opts, idx = shuffle_options(str(d), [str(d+1), str(d-1), str(d+2)])
        questions.append({
            'text': f"T{n1} = {t1}, T{n2} = {t2}. Find d.",
            'opts': opts, 'idx': idx,
            'exp': f"d = ({t2}-{t1})/{n2-n1} = {d}."
        })
        if len(questions) >= 42:
            break
    
    # Find a from two terms
    for d in range(2, 6):
        for a in range(2, 10):
            n1, n2 = 2, 5
            t1, t2 = a + (n1-1)*d, a + (n2-1)*d
            opts, idx = shuffle_options(str(a), [str(a+1), str(a-1), str(t1)])
            questions.append({
                'text': f"T{n1} = {t1}, T{n2} = {t2}. Find a.",
                'opts': opts, 'idx': idx,
                'exp': f"d={d}, a = {t1}-{d} = {a}."
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    # Given Sn and d, find a
    for d in range(2, 4):
        for n in range(6, 10):
            a = random.randint(1, 5)
            sn = n * (2*a + (n-1)*d) // 2
            opts, idx = shuffle_options(str(a), [str(a+1), str(a-1), str(a+2)])
            questions.append({
                'text': f"S{n} = {sn}, d = {d}. Find a.",
                'opts': opts, 'idx': idx,
                'exp': f"a = {a}."
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_10():
    """Complex Applications"""
    questions = []
    
    # Sum exceeds value
    for a, d, target in [(2, 3, 100), (3, 4, 150), (1, 5, 120), (5, 2, 80), (4, 3, 100), (2, 4, 90)]:
        n = 1
        while n * (2*a + (n-1)*d) // 2 <= target:
            n += 1
        opts, idx = shuffle_options(str(n), [str(n-1), str(n+1), str(n+2)])
        questions.append({
            'text': f"a={a}, d={d}. How many terms for sum > {target}?",
            'opts': opts, 'idx': idx,
            'exp': f"Need {n} terms."
        })
    
    # Given Sn, find a
    for d in range(2, 4):
        for n in range(10, 14):
            a = random.randint(1, 5)
            sn = n * (2*a + (n-1)*d) // 2
            opts, idx = shuffle_options(str(a), [str(a+1), str(a-1), str(a+2)])
            questions.append({
                'text': f"S{n} = {sn}, d = {d}. Find a.",
                'opts': opts, 'idx': idx,
                'exp': f"a = {a}."
            })
            if len(questions) >= 20:
                break
        if len(questions) >= 20:
            break
    
    # Middle term from sum
    for x in range(4, 12):
        d = random.randint(2, 4)
        t1, t2, t3 = x-d, x, x+d
        total = t1 + t2 + t3
        opts, idx = shuffle_options(str(x), [str(x+1), str(x-1), str(t1)])
        questions.append({
            'text': f"3 AP terms sum to {total}. Middle term?",
            'opts': opts, 'idx': idx,
            'exp': f"3x = {total} → x = {x}."
        })
        if len(questions) >= 32:
            break
    
    # Insert means
    for start, end, count in [(2, 14, 2), (3, 27, 3), (5, 25, 3), (10, 50, 4), (4, 28, 5), (6, 30, 3)]:
        d = (end - start) // (count + 1)
        means = [start + i*d for i in range(1, count+1)]
        ans = ", ".join(map(str, means))
        opts, idx = shuffle_options(ans, [", ".join(map(str, [m+1 for m in means])), 
                                          ", ".join(map(str, [m-1 for m in means])),
                                          ", ".join(map(str, [m+d for m in means]))])
        questions.append({
            'text': f"Insert {count} means between {start} and {end}.",
            'opts': opts, 'idx': idx,
            'exp': f"d={d}. Means: {ans}."
        })
        if len(questions) >= 42:
            break
    
    # Given Sn find d
    for a in range(1, 6):
        for n in range(8, 14):
            d = random.randint(2, 5)
            sn = n * (2*a + (n-1)*d) // 2
            opts, idx = shuffle_options(str(d), [str(d+1), str(d-1), str(d+2)])
            questions.append({
                'text': f"a = {a}, S{n} = {sn}. Find d.",
                'opts': opts, 'idx': idx,
                'exp': f"d = {d}."
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_11():
    """Proof & Reasoning"""
    questions = []
    
    # Sum formulas
    formulas = [
        ("Sum of first n odd numbers", "n²", ["n(n+1)", "2n", "n(n-1)"]),
        ("Sum of first n even numbers", "n(n+1)", ["n²", "2n²", "n(n-1)"]),
        ("Sum 1+2+3+...+n", "n(n+1)/2", ["n²/2", "n(n-1)/2", "(n+1)/2"]),
    ]
    for q, ans, wrongs in formulas:
        opts, idx = shuffle_options(ans, wrongs)
        questions.append({
            'text': f"{q} = ?",
            'opts': opts, 'idx': idx,
            'exp': f"{ans}."
        })
    
    # Tn from Sn
    sn_formulas = [
        ("Sₙ = 3n² + 2n", "6n - 1"), ("Sₙ = 2n² + n", "4n - 1"),
        ("Sₙ = n² + 3n", "2n + 2"), ("Sₙ = 4n² - n", "8n - 5"),
        ("Sₙ = 2n² + 3n", "4n + 1"), ("Sₙ = 3n² - n", "6n - 4"),
    ]
    for sn, tn in sn_formulas:
        opts, idx = shuffle_options(tn, ["n² - 1", "2n + 1", "n - 1"])
        questions.append({
            'text': f"If {sn}, find Tₙ.",
            'opts': opts, 'idx': idx,
            'exp': f"Tₙ = Sₙ - Sₙ₋₁ = {tn}."
        })
    
    # d from Sn
    for mult in range(2, 8):
        d = 2 * mult
        opts, idx = shuffle_options(str(d), [str(d+2), str(d-2), str(mult)])
        questions.append({
            'text': f"If Sₙ = {mult}n² + {mult}n, find d.",
            'opts': opts, 'idx': idx,
            'exp': f"d = {d}."
        })
    
    # AP properties
    properties = [
        ("T₃ + T₇", "2T₅"), ("T₂ + T₈", "2T₅"), ("T₁ + T₉", "2T₅"),
        ("T₄ + T₆", "2T₅"), ("T₁ + T₅", "2T₃"), ("T₂ + T₆", "2T₄"),
    ]
    for lhs, ans in properties:
        opts, idx = shuffle_options(ans, ["T₄ + T₆", "3T₅", "T₃ + T₆"])
        questions.append({
            'text': f"In AP, {lhs} = ?",
            'opts': opts, 'idx': idx,
            'exp': f"{ans}."
        })
    
    # T100 for various sequences
    for a, d in [(2, 3), (5, 4), (1, 6), (3, 5), (4, 2), (7, 3)]:
        t100 = a + 99*d
        opts, idx = shuffle_options(str(t100), [str(t100+1), str(t100-1), str(t100+d)])
        questions.append({
            'text': f"a={a}, d={d}. Find T₁₀₀.",
            'opts': opts, 'idx': idx,
            'exp': f"T₁₀₀ = {a}+99×{d} = {t100}."
        })
    
    # If p,q,r in AP
    for _ in range(5):
        opts, idx = shuffle_options("r - q", ["p - r", "q - r", "r - p"])
        questions.append({
            'text': "If p, q, r in AP, q - p = ?",
            'opts': opts, 'idx': idx,
            'exp': "q - p = r - q (common difference)."
        })
    
    # T50
    for a in range(1, 10):
        for d in range(2, 6):
            t50 = a + 49*d
            opts, idx = shuffle_options(str(t50), [str(t50+d), str(t50-d), str(t50+1)])
            questions.append({
                'text': f"a={a}, d={d}. Find T₅₀.",
                'opts': opts, 'idx': idx,
                'exp': f"T₅₀ = {a}+49×{d} = {t50}."
            })
            if len(questions) >= 45:
                break
        if len(questions) >= 45:
            break
    
    # Sum properties
    for n in [10, 20, 30, 40, 50]:
        sn = n * (n + 1) // 2
        opts, idx = shuffle_options(str(sn), [str(sn+n), str(sn-n), str(n*n)])
        questions.append({
            'text': f"Sum 1+2+3+...+{n} = ?",
            'opts': opts, 'idx': idx,
            'exp': f"{n}×{n+1}/2 = {sn}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_12():
    """SEC Exam Style"""
    questions = []
    
    # Savings word problems
    savings = [
        ("Pat saves €5 week 1, €8 week 2, €11 week 3", 5, 3, 20),
        ("Mary saves €10 month 1, adds €5 each month", 10, 5, 12),
        ("John puts €20 week 1, adds €4 each week", 20, 4, 15),
        ("Lisa saves €15 day 1, adds €3 daily", 15, 3, 10),
        ("Tom saves €8 week 1, adds €6 each week", 8, 6, 8),
    ]
    for desc, a, d, n in savings:
        # Find Tn
        tn = a + (n-1)*d
        opts, idx = shuffle_options(f"€{tn}", [f"€{tn+d}", f"€{tn-d}", f"€{tn+1}"])
        questions.append({
            'text': f"{desc}. Amount in week/day {n}?",
            'opts': opts, 'idx': idx,
            'exp': f"T{n} = {a}+{n-1}×{d} = {tn}."
        })
        # Find Sn
        sn = n * (2*a + (n-1)*d) // 2
        opts, idx = shuffle_options(f"€{sn}", [f"€{sn+50}", f"€{sn-50}", f"€{sn+n}"])
        questions.append({
            'text': f"{desc}. Total after {n} periods?",
            'opts': opts, 'idx': idx,
            'exp': f"S{n} = {sn}."
        })
    
    # Cinema problems
    for front, d, rows in [(12, 3, 15), (15, 2, 20), (10, 4, 12), (18, 2, 18)]:
        sn = rows * (2*front + (rows-1)*d) // 2
        opts, idx = shuffle_options(str(sn), [str(sn+rows), str(sn-rows), str(sn+10)])
        questions.append({
            'text': f"Cinema: {rows} rows, {front} seats row 1, +{d}/row. Total?",
            'opts': opts, 'idx': idx,
            'exp': f"S{rows} = {sn}."
        })
    
    # From two terms
    for a, d in [(7, 3), (4, 5), (10, 2), (3, 6), (8, 4)]:
        t10 = a + 9*d
        t25 = a + 24*d
        opts, idx = shuffle_options(str(t25), [str(t25+d), str(t25-d), str(t25+1)])
        questions.append({
            'text': f"T₁ = {a}, T₁₀ = {t10}. Find T₂₅.",
            'opts': opts, 'idx': idx,
            'exp': f"d={d}. T₂₅ = {a}+24×{d} = {t25}."
        })
    
    # Find n given Sn
    for a, d in [(2, 3), (3, 4), (5, 2), (4, 3)]:
        n = 10
        sn = n * (2*a + (n-1)*d) // 2
        opts, idx = shuffle_options(str(n), [str(n-1), str(n+1), str(n+2)])
        questions.append({
            'text': f"a={a}, d={d}. Find n if Sₙ = {sn}.",
            'opts': opts, 'idx': idx,
            'exp': f"n = {n}."
        })
    
    # Log stacking
    opts, idx = shuffle_options("325", ["300", "350", "275"])
    questions.append({
        'text': "Logs: 25 bottom, 24 next...1 top. Total?",
        'opts': opts, 'idx': idx,
        'exp': "S₂₅ = 25×26/2 = 325."
    })
    
    # Not arithmetic
    opts, idx = shuffle_options("Geometric", ["Arithmetic", "Neither", "Both"])
    questions.append({
        'text': "10m, 8m, 6.4m, 5.12m... bounce heights. Type?",
        'opts': opts, 'idx': idx,
        'exp': "Ratio 0.8 = geometric."
    })
    
    # Product problems
    for a in range(5, 15):
        d = random.randint(2, 5)
        t1, t2, t3 = a-d, a, a+d
        total = t1 + t2 + t3
        opts, idx = shuffle_options(str(a), [str(a+1), str(a-1), str(t1)])
        questions.append({
            'text': f"3 AP terms sum to {total}. Middle term?",
            'opts': opts, 'idx': idx,
            'exp': f"3a = {total} → a = {a}."
        })
        if len(questions) >= 40:
            break
    
    # More savings problems
    for start, inc in [(25, 5), (30, 10), (50, 15), (40, 8), (60, 12)]:
        for n in [10, 12, 15]:
            sn = n * (2*start + (n-1)*inc) // 2
            opts, idx = shuffle_options(f"€{sn}", [f"€{sn+50}", f"€{sn-50}", f"€{sn+n}"])
            questions.append({
                'text': f"Save €{start} week 1, +€{inc}/week. Total in {n} weeks?",
                'opts': opts, 'idx': idx,
                'exp': f"S{n} = {sn}."
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]


def generate_all():
    all_q = []
    generators = [generate_level_1, generate_level_2, generate_level_3, generate_level_4,
                  generate_level_5, generate_level_6, generate_level_7, generate_level_8,
                  generate_level_9, generate_level_10, generate_level_11, generate_level_12]
    
    for level, gen in enumerate(generators, 1):
        qs = gen()
        name, band = LEVEL_CONFIG[level]
        for q in qs:
            q['level'] = level
            q['band'] = band
        all_q.extend(qs)
        print(f"Level {level:2d}: {len(qs):3d} - {name}")
    
    return all_q


def generate_sql(questions):
    lines = [
        "-- LC OL Sequences - 600 Questions",
        f"-- Total: {len(questions)}",
        "",
        "-- Create topic",
        f"INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)",
        f"VALUES ('{TOPIC_ID}', 'Sequences', {STRAND_ID}, '🔢', 8, 1);",
        "",
        "-- Clear existing",
        f"DELETE FROM questions_adaptive WHERE topic = '{TOPIC_ID}';",
        "",
    ]
    
    for q in questions:
        txt = q['text'].replace("'", "''")
        a = q['opts'][0].replace("'", "''")
        b = q['opts'][1].replace("'", "''")
        c = q['opts'][2].replace("'", "''")
        d = q['opts'][3].replace("'", "''")
        exp = q['exp'].replace("'", "''")
        
        sql = f"INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode) VALUES ('{TOPIC_ID}', '{txt}', '{a}', '{b}', '{c}', '{d}', {q['idx']}, '{exp}', {q['level']}, '{q['band']}', 'adaptive');"
        lines.append(sql)
    
    lines.append("")
    lines.append(f"SELECT COUNT(*) as total FROM questions_adaptive WHERE topic = '{TOPIC_ID}';")
    
    return '\n'.join(lines)


if __name__ == "__main__":
    print("="*60)
    print("LC OL Sequences - 600 Questions Generator")
    print("="*60 + "\n")
    
    questions = generate_all()
    print(f"\nTotal: {len(questions)}\n")
    
    sql = generate_sql(questions)
    with open('lc_ol_sequences_600.sql', 'w') as f:
        f.write(sql)
    
    print(f"Saved: lc_ol_sequences_600.sql ({len(sql):,} chars)")
