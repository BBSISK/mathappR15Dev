"""
MATHS PASSPORT V2 - CONFIGURATION CODE
Add this code to app.py after the existing PASSPORT_DESTINATIONS

This file contains:
1. Topic strands for granular self-assessment
2. Curriculum hierarchy (cumulative model)
3. Irish school calendar helper functions
4. Entry level calculation logic
5. 25-question quiz configuration
"""

# =========================================================
# TOPIC STRANDS - For granular self-assessment
# Each strand contains individual topics that can be rated
# =========================================================

PASSPORT_TOPIC_STRANDS = {
    'numeracy': {
        'id': 'numeracy',
        'display_name': 'Numeracy',
        'icon': '🧮',
        'curriculum': ['Primary', 'L1LP', 'L2LP', 'JC', 'LC_OL', 'LC_HL'],
        'topics': [
            {'id': 'addition', 'name': 'Addition', 'difficulty': 1},
            {'id': 'subtraction', 'name': 'Subtraction', 'difficulty': 1},
            {'id': 'multiplication', 'name': 'Multiplication', 'difficulty': 2},
            {'id': 'division', 'name': 'Division', 'difficulty': 2},
            {'id': 'number_operations', 'name': 'Mixed Operations', 'difficulty': 3},
        ]
    },
    'number': {
        'id': 'number',
        'display_name': 'Number Skills',
        'icon': '🔢',
        'curriculum': ['L2LP', 'JC', 'LC_OL', 'LC_HL'],
        'topics': [
            {'id': 'fractions', 'name': 'Fractions', 'difficulty': 3},
            {'id': 'decimals', 'name': 'Decimals', 'difficulty': 3},
            {'id': 'percentages', 'name': 'Percentages', 'difficulty': 4},
            {'id': 'ratio', 'name': 'Ratio & Proportion', 'difficulty': 4},
            {'id': 'indices', 'name': 'Indices & Powers', 'difficulty': 5},
        ]
    },
    'algebra': {
        'id': 'algebra',
        'display_name': 'Algebra',
        'icon': '🏔️',
        'curriculum': ['JC', 'LC_OL', 'LC_HL'],
        'topics': [
            {'id': 'introductory_algebra', 'name': 'Expressions', 'difficulty': 4},
            {'id': 'solving_equations', 'name': 'Solving Equations', 'difficulty': 5},
            {'id': 'simplifying_expressions', 'name': 'Simplifying', 'difficulty': 5},
            {'id': 'expanding_factorising', 'name': 'Expanding & Factorising', 'difficulty': 6},
            {'id': 'inequalities', 'name': 'Inequalities', 'difficulty': 6},
        ]
    },
    'geometry': {
        'id': 'geometry',
        'display_name': 'Geometry',
        'icon': '📐',
        'curriculum': ['JC', 'LC_OL', 'LC_HL'],
        'topics': [
            {'id': 'area', 'name': 'Area & Perimeter', 'difficulty': 4},
            {'id': 'angles', 'name': 'Angles', 'difficulty': 4},
            {'id': 'triangles', 'name': 'Triangles', 'difficulty': 5},
            {'id': 'geometry', 'name': 'Shapes & Properties', 'difficulty': 5},
            {'id': 'circle_geometry', 'name': 'Circles', 'difficulty': 6},
            {'id': 'coordinate_geometry', 'name': 'Coordinate Geometry', 'difficulty': 6},
        ]
    },
    'functions': {
        'id': 'functions',
        'display_name': 'Functions & Graphs',
        'icon': '⚙️',
        'curriculum': ['JC', 'LC_OL', 'LC_HL'],
        'topics': [
            {'id': 'functions', 'name': 'Functions', 'difficulty': 5},
            {'id': 'graphs', 'name': 'Reading Graphs', 'difficulty': 4},
            {'id': 'linear_functions', 'name': 'Linear Functions', 'difficulty': 5},
            {'id': 'quadratic_functions', 'name': 'Quadratic Functions', 'difficulty': 7},
        ]
    },
    'statistics': {
        'id': 'statistics',
        'display_name': 'Statistics & Probability',
        'icon': '📊',
        'curriculum': ['JC', 'LC_OL', 'LC_HL'],
        'topics': [
            {'id': 'data_analysis', 'name': 'Data Analysis', 'difficulty': 4},
            {'id': 'mean_median_mode', 'name': 'Mean, Median & Mode', 'difficulty': 4},
            {'id': 'statistics', 'name': 'Statistics', 'difficulty': 5},
            {'id': 'probability', 'name': 'Probability', 'difficulty': 5},
        ]
    },
    'trigonometry': {
        'id': 'trigonometry',
        'display_name': 'Trigonometry',
        'icon': '🗼',
        'curriculum': ['JC', 'LC_OL', 'LC_HL'],
        'topics': [
            {'id': 'pythagoras', 'name': 'Pythagoras', 'difficulty': 5},
            {'id': 'trigonometry', 'name': 'Trigonometry', 'difficulty': 6},
            {'id': 'right_angled_triangles', 'name': 'Right-Angled Triangles', 'difficulty': 6},
        ]
    },
    # L1LP Specific
    'l1lp_number': {
        'id': 'l1lp_number',
        'display_name': 'L1LP Number',
        'icon': '🔢',
        'curriculum': ['L1LP', 'L2LP'],
        'topics': [
            {'id': 'l1lp_counting', 'name': 'Counting', 'difficulty': 1},
            {'id': 'l1lp_ordering', 'name': 'Ordering Numbers', 'difficulty': 1},
            {'id': 'l1lp_place_value', 'name': 'Place Value', 'difficulty': 2},
            {'id': 'l1lp_money', 'name': 'Money', 'difficulty': 2},
        ]
    },
    # L2LP Specific
    'l2lp_number': {
        'id': 'l2lp_number',
        'display_name': 'L2LP Number',
        'icon': '🔢',
        'curriculum': ['L2LP', 'JC'],
        'topics': [
            {'id': 'l2lp_whole_numbers', 'name': 'Whole Numbers', 'difficulty': 2},
            {'id': 'l2lp_fractions_intro', 'name': 'Fractions (Intro)', 'difficulty': 3},
            {'id': 'l2lp_decimals_intro', 'name': 'Decimals (Intro)', 'difficulty': 3},
            {'id': 'l2lp_percentages_intro', 'name': 'Percentages (Intro)', 'difficulty': 3},
        ]
    },
}

# =========================================================
# CURRICULUM HIERARCHY - Cumulative model
# Each level includes all levels below it
# =========================================================

CURRICULUM_HIERARCHY = {
    'Primary': {
        'display_name': 'Primary Numeracy',
        'icon': '🔢',
        'includes': ['numeracy'],
        'order': 1
    },
    'L1LP': {
        'display_name': 'Level 1 Learning Programme',
        'icon': '📓',
        'includes': ['numeracy', 'l1lp_number'],
        'order': 2
    },
    'L2LP': {
        'display_name': 'Level 2 Learning Programme', 
        'icon': '📕',
        'includes': ['numeracy', 'l1lp_number', 'l2lp_number'],
        'order': 3
    },
    'JC': {
        'display_name': 'Junior Cycle',
        'icon': '📗',
        'includes': ['numeracy', 'l1lp_number', 'l2lp_number', 'number', 'algebra', 'geometry', 'functions', 'statistics', 'trigonometry'],
        'order': 4
    },
    'LC_OL': {
        'display_name': 'Leaving Cert (Ordinary)',
        'icon': '📙',
        'includes': ['numeracy', 'l1lp_number', 'l2lp_number', 'number', 'algebra', 'geometry', 'functions', 'statistics', 'trigonometry'],
        'order': 5
    },
    'LC_HL': {
        'display_name': 'Leaving Cert (Higher)',
        'icon': '📘',
        'includes': ['numeracy', 'l1lp_number', 'l2lp_number', 'number', 'algebra', 'geometry', 'functions', 'statistics', 'trigonometry'],
        'order': 6
    }
}

# =========================================================
# 25-QUESTION QUIZ CONFIGURATION
# =========================================================

PASSPORT_QUIZ_CONFIG = {
    'total_questions': 25,
    'difficulty_mix': {
        'easy': 8,      # L1-4 questions
        'medium': 10,   # L5-7 questions  
        'hard': 7       # L8-10 questions
    },
    'strand_distribution': {
        # For JC - adjust based on curriculum
        'JC': {
            'number': 5,
            'algebra': 5,
            'geometry': 4,
            'functions': 4,
            'statistics': 4,
            'trigonometry': 3
        },
        'L2LP': {
            'numeracy': 8,
            'l2lp_number': 10,
            'l1lp_number': 7
        },
        'L1LP': {
            'numeracy': 15,
            'l1lp_number': 10
        },
        'Primary': {
            'numeracy': 25
        }
    }
}

# =========================================================
# WEEKLY PLAN CONFIGURATION
# =========================================================

PASSPORT_PLAN_CONFIG = {
    'normal_hours_per_week': 3.5,
    'max_topics_per_week': {
        'normal': 3,
        'intensive': 4,
        'light': 1
    },
    'intensive_threshold_months': 9,  # If < 9 months to exam, holidays = intensive
    'entry_level_cap': 10,  # Maximum entry level (always leave room to grow)
    'questions_per_level': 17,  # Approx questions to advance one level
    'revision_weeks': 2  # Reserve last N weeks for revision
}


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def get_strands_for_curriculum(curriculum):
    """Get all topic strands available for a curriculum level"""
    if curriculum not in CURRICULUM_HIERARCHY:
        curriculum = 'JC'  # Default
    
    included_strands = CURRICULUM_HIERARCHY[curriculum]['includes']
    strands = {}
    
    for strand_id in included_strands:
        if strand_id in PASSPORT_TOPIC_STRANDS:
            strands[strand_id] = PASSPORT_TOPIC_STRANDS[strand_id]
    
    return strands


def get_all_topics_for_curriculum(curriculum):
    """Get flat list of all topics for a curriculum"""
    strands = get_strands_for_curriculum(curriculum)
    topics = []
    
    for strand_id, strand in strands.items():
        for topic in strand['topics']:
            topics.append({
                'topic_id': topic['id'],
                'topic_name': topic['name'],
                'strand_id': strand_id,
                'strand_name': strand['display_name'],
                'strand_icon': strand['icon'],
                'difficulty': topic['difficulty']
            })
    
    return topics


def calculate_entry_level(progress_level, confidence, quiz_score):
    """
    Calculate entry level for a topic based on:
    - progress_level: Current level from adaptive_progress (0-12)
    - confidence: Self-assessment rating (1=Need Help, 2=Okay, 3=Confident)
    - quiz_score: Percentage score from diagnostic quiz (0-100, or None if not tested)
    
    Returns: Entry level (1-10, capped)
    """
    # Start with progress level (or 1 if no progress)
    base_level = max(1, progress_level) if progress_level else 1
    
    # Apply confidence modifier
    if confidence == 1:  # Need Help
        adjusted = base_level - 1 if progress_level else 1
    elif confidence == 3:  # Confident
        adjusted = base_level + 1 if progress_level else 3
    else:  # Okay
        adjusted = base_level
    
    # Apply quiz modifier if tested
    if quiz_score is not None:
        if quiz_score >= 80:
            adjusted += 2
        elif quiz_score < 50:
            adjusted -= 2
    
    # Cap at 10 (always leave room to grow to L11-12)
    entry_level = max(1, min(adjusted, PASSPORT_PLAN_CONFIG['entry_level_cap']))
    
    return entry_level


def calculate_target_level(entry_level, weeks_remaining):
    """
    Calculate realistic target level based on:
    - entry_level: Starting level
    - weeks_remaining: Weeks until exam
    
    Returns: Target level (entry_level+1 to 12)
    """
    if weeks_remaining > 20:
        # Plenty of time - aim for mastery
        target = 12
    elif weeks_remaining > 10:
        # Moderate time - aim for competence
        target = min(entry_level + 6, 10)
    else:
        # Limited time - aim for improvement
        target = min(entry_level + 3, 8)
    
    # Never set target below entry + 1
    target = max(target, entry_level + 1)
    
    return min(target, 12)


def calculate_topic_priority(entry_level, confidence, max_level=12):
    """
    Calculate priority score for a topic.
    Higher score = higher priority (should be tackled earlier)
    
    Returns: Priority score (0-20+)
    """
    gap_to_mastery = max_level - entry_level
    confidence_weight = (4 - confidence) * 3  # 1→9, 2→6, 3→3
    
    priority_score = gap_to_mastery + confidence_weight
    return priority_score


def get_week_capacity(week_date, exam_date, calendar_events):
    """
    Determine the capacity type for a given week.
    
    Returns: dict with capacity_type, hours, holiday_name
    """
    from datetime import datetime, timedelta
    
    # Calculate months to exam
    if exam_date:
        days_to_exam = (exam_date - week_date).days
        months_to_exam = days_to_exam / 30
        intensive_mode = months_to_exam < PASSPORT_PLAN_CONFIG['intensive_threshold_months']
    else:
        intensive_mode = False  # No exam = normal mode
    
    # Check if week falls in any calendar event
    for event in calendar_events:
        event_start = datetime.strptime(event['start_date'], '%Y-%m-%d').date() if isinstance(event['start_date'], str) else event['start_date']
        event_end = datetime.strptime(event['end_date'], '%Y-%m-%d').date() if isinstance(event['end_date'], str) else event['end_date']
        
        # Check if week overlaps with event
        week_end = week_date + timedelta(days=6)
        if not (week_end < event_start or week_date > event_end):
            # Week overlaps with this event
            if intensive_mode:
                # Close to exam - holidays = intensive study time
                return {
                    'capacity_type': 'intensive',
                    'hours': 5.5,
                    'holiday_name': event['event_name'],
                    'max_topics': PASSPORT_PLAN_CONFIG['max_topics_per_week']['intensive']
                }
            else:
                # Far from exam - holidays = light study
                return {
                    'capacity_type': 'light',
                    'hours': 1.5,
                    'holiday_name': event['event_name'],
                    'max_topics': PASSPORT_PLAN_CONFIG['max_topics_per_week']['light']
                }
    
    # Normal week
    return {
        'capacity_type': 'normal',
        'hours': PASSPORT_PLAN_CONFIG['normal_hours_per_week'],
        'holiday_name': None,
        'max_topics': PASSPORT_PLAN_CONFIG['max_topics_per_week']['normal']
    }


# =========================================================
# EXAMPLE: Get topics for Junior Cycle student
# =========================================================
# topics = get_all_topics_for_curriculum('JC')
# print(f"JC has {len(topics)} topics across {len(get_strands_for_curriculum('JC'))} strands")
