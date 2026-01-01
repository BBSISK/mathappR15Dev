#!/usr/bin/env python3
"""
LC Ordinary Level - Statistics (Descriptive) Question Generator
Version: 1.0
Date: 2025-12-15

Generates 600 questions (50 per level × 12 levels) for LC OL Statistics
Based on SEC Paper Analysis 2019-2025 (330 marks - #3 priority Paper 2)

OL Statistics Focus:
- Mean, median, mode, range
- Frequency tables
- Bar charts, pie charts, histograms
- Stem-and-leaf plots
- Standard deviation
- Cumulative frequency
- Empirical Rule
- Correlation coefficient interpretation

Levels:
1. Mean & Median
2. Mode & Range
3. Frequency Tables - Reading
4. Frequency Tables - Calculations
5. Bar Charts & Pie Charts
6. Histograms
7. Stem-and-Leaf Plots
8. Standard Deviation
9. Cumulative Frequency
10. Empirical Rule
11. Correlation
12. Mastery Challenge
"""

import random
import math

TOPIC = 'lc_ol_statistics'
MODE = 'lc_ol'

LEVEL_TITLES = [
    'Mean & Median',
    'Mode & Range',
    'Frequency Tables - Reading',
    'Frequency Tables - Calculations',
    'Bar Charts & Pie Charts',
    'Histograms',
    'Stem-and-Leaf Plots',
    'Standard Deviation',
    'Cumulative Frequency',
    'Empirical Rule',
    'Correlation',
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
        unique_wrong.append("Cannot determine")
    options = [correct_str] + unique_wrong[:3]
    random.shuffle(options)
    return options, options.index(correct_str)


def generate_level_1():
    """Level 1: Mean & Median"""
    questions = []
    
    # Type 1: Calculate mean of small dataset (25 questions)
    for _ in range(25):
        n = random.choice([4, 5, 6])
        data = [random.randint(2, 15) for _ in range(n)]
        total = sum(data)
        mean = total / n
        mean_rounded = round(mean, 1) if mean != int(mean) else int(mean)
        
        data_str = ", ".join(map(str, data))
        question = f"Find the mean of: {data_str}"
        correct = str(mean_rounded)
        distractors = [
            str(round(mean + 1, 1)),
            str(round(mean - 1, 1)),
            str(total)
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Mean = ({' + '.join(map(str, data))}) ÷ {n} = {total} ÷ {n} = {mean_rounded}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Find median - odd number of values (15 questions)
    for _ in range(15):
        n = random.choice([5, 7, 9])
        data = sorted([random.randint(1, 20) for _ in range(n)])
        median = data[n // 2]
        
        # Shuffle for display
        display_data = data.copy()
        random.shuffle(display_data)
        data_str = ", ".join(map(str, display_data))
        
        question = f"Find the median of: {data_str}"
        correct = str(median)
        distractors = [
            str(data[n // 2 - 1]),
            str(data[n // 2 + 1]) if n // 2 + 1 < n else str(median + 1),
            str(round(sum(data) / n, 1))
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Ordered: {', '.join(map(str, data))}. Middle value (position {n // 2 + 1}) = {median}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Find median - even number of values (10 questions)
    for _ in range(10):
        n = random.choice([4, 6, 8])
        data = sorted([random.randint(1, 20) for _ in range(n)])
        median = (data[n // 2 - 1] + data[n // 2]) / 2
        median_rounded = median if median == int(median) else round(median, 1)
        
        display_data = data.copy()
        random.shuffle(display_data)
        data_str = ", ".join(map(str, display_data))
        
        question = f"Find the median of: {data_str}"
        correct = str(median_rounded)
        distractors = [
            str(data[n // 2 - 1]),
            str(data[n // 2]),
            str(round(sum(data) / n, 1))
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Ordered: {', '.join(map(str, data))}. Median = ({data[n // 2 - 1]} + {data[n // 2]}) ÷ 2 = {median_rounded}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 1, 'difficulty_band': 'foundation'
        })
    
    return questions


def generate_level_2():
    """Level 2: Mode & Range"""
    questions = []
    
    # Type 1: Find the mode (25 questions)
    for _ in range(25):
        mode = random.randint(3, 15)
        data = [mode, mode, mode]  # mode appears 3 times
        for _ in range(random.randint(3, 5)):
            val = random.randint(1, 20)
            if val != mode:
                data.append(val)
        random.shuffle(data)
        
        data_str = ", ".join(map(str, data))
        question = f"Find the mode of: {data_str}"
        correct = str(mode)
        
        other_vals = [x for x in set(data) if x != mode]
        distractors = other_vals[:2] + [str(round(sum(data) / len(data), 1))]
        distractors = [str(d) for d in distractors]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"The mode is {mode} as it appears most frequently (3 times)"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Find the range (15 questions)
    for _ in range(15):
        data = [random.randint(5, 50) for _ in range(random.randint(5, 8))]
        range_val = max(data) - min(data)
        
        data_str = ", ".join(map(str, data))
        question = f"Find the range of: {data_str}"
        correct = str(range_val)
        distractors = [
            str(max(data)),
            str(min(data)),
            str(range_val + 5)
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Range = Maximum - Minimum = {max(data)} - {min(data)} = {range_val}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    # Type 3: No mode / bimodal (10 questions)
    for i in range(10):
        if i < 5:
            # No mode - all different
            data = random.sample(range(1, 20), 5)
            data_str = ", ".join(map(str, data))
            question = f"Find the mode of: {data_str}"
            correct = "No mode"
            distractors = [str(min(data)), str(max(data)), str(data[2])]
            explanation = "Each value appears only once, so there is no mode"
        else:
            # Bimodal
            mode1 = random.randint(3, 10)
            mode2 = random.randint(12, 18)
            data = [mode1, mode1, mode2, mode2, random.randint(1, 20)]
            random.shuffle(data)
            data_str = ", ".join(map(str, data))
            question = f"Find the mode(s) of: {data_str}"
            correct = f"{min(mode1, mode2)} and {max(mode1, mode2)}"
            distractors = [str(mode1), str(mode2), "No mode"]
            explanation = f"Both {mode1} and {mode2} appear twice, so the data is bimodal"
        
        options, idx = make_unique_options(correct, distractors)
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 2, 'difficulty_band': 'foundation'
        })
    
    return questions


def generate_level_3():
    """Level 3: Frequency Tables - Reading"""
    questions = []
    
    # Type 1: Find total frequency (20 questions)
    for _ in range(20):
        categories = random.randint(4, 6)
        frequencies = [random.randint(3, 15) for _ in range(categories)]
        total = sum(frequencies)
        
        table_desc = f"A frequency table has {categories} categories with frequencies: {', '.join(map(str, frequencies))}"
        question = f"{table_desc}. Find the total frequency."
        correct = str(total)
        distractors = [
            str(total + random.randint(1, 5)),
            str(total - random.randint(1, 5)),
            str(max(frequencies))
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Total frequency = {' + '.join(map(str, frequencies))} = {total}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 2: Find mode from frequency table (15 questions)
    for _ in range(15):
        values = [1, 2, 3, 4, 5]
        frequencies = [random.randint(2, 8) for _ in range(5)]
        max_freq = max(frequencies)
        mode_idx = frequencies.index(max_freq)
        mode = values[mode_idx]
        
        freq_str = ", ".join([f"Value {v}: {f}" for v, f in zip(values, frequencies)])
        question = f"From the frequency table ({freq_str}), find the mode."
        correct = str(mode)
        distractors = [str(max_freq), str(values[(mode_idx + 1) % 5]), str(values[(mode_idx - 1) % 5])]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"The mode is {mode} as it has the highest frequency ({max_freq})"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    # Type 3: Find missing frequency (15 questions)
    for _ in range(15):
        frequencies = [random.randint(5, 12) for _ in range(4)]
        total = sum(frequencies) + random.randint(8, 15)
        missing = total - sum(frequencies)
        
        freq_display = frequencies.copy()
        missing_pos = random.randint(0, 3)
        freq_display[missing_pos] = "?"
        
        question = f"Frequencies are {freq_display[0]}, {freq_display[1]}, {freq_display[2]}, {freq_display[3]}. Total = {total}. Find the missing frequency."
        correct = str(missing)
        distractors = [str(missing + 3), str(missing - 2), str(total)]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Missing = {total} - ({' + '.join([str(f) for f in frequencies if f != frequencies[missing_pos]])}) = {missing}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 3, 'difficulty_band': 'foundation'
        })
    
    return questions


def generate_level_4():
    """Level 4: Frequency Tables - Calculations"""
    questions = []
    
    # Type 1: Mean from frequency table (25 questions)
    for _ in range(25):
        values = [1, 2, 3, 4, 5]
        frequencies = [random.randint(2, 8) for _ in range(5)]
        total_freq = sum(frequencies)
        total_fx = sum(v * f for v, f in zip(values, frequencies))
        mean = total_fx / total_freq
        mean_rounded = round(mean, 2)
        
        freq_str = ", ".join([f"({v}, {f})" for v, f in zip(values, frequencies)])
        question = f"From (value, frequency) pairs: {freq_str}, calculate the mean."
        correct = str(mean_rounded)
        distractors = [
            str(round(mean + 0.5, 2)),
            str(round(sum(values) / 5, 2)),
            str(round(total_fx / 10, 2))
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Mean = Σfx / Σf = {total_fx} / {total_freq} = {mean_rounded}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 2: Median from frequency table (15 questions)
    for _ in range(15):
        values = [1, 2, 3, 4, 5]
        frequencies = [random.randint(3, 10) for _ in range(5)]
        total = sum(frequencies)
        
        # Find median position
        median_pos = (total + 1) / 2
        cumulative = 0
        median = 0
        for v, f in zip(values, frequencies):
            cumulative += f
            if cumulative >= median_pos:
                median = v
                break
        
        freq_str = ", ".join([f"({v}: {f})" for v, f in zip(values, frequencies)])
        question = f"Score frequencies: {freq_str}. Find the median score."
        correct = str(median)
        distractors = [str(median + 1), str(median - 1), str(values[2])]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Total = {total}. Median position = {median_pos}. Counting through frequencies, median = {median}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    # Type 3: Mean from grouped data (midpoints) (10 questions)
    for _ in range(10):
        groups = ["0-10", "10-20", "20-30", "30-40"]
        midpoints = [5, 15, 25, 35]
        frequencies = [random.randint(3, 10) for _ in range(4)]
        total_freq = sum(frequencies)
        total_fx = sum(m * f for m, f in zip(midpoints, frequencies))
        mean = total_fx / total_freq
        mean_rounded = round(mean, 1)
        
        freq_str = ", ".join([f"{g}: {f}" for g, f in zip(groups, frequencies)])
        question = f"Grouped data ({freq_str}). Using midpoints, estimate the mean."
        correct = str(mean_rounded)
        distractors = [
            str(round(mean + 3, 1)),
            str(round(mean - 3, 1)),
            str(round(sum(midpoints) / 4, 1))
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Midpoints: {midpoints}. Mean = Σfx / Σf = {total_fx} / {total_freq} = {mean_rounded}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 4, 'difficulty_band': 'developing'
        })
    
    return questions


def generate_level_5():
    """Level 5: Bar Charts & Pie Charts"""
    questions = []
    
    # Type 1: Read bar chart (20 questions)
    for _ in range(20):
        categories = ["A", "B", "C", "D", "E"]
        values = [random.randint(5, 25) for _ in range(5)]
        max_val = max(values)
        max_cat = categories[values.index(max_val)]
        total = sum(values)
        
        bar_desc = ", ".join([f"{c}={v}" for c, v in zip(categories, values)])
        question = f"A bar chart shows: {bar_desc}. Which category has the highest value and what is the total?"
        correct = f"{max_cat}, total = {total}"
        distractors = [
            f"{categories[(values.index(max_val) + 1) % 5]}, total = {total}",
            f"{max_cat}, total = {total + 10}",
            f"{max_cat}, total = {max_val}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Highest: {max_cat} with {max_val}. Total = {' + '.join(map(str, values))} = {total}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 2: Pie chart - find angle (20 questions)
    for _ in range(20):
        total = random.choice([60, 72, 90, 100, 120, 180])
        part = random.choice([10, 12, 15, 18, 20, 24, 25, 30, 36, 40, 45])
        if part > total:
            part = total // 4
        
        angle = (part / total) * 360
        angle_rounded = round(angle, 1) if angle != int(angle) else int(angle)
        
        question = f"In a pie chart, {part} out of {total} people chose option A. What angle represents this?"
        correct = f"{angle_rounded}°"
        distractors = [
            f"{round(part / total * 100, 1)}°",
            f"{round(angle + 20, 1)}°",
            f"{part}°"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Angle = ({part}/{total}) × 360° = {angle_rounded}°"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    # Type 3: Pie chart - find frequency from angle (10 questions)
    for _ in range(10):
        total = random.choice([60, 72, 90, 120, 180])
        angle = random.choice([30, 45, 60, 72, 90, 120])
        
        frequency = (angle / 360) * total
        freq_rounded = int(frequency) if frequency == int(frequency) else round(frequency, 1)
        
        question = f"A pie chart represents {total} items. A sector has angle {angle}°. How many items does it represent?"
        correct = str(freq_rounded)
        distractors = [
            str(round(frequency + 5)),
            str(round(angle / 360 * 100)),
            str(total)
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Frequency = ({angle}/360) × {total} = {freq_rounded}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 5, 'difficulty_band': 'developing'
        })
    
    return questions


def generate_level_6():
    """Level 6: Histograms"""
    questions = []
    
    # Type 1: Read histogram - find frequency (20 questions)
    for _ in range(20):
        groups = ["0-10", "10-20", "20-30", "30-40", "40-50"]
        frequencies = [random.randint(3, 15) for _ in range(5)]
        
        target_group = random.choice(groups)
        target_freq = frequencies[groups.index(target_group)]
        
        freq_desc = ", ".join([f"{g}: {f}" for g, f in zip(groups, frequencies)])
        question = f"A histogram shows ({freq_desc}). How many values are in the {target_group} group?"
        correct = str(target_freq)
        distractors = [
            str(target_freq + 3),
            str(target_freq - 2),
            str(sum(frequencies))
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Reading from the histogram, the {target_group} bar has frequency {target_freq}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 2: Total from histogram (15 questions)
    for _ in range(15):
        frequencies = [random.randint(4, 12) for _ in range(5)]
        total = sum(frequencies)
        
        freq_str = ", ".join(map(str, frequencies))
        question = f"A histogram has 5 bars with frequencies: {freq_str}. How many data values are there in total?"
        correct = str(total)
        distractors = [
            str(total + 5),
            str(max(frequencies)),
            str(total - min(frequencies))
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Total = {' + '.join(map(str, frequencies))} = {total}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    # Type 3: Modal class (15 questions)
    for _ in range(15):
        groups = ["0-10", "10-20", "20-30", "30-40", "40-50"]
        frequencies = [random.randint(3, 15) for _ in range(5)]
        max_freq = max(frequencies)
        modal_class = groups[frequencies.index(max_freq)]
        
        freq_desc = ", ".join([f"{g}: {f}" for g, f in zip(groups, frequencies)])
        question = f"From the histogram ({freq_desc}), identify the modal class."
        correct = modal_class
        distractors = [
            groups[(frequencies.index(max_freq) + 1) % 5],
            groups[(frequencies.index(max_freq) - 1) % 5],
            str(max_freq)
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"The modal class is {modal_class} with the highest frequency ({max_freq})"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 6, 'difficulty_band': 'developing'
        })
    
    return questions


def generate_level_7():
    """Level 7: Stem-and-Leaf Plots"""
    questions = []
    
    # Type 1: Read values from stem-leaf (20 questions)
    for _ in range(20):
        stem = random.randint(2, 5)
        leaves = sorted(random.sample(range(0, 10), random.randint(4, 6)))
        values = [stem * 10 + leaf for leaf in leaves]
        
        leaves_str = " ".join(map(str, leaves))
        question = f"In a stem-and-leaf plot, stem {stem} has leaves: {leaves_str}. What is the largest value?"
        correct = str(max(values))
        distractors = [
            str(min(values)),
            str(stem * 10),
            str(max(values) + 10)
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Stem {stem} with leaf {max(leaves)} gives {stem}{max(leaves)} = {max(values)}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Find median from stem-leaf (15 questions)
    for _ in range(15):
        # Create a complete stem-leaf dataset
        data = sorted([random.randint(20, 59) for _ in range(9)])  # Odd number for easy median
        median = data[4]  # Middle of 9 values
        
        # Create stem-leaf description
        stems = {}
        for val in data:
            s = val // 10
            l = val % 10
            if s not in stems:
                stems[s] = []
            stems[s].append(l)
        
        stem_desc = "; ".join([f"Stem {s}: {' '.join(map(str, sorted(leaves)))}" for s, leaves in sorted(stems.items())])
        
        question = f"A stem-leaf plot shows: {stem_desc}. Find the median."
        correct = str(median)
        distractors = [
            str(median + 1),
            str(median - 1),
            str(data[3])
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"9 values, so median is the 5th value. Ordered: {', '.join(map(str, data))}. Median = {median}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Count values / find range (15 questions)
    for _ in range(15):
        data = sorted([random.randint(15, 65) for _ in range(random.randint(8, 12))])
        n = len(data)
        range_val = max(data) - min(data)
        
        stems = {}
        for val in data:
            s = val // 10
            l = val % 10
            if s not in stems:
                stems[s] = []
            stems[s].append(l)
        
        stem_desc = "; ".join([f"{s}|{' '.join(map(str, sorted(leaves)))}" for s, leaves in sorted(stems.items())])
        
        question = f"Stem-leaf plot: {stem_desc}. How many data values are there?"
        correct = str(n)
        distractors = [
            str(n + 2),
            str(n - 1),
            str(len(stems))
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Count all leaves: {n} data values"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 7, 'difficulty_band': 'proficient'
        })
    
    return questions


def generate_level_8():
    """Level 8: Standard Deviation"""
    questions = []
    
    # Type 1: Interpret standard deviation (20 questions)
    for _ in range(20):
        mean = random.randint(50, 80)
        sd1 = random.randint(3, 8)
        sd2 = random.randint(12, 20)
        
        question = f"Dataset A has mean {mean}, SD = {sd1}. Dataset B has mean {mean}, SD = {sd2}. Which is more spread out?"
        correct = f"Dataset B (higher SD = more spread)"
        distractors = [
            f"Dataset A (lower SD = more spread)",
            "Both the same (same mean)",
            "Cannot tell without the data"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Standard deviation measures spread. Higher SD ({sd2} > {sd1}) means more spread out."
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Calculate SD for small dataset (20 questions)
    for _ in range(20):
        # Use simple numbers for easy calculation
        data = [random.randint(2, 10) for _ in range(4)]
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        sd = math.sqrt(variance)
        sd_rounded = round(sd, 2)
        
        data_str = ", ".join(map(str, data))
        question = f"Calculate the standard deviation of: {data_str} (population SD)"
        correct = str(sd_rounded)
        distractors = [
            str(round(sd + 0.5, 2)),
            str(round(variance, 2)),
            str(round(mean, 2))
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Mean = {mean}. Variance = Σ(x-μ)²/n = {round(variance, 2)}. SD = √{round(variance, 2)} = {sd_rounded}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Effect of adding constant (10 questions)
    for _ in range(10):
        sd = random.randint(5, 15)
        constant = random.randint(5, 20)
        
        question = f"A dataset has SD = {sd}. If {constant} is added to every value, what is the new SD?"
        correct = str(sd)
        distractors = [
            str(sd + constant),
            str(sd - constant) if sd > constant else str(constant - sd),
            str(sd * 2)
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Adding a constant shifts all values but doesn't change the spread. SD stays {sd}."
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 8, 'difficulty_band': 'proficient'
        })
    
    return questions


def generate_level_9():
    """Level 9: Cumulative Frequency"""
    questions = []
    
    # Type 1: Calculate cumulative frequency (20 questions)
    for _ in range(20):
        frequencies = [random.randint(3, 12) for _ in range(5)]
        cumulative = []
        total = 0
        for f in frequencies:
            total += f
            cumulative.append(total)
        
        target_pos = random.randint(1, 4)
        
        freq_str = ", ".join(map(str, frequencies))
        question = f"Frequencies: {freq_str}. What is the cumulative frequency after group {target_pos + 1}?"
        correct = str(cumulative[target_pos])
        distractors = [
            str(frequencies[target_pos]),
            str(cumulative[target_pos] + frequencies[0]),
            str(cumulative[-1])
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Cumulative = {' + '.join(map(str, frequencies[:target_pos + 1]))} = {cumulative[target_pos]}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 2: Find median class from cumulative frequency (15 questions)
    for _ in range(15):
        groups = ["0-10", "10-20", "20-30", "30-40", "40-50"]
        frequencies = [random.randint(5, 15) for _ in range(5)]
        total = sum(frequencies)
        median_pos = total / 2
        
        cumulative = []
        cum_total = 0
        median_class = ""
        for i, f in enumerate(frequencies):
            cum_total += f
            cumulative.append(cum_total)
            if cum_total >= median_pos and median_class == "":
                median_class = groups[i]
        
        cum_str = ", ".join(map(str, cumulative))
        question = f"Cumulative frequencies: {cum_str} for groups {', '.join(groups)}. Which is the median class?"
        correct = median_class
        distractors = [
            groups[(groups.index(median_class) + 1) % 5],
            groups[(groups.index(median_class) - 1) % 5],
            groups[2]
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Total = {total}. Median position = {median_pos}. Median class is {median_class}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    # Type 3: Percentile from cumulative frequency (15 questions)
    for _ in range(15):
        total = random.choice([40, 50, 60, 80, 100])
        percentile = random.choice([25, 50, 75])
        position = total * percentile / 100
        
        question = f"A cumulative frequency diagram has {total} data points. At what cumulative frequency is the {percentile}th percentile?"
        correct = str(int(position))
        distractors = [
            str(int(position + total / 10)),
            str(percentile),
            str(total)
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"{percentile}th percentile position = {percentile}% of {total} = {int(position)}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 9, 'difficulty_band': 'proficient'
        })
    
    return questions


def generate_level_10():
    """Level 10: Empirical Rule (68-95-99.7)"""
    questions = []
    
    # Type 1: Within 1 SD (20 questions)
    for _ in range(20):
        mean = random.choice([50, 60, 70, 80, 100])
        sd = random.choice([5, 8, 10, 12, 15])
        
        lower = mean - sd
        upper = mean + sd
        
        question = f"Data is normally distributed with mean {mean} and SD {sd}. What percentage lies within 1 SD of the mean?"
        correct = "68%"
        distractors = ["95%", "99.7%", "50%"]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"By the Empirical Rule, 68% of data lies within 1 SD (between {lower} and {upper})"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Within 2 SD / 3 SD (15 questions)
    for _ in range(15):
        mean = random.choice([50, 60, 70, 80, 100])
        sd = random.choice([5, 8, 10, 12])
        num_sd = random.choice([2, 3])
        
        if num_sd == 2:
            percent = 95
            lower, upper = mean - 2*sd, mean + 2*sd
        else:
            percent = 99.7
            lower, upper = mean - 3*sd, mean + 3*sd
        
        question = f"Mean = {mean}, SD = {sd}. What percentage lies between {lower} and {upper}?"
        correct = f"{percent}%"
        distractors = ["68%", "95%" if percent != 95 else "99.7%", "50%"]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Range is ±{num_sd} SD. By Empirical Rule, {percent}% lies within {num_sd} SD"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Find bounds (15 questions)
    for _ in range(15):
        mean = random.choice([100, 150, 200])
        sd = random.choice([10, 15, 20, 25])
        num_sd = random.choice([1, 2])
        
        lower = mean - num_sd * sd
        upper = mean + num_sd * sd
        
        question = f"Mean = {mean}, SD = {sd}. Find the range containing {'68' if num_sd == 1 else '95'}% of the data."
        correct = f"{lower} to {upper}"
        distractors = [
            f"{mean - sd} to {mean + sd}" if num_sd != 1 else f"{mean - 2*sd} to {mean + 2*sd}",
            f"{lower - sd} to {upper + sd}",
            f"{mean} to {upper}"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"{'68' if num_sd == 1 else '95'}% within {num_sd} SD: {mean} ± {num_sd}×{sd} = {lower} to {upper}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 10, 'difficulty_band': 'advanced'
        })
    
    return questions


def generate_level_11():
    """Level 11: Correlation"""
    questions = []
    
    # Type 1: Interpret correlation coefficient (25 questions)
    correlations = [
        (0.95, "strong positive"),
        (0.85, "strong positive"),
        (0.6, "moderate positive"),
        (0.3, "weak positive"),
        (0.1, "very weak positive"),
        (0, "no correlation"),
        (-0.3, "weak negative"),
        (-0.6, "moderate negative"),
        (-0.85, "strong negative"),
        (-0.95, "strong negative"),
    ]
    
    for _ in range(25):
        r, description = random.choice(correlations)
        
        question = f"A correlation coefficient r = {r}. Describe the relationship."
        correct = description.capitalize()
        
        # Generate different distractors
        all_descriptions = ["Strong positive", "Strong negative", "Moderate positive", 
                          "Moderate negative", "Weak positive", "Weak negative", "No correlation"]
        distractors = [d for d in all_descriptions if d.lower() != description][:3]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"r = {r} indicates {description} correlation. Closer to ±1 = stronger, closer to 0 = weaker."
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Correlation range validity (15 questions)
    for _ in range(15):
        invalid_r = random.choice([1.2, 1.5, -1.3, -1.8, 2, 5])
        
        question = f"A student calculated r = {invalid_r}. Is this valid?"
        correct = "No, r must be between -1 and 1"
        distractors = [
            "Yes, this is a strong correlation",
            "Yes, but it's unusual",
            "No, r must be positive"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Correlation coefficient r must satisfy -1 ≤ r ≤ 1. r = {invalid_r} is invalid."
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Correlation vs causation (10 questions)
    scenarios = [
        ("Ice cream sales and drowning rates both increase in summer", "No - both caused by hot weather (confounding variable)"),
        ("Study time and test scores show positive correlation", "Possibly - but other factors may contribute"),
        ("Shoe size and reading ability correlate in children", "No - both increase with age (confounding variable)"),
        ("Smoking and lung cancer show strong correlation", "Correlation suggests relationship but doesn't prove causation directly"),
        ("Number of firefighters and fire damage correlate", "No - larger fires need more firefighters (reverse causation)"),
    ]
    
    for i in range(10):
        scenario, answer = scenarios[i % len(scenarios)]
        
        question = f"{scenario}. Does this prove causation?"
        correct = answer
        distractors = [
            "Yes, correlation always means causation",
            "Yes, the data proves it",
            "Cannot determine from correlation"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = "Correlation does not imply causation. Consider confounding variables and reverse causation."
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 11, 'difficulty_band': 'advanced'
        })
    
    return questions


def generate_level_12():
    """Level 12: Mastery Challenge"""
    questions = []
    
    # Type 1: Multi-step calculations (15 questions)
    for _ in range(15):
        data = [random.randint(10, 30) for _ in range(5)]
        mean = sum(data) / len(data)
        data_sorted = sorted(data)
        median = data_sorted[2]
        mode_val = random.choice(data)
        data_with_mode = data + [mode_val]
        random.shuffle(data_with_mode)
        
        new_mean = sum(data_with_mode) / len(data_with_mode)
        
        data_str = ", ".join(map(str, data))
        question = f"Data: {data_str}. If {mode_val} is added, what is the new mean?"
        correct = str(round(new_mean, 1))
        distractors = [
            str(round(mean, 1)),
            str(round(new_mean + 1, 1)),
            str(mode_val)
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"New total = {sum(data_with_mode)}, n = {len(data_with_mode)}. New mean = {round(new_mean, 1)}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 2: Compare datasets (15 questions)
    for _ in range(15):
        mean_a = random.randint(50, 70)
        sd_a = random.randint(5, 10)
        mean_b = mean_a + random.randint(-5, 5)
        sd_b = sd_a + random.randint(3, 8)
        
        question = f"Set A: mean={mean_a}, SD={sd_a}. Set B: mean={mean_b}, SD={sd_b}. Which set has more consistent values?"
        correct = f"Set A (lower SD = more consistent)"
        distractors = [
            f"Set B (higher SD = more consistent)",
            "Same consistency (similar means)",
            "Cannot compare without raw data"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"Lower SD means less spread, so more consistent. Set A has SD {sd_a} < {sd_b}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    # Type 3: Real-world interpretation (20 questions)
    for _ in range(20):
        context = random.choice([
            ("exam scores", 65, 12),
            ("heights (cm)", 170, 8),
            ("waiting times (min)", 15, 4),
            ("temperatures (°C)", 20, 5),
            ("weights (kg)", 70, 10)
        ])
        
        name, mean, sd = context
        value = mean + random.choice([-2, -1, 1, 2]) * sd
        z = (value - mean) / sd
        
        if abs(z) <= 1:
            interpretation = "typical (within 1 SD)"
        elif abs(z) <= 2:
            interpretation = "somewhat unusual (between 1-2 SD)"
        else:
            interpretation = "unusual (beyond 2 SD)"
        
        question = f"For {name}: mean = {mean}, SD = {sd}. How would you describe a value of {value}?"
        correct = interpretation.capitalize()
        distractors = [
            "Typical (within 1 SD)" if interpretation != "typical (within 1 SD)" else "Very unusual (beyond 3 SD)",
            "Unusual (beyond 2 SD)" if interpretation != "unusual (beyond 2 SD)" else "Typical (within 1 SD)",
            "Cannot determine"
        ]
        
        options, idx = make_unique_options(correct, distractors)
        explanation = f"z = ({value} - {mean})/{sd} = {z}. This is {interpretation}"
        questions.append({
            'question_text': question, 'option_a': options[0], 'option_b': options[1],
            'option_c': options[2], 'option_d': options[3], 'correct_idx': idx,
            'explanation': explanation, 'difficulty': 12, 'difficulty_band': 'advanced'
        })
    
    return questions


def main():
    """Generate all questions and output SQL"""
    all_questions = []
    generators = [
        generate_level_1, generate_level_2, generate_level_3, generate_level_4,
        generate_level_5, generate_level_6, generate_level_7, generate_level_8,
        generate_level_9, generate_level_10, generate_level_11, generate_level_12,
    ]
    
    print(f"Generating questions for {TOPIC}...")
    print("=" * 60)
    
    for level, generator in enumerate(generators, 1):
        questions = generator()
        all_questions.extend(questions)
        print(f"Level {level:2d} ({LEVEL_TITLES[level-1]:25s}): {len(questions)} questions")
    
    print("=" * 60)
    print(f"Total questions generated: {len(all_questions)}")
    
    # Generate SQL statements
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
    
    # Create complete SQL file
    complete_sql = f"""-- LC Ordinary Level - Statistics (Descriptive) Complete SQL
-- Generated: 2025-12-15
-- Total: {len(all_questions)} questions across 12 levels

-- First, ensure LC Ordinary Level strand exists
INSERT OR IGNORE INTO strands (name, description, icon, sort_order)
VALUES ('LC Ordinary Level', 'Leaving Certificate Ordinary Level Mathematics', '📘', 50);

-- Add Statistics topic to LC Ordinary Level strand
INSERT OR IGNORE INTO topics (topic_id, display_name, strand_id, icon, sort_order, is_visible)
SELECT '{TOPIC}', 'Statistics', id, '📊', 4, 1
FROM strands WHERE name = 'LC Ordinary Level';

-- Verify topic was added
SELECT 'Topic added:' as info, topic_id, display_name FROM topics WHERE topic_id = '{TOPIC}';

-- Insert questions
{chr(10).join(sql_statements)}

-- Verify question count
SELECT 'Questions imported:' as info, COUNT(*) as count FROM questions_adaptive WHERE topic = '{TOPIC}';
"""
    
    with open('lc_ol_statistics_complete.sql', 'w', encoding='utf-8') as f:
        f.write(complete_sql)
    print(f"\nSQL written to: lc_ol_statistics_complete.sql")
    
    return all_questions


if __name__ == '__main__':
    main()
