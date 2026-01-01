#!/usr/bin/env python3
"""
AgentMath - Probability Topic Generator v1
SEC Junior Cycle Mathematics - 600 questions (50 x 12 levels)
"""

import random
import sqlite3
import os
from fractions import Fraction
import math

TOPIC = 'probability'
MODE = 'jc_exam'
QUESTIONS_PER_LEVEL = 50

COLOURS = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

def make_options(correct, wrong_set):
    """Create 4 unique options from correct answer and a set of wrong answers"""
    wrong_set.discard(correct)
    wrongs = list(wrong_set)
    while len(wrongs) < 3:
        w = str(Fraction(random.randint(1, 9), 10))
        if w != correct and w not in wrongs:
            wrongs.append(w)
    options = [correct] + wrongs[:3]
    random.shuffle(options)
    return options, options.index(correct)

def spinner_svg(n, cols):
    angle = 360 / n
    svg = '<svg viewBox="0 0 100 100" width="100">'
    cmap = {'red': '#ef4444', 'blue': '#3b82f6', 'green': '#22c55e', 'yellow': '#eab308', 'orange': '#f97316', 'purple': '#8b5cf6', 'white': '#f1f5f9'}
    for i in range(n):
        s, e = math.radians(i * angle - 90), math.radians((i + 1) * angle - 90)
        x1, y1 = 50 + 40 * math.cos(s), 50 + 40 * math.sin(s)
        x2, y2 = 50 + 40 * math.cos(e), 50 + 40 * math.sin(e)
        fill = cmap.get(cols[i % len(cols)], '#6b7280')
        svg += f'<path d="M50,50 L{x1:.1f},{y1:.1f} A40,40 0 0,1 {x2:.1f},{y2:.1f} Z" fill="{fill}" stroke="#374151"/>'
    svg += '<circle cx="50" cy="50" r="5" fill="#374151"/></svg>'
    return svg

def dice_svg(n=None):
    svg = '<svg viewBox="0 0 50 50" width="50"><rect x="5" y="5" width="40" height="40" rx="6" fill="white" stroke="#374151" stroke-width="2"/>'
    dots = {1: [(25,25)], 2: [(17,17),(33,33)], 3: [(17,17),(25,25),(33,33)], 4: [(17,17),(33,17),(17,33),(33,33)], 5: [(17,17),(33,17),(25,25),(17,33),(33,33)], 6: [(17,17),(33,17),(17,25),(33,25),(17,33),(33,33)]}
    if n in dots:
        for x, y in dots[n]:
            svg += f'<circle cx="{x}" cy="{y}" r="4" fill="#1f2937"/>'
    return svg + '</svg>'

def bag_svg(desc):
    return f'<svg viewBox="0 0 80 60" width="80"><path d="M15,20 Q8,20 8,30 L8,50 Q8,55 15,55 L65,55 Q72,55 72,50 L72,30 Q72,20 65,20 Z" fill="#8b5cf6" stroke="#6d28d9" stroke-width="2"/><text x="40" y="42" text-anchor="middle" font-size="8" fill="white">{desc}</text></svg>'

def coin_svg():
    return '<svg viewBox="0 0 50 50" width="50"><circle cx="25" cy="25" r="20" fill="#fbbf24" stroke="#d97706" stroke-width="2"/><text x="25" y="30" text-anchor="middle" font-size="12" fill="#92400e">€</text></svg>'

# Level 1: Probability Language
def gen_level_1(n=50):
    qs = []
    scenarios = [
        ("The sun rising tomorrow", "certain"), ("Rolling 7 on a dice", "impossible"),
        ("Coin landing heads", "equally likely"), ("Rain in Ireland this month", "likely"),
        ("Snow in Dublin in July", "unlikely"), ("Monday after Sunday", "certain"),
        ("Picking blue from bag of red only", "impossible"), ("Rolling even on dice", "equally likely"),
        ("Baby born on a weekday", "likely"), ("Winning lottery", "unlikely"),
        ("Water boiling at 100°C", "certain"), ("Rolling less than 7", "certain"),
        ("Getting a head or tail on a coin", "certain"), ("Picking a vowel from AEIOU", "certain"),
        ("Rolling 0 on a dice", "impossible"), ("A square having 5 sides", "impossible"),
        ("Sun setting in the East", "impossible"), ("February having 30 days", "impossible"),
        ("Picking red from 3 red, 3 blue", "equally likely"), ("Next baby is a boy", "equally likely"),
        ("Rolling odd on dice", "equally likely"), ("Picking heart from deck", "unlikely"),
        ("It raining somewhere today", "likely"), ("Student passing with study", "likely"),
        ("Finding a 4-leaf clover", "unlikely"), ("Bus arriving exactly on time", "unlikely"),
    ]
    used = set()
    for _ in range(n * 10):
        if len(qs) >= n: break
        s, ans = random.choice(scenarios)
        # Add variation with different phrasing
        phrasing = random.choice([f'Describe: "{s}"', f'How likely: "{s}"?', f'What type of event: "{s}"?'])
        txt = phrasing
        if txt in used: continue
        used.add(txt)
        opts = ["certain", "likely", "equally likely", "unlikely", "impossible"]
        random.shuffle(opts)
        opts = opts[:4]
        if ans not in opts:
            opts[0] = ans
            random.shuffle(opts)
        qs.append({'question_text': txt, 'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3], 'correct_idx': opts.index(ans), 'explanation': f"This is '{ans}'", 'image_svg': dice_svg()})
    return qs

# Level 2: Simple Probability Fractions
def gen_level_2(n=50):
    qs = []
    used = set()
    for _ in range(n * 5):
        if len(qs) >= n: break
        c1, c2 = random.sample(COLOURS[:4], 2)
        n1, n2 = random.randint(2, 6), random.randint(2, 6)
        total = n1 + n2
        target = random.choice([c1, c2])
        fav = n1 if target == c1 else n2
        ans = Fraction(fav, total)
        txt = f"Bag: {n1} {c1}, {n2} {c2}. P({target})?"
        if txt in used: continue
        used.add(txt)
        wrongs = {str(Fraction(total-fav, total)), str(Fraction(1, total)), str(Fraction(fav+1, total)), str(Fraction(fav, total+2))}
        opts, idx = make_options(str(ans), wrongs)
        qs.append({'question_text': txt, 'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3], 'correct_idx': idx, 'explanation': f"P = {fav}/{total} = {ans}", 'image_svg': bag_svg(f"{n1} {c1}, {n2} {c2}")})
    return qs

# Level 3: Probability from Tables
def gen_level_3(n=50):
    qs = []
    used = set()
    for _ in range(n * 5):
        if len(qs) >= n: break
        cats = random.sample(['Maths', 'English', 'Science', 'Art'], 3)
        freqs = [random.randint(5, 15) for _ in cats]
        total = sum(freqs)
        target = random.choice(cats)
        fav = freqs[cats.index(target)]
        ans = Fraction(fav, total)
        tbl = ', '.join([f"{c}:{f}" for c, f in zip(cats, freqs)])
        txt = f"Subjects: {tbl}. P({target})?"
        if txt in used: continue
        used.add(txt)
        wrongs = {str(Fraction(total-fav, total)), str(Fraction(1, 3)), str(Fraction(fav+2, total))}
        opts, idx = make_options(str(ans), wrongs)
        qs.append({'question_text': txt, 'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3], 'correct_idx': idx, 'explanation': f"P = {fav}/{total} = {ans}", 'image_svg': bag_svg(f"Total: {total}")})
    return qs

# Level 4: Complement
def gen_level_4(n=50):
    qs = []
    used = set()
    events = ['rain', 'win', 'red', 'pass', 'heads']
    for _ in range(n * 5):
        if len(qs) >= n: break
        d = random.choice([4, 5, 6, 8, 10])
        num = random.randint(1, d-1)
        p = Fraction(num, d)
        comp = 1 - p
        e = random.choice(events)
        txt = f"P({e}) = {p}. P(not {e})?"
        if txt in used: continue
        used.add(txt)
        wrongs = {str(p), str(Fraction(num, d*2)), str(Fraction(1, d)), str(Fraction(num+1, d))}
        opts, idx = make_options(str(comp), wrongs)
        qs.append({'question_text': txt, 'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3], 'correct_idx': idx, 'explanation': f"P(not A) = 1 - {p} = {comp}", 'image_svg': spinner_svg(d, ['blue']*num + ['white']*(d-num))})
    return qs

# Level 5: Expected Outcomes
def gen_level_5(n=50):
    qs = []
    used = set()
    for _ in range(n * 5):
        if len(qs) >= n: break
        d = random.choice([4, 5, 10])
        num = random.randint(1, d-1)
        p = Fraction(num, d)
        trials = d * random.randint(4, 20)
        exp = trials * num // d
        txt = f"P(win) = {p}. In {trials} games, expected wins?"
        if txt in used: continue
        used.add(txt)
        wrongs = {str(trials - exp), str(exp + d), str(trials // 2), str(exp - d if exp > d else exp + 2*d)}
        wrongs = {w for w in wrongs if int(w) > 0}
        opts, idx = make_options(str(exp), wrongs)
        qs.append({'question_text': txt, 'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3], 'correct_idx': idx, 'explanation': f"Expected = {p} x {trials} = {exp}", 'image_svg': spinner_svg(d, ['green']*num + ['red']*(d-num))})
    return qs

# Level 6: Two Dice Sample Space
def gen_level_6(n=50):
    qs = []
    used = set()
    for _ in range(n * 50):
        if len(qs) >= n: break
        qtype = random.choice(['sum', 'sum', 'product', 'diff', 'double', 'atleast', 'atmost', 'both_even', 'both_odd', 'one_six', 'sum_even', 'sum_odd'])
        if qtype == 'sum':
            target = random.randint(2, 12)
            fav = sum(1 for d1 in range(1,7) for d2 in range(1,7) if d1+d2 == target)
            txt = f"Two dice rolled. P(sum = {target})?"
            exp_txt = f"{fav} ways to get sum {target}"
        elif qtype == 'product':
            target = random.choice([1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 30, 36])
            fav = sum(1 for d1 in range(1,7) for d2 in range(1,7) if d1*d2 == target)
            txt = f"Two dice rolled. P(product = {target})?"
            exp_txt = f"{fav} ways to get product {target}"
        elif qtype == 'diff':
            target = random.randint(0, 5)
            fav = sum(1 for d1 in range(1,7) for d2 in range(1,7) if abs(d1-d2) == target)
            txt = f"Two dice rolled. P(|difference| = {target})?"
            exp_txt = f"{fav} ways to get difference {target}"
        elif qtype == 'double':
            fav = 6
            txt = "Two dice rolled. P(getting a double)?"
            exp_txt = "6 doubles: (1,1), (2,2), ..., (6,6)"
        elif qtype == 'atleast':
            target = random.randint(3, 11)
            fav = sum(1 for d1 in range(1,7) for d2 in range(1,7) if d1+d2 >= target)
            txt = f"Two dice rolled. P(sum ≥ {target})?"
            exp_txt = f"{fav} ways to get sum at least {target}"
        elif qtype == 'atmost':
            target = random.randint(4, 10)
            fav = sum(1 for d1 in range(1,7) for d2 in range(1,7) if d1+d2 <= target)
            txt = f"Two dice rolled. P(sum ≤ {target})?"
            exp_txt = f"{fav} ways to get sum at most {target}"
        elif qtype == 'both_even':
            fav = 9
            txt = "Two dice rolled. P(both show even)?"
            exp_txt = "9 ways: 3 even choices × 3 even choices"
        elif qtype == 'both_odd':
            fav = 9
            txt = "Two dice rolled. P(both show odd)?"
            exp_txt = "9 ways: 3 odd choices × 3 odd choices"
        elif qtype == 'one_six':
            fav = 11
            txt = "Two dice rolled. P(at least one 6)?"
            exp_txt = "11 ways (36 - 25 with no 6)"
        elif qtype == 'sum_even':
            fav = 18
            txt = "Two dice rolled. P(sum is even)?"
            exp_txt = "18 ways (both even or both odd)"
        else:  # sum_odd
            fav = 18
            txt = "Two dice rolled. P(sum is odd)?"
            exp_txt = "18 ways (one even, one odd)"
        if fav == 0: continue
        ans = Fraction(fav, 36)
        if txt in used: continue
        used.add(txt)
        wrongs = {str(Fraction(fav+1, 36)), str(Fraction(fav-1, 36) if fav > 1 else Fraction(fav+2, 36)), str(Fraction(fav, 12)), str(Fraction(1, 6)), str(Fraction(fav+2, 36))}
        opts, idx = make_options(str(ans), wrongs)
        qs.append({'question_text': txt, 'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3], 'correct_idx': idx, 'explanation': f"{exp_txt}. P = {fav}/36 = {ans}", 'image_svg': dice_svg(random.randint(1,6))})
    return qs

# Level 7: Relative Frequency
def gen_level_7(n=50):
    qs = []
    used = set()
    for _ in range(n * 5):
        if len(qs) >= n: break
        total = random.choice([20, 25, 40, 50, 100])
        outcomes = random.randint(total//5, total*4//5)
        ans = Fraction(outcomes, total)
        txt = f"In {total} trials, event happened {outcomes} times. Relative frequency?"
        if txt in used: continue
        used.add(txt)
        wrongs = {str(Fraction(total-outcomes, total)), str(Fraction(outcomes, total+10)), str(Fraction(outcomes+5, total))}
        opts, idx = make_options(str(ans), wrongs)
        qs.append({'question_text': txt, 'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3], 'correct_idx': idx, 'explanation': f"Rel freq = {outcomes}/{total} = {ans}", 'image_svg': spinner_svg(4, ['blue', 'red', 'green', 'yellow'])})
    return qs

# Level 8: OR Rule
def gen_level_8(n=50):
    qs = []
    used = set()
    for _ in range(n * 10):
        if len(qs) >= n: break
        qtype = random.choice(['dice', 'cards', 'spinner'])
        if qtype == 'dice':
            events = [
                ("even or 5", 4), ("1 or 6", 2), ("prime or 4", 4), ("< 3 or > 4", 4),
                ("odd or 6", 4), ("1 or 2 or 3", 3), ("4 or 5 or 6", 3), ("> 2 or even", 5),
                ("prime or 1", 4), ("< 4 or > 3", 6), ("1 or prime", 4), ("even or > 4", 4),
            ]
            desc, fav = random.choice(events)
            total = 6
            txt = f"Dice rolled. P({desc})?"
            vis = dice_svg()
        elif qtype == 'cards':
            events = [
                ("heart or diamond", 26, 52), ("king or queen", 8, 52), ("red or ace", 28, 52),
                ("face card", 12, 52), ("black or king", 28, 52), ("spade or club", 26, 52),
            ]
            desc, fav, total = random.choice(events)
            txt = f"Card drawn. P({desc})?"
            vis = bag_svg("52 cards")
        else:
            c1, c2 = random.sample(COLOURS[:4], 2)
            n1, n2 = random.randint(1, 4), random.randint(1, 4)
            other = random.randint(1, 3)
            total = n1 + n2 + other
            fav = n1 + n2
            txt = f"Spinner: {n1} {c1}, {n2} {c2}, {other} white. P({c1} or {c2})?"
            vis = spinner_svg(total, [c1]*n1 + [c2]*n2 + ['white']*other)
        ans = Fraction(fav, total)
        if txt in used: continue
        used.add(txt)
        wrongs = {str(Fraction(total-fav, total)), str(Fraction(fav-1, total)), str(Fraction(1, total)), str(Fraction(fav+1, total))}
        opts, idx = make_options(str(ans), wrongs)
        qs.append({'question_text': txt, 'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3], 'correct_idx': idx, 'explanation': f"P(A or B) = {fav}/{total} = {ans}", 'image_svg': vis})
    return qs

# Level 9: AND Rule
def gen_level_9(n=50):
    qs = []
    used = set()
    for _ in range(n * 10):
        if len(qs) >= n: break
        qtype = random.choice(['coin2', 'coin3', 'dice', 'spinner'])
        if qtype == 'coin2':
            outcome = random.choice(['both heads', 'both tails', 'head then tail', 'tail then head'])
            txt = f"Two coins tossed. P({outcome})?"
            ans = Fraction(1, 4)
            exp = "P = 1/2 × 1/2 = 1/4"
            vis = coin_svg()
        elif qtype == 'coin3':
            outcome = random.choice(['all heads', 'all tails', 'HHT in order', 'THH in order'])
            txt = f"Three coins tossed. P({outcome})?"
            ans = Fraction(1, 8)
            exp = "P = 1/2 × 1/2 × 1/2 = 1/8"
            vis = coin_svg()
        elif qtype == 'dice':
            t1, t2 = random.randint(1, 6), random.randint(1, 6)
            txt = f"Two dice rolled. P(first={t1} AND second={t2})?"
            ans = Fraction(1, 36)
            exp = "P = 1/6 × 1/6 = 1/36"
            vis = dice_svg(t1)
        else:
            sections = random.choice([4, 5, 6])
            colour = random.choice(COLOURS[:3])
            count = random.randint(1, sections - 1)
            p = Fraction(count, sections)
            ans = p * p
            txt = f"Spinner ({count} {colour} of {sections}). Spun twice. P({colour} both times)?"
            exp = f"P = {p} × {p} = {ans}"
            vis = spinner_svg(sections, [colour]*count + ['white']*(sections-count))
        if txt in used: continue
        used.add(txt)
        wrongs = {str(Fraction(1, 2)), str(Fraction(1, 6)), str(Fraction(2, 36)), str(Fraction(1, 12)), str(Fraction(1, 8)), str(Fraction(1, 16))}
        opts, idx = make_options(str(ans), wrongs)
        qs.append({'question_text': txt, 'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3], 'correct_idx': idx, 'explanation': exp, 'image_svg': vis})
    return qs

# Level 10: Tree Diagrams
def gen_level_10(n=50):
    qs = []
    used = set()
    for _ in range(n * 10):
        if len(qs) >= n: break
        d1, d2 = random.choice([4, 5]), random.choice([4, 5, 6])
        n1, n2 = random.randint(1, d1-1), random.randint(1, d2-1)
        p1, p2 = Fraction(n1, d1), Fraction(n2, d2)
        target = random.choice(['both', 'neither', 'first_only', 'second_only', 'exactly_one'])
        if target == 'both':
            ans = p1 * p2
            desc = "both events happen"
        elif target == 'neither':
            ans = (1-p1) * (1-p2)
            desc = "neither event happens"
        elif target == 'first_only':
            ans = p1 * (1-p2)
            desc = "only first event happens"
        elif target == 'second_only':
            ans = (1-p1) * p2
            desc = "only second event happens"
        else:
            ans = p1 * (1-p2) + (1-p1) * p2
            desc = "exactly one event happens"
        txt = f"P(A)={p1}, P(B)={p2}. Using tree diagram, P({desc})?"
        if txt in used: continue
        used.add(txt)
        wrongs = {str(p1*p2), str(p1+p2), str((1-p1)*(1-p2)), str(p1*(1-p2)), str((1-p1)*p2)}
        opts, idx = make_options(str(ans), wrongs)
        qs.append({'question_text': txt, 'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3], 'correct_idx': idx, 'explanation': f"P({desc}) = {ans}", 'image_svg': spinner_svg(4, ['blue']*2 + ['red']*2)})
    return qs

# Level 11: Without Replacement
def gen_level_11(n=50):
    qs = []
    used = set()
    for _ in range(n * 5):
        if len(qs) >= n: break
        c1, c2 = random.sample(COLOURS[:4], 2)
        n1, n2 = random.randint(3, 6), random.randint(3, 6)
        total = n1 + n2
        p1 = Fraction(n1, total)
        p2 = Fraction(n1-1, total-1)
        ans = p1 * p2
        txt = f"Bag: {n1} {c1}, {n2} {c2}. Two picked WITHOUT replacement. P(both {c1})?"
        if txt in used: continue
        used.add(txt)
        wrongs = {str(Fraction(n1,total)*Fraction(n1,total)), str(Fraction(n1,total)), str(Fraction(2*n1, total*(total-1)))}
        opts, idx = make_options(str(ans), wrongs)
        qs.append({'question_text': txt, 'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3], 'correct_idx': idx, 'explanation': f"Without replacement: {n1}/{total} x {n1-1}/{total-1} = {ans}", 'image_svg': bag_svg(f"{n1} {c1}, {n2} {c2}")})
    return qs

# Level 12: Problem Solving
def gen_level_12(n=50):
    qs = []
    used = set()
    for _ in range(n * 10):
        if len(qs) >= n: break
        qtype = random.choice(['fair', 'atleast', 'expected_money', 'reverse'])
        if qtype == 'fair':
            num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
            p = Fraction(num, 10)
            is_fair = (p == Fraction(1, 2))
            txt = f"Game: P(win) = {p}. Is this a fair game?"
            ans = "Yes" if is_fair else "No"
            opts = ["Yes", "No", "Cannot tell", "Need more info"]
            exp = f"Fair means P(win) = 1/2. Here P = {p}, so {'fair' if is_fair else 'not fair'}."
            vis = coin_svg()
            if txt in used: continue
            used.add(txt)
            qs.append({'question_text': txt, 'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3], 'correct_idx': opts.index(ans), 'explanation': exp, 'image_svg': vis})
        elif qtype == 'atleast':
            denom = random.choice([4, 5, 6])
            p = Fraction(1, denom)
            trials = random.choice([2, 3])
            p_none = (1 - p) ** trials
            ans = 1 - p_none
            txt = f"P(success) = {p}. In {trials} independent tries, P(at least one success)?"
            if txt in used: continue
            used.add(txt)
            wrongs = {str(p * trials), str(p ** trials), str(p_none), str(Fraction(trials, denom))}
            opts, idx = make_options(str(ans), wrongs)
            exp = f"P(at least one) = 1 - P(none) = 1 - ({1-p})^{trials} = 1 - {p_none} = {ans}"
            qs.append({'question_text': txt, 'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3], 'correct_idx': idx, 'explanation': exp, 'image_svg': spinner_svg(denom, ['green'] + ['red']*(denom-1))})
        elif qtype == 'expected_money':
            win = random.choice([5, 10, 20])
            lose = random.choice([1, 2, 5])
            p_win = Fraction(1, random.choice([4, 5, 6]))
            expected = float(p_win) * win - float(1-p_win) * lose
            expected = round(expected, 2)
            txt = f"Game: Win €{win} with P={p_win}, else lose €{lose}. Expected value per game?"
            if txt in used: continue
            used.add(txt)
            ans = f"€{expected}"
            wrongs = set()
            wrongs.add(f"€{win-lose}")
            wrongs.add(f"€{round(expected+1, 2)}")
            wrongs.add(f"€{round(float(p_win)*win, 2)}")
            wrongs.add(f"€{round(-expected, 2)}")
            wrongs.add(f"€{round(expected-1, 2)}")
            wrongs.discard(ans)
            wrongs = list(wrongs)[:3]
            while len(wrongs) < 3:
                w = f"€{round(random.uniform(-5, 10), 2)}"
                if w != ans and w not in wrongs:
                    wrongs.append(w)
            opts = [ans] + wrongs[:3]
            random.shuffle(opts)
            exp = f"E = {p_win}×{win} - {1-p_win}×{lose} = €{expected}"
            qs.append({'question_text': txt, 'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3], 'correct_idx': opts.index(ans), 'explanation': exp, 'image_svg': coin_svg()})
        else:  # reverse
            total = random.randint(8, 15)
            target_num = random.randint(3, total - 3)
            known = random.randint(1, target_num - 1)
            unknown = target_num - known
            other = total - target_num
            colour = random.choice(COLOURS[:3])
            p = Fraction(target_num, total)
            txt = f"Bag: {known} {colour}, x more {colour}, {other} other. If P({colour})={p}, find x."
            if txt in used: continue
            used.add(txt)
            ans = str(unknown)
            wrongs = set()
            wrongs.add(str(unknown + 1))
            wrongs.add(str(unknown + 2))
            wrongs.add(str(known))
            wrongs.add(str(target_num))
            wrongs.add(str(other))
            if unknown > 1: wrongs.add(str(unknown - 1))
            wrongs.discard(ans)
            wrongs = list(wrongs)[:3]
            while len(wrongs) < 3:
                w = str(random.randint(1, 10))
                if w != ans and w not in wrongs:
                    wrongs.append(w)
            opts = [ans] + wrongs[:3]
            random.shuffle(opts)
            exp = f"P({colour}) = ({known}+x)/{total} = {p}, so {known}+x = {target_num}, x = {unknown}"
            qs.append({'question_text': txt, 'option_a': opts[0], 'option_b': opts[1], 'option_c': opts[2], 'option_d': opts[3], 'correct_idx': opts.index(ans), 'explanation': exp, 'image_svg': bag_svg(f"{known}+x {colour}")})
    return qs
    return qs

def generate_all():
    all_q = []
    gens = [(1, gen_level_1), (2, gen_level_2), (3, gen_level_3), (4, gen_level_4), (5, gen_level_5), (6, gen_level_6), (7, gen_level_7), (8, gen_level_8), (9, gen_level_9), (10, gen_level_10), (11, gen_level_11), (12, gen_level_12)]
    for lvl, gen in gens:
        print(f"Generating Level {lvl}...")
        qs = gen(QUESTIONS_PER_LEVEL)
        band = "foundation" if lvl <= 3 else ("ordinary" if lvl <= 6 else ("higher" if lvl <= 9 else "mastery"))
        for q in qs:
            q['topic'] = TOPIC
            q['difficulty'] = lvl
            q['difficulty_band'] = band
            q['mode'] = MODE
        all_q.extend(qs)
    return all_q

def validate(questions):
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)
    errors = []
    lvl_counts = {}
    lvl_vis = {}
    for q in questions:
        lvl = q['difficulty']
        lvl_counts[lvl] = lvl_counts.get(lvl, 0) + 1
        if q.get('image_svg'): lvl_vis[lvl] = lvl_vis.get(lvl, 0) + 1
        opts = [q['option_a'], q['option_b'], q['option_c'], q['option_d']]
        if len(set(opts)) != 4: errors.append(f"L{lvl}: dup opts")
        if not q.get('explanation'): errors.append(f"L{lvl}: no exp")
    for lvl in range(1, 13):
        cnt = lvl_counts.get(lvl, 0)
        vis = lvl_vis.get(lvl, 0)
        pct = (vis / cnt * 100) if cnt else 0
        bar = "█" * (cnt // 2)
        status = "✓" if cnt >= QUESTIONS_PER_LEVEL else "✗"
        print(f"Level {lvl:2}: [{bar:<20}] {cnt}/{QUESTIONS_PER_LEVEL} | Vis: {pct:.0f}% | {status}")
    print("=" * 60)
    print(f"Total Errors: {len(errors)}")
    return len(errors) == 0

def test_insert(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO questions_adaptive (question_text, option_a, option_b, option_c, option_d, correct_answer, topic, difficulty_level, difficulty_band, mode, explanation, image_svg, is_active) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,1)", ("TEST_DEL","A","B","C","D",0,"test",1,"foundation","jc_exam","t",None))
        c.execute("DELETE FROM questions_adaptive WHERE question_text='TEST_DEL'")
        conn.commit()
        conn.close()
        print("✓ Schema validated")
        return True
    except Exception as e:
        conn.close()
        print(f"✗ Schema error: {e}")
        return False

def insert_db(questions):
    db = 'instance/mathquiz.db'
    if not os.path.exists(db):
        print(f"DB not found: {db}")
        return False
    if not test_insert(db):
        print("ABORT: Fix schema!")
        return False
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("DELETE FROM questions_adaptive WHERE topic=? AND mode=?", (TOPIC, MODE))
    print(f"Deleted existing {TOPIC} questions")
    sql = "INSERT INTO questions_adaptive (question_text, option_a, option_b, option_c, option_d, correct_answer, topic, difficulty_level, difficulty_band, mode, explanation, image_svg, is_active) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,1)"
    ok, err = 0, 0
    for q in questions:
        try:
            c.execute(sql, (q['question_text'], q['option_a'], q['option_b'], q['option_c'], q['option_d'], q['correct_idx'], q['topic'], q['difficulty'], q['difficulty_band'], q['mode'], q['explanation'], q.get('image_svg','')))
            ok += 1
        except Exception as e:
            err += 1
            if err <= 3: print(f"Err: {e}")
    conn.commit()
    conn.close()
    print(f"\nInserted {ok}, errors {err}")
    return err == 0

if __name__ == "__main__":
    print("=" * 60)
    print("AgentMath - Probability Generator v1")
    print("=" * 60)
    qs = generate_all()
    validate(qs)
    print("\n" + "=" * 60)
    r = input("Insert? (y/n): ")
    if r.lower() == 'y':
        insert_db(qs)
