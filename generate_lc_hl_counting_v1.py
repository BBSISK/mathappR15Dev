#!/usr/bin/env python3
"""
LC Higher Level - Counting & Combinatorics Question Generator
Version: 1.0
Date: 2025-12-15

Generates 600 questions (50 per level x 12 levels) for LC HL Counting & Combinatorics
"""

import random
import math

TOPIC = 'lc_hl_counting'
MODE = 'lc_hl'

LEVEL_TITLES = [
    'Fundamental Counting Principle',
    'Factorials',
    'Permutations - Basics',
    'Permutations - Restrictions',
    'Combinations - Basics',
    'Combinations - Selection Problems',
    'Permutations vs Combinations',
    'Arrangements with Repetition',
    'Circular Arrangements',
    'Partitions & Distributions',
    'Pascal\'s Triangle & Binomial',
    'Mastery Challenge'
]

def make_unique_options(correct, distractors):
    correct_str = str(correct)
    unique_wrong = []
    for d in distractors:
        d_str = str(d)
        if d_str != correct_str and d_str not in unique_wrong:
            unique_wrong.append(d_str)
    while len(unique_wrong) < 3:
        unique_wrong.append("None of these")
    options = [correct_str] + unique_wrong[:3]
    random.shuffle(options)
    return options, options.index(correct_str)

def factorial(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def perm(n, r):
    return factorial(n) // factorial(n - r)

def comb(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def generate_level_1():
    """Level 1: Fundamental Counting Principle"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            # Two choices
            a = random.randint(3, 8)
            b = random.randint(3, 8)
            total = a * b
            correct, distractors = str(total), [str(a + b), str(a * b + 1), str(total - 1)]
            question = f"A restaurant offers {a} starters and {b} mains. How many different two-course meals are possible?"
            explanation = f"By multiplication principle: {a} × {b} = {total} meals"
        elif qtype == 2:
            # Three choices
            a = random.randint(2, 5)
            b = random.randint(3, 6)
            c = random.randint(2, 4)
            total = a * b * c
            correct, distractors = str(total), [str(a + b + c), str(a * b), str(total + a)]
            question = f"Choose 1 shirt from {a}, 1 trouser from {b}, and 1 tie from {c}. How many outfits?"
            explanation = f"{a} × {b} × {c} = {total} outfits"
        elif qtype == 3:
            # Digits without repetition
            correct, distractors = "90", ["100", "81", "99"]
            question = "How many 2-digit numbers can be formed using digits 0-9 (no repetition)?"
            explanation = "First digit: 9 choices (1-9), second: 9 choices. 9 × 9 = 81. Wait - 9 × 9 = 81"
            # Actually: first digit 9 (not 0), second digit 9 (any except first) = 81
            correct, distractors = "81", ["90", "100", "72"]
            explanation = "First digit: 9 choices (1-9), second: 9 choices (0-9 except first). 9 × 9 = 81"
        elif qtype == 4:
            # PIN codes
            digits = random.randint(3, 4)
            total = 10 ** digits
            correct, distractors = str(total), [str(10 * digits), str(total // 10), str(total + 1)]
            question = f"How many {digits}-digit PIN codes are possible (digits can repeat)?"
            explanation = f"10 choices for each digit: 10^{digits} = {total}"
        else:
            # Routes
            a = random.randint(2, 4)
            b = random.randint(2, 4)
            total = a * b
            correct, distractors = str(total), [str(a + b), str(2 * a * b), str(total - 1)]
            question = f"There are {a} roads from A to B and {b} roads from B to C. How many routes from A to C via B?"
            explanation = f"{a} × {b} = {total} routes"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 1, 'difficulty_band': 'foundation'})
    return questions

def generate_level_2():
    """Level 2: Factorials"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 6)
        if qtype == 1:
            # Calculate factorial
            n = random.randint(4, 7)
            result = factorial(n)
            correct, distractors = str(result), [str(result + n), str(result // n), str(n * n)]
            question = f"Calculate {n}!"
            explanation = f"{n}! = {' × '.join(str(i) for i in range(n, 0, -1))} = {result}"
        elif qtype == 2:
            # Simplify n!/k!
            n = random.randint(6, 10)
            k = n - random.randint(2, 3)
            result = perm(n, n - k)
            correct, distractors = str(result), [str(n * k), str(factorial(n - k)), str(result + n)]
            question = f"Simplify {n}!/{k}!"
            explanation = f"{n}!/{k}! = {n} × {n-1} × ... × {k+1} = {result}"
        elif qtype == 3:
            # 0! = 1
            correct, distractors = "1", ["0", "undefined", "∞"]
            question = "What is 0!?"
            explanation = "By definition, 0! = 1"
        elif qtype == 4:
            # n!/(n-1)!
            n = random.randint(5, 12)
            correct, distractors = str(n), [str(n - 1), str(factorial(n)), str(n + 1)]
            question = f"Simplify {n}!/{n-1}!"
            explanation = f"{n}!/{n-1}! = {n}"
        elif qtype == 5:
            # Expression with factorials
            n = random.randint(4, 6)
            result = factorial(n + 1) // factorial(n)
            correct, distractors = str(result), [str(n), str(result + 1), str(factorial(n))]
            question = f"Simplify ({n+1})!/{n}!"
            explanation = f"({n+1})!/{n}! = {n+1}"
        else:
            # n!/(n-2)!
            n = random.randint(5, 10)
            result = n * (n - 1)
            correct, distractors = str(result), [str(n - 2), str(n * n), str(result + 1)]
            question = f"Simplify {n}!/{n-2}!"
            explanation = f"{n}!/{n-2}! = {n} × {n-1} = {result}"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 2, 'difficulty_band': 'foundation'})
    return questions

def generate_level_3():
    """Level 3: Permutations - Basics"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            # nPr calculation
            n = random.randint(5, 8)
            r = random.randint(2, 4)
            result = perm(n, r)
            correct, distractors = str(result), [str(comb(n, r)), str(n * r), str(result + n)]
            question = f"Calculate {n}P{r} (permutations of {r} from {n})."
            explanation = f"{n}P{r} = {n}!/({n}-{r})! = {result}"
        elif qtype == 2:
            # Arrange all items
            n = random.randint(4, 6)
            result = factorial(n)
            correct, distractors = str(result), [str(n * n), str(result // n), str(n)]
            question = f"In how many ways can {n} different books be arranged on a shelf?"
            explanation = f"{n}! = {result} arrangements"
        elif qtype == 3:
            # Arrange some items
            n = random.randint(6, 8)
            r = random.randint(3, 4)
            result = perm(n, r)
            correct, distractors = str(result), [str(comb(n, r)), str(factorial(n)), str(n * r)]
            question = f"From {n} athletes, how many ways to award gold, silver, bronze ({r} positions)?"
            explanation = f"{n}P{r} = {result} ways"
        elif qtype == 4:
            # Word arrangements (all different letters)
            words = [("MATHS", 5, 120), ("CARD", 4, 24), ("HELP", 4, 24), ("STUDY", 5, 120)]
            word, n, result = random.choice(words)
            correct, distractors = str(result), [str(n * n), str(result // 2), str(result + n)]
            question = f"How many arrangements of the letters in '{word}'?"
            explanation = f"{n} different letters: {n}! = {result}"
        else:
            # Seats in a row
            n = random.randint(4, 6)
            result = factorial(n)
            correct, distractors = str(result), [str(n * n), str(2 * n), str(result // 2)]
            question = f"{n} students sit in {n} chairs in a row. How many seating arrangements?"
            explanation = f"{n}! = {result} arrangements"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 3, 'difficulty_band': 'foundation'})
    return questions

def generate_level_4():
    """Level 4: Permutations - Restrictions"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            # First position fixed
            n = random.randint(5, 7)
            result = factorial(n - 1)
            correct, distractors = str(result), [str(factorial(n)), str(n - 1), str(result * 2)]
            question = f"{n} people in a row, but one specific person must be first. How many arrangements?"
            explanation = f"Fix 1 person first, arrange remaining {n-1}: ({n-1})! = {result}"
        elif qtype == 2:
            # Two people together
            n = random.randint(5, 6)
            # Treat pair as one unit: (n-1)! × 2
            result = factorial(n - 1) * 2
            correct, distractors = str(result), [str(factorial(n)), str(factorial(n - 1)), str(result // 2)]
            question = f"{n} people in a row, 2 specific people must be adjacent. How many arrangements?"
            explanation = f"Treat pair as unit: ({n-1})! × 2! = {factorial(n-1)} × 2 = {result}"
        elif qtype == 3:
            # Two people NOT together
            n = random.randint(5, 6)
            total = factorial(n)
            together = factorial(n - 1) * 2
            result = total - together
            correct, distractors = str(result), [str(total), str(together), str(result + together)]
            question = f"{n} people in a row, 2 specific people must NOT be adjacent. How many arrangements?"
            explanation = f"Total - together = {n}! - ({n-1})!×2 = {total} - {together} = {result}"
        elif qtype == 4:
            # Ends fixed
            n = random.randint(5, 7)
            # 2 ways to arrange ends, (n-2)! for middle
            result = 2 * factorial(n - 2)
            correct, distractors = str(result), [str(factorial(n)), str(factorial(n - 2)), str(result * 2)]
            question = f"{n} people in a row, 2 specific people at the ends. How many arrangements?"
            explanation = f"2 ways for ends, ({n-2})! for middle: 2 × {factorial(n-2)} = {result}"
        else:
            # Vowels together in a word
            # EDUCATION has 5 vowels (E,U,A,I,O) and 4 consonants
            # Treat vowels as one unit: 5! arrangements
            # 5 units total, arranged 5! ways, vowels arrange 5! ways
            # Simpler example: TEAM (2 vowels EA, 2 consonants TM)
            result = factorial(3) * factorial(2)  # 3 units × vowel arrangements
            correct, distractors = str(result), [str(factorial(4)), str(factorial(3)), str(12)]
            question = "Arrange letters of TEAM keeping vowels (E,A) together. How many ways?"
            explanation = f"3 units (T, EA, M) × 2! vowel arrangements = 3! × 2! = 6 × 2 = {result}"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 4, 'difficulty_band': 'developing'})
    return questions

def generate_level_5():
    """Level 5: Combinations - Basics"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            # nCr calculation
            n = random.randint(6, 10)
            r = random.randint(2, 4)
            result = comb(n, r)
            correct, distractors = str(result), [str(perm(n, r)), str(n * r), str(result + n)]
            question = f"Calculate {n}C{r} (combinations of {r} from {n})."
            explanation = f"{n}C{r} = {n}!/({r}!({n}-{r})!) = {result}"
        elif qtype == 2:
            # Choose committee
            n = random.randint(8, 12)
            r = random.randint(3, 5)
            result = comb(n, r)
            correct, distractors = str(result), [str(perm(n, r)), str(n * r), str(factorial(r))]
            question = f"Choose {r} people from {n} for a committee. How many ways?"
            explanation = f"{n}C{r} = {result} ways (order doesn't matter)"
        elif qtype == 3:
            # nCn and nC0
            n = random.randint(5, 10)
            choice = random.choice(['n', '0'])
            correct, distractors = "1", [str(n), str(factorial(n)), "0"]
            if choice == 'n':
                question = f"What is {n}C{n}?"
                explanation = f"{n}C{n} = 1 (only one way to choose all)"
            else:
                question = f"What is {n}C0?"
                explanation = f"{n}C0 = 1 (only one way to choose none)"
        elif qtype == 4:
            # nCr = nC(n-r)
            n = random.randint(8, 12)
            r = random.randint(2, 4)
            result = comb(n, r)
            correct, distractors = str(result), [str(comb(n, r + 1)), str(n - r), str(result + 1)]
            question = f"If {n}C{r} = {result}, what is {n}C{n-r}?"
            explanation = f"{n}C{r} = {n}C{n-r} = {result}"
        else:
            # Select team
            n = random.randint(10, 15)
            r = random.randint(4, 6)
            result = comb(n, r)
            correct, distractors = str(result), [str(perm(n, r)), str(n * r), str(result // 2)]
            question = f"From {n} players, select {r} for a team. How many selections?"
            explanation = f"{n}C{r} = {result} selections"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 5, 'difficulty_band': 'developing'})
    return questions

def generate_level_6():
    """Level 6: Combinations - Selection Problems"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            # At least one of a type
            m = random.randint(4, 6)  # men
            w = random.randint(4, 6)  # women
            k = 3  # committee size
            total = comb(m + w, k)
            all_men = comb(m, k)
            result = total - all_men
            correct, distractors = str(result), [str(total), str(all_men), str(comb(w, k))]
            question = f"From {m} men and {w} women, choose 3 with at least 1 woman. How many ways?"
            explanation = f"Total - all men = {m+w}C3 - {m}C3 = {total} - {all_men} = {result}"
        elif qtype == 2:
            # Exactly k of one type
            m, w = 5, 4
            # Choose 2 men AND 2 women for committee of 4
            result = comb(m, 2) * comb(w, 2)
            correct, distractors = str(result), [str(comb(m + w, 4)), str(comb(m, 2) + comb(w, 2)), str(result + 10)]
            question = f"From {m} men and {w} women, choose 4 with exactly 2 men and 2 women."
            explanation = f"{m}C2 × {w}C2 = {comb(m,2)} × {comb(w,2)} = {result}"
        elif qtype == 3:
            # Must include specific person
            n = random.randint(8, 12)
            r = random.randint(4, 5)
            # If 1 person must be included, choose r-1 from remaining n-1
            result = comb(n - 1, r - 1)
            correct, distractors = str(result), [str(comb(n, r)), str(comb(n - 1, r)), str(result + 1)]
            question = f"Choose {r} from {n} people, must include the captain. How many ways?"
            explanation = f"Fix captain, choose {r-1} from {n-1}: {n-1}C{r-1} = {result}"
        elif qtype == 4:
            # Must exclude specific person
            n = random.randint(8, 12)
            r = random.randint(4, 5)
            result = comb(n - 1, r)
            correct, distractors = str(result), [str(comb(n, r)), str(comb(n - 1, r - 1)), str(result - 1)]
            question = f"Choose {r} from {n} people, must NOT include Tom. How many ways?"
            explanation = f"Exclude Tom, choose {r} from {n-1}: {n-1}C{r} = {result}"
        else:
            # Cards: choose from suits
            # Choose 3 cards from hearts (13 cards)
            r = random.randint(3, 5)
            result = comb(13, r)
            correct, distractors = str(result), [str(13 * r), str(comb(52, r)), str(result + 13)]
            question = f"From a standard deck, choose {r} hearts. How many ways?"
            explanation = f"13C{r} = {result} ways"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 6, 'difficulty_band': 'developing'})
    return questions

def generate_level_7():
    """Level 7: Permutations vs Combinations"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            # Identify: order matters?
            scenarios = [
                ("Choosing a 4-digit PIN", "Permutation", ["Combination", "Neither", "Both"]),
                ("Selecting 3 books from a shelf to read (not order)", "Combination", ["Permutation", "Neither", "Both"]),
                ("Arranging 5 people in a queue", "Permutation", ["Combination", "Neither", "Both"]),
                ("Choosing 4 cards from a deck", "Combination", ["Permutation", "Neither", "Both"]),
                ("Ranking top 3 in a race", "Permutation", ["Combination", "Neither", "Both"]),
            ]
            scenario, correct, distractors = random.choice(scenarios)
            question = f"Is this a permutation or combination? '{scenario}'"
            explanation = f"{'Order matters' if correct == 'Permutation' else 'Order does not matter'}: {correct}"
        elif qtype == 2:
            # Compare nPr and nCr
            n = random.randint(6, 9)
            r = random.randint(3, 4)
            p = perm(n, r)
            c = comb(n, r)
            ratio = factorial(r)
            correct, distractors = str(ratio), [str(r), str(n), str(ratio + 1)]
            question = f"If {n}P{r} = {p} and {n}C{r} = {c}, what is {n}P{r} ÷ {n}C{r}?"
            explanation = f"{n}P{r}/{n}C{r} = {r}! = {ratio}"
        elif qtype == 3:
            # Password vs team selection
            n = random.randint(8, 10)
            r = 4
            p = perm(n, r)
            c = comb(n, r)
            correct, distractors = f"{p} and {c}", [f"{c} and {p}", f"{p} and {p}", f"{c} and {c}"]
            question = f"From {n} letters: (a) {r}-letter passwords (b) {r}-letter subsets. How many each?"
            explanation = f"Passwords (order matters): {n}P{r} = {p}. Subsets: {n}C{r} = {c}"
        elif qtype == 4:
            # Given one, find other
            n = random.randint(7, 10)
            r = 3
            c = comb(n, r)
            p = perm(n, r)
            correct, distractors = str(p), [str(c * 2), str(c + 6), str(p // 2)]
            question = f"If {n}C{r} = {c}, find {n}P{r}."
            explanation = f"{n}P{r} = {n}C{r} × {r}! = {c} × {factorial(r)} = {p}"
        else:
            # Real-world comparison
            n = random.randint(5, 7)
            p = factorial(n)
            c = comb(n, n)
            correct, distractors = str(p), [str(c), str(n), str(p // 2)]
            question = f"{n} runners: how many ways to arrange them at the finish line?"
            explanation = f"Order matters (permutation): {n}! = {p}"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 7, 'difficulty_band': 'proficient'})
    return questions

def generate_level_8():
    """Level 8: Arrangements with Repetition"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            # Word with repeated letters
            # MISSISSIPPI: 11!/(4!4!2!) = 34650
            # Simpler: PEPPER = 6!/(3!2!) = 60
            words = [
                ("PEPPER", 6, [3, 2, 1], 60),  # P×3, E×2, R×1
                ("BOOK", 4, [2, 1, 1], 12),    # O×2, B×1, K×1
                ("MOON", 4, [2, 1, 1], 12),    # O×2, M×1, N×1
                ("SEES", 4, [2, 2], 6),        # S×2, E×2
            ]
            word, n, reps, result = random.choice(words)
            correct, distractors = str(result), [str(factorial(n)), str(result * 2), str(result + n)]
            question = f"How many distinct arrangements of the letters in '{word}'?"
            explanation = f"{n}! ÷ (repeated letters factorials) = {result}"
        elif qtype == 2:
            # Digits with repetition allowed
            n = random.randint(3, 4)  # number of positions
            result = 10 ** n
            correct, distractors = str(result), [str(perm(10, n)), str(10 * n), str(result // 10)]
            question = f"How many {n}-digit numbers (including those starting with 0) if digits can repeat?"
            explanation = f"10 choices for each of {n} positions: 10^{n} = {result}"
        elif qtype == 3:
            # Binary strings
            n = random.randint(4, 6)
            result = 2 ** n
            correct, distractors = str(result), [str(2 * n), str(factorial(n)), str(result - 1)]
            question = f"How many binary strings of length {n}?"
            explanation = f"2 choices (0 or 1) for each position: 2^{n} = {result}"
        elif qtype == 4:
            # AABB type arrangement
            # n items with repetitions: n!/(a!b!...)
            result = factorial(4) // (factorial(2) * factorial(2))  # 24/4 = 6
            correct, distractors = str(result), [str(factorial(4)), str(4), str(result + 2)]
            question = "Arrange 2 identical red balls and 2 identical blue balls in a row. How many ways?"
            explanation = f"4!/(2!×2!) = 24/4 = {result}"
        else:
            # Letters with some identical
            # TOOTH: 5!/(2!2!) = 30 (O×2, T×2)
            result = factorial(5) // (factorial(2) * factorial(2))
            correct, distractors = str(result), [str(factorial(5)), str(result // 2), str(result + 5)]
            question = "How many distinct arrangements of 'TOOTH'?"
            explanation = f"5!/(2!×2!) = 120/4 = {result}"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 8, 'difficulty_band': 'proficient'})
    return questions

def generate_level_9():
    """Level 9: Circular Arrangements"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            # Basic circular arrangement
            n = random.randint(4, 7)
            result = factorial(n - 1)
            correct, distractors = str(result), [str(factorial(n)), str(n), str(result * n)]
            question = f"{n} people sit around a circular table. How many distinct arrangements?"
            explanation = f"Circular arrangements: (n-1)! = ({n}-1)! = {result}"
        elif qtype == 2:
            # Necklace/bracelet (can be flipped)
            n = random.randint(4, 6)
            circular = factorial(n - 1)
            result = circular // 2
            correct, distractors = str(result), [str(circular), str(factorial(n)), str(result * 2)]
            question = f"{n} different beads on a bracelet (can be flipped). How many distinct arrangements?"
            explanation = f"Bracelet = circular ÷ 2 = (n-1)!/2 = {circular}/2 = {result}"
        elif qtype == 3:
            # Two people must sit together (circular)
            n = random.randint(5, 7)
            # Treat pair as one: (n-2)! arrangements × 2 for pair order
            result = factorial(n - 2) * 2
            correct, distractors = str(result), [str(factorial(n - 1)), str(factorial(n - 2)), str(result // 2)]
            question = f"{n} people around a table, 2 must sit together. How many arrangements?"
            explanation = f"Treat pair as unit: ({n}-2)! × 2! = {factorial(n-2)} × 2 = {result}"
        elif qtype == 4:
            # Two people must NOT sit together (circular)
            n = random.randint(5, 6)
            total = factorial(n - 1)
            together = factorial(n - 2) * 2
            result = total - together
            correct, distractors = str(result), [str(total), str(together), str(result + together)]
            question = f"{n} people around a table, 2 must NOT sit together. How many arrangements?"
            explanation = f"Total - together = ({n}-1)! - ({n}-2)!×2 = {total} - {together} = {result}"
        else:
            # Keys on a ring
            n = random.randint(4, 6)
            result = factorial(n - 1) // 2
            correct, distractors = str(result), [str(factorial(n - 1)), str(factorial(n)), str(result * 2)]
            question = f"{n} keys on a keyring (can be flipped). How many distinct arrangements?"
            explanation = f"Keyring = (n-1)!/2 = {factorial(n-1)}/2 = {result}"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 9, 'difficulty_band': 'proficient'})
    return questions

def generate_level_10():
    """Level 10: Partitions & Distributions"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 5)
        if qtype == 1:
            # Distribute identical items into distinct groups
            # Stars and bars: (n+k-1)C(k-1) ways to put n identical items into k distinct boxes
            n = random.randint(4, 6)  # items
            k = random.randint(2, 3)  # boxes
            result = comb(n + k - 1, k - 1)
            correct, distractors = str(result), [str(n * k), str(comb(n, k)), str(result + k)]
            question = f"Distribute {n} identical balls into {k} distinct boxes. How many ways?"
            explanation = f"Stars and bars: ({n}+{k}-1)C({k}-1) = {n+k-1}C{k-1} = {result}"
        elif qtype == 2:
            # Partition into groups of specified sizes
            # 6 people into groups of 3,2,1: 6!/(3!2!1!) = 60
            result = factorial(6) // (factorial(3) * factorial(2) * factorial(1))
            correct, distractors = str(result), [str(factorial(6)), str(comb(6, 3)), str(result + 10)]
            question = "Divide 6 people into groups of 3, 2, and 1. How many ways?"
            explanation = f"6!/(3!×2!×1!) = 720/12 = {result}"
        elif qtype == 3:
            # Into equal groups (unlabeled)
            # 4 people into 2 groups of 2: 4C2 ÷ 2! = 3
            result = comb(4, 2) // factorial(2)
            correct, distractors = str(result), [str(comb(4, 2)), str(factorial(4)), str(result * 2)]
            question = "Divide 4 people into 2 unlabeled groups of 2. How many ways?"
            explanation = f"4C2 ÷ 2! = 6 ÷ 2 = {result}"
        elif qtype == 4:
            # Distribute distinct items to distinct people
            n = random.randint(3, 4)  # items
            k = random.randint(2, 3)  # people
            result = k ** n
            correct, distractors = str(result), [str(n * k), str(perm(k, n) if n <= k else 0), str(result + k)]
            question = f"Distribute {n} distinct gifts to {k} people (each person can get any number). How many ways?"
            explanation = f"{k} choices for each gift: {k}^{n} = {result}"
        else:
            # Multiset permutation
            # Arrange AABBC: 5!/(2!2!1!) = 30
            result = factorial(5) // (factorial(2) * factorial(2) * factorial(1))
            correct, distractors = str(result), [str(factorial(5)), str(result // 2), str(result + 5)]
            question = "How many ways to arrange 2 A's, 2 B's, and 1 C?"
            explanation = f"5!/(2!×2!×1!) = 120/4 = {result}"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 10, 'difficulty_band': 'advanced'})
    return questions

def generate_level_11():
    """Level 11: Pascal's Triangle & Binomial"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 6)
        if qtype == 1:
            # Pascal's triangle value
            n = random.randint(4, 7)
            r = random.randint(1, n - 1)
            result = comb(n, r)
            correct, distractors = str(result), [str(comb(n, r - 1)), str(comb(n - 1, r)), str(result + 1)]
            question = f"In Pascal's triangle, what is the entry in row {n}, position {r}? (Row 0 = top, position 0 = left)"
            explanation = f"Entry = {n}C{r} = {result}"
        elif qtype == 2:
            # Sum of row
            n = random.randint(4, 7)
            result = 2 ** n
            correct, distractors = str(result), [str(n * 2), str(factorial(n)), str(result - 1)]
            question = f"What is the sum of all entries in row {n} of Pascal's triangle?"
            explanation = f"Sum of row n = 2^n = 2^{n} = {result}"
        elif qtype == 3:
            # Binomial coefficient in expansion
            n = random.randint(4, 6)
            r = random.randint(1, n - 1)
            coeff = comb(n, r)
            correct, distractors = str(coeff), [str(comb(n, r + 1)), str(n * r), str(coeff + n)]
            question = f"In (a + b)^{n}, what is the coefficient of a^{n-r}b^{r}?"
            explanation = f"Coefficient = {n}C{r} = {coeff}"
        elif qtype == 4:
            # Pascal's identity
            n = random.randint(5, 8)
            r = random.randint(2, n - 2)
            left = comb(n - 1, r - 1)
            right = comb(n - 1, r)
            result = left + right
            correct, distractors = str(result), [str(left), str(right), str(result - 1)]
            question = f"Using Pascal's identity, find {n-1}C{r-1} + {n-1}C{r}."
            explanation = f"{n-1}C{r-1} + {n-1}C{r} = {n}C{r} = {result}"
        elif qtype == 5:
            # Specific term in binomial expansion
            # (x + 2)^4, find coefficient of x²
            # Term with x² is C(4,2) × x² × 2² = 6 × 4 = 24
            n = 4
            r = 2
            coeff = comb(n, r) * (2 ** r)
            correct, distractors = str(coeff), [str(comb(n, r)), str(2 ** n), str(coeff + 6)]
            question = f"In (x + 2)^4, find the coefficient of x²."
            explanation = f"4C2 × 2² = 6 × 4 = {coeff}"
        else:
            # Number of terms
            n = random.randint(5, 10)
            result = n + 1
            correct, distractors = str(result), [str(n), str(2 * n), str(n - 1)]
            question = f"How many terms are in the expansion of (a + b)^{n}?"
            explanation = f"(a + b)^n has n + 1 terms: {n} + 1 = {result}"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 11, 'difficulty_band': 'advanced'})
    return questions

def generate_level_12():
    """Level 12: Mastery Challenge"""
    questions = []
    for _ in range(50):
        qtype = random.randint(1, 6)
        if qtype == 1:
            # Complex committee selection
            m, w = 6, 5
            # 5-person committee with at least 2 women
            # = Total - (0 women) - (1 woman)
            total = comb(11, 5)
            zero_w = comb(6, 5)
            one_w = comb(5, 1) * comb(6, 4)
            result = total - zero_w - one_w
            correct, distractors = str(result), [str(total), str(one_w), str(result + 50)]
            question = f"From {m} men and {w} women, form 5-person committee with at least 2 women. How many ways?"
            explanation = f"Total - (0 women) - (1 woman) = {total} - {zero_w} - {one_w} = {result}"
        elif qtype == 2:
            # Derangements concept
            # For n=4: D(4) = 9
            correct, distractors = "9", ["24", "6", "15"]
            question = "4 letters in 4 envelopes, none in correct envelope. How many ways? (Derangement)"
            explanation = f"D(4) = 4!(1 - 1/1! + 1/2! - 1/3! + 1/4!) = 9"
        elif qtype == 3:
            # Paths in grid
            # From (0,0) to (3,2): need 3 right + 2 up moves = 5!/(3!2!) = 10
            r, u = random.randint(2, 4), random.randint(2, 3)
            result = comb(r + u, r)
            correct, distractors = str(result), [str(r * u), str(r + u), str(result + 5)]
            question = f"Paths from (0,0) to ({r},{u}) moving only right or up. How many?"
            explanation = f"Need {r} rights and {u} ups: ({r}+{u})!/({r}!{u}!) = {result}"
        elif qtype == 4:
            # Circular with restrictions
            n = 6
            # 6 people, 2 specific people not adjacent
            total = factorial(n - 1)  # 120
            together = factorial(n - 2) * 2  # 48
            result = total - together
            correct, distractors = str(result), [str(total), str(together), str(result + 24)]
            question = f"{n} people around a table, A and B must NOT sit together. How many arrangements?"
            explanation = f"Total - together = (n-1)! - (n-2)!×2 = {total} - {together} = {result}"
        elif qtype == 5:
            # Multinomial coefficient
            # MISSISSIPPI: 11!/(4!4!2!1!) = 34650
            # Simpler: BANANA = 6!/(3!2!1!) = 60
            result = factorial(6) // (factorial(3) * factorial(2) * factorial(1))
            correct, distractors = str(result), [str(factorial(6)), str(result // 2), str(result + 6)]
            question = "How many distinct arrangements of 'BANANA'?"
            explanation = f"6!/(3!×2!×1!) = 720/12 = {result}"
        else:
            # Combined probability and counting
            # Choose 3 cards from deck, all same suit
            # 4 suits × 13C3 = 4 × 286 = 1144
            result = 4 * comb(13, 3)
            correct, distractors = str(result), [str(comb(52, 3)), str(comb(13, 3)), str(result + 100)]
            question = "Choose 3 cards from a deck, all from the same suit. How many ways?"
            explanation = f"4 suits × 13C3 = 4 × {comb(13,3)} = {result}"
        options, correct_idx = make_unique_options(correct, distractors)
        questions.append({'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': correct_idx,
            'explanation': explanation, 'difficulty': 12, 'difficulty_band': 'advanced'})
    return questions

def main():
    all_questions = []
    generators = [generate_level_1, generate_level_2, generate_level_3, generate_level_4,
        generate_level_5, generate_level_6, generate_level_7, generate_level_8,
        generate_level_9, generate_level_10, generate_level_11, generate_level_12]
    
    print(f"Generating questions for {TOPIC}...")
    print("=" * 50)
    for level, generator in enumerate(generators, 1):
        questions = generator()
        all_questions.extend(questions)
        print(f"Level {level} ({LEVEL_TITLES[level-1]}): {len(questions)} questions")
    print("=" * 50)
    print(f"Total questions generated: {len(all_questions)}")
    
    sql_statements = []
    for q in all_questions:
        q_text = q['question_text'].replace("'", "''")
        opt_a, opt_b = q['option_a'].replace("'", "''"), q['option_b'].replace("'", "''")
        opt_c, opt_d = q['option_c'].replace("'", "''"), q['option_d'].replace("'", "''")
        expl = q['explanation'].replace("'", "''")
        sql = f"""INSERT OR IGNORE INTO questions_adaptive 
(question_text, option_a, option_b, option_c, option_d, correct_answer, 
topic, difficulty_level, difficulty_band, mode, explanation, is_active)
VALUES ('{q_text}', '{opt_a}', '{opt_b}', '{opt_c}', '{opt_d}', {q['correct_idx']},
'{TOPIC}', {q['difficulty']}, '{q['difficulty_band']}', '{MODE}', '{expl}', 1);"""
        sql_statements.append(sql)
    
    sql_file = f'/home/claude/{TOPIC}_questions.sql'
    with open(sql_file, 'w') as f:
        f.write(f"-- LC Higher Level - Counting & Combinatorics Questions\n-- Generated: 2025-12-15\n-- Total: {len(all_questions)} questions\n\n")
        f.write('\n'.join(sql_statements))
    print(f"\nSQL file written to: {sql_file}")
    return all_questions

if __name__ == '__main__':
    main()
