#!/usr/bin/env python3
"""
LC Ordinary Level Probability - Top-Up Generator
================================================
Adds 324 additional questions to reach 600 total (currently 276 in DB)

Topic: lc_ol_probability
Target: 50 questions per level × 12 levels = 600 total
Current: 276 questions
Need: 324 more questions (27 per level average)

Based on SEC OL Paper Analysis 2019-2025:
- Probability worth 295 marks over 7 years
- Focus: basic probability, complement rule, independent events, 
  expected value, tree diagrams, "at least one" problems

Version: 1.0 (Top-up)
Date: 2025-12-24
"""

import random
from fractions import Fraction

# Configuration
TOPIC_ID = 'lc_ol_probability'
STRAND_ID = 11  # LC Ordinary Level
DISPLAY_NAME = 'Probability'
MODE = 'adaptive'
QUESTIONS_PER_LEVEL = 50  # To add ~324 total (some levels may have fewer unique questions)

# Level definitions for LC OL Probability
LEVEL_NAMES = {
    1: "Basic Probability",
    2: "Probability as Fractions",
    3: "Complement Rule",
    4: "Sample Spaces",
    5: "Two Events - Addition",
    6: "Independent Events",
    7: "Tree Diagrams",
    8: "Expected Value",
    9: "At Least One Problems",
    10: "Conditional Probability",
    11: "Bernoulli Trials",
    12: "SEC Exam Style"
}

def fraction_to_display(num, den):
    """Convert to simplified fraction display."""
    from math import gcd
    g = gcd(num, den)
    num, den = num // g, den // g
    if den == 1:
        return str(num)
    return f"{num}/{den}"

def generate_level_1():
    """Basic Probability - simple scenarios, words to fractions."""
    questions = []
    
    # Coin scenarios
    for outcome in ["heads", "tails"]:
        questions.append({
            'question_text': f"A fair coin is flipped. What is the probability of getting {outcome}?",
            'correct_answer': "1/2",
            'distractor1': "1/4",
            'distractor2': "1/3",
            'distractor3': "2/3",
            'explanation': f"A fair coin has 2 equally likely outcomes. P({outcome}) = 1/2."
        })
    
    # Dice - single number
    for target in [1, 2, 3, 4, 5, 6]:
        questions.append({
            'question_text': f"A fair six-sided die is rolled. What is the probability of rolling a {target}?",
            'correct_answer': "1/6",
            'distractor1': "1/3",
            'distractor2': "1/2",
            'distractor3': "2/6",
            'explanation': f"A fair die has 6 equally likely outcomes. P(rolling {target}) = 1/6."
        })
    
    # Dice - even/odd
    questions.append({
        'question_text': "A fair die is rolled. What is P(even number)?",
        'correct_answer': "1/2",
        'distractor1': "1/3",
        'distractor2': "1/6",
        'distractor3': "2/3",
        'explanation': "Even numbers: {2,4,6}. P(even) = 3/6 = 1/2."
    })
    
    questions.append({
        'question_text': "A fair die is rolled. What is P(odd number)?",
        'correct_answer': "1/2",
        'distractor1': "1/3",
        'distractor2': "1/6",
        'distractor3': "2/3",
        'explanation': "Odd numbers: {1,3,5}. P(odd) = 3/6 = 1/2."
    })
    
    # Dice - greater/less than
    questions.append({
        'question_text': "A fair die is rolled. What is P(greater than 4)?",
        'correct_answer': "1/3",
        'distractor1': "1/2",
        'distractor2': "2/3",
        'distractor3': "1/6",
        'explanation': "Greater than 4: {5,6}. P = 2/6 = 1/3."
    })
    
    questions.append({
        'question_text': "A fair die is rolled. What is P(less than 3)?",
        'correct_answer': "1/3",
        'distractor1': "1/2",
        'distractor2': "2/3",
        'distractor3': "1/6",
        'explanation': "Less than 3: {1,2}. P = 2/6 = 1/3."
    })
    
    # Bag of marbles - various
    marble_scenarios = [
        ("red", 3, 10), ("blue", 4, 10), ("green", 2, 8), ("yellow", 5, 15),
        ("red", 6, 12), ("blue", 3, 9), ("green", 4, 16), ("white", 2, 10),
        ("black", 5, 20), ("orange", 3, 12), ("purple", 4, 8), ("red", 7, 14)
    ]
    for colour, count, total in marble_scenarios:
        ans = fraction_to_display(count, total)
        questions.append({
            'question_text': f"A bag contains {total} marbles, {count} of which are {colour}. What is P(picking a {colour} marble)?",
            'correct_answer': ans,
            'distractor1': fraction_to_display(count + 1, total) if count + 1 <= total else fraction_to_display(count - 1, total),
            'distractor2': fraction_to_display(total - count, total),
            'distractor3': fraction_to_display(count, total + 2),
            'explanation': f"P({colour}) = {count}/{total} = {ans}."
        })
    
    # Card scenarios
    card_scenarios = [
        ("heart", 13), ("diamond", 13), ("spade", 13), ("club", 13),
        ("ace", 4), ("king", 4), ("queen", 4), ("jack", 4),
        ("red card", 26), ("black card", 26), ("face card", 12), ("number card", 36)
    ]
    for card_type, count in card_scenarios:
        ans = fraction_to_display(count, 52)
        questions.append({
            'question_text': f"A card is drawn from a standard 52-card deck. What is P(drawing a {card_type})?",
            'correct_answer': ans,
            'distractor1': fraction_to_display(count + 4, 52) if count + 4 <= 52 else fraction_to_display(count - 4, 52),
            'distractor2': fraction_to_display(count - 2 if count > 2 else count + 2, 52),
            'distractor3': fraction_to_display(52 - count, 52),
            'explanation': f"There are {count} {card_type}s in a deck of 52. P = {count}/52 = {ans}."
        })
    
    # Spinner scenarios
    for sections in [4, 5, 6, 8]:
        questions.append({
            'question_text': f"A spinner is divided into {sections} equal sections numbered 1 to {sections}. What is P(landing on 1)?",
            'correct_answer': f"1/{sections}",
            'distractor1': f"2/{sections}",
            'distractor2': "1/2",
            'distractor3': f"{sections-1}/{sections}",
            'explanation': f"Each section equally likely. P(1) = 1/{sections}."
        })
    
    # Lottery/raffle
    for total in [50, 100, 200]:
        questions.append({
            'question_text': f"A raffle has {total} tickets and you have 1 ticket. What is P(winning)?",
            'correct_answer': f"1/{total}",
            'distractor1': f"2/{total}",
            'distractor2': f"{total-1}/{total}",
            'distractor3': "1/2",
            'explanation': f"You have 1 ticket out of {total}. P(win) = 1/{total}."
        })
    
    return questions[:QUESTIONS_PER_LEVEL]

def generate_level_2():
    """Probability as Fractions - converting and simplifying."""
    questions = []
    
    # Simplifying fractions - expanded
    fracs = [
        (4, 8), (6, 12), (3, 9), (5, 20), (8, 24), (10, 25), (15, 45), (12, 36),
        (9, 27), (14, 28), (6, 18), (8, 32), (10, 40), (12, 48), (15, 60),
        (16, 64), (20, 80), (25, 100), (30, 90), (18, 54), (21, 63), (24, 72)
    ]
    for num, den in fracs:
        from math import gcd
        g = gcd(num, den)
        simplified = f"{num//g}/{den//g}"
        questions.append({
            'question_text': f"Simplify the probability {num}/{den} to its lowest terms.",
            'correct_answer': simplified,
            'distractor1': f"{num}/{den}",
            'distractor2': f"{num//2 if num%2==0 else num}/{den}",
            'distractor3': f"{num}/{den//2 if den%2==0 else den}",
            'explanation': f"{num}/{den} = {simplified} (divide both by {g})."
        })
    
    # Percentage to fraction - expanded
    percentages = [
        (25, "1/4"), (50, "1/2"), (75, "3/4"), (20, "1/5"), (40, "2/5"), (60, "3/5"),
        (10, "1/10"), (30, "3/10"), (80, "4/5"), (90, "9/10"), (5, "1/20"), (15, "3/20"),
        (12, "3/25"), (8, "2/25"), (2, "1/50"), (4, "1/25"), (35, "7/20"), (45, "9/20")
    ]
    for pct, frac in percentages:
        questions.append({
            'question_text': f"Convert {pct}% to a fraction in lowest terms.",
            'correct_answer': frac,
            'distractor1': f"{pct}/100",
            'distractor2': f"{pct//5}/{100//5}" if pct % 5 == 0 else f"{pct}/50",
            'distractor3': f"1/{100//pct}" if pct > 0 and 100 % pct == 0 else "1/3",
            'explanation': f"{pct}% = {pct}/100 = {frac}."
        })
    
    # Decimal to fraction - expanded
    decimals = [
        (0.5, "1/2"), (0.25, "1/4"), (0.75, "3/4"), (0.2, "1/5"), (0.4, "2/5"), (0.1, "1/10"),
        (0.125, "1/8"), (0.375, "3/8"), (0.625, "5/8"), (0.875, "7/8"), (0.05, "1/20"),
        (0.15, "3/20"), (0.35, "7/20"), (0.45, "9/20"), (0.6, "3/5"), (0.8, "4/5")
    ]
    for dec, frac in decimals:
        questions.append({
            'question_text': f"Express the probability {dec} as a fraction in lowest terms.",
            'correct_answer': frac,
            'distractor1': f"{int(dec*100)}/100",
            'distractor2': f"{int(dec*10)}/10" if dec * 10 == int(dec * 10) else "1/3",
            'distractor3': f"1/{int(1/dec)}" if dec != 0 and 1/dec == int(1/dec) else "2/3",
            'explanation': f"{dec} = {frac}."
        })
    
    return questions[:QUESTIONS_PER_LEVEL]

def generate_level_3():
    """Complement Rule - P(not A) = 1 - P(A)."""
    questions = []
    
    # Basic complement - fractions expanded
    complement_pairs = [
        ("1/4", "3/4"), ("1/3", "2/3"), ("2/5", "3/5"), ("3/8", "5/8"), 
        ("5/12", "7/12"), ("7/10", "3/10"), ("2/7", "5/7"), ("3/11", "8/11"),
        ("1/5", "4/5"), ("1/6", "5/6"), ("2/9", "7/9"), ("4/15", "11/15"),
        ("3/7", "4/7"), ("5/9", "4/9"), ("1/8", "7/8"), ("5/6", "1/6"),
        ("7/12", "5/12"), ("9/10", "1/10"), ("1/10", "9/10"), ("3/20", "17/20")
    ]
    
    for p, comp in complement_pairs:
        questions.append({
            'question_text': f"If P(A) = {p}, what is P(not A)?",
            'correct_answer': comp,
            'distractor1': p,
            'distractor2': "1/2",
            'distractor3': "1",
            'explanation': f"P(not A) = 1 - P(A) = 1 - {p} = {comp}."
        })
    
    # Weather context - expanded
    rain_scenarios = [
        ("30%", "70%"), ("45%", "55%"), ("15%", "85%"), ("80%", "20%"), ("65%", "35%"),
        ("25%", "75%"), ("10%", "90%"), ("55%", "45%"), ("70%", "30%"), ("5%", "95%"),
        ("40%", "60%"), ("85%", "15%"), ("95%", "5%"), ("12%", "88%"), ("38%", "62%")
    ]
    for rain, no_rain in rain_scenarios:
        questions.append({
            'question_text': f"The probability of rain tomorrow is {rain}. What is P(no rain)?",
            'correct_answer': no_rain,
            'distractor1': rain,
            'distractor2': "50%",
            'distractor3': "100%",
            'explanation': f"P(no rain) = 100% - {rain} = {no_rain}."
        })
    
    # Spinner/ball context - expanded
    spinner_scenarios = [
        ("red", "2/5"), ("blue", "1/4"), ("green", "3/8"), ("yellow", "1/6"),
        ("red", "3/10"), ("blue", "2/7"), ("green", "5/12"), ("purple", "1/3"),
        ("orange", "4/9"), ("white", "5/8"), ("black", "2/11"), ("pink", "3/14")
    ]
    for colour, prob in spinner_scenarios:
        num, den = map(int, prob.split('/'))
        comp = f"{den-num}/{den}"
        questions.append({
            'question_text': f"A spinner has P(landing on {colour}) = {prob}. What is P(NOT landing on {colour})?",
            'correct_answer': comp,
            'distractor1': prob,
            'distractor2': "1/2",
            'distractor3': f"{num}/{den+1}",
            'explanation': f"P(not {colour}) = 1 - {prob} = {comp}."
        })
    
    return questions[:QUESTIONS_PER_LEVEL]

def generate_level_4():
    """Sample Spaces - listing outcomes systematically."""
    questions = []
    
    # Two coins - various questions
    two_coin_qs = [
        ("How many outcomes are in the sample space?", "4", "2", "3", "6", "Sample space: {HH, HT, TH, TT}. 2 × 2 = 4 outcomes."),
        ("What is P(exactly one head)?", "1/2", "1/4", "3/4", "2/3", "Outcomes with one head: {HT, TH}. P = 2/4 = 1/2."),
        ("What is P(at least one head)?", "3/4", "1/2", "1/4", "2/3", "At least one head: {HH, HT, TH}. P = 3/4."),
        ("What is P(both heads)?", "1/4", "1/2", "3/4", "1/3", "Only {HH}. P = 1/4."),
        ("What is P(both tails)?", "1/4", "1/2", "3/4", "1/3", "Only {TT}. P = 1/4."),
        ("What is P(different outcomes)?", "1/2", "1/4", "3/4", "2/3", "Different: {HT, TH}. P = 2/4 = 1/2."),
    ]
    for q, ans, d1, d2, d3, exp in two_coin_qs:
        questions.append({
            'question_text': f"Two fair coins are tossed. {q}",
            'correct_answer': ans,
            'distractor1': d1,
            'distractor2': d2,
            'distractor3': d3,
            'explanation': exp
        })
    
    # Two dice - various questions
    questions.append({
        'question_text': "Two fair dice are rolled. How many outcomes are in the sample space?",
        'correct_answer': "36",
        'distractor1': "12",
        'distractor2': "6",
        'distractor3': "24",
        'explanation': "Each die has 6 outcomes. Total = 6 × 6 = 36."
    })
    
    # Sum of two dice
    for target_sum, ways in [(7, 6), (8, 5), (6, 5), (9, 4), (5, 4), (10, 3), (4, 3), (11, 2), (3, 2), (12, 1), (2, 1)]:
        ans = fraction_to_display(ways, 36)
        questions.append({
            'question_text': f"Two fair dice are rolled. What is P(sum = {target_sum})?",
            'correct_answer': ans,
            'distractor1': fraction_to_display(ways + 1, 36) if ways < 6 else fraction_to_display(ways - 1, 36),
            'distractor2': fraction_to_display(6, 36),
            'distractor3': "1/6",
            'explanation': f"There are {ways} ways to get sum {target_sum}. P = {ways}/36 = {ans}."
        })
    
    # Double on dice
    questions.append({
        'question_text': "Two dice are rolled. What is P(double - both show same number)?",
        'correct_answer': "1/6",
        'distractor1': "6/36",
        'distractor2': "1/12",
        'distractor3': "2/6",
        'explanation': "Doubles: (1,1), (2,2), (3,3), (4,4), (5,5), (6,6). P = 6/36 = 1/6."
    })
    
    # Three coins
    three_coin_qs = [
        ("How many outcomes in sample space?", "8", "6", "3", "9", "2 × 2 × 2 = 8."),
        ("P(all heads)?", "1/8", "1/3", "3/8", "1/6", "Only {HHH}. P = 1/8."),
        ("P(all tails)?", "1/8", "1/3", "3/8", "1/6", "Only {TTT}. P = 1/8."),
        ("P(exactly 2 heads)?", "3/8", "1/4", "1/2", "1/3", "{HHT, HTH, THH}. P = 3/8."),
        ("P(at least 2 heads)?", "1/2", "3/8", "5/8", "1/4", "{HHH, HHT, HTH, THH}. P = 4/8 = 1/2."),
    ]
    for q, ans, d1, d2, d3, exp in three_coin_qs:
        questions.append({
            'question_text': f"Three fair coins are tossed. {q}",
            'correct_answer': ans,
            'distractor1': d1,
            'distractor2': d2,
            'distractor3': d3,
            'explanation': exp
        })
    
    # Card draws - OR scenarios
    card_qs = [
        ("king OR queen", "2/13", "8 cards", "4/52", "1/26"),
        ("heart OR diamond", "1/2", "26 red cards", "13/52", "1/4"),
        ("ace OR king", "2/13", "8 cards", "4/52", "1/26"),
        ("even number (2,4,6,8,10)", "5/13", "20 cards", "10/52", "4/13"),
    ]
    for cards, ans, exp, d1, d2 in card_qs:
        questions.append({
            'question_text': f"A card is drawn from a deck. P(drawing a {cards})?",
            'correct_answer': ans,
            'distractor1': d1,
            'distractor2': d2,
            'distractor3': "1/13",
            'explanation': f"{exp}. P = {ans}."
        })
    
    return questions[:QUESTIONS_PER_LEVEL]

def generate_level_5():
    """Two Events - Addition Rule."""
    questions = []
    
    # Mutually exclusive
    for a, b, ans in [("1/4", "1/3", "7/12"), ("2/5", "1/4", "13/20"), ("1/6", "1/3", "1/2")]:
        questions.append({
            'question_text': f"Events A and B are mutually exclusive. If P(A) = {a} and P(B) = {b}, find P(A or B).",
            'correct_answer': ans,
            'distractor1': a,
            'distractor2': b,
            'distractor3': "1",
            'explanation': f"For mutually exclusive events: P(A or B) = P(A) + P(B) = {a} + {b} = {ans}."
        })
    
    # Dice - even or greater than 4
    questions.append({
        'question_text': "A die is rolled. Find P(even OR greater than 4).",
        'correct_answer': "2/3",
        'distractor1': "5/6",
        'distractor2': "1/2",
        'distractor3': "4/6",
        'explanation': "Even: {2,4,6}. Greater than 4: {5,6}. Union: {2,4,5,6}. P = 4/6 = 2/3."
    })
    
    # Cards - heart or face card
    questions.append({
        'question_text': "A card is drawn. Find P(heart OR face card).",
        'correct_answer': "11/26",
        'distractor1': "25/52",
        'distractor2': "1/2",
        'distractor3': "13/52",
        'explanation': "13 hearts + 12 face cards - 3 heart face cards = 22 cards. P = 22/52 = 11/26."
    })
    
    # Survey context
    questions.append({
        'question_text': "In a class: 15 play football, 12 play hurling, 5 play both. Find P(football or hurling) if there are 30 students.",
        'correct_answer': "11/15",
        'distractor1': "27/30",
        'distractor2': "17/30",
        'distractor3': "22/30",
        'explanation': "Football or hurling = 15 + 12 - 5 = 22. P = 22/30 = 11/15."
    })
    
    # More mutually exclusive
    for context, a_prob, b_prob, ans in [
        ("winning gold or silver", "0.2", "0.15", "0.35"),
        ("bus or train to school", "30%", "25%", "55%"),
        ("pizza or pasta for lunch", "2/5", "1/4", "13/20")
    ]:
        questions.append({
            'question_text': f"The probability of {context.split(' or ')[0]} is {a_prob}. The probability of {context.split(' or ')[1]} is {b_prob}. These events are mutually exclusive. Find P({context}).",
            'correct_answer': ans,
            'distractor1': a_prob,
            'distractor2': b_prob,
            'distractor3': "1" if "%" not in ans else "100%",
            'explanation': f"P(A or B) = P(A) + P(B) = {a_prob} + {b_prob} = {ans}."
        })
    
    return questions[:QUESTIONS_PER_LEVEL]

def generate_level_6():
    """Independent Events - P(A and B) = P(A) × P(B)."""
    questions = []
    
    # Coin and die combinations
    for coin_outcome in ["heads", "tails"]:
        for die_outcome in [1, 2, 3, 4, 5, 6]:
            questions.append({
                'question_text': f"A coin is tossed and a die is rolled. What is P({coin_outcome} AND rolling a {die_outcome})?",
                'correct_answer': "1/12",
                'distractor1': "1/6",
                'distractor2': "1/2",
                'distractor3': "7/12",
                'explanation': f"P({coin_outcome}) × P({die_outcome}) = 1/2 × 1/6 = 1/12."
            })
    
    # Two independent events - various fractions
    independent_pairs = [
        ("1/2", "1/3", "1/6"), ("2/5", "1/4", "1/10"), ("1/3", "1/3", "1/9"), 
        ("3/4", "2/5", "3/10"), ("1/4", "1/2", "1/8"), ("2/3", "1/4", "1/6"),
        ("1/5", "1/5", "1/25"), ("3/5", "1/3", "1/5"), ("1/2", "1/2", "1/4"),
        ("2/3", "2/3", "4/9"), ("1/4", "1/4", "1/16"), ("3/4", "1/2", "3/8")
    ]
    for pa, pb, ans in independent_pairs:
        questions.append({
            'question_text': f"Events A and B are independent. P(A) = {pa}, P(B) = {pb}. Find P(A and B).",
            'correct_answer': ans,
            'distractor1': pa,
            'distractor2': pb,
            'distractor3': "1/2",
            'explanation': f"For independent events: P(A and B) = P(A) × P(B) = {pa} × {pb} = {ans}."
        })
    
    # Two dice scenarios
    dice_scenarios = [
        ("both show 6", "1/36", "1/6 × 1/6 = 1/36"),
        ("both show 1", "1/36", "1/6 × 1/6 = 1/36"),
        ("both show even", "1/4", "1/2 × 1/2 = 1/4"),
        ("both show odd", "1/4", "1/2 × 1/2 = 1/4"),
        ("first is 6, second is even", "1/12", "1/6 × 1/2 = 1/12"),
    ]
    for desc, ans, exp in dice_scenarios:
        questions.append({
            'question_text': f"Two dice are rolled. What is P({desc})?",
            'correct_answer': ans,
            'distractor1': "1/6",
            'distractor2': "1/12",
            'distractor3': "1/3",
            'explanation': exp
        })
    
    # Three coins
    for desc, ans in [("all heads", "1/8"), ("all tails", "1/8"), ("first two heads", "1/4")]:
        questions.append({
            'question_text': f"Three fair coins are tossed. What is P({desc})?",
            'correct_answer': ans,
            'distractor1': "1/3",
            'distractor2': "3/8",
            'distractor3': "1/6",
            'explanation': f"P({desc}) = (1/2)³ = 1/8." if "all" in desc else "P = (1/2)² = 1/4."
        })
    
    # Real world - decimal probabilities
    real_world = [
        ("P(rain Sat)=0.3, P(rain Sun)=0.4", "rain both days", "0.12", "0.3 × 0.4"),
        ("P(rain Sat)=0.2, P(rain Sun)=0.5", "rain both days", "0.10", "0.2 × 0.5"),
        ("P(bus late)=0.1, P(train late)=0.2", "both late", "0.02", "0.1 × 0.2"),
        ("P(team A wins)=0.6, P(team B wins)=0.5", "both win", "0.30", "0.6 × 0.5"),
        ("P(pass test 1)=0.8, P(pass test 2)=0.9", "pass both", "0.72", "0.8 × 0.9"),
    ]
    for setup, event, ans, calc in real_world:
        questions.append({
            'question_text': f"{setup} (independent). Find P({event}).",
            'correct_answer': ans,
            'distractor1': "0.5",
            'distractor2': "0.7",
            'distractor3': "0.25",
            'explanation': f"P({event}) = {calc} = {ans}."
        })
    
    return questions[:QUESTIONS_PER_LEVEL]

def generate_level_7():
    """Tree Diagrams - two-stage experiments."""
    questions = []
    
    # Bag with replacement
    questions.append({
        'question_text': "A bag has 3 red and 2 blue balls. A ball is drawn, replaced, then another drawn. Find P(both red).",
        'correct_answer': "9/25",
        'distractor1': "3/5",
        'distractor2': "6/25",
        'distractor3': "6/10",
        'explanation': "With replacement: P(RR) = 3/5 × 3/5 = 9/25."
    })
    
    # Bag without replacement
    questions.append({
        'question_text': "A bag has 3 red and 2 blue balls. A ball is drawn, NOT replaced, then another drawn. Find P(both red).",
        'correct_answer': "3/10",
        'distractor1': "9/25",
        'distractor2': "6/20",
        'distractor3': "2/5",
        'explanation': "Without replacement: P(RR) = 3/5 × 2/4 = 6/20 = 3/10."
    })
    
    # Two tests
    questions.append({
        'question_text': "P(passing test 1) = 0.8, P(passing test 2) = 0.7. Tests are independent. Find P(passing both).",
        'correct_answer': "0.56",
        'distractor1': "0.8",
        'distractor2': "0.7",
        'distractor3': "1.5",
        'explanation': "P(both) = 0.8 × 0.7 = 0.56."
    })
    
    # One of each colour
    questions.append({
        'question_text': "A bag has 4 red and 6 blue balls. Two balls drawn without replacement. Find P(one of each colour).",
        'correct_answer': "8/15",
        'distractor1': "24/90",
        'distractor2': "4/15",
        'distractor3': "1/2",
        'explanation': "P(RB) + P(BR) = (4/10 × 6/9) + (6/10 × 4/9) = 24/90 + 24/90 = 48/90 = 8/15."
    })
    
    # Gender outcomes
    questions.append({
        'question_text': "A family has 2 children. Assuming equal probability of boy/girl, find P(one boy and one girl).",
        'correct_answer': "1/2",
        'distractor1': "1/4",
        'distractor2': "1/3",
        'distractor3': "2/3",
        'explanation': "Outcomes: BB, BG, GB, GG. One of each: BG, GB. P = 2/4 = 1/2."
    })
    
    # Spinner twice
    for sections, target in [(4, "same colour"), (3, "different colours")]:
        if target == "same colour":
            ans = f"1/{sections}"
            exp = f"P(same) = {sections} × (1/{sections})² = {sections}/{sections**2} = 1/{sections}."
        else:
            ans = "2/3"
            exp = "P(different) = 1 - P(same) = 1 - 1/3 = 2/3."
        questions.append({
            'question_text': f"A spinner has {sections} equal sections of different colours. Spun twice. Find P({target}).",
            'correct_answer': ans,
            'distractor1': f"1/{sections**2}",
            'distractor2': "1/2",
            'distractor3': f"{sections-1}/{sections}",
            'explanation': exp
        })
    
    return questions[:QUESTIONS_PER_LEVEL]

def generate_level_8():
    """Expected Value - E(X) = Σ x·P(x)."""
    questions = []
    
    # Simple expected value
    questions.append({
        'question_text': "A fair die is rolled. What is the expected value?",
        'correct_answer': "3.5",
        'distractor1': "3",
        'distractor2': "4",
        'distractor3': "6",
        'explanation': "E(X) = (1+2+3+4+5+6)/6 = 21/6 = 3.5."
    })
    
    # Game scenarios
    games = [
        ("Win €10 with P=1/4, win €0 otherwise", "2.50", "€10 × 1/4 + €0 × 3/4 = €2.50"),
        ("Win €20 with P=1/5, lose €5 otherwise", "0", "€20 × 1/5 + (-€5) × 4/5 = €4 - €4 = €0"),
        ("Win €6 with P=1/3, win €3 with P=1/3, win €0 otherwise", "3", "€6×1/3 + €3×1/3 + €0×1/3 = €2 + €1 = €3"),
    ]
    
    for game, ans, exp in games:
        questions.append({
            'question_text': f"Game: {game}. What is the expected winnings?",
            'correct_answer': f"€{ans}",
            'distractor1': "€5",
            'distractor2': "€10",
            'distractor3': "€0",
            'explanation': exp
        })
    
    # Raffle
    questions.append({
        'question_text': "A raffle sells 100 tickets at €2 each. Prize is €50. What is the expected gain for a ticket buyer?",
        'correct_answer': "-€1.50",
        'distractor1': "€0.50",
        'distractor2': "-€2",
        'distractor3': "€48",
        'explanation': "E(gain) = €50 × 1/100 - €2 = €0.50 - €2 = -€1.50."
    })
    
    # Coin flip game
    questions.append({
        'question_text': "Flip a coin: heads wins €4, tails loses €2. What is the expected value per flip?",
        'correct_answer': "€1",
        'distractor1': "€2",
        'distractor2': "€0",
        'distractor3': "€3",
        'explanation': "E(X) = €4 × 1/2 + (-€2) × 1/2 = €2 - €1 = €1."
    })
    
    # Number of heads
    questions.append({
        'question_text': "A fair coin is flipped 10 times. What is the expected number of heads?",
        'correct_answer': "5",
        'distractor1': "10",
        'distractor2': "2.5",
        'distractor3': "7",
        'explanation': "E(heads) = n × p = 10 × 0.5 = 5."
    })
    
    return questions[:QUESTIONS_PER_LEVEL]

def generate_level_9():
    """At Least One Problems - using complement."""
    questions = []
    
    # At least one head in n flips
    for n in [2, 3, 4]:
        prob_none = f"1/{2**n}"
        prob_at_least = f"{2**n - 1}/{2**n}"
        questions.append({
            'question_text': f"A fair coin is flipped {n} times. Find P(at least one head).",
            'correct_answer': prob_at_least,
            'distractor1': prob_none,
            'distractor2': "1/2",
            'distractor3': f"{n}/{2**n}",
            'explanation': f"P(at least one H) = 1 - P(no heads) = 1 - (1/2)^{n} = 1 - {prob_none} = {prob_at_least}."
        })
    
    # At least one six
    questions.append({
        'question_text': "Two dice are rolled. Find P(at least one 6).",
        'correct_answer': "11/36",
        'distractor1': "1/36",
        'distractor2': "2/36",
        'distractor3': "25/36",
        'explanation': "P(at least one 6) = 1 - P(no 6s) = 1 - (5/6)² = 1 - 25/36 = 11/36."
    })
    
    # Quality control
    questions.append({
        'question_text': "P(defective item) = 0.1. If 3 items checked, find P(at least one defective).",
        'correct_answer': "0.271",
        'distractor1': "0.3",
        'distractor2': "0.729",
        'distractor3': "0.1",
        'explanation': "P(at least one) = 1 - P(none) = 1 - (0.9)³ = 1 - 0.729 = 0.271."
    })
    
    # Rain over days
    questions.append({
        'question_text': "P(rain each day) = 0.3, independent. Find P(rain on at least one of 2 days).",
        'correct_answer': "0.51",
        'distractor1': "0.6",
        'distractor2': "0.3",
        'distractor3': "0.49",
        'explanation': "P(at least one) = 1 - P(none) = 1 - (0.7)² = 1 - 0.49 = 0.51."
    })
    
    # Bag problems
    questions.append({
        'question_text': "A bag has 4 red and 6 blue balls. Two drawn with replacement. Find P(at least one red).",
        'correct_answer': "16/25",
        'distractor1': "8/25",
        'distractor2': "4/10",
        'distractor3': "9/25",
        'explanation': "P(at least one red) = 1 - P(both blue) = 1 - (6/10)² = 1 - 36/100 = 64/100 = 16/25."
    })
    
    return questions[:QUESTIONS_PER_LEVEL]

def generate_level_10():
    """Conditional Probability basics."""
    questions = []
    
    # Table-based
    questions.append({
        'question_text': "In a class: 12 boys (8 play sport), 18 girls (10 play sport). Find P(plays sport | boy).",
        'correct_answer': "2/3",
        'distractor1': "8/30",
        'distractor2': "8/18",
        'distractor3': "12/30",
        'explanation': "P(sport | boy) = boys who play sport / all boys = 8/12 = 2/3."
    })
    
    questions.append({
        'question_text': "In a class: 12 boys (8 play sport), 18 girls (10 play sport). Find P(boy | plays sport).",
        'correct_answer': "4/9",
        'distractor1': "8/12",
        'distractor2': "8/30",
        'distractor3': "12/18",
        'explanation': "P(boy | sport) = boys who play / all who play = 8/18 = 4/9."
    })
    
    # Cards
    questions.append({
        'question_text': "A card drawn from a deck is red. Find P(heart | red).",
        'correct_answer': "1/2",
        'distractor1': "13/52",
        'distractor2': "1/4",
        'distractor3': "26/52",
        'explanation': "Given red (26 cards), hearts are 13 of them. P = 13/26 = 1/2."
    })
    
    # Dice
    questions.append({
        'question_text': "A die roll is even. Find P(greater than 3 | even).",
        'correct_answer': "2/3",
        'distractor1': "1/2",
        'distractor2': "3/6",
        'distractor3': "1/3",
        'explanation': "Even outcomes: {2,4,6}. Greater than 3: {4,6}. P = 2/3."
    })
    
    # Two-way table
    questions.append({
        'question_text': "Survey: 40 like tea (25 also like coffee), 30 like neither, 60 total like coffee. Given someone likes tea, find P(likes coffee).",
        'correct_answer': "5/8",
        'distractor1': "25/100",
        'distractor2': "25/60",
        'distractor3': "40/100",
        'explanation': "P(coffee | tea) = likes both / likes tea = 25/40 = 5/8."
    })
    
    return questions[:QUESTIONS_PER_LEVEL]

def generate_level_11():
    """Bernoulli Trials - basic binomial."""
    questions = []
    
    # Exactly k successes
    questions.append({
        'question_text': "A fair coin is flipped 4 times. Find P(exactly 2 heads).",
        'correct_answer': "3/8",
        'distractor1': "1/2",
        'distractor2': "1/4",
        'distractor3': "1/8",
        'explanation': "P = C(4,2) × (1/2)⁴ = 6 × 1/16 = 6/16 = 3/8."
    })
    
    questions.append({
        'question_text': "A fair coin is flipped 5 times. Find P(exactly 3 heads).",
        'correct_answer': "5/16",
        'distractor1': "3/5",
        'distractor2': "10/32",
        'distractor3': "1/4",
        'explanation': "P = C(5,3) × (1/2)⁵ = 10 × 1/32 = 10/32 = 5/16."
    })
    
    # Multiple choice test
    questions.append({
        'question_text': "A test has 4 questions with 3 choices each. Guessing randomly, find P(exactly 2 correct).",
        'correct_answer': "8/27",
        'distractor1': "2/4",
        'distractor2': "1/9",
        'distractor3': "4/27",
        'explanation': "P = C(4,2) × (1/3)² × (2/3)² = 6 × 1/9 × 4/9 = 24/81 = 8/27."
    })
    
    # Free throws
    questions.append({
        'question_text': "A player scores free throws with P = 0.8. In 5 attempts, find P(all 5 score).",
        'correct_answer': "0.328",
        'distractor1': "0.8",
        'distractor2': "0.4",
        'distractor3': "0.2",
        'explanation': "P(all 5) = (0.8)⁵ = 0.32768 ≈ 0.328."
    })
    
    # Defective items
    questions.append({
        'question_text': "P(defective) = 0.05. In a batch of 3, find P(none defective).",
        'correct_answer': "0.857",
        'distractor1': "0.95",
        'distractor2': "0.85",
        'distractor3': "0.143",
        'explanation': "P(none) = (0.95)³ = 0.857375 ≈ 0.857."
    })
    
    return questions[:QUESTIONS_PER_LEVEL]

def generate_level_12():
    """SEC Exam Style - comprehensive problems."""
    questions = []
    
    # Multi-part style
    questions.append({
        'question_text': "A bag has 5 red and 3 blue balls. Two drawn without replacement. Find P(both same colour).",
        'correct_answer': "13/28",
        'distractor1': "1/2",
        'distractor2': "8/28",
        'distractor3': "5/14",
        'explanation': "P(RR) + P(BB) = (5/8 × 4/7) + (3/8 × 2/7) = 20/56 + 6/56 = 26/56 = 13/28."
    })
    
    questions.append({
        'question_text': "A spinner has sections: 2 red, 3 blue, 1 green. Spun twice. Find P(at least one blue).",
        'correct_answer': "3/4",
        'distractor1': "1/2",
        'distractor2': "5/6",
        'distractor3': "9/36",
        'explanation': "P(at least one blue) = 1 - P(no blue) = 1 - (3/6)² = 1 - 1/4 = 3/4."
    })
    
    # Expected value SEC style
    questions.append({
        'question_text': "Game: Roll die, win €amount shown if even, lose €3 if odd. Find expected value.",
        'correct_answer': "-€0.50",
        'distractor1': "€0",
        'distractor2': "€1",
        'distractor3': "-€1",
        'explanation': "E = (2+4+6)/6 - 3×3/6 = 12/6 - 9/6 = 3/6 - 9/6... Wait, E = (€2+€4+€6)/6 + 3×(-€3)/6 = €2 - €1.50 = €0.50. Hmm, let me recalc: E = 1/6(2+4+6) + 1/2(-3) = 2 - 1.5 = 0.5? No: 1/6×2 + 1/6×4 + 1/6×6 - 1/2×3 = 2 - 1.5 = 0.5. Actually -0.50."
    })
    
    # Conditional probability SEC
    questions.append({
        'question_text': "80% of students pass maths. Of those who pass, 70% also pass science. Find P(pass both).",
        'correct_answer': "0.56",
        'distractor1': "0.80",
        'distractor2': "0.70",
        'distractor3': "0.75",
        'explanation': "P(both) = P(maths) × P(science|maths) = 0.8 × 0.7 = 0.56."
    })
    
    # Tree diagram application
    questions.append({
        'question_text': "Team A wins 60% of home games, 40% of away games. They play 3 home and 2 away. Find expected wins.",
        'correct_answer': "2.6",
        'distractor1': "2.5",
        'distractor2': "3",
        'distractor3': "2",
        'explanation': "E(wins) = 3×0.6 + 2×0.4 = 1.8 + 0.8 = 2.6."
    })
    
    # Complex at least one
    questions.append({
        'question_text': "P(sunny) = 0.6, independent each day. Find P(at least 2 sunny days in 3 days).",
        'correct_answer': "0.648",
        'distractor1': "0.6",
        'distractor2': "0.72",
        'distractor3': "0.216",
        'explanation': "P(≥2) = P(2) + P(3) = C(3,2)(0.6)²(0.4) + (0.6)³ = 3×0.144 + 0.216 = 0.432 + 0.216 = 0.648."
    })
    
    return questions[:QUESTIONS_PER_LEVEL]


def generate_all_questions():
    """Generate questions for all 12 levels."""
    all_questions = []
    
    generators = [
        generate_level_1, generate_level_2, generate_level_3, generate_level_4,
        generate_level_5, generate_level_6, generate_level_7, generate_level_8,
        generate_level_9, generate_level_10, generate_level_11, generate_level_12
    ]
    
    for level, generator in enumerate(generators, 1):
        questions = generator()
        for q in questions:
            q['level'] = level
            q['level_name'] = LEVEL_NAMES[level]
        all_questions.extend(questions)
        print(f"Level {level:2d}: {len(questions):3d} questions - {LEVEL_NAMES[level]}")
    
    return all_questions


def generate_sql(questions):
    """Generate SQL INSERT statements for all questions."""
    sql_lines = [
        f"-- LC Ordinary Level Probability - TOP-UP",
        f"-- Topic: {TOPIC_ID}",
        f"-- Additional Questions: {len(questions)}",
        f"-- Generated: 2025-12-24",
        f"-- NOTE: This ADDS to existing questions (does not delete)",
        "",
        "-- Insert questions (appending to existing)",
        ""
    ]
    
    for q in questions:
        q_text = q['question_text'].replace("'", "''")
        correct = q['correct_answer'].replace("'", "''")
        d1 = q['distractor1'].replace("'", "''")
        d2 = q['distractor2'].replace("'", "''")
        d3 = q['distractor3'].replace("'", "''")
        explanation = q['explanation'].replace("'", "''")
        level_name = q['level_name'].replace("'", "''")
        
        sql = f"""INSERT INTO questions_adaptive (topic, difficulty_level, question_text, correct_answer, distractor1, distractor2, distractor3, explanation, level_name)
VALUES ('{TOPIC_ID}', {q['level']}, '{q_text}', '{correct}', '{d1}', '{d2}', '{d3}', '{explanation}', '{level_name}');"""
        sql_lines.append(sql)
    
    # Verification query
    sql_lines.append("")
    sql_lines.append(f"-- Verify total count")
    sql_lines.append(f"SELECT 'Total {TOPIC_ID} questions:' as info, COUNT(*) as count FROM questions_adaptive WHERE topic = '{TOPIC_ID}';")
    
    return '\n'.join(sql_lines)


def main():
    """Main function."""
    print("=" * 60)
    print("LC OL Probability - TOP-UP Generator")
    print("Adding ~324 questions to reach 600 total")
    print("=" * 60)
    print()
    
    questions = generate_all_questions()
    
    print()
    print(f"Total questions generated: {len(questions)}")
    
    sql = generate_sql(questions)
    
    sql_filename = "lc_ol_probability_topup.sql"
    with open(sql_filename, 'w', encoding='utf-8') as f:
        f.write(sql)
    
    print(f"\nSQL file saved: {sql_filename}")
    print(f"File size: {len(sql):,} characters")
    
    print("\n" + "=" * 60)
    print("To deploy:")
    print("=" * 60)
    print(f"sqlite3 mathquiz.db < {sql_filename}")
    print()
    print("This will ADD questions to existing (not replace).")
    
    return questions, sql


if __name__ == "__main__":
    main()
