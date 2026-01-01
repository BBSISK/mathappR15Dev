#!/usr/bin/env python3
"""
LC Ordinary Level Probability - Top-Up Generator v2
====================================================
CORRECTED for actual database schema

Schema: option_a, option_b, option_c, option_d, correct_answer (0-3 index)
"""

import random
from fractions import Fraction

# Configuration
TOPIC_ID = 'lc_ol_probability'
QUESTIONS_PER_LEVEL = 50

# Level definitions
LEVEL_CONFIG = {
    1: ("Basic Probability", "Foundation"),
    2: ("Probability as Fractions", "Foundation"),
    3: ("Complement Rule", "Foundation"),
    4: ("Sample Spaces", "Developing"),
    5: ("Two Events - Addition", "Developing"),
    6: ("Independent Events", "Developing"),
    7: ("Tree Diagrams", "Proficient"),
    8: ("Expected Value", "Proficient"),
    9: ("At Least One Problems", "Proficient"),
    10: ("Conditional Probability", "Advanced"),
    11: ("Bernoulli Trials", "Advanced"),
    12: ("SEC Exam Style", "Advanced"),
}

def fraction_to_display(num, den):
    """Convert to simplified fraction display."""
    from math import gcd
    g = gcd(num, den)
    num, den = num // g, den // g
    if den == 1:
        return str(num)
    return f"{num}/{den}"

def shuffle_options(correct, distractors):
    """Shuffle options and return (options_list, correct_index)."""
    options = [correct] + distractors[:3]  # Ensure exactly 4 options
    random.shuffle(options)
    correct_index = options.index(correct)
    return options, correct_index

def generate_level_1():
    """Basic Probability - simple scenarios."""
    questions = []
    
    # Coin scenarios
    for outcome in ["heads", "tails"]:
        opts, idx = shuffle_options("1/2", ["1/4", "1/3", "2/3"])
        questions.append({
            'question_text': f"A fair coin is flipped. What is the probability of getting {outcome}?",
            'options': opts, 'correct_index': idx,
            'explanation': f"A fair coin has 2 equally likely outcomes. P({outcome}) = 1/2."
        })
    
    # Dice - single number
    for target in [1, 2, 3, 4, 5, 6]:
        opts, idx = shuffle_options("1/6", ["1/3", "1/2", "2/6"])
        questions.append({
            'question_text': f"A fair die is rolled. What is P(rolling a {target})?",
            'options': opts, 'correct_index': idx,
            'explanation': f"A fair die has 6 equally likely outcomes. P({target}) = 1/6."
        })
    
    # Dice - even/odd
    opts, idx = shuffle_options("1/2", ["1/3", "1/6", "2/3"])
    questions.append({
        'question_text': "A fair die is rolled. What is P(even number)?",
        'options': opts, 'correct_index': idx,
        'explanation': "Even: {2,4,6}. P(even) = 3/6 = 1/2."
    })
    
    opts, idx = shuffle_options("1/2", ["1/3", "1/6", "2/3"])
    questions.append({
        'question_text': "A fair die is rolled. What is P(odd number)?",
        'options': opts, 'correct_index': idx,
        'explanation': "Odd: {1,3,5}. P(odd) = 3/6 = 1/2."
    })
    
    opts, idx = shuffle_options("1/3", ["1/2", "2/3", "1/6"])
    questions.append({
        'question_text': "A fair die is rolled. What is P(greater than 4)?",
        'options': opts, 'correct_index': idx,
        'explanation': "Greater than 4: {5,6}. P = 2/6 = 1/3."
    })
    
    opts, idx = shuffle_options("1/3", ["1/2", "2/3", "1/6"])
    questions.append({
        'question_text': "A fair die is rolled. What is P(less than 3)?",
        'options': opts, 'correct_index': idx,
        'explanation': "Less than 3: {1,2}. P = 2/6 = 1/3."
    })
    
    # Bag of marbles
    marble_scenarios = [
        ("red", 3, 10), ("blue", 4, 10), ("green", 2, 8), ("yellow", 5, 15),
        ("red", 6, 12), ("blue", 3, 9), ("green", 4, 16), ("white", 2, 10),
        ("black", 5, 20), ("orange", 3, 12), ("purple", 4, 8), ("red", 7, 14)
    ]
    for colour, count, total in marble_scenarios:
        ans = fraction_to_display(count, total)
        d1 = fraction_to_display(count + 1, total) if count + 1 <= total else fraction_to_display(count - 1, total)
        d2 = fraction_to_display(total - count, total)
        d3 = fraction_to_display(count, total + 2)
        opts, idx = shuffle_options(ans, [d1, d2, d3])
        questions.append({
            'question_text': f"A bag has {total} marbles, {count} are {colour}. What is P(picking {colour})?",
            'options': opts, 'correct_index': idx,
            'explanation': f"P({colour}) = {count}/{total} = {ans}."
        })
    
    # Card scenarios
    card_scenarios = [
        ("heart", 13), ("diamond", 13), ("spade", 13), ("club", 13),
        ("ace", 4), ("king", 4), ("queen", 4), ("jack", 4),
        ("red card", 26), ("black card", 26), ("face card", 12)
    ]
    for card_type, count in card_scenarios:
        ans = fraction_to_display(count, 52)
        d1 = fraction_to_display(count + 4, 52) if count + 4 <= 52 else fraction_to_display(count - 4, 52)
        d2 = fraction_to_display(count - 2 if count > 2 else count + 2, 52)
        d3 = fraction_to_display(52 - count, 52)
        opts, idx = shuffle_options(ans, [d1, d2, d3])
        questions.append({
            'question_text': f"A card is drawn from a 52-card deck. What is P({card_type})?",
            'options': opts, 'correct_index': idx,
            'explanation': f"There are {count} {card_type}s in 52 cards. P = {count}/52 = {ans}."
        })
    
    # Spinner scenarios
    for sections in [4, 5, 6, 8]:
        ans = f"1/{sections}"
        opts, idx = shuffle_options(ans, [f"2/{sections}", "1/2", f"{sections-1}/{sections}"])
        questions.append({
            'question_text': f"A spinner has {sections} equal sections (1 to {sections}). What is P(landing on 1)?",
            'options': opts, 'correct_index': idx,
            'explanation': f"Each section equally likely. P(1) = 1/{sections}."
        })
    
    # Raffle
    for total in [50, 100, 200]:
        ans = f"1/{total}"
        opts, idx = shuffle_options(ans, [f"2/{total}", f"{total-1}/{total}", "1/2"])
        questions.append({
            'question_text': f"A raffle has {total} tickets. You have 1. What is P(winning)?",
            'options': opts, 'correct_index': idx,
            'explanation': f"P(win) = 1/{total}."
        })
    
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_2():
    """Probability as Fractions."""
    questions = []
    
    # Simplifying fractions
    from math import gcd
    fracs = [
        (4, 8), (6, 12), (3, 9), (5, 20), (8, 24), (10, 25), (15, 45), (12, 36),
        (9, 27), (14, 28), (6, 18), (8, 32), (10, 40), (12, 48), (15, 60),
        (16, 64), (20, 80), (25, 100), (30, 90), (18, 54), (21, 63), (24, 72)
    ]
    for num, den in fracs:
        g = gcd(num, den)
        simplified = f"{num//g}/{den//g}"
        opts, idx = shuffle_options(simplified, [f"{num}/{den}", f"{num//2}/{den}" if num%2==0 else f"{num+1}/{den}", f"{num}/{den//2}" if den%2==0 else f"{num}/{den+1}"])
        questions.append({
            'question_text': f"Simplify {num}/{den} to lowest terms.",
            'options': opts, 'correct_index': idx,
            'explanation': f"{num}/{den} = {simplified} (divide by {g})."
        })
    
    # Percentage to fraction
    percentages = [
        (25, "1/4"), (50, "1/2"), (75, "3/4"), (20, "1/5"), (40, "2/5"), (60, "3/5"),
        (10, "1/10"), (30, "3/10"), (80, "4/5"), (90, "9/10"), (5, "1/20"), (15, "3/20")
    ]
    for pct, frac in percentages:
        opts, idx = shuffle_options(frac, [f"{pct}/100", "1/3", "2/3"])
        questions.append({
            'question_text': f"Convert {pct}% to a fraction in lowest terms.",
            'options': opts, 'correct_index': idx,
            'explanation': f"{pct}% = {pct}/100 = {frac}."
        })
    
    # Decimal to fraction
    decimals = [
        (0.5, "1/2"), (0.25, "1/4"), (0.75, "3/4"), (0.2, "1/5"), (0.4, "2/5"), (0.1, "1/10"),
        (0.125, "1/8"), (0.375, "3/8"), (0.625, "5/8"), (0.875, "7/8"), (0.6, "3/5"), (0.8, "4/5")
    ]
    for dec, frac in decimals:
        opts, idx = shuffle_options(frac, [f"{int(dec*100)}/100", "1/3", "2/3"])
        questions.append({
            'question_text': f"Express {dec} as a fraction in lowest terms.",
            'options': opts, 'correct_index': idx,
            'explanation': f"{dec} = {frac}."
        })
    
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_3():
    """Complement Rule."""
    questions = []
    
    # Basic complement
    pairs = [
        ("1/4", "3/4"), ("1/3", "2/3"), ("2/5", "3/5"), ("3/8", "5/8"),
        ("5/12", "7/12"), ("7/10", "3/10"), ("2/7", "5/7"), ("3/11", "8/11"),
        ("1/5", "4/5"), ("1/6", "5/6"), ("2/9", "7/9"), ("4/15", "11/15"),
        ("3/7", "4/7"), ("5/9", "4/9"), ("1/8", "7/8"), ("5/6", "1/6")
    ]
    for p, comp in pairs:
        opts, idx = shuffle_options(comp, [p, "1/2", "1"])
        questions.append({
            'question_text': f"If P(A) = {p}, what is P(not A)?",
            'options': opts, 'correct_index': idx,
            'explanation': f"P(not A) = 1 - {p} = {comp}."
        })
    
    # Weather
    rain_scenarios = [
        ("30%", "70%"), ("45%", "55%"), ("15%", "85%"), ("80%", "20%"), ("65%", "35%"),
        ("25%", "75%"), ("10%", "90%"), ("55%", "45%"), ("70%", "30%"), ("5%", "95%")
    ]
    for rain, no_rain in rain_scenarios:
        opts, idx = shuffle_options(no_rain, [rain, "50%", "100%"])
        questions.append({
            'question_text': f"P(rain) = {rain}. What is P(no rain)?",
            'options': opts, 'correct_index': idx,
            'explanation': f"P(no rain) = 100% - {rain} = {no_rain}."
        })
    
    # Spinner
    spinner_scenarios = [
        ("red", "2/5", "3/5"), ("blue", "1/4", "3/4"), ("green", "3/8", "5/8"),
        ("yellow", "1/6", "5/6"), ("red", "3/10", "7/10"), ("blue", "2/7", "5/7")
    ]
    for colour, prob, comp in spinner_scenarios:
        opts, idx = shuffle_options(comp, [prob, "1/2", "1"])
        questions.append({
            'question_text': f"P(landing on {colour}) = {prob}. What is P(NOT {colour})?",
            'options': opts, 'correct_index': idx,
            'explanation': f"P(not {colour}) = 1 - {prob} = {comp}."
        })
    
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_4():
    """Sample Spaces."""
    questions = []
    
    # Two coins
    two_coin_qs = [
        ("How many outcomes in the sample space?", "4", ["2", "3", "6"], "Sample space: {HH, HT, TH, TT}. 4 outcomes."),
        ("P(exactly one head)?", "1/2", ["1/4", "3/4", "2/3"], "{HT, TH}. P = 2/4 = 1/2."),
        ("P(at least one head)?", "3/4", ["1/2", "1/4", "2/3"], "{HH, HT, TH}. P = 3/4."),
        ("P(both heads)?", "1/4", ["1/2", "3/4", "1/3"], "{HH}. P = 1/4."),
        ("P(both tails)?", "1/4", ["1/2", "3/4", "1/3"], "{TT}. P = 1/4."),
    ]
    for q, ans, dists, exp in two_coin_qs:
        opts, idx = shuffle_options(ans, dists)
        questions.append({
            'question_text': f"Two fair coins are tossed. {q}",
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    # Two dice
    opts, idx = shuffle_options("36", ["12", "6", "24"])
    questions.append({
        'question_text': "Two dice are rolled. How many outcomes?",
        'options': opts, 'correct_index': idx,
        'explanation': "6 × 6 = 36 outcomes."
    })
    
    # Sum of two dice
    for target_sum, ways in [(7, 6), (8, 5), (6, 5), (9, 4), (5, 4), (10, 3), (4, 3), (11, 2), (3, 2), (12, 1), (2, 1)]:
        ans = fraction_to_display(ways, 36)
        opts, idx = shuffle_options(ans, [fraction_to_display(ways + 1 if ways < 6 else ways - 1, 36), "1/6", fraction_to_display(6, 36)])
        questions.append({
            'question_text': f"Two dice rolled. P(sum = {target_sum})?",
            'options': opts, 'correct_index': idx,
            'explanation': f"{ways} ways to get {target_sum}. P = {ways}/36 = {ans}."
        })
    
    # Double
    opts, idx = shuffle_options("1/6", ["1/12", "2/6", "1/36"])
    questions.append({
        'question_text': "Two dice rolled. P(double - same number)?",
        'options': opts, 'correct_index': idx,
        'explanation': "6 doubles out of 36. P = 6/36 = 1/6."
    })
    
    # Three coins
    three_coin_qs = [
        ("How many outcomes?", "8", ["6", "3", "9"], "2³ = 8."),
        ("P(all heads)?", "1/8", ["1/3", "3/8", "1/6"], "{HHH}. P = 1/8."),
        ("P(exactly 2 heads)?", "3/8", ["1/4", "1/2", "1/3"], "{HHT, HTH, THH}. P = 3/8."),
    ]
    for q, ans, dists, exp in three_coin_qs:
        opts, idx = shuffle_options(ans, dists)
        questions.append({
            'question_text': f"Three fair coins tossed. {q}",
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_5():
    """Two Events - Addition Rule."""
    questions = []
    
    # Mutually exclusive
    me_pairs = [
        ("1/4", "1/3", "7/12"), ("2/5", "1/4", "13/20"), ("1/6", "1/3", "1/2"),
        ("1/5", "2/5", "3/5"), ("1/8", "1/4", "3/8"), ("3/10", "1/5", "1/2"),
        ("1/6", "1/4", "5/12"), ("2/9", "1/3", "5/9"), ("1/3", "1/4", "7/12")
    ]
    for a, b, ans in me_pairs:
        opts, idx = shuffle_options(ans, [a, b, "1"])
        questions.append({
            'question_text': f"A and B mutually exclusive. P(A)={a}, P(B)={b}. P(A or B)?",
            'options': opts, 'correct_index': idx,
            'explanation': f"P(A or B) = {a} + {b} = {ans}."
        })
    
    # Dice
    dice_qs = [
        ("even OR greater than 4", "2/3", "Even:{2,4,6}, >4:{5,6}. Union:{2,4,5,6}. P=4/6=2/3."),
        ("odd OR less than 3", "2/3", "Odd:{1,3,5}, <3:{1,2}. Union:{1,2,3,5}. P=4/6=2/3."),
        ("prime OR even", "5/6", "Prime:{2,3,5}, Even:{2,4,6}. Union:{2,3,4,5,6}. P=5/6."),
    ]
    for event, ans, exp in dice_qs:
        opts, idx = shuffle_options(ans, ["5/6", "1/2", "1/3"])
        questions.append({
            'question_text': f"Die rolled. P({event})?",
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    # Cards
    card_qs = [
        ("heart OR face card", "11/26", "13+12-3=22. P=22/52=11/26."),
        ("red OR ace", "7/13", "26+4-2=28. P=28/52=7/13."),
        ("spade OR king", "4/13", "13+4-1=16. P=16/52=4/13."),
    ]
    for event, ans, exp in card_qs:
        opts, idx = shuffle_options(ans, ["1/2", "1/4", "13/52"])
        questions.append({
            'question_text': f"Card drawn. P({event})?",
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_6():
    """Independent Events."""
    questions = []
    
    # Coin and die
    for coin in ["heads", "tails"]:
        for die in [1, 6]:
            opts, idx = shuffle_options("1/12", ["1/6", "1/2", "7/12"])
            questions.append({
                'question_text': f"Coin tossed, die rolled. P({coin} AND {die})?",
                'options': opts, 'correct_index': idx,
                'explanation': f"1/2 × 1/6 = 1/12."
            })
    
    # Independent pairs
    pairs = [
        ("1/2", "1/3", "1/6"), ("2/5", "1/4", "1/10"), ("1/3", "1/3", "1/9"),
        ("3/4", "2/5", "3/10"), ("1/4", "1/2", "1/8"), ("2/3", "1/4", "1/6"),
        ("1/2", "1/2", "1/4"), ("3/4", "1/2", "3/8")
    ]
    for pa, pb, ans in pairs:
        opts, idx = shuffle_options(ans, [pa, pb, "1/2"])
        questions.append({
            'question_text': f"A,B independent. P(A)={pa}, P(B)={pb}. P(A and B)?",
            'options': opts, 'correct_index': idx,
            'explanation': f"P(A and B) = {pa} × {pb} = {ans}."
        })
    
    # Two dice
    dice_qs = [
        ("both show 6", "1/36", "1/6 × 1/6 = 1/36"),
        ("both show 1", "1/36", "1/6 × 1/6 = 1/36"),
        ("both even", "1/4", "1/2 × 1/2 = 1/4"),
        ("both odd", "1/4", "1/2 × 1/2 = 1/4"),
    ]
    for event, ans, exp in dice_qs:
        opts, idx = shuffle_options(ans, ["1/6", "1/12", "1/3"])
        questions.append({
            'question_text': f"Two dice rolled. P({event})?",
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    # Three coins
    opts, idx = shuffle_options("1/8", ["1/3", "3/8", "1/6"])
    questions.append({
        'question_text': "Three coins tossed. P(all heads)?",
        'options': opts, 'correct_index': idx,
        'explanation': "(1/2)³ = 1/8."
    })
    
    # Real world
    real_qs = [
        ("P(rain Sat)=0.3, P(rain Sun)=0.4", "rain both", "0.12", "0.3×0.4=0.12"),
        ("P(pass test1)=0.8, P(pass test2)=0.9", "pass both", "0.72", "0.8×0.9=0.72"),
        ("P(win game1)=0.6, P(win game2)=0.5", "win both", "0.30", "0.6×0.5=0.30"),
    ]
    for setup, event, ans, exp in real_qs:
        opts, idx = shuffle_options(ans, ["0.5", "0.7", "0.25"])
        questions.append({
            'question_text': f"{setup} (independent). P({event})?",
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_7():
    """Tree Diagrams."""
    questions = []
    
    # With replacement
    wr_qs = [
        (3, 2, "both red", "9/25", "3/5 × 3/5 = 9/25"),
        (3, 2, "both blue", "4/25", "2/5 × 2/5 = 4/25"),
        (4, 6, "both red", "4/25", "4/10 × 4/10 = 16/100 = 4/25"),
        (4, 6, "both blue", "9/25", "6/10 × 6/10 = 36/100 = 9/25"),
    ]
    for red, blue, event, ans, exp in wr_qs:
        total = red + blue
        opts, idx = shuffle_options(ans, [f"{red}/{total}", "1/2", f"{blue}/{total}"])
        questions.append({
            'question_text': f"Bag: {red} red, {blue} blue. Two drawn WITH replacement. P({event})?",
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    # Without replacement
    wor_qs = [
        (3, 2, "both red", "3/10", "3/5 × 2/4 = 6/20 = 3/10"),
        (3, 2, "both blue", "1/10", "2/5 × 1/4 = 2/20 = 1/10"),
        (4, 6, "both red", "2/15", "4/10 × 3/9 = 12/90 = 2/15"),
    ]
    for red, blue, event, ans, exp in wor_qs:
        total = red + blue
        opts, idx = shuffle_options(ans, ["9/25", "1/2", f"{red}/{total}"])
        questions.append({
            'question_text': f"Bag: {red} red, {blue} blue. Two drawn WITHOUT replacement. P({event})?",
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    # Tests
    test_qs = [
        (0.8, 0.7, "pass both", "0.56"),
        (0.9, 0.8, "pass both", "0.72"),
        (0.7, 0.6, "pass both", "0.42"),
    ]
    for p1, p2, event, ans in test_qs:
        opts, idx = shuffle_options(ans, [str(p1), str(p2), "0.5"])
        questions.append({
            'question_text': f"P(pass test1)={p1}, P(pass test2)={p2}. Independent. P({event})?",
            'options': opts, 'correct_index': idx,
            'explanation': f"{p1} × {p2} = {ans}."
        })
    
    # Children
    child_qs = [
        ("2 children. P(one boy, one girl)?", "1/2", ["1/4", "1/3", "2/3"], "BG,GB: 2/4=1/2."),
        ("3 children. P(all same gender)?", "1/4", ["1/8", "1/3", "3/8"], "BBB,GGG: 2/8=1/4."),
    ]
    for q, ans, dists, exp in child_qs:
        opts, idx = shuffle_options(ans, dists)
        questions.append({
            'question_text': q,
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_8():
    """Expected Value."""
    questions = []
    
    # Die
    opts, idx = shuffle_options("3.5", ["3", "4", "6"])
    questions.append({
        'question_text': "A fair die is rolled. Expected value?",
        'options': opts, 'correct_index': idx,
        'explanation': "E = (1+2+3+4+5+6)/6 = 3.5."
    })
    
    opts, idx = shuffle_options("7", ["6", "8", "3.5"])
    questions.append({
        'question_text': "Two dice rolled. Expected sum?",
        'options': opts, 'correct_index': idx,
        'explanation': "E = 3.5 + 3.5 = 7."
    })
    
    # Games
    games = [
        ("Win €10 with P=1/4, €0 otherwise", "€2.50", "€10×1/4 = €2.50"),
        ("Win €12 with P=1/3, €0 otherwise", "€4", "€12×1/3 = €4"),
        ("Win €6 with P=1/2, lose €2 with P=1/2", "€2", "€6×1/2 - €2×1/2 = €2"),
        ("Win €8 with P=1/4, lose €4 otherwise", "-€1", "€8×1/4 - €4×3/4 = -€1"),
    ]
    for game, ans, exp in games:
        opts, idx = shuffle_options(ans, ["€5", "€0", "€10"])
        questions.append({
            'question_text': f"Game: {game}. Expected winnings?",
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    # Coin flips expected heads
    for n in [5, 10, 20, 100]:
        ans = str(n // 2)
        opts, idx = shuffle_options(ans, [str(n), str(n // 4), str(n // 2 + 1)])
        questions.append({
            'question_text': f"Fair coin flipped {n} times. Expected heads?",
            'options': opts, 'correct_index': idx,
            'explanation': f"E = {n} × 0.5 = {n//2}."
        })
    
    # Raffle
    raffle_qs = [
        (100, 2, 50, "-€1.50", "€50/100 - €2 = -€1.50"),
        (200, 5, 100, "-€4.50", "€100/200 - €5 = -€4.50"),
    ]
    for tickets, cost, prize, ans, exp in raffle_qs:
        opts, idx = shuffle_options(ans, ["€0.50", "-€2", "€0"])
        questions.append({
            'question_text': f"Raffle: {tickets} tickets at €{cost}, prize €{prize}. Expected gain?",
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_9():
    """At Least One Problems."""
    questions = []
    
    # Coin flips
    for n in [2, 3, 4, 5]:
        ans = f"{2**n - 1}/{2**n}"
        opts, idx = shuffle_options(ans, [f"1/{2**n}", "1/2", f"{n}/{2**n}"])
        questions.append({
            'question_text': f"Coin flipped {n} times. P(at least one head)?",
            'options': opts, 'correct_index': idx,
            'explanation': f"1 - (1/2)^{n} = {ans}."
        })
    
    # Dice - at least one 6
    opts, idx = shuffle_options("11/36", ["1/36", "2/36", "25/36"])
    questions.append({
        'question_text': "Two dice rolled. P(at least one 6)?",
        'options': opts, 'correct_index': idx,
        'explanation': "1 - (5/6)² = 11/36."
    })
    
    # Quality control
    qc_qs = [
        (0.1, 3, "0.271", "1 - 0.9³ = 0.271"),
        (0.05, 2, "0.0975", "1 - 0.95² = 0.0975"),
        (0.2, 3, "0.488", "1 - 0.8³ = 0.488"),
    ]
    for p, n, ans, exp in qc_qs:
        opts, idx = shuffle_options(ans, [str(round(p * n, 2)), str(p), "0.5"])
        questions.append({
            'question_text': f"P(defective)={p}. In {n} items, P(at least one defective)?",
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    # Rain
    rain_qs = [
        (0.3, 2, "0.51", "1 - 0.7² = 0.51"),
        (0.4, 2, "0.64", "1 - 0.6² = 0.64"),
    ]
    for p, days, ans, exp in rain_qs:
        opts, idx = shuffle_options(ans, [str(round(p * days, 2)), str(p), "0.5"])
        questions.append({
            'question_text': f"P(rain)={p}. P(rain at least one of {days} days)?",
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    # Bag
    opts, idx = shuffle_options("16/25", ["8/25", "4/10", "9/25"])
    questions.append({
        'question_text': "Bag: 4 red, 6 blue. Two drawn with replacement. P(at least one red)?",
        'options': opts, 'correct_index': idx,
        'explanation': "1 - (6/10)² = 16/25."
    })
    
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_10():
    """Conditional Probability."""
    questions = []
    
    # Class tables
    class_qs = [
        (12, 8, 18, 10, "sport", "boy", "2/3", "8/12 = 2/3"),
        (12, 8, 18, 10, "boy", "sport", "4/9", "8/18 = 4/9"),
        (15, 10, 25, 15, "music", "girl", "3/5", "15/25 = 3/5"),
    ]
    for boys, boys_yes, girls, girls_yes, given, find, ans, exp in class_qs:
        opts, idx = shuffle_options(ans, [f"{boys_yes}/{boys+girls}", "1/2", f"{boys}/{boys+girls}"])
        questions.append({
            'question_text': f"Class: {boys} boys ({boys_yes} play {given}), {girls} girls ({girls_yes} play {given}). P({given}|{find})?",
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    # Cards
    card_cond = [
        ("red", "heart", "1/2", "13/26 = 1/2"),
        ("face card", "red", "3/13", "6/26 = 3/13"),
        ("king", "face card", "1/3", "4/12 = 1/3"),
    ]
    for given, find, ans, exp in card_cond:
        opts, idx = shuffle_options(ans, ["13/52", "1/4", "4/52"])
        questions.append({
            'question_text': f"Card is {given}. P({find}|{given})?",
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    # Dice
    dice_cond = [
        ("even", ">3", "2/3", "Even:{2,4,6}. >3:{4,6}. P=2/3."),
        (">2", "even", "1/2", ">2:{3,4,5,6}. Even:{4,6}. P=2/4=1/2."),
    ]
    for given, find, ans, exp in dice_cond:
        opts, idx = shuffle_options(ans, ["1/2", "1/3", "1/6"])
        questions.append({
            'question_text': f"Die roll is {given}. P({find}|{given})?",
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_11():
    """Bernoulli Trials."""
    questions = []
    
    # Coin flips
    coin_qs = [
        (4, 2, "3/8", "C(4,2)×(1/2)⁴ = 6/16 = 3/8"),
        (5, 3, "5/16", "C(5,3)×(1/2)⁵ = 10/32 = 5/16"),
        (4, 0, "1/16", "C(4,0)×(1/2)⁴ = 1/16"),
        (4, 4, "1/16", "C(4,4)×(1/2)⁴ = 1/16"),
        (6, 3, "5/16", "C(6,3)×(1/2)⁶ = 20/64 = 5/16"),
    ]
    for n, k, ans, exp in coin_qs:
        opts, idx = shuffle_options(ans, [f"{k}/{n}", "1/2", f"1/{2**n}"])
        questions.append({
            'question_text': f"Coin flipped {n} times. P(exactly {k} heads)?",
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    # Success probabilities
    success_qs = [
        (0.8, 5, 5, "0.328", "(0.8)⁵ = 0.328"),
        (0.7, 4, 4, "0.240", "(0.7)⁴ = 0.240"),
        (0.9, 3, 3, "0.729", "(0.9)³ = 0.729"),
    ]
    for p, n, k, ans, exp in success_qs:
        opts, idx = shuffle_options(ans, [str(p), str(round(p * n, 2)), "0.5"])
        questions.append({
            'question_text': f"P(success)={p}. In {n} trials, P(all {k} succeed)?",
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    # Defective
    defect_qs = [
        (0.05, 3, "0.857", "(0.95)³ = 0.857"),
        (0.1, 4, "0.656", "(0.9)⁴ = 0.656"),
    ]
    for p, n, ans, exp in defect_qs:
        opts, idx = shuffle_options(ans, [str(round(1 - p, 2)), str(round(p * n, 2)), "0.5"])
        questions.append({
            'question_text': f"P(defective)={p}. In {n} items, P(none defective)?",
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    return questions[:QUESTIONS_PER_LEVEL]


def generate_level_12():
    """SEC Exam Style."""
    questions = []
    
    # Same colour
    same_qs = [
        (5, 3, "13/28", "(5/8×4/7)+(3/8×2/7) = 13/28"),
        (4, 6, "7/15", "(4/10×3/9)+(6/10×5/9) = 7/15"),
    ]
    for red, blue, ans, exp in same_qs:
        opts, idx = shuffle_options(ans, ["1/2", f"{red}/{red+blue}", f"{blue}/{red+blue}"])
        questions.append({
            'question_text': f"Bag: {red} red, {blue} blue. Two without replacement. P(same colour)?",
            'options': opts, 'correct_index': idx,
            'explanation': exp
        })
    
    # At least one blue spinner
    opts, idx = shuffle_options("3/4", ["1/2", "5/6", "9/36"])
    questions.append({
        'question_text': "Spinner: 2 red, 3 blue, 1 green. Spun twice. P(at least one blue)?",
        'options': opts, 'correct_index': idx,
        'explanation': "1 - (3/6)² = 3/4."
    })
    
    # Expected value game
    opts, idx = shuffle_options("€1", ["€0", "-€1", "€2"])
    questions.append({
        'question_text': "Game: Roll die, win €(number) if even, lose €2 if odd. Expected value?",
        'options': opts, 'correct_index': idx,
        'explanation': "(2+4+6)/6 - 2×3/6 = 2 - 1 = €1."
    })
    
    # Conditional
    opts, idx = shuffle_options("0.56", ["0.80", "0.70", "0.75"])
    questions.append({
        'question_text': "80% pass maths. Of those, 70% pass science. P(pass both)?",
        'options': opts, 'correct_index': idx,
        'explanation': "0.8 × 0.7 = 0.56."
    })
    
    # Expected wins
    opts, idx = shuffle_options("2.6", ["2.5", "3", "2"])
    questions.append({
        'question_text': "Team wins 60% home, 40% away. 3 home + 2 away. Expected wins?",
        'options': opts, 'correct_index': idx,
        'explanation': "3×0.6 + 2×0.4 = 2.6."
    })
    
    # At least 2 sunny
    opts, idx = shuffle_options("0.648", ["0.6", "0.72", "0.216"])
    questions.append({
        'question_text': "P(sunny)=0.6. P(at least 2 sunny in 3 days)?",
        'options': opts, 'correct_index': idx,
        'explanation': "P(2)+P(3) = 0.432+0.216 = 0.648."
    })
    
    # Survey neither
    opts, idx = shuffle_options("1/4", ["15/60", "45/60", "1/3"])
    questions.append({
        'question_text': "Survey: 60 students, 35 sport, 25 music, 15 both. P(neither)?",
        'options': opts, 'correct_index': idx,
        'explanation': "Neither = 60-(35+25-15) = 15. P = 15/60 = 1/4."
    })
    
    return questions[:QUESTIONS_PER_LEVEL]


def generate_all_questions():
    """Generate all questions."""
    all_questions = []
    
    generators = [
        generate_level_1, generate_level_2, generate_level_3, generate_level_4,
        generate_level_5, generate_level_6, generate_level_7, generate_level_8,
        generate_level_9, generate_level_10, generate_level_11, generate_level_12
    ]
    
    for level, generator in enumerate(generators, 1):
        questions = generator()
        level_name, band = LEVEL_CONFIG[level]
        for q in questions:
            q['level'] = level
            q['level_name'] = level_name
            q['band'] = band
        all_questions.extend(questions)
        print(f"Level {level:2d}: {len(questions):3d} questions - {level_name}")
    
    return all_questions


def generate_sql(questions):
    """Generate SQL with correct schema."""
    sql_lines = [
        f"-- LC OL Probability Top-Up v2",
        f"-- Correct schema: option_a/b/c/d, correct_answer (0-3)",
        f"-- Total: {len(questions)} questions",
        f"-- Generated: 2025-12-24",
        "",
    ]
    
    for q in questions:
        q_text = q['question_text'].replace("'", "''")
        opt_a = q['options'][0].replace("'", "''")
        opt_b = q['options'][1].replace("'", "''")
        opt_c = q['options'][2].replace("'", "''")
        opt_d = q['options'][3].replace("'", "''")
        correct_idx = q['correct_index']
        explanation = q['explanation'].replace("'", "''")
        band = q['band']
        level = q['level']
        
        sql = f"""INSERT INTO questions_adaptive (topic, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, difficulty_level, difficulty_band, mode)
VALUES ('{TOPIC_ID}', '{q_text}', '{opt_a}', '{opt_b}', '{opt_c}', '{opt_d}', {correct_idx}, '{explanation}', {level}, '{band}', 'adaptive');"""
        sql_lines.append(sql)
    
    sql_lines.append("")
    sql_lines.append(f"SELECT 'Total {TOPIC_ID}:' as info, COUNT(*) FROM questions_adaptive WHERE topic = '{TOPIC_ID}';")
    
    return '\n'.join(sql_lines)


def main():
    print("=" * 60)
    print("LC OL Probability Top-Up v2 (Correct Schema)")
    print("=" * 60)
    print()
    
    questions = generate_all_questions()
    print()
    print(f"Total: {len(questions)}")
    
    sql = generate_sql(questions)
    
    with open('lc_ol_probability_topup_v2.sql', 'w', encoding='utf-8') as f:
        f.write(sql)
    
    print(f"\nSaved: lc_ol_probability_topup_v2.sql")


if __name__ == "__main__":
    main()
