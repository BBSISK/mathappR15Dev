"""
Adaptive Quiz Engine Patches for Levels 11-12
=============================================

Copy these functions into adaptive_quiz_engine.py

Changes:
1. adjust_level() - Update cap from 10 to 12
2. check_level_12_unlock() - NEW function for Option B unlock logic
3. get_effective_max_level() - NEW function to determine max available level
4. select_question_for_level() - Update adjacent level check from 10 to 12
"""

# ============================================================
# PATCH 1: Update adjust_level() - change min(10, ...) to min(12, ...)
# ============================================================
# Find this line:
#     return min(10, current_level + 1)
# Replace with:
#     return min(12, current_level + 1)


# ============================================================
# PATCH 2: Add these NEW functions (add after adjust_level function)
# ============================================================

def check_level_12_unlock(topic, user_id=None, guest_code=None):
    """
    Check if Level 12 (Linked Topics) is unlocked for a user.
    
    Level 12 Unlock Requirements (Option B):
    - User must have Level 8+ in the PRIMARY topic
    - User must have Level 8+ in ALL linked topics for that question
    
    Returns: dict with unlock status and missing requirements
    """
    try:
        # First, get the user's level in the primary topic
        primary_level = get_user_current_level(topic, user_id, guest_code)
        
        if primary_level < 8:
            return {
                'unlocked': False,
                'reason': f'Need Level 8+ in {topic} (currently Level {primary_level})',
                'primary_level': primary_level,
                'missing_topics': [topic]
            }
        
        # Get all unique linked_topics for Level 12 questions in this topic
        result = _db.session.execute(text("""
            SELECT DISTINCT linked_topics 
            FROM questions_adaptive 
            WHERE topic = :topic 
            AND difficulty_level = 12 
            AND linked_topics IS NOT NULL
            AND is_active = 1
        """), {'topic': topic}).fetchall()
        
        # Collect all unique linked topics
        all_linked = set()
        for row in result:
            if row[0]:
                for linked in row[0].split(','):
                    linked = linked.strip()
                    if linked:
                        all_linked.add(linked)
        
        # Check user's level in each linked topic
        missing_topics = []
        topic_levels = {}
        
        for linked_topic in all_linked:
            linked_level = get_user_current_level(linked_topic, user_id, guest_code)
            topic_levels[linked_topic] = linked_level
            if linked_level < 8:
                missing_topics.append(f"{linked_topic} (Level {linked_level})")
        
        if missing_topics:
            return {
                'unlocked': False,
                'reason': f'Need Level 8+ in linked topics: {", ".join(missing_topics)}',
                'primary_level': primary_level,
                'topic_levels': topic_levels,
                'missing_topics': missing_topics
            }
        
        return {
            'unlocked': True,
            'primary_level': primary_level,
            'topic_levels': topic_levels
        }
        
    except Exception as e:
        print(f"Error checking Level 12 unlock: {e}")
        return {'unlocked': False, 'reason': str(e)}


def get_effective_max_level(topic, user_id=None, guest_code=None):
    """
    Get the maximum level a user can access for a topic.
    
    Returns:
    - 10 if Level 11 not yet earned
    - 11 if Level 11 available but Level 12 locked
    - 12 if Level 12 unlocked
    """
    current_level = get_user_current_level(topic, user_id, guest_code)
    
    # Must reach Level 10 to unlock Level 11
    if current_level < 10:
        return min(current_level + 1, 10)  # Can only see up to one level ahead
    
    # At Level 10+, check if Level 11 questions exist
    level_11_count = _db.session.execute(text("""
        SELECT COUNT(*) FROM questions_adaptive 
        WHERE topic = :topic AND difficulty_level = 11 AND is_active = 1
    """), {'topic': topic}).fetchone()[0]
    
    if level_11_count == 0:
        return 10  # No Level 11 questions available
    
    # Level 11 is available, check Level 12
    if current_level < 11:
        return 11
    
    # At Level 11, check Level 12 unlock
    level_12_status = check_level_12_unlock(topic, user_id, guest_code)
    
    if level_12_status['unlocked']:
        return 12
    else:
        return 11


def select_question_for_level_12(topic, exclude_ids=None, user_id=None, guest_code=None):
    """
    Select a Level 12 question that the user is qualified for.
    
    Only returns questions where user has Level 8+ in ALL linked topics.
    """
    try:
        exclude_ids = exclude_ids or []
        
        # Get user's levels in all topics
        all_topics_result = _db.session.execute(text("""
            SELECT DISTINCT topic FROM questions_adaptive WHERE is_active = 1
        """)).fetchall()
        
        user_topic_levels = {}
        for row in all_topics_result:
            t = row[0]
            user_topic_levels[t] = get_user_current_level(t, user_id, guest_code)
        
        # Get all Level 12 questions for this topic
        if exclude_ids:
            placeholders = ','.join([':ex' + str(i) for i in range(len(exclude_ids))])
            params = {'topic': topic}
            for i, ex_id in enumerate(exclude_ids):
                params['ex' + str(i)] = ex_id
            
            query = f"""
                SELECT id, question_text, option_a, option_b, option_c, option_d,
                       correct_answer, explanation, difficulty_level, question_type,
                       hint_text, estimated_time_seconds, image_svg, linked_topics
                FROM questions_adaptive 
                WHERE topic = :topic 
                AND difficulty_level = 12 
                AND is_active = 1
                AND id NOT IN ({placeholders})
            """
        else:
            params = {'topic': topic}
            query = """
                SELECT id, question_text, option_a, option_b, option_c, option_d,
                       correct_answer, explanation, difficulty_level, question_type,
                       hint_text, estimated_time_seconds, image_svg, linked_topics
                FROM questions_adaptive 
                WHERE topic = :topic 
                AND difficulty_level = 12 
                AND is_active = 1
            """
        
        results = _db.session.execute(text(query), params).fetchall()
        
        # Filter to questions where user qualifies (Level 8+ in all linked topics)
        qualified_questions = []
        
        for row in results:
            linked_topics_str = row[13]  # linked_topics column
            
            if not linked_topics_str:
                # No linked topics requirement - include it
                qualified_questions.append(row)
                continue
            
            # Parse linked topics and check levels
            linked_topics = [t.strip() for t in linked_topics_str.split(',') if t.strip()]
            qualified = True
            
            for linked in linked_topics:
                level = user_topic_levels.get(linked, 0)
                if level < 8:
                    qualified = False
                    break
            
            if qualified:
                qualified_questions.append(row)
        
        if not qualified_questions:
            return None
        
        # Randomly select one
        import random
        result = random.choice(qualified_questions)
        
        return {
            'id': result[0],
            'question_text': result[1],
            'options': [result[2], result[3], result[4], result[5]],
            'correct_answer': result[6],
            'explanation': result[7],
            'difficulty_level': result[8],
            'question_type': result[9],
            'hint_text': result[10],
            'estimated_time': result[11],
            'image_svg': result[12],
            'linked_topics': result[13]
        }
        
    except Exception as e:
        print(f"Error selecting Level 12 question: {e}")
        return None


# ============================================================
# PATCH 3: Update select_question_for_level() 
# ============================================================
# Find this line:
#     if not result and level < 10:
# Replace with:
#     if not result and level < 12:

# Also add this at the beginning of select_question_for_level():
#     # Special handling for Level 12
#     if level == 12:
#         return select_question_for_level_12(topic, exclude_ids, user_id, guest_code)


# ============================================================
# SUMMARY OF CHANGES TO adaptive_quiz_engine.py
# ============================================================
"""
1. In adjust_level():
   - Change: return min(10, current_level + 1)
   - To:     return min(12, current_level + 1)

2. Add three new functions after adjust_level():
   - check_level_12_unlock()
   - get_effective_max_level()
   - select_question_for_level_12()

3. In select_question_for_level():
   - Add at start: if level == 12: return select_question_for_level_12(...)
   - Change: if not result and level < 10:
   - To:     if not result and level < 12:

4. Update any other references to max level 10 → 12
"""
