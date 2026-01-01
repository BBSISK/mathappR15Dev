#!/usr/bin/env python3
"""
LC Higher Level - Probability Question Generator
Version: 1.0
Date: 2025-12-15

Generates 600 questions (50 per level x 12 levels) for LC HL Probability
"""

import random
from fractions import Fraction

TOPIC = 'lc_hl_probability'
MODE = 'lc_hl'

LEVEL_TITLES = [
    'Basic Probability',
    'Sample Spaces',
    'Combined Events',
    'Conditional Probability',
    'Independent Events',
    'Tree Diagrams',
    'Probability Distributions',
    'Expected Value',
    'Binomial Distribution',
    'Normal Distribution Basics',
    'Normal Distribution Applications',
    'Mastery Challenge'
]

def fraction_str(num, den):
    """Format fraction as string, simplifying where possible"""
    from math import gcd
    g = gcd(num, den)
    num, den = num // g, den // g
    if den == 1:
        return str(num)
    return f"{num}/{den}"

def make_unique_options(correct, distractors):
    """Create 4 unique options with correct answer randomly placed"""
    correct_str = str(correct)
    unique_wrong = []
    for d in distractors:
        d_str = str(d)
        if d_str != correct_str and d_str not in unique_wrong:
            unique_wrong.append(d_str)
    while len(unique_wrong) < 3:
        unique_wrong.append(f"None of these")
    options = [correct_str] + unique_wrong[:3]
    random.shuffle(options)
    return options, options.index(correct_str)

def generate_level_1():
    """Level 1: Basic Probability - single events, simple fractions"""
    questions = []
    
    # Type 1: Dice probability
    for i in range(10):
        outcomes = random.choice([
            ("even number", [2, 4, 6], 3),
            ("odd number", [1, 3, 5], 3),
            ("number greater than 4", [5, 6], 2),
            ("number less than 3", [1, 2], 2),
            ("prime number", [2, 3, 5], 3),
            ("number divisible by 3", [3, 6], 2),
            ("the number 6", [6], 1),
            ("a number greater than 2", [3, 4, 5, 6], 4),
        ])
        event, vals, count = outcomes
        correct = fraction_str(count, 6)
        distractors = [fraction_str(6-count, 6), fraction_str(count+1, 6) if count < 5 else "5/6", fraction_str(1, 6)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"A fair six-sided die is rolled once. What is the probability of getting {event}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"There are {count} favourable outcomes out of 6 possible outcomes. P = {correct}",
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Card probability
    for i in range(10):
        outcomes = random.choice([
            ("a heart", 13, 52),
            ("a red card", 26, 52),
            ("a king", 4, 52),
            ("a face card (J, Q, K)", 12, 52),
            ("an ace", 4, 52),
            ("a black card", 26, 52),
            ("a spade", 13, 52),
            ("a numbered card (2-10)", 36, 52),
        ])
        event, fav, total = outcomes
        correct = fraction_str(fav, total)
        distractors = [fraction_str(total-fav, total), fraction_str(fav+4, total) if fav+4 <= 52 else "1/2", fraction_str(fav, 54)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"A card is drawn at random from a standard 52-card deck. What is the probability of drawing {event}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"There are {fav} favourable outcomes out of {total} cards. P = {correct}",
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Bag of coloured balls
    for i in range(10):
        red = random.randint(2, 6)
        blue = random.randint(2, 6)
        green = random.randint(1, 4)
        total = red + blue + green
        color_choice = random.choice([("red", red), ("blue", blue), ("green", green)])
        color, count = color_choice
        correct = fraction_str(count, total)
        distractors = [fraction_str(total-count, total), fraction_str(count, total+1), fraction_str(count+1, total)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"A bag contains {red} red, {blue} blue, and {green} green balls. One ball is drawn at random. What is the probability it is {color}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Total balls = {total}. Number of {color} balls = {count}. P = {correct}",
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 4: Spinner probability
    for i in range(10):
        sections = random.randint(5, 10)
        color_count = random.randint(1, sections-1)
        color = random.choice(["red", "blue", "green", "yellow"])
        correct = fraction_str(color_count, sections)
        distractors = [fraction_str(sections-color_count, sections), fraction_str(color_count+1, sections) if color_count < sections else "1", fraction_str(color_count, sections+1)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"A spinner has {sections} equal sections. {color_count} sections are {color}. What is the probability of landing on {color}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P(landing on {color}) = {color_count}/{sections} = {correct}",
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 5: Probability concepts
    concepts = [
        ("What is the probability of a certain event?", "1", ["0", "1/2", "Cannot be determined"]),
        ("What is the probability of an impossible event?", "0", ["1", "1/2", "Cannot be determined"]),
        ("If P(A) = 0.3, what is P(not A)?", "0.7", ["0.3", "0.6", "1.3"]),
        ("If P(A) = 1/4, what is P(not A)?", "3/4", ["1/4", "1/2", "4/4"]),
        ("If P(A) = 2/5, what is P(not A)?", "3/5", ["2/5", "1/5", "5/5"]),
        ("If P(A) = 0.45, what is P(not A)?", "0.55", ["0.45", "0.65", "1.45"]),
        ("If P(A) = 5/8, what is P(not A)?", "3/8", ["5/8", "1/8", "8/8"]),
        ("The probability of an event must be between which values?", "0 and 1", ["0 and 100", "-1 and 1", "1 and 2"]),
        ("If P(A) = 0.6, what is P(A′)?", "0.4", ["0.6", "0.5", "1.6"]),
        ("If P(B) = 7/10, what is P(B′)?", "3/10", ["7/10", "10/7", "1"]),
    ]
    for concept in concepts:
        question, correct, distractors = concept
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The answer is {correct}. P(not A) = 1 - P(A)",
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    return questions

def generate_level_2():
    """Level 2: Sample Spaces - listing outcomes, counting"""
    questions = []
    
    # Type 1: Coin flips sample space
    for i in range(8):
        n = random.choice([2, 3])
        if n == 2:
            total = 4
            question = "Two coins are flipped. How many outcomes are in the sample space?"
            explanation = "Sample space: {HH, HT, TH, TT}. Total = 4 outcomes"
        else:
            total = 8
            question = "Three coins are flipped. How many outcomes are in the sample space?"
            explanation = "Sample space has 2³ = 8 outcomes"
        
        correct = str(total)
        distractors = [str(total*2), str(total-1), str(total+2)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Two dice sample space
    for i in range(8):
        target = random.randint(2, 12)
        if target <= 7:
            ways = target - 1
        else:
            ways = 13 - target
        
        correct = str(ways)
        distractors = [str(ways+1), str(ways+2) if ways > 1 else "3", str(max(1, ways-1))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Two dice are rolled. How many ways can the sum equal {target}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Count the pairs that sum to {target}. There are {ways} ways.",
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Probability from sample space
    for i in range(8):
        target = random.randint(4, 10)
        if target <= 7:
            ways = target - 1
        else:
            ways = 13 - target
        
        correct = fraction_str(ways, 36)
        distractors = [fraction_str(ways+1, 36), fraction_str(ways, 12), fraction_str(6, 36)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Two fair dice are rolled. What is the probability the sum equals {target}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Total outcomes = 36. Ways to get {target} = {ways}. P = {correct}",
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 4: Counting sample space elements
    for i in range(10):
        items = random.randint(3, 5)
        choices = random.randint(2, 3)
        total = items ** choices
        
        item_type = random.choice(["shirts", "flavours", "colours", "dishes"])
        choice_type = random.choice(["days", "meals", "items"])
        
        correct = str(total)
        distractors = [str(items * choices), str(total + items), str(total - items)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"If there are {items} {item_type} and {choices} {choice_type}, how many combinations are possible if repetition is allowed?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"With repetition: {items}^{choices} = {total} combinations",
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 5: Sample space size
    for i in range(8):
        n = random.randint(2, 4)
        total = 6 ** n
        correct = str(total)
        distractors = [str(6 * n), str(total + 6), str(total // 2)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"How many outcomes are in the sample space when {n} fair dice are rolled?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Each die has 6 outcomes. Total = 6^{n} = {total}",
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 6: Two coin probability
    for i in range(8):
        outcome = random.choice([
            ("exactly one head", 2, "HT, TH"),
            ("at least one head", 3, "HH, HT, TH"),
            ("two heads", 1, "HH"),
            ("no heads", 1, "TT"),
            ("at most one head", 3, "HT, TH, TT"),
        ])
        event, count, listing = outcome
        correct = fraction_str(count, 4)
        distractors = [fraction_str(4-count, 4), "1/2", fraction_str(count, 2)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Two coins are flipped. What is the probability of getting {event}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Favourable outcomes: {listing}. P = {count}/4 = {correct}",
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    return questions

def generate_level_3():
    """Level 3: Combined Events - OR and AND rules"""
    questions = []
    
    # Type 1: OR rule (mutually exclusive)
    for i in range(10):
        p1_num = random.randint(1, 4)
        p2_num = random.randint(1, 4)
        while p1_num + p2_num > 10:
            p2_num = random.randint(1, 4)
        den = 10
        
        sum_num = p1_num + p2_num
        correct = fraction_str(sum_num, den)
        distractors = [fraction_str(p1_num * p2_num, 100), fraction_str(p1_num, den), fraction_str(sum_num + 1, den)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Events A and B are mutually exclusive. If P(A) = {p1_num}/{den} and P(B) = {p2_num}/{den}, find P(A or B).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"For mutually exclusive events: P(A or B) = P(A) + P(B) = {p1_num}/{den} + {p2_num}/{den} = {correct}",
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 2: AND rule (independent)
    for i in range(10):
        p1_num = random.randint(1, 3)
        p2_num = random.randint(1, 3)
        den1 = random.choice([4, 5])
        den2 = random.choice([4, 5])
        
        prod_num = p1_num * p2_num
        prod_den = den1 * den2
        correct = fraction_str(prod_num, prod_den)
        distractors = [fraction_str(p1_num + p2_num, den1), fraction_str(p1_num, den1), fraction_str(prod_num, prod_den + 5)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Events A and B are independent. If P(A) = {p1_num}/{den1} and P(B) = {p2_num}/{den2}, find P(A and B).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"For independent events: P(A and B) = P(A) × P(B) = {p1_num}/{den1} × {p2_num}/{den2} = {correct}",
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 3: General addition rule
    for i in range(10):
        pa = random.randint(3, 6)
        pb = random.randint(3, 6)
        pab = random.randint(1, min(pa, pb) - 1)
        den = 10
        
        p_or = pa + pb - pab
        correct = fraction_str(p_or, den)
        distractors = [fraction_str(pa + pb, den), fraction_str(pa + pb + pab, den), fraction_str(pab, den)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"If P(A) = {pa}/{den}, P(B) = {pb}/{den}, and P(A and B) = {pab}/{den}, find P(A or B).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P(A or B) = P(A) + P(B) - P(A and B) = {pa}/{den} + {pb}/{den} - {pab}/{den} = {correct}",
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 4: Complement with combined events
    for i in range(10):
        p = random.randint(1, 4)
        den = 5
        
        p_comp = den - p
        correct = fraction_str(p_comp, den)
        distractors = [fraction_str(p, den), fraction_str(p + 1, den), "1"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"If P(A) = {p}/{den}, what is P(A′)?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P(A′) = 1 - P(A) = 1 - {p}/{den} = {correct}",
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 5: Card problems with OR
    for i in range(10):
        outcomes = random.choice([
            ("a king or a queen", 8, 52, "4 kings + 4 queens = 8"),
            ("a heart or a diamond", 26, 52, "13 hearts + 13 diamonds = 26"),
            ("a red card or an ace", 28, 52, "26 red + 4 aces - 2 red aces = 28"),
            ("a face card or a spade", 22, 52, "12 face + 13 spades - 3 spade faces = 22"),
            ("a club or a king", 16, 52, "13 clubs + 4 kings - 1 king of clubs = 16"),
        ])
        event, fav, total, work = outcomes
        correct = fraction_str(fav, total)
        distractors = [fraction_str(fav+4, total), fraction_str(fav-4, total) if fav > 4 else "1/13", fraction_str(fav, 54)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"A card is drawn at random. What is the probability of drawing {event}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{work}. P = {correct}",
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    return questions

def generate_level_4():
    """Level 4: Conditional Probability"""
    questions = []
    
    # Type 1: Basic conditional probability formula
    for i in range(10):
        pab = random.randint(1, 3)
        pb = random.randint(pab + 1, 8)
        den = 10
        
        # P(A|B) = P(A and B) / P(B)
        correct = fraction_str(pab, pb)
        distractors = [fraction_str(pb, pab) if pab > 0 else "2", fraction_str(pab, den), fraction_str(pab + pb, den)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"If P(A and B) = {pab}/{den} and P(B) = {pb}/{den}, find P(A|B).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P(A|B) = P(A and B) / P(B) = ({pab}/{den}) ÷ ({pb}/{den}) = {pab}/{pb} = {correct}",
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 2: Two-way table conditional probability
    for i in range(10):
        a_and_b = random.randint(10, 30)
        a_and_not_b = random.randint(10, 30)
        not_a_and_b = random.randint(10, 30)
        not_a_not_b = random.randint(10, 30)
        
        total_b = a_and_b + not_a_and_b
        
        correct = fraction_str(a_and_b, total_b)
        distractors = [fraction_str(a_and_b, a_and_b + a_and_not_b), 
                       fraction_str(not_a_and_b, total_b),
                       fraction_str(a_and_b, a_and_b + a_and_not_b + not_a_and_b + not_a_not_b)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"In a group: {a_and_b} have A and B, {a_and_not_b} have A only, {not_a_and_b} have B only, {not_a_not_b} have neither. Given someone has B, what is P(A|B)?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Total with B = {total_b}. Those with A and B = {a_and_b}. P(A|B) = {correct}",
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 3: Conditional probability word problems
    for i in range(10):
        total = 100
        both = random.randint(15, 35)
        only_a = random.randint(15, 30)
        only_b = random.randint(15, 30)
        neither = total - both - only_a - only_b
        
        total_a = both + only_a
        
        correct = fraction_str(both, total_a)
        distractors = [fraction_str(both, total), fraction_str(only_b, total), fraction_str(both + only_b, total)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        subject1 = random.choice(["Maths", "Physics", "Biology"])
        subject2 = random.choice(["Irish", "French", "German"])
        
        questions.append({
            'question_text': f"Of 100 students: {both} study both {subject1} and {subject2}, {only_a} study only {subject1}, {only_b} study only {subject2}. Given a student studies {subject1}, what is the probability they also study {subject2}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Students studying {subject1} = {total_a}. Of these, {both} also study {subject2}. P = {correct}",
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 4: Dice conditional probability
    for i in range(10):
        condition = random.choice([
            ("the number is even", [2, 4, 6], "greater than 3", [4, 6], 2, 3),
            ("the number is odd", [1, 3, 5], "less than 4", [1, 3], 2, 3),
            ("the number is greater than 2", [3, 4, 5, 6], "even", [4, 6], 2, 4),
            ("the number is less than 5", [1, 2, 3, 4], "odd", [1, 3], 2, 4),
        ])
        cond, cond_vals, event, event_vals, count, total = condition
        
        correct = fraction_str(count, total)
        distractors = [fraction_str(count, 6), fraction_str(total - count, total), fraction_str(count + 1, total)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"A die is rolled. Given that {cond}, what is the probability the number is {event}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Given {cond}, sample space is {cond_vals}. Favourable: {event_vals}. P = {correct}",
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 5: Find P(A and B) given conditional
    for i in range(10):
        pa_given_b = random.randint(1, 4)
        pb = random.randint(2, 5)
        den = 5
        
        pab = pa_given_b * pb
        den_result = den * den
        
        correct = fraction_str(pab, den_result)
        distractors = [fraction_str(pa_given_b, den), fraction_str(pb, den), fraction_str(pa_given_b + pb, den)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"If P(A|B) = {pa_given_b}/{den} and P(B) = {pb}/{den}, find P(A and B).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P(A and B) = P(A|B) × P(B) = {pa_given_b}/{den} × {pb}/{den} = {correct}",
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    return questions

def generate_level_5():
    """Level 5: Independent Events"""
    questions = []
    
    # Type 1: Testing for independence
    for i in range(10):
        pa = random.randint(2, 4)
        pb = random.randint(2, 4)
        den = 10
        
        # Independent if P(A and B) = P(A) × P(B)
        pab_independent = pa * pb
        pab_actual = random.choice([pab_independent, pab_independent + random.randint(5, 15)])
        
        if pab_actual == pab_independent:
            correct = "Yes, they are independent"
            explanation = f"P(A) × P(B) = {pa}/10 × {pb}/10 = {pab_independent}/100 = P(A and B). Independent."
        else:
            correct = "No, they are not independent"
            explanation = f"P(A) × P(B) = {pab_independent}/100 ≠ {pab_actual}/100 = P(A and B). Not independent."
        
        distractors = ["Cannot determine", "Yes, they are independent" if pab_actual != pab_independent else "No, they are not independent", "They are mutually exclusive"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"P(A) = {pa}/{den}, P(B) = {pb}/{den}, P(A and B) = {pab_actual}/100. Are A and B independent?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx, 'explanation': explanation,
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 2: Independent events - both occur
    for i in range(10):
        p1 = random.choice([0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
        p2 = random.choice([0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
        
        both = round(p1 * p2, 2)
        correct = str(both)
        distractors = [str(round(p1 + p2, 2)), str(p1), str(round(p1 + p2 - both, 2))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Two independent events have probabilities {p1} and {p2}. What is the probability both occur?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P(both) = {p1} × {p2} = {both}",
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 3: Independent events - at least one
    for i in range(10):
        p1 = random.choice([0.2, 0.3, 0.4, 0.5])
        p2 = random.choice([0.2, 0.3, 0.4, 0.5])
        
        neither = round((1 - p1) * (1 - p2), 2)
        at_least_one = round(1 - neither, 2)
        correct = str(at_least_one)
        distractors = [str(round(p1 * p2, 2)), str(round(p1 + p2, 2)), str(neither)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Two independent events have probabilities {p1} and {p2}. What is the probability at least one occurs?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P(at least one) = 1 - P(neither) = 1 - {1-p1} × {1-p2} = 1 - {neither} = {at_least_one}",
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 4: Repeated trials - independent
    for i in range(10):
        p = random.choice([0.5, 0.6, 0.7, 0.8, 0.9])
        n = random.choice([2, 3, 4])
        
        result = round(p ** n, 4)
        if result == int(result):
            result = int(result)
        correct = str(result)
        distractors = [str(round(p * n, 2)), str(round(1 - result, 4)), str(p)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"The probability of success on each trial is {p}. If {n} independent trials are performed, what is the probability of success on all trials?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P(all succeed) = {p}^{n} = {correct}",
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 5: Real-world independent events
    for i in range(10):
        p_rain = random.choice([0.2, 0.3, 0.4])
        days = random.choice([2, 3])
        
        no_rain_all = round((1 - p_rain) ** days, 3)
        correct = str(no_rain_all)
        distractors = [str(round(p_rain ** days, 3)), str(round(1 - p_rain, 1)), str(round(p_rain * days, 2))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"The probability of rain on any day is {p_rain}. Assuming days are independent, what is the probability of no rain over {days} consecutive days?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P(no rain all days) = {1-p_rain}^{days} = {correct}",
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    return questions

def generate_level_6():
    """Level 6: Tree Diagrams"""
    questions = []
    
    # Type 1: Two-stage tree - with replacement
    for i in range(10):
        red = random.randint(2, 5)
        blue = random.randint(2, 5)
        total = red + blue
        
        target = random.choice([
            ("two red balls", red * red, total * total, f"{red}/{total} × {red}/{total}"),
            ("two blue balls", blue * blue, total * total, f"{blue}/{total} × {blue}/{total}"),
            ("one of each colour", 2 * red * blue, total * total, f"2 × {red}/{total} × {blue}/{total}"),
        ])
        event, num, den, work = target
        
        correct = fraction_str(num, den)
        distractors = [fraction_str(red, total), fraction_str(blue, total), fraction_str(num + total, den)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"A bag has {red} red and {blue} blue balls. Two balls are drawn with replacement. What is P({event})?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P = {work} = {correct}",
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 2: Two-stage tree - without replacement
    for i in range(10):
        red = random.randint(3, 6)
        blue = random.randint(3, 6)
        total = red + blue
        
        target = random.choice([
            ("two red balls", red * (red - 1), total * (total - 1), f"{red}/{total} × {red-1}/{total-1}"),
            ("two blue balls", blue * (blue - 1), total * (total - 1), f"{blue}/{total} × {blue-1}/{total-1}"),
            ("one of each colour", 2 * red * blue, total * (total - 1), f"2 × {red}/{total} × {blue}/{total-1}"),
        ])
        event, num, den, work = target
        
        correct = fraction_str(num, den)
        distractors = [fraction_str(red, total), fraction_str(num, total * total), fraction_str(red * blue, den)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"A bag has {red} red and {blue} blue balls. Two balls are drawn without replacement. What is P({event})?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P = {work} = {correct}",
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 3: Sequential events with different probabilities
    for i in range(10):
        p1 = random.choice([0.6, 0.7, 0.8])
        p2 = random.choice([0.5, 0.6, 0.7])
        
        both_pass = round(p1 * p2, 2)
        correct = str(both_pass)
        distractors = [str(round(p1 + p2, 2)), str(round((1-p1)*(1-p2), 2)), str(p1)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"A student has probability {p1} of passing Exam 1 and {p2} of passing Exam 2 (independent). What is P(passing both)?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P(both pass) = {p1} × {p2} = {both_pass}",
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 4: At least one success using tree
    for i in range(10):
        p = random.choice([0.3, 0.4, 0.5, 0.6])
        
        neither = round((1-p) * (1-p), 2)
        at_least_one = round(1 - neither, 2)
        correct = str(at_least_one)
        distractors = [str(round(p * p, 2)), str(neither), str(p)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Two independent events each have probability {p}. What is P(at least one occurs)?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P(at least one) = 1 - P(none) = 1 - {1-p}² = 1 - {neither} = {at_least_one}",
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 5: Three-stage tree
    for i in range(10):
        p = random.choice([0.5, 0.6, 0.7, 0.8])
        
        all_three = round(p ** 3, 3)
        correct = str(all_three)
        distractors = [str(round(3 * p, 1)), str(round(p * p, 2)), str(round(1 - all_three, 3))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"A coin lands heads with probability {p}. If flipped 3 times, what is P(3 heads)?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P(3 heads) = {p}³ = {all_three}",
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    return questions

def generate_level_7():
    """Level 7: Probability Distributions"""
    questions = []
    
    # Type 1: Discrete probability distribution validity
    for i in range(10):
        valid = random.choice([True, False])
        if valid:
            p1 = random.randint(1, 4)
            p2 = random.randint(1, 4)
            p3 = random.randint(1, 4)
            p4 = 10 - p1 - p2 - p3
            if p4 < 0:
                p4 = 1
                p3 = 10 - p1 - p2 - p4
            correct = "Yes, it is valid"
            probs = f"{p1}/10, {p2}/10, {p3}/10, {p4}/10"
        else:
            p1, p2, p3, p4 = random.randint(2,4), random.randint(2,4), random.randint(2,4), random.randint(2,4)
            correct = "No, probabilities do not sum to 1"
            probs = f"{p1}/10, {p2}/10, {p3}/10, {p4}/10"
        
        distractors = ["Yes, it is valid" if not valid else "No, probabilities do not sum to 1", 
                       "No, negative probability", "Cannot determine"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Is this a valid probability distribution? P(X=1)={probs.split(', ')[0]}, P(X=2)={probs.split(', ')[1]}, P(X=3)={probs.split(', ')[2]}, P(X=4)={probs.split(', ')[3]}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Sum = {p1+p2+p3+p4}/10. {'Valid since sum = 1' if valid else 'Invalid since sum ≠ 1'}",
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Find missing probability
    for i in range(10):
        p1 = random.randint(1, 3)
        p2 = random.randint(1, 3)
        p3 = random.randint(1, 3)
        p4 = 10 - p1 - p2 - p3
        
        correct = fraction_str(p4, 10)
        distractors = [fraction_str(p1, 10), fraction_str(p1 + p2, 10), fraction_str(10 - p4, 10)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"X has distribution: P(X=1)={p1}/10, P(X=2)={p2}/10, P(X=3)={p3}/10, P(X=4)=k. Find k.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Sum must equal 1: {p1}/10 + {p2}/10 + {p3}/10 + k = 1, so k = {correct}",
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 3: P(X ≤ a) cumulative
    for i in range(10):
        p1, p2, p3, p4, p5 = 1, 2, 3, 2, 2
        cutoff = random.randint(1, 4)
        
        cumulative = sum([p1, p2, p3, p4, p5][:cutoff])
        correct = fraction_str(cumulative, 10)
        distractors = [fraction_str([p1,p2,p3,p4,p5][cutoff-1], 10), fraction_str(10-cumulative, 10), fraction_str(cumulative+1, 10)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P(X ≤ {cutoff}).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P(X ≤ {cutoff}) = sum of probabilities from 1 to {cutoff} = {correct}",
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 4: P(a ≤ X ≤ b)
    for i in range(10):
        probs = [1, 2, 3, 2, 2]
        a = random.randint(1, 3)
        b = random.randint(a + 1, 5)
        
        range_sum = sum(probs[a-1:b])
        correct = fraction_str(range_sum, 10)
        distractors = [fraction_str(probs[a-1], 10), fraction_str(sum(probs[:b]), 10), fraction_str(range_sum + 1, 10)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"X has P(X=1)=1/10, P(X=2)=2/10, P(X=3)=3/10, P(X=4)=2/10, P(X=5)=2/10. Find P({a} ≤ X ≤ {b}).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P({a} ≤ X ≤ {b}) = sum from X={a} to X={b} = {correct}",
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 5: Uniform distribution
    for i in range(10):
        n = random.randint(4, 8)
        a = random.randint(1, n - 2)
        b = random.randint(a + 1, n)
        
        count = b - a + 1
        correct = fraction_str(count, n)
        distractors = [fraction_str(1, n), fraction_str(a, n), fraction_str(b - a, n)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"X is uniformly distributed on {{1, 2, ..., {n}}}. Find P({a} ≤ X ≤ {b}).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Uniform: each outcome has probability 1/{n}. P({a} ≤ X ≤ {b}) = {count}/{n} = {correct}",
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    return questions

def generate_level_8():
    """Level 8: Expected Value"""
    questions = []
    
    # Type 1: Basic expected value calculation
    for i in range(10):
        x_vals = [1, 2, 3, 4]
        p_vals = [random.randint(1, 3) for _ in range(3)]
        p_vals.append(10 - sum(p_vals))
        
        ev = sum(x * p / 10 for x, p in zip(x_vals, p_vals))
        correct = str(round(ev, 1))
        distractors = [str(round(ev + 0.5, 1)), str(round(ev - 0.5, 1)), str(sum(x_vals) / 4)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        dist_str = ", ".join([f"P(X={x})={p}/10" for x, p in zip(x_vals, p_vals)])
        questions.append({
            'question_text': f"Find E(X) for: {dist_str}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"E(X) = Σ(x × P(X=x)) = {correct}",
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Dice expected value
    for i in range(8):
        modifier = random.choice([
            ("doubled", lambda x: 2*x, 7),
            ("increased by 3", lambda x: x+3, 6.5),
            ("squared", lambda x: x**2, 91/6),
        ])
        desc, func, result = modifier
        correct = str(round(result, 2))
        distractors = [str(round(result + 1, 2)), str(round(result - 1, 2)), "3.5"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"A fair die is rolled. If the score is {desc}, what is the expected value?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"E(X) = 3.5 for fair die. After transformation: E = {correct}",
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Fair game calculation
    for i in range(8):
        win_amount = random.randint(10, 50)
        lose_amount = random.randint(5, 20)
        p_win = random.choice([Fraction(1, 4), Fraction(1, 3), Fraction(2, 5)])
        p_lose = 1 - p_win
        
        ev = float(win_amount * p_win - lose_amount * p_lose)
        correct = str(round(ev, 2))
        distractors = [str(win_amount - lose_amount), str(round(ev + 5, 2)), str(round(-ev, 2))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"A game pays €{win_amount} with probability {p_win} and loses €{lose_amount} otherwise. What is E(X)?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"E(X) = {win_amount} × {p_win} - {lose_amount} × {p_lose} = {correct}",
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 4: E(aX + b)
    for i in range(8):
        ex = random.randint(3, 8)
        a = random.randint(2, 5)
        b = random.randint(-5, 10)
        
        result = a * ex + b
        correct = str(result)
        distractors = [str(a * ex), str(ex + b), str(a + ex + b)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        sign = "+" if b >= 0 else ""
        questions.append({
            'question_text': f"If E(X) = {ex}, find E({a}X {sign}{b}).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"E({a}X {sign}{b}) = {a}×E(X) {sign}{b} = {a}×{ex} {sign}{b} = {correct}",
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 5: Variance calculation
    for i in range(8):
        ex = random.randint(4, 7)
        ex2 = ex ** 2 + random.randint(2, 6)  # E(X²) > E(X)²
        
        var = ex2 - ex ** 2
        correct = str(var)
        distractors = [str(ex2), str(ex ** 2), str(var + ex)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"If E(X) = {ex} and E(X²) = {ex2}, find Var(X).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Var(X) = E(X²) - [E(X)]² = {ex2} - {ex}² = {ex2} - {ex**2} = {correct}",
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 6: Var(aX + b)
    for i in range(8):
        var_x = random.randint(4, 12)
        a = random.randint(2, 4)
        b = random.randint(1, 10)
        
        result = a ** 2 * var_x
        correct = str(result)
        distractors = [str(a * var_x), str(a * var_x + b), str(var_x + b)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"If Var(X) = {var_x}, find Var({a}X + {b}).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Var(aX + b) = a²Var(X). Var({a}X + {b}) = {a}² × {var_x} = {correct}",
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    return questions

def generate_level_9():
    """Level 9: Binomial Distribution"""
    questions = []
    
    # Helper for binomial coefficient
    def C(n, r):
        from math import factorial
        if r > n or r < 0:
            return 0
        return factorial(n) // (factorial(r) * factorial(n - r))
    
    # Type 1: Identify binomial parameters
    for i in range(8):
        n = random.randint(5, 15)
        p = random.choice([0.2, 0.3, 0.4, 0.5, 0.6])
        
        correct = f"n = {n}, p = {p}"
        distractors = [f"n = {n}, p = {1-p}", f"n = {n-1}, p = {p}", f"n = {n+1}, p = {p}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        context = random.choice([
            f"A fair coin (P(H) = {p}) is flipped {n} times",
            f"A biased die lands on 6 with probability {p}. It is rolled {n} times",
            f"Each trial has success probability {p}. There are {n} independent trials",
        ])
        
        questions.append({
            'question_text': f"{context}. X = number of successes. Identify the binomial parameters.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"X ~ B({n}, {p}). n = number of trials, p = probability of success",
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Calculate P(X = k) - small numbers
    for i in range(10):
        n = random.randint(3, 5)
        p_frac = random.choice([(1, 2), (1, 3), (1, 4), (2, 3)])
        p = p_frac[0] / p_frac[1]
        k = random.randint(1, n - 1)
        
        coeff = C(n, k)
        prob = coeff * (p ** k) * ((1 - p) ** (n - k))
        
        # Express answer as fraction where possible
        correct = str(round(prob, 4))
        distractors = [str(round(prob * 2, 4)), str(round(prob / 2, 4)), str(round(1 - prob, 4))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"X ~ B({n}, {p_frac[0]}/{p_frac[1]}). Calculate P(X = {k}).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P(X = {k}) = C({n},{k}) × ({p_frac[0]}/{p_frac[1]})^{k} × ({p_frac[1]-p_frac[0]}/{p_frac[1]})^{n-k} = {correct}",
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Expected value of binomial
    for i in range(8):
        n = random.randint(10, 50)
        p = random.choice([0.2, 0.25, 0.3, 0.4, 0.5])
        
        ev = n * p
        correct = str(ev)
        distractors = [str(n * (1 - p)), str(n + p), str(n / p)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"X ~ B({n}, {p}). Find E(X).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"E(X) = np = {n} × {p} = {correct}",
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 4: Variance of binomial
    for i in range(8):
        n = random.randint(10, 40)
        p = random.choice([0.2, 0.25, 0.3, 0.4, 0.5])
        
        var = n * p * (1 - p)
        correct = str(var)
        distractors = [str(n * p), str(n * (1 - p)), str(round(var ** 0.5, 2))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"X ~ B({n}, {p}). Find Var(X).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Var(X) = np(1-p) = {n} × {p} × {1-p} = {correct}",
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 5: P(X ≥ 1) using complement
    for i in range(8):
        n = random.randint(3, 6)
        p = random.choice([0.1, 0.2, 0.3, 0.4])
        
        p_none = (1 - p) ** n
        p_at_least_one = round(1 - p_none, 4)
        correct = str(p_at_least_one)
        distractors = [str(round(p_none, 4)), str(round(n * p, 4)), str(p)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"X ~ B({n}, {p}). Find P(X ≥ 1).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P(X ≥ 1) = 1 - P(X = 0) = 1 - {1-p}^{n} = 1 - {round(p_none, 4)} = {correct}",
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 6: Applied binomial problems
    for i in range(8):
        n = random.randint(4, 8)
        p = 0.5
        
        prob_all = p ** n
        correct = str(round(prob_all, 4))
        distractors = [str(round(1 - prob_all, 4)), str(round(n * p, 4)), str(round(prob_all * 2, 4))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"A fair coin is flipped {n} times. What is the probability of getting all heads?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P(all heads) = 0.5^{n} = {correct}",
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    return questions

def generate_level_10():
    """Level 10: Normal Distribution Basics"""
    questions = []
    
    # Type 1: Standard normal - z-score meaning
    for i in range(8):
        z = random.choice([1, 2, 3, -1, -2])
        if z > 0:
            meaning = f"{z} standard deviation(s) above the mean"
        else:
            meaning = f"{abs(z)} standard deviation(s) below the mean"
        
        distractors = [f"{abs(z)} standard deviation(s) {'below' if z > 0 else 'above'} the mean",
                       f"{z} units from 0", "At the mean"]
        options, correct_idx = make_unique_options(meaning, distractors)
        
        questions.append({
            'question_text': f"For a standard normal distribution, what does z = {z} represent?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"z = {z} means the value is {meaning}",
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Calculate z-score
    for i in range(10):
        mu = random.choice([50, 60, 70, 80, 100])
        sigma = random.choice([5, 10, 15])
        x = mu + random.choice([-2, -1, 1, 2]) * sigma
        
        z = (x - mu) / sigma
        correct = str(int(z))
        distractors = [str(int(-z)), str(int(z + 1)), str(int(z - 1))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"X ~ N({mu}, {sigma}²). Find the z-score for x = {x}.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"z = (x - μ)/σ = ({x} - {mu})/{sigma} = {correct}",
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Empirical rule percentages
    for i in range(10):
        scenario = random.choice([
            ("within 1 standard deviation of the mean", "68%", ["34%", "95%", "99.7%"]),
            ("within 2 standard deviations of the mean", "95%", ["68%", "99.7%", "47.5%"]),
            ("within 3 standard deviations of the mean", "99.7%", ["95%", "68%", "99%"]),
            ("above the mean", "50%", ["34%", "68%", "84%"]),
            ("between the mean and +1σ", "34%", ["50%", "68%", "16%"]),
        ])
        desc, correct, distractors = scenario
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"For a normal distribution, what percentage of data lies {desc}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"By the empirical rule, approximately {correct} of data lies {desc}",
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 4: Convert x to z and find probability region
    for i in range(10):
        mu = 100
        sigma = 15
        x = random.choice([85, 115, 130, 70])
        z = (x - mu) / sigma
        
        if z > 0:
            region = f"above {x}"
            approx = "less than 50%"
        else:
            region = f"below {x}"
            approx = "less than 50%"
        
        correct = f"z = {z:.1f}"
        distractors = [f"z = {-z:.1f}", f"z = {z+1:.1f}", f"z = {z/2:.1f}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"IQ scores are N(100, 15²). What is the z-score for an IQ of {x}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"z = ({x} - 100)/15 = {z:.1f}",
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 5: Finding x from z
    for i in range(12):
        mu = random.choice([50, 60, 100])
        sigma = random.choice([5, 10, 15])
        z = random.choice([-2, -1, 1, 2])
        
        x = mu + z * sigma
        correct = str(x)
        distractors = [str(mu - z * sigma), str(x + sigma), str(x - sigma)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"X ~ N({mu}, {sigma}²). If z = {z}, find x.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"x = μ + zσ = {mu} + ({z})({sigma}) = {correct}",
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    return questions

def generate_level_11():
    """Level 11: Normal Distribution Applications"""
    questions = []
    
    # Type 1: Probability using z-tables (conceptual)
    for i in range(8):
        z = random.choice([1.0, 1.5, 2.0, -1.0, -1.5])
        # Approximate probabilities
        z_probs = {1.0: 0.8413, 1.5: 0.9332, 2.0: 0.9772, -1.0: 0.1587, -1.5: 0.0668}
        prob = z_probs[z]
        
        correct = str(round(prob, 4))
        distractors = [str(round(1 - prob, 4)), str(round(prob + 0.1, 4)), str(round(prob - 0.15, 4))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"For Z ~ N(0,1), P(Z < {z}) ≈ {correct}. What is P(Z > {z})?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P(Z > {z}) = 1 - P(Z < {z}) = 1 - {correct} = {round(1-prob, 4)}",
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Applied normal problems
    for i in range(8):
        mu = 170
        sigma = 10
        x = random.choice([160, 180, 190])
        z = (x - mu) / sigma
        
        correct = str(z)
        distractors = [str(-z), str(z + 0.5), str(round((x - mu) / (2 * sigma), 1))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Heights are normally distributed with μ = {mu} cm and σ = {sigma} cm. Find the z-score for a height of {x} cm.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"z = ({x} - {mu})/{sigma} = {correct}",
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Percentile problems
    for i in range(8):
        mu = 500
        sigma = 100
        # Common z-values for percentiles
        percentiles = [(84, 1.0), (16, -1.0), (97.5, 2.0), (2.5, -2.0)]
        perc, z = random.choice(percentiles)
        
        x = mu + z * sigma
        correct = str(int(x))
        distractors = [str(int(x + sigma)), str(int(x - sigma)), str(mu)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"SAT scores are N({mu}, {sigma}²). The {perc}th percentile corresponds to z = {z}. What score is the {perc}th percentile?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"x = μ + zσ = {mu} + ({z})({sigma}) = {correct}",
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 4: Inverse normal problems
    for i in range(8):
        mu = random.choice([50, 100, 200])
        sigma = random.choice([10, 15, 25])
        z = random.choice([1.28, 1.645, 1.96, 2.33])
        percentile = {1.28: 90, 1.645: 95, 1.96: 97.5, 2.33: 99}[z]
        
        x = round(mu + z * sigma, 1)
        correct = str(x)
        distractors = [str(round(mu - z * sigma, 1)), str(round(x + sigma, 1)), str(mu)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"X ~ N({mu}, {sigma}²). The {percentile}th percentile has z = {z}. Find x.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"x = {mu} + {z} × {sigma} = {correct}",
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 5: P(a < X < b) problems
    for i in range(8):
        mu = 100
        sigma = 15
        a = mu - sigma
        b = mu + sigma
        
        correct = "68%"
        distractors = ["95%", "99.7%", "50%"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"X ~ N({mu}, {sigma}²). What percentage of values lie between {a} and {b}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{a} and {b} are exactly μ ± σ. By the empirical rule, 68% of data lies within 1σ of the mean.",
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 6: Quality control applications
    for i in range(10):
        mu = random.choice([200, 250, 300])
        sigma = random.choice([5, 10])
        spec = random.choice([
            (mu - 2 * sigma, mu + 2 * sigma, "within specification (μ ± 2σ)", "95%"),
            (mu - sigma, mu + sigma, "within specification (μ ± σ)", "68%"),
            (mu - 3 * sigma, mu + 3 * sigma, "within specification (μ ± 3σ)", "99.7%"),
        ])
        lower, upper, desc, correct = spec
        
        distractors = ["68%" if correct != "68%" else "95%", 
                       "99.7%" if correct != "99.7%" else "95%",
                       "50%"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Machine output ~ N({mu}, {sigma}²). Acceptable range is {lower} to {upper}. What percentage passes?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Range is μ ± {(upper-mu)//sigma}σ. By empirical rule: {correct}",
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    return questions

def generate_level_12():
    """Level 12: Mastery Challenge - Mixed advanced problems"""
    questions = []
    
    # Type 1: Bayes' theorem
    for i in range(8):
        p_a = random.choice([0.01, 0.02, 0.05])  # P(disease)
        p_b_given_a = random.choice([0.95, 0.98, 0.99])  # P(positive | disease)
        p_b_given_not_a = random.choice([0.05, 0.10])  # P(positive | no disease)
        
        p_not_a = 1 - p_a
        p_b = p_a * p_b_given_a + p_not_a * p_b_given_not_a
        p_a_given_b = round((p_a * p_b_given_a) / p_b, 3)
        
        correct = str(p_a_given_b)
        distractors = [str(p_b_given_a), str(round(p_b, 3)), str(round(p_a_given_b + 0.2, 3))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"A disease affects {p_a*100:.0f}% of people. A test is {p_b_given_a*100:.0f}% accurate for positive cases and has a {p_b_given_not_a*100:.0f}% false positive rate. If someone tests positive, what is P(disease|positive)?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Using Bayes: P(D|+) = P(+|D)P(D) / P(+) = {p_a} × {p_b_given_a} / {round(p_b, 4)} = {correct}",
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Complex binomial
    for i in range(8):
        n = random.randint(5, 8)
        p = 0.5
        k = random.randint(2, n - 2)
        
        from math import factorial
        def C(n, r):
            return factorial(n) // (factorial(r) * factorial(n - r))
        
        prob = sum(C(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))
        correct = str(round(prob, 4))
        distractors = [str(round(1 - prob, 4)), str(round(prob / 2, 4)), str(round(prob + 0.1, 4))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"X ~ B({n}, 0.5). Find P(X ≥ {k}).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P(X ≥ {k}) = Σ P(X = i) for i = {k} to {n} = {correct}",
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Normal approximation to binomial
    for i in range(6):
        n = random.choice([100, 200])
        p = 0.5
        
        mu = n * p
        sigma = round((n * p * (1 - p)) ** 0.5, 2)
        
        correct = f"μ = {int(mu)}, σ ≈ {sigma}"
        distractors = [f"μ = {int(mu)}, σ ≈ {round(sigma*2, 2)}", 
                       f"μ = {int(mu/2)}, σ ≈ {sigma}",
                       f"μ = {int(mu)}, σ ≈ {round(sigma/2, 2)}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"X ~ B({n}, {p}) can be approximated by N(μ, σ²). Find μ and σ.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"For binomial: μ = np = {int(mu)}, σ = √(np(1-p)) ≈ {sigma}",
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 4: Combined probability concepts
    for i in range(8):
        p_a = random.randint(3, 6) / 10
        p_b = random.randint(3, 6) / 10
        
        # Independent events
        p_both = round(p_a * p_b, 2)
        p_either = round(p_a + p_b - p_both, 2)
        p_neither = round((1 - p_a) * (1 - p_b), 2)
        
        question_type = random.choice([
            (f"P(neither A nor B)", p_neither),
            (f"P(exactly one of A or B)", round(p_either - p_both, 2)),
        ])
        q_text, correct = question_type
        correct = str(correct)
        distractors = [str(p_both), str(p_either), str(round(float(correct) + 0.1, 2))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"A and B are independent with P(A) = {p_a} and P(B) = {p_b}. Find {q_text}.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"For independent events: {q_text} = {correct}",
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 5: Geometric probability
    for i in range(6):
        p = random.choice([0.2, 0.25, 0.3, 0.4])
        k = random.randint(2, 5)
        
        # P(first success on trial k) = (1-p)^(k-1) * p
        prob = round(((1 - p) ** (k - 1)) * p, 4)
        correct = str(prob)
        distractors = [str(round(p ** k, 4)), str(round((1 - p) ** k, 4)), str(p)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Probability of success is {p}. What is P(first success on trial {k})?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Geometric: P(X = {k}) = (1-{p})^{k-1} × {p} = {correct}",
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 6: Conditional expected value
    for i in range(6):
        # Dice: E(X | X > 3) = (4+5+6)/3 = 5
        condition = random.choice([
            ("X > 3", [4, 5, 6], 5),
            ("X ≤ 3", [1, 2, 3], 2),
            ("X is even", [2, 4, 6], 4),
            ("X is odd", [1, 3, 5], 3),
        ])
        cond_text, values, ev = condition
        
        correct = str(ev)
        distractors = ["3.5", str(ev + 1), str(ev - 1)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"A fair die is rolled. Find E(X | {cond_text}).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Given {cond_text}, possible values are {values}. E(X | {cond_text}) = {'+'.join(map(str, values))}/{len(values)} = {correct}",
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 7: Complex tree diagram
    for i in range(8):
        p_rain = random.choice([0.3, 0.4])
        p_late_if_rain = random.choice([0.6, 0.7])
        p_late_if_no_rain = random.choice([0.1, 0.2])
        
        p_late = round(p_rain * p_late_if_rain + (1 - p_rain) * p_late_if_no_rain, 3)
        correct = str(p_late)
        distractors = [str(p_late_if_rain), str(round(p_late + 0.1, 3)), str(round(p_rain + p_late_if_rain, 3))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"P(rain) = {p_rain}. If it rains, P(late) = {p_late_if_rain}. Otherwise, P(late) = {p_late_if_no_rain}. Find P(late).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"P(late) = P(rain)P(late|rain) + P(no rain)P(late|no rain) = {p_rain}×{p_late_if_rain} + {1-p_rain}×{p_late_if_no_rain} = {correct}",
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    return questions

def main():
    all_questions = []
    generators = [
        generate_level_1, generate_level_2, generate_level_3, generate_level_4,
        generate_level_5, generate_level_6, generate_level_7, generate_level_8,
        generate_level_9, generate_level_10, generate_level_11, generate_level_12,
    ]
    
    print(f"Generating questions for {TOPIC}...")
    print("=" * 50)
    
    for level, generator in enumerate(generators, 1):
        questions = generator()
        all_questions.extend(questions)
        print(f"Level {level} ({LEVEL_TITLES[level-1]}): {len(questions)} questions")
    
    print("=" * 50)
    print(f"Total questions generated: {len(all_questions)}")
    
    # Output SQL
    sql_statements = []
    for q in all_questions:
        q_text = q['question_text'].replace("'", "''")
        opt_a = q['option_a'].replace("'", "''")
        opt_b = q['option_b'].replace("'", "''")
        opt_c = q['option_c'].replace("'", "''")
        opt_d = q['option_d'].replace("'", "''")
        expl = q['explanation'].replace("'", "''")
        
        sql = f"""INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('{q_text}', '{opt_a}', '{opt_b}', '{opt_c}', '{opt_d}', {q['correct_idx']},
'{TOPIC}', {q['difficulty']}, '{q['difficulty_band']}', '{MODE}', '{expl}', 1);"""
        sql_statements.append(sql)
    
    sql_file = f'/home/claude/{TOPIC}_questions.sql'
    with open(sql_file, 'w') as f:
        f.write(f"-- LC Higher Level - Probability Questions\n")
        f.write(f"-- Generated: 2025-12-15\n")
        f.write(f"-- Total: {len(all_questions)} questions\n\n")
        f.write('\n'.join(sql_statements))
    
    print(f"\nSQL file written to: {sql_file}")
    return all_questions

if __name__ == '__main__':
    main()
