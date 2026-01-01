# routes/interactive.py
# Interactive learning activities for AgentMath
# Extracted from app.py for better maintainability
#
# Revision: 1.0.0
# Date: 2025-12-31
# Phase 8: Interactive activities extraction
#
# Contains 36 routes for:
# - Adaptive Quiz API (questions, progress, levels)
# - Flow Sums (arithmetic chains)
# - Number Pyramids (addition puzzles)
# - Code Breaker (logic puzzles)
# - Mastering Counting (number sequences)
# - Words to Numbers (matching activity)
# - Ordering & Number Lines
# - Number Bonds Pop
# - Place Value Builder
# - Double Trouble (doubling/halving)
# - Addition Blitz (speed addition)
# - Times Tables Blitz (speed multiplication)
# - Interactive Level Persistence
# - Award Points System

from flask import Blueprint, request, jsonify, session
from functools import wraps
from datetime import datetime, timedelta
import random

# Create blueprint
interactive_bp = Blueprint('interactive', __name__)

# Import database and models
from models import db, User, UserStats, TopicProgress

# Import decorators from utils
from utils import login_required, guest_or_login_required, approved_required

# Import badge checking
from utils import check_and_award_badges, update_user_stats_after_quiz


# ===== ADAPTIVE QUIZ BETA API =====
@interactive_bp.route('/api/adaptive/question/<topic>/<int:level>')
@guest_or_login_required
@approved_required
def get_adaptive_question(topic, level):
    """
    Get a random question for adaptive quiz at the specified level.
    Uses questions_adaptive table with difficulty_level column.
    
    SERVER-SIDE DUPLICATE PREVENTION:
    - Tracks seen questions in user_adaptive_question_history table
    - Ensures students never see repeat questions until all questions exhausted
    - Works across sessions, page refreshes, and device changes
    
    Also supports ?exclude=1,2,3 parameter as secondary mechanism.
    """
    from sqlalchemy import text
    
    # Get user identifier for tracking
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    # Get excluded question IDs from query parameter (secondary mechanism)
    exclude_param = request.args.get('exclude', '')
    frontend_excluded_ids = []
    if exclude_param:
        try:
            frontend_excluded_ids = [int(x) for x in exclude_param.split(',') if x.strip().isdigit()]
        except:
            frontend_excluded_ids = []
    
    # Map level to difficulty band
    if level <= 3:
        band = 'beginner'
    elif level <= 6:
        band = 'intermediate'
    elif level <= 9:
        band = 'advanced'
    elif level == 10:
        band = 'mastery'
    elif level == 11:
        band = 'application'
    else:
        band = 'linked'  # Level 12
    
    # === SERVER-SIDE DUPLICATE PREVENTION ===
    # Get IDs of questions this user has already seen for this topic/level
    seen_question_ids = set()
    
    try:
        if user_id:
            seen = db.session.execute(text("""
                SELECT question_id FROM user_adaptive_question_history
                WHERE user_id = :user_id AND topic = :topic AND difficulty_level = :level
            """), {'user_id': user_id, 'topic': topic, 'level': level}).fetchall()
            seen_question_ids = {row.question_id for row in seen}
        elif guest_code:
            seen = db.session.execute(text("""
                SELECT question_id FROM user_adaptive_question_history
                WHERE guest_code = :guest_code AND topic = :topic AND difficulty_level = :level
            """), {'guest_code': guest_code, 'topic': topic, 'level': level}).fetchall()
            seen_question_ids = {row.question_id for row in seen}
    except Exception as e:
        # Table might not exist yet - proceed without filtering
        print(f"Note: Could not check adaptive question history (table may not exist): {e}")
        seen_question_ids = set()
    
    # Combine server-side seen IDs with frontend excluded IDs
    all_excluded_ids = seen_question_ids.union(set(frontend_excluded_ids))
    
    try:
        # Build exclusion clause
        exclude_clause = ""
        params = {'topic': topic, 'level': level, 'band': band}
        if all_excluded_ids:
            exclude_clause = f"AND id NOT IN ({','.join(str(x) for x in all_excluded_ids)})"
        
        # Try to get a question from questions_adaptive table
        result = db.session.execute(text(f"""
            SELECT id, topic, question_text, option_a, option_b, option_c, option_d,
                   correct_answer, explanation, difficulty_level, difficulty_band,
                   question_type, image_svg
            FROM questions_adaptive
            WHERE topic = :topic 
              AND difficulty_level = :level
              AND is_active = 1
              {exclude_clause}
            ORDER BY RANDOM()
            LIMIT 1
        """), params).fetchone()
        
        # If no exact level match, try the band
        if not result:
            result = db.session.execute(text(f"""
                SELECT id, topic, question_text, option_a, option_b, option_c, option_d,
                       correct_answer, explanation, difficulty_level, difficulty_band,
                       question_type, image_svg
                FROM questions_adaptive
                WHERE topic = :topic 
                  AND difficulty_band = :band
                  AND is_active = 1
                  {exclude_clause}
                ORDER BY RANDOM()
                LIMIT 1
            """), params).fetchone()
        
        # If still no result and we have exclusions, reset history and try again
        if not result and all_excluded_ids:
            # All questions have been seen - reset history for this topic/level
            try:
                if user_id:
                    db.session.execute(text("""
                        DELETE FROM user_adaptive_question_history
                        WHERE user_id = :user_id AND topic = :topic AND difficulty_level = :level
                    """), {'user_id': user_id, 'topic': topic, 'level': level})
                elif guest_code:
                    db.session.execute(text("""
                        DELETE FROM user_adaptive_question_history
                        WHERE guest_code = :guest_code AND topic = :topic AND difficulty_level = :level
                    """), {'guest_code': guest_code, 'topic': topic, 'level': level})
                db.session.commit()
                print(f"Reset adaptive question history for {user_id or guest_code} on {topic}/level {level}")
            except Exception as e:
                print(f"Could not reset adaptive question history: {e}")
            
            # Try again without exclusions
            result = db.session.execute(text("""
                SELECT id, topic, question_text, option_a, option_b, option_c, option_d,
                       correct_answer, explanation, difficulty_level, difficulty_band,
                       question_type, image_svg
                FROM questions_adaptive
                WHERE topic = :topic 
                  AND difficulty_band = :band
                  AND is_active = 1
                ORDER BY RANDOM()
                LIMIT 1
            """), {'topic': topic, 'band': band}).fetchone()
        
        if result:
            # Record this question as seen
            try:
                if user_id:
                    db.session.execute(text("""
                        INSERT OR IGNORE INTO user_adaptive_question_history 
                        (user_id, question_id, topic, difficulty_level, seen_at)
                        VALUES (:user_id, :question_id, :topic, :level, CURRENT_TIMESTAMP)
                    """), {
                        'user_id': user_id,
                        'question_id': result.id,
                        'topic': topic,
                        'level': level
                    })
                elif guest_code:
                    db.session.execute(text("""
                        INSERT OR IGNORE INTO user_adaptive_question_history 
                        (guest_code, question_id, topic, difficulty_level, seen_at)
                        VALUES (:guest_code, :question_id, :topic, :level, CURRENT_TIMESTAMP)
                    """), {
                        'guest_code': guest_code,
                        'question_id': result.id,
                        'topic': topic,
                        'level': level
                    })
                db.session.commit()
            except Exception as e:
                # Don't fail the request if tracking fails
                print(f"Could not record adaptive question history: {e}")
                db.session.rollback()
            
            question = {
                'id': result.id,
                'topic': result.topic,
                'question_text': result.question_text,
                'option_a': result.option_a,
                'option_b': result.option_b,
                'option_c': result.option_c,
                'option_d': result.option_d,
                'correct_answer': result.correct_answer,
                'explanation': result.explanation or '',
                'difficulty_level': result.difficulty_level,
                'difficulty_band': result.difficulty_band,
                'question_type': result.question_type or 'text',
                'image_svg': result.image_svg or None
            }
            return jsonify(question)
        else:
            # Fallback: Try regular questions table with matching difficulty
            difficulty_map = {'beginner': 'easy', 'intermediate': 'medium', 'advanced': 'hard'}
            difficulty = difficulty_map.get(band, 'medium')
            
            fallback = Question.query.filter_by(topic=topic, difficulty=difficulty).order_by(db.func.random()).first()
            
            if fallback:
                question = fallback.to_dict()
                question['image_svg'] = None  # Regular questions don't have SVG
                question['difficulty_level'] = level
                question['difficulty_band'] = band
                return jsonify(question)
            else:
                return jsonify({'error': f'No questions found for {topic} at level {level}'}), 404
                
    except Exception as e:
        print(f"Error getting adaptive question: {e}")
        # Table might not exist - fallback to regular questions
        difficulty_map = {'beginner': 'easy', 'intermediate': 'medium', 'advanced': 'hard'}
        difficulty = difficulty_map.get(band, 'medium')
        
        fallback = Question.query.filter_by(topic=topic, difficulty=difficulty).order_by(db.func.random()).first()
        
        if fallback:
            question = fallback.to_dict()
            question['image_svg'] = None
            question['difficulty_level'] = level
            question['difficulty_band'] = band
            return jsonify(question)
        else:
            return jsonify({'error': f'No questions found for {topic}'}), 404


@interactive_bp.route('/api/adaptive/progress/<topic>')
@guest_or_login_required
def get_adaptive_progress(topic):
    """
    Get the user's current progress/level for a topic.
    Supports optional entry_level parameter for passport integration.
    """
    from sqlalchemy import text
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    # Check for entry level parameter (from passport)
    entry_level = request.args.get('entry_level', type=int)
    
    try:
        # Check for existing progress
        if user_id:
            result = db.session.execute(text("""
                SELECT current_level, current_points, total_questions, correct_answers
                FROM adaptive_progress
                WHERE user_id = :user_id AND topic = :topic
            """), {'user_id': user_id, 'topic': topic}).fetchone()
        elif guest_code:
            result = db.session.execute(text("""
                SELECT current_level, current_points, total_questions, correct_answers
                FROM adaptive_progress
                WHERE guest_code = :guest_code AND topic = :topic
            """), {'guest_code': guest_code, 'topic': topic}).fetchone()
        else:
            result = None
        
        if result:
            current_level = result.current_level
            # If entry_level is higher than current AND current is still at basics (1-3),
            # allow jumping to entry level
            if entry_level and entry_level > current_level and current_level <= 3:
                current_level = entry_level
                # Save the new entry level
                if user_id:
                    db.session.execute(text("""
                        UPDATE adaptive_progress 
                        SET current_level = :level, updated_at = CURRENT_TIMESTAMP
                        WHERE user_id = :user_id AND topic = :topic
                    """), {'level': current_level, 'user_id': user_id, 'topic': topic})
                elif guest_code:
                    db.session.execute(text("""
                        UPDATE adaptive_progress 
                        SET current_level = :level, updated_at = CURRENT_TIMESTAMP
                        WHERE guest_code = :guest_code AND topic = :topic
                    """), {'level': current_level, 'guest_code': guest_code, 'topic': topic})
                db.session.commit()
            
            return jsonify({
                'topic': topic,
                'current_level': current_level,
                'current_points': result.current_points,
                'total_questions': result.total_questions,
                'correct_answers': result.correct_answers
            })
        else:
            # No progress yet - use entry level if provided, otherwise start at level 1
            start_level = entry_level if entry_level and entry_level > 1 else 1
            
            # Create the progress record with the entry level
            if start_level > 1:
                if user_id:
                    db.session.execute(text("""
                        INSERT INTO adaptive_progress (user_id, topic, current_level, current_points, updated_at)
                        VALUES (:user_id, :topic, :level, 0, CURRENT_TIMESTAMP)
                    """), {'user_id': user_id, 'topic': topic, 'level': start_level})
                elif guest_code:
                    db.session.execute(text("""
                        INSERT INTO adaptive_progress (guest_code, topic, current_level, current_points, updated_at)
                        VALUES (:guest_code, :topic, :level, 0, CURRENT_TIMESTAMP)
                    """), {'guest_code': guest_code, 'topic': topic, 'level': start_level})
                db.session.commit()
            
            return jsonify({
                'topic': topic,
                'current_level': start_level,
                'current_points': 0,
                'total_questions': 0,
                'correct_answers': 0,
                'entry_level_applied': start_level > 1
            })
            
    except Exception as e:
        print(f"Error getting adaptive progress: {e}")
        db.session.rollback()
        # Table might not exist
        return jsonify({
            'topic': topic,
            'current_level': entry_level if entry_level else 1,
            'current_points': 0,
            'total_questions': 0,
            'correct_answers': 0
        })


@interactive_bp.route('/api/adaptive/save-progress', methods=['POST'])
@guest_or_login_required
def save_adaptive_progress():
    """
    Save the user's progress for a topic.
    """
    from sqlalchemy import text
    
    data = request.get_json()
    topic = data.get('topic')
    current_level = data.get('current_level', 1)
    current_points = data.get('current_points', 0)
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    if not topic:
        return jsonify({'error': 'Topic is required'}), 400
    
    try:
        if user_id:
            db.session.execute(text("""
                INSERT INTO adaptive_progress (user_id, topic, current_level, current_points, updated_at)
                VALUES (:user_id, :topic, :level, :points, CURRENT_TIMESTAMP)
                ON CONFLICT(user_id, topic) DO UPDATE SET
                    current_level = :level,
                    current_points = :points,
                    updated_at = CURRENT_TIMESTAMP
            """), {'user_id': user_id, 'topic': topic, 'level': current_level, 'points': current_points})
        elif guest_code:
            db.session.execute(text("""
                INSERT INTO adaptive_progress (guest_code, topic, current_level, current_points, updated_at)
                VALUES (:guest_code, :topic, :level, :points, CURRENT_TIMESTAMP)
                ON CONFLICT(guest_code, topic) DO UPDATE SET
                    current_level = :level,
                    current_points = :points,
                    updated_at = CURRENT_TIMESTAMP
            """), {'guest_code': guest_code, 'topic': topic, 'level': current_level, 'points': current_points})
        
        db.session.commit()
        return jsonify({'success': True})
        
    except Exception as e:
        db.session.rollback()
        print(f"Error saving adaptive progress: {e}")
        return jsonify({'error': str(e)}), 500


@interactive_bp.route('/api/adaptive/reset-progress', methods=['POST'])
@guest_or_login_required
def reset_adaptive_progress():
    """
    Reset the user's progress for a topic back to level 1.
    """
    from sqlalchemy import text
    
    data = request.get_json()
    topic = data.get('topic')
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    if not topic:
        return jsonify({'error': 'Topic is required'}), 400
    
    try:
        if user_id:
            db.session.execute(text("""
                DELETE FROM adaptive_progress
                WHERE user_id = :user_id AND topic = :topic
            """), {'user_id': user_id, 'topic': topic})
        elif guest_code:
            db.session.execute(text("""
                DELETE FROM adaptive_progress
                WHERE guest_code = :guest_code AND topic = :topic
            """), {'guest_code': guest_code, 'topic': topic})
        
        db.session.commit()
        return jsonify({'success': True, 'message': f'Progress reset for {topic}'})
        
    except Exception as e:
        db.session.rollback()
        print(f"Error resetting adaptive progress: {e}")
        return jsonify({'error': str(e)}), 500


@interactive_bp.route('/api/adaptive/set-entry-level', methods=['POST'])
@guest_or_login_required
def set_entry_level():
    """
    Set entry level for a topic from passport.
    Only applies if user hasn't started (level 0-1) or hasn't progressed past basics (level 1-3).
    """
    from sqlalchemy import text
    
    data = request.get_json()
    topic = data.get('topic')
    entry_level = data.get('entry_level', 1)
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    if not topic:
        return jsonify({'error': 'Topic is required'}), 400
    
    # Validate entry level (must be 1, 4, 7, or 10)
    valid_entry_levels = [1, 4, 7, 10]
    if entry_level not in valid_entry_levels:
        entry_level = max([l for l in valid_entry_levels if l <= entry_level], default=1)
    
    try:
        # Check existing progress
        if user_id:
            result = db.session.execute(text("""
                SELECT current_level FROM adaptive_progress
                WHERE user_id = :user_id AND topic = :topic
            """), {'user_id': user_id, 'topic': topic}).fetchone()
        elif guest_code:
            result = db.session.execute(text("""
                SELECT current_level FROM adaptive_progress
                WHERE guest_code = :guest_code AND topic = :topic
            """), {'guest_code': guest_code, 'topic': topic}).fetchone()
        else:
            return jsonify({'error': 'Not logged in'}), 401
        
        current_level = result[0] if result else 0
        
        # Only allow entry level if:
        # 1. No progress yet (current_level = 0 or None)
        # 2. Still at basics (current_level <= 3)
        # 3. Entry level is higher than current
        if current_level <= 3 and entry_level > current_level:
            if result:
                # Update existing record
                if user_id:
                    db.session.execute(text("""
                        UPDATE adaptive_progress 
                        SET current_level = :level, updated_at = CURRENT_TIMESTAMP
                        WHERE user_id = :user_id AND topic = :topic
                    """), {'level': entry_level, 'user_id': user_id, 'topic': topic})
                elif guest_code:
                    db.session.execute(text("""
                        UPDATE adaptive_progress 
                        SET current_level = :level, updated_at = CURRENT_TIMESTAMP
                        WHERE guest_code = :guest_code AND topic = :topic
                    """), {'level': entry_level, 'guest_code': guest_code, 'topic': topic})
            else:
                # Create new record
                if user_id:
                    db.session.execute(text("""
                        INSERT INTO adaptive_progress (user_id, topic, current_level, current_points, updated_at)
                        VALUES (:user_id, :topic, :level, 0, CURRENT_TIMESTAMP)
                    """), {'user_id': user_id, 'topic': topic, 'level': entry_level})
                elif guest_code:
                    db.session.execute(text("""
                        INSERT INTO adaptive_progress (guest_code, topic, current_level, current_points, updated_at)
                        VALUES (:guest_code, :topic, :level, 0, CURRENT_TIMESTAMP)
                    """), {'guest_code': guest_code, 'topic': topic, 'level': entry_level})
            
            db.session.commit()
            return jsonify({
                'success': True,
                'topic': topic,
                'entry_level': entry_level,
                'previous_level': current_level,
                'message': f'Entry level set to {entry_level} for {topic}'
            })
        else:
            # User has already progressed beyond entry level
            return jsonify({
                'success': False,
                'topic': topic,
                'current_level': current_level,
                'entry_level_requested': entry_level,
                'message': f'Cannot set entry level - already at level {current_level}'
            })
        
    except Exception as e:
        db.session.rollback()
        print(f"Error setting entry level: {e}")
        return jsonify({'error': str(e)}), 500


# =============================================================================
# FLOW SUMS - INTERACTIVE ARITHMETIC CHAINS (NUMERACY STRAND)
# =============================================================================

def get_flow_sum_level_config(level: int) -> dict:
    """Get configuration for a specific Flow Sum level"""
    configs = {
        1: {'steps': 3, 'ops': ['basic_add', 'basic_subtract'], 'num_range': (2, 15), 'gateway_range': (5, 15)},
        2: {'steps': 3, 'ops': ['basic_add', 'basic_subtract'], 'num_range': (2, 20), 'gateway_range': (5, 20)},
        3: {'steps': 4, 'ops': ['basic_add', 'basic_subtract', 'double'], 'num_range': (2, 20), 'gateway_range': (5, 25)},
        4: {'steps': 4, 'ops': ['basic_add', 'basic_subtract', 'double', 'halve'], 'num_range': (2, 25), 'gateway_range': (10, 40)},
        5: {'steps': 5, 'ops': ['basic_add', 'basic_subtract', 'double', 'halve', 'times'], 'num_range': (2, 10), 'gateway_range': (5, 30)},
        6: {'steps': 5, 'ops': ['basic_add', 'basic_subtract', 'double', 'times', 'divide'], 'num_range': (2, 10), 'gateway_range': (10, 50)},
        7: {'steps': 5, 'ops': ['basic_add', 'basic_subtract', 'times', 'divide', 'add_square', 'times_10'], 'num_range': (2, 12), 'gateway_range': (5, 30)},
        8: {'steps': 6, 'ops': ['basic_add', 'basic_subtract', 'times', 'divide', 'add_square', 'times_10', 'divide_10'], 'num_range': (2, 15), 'gateway_range': (10, 50)},
        9: {'steps': 6, 'ops': ['basic_add', 'basic_subtract', 'times', 'percent_50', 'percent_10', 'double'], 'num_range': (5, 20), 'gateway_range': (20, 100)},
        10: {'steps': 7, 'ops': ['basic_add', 'basic_subtract', 'times', 'percent_50', 'percent_25', 'percent_200', 'double'], 'num_range': (5, 25), 'gateway_range': (20, 100)},
        11: {'steps': 7, 'ops': ['basic_add', 'basic_subtract', 'times', 'subtract_from', 'add_square', 'percent_50', 'double'], 'num_range': (5, 30), 'gateway_range': (10, 50)},
        12: {'steps': 8, 'ops': ['basic_add', 'basic_subtract', 'times', 'subtract_from', 'add_square', 'add_product', 'percent_50', 'times'], 'num_range': (5, 30), 'gateway_range': (10, 50)},
    }
    return configs.get(level, configs[1])


def generate_flow_sum_operation(op_type: str, current_value: int, config: dict):
    """Generate a single Flow Sum operation. Returns (display, new_value, hint)"""
    import random
    num_range = config['num_range']
    
    if op_type == 'basic_add':
        n = random.randint(num_range[0], num_range[1])
        return f"Add {n}", current_value + n, f"Take your number and add {n} to it"
        
    elif op_type == 'basic_subtract':
        max_sub = min(num_range[1], current_value - 1)
        if max_sub < 1:
            n = random.randint(num_range[0], num_range[1])
            return f"Add {n}", current_value + n, f"Add {n} to your number"
        n = random.randint(max(1, num_range[0]), max(1, max_sub))
        return f"Subtract {n}", current_value - n, f"Take away {n} from your number"
        
    elif op_type == 'double':
        return "Double it", current_value * 2, "Multiply your number by 2"
        
    elif op_type == 'halve':
        if current_value % 2 != 0:
            return "Double it", current_value * 2, "Multiply your number by 2"
        return "Halve it", current_value // 2, "Divide your number by 2"
        
    elif op_type == 'times':
        n = random.randint(2, min(6, num_range[1]))
        return f"Times {n}", current_value * n, f"Multiply your number by {n}"
        
    elif op_type == 'divide':
        divisors = [d for d in range(2, min(10, current_value)) if current_value % d == 0]
        if not divisors:
            n = random.randint(2, 5)
            return f"Times {n}", current_value * n, f"Multiply by {n}"
        n = random.choice(divisors)
        return f"Divide by {n}", current_value // n, f"Divide your number by {n}"
        
    elif op_type == 'add_square':
        n = random.randint(2, 5)
        return f"Add {n}²", current_value + (n * n), f"Calculate {n}² = {n*n}, then add it"
        
    elif op_type == 'times_10':
        return "Times 10", current_value * 10, "Add a zero to the end"
        
    elif op_type == 'divide_10':
        if current_value % 10 != 0:
            return "Times 10", current_value * 10, "Add a zero to the end"
        return "Divide by 10", current_value // 10, "Remove the last digit"
        
    elif op_type == 'percent_50':
        if current_value % 2 != 0:
            return "Double it", current_value * 2, "Multiply by 2"
        return "Get 50% of this", current_value // 2, "Find half (50% means ÷2)"
        
    elif op_type == 'percent_25':
        if current_value % 4 != 0:
            return "Double it", current_value * 2, "Multiply by 2"
        return "Get 25% of this", current_value // 4, "Find a quarter (25% means ÷4)"
        
    elif op_type == 'percent_10':
        if current_value % 10 != 0:
            return "Times 10", current_value * 10, "Add a zero"
        return "Get 10% of this", current_value // 10, "Divide by 10"
        
    elif op_type == 'percent_200':
        return "Get 200% of this", current_value * 2, "Double it (200% means ×2)"
        
    elif op_type == 'subtract_from':
        n = ((current_value + random.randint(50, 200)) // 50) * 50
        return f"Subtract from {n}", n - current_value, f"Take {n} and subtract your number from it"
        
    elif op_type == 'add_product':
        a, b = random.randint(2, 8), random.randint(2, 8)
        return f"Add the product of {a} and {b}", current_value + (a * b), f"Calculate {a} × {b} = {a*b}, then add it"
        
    else:
        n = random.randint(num_range[0], num_range[1])
        return f"Add {n}", current_value + n, f"Add {n} to your number"


def generate_flow_sum(level: int) -> dict:
    """Generate a complete Flow Sum question"""
    import random
    config = get_flow_sum_level_config(level)
    
    # Choose appropriate layouts based on level
    # Levels 1-4: Simple vertical only (clearer for beginners)
    # Levels 5-8: Vertical layouts
    # Levels 9-12: All layouts including snake
    if level <= 4:
        layouts = ['arrow_down']
    elif level <= 8:
        layouts = ['arrow_down', 'arrow_up']
    else:
        layouts = ['arrow_down', 'arrow_up', 'snake_right', 'snake_left']
    
    for attempt in range(50):
        try:
            gateway = random.randint(config['gateway_range'][0], config['gateway_range'][1])
            
            # Adjust for divisibility if needed
            if any(op in config['ops'] for op in ['halve', 'percent_50']):
                gateway = (gateway // 2) * 2
            if 'percent_25' in config['ops']:
                gateway = (gateway // 4) * 4
                
            current_value = gateway
            steps = []
            used_ops = []
            valid = True
            
            for step_num in range(config['steps']):
                available_ops = [op for op in config['ops'] if op not in used_ops[-1:]]
                if not available_ops:
                    available_ops = config['ops']
                    
                op_type = random.choice(available_ops)
                display, new_value, hint = generate_flow_sum_operation(op_type, current_value, config)
                
                # Validate
                if not isinstance(new_value, int) or new_value <= 0 or new_value > 5000:
                    valid = False
                    break
                if level <= 4 and new_value > 200:
                    valid = False
                    break
                    
                steps.append({
                    'operation': display,
                    'expected_value': new_value,
                    'hint': hint
                })
                
                current_value = new_value
                used_ops.append(op_type)
            
            if valid and len(steps) == config['steps']:
                # Choose layout based on level - simpler layouts for lower levels
                if level <= 4:
                    layout = 'arrow_down'  # Simple vertical flow for beginners
                elif level <= 8:
                    layout = random.choice(['arrow_down', 'arrow_up'])
                else:
                    layout = random.choice(layouts)
                    
                return {
                    'gateway_number': gateway,
                    'steps': steps,
                    'final_answer': current_value,
                    'layout': layout,
                    'level': level,
                    'total_steps': len(steps)
                }
                
        except:
            continue
    
    # Fallback simple question
    gateway = random.randint(5, 15)
    return {
        'gateway_number': gateway,
        'steps': [
            {'operation': 'Add 5', 'expected_value': gateway + 5, 'hint': 'Add 5'},
            {'operation': 'Double it', 'expected_value': (gateway + 5) * 2, 'hint': 'Multiply by 2'},
            {'operation': 'Subtract 3', 'expected_value': (gateway + 5) * 2 - 3, 'hint': 'Take away 3'},
        ],
        'final_answer': (gateway + 5) * 2 - 3,
        'layout': 'arrow_down',
        'level': level,
        'total_steps': 3
    }


@interactive_bp.route('/api/flow-sums/question/<int:level>')
@guest_or_login_required
@approved_required
def get_flow_sum_question(level):
    """
    Get a Flow Sum question for the specified level (1-12).
    Returns an interactive arithmetic chain question.
    """
    if level < 1 or level > 12:
        level = 1
    
    question = generate_flow_sum(level)
    
    return jsonify({
        'success': True,
        'question': question
    })


@interactive_bp.route('/api/flow-sums/validate', methods=['POST'])
@guest_or_login_required
def validate_flow_sum_step():
    """
    Validate a single step in a Flow Sum.
    """
    data = request.get_json()
    user_answer = data.get('answer')
    expected = data.get('expected')
    step_index = data.get('step_index', 0)
    
    try:
        user_answer = int(user_answer)
        expected = int(expected)
        correct = (user_answer == expected)
        
        return jsonify({
            'correct': correct,
            'step_index': step_index
        })
    except:
        return jsonify({
            'correct': False,
            'step_index': step_index,
            'error': 'Invalid number'
        })


@interactive_bp.route('/api/flow-sums/complete', methods=['POST'])
@guest_or_login_required
def complete_flow_sum():
    """
    Record completion of a Flow Sum question and award points.
    """
    from sqlalchemy import text
    
    data = request.get_json()
    level = data.get('level', 1)
    hints_used = data.get('hints_used', 0)
    total_attempts = data.get('total_attempts', 0)
    time_taken = data.get('time_taken', 0)
    steps_count = data.get('steps_count', 3)
    
    # Calculate points
    base_points = 5 + (level * 2)  # Higher levels worth more
    hint_penalty = hints_used * 2
    attempt_penalty = max(0, (total_attempts - steps_count) * 1)
    points = max(1, base_points - hint_penalty - attempt_penalty)
    
    # Award points to user
    guest_code = session.get('guest_code')
    user_id = session.get('user_id') if not session.get('is_guest') else None
    
    try:
        if guest_code:
            db.session.execute(text("""
                UPDATE guest_users 
                SET total_score = total_score + :points
                WHERE guest_code = :code
            """), {'points': points, 'code': guest_code})
            db.session.commit()
        elif user_id:
            db.session.execute(text("""
                UPDATE users 
                SET score = score + :points
                WHERE id = :user_id
            """), {'points': points, 'user_id': user_id})
            db.session.commit()
    except Exception as e:
        print(f"Could not award Flow Sum points: {e}")
        db.session.rollback()
    
    return jsonify({
        'success': True,
        'points_earned': points,
        'base_points': base_points,
        'hint_penalty': hint_penalty,
        'attempt_penalty': attempt_penalty
    })


# =============================================================================
# NUMBER PYRAMIDS - INTERACTIVE ADDITION PUZZLES (NUMERACY STRAND)
# =============================================================================

def get_pyramid_level_config(level: int) -> dict:
    """Get configuration for a specific Number Pyramid level"""
    configs = {
        1:  {'rows': 3, 'num_range': (1, 5),   'blanks': 2,  'allow_negative': False},
        2:  {'rows': 3, 'num_range': (1, 8),   'blanks': 3,  'allow_negative': False},
        3:  {'rows': 4, 'num_range': (1, 10),  'blanks': 3,  'allow_negative': False},
        4:  {'rows': 4, 'num_range': (1, 12),  'blanks': 4,  'allow_negative': False},
        5:  {'rows': 4, 'num_range': (1, 15),  'blanks': 5,  'allow_negative': False},
        6:  {'rows': 4, 'num_range': (2, 20),  'blanks': 5,  'allow_negative': False},
        7:  {'rows': 5, 'num_range': (1, 15),  'blanks': 5,  'allow_negative': False},
        8:  {'rows': 5, 'num_range': (2, 20),  'blanks': 6,  'allow_negative': False},
        9:  {'rows': 5, 'num_range': (1, 25),  'blanks': 7,  'allow_negative': True},
        10: {'rows': 5, 'num_range': (2, 30),  'blanks': 8,  'allow_negative': True},
        11: {'rows': 6, 'num_range': (1, 20),  'blanks': 8,  'allow_negative': True},
        12: {'rows': 6, 'num_range': (2, 25),  'blanks': 10, 'allow_negative': True},
    }
    return configs.get(level, configs[1])


def generate_full_pyramid(rows: int, num_range: tuple) -> list:
    """Generate a complete pyramid with all values filled in"""
    import random
    base = [random.randint(num_range[0], num_range[1]) for _ in range(rows)]
    pyramid = [None] * rows
    pyramid[rows - 1] = base
    
    for row in range(rows - 2, -1, -1):
        pyramid[row] = []
        for i in range(row + 1):
            value = pyramid[row + 1][i] + pyramid[row + 1][i + 1]
            pyramid[row].append(value)
    
    return pyramid


def is_pyramid_solvable(pyramid: list, blanks: set) -> bool:
    """Check if a pyramid with given blanks is solvable"""
    rows = len(pyramid)
    known = set()
    
    for row in range(rows):
        for col in range(row + 1):
            if (row, col) not in blanks:
                known.add((row, col))
    
    changed = True
    max_iterations = 50
    iteration = 0
    
    while changed and iteration < max_iterations:
        changed = False
        iteration += 1
        
        for row in range(rows):
            for col in range(row + 1):
                if (row, col) in known:
                    continue
                
                can_solve = False
                
                if row < rows - 1:
                    left_below = (row + 1, col)
                    right_below = (row + 1, col + 1)
                    if left_below in known and right_below in known:
                        can_solve = True
                
                if row > 0:
                    if col > 0:
                        parent = (row - 1, col - 1)
                        sibling = (row, col - 1)
                        if parent in known and sibling in known:
                            can_solve = True
                    if col < row:
                        parent = (row - 1, col)
                        sibling = (row, col + 1)
                        if parent in known and sibling in known:
                            can_solve = True
                
                if can_solve:
                    known.add((row, col))
                    changed = True
    
    total_cells = sum(range(1, rows + 1))
    return len(known) == total_cells


def select_pyramid_blanks(pyramid: list, num_blanks: int, level: int) -> set:
    """Select which cells to blank out while ensuring solvability"""
    import random
    rows = len(pyramid)
    all_cells = [(row, col) for row in range(rows) for col in range(row + 1)]
    
    for attempt in range(100):
        blanks = set()
        
        if level <= 4:
            candidates = [(r, c) for r, c in all_cells if r > 0 and r < rows - 1]
            if len(candidates) < num_blanks:
                candidates = [(r, c) for r, c in all_cells if r > 0]
        elif level <= 8:
            candidates = [(r, c) for r, c in all_cells if r > 0]
        else:
            candidates = [(r, c) for r, c in all_cells if r > 0]
            base_cells = [(rows - 1, c) for c in range(rows)]
            random.shuffle(base_cells)
            candidates.extend(base_cells[:2])
        
        random.shuffle(candidates)
        
        for cell in candidates:
            if len(blanks) >= num_blanks:
                break
            test_blanks = blanks | {cell}
            if is_pyramid_solvable(pyramid, test_blanks):
                blanks.add(cell)
        
        if len(blanks) >= num_blanks:
            return blanks
    
    return blanks


def generate_pyramid_puzzle(level: int) -> dict:
    """Generate a Number Pyramid puzzle for the given level"""
    import random
    config = get_pyramid_level_config(level)
    
    for attempt in range(50):
        pyramid = generate_full_pyramid(config['rows'], config['num_range'])
        
        max_top = 200 if level <= 6 else 500 if level <= 10 else 1000
        if pyramid[0][0] > max_top:
            continue
        
        blanks_set = select_pyramid_blanks(pyramid, config['blanks'], level)
        
        if len(blanks_set) >= config['blanks'] - 1:
            # Create 2D boolean array for blanks (True = blank, False = given)
            blanks_2d = []
            for row in range(len(pyramid)):
                blanks_row = []
                for col in range(row + 1):
                    blanks_row.append((row, col) in blanks_set)
                blanks_2d.append(blanks_row)
            
            return {
                'pyramid': pyramid,
                'blanks': blanks_2d,
                'level': level,
                'rows': config['rows'],
                'blank_count': len(blanks_set)
            }
    
    # Fallback
    pyramid = [[10], [4, 6], [1, 3, 3]]
    return {
        'pyramid': pyramid,
        'blanks': [[False], [True, False], [False, False, True]],
        'level': level,
        'rows': 3,
        'blank_count': 2
    }


def get_pyramid_hint(pyramid: list, row: int, col: int) -> str:
    """Generate a hint for solving a specific cell"""
    rows = len(pyramid)
    
    if row < rows - 1:
        left = pyramid[row + 1][col]
        right = pyramid[row + 1][col + 1]
        return f"Add the two bricks below: {left} + {right}"
    
    if row > 0:
        if col > 0:
            parent = pyramid[row - 1][col - 1]
            sibling = pyramid[row][col - 1]
            return f"Subtract from brick above: {parent} - {sibling}"
        else:
            parent = pyramid[row - 1][col]
            sibling = pyramid[row][col + 1]
            return f"Subtract from brick above: {parent} - {sibling}"
    
    return "Look at the bricks around it"


@interactive_bp.route('/api/number-pyramids/question/<int:level>')
@guest_or_login_required
@approved_required
def get_pyramid_question(level):
    """Get a Number Pyramid puzzle for the specified level (1-12)"""
    if level < 1 or level > 12:
        level = 1
    
    puzzle = generate_pyramid_puzzle(level)
    
    return jsonify({
        'success': True,
        'puzzle': puzzle
    })


@interactive_bp.route('/api/number-pyramids/validate', methods=['POST'])
@guest_or_login_required
def validate_pyramid_cell():
    """Validate a single cell answer in a Number Pyramid"""
    data = request.get_json()
    user_answer = data.get('answer')
    expected = data.get('expected')
    row = data.get('row', 0)
    col = data.get('col', 0)
    
    try:
        user_answer = int(user_answer)
        expected = int(expected)
        correct = (user_answer == expected)
        
        return jsonify({
            'correct': correct,
            'row': row,
            'col': col
        })
    except:
        return jsonify({
            'correct': False,
            'row': row,
            'col': col,
            'error': 'Invalid number'
        })


@interactive_bp.route('/api/number-pyramids/hint', methods=['POST'])
@guest_or_login_required
def get_pyramid_hint_endpoint():
    """Get a hint for a specific cell"""
    data = request.get_json()
    pyramid = data.get('pyramid', [])
    row = data.get('row', 0)
    col = data.get('col', 0)
    
    hint = get_pyramid_hint(pyramid, row, col)
    
    return jsonify({
        'success': True,
        'hint': hint
    })


@interactive_bp.route('/api/number-pyramids/complete', methods=['POST'])
@guest_or_login_required
def complete_pyramid():
    """Record completion of a Number Pyramid and award points"""
    from sqlalchemy import text
    
    data = request.get_json()
    level = data.get('level', 1)
    hints_used = data.get('hints_used', 0)
    total_attempts = data.get('total_attempts', 0)
    total_blanks = data.get('total_blanks', 3)
    time_taken = data.get('time_taken', 0)
    
    # Calculate points
    base_points = 5 + (level * 2)
    hint_penalty = hints_used * 2
    attempt_penalty = max(0, (total_attempts - total_blanks) * 1)
    points = max(1, base_points - hint_penalty - attempt_penalty)
    
    # Award points
    guest_code = session.get('guest_code')
    user_id = session.get('user_id') if not session.get('is_guest') else None
    
    try:
        if guest_code:
            db.session.execute(text("""
                UPDATE guest_users 
                SET total_score = total_score + :points
                WHERE guest_code = :code
            """), {'points': points, 'code': guest_code})
            db.session.commit()
        elif user_id:
            db.session.execute(text("""
                UPDATE users 
                SET score = score + :points
                WHERE id = :user_id
            """), {'points': points, 'user_id': user_id})
            db.session.commit()
    except Exception as e:
        print(f"Could not award Number Pyramid points: {e}")
        db.session.rollback()
    
    return jsonify({
        'success': True,
        'points_earned': points,
        'base_points': base_points,
        'hint_penalty': hint_penalty,
        'attempt_penalty': attempt_penalty
    })


# =============================================================================
# CODE BREAKER - LOGIC AND NUMERACY PUZZLE (NUMERACY STRAND)
# =============================================================================

def get_code_level_config(level: int) -> dict:
    """Get configuration for a specific Code Breaker level"""
    configs = {
        1:  {'digits': 3, 'range': (1, 5), 'repeats': False, 'guesses': 8, 'clue_types': ['add']},
        2:  {'digits': 3, 'range': (1, 5), 'repeats': False, 'guesses': 7, 'clue_types': ['add', 'biggest']},
        3:  {'digits': 3, 'range': (1, 6), 'repeats': False, 'guesses': 7, 'clue_types': ['add', 'smallest', 'biggest']},
        4:  {'digits': 3, 'range': (1, 7), 'repeats': False, 'guesses': 7, 'clue_types': ['add', 'odd_even', 'biggest']},
        5:  {'digits': 3, 'range': (1, 9), 'repeats': True,  'guesses': 7, 'clue_types': ['add', 'odd_even', 'has_repeat']},
        6:  {'digits': 3, 'range': (1, 9), 'repeats': True,  'guesses': 6, 'clue_types': ['add', 'multiply_two', 'odd_even']},
        7:  {'digits': 4, 'range': (1, 6), 'repeats': False, 'guesses': 8, 'clue_types': ['add', 'multiply_two', 'biggest']},
        8:  {'digits': 4, 'range': (1, 8), 'repeats': False, 'guesses': 7, 'clue_types': ['add', 'multiply_two', 'difference']},
        9:  {'digits': 4, 'range': (1, 9), 'repeats': True,  'guesses': 7, 'clue_types': ['sum', 'product_two', 'double']},
        10: {'digits': 4, 'range': (1, 9), 'repeats': True,  'guesses': 6, 'clue_types': ['sum', 'product_two', 'relationship']},
        11: {'digits': 5, 'range': (1, 9), 'repeats': True,  'guesses': 7, 'clue_types': ['sum', 'product_two', 'consecutive']},
        12: {'digits': 5, 'range': (1, 9), 'repeats': True,  'guesses': 6, 'clue_types': ['sum', 'product_all', 'relationship']},
    }
    return configs.get(level, configs[1])


def generate_secret_code(config: dict) -> list:
    """Generate a secret code based on config"""
    import random
    digits = config['digits']
    min_val, max_val = config['range']
    repeats = config['repeats']
    
    if repeats:
        return [random.randint(min_val, max_val) for _ in range(digits)]
    else:
        available = list(range(min_val, max_val + 1))
        random.shuffle(available)
        return available[:digits]


def generate_code_clue(code: list, clue_type: str, level: int) -> dict:
    """Generate a single clue with simple or advanced language based on level"""
    simple = level <= 8  # Simple language for levels 1-8
    
    if clue_type == 'add':
        total = sum(code)
        return {
            'type': 'add',
            'text': f"Add all the digits together to get {total}",
            'value': total
        }
    
    elif clue_type == 'sum':
        total = sum(code)
        return {
            'type': 'sum',
            'text': f"The sum of all digits is {total}",
            'value': total
        }
    
    elif clue_type == 'biggest':
        biggest = max(code)
        return {
            'type': 'biggest',
            'text': f"The biggest digit is {biggest}" if simple else f"The largest digit is {biggest}",
            'value': biggest
        }
    
    elif clue_type == 'smallest':
        smallest = min(code)
        return {
            'type': 'smallest',
            'text': f"The smallest digit is {smallest}",
            'value': smallest
        }
    
    elif clue_type == 'odd_even':
        odd_count = sum(1 for d in code if d % 2 == 1)
        even_count = len(code) - odd_count
        if odd_count == 0:
            text = "All the digits are even numbers"
        elif even_count == 0:
            text = "All the digits are odd numbers"
        elif odd_count == 1:
            text = "There is 1 odd number"
        else:
            text = f"There are {odd_count} odd numbers"
        return {
            'type': 'odd_even',
            'text': text,
            'odd_count': odd_count
        }
    
    elif clue_type == 'has_repeat':
        has_repeat = len(code) != len(set(code))
        if has_repeat:
            return {
                'type': 'has_repeat',
                'text': "At least two digits are the same",
                'value': True
            }
        else:
            return {
                'type': 'has_repeat',
                'text': "All digits are different",
                'value': False
            }
    
    elif clue_type == 'multiply_two':
        product = code[0] * code[1]
        return {
            'type': 'multiply_two',
            'text': f"Multiply the 1st and 2nd digits to get {product}",
            'positions': [0, 1],
            'value': product
        }
    
    elif clue_type == 'product_two':
        product = code[0] * code[1]
        return {
            'type': 'product_two',
            'text': f"The product of digits 1 and 2 is {product}",
            'positions': [0, 1],
            'value': product
        }
    
    elif clue_type == 'difference':
        diff = max(code) - min(code)
        return {
            'type': 'difference',
            'text': f"Take the smallest from the biggest to get {diff}" if simple else f"The difference between largest and smallest is {diff}",
            'value': diff
        }
    
    elif clue_type == 'double':
        # Find if any digit is double another
        for i, d1 in enumerate(code):
            for j, d2 in enumerate(code):
                if i != j and d1 == d2 * 2:
                    pos1, pos2 = i + 1, j + 1
                    return {
                        'type': 'double',
                        'text': f"Digit {pos1} is double digit {pos2}",
                        'positions': [i, j]
                    }
        # Fallback
        return generate_code_clue(code, 'biggest', level)
    
    elif clue_type == 'relationship':
        # Check if any two digits add to another
        if len(code) >= 3:
            for i in range(len(code)):
                for j in range(len(code)):
                    for k in range(len(code)):
                        if i != j and j != k and i != k:
                            if code[i] + code[j] == code[k]:
                                return {
                                    'type': 'relationship',
                                    'text': f"Digit {i+1} plus Digit {j+1} equals Digit {k+1}",
                                    'positions': [i, j, k]
                                }
        # Fallback
        return generate_code_clue(code, 'difference', level)
    
    elif clue_type == 'consecutive':
        sorted_code = sorted(code)
        for i in range(len(sorted_code) - 1):
            if sorted_code[i+1] - sorted_code[i] == 1:
                return {
                    'type': 'consecutive',
                    'text': "Two of the digits are next to each other when counting (like 3 and 4)",
                    'value': True
                }
        return {
            'type': 'consecutive',
            'text': "No two digits are next to each other when counting",
            'value': False
        }
    
    elif clue_type == 'product_all':
        product = 1
        for d in code:
            product *= d
        return {
            'type': 'product_all',
            'text': f"Multiply all the digits together to get {product}",
            'value': product
        }
    
    return None


def generate_code_clues(code: list, clue_types: list, level: int) -> list:
    """Generate all clues for the code"""
    clues = []
    for clue_type in clue_types:
        clue = generate_code_clue(code, clue_type, level)
        if clue:
            clues.append(clue)
    return clues


def generate_code_breaker(level: int) -> dict:
    """Generate a complete Code Breaker puzzle for the given level"""
    import random
    config = get_code_level_config(level)
    
    for attempt in range(50):
        code = generate_secret_code(config)
        clues = generate_code_clues(code, config['clue_types'], level)
        if len(clues) >= 1:
            break
    
    # Simple tips for younger students
    if level <= 4:
        tip = "Use the clues to work out what digits are in the code!"
    elif level <= 8:
        tip = "Each clue helps you narrow down the possibilities."
    else:
        tip = "Combine the clues logically to crack the code."
    
    return {
        'code': code,
        'clues': clues,
        'level': level,
        'digits': config['digits'],
        'digit_range': config['range'],
        'allows_repeats': config['repeats'],
        'max_guesses': config['guesses'],
        'tip': tip
    }


def check_code_guess(guess: list, secret: list) -> dict:
    """Check a guess against the secret code"""
    result = []
    secret_remaining = list(secret)
    guess_remaining = []
    
    # First pass: exact matches (green)
    for i, (g, s) in enumerate(zip(guess, secret)):
        if g == s:
            result.append({'position': i, 'status': 'correct'})
            secret_remaining[i] = None
        else:
            result.append({'position': i, 'status': 'pending'})
            guess_remaining.append((i, g))
    
    # Second pass: wrong position matches (yellow)
    for i, g in guess_remaining:
        if g in secret_remaining:
            result[i] = {'position': i, 'status': 'wrong_position'}
            secret_remaining[secret_remaining.index(g)] = None
        else:
            result[i] = {'position': i, 'status': 'not_in_code'}
    
    return {
        'feedback': result,
        'correct_count': sum(1 for r in result if r['status'] == 'correct'),
        'wrong_position_count': sum(1 for r in result if r['status'] == 'wrong_position'),
        'is_solved': all(r['status'] == 'correct' for r in result)
    }


@interactive_bp.route('/api/code-breaker/question/<int:level>')
@guest_or_login_required
@approved_required
def get_code_breaker_question(level):
    """Get a Code Breaker puzzle for the specified level (1-12)"""
    if level < 1 or level > 12:
        level = 1
    
    puzzle = generate_code_breaker(level)
    
    # Don't send the actual code to the client!
    # Store it in session for validation
    session['code_breaker_code'] = puzzle['code']
    session['code_breaker_level'] = level
    
    return jsonify({
        'success': True,
        'puzzle': {
            'clues': puzzle['clues'],
            'level': puzzle['level'],
            'digits': puzzle['digits'],
            'digit_range': puzzle['digit_range'],
            'allows_repeats': puzzle['allows_repeats'],
            'max_guesses': puzzle['max_guesses'],
            'tip': puzzle['tip']
        }
    })


@interactive_bp.route('/api/code-breaker/guess', methods=['POST'])
@guest_or_login_required
def check_code_breaker_guess():
    """Check a guess against the secret code"""
    data = request.get_json()
    guess = data.get('guess', [])
    
    secret = session.get('code_breaker_code')
    if not secret:
        return jsonify({'success': False, 'error': 'No active puzzle'})
    
    # Validate guess format
    if len(guess) != len(secret):
        return jsonify({'success': False, 'error': 'Wrong number of digits'})
    
    try:
        guess = [int(g) for g in guess]
    except:
        return jsonify({'success': False, 'error': 'Invalid digits'})
    
    result = check_code_guess(guess, secret)
    
    return jsonify({
        'success': True,
        'result': result
    })


@interactive_bp.route('/api/code-breaker/reveal', methods=['POST'])
@guest_or_login_required
def reveal_code_breaker():
    """Reveal the secret code (when giving up or out of guesses)"""
    secret = session.get('code_breaker_code')
    if not secret:
        return jsonify({'success': False, 'error': 'No active puzzle'})
    
    return jsonify({
        'success': True,
        'code': secret
    })


@interactive_bp.route('/api/code-breaker/complete', methods=['POST'])
@guest_or_login_required
def complete_code_breaker():
    """Record completion of a Code Breaker and award points"""
    from sqlalchemy import text
    
    data = request.get_json()
    level = data.get('level', 1)
    guesses_used = data.get('guesses_used', 1)
    max_guesses = data.get('max_guesses', 8)
    solved = data.get('solved', False)
    
    # Calculate points
    if solved:
        base_points = 5 + (level * 2)
        # Bonus for fewer guesses
        guesses_saved = max_guesses - guesses_used
        guess_bonus = guesses_saved * 2
        points = base_points + guess_bonus
    else:
        points = max(1, level)  # Participation points
    
    # Award points
    guest_code = session.get('guest_code')
    user_id = session.get('user_id') if not session.get('is_guest') else None
    
    try:
        if guest_code:
            db.session.execute(text("""
                UPDATE guest_users 
                SET total_score = total_score + :points
                WHERE guest_code = :code
            """), {'points': points, 'code': guest_code})
            db.session.commit()
        elif user_id:
            db.session.execute(text("""
                UPDATE users 
                SET score = score + :points
                WHERE id = :user_id
            """), {'points': points, 'user_id': user_id})
            db.session.commit()
    except Exception as e:
        print(f"Could not award Code Breaker points: {e}")
        db.session.rollback()
    
    # Clear session
    session.pop('code_breaker_code', None)
    session.pop('code_breaker_level', None)
    
    return jsonify({
        'success': True,
        'points_earned': points,
        'solved': solved
    })


# =============================================================================
# MASTERING COUNTING - NUMBER SEQUENCE ACTIVITY (NUMERACY STRAND)
# =============================================================================

def get_counting_level_config(level: int) -> dict:
    """Get configuration for each Mastering Counting level"""
    configs = {
        # Level 1-2: Forward by 1s
        1:  {'step': 1,  'direction': 'forward',  'min_start': 1,   'max_start': 10,  'cells': 15, 'rows': 3, 'blanks_per_row': 8,  'allow_negative': False, 'name': 'Count by 1s'},
        2:  {'step': 1,  'direction': 'forward',  'min_start': 15,  'max_start': 40,  'cells': 15, 'rows': 3, 'blanks_per_row': 9,  'allow_negative': False, 'name': 'Count by 1s (bigger)'},
        
        # Level 3-4: Forward by 2s
        3:  {'step': 2,  'direction': 'forward',  'min_start': 2,   'max_start': 10,  'cells': 12, 'rows': 3, 'blanks_per_row': 7,  'allow_negative': False, 'name': 'Count by 2s (even)', 'force_even': True},
        4:  {'step': 2,  'direction': 'forward',  'min_start': 1,   'max_start': 11,  'cells': 12, 'rows': 3, 'blanks_per_row': 7,  'allow_negative': False, 'name': 'Count by 2s (odd)', 'force_odd': True},
        
        # Level 5-6: Forward by 5s and 10s
        5:  {'step': 5,  'direction': 'forward',  'min_start': 0,   'max_start': 25,  'cells': 10, 'rows': 3, 'blanks_per_row': 6,  'allow_negative': False, 'name': 'Count by 5s'},
        6:  {'step': 10, 'direction': 'forward',  'min_start': 0,   'max_start': 30,  'cells': 8,  'rows': 3, 'blanks_per_row': 5,  'allow_negative': False, 'name': 'Count by 10s'},
        
        # Level 7-9: Backwards
        7:  {'step': 1,  'direction': 'backward', 'min_start': 15,  'max_start': 25,  'cells': 12, 'rows': 3, 'blanks_per_row': 8,  'allow_negative': False, 'name': 'Count back by 1s'},
        8:  {'step': 2,  'direction': 'backward', 'min_start': 20,  'max_start': 30,  'cells': 10, 'rows': 3, 'blanks_per_row': 6,  'allow_negative': False, 'name': 'Count back by 2s'},
        9:  {'step': 5,  'direction': 'backward', 'min_start': 40,  'max_start': 60,  'cells': 10, 'rows': 3, 'blanks_per_row': 6,  'allow_negative': False, 'name': 'Count back by 5s'},
        
        # Level 10-12: Through zero and negatives
        10: {'step': 1,  'direction': 'forward',  'min_start': -5,  'max_start': -3,  'cells': 12, 'rows': 3, 'blanks_per_row': 7,  'allow_negative': True, 'name': 'Through zero (+1)'},
        11: {'step': 2,  'direction': 'forward',  'min_start': -12, 'max_start': -8,  'cells': 10, 'rows': 3, 'blanks_per_row': 6,  'allow_negative': True, 'name': 'Negatives by 2s'},
        12: {'step': 2,  'direction': 'backward', 'min_start': 8,   'max_start': 12,  'cells': 12, 'rows': 4, 'blanks_per_row': 7,  'allow_negative': True, 'name': 'Back through zero'},
    }
    return configs.get(level, configs[1])


def generate_counting_row(config: dict) -> dict:
    """Generate a single row of the counting sequence"""
    import random
    step = config['step']
    direction = config['direction']
    cells = config['cells']
    blanks = config['blanks_per_row']
    
    # Determine start value
    start = random.randint(config['min_start'], config['max_start'])
    
    # Force even/odd for levels 3-4
    if config.get('force_even') and start % 2 != 0:
        start += 1
    if config.get('force_odd') and start % 2 == 0:
        start += 1
    
    # Generate the full sequence
    sequence = []
    current = start
    for i in range(cells):
        sequence.append(current)
        if direction == 'forward':
            current += step
        else:
            current -= step
    
    # Show at least 3-4 cells at the start as hints
    hints_at_start = random.randint(3, min(5, cells - blanks))
    
    # Create blank positions
    available_positions = list(range(hints_at_start, cells))
    random.shuffle(available_positions)
    blank_positions = set(available_positions[:blanks])
    
    # Build the row data
    row_data = []
    for i, value in enumerate(sequence):
        row_data.append({
            'value': value,
            'is_blank': i in blank_positions,
            'position': i
        })
    
    return {
        'cells': row_data,
        'start': start,
        'step': step,
        'direction': direction
    }


def generate_counting_puzzle(level: int) -> dict:
    """Generate a complete counting puzzle for the given level"""
    import random
    config = get_counting_level_config(level)
    
    rows = []
    for i in range(config['rows']):
        row_config = config.copy()
        
        # Vary start for each row
        if config['direction'] == 'forward':
            row_config['min_start'] = config['min_start'] + (i * config['step'] * 2)
            row_config['max_start'] = config['max_start'] + (i * config['step'] * 2)
        else:
            row_config['min_start'] = config['min_start'] + (i * config['step'])
            row_config['max_start'] = config['max_start'] + (i * config['step'])
        
        rows.append(generate_counting_row(row_config))
    
    # Count total blanks
    total_blanks = sum(
        sum(1 for cell in row['cells'] if cell['is_blank'])
        for row in rows
    )
    
    # Simple instruction based on level
    if level <= 2:
        instruction = "Fill in the missing numbers. Count forward by 1."
    elif level <= 4:
        instruction = "Fill in the missing numbers. Count forward by 2."
    elif level == 5:
        instruction = "Fill in the missing numbers. Count forward by 5."
    elif level == 6:
        instruction = "Fill in the missing numbers. Count forward by 10."
    elif level == 7:
        instruction = "Fill in the missing numbers. Count backwards by 1."
    elif level == 8:
        instruction = "Fill in the missing numbers. Count backwards by 2."
    elif level == 9:
        instruction = "Fill in the missing numbers. Count backwards by 5."
    elif level == 10:
        instruction = "Fill in the missing numbers. Count through zero!"
    elif level == 11:
        instruction = "Fill in the missing numbers. Counting with negative numbers."
    else:
        instruction = "Fill in the missing numbers. Count backwards through zero!"
    
    return {
        'level': level,
        'level_name': config['name'],
        'rows': rows,
        'total_blanks': total_blanks,
        'step': config['step'],
        'direction': config['direction'],
        'instruction': instruction,
        'allow_negative': config['allow_negative']
    }


@interactive_bp.route('/api/mastering-counting/question/<int:level>')
@guest_or_login_required
@approved_required
def get_counting_question(level):
    """Get a Mastering Counting puzzle for the specified level (1-12)"""
    if level < 1 or level > 12:
        level = 1
    
    puzzle = generate_counting_puzzle(level)
    
    return jsonify({
        'success': True,
        'puzzle': puzzle
    })


@interactive_bp.route('/api/mastering-counting/complete', methods=['POST'])
@guest_or_login_required
def complete_mastering_counting():
    """Record completion of a Mastering Counting puzzle and award points"""
    from sqlalchemy import text
    
    data = request.get_json()
    level = data.get('level', 1)
    total_blanks = data.get('total_blanks', 10)
    correct_count = data.get('correct_count', 0)
    time_taken = data.get('time_taken', 0)
    
    # Calculate points
    # Base: 5 + (level × 2) for perfect score
    # Partial credit for incomplete
    base_points = 5 + (level * 2)
    
    if correct_count >= total_blanks:
        # Perfect - all blanks filled correctly
        points = base_points
        # Time bonus for speed (under 60 seconds)
        if time_taken < 60:
            points += 3
        elif time_taken < 90:
            points += 1
    else:
        # Partial credit
        completion_ratio = correct_count / max(total_blanks, 1)
        points = max(1, int(base_points * completion_ratio))
    
    # Award points
    guest_code = session.get('guest_code')
    user_id = session.get('user_id') if not session.get('is_guest') else None
    
    try:
        if guest_code:
            db.session.execute(text("""
                UPDATE guest_users 
                SET total_score = total_score + :points
                WHERE guest_code = :code
            """), {'points': points, 'code': guest_code})
            db.session.commit()
        elif user_id:
            db.session.execute(text("""
                UPDATE users 
                SET score = score + :points
                WHERE id = :user_id
            """), {'points': points, 'user_id': user_id})
            db.session.commit()
    except Exception as e:
        print(f"Could not award Mastering Counting points: {e}")
        db.session.rollback()
    
    return jsonify({
        'success': True,
        'points_earned': points,
        'perfect': correct_count >= total_blanks
    })


# =============================================================================
# WORDS TO NUMBERS - MATCHING ACTIVITY (NUMERACY STRAND)
# =============================================================================

# Number words mapping
WORDS_NUMBER_MAP = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
    30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
    70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'one hundred',
}

WORDS_TENS_MAP = {
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
    60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
}

WORDS_ONES_MAP = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
}

MATH_VOCAB_LIST = [
    ('plus', '+'), ('minus', '−'), ('equals', '='), ('add', '+'),
    ('take away', '−'), ('subtract', '−'), ('multiply', '×'), ('times', '×'),
    ('divide', '÷'), ('shared by', '÷'), ('greater than', '>'), ('less than', '<'),
    ('half', '½'), ('quarter', '¼'), ('double', '×2'), ('total', '='),
]


def words_number_to_word(n: int) -> str:
    """Convert a number to its word form"""
    if n in WORDS_NUMBER_MAP:
        return WORDS_NUMBER_MAP[n]
    if 21 <= n <= 99:
        tens = (n // 10) * 10
        ones = n % 10
        if ones == 0:
            return WORDS_TENS_MAP[tens]
        else:
            return f"{WORDS_TENS_MAP[tens]} {WORDS_ONES_MAP[ones]}"
    return str(n)


def get_words_level_config(level: int) -> dict:
    """Get configuration for Words to Numbers level"""
    configs = {
        1:  {'type': 'numbers', 'range': (1, 10),  'count': 6,  'name': 'Numbers 1-10'},
        2:  {'type': 'numbers', 'range': (1, 10),  'count': 8,  'name': 'Numbers 1-10'},
        3:  {'type': 'numbers', 'range': (11, 20), 'count': 6,  'name': 'Numbers 11-20'},
        4:  {'type': 'numbers', 'range': (11, 20), 'count': 8,  'name': 'Numbers 11-20'},
        5:  {'type': 'tens',    'range': (10, 100), 'count': 6, 'name': 'Counting by 10s'},
        6:  {'type': 'tens',    'range': (10, 100), 'count': 8, 'name': 'Counting by 10s'},
        7:  {'type': 'mixed',   'range': (1, 50),  'count': 6,  'name': 'Numbers to 50'},
        8:  {'type': 'mixed',   'range': (1, 50),  'count': 8,  'name': 'Numbers to 50'},
        9:  {'type': 'mixed',   'range': (1, 100), 'count': 6,  'name': 'Numbers to 100'},
        10: {'type': 'mixed',   'range': (1, 100), 'count': 8,  'name': 'Numbers to 100'},
        11: {'type': 'vocab',   'count': 6,  'name': 'Maths Words'},
        12: {'type': 'vocab',   'count': 8,  'name': 'Maths Words'},
    }
    return configs.get(level, configs[1])


def generate_words_pairs(level: int) -> list:
    """Generate word-number pairs for the given level"""
    import random
    config = get_words_level_config(level)
    pairs = []
    
    if config['type'] == 'vocab':
        vocab_items = random.sample(MATH_VOCAB_LIST, min(config['count'], len(MATH_VOCAB_LIST)))
        for word, symbol in vocab_items:
            pairs.append({'word': word, 'value': symbol, 'display': symbol})
    
    elif config['type'] == 'tens':
        tens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        selected = random.sample(tens, min(config['count'], len(tens)))
        for n in selected:
            pairs.append({'word': words_number_to_word(n), 'value': n, 'display': str(n)})
    
    elif config['type'] == 'numbers':
        min_val, max_val = config['range']
        numbers = list(range(min_val, max_val + 1))
        selected = random.sample(numbers, min(config['count'], len(numbers)))
        for n in selected:
            pairs.append({'word': words_number_to_word(n), 'value': n, 'display': str(n)})
    
    else:  # mixed
        min_val, max_val = config['range']
        candidates = []
        simple = [n for n in range(1, 21) if min_val <= n <= max_val]
        candidates.extend(simple)
        tens = [n for n in [20, 30, 40, 50, 60, 70, 80, 90, 100] if min_val <= n <= max_val]
        candidates.extend(tens)
        compounds = [n for n in range(21, max_val + 1) if n % 10 != 0]
        candidates.extend(random.sample(compounds, min(10, len(compounds))))
        candidates = list(set(candidates))
        selected = random.sample(candidates, min(config['count'], len(candidates)))
        for n in selected:
            pairs.append({'word': words_number_to_word(n), 'value': n, 'display': str(n)})
    
    return pairs


def generate_words_to_numbers(level: int, mode: str = 'chain') -> dict:
    """Generate a complete Words to Numbers puzzle"""
    import random
    config = get_words_level_config(level)
    pairs = generate_words_pairs(level)
    
    words = [p['word'] for p in pairs]
    values = [p['display'] for p in pairs]
    random.shuffle(words)
    random.shuffle(values)
    
    answer_key = {p['word']: p['display'] for p in pairs}
    
    if mode == 'jigsaw':
        time_limit = 120
        instruction = "Drag the word pieces to match the numbers!"
    elif mode == 'balloon':
        time_limit = 60
        instruction = "Pop the matching pairs before time runs out!"
    else:
        time_limit = 90
        instruction = "Tap a word, then tap its matching number!"
    
    return {
        'level': level,
        'level_name': config['name'],
        'mode': mode,
        'pairs': pairs,
        'words': words,
        'values': values,
        'answer_key': answer_key,
        'total_pairs': len(pairs),
        'time_limit': time_limit,
        'instruction': instruction
    }


@interactive_bp.route('/api/words-to-numbers/question/<int:level>')
@guest_or_login_required
@approved_required
def get_words_to_numbers_question(level):
    """Get a Words to Numbers puzzle for the specified level"""
    if level < 1 or level > 12:
        level = 1
    
    mode = request.args.get('mode', 'chain')
    puzzle = generate_words_to_numbers(level, mode)
    
    return jsonify({
        'success': True,
        'puzzle': puzzle
    })


@interactive_bp.route('/api/words-to-numbers/complete', methods=['POST'])
@guest_or_login_required
def complete_words_to_numbers():
    """Record completion of Words to Numbers and award points"""
    from sqlalchemy import text
    
    data = request.get_json()
    level = data.get('level', 1)
    total_pairs = data.get('total_pairs', 6)
    correct_count = data.get('correct_count', 0)
    mode = data.get('mode', 'chain')
    time_taken = data.get('time_taken', 0)
    
    # Calculate points
    base_points = 5 + (level * 2)
    
    if correct_count >= total_pairs:
        points = base_points
        # Time bonus
        if mode == 'balloon' and time_taken < 30:
            points += 5
        elif time_taken < 45:
            points += 3
        elif time_taken < 60:
            points += 1
    else:
        completion_ratio = correct_count / max(total_pairs, 1)
        points = max(1, int(base_points * completion_ratio))
    
    # Award points
    guest_code = session.get('guest_code')
    user_id = session.get('user_id') if not session.get('is_guest') else None
    
    try:
        if guest_code:
            db.session.execute(text("""
                UPDATE guest_users 
                SET total_score = total_score + :points
                WHERE guest_code = :code
            """), {'points': points, 'code': guest_code})
            db.session.commit()
        elif user_id:
            db.session.execute(text("""
                UPDATE users 
                SET score = score + :points
                WHERE id = :user_id
            """), {'points': points, 'user_id': user_id})
            db.session.commit()
    except Exception as e:
        print(f"Could not award Words to Numbers points: {e}")
        db.session.rollback()
    
    return jsonify({
        'success': True,
        'points_earned': points,
        'perfect': correct_count >= total_pairs
    })


# =============================================================================
# ORDERING & NUMBER LINES - INTERACTIVE ACTIVITY (NUMERACY STRAND)
# =============================================================================

def get_ordering_level_config(level: int) -> dict:
    """Get configuration for Ordering level"""
    configs = {
        # Levels 1-4: Sorting mode
        1:  {'mode': 'sort', 'min': 1,    'max': 10,   'count': 4, 'name': 'Order to 10'},
        2:  {'mode': 'sort', 'min': 1,    'max': 20,   'count': 5, 'name': 'Order to 20'},
        3:  {'mode': 'sort', 'min': 1,    'max': 50,   'count': 5, 'name': 'Order to 50'},
        4:  {'mode': 'sort', 'min': 1,    'max': 100,  'count': 6, 'name': 'Order to 100'},
        # Levels 5-10: Number line mode (positive)
        5:  {'mode': 'line', 'min': 0,    'max': 100,  'count': 4, 'name': 'Number Line 0-100'},
        6:  {'mode': 'line', 'min': 0,    'max': 100,  'count': 5, 'name': 'Number Line 0-100'},
        7:  {'mode': 'line', 'min': 0,    'max': 500,  'count': 5, 'name': 'Number Line 0-500'},
        8:  {'mode': 'line', 'min': 0,    'max': 1000, 'count': 5, 'name': 'Number Line 0-1000'},
        9:  {'mode': 'line', 'min': 0,    'max': 1000, 'count': 6, 'name': 'Number Line 0-1000'},
        10: {'mode': 'line', 'min': 0,    'max': 1200, 'count': 6, 'name': 'Number Line 0-1200'},
        # Levels 11-12: Number line with negatives
        11: {'mode': 'line', 'min': -50,  'max': 50,   'count': 5, 'name': 'Negatives -50 to 50'},
        12: {'mode': 'line', 'min': -100, 'max': 100,  'count': 6, 'name': 'Negatives -100 to 100'},
    }
    return configs.get(level, configs[1])


def generate_sort_numbers(config: dict) -> list:
    """Generate numbers for sorting mode"""
    import random
    min_val, max_val, count = config['min'], config['max'], config['count']
    range_size = max_val - min_val
    step = range_size // (count + 1)
    
    numbers = []
    for i in range(count):
        base = min_val + (i + 1) * step
        variance = max(1, step // 3)
        num = base + random.randint(-variance, variance)
        num = max(min_val, min(max_val, num))
        numbers.append(num)
    
    numbers = list(set(numbers))
    while len(numbers) < count:
        new_num = random.randint(min_val, max_val)
        if new_num not in numbers:
            numbers.append(new_num)
    return numbers[:count]


def generate_line_numbers(config: dict) -> list:
    """Generate numbers for number line mode"""
    import random
    min_val, max_val, count = config['min'], config['max'], config['count']
    buffer = (max_val - min_val) // 20
    effective_min, effective_max = min_val + buffer, max_val - buffer
    
    numbers = []
    attempts = 0
    while len(numbers) < count and attempts < 100:
        num = random.randint(effective_min, effective_max)
        if max_val - min_val >= 500:
            num = round(num / 5) * 5
        min_gap = (max_val - min_val) // (count + 2)
        too_close = any(abs(num - existing) < min_gap for existing in numbers)
        if not too_close and num not in numbers:
            numbers.append(num)
        attempts += 1
    
    if len(numbers) < count:
        step = (effective_max - effective_min) // (count + 1)
        numbers = [effective_min + (i + 1) * step for i in range(count)]
    return numbers[:count]


def generate_ordering_puzzle(level: int) -> dict:
    """Generate a complete Ordering puzzle"""
    config = get_ordering_level_config(level)
    mode = config['mode']
    
    if mode == 'sort':
        numbers = generate_sort_numbers(config)
        correct_order = sorted(numbers)
        return {
            'level': level,
            'level_name': config['name'],
            'mode': 'sort',
            'numbers': numbers,
            'correct_order': correct_order,
            'count': len(numbers),
            'instruction': 'Put these numbers in order from smallest to largest'
        }
    else:
        numbers = generate_line_numbers(config)
        line_min, line_max = config['min'], config['max']
        positions = {}
        for num in numbers:
            percent = ((num - line_min) / (line_max - line_min)) * 100
            positions[num] = round(percent, 1)
        
        range_size = line_max - line_min
        if range_size <= 100:
            tick_step = 10
        elif range_size <= 200:
            tick_step = 20
        elif range_size <= 500:
            tick_step = 50
        else:
            tick_step = 100
        ticks = list(range(line_min, line_max + 1, tick_step))
        
        return {
            'level': level,
            'level_name': config['name'],
            'mode': 'line',
            'numbers': numbers,
            'positions': positions,
            'line_min': line_min,
            'line_max': line_max,
            'ticks': ticks,
            'count': len(numbers),
            'instruction': 'Drag each number to its position on the number line',
            'tolerance': 5
        }


@interactive_bp.route('/api/ordering/question/<int:level>')
@guest_or_login_required
@approved_required
def get_ordering_question(level):
    """Get an Ordering puzzle for the specified level"""
    if level < 1 or level > 12:
        level = 1
    puzzle = generate_ordering_puzzle(level)
    return jsonify({'success': True, 'puzzle': puzzle})


@interactive_bp.route('/api/ordering/complete', methods=['POST'])
@guest_or_login_required
def complete_ordering():
    """Record completion of Ordering puzzle and award points"""
    from sqlalchemy import text
    
    data = request.get_json()
    level = data.get('level', 1)
    correct_count = data.get('correct_count', 0)
    total_count = data.get('total_count', 4)
    time_taken = data.get('time_taken', 0)
    
    base_points = 5 + (level * 2)
    if correct_count >= total_count:
        points = base_points
        if time_taken < 30:
            points += 5
        elif time_taken < 60:
            points += 2
    else:
        completion_ratio = correct_count / max(total_count, 1)
        points = max(1, int(base_points * completion_ratio))
    
    guest_code = session.get('guest_code')
    user_id = session.get('user_id') if not session.get('is_guest') else None
    
    try:
        if guest_code:
            db.session.execute(text("""
                UPDATE guest_users SET total_score = total_score + :points
                WHERE guest_code = :code
            """), {'points': points, 'code': guest_code})
            db.session.commit()
        elif user_id:
            db.session.execute(text("""
                UPDATE users SET score = score + :points WHERE id = :user_id
            """), {'points': points, 'user_id': user_id})
            db.session.commit()
    except Exception as e:
        print(f"Could not award Ordering points: {e}")
        db.session.rollback()
    
    return jsonify({
        'success': True,
        'points_earned': points,
        'perfect': correct_count >= total_count
    })


# =============================================================================
# NUMBER BONDS POP - INTERACTIVE ACTIVITY (NUMERACY STRAND)
# =============================================================================

def get_bonds_level_config(level: int) -> dict:
    """Get configuration for Number Bonds level"""
    configs = {
        1:  {'target': 10,   'pairs': 4,  'distractors': 2, 'name': 'Bonds to 10'},
        2:  {'target': 10,   'pairs': 5,  'distractors': 3, 'name': 'Bonds to 10'},
        3:  {'target': 20,   'pairs': 5,  'distractors': 3, 'name': 'Bonds to 20'},
        4:  {'target': 20,   'pairs': 6,  'distractors': 4, 'name': 'Bonds to 20'},
        5:  {'target': 50,   'pairs': 5,  'distractors': 4, 'name': 'Bonds to 50'},
        6:  {'target': 50,   'pairs': 6,  'distractors': 5, 'name': 'Bonds to 50'},
        7:  {'target': 100,  'pairs': 5,  'distractors': 4, 'name': 'Bonds to 100'},
        8:  {'target': 100,  'pairs': 6,  'distractors': 5, 'name': 'Bonds to 100'},
        9:  {'target': 100,  'pairs': 7,  'distractors': 5, 'name': 'Bonds to 100 Challenge'},
        10: {'target': 100,  'pairs': 8,  'distractors': 6, 'name': 'Bonds to 100 Challenge'},
        11: {'target': 1000, 'pairs': 6,  'distractors': 5, 'name': 'Bonds to 1000'},
        12: {'target': 1000, 'pairs': 7,  'distractors': 6, 'name': 'Bonds to 1000'},
    }
    return configs.get(level, configs[1])


def generate_bond_pairs(target: int, num_pairs: int) -> list:
    """Generate pairs of numbers that add to target"""
    import random
    pairs = []
    used = set()
    possible = list(range(1, min(target, 100)))
    random.shuffle(possible)
    for first in possible:
        if len(pairs) >= num_pairs:
            break
        second = target - first
        if second > 0 and first not in used and second not in used:
            pairs.append((first, second))
            used.add(first)
            used.add(second)
    return pairs


def generate_bonds_distractors(target: int, num_dist: int, existing: set) -> list:
    """Generate distractor numbers"""
    import random
    distractors = []
    attempts = 0
    while len(distractors) < num_dist and attempts < 100:
        num = random.randint(1, min(target + 20, 500))
        complement = target - num
        if num not in existing and complement not in existing:
            distractors.append(num)
            existing.add(num)
        attempts += 1
    return distractors


def generate_bonds_puzzle(level: int) -> dict:
    """Generate Number Bonds puzzle"""
    import random
    config = get_bonds_level_config(level)
    target = config['target']
    pairs = generate_bond_pairs(target, config['pairs'])
    
    all_numbers = []
    existing = set()
    for a, b in pairs:
        all_numbers.extend([a, b])
        existing.update([a, b])
    
    distractors = generate_bonds_distractors(target, config['distractors'], existing)
    all_numbers.extend(distractors)
    random.shuffle(all_numbers)
    
    bubbles = []
    for i, num in enumerate(all_numbers):
        bubbles.append({
            'id': i, 'value': num,
            'x': random.randint(10, 85), 'y': random.randint(10, 80),
            'size': random.choice(['small', 'medium', 'large'])
        })
    
    return {
        'level': level, 'level_name': config['name'], 'target': target,
        'bubbles': bubbles, 'pairs': pairs, 'total_pairs': len(pairs),
        'instruction': f'Pop pairs that add to {target}!'
    }


@interactive_bp.route('/api/number-bonds/question/<int:level>')
@guest_or_login_required
@approved_required
def get_bonds_question(level):
    """Get a Number Bonds puzzle"""
    if level < 1 or level > 12:
        level = 1
    puzzle = generate_bonds_puzzle(level)
    return jsonify({'success': True, 'puzzle': puzzle})


@interactive_bp.route('/api/number-bonds/complete', methods=['POST'])
@guest_or_login_required
def complete_bonds():
    """Record Number Bonds completion"""
    from sqlalchemy import text
    data = request.get_json()
    level = data.get('level', 1)
    pairs_found = data.get('pairs_found', 0)
    total_pairs = data.get('total_pairs', 4)
    time_taken = data.get('time_taken', 0)
    
    base_points = 5 + (level * 2)
    if pairs_found >= total_pairs:
        points = base_points + (5 if time_taken < 30 else 2 if time_taken < 60 else 0)
    else:
        points = max(1, int(base_points * (pairs_found / max(total_pairs, 1))))
    
    guest_code = session.get('guest_code')
    user_id = session.get('user_id') if not session.get('is_guest') else None
    try:
        if guest_code:
            db.session.execute(text("UPDATE guest_users SET total_score = total_score + :p WHERE guest_code = :c"), {'p': points, 'c': guest_code})
            db.session.commit()
        elif user_id:
            db.session.execute(text("UPDATE users SET score = score + :p WHERE id = :u"), {'p': points, 'u': user_id})
            db.session.commit()
    except Exception as e:
        print(f"Could not award Number Bonds points: {e}")
        db.session.rollback()
    
    return jsonify({'success': True, 'points_earned': points, 'perfect': pairs_found >= total_pairs})


# =============================================================================
# PLACE VALUE BUILDER - INTERACTIVE ACTIVITY (NUMERACY STRAND)
# =============================================================================

PLACE_NAMES = {
    'hundred_thousands': 'hundred thousands', 'ten_thousands': 'ten thousands',
    'thousands': 'thousands', 'hundreds': 'hundreds', 'tens': 'tens',
    'ones': 'ones', 'tenths': 'tenths', 'hundredths': 'hundredths'
}

def get_placevalue_level_config(level: int) -> dict:
    """Get configuration for Place Value level"""
    configs = {
        1:  {'digits': 2, 'decimal': False, 'clue_type': 'words',   'name': '2 Digits (Words)'},
        2:  {'digits': 2, 'decimal': False, 'clue_type': 'mixed',   'name': '2 Digits'},
        3:  {'digits': 3, 'decimal': False, 'clue_type': 'words',   'name': '3 Digits (Words)'},
        4:  {'digits': 3, 'decimal': False, 'clue_type': 'mixed',   'name': '3 Digits'},
        5:  {'digits': 4, 'decimal': False, 'clue_type': 'words',   'name': '4 Digits (Words)'},
        6:  {'digits': 4, 'decimal': False, 'clue_type': 'mixed',   'name': '4 Digits'},
        7:  {'digits': 5, 'decimal': False, 'clue_type': 'words',   'name': '5 Digits (Words)'},
        8:  {'digits': 5, 'decimal': False, 'clue_type': 'mixed',   'name': '5 Digits'},
        9:  {'digits': 6, 'decimal': False, 'clue_type': 'mixed',   'name': '6 Digits'},
        10: {'digits': 6, 'decimal': False, 'clue_type': 'reverse', 'name': '6 Digits (Reverse)'},
        11: {'digits': 4, 'decimal': True,  'clue_type': 'words',   'name': 'Decimals (Words)'},
        12: {'digits': 4, 'decimal': True,  'clue_type': 'mixed',   'name': 'Decimals'},
    }
    return configs.get(level, configs[1])


def generate_placevalue_number(num_digits: int, has_decimal: bool) -> dict:
    """Generate target number for Place Value"""
    import random
    if has_decimal:
        whole = random.randint(10, 99)
        dec = random.randint(1, 99)
        number = float(f"{whole}.{dec:02d}")
        digits = {'tens': whole // 10, 'ones': whole % 10, 'tenths': dec // 10, 'hundredths': dec % 10}
        places = ['tens', 'ones', 'tenths', 'hundredths']
    else:
        if num_digits == 2:
            number = random.randint(10, 99)
            digits = {'tens': number // 10, 'ones': number % 10}
            places = ['tens', 'ones']
        elif num_digits == 3:
            number = random.randint(100, 999)
            digits = {'hundreds': number // 100, 'tens': (number // 10) % 10, 'ones': number % 10}
            places = ['hundreds', 'tens', 'ones']
        elif num_digits == 4:
            number = random.randint(1000, 9999)
            digits = {'thousands': number // 1000, 'hundreds': (number // 100) % 10, 'tens': (number // 10) % 10, 'ones': number % 10}
            places = ['thousands', 'hundreds', 'tens', 'ones']
        elif num_digits == 5:
            number = random.randint(10000, 99999)
            digits = {'ten_thousands': number // 10000, 'thousands': (number // 1000) % 10, 'hundreds': (number // 100) % 10, 'tens': (number // 10) % 10, 'ones': number % 10}
            places = ['ten_thousands', 'thousands', 'hundreds', 'tens', 'ones']
        else:
            number = random.randint(100000, 999999)
            digits = {'hundred_thousands': number // 100000, 'ten_thousands': (number // 10000) % 10, 'thousands': (number // 1000) % 10, 'hundreds': (number // 100) % 10, 'tens': (number // 10) % 10, 'ones': number % 10}
            places = ['hundred_thousands', 'ten_thousands', 'thousands', 'hundreds', 'tens', 'ones']
    return {'number': number, 'digits': digits, 'places': places}


def generate_placevalue_clue(digits: dict, places: list, number, clue_type: str) -> str:
    """Generate clue for Place Value"""
    import random
    if clue_type == 'words':
        return ', '.join([f"{digits[p]} {PLACE_NAMES[p]}" for p in places if p in digits])
    elif clue_type == 'reverse':
        return "What number has " + ', '.join([f"{digits[p]} in the {PLACE_NAMES[p]} place" for p in places if p in digits]) + "?"
    else:
        if random.random() < 0.4:
            return f"Build the number: {number}"
        return ', '.join([f"{digits[p]} {PLACE_NAMES[p]}" for p in places if p in digits])


def generate_placevalue_puzzle(level: int) -> dict:
    """Generate Place Value puzzle"""
    import random
    config = get_placevalue_level_config(level)
    num_data = generate_placevalue_number(config['digits'], config['decimal'])
    clue = generate_placevalue_clue(num_data['digits'], num_data['places'], num_data['number'], config['clue_type'])
    
    digit_values = list(num_data['digits'].values())
    if level >= 5:
        for _ in range(1 if level < 9 else 2):
            digit_values.append(random.randint(0, 9))
    random.shuffle(digit_values)
    
    return {
        'level': level, 'level_name': config['name'], 'target_number': num_data['number'],
        'digits': num_data['digits'], 'places': num_data['places'], 'has_decimal': config['decimal'],
        'clue': clue, 'available_digits': digit_values, 'instruction': 'Drag the digits into the correct places!'
    }


@interactive_bp.route('/api/place-value/question/<int:level>')
@guest_or_login_required
@approved_required
def get_placevalue_question(level):
    """Get a Place Value puzzle"""
    if level < 1 or level > 12:
        level = 1
    puzzle = generate_placevalue_puzzle(level)
    return jsonify({'success': True, 'puzzle': puzzle})


@interactive_bp.route('/api/place-value/complete', methods=['POST'])
@guest_or_login_required
def complete_placevalue():
    """Record Place Value completion"""
    from sqlalchemy import text
    data = request.get_json()
    level = data.get('level', 1)
    correct = data.get('correct', False)
    time_taken = data.get('time_taken', 0)
    attempts = data.get('attempts', 1)
    
    base_points = 5 + (level * 2)
    if correct:
        points = base_points + (5 if time_taken < 20 else 2 if time_taken < 45 else 0)
        if attempts > 1:
            points = max(1, points - (attempts - 1) * 2)
    else:
        points = max(1, base_points // 3)
    
    guest_code = session.get('guest_code')
    user_id = session.get('user_id') if not session.get('is_guest') else None
    try:
        if guest_code:
            db.session.execute(text("UPDATE guest_users SET total_score = total_score + :p WHERE guest_code = :c"), {'p': points, 'c': guest_code})
            db.session.commit()
        elif user_id:
            db.session.execute(text("UPDATE users SET score = score + :p WHERE id = :u"), {'p': points, 'u': user_id})
            db.session.commit()
    except Exception as e:
        print(f"Could not award Place Value points: {e}")
        db.session.rollback()
    
    return jsonify({'success': True, 'points_earned': points, 'perfect': correct and attempts == 1})


# =============================================================================
# DOUBLE TROUBLE - INTERACTIVE ACTIVITY (NUMERACY STRAND)
# =============================================================================

def get_double_level_config(level: int) -> dict:
    """Get configuration for Double Trouble level"""
    configs = {
        1:  {'max_double': 10,  'include_halves': False, 'decimals': False, 'questions': 8,  'time_per_q': 8,  'name': 'Doubles to 10'},
        2:  {'max_double': 10,  'include_halves': False, 'decimals': False, 'questions': 10, 'time_per_q': 6,  'name': 'Doubles to 10'},
        3:  {'max_double': 20,  'include_halves': True,  'decimals': False, 'questions': 10, 'time_per_q': 6,  'name': 'Doubles & Halves to 20'},
        4:  {'max_double': 20,  'include_halves': True,  'decimals': False, 'questions': 12, 'time_per_q': 5,  'name': 'Doubles & Halves to 20'},
        5:  {'max_double': 50,  'include_halves': True,  'decimals': False, 'questions': 10, 'time_per_q': 6,  'name': 'Doubles & Halves to 50'},
        6:  {'max_double': 50,  'include_halves': True,  'decimals': False, 'questions': 12, 'time_per_q': 5,  'name': 'Doubles & Halves to 50'},
        7:  {'max_double': 100, 'include_halves': True,  'decimals': False, 'questions': 10, 'time_per_q': 6,  'name': 'Doubles & Halves to 100'},
        8:  {'max_double': 100, 'include_halves': True,  'decimals': False, 'questions': 12, 'time_per_q': 5,  'name': 'Doubles & Halves to 100'},
        9:  {'max_double': 100, 'include_halves': True,  'decimals': False, 'questions': 15, 'time_per_q': 4,  'name': 'Speed Challenge'},
        10: {'max_double': 100, 'include_halves': True,  'decimals': False, 'questions': 15, 'time_per_q': 3,  'name': 'Speed Challenge'},
        11: {'max_double': 50,  'include_halves': True,  'decimals': True,  'questions': 10, 'time_per_q': 6,  'name': 'Decimal Doubles'},
        12: {'max_double': 100, 'include_halves': True,  'decimals': True,  'questions': 12, 'time_per_q': 5,  'name': 'Decimal Doubles'},
    }
    return configs.get(level, configs[1])


def generate_double_question(config: dict) -> dict:
    """Generate a single double/half question"""
    import random
    is_double = True if not config['include_halves'] else random.choice([True, False])
    use_decimals = config['decimals']
    max_val = config['max_double']
    
    if use_decimals:
        if is_double:
            whole = random.randint(1, max_val // 2)
            dec = random.choice([0, 25, 5, 75])
            if dec == 25:
                number, answer = whole + 0.25, whole * 2 + 0.5
            elif dec == 5:
                number, answer = whole + 0.5, whole * 2 + 1
            elif dec == 75:
                number, answer = whole + 0.75, whole * 2 + 1.5
            else:
                number, answer = float(whole), float(whole * 2)
            text = f"Double {number}"
        else:
            base = random.randint(2, max_val)
            number, answer = float(base), base / 2
            text = f"Half of {number}"
    else:
        if is_double:
            number = random.randint(1, max_val)
            answer = number * 2
            text = f"Double {number}"
        else:
            number = random.randint(1, max_val // 2) * 2
            answer = number // 2
            text = f"Half of {number}"
    
    return {'type': 'double' if is_double else 'half', 'number': number, 'answer': answer, 'question_text': text}


def generate_double_trouble_set(level: int) -> dict:
    """Generate Double Trouble question set"""
    import random
    config = get_double_level_config(level)
    questions = []
    used = set()
    
    for i in range(config['questions']):
        for _ in range(20):
            q = generate_double_question(config)
            key = (q['type'], q['number'])
            if key not in used:
                used.add(key)
                q['id'] = i + 1
                questions.append(q)
                break
        else:
            q = generate_double_question(config)
            q['id'] = i + 1
            questions.append(q)
    
    return {
        'level': level, 'level_name': config['name'], 'questions': questions,
        'total_questions': len(questions), 'time_per_question': config['time_per_q'],
        'instruction': 'Answer as fast as you can!'
    }


@interactive_bp.route('/api/double-trouble/question/<int:level>')
@guest_or_login_required
@approved_required
def get_double_question(level):
    """Get a Double Trouble question set"""
    if level < 1 or level > 12:
        level = 1
    puzzle = generate_double_trouble_set(level)
    return jsonify({'success': True, 'puzzle': puzzle})


@interactive_bp.route('/api/double-trouble/complete', methods=['POST'])
@guest_or_login_required
def complete_double_trouble():
    """Record Double Trouble completion"""
    from sqlalchemy import text
    data = request.get_json()
    level = data.get('level', 1)
    correct_count = data.get('correct_count', 0)
    total_questions = data.get('total_questions', 10)
    total_time = data.get('total_time', 0)
    
    base_points = 5 + (level * 2)
    accuracy = correct_count / max(total_questions, 1)
    points = int(base_points * accuracy)
    if accuracy >= 0.9:
        points += 5
    elif accuracy >= 0.7:
        points += 2
    points = max(1, points)
    
    guest_code = session.get('guest_code')
    user_id = session.get('user_id') if not session.get('is_guest') else None
    try:
        if guest_code:
            db.session.execute(text("UPDATE guest_users SET total_score = total_score + :p WHERE guest_code = :c"), {'p': points, 'c': guest_code})
            db.session.commit()
        elif user_id:
            db.session.execute(text("UPDATE users SET score = score + :p WHERE id = :u"), {'p': points, 'u': user_id})
            db.session.commit()
    except Exception as e:
        print(f"Could not award Double Trouble points: {e}")
        db.session.rollback()
    
    return jsonify({'success': True, 'points_earned': points, 'perfect': correct_count >= total_questions})


# =============================================================================
# ADDITION BLITZ - Speed Addition Tables Practice
# =============================================================================

def get_addition_blitz_level_config(level: int) -> dict:
    """Get configuration for Addition Blitz level"""
    configs = {
        # Levels 1-4: Tables 1-4 (gentle introduction)
        1:  {'max_table': 2,  'questions': 8,  'time_per_q': 8, 'name': '1s and 2s'},
        2:  {'max_table': 3,  'questions': 10, 'time_per_q': 7, 'name': '1s to 3s'},
        3:  {'max_table': 4,  'questions': 10, 'time_per_q': 6, 'name': '1s to 4s'},
        4:  {'max_table': 4,  'questions': 12, 'time_per_q': 5, 'name': '1s to 4s Speed'},
        # Levels 5-8: Tables 1-8 (building fluency)
        5:  {'max_table': 6,  'questions': 10, 'time_per_q': 6, 'name': '1s to 6s'},
        6:  {'max_table': 7,  'questions': 12, 'time_per_q': 5, 'name': '1s to 7s'},
        7:  {'max_table': 8,  'questions': 12, 'time_per_q': 5, 'name': '1s to 8s'},
        8:  {'max_table': 8,  'questions': 15, 'time_per_q': 4, 'name': '1s to 8s Speed'},
        # Levels 9-12: Tables 1-12 (mastery)
        9:  {'max_table': 10, 'questions': 12, 'time_per_q': 5, 'name': '1s to 10s'},
        10: {'max_table': 11, 'questions': 15, 'time_per_q': 4, 'name': '1s to 11s'},
        11: {'max_table': 12, 'questions': 15, 'time_per_q': 4, 'name': 'Full Tables'},
        12: {'max_table': 12, 'questions': 20, 'time_per_q': 3, 'name': 'Master Speed'},
    }
    return configs.get(level, configs[1])


def generate_addition_question(config: dict) -> dict:
    """Generate a single addition question: a + b = ?"""
    import random
    # Pick two numbers from 1 to max_table
    a = random.randint(1, config['max_table'])
    b = random.randint(1, config['max_table'])
    answer = a + b
    text = f"{a} + {b}"
    return {'a': a, 'b': b, 'answer': answer, 'question_text': text}


def generate_addition_blitz_set(level: int) -> dict:
    """Generate Addition Blitz question set"""
    import random
    config = get_addition_blitz_level_config(level)
    questions = []
    used = set()
    
    for i in range(config['questions']):
        for _ in range(30):
            q = generate_addition_question(config)
            # Use sorted tuple to avoid a+b and b+a duplicates
            key = tuple(sorted([q['a'], q['b']]))
            if key not in used:
                used.add(key)
                q['id'] = i + 1
                questions.append(q)
                break
        else:
            q = generate_addition_question(config)
            q['id'] = i + 1
            questions.append(q)
    
    return {
        'level': level, 'level_name': config['name'], 'questions': questions,
        'total_questions': len(questions), 'time_per_question': config['time_per_q'],
        'instruction': 'Answer the addition as fast as you can!'
    }


@interactive_bp.route('/api/addition-blitz/question/<int:level>')
@guest_or_login_required
@approved_required
def get_addition_blitz_question(level):
    """Get an Addition Blitz question set"""
    if level < 1 or level > 12:
        level = 1
    puzzle = generate_addition_blitz_set(level)
    return jsonify({'success': True, 'puzzle': puzzle})


@interactive_bp.route('/api/addition-blitz/complete', methods=['POST'])
@guest_or_login_required
def complete_addition_blitz():
    """Record Addition Blitz completion"""
    from sqlalchemy import text
    data = request.get_json()
    level = data.get('level', 1)
    correct_count = data.get('correct_count', 0)
    total_questions = data.get('total_questions', 10)
    
    base_points = 5 + (level * 2)
    accuracy = correct_count / max(total_questions, 1)
    points = int(base_points * accuracy)
    if accuracy >= 0.9:
        points += 5
    elif accuracy >= 0.7:
        points += 2
    points = max(1, points)
    
    guest_code = session.get('guest_code')
    user_id = session.get('user_id') if not session.get('is_guest') else None
    try:
        if guest_code:
            db.session.execute(text("UPDATE guest_users SET total_score = total_score + :p WHERE guest_code = :c"), {'p': points, 'c': guest_code})
            db.session.commit()
        elif user_id:
            db.session.execute(text("UPDATE users SET score = score + :p WHERE id = :u"), {'p': points, 'u': user_id})
            db.session.commit()
    except Exception as e:
        print(f"Could not award Addition Blitz points: {e}")
        db.session.rollback()
    
    return jsonify({'success': True, 'points_earned': points, 'perfect': correct_count >= total_questions})


# =============================================================================
# TIMES TABLES BLITZ - Speed Multiplication Tables Practice
# =============================================================================

def get_times_tables_level_config(level: int) -> dict:
    """Get configuration for Times Tables Blitz level"""
    configs = {
        # Levels 1-4: Tables 1-4 (gentle introduction)
        1:  {'max_table': 2,  'questions': 8,  'time_per_q': 8, 'name': '1× and 2×'},
        2:  {'max_table': 3,  'questions': 10, 'time_per_q': 7, 'name': '1× to 3×'},
        3:  {'max_table': 4,  'questions': 10, 'time_per_q': 6, 'name': '1× to 4×'},
        4:  {'max_table': 4,  'questions': 12, 'time_per_q': 5, 'name': '1× to 4× Speed'},
        # Levels 5-8: Tables 1-8 (building fluency)
        5:  {'max_table': 6,  'questions': 10, 'time_per_q': 6, 'name': '1× to 6×'},
        6:  {'max_table': 7,  'questions': 12, 'time_per_q': 5, 'name': '1× to 7×'},
        7:  {'max_table': 8,  'questions': 12, 'time_per_q': 5, 'name': '1× to 8×'},
        8:  {'max_table': 8,  'questions': 15, 'time_per_q': 4, 'name': '1× to 8× Speed'},
        # Levels 9-12: Tables 1-12 (mastery)
        9:  {'max_table': 10, 'questions': 12, 'time_per_q': 5, 'name': '1× to 10×'},
        10: {'max_table': 11, 'questions': 15, 'time_per_q': 4, 'name': '1× to 11×'},
        11: {'max_table': 12, 'questions': 15, 'time_per_q': 4, 'name': 'Full Tables'},
        12: {'max_table': 12, 'questions': 20, 'time_per_q': 3, 'name': 'Master Speed'},
    }
    return configs.get(level, configs[1])


def generate_times_table_question(config: dict) -> dict:
    """Generate a single multiplication question: a × b = ?"""
    import random
    # Pick two numbers from 1 to max_table
    a = random.randint(1, config['max_table'])
    b = random.randint(1, config['max_table'])
    answer = a * b
    text = f"{a} × {b}"
    return {'a': a, 'b': b, 'answer': answer, 'question_text': text}


def generate_times_tables_set(level: int) -> dict:
    """Generate Times Tables Blitz question set"""
    import random
    config = get_times_tables_level_config(level)
    questions = []
    used = set()
    
    for i in range(config['questions']):
        for _ in range(30):
            q = generate_times_table_question(config)
            # Use sorted tuple to avoid a×b and b×a duplicates
            key = tuple(sorted([q['a'], q['b']]))
            if key not in used:
                used.add(key)
                q['id'] = i + 1
                questions.append(q)
                break
        else:
            q = generate_times_table_question(config)
            q['id'] = i + 1
            questions.append(q)
    
    return {
        'level': level, 'level_name': config['name'], 'questions': questions,
        'total_questions': len(questions), 'time_per_question': config['time_per_q'],
        'instruction': 'Answer the multiplication as fast as you can!'
    }


@interactive_bp.route('/api/times-tables/question/<int:level>')
@guest_or_login_required
@approved_required
def get_times_tables_question(level):
    """Get a Times Tables Blitz question set"""
    if level < 1 or level > 12:
        level = 1
    puzzle = generate_times_tables_set(level)
    return jsonify({'success': True, 'puzzle': puzzle})


@interactive_bp.route('/api/times-tables/complete', methods=['POST'])
@guest_or_login_required
def complete_times_tables():
    """Record Times Tables Blitz completion"""
    from sqlalchemy import text
    data = request.get_json()
    level = data.get('level', 1)
    correct_count = data.get('correct_count', 0)
    total_questions = data.get('total_questions', 10)
    
    base_points = 5 + (level * 2)
    accuracy = correct_count / max(total_questions, 1)
    points = int(base_points * accuracy)
    if accuracy >= 0.9:
        points += 5
    elif accuracy >= 0.7:
        points += 2
    points = max(1, points)
    
    guest_code = session.get('guest_code')
    user_id = session.get('user_id') if not session.get('is_guest') else None
    try:
        if guest_code:
            db.session.execute(text("UPDATE guest_users SET total_score = total_score + :p WHERE guest_code = :c"), {'p': points, 'c': guest_code})
            db.session.commit()
        elif user_id:
            db.session.execute(text("UPDATE users SET score = score + :p WHERE id = :u"), {'p': points, 'u': user_id})
            db.session.commit()
    except Exception as e:
        print(f"Could not award Times Tables points: {e}")
        db.session.rollback()
    
    return jsonify({'success': True, 'points_earned': points, 'perfect': correct_count >= total_questions})


# =============================================================================
# INTERACTIVE GAMES - LEVEL PERSISTENCE
# =============================================================================

@interactive_bp.route('/api/interactive/get-level/<topic>')
@guest_or_login_required
def get_interactive_level(topic):
    """Get saved level for an interactive game"""
    from sqlalchemy import text
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    try:
        if user_id:
            result = db.session.execute(text("""
                SELECT current_level FROM adaptive_progress
                WHERE user_id = :user_id AND topic = :topic
            """), {'user_id': user_id, 'topic': topic}).fetchone()
        elif guest_code:
            result = db.session.execute(text("""
                SELECT current_level FROM adaptive_progress
                WHERE guest_code = :guest_code AND topic = :topic
            """), {'guest_code': guest_code, 'topic': topic}).fetchone()
        else:
            result = None
        
        if result:
            return jsonify({'success': True, 'level': result[0]})
        else:
            return jsonify({'success': True, 'level': 1})
    except Exception as e:
        print(f"Error getting interactive level: {e}")
        return jsonify({'success': True, 'level': 1})


@interactive_bp.route('/api/interactive/save-level', methods=['POST'])
@guest_or_login_required
def save_interactive_level():
    """Save level for an interactive game"""
    from sqlalchemy import text
    
    data = request.get_json()
    topic = data.get('topic')
    level = data.get('level', 1)
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    if not topic:
        return jsonify({'error': 'Topic is required'}), 400
    
    try:
        if user_id:
            db.session.execute(text("""
                INSERT INTO adaptive_progress (user_id, topic, current_level, updated_at)
                VALUES (:user_id, :topic, :level, CURRENT_TIMESTAMP)
                ON CONFLICT(user_id, topic) DO UPDATE SET
                    current_level = MAX(adaptive_progress.current_level, :level),
                    updated_at = CURRENT_TIMESTAMP
            """), {'user_id': user_id, 'topic': topic, 'level': level})
        elif guest_code:
            db.session.execute(text("""
                INSERT INTO adaptive_progress (guest_code, topic, current_level, updated_at)
                VALUES (:guest_code, :topic, :level, CURRENT_TIMESTAMP)
                ON CONFLICT(guest_code, topic) DO UPDATE SET
                    current_level = MAX(adaptive_progress.current_level, :level),
                    updated_at = CURRENT_TIMESTAMP
            """), {'guest_code': guest_code, 'topic': topic, 'level': level})
        
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        db.session.rollback()
        print(f"Error saving interactive level: {e}")
        return jsonify({'error': str(e)}), 500


@interactive_bp.route('/api/interactive/reset-level', methods=['POST'])
@guest_or_login_required
def reset_interactive_level():
    """Reset level for an interactive game back to 1"""
    from sqlalchemy import text
    
    data = request.get_json()
    topic = data.get('topic')
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    if not topic:
        return jsonify({'error': 'Topic is required'}), 400
    
    try:
        if user_id:
            db.session.execute(text("""
                UPDATE adaptive_progress SET current_level = 1, updated_at = CURRENT_TIMESTAMP
                WHERE user_id = :user_id AND topic = :topic
            """), {'user_id': user_id, 'topic': topic})
        elif guest_code:
            db.session.execute(text("""
                UPDATE adaptive_progress SET current_level = 1, updated_at = CURRENT_TIMESTAMP
                WHERE guest_code = :guest_code AND topic = :topic
            """), {'guest_code': guest_code, 'topic': topic})
        
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        db.session.rollback()
        print(f"Error resetting interactive level: {e}")
        return jsonify({'error': str(e)}), 500


@interactive_bp.route('/api/award-points', methods=['POST'])
@guest_or_login_required
def award_points():
    """
    Award points to a user's account.
    Used by adaptive quiz and other features.
    Supports: registered users, repeat guests (with code), casual guests (no persist)
    """
    from sqlalchemy import text
    
    data = request.get_json()
    points = data.get('points', 0)
    source = data.get('source', 'unknown')
    topic = data.get('topic', '')
    level = data.get('level', 1)
    
    if points <= 0:
        return jsonify({'success': False, 'error': 'Invalid points value'}), 400
    
    guest_code = session.get('guest_code')
    user_id = session.get('user_id') if not session.get('is_guest') else None
    
    # REPEAT GUEST: Has guest_code - persist to guest_users table
    if guest_code:
        try:
            # Update guest_users.total_score
            db.session.execute(
                text("""
                    UPDATE guest_users 
                    SET total_score = total_score + :points
                    WHERE guest_code = :code
                """),
                {'points': points, 'code': guest_code}
            )
            db.session.commit()
            
            # Get updated total
            result = db.session.execute(
                text("SELECT total_score FROM guest_users WHERE guest_code = :code"),
                {'code': guest_code}
            ).fetchone()
            
            total_points = result[0] if result else points
            new_level = (total_points // 100) + 1
            
            print(f"📊 Awarded {points} points to repeat guest {guest_code} from {source} ({topic} L{level}) - Total: {total_points}")
            
            return jsonify({
                'success': True,
                'points_awarded': points,
                'total_points': total_points,
                'level': new_level
            })
            
        except Exception as e:
            db.session.rollback()
            print(f"Error awarding points to repeat guest: {e}")
            return jsonify({'error': str(e)}), 500
    
    # REGISTERED USER: Has user_id (not guest) - persist to user_stats table
    elif user_id:
        try:
            # Get or create user stats
            stats = UserStats.query.filter_by(user_id=user_id).first()
            if not stats:
                stats = UserStats(user_id=user_id, total_points=0, level=1)
                db.session.add(stats)
            
            # Add points
            stats.total_points += points
            
            # Recalculate level (every 100 points = 1 level)
            stats.level = (stats.total_points // 100) + 1
            
            db.session.commit()
            
            print(f"📊 Awarded {points} points to user {user_id} from {source} ({topic} L{level}) - Total: {stats.total_points}")
            
            return jsonify({
                'success': True,
                'points_awarded': points,
                'total_points': stats.total_points,
                'level': stats.level
            })
            
        except Exception as e:
            db.session.rollback()
            print(f"Error awarding points: {e}")
            return jsonify({'error': str(e)}), 500
    
    # CASUAL GUEST: No guest_code, no user_id - don't persist
    else:
        return jsonify({
            'success': True, 
            'points_awarded': points,
            'message': 'Points not persisted for casual guest users'
        })

# ===== END ADAPTIVE QUIZ BETA API =====
