#!/usr/bin/env python3
"""
LC Higher Level - Statistics Question Generator
Version: 1.0
Date: 2025-12-15

Generates 600 questions (50 per level x 12 levels) for LC HL Statistics
"""

import random
from math import sqrt

TOPIC = 'lc_hl_statistics'
MODE = 'lc_hl'

LEVEL_TITLES = [
    'Data Types & Collection',
    'Frequency Tables',
    'Measures of Centre',
    'Measures of Spread',
    'Standard Deviation',
    'Histograms & Cumulative Frequency',
    'Scatter Plots & Correlation',
    'Line of Best Fit',
    'Hypothesis Testing Basics',
    'Confidence Intervals',
    'Statistical Inference',
    'Mastery Challenge'
]

def make_unique_options(correct, distractors):
    """Create 4 unique options with correct answer randomly placed"""
    correct_str = str(correct)
    unique_wrong = []
    for d in distractors:
        d_str = str(d)
        if d_str != correct_str and d_str not in unique_wrong:
            unique_wrong.append(d_str)
    while len(unique_wrong) < 3:
        unique_wrong.append(f"Cannot determine")
    options = [correct_str] + unique_wrong[:3]
    random.shuffle(options)
    return options, options.index(correct_str)

def generate_level_1():
    """Level 1: Data Types & Collection"""
    questions = []
    
    # Type 1: Classify data type
    data_types = [
        ("The number of students in a class", "Discrete numerical", ["Continuous numerical", "Categorical nominal", "Categorical ordinal"]),
        ("A person's height in centimetres", "Continuous numerical", ["Discrete numerical", "Categorical nominal", "Categorical ordinal"]),
        ("Favourite colour", "Categorical nominal", ["Categorical ordinal", "Discrete numerical", "Continuous numerical"]),
        ("Rating on a scale of 1-5", "Categorical ordinal", ["Categorical nominal", "Discrete numerical", "Continuous numerical"]),
        ("Temperature in degrees Celsius", "Continuous numerical", ["Discrete numerical", "Categorical ordinal", "Categorical nominal"]),
        ("Number of goals scored", "Discrete numerical", ["Continuous numerical", "Categorical nominal", "Categorical ordinal"]),
        ("Blood type (A, B, AB, O)", "Categorical nominal", ["Categorical ordinal", "Discrete numerical", "Continuous numerical"]),
        ("Education level (Primary, Secondary, Third Level)", "Categorical ordinal", ["Categorical nominal", "Discrete numerical", "Continuous numerical"]),
        ("Weight in kilograms", "Continuous numerical", ["Discrete numerical", "Categorical ordinal", "Categorical nominal"]),
        ("Number of siblings", "Discrete numerical", ["Continuous numerical", "Categorical nominal", "Categorical ordinal"]),
        ("Time taken to complete a race", "Continuous numerical", ["Discrete numerical", "Categorical ordinal", "Categorical nominal"]),
        ("Shoe size (35, 36, 37, ...)", "Discrete numerical", ["Continuous numerical", "Categorical ordinal", "Categorical nominal"]),
    ]
    
    for i in range(12):
        data, correct, distractors = data_types[i % len(data_types)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Classify this data type: {data}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"'{data}' is {correct} data.",
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Sampling methods
    sampling_methods = [
        ("Every 10th person on a list is selected", "Systematic sampling", ["Simple random sampling", "Stratified sampling", "Cluster sampling"]),
        ("Names are drawn from a hat", "Simple random sampling", ["Systematic sampling", "Stratified sampling", "Convenience sampling"]),
        ("Students are sampled proportionally from each year group", "Stratified sampling", ["Simple random sampling", "Cluster sampling", "Systematic sampling"]),
        ("All students in randomly selected classes are surveyed", "Cluster sampling", ["Stratified sampling", "Simple random sampling", "Systematic sampling"]),
        ("Surveying people walking past a shop", "Convenience sampling", ["Simple random sampling", "Systematic sampling", "Stratified sampling"]),
        ("Using a random number generator to select participants", "Simple random sampling", ["Systematic sampling", "Convenience sampling", "Cluster sampling"]),
        ("Selecting every 5th item on a production line", "Systematic sampling", ["Cluster sampling", "Simple random sampling", "Stratified sampling"]),
        ("Sampling equal numbers from each age group", "Stratified sampling", ["Cluster sampling", "Systematic sampling", "Simple random sampling"]),
    ]
    
    for i in range(8):
        desc, correct, distractors = sampling_methods[i]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Identify the sampling method: {desc}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"This describes {correct}.",
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Population vs Sample
    for i in range(10):
        scenarios = [
            ("All students in Ireland", "Population", ["Sample", "Census", "Survey"]),
            ("100 voters selected for a poll", "Sample", ["Population", "Census", "Parameter"]),
            ("Every registered voter in a constituency", "Population", ["Sample", "Statistic", "Survey"]),
            ("50 products tested from a factory", "Sample", ["Population", "Census", "Parameter"]),
            ("All employees of a company", "Population", ["Sample", "Statistic", "Survey"]),
            ("20 patients selected for a clinical trial", "Sample", ["Population", "Census", "Parameter"]),
        ]
        desc, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Is this a population or a sample? {desc}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"'{desc}' is a {correct.lower()}.",
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 4: Bias identification
    for i in range(10):
        scenarios = [
            ("A survey about exercise conducted at a gym", "Yes, sampling bias (unrepresentative location)", ["No bias", "Response bias", "Measurement bias"]),
            ("A questionnaire asking 'Don't you agree that...?'", "Yes, leading question bias", ["No bias", "Sampling bias", "Non-response bias"]),
            ("Only 20% of surveys were returned", "Yes, non-response bias", ["No bias", "Sampling bias", "Leading question bias"]),
            ("Random selection of voters from electoral register", "No bias (proper random sampling)", ["Sampling bias", "Response bias", "Non-response bias"]),
            ("Online survey about internet usage", "Yes, sampling bias (excludes non-internet users)", ["No bias", "Response bias", "Measurement bias"]),
        ]
        desc, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Is there bias in this scenario? {desc}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{correct}",
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 5: Primary vs Secondary data
    for i in range(10):
        scenarios = [
            ("Data collected through your own survey", "Primary data", ["Secondary data", "Tertiary data", "Sample data"]),
            ("Using census data from the CSO", "Secondary data", ["Primary data", "Tertiary data", "Population data"]),
            ("Conducting interviews for your research", "Primary data", ["Secondary data", "Tertiary data", "Sample data"]),
            ("Data from a published research paper", "Secondary data", ["Primary data", "Tertiary data", "Raw data"]),
            ("Observations recorded during an experiment", "Primary data", ["Secondary data", "Tertiary data", "Derived data"]),
        ]
        desc, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Classify this data source: {desc}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"This is {correct.lower()} because it was {'collected by the researcher' if 'Primary' in correct else 'collected by someone else'}.",
            'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    return questions

def generate_level_2():
    """Level 2: Frequency Tables"""
    questions = []
    
    # Type 1: Reading frequency tables
    for i in range(10):
        values = [random.randint(1, 5) for _ in range(5)]
        freqs = [random.randint(2, 8) for _ in range(5)]
        total = sum(freqs)
        
        target_idx = random.randint(0, 4)
        target_val = values[target_idx]
        target_freq = freqs[target_idx]
        
        correct = str(target_freq)
        distractors = [str(target_freq + 1), str(target_freq - 1) if target_freq > 1 else "1", str(total)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        table = ", ".join([f"({v}, {f})" for v, f in zip(values, freqs)])
        questions.append({
            'question_text': f"From the (value, frequency) pairs: {table}. What is the frequency of value {target_val}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The frequency of {target_val} is {target_freq}.",
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Total frequency
    for i in range(10):
        freqs = [random.randint(3, 10) for _ in range(4)]
        total = sum(freqs)
        
        correct = str(total)
        distractors = [str(total + 2), str(total - 2), str(len(freqs))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        freq_str = " + ".join(map(str, freqs))
        questions.append({
            'question_text': f"A frequency table has frequencies: {', '.join(map(str, freqs))}. What is the total frequency (n)?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Total n = {freq_str} = {total}",
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Relative frequency
    for i in range(10):
        freq = random.randint(5, 20)
        total = random.randint(40, 100)
        
        rel_freq = round(freq / total, 2)
        correct = str(rel_freq)
        distractors = [str(round(total / freq, 2)), str(round(rel_freq + 0.1, 2)), str(round(freq / 100, 2))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"If a value has frequency {freq} out of {total} observations, what is its relative frequency?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Relative frequency = {freq}/{total} = {correct}",
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 4: Class intervals
    for i in range(10):
        lower = random.choice([0, 10, 20, 50, 100])
        upper = lower + random.choice([10, 20, 25, 50])
        width = upper - lower
        
        correct = str(width)
        distractors = [str(width + 5), str(width - 5) if width > 5 else "5", str(upper)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"What is the class width of the interval {lower} - {upper}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Class width = {upper} - {lower} = {correct}",
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 5: Midpoint of class interval
    for i in range(10):
        lower = random.choice([0, 10, 20, 30, 40])
        upper = lower + random.choice([10, 20])
        midpoint = (lower + upper) / 2
        
        correct = str(int(midpoint)) if midpoint == int(midpoint) else str(midpoint)
        distractors = [str(int(midpoint) + 5), str(int(midpoint) - 5), str(upper - lower)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"What is the midpoint of the class interval {lower} - {upper}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Midpoint = ({lower} + {upper})/2 = {correct}",
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 6: Cumulative frequency
    for i in range(10):
        freqs = [random.randint(3, 8) for _ in range(4)]
        target_idx = random.randint(1, 3)
        cum_freq = sum(freqs[:target_idx + 1])
        
        correct = str(cum_freq)
        distractors = [str(freqs[target_idx]), str(sum(freqs)), str(cum_freq + freqs[0])]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Frequencies are {', '.join(map(str, freqs))}. What is the cumulative frequency after class {target_idx + 1}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Cumulative frequency = {' + '.join(map(str, freqs[:target_idx+1]))} = {correct}",
            'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    return questions

def generate_level_3():
    """Level 3: Measures of Centre"""
    questions = []
    
    # Type 1: Mean calculation
    for i in range(10):
        n = random.randint(4, 6)
        data = [random.randint(2, 15) for _ in range(n)]
        mean = sum(data) / n
        
        correct = str(round(mean, 1))
        distractors = [str(round(mean + 1, 1)), str(round(mean - 1, 1)), str(sum(data))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Find the mean of: {', '.join(map(str, data))}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Mean = ({' + '.join(map(str, data))})/{n} = {sum(data)}/{n} = {correct}",
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Median calculation (odd)
    for i in range(8):
        n = random.choice([5, 7])
        data = sorted([random.randint(1, 20) for _ in range(n)])
        median = data[n // 2]
        
        correct = str(median)
        distractors = [str(median + 1), str(median - 1), str(round(sum(data) / n, 1))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Find the median of: {', '.join(map(str, data))}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Data is sorted. Median is the middle value ({n//2 + 1}th value) = {correct}",
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Median calculation (even)
    for i in range(8):
        n = random.choice([4, 6])
        data = sorted([random.randint(1, 20) for _ in range(n)])
        median = (data[n // 2 - 1] + data[n // 2]) / 2
        
        correct = str(median) if median == int(median) else str(round(median, 1))
        distractors = [str(data[n // 2]), str(data[n // 2 - 1]), str(round(sum(data) / n, 1))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Find the median of: {', '.join(map(str, data))}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Even count. Median = ({data[n//2-1]} + {data[n//2]})/2 = {correct}",
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 4: Mode calculation
    for i in range(8):
        base = [random.randint(1, 10) for _ in range(4)]
        mode = random.choice(base)
        data = base + [mode, mode]  # Ensure mode appears more
        random.shuffle(data)
        
        correct = str(mode)
        other_vals = [v for v in set(data) if v != mode]
        distractors = [str(v) for v in other_vals[:3]] if len(other_vals) >= 3 else [str(v) for v in other_vals] + ["No mode"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Find the mode of: {', '.join(map(str, data))}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The mode is the most frequent value. {mode} appears most often.",
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 5: Mean from frequency table
    for i in range(8):
        values = [1, 2, 3, 4, 5]
        freqs = [random.randint(1, 5) for _ in range(5)]
        total = sum(freqs)
        fx_sum = sum(v * f for v, f in zip(values, freqs))
        mean = round(fx_sum / total, 2)
        
        correct = str(mean)
        distractors = [str(round(mean + 0.5, 2)), str(round(mean - 0.5, 2)), str(round(sum(values) / 5, 2))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        table = ", ".join([f"({v}: {f})" for v, f in zip(values, freqs)])
        questions.append({
            'question_text': f"Find the mean from this frequency table (value: frequency): {table}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Mean = Σfx/Σf = {fx_sum}/{total} = {correct}",
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 6: Choosing appropriate average
    for i in range(8):
        scenarios = [
            ("Salaries in a company with one very high earner", "Median", ["Mean", "Mode", "Range"]),
            ("Shoe sizes sold in a shop", "Mode", ["Mean", "Median", "Range"]),
            ("Exam scores with no outliers", "Mean", ["Mode", "Median", "Range"]),
            ("House prices in an area with mansions", "Median", ["Mean", "Mode", "Range"]),
            ("Most popular car colour", "Mode", ["Mean", "Median", "Range"]),
            ("Symmetrically distributed heights", "Mean", ["Mode", "Range", "Interquartile range"]),
        ]
        desc, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Which average is most appropriate for: {desc}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The {correct.lower()} is most appropriate because it's {'not affected by outliers' if correct == 'Median' else 'measures most common value' if correct == 'Mode' else 'uses all values when distribution is symmetric'}.",
            'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    return questions

def generate_level_4():
    """Level 4: Measures of Spread"""
    questions = []
    
    # Type 1: Range calculation
    for i in range(10):
        data = [random.randint(5, 50) for _ in range(5)]
        range_val = max(data) - min(data)
        
        correct = str(range_val)
        distractors = [str(max(data)), str(min(data)), str(range_val + 5)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Find the range of: {', '.join(map(str, data))}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Range = Max - Min = {max(data)} - {min(data)} = {correct}",
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 2: Quartiles - Q1
    for i in range(8):
        data = sorted([random.randint(10, 50) for _ in range(8)])
        # For n=8, Q1 is average of 2nd and 3rd values
        q1 = (data[1] + data[2]) / 2
        
        correct = str(q1) if q1 == int(q1) else str(round(q1, 1))
        distractors = [str(data[1]), str(data[2]), str(data[0])]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Find Q1 (lower quartile) for: {', '.join(map(str, data))}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"For n=8, Q1 is the average of the 2nd and 3rd values: ({data[1]} + {data[2]})/2 = {correct}",
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 3: Quartiles - Q3
    for i in range(8):
        data = sorted([random.randint(10, 50) for _ in range(8)])
        # For n=8, Q3 is average of 6th and 7th values
        q3 = (data[5] + data[6]) / 2
        
        correct = str(q3) if q3 == int(q3) else str(round(q3, 1))
        distractors = [str(data[5]), str(data[6]), str(data[7])]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Find Q3 (upper quartile) for: {', '.join(map(str, data))}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"For n=8, Q3 is the average of the 6th and 7th values: ({data[5]} + {data[6]})/2 = {correct}",
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 4: Interquartile Range
    for i in range(10):
        q1 = random.randint(20, 35)
        q3 = q1 + random.randint(10, 25)
        iqr = q3 - q1
        
        correct = str(iqr)
        distractors = [str(q3), str(q1), str(q3 + q1)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"If Q1 = {q1} and Q3 = {q3}, find the Interquartile Range (IQR).",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"IQR = Q3 - Q1 = {q3} - {q1} = {correct}",
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 5: Identifying outliers
    for i in range(8):
        q1 = 20
        q3 = 40
        iqr = 20
        lower_fence = q1 - 1.5 * iqr
        upper_fence = q3 + 1.5 * iqr
        
        test_val = random.choice([random.randint(-15, -5), random.randint(65, 80), random.randint(25, 35)])
        is_outlier = test_val < lower_fence or test_val > upper_fence
        
        correct = "Yes, it is an outlier" if is_outlier else "No, it is not an outlier"
        distractors = ["No, it is not an outlier" if is_outlier else "Yes, it is an outlier", 
                       "Cannot determine", "Need more data"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Given Q1 = {q1}, Q3 = {q3}. Is {test_val} an outlier? (Use 1.5 × IQR rule)",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"IQR = {iqr}. Fences: [{lower_fence}, {upper_fence}]. {test_val} is {'outside' if is_outlier else 'inside'} this range.",
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 6: Effect of outliers on measures
    for i in range(6):
        scenarios = [
            ("Adding a very high value affects which measure most?", "Mean", ["Median", "Mode", "IQR"]),
            ("Which measure of spread is resistant to outliers?", "IQR", ["Range", "Standard deviation", "Variance"]),
            ("Which average is most affected by outliers?", "Mean", ["Median", "Mode", "Both median and mode"]),
            ("Which is a better measure of spread when outliers exist?", "IQR", ["Range", "Mean deviation", "Total spread"]),
        ]
        question, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The {correct} is {'most affected by' if 'affected' in question else 'resistant to'} outliers.",
            'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    return questions

def generate_level_5():
    """Level 5: Standard Deviation"""
    questions = []
    
    # Type 1: Calculate variance from deviations
    for i in range(8):
        data = [random.randint(1, 10) for _ in range(4)]
        mean = sum(data) / 4
        sq_devs = [(x - mean) ** 2 for x in data]
        variance = sum(sq_devs) / 4
        
        correct = str(round(variance, 2))
        distractors = [str(round(sqrt(variance), 2)), str(round(variance * 2, 2)), str(round(sum(sq_devs), 2))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Find the population variance for: {', '.join(map(str, data))} (Mean = {mean})",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Variance = Σ(x-μ)²/n = {round(sum(sq_devs), 2)}/4 = {correct}",
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 2: Calculate standard deviation
    for i in range(8):
        variance = random.choice([4, 9, 16, 25, 36])
        sd = sqrt(variance)
        
        correct = str(int(sd))
        distractors = [str(variance), str(int(sd) + 1), str(int(sd * 2))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"If the variance is {variance}, what is the standard deviation?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Standard deviation = √variance = √{variance} = {correct}",
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 3: Using the formula Var(X) = E(X²) - [E(X)]²
    for i in range(8):
        mean = random.randint(5, 10)
        mean_sq = mean ** 2 + random.randint(2, 10)
        variance = mean_sq - mean ** 2
        
        correct = str(variance)
        distractors = [str(mean_sq), str(mean ** 2), str(mean_sq + mean ** 2)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"If the mean is {mean} and the mean of squares is {mean_sq}, find the variance.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Var = E(X²) - [E(X)]² = {mean_sq} - {mean}² = {mean_sq} - {mean**2} = {correct}",
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 4: Effect of linear transformation on SD
    for i in range(8):
        sd = random.randint(3, 8)
        a = random.randint(2, 5)
        b = random.randint(1, 10)
        
        new_sd = a * sd
        correct = str(new_sd)
        distractors = [str(a * sd + b), str(sd), str(sd + b)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"If σ = {sd}, what is the standard deviation of {a}X + {b}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"SD({a}X + {b}) = |{a}| × σ = {a} × {sd} = {correct}. Adding {b} doesn't affect spread.",
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 5: Sample vs Population standard deviation
    for i in range(8):
        n = random.randint(5, 10)
        sum_sq_dev = random.randint(50, 200)
        
        pop_var = sum_sq_dev / n
        sample_var = sum_sq_dev / (n - 1)
        
        correct = str(round(sample_var, 2))
        distractors = [str(round(pop_var, 2)), str(round(sqrt(sample_var), 2)), str(round(sum_sq_dev, 2))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"For a sample of size {n} with Σ(x-x̄)² = {sum_sq_dev}, find the sample variance.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Sample variance uses n-1: s² = {sum_sq_dev}/{n-1} = {correct}",
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 6: Interpreting standard deviation
    for i in range(10):
        scenarios = [
            ("Two datasets have the same mean but different standard deviations. What does a larger SD indicate?", "Greater spread/variability", ["Higher mean", "More data points", "Smaller range"]),
            ("If SD = 0, what does this tell us about the data?", "All values are identical", ["Mean equals median", "Data is normally distributed", "There are no outliers"]),
            ("A dataset has SD = 5. After multiplying all values by 2, the new SD is:", "10", ["5", "25", "7"]),
            ("Adding 10 to every value in a dataset will:", "Not change the SD", ["Increase SD by 10", "Double the SD", "Decrease the SD"]),
        ]
        question, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The answer is: {correct}",
            'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    return questions

def generate_level_6():
    """Level 6: Histograms & Cumulative Frequency"""
    questions = []
    
    # Type 1: Reading histogram bars
    for i in range(8):
        class_width = random.choice([5, 10])
        start = random.choice([0, 10, 20])
        freqs = [random.randint(5, 20) for _ in range(4)]
        
        target_idx = random.randint(0, 3)
        target_class = f"{start + target_idx * class_width}-{start + (target_idx + 1) * class_width}"
        
        correct = str(freqs[target_idx])
        distractors = [str(freqs[(target_idx + 1) % 4]), str(sum(freqs)), str(freqs[target_idx] + 2)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        class_str = ", ".join([f"{start + i*class_width}-{start + (i+1)*class_width}: {f}" for i, f in enumerate(freqs)])
        questions.append({
            'question_text': f"A histogram shows: {class_str}. What is the frequency for the class {target_class}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The frequency for class {target_class} is {correct}.",
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 2: Cumulative frequency table
    for i in range(8):
        freqs = [random.randint(5, 15) for _ in range(4)]
        cum_freqs = []
        total = 0
        for f in freqs:
            total += f
            cum_freqs.append(total)
        
        target_idx = random.randint(1, 3)
        correct = str(cum_freqs[target_idx])
        distractors = [str(freqs[target_idx]), str(cum_freqs[-1]), str(cum_freqs[target_idx - 1])]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Frequencies are {', '.join(map(str, freqs))}. What is the cumulative frequency after class {target_idx + 1}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Cumulative frequency = {' + '.join(map(str, freqs[:target_idx+1]))} = {correct}",
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 3: Finding median from cumulative frequency
    for i in range(8):
        n = random.choice([40, 50, 60, 80, 100])
        median_pos = n / 2
        
        correct = str(median_pos)
        distractors = [str(n), str(median_pos + 0.5), str(n / 4)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"There are {n} data points. At what cumulative frequency position is the median?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Median position = n/2 = {n}/2 = {correct}",
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 4: Quartile positions from cumulative frequency
    for i in range(8):
        n = random.choice([40, 60, 80, 100])
        quartile = random.choice([("Q1", 1), ("Q3", 3)])
        q_name, q_num = quartile
        position = n * q_num / 4
        
        correct = str(position)
        distractors = [str(n / 2), str(n / 4), str(n * (4 - q_num) / 4)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"For {n} data points, at what cumulative frequency position is {q_name}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{q_name} position = {q_num}n/4 = {q_num}×{n}/4 = {correct}",
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 5: Frequency density
    for i in range(8):
        freq = random.randint(10, 40)
        width = random.choice([5, 10, 20])
        density = freq / width
        
        correct = str(round(density, 1))
        distractors = [str(freq), str(width), str(freq * width)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"A class has frequency {freq} and width {width}. What is the frequency density?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Frequency density = frequency/width = {freq}/{width} = {correct}",
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 6: Reading percentiles from cumulative frequency
    for i in range(10):
        n = 100
        percentile = random.choice([25, 50, 75, 90])
        position = n * percentile / 100
        
        correct = str(int(position))
        distractors = [str(percentile), str(n - int(position)), str(int(position / 2))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"For {n} data points, at what position is the {percentile}th percentile?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{percentile}th percentile position = {percentile}% of {n} = {correct}",
            'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    return questions

def generate_level_7():
    """Level 7: Scatter Plots & Correlation"""
    questions = []
    
    # Type 1: Identify correlation type
    for i in range(12):
        scenarios = [
            ("As height increases, weight tends to increase", "Positive correlation", ["Negative correlation", "No correlation", "Perfect correlation"]),
            ("As temperature increases, heating costs decrease", "Negative correlation", ["Positive correlation", "No correlation", "Perfect correlation"]),
            ("Shoe size and IQ show no pattern", "No correlation", ["Positive correlation", "Negative correlation", "Weak correlation"]),
            ("More study hours leads to higher exam scores", "Positive correlation", ["Negative correlation", "No correlation", "Perfect correlation"]),
            ("Higher car age corresponds to lower value", "Negative correlation", ["Positive correlation", "No correlation", "Perfect correlation"]),
            ("Hair colour and maths ability", "No correlation", ["Positive correlation", "Negative correlation", "Weak positive correlation"]),
        ]
        desc, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"What type of correlation? {desc}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"This shows {correct.lower()}.",
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Correlation coefficient interpretation
    for i in range(10):
        r = random.choice([0.95, 0.75, 0.35, 0.05, -0.45, -0.85, -0.98])
        
        if abs(r) > 0.9:
            strength = "Strong"
        elif abs(r) > 0.6:
            strength = "Moderate"
        elif abs(r) > 0.3:
            strength = "Weak"
        else:
            strength = "Very weak/none"
        
        direction = "positive" if r > 0 else "negative" if r < 0 else ""
        correct = f"{strength} {direction}".strip()
        
        distractors = [f"{'Weak' if 'Strong' in strength else 'Strong'} {direction}",
                       f"{strength} {'negative' if direction == 'positive' else 'positive'}",
                       "No correlation"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Describe the correlation for r = {r}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"r = {r} indicates {correct.lower()} correlation.",
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Properties of correlation coefficient
    for i in range(8):
        scenarios = [
            ("The correlation coefficient r must be between:", "-1 and 1", ["-∞ and ∞", "0 and 1", "-100 and 100"]),
            ("If r = 1, this indicates:", "Perfect positive correlation", ["Perfect negative correlation", "No correlation", "Weak correlation"]),
            ("If r = -1, this indicates:", "Perfect negative correlation", ["Perfect positive correlation", "No correlation", "Strong positive correlation"]),
            ("If r = 0, this indicates:", "No linear correlation", ["Perfect correlation", "Negative correlation", "Positive correlation"]),
            ("Correlation measures:", "Strength and direction of linear relationship", ["Causation", "The slope of the line", "The y-intercept"]),
            ("Does correlation imply causation?", "No", ["Yes", "Sometimes", "Only for r > 0.9"]),
        ]
        question, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The answer is: {correct}",
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 4: Coefficient of determination
    for i in range(10):
        r = random.choice([0.8, 0.9, 0.7, 0.6, -0.8, -0.9])
        r_sq = round(r ** 2, 2)
        percentage = int(r_sq * 100)
        
        correct = f"{percentage}%"
        distractors = [f"{int(abs(r) * 100)}%", f"{100 - percentage}%", f"{int(r_sq * 50)}%"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"If r = {r}, what percentage of variation in y is explained by x?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"r² = {r}² = {r_sq}, so {percentage}% of variation is explained.",
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 5: Outliers and correlation
    for i in range(10):
        scenarios = [
            ("An outlier can:", "Significantly affect r", ["Never affect r", "Only increase r", "Only decrease r"]),
            ("A single extreme point can:", "Make correlation appear stronger or weaker", ["Only strengthen correlation", "Only weaken correlation", "Have no effect"]),
            ("Before calculating correlation, you should:", "Check for outliers in the scatter plot", ["Ignore any outliers", "Remove all extreme values", "Calculate mean first"]),
        ]
        question, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{correct}",
            'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    return questions

def generate_level_8():
    """Level 8: Line of Best Fit"""
    questions = []
    
    # Type 1: Interpreting slope
    for i in range(10):
        slope = random.choice([2.5, 3.0, 1.5, -2.0, -1.5, 0.5])
        context = random.choice([
            ("sales (€) vs advertising (€)", "€"),
            ("weight (kg) vs height (cm)", "kg"),
            ("score vs hours studied", "points"),
        ])
        desc, unit = context
        
        if slope > 0:
            interpretation = f"For each 1 unit increase in x, y increases by {abs(slope)}"
        else:
            interpretation = f"For each 1 unit increase in x, y decreases by {abs(slope)}"
        
        distractors = [f"y equals {slope} when x is 0",
                       f"The correlation is {slope}",
                       f"x increases by {slope} for each unit of y"]
        options, correct_idx = make_unique_options(interpretation, distractors)
        
        questions.append({
            'question_text': f"The regression line for {desc} has slope {slope}. What does this mean?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Slope = {slope} means {interpretation}",
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Interpreting y-intercept
    for i in range(8):
        intercept = random.randint(10, 50)
        
        correct = f"When x = 0, y = {intercept}"
        distractors = [f"The slope is {intercept}",
                       f"The correlation is {intercept}",
                       f"y increases by {intercept} per unit of x"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"A regression line has y-intercept {intercept}. What does this represent?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The y-intercept is the value of y when x = 0, so y = {intercept}.",
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Using regression equation for prediction
    for i in range(10):
        m = round(random.uniform(1.5, 4.0), 1)
        c = random.randint(5, 30)
        x = random.randint(5, 20)
        y = round(m * x + c, 1)
        
        correct = str(y)
        distractors = [str(round(y + m, 1)), str(round(y - c, 1)), str(round(m * x, 1))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"The regression line is y = {m}x + {c}. Predict y when x = {x}.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"y = {m}({x}) + {c} = {round(m*x, 1)} + {c} = {correct}",
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 4: Interpolation vs Extrapolation
    for i in range(8):
        data_range = f"{random.randint(10, 20)} to {random.randint(40, 60)}"
        x_low = random.randint(10, 20)
        x_high = random.randint(40, 60)
        
        predict_val = random.choice([x_low + 10, x_high + 20])
        
        if x_low < predict_val < x_high:
            correct = "Interpolation - reliable prediction"
        else:
            correct = "Extrapolation - less reliable prediction"
        
        distractors = ["Extrapolation - less reliable prediction" if "Interpolation" in correct else "Interpolation - reliable prediction",
                       "Cannot make predictions",
                       "Perfect prediction"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Data ranges from x = {x_low} to x = {x_high}. Predicting y for x = {predict_val} is:",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Predicting {'within' if 'Interpolation' in correct else 'outside'} the data range is {'interpolation' if 'Interpolation' in correct else 'extrapolation'}.",
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 5: Properties of regression line
    for i in range(8):
        scenarios = [
            ("The regression line always passes through:", "(x̄, ȳ)", ["(0, 0)", "(1, 1)", "The origin"]),
            ("The regression line minimises:", "Sum of squared residuals", ["Sum of residuals", "Sum of x values", "Correlation"]),
            ("A residual is:", "Actual y - Predicted y", ["Predicted y - x", "Slope × x", "y-intercept"]),
            ("If all points lie exactly on the regression line:", "r² = 1", ["r² = 0", "r = 0", "Slope = 0"]),
        ]
        question, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The answer is: {correct}",
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 6: Finding equation from data
    for i in range(6):
        x_mean = random.randint(5, 15)
        y_mean = random.randint(20, 40)
        slope = round(random.uniform(1.0, 3.0), 1)
        intercept = round(y_mean - slope * x_mean, 1)
        
        correct = f"y = {slope}x + {intercept}"
        distractors = [f"y = {slope}x + {y_mean}",
                       f"y = {intercept}x + {slope}",
                       f"y = {round(slope+1, 1)}x + {intercept}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Given x̄ = {x_mean}, ȳ = {y_mean}, and slope = {slope}, find the regression equation.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Using ȳ = m·x̄ + c: {y_mean} = {slope}×{x_mean} + c, so c = {intercept}. Equation: {correct}",
            'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    return questions

def generate_level_9():
    """Level 9: Hypothesis Testing Basics"""
    questions = []
    
    # Type 1: Null and alternative hypothesis
    for i in range(10):
        scenarios = [
            ("Testing if a coin is fair", "H₀: p = 0.5", ["H₀: p ≠ 0.5", "H₀: p > 0.5", "H₀: p < 0.5"]),
            ("Testing if a new drug is better than standard", "H₀: μ₁ = μ₂", ["H₀: μ₁ > μ₂", "H₀: μ₁ ≠ μ₂", "H₀: μ₁ < μ₂"]),
            ("Testing if average height differs from 170cm", "H₀: μ = 170", ["H₀: μ ≠ 170", "H₀: μ > 170", "H₀: μ < 170"]),
            ("Testing if a process mean exceeds target", "H₀: μ ≤ target", ["H₀: μ > target", "H₀: μ = 0", "H₀: μ ≠ target"]),
        ]
        desc, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"What is the null hypothesis for: {desc}?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The null hypothesis (H₀) represents no effect or no difference: {correct}",
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Type I and Type II errors
    for i in range(10):
        scenarios = [
            ("Rejecting H₀ when it is true", "Type I error", ["Type II error", "Correct decision", "Power"]),
            ("Failing to reject H₀ when it is false", "Type II error", ["Type I error", "Correct decision", "Significance level"]),
            ("The probability of a Type I error is denoted by:", "α (alpha)", ["β (beta)", "p-value", "Power"]),
            ("The probability of a Type II error is denoted by:", "β (beta)", ["α (alpha)", "p-value", "1 - α"]),
            ("Power of a test equals:", "1 - β", ["α", "β", "1 - α"]),
            ("A significant result means:", "Reject H₀", ["Accept H₀", "Type II error", "Inconclusive"]),
        ]
        question, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The answer is: {correct}",
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Significance levels
    for i in range(10):
        scenarios = [
            ("A 5% significance level means:", "5% chance of Type I error", ["5% chance of Type II error", "95% chance of error", "5% of data is significant"]),
            ("If α = 0.01, we:", "Require stronger evidence to reject H₀", ["Have a 99% chance of error", "Always reject H₀", "Have a larger Type I error rate"]),
            ("Common significance levels are:", "0.05 and 0.01", ["0.5 and 0.1", "5 and 10", "0.95 and 0.99"]),
            ("A smaller α means:", "More conservative test", ["More likely to reject H₀", "Larger Type I error", "Weaker evidence needed"]),
        ]
        question, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The answer is: {correct}",
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 4: P-value interpretation
    for i in range(10):
        p_val = random.choice([0.03, 0.08, 0.001, 0.12, 0.04, 0.06])
        alpha = 0.05
        
        if p_val < alpha:
            decision = "Reject H₀"
            reason = f"p-value ({p_val}) < α ({alpha})"
        else:
            decision = "Fail to reject H₀"
            reason = f"p-value ({p_val}) ≥ α ({alpha})"
        
        correct = decision
        distractors = ["Fail to reject H₀" if decision == "Reject H₀" else "Reject H₀",
                       "Accept H₁",
                       "Test is inconclusive"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"If p-value = {p_val} and α = {alpha}, what is your conclusion?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{reason}, so we {decision.lower()}.",
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 5: One-tailed vs two-tailed
    for i in range(10):
        scenarios = [
            ("Testing if μ ≠ 50", "Two-tailed test", ["One-tailed test", "No test needed", "Z-test only"]),
            ("Testing if μ > 100", "One-tailed test (right)", ["Two-tailed test", "One-tailed test (left)", "No test needed"]),
            ("Testing if μ < 30", "One-tailed test (left)", ["Two-tailed test", "One-tailed test (right)", "No test needed"]),
            ("H₁: p ≠ 0.5 suggests:", "Two-tailed test", ["One-tailed test", "No hypothesis test", "Chi-square test"]),
        ]
        question, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The answer is: {correct}",
            'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    return questions

def generate_level_10():
    """Level 10: Confidence Intervals"""
    questions = []
    
    # Type 1: Interpreting confidence intervals
    for i in range(10):
        lower = random.randint(45, 55)
        upper = lower + random.randint(5, 15)
        level = random.choice([90, 95, 99])
        
        correct = f"We are {level}% confident the true mean lies between {lower} and {upper}"
        distractors = [f"{level}% of the data lies between {lower} and {upper}",
                       f"The probability the mean is between {lower} and {upper} is {level}%",
                       f"The mean equals {(lower + upper) / 2} with {level}% certainty"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Interpret the {level}% confidence interval ({lower}, {upper}) for the population mean.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{correct}. This is about the procedure, not the specific interval.",
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Margin of error
    for i in range(10):
        z = random.choice([1.645, 1.96, 2.576])
        sigma = random.randint(5, 15)
        n = random.choice([25, 36, 49, 64, 100])
        
        me = round(z * sigma / sqrt(n), 2)
        correct = str(me)
        distractors = [str(round(z * sigma, 2)), str(round(me * 2, 2)), str(round(z * n / sigma, 2))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        level = {1.645: 90, 1.96: 95, 2.576: 99}[z]
        questions.append({
            'question_text': f"Find the margin of error for a {level}% CI with σ = {sigma}, n = {n}, z = {z}.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"ME = z × σ/√n = {z} × {sigma}/√{n} = {correct}",
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Effect of sample size on CI width
    for i in range(8):
        scenarios = [
            ("Increasing sample size will:", "Narrow the confidence interval", ["Widen the confidence interval", "Not affect the interval", "Increase confidence level"]),
            ("Doubling the sample size will:", "Decrease width by factor of √2", ["Halve the width", "Double the width", "Not affect width"]),
            ("To halve the margin of error, sample size must:", "Quadruple", ["Double", "Halve", "Stay the same"]),
            ("Larger n leads to:", "More precise estimate", ["Wider interval", "Lower confidence", "Larger margin of error"]),
        ]
        question, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The answer is: {correct}",
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 4: Effect of confidence level
    for i in range(8):
        scenarios = [
            ("A 99% CI compared to a 95% CI is:", "Wider", ["Narrower", "The same width", "More precise"]),
            ("Higher confidence level means:", "Wider interval", ["Narrower interval", "Smaller z-value", "Lower margin of error"]),
            ("The z-value for 95% confidence is approximately:", "1.96", ["1.645", "2.576", "1.28"]),
            ("The z-value for 99% confidence is approximately:", "2.576", ["1.96", "1.645", "3.00"]),
        ]
        question, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The answer is: {correct}",
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 5: Constructing confidence intervals
    for i in range(8):
        x_bar = random.randint(45, 55)
        me = random.randint(3, 8)
        lower = x_bar - me
        upper = x_bar + me
        
        correct = f"({lower}, {upper})"
        distractors = [f"({x_bar}, {upper})", f"({lower}, {x_bar})", f"({x_bar - me/2}, {x_bar + me/2})"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"If x̄ = {x_bar} and margin of error = {me}, what is the confidence interval?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"CI = (x̄ - ME, x̄ + ME) = ({x_bar} - {me}, {x_bar} + {me}) = {correct}",
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 6: CI and hypothesis testing connection
    for i in range(8):
        scenarios = [
            ("If 95% CI for μ is (52, 58), testing H₀: μ = 50 at α = 0.05:", "Reject H₀", ["Fail to reject H₀", "Cannot determine", "Accept H₀"]),
            ("If 95% CI for μ is (48, 56), testing H₀: μ = 50 at α = 0.05:", "Fail to reject H₀", ["Reject H₀", "Cannot determine", "Accept H₁"]),
            ("If H₀ value is inside the CI:", "Fail to reject H₀", ["Reject H₀", "Test is inconclusive", "Need more data"]),
            ("If H₀ value is outside the CI:", "Reject H₀", ["Fail to reject H₀", "Accept H₀", "Need larger sample"]),
        ]
        question, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The answer is: {correct}",
            'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    return questions

def generate_level_11():
    """Level 11: Statistical Inference"""
    questions = []
    
    # Type 1: Central Limit Theorem
    for i in range(10):
        scenarios = [
            ("The Central Limit Theorem states that sample means:", "Are approximately normally distributed for large n", ["Are always exactly normal", "Have the same variance as the population", "Equal the population mean"]),
            ("CLT applies when sample size is:", "Large (typically n ≥ 30)", ["Any size", "n < 30 only", "n = 100 exactly"]),
            ("The standard error of the mean equals:", "σ/√n", ["σ", "σ×n", "σ/n"]),
            ("As sample size increases, standard error:", "Decreases", ["Increases", "Stays the same", "Becomes zero"]),
            ("The sampling distribution of x̄ has mean:", "μ (population mean)", ["σ", "0", "x̄"]),
        ]
        question, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The answer is: {correct}",
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Standard error calculations
    for i in range(10):
        sigma = random.choice([10, 12, 15, 20])
        n = random.choice([16, 25, 36, 49, 64, 100])
        se = round(sigma / sqrt(n), 2)
        
        correct = str(se)
        distractors = [str(sigma), str(round(sigma / n, 2)), str(round(sigma * sqrt(n), 2))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"If σ = {sigma} and n = {n}, what is the standard error of the mean?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"SE = σ/√n = {sigma}/√{n} = {sigma}/{sqrt(n):.0f} = {correct}",
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Z-test for means
    for i in range(8):
        x_bar = random.randint(48, 52)
        mu = 50
        sigma = random.randint(8, 12)
        n = random.choice([36, 64, 100])
        
        se = sigma / sqrt(n)
        z = round((x_bar - mu) / se, 2)
        
        correct = str(z)
        distractors = [str(round(-z, 2)), str(round(z * 2, 2)), str(round((x_bar - mu) / sigma, 2))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Calculate the z-statistic: x̄ = {x_bar}, μ₀ = {mu}, σ = {sigma}, n = {n}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"z = (x̄ - μ)/(σ/√n) = ({x_bar} - {mu})/({sigma}/√{n}) = {correct}",
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 4: T-distribution concepts
    for i in range(8):
        scenarios = [
            ("Use t-distribution instead of z when:", "Population σ is unknown", ["n is large", "Population is normal", "Sample mean is known"]),
            ("Degrees of freedom for one-sample t-test:", "n - 1", ["n", "n + 1", "n/2"]),
            ("As df increases, t-distribution:", "Approaches normal distribution", ["Becomes more spread out", "Has larger critical values", "Changes shape randomly"]),
            ("T-distribution compared to normal is:", "More spread out with heavier tails", ["Narrower", "Identical", "Only positive values"]),
        ]
        question, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The answer is: {correct}",
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 5: Proportion inference
    for i in range(8):
        p_hat = round(random.uniform(0.4, 0.6), 2)
        n = random.choice([100, 200, 400])
        se = round(sqrt(p_hat * (1 - p_hat) / n), 3)
        
        correct = str(se)
        distractors = [str(round(p_hat / sqrt(n), 3)), str(round(sqrt(p_hat / n), 3)), str(round(p_hat * (1 - p_hat), 3))]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Find SE for a proportion: p̂ = {p_hat}, n = {n}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"SE = √(p̂(1-p̂)/n) = √({p_hat}×{round(1-p_hat, 2)}/{n}) = {correct}",
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 6: Sample size determination
    for i in range(8):
        scenarios = [
            ("To decrease margin of error by half, sample size must:", "Quadruple", ["Double", "Halve", "Stay the same"]),
            ("For 95% CI with ME = 2 and σ = 10, minimum n is approximately:", "96", ["50", "25", "200"]),
            ("Larger desired confidence level requires:", "Larger sample size", ["Smaller sample size", "Same sample size", "Cannot determine"]),
            ("Smaller desired margin of error requires:", "Larger sample size", ["Smaller sample size", "Same sample size", "Higher confidence"]),
        ]
        question, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The answer is: {correct}",
            'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    return questions

def generate_level_12():
    """Level 12: Mastery Challenge - Mixed advanced problems"""
    questions = []
    
    # Type 1: Complex CI problems
    for i in range(8):
        x_bar = random.randint(95, 105)
        s = random.randint(10, 20)
        n = random.choice([25, 36, 49])
        z = 1.96
        
        me = round(z * s / sqrt(n), 2)
        lower = round(x_bar - me, 2)
        upper = round(x_bar + me, 2)
        
        correct = f"({lower}, {upper})"
        distractors = [f"({x_bar - s}, {x_bar + s})",
                       f"({round(lower - 2, 2)}, {round(upper + 2, 2)})",
                       f"({x_bar}, {upper})"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Construct a 95% CI: x̄ = {x_bar}, s = {s}, n = {n}, z = 1.96",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"ME = 1.96 × {s}/√{n} = {me}. CI = ({x_bar} ± {me}) = {correct}",
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Hypothesis testing conclusions
    for i in range(8):
        z = round(random.uniform(-3, 3), 2)
        alpha = 0.05
        critical = 1.96
        
        if abs(z) > critical:
            decision = "Reject H₀ (significant result)"
            reason = f"|{z}| > {critical}"
        else:
            decision = "Fail to reject H₀ (not significant)"
            reason = f"|{z}| ≤ {critical}"
        
        correct = decision
        distractors = ["Fail to reject H₀ (not significant)" if "Reject" in decision else "Reject H₀ (significant result)",
                       "Accept H₁",
                       "Test inconclusive"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"z = {z}, α = 0.05 (two-tailed, critical = ±1.96). Decision?",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"{reason}, so we {decision.lower().split('(')[0].strip()}.",
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Combined statistics concepts
    for i in range(8):
        data = sorted([random.randint(10, 50) for _ in range(5)])
        mean = sum(data) / 5
        median = data[2]
        range_val = data[4] - data[0]
        
        question_type = random.choice([
            (f"mean", round(mean, 1)),
            (f"median", median),
            (f"range", range_val),
        ])
        q_name, answer = question_type
        
        correct = str(answer)
        distractors = [str(round(mean + 2, 1)), str(median + 1), str(range_val - 5)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Find the {q_name} of: {', '.join(map(str, data))}",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The {q_name} = {correct}",
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 4: Regression analysis
    for i in range(6):
        r = random.choice([0.8, 0.85, 0.9, -0.75, -0.8])
        r_sq = round(r ** 2, 2)
        
        slope = round(random.uniform(1.5, 3.5), 1) * (1 if r > 0 else -1)
        intercept = random.randint(5, 20)
        
        correct = f"y = {slope}x + {intercept}, r² = {r_sq}"
        distractors = [f"y = {slope}x + {intercept}, r² = {abs(r)}",
                       f"y = {-slope}x + {intercept}, r² = {r_sq}",
                       f"y = {intercept}x + {slope}, r² = {r_sq}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"If r = {r}, slope = {slope}, intercept = {intercept}, express the regression with r².",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"r² = {r}² = {r_sq}. Equation: {correct}",
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 5: Normal distribution applications
    for i in range(6):
        mu = 100
        sigma = 15
        x = random.choice([85, 115, 130, 70])
        z = (x - mu) / sigma
        
        correct = str(round(z, 2))
        distractors = [str(round(-z, 2)), str(round(z + 1, 2)), str(x - mu)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Scores ~ N(100, 15²). Calculate z for score = {x}.",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"z = ({x} - 100)/15 = {correct}",
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 6: Sampling distribution
    for i in range(6):
        mu = random.randint(45, 55)
        sigma = random.randint(8, 12)
        n = random.choice([16, 25, 36])
        se = round(sigma / sqrt(n), 2)
        
        correct = f"Mean = {mu}, SE = {se}"
        distractors = [f"Mean = {mu}, SE = {sigma}",
                       f"Mean = {mu + 5}, SE = {se}",
                       f"Mean = {mu}, SE = {round(sigma/n, 2)}"]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': f"Population: μ = {mu}, σ = {sigma}. For samples of size {n}, the sampling distribution of x̄ has:",
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"Mean of x̄ = μ = {mu}. SE = σ/√n = {sigma}/√{n} = {se}",
            'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 7: Critical thinking questions
    for i in range(8):
        scenarios = [
            ("A study with n=10 finds p=0.04. Most appropriate response:", "Results suggest significance but small sample warrants caution", ["Definitely reject H₀", "Result is not significant", "Increase α to 0.10"]),
            ("Two variables correlate (r=0.9). Can we conclude causation?", "No, correlation does not imply causation", ["Yes, strong correlation proves causation", "Only if r > 0.95", "Yes, if p < 0.05"]),
            ("A 95% CI is (45, 55). A 99% CI would be:", "Wider than (45, 55)", ["Narrower than (45, 55)", "The same", "(45, 55) exactly"]),
            ("Sample mean differs from population mean. This is due to:", "Sampling variability", ["Calculation error", "Bias only", "Invalid sample"]),
        ]
        question, correct, distractors = scenarios[i % len(scenarios)]
        options, correct_idx = make_unique_options(correct, distractors)
        
        questions.append({
            'question_text': question,
            'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3],
            'correct_idx': correct_idx,
            'explanation': f"The answer is: {correct}",
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
        f.write(f"-- LC Higher Level - Statistics Questions\n")
        f.write(f"-- Generated: 2025-12-15\n")
        f.write(f"-- Total: {len(all_questions)} questions\n\n")
        f.write('\n'.join(sql_statements))
    
    print(f"\nSQL file written to: {sql_file}")
    return all_questions

if __name__ == '__main__':
    main()
