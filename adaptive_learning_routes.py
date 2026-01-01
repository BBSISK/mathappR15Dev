"""
Adaptive Learning Routes
========================
Flask routes for the Adaptive Learning System.
Supports both registered users AND repeat guests (with guest_code).

Register these routes with your Flask app using register_adaptive_routes(app, db).

Usage in app.py:
    from adaptive_learning_routes import register_adaptive_routes
    register_adaptive_routes(app, db)
"""

from flask import Blueprint, request, jsonify, session
from datetime import datetime, timedelta
from functools import wraps
from sqlalchemy import text
import random

# Create blueprint
adaptive_bp = Blueprint('adaptive', __name__)

# Import adaptive learning functions (will be imported when routes are registered)
adaptive_module = None
db_instance = None

def register_adaptive_routes(app, db):
    """Register adaptive learning routes with the Flask app"""
    global adaptive_module, db_instance
    db_instance = db
    
    try:
        import adaptive_learning as al
        adaptive_module = al
        print("✓ Adaptive Learning System loaded")
    except ImportError as e:
        print(f"⚠ Adaptive Learning System not available: {e}")
        adaptive_module = None
    
    app.register_blueprint(adaptive_bp, url_prefix='/api/adaptive')
    print("✓ Adaptive Learning routes registered at /api/adaptive")


def adaptive_enabled(f):
    """Decorator to check if adaptive learning is enabled"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if adaptive_module is None:
            return jsonify({'error': 'Adaptive learning not available'}), 503
        if not adaptive_module.ADAPTIVE_CONFIG.get('ENABLED', False):
            return jsonify({'error': 'Adaptive learning is disabled'}), 503
        return f(*args, **kwargs)
    return decorated_function


def get_user_id():
    """Get user ID from session (registered users only)"""
    if 'guest_code' in session:
        return None  # Use get_guest_code() for repeat guests
    if 'is_guest' in session:
        return None  # Casual guests not supported
    return session.get('user_id')


def get_guest_code():
    """Get guest code from session (repeat guests only)"""
    return session.get('guest_code')


def is_repeat_guest():
    """Check if current user is a repeat guest"""
    return 'guest_code' in session


def is_casual_guest():
    """Check if current user is a casual (non-repeat) guest"""
    return 'is_guest' in session and 'guest_code' not in session


# ============================================================================
# GUEST SMART QUIZ FUNCTIONS
# ============================================================================

def get_guest_quiz_history(guest_code):
    """Get quiz history for a repeat guest"""
    try:
        result = db_instance.session.execute(text("""
            SELECT topic, difficulty, score, total_questions, completed_at
            FROM guest_quiz_attempts
            WHERE guest_code = :code
            ORDER BY completed_at DESC
            LIMIT 50
        """), {'code': guest_code})
        
        history = []
        for row in result.fetchall():
            history.append({
                'topic': row[0],
                'difficulty': row[1],
                'score': row[2],
                'total': row[3],
                'percentage': round((row[2] / row[3] * 100), 1) if row[3] > 0 else 0,
                'completed_at': row[4]
            })
        return history
    except Exception as e:
        print(f"Error getting guest history: {e}")
        return []


def get_guest_topic_stats(guest_code):
    """Get aggregated stats per topic for a repeat guest"""
    try:
        result = db_instance.session.execute(text("""
            SELECT topic, difficulty,
                   COUNT(*) as attempts,
                   SUM(score) as total_correct,
                   SUM(total_questions) as total_questions,
                   MAX(completed_at) as last_attempt
            FROM guest_quiz_attempts
            WHERE guest_code = :code
            GROUP BY topic, difficulty
            ORDER BY last_attempt DESC
        """), {'code': guest_code})
        
        stats = {}
        for row in result.fetchall():
            topic = row[0]
            diff = row[1]
            if topic not in stats:
                stats[topic] = {}
            stats[topic][diff] = {
                'attempts': row[2],
                'total_correct': row[3],
                'total_questions': row[4],
                'percentage': round((row[3] / row[4] * 100), 1) if row[4] > 0 else 0,
                'last_attempt': row[5]
            }
        return stats
    except Exception as e:
        print(f"Error getting guest stats: {e}")
        return {}


def get_available_topics():
    """Get list of available topics from database"""
    try:
        result = db_instance.session.execute(text("""
            SELECT topic_id FROM topics WHERE is_visible = 1
        """))
        topics = [row[0] for row in result.fetchall()]
        if topics:
            return topics
        # If no topics found, use fallback
        raise Exception("No topics in database")
    except Exception as e:
        print(f"Warning: Could not load topics from DB: {e}")
        # Fallback topics matching actual database topic_ids
        return [
            'fractions', 'decimals', 'percentages', 'arithmetic', 
            'introductory_algebra', 'solving_equations', 'probability',
            'descriptive_statistics', 'geometry', 'area_perimeter_volume',
            'patterns', 'sets', 'functions', 'bodmas', 'currency',
            'speed_distance_time', 'trigonometry', 'coordinate_geometry'
        ]


def get_smart_quiz_for_guest(guest_code, mode='auto'):
    """
    Generate smart quiz recommendation for a repeat guest.
    
    Uses their quiz history to recommend:
    - Topics they haven't tried (for discovery)
    - Topics they're struggling with (for practice)
    - Topics they're doing well in at higher difficulty (for challenge)
    """
    history = get_guest_quiz_history(guest_code)
    topic_stats = get_guest_topic_stats(guest_code)
    available_topics = get_available_topics()
    
    # If no history, recommend a beginner topic
    if not history:
        topic = random.choice(available_topics) if available_topics else 'fractions'
        return {
            'topic': topic,
            'difficulty': 'beginner',
            'reason': 'Start your learning journey!',
            'is_guest': True
        }
    
    # Analyze performance
    tried_topics = set(topic_stats.keys())
    untried_topics = [t for t in available_topics if t not in tried_topics]
    
    # Find struggling topics (low percentage)
    struggling = []
    for topic, diffs in topic_stats.items():
        for diff, data in diffs.items():
            if data['attempts'] >= 2 and data['percentage'] < 60:
                struggling.append({
                    'topic': topic,
                    'difficulty': diff,
                    'percentage': data['percentage'],
                    'attempts': data['attempts']
                })
    
    # Find mastered topics (high percentage, could try harder)
    mastered = []
    for topic, diffs in topic_stats.items():
        for diff, data in diffs.items():
            if data['attempts'] >= 2 and data['percentage'] >= 80:
                mastered.append({
                    'topic': topic,
                    'difficulty': diff,
                    'percentage': data['percentage']
                })
    
    # Mode-based selection
    if mode == 'review':
        # Pick a topic they haven't done recently
        if history:
            # Get topics sorted by last attempt (oldest first for review)
            recent_topics = {}
            for h in history:
                if h['topic'] not in recent_topics:
                    recent_topics[h['topic']] = h
            
            # Find oldest attempted topic
            oldest = None
            for topic, data in recent_topics.items():
                if oldest is None or (data['completed_at'] and data['completed_at'] < oldest['completed_at']):
                    oldest = data
            
            if oldest:
                return {
                    'topic': oldest['topic'],
                    'difficulty': oldest['difficulty'],
                    'reason': f"Time to refresh! Last practiced a while ago.",
                    'mastery_level': oldest['percentage'],
                    'is_guest': True
                }
    
    elif mode == 'practice':
        # Focus on weak areas
        if struggling:
            # Pick the weakest
            struggling.sort(key=lambda x: x['percentage'])
            pick = struggling[0]
            return {
                'topic': pick['topic'],
                'difficulty': pick['difficulty'],
                'reason': f"Practice makes perfect! Currently at {pick['percentage']}%",
                'mastery_level': pick['percentage'],
                'is_guest': True
            }
        # No struggling topics - suggest something new
        if untried_topics:
            topic = random.choice(untried_topics)
            return {
                'topic': topic,
                'difficulty': 'beginner',
                'reason': "No weak areas found! Try something new.",
                'is_guest': True
            }
    
    elif mode == 'challenge':
        # Push to harder content
        if mastered:
            # Find one where we can increase difficulty
            difficulty_order = ['beginner', 'intermediate', 'advanced']
            for m in mastered:
                current_idx = difficulty_order.index(m['difficulty']) if m['difficulty'] in difficulty_order else 0
                if current_idx < 2:  # Can go harder
                    next_diff = difficulty_order[current_idx + 1]
                    return {
                        'topic': m['topic'],
                        'difficulty': next_diff,
                        'reason': f"You crushed {m['difficulty']}! Ready for {next_diff}?",
                        'mastery_level': m['percentage'],
                        'is_guest': True
                    }
        # Nothing to level up - try new advanced topic
        if untried_topics:
            return {
                'topic': random.choice(untried_topics),
                'difficulty': 'intermediate',
                'reason': "Challenge yourself with something new!",
                'is_guest': True
            }
    
    # Auto mode - balanced selection
    # Priority: 1) Struggling topics, 2) New topics, 3) Level up mastered
    
    # 40% chance: practice struggling topic
    if struggling and random.random() < 0.4:
        pick = random.choice(struggling)
        return {
            'topic': pick['topic'],
            'difficulty': pick['difficulty'],
            'reason': f"Keep practicing! Currently at {pick['percentage']}%",
            'mastery_level': pick['percentage'],
            'is_guest': True
        }
    
    # 30% chance: try new topic
    if untried_topics and random.random() < 0.5:
        return {
            'topic': random.choice(untried_topics),
            'difficulty': 'beginner',
            'reason': "Discover a new topic!",
            'is_guest': True
        }
    
    # 30% chance: level up mastered topic
    if mastered:
        difficulty_order = ['beginner', 'intermediate', 'advanced']
        for m in mastered:
            current_idx = difficulty_order.index(m['difficulty']) if m['difficulty'] in difficulty_order else 0
            if current_idx < 2:
                next_diff = difficulty_order[current_idx + 1]
                return {
                    'topic': m['topic'],
                    'difficulty': next_diff,
                    'reason': f"Level up! You're ready for {next_diff}.",
                    'mastery_level': m['percentage'],
                    'is_guest': True
                }
    
    # Fallback: random from history
    if history:
        pick = random.choice(history[:10])  # Recent 10
        return {
            'topic': pick['topic'],
            'difficulty': pick['difficulty'],
            'reason': "Keep up the good work!",
            'mastery_level': pick['percentage'],
            'is_guest': True
        }
    
    # Ultimate fallback
    return {
        'topic': random.choice(available_topics) if available_topics else 'fractions',
        'difficulty': 'beginner',
        'reason': 'Start learning!',
        'is_guest': True
    }


# ============================================================================
# STUDENT ENDPOINTS
# ============================================================================

@adaptive_bp.route('/dashboard', methods=['GET'])
@adaptive_enabled
def adaptive_dashboard():
    """Get student's adaptive learning dashboard data"""
    user_id = get_user_id()
    guest_code = get_guest_code()
    
    # Handle repeat guests
    if guest_code:
        topic_stats = get_guest_topic_stats(guest_code)
        history = get_guest_quiz_history(guest_code)
        
        # Calculate overall stats
        total_quizzes = len(history)
        total_correct = sum(h['score'] for h in history)
        total_questions = sum(h['total'] for h in history)
        overall_percentage = round((total_correct / total_questions * 100), 1) if total_questions > 0 else 0
        
        return jsonify({
            'is_guest': True,
            'overall': {
                'total_quizzes': total_quizzes,
                'total_correct': total_correct,
                'total_questions': total_questions,
                'average_score': overall_percentage
            },
            'topics': topic_stats,
            'recent_history': history[:10],
            'message': 'Register for full adaptive learning features!'
        }), 200
    
    if not user_id:
        return jsonify({'error': 'Login required for adaptive learning'}), 401
    
    try:
        data = adaptive_module.get_student_adaptive_dashboard(user_id, db_instance.session)
        return jsonify(data), 200
    except Exception as e:
        print(f"Adaptive dashboard error: {e}")
        return jsonify({'error': str(e)}), 500


@adaptive_bp.route('/recommendations', methods=['GET'])
@adaptive_enabled
def get_recommendations():
    """Get personalised learning recommendations"""
    user_id = get_user_id()
    guest_code = get_guest_code()
    
    # Handle repeat guests with simpler recommendations
    if guest_code:
        recommendations = []
        topic_stats = get_guest_topic_stats(guest_code)
        available_topics = get_available_topics()
        tried_topics = set(topic_stats.keys())
        untried = [t for t in available_topics if t not in tried_topics]
        
        # Recommend untried topics
        for topic in untried[:3]:
            recommendations.append({
                'type': 'new_topic',
                'topic': topic,
                'difficulty': 'beginner',
                'reason': 'Try something new!'
            })
        
        # Recommend practice for low-scoring topics
        for topic, diffs in topic_stats.items():
            for diff, data in diffs.items():
                if data['percentage'] < 60 and data['attempts'] >= 2:
                    recommendations.append({
                        'type': 'practice',
                        'topic': topic,
                        'difficulty': diff,
                        'reason': f'Practice needed - currently {data["percentage"]}%'
                    })
        
        return jsonify({
            'recommendations': recommendations[:5],
            'is_guest': True
        }), 200
    
    if not user_id:
        return jsonify({'error': 'Login required'}), 401
    
    try:
        recommendations = adaptive_module.generate_recommendations(
            user_id, db_instance.session
        )
        return jsonify({'recommendations': recommendations}), 200
    except Exception as e:
        print(f"Recommendations error: {e}")
        return jsonify({'error': str(e)}), 500


@adaptive_bp.route('/smart-quiz', methods=['GET', 'POST'])
@adaptive_enabled
def smart_quiz_selection():
    """
    Get intelligent topic/difficulty selection for a quiz.
    Works for both registered users AND repeat guests.
    
    GET: Returns recommendation with default 'auto' mode
    POST: Accepts mode parameter for specific selection
        - 'auto': Balanced selection
        - 'review': Prioritise spaced repetition reviews
        - 'practice': Focus on weak areas
        - 'challenge': Push to harder topics/difficulties
    """
    user_id = get_user_id()
    guest_code = get_guest_code()
    
    # Casual guests not supported
    if is_casual_guest():
        return jsonify({'error': 'Smart Quiz requires a guest code or account'}), 401
    
    mode = 'auto'
    if request.method == 'POST':
        data = request.get_json() or {}
        mode = data.get('mode', 'auto')
    
    # Handle repeat guests
    if guest_code:
        try:
            selection = get_smart_quiz_for_guest(guest_code, mode=mode)
            return jsonify(selection), 200
        except Exception as e:
            print(f"Guest smart quiz error: {e}")
            return jsonify({'error': str(e)}), 500
    
    # Handle registered users
    if not user_id:
        return jsonify({'error': 'Login required'}), 401
    
    try:
        selection = adaptive_module.get_smart_quiz_selection(
            user_id, db_instance.session, mode=mode
        )
        return jsonify(selection), 200
    except Exception as e:
        print(f"Smart quiz error: {e}")
        return jsonify({'error': str(e)}), 500


@adaptive_bp.route('/topic-status/<topic>', methods=['GET'])
@adaptive_enabled
def topic_status(topic):
    """Get detailed mastery status for a specific topic"""
    user_id = get_user_id()
    guest_code = get_guest_code()
    
    # Handle repeat guests
    if guest_code:
        topic_stats = get_guest_topic_stats(guest_code)
        if topic in topic_stats:
            return jsonify({
                'topic': topic,
                'mastery': topic_stats[topic],
                'is_guest': True
            }), 200
        return jsonify({
            'topic': topic,
            'mastery': {},
            'message': 'No data for this topic yet',
            'is_guest': True
        }), 200
    
    if not user_id:
        return jsonify({'error': 'Login required'}), 401
    
    try:
        # Get mastery data for all difficulties
        result = db_instance.session.execute(text("""
            SELECT difficulty, mastery_level, total_attempts, streak_current,
                   is_mastered, next_review_at, last_attempt_at
            FROM topic_mastery 
            WHERE user_id = :user_id AND topic = :topic
        """), {'user_id': user_id, 'topic': topic})
        
        mastery_data = {}
        for row in result.fetchall():
            mastery_data[row[0]] = {
                'mastery_level': round(row[1] * 100, 1) if row[1] else 0,
                'attempts': row[2] or 0,
                'streak': row[3] or 0,
                'is_mastered': bool(row[4]),
                'next_review': row[5].isoformat() if row[5] else None,
                'last_attempt': row[6].isoformat() if row[6] else None
            }
        
        # Get recommended difficulty
        recommended = adaptive_module.get_recommended_difficulty(
            user_id, topic, db_instance.session
        )
        
        # Check prerequisites
        prereqs_met, unmet = adaptive_module.check_prerequisites_met(
            user_id, topic, db_instance.session
        )
        
        return jsonify({
            'topic': topic,
            'mastery': mastery_data,
            'recommended_difficulty': recommended,
            'prerequisites_met': prereqs_met,
            'unmet_prerequisites': unmet
        }), 200
        
    except Exception as e:
        print(f"Topic status error: {e}")
        return jsonify({'error': str(e)}), 500


@adaptive_bp.route('/review-queue', methods=['GET'])
@adaptive_enabled
def review_queue():
    """Get topics due for spaced repetition review"""
    user_id = get_user_id()
    guest_code = get_guest_code()
    
    # Guests don't have spaced repetition (simplified system)
    if guest_code:
        # Return topics they haven't practiced recently
        history = get_guest_quiz_history(guest_code)
        if not history:
            return jsonify({'review_queue': [], 'count': 0, 'is_guest': True}), 200
        
        # Find topics not practiced in last 7 days
        now = datetime.utcnow()
        week_ago = now - timedelta(days=7)
        
        topic_last_seen = {}
        for h in history:
            topic = h['topic']
            if topic not in topic_last_seen:
                topic_last_seen[topic] = h
        
        queue = []
        for topic, data in topic_last_seen.items():
            if data['completed_at'] and data['completed_at'] < week_ago:
                queue.append({
                    'topic': topic,
                    'difficulty': data['difficulty'],
                    'mastery': data['percentage'],
                    'days_since': (now - data['completed_at']).days if data['completed_at'] else 0
                })
        
        return jsonify({
            'review_queue': queue[:10],
            'count': len(queue),
            'is_guest': True
        }), 200
    
    if not user_id:
        return jsonify({'error': 'Login required'}), 401
    
    now = datetime.utcnow()
    
    try:
        result = db_instance.session.execute(text("""
            SELECT topic, difficulty, mastery_level, next_review_at,
                   review_interval_days
            FROM topic_mastery 
            WHERE user_id = :user_id 
            AND next_review_at <= :now
            AND mastery_level >= 0.5
            ORDER BY next_review_at ASC
            LIMIT 10
        """), {'user_id': user_id, 'now': now})
        
        queue = []
        for row in result.fetchall():
            days_overdue = (now - row[3]).days if row[3] else 0
            queue.append({
                'topic': row[0],
                'difficulty': row[1],
                'mastery': round(row[2] * 100, 1),
                'due_at': row[3].isoformat() if row[3] else None,
                'days_overdue': days_overdue,
                'review_interval': row[4]
            })
        
        return jsonify({
            'review_queue': queue,
            'count': len(queue)
        }), 200
        
    except Exception as e:
        print(f"Review queue error: {e}")
        return jsonify({'error': str(e)}), 500


@adaptive_bp.route('/struggling', methods=['GET'])
@adaptive_enabled
def struggling_topics():
    """Get topics where user is struggling"""
    user_id = get_user_id()
    guest_code = get_guest_code()
    
    # Handle repeat guests
    if guest_code:
        topic_stats = get_guest_topic_stats(guest_code)
        struggling = []
        
        for topic, diffs in topic_stats.items():
            for diff, data in diffs.items():
                if data['attempts'] >= 2 and data['percentage'] < 60:
                    struggling.append({
                        'topic': topic,
                        'difficulty': diff,
                        'mastery': data['percentage'],
                        'attempts': data['attempts']
                    })
        
        struggling.sort(key=lambda x: x['mastery'])
        return jsonify({
            'struggling': struggling[:5],
            'is_guest': True
        }), 200
    
    if not user_id:
        return jsonify({'error': 'Login required'}), 401
    
    try:
        result = db_instance.session.execute(text("""
            SELECT topic, difficulty, mastery_level, total_attempts
            FROM topic_mastery 
            WHERE user_id = :user_id 
            AND mastery_level > 0 
            AND mastery_level < 0.5
            AND total_attempts >= 5
            ORDER BY mastery_level ASC
            LIMIT 5
        """), {'user_id': user_id})
        
        struggling = [{
            'topic': row[0],
            'difficulty': row[1],
            'mastery': round(row[2] * 100, 1),
            'attempts': row[3]
        } for row in result.fetchall()]
        
        return jsonify({'struggling': struggling}), 200
        
    except Exception as e:
        print(f"Struggling topics error: {e}")
        return jsonify({'error': str(e)}), 500


# ============================================================================
# TEACHER ENDPOINTS
# ============================================================================

@adaptive_bp.route('/class-overview/<int:class_id>', methods=['GET'])
@adaptive_enabled
def class_mastery_overview(class_id):
    """Get class-wide mastery overview for teachers"""
    user_id = get_user_id()
    if not user_id:
        return jsonify({'error': 'Login required'}), 401
    
    try:
        # Verify teacher owns this class
        result = db_instance.session.execute(text("""
            SELECT id FROM classes WHERE id = :class_id AND teacher_id = :user_id
        """), {'class_id': class_id, 'user_id': user_id})
        
        if not result.fetchone():
            return jsonify({'error': 'Class not found or access denied'}), 403
        
        data = adaptive_module.get_class_mastery_overview(class_id, db_instance.session)
        return jsonify(data), 200
        
    except Exception as e:
        print(f"Class overview error: {e}")
        return jsonify({'error': str(e)}), 500


@adaptive_bp.route('/student-detail/<int:student_id>', methods=['GET'])
@adaptive_enabled
def student_detail(student_id):
    """Get detailed adaptive data for a specific student (teacher view)"""
    user_id = get_user_id()
    if not user_id:
        return jsonify({'error': 'Login required'}), 401
    
    try:
        # Verify teacher has access to this student (student is in one of their classes)
        result = db_instance.session.execute(text("""
            SELECT ce.student_id 
            FROM class_enrollments ce
            JOIN classes c ON ce.class_id = c.id
            WHERE c.teacher_id = :teacher_id AND ce.student_id = :student_id
            LIMIT 1
        """), {'teacher_id': user_id, 'student_id': student_id})
        
        if not result.fetchone():
            return jsonify({'error': 'Student not found or access denied'}), 403
        
        data = adaptive_module.get_student_adaptive_dashboard(student_id, db_instance.session)
        return jsonify(data), 200
        
    except Exception as e:
        print(f"Student detail error: {e}")
        return jsonify({'error': str(e)}), 500


# ============================================================================
# INTERNAL HELPER - Called from submit_quiz
# ============================================================================

def update_adaptive_after_quiz(user_id, topic, difficulty, score, total_questions, 
                               time_taken, question_results=None):
    """
    Update adaptive learning data after quiz completion.
    Call this from the submit_quiz route.
    
    Note: This only works for registered users, not guests.
    Guest quiz data is already stored in guest_quiz_attempts table.
    
    Returns dict with update results, or None if adaptive is disabled.
    """
    if adaptive_module is None:
        return None
    
    if not adaptive_module.ADAPTIVE_CONFIG.get('ENABLED', False):
        return None
    
    try:
        result = adaptive_module.update_after_quiz(
            user_id=user_id,
            topic=topic,
            difficulty=difficulty,
            score=score,
            total_questions=total_questions,
            time_taken=time_taken,
            db_session=db_instance.session,
            question_results=question_results
        )
        return result
    except Exception as e:
        print(f"Adaptive update error: {e}")
        return {'error': str(e)}
