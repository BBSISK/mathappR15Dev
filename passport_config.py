# passport_config.py
# Passport/ILP configuration for AgentMath
# Extracted from app.py for better maintainability
#
# Revision: 1.0.0
# Date: 2025-12-27
#
# Contains:
# - PASSPORT_DESTINATIONS - Destination/topic mapping
# - PASSPORT_TOPIC_STRANDS - Topic structure by curriculum
# - CURRICULUM_HIERARCHY - Which strands belong to which curriculum
# - PASSPORT_QUIZ_CONFIG - Quiz settings
# - PASSPORT_PLAN_CONFIG - Weekly planning configuration
# - ILP_PREREQUISITE_MAP - Topic prerequisites
# - ILP_TOPIC_SKILL_TAGS - Skill tagging config
# - ILP_SKILL_TO_NUMERACY - Skill to numeracy mapping
# - ILP_THRESHOLDS - ILP recommendation thresholds
# - ILP_PRIORITY_CONFIG - Priority settings
# - Helper functions for passport calculations

PASSPORT_DESTINATIONS = {
    'algebra_alps': {
        'id': 'algebra_alps',
        'display_name': 'Algebra Alps',
        'icon': '🏔️',
        'colour': '#6366f1',
        'tagline': 'Conquer equations & expressions',
        'topics': ['introductory_algebra', 'solving_equations', 'simplifying_expressions', 'expanding_factorising', 'quadratic_equations', 'simultaneous_equations'],
        'curriculum': ['JC', 'LC_OL', 'LC_HL']
    },
    'number_explorers': {
        'id': 'number_explorers',
        'display_name': 'Number Explorers',
        'icon': '🔢',
        'colour': '#10b981',
        'tagline': 'Master fractions, decimals & percentages',
        'topics': ['fractions', 'decimals', 'percentages', 'arithmetic', 'bodmas', 'indices'],
        'curriculum': ['JC', 'LC_OL', 'LC_HL']
    },
    'function_factory': {
        'id': 'function_factory',
        'display_name': 'Function Factory',
        'icon': '⚙️',
        'colour': '#8b5cf6',
        'tagline': 'Build & graph functions',
        'topics': ['functions', 'patterns', 'coordinate_geometry', 'lc_hl_functions'],
        'curriculum': ['JC', 'LC_OL', 'LC_HL']
    },
    'geometry_gardens': {
        'id': 'geometry_gardens',
        'display_name': 'Geometry Gardens',
        'icon': '📐',
        'colour': '#f59e0b',
        'tagline': 'Explore shapes, angles & measurements',
        'topics': ['geometry', 'area_perimeter_volume', 'coordinate_geometry', 'lc_hl_geometry'],
        'curriculum': ['JC', 'LC_OL', 'LC_HL']
    },
    'stats_station': {
        'id': 'stats_station',
        'display_name': 'Stats Station',
        'icon': '📊',
        'colour': '#ec4899',
        'tagline': 'Decode data & probability',
        'topics': ['probability', 'descriptive_statistics', 'lc_hl_probability', 'lc_hl_statistics'],
        'curriculum': ['JC', 'LC_OL', 'LC_HL']
    },
    'trig_towers': {
        'id': 'trig_towers',
        'display_name': 'Trig Towers',
        'icon': '🗼',
        'colour': '#ef4444',
        'tagline': 'Master trigonometry & Pythagoras',
        'topics': ['trigonometry', 'lc_hl_trigonometry', 'lc_ol_trigonometry'],
        'curriculum': ['JC', 'LC_OL', 'LC_HL']
    },
    'numeracy_nation': {
        'id': 'numeracy_nation',
        'display_name': 'Numeracy Nation',
        'icon': '🧮',
        'colour': '#14b8a6',
        'tagline': 'Build core number skills',
        'topics': ['addition_subtraction', 'multiplication_skills', 'division_skills', 'whole_numbers', 'basic_fractions', 'basic_decimals'],
        'curriculum': ['L1LP', 'L2LP', 'JC']
    },
    'calculus_canyon': {
        'id': 'calculus_canyon',
        'display_name': 'Calculus Canyon',
        'icon': '🏜️',
        'colour': '#7c3aed',
        'tagline': 'Explore differentiation & integration',
        'topics': ['lc_hl_calculus_diff', 'lc_hl_calculus_int', 'lc_ol_calculus'],
        'curriculum': ['LC_OL', 'LC_HL']
    },
    'complex_castle': {
        'id': 'complex_castle',
        'display_name': 'Complex Castle',
        'icon': '🏰',
        'colour': '#db2777',
        'tagline': 'Master complex numbers & surds',
        'topics': ['complex_numbers_intro', 'complex_numbers_expanded', 'surds', 'lc_hl_complex'],
        'curriculum': ['LC_OL', 'LC_HL']
    },
    'financial_forest': {
        'id': 'financial_forest',
        'display_name': 'Financial Forest',
        'icon': '🌲',
        'colour': '#059669',
        'tagline': 'Navigate money & financial maths',
        'topics': ['applied_arithmetic', 'currency', 'lc_hl_financial', 'lc_ol_financial', 'money_skills'],
        'curriculum': ['JC', 'LC_OL', 'LC_HL']
    }
}

# =====================================================
# PASSPORT V2 - WEEKLY PLANNER CONFIGURATION
# =====================================================

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

# Plan configuration
PASSPORT_PLAN_CONFIG = {
    'target_level': 12,
    'normal_hours_per_week': 3.5,
    'intensive_hours_holiday': 5.5,
    'light_hours_holiday': 1.5,
    'revision_weeks': 2,
    'intensive_threshold_months': 9
}

# =====================================================
# ILP ENGINE - PREREQUISITE MAP & SKILL TAGGING
# Phase 12: Reactive Recommendations System
# =====================================================

# Complete prerequisite map for all topics
# Format: 'topic_id': ['prerequisite1', 'prerequisite2', ...]
# Topics with no prerequisites are entry points (base skills)

ILP_PREREQUISITE_MAP = {
    # ========== TIER 0: L1LP/L2LP (Learning Support) ==========
    'developing_number_sense': [],  # Base skill
    'pattern_and_sequence': ['developing_number_sense'],
    'shape_and_space': ['developing_number_sense'],
    'measure_and_data': ['developing_number_sense'],
    'time': ['developing_number_sense'],
    'awareness_of_environment': ['developing_number_sense'],
    'l2_number_and_money': ['developing_number_sense'],
    'l2_shape_pattern_number': ['pattern_and_sequence'],
    'l2_measurement_location': ['shape_and_space'],
    'l2_time_management': ['time'],
    
    # ========== TIER 1: Numeracy Foundation ==========
    'whole_numbers': [],  # Base skill
    'addition_subtraction': ['whole_numbers'],
    'multiplication_skills': ['addition_subtraction'],
    'division_skills': ['multiplication_skills'],
    'number_patterns': ['addition_subtraction'],
    'basic_fractions': ['division_skills'],
    'basic_decimals': ['basic_fractions', 'division_skills'],
    'basic_percentages': ['basic_fractions', 'basic_decimals'],
    'money_skills': ['basic_decimals', 'addition_subtraction'],
    'time_and_clocks': ['whole_numbers', 'addition_subtraction'],
    'measurement': ['multiplication_skills', 'basic_decimals'],
    'data_and_charts': ['whole_numbers', 'basic_fractions'],
    
    # ========== TIER 1.5: Numeracy Activities ==========
    'flow_sums': ['addition_subtraction'],
    'number_pyramids': ['addition_subtraction', 'multiplication_skills'],
    'code_breaker': ['addition_subtraction', 'multiplication_skills'],
    'addition_blitz': ['addition_subtraction'],
    'times_tables_blitz': ['multiplication_skills'],
    
    # ========== TIER 2: Junior Cycle Core ==========
    'arithmetic': ['addition_subtraction', 'multiplication_skills', 'division_skills'],
    'fractions': ['basic_fractions', 'multiplication_skills'],
    'decimals': ['basic_decimals', 'fractions'],
    'percentages': ['basic_percentages', 'fractions', 'decimals'],
    'bodmas': ['arithmetic'],
    'indices': ['multiplication_skills', 'bodmas'],
    'introductory_algebra': ['arithmetic', 'bodmas'],
    'simplifying_expressions': ['introductory_algebra'],
    'solving_equations': ['simplifying_expressions', 'fractions'],
    'expanding_factorising': ['simplifying_expressions', 'indices'],
    'sets': ['whole_numbers'],
    'patterns': ['number_patterns', 'introductory_algebra'],
    
    # ========== TIER 3: Junior Cycle Extended ==========
    'functions': ['solving_equations', 'patterns', 'coordinate_geometry'],
    'quadratic_equations': ['expanding_factorising', 'solving_equations'],
    'simultaneous_equations': ['solving_equations', 'coordinate_geometry'],
    'geometry': ['measurement', 'fractions'],
    'coordinate_geometry': ['introductory_algebra', 'fractions'],
    'trigonometry': ['geometry', 'fractions', 'solving_equations'],
    'probability': ['fractions', 'percentages'],
    'descriptive_statistics': ['fractions', 'percentages', 'arithmetic'],
    'area_perimeter_volume': ['geometry', 'multiplication_skills', 'fractions'],
    'speed_distance_time': ['fractions', 'solving_equations'],
    'currency': ['percentages', 'decimals'],
    'applied_arithmetic': ['percentages', 'fractions'],
    
    # ========== TIER 4: Leaving Cert Ordinary Level ==========
    'complex_numbers_intro': ['quadratic_equations', 'indices'],
    'surds': ['indices', 'fractions'],
    'lc_ol_trigonometry': ['trigonometry', 'solving_equations'],
    'lc_ol_calculus': ['functions', 'indices', 'solving_equations'],
    'lc_ol_financial': ['percentages', 'arithmetic'],
    'lc_ol_probability': ['probability', 'fractions'],
    'lc_ol_statistics_desc': ['descriptive_statistics'],
    'lc_ol_mensuration': ['area_perimeter_volume', 'trigonometry'],
    'lc_ol_applied_measure': ['measurement', 'percentages'],
    
    # ========== TIER 5: Leaving Cert Higher Level ==========
    'complex_numbers_expanded': ['complex_numbers_intro', 'trigonometry'],
    'lc_hl_algebra': ['quadratic_equations', 'simultaneous_equations'],
    'lc_hl_functions': ['functions', 'lc_hl_algebra'],
    'lc_hl_calculus_diff': ['lc_ol_calculus', 'lc_hl_functions', 'indices'],
    'lc_hl_calculus_int': ['lc_hl_calculus_diff'],
    'lc_hl_trigonometry': ['lc_ol_trigonometry', 'lc_hl_algebra'],
    'lc_hl_complex': ['complex_numbers_expanded', 'lc_hl_trigonometry'],
    'lc_hl_coord_geom': ['coordinate_geometry', 'lc_hl_algebra'],
    'lc_hl_probability': ['lc_ol_probability', 'lc_hl_counting'],
    'lc_hl_statistics': ['lc_ol_statistics_desc', 'probability'],
    'lc_hl_counting': ['indices', 'multiplication_skills'],
    'lc_hl_financial': ['lc_ol_financial', 'indices'],
    'lc_hl_proof': ['lc_hl_algebra', 'indices'],
    'lc_hl_mensuration': ['lc_ol_mensuration', 'lc_hl_calculus_int'],
    'lc_hl_geometry': ['geometry', 'lc_hl_coord_geom'],
}

# Skill tags auto-assigned to questions based on topic
# Format: 'topic_id': [('skill_tag', weight), ...]
# Weight: 1.0 = primary skill, 0.5 = supporting skill, 0.3 = minor skill

ILP_TOPIC_SKILL_TAGS = {
    # Numeracy Foundation
    'whole_numbers': [('number_recognition', 1.0), ('place_value', 1.0)],
    'addition_subtraction': [('arithmetic_addition', 1.0), ('arithmetic_subtraction', 1.0), ('mental_math', 0.5)],
    'multiplication_skills': [('arithmetic_multiplication', 1.0), ('times_tables', 1.0), ('mental_math', 0.5)],
    'division_skills': [('arithmetic_division', 1.0), ('mental_math', 0.5)],
    'basic_fractions': [('fraction_recognition', 1.0), ('fraction_equivalence', 0.8), ('arithmetic_division', 0.5)],
    'basic_decimals': [('decimal_recognition', 1.0), ('place_value', 0.8), ('fraction_decimal_conversion', 0.5)],
    'basic_percentages': [('percentage_recognition', 1.0), ('fraction_decimal_conversion', 0.5)],
    'number_patterns': [('pattern_recognition', 1.0), ('arithmetic_addition', 0.5)],
    'money_skills': [('decimal_operations', 1.0), ('arithmetic_addition', 0.5), ('arithmetic_subtraction', 0.5)],
    'time_and_clocks': [('time_reading', 1.0), ('time_calculation', 1.0), ('arithmetic_addition', 0.3)],
    'measurement': [('unit_conversion', 1.0), ('arithmetic_multiplication', 0.5)],
    'data_and_charts': [('graph_reading', 1.0), ('data_interpretation', 1.0)],
    
    # Numeracy Activities
    'flow_sums': [('arithmetic_addition', 1.0), ('arithmetic_subtraction', 1.0), ('mental_math', 1.0)],
    'number_pyramids': [('arithmetic_addition', 1.0), ('pattern_recognition', 0.8), ('mental_math', 1.0)],
    'code_breaker': [('arithmetic_multiplication', 1.0), ('arithmetic_division', 1.0), ('mental_math', 1.0)],
    'addition_blitz': [('arithmetic_addition', 1.0), ('mental_math', 1.0), ('speed_accuracy', 1.0)],
    'times_tables_blitz': [('times_tables', 1.0), ('arithmetic_multiplication', 1.0), ('speed_accuracy', 1.0)],
    
    # Junior Cycle Core
    'arithmetic': [('arithmetic_addition', 1.0), ('arithmetic_subtraction', 1.0), ('arithmetic_multiplication', 1.0), ('arithmetic_division', 1.0), ('negative_numbers', 0.8)],
    'fractions': [('fraction_operations', 1.0), ('fraction_simplify', 1.0), ('fraction_multiply', 1.0), ('fraction_divide', 0.8), ('mixed_numbers', 0.8)],
    'decimals': [('decimal_operations', 1.0), ('decimal_multiply', 1.0), ('decimal_divide', 0.8), ('rounding', 0.5)],
    'percentages': [('percentage_calculation', 1.0), ('percentage_increase_decrease', 1.0), ('fraction_decimal_conversion', 0.8)],
    'bodmas': [('order_of_operations', 1.0), ('bracket_evaluation', 1.0), ('arithmetic_all', 0.8)],
    'indices': [('index_laws', 1.0), ('index_multiply', 1.0), ('index_divide', 1.0), ('negative_index', 0.8), ('fractional_index', 0.5)],
    'introductory_algebra': [('variable_understanding', 1.0), ('expression_evaluation', 1.0), ('substitution', 1.0)],
    'simplifying_expressions': [('like_terms', 1.0), ('expression_simplify', 1.0), ('variable_manipulation', 1.0)],
    'solving_equations': [('equation_balancing', 1.0), ('variable_isolation', 1.0), ('inverse_operations', 1.0), ('arithmetic_all', 0.5), ('fraction_operations', 0.5)],
    'expanding_factorising': [('expanding_brackets', 1.0), ('factoring', 1.0), ('like_terms', 0.8), ('arithmetic_multiplication', 0.5)],
    'sets': [('set_notation', 1.0), ('set_operations', 1.0), ('venn_diagrams', 0.8)],
    'patterns': [('pattern_recognition', 1.0), ('sequence_nth_term', 1.0), ('arithmetic_sequences', 0.8)],
    
    # Junior Cycle Extended
    'functions': [('function_notation', 1.0), ('function_evaluation', 1.0), ('domain_range', 0.8), ('graph_interpretation', 0.8)],
    'quadratic_equations': [('quadratic_factoring', 1.0), ('quadratic_formula', 1.0), ('completing_square', 0.8), ('discriminant', 0.5)],
    'simultaneous_equations': [('simultaneous_substitution', 1.0), ('simultaneous_elimination', 1.0), ('equation_balancing', 0.8)],
    'geometry': [('angle_calculation', 1.0), ('shape_properties', 1.0), ('geometric_reasoning', 0.8)],
    'coordinate_geometry': [('coordinate_plotting', 1.0), ('slope_calculation', 1.0), ('distance_formula', 0.8), ('midpoint_formula', 0.8), ('negative_numbers', 0.5)],
    'trigonometry': [('trig_ratios', 1.0), ('trig_equations', 1.0), ('pythagoras', 1.0), ('angle_calculation', 0.8), ('fraction_operations', 0.5)],
    'probability': [('probability_calculation', 1.0), ('probability_trees', 0.8), ('expected_value', 0.5), ('fraction_operations', 0.5)],
    'descriptive_statistics': [('mean_median_mode', 1.0), ('data_interpretation', 1.0), ('frequency_tables', 0.8), ('standard_deviation', 0.5)],
    'area_perimeter_volume': [('area_formulas', 1.0), ('perimeter_formulas', 1.0), ('volume_formulas', 1.0), ('unit_conversion', 0.5)],
    'speed_distance_time': [('sdt_formula', 1.0), ('unit_conversion', 0.8), ('equation_rearranging', 0.8)],
    'currency': [('exchange_rate', 1.0), ('percentage_calculation', 0.8), ('decimal_operations', 0.5)],
    'applied_arithmetic': [('percentage_calculation', 1.0), ('profit_loss', 1.0), ('compound_interest', 0.8)],
    
    # Leaving Cert Topics
    'complex_numbers_intro': [('complex_arithmetic', 1.0), ('argand_diagram', 0.8), ('conjugate', 0.8)],
    'complex_numbers_expanded': [('complex_polar', 1.0), ('de_moivre', 1.0), ('complex_roots', 0.8)],
    'surds': [('surd_simplify', 1.0), ('surd_operations', 1.0), ('rationalising', 0.8)],
    'lc_ol_trigonometry': [('trig_ratios', 1.0), ('trig_identities', 0.8), ('trig_equations', 1.0)],
    'lc_ol_calculus': [('differentiation_basic', 1.0), ('integration_basic', 1.0), ('slope_tangent', 0.8)],
    'lc_ol_financial': [('compound_interest', 1.0), ('depreciation', 1.0), ('tax_calculation', 0.8)],
    'lc_ol_probability': [('probability_calculation', 1.0), ('conditional_probability', 0.8), ('bernoulli', 0.5)],
    'lc_ol_statistics_desc': [('mean_median_mode', 1.0), ('standard_deviation', 1.0), ('data_interpretation', 0.8)],
    'lc_hl_algebra': [('polynomial_division', 1.0), ('factor_theorem', 1.0), ('algebraic_manipulation', 1.0)],
    'lc_hl_functions': [('function_composition', 1.0), ('inverse_functions', 1.0), ('transformations', 0.8)],
    'lc_hl_calculus_diff': [('differentiation_rules', 1.0), ('chain_rule', 1.0), ('product_quotient', 1.0), ('maxima_minima', 0.8)],
    'lc_hl_calculus_int': [('integration_rules', 1.0), ('integration_by_parts', 0.8), ('definite_integrals', 1.0), ('area_under_curve', 0.8)],
    'lc_hl_trigonometry': [('trig_identities', 1.0), ('trig_equations', 1.0), ('inverse_trig', 0.8)],
    'lc_hl_complex': [('complex_polar', 1.0), ('de_moivre', 1.0), ('complex_roots', 1.0)],
    'lc_hl_coord_geom': [('line_equations', 1.0), ('circle_equations', 1.0), ('tangent_normal', 0.8)],
    'lc_hl_probability': [('conditional_probability', 1.0), ('bayes_theorem', 0.8), ('distributions', 1.0)],
    'lc_hl_statistics': [('hypothesis_testing', 1.0), ('confidence_intervals', 1.0), ('correlation', 0.8)],
    'lc_hl_counting': [('permutations', 1.0), ('combinations', 1.0), ('factorial', 0.8)],
    'lc_hl_financial': [('amortisation', 1.0), ('present_value', 1.0), ('geometric_series', 0.8)],
    'lc_hl_proof': [('proof_by_induction', 1.0), ('proof_by_contradiction', 0.8), ('logical_reasoning', 1.0)],
}

# Maps skill gaps to remedial numeracy topics
# When a skill tag shows weakness, recommend these foundation topics

ILP_SKILL_TO_NUMERACY = {
    # Arithmetic skills → Numeracy topics
    'arithmetic_addition': ['addition_subtraction', 'flow_sums', 'addition_blitz'],
    'arithmetic_subtraction': ['addition_subtraction', 'flow_sums'],
    'arithmetic_multiplication': ['multiplication_skills', 'times_tables_blitz', 'code_breaker'],
    'arithmetic_division': ['division_skills', 'code_breaker'],
    'times_tables': ['multiplication_skills', 'times_tables_blitz'],
    'mental_math': ['addition_blitz', 'times_tables_blitz', 'flow_sums'],
    'negative_numbers': ['arithmetic', 'addition_subtraction'],
    'arithmetic_all': ['arithmetic', 'addition_subtraction', 'multiplication_skills', 'division_skills'],
    
    # Fraction skills → Numeracy topics
    'fraction_operations': ['basic_fractions', 'fractions'],
    'fraction_recognition': ['basic_fractions'],
    'fraction_equivalence': ['basic_fractions'],
    'fraction_simplify': ['basic_fractions', 'division_skills'],
    'fraction_multiply': ['basic_fractions', 'multiplication_skills'],
    'fraction_divide': ['basic_fractions', 'division_skills'],
    'mixed_numbers': ['basic_fractions', 'fractions'],
    
    # Decimal/Percentage skills → Numeracy topics
    'decimal_operations': ['basic_decimals', 'decimals'],
    'decimal_recognition': ['basic_decimals'],
    'decimal_multiply': ['basic_decimals', 'multiplication_skills'],
    'decimal_divide': ['basic_decimals', 'division_skills'],
    'percentage_calculation': ['basic_percentages', 'percentages'],
    'fraction_decimal_conversion': ['basic_fractions', 'basic_decimals'],
    
    # Pattern/Number sense → Numeracy topics
    'pattern_recognition': ['number_patterns', 'number_pyramids'],
    'place_value': ['whole_numbers', 'basic_decimals'],
    'number_recognition': ['whole_numbers'],
    
    # Algebra foundations → Pre-algebra topics
    'order_of_operations': ['bodmas', 'arithmetic'],
    'bracket_evaluation': ['bodmas'],
    'variable_understanding': ['introductory_algebra', 'patterns'],
    'expression_evaluation': ['introductory_algebra', 'bodmas'],
    'substitution': ['introductory_algebra'],
    'like_terms': ['simplifying_expressions'],
    'equation_balancing': ['solving_equations', 'arithmetic'],
    'inverse_operations': ['solving_equations', 'arithmetic'],
}

# ILP Analysis thresholds
ILP_THRESHOLDS = {
    'low_accuracy': 0.5,           # Below 50% = struggling
    'critical_accuracy': 0.3,      # Below 30% = critical
    'numeracy_trigger': 0.4,       # Below 40% on numeracy skill = insert remedial
    'min_questions_for_signal': 10, # Need at least 10 questions to judge
    'plateau_days': 7,             # Same level for 7 days = plateau
    'plateau_min_questions': 15,   # Need 15+ questions to detect plateau
    'rust_days': 14,               # 14 days without practice = rust alert
    'skip_rate_threshold': 0.3,    # Skipping 30%+ = avoidance
    'confidence_gap_threshold': 2, # Self-rating 2+ levels above actual = mismatch
    'max_weekly_topics': 3,        # Maximum topics per week in plan
    'auto_apply_hours': 24,        # Hours before auto-applying recommendations
    'bronze_level': 4,             # Level needed for bronze stamp
    'silver_level': 7,             # Level needed for silver stamp
    'gold_level': 10,              # Level needed for gold stamp
}

# Priority levels for recommendations
ILP_PRIORITY_CONFIG = {
    'critical': {
        'label': 'Critical',
        'colour': '#ef4444',  # Red
        'auto_apply': True,
        'apply_hours': 24,
        'description': 'Severe foundation gaps requiring immediate attention'
    },
    'high': {
        'label': 'High Priority',
        'colour': '#f97316',  # Orange
        'auto_apply': True,
        'apply_hours': 24,
        'description': 'Prerequisite gaps affecting current learning'
    },
    'medium': {
        'label': 'Recommended',
        'colour': '#eab308',  # Yellow
        'auto_apply': True,
        'apply_hours': 48,
        'description': 'Consolidation needed for better progress'
    },
    'low': {
        'label': 'Suggestion',
        'colour': '#3b82f6',  # Blue
        'auto_apply': False,
        'apply_hours': None,
        'description': 'Optional improvement opportunity'
    }
}


def get_all_topics_for_curriculum(curriculum):
    """Get all topics for a curriculum based on hierarchy"""
    if curriculum not in CURRICULUM_HIERARCHY:
        curriculum = 'JC'
    
    strand_ids = CURRICULUM_HIERARCHY[curriculum]['includes']
    topics = []
    
    for strand_id in strand_ids:
        if strand_id in PASSPORT_TOPIC_STRANDS:
            strand = PASSPORT_TOPIC_STRANDS[strand_id]
            for topic in strand['topics']:
                topics.append({
                    'topic_id': topic['id'],
                    'topic_name': topic['name'],
                    'strand_id': strand_id,
                    'strand_name': strand['display_name'],
                    'strand_icon': strand['icon']
                })
    
    return topics


def calculate_entry_level_v2(progress_level, confidence, quiz_score):
    """Calculate entry level from multiple factors"""
    # Start with progress level (0-12)
    base = progress_level if progress_level else 1
    
    # Adjust for confidence (1=need help, 2=okay, 3=confident)
    if confidence == 1:
        base = max(1, base - 2)
    elif confidence == 3:
        base = min(12, base + 1)
    
    # Adjust for quiz score if available
    if quiz_score is not None:
        if quiz_score >= 80:
            base = min(12, base + 2)
        elif quiz_score >= 60:
            base = min(12, base + 1)
        elif quiz_score < 40:
            base = max(1, base - 1)
    
    return max(1, min(12, base))


def calculate_topic_priority_v2(entry_level, confidence):
    """Calculate priority score for topic ordering"""
    # Higher priority for lower entry levels and lower confidence
    gap_to_mastery = 12 - entry_level
    confidence_weight = (4 - confidence) * 3  # 1->9, 2->6, 3->3
    return gap_to_mastery + confidence_weight


def calculate_target_level_v2(entry_level, weeks_available):
    """Calculate realistic target level based on time"""
    # Assume 1-2 levels of progress per week of focused study
    progress_rate = 1.5
    max_progress = int(weeks_available * progress_rate)
    target = min(12, entry_level + max_progress)
    return max(entry_level + 1, target)  # At least 1 level improvement


def get_week_capacity_from_calendar(week_start, exam_date, calendar_events, intensive_mode):
    """Determine week capacity based on calendar"""
    from datetime import timedelta
    
    week_end = week_start + timedelta(days=6)
    
    # Check for holidays/breaks in this week
    holiday_name = None
    for event in calendar_events:
        event_start = event['start_date'] if isinstance(event['start_date'], date) else datetime.strptime(event['start_date'], '%Y-%m-%d').date()
        event_end = event['end_date'] if isinstance(event['end_date'], date) else datetime.strptime(event['end_date'], '%Y-%m-%d').date()
        
        # Check if week overlaps with event
        if event_start <= week_end and event_end >= week_start:
            holiday_name = event['event_name']
            break
    
    # Determine capacity based on whether it's a holiday and mode
    if holiday_name:
        if intensive_mode:
            return {
                'hours': PASSPORT_PLAN_CONFIG['intensive_hours_holiday'],
                'max_topics': 4,
                'capacity_type': 'intensive',
                'holiday_name': holiday_name,
                'focus_area': 'Holiday intensive study'
            }
        else:
            return {
                'hours': PASSPORT_PLAN_CONFIG['light_hours_holiday'],
                'max_topics': 1,
                'capacity_type': 'light',
                'holiday_name': holiday_name,
                'focus_area': 'Light holiday practice'
            }
    else:
        return {
            'hours': PASSPORT_PLAN_CONFIG['normal_hours_per_week'],
            'max_topics': 3,
            'capacity_type': 'normal',
            'holiday_name': None,
            'focus_area': 'Regular study week'
        }

