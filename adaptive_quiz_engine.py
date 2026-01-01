"""
ADAPTIVE QUIZ ENGINE
====================
Serves questions from questions_adaptive table with intelligent progression.
Completely separate from the existing quiz system.

Features:
- Starts at appropriate level based on user history
- Adjusts difficulty based on performance
- Tracks skill mastery
- Provides personalised question selection

Usage:
    from adaptive_quiz_engine import register_adaptive_quiz_routes
    register_adaptive_quiz_routes(app, db)

Endpoints:
    POST /api/quiz-adaptive/start - Start an adaptive quiz session
    POST /api/quiz-adaptive/next - Get next question based on performance
    POST /api/quiz-adaptive/submit - Submit answer and get feedback
    GET /api/quiz-adaptive/status - Get current session status
"""

from flask import Blueprint, request, jsonify, session
from sqlalchemy import text
from datetime import datetime, timedelta
import json
import random
import traceback

# Blueprint for adaptive quiz routes
adaptive_quiz_bp = Blueprint('adaptive_quiz', __name__)

# Store for db instance
_db = None


def register_adaptive_quiz_routes(app, db):
    """Register adaptive quiz engine routes"""
    global _db
    _db = db
    
    app.register_blueprint(adaptive_quiz_bp, url_prefix='/api/quiz-adaptive')
    print("✓ Adaptive Quiz Engine routes registered at /api/quiz-adaptive")


def get_user_identifier():
    """Get user_id or guest_code from session"""
    try:
        if 'user_id' in session and 'is_guest' not in session:
            return {'user_id': session['user_id'], 'guest_code': None}
        if 'guest_code' in session:
            return {'user_id': None, 'guest_code': session['guest_code']}
    except Exception as e:
        print(f"Error getting user identifier: {e}")
    return None


def get_user_current_level(topic, user_id=None, guest_code=None):
    """
    Determine appropriate starting level for user on a topic.
    Uses saved level from user_adaptive_levels table.
    """
    try:
        # First check user_adaptive_levels table (our saved progress)
        if user_id:
            result = _db.session.execute(text("""
                SELECT current_level FROM user_adaptive_levels 
                WHERE user_id = :user_id AND topic = :topic
            """), {'user_id': user_id, 'topic': topic}).fetchone()
        elif guest_code:
            result = _db.session.execute(text("""
                SELECT current_level FROM user_adaptive_levels 
                WHERE guest_code = :guest_code AND topic = :topic
            """), {'guest_code': guest_code, 'topic': topic}).fetchone()
        else:
            return 1  # Default to level 1
        
        if result:
            return result[0]
        
        # No saved level, start at level 1
        return 1
        
    except Exception as e:
        print(f"Error getting user level: {e}")
        return 1


def select_question_for_level(topic, level, exclude_ids=None):
    """Select a question at the specified level"""
    try:
        exclude_ids = exclude_ids or []
        
        # Try exact level first
        if exclude_ids:
            # Use NOT IN clause
            placeholders = ','.join([':ex' + str(i) for i in range(len(exclude_ids))])
            params = {'topic': topic, 'level': level}
            for i, ex_id in enumerate(exclude_ids):
                params['ex' + str(i)] = ex_id
            
            query = f"""
                SELECT id, question_text, option_a, option_b, option_c, option_d,
                       correct_answer, explanation, difficulty_level, question_type,
                       hint_text, estimated_time_seconds, image_svg
                FROM questions_adaptive 
                WHERE topic = :topic 
                AND difficulty_level = :level 
                AND is_active = 1
                AND id NOT IN ({placeholders})
                ORDER BY RANDOM()
                LIMIT 1
            """
        else:
            params = {'topic': topic, 'level': level}
            query = """
                SELECT id, question_text, option_a, option_b, option_c, option_d,
                       correct_answer, explanation, difficulty_level, question_type,
                       hint_text, estimated_time_seconds, image_svg
                FROM questions_adaptive 
                WHERE topic = :topic 
                AND difficulty_level = :level 
                AND is_active = 1
                ORDER BY RANDOM()
                LIMIT 1
            """
        
        result = _db.session.execute(text(query), params).fetchone()
        
        # If no question at exact level, try adjacent levels
        if not result and level > 1:
            params['level'] = level - 1
            result = _db.session.execute(text(query.replace(':level', str(level - 1))), params).fetchone()
        
        if not result and level < 12:
            params['level'] = level + 1
            result = _db.session.execute(text(query.replace(':level', str(level + 1))), params).fetchone()
        
        # If still no result, try without exclusions
        if not result:
            simple_query = """
                SELECT id, question_text, option_a, option_b, option_c, option_d,
                       correct_answer, explanation, difficulty_level, question_type,
                       hint_text, estimated_time_seconds, image_svg
                FROM questions_adaptive 
                WHERE topic = :topic 
                AND difficulty_level = :level 
                AND is_active = 1
                ORDER BY RANDOM()
                LIMIT 1
            """
            result = _db.session.execute(text(simple_query), {'topic': topic, 'level': level}).fetchone()
        
        if not result:
            return None
        
        # Handle image_svg - might not exist in older databases
        try:
            image_svg = result[12]
        except (IndexError, KeyError):
            image_svg = None
        
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
            'image_svg': image_svg
        }
    except Exception as e:
        print(f"Error selecting question: {e}")
        traceback.print_exc()
        return None


def adjust_level(current_level, recent_results):
    """
    Adjust difficulty level based on recent performance.
    
    recent_results: list of booleans (True=correct, False=incorrect)
    
    Levels 1-10: Standard progression
    Level 11: Application (real-world problems) - unlocks after mastering Level 10
    Level 12: Linked Topics - requires Level 8+ in linked topics
    """
    if len(recent_results) < 3:
        return current_level
    
    # Look at last 5 questions
    recent = recent_results[-5:]
    correct_rate = sum(1 for r in recent if r) / len(recent)
    
    # Strong performance → level up
    if correct_rate >= 0.8 and len(recent) >= 3:
        # Check if last 3 were correct (streak)
        if all(recent[-3:]):
            return min(12, current_level + 1)  # Updated: cap at 12
    
    # Struggling → level down
    if correct_rate <= 0.3 and len(recent) >= 4:
        return max(1, current_level - 1)
    
    return current_level


def save_adaptive_progress(user_id, guest_code, topic, starting_level, ending_level, score, total_questions):
    """
    Save adaptive quiz progress to database.
    Records the attempt and updates user's level for the topic.
    """
    try:
        percentage = round((score / total_questions) * 100, 1) if total_questions > 0 else 0
        
        # Save to adaptive_quiz_history table (create if not exists)
        _db.session.execute(text("""
            CREATE TABLE IF NOT EXISTS adaptive_quiz_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                guest_code VARCHAR(20),
                topic VARCHAR(50) NOT NULL,
                starting_level INTEGER NOT NULL,
                ending_level INTEGER NOT NULL,
                score INTEGER NOT NULL,
                total_questions INTEGER NOT NULL,
                percentage REAL NOT NULL,
                completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """))
        
        # Insert the quiz attempt
        _db.session.execute(text("""
            INSERT INTO adaptive_quiz_history 
            (user_id, guest_code, topic, starting_level, ending_level, score, total_questions, percentage)
            VALUES (:user_id, :guest_code, :topic, :start, :end, :score, :total, :pct)
        """), {
            'user_id': user_id,
            'guest_code': guest_code,
            'topic': topic,
            'start': starting_level,
            'end': ending_level,
            'score': score,
            'total': total_questions,
            'pct': percentage
        })
        
        # Update user's current level for this topic in user_adaptive_levels table
        _db.session.execute(text("""
            CREATE TABLE IF NOT EXISTS user_adaptive_levels (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                guest_code VARCHAR(20),
                topic VARCHAR(50) NOT NULL,
                current_level INTEGER NOT NULL DEFAULT 1,
                highest_level INTEGER NOT NULL DEFAULT 1,
                total_quizzes INTEGER NOT NULL DEFAULT 0,
                total_correct INTEGER NOT NULL DEFAULT 0,
                total_questions INTEGER NOT NULL DEFAULT 0,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, guest_code, topic)
            )
        """))
        
        # Check if record exists
        if user_id:
            existing = _db.session.execute(text("""
                SELECT id, highest_level FROM user_adaptive_levels 
                WHERE user_id = :user_id AND topic = :topic
            """), {'user_id': user_id, 'topic': topic}).fetchone()
        else:
            existing = _db.session.execute(text("""
                SELECT id, highest_level FROM user_adaptive_levels 
                WHERE guest_code = :guest_code AND topic = :topic
            """), {'guest_code': guest_code, 'topic': topic}).fetchone()
        
        if existing:
            # Update existing record
            new_highest = max(existing[1], ending_level)
            if user_id:
                _db.session.execute(text("""
                    UPDATE user_adaptive_levels 
                    SET current_level = :level, 
                        highest_level = :highest,
                        total_quizzes = total_quizzes + 1,
                        total_correct = total_correct + :correct,
                        total_questions = total_questions + :total,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE user_id = :user_id AND topic = :topic
                """), {
                    'level': ending_level,
                    'highest': new_highest,
                    'correct': score,
                    'total': total_questions,
                    'user_id': user_id,
                    'topic': topic
                })
            else:
                _db.session.execute(text("""
                    UPDATE user_adaptive_levels 
                    SET current_level = :level, 
                        highest_level = :highest,
                        total_quizzes = total_quizzes + 1,
                        total_correct = total_correct + :correct,
                        total_questions = total_questions + :total,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE guest_code = :guest_code AND topic = :topic
                """), {
                    'level': ending_level,
                    'highest': new_highest,
                    'correct': score,
                    'total': total_questions,
                    'guest_code': guest_code,
                    'topic': topic
                })
        else:
            # Insert new record
            _db.session.execute(text("""
                INSERT INTO user_adaptive_levels 
                (user_id, guest_code, topic, current_level, highest_level, total_quizzes, total_correct, total_questions)
                VALUES (:user_id, :guest_code, :topic, :level, :highest, 1, :correct, :total)
            """), {
                'user_id': user_id,
                'guest_code': guest_code,
                'topic': topic,
                'level': ending_level,
                'highest': ending_level,
                'correct': score,
                'total': total_questions
            })
        
        _db.session.commit()
        print(f"✓ Saved adaptive progress: {topic} Level {starting_level}→{ending_level} ({score}/{total_questions})")
        
    except Exception as e:
        print(f"Error in save_adaptive_progress: {e}")
        traceback.print_exc()
        _db.session.rollback()


# ============================================================================
# QUIZ SESSION ROUTES
# ============================================================================

@adaptive_quiz_bp.route('/start', methods=['POST'])
def start_adaptive_quiz():
    """
    Start a new adaptive quiz session.
    
    Request body:
    {
        "topic": "solving_equations",
        "num_questions": 10,
        "mode": "adaptive" | "fixed_level",
        "fixed_level": 5  (only if mode is fixed_level)
    }
    """
    try:
        user = get_user_identifier()
        if not user:
            return jsonify({'error': 'Login required'}), 401
        
        data = request.get_json() or {}
        topic = data.get('topic')
        num_questions = data.get('num_questions', 10)
        mode = data.get('mode', 'adaptive')
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        # Check if topic has adaptive questions
        count = _db.session.execute(text("""
            SELECT COUNT(*) FROM questions_adaptive WHERE topic = :topic AND is_active = 1
        """), {'topic': topic}).fetchone()[0]
        
        if count < 10:
            return jsonify({
                'error': f'Not enough adaptive questions for {topic}. Found: {count}, Need: 10+',
                'available': count
            }), 400
        
        # Determine starting level
        if mode == 'fixed_level':
            starting_level = data.get('fixed_level', 5)
        else:
            starting_level = get_user_current_level(
                topic, 
                user_id=user['user_id'], 
                guest_code=user['guest_code']
            )
        
        # Get first question
        question = select_question_for_level(topic, starting_level)
        
        if not question:
            return jsonify({'error': 'Could not find questions for this topic'}), 500
        
        # Create session data
        quiz_session = {
            'topic': topic,
            'mode': mode,
            'current_level': starting_level,
            'starting_level': starting_level,
            'num_questions': num_questions,
            'questions_answered': 0,
            'correct_count': 0,
            'recent_results': [],
            'question_ids_shown': [question['id']],
            'started_at': datetime.utcnow().isoformat(),
            'current_question': question,
            'question_start_time': datetime.utcnow().isoformat(),
            'previous_level': starting_level
        }
        
        # Store in session
        session['adaptive_quiz'] = quiz_session
        session.modified = True  # IMPORTANT: Mark session as modified
        
        return jsonify({
            'success': True,
            'session_started': True,
            'topic': topic,
            'starting_level': starting_level,
            'total_questions': num_questions,
            'question_number': 1,
            'question': {
                'id': question['id'],
                'text': question['question_text'],
                'options': question['options'],
                'difficulty_level': question['difficulty_level'],
                'hint_available': bool(question.get('hint_text')),
                'estimated_time': question.get('estimated_time', 30),
                'image_svg': question.get('image_svg')
            }
        })
        
    except Exception as e:
        print(f"Error starting adaptive quiz: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@adaptive_quiz_bp.route('/submit', methods=['POST'])
def submit_adaptive_answer():
    """
    Submit answer for current question and get next.
    
    Request body:
    {
        "answer": 0-3,
        "time_taken": seconds
    }
    """
    try:
        if 'adaptive_quiz' not in session:
            return jsonify({'error': 'No active quiz session'}), 400
        
        quiz = session['adaptive_quiz']
        data = request.get_json() or {}
        
        answer = data.get('answer')
        time_taken = data.get('time_taken', 30)
        
        if answer is None:
            return jsonify({'error': 'Answer is required'}), 400
        
        current_q = quiz.get('current_question')
        if not current_q:
            return jsonify({'error': 'No current question'}), 400
        
        # Check answer
        is_correct = (answer == current_q['correct_answer'])
        
        # Update quiz state
        quiz['questions_answered'] += 1
        if is_correct:
            quiz['correct_count'] += 1
        quiz['recent_results'].append(is_correct)
        
        # Keep only last 10 results
        if len(quiz['recent_results']) > 10:
            quiz['recent_results'] = quiz['recent_results'][-10:]
        
        # Store previous level for comparison
        previous_level = quiz['current_level']
        
        # Adjust level if in adaptive mode
        if quiz['mode'] == 'adaptive':
            quiz['current_level'] = adjust_level(quiz['current_level'], quiz['recent_results'])
        
        # Build response
        response = {
            'correct': is_correct,
            'correct_answer': current_q['correct_answer'],
            'explanation': current_q.get('explanation', 'No explanation available'),
            'question_number': quiz['questions_answered'],
            'total_questions': quiz['num_questions'],
            'current_score': quiz['correct_count'],
            'current_level': quiz['current_level'],
            'level_changed': quiz['current_level'] != previous_level
        }
        quiz['previous_level'] = quiz['current_level']
        
        # Check if quiz complete
        if quiz['questions_answered'] >= quiz['num_questions']:
            response['quiz_complete'] = True
            response['final_score'] = quiz['correct_count']
            response['final_percentage'] = round((quiz['correct_count'] / quiz['num_questions']) * 100, 1)
            response['starting_level'] = quiz['starting_level']
            response['ending_level'] = quiz['current_level']
            response['level_progress'] = quiz['current_level'] - quiz['starting_level']
            
            # SAVE PROGRESS TO DATABASE
            try:
                user = get_user_identifier()
                if user:
                    save_adaptive_progress(
                        user_id=user['user_id'],
                        guest_code=user['guest_code'],
                        topic=quiz['topic'],
                        starting_level=quiz['starting_level'],
                        ending_level=quiz['current_level'],
                        score=quiz['correct_count'],
                        total_questions=quiz['num_questions']
                    )
            except Exception as save_error:
                print(f"Error saving adaptive progress: {save_error}")
                traceback.print_exc()
            
            # Clear session
            session.pop('adaptive_quiz', None)
            session.modified = True
            
            return jsonify(response)
        
        # Get next question
        next_question = select_question_for_level(
            quiz['topic'], 
            quiz['current_level'],
            exclude_ids=quiz['question_ids_shown']
        )
        
        if not next_question:
            # Reset exclusions if we've shown too many
            quiz['question_ids_shown'] = []
            next_question = select_question_for_level(quiz['topic'], quiz['current_level'])
        
        if not next_question:
            response['quiz_complete'] = True
            response['error'] = 'No more questions available'
            response['final_score'] = quiz['correct_count']
            response['final_percentage'] = round((quiz['correct_count'] / max(1, quiz['questions_answered'])) * 100, 1)
            response['starting_level'] = quiz['starting_level']
            response['ending_level'] = quiz['current_level']
            session.pop('adaptive_quiz', None)
            session.modified = True
            return jsonify(response)
        
        # Update session with next question
        quiz['current_question'] = next_question
        quiz['question_ids_shown'].append(next_question['id'])
        quiz['question_start_time'] = datetime.utcnow().isoformat()
        
        # Save to session
        session['adaptive_quiz'] = quiz
        session.modified = True  # IMPORTANT: Mark session as modified
        
        response['quiz_complete'] = False
        response['next_question'] = {
            'id': next_question['id'],
            'text': next_question['question_text'],
            'options': next_question['options'],
            'difficulty_level': next_question['difficulty_level'],
            'hint_available': bool(next_question.get('hint_text')),
            'estimated_time': next_question.get('estimated_time', 30),
            'image_svg': next_question.get('image_svg')
        }
        
        return jsonify(response)
        
    except Exception as e:
        print(f"Error submitting adaptive answer: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@adaptive_quiz_bp.route('/hint', methods=['GET'])
def get_hint():
    """Get hint for current question"""
    try:
        if 'adaptive_quiz' not in session:
            return jsonify({'error': 'No active quiz session'}), 400
        
        quiz = session['adaptive_quiz']
        current_q = quiz.get('current_question')
        
        if not current_q:
            return jsonify({'error': 'No current question'}), 400
        
        hint = current_q.get('hint_text')
        if not hint:
            return jsonify({'error': 'No hint available for this question'}), 404
        
        return jsonify({
            'hint': hint,
            'penalty': 50  # Points penalty for using hint
        })
    except Exception as e:
        print(f"Error getting hint: {e}")
        return jsonify({'error': str(e)}), 500


@adaptive_quiz_bp.route('/status', methods=['GET'])
def get_quiz_status():
    """Get current quiz session status"""
    try:
        if 'adaptive_quiz' not in session:
            return jsonify({'active': False})
        
        quiz = session['adaptive_quiz']
        
        return jsonify({
            'active': True,
            'topic': quiz['topic'],
            'mode': quiz['mode'],
            'current_level': quiz['current_level'],
            'questions_answered': quiz['questions_answered'],
            'total_questions': quiz['num_questions'],
            'correct_count': quiz['correct_count'],
            'current_percentage': round((quiz['correct_count'] / max(1, quiz['questions_answered'])) * 100, 1)
        })
    except Exception as e:
        print(f"Error getting status: {e}")
        return jsonify({'error': str(e)}), 500


@adaptive_quiz_bp.route('/abandon', methods=['POST'])
def abandon_quiz():
    """Abandon current quiz session"""
    try:
        session.pop('adaptive_quiz', None)
        session.modified = True
        return jsonify({'success': True, 'message': 'Quiz abandoned'})
    except Exception as e:
        print(f"Error abandoning quiz: {e}")
        return jsonify({'error': str(e)}), 500


# ============================================================================
# TOPIC INFO ROUTES
# ============================================================================

@adaptive_quiz_bp.route('/topics', methods=['GET'])
def get_available_topics():
    """Get topics that have adaptive questions"""
    try:
        result = _db.session.execute(text("""
            SELECT topic, COUNT(*) as count,
                   MIN(difficulty_level) as min_level,
                   MAX(difficulty_level) as max_level
            FROM questions_adaptive 
            WHERE is_active = 1
            GROUP BY topic
            HAVING COUNT(*) >= 10
            ORDER BY topic
        """)).fetchall()
        
        topics = [{
            'topic': r[0],
            'question_count': r[1],
            'min_level': r[2],
            'max_level': r[3]
        } for r in result]
        
        return jsonify({'topics': topics})
    except Exception as e:
        print(f"Error getting topics: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e), 'topics': []}), 500


@adaptive_quiz_bp.route('/topic-levels/<topic>', methods=['GET'])
def get_topic_levels(topic):
    """Get available levels and question counts for a topic"""
    try:
        result = _db.session.execute(text("""
            SELECT difficulty_level, COUNT(*) as count
            FROM questions_adaptive 
            WHERE topic = :topic AND is_active = 1
            GROUP BY difficulty_level
            ORDER BY difficulty_level
        """), {'topic': topic}).fetchall()
        
        levels = {r[0]: r[1] for r in result}
        
        # Fill in zeros for missing levels
        for i in range(1, 11):
            if i not in levels:
                levels[i] = 0
        
        return jsonify({
            'topic': topic,
            'levels': levels,
            'total': sum(levels.values())
        })
    except Exception as e:
        print(f"Error getting topic levels: {e}")
        return jsonify({'error': str(e)}), 500


@adaptive_quiz_bp.route('/recommended-level/<topic>', methods=['GET'])
def get_recommended_level(topic):
    """Get recommended starting level for current user"""
    try:
        user = get_user_identifier()
        
        if not user:
            return jsonify({'level': 1, 'reason': 'Guest user - starting at level 1'})
        
        level = get_user_current_level(
            topic,
            user_id=user['user_id'],
            guest_code=user['guest_code']
        )
        
        return jsonify({
            'level': level,
            'reason': f'Based on your previous performance'
        })
    except Exception as e:
        print(f"Error getting recommended level: {e}")
        return jsonify({'level': 1, 'reason': 'Starting at level 1'})
