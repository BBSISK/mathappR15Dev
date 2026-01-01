# ============================================================
# APP.PY UPDATE - PASSPORT TOPIC STRANDS
# ============================================================
# 
# INSTRUCTIONS:
# 1. Open app.py in a text editor
# 2. Find line 19622 (search for "PASSPORT_TOPIC_STRANDS = {")
# 3. Select from line 19622 to line 19793 (ends with PASSPORT_PLAN_CONFIG closing brace)
# 4. Delete those lines
# 5. Paste the content below in their place
# 6. Save and reload the web app
#
# Alternative: You can import from passport_config.py instead
# (see IMPORT_OPTION at bottom of this file)
#
# ============================================================

# ==================== PASSPORT TOPIC STRANDS ====================
# Revision 1.0 - 2025-12-23 - Fixed topic IDs to match database
# Each topic 'id' must match a topic_id from the database topics table

PASSPORT_TOPIC_STRANDS = {
    # ========== NUMERACY FOUNDATION (strand_id: 6) ==========
    'numeracy_foundation': {
        'id': 'numeracy_foundation',
        'display_name': 'Numeracy Foundation',
        'icon': '🔢',
        'colour': '#10b981',
        'topics': [
            {'id': 'whole_numbers', 'name': 'Whole Numbers'},
            {'id': 'addition_subtraction', 'name': 'Addition & Subtraction'},
            {'id': 'multiplication_skills', 'name': 'Multiplication'},
            {'id': 'division_skills', 'name': 'Division'},
            {'id': 'number_patterns', 'name': 'Number Patterns'},
            {'id': 'basic_fractions', 'name': 'Basic Fractions'},
            {'id': 'basic_decimals', 'name': 'Basic Decimals'},
            {'id': 'basic_percentages', 'name': 'Basic Percentages'},
            {'id': 'money_skills', 'name': 'Money Skills'},
            {'id': 'time_and_clocks', 'name': 'Time & Clocks'},
            {'id': 'measurement', 'name': 'Measurement'},
            {'id': 'data_and_charts', 'name': 'Data & Charts'},
        ]
    },
    
    # ========== NUMERACY ACTIVITIES / INTERACTIVE (strand_id: 10) ==========
    'numeracy_activities': {
        'id': 'numeracy_activities',
        'display_name': 'Numeracy Activities',
        'icon': '🎮',
        'colour': '#8b5cf6',
        'topics': [
            {'id': 'flow_sums', 'name': 'Flow Sums'},
            {'id': 'number_pyramids', 'name': 'Number Pyramids'},
            {'id': 'code_breaker', 'name': 'Code Breaker'},
            {'id': 'mastering_counting', 'name': 'Mastering Counting'},
            {'id': 'words_to_numbers', 'name': 'Words & Numbers'},
            {'id': 'ordering_magnitude', 'name': 'Ordering & Number Lines'},
            {'id': 'number_bonds', 'name': 'Number Bonds Pop'},
            {'id': 'place_value', 'name': 'Place Value Builder'},
            {'id': 'double_trouble', 'name': 'Double Trouble'},
            {'id': 'addition_blitz', 'name': 'Addition Blitz'},
            {'id': 'times_tables_blitz', 'name': 'Times Tables Blitz'},
        ]
    },
    
    # ========== NUMBER (JC - strand_id: 1) ==========
    'number': {
        'id': 'number',
        'display_name': 'Number',
        'icon': '🔢',
        'colour': '#3b82f6',
        'topics': [
            {'id': 'arithmetic', 'name': 'Arithmetic'},
            {'id': 'fractions', 'name': 'Fractions'},
            {'id': 'decimals', 'name': 'Decimals'},
            {'id': 'percentages', 'name': 'Percentages'},
            {'id': 'multiplication_division', 'name': 'Multiplication & Division'},
            {'id': 'bodmas', 'name': 'BODMAS'},
            {'id': 'number_systems', 'name': 'Number Systems'},
            {'id': 'indices', 'name': 'Indices & Scientific Notation'},
            {'id': 'sets', 'name': 'Sets'},
            {'id': 'currency', 'name': 'Currency'},
            {'id': 'speed_distance_time', 'name': 'Speed Distance Time'},
            {'id': 'applied_arithmetic', 'name': 'Applied Arithmetic (Financial Maths)'},
        ]
    },
    
    # ========== ALGEBRA (JC - strand_id: 2) ==========
    'algebra': {
        'id': 'algebra',
        'display_name': 'Algebra',
        'icon': '📐',
        'colour': '#8b5cf6',
        'topics': [
            {'id': 'introductory_algebra', 'name': 'Introductory Algebra'},
            {'id': 'simplifying_expressions', 'name': 'Simplifying Expressions'},
            {'id': 'solving_equations', 'name': 'Solving Equations'},
            {'id': 'expanding_factorising', 'name': 'Expanding & Factorising'},
            {'id': 'linear_inequalities', 'name': 'Linear Inequalities'},
            {'id': 'patterns', 'name': 'Patterns'},
            {'id': 'functions', 'name': 'Functions'},
            {'id': 'simultaneous_equations', 'name': 'Simultaneous Equations'},
            {'id': 'quadratic_equations', 'name': 'Quadratic Equations'},
            {'id': 'area_perimeter_volume', 'name': 'Area, Perimeter & Volume'},
        ]
    },
    
    # ========== STATISTICS & PROBABILITY (JC - strand_id: 3) ==========
    'statistics': {
        'id': 'statistics',
        'display_name': 'Statistics & Probability',
        'icon': '📊',
        'colour': '#f59e0b',
        'topics': [
            {'id': 'descriptive_statistics', 'name': 'Descriptive Statistics'},
            {'id': 'probability', 'name': 'Probability'},
        ]
    },
    
    # ========== GEOMETRY & TRIGONOMETRY (JC - strand_id: 5) ==========
    'geometry': {
        'id': 'geometry',
        'display_name': 'Geometry & Trigonometry',
        'icon': '📏',
        'colour': '#10b981',
        'topics': [
            {'id': 'geometry', 'name': 'Geometry'},
            {'id': 'coordinate_geometry', 'name': 'Coordinate Geometry'},
            {'id': 'trigonometry', 'name': 'Trigonometry'},
        ]
    },
    
    # ========== COMPLEX NUMBERS (LC - strand_id: 4) ==========
    'complex_numbers': {
        'id': 'complex_numbers',
        'display_name': 'Complex Numbers',
        'icon': '🔮',
        'colour': '#ec4899',
        'topics': [
            {'id': 'complex_numbers_intro', 'name': 'Complex Numbers Intro'},
            {'id': 'complex_numbers_expanded', 'name': 'Complex Numbers - Expanded'},
            {'id': 'surds', 'name': 'Surds'},
        ]
    },
    
    # ========== L1LP (strand_id: 7) ==========
    'l1lp': {
        'id': 'l1lp',
        'display_name': 'L1LP - Foundation',
        'icon': '🌱',
        'colour': '#22c55e',
        'topics': [
            {'id': 'developing_number_sense', 'name': 'Developing Number Sense'},
            {'id': 'pattern_and_sequence', 'name': 'Pattern & Sequence'},
            {'id': 'shape_and_space', 'name': 'Shape & Space'},
            {'id': 'measure_and_data', 'name': 'Measure & Data'},
            {'id': 'time', 'name': 'Time'},
            {'id': 'awareness_of_environment', 'name': 'Awareness of Environment'},
        ]
    },
    
    # ========== L2LP (strand_id: 8) ==========
    'l2lp': {
        'id': 'l2lp',
        'display_name': 'L2LP - Developing',
        'icon': '🌿',
        'colour': '#16a34a',
        'topics': [
            {'id': 'l2_number_and_money', 'name': 'Number & Money'},
            {'id': 'l2_shape_pattern_number', 'name': 'Shape, Pattern & Number'},
            {'id': 'l2_measurement_location', 'name': 'Measurement & Location'},
            {'id': 'l2_time_management', 'name': 'Time & Timetables'},
        ]
    },
    
    # ========== LC HIGHER LEVEL (strand_id: 9) ==========
    'lc_hl': {
        'id': 'lc_hl',
        'display_name': 'LC Higher Level',
        'icon': '🎓',
        'colour': '#7c3aed',
        'topics': [
            {'id': 'lc_hl_algebra', 'name': 'Algebra'},
            {'id': 'lc_hl_functions', 'name': 'Functions'},
            {'id': 'lc_hl_sequences', 'name': 'Sequences & Series'},
            {'id': 'lc_hl_complex', 'name': 'Complex Numbers'},
            {'id': 'lc_hl_calculus_diff', 'name': 'Calculus - Differentiation'},
            {'id': 'lc_hl_calculus_int', 'name': 'Calculus - Integration'},
            {'id': 'lc_hl_coord_geom', 'name': 'Coordinate Geometry'},
            {'id': 'lc_hl_trigonometry', 'name': 'Trigonometry'},
            {'id': 'lc_hl_geometry', 'name': 'Geometry'},
            {'id': 'lc_hl_probability', 'name': 'Probability'},
            {'id': 'lc_hl_statistics', 'name': 'Statistics'},
            {'id': 'lc_hl_counting', 'name': 'Counting & Combinatorics'},
            {'id': 'lc_hl_financial', 'name': 'Financial Maths'},
            {'id': 'lc_hl_mensuration', 'name': 'Measurement'},
            {'id': 'lc_hl_proof', 'name': 'Proof & Reasoning'},
        ]
    },
    
    # ========== LC ORDINARY LEVEL (strand_id: 11) ==========
    'lc_ol': {
        'id': 'lc_ol',
        'display_name': 'LC Ordinary Level',
        'icon': '📚',
        'colour': '#6366f1',
        'topics': [
            {'id': 'lc_ol_financial', 'name': 'Financial Maths'},
            {'id': 'lc_ol_probability', 'name': 'Probability'},
            {'id': 'lc_ol_statistics_desc', 'name': 'Statistics'},
            {'id': 'lc_ol_trigonometry', 'name': 'Trigonometry'},
            {'id': 'lc_ol_mensuration', 'name': 'Measurement'},
            {'id': 'lc_ol_applied_measure', 'name': 'Applied Measure'},
            {'id': 'lc_ol_calculus', 'name': 'Calculus'},
        ]
    },
}


# ==================== CURRICULUM HIERARCHY ====================
# Defines which strands are included in each curriculum level

CURRICULUM_HIERARCHY = {
    'L1LP': {
        'display_name': 'Level 1 Learning Programme',
        'description': 'Foundation skills for students with significant learning needs',
        'includes': ['l1lp', 'numeracy_activities'],
        'level': 1
    },
    'L2LP': {
        'display_name': 'Level 2 Learning Programme',
        'description': 'Developing skills for students with moderate learning needs',
        'includes': ['l1lp', 'l2lp', 'numeracy_foundation', 'numeracy_activities'],
        'level': 2
    },
    'JC': {
        'display_name': 'Junior Cycle',
        'description': 'Junior Cycle Mathematics (1st-3rd Year)',
        'includes': ['numeracy_foundation', 'numeracy_activities', 'number', 'algebra', 'statistics', 'geometry'],
        'level': 3
    },
    'LC_OL': {
        'display_name': 'Leaving Cert Ordinary Level',
        'description': 'Leaving Certificate Ordinary Level (5th-6th Year)',
        'includes': ['number', 'algebra', 'statistics', 'geometry', 'complex_numbers', 'lc_ol'],
        'level': 4
    },
    'LC_HL': {
        'display_name': 'Leaving Cert Higher Level',
        'description': 'Leaving Certificate Higher Level (5th-6th Year)',
        'includes': ['number', 'algebra', 'statistics', 'geometry', 'complex_numbers', 'lc_hl'],
        'level': 5
    }
}


# ==================== QUIZ CONFIGURATION ====================
# Distribution of questions by strand for diagnostic quiz

PASSPORT_QUIZ_CONFIG = {
    'total_questions': 25,
    'time_limit_minutes': 15,
    'strand_distribution': {
        'L1LP': {'l1lp': 20, 'numeracy_activities': 5},
        'L2LP': {'l1lp': 8, 'l2lp': 8, 'numeracy_foundation': 5, 'numeracy_activities': 4},
        'JC': {'numeracy_foundation': 4, 'number': 6, 'algebra': 6, 'geometry': 5, 'statistics': 4},
        'LC_OL': {'number': 4, 'algebra': 5, 'geometry': 4, 'statistics': 4, 'complex_numbers': 3, 'lc_ol': 5},
        'LC_HL': {'number': 3, 'algebra': 4, 'geometry': 3, 'statistics': 3, 'complex_numbers': 3, 'lc_hl': 9}
    }
}


# ==================== PLAN CONFIGURATION ====================
# Settings for weekly study plan generation

PASSPORT_PLAN_CONFIG = {
    'target_level': 12,
    'normal_hours_per_week': 3.5,
    'intensive_hours_holiday': 5.5,
    'light_hours_holiday': 1.5,
    'revision_weeks': 2,
    'intensive_threshold_months': 9
}


# ============================================================
# IMPORT OPTION (Alternative to copy-paste)
# ============================================================
#
# Instead of replacing the code above, you can use passport_config.py:
#
# 1. Upload passport_config.py to /home/bbsisk/mathappR15Dev/
#
# 2. At the top of app.py (around line 50), add:
#
#    from passport_config import (
#        PASSPORT_TOPIC_STRANDS, 
#        CURRICULUM_HIERARCHY,
#        PASSPORT_QUIZ_CONFIG,
#        PASSPORT_PLAN_CONFIG,
#        get_all_topics_for_curriculum
#    )
#
# 3. Delete lines 19622-19856 from app.py (the old constants and 
#    get_all_topics_for_curriculum function)
#
# This keeps app.py cleaner and makes future updates easier.
# ============================================================
