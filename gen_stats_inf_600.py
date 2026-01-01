#!/usr/bin/env python3
"""
LC Ordinary Level Statistics (Inferential) - 600 Questions Generator
=====================================================================
50 questions per level × 12 levels = 600 questions

Based on SEC Paper Analysis 2019-2025:
- Inferential Statistics: sampling, hypothesis testing, correlation, normal distribution
- Complements lc_ol_statistics_desc (descriptive statistics)
"""

import random

TOPIC_ID = 'lc_ol_statistics_inf'
STRAND_ID = 11

LEVEL_CONFIG = {
    1: ("Sampling Methods", "Foundation"),
    2: ("Bias and Reliability", "Foundation"),
    3: ("Normal Distribution Basics", "Foundation"),
    4: ("Standard Deviation", "Developing"),
    5: ("Z-Scores", "Developing"),
    6: ("Empirical Rule", "Developing"),
    7: ("Scatter Plots", "Proficient"),
    8: ("Correlation", "Proficient"),
    9: ("Line of Best Fit", "Proficient"),
    10: ("Hypothesis Testing Concepts", "Advanced"),
    11: ("Margin of Error", "Advanced"),
    12: ("SEC Exam Style", "Advanced"),
}

def shuffle_options(correct, distractors):
    options = [correct] + distractors[:3]
    random.shuffle(options)
    return options, options.index(correct)

def generate_level_1():
    """Sampling Methods"""
    questions = []
    
    # Define population
    opts, idx = shuffle_options("The entire group being studied", ["A subset of data", "The average value", "The most common value"])
    questions.append({
        'text': "What is a population in statistics?",
        'opts': opts, 'idx': idx,
        'exp': "Population = entire group we want to learn about."
    })
    
    # Define sample
    opts, idx = shuffle_options("A subset of the population", ["The entire group", "The average", "An outlier"])
    questions.append({
        'text': "What is a sample in statistics?",
        'opts': opts, 'idx': idx,
        'exp': "Sample = smaller group selected from population."
    })
    
    # Why sample?
    opts, idx = shuffle_options("Too costly/time-consuming to survey everyone", ["Samples are more accurate", "Populations are too small", "It's required by law"])
    questions.append({
        'text': "Why do we use samples instead of populations?",
        'opts': opts, 'idx': idx,
        'exp': "Surveying entire populations is often impractical."
    })
    
    # Simple random sampling
    opts, idx = shuffle_options("Every member has equal chance of selection", ["Members are selected alphabetically", "Only certain groups included", "First 100 people selected"])
    questions.append({
        'text': "What is simple random sampling?",
        'opts': opts, 'idx': idx,
        'exp': "Random sampling gives everyone equal probability."
    })
    
    # Stratified sampling
    opts, idx = shuffle_options("Population divided into groups, sample from each", ["Random selection only", "Choosing convenient subjects", "Selecting every nth person"])
    questions.append({
        'text': "What is stratified sampling?",
        'opts': opts, 'idx': idx,
        'exp': "Stratified = divide into strata, sample proportionally."
    })
    
    # Systematic sampling
    opts, idx = shuffle_options("Select every nth member", ["Random selection", "Choose by age groups", "Volunteer participation"])
    questions.append({
        'text': "What is systematic sampling?",
        'opts': opts, 'idx': idx,
        'exp': "Systematic = select every kth item (e.g., every 10th)."
    })
    
    # Convenience sampling
    opts, idx = shuffle_options("Selecting easily accessible subjects", ["Random selection", "Stratified groups", "Systematic intervals"])
    questions.append({
        'text': "What is convenience sampling?",
        'opts': opts, 'idx': idx,
        'exp': "Convenience = choose whoever is easily available."
    })
    
    # Identify sampling method - scenarios
    scenarios = [
        ("Survey every 5th customer entering a shop", "Systematic"),
        ("Put all names in a hat and draw 50", "Simple random"),
        ("Survey students you meet in the canteen", "Convenience"),
        ("Survey 10% of each year group", "Stratified"),
        ("Use a random number generator to select participants", "Simple random"),
        ("Interview people walking past your house", "Convenience"),
        ("Select every 10th name from a list", "Systematic"),
        ("Ensure equal representation from each county", "Stratified"),
    ]
    for scenario, method in scenarios:
        opts, idx = shuffle_options(method, ["Simple random", "Stratified", "Systematic", "Convenience"])
        # Remove the correct answer from distractors
        distractors = [m for m in ["Simple random", "Stratified", "Systematic", "Convenience"] if m != method]
        opts, idx = shuffle_options(method, distractors)
        questions.append({
            'text': f"Sampling method: {scenario}",
            'opts': opts, 'idx': idx,
            'exp': f"This is {method} sampling."
        })
    
    # Sample size effects
    for size in ["larger", "smaller"]:
        if size == "larger":
            opts, idx = shuffle_options("More representative", ["Less accurate", "More biased", "Harder to analyse"])
        else:
            opts, idx = shuffle_options("Less representative", ["More accurate", "Less biased", "Easier to generalise"])
        questions.append({
            'text': f"A {size} sample is generally...",
            'opts': opts, 'idx': idx,
            'exp': f"{'Larger' if size == 'larger' else 'Smaller'} samples are {'more' if size == 'larger' else 'less'} representative."
        })
    
    # Identify population and sample
    pop_sample = [
        ("Survey 200 students about school lunches", "All students", "The 200 surveyed"),
        ("Test 50 batteries from a factory", "All batteries produced", "The 50 tested"),
        ("Poll 1000 voters about election", "All voters", "The 1000 polled"),
        ("Measure height of 30 trees in forest", "All trees in forest", "The 30 measured"),
    ]
    for scenario, pop, samp in pop_sample:
        opts, idx = shuffle_options(pop, [samp, "The researcher", "The results"])
        questions.append({
            'text': f"{scenario}. What is the population?",
            'opts': opts, 'idx': idx,
            'exp': f"Population: {pop}."
        })
        opts, idx = shuffle_options(samp, [pop, "The researcher", "The results"])
        questions.append({
            'text': f"{scenario}. What is the sample?",
            'opts': opts, 'idx': idx,
            'exp': f"Sample: {samp}."
        })
        if len(questions) >= 35:
            break
    
    # Census vs sample
    opts, idx = shuffle_options("Data from every member of population", ["Data from a sample", "Average of results", "Most common value"])
    questions.append({
        'text': "What is a census?",
        'opts': opts, 'idx': idx,
        'exp': "Census = survey of entire population."
    })
    
    # When to use census
    opts, idx = shuffle_options("When population is small", ["When population is large", "Never", "Always"])
    questions.append({
        'text': "When is a census practical?",
        'opts': opts, 'idx': idx,
        'exp': "Census practical for small populations."
    })
    
    # Sample frame
    opts, idx = shuffle_options("List of all members of population", ["The sample itself", "The results", "The analysis"])
    questions.append({
        'text': "What is a sampling frame?",
        'opts': opts, 'idx': idx,
        'exp': "Sampling frame = complete list from which sample is drawn."
    })
    
    # Fill remaining
    for i in range(50 - len(questions)):
        n = random.randint(50, 200)
        pop_size = random.randint(1000, 5000)
        opts, idx = shuffle_options(f"{n}/{pop_size}", [f"{pop_size}/{n}", f"{n}", f"{pop_size}"])
        questions.append({
            'text': f"Sample of {n} from population of {pop_size}. Sampling fraction?",
            'opts': opts, 'idx': idx,
            'exp': f"Fraction = sample/population = {n}/{pop_size}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_2():
    """Bias and Reliability"""
    questions = []
    
    # Define bias
    opts, idx = shuffle_options("Systematic error favouring certain outcomes", ["Random error", "Large sample size", "Accurate results"])
    questions.append({
        'text': "What is bias in statistics?",
        'opts': opts, 'idx': idx,
        'exp': "Bias = systematic tendency to over/underestimate."
    })
    
    # Selection bias
    opts, idx = shuffle_options("Sample not representative of population", ["Random errors", "Too many questions", "Accurate sampling"])
    questions.append({
        'text': "What is selection bias?",
        'opts': opts, 'idx': idx,
        'exp': "Selection bias = sample differs systematically from population."
    })
    
    # Response bias
    opts, idx = shuffle_options("Answers influenced by question wording", ["Random selection", "Large samples", "Accurate responses"])
    questions.append({
        'text': "What is response bias?",
        'opts': opts, 'idx': idx,
        'exp': "Response bias = questions or context affect answers."
    })
    
    # Non-response bias
    opts, idx = shuffle_options("People who respond differ from non-responders", ["Everyone responds", "Random errors", "Too few questions"])
    questions.append({
        'text': "What is non-response bias?",
        'opts': opts, 'idx': idx,
        'exp': "Non-response bias = responders not representative."
    })
    
    # Identify biased scenarios
    biased = [
        ("Online survey about internet usage", "Selection bias - excludes non-internet users"),
        ("Asking 'Don't you agree pollution is bad?'", "Response bias - leading question"),
        ("Survey at 2pm on weekday in shopping centre", "Selection bias - excludes workers"),
        ("Voluntary phone-in poll", "Selection bias - only motivated people respond"),
        ("Survey with 50% non-response rate", "Non-response bias"),
        ("Asking employees if boss is good while boss watches", "Response bias"),
    ]
    for scenario, bias_type in biased:
        opts, idx = shuffle_options("Yes, biased", ["No, unbiased", "Cannot tell", "Only if sample is small"])
        questions.append({
            'text': f"Is this biased? {scenario}",
            'opts': opts, 'idx': idx,
            'exp': bias_type
        })
    
    # Reliability
    opts, idx = shuffle_options("Consistency of results if repeated", ["Accuracy of results", "Size of sample", "Type of sampling"])
    questions.append({
        'text': "What does reliability mean?",
        'opts': opts, 'idx': idx,
        'exp': "Reliable = consistent results when repeated."
    })
    
    # Validity
    opts, idx = shuffle_options("Measuring what we intend to measure", ["Consistency", "Sample size", "Response rate"])
    questions.append({
        'text': "What does validity mean?",
        'opts': opts, 'idx': idx,
        'exp': "Valid = actually measures what we want."
    })
    
    # How to reduce bias
    reduce_bias = [
        ("Use random sampling", "Yes"),
        ("Use larger sample", "Yes"),
        ("Survey only friends", "No"),
        ("Use neutral question wording", "Yes"),
        ("Ensure high response rate", "Yes"),
        ("Survey at various times/locations", "Yes"),
    ]
    for method, helps in reduce_bias:
        opts, idx = shuffle_options(helps, ["No", "Sometimes", "Only for large samples"])
        questions.append({
            'text': f"Does this reduce bias? {method}",
            'opts': opts, 'idx': idx,
            'exp': f"{helps}, this {'helps reduce' if helps == 'Yes' else 'does not reduce'} bias."
        })
    
    # Leading questions
    leading = [
        ("Do you agree that exercise is important?", "Yes - leading"),
        ("How often do you exercise?", "No - neutral"),
        ("Don't you think taxes are too high?", "Yes - leading"),
        ("What is your opinion on taxes?", "No - neutral"),
        ("Wouldn't you say the food here is excellent?", "Yes - leading"),
    ]
    for q, is_leading in leading:
        ans = "Yes" if "Yes" in is_leading else "No"
        opts, idx = shuffle_options(ans, ["No" if ans == "Yes" else "Yes", "Cannot tell", "Depends on context"])
        questions.append({
            'text': f"Is this a leading question? '{q}'",
            'opts': opts, 'idx': idx,
            'exp': is_leading
        })
    
    # Sample size and reliability
    for n in [10, 50, 100, 500, 1000]:
        reliability = "Low" if n < 30 else "Medium" if n < 200 else "High"
        opts, idx = shuffle_options(reliability, ["Low", "Medium", "High"])
        questions.append({
            'text': f"Reliability of sample size n = {n}?",
            'opts': opts, 'idx': idx,
            'exp': f"Sample of {n} has {reliability.lower()} reliability."
        })
        if len(questions) >= 35:
            break
    
    # Generalisation
    opts, idx = shuffle_options("Applying sample results to population", ["Collecting data", "Calculating mean", "Drawing graphs"])
    questions.append({
        'text': "What is generalisation in statistics?",
        'opts': opts, 'idx': idx,
        'exp': "Generalisation = extending findings to whole population."
    })
    
    # Random vs non-random
    opts, idx = shuffle_options("Random sampling", ["Convenience sampling", "Voluntary sampling", "Quota sampling"])
    questions.append({
        'text': "Which sampling method best avoids selection bias?",
        'opts': opts, 'idx': idx,
        'exp': "Random sampling gives everyone equal chance."
    })
    
    # Fill to 50
    problems = [
        ("Magazine survey sent to subscribers only", "Selection bias"),
        ("Exit poll at one polling station", "Selection bias"),
        ("Survey asking 'How much do you love our product?'", "Response bias"),
        ("Medical trial where patients can choose treatment", "Selection bias"),
        ("Taste test where tasters know brand names", "Response bias"),
    ]
    for scenario, bias in problems:
        opts, idx = shuffle_options(bias, ["No bias", "Random error", "Measurement error"])
        questions.append({
            'text': f"What type of bias? {scenario}",
            'opts': opts, 'idx': idx,
            'exp': f"This is {bias}."
        })
    
    # More bias scenarios
    more_problems = [
        ("Phone survey during work hours", "Selection bias"),
        ("Asking employees about job satisfaction in front of manager", "Response bias"),
        ("Survey about exercise at a gym", "Selection bias"),
        ("Question: 'Do you support our excellent new policy?'", "Response bias"),
        ("Online poll with no verification", "Selection bias"),
        ("Survey with complex technical language", "Response bias"),
        ("Only surveying people who volunteer", "Selection bias"),
        ("Low response rate survey", "Non-response bias"),
        ("Street survey in wealthy neighbourhood", "Selection bias"),
        ("Anonymous vs non-anonymous responses differ", "Response bias"),
        ("Email survey to company mailing list", "Selection bias"),
        ("Survey about diet at health food store", "Selection bias"),
        ("Asking loaded questions", "Response bias"),
        ("Different interviewers get different results", "Response bias"),
        ("Survey missing certain demographics", "Selection bias"),
    ]
    for scenario, bias in more_problems:
        opts, idx = shuffle_options(bias, ["Selection bias", "Response bias", "Non-response bias", "No bias"])
        questions.append({
            'text': f"Identify bias: {scenario}",
            'opts': opts, 'idx': idx,
            'exp': f"This is {bias}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_3():
    """Normal Distribution Basics"""
    questions = []
    
    # Shape
    opts, idx = shuffle_options("Bell-shaped and symmetric", ["Skewed right", "Skewed left", "Uniform"])
    questions.append({
        'text': "What shape is a normal distribution?",
        'opts': opts, 'idx': idx,
        'exp': "Normal distribution is bell-shaped and symmetric."
    })
    
    # Center
    opts, idx = shuffle_options("Mean = Median = Mode", ["Mean > Median", "Mean < Mode", "All different"])
    questions.append({
        'text': "In a normal distribution, which is true?",
        'opts': opts, 'idx': idx,
        'exp': "In normal distribution, mean = median = mode."
    })
    
    # Symmetry
    opts, idx = shuffle_options("The mean", ["Zero", "The mode only", "The maximum"])
    questions.append({
        'text': "A normal distribution is symmetric about...",
        'opts': opts, 'idx': idx,
        'exp': "Symmetric about the mean (center)."
    })
    
    # Tails
    opts, idx = shuffle_options("Approach but never touch x-axis", ["Touch x-axis", "Stop at ±3σ", "Are cut off"])
    questions.append({
        'text': "The tails of a normal distribution...",
        'opts': opts, 'idx': idx,
        'exp': "Tails extend infinitely, approaching but never reaching zero."
    })
    
    # Area under curve
    opts, idx = shuffle_options("1 (or 100%)", ["0", "0.5", "Depends on σ"])
    questions.append({
        'text': "Total area under normal curve equals...",
        'opts': opts, 'idx': idx,
        'exp': "Total probability = 1 (100%)."
    })
    
    # What determines shape
    opts, idx = shuffle_options("Standard deviation (σ)", ["Mean only", "Sample size", "Median"])
    questions.append({
        'text': "What determines the spread of a normal curve?",
        'opts': opts, 'idx': idx,
        'exp': "Standard deviation determines width/spread."
    })
    
    # What determines position
    opts, idx = shuffle_options("Mean (μ)", ["Standard deviation", "Sample size", "Range"])
    questions.append({
        'text': "What determines the center of a normal curve?",
        'opts': opts, 'idx': idx,
        'exp': "Mean determines the center position."
    })
    
    # Larger σ effect
    opts, idx = shuffle_options("Wider and flatter", ["Taller and narrower", "Shifted right", "Shifted left"])
    questions.append({
        'text': "A larger standard deviation makes the curve...",
        'opts': opts, 'idx': idx,
        'exp': "Larger σ = more spread = wider, flatter curve."
    })
    
    # Smaller σ effect
    opts, idx = shuffle_options("Taller and narrower", ["Wider and flatter", "Shifted right", "Shifted left"])
    questions.append({
        'text': "A smaller standard deviation makes the curve...",
        'opts': opts, 'idx': idx,
        'exp': "Smaller σ = less spread = taller, narrower curve."
    })
    
    # Examples of normal distribution
    normal_examples = [
        ("Heights of adult women", "Yes"),
        ("IQ scores", "Yes"),
        ("Blood pressure readings", "Yes"),
        ("Number of cars sold per day", "No - likely skewed"),
        ("Exam scores (well-designed test)", "Yes"),
        ("Household income", "No - typically skewed right"),
        ("Weights of manufactured items", "Yes"),
        ("Age at death", "No - skewed left"),
    ]
    for example, is_normal in normal_examples:
        ans = "Likely normal" if is_normal == "Yes" else "Likely not normal"
        opts, idx = shuffle_options(ans, ["Likely normal", "Likely not normal", "Cannot tell", "Always normal"])
        questions.append({
            'text': f"Is this normally distributed? {example}",
            'opts': opts, 'idx': idx,
            'exp': is_normal
        })
    
    # 50% above/below mean
    opts, idx = shuffle_options("50%", ["68%", "95%", "34%"])
    questions.append({
        'text': "What percentage of data lies above the mean?",
        'opts': opts, 'idx': idx,
        'exp': "Symmetric: 50% above, 50% below mean."
    })
    
    # Compare distributions
    for mu1, mu2 in [(50, 60), (100, 100), (20, 30)]:
        for s1, s2 in [(10, 10), (5, 10), (10, 5)]:
            if mu1 != mu2 or s1 != s2:
                if mu1 < mu2:
                    ans = "Curve B is shifted right"
                elif mu1 > mu2:
                    ans = "Curve A is shifted right"
                elif s1 < s2:
                    ans = "Curve A is taller/narrower"
                else:
                    ans = "Curve B is taller/narrower"
                opts, idx = shuffle_options(ans, ["Curves are identical", "Curve A is shifted right", "Curve B is taller/narrower"])
                questions.append({
                    'text': f"Compare: A(μ={mu1}, σ={s1}) vs B(μ={mu2}, σ={s2})",
                    'opts': opts, 'idx': idx,
                    'exp': ans
                })
                if len(questions) >= 40:
                    break
        if len(questions) >= 40:
            break
    
    # Standard normal
    opts, idx = shuffle_options("μ = 0, σ = 1", ["μ = 1, σ = 0", "μ = 0, σ = 0", "μ = 1, σ = 1"])
    questions.append({
        'text': "What are the parameters of standard normal?",
        'opts': opts, 'idx': idx,
        'exp': "Standard normal: mean = 0, SD = 1."
    })
    
    # Notation
    opts, idx = shuffle_options("N(μ, σ²)", ["N(σ, μ)", "N(μ, σ)", "μ(N, σ)"])
    questions.append({
        'text': "How is normal distribution written?",
        'opts': opts, 'idx': idx,
        'exp': "N(μ, σ²) or sometimes N(μ, σ)."
    })
    
    # Fill remaining
    for mean in [50, 100, 170, 60, 80, 120, 150, 200]:
        for sd in [5, 10, 15, 8, 12, 20]:
            opts, idx = shuffle_options(f"μ = {mean}, σ = {sd}", [f"μ = {sd}, σ = {mean}", f"μ = {mean + sd}, σ = {sd}", f"μ = {mean}, σ = {sd + 5}"])
            questions.append({
                'text': f"Data ~ N({mean}, {sd}²). State μ and σ.",
                'opts': opts, 'idx': idx,
                'exp': f"Mean μ = {mean}, SD σ = {sd}."
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_4():
    """Standard Deviation"""
    questions = []
    
    # Definition
    opts, idx = shuffle_options("Measure of spread from the mean", ["The middle value", "The most common value", "The range"])
    questions.append({
        'text': "What does standard deviation measure?",
        'opts': opts, 'idx': idx,
        'exp': "SD measures how spread out data is from mean."
    })
    
    # Symbol
    opts, idx = shuffle_options("σ (sigma)", ["μ (mu)", "Σ (sum)", "π (pi)"])
    questions.append({
        'text': "What symbol represents standard deviation?",
        'opts': opts, 'idx': idx,
        'exp': "σ (lowercase sigma) for population SD."
    })
    
    # Low SD means
    opts, idx = shuffle_options("Data clustered close to mean", ["Data spread far from mean", "Large range", "Many outliers"])
    questions.append({
        'text': "A low standard deviation indicates...",
        'opts': opts, 'idx': idx,
        'exp': "Low SD = data points close to mean."
    })
    
    # High SD means
    opts, idx = shuffle_options("Data spread far from mean", ["Data clustered close to mean", "Small range", "No outliers"])
    questions.append({
        'text': "A high standard deviation indicates...",
        'opts': opts, 'idx': idx,
        'exp': "High SD = data points spread from mean."
    })
    
    # SD always positive
    opts, idx = shuffle_options("Always ≥ 0", ["Can be negative", "Always > 1", "Always < 1"])
    questions.append({
        'text': "Standard deviation is...",
        'opts': opts, 'idx': idx,
        'exp': "SD is always non-negative (≥ 0)."
    })
    
    # SD = 0 means
    opts, idx = shuffle_options("All values are identical", ["Data is spread out", "Mean is zero", "No data exists"])
    questions.append({
        'text': "If SD = 0, what does this mean?",
        'opts': opts, 'idx': idx,
        'exp': "SD = 0 means all data points are the same."
    })
    
    # Compare datasets by SD
    comparisons = [
        ("Test A: scores 45, 50, 55. Test B: scores 20, 50, 80", "Test B"),
        ("Heights: 170, 172, 171, 169. Weights: 60, 80, 55, 95", "Weights"),
        ("Group X: all scored 75. Group Y: scores varied 60-90", "Group Y"),
    ]
    for scenario, higher in comparisons:
        opts, idx = shuffle_options(higher, ["Test A" if "Test B" in higher else "Test B", "Same SD", "Cannot tell"])
        questions.append({
            'text': f"Which has higher SD? {scenario}",
            'opts': opts, 'idx': idx,
            'exp': f"{higher} has more spread, so higher SD."
        })
    
    # Effect of adding constant
    for c in [5, 10, 20]:
        opts, idx = shuffle_options("SD stays the same", [f"SD increases by {c}", f"SD decreases by {c}", "SD doubles"])
        questions.append({
            'text': f"If we add {c} to every value, SD...",
            'opts': opts, 'idx': idx,
            'exp': "Adding constant shifts data but doesn't change spread."
        })
        if len(questions) >= 18:
            break
    
    # Effect of multiplying by constant
    for c in [2, 3, 5]:
        opts, idx = shuffle_options(f"SD multiplied by {c}", ["SD stays same", f"SD divided by {c}", "SD squared"])
        questions.append({
            'text': f"If we multiply every value by {c}, SD...",
            'opts': opts, 'idx': idx,
            'exp': f"Multiplying by {c} multiplies SD by {c}."
        })
        if len(questions) >= 24:
            break
    
    # Calculate simple SD (conceptual)
    datasets = [
        ([10, 10, 10, 10], 0, "All same"),
        ([5, 10, 15], 5, "Spread of 5 from mean"),
        ([0, 10], 5, "Values 5 away from mean of 5"),
    ]
    for data, sd, reason in datasets:
        opts, idx = shuffle_options(str(sd), [str(sd + 1), str(sd + 2), str(sd - 1) if sd > 1 else "1"])
        questions.append({
            'text': f"Estimate SD for {data}.",
            'opts': opts, 'idx': idx,
            'exp': reason
        })
    
    # Variance relationship
    opts, idx = shuffle_options("Variance = SD²", ["SD = Variance²", "Variance = 2 × SD", "They're unrelated"])
    questions.append({
        'text': "How are variance and SD related?",
        'opts': opts, 'idx': idx,
        'exp': "Variance = SD², or SD = √Variance."
    })
    
    # Find SD from variance
    for var in [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]:
        sd = int(var ** 0.5)
        opts, idx = shuffle_options(str(sd), [str(sd + 1), str(sd - 1) if sd > 1 else "1", str(var)])
        questions.append({
            'text': f"If variance = {var}, what is SD?",
            'opts': opts, 'idx': idx,
            'exp': f"SD = √{var} = {sd}."
        })
        if len(questions) >= 42:
            break
    
    # Find variance from SD
    for sd in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
        var = sd * sd
        opts, idx = shuffle_options(str(var), [str(var + 1), str(sd), str(2 * sd)])
        questions.append({
            'text': f"If SD = {sd}, what is variance?",
            'opts': opts, 'idx': idx,
            'exp': f"Variance = {sd}² = {var}."
        })
        if len(questions) >= 48:
            break
    
    # More conceptual
    opts, idx = shuffle_options("Units squared", ["Same units as data", "No units", "Percentage"])
    questions.append({
        'text': "What units does variance have?",
        'opts': opts, 'idx': idx,
        'exp': "Variance is in squared units (e.g., cm² for height in cm)."
    })
    
    opts, idx = shuffle_options("Same units as data", ["Units squared", "No units", "Percentage"])
    questions.append({
        'text': "What units does standard deviation have?",
        'opts': opts, 'idx': idx,
        'exp': "SD has same units as original data."
    })
    
    opts, idx = shuffle_options("Standard deviation", ["Variance", "Mean", "Range"])
    questions.append({
        'text': "Which is easier to interpret: SD or variance?",
        'opts': opts, 'idx': idx,
        'exp': "SD is in same units as data, so easier to interpret."
    })
    
    return questions[:50]

def generate_level_5():
    """Z-Scores"""
    questions = []
    
    # Definition
    opts, idx = shuffle_options("Number of SDs from the mean", ["The mean value", "The range", "The median"])
    questions.append({
        'text': "What does a z-score tell us?",
        'opts': opts, 'idx': idx,
        'exp': "Z-score = how many SDs a value is from mean."
    })
    
    # Formula
    opts, idx = shuffle_options("z = (x - μ)/σ", ["z = (μ - x)/σ", "z = x × σ + μ", "z = σ/(x - μ)"])
    questions.append({
        'text': "What is the z-score formula?",
        'opts': opts, 'idx': idx,
        'exp': "z = (x - μ)/σ = (value - mean)/SD."
    })
    
    # Z = 0 means
    opts, idx = shuffle_options("Value equals the mean", ["Value is one SD above", "Value is maximum", "Value is minimum"])
    questions.append({
        'text': "A z-score of 0 means...",
        'opts': opts, 'idx': idx,
        'exp': "z = 0 means x = μ (at the mean)."
    })
    
    # Positive z means
    opts, idx = shuffle_options("Value above the mean", ["Value below the mean", "Value equals mean", "Impossible"])
    questions.append({
        'text': "A positive z-score means...",
        'opts': opts, 'idx': idx,
        'exp': "Positive z = above mean."
    })
    
    # Negative z means
    opts, idx = shuffle_options("Value below the mean", ["Value above the mean", "Value equals mean", "Impossible"])
    questions.append({
        'text': "A negative z-score means...",
        'opts': opts, 'idx': idx,
        'exp': "Negative z = below mean."
    })
    
    # Calculate z-scores
    for mu in [50, 100, 170]:
        for sigma in [5, 10, 15]:
            for z in [-2, -1, 0, 1, 2]:
                x = mu + z * sigma
                opts, idx = shuffle_options(str(z), [str(z + 1), str(z - 1), str(z + 2)])
                questions.append({
                    'text': f"μ = {mu}, σ = {sigma}. Z-score for x = {x}?",
                    'opts': opts, 'idx': idx,
                    'exp': f"z = ({x} - {mu})/{sigma} = {z}."
                })
                if len(questions) >= 25:
                    break
            if len(questions) >= 25:
                break
        if len(questions) >= 25:
            break
    
    # Find x from z-score
    for mu in [50, 100]:
        for sigma in [10, 15]:
            for z in [-1, 1, 2]:
                x = mu + z * sigma
                opts, idx = shuffle_options(str(x), [str(x + sigma), str(x - sigma), str(mu)])
                questions.append({
                    'text': f"μ = {mu}, σ = {sigma}. If z = {z}, find x.",
                    'opts': opts, 'idx': idx,
                    'exp': f"x = μ + zσ = {mu} + ({z})({sigma}) = {x}."
                })
                if len(questions) >= 35:
                    break
            if len(questions) >= 35:
                break
        if len(questions) >= 35:
            break
    
    # Compare z-scores
    for z1, z2 in [(1.5, 0.8), (-0.5, -1.2), (2.1, 1.9), (0, -0.5)]:
        if z1 > z2:
            ans = "First value"
        else:
            ans = "Second value"
        opts, idx = shuffle_options(ans, ["First value" if ans == "Second value" else "Second value", "Same", "Cannot compare"])
        questions.append({
            'text': f"Which is higher: z = {z1} or z = {z2}?",
            'opts': opts, 'idx': idx,
            'exp': f"Higher z-score = higher relative position."
        })
        if len(questions) >= 42:
            break
    
    # Unusual values (|z| > 2)
    for z in [-2.5, -1.5, 0.5, 1.8, 2.3, 3.0, -0.8, 1.2, -2.1, 2.8, 0.3, -1.9, 1.5, -3.2]:
        unusual = "Yes" if abs(z) > 2 else "No"
        opts, idx = shuffle_options(unusual, ["Yes" if unusual == "No" else "No", "Maybe", "Cannot tell"])
        questions.append({
            'text': f"Is z = {z} considered unusual (|z| > 2)?",
            'opts': opts, 'idx': idx,
            'exp': f"|{z}| = {abs(z)}, {'> 2 so unusual' if abs(z) > 2 else '≤ 2 so not unusual'}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_6():
    """Empirical Rule (68-95-99.7)"""
    questions = []
    
    # 68% rule
    opts, idx = shuffle_options("68%", ["50%", "95%", "99.7%"])
    questions.append({
        'text': "% of data within 1 SD of mean in normal distribution?",
        'opts': opts, 'idx': idx,
        'exp': "68% within μ ± σ (1 SD)."
    })
    
    # 95% rule
    opts, idx = shuffle_options("95%", ["68%", "99.7%", ["90%"]])
    questions.append({
        'text': "% of data within 2 SDs of mean?",
        'opts': opts, 'idx': idx,
        'exp': "95% within μ ± 2σ (2 SDs)."
    })
    
    # 99.7% rule
    opts, idx = shuffle_options("99.7%", ["68%", "95%", "100%"])
    questions.append({
        'text': "% of data within 3 SDs of mean?",
        'opts': opts, 'idx': idx,
        'exp': "99.7% within μ ± 3σ (3 SDs)."
    })
    
    # Outside 1 SD
    opts, idx = shuffle_options("32%", ["68%", ["16%"], "50%"])
    questions.append({
        'text': "% of data MORE than 1 SD from mean?",
        'opts': opts, 'idx': idx,
        'exp': "100% - 68% = 32% outside 1 SD."
    })
    
    # Outside 2 SDs
    opts, idx = shuffle_options("5%", ["95%", "2.5%", "10%"])
    questions.append({
        'text': "% of data MORE than 2 SDs from mean?",
        'opts': opts, 'idx': idx,
        'exp': "100% - 95% = 5% outside 2 SDs."
    })
    
    # Above/below mean (half of middle)
    opts, idx = shuffle_options("34%", ["68%", "50%", "17%"])
    questions.append({
        'text': "% of data between mean and 1 SD above?",
        'opts': opts, 'idx': idx,
        'exp': "Half of 68% = 34%."
    })
    
    # Applied problems
    for mu, sigma in [(100, 15), (170, 10), (50, 5)]:
        # Within 1 SD
        low1, high1 = mu - sigma, mu + sigma
        opts, idx = shuffle_options("68%", ["95%", "50%", "34%"])
        questions.append({
            'text': f"μ = {mu}, σ = {sigma}. % between {low1} and {high1}?",
            'opts': opts, 'idx': idx,
            'exp': f"This is μ ± σ, so 68%."
        })
        
        # Within 2 SDs
        low2, high2 = mu - 2*sigma, mu + 2*sigma
        opts, idx = shuffle_options("95%", ["68%", "99.7%", "90%"])
        questions.append({
            'text': f"μ = {mu}, σ = {sigma}. % between {low2} and {high2}?",
            'opts': opts, 'idx': idx,
            'exp': f"This is μ ± 2σ, so 95%."
        })
        
        if len(questions) >= 18:
            break
    
    # IQ example (μ=100, σ=15)
    opts, idx = shuffle_options("68%", ["95%", ["50%"], "34%"])
    questions.append({
        'text': "IQ: μ=100, σ=15. % with IQ between 85 and 115?",
        'opts': opts, 'idx': idx,
        'exp': "85 to 115 is μ ± σ, so 68%."
    })
    
    opts, idx = shuffle_options("95%", ["68%", "99.7%", "90%"])
    questions.append({
        'text': "IQ: μ=100, σ=15. % with IQ between 70 and 130?",
        'opts': opts, 'idx': idx,
        'exp': "70 to 130 is μ ± 2σ, so 95%."
    })
    
    # Heights example
    opts, idx = shuffle_options("68%", ["50%", "95%", "34%"])
    questions.append({
        'text': "Heights: μ=170cm, σ=10cm. % between 160 and 180?",
        'opts': opts, 'idx': idx,
        'exp': "160 to 180 is μ ± σ, so 68%."
    })
    
    # Above certain value
    opts, idx = shuffle_options("16%", ["32%", "50%", "84%"])
    questions.append({
        'text': "% of data more than 1 SD ABOVE mean?",
        'opts': opts, 'idx': idx,
        'exp': "Half of 32% = 16% above (or below)."
    })
    
    opts, idx = shuffle_options("2.5%", ["5%", "16%", "0.15%"])
    questions.append({
        'text': "% of data more than 2 SDs ABOVE mean?",
        'opts': opts, 'idx': idx,
        'exp': "Half of 5% = 2.5% above (or below)."
    })
    
    # Between mean and 2 SDs
    opts, idx = shuffle_options("47.5%", ["95%", ["50%"], "34%"])
    questions.append({
        'text': "% between mean and 2 SDs above?",
        'opts': opts, 'idx': idx,
        'exp': "Half of 95% = 47.5%."
    })
    
    # More applied
    for mu, sigma, context in [(500, 100, "exam scores"), (65, 5, "pulse rates"), (3000, 500, "birth weights (g)")]:
        for sds in [1, 2]:
            low = mu - sds * sigma
            high = mu + sds * sigma
            pct = "68" if sds == 1 else "95"
            opts, idx = shuffle_options(f"{pct}%", ["50%", "68%" if pct == "95" else "95%", "99.7%"])
            questions.append({
                'text': f"{context.title()}: μ={mu}, σ={sigma}. % between {low} and {high}?",
                'opts': opts, 'idx': idx,
                'exp': f"μ ± {sds}σ = {pct}%."
            })
            if len(questions) >= 45:
                break
        if len(questions) >= 45:
            break
    
    # Fill remaining
    for i in range(50 - len(questions)):
        opts, idx = shuffle_options("84%", ["16%", "68%", "50%"])
        questions.append({
            'text': "% of data BELOW 1 SD above the mean?",
            'opts': opts, 'idx': idx,
            'exp': "50% + 34% = 84%."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_7():
    """Scatter Plots"""
    questions = []
    
    # Purpose
    opts, idx = shuffle_options("Show relationship between two variables", ["Show frequency distribution", "Compare categories", "Show change over time"])
    questions.append({
        'text': "What is the purpose of a scatter plot?",
        'opts': opts, 'idx': idx,
        'exp': "Scatter plots show relationship between two numerical variables."
    })
    
    # Axes
    opts, idx = shuffle_options("Independent variable", ["Dependent variable", "The frequency", "The mean"])
    questions.append({
        'text': "What is typically on the x-axis of a scatter plot?",
        'opts': opts, 'idx': idx,
        'exp': "X-axis = independent (explanatory) variable."
    })
    
    opts, idx = shuffle_options("Dependent variable", ["Independent variable", "The frequency", "The range"])
    questions.append({
        'text': "What is typically on the y-axis?",
        'opts': opts, 'idx': idx,
        'exp': "Y-axis = dependent (response) variable."
    })
    
    # Positive correlation appearance
    opts, idx = shuffle_options("Points slope upward left to right", ["Points slope downward", "Points form horizontal line", "Points scattered randomly"])
    questions.append({
        'text': "How does positive correlation appear?",
        'opts': opts, 'idx': idx,
        'exp': "Positive correlation: as x increases, y increases."
    })
    
    # Negative correlation appearance
    opts, idx = shuffle_options("Points slope downward left to right", ["Points slope upward", "Points form horizontal line", "Points scattered randomly"])
    questions.append({
        'text': "How does negative correlation appear?",
        'opts': opts, 'idx': idx,
        'exp': "Negative correlation: as x increases, y decreases."
    })
    
    # No correlation appearance
    opts, idx = shuffle_options("Points scattered randomly", ["Points slope upward", "Points slope downward", "Points form a curve"])
    questions.append({
        'text': "How does no correlation appear?",
        'opts': opts, 'idx': idx,
        'exp': "No correlation: no clear pattern, random scatter."
    })
    
    # Identify correlation from description
    scenarios = [
        ("Study hours vs exam score (more study = higher score)", "Positive"),
        ("Age of car vs value (older = less valuable)", "Negative"),
        ("Height vs favourite colour", "No correlation"),
        ("Temperature vs ice cream sales", "Positive"),
        ("Speed vs travel time", "Negative"),
        ("Shoe size vs IQ", "No correlation"),
        ("Exercise vs weight loss", "Positive"),
        ("Smoking vs lung capacity", "Negative"),
        ("Hours of sleep vs alertness", "Positive"),
        ("Practice hours vs mistakes made", "Negative"),
    ]
    for scenario, corr in scenarios:
        opts, idx = shuffle_options(corr, ["Positive", "Negative", "No correlation"])
        questions.append({
            'text': f"What correlation? {scenario}",
            'opts': opts, 'idx': idx,
            'exp': f"{corr} correlation."
        })
        if len(questions) >= 25:
            break
    
    # Strong vs weak correlation
    opts, idx = shuffle_options("Points close to a line", ["Points scattered widely", "Many outliers", "Curved pattern"])
    questions.append({
        'text': "What indicates strong correlation?",
        'opts': opts, 'idx': idx,
        'exp': "Strong = points tightly clustered around line."
    })
    
    opts, idx = shuffle_options("Points spread from the line", ["Points on the line", "No outliers", "Linear pattern"])
    questions.append({
        'text': "What indicates weak correlation?",
        'opts': opts, 'idx': idx,
        'exp': "Weak = points loosely scattered around trend."
    })
    
    # Outliers
    opts, idx = shuffle_options("A point far from the general pattern", ["The highest point", "The lowest point", "The mean point"])
    questions.append({
        'text': "What is an outlier on a scatter plot?",
        'opts': opts, 'idx': idx,
        'exp': "Outlier = point that doesn't follow the pattern."
    })
    
    # Reading scatter plots
    for x, y in [(3, 6), (5, 10), (2, 4), (4, 8)]:
        opts, idx = shuffle_options(f"({x}, {y})", [f"({y}, {x})", f"({x+1}, {y})", f"({x}, {y+1})"])
        questions.append({
            'text': f"Point at x = {x}, y = {y} is written as...",
            'opts': opts, 'idx': idx,
            'exp': f"Coordinates: ({x}, {y})."
        })
        if len(questions) >= 38:
            break
    
    # Causation vs correlation
    opts, idx = shuffle_options("No, correlation doesn't imply causation", ["Yes, always", "Only for strong correlation", "Only for positive correlation"])
    questions.append({
        'text': "Does correlation prove causation?",
        'opts': opts, 'idx': idx,
        'exp': "Correlation ≠ causation. Other factors may be involved."
    })
    
    # Fill remaining with interpretation
    interpretations = [
        ("Points form tight upward line", "Strong positive"),
        ("Points form loose downward trend", "Weak negative"),
        ("Points show no pattern", "No correlation"),
        ("Points tightly follow downward line", "Strong negative"),
        ("Points loosely trend upward", "Weak positive"),
        ("Scattered dots sloping up", "Positive correlation"),
        ("Scattered dots sloping down", "Negative correlation"),
        ("Random scatter with no trend", "No correlation"),
        ("Points clustered in upward diagonal", "Positive correlation"),
        ("Points clustered in downward diagonal", "Negative correlation"),
    ]
    for desc, corr in interpretations:
        opts, idx = shuffle_options(corr, ["Strong positive", "Strong negative", "Weak positive", "No correlation"][:4])
        questions.append({
            'text': f"Describe: {desc}",
            'opts': opts, 'idx': idx,
            'exp': f"{corr}."
        })
        if len(questions) >= 45:
            break
    
    # More scenarios
    more_scenarios = [
        ("Coffee consumption vs productivity", "Could be positive"),
        ("Screen time vs sleep quality", "Likely negative"),
        ("Price vs demand", "Typically negative"),
        ("Advertising spend vs sales", "Likely positive"),
        ("Age of phone vs battery life", "Negative"),
        ("Education level vs income", "Positive"),
        ("Distance from city vs house price", "Negative"),
        ("Exercise frequency vs resting heart rate", "Negative"),
        ("Hours worked vs fatigue level", "Positive"),
        ("Study time vs test anxiety", "Negative"),
        ("Car age vs maintenance costs", "Positive"),
        ("Employee training vs error rate", "Negative"),
        ("Temperature vs heating bill", "Negative"),
        ("Rainfall vs crop yield", "Positive"),
        ("Age vs flexibility", "Negative"),
        ("Practice hours vs skill level", "Positive"),
    ]
    for scenario, expected in more_scenarios:
        opts, idx = shuffle_options(expected, ["Positive", "Negative", "No correlation", "Cannot predict"])
        questions.append({
            'text': f"Expected correlation: {scenario}",
            'opts': opts, 'idx': idx,
            'exp': f"{expected} correlation expected."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_8():
    """Correlation"""
    questions = []
    
    # Correlation coefficient range
    opts, idx = shuffle_options("-1 to +1", ["0 to 1", ["-∞ to +∞"], "0 to 100"])
    questions.append({
        'text': "What is the range of correlation coefficient r?",
        'opts': opts, 'idx': idx,
        'exp': "r is always between -1 and +1."
    })
    
    # r = 1 means
    opts, idx = shuffle_options("Perfect positive correlation", ["Perfect negative correlation", "No correlation", "Strong negative"])
    questions.append({
        'text': "What does r = 1 mean?",
        'opts': opts, 'idx': idx,
        'exp': "r = 1 is perfect positive linear relationship."
    })
    
    # r = -1 means
    opts, idx = shuffle_options("Perfect negative correlation", ["Perfect positive correlation", "No correlation", "Weak positive"])
    questions.append({
        'text': "What does r = -1 mean?",
        'opts': opts, 'idx': idx,
        'exp': "r = -1 is perfect negative linear relationship."
    })
    
    # r = 0 means
    opts, idx = shuffle_options("No linear correlation", ["Perfect correlation", "Strong correlation", "Moderate correlation"])
    questions.append({
        'text': "What does r = 0 mean?",
        'opts': opts, 'idx': idx,
        'exp': "r = 0 means no linear relationship."
    })
    
    # Interpret r values
    r_values = [
        (0.95, "Strong positive"),
        (0.75, "Moderate positive"),
        (0.25, "Weak positive"),
        (-0.90, "Strong negative"),
        (-0.60, "Moderate negative"),
        (-0.15, "Weak negative"),
        (0.05, "No correlation"),
    ]
    for r, interp in r_values:
        opts, idx = shuffle_options(interp, ["Strong positive", "Strong negative", "Weak positive", "No correlation"][:4])
        questions.append({
            'text': f"Interpret r = {r}",
            'opts': opts, 'idx': idx,
            'exp': f"r = {r} indicates {interp.lower()}."
        })
    
    # Compare r values (which is stronger)
    pairs = [
        (0.8, -0.9, "r = -0.9 (stronger)"),
        (0.6, 0.3, "r = 0.6 (stronger)"),
        (-0.7, -0.4, "r = -0.7 (stronger)"),
        (0.5, -0.5, "Same strength"),
        (0.85, -0.85, "Same strength"),
    ]
    for r1, r2, ans in pairs:
        opts, idx = shuffle_options(ans, [f"r = {r1} (stronger)", f"r = {r2} (stronger)", "Same strength", "Cannot compare"])
        questions.append({
            'text': f"Which shows stronger correlation: r = {r1} or r = {r2}?",
            'opts': opts, 'idx': idx,
            'exp': f"Strength is |r|. {ans}."
        })
    
    # Coefficient of determination r²
    opts, idx = shuffle_options("% of variation explained by relationship", ["The slope", "The correlation", "The intercept"])
    questions.append({
        'text': "What does r² represent?",
        'opts': opts, 'idx': idx,
        'exp': "r² = proportion of variance explained."
    })
    
    # Calculate r²
    for r in [0.9, 0.8, 0.7, 0.6, 0.5]:
        r_sq = r * r
        ans = f"{r_sq:.2f}" if r_sq != int(r_sq) else f"{int(r_sq*100)}%"
        r_sq_pct = int(r_sq * 100)
        opts, idx = shuffle_options(f"{r_sq_pct}%", [f"{r_sq_pct + 10}%", f"{r_sq_pct - 10}%", f"{int(r * 100)}%"])
        questions.append({
            'text': f"If r = {r}, what is r² (as %)?",
            'opts': opts, 'idx': idx,
            'exp': f"r² = {r}² = {r_sq:.2f} = {r_sq_pct}%."
        })
        if len(questions) >= 32:
            break
    
    # Interpret r²
    for r_sq_pct in [81, 64, 49, 36]:
        opts, idx = shuffle_options(f"{r_sq_pct}% of variation explained", [f"{100-r_sq_pct}% explained", f"{r_sq_pct}% unexplained", "Cannot interpret"])
        questions.append({
            'text': f"r² = {r_sq_pct/100}. Interpretation?",
            'opts': opts, 'idx': idx,
            'exp': f"{r_sq_pct}% of y's variation explained by x."
        })
        if len(questions) >= 40:
            break
    
    # Sign of r
    opts, idx = shuffle_options("Positive", ["Negative", "Zero", "Cannot tell"])
    questions.append({
        'text': "If y increases as x increases, r is...",
        'opts': opts, 'idx': idx,
        'exp': "Both increase together = positive r."
    })
    
    opts, idx = shuffle_options("Negative", ["Positive", "Zero", "Cannot tell"])
    questions.append({
        'text': "If y decreases as x increases, r is...",
        'opts': opts, 'idx': idx,
        'exp': "One increases, other decreases = negative r."
    })
    
    # Fill remaining
    for r in [0.45, -0.72, 0.88, -0.33, 0.91, -0.85, 0.62, -0.55, 0.78, -0.68, 0.35, -0.42, 0.95, -0.92, 0.28, -0.25, 0.52, -0.48, 0.82, -0.76, 0.15, -0.18]:
        direction = "positive" if r > 0 else "negative"
        if abs(r) > 0.7:
            strength = "Strong"
        elif abs(r) > 0.4:
            strength = "Moderate"
        else:
            strength = "Weak"
        ans = f"{strength} {direction}"
        opts, idx = shuffle_options(ans, ["Strong positive", "Weak negative", "No correlation", "Moderate positive"])
        questions.append({
            'text': f"Describe correlation when r = {r}",
            'opts': opts, 'idx': idx,
            'exp': f"|r| = {abs(r):.2f}. {ans}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_9():
    """Line of Best Fit"""
    questions = []
    
    # Purpose
    opts, idx = shuffle_options("Summarize the trend in data", ["Connect all points", "Find outliers", "Calculate mean"])
    questions.append({
        'text': "What is the purpose of line of best fit?",
        'opts': opts, 'idx': idx,
        'exp': "Line of best fit shows overall trend."
    })
    
    # Property
    opts, idx = shuffle_options("Minimizes total distance from points", ["Passes through all points", "Passes through origin", "Is always horizontal"])
    questions.append({
        'text': "How is line of best fit determined?",
        'opts': opts, 'idx': idx,
        'exp': "Best fit minimizes squared distances from points."
    })
    
    # Must pass through
    opts, idx = shuffle_options("(x̄, ȳ) - the point of means", ["The origin (0, 0)", "All data points", "The highest point"])
    questions.append({
        'text': "The line of best fit always passes through...",
        'opts': opts, 'idx': idx,
        'exp': "Line passes through (mean of x, mean of y)."
    })
    
    # Equation form
    opts, idx = shuffle_options("y = mx + c", ["y = ax²", "y = a/x", "y = logx"])
    questions.append({
        'text': "What form is the line of best fit equation?",
        'opts': opts, 'idx': idx,
        'exp': "Linear: y = mx + c (slope-intercept form)."
    })
    
    # Slope meaning
    opts, idx = shuffle_options("Change in y for each unit increase in x", ["The y-intercept", "The correlation", "The mean"])
    questions.append({
        'text': "What does the slope (m) represent?",
        'opts': opts, 'idx': idx,
        'exp': "Slope = rate of change of y per unit x."
    })
    
    # Intercept meaning
    opts, idx = shuffle_options("Value of y when x = 0", ["Value of x when y = 0", "The slope", "The correlation"])
    questions.append({
        'text': "What does the y-intercept (c) represent?",
        'opts': opts, 'idx': idx,
        'exp': "Intercept = y value when x = 0."
    })
    
    # Use equation for prediction
    for m in [2, 3, 4, 5]:
        for c in [1, 5, 10]:
            for x in [3, 5, 7, 10]:
                y = m * x + c
                ans = str(y)
                opts, idx = shuffle_options(ans, [str(y + m), str(y - m), str(m * x)])
                questions.append({
                    'text': f"y = {m}x + {c}. Predict y when x = {x}.",
                    'opts': opts, 'idx': idx,
                    'exp': f"y = {m}({x}) + {c} = {y}."
                })
                if len(questions) >= 22:
                    break
            if len(questions) >= 22:
                break
        if len(questions) >= 22:
            break
    
    # Interpolation vs extrapolation
    opts, idx = shuffle_options("Predicting within data range", ["Predicting beyond data range", "Finding the slope", "Calculating correlation"])
    questions.append({
        'text': "What is interpolation?",
        'opts': opts, 'idx': idx,
        'exp': "Interpolation = prediction within known range."
    })
    
    opts, idx = shuffle_options("Predicting beyond data range", ["Predicting within data range", "Finding the slope", "Calculating correlation"])
    questions.append({
        'text': "What is extrapolation?",
        'opts': opts, 'idx': idx,
        'exp': "Extrapolation = prediction outside known range."
    })
    
    # Which is more reliable
    opts, idx = shuffle_options("Interpolation", ["Extrapolation", "Both equally reliable", "Neither"])
    questions.append({
        'text': "Which is generally more reliable?",
        'opts': opts, 'idx': idx,
        'exp': "Interpolation is safer - within known data."
    })
    
    # Interpret slope in context
    contexts = [
        ("height vs shoe size", "cm increase in height per shoe size"),
        ("study hours vs marks", "marks gained per hour studied"),
        ("temperature vs ice cream sales", "sales increase per degree"),
        ("age vs reaction time", "ms change per year of age"),
    ]
    for context, meaning in contexts:
        m = random.randint(2, 8)
        opts, idx = shuffle_options(f"{m} {meaning}", [f"{m} units", f"1/{m} {meaning}", f"{m}% increase"])
        questions.append({
            'text': f"For {context}, slope = {m}. Meaning?",
            'opts': opts, 'idx': idx,
            'exp': f"For each unit increase in x, y increases by {m}."
        })
        if len(questions) >= 35:
            break
    
    # Residual
    opts, idx = shuffle_options("Difference between actual and predicted y", ["The slope", "The intercept", "The correlation"])
    questions.append({
        'text': "What is a residual?",
        'opts': opts, 'idx': idx,
        'exp': "Residual = actual y - predicted y."
    })
    
    # Calculate residual
    for m, c in [(2, 3), (3, 1), (4, 2), (2, 5), (3, 4), (5, 2)]:
        for x, actual_y in [(2, 8), (3, 12), (5, 20), (4, 15), (6, 25), (1, 5)]:
            predicted = m * x + c
            residual = actual_y - predicted
            ans = str(residual)
            opts, idx = shuffle_options(ans, [str(residual + 1), str(predicted), str(actual_y)])
            questions.append({
                'text': f"y = {m}x + {c}. At x = {x}, actual y = {actual_y}. Residual?",
                'opts': opts, 'idx': idx,
                'exp': f"Predicted = {predicted}. Residual = {actual_y} - {predicted} = {residual}."
            })
            if len(questions) >= 50:
                break
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_10():
    """Hypothesis Testing Concepts"""
    questions = []
    
    # Null hypothesis
    opts, idx = shuffle_options("Statement of no effect/difference", ["Statement of significant effect", "The research question", "The conclusion"])
    questions.append({
        'text': "What is the null hypothesis (H₀)?",
        'opts': opts, 'idx': idx,
        'exp': "H₀ = no effect, no difference, status quo."
    })
    
    # Alternative hypothesis
    opts, idx = shuffle_options("Statement that there is an effect/difference", ["No effect exists", "The null hypothesis", "The sample mean"])
    questions.append({
        'text': "What is the alternative hypothesis (H₁)?",
        'opts': opts, 'idx': idx,
        'exp': "H₁ = there is an effect/difference."
    })
    
    # P-value definition
    opts, idx = shuffle_options("Probability of results if H₀ is true", ["Probability H₀ is true", "Probability H₁ is true", "The significance level"])
    questions.append({
        'text': "What does the p-value measure?",
        'opts': opts, 'idx': idx,
        'exp': "P-value = probability of data (or more extreme) if H₀ true."
    })
    
    # Small p-value means
    opts, idx = shuffle_options("Evidence against H₀", ["Evidence for H₀", "Test is invalid", "Sample too small"])
    questions.append({
        'text': "A small p-value indicates...",
        'opts': opts, 'idx': idx,
        'exp': "Small p = unlikely under H₀ = evidence against H₀."
    })
    
    # Significance level
    opts, idx = shuffle_options("Threshold for rejecting H₀", ["The p-value", "The sample size", "The effect size"])
    questions.append({
        'text': "What is the significance level (α)?",
        'opts': opts, 'idx': idx,
        'exp': "α = threshold below which we reject H₀."
    })
    
    # Common significance level
    opts, idx = shuffle_options("0.05 (5%)", ["0.50 (50%)", "0.95 (95%)", "1.00 (100%)"])
    questions.append({
        'text': "What is the most common significance level?",
        'opts': opts, 'idx': idx,
        'exp': "α = 0.05 (5%) is standard."
    })
    
    # Decision rule
    decisions = [
        (0.03, 0.05, "Reject H₀"),
        (0.08, 0.05, "Fail to reject H₀"),
        (0.001, 0.05, "Reject H₀"),
        (0.15, 0.05, "Fail to reject H₀"),
        (0.04, 0.05, "Reject H₀"),
        (0.06, 0.05, "Fail to reject H₀"),
        (0.01, 0.01, "Reject H₀"),
        (0.02, 0.01, "Fail to reject H₀"),
    ]
    for p, alpha, decision in decisions:
        opts, idx = shuffle_options(decision, ["Reject H₀", "Fail to reject H₀", "Accept H₁", "Test inconclusive"])
        questions.append({
            'text': f"p = {p}, α = {alpha}. Decision?",
            'opts': opts, 'idx': idx,
            'exp': f"p {'<' if p < alpha else '>'} α, so {decision.lower()}."
        })
        if len(questions) >= 22:
            break
    
    # Type I error
    opts, idx = shuffle_options("Rejecting H₀ when it's actually true", ["Failing to reject H₀ when it's false", "Correct decision", "Inconclusive result"])
    questions.append({
        'text': "What is a Type I error?",
        'opts': opts, 'idx': idx,
        'exp': "Type I = false positive (reject true H₀)."
    })
    
    # Type II error
    opts, idx = shuffle_options("Failing to reject H₀ when it's false", ["Rejecting H₀ when it's true", "Correct decision", "Inconclusive result"])
    questions.append({
        'text': "What is a Type II error?",
        'opts': opts, 'idx': idx,
        'exp': "Type II = false negative (fail to reject false H₀)."
    })
    
    # Statistically significant means
    opts, idx = shuffle_options("Unlikely to occur by chance alone", ["100% certain", "Practically important", "Large effect"])
    questions.append({
        'text': "'Statistically significant' means...",
        'opts': opts, 'idx': idx,
        'exp': "Significant = probably not due to chance."
    })
    
    # Write hypotheses for scenarios
    scenarios = [
        ("Test if new drug lowers blood pressure", "H₀: No difference, H₁: Drug lowers BP"),
        ("Check if coin is fair", "H₀: p = 0.5, H₁: p ≠ 0.5"),
        ("Test if training improves scores", "H₀: No improvement, H₁: Scores improve"),
    ]
    for scenario, hyp in scenarios:
        opts, idx = shuffle_options(hyp, ["H₀: Effect exists", "H₁: No effect", "Cannot form hypotheses"])
        questions.append({
            'text': f"Form hypotheses: {scenario}",
            'opts': opts, 'idx': idx,
            'exp': hyp
        })
    
    # Fill remaining
    for _ in range(50 - len(questions)):
        p = random.choice([0.001, 0.02, 0.04, 0.07, 0.12, 0.25])
        conclusion = "statistically significant" if p < 0.05 else "not statistically significant"
        opts, idx = shuffle_options(conclusion, ["statistically significant", "not statistically significant", "inconclusive", "invalid"])
        questions.append({
            'text': f"p = {p}. At 5% level, result is...",
            'opts': opts, 'idx': idx,
            'exp': f"p {'<' if p < 0.05 else '≥'} 0.05, so {conclusion}."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_11():
    """Margin of Error"""
    questions = []
    
    # Definition
    opts, idx = shuffle_options("Range of uncertainty in estimate", ["The exact error", "The sample size", "The population mean"])
    questions.append({
        'text': "What is margin of error?",
        'opts': opts, 'idx': idx,
        'exp': "MOE = how much estimate might differ from true value."
    })
    
    # Confidence interval
    opts, idx = shuffle_options("Range likely to contain true value", ["The exact value", "The sample mean only", "The margin of error"])
    questions.append({
        'text': "What is a confidence interval?",
        'opts': opts, 'idx': idx,
        'exp': "CI = range (estimate ± MOE) likely containing true value."
    })
    
    # 95% confidence means
    opts, idx = shuffle_options("95% of such intervals contain true value", ["95% probability true value in this interval", "Result is 95% accurate", "5% margin of error"])
    questions.append({
        'text': "What does 95% confidence mean?",
        'opts': opts, 'idx': idx,
        'exp': "If we repeated sampling, 95% of CIs would capture true value."
    })
    
    # Form of CI
    opts, idx = shuffle_options("Estimate ± margin of error", ["Estimate × margin of error", "Estimate / margin of error", "Margin of error - estimate"])
    questions.append({
        'text': "How is a confidence interval formed?",
        'opts': opts, 'idx': idx,
        'exp': "CI = point estimate ± margin of error."
    })
    
    # Calculate CI
    for est in [50, 65, 72, 80]:
        for moe in [3, 4, 5]:
            low, high = est - moe, est + moe
            ans = f"({low}, {high})"
            opts, idx = shuffle_options(ans, [f"({low-1}, {high+1})", f"({est}, {moe})", f"({high}, {low})"])
            questions.append({
                'text': f"Estimate = {est}%, MOE = {moe}%. Find 95% CI.",
                'opts': opts, 'idx': idx,
                'exp': f"CI = {est} ± {moe} = ({low}, {high})."
            })
            if len(questions) >= 18:
                break
        if len(questions) >= 18:
            break
    
    # Effect of sample size on MOE
    opts, idx = shuffle_options("MOE decreases", ["MOE increases", "MOE stays same", "Cannot tell"])
    questions.append({
        'text': "As sample size increases, margin of error...",
        'opts': opts, 'idx': idx,
        'exp': "Larger sample = more precision = smaller MOE."
    })
    
    # Effect of confidence level on MOE
    opts, idx = shuffle_options("MOE increases", ["MOE decreases", "MOE stays same", "Cannot tell"])
    questions.append({
        'text': "As confidence level increases (95% to 99%), MOE...",
        'opts': opts, 'idx': idx,
        'exp': "Higher confidence = wider interval = larger MOE."
    })
    
    # Interpret CI
    interpretations = [
        ("CI for mean height: (168, 172) cm", "True mean likely between 168 and 172 cm"),
        ("CI for proportion: (0.45, 0.55)", "True proportion likely between 45% and 55%"),
        ("CI for difference: (2, 8)", "True difference likely between 2 and 8"),
    ]
    for ci, interp in interpretations:
        opts, idx = shuffle_options(interp, ["Cannot interpret", "Mean is exactly in middle", "Result is certain"])
        questions.append({
            'text': f"Interpret: {ci}",
            'opts': opts, 'idx': idx,
            'exp': interp
        })
    
    # Find MOE from CI
    for low, high in [(42, 58), (65, 75), (30, 40), (82, 92), (55, 65), (38, 48), (70, 80), (25, 35), (60, 72), (45, 51)]:
        moe = (high - low) // 2
        opts, idx = shuffle_options(str(moe), [str(moe + 1), str(moe - 1) if moe > 1 else "1", str(high - low)])
        questions.append({
            'text': f"CI = ({low}, {high}). What is the MOE?",
            'opts': opts, 'idx': idx,
            'exp': f"MOE = (upper - lower)/2 = ({high} - {low})/2 = {moe}."
        })
        if len(questions) >= 35:
            break
    
    # Poll results
    polls = [
        (48, 3, "between 45% and 51%"),
        (52, 4, "between 48% and 56%"),
        (35, 2, "between 33% and 37%"),
        (60, 5, "between 55% and 65%"),
        (45, 4, "between 41% and 49%"),
        (72, 3, "between 69% and 75%"),
    ]
    for result, moe, answer in polls:
        opts, idx = shuffle_options(answer, [f"exactly {result}%", f"at least {result}%", "cannot determine"])
        questions.append({
            'text': f"Poll: {result}% ± {moe}%. True support is likely...",
            'opts': opts, 'idx': idx,
            'exp': f"{result} ± {moe} = {answer}."
        })
    
    # Does CI contain value?
    for low, high, test in [(45, 55, 50), (60, 70, 75), (30, 40, 35), (48, 52, 45), (55, 65, 60), (40, 50, 55), (35, 45, 38), (70, 80, 82), (25, 35, 30), (62, 68, 70), (42, 52, 47), (58, 66, 62), (72, 78, 75)]:
        contains = "Yes" if low <= test <= high else "No"
        opts, idx = shuffle_options(contains, ["Yes", "No", "Cannot tell", "Maybe"])
        questions.append({
            'text': f"CI = ({low}, {high}). Does it contain {test}?",
            'opts': opts, 'idx': idx,
            'exp': f"{test} is {'within' if contains == 'Yes' else 'outside'} ({low}, {high})."
        })
        if len(questions) >= 50:
            break
    
    return questions[:50]

def generate_level_12():
    """SEC Exam Style"""
    questions = []
    
    # Multi-concept sampling
    opts, idx = shuffle_options("Stratified", ["Simple random", "Convenience", "Systematic"])
    questions.append({
        'text': "Survey needs equal representation from each year group. Best method?",
        'opts': opts, 'idx': idx,
        'exp': "Stratified ensures representation from each stratum."
    })
    
    # Normal distribution application
    for mu, sigma in [(100, 15), (50, 10)]:
        low, high = mu - sigma, mu + sigma
        opts, idx = shuffle_options("68%", ["95%", "50%", "99.7%"])
        questions.append({
            'text': f"Scores ~ N({mu}, {sigma}²). % between {low} and {high}?",
            'opts': opts, 'idx': idx,
            'exp': f"{low} to {high} is μ ± σ = 68%."
        })
    
    # Z-score calculation
    for mu, sigma, x in [(170, 10, 185), (100, 15, 130), (50, 5, 60)]:
        z = (x - mu) // sigma
        opts, idx = shuffle_options(str(z), [str(z + 1), str(z - 1), str(x - mu)])
        questions.append({
            'text': f"μ = {mu}, σ = {sigma}. Z-score for {x}?",
            'opts': opts, 'idx': idx,
            'exp': f"z = ({x} - {mu})/{sigma} = {z}."
        })
    
    # Correlation interpretation
    opts, idx = shuffle_options("Strong negative", ["Strong positive", "Weak negative", "No correlation"])
    questions.append({
        'text': "r = -0.85. Describe the correlation.",
        'opts': opts, 'idx': idx,
        'exp': "|r| = 0.85 > 0.7 = strong; negative sign."
    })
    
    # Line of best fit prediction
    for m, c in [(3, 5), (2, 10), (4, 2)]:
        for x in [6, 8, 10]:
            y = m * x + c
            opts, idx = shuffle_options(str(y), [str(y + m), str(y - m), str(m * x)])
            questions.append({
                'text': f"Line of best fit: y = {m}x + {c}. Predict y when x = {x}.",
                'opts': opts, 'idx': idx,
                'exp': f"y = {m}({x}) + {c} = {y}."
            })
            if len(questions) >= 18:
                break
        if len(questions) >= 18:
            break
    
    # Hypothesis testing decision
    for p in [0.02, 0.08, 0.03, 0.12]:
        decision = "Reject H₀" if p < 0.05 else "Fail to reject H₀"
        opts, idx = shuffle_options(decision, ["Reject H₀", "Fail to reject H₀", "Accept H₀", "Inconclusive"])
        questions.append({
            'text': f"p-value = {p}. At α = 0.05, decision?",
            'opts': opts, 'idx': idx,
            'exp': f"p = {p} {'<' if p < 0.05 else '>'} 0.05, so {decision.lower()}."
        })
        if len(questions) >= 26:
            break
    
    # Confidence interval
    for est, moe in [(55, 4), (48, 3), (72, 5)]:
        low, high = est - moe, est + moe
        ans = f"({low}%, {high}%)"
        opts, idx = shuffle_options(ans, [f"({est}%, {moe}%)", f"({low}%, {moe}%)", f"({moe}%, {high}%)"])
        questions.append({
            'text': f"Poll: {est}% ± {moe}%. 95% confidence interval?",
            'opts': opts, 'idx': idx,
            'exp': f"{est} ± {moe} = ({low}%, {high}%)."
        })
    
    # Bias identification
    biased_scenarios = [
        ("Online survey about internet habits", "Selection bias"),
        ("Leading question about product quality", "Response bias"),
        ("Survey with 60% non-response", "Non-response bias"),
    ]
    for scenario, bias in biased_scenarios:
        opts, idx = shuffle_options(bias, ["Selection bias", "Response bias", "Non-response bias", "No bias"])
        questions.append({
            'text': f"Identify bias: {scenario}",
            'opts': opts, 'idx': idx,
            'exp': f"This is {bias}."
        })
    
    # r² interpretation
    for r in [0.9, 0.8, 0.7]:
        r_sq = int(r * r * 100)
        opts, idx = shuffle_options(f"{r_sq}%", [f"{int(r*100)}%", f"{100-r_sq}%", f"{r_sq//2}%"])
        questions.append({
            'text': f"r = {r}. What % of variation is explained?",
            'opts': opts, 'idx': idx,
            'exp': f"r² = {r}² = {r*r:.2f} = {r_sq}%."
        })
    
    # Empirical rule
    opts, idx = shuffle_options("2.5%", ["5%", "16%", "0.15%"])
    questions.append({
        'text': "% of data more than 2 SDs ABOVE the mean?",
        'opts': opts, 'idx': idx,
        'exp': "5% outside ±2σ, so 2.5% above."
    })
    
    # Sample vs population
    opts, idx = shuffle_options("All students in the school", ["The 50 surveyed", "The questionnaire", "The results"])
    questions.append({
        'text': "50 students surveyed about canteen. What is the population?",
        'opts': opts, 'idx': idx,
        'exp': "Population = all students (group of interest)."
    })
    
    # Fill to 50
    for i in range(50 - len(questions)):
        opts, idx = shuffle_options("Correlation does not imply causation", ["Correlation proves causation", "r² proves causation", "Strong r means causation"])
        questions.append({
            'text': "Why can't we conclude causation from correlation?",
            'opts': opts, 'idx': idx,
            'exp': "Third variables or coincidence may explain relationship."
        })
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
        "-- LC OL Statistics (Inferential) - 600 Questions",
        f"-- Total: {len(questions)}",
        "",
        "-- Create topic",
        f"INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)",
        f"VALUES ('{TOPIC_ID}', 'Statistics (Inferential)', {STRAND_ID}, '📊', 11, 1);",
        "",
        "-- Clear existing",
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
    print("LC OL Statistics (Inferential) - 600 Questions Generator")
    print("="*60 + "\n")
    
    questions = generate_all()
    print(f"\nTotal: {len(questions)}\n")
    
    sql = generate_sql(questions)
    with open('lc_ol_statistics_inf_600.sql', 'w') as f:
        f.write(sql)
    
    print(f"Saved: lc_ol_statistics_inf_600.sql ({len(sql):,} chars)")
