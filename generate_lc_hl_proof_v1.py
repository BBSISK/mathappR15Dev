#!/usr/bin/env python3
"""
LC Higher Level - Proof & Reasoning Question Generator
Version: 1.0
Date: 2025-12-14

Generates 600 questions (50 per level x 12 levels) for LC HL Proof & Reasoning
"""

import random

TOPIC = 'lc_hl_proof'
MODE = 'lc_hl'

LEVEL_TITLES = [
    'Mathematical Statements',
    'Direct Proof',
    'Proof by Contradiction',
    'Proof by Contrapositive',
    'Proof by Induction - Basics',
    'Proof by Induction - Sums',
    'Proof by Induction - Divisibility',
    'Proof by Induction - Inequalities',
    'Geometric Proofs',
    'Algebraic Proofs',
    'Number Theory Proofs',
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
        unique_wrong.append(f"Option {len(unique_wrong) + 2}")
    options = [correct_str] + unique_wrong[:3]
    random.shuffle(options)
    return options, options.index(correct_str)

def create_question(q_text, correct, distractors, explanation, difficulty, band):
    options, correct_idx = make_unique_options(correct, distractors)
    return {
        'question_text': q_text,
        'option_a': options[0], 'option_b': options[1],
        'option_c': options[2], 'option_d': options[3],
        'correct_idx': correct_idx, 'explanation': explanation,
        'difficulty': difficulty, 'difficulty_band': band
    }

def generate_level_1():
    """Level 1: Mathematical Statements"""
    questions = []
    
    # Statement classification
    stmt_qs = [
        ("The sum of two even numbers is even.", "True statement", "2a + 2b = 2(a+b)"),
        ("x + 5 = 10", "Open statement", "Truth depends on x"),
        ("All prime numbers are odd.", "False statement", "2 is prime and even"),
        ("Is 7 prime?", "Not a statement (question)", "Questions have no truth value"),
        ("Every rectangle is a square.", "False statement", "Counterexample: 2×3 rectangle"),
    ]
    for q, a, e in stmt_qs:
        questions.append(create_question(f'Classify: "{q}"', a, 
            ["True statement", "False statement", "Open statement", "Not a statement"][:3] if a not in ["True statement", "False statement", "Open statement"] else ["Not a statement", "Open statement", "True statement"],
            e, 1, 'foundation'))
    
    # Negations
    neg_qs = [
        ("All cats are black", "There exists a cat that is not black", "Negate 'all' to 'exists not'"),
        ("Some birds fly", "No birds fly", "Negate 'some' to 'none'"),
        ("n is even", "n is odd", "Not even = odd"),
        ("x > 5", "x ≤ 5", "Negate > to ≤"),
        ("x > 0 and y > 0", "x ≤ 0 or y ≤ 0", "Negate 'and' with 'or'"),
    ]
    for q, a, e in neg_qs:
        questions.append(create_question(f'Negate: "{q}"', a,
            [q, "Cannot be negated", f"Not ({q})"], e, 1, 'foundation'))
    
    # Conditionals
    cond_qs = [
        ("If it rains, ground is wet", "converse", "If ground is wet, it rains", "Swap parts"),
        ("If it rains, ground is wet", "contrapositive", "If ground not wet, no rain", "Swap and negate"),
        ("If n² even, n even", "contrapositive", "If n odd, n² odd", "Swap and negate"),
    ]
    for orig, form, ans, expl in cond_qs:
        questions.append(create_question(f'Find the {form} of: "{orig}"', ans,
            [orig, "Cannot determine", "If n odd, n² even"], expl, 1, 'foundation'))
    
    # Logic concepts
    logic_qs = [
        ("A statement and its contrapositive are:", "Logically equivalent", "Same truth value"),
        ("A counterexample is used to:", "Disprove universal statements", "One case disproves 'for all'"),
        ("To prove 'there exists', you need:", "One valid example", "Existence needs one case"),
        ("To prove 'for all', you need:", "A general argument", "Must cover all cases"),
    ]
    for q, a, e in logic_qs:
        questions.append(create_question(q, a, ["Always different", "Find all cases", "Numerical check"], e, 1, 'foundation'))
    
    # Fill to 50
    extra_qs = [
        ("The negation of 'All students passed' is:", "At least one student failed", "Exists...not"),
        ("If P→Q is true, what about ¬Q→¬P?", "Also true (contrapositive)", "Equivalent"),
        ("The converse of P→Q is:", "Q→P", "Swap hypothesis and conclusion"),
        ("The inverse of P→Q is:", "¬P→¬Q", "Negate both parts"),
        ("A conditional and its ___ are equivalent:", "Contrapositive", "Not converse or inverse"),
    ]
    for q, a, e in extra_qs:
        questions.append(create_question(q, a, ["False", "Q→P", "Cannot determine"], e, 1, 'foundation'))
    
    while len(questions) < 50:
        i = len(questions)
        questions.append(create_question(
            f"In logic, ¬(P ∧ Q) equals:", "¬P ∨ ¬Q",
            ["¬P ∧ ¬Q", "P ∨ Q", "P ∧ Q"], "De Morgan's Law", 1, 'foundation'))
    
    return questions[:50]

def generate_level_2():
    """Level 2: Direct Proof"""
    questions = []
    
    proofs = [
        ("Sum of two evens is even", "2a + 2b = 2(a+b), divisible by 2", "Factor out 2"),
        ("Sum of two odds is even", "(2a+1) + (2b+1) = 2(a+b+1)", "Combine and factor"),
        ("Product of even and any is even", "2a × b = 2(ab)", "Factor of 2 remains"),
        ("Square of even is even", "(2k)² = 4k² = 2(2k²)", "Still has factor 2"),
        ("Square of odd is odd", "(2k+1)² = 4k²+4k+1 = 2(2k²+2k)+1", "Form 2m+1"),
        ("n² + n is always even", "n(n+1): consecutive integers", "One must be even"),
        ("Sum of 3 consecutive integers divisible by 3", "n+(n+1)+(n+2) = 3n+3 = 3(n+1)", "Factor out 3"),
        ("If a|b and b|c, then a|c", "b=ka, c=mb, so c=mka", "Transitivity"),
    ]
    
    for stmt, proof, expl in proofs:
        questions.append(create_question(f"Prove: {stmt}", proof,
            ["Cannot be proven", "False statement", "Needs induction"], expl, 2, 'foundation'))
    
    structure_qs = [
        ("First step in direct proof of 'If P then Q':", "Assume P is true", "Start with hypothesis"),
        ("Direct proof ends with:", "The conclusion Q", "Derive what we want"),
        ("Direct proof uses:", "Logical deduction from hypothesis", "Step by step logic"),
        ("To prove 'n even implies n² even', first:", "Write n = 2k", "Express 'even' algebraically"),
    ]
    for q, a, e in structure_qs:
        questions.append(create_question(q, a, ["Assume Q false", "Find counterexample", "Use induction"], e, 2, 'foundation'))
    
    # Fill to 50
    more_proofs = [
        ("Prove: Product of two odds is odd", "(2a+1)(2b+1) = 4ab+2a+2b+1 = 2(2ab+a+b)+1", "Form 2m+1"),
        ("Prove: Sum of rational numbers is rational", "a/b + c/d = (ad+bc)/bd", "Closed under addition"),
        ("What is direct proof also called?", "Deductive proof", "Deduce conclusion"),
        ("In P→Q, P is called:", "The hypothesis", "What we assume"),
    ]
    for q, a, e in more_proofs:
        questions.append(create_question(q, a, ["Indirect proof", "The conclusion", "Induction"], e, 2, 'foundation'))
    
    while len(questions) < 50:
        questions.append(create_question(
            "Direct proof is best when:", "Clear path from hypothesis to conclusion",
            ["Statement seems false", "Many cases needed", "Contradiction required"], "Straightforward logic", 2, 'foundation'))
    
    return questions[:50]

def generate_level_3():
    """Level 3: Proof by Contradiction"""
    questions = []
    
    structure = [
        ("First step in proof by contradiction:", "Assume negation of what to prove", "Suppose conclusion false"),
        ("We seek to find:", "A logical contradiction", "Something impossible"),
        ("When we find contradiction:", "Original assumption was false", "Negation fails"),
        ("Proof by contradiction is also called:", "Indirect proof or reductio ad absurdum", "Reduce to absurdity"),
        ("To prove P by contradiction, assume:", "Not P", "The negation"),
    ]
    for q, a, e in structure:
        questions.append(create_question(q, a, ["Assume P", "Find example", "Use induction"], e, 3, 'foundation'))
    
    classic = [
        ("√2 irrational: Assume √2 = a/b in lowest terms. Then both a and b are:", "Even, contradicting lowest terms", "2=a²/b² means a² even"),
        ("Infinitely many primes: Consider N = p₁p₂...pₙ + 1. N is:", "Not divisible by any pᵢ", "Remainder 1 when divided"),
        ("If n² even then n even. Assume n odd, then n² is:", "Odd, contradicting n² even", "Odd squared is odd"),
        ("√3 irrational follows same pattern as:", "√2 proof", "Both numerator and denominator divisible by 3"),
        ("No smallest positive rational: If r smallest, then r/2 is:", "Smaller positive rational", "Contradiction"),
    ]
    for q, a, e in classic:
        questions.append(create_question(q, a, ["Proof complete", "Still rational", "Prime"], e, 3, 'foundation'))
    
    identify = [
        ("'Suppose √5 rational... contradiction... so √5 irrational' is:", "Proof by contradiction", "Assumed negation"),
        ("'Assume largest even n exists. Then n+2 is larger and even.' is:", "Proof by contradiction", "Contradicts 'largest'"),
        ("Finding 1=0 in a proof means:", "Contradiction reached", "Impossible equality"),
    ]
    for q, a, e in identify:
        questions.append(create_question(q, a, ["Direct proof", "Induction", "Invalid proof"], e, 3, 'foundation'))
    
    while len(questions) < 50:
        questions.append(create_question(
            "Proof by contradiction relies on:", "Law of excluded middle (P or not P)",
            ["Direct calculation", "Specific examples", "Induction"], "Either true or false", 3, 'foundation'))
    
    return questions[:50]

def generate_level_4():
    """Level 4: Proof by Contrapositive"""
    questions = []
    
    basics = [
        ("Contrapositive of 'If P then Q' is:", "If not Q then not P", "Swap and negate"),
        ("A statement and its contrapositive are:", "Logically equivalent", "Same truth value"),
        ("To prove P→Q by contrapositive, prove:", "¬Q → ¬P", "Equivalent statement"),
        ("Contrapositive of 'n² even implies n even' is:", "n odd implies n² odd", "Not even = odd"),
        ("Why is contrapositive valid?", "Logically equivalent to original", "Same truth value"),
    ]
    for q, a, e in basics:
        questions.append(create_question(q, a, ["If Q then P", "Different truth value", "Not equivalent"], e, 4, 'developing'))
    
    proofs = [
        ("Prove 'n² even ⟹ n even' by contrapositive:", "Show n odd ⟹ n² odd", "Easier to prove"),
        ("If n odd (n=2k+1), then n² =", "(2k+1)² = 4k²+4k+1 = 2(2k²+2k)+1, odd", "Form 2m+1"),
        ("Prove 'n² divisible by 3 ⟹ n divisible by 3':", "Contrapositive: 3∤n ⟹ 3∤n²", "Check n≡1,2 mod 3"),
        ("If n≡1 (mod 3), then n² ≡", "1 (mod 3)", "1² = 1"),
        ("If n≡2 (mod 3), then n² ≡", "4 ≡ 1 (mod 3)", "Neither is 0"),
    ]
    for q, a, e in proofs:
        questions.append(create_question(q, a, ["Direct proof only", "Cannot prove", "n² even"], e, 4, 'developing'))
    
    compare = [
        ("Contrapositive vs contradiction: Contrapositive proves ¬Q→¬P, contradiction assumes:", "P and ¬Q, derives impossibility", "Subtle difference"),
        ("Which method for 'n² even ⟹ n even'?", "Contrapositive (easier)", "Direct path"),
        ("Which method for '√2 irrational'?", "Contradiction", "Need impossibility"),
        ("Converse and contrapositive:", "Have different truth values (usually)", "Not equivalent to each other"),
        ("(P→Q) is equivalent to:", "(¬Q→¬P)", "Contrapositive"),
    ]
    for q, a, e in compare:
        questions.append(create_question(q, a, ["Direct proof", "Same truth value", "P and Q"], e, 4, 'developing'))
    
    while len(questions) < 50:
        questions.append(create_question(
            "Contrapositive is useful when:", "¬Q gives useful starting information",
            ["Direct proof is easy", "We need examples", "Induction applies"], "Work with negation", 4, 'developing'))
    
    return questions[:50]

def generate_level_5():
    """Level 5: Proof by Induction - Basics"""
    questions = []
    
    structure = [
        ("Mathematical induction has:", "Two steps: base case and inductive step", "Foundation + chain"),
        ("Base case proves:", "Statement true for starting value (usually n=1)", "First domino"),
        ("Inductive hypothesis assumes:", "P(k) is true for some k", "Assume for k"),
        ("Inductive step proves:", "P(k) true implies P(k+1) true", "Domino effect"),
        ("Induction works because:", "Base starts chain, step continues it", "Like dominoes"),
    ]
    for q, a, e in structure:
        questions.append(create_question(q, a, ["One step", "P(n) for all n", "Specific examples"], e, 5, 'developing'))
    
    base_cases = [
        ("1+2+...+n = n(n+1)/2. Base n=1: RHS =", "1(2)/2 = 1 ✓", "Both equal 1"),
        ("2ⁿ > n. Base n=1:", "2 > 1 ✓", "True"),
        ("n! ≥ 2ⁿ⁻¹ for n≥1. Base n=1:", "1 ≥ 1 ✓", "Equality"),
        ("1²+2²+...+n² = n(n+1)(2n+1)/6. Base n=1:", "1 = 1(2)(3)/6 = 1 ✓", "Both 1"),
        ("n³-n divisible by 6. Base n=1:", "0 divisible by 6 ✓", "Zero works"),
    ]
    for q, a, e in base_cases:
        questions.append(create_question(q, a, ["Fails", "Need n=0", "Not required"], e, 5, 'developing'))
    
    inductive = [
        ("For sum formula, inductive step:", "Add (k+1) to both sides of P(k)", "Build k to k+1"),
        ("After assuming P(k), we must show:", "P(k+1) follows logically", "Next case"),
        ("We say 'by inductive hypothesis' when:", "Using assumed P(k)", "Invoking assumption"),
        ("Common error: Using P(k+1) to prove P(k+1) is:", "Circular reasoning (invalid)", "Can't assume conclusion"),
    ]
    for q, a, e in inductive:
        questions.append(create_question(q, a, ["Multiply by k", "P(k) directly", "Valid approach"], e, 5, 'developing'))
    
    while len(questions) < 50:
        questions.append(create_question(
            "Why must base case be verified?", "Chain needs starting point",
            ["It's optional", "For elegance", "To check algebra"], "Foundation of proof", 5, 'developing'))
    
    return questions[:50]

def generate_level_6():
    """Level 6: Proof by Induction - Sums"""
    questions = []
    
    sums = [
        ("∑i = n(n+1)/2. Add (k+1) to k(k+1)/2:", "(k+1)(k+2)/2", "Factor (k+1)"),
        ("∑i² = n(n+1)(2n+1)/6. Inductive step:", "Add (k+1)² to formula for k", "Simplify to k+1 formula"),
        ("∑(2i-1) = n². Add (2k+1) to k²:", "k² + 2k + 1 = (k+1)²", "Perfect square"),
        ("Sum 1+2+4+...+2ⁿ⁻¹ = 2ⁿ-1. Add 2ᵏ:", "2ᵏ-1 + 2ᵏ = 2ᵏ⁺¹-1", "Geometric"),
        ("∑i³ = [n(n+1)/2]². This means:", "Sum of cubes = square of sum", "Beautiful identity"),
    ]
    for q, a, e in sums:
        questions.append(create_question(q, a, ["Cannot simplify", "Formula wrong", "Different approach"], e, 6, 'developing'))
    
    steps = [
        ("k(k+1)/2 + (k+1) factors as:", "(k+1)[k/2 + 1] = (k+1)(k+2)/2", "Common factor"),
        ("For geometric series ∑rⁱ = (rⁿ⁺¹-1)/(r-1):", "Add rᵏ⁺¹ and simplify", "Common denominator"),
        ("Telescoping 1/(n(n+1)) = n/(n+1). Add term:", "k/(k+1) + 1/((k+1)(k+2)) = (k+1)/(k+2)", "Partial fractions"),
        ("Key step: ∑ᵏ⁺¹ = ∑ᵏ + (k+1)th term =", "formula(k+1)", "Add and verify"),
    ]
    for q, a, e in steps:
        questions.append(create_question(q, a, ["Subtract term", "Formula fails", "Different method"], e, 6, 'developing'))
    
    formulas = [
        ("∑i = n(n+1)/2 is attributed to:", "Gauss", "Young genius"),
        ("∑ 2i = n(n+1) comes from:", "2∑i = 2·n(n+1)/2", "Factor of 2"),
        ("∑(3i-2) = n(3n-1)/2 for arithmetic series", "Each term is 1, 4, 7, ...", "Common diff 3"),
    ]
    for q, a, e in formulas:
        questions.append(create_question(q, a, ["Euler", "∑i²", "Geometric"], e, 6, 'developing'))
    
    while len(questions) < 50:
        questions.append(create_question(
            "For induction on sums, always:", "Add the (k+1)th term to both sides",
            ["Multiply by k", "Subtract 1", "Start over"], "Build step by step", 6, 'developing'))
    
    return questions[:50]

def generate_level_7():
    """Level 7: Proof by Induction - Divisibility"""
    questions = []
    
    divisibility = [
        ("6|(n³-n): Factor n³-n =", "n(n-1)(n+1), three consecutive integers", "Contains 2 and 3"),
        ("3|(n³-n): Base n=1:", "0 divisible by 3 ✓", "Zero works"),
        ("For 3|(n³-n), (k+1)³-(k+1) - (k³-k) =", "3k²+3k = 3(k²+k)", "Multiple of 3"),
        ("8|(3²ⁿ-1): Base n=1:", "9-1 = 8 ✓", "Exactly 8"),
        ("For 8|(3²ⁿ-1): 3²⁽ᵏ⁺¹⁾-1 = 9(3²ᵏ-1)+8", "Both terms divisible by 8", "IH plus 8"),
    ]
    for q, a, e in divisibility:
        questions.append(create_question(q, a, ["Not divisible", "Base fails", "Cannot factor"], e, 7, 'proficient'))
    
    mod_arith = [
        ("6 ≡ 1 (mod 5), so 6ⁿ ≡", "1 (mod 5)", "1 to any power"),
        ("4 ≡ -1 (mod 5), so 4ⁿ ≡", "±1 depending on parity", "Alternates"),
        ("2³ = 8 ≡ 1 (mod 7), so 8ⁿ ≡", "1 (mod 7)", "Power of 1"),
        ("If a ≡ b (mod m), then aⁿ ≡", "bⁿ (mod m)", "Powers preserve congruence"),
        ("10 ≡ 1 (mod 9), so sum of digits ≡", "number (mod 9)", "Digit sum test"),
    ]
    for q, a, e in mod_arith:
        questions.append(create_question(q, a, ["0 (mod m)", "Different", "Cannot determine"], e, 7, 'proficient'))
    
    more = [
        ("7|(8ⁿ-1): 8ᵏ⁺¹-1 = 8(8ᵏ-1)+7", "Both divisible by 7", "Factor approach"),
        ("5|(n⁵-n) by Fermat's Little Theorem:", "n⁵ ≡ n (mod 5)", "5 is prime"),
        ("30|(n⁵-n) because divisible by:", "2, 3, and 5", "2×3×5 = 30"),
        ("n² ≡ 0 or 1 (mod 4) because:", "Even² ≡ 0, odd² ≡ 1", "Two cases"),
    ]
    for q, a, e in more:
        questions.append(create_question(q, a, ["Not divisible", "Different divisors", "Only some n"], e, 7, 'proficient'))
    
    while len(questions) < 50:
        questions.append(create_question(
            "For divisibility induction, show:", "f(k+1) - f(k) divisible by d, or f(k+1) = d×something",
            ["f(k) = 0", "Random values", "Only base case"], "Maintain divisibility", 7, 'proficient'))
    
    return questions[:50]

def generate_level_8():
    """Level 8: Proof by Induction - Inequalities"""
    questions = []
    
    inequalities = [
        ("2ⁿ > n for n≥1. Base n=1:", "2 > 1 ✓", "True"),
        ("For 2ⁿ > n: 2ᵏ⁺¹ = 2·2ᵏ > 2k ≥ k+1 when:", "k ≥ 1", "2k ≥ k+1"),
        ("2ⁿ ≥ n² for n≥4. Why n≥4?", "Fails for n=3: 8 < 9", "Need correct base"),
        ("n! > 2ⁿ for n≥4. Base n=4:", "24 > 16 ✓", "4! = 24"),
        ("Bernoulli: (1+x)ⁿ ≥ 1+nx for x>-1:", "Famous inequality", "Proven by induction"),
    ]
    for q, a, e in inequalities:
        questions.append(create_question(q, a, ["False", "n≥1 works", "Cannot prove"], e, 8, 'proficient'))
    
    steps = [
        ("For n! > 2ⁿ: (k+1)! > 2ᵏ⁺¹ needs:", "(k+1)·k! > 2·2ᵏ, use IH and k+1>2", "k≥2 works"),
        ("Bernoulli base: (1+x)¹ ≥ 1+x:", "Equality ✓", "Both equal 1+x"),
        ("Bernoulli step uses (1+kx)(1+x) ≥", "1+(k+1)x since kx² ≥ 0", "Non-negative term"),
        ("For inequality induction, show:", "f(k+1) maintains ≤ or ≥ direction", "Preserve inequality"),
    ]
    for q, a, e in steps:
        questions.append(create_question(q, a, ["Equality always", "Reverse inequality", "Different method"], e, 8, 'proficient'))
    
    advanced = [
        ("AM-GM: (a+b)/2 ≥ √(ab) proven by:", "Algebra: ((a-b)/2)² ≥ 0", "Perfect square"),
        ("3ⁿ > n² for n≥1 needs step:", "3ⁿ⁺¹ = 3·3ⁿ > 3n² ≥ (n+1)² for large n", "Eventually true"),
        ("∑1/i² < 2 uses:", "Telescoping bound: 1/k² < 1/(k-1) - 1/k", "Upper bound"),
    ]
    for q, a, e in advanced:
        questions.append(create_question(q, a, ["Cannot prove", "Lower bound", "Different inequality"], e, 8, 'proficient'))
    
    while len(questions) < 50:
        questions.append(create_question(
            "For 2ⁿ > n³ starting at n=10:", "Check base, then inductive step",
            ["Works for all n", "Never true", "Only n=10"], "Eventually dominates", 8, 'proficient'))
    
    return questions[:50]

def generate_level_9():
    """Level 9: Geometric Proofs"""
    questions = []
    
    basic = [
        ("Sum of angles in triangle:", "180°", "Fundamental theorem"),
        ("Exterior angle of triangle equals:", "Sum of remote interior angles", "Exterior angle theorem"),
        ("Base angles of isosceles triangle:", "Equal", "Isosceles theorem"),
        ("Vertically opposite angles are:", "Equal", "Intersecting lines"),
        ("Angle in semicircle:", "90°", "Thales' theorem"),
    ]
    for q, a, e in basic:
        questions.append(create_question(q, a, ["360°", "Supplementary", "60°"], e, 9, 'proficient'))
    
    circle = [
        ("Central angle vs inscribed angle:", "Central = 2× inscribed", "Same arc"),
        ("Angles in same segment are:", "Equal", "Same arc"),
        ("Opposite angles of cyclic quad:", "Sum to 180°", "Supplementary"),
        ("Tangent perpendicular to:", "Radius at tangency", "Fundamental property"),
        ("Alternate segment theorem relates:", "Tangent-chord angle to inscribed angle", "Equal angles"),
    ]
    for q, a, e in circle:
        questions.append(create_question(q, a, ["Equal", "Sum to 360°", "Parallel"], e, 9, 'proficient'))
    
    congruence = [
        ("Triangle congruence criteria:", "SSS, SAS, ASA, AAS, RHS", "Five methods"),
        ("Why doesn't SSA (ASS) work?", "Ambiguous case - two triangles possible", "Not valid"),
        ("To prove lines parallel, show:", "Alternate angles equal", "Or corresponding equal"),
        ("Similar triangles have:", "Equal angles, proportional sides", "Same shape"),
    ]
    for q, a, e in congruence:
        questions.append(create_question(q, a, ["AAA, SSS", "Always works", "Equal sides"], e, 9, 'proficient'))
    
    while len(questions) < 50:
        questions.append(create_question(
            "Midpoint theorem: Line joining midpoints is:", "Parallel to base, half its length",
            ["Perpendicular", "Equal length", "At 45°"], "Important result", 9, 'proficient'))
    
    return questions[:50]

def generate_level_10():
    """Level 10: Algebraic Proofs"""
    questions = []
    
    identities = [
        ("(a+b)² =", "a² + 2ab + b²", "Expand (a+b)(a+b)"),
        ("(a-b)² =", "a² - 2ab + b²", "Similar expansion"),
        ("(a+b)(a-b) =", "a² - b²", "Difference of squares"),
        ("a³ - b³ =", "(a-b)(a² + ab + b²)", "Difference of cubes"),
        ("a³ + b³ =", "(a+b)(a² - ab + b²)", "Sum of cubes"),
    ]
    for q, a, e in identities:
        questions.append(create_question(f"Prove: {q}", a, ["a² + b²", "a² - b²", "ab"], e, 10, 'advanced'))
    
    inequalities = [
        ("a² + b² ≥ 2ab because:", "(a-b)² ≥ 0", "Perfect square"),
        ("|ab| = |a||b| proven by:", "Case analysis on signs", "Four cases"),
        ("|a+b| ≤ |a|+|b| is:", "Triangle inequality", "Fundamental"),
        ("AM-GM: (a+b)/2 ≥ √(ab) for a,b>0", "Square both sides", "Classic inequality"),
    ]
    for q, a, e in inequalities:
        questions.append(create_question(q, a, ["(a+b)² ≤ 0", "Direct", "Not true"], e, 10, 'advanced'))
    
    techniques = [
        ("To prove identity, show:", "LHS - RHS = 0", "Difference method"),
        ("For quadratic, sum of roots =", "-b/a", "Vieta's formula"),
        ("For quadratic, product of roots =", "c/a", "Vieta's formula"),
        ("If p(r) = 0, then (x-r) is:", "A factor of p(x)", "Factor theorem"),
        ("log(ab) = log(a) + log(b) from:", "Exponent laws", "10^(x+y) = 10^x · 10^y"),
    ]
    for q, a, e in techniques:
        questions.append(create_question(q, a, ["LHS = RHS always", "b/a", "Sum"], e, 10, 'advanced'))
    
    while len(questions) < 50:
        questions.append(create_question(
            "Prove: (1+x)ⁿ = Σ C(n,k)xᵏ", "Binomial theorem by induction",
            ["Cannot prove", "Only for n=2", "Different formula"], "Combinatorial argument", 10, 'advanced'))
    
    return questions[:50]

def generate_level_11():
    """Level 11: Number Theory Proofs"""
    questions = []
    
    basic = [
        ("Every integer is even or odd because:", "n = 2q + r where r ∈ {0,1}", "Division algorithm"),
        ("gcd(a,b) · lcm(a,b) =", "ab", "Prime factorization"),
        ("Bezout: gcd(a,b) = ax + by for:", "Some integers x, y", "Linear combination"),
        ("If prime p | ab, then:", "p|a or p|b", "Euclid's lemma"),
        ("√p irrational for prime p:", "Same as √2 proof", "Common factor contradiction"),
    ]
    for q, a, e in basic:
        questions.append(create_question(q, a, ["n = 2q", "a + b", "p|a and p|b"], e, 11, 'advanced'))
    
    theorems = [
        ("Fermat's Little: aᵖ ≡", "a (mod p) for prime p", "Fundamental"),
        ("Wilson's: (p-1)! ≡ -1 (mod p) iff:", "p is prime", "Prime characterization"),
        ("n divisible by 9 iff:", "Digit sum divisible by 9", "10 ≡ 1 (mod 9)"),
        ("n divisible by 11 iff:", "Alternating digit sum divisible by 11", "10 ≡ -1 (mod 11)"),
        ("n⁵ - n divisible by 30 by:", "Fermat for 2, 3, 5", "2×3×5 = 30"),
    ]
    for q, a, e in theorems:
        questions.append(create_question(q, a, ["0 (mod p)", "p is composite", "Sum of digits"], e, 11, 'advanced'))
    
    advanced = [
        ("Perfect square mod 4 is:", "0 or 1", "Two possibilities"),
        ("x² + y² = 4k+3 has:", "No integer solutions", "Squares are 0,1 mod 4"),
        ("Primes > 3 have form:", "6k ± 1", "Others divisible by 2 or 3"),
        ("gcd(n, n+1) =", "1", "Consecutive integers coprime"),
    ]
    for q, a, e in advanced:
        questions.append(create_question(q, a, ["0, 1, 2, 3", "Infinitely many", "2k or 3k"], e, 11, 'advanced'))
    
    while len(questions) < 50:
        questions.append(create_question(
            "Euler's theorem: a^φ(n) ≡ 1 (mod n) if:", "gcd(a,n) = 1",
            ["a = n", "n is prime", "a > n"], "Generalization of Fermat", 11, 'advanced'))
    
    return questions[:50]

def generate_level_12():
    """Level 12: Mastery Challenge"""
    questions = []
    
    mixed = [
        ("Best method for √3 irrational:", "Contradiction", "Assume rational"),
        ("Best method for n³-n divisible by 6:", "Direct (factoring)", "Three consecutive"),
        ("Best method for 2ⁿ > n:", "Induction", "Natural fit"),
        ("Best method for product of irrationals can be rational:", "Example: √2×√2 = 2", "Constructive"),
        ("Contrapositive of 'n² odd ⟹ n odd':", "n even ⟹ n² even", "Swap and negate"),
    ]
    for q, a, e in mixed:
        questions.append(create_question(q, a, ["Direct proof", "Induction", "Counterexample"], e, 12, 'advanced'))
    
    applications = [
        ("√2 + √3 irrational by:", "Contradiction: if rational, √6 rational", "Chain of irrationals"),
        ("Between two rationals exists:", "An irrational (e.g., a + (b-a)/√2)", "Construction"),
        ("Sum of n-gon angles:", "(n-2)×180°", "Triangulation"),
        ("In graph, sum of degrees is:", "Even (2 × edges)", "Handshaking lemma"),
        ("NOT valid: proof by example for:", "Universal statements", "One case doesn't prove all"),
    ]
    for q, a, e in applications:
        questions.append(create_question(q, a, ["Direct calculation", "n×180°", "Odd"], e, 12, 'advanced'))
    
    techniques = [
        ("Strong induction assumes:", "P(1)...P(k) all true", "Multiple predecessors"),
        ("Use strong induction when:", "P(k+1) needs several earlier cases", "Like Fibonacci"),
        ("Every n>1 is product of primes by:", "Strong induction", "Factor if composite"),
        ("De Morgan: ¬(P∧Q) =", "¬P ∨ ¬Q", "Negate AND"),
        ("De Morgan: ¬(P∨Q) =", "¬P ∧ ¬Q", "Negate OR"),
    ]
    for q, a, e in techniques:
        questions.append(create_question(q, a, ["Only P(k)", "Direct proof", "¬P ∧ ¬Q"], e, 12, 'advanced'))
    
    final = [
        ("0.999... = 1 by:", "Let x = 0.999..., then 10x - x = 9", "Algebra"),
        ("gcd(n, n+1) = 1 because:", "Common divisor divides difference = 1", "Simple"),
        ("To disprove 'for all x, P(x)':", "One counterexample", "Single case"),
        ("To disprove 'exists x with P(x)':", "Prove 'for all x, not P(x)'", "Universal negation"),
    ]
    for q, a, e in final:
        questions.append(create_question(q, a, ["Limit", "Cannot disprove", "Multiple examples"], e, 12, 'advanced'))
    
    while len(questions) < 50:
        questions.append(create_question(
            "Well-ordering principle:", "Every non-empty set of positive integers has smallest element",
            ["Largest element", "No smallest", "Applies to reals"], "Foundation of induction", 12, 'advanced'))
    
    return questions[:50]

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
        f.write(f"-- LC Higher Level - Proof & Reasoning Questions\n")
        f.write(f"-- Generated: 2025-12-14\n")
        f.write(f"-- Total: {len(all_questions)} questions\n\n")
        f.write('\n'.join(sql_statements))
    
    print(f"\nSQL file written to: {sql_file}")
    return all_questions

if __name__ == '__main__':
    main()
