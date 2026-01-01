"""
Team Play Routes - AgentMath Collaborative Quiz Feature
Version 1.0 - December 2025

This module provides the backend API for Team Play functionality.
Register with main app using: register_team_play_routes(app, db)
"""

from flask import Blueprint, request, jsonify, session
from datetime import datetime, timedelta
from functools import wraps
import random
import string
import re

team_play_bp = Blueprint('team_play', __name__)

# Will be set when routes are registered
db = None

# ==================== CONFIGURATION ====================

TEAM_PLAY_CONFIG = {
    'min_players': 2,
    'max_players': 4,
    'code_length': 7,  # e.g., FOX-247
    'invite_expiry_minutes': 5,
    'session_timeout_minutes': 5,
    'lock_in_seconds': 15,
    'chat_max_chars': 150,
    'bonus_multipliers': {
        2: 0.10,  # 10% for 2 players
        3: 0.25,  # 25% for 3 players
        4: 0.50   # 50% for 4 players
    }
}

# Expletive filter
BLOCKED_WORDS = [
    'fuck', 'shit', 'bitch', 'ass', 'damn', 'crap', 'bastard', 'piss',
    'dick', 'cock', 'pussy', 'cunt', 'fck', 'fuk', 'sh1t', 'b1tch', 
    'a$$', 'f*ck', 'sh*t', 'bullshit', 'asshole', 'arsehole', 'wanker',
    'bollocks', 'tosser', 'twat', 'prick', 'slut', 'whore'
]

# In-memory chat storage (ephemeral - no database storage)
# Format: {session_code: [{'player': 'name', 'message': 'text', 'timestamp': datetime}, ...]}
session_chats = {}

# In-memory current question tracking
# Format: {session_code: {'question_number': 1, 'question_id': 123, 'question_data': {...}, 'started_at': datetime, 'first_lock_at': None}}
session_questions = {}


# ==================== HELPERS ====================

def generate_session_code():
    """Generate a unique session code like FOX-247"""
    animals = ['FOX', 'OWL', 'CAT', 'DOG', 'BAT', 'BEE', 'ANT', 'ELF', 'APE', 'COW']
    animal = random.choice(animals)
    numbers = ''.join(random.choices(string.digits, k=3))
    return f"{animal}-{numbers}"


def filter_chat_message(message):
    """Replace blocked words with asterisks"""
    if not message:
        return message
    filtered = message
    for word in BLOCKED_WORDS:
        pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
        filtered = pattern.sub('*' * len(word), filtered)
    return filtered[:TEAM_PLAY_CONFIG['chat_max_chars']]


def get_user_identifier():
    """Get current user's identifier (user_id or guest_code)"""
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    return user_id, guest_code


def get_display_name():
    """Get display name for current user"""
    if session.get('is_guest'):
        return session.get('guest_name', 'Guest')
    return session.get('name', session.get('username', 'Player'))


def is_repeat_guest_or_account():
    """Check if user is an account holder or repeat guest"""
    # Account holders always allowed
    if session.get('user_id') and not session.get('is_guest'):
        return True
    
    # Check if guest has used the app before (has some history)
    guest_code = session.get('guest_code')
    if guest_code:
        from sqlalchemy import text
        # Check for any previous activity
        result = db.session.execute(text("""
            SELECT COUNT(*) as count FROM user_points 
            WHERE guest_code = :guest_code
        """), {'guest_code': guest_code}).fetchone()
        if result and result.count > 0:
            return True
        
        # Also check adaptive progress
        result = db.session.execute(text("""
            SELECT COUNT(*) as count FROM user_adaptive_progress 
            WHERE guest_code = :guest_code
        """), {'guest_code': guest_code}).fetchone()
        if result and result.count > 0:
            return True
    
    return False


def require_team_play_eligible(f):
    """Decorator to ensure user can participate in Team Play"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('user_id') and not session.get('guest_code'):
            return jsonify({'error': 'Must be logged in or have a guest code'}), 401
        
        if not is_repeat_guest_or_account():
            return jsonify({'error': 'Team Play requires an account or repeat guest status'}), 403
        
        return f(*args, **kwargs)
    return decorated_function


def update_session_activity(session_code):
    """Update last activity timestamp for a session"""
    from sqlalchemy import text
    db.session.execute(text("""
        UPDATE team_sessions 
        SET last_activity = :now 
        WHERE session_code = :code
    """), {'now': datetime.utcnow(), 'code': session_code})
    db.session.commit()


def check_session_timeout(session_code):
    """Check if session has timed out due to inactivity"""
    from sqlalchemy import text
    result = db.session.execute(text("""
        SELECT last_activity, status FROM team_sessions 
        WHERE session_code = :code
    """), {'code': session_code}).fetchone()
    
    if not result:
        return True
    
    if result.status in ['completed', 'cancelled']:
        return True
    
    if result.last_activity:
        timeout = datetime.utcnow() - timedelta(minutes=TEAM_PLAY_CONFIG['session_timeout_minutes'])
        if result.last_activity < timeout:
            # Mark session as cancelled
            db.session.execute(text("""
                UPDATE team_sessions 
                SET status = 'cancelled', ended_at = :now 
                WHERE session_code = :code
            """), {'now': datetime.utcnow(), 'code': session_code})
            db.session.commit()
            return True
    
    return False


# ==================== SESSION MANAGEMENT ====================

@team_play_bp.route('/api/team/create-session', methods=['POST'])
@require_team_play_eligible
def create_team_session():
    """Create a new Team Play session"""
    from sqlalchemy import text
    
    data = request.get_json() or {}
    topic = data.get('topic')
    question_count = data.get('question_count', 10)
    time_limit = data.get('time_limit_minutes')  # None for unlimited
    difficulty_levels = data.get('difficulty_levels', '1-12')
    
    if not topic:
        return jsonify({'error': 'Topic is required'}), 400
    
    user_id, guest_code = get_user_identifier()
    
    # Generate unique code
    for _ in range(10):  # Try up to 10 times
        code = generate_session_code()
        existing = db.session.execute(text(
            "SELECT id FROM team_sessions WHERE session_code = :code"
        ), {'code': code}).fetchone()
        if not existing:
            break
    else:
        return jsonify({'error': 'Could not generate unique code'}), 500
    
    # Create session
    now = datetime.utcnow()
    db.session.execute(text("""
        INSERT INTO team_sessions 
        (session_code, organiser_user_id, organiser_guest_code, topic, 
         difficulty_levels, question_count, time_limit_minutes, status, 
         created_at, last_activity)
        VALUES (:code, :user_id, :guest_code, :topic, :levels, :count, 
                :time_limit, 'waiting', :now, :now)
    """), {
        'code': code,
        'user_id': user_id,
        'guest_code': guest_code if not user_id else None,
        'topic': topic,
        'levels': difficulty_levels,
        'count': question_count,
        'time_limit': time_limit,
        'now': now
    })
    db.session.commit()
    
    # Get session ID
    result = db.session.execute(text(
        "SELECT id FROM team_sessions WHERE session_code = :code"
    ), {'code': code}).fetchone()
    session_id = result.id
    
    # Add organiser as first player
    display_name = get_display_name()
    db.session.execute(text("""
        INSERT INTO team_session_players 
        (session_id, user_id, guest_code, display_name, is_organiser, joined_at, status)
        VALUES (:session_id, :user_id, :guest_code, :name, 1, :now, 'active')
    """), {
        'session_id': session_id,
        'user_id': user_id,
        'guest_code': guest_code if not user_id else None,
        'name': display_name,
        'now': now
    })
    db.session.commit()
    
    # Initialize chat for session
    session_chats[code] = []
    
    return jsonify({
        'success': True,
        'session_code': code,
        'session_id': session_id,
        'topic': topic,
        'question_count': question_count
    })


@team_play_bp.route('/api/team/session/<code>', methods=['GET'])
@require_team_play_eligible
def get_team_session(code):
    """Get session details"""
    from sqlalchemy import text
    
    code = code.upper()
    
    if check_session_timeout(code):
        return jsonify({'error': 'Session has timed out'}), 410
    
    # Get session
    session_data = db.session.execute(text("""
        SELECT id, session_code, topic, difficulty_levels, question_count,
               time_limit_minutes, status, created_at, started_at,
               organiser_user_id, organiser_guest_code
        FROM team_sessions WHERE session_code = :code
    """), {'code': code}).fetchone()
    
    if not session_data:
        return jsonify({'error': 'Session not found'}), 404
    
    # Get players
    players = db.session.execute(text("""
        SELECT id, user_id, guest_code, display_name, is_organiser, status
        FROM team_session_players 
        WHERE session_id = :session_id AND status = 'active'
        ORDER BY is_organiser DESC, joined_at ASC
    """), {'session_id': session_data.id}).fetchall()
    
    player_list = [{
        'id': p.id,
        'name': p.display_name,
        'is_organiser': bool(p.is_organiser),
        'is_me': (p.user_id == session.get('user_id') if p.user_id else p.guest_code == session.get('guest_code'))
    } for p in players]
    
    return jsonify({
        'session_code': session_data.session_code,
        'topic': session_data.topic,
        'difficulty_levels': session_data.difficulty_levels,
        'question_count': session_data.question_count,
        'time_limit_minutes': session_data.time_limit_minutes,
        'status': session_data.status,
        'players': player_list,
        'player_count': len(player_list),
        'max_players': TEAM_PLAY_CONFIG['max_players'],
        'min_players': TEAM_PLAY_CONFIG['min_players']
    })


@team_play_bp.route('/api/team/session/<code>/join', methods=['POST'])
@require_team_play_eligible
def join_team_session(code):
    """Join an existing Team Play session"""
    from sqlalchemy import text
    
    code = code.upper()
    
    if check_session_timeout(code):
        return jsonify({'error': 'Session has timed out'}), 410
    
    # Get session
    session_data = db.session.execute(text("""
        SELECT id, status FROM team_sessions WHERE session_code = :code
    """), {'code': code}).fetchone()
    
    if not session_data:
        return jsonify({'error': 'Session not found'}), 404
    
    if session_data.status != 'waiting':
        return jsonify({'error': 'Session has already started or ended'}), 400
    
    user_id, guest_code = get_user_identifier()
    
    # Check if already in session
    existing = db.session.execute(text("""
        SELECT id FROM team_session_players 
        WHERE session_id = :session_id 
        AND ((user_id = :user_id AND :user_id IS NOT NULL) 
             OR (guest_code = :guest_code AND :guest_code IS NOT NULL))
        AND status = 'active'
    """), {
        'session_id': session_data.id,
        'user_id': user_id,
        'guest_code': guest_code
    }).fetchone()
    
    if existing:
        return jsonify({'success': True, 'message': 'Already in session'})
    
    # Check player count
    count = db.session.execute(text("""
        SELECT COUNT(*) as count FROM team_session_players 
        WHERE session_id = :session_id AND status = 'active'
    """), {'session_id': session_data.id}).fetchone()
    
    if count.count >= TEAM_PLAY_CONFIG['max_players']:
        return jsonify({'error': 'Session is full'}), 400
    
    # Add player
    display_name = get_display_name()
    db.session.execute(text("""
        INSERT INTO team_session_players 
        (session_id, user_id, guest_code, display_name, is_organiser, joined_at, status)
        VALUES (:session_id, :user_id, :guest_code, :name, 0, :now, 'active')
    """), {
        'session_id': session_data.id,
        'user_id': user_id,
        'guest_code': guest_code if not user_id else None,
        'name': display_name,
        'now': datetime.utcnow()
    })
    db.session.commit()
    
    update_session_activity(code)
    
    return jsonify({'success': True, 'message': 'Joined session'})


@team_play_bp.route('/api/team/session/<code>/leave', methods=['POST'])
@require_team_play_eligible
def leave_team_session(code):
    """Leave a Team Play session"""
    from sqlalchemy import text
    
    code = code.upper()
    user_id, guest_code = get_user_identifier()
    
    # Get session
    session_data = db.session.execute(text("""
        SELECT id, organiser_user_id, organiser_guest_code, status
        FROM team_sessions WHERE session_code = :code
    """), {'code': code}).fetchone()
    
    if not session_data:
        return jsonify({'error': 'Session not found'}), 404
    
    # Check if user is organiser
    is_organiser = (
        (session_data.organiser_user_id and session_data.organiser_user_id == user_id) or
        (session_data.organiser_guest_code and session_data.organiser_guest_code == guest_code)
    )
    
    if is_organiser:
        # Organiser leaving cancels the session
        db.session.execute(text("""
            UPDATE team_sessions 
            SET status = 'cancelled', ended_at = :now 
            WHERE session_code = :code
        """), {'now': datetime.utcnow(), 'code': code})
    else:
        # Mark player as left
        db.session.execute(text("""
            UPDATE team_session_players 
            SET status = 'left'
            WHERE session_id = :session_id 
            AND ((user_id = :user_id AND :user_id IS NOT NULL) 
                 OR (guest_code = :guest_code AND :guest_code IS NOT NULL))
        """), {
            'session_id': session_data.id,
            'user_id': user_id,
            'guest_code': guest_code
        })
    
    db.session.commit()
    
    return jsonify({'success': True, 'cancelled': is_organiser})


@team_play_bp.route('/api/team/session/<code>/start', methods=['POST'])
@require_team_play_eligible
def start_team_session(code):
    """Start the Team Play quiz (organiser only)"""
    from sqlalchemy import text
    
    code = code.upper()
    user_id, guest_code = get_user_identifier()
    
    # Get session and verify organiser
    session_data = db.session.execute(text("""
        SELECT id, organiser_user_id, organiser_guest_code, status, topic, difficulty_levels
        FROM team_sessions WHERE session_code = :code
    """), {'code': code}).fetchone()
    
    if not session_data:
        return jsonify({'error': 'Session not found'}), 404
    
    is_organiser = (
        (session_data.organiser_user_id and session_data.organiser_user_id == user_id) or
        (session_data.organiser_guest_code and session_data.organiser_guest_code == guest_code)
    )
    
    if not is_organiser:
        return jsonify({'error': 'Only the organiser can start the session'}), 403
    
    if session_data.status != 'waiting':
        return jsonify({'error': 'Session has already started or ended'}), 400
    
    # Check minimum players
    count = db.session.execute(text("""
        SELECT COUNT(*) as count FROM team_session_players 
        WHERE session_id = :session_id AND status = 'active'
    """), {'session_id': session_data.id}).fetchone()
    
    if count.count < TEAM_PLAY_CONFIG['min_players']:
        return jsonify({'error': f'Need at least {TEAM_PLAY_CONFIG["min_players"]} players'}), 400
    
    # Start session
    now = datetime.utcnow()
    db.session.execute(text("""
        UPDATE team_sessions 
        SET status = 'active', started_at = :now, last_activity = :now 
        WHERE session_code = :code
    """), {'now': now, 'code': code})
    db.session.commit()
    
    # Initialize first question
    session_questions[code] = {
        'question_number': 0,
        'question_id': None,
        'question_data': None,
        'started_at': None,
        'first_lock_at': None
    }
    
    return jsonify({'success': True, 'message': 'Session started'})


@team_play_bp.route('/api/team/session/<code>/end', methods=['POST'])
@require_team_play_eligible
def end_team_session(code):
    """End the Team Play session (organiser only)"""
    from sqlalchemy import text
    
    code = code.upper()
    user_id, guest_code = get_user_identifier()
    
    # Get session and verify organiser
    session_data = db.session.execute(text("""
        SELECT id, organiser_user_id, organiser_guest_code
        FROM team_sessions WHERE session_code = :code
    """), {'code': code}).fetchone()
    
    if not session_data:
        return jsonify({'error': 'Session not found'}), 404
    
    is_organiser = (
        (session_data.organiser_user_id and session_data.organiser_user_id == user_id) or
        (session_data.organiser_guest_code and session_data.organiser_guest_code == guest_code)
    )
    
    if not is_organiser:
        return jsonify({'error': 'Only the organiser can end the session'}), 403
    
    # End session
    db.session.execute(text("""
        UPDATE team_sessions 
        SET status = 'completed', ended_at = :now 
        WHERE session_code = :code
    """), {'now': datetime.utcnow(), 'code': code})
    db.session.commit()
    
    # Clean up in-memory data
    if code in session_chats:
        del session_chats[code]
    if code in session_questions:
        del session_questions[code]
    
    return jsonify({'success': True})


# ==================== GAMEPLAY ====================

@team_play_bp.route('/api/team/session/<code>/next-question', methods=['POST'])
@require_team_play_eligible
def next_team_question(code):
    """Load the next question for the team"""
    from sqlalchemy import text
    
    code = code.upper()
    
    if check_session_timeout(code):
        return jsonify({'error': 'Session has timed out'}), 410
    
    # Get session
    session_data = db.session.execute(text("""
        SELECT id, topic, difficulty_levels, question_count, status
        FROM team_sessions WHERE session_code = :code
    """), {'code': code}).fetchone()
    
    if not session_data:
        return jsonify({'error': 'Session not found'}), 404
    
    if session_data.status != 'active':
        return jsonify({'error': 'Session is not active'}), 400
    
    # Get current question number
    current = session_questions.get(code, {'question_number': 0})
    next_num = current['question_number'] + 1
    
    if next_num > session_data.question_count:
        return jsonify({'complete': True, 'message': 'All questions completed'})
    
    # Parse difficulty levels (e.g., "3-6" -> [3,4,5,6])
    levels = session_data.difficulty_levels or '1-12'
    if '-' in levels:
        start, end = map(int, levels.split('-'))
        level_list = list(range(start, end + 1))
    else:
        level_list = [int(levels)]
    
    # Pick a random level for this question
    level = random.choice(level_list)
    
    # Get a question from the database
    question = db.session.execute(text("""
        SELECT id, question_text, option_a, option_b, option_c, option_d,
               correct_answer, explanation, image_svg
        FROM questions_adaptive
        WHERE topic = :topic 
        AND difficulty_level = :level
        AND is_active = 1
        ORDER BY RANDOM()
        LIMIT 1
    """), {'topic': session_data.topic, 'level': level}).fetchone()
    
    if not question:
        # Try any level in range
        question = db.session.execute(text("""
            SELECT id, question_text, option_a, option_b, option_c, option_d,
                   correct_answer, explanation, image_svg
            FROM questions_adaptive
            WHERE topic = :topic AND is_active = 1
            ORDER BY RANDOM()
            LIMIT 1
        """), {'topic': session_data.topic}).fetchone()
    
    if not question:
        return jsonify({'error': 'No questions available'}), 404
    
    # Store question state
    now = datetime.utcnow()
    session_questions[code] = {
        'question_number': next_num,
        'question_id': question.id,
        'question_data': {
            'question_text': question.question_text,
            'option_a': question.option_a,
            'option_b': question.option_b,
            'option_c': question.option_c,
            'option_d': question.option_d,
            'image_svg': question.image_svg
        },
        'correct_answer': question.correct_answer,
        'explanation': question.explanation,
        'started_at': now,
        'first_lock_at': None
    }
    
    update_session_activity(code)
    
    return jsonify({
        'success': True,
        'question_number': next_num,
        'total_questions': session_data.question_count,
        'question': session_questions[code]['question_data']
    })


@team_play_bp.route('/api/team/session/<code>/answer', methods=['POST'])
@require_team_play_eligible
def submit_team_answer(code):
    """Submit answer for current question"""
    from sqlalchemy import text
    
    code = code.upper()
    data = request.get_json() or {}
    answer = data.get('answer', '').upper()
    
    if answer not in ['A', 'B', 'C', 'D']:
        return jsonify({'error': 'Invalid answer'}), 400
    
    if check_session_timeout(code):
        return jsonify({'error': 'Session has timed out'}), 410
    
    user_id, guest_code = get_user_identifier()
    
    # Get session and player
    session_data = db.session.execute(text("""
        SELECT id, status FROM team_sessions WHERE session_code = :code
    """), {'code': code}).fetchone()
    
    if not session_data or session_data.status != 'active':
        return jsonify({'error': 'Session not active'}), 400
    
    player = db.session.execute(text("""
        SELECT id FROM team_session_players 
        WHERE session_id = :session_id 
        AND ((user_id = :user_id AND :user_id IS NOT NULL) 
             OR (guest_code = :guest_code AND :guest_code IS NOT NULL))
        AND status = 'active'
    """), {
        'session_id': session_data.id,
        'user_id': user_id,
        'guest_code': guest_code
    }).fetchone()
    
    if not player:
        return jsonify({'error': 'Player not in session'}), 403
    
    # Get current question
    q_state = session_questions.get(code)
    if not q_state or not q_state['question_id']:
        return jsonify({'error': 'No active question'}), 400
    
    # Check if already answered
    existing = db.session.execute(text("""
        SELECT id FROM team_session_answers 
        WHERE session_id = :session_id 
        AND question_number = :q_num 
        AND player_id = :player_id
    """), {
        'session_id': session_data.id,
        'q_num': q_state['question_number'],
        'player_id': player.id
    }).fetchone()
    
    if existing:
        return jsonify({'error': 'Already answered this question'}), 400
    
    now = datetime.utcnow()
    
    # If this is first lock-in, start the timer
    if not q_state['first_lock_at']:
        q_state['first_lock_at'] = now
        session_questions[code] = q_state
    
    # Check if within time limit
    if q_state['first_lock_at']:
        elapsed = (now - q_state['first_lock_at']).total_seconds()
        if elapsed > TEAM_PLAY_CONFIG['lock_in_seconds']:
            return jsonify({'error': 'Time expired'}), 400
    
    # Determine if correct
    correct_answer = q_state.get('correct_answer')
    # Normalize correct answer
    if isinstance(correct_answer, int) or (isinstance(correct_answer, str) and correct_answer.isdigit()):
        correct_answer = ['A', 'B', 'C', 'D'][int(correct_answer)]
    else:
        correct_answer = str(correct_answer).upper()
    
    is_correct = (answer == correct_answer)
    
    # Record answer
    db.session.execute(text("""
        INSERT INTO team_session_answers 
        (session_id, question_number, question_id, player_id, answer, is_correct, locked_at)
        VALUES (:session_id, :q_num, :q_id, :player_id, :answer, :is_correct, :now)
    """), {
        'session_id': session_data.id,
        'q_num': q_state['question_number'],
        'q_id': q_state['question_id'],
        'player_id': player.id,
        'answer': answer,
        'is_correct': is_correct,
        'now': now
    })
    db.session.commit()
    
    update_session_activity(code)
    
    return jsonify({'success': True, 'locked_in': True})


@team_play_bp.route('/api/team/session/<code>/status', methods=['GET'])
@require_team_play_eligible
def get_team_status(code):
    """Poll for session status (call every 2 seconds)"""
    from sqlalchemy import text
    
    code = code.upper()
    
    if check_session_timeout(code):
        return jsonify({'error': 'Session has timed out', 'status': 'timeout'}), 410
    
    # Get session
    session_data = db.session.execute(text("""
        SELECT id, status, topic, question_count, started_at
        FROM team_sessions WHERE session_code = :code
    """), {'code': code}).fetchone()
    
    if not session_data:
        return jsonify({'error': 'Session not found'}), 404
    
    # Get players
    players = db.session.execute(text("""
        SELECT id, display_name, is_organiser, user_id, guest_code
        FROM team_session_players 
        WHERE session_id = :session_id AND status = 'active'
    """), {'session_id': session_data.id}).fetchall()
    
    player_list = []
    for p in players:
        is_me = (p.user_id == session.get('user_id') if p.user_id else p.guest_code == session.get('guest_code'))
        player_list.append({
            'id': p.id,
            'name': p.display_name,
            'is_organiser': bool(p.is_organiser),
            'is_me': is_me
        })
    
    result = {
        'status': session_data.status,
        'players': player_list,
        'player_count': len(player_list)
    }
    
    # If active, include question state
    if session_data.status == 'active':
        q_state = session_questions.get(code, {})
        
        result['question_number'] = q_state.get('question_number', 0)
        result['total_questions'] = session_data.question_count
        result['question'] = q_state.get('question_data')
        
        # Calculate time remaining
        if q_state.get('first_lock_at'):
            elapsed = (datetime.utcnow() - q_state['first_lock_at']).total_seconds()
            remaining = max(0, TEAM_PLAY_CONFIG['lock_in_seconds'] - elapsed)
            result['time_remaining'] = round(remaining)
            result['timer_active'] = True
        else:
            result['time_remaining'] = TEAM_PLAY_CONFIG['lock_in_seconds']
            result['timer_active'] = False
        
        # Get lock-in status for each player
        if q_state.get('question_number'):
            answers = db.session.execute(text("""
                SELECT player_id FROM team_session_answers 
                WHERE session_id = :session_id AND question_number = :q_num
            """), {
                'session_id': session_data.id,
                'q_num': q_state['question_number']
            }).fetchall()
            
            locked_player_ids = {a.player_id for a in answers}
            
            for p in result['players']:
                p['locked_in'] = p['id'] in locked_player_ids
        
        # Get chat messages (last 20)
        chat_messages = session_chats.get(code, [])[-20:]
        result['chat'] = chat_messages
    
    return jsonify(result)


@team_play_bp.route('/api/team/session/<code>/reveal', methods=['GET'])
@require_team_play_eligible
def get_question_results(code):
    """Get results for current question after all locked in or timeout"""
    from sqlalchemy import text
    
    code = code.upper()
    
    # Get session
    session_data = db.session.execute(text("""
        SELECT id, status FROM team_sessions WHERE session_code = :code
    """), {'code': code}).fetchone()
    
    if not session_data or session_data.status != 'active':
        return jsonify({'error': 'Session not active'}), 400
    
    q_state = session_questions.get(code, {})
    if not q_state.get('question_number'):
        return jsonify({'error': 'No active question'}), 400
    
    # Get all players
    players = db.session.execute(text("""
        SELECT id, display_name FROM team_session_players 
        WHERE session_id = :session_id AND status = 'active'
    """), {'session_id': session_data.id}).fetchall()
    
    # Get all answers for this question
    answers = db.session.execute(text("""
        SELECT player_id, answer, is_correct, points_earned, bonus_earned
        FROM team_session_answers 
        WHERE session_id = :session_id AND question_number = :q_num
    """), {
        'session_id': session_data.id,
        'q_num': q_state['question_number']
    }).fetchall()
    
    answer_map = {a.player_id: a for a in answers}
    
    # Determine correct answer
    correct_answer = q_state.get('correct_answer')
    if isinstance(correct_answer, int) or (isinstance(correct_answer, str) and correct_answer.isdigit()):
        correct_letter = ['A', 'B', 'C', 'D'][int(correct_answer)]
    else:
        correct_letter = str(correct_answer).upper()
    
    # Build results
    results = []
    all_answers = []
    any_correct = False
    
    for p in players:
        ans = answer_map.get(p.id)
        if ans:
            results.append({
                'name': p.display_name,
                'answer': ans.answer,
                'is_correct': ans.is_correct,
                'points': ans.points_earned or 0,
                'bonus': ans.bonus_earned or 0
            })
            all_answers.append(ans.answer)
            if ans.is_correct:
                any_correct = True
        else:
            # Abstained
            results.append({
                'name': p.display_name,
                'answer': None,
                'is_correct': False,
                'points': 0,
                'bonus': 0,
                'abstained': True
            })
    
    # Check for team bonus
    locked_answers = [a for a in all_answers if a]  # Non-abstained
    all_match = len(set(locked_answers)) == 1 and len(locked_answers) == len(players)
    team_bonus = all_match and any_correct
    
    return jsonify({
        'question_number': q_state['question_number'],
        'correct_answer': correct_letter,
        'explanation': q_state.get('explanation'),
        'results': results,
        'team_bonus': team_bonus,
        'all_matched': all_match
    })


@team_play_bp.route('/api/team/session/<code>/calculate-points', methods=['POST'])
@require_team_play_eligible
def calculate_question_points(code):
    """Calculate and award points for the current question"""
    from sqlalchemy import text
    
    code = code.upper()
    
    # Get session
    session_data = db.session.execute(text("""
        SELECT id FROM team_sessions WHERE session_code = :code
    """), {'code': code}).fetchone()
    
    if not session_data:
        return jsonify({'error': 'Session not found'}), 404
    
    q_state = session_questions.get(code, {})
    if not q_state.get('question_number'):
        return jsonify({'error': 'No active question'}), 400
    
    # Get all active players
    players = db.session.execute(text("""
        SELECT id, user_id, guest_code FROM team_session_players 
        WHERE session_id = :session_id AND status = 'active'
    """), {'session_id': session_data.id}).fetchall()
    
    player_count = len(players)
    bonus_multiplier = TEAM_PLAY_CONFIG['bonus_multipliers'].get(player_count, 0)
    
    # Get answers
    answers = db.session.execute(text("""
        SELECT player_id, answer, is_correct
        FROM team_session_answers 
        WHERE session_id = :session_id AND question_number = :q_num
    """), {
        'session_id': session_data.id,
        'q_num': q_state['question_number']
    }).fetchall()
    
    answer_map = {a.player_id: a for a in answers}
    
    # Check if all match and correct
    locked_answers = [a.answer for a in answers if a.answer]
    all_match = len(set(locked_answers)) == 1 and len(locked_answers) == player_count
    any_correct = any(a.is_correct for a in answers)
    team_bonus_applies = all_match and any_correct
    
    # Calculate and award points
    base_points = 10  # Base points per correct answer
    
    for p in players:
        ans = answer_map.get(p.id)
        points = 0
        bonus = 0
        
        if ans and ans.is_correct:
            points = base_points
            if team_bonus_applies:
                bonus = int(base_points * bonus_multiplier)
        
        # Update answer record
        db.session.execute(text("""
            UPDATE team_session_answers 
            SET points_earned = :points, bonus_earned = :bonus
            WHERE session_id = :session_id 
            AND question_number = :q_num 
            AND player_id = :player_id
        """), {
            'points': points,
            'bonus': bonus,
            'session_id': session_data.id,
            'q_num': q_state['question_number'],
            'player_id': p.id
        })
        
        # Award to user's account
        total_earned = points + bonus
        if total_earned > 0:
            if p.user_id:
                db.session.execute(text("""
                    UPDATE users SET total_points = total_points + :pts WHERE id = :uid
                """), {'pts': total_earned, 'uid': p.user_id})
            elif p.guest_code:
                # Update or insert guest points
                existing = db.session.execute(text("""
                    SELECT id FROM user_points WHERE guest_code = :gc
                """), {'gc': p.guest_code}).fetchone()
                
                if existing:
                    db.session.execute(text("""
                        UPDATE user_points SET points = points + :pts WHERE guest_code = :gc
                    """), {'pts': total_earned, 'gc': p.guest_code})
                else:
                    db.session.execute(text("""
                        INSERT INTO user_points (guest_code, points) VALUES (:gc, :pts)
                    """), {'gc': p.guest_code, 'pts': total_earned})
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'team_bonus_applied': team_bonus_applies,
        'bonus_multiplier': bonus_multiplier if team_bonus_applies else 0
    })


# ==================== CHAT ====================

@team_play_bp.route('/api/team/session/<code>/chat', methods=['POST'])
@require_team_play_eligible
def send_chat_message(code):
    """Send a chat message"""
    code = code.upper()
    
    data = request.get_json() or {}
    message = data.get('message', '').strip()
    
    if not message:
        return jsonify({'error': 'Message is required'}), 400
    
    # Filter and truncate
    filtered_message = filter_chat_message(message)
    
    display_name = get_display_name()
    
    # Add to in-memory chat
    if code not in session_chats:
        session_chats[code] = []
    
    session_chats[code].append({
        'player': display_name,
        'message': filtered_message,
        'timestamp': datetime.utcnow().isoformat()
    })
    
    # Keep only last 50 messages
    session_chats[code] = session_chats[code][-50:]
    
    update_session_activity(code)
    
    return jsonify({'success': True})


# ==================== INVITATIONS ====================

@team_play_bp.route('/api/team/invite', methods=['POST'])
@require_team_play_eligible
def send_invitation():
    """Send invitation to another user"""
    from sqlalchemy import text
    
    data = request.get_json() or {}
    session_code = data.get('session_code', '').upper()
    username = data.get('username', '').strip()
    
    if not session_code or not username:
        return jsonify({'error': 'Session code and username required'}), 400
    
    # Get session
    session_data = db.session.execute(text("""
        SELECT id, status FROM team_sessions WHERE session_code = :code
    """), {'code': session_code}).fetchone()
    
    if not session_data or session_data.status != 'waiting':
        return jsonify({'error': 'Invalid or started session'}), 400
    
    # Find user by username (case-insensitive)
    target_user = db.session.execute(text("""
        SELECT id, username FROM users WHERE LOWER(username) = LOWER(:username)
    """), {'username': username}).fetchone()
    
    target_guest = None
    if not target_user:
        # Try finding a guest by their guest_name or code
        target_guest = db.session.execute(text("""
            SELECT guest_code, guest_name FROM guest_sessions 
            WHERE LOWER(guest_name) = LOWER(:username)
            OR LOWER(guest_code) = LOWER(:username)
            ORDER BY created_at DESC LIMIT 1
        """), {'username': username}).fetchone()
    
    if not target_user and not target_guest:
        return jsonify({'error': 'User not found'}), 404
    
    # Create invitation
    expires_at = datetime.utcnow() + timedelta(minutes=TEAM_PLAY_CONFIG['invite_expiry_minutes'])
    
    db.session.execute(text("""
        INSERT INTO team_session_invites 
        (session_id, invited_user_id, invited_guest_code, status, created_at, expires_at)
        VALUES (:session_id, :user_id, :guest_code, 'pending', :now, :expires)
    """), {
        'session_id': session_data.id,
        'user_id': target_user.id if target_user else None,
        'guest_code': target_guest.guest_code if target_guest else None,
        'now': datetime.utcnow(),
        'expires': expires_at
    })
    db.session.commit()
    
    return jsonify({
        'success': True,
        'invited': target_user.username if target_user else target_guest.guest_name
    })


@team_play_bp.route('/api/team/invitations', methods=['GET'])
@require_team_play_eligible
def get_pending_invitations():
    """Get pending invitations for current user"""
    from sqlalchemy import text
    
    user_id, guest_code = get_user_identifier()
    now = datetime.utcnow()
    
    # Expire old invitations
    db.session.execute(text("""
        UPDATE team_session_invites 
        SET status = 'expired' 
        WHERE status = 'pending' AND expires_at < :now
    """), {'now': now})
    db.session.commit()
    
    # Get pending invitations
    invites = db.session.execute(text("""
        SELECT i.id, i.session_id, i.expires_at,
               s.session_code, s.topic, s.question_count,
               COALESCE(u.username, g.guest_name) as organiser_name
        FROM team_session_invites i
        JOIN team_sessions s ON i.session_id = s.id
        LEFT JOIN users u ON s.organiser_user_id = u.id
        LEFT JOIN guest_sessions g ON s.organiser_guest_code = g.guest_code
        WHERE i.status = 'pending'
        AND s.status = 'waiting'
        AND ((i.invited_user_id = :user_id AND :user_id IS NOT NULL)
             OR (i.invited_guest_code = :guest_code AND :guest_code IS NOT NULL))
    """), {'user_id': user_id, 'guest_code': guest_code}).fetchall()
    
    result = []
    for inv in invites:
        remaining = (inv.expires_at - now).total_seconds()
        if remaining > 0:
            result.append({
                'id': inv.id,
                'session_code': inv.session_code,
                'topic': inv.topic,
                'question_count': inv.question_count,
                'organiser': inv.organiser_name,
                'expires_in_seconds': int(remaining)
            })
    
    return jsonify({'invitations': result})


@team_play_bp.route('/api/team/invitation/<int:invite_id>/accept', methods=['POST'])
@require_team_play_eligible
def accept_invitation(invite_id):
    """Accept an invitation"""
    from sqlalchemy import text
    
    user_id, guest_code = get_user_identifier()
    
    # Get invitation
    invite = db.session.execute(text("""
        SELECT i.*, s.session_code 
        FROM team_session_invites i
        JOIN team_sessions s ON i.session_id = s.id
        WHERE i.id = :id AND i.status = 'pending'
        AND ((i.invited_user_id = :user_id AND :user_id IS NOT NULL)
             OR (i.invited_guest_code = :guest_code AND :guest_code IS NOT NULL))
    """), {'id': invite_id, 'user_id': user_id, 'guest_code': guest_code}).fetchone()
    
    if not invite:
        return jsonify({'error': 'Invitation not found or expired'}), 404
    
    # Mark as accepted
    db.session.execute(text("""
        UPDATE team_session_invites SET status = 'accepted' WHERE id = :id
    """), {'id': invite_id})
    db.session.commit()
    
    return jsonify({
        'success': True,
        'session_code': invite.session_code
    })


@team_play_bp.route('/api/team/invitation/<int:invite_id>/decline', methods=['POST'])
@require_team_play_eligible
def decline_invitation(invite_id):
    """Decline an invitation"""
    from sqlalchemy import text
    
    user_id, guest_code = get_user_identifier()
    
    db.session.execute(text("""
        UPDATE team_session_invites SET status = 'declined' 
        WHERE id = :id
        AND ((invited_user_id = :user_id AND :user_id IS NOT NULL)
             OR (invited_guest_code = :guest_code AND :guest_code IS NOT NULL))
    """), {'id': invite_id, 'user_id': user_id, 'guest_code': guest_code})
    db.session.commit()
    
    return jsonify({'success': True})


# ==================== FINAL RESULTS ====================

@team_play_bp.route('/api/team/session/<code>/final-results', methods=['GET'])
@require_team_play_eligible
def get_final_results(code):
    """Get final results for completed session"""
    from sqlalchemy import text
    
    code = code.upper()
    
    # Get session
    session_data = db.session.execute(text("""
        SELECT id, topic, question_count, started_at, ended_at
        FROM team_sessions WHERE session_code = :code
    """), {'code': code}).fetchone()
    
    if not session_data:
        return jsonify({'error': 'Session not found'}), 404
    
    # Get players with totals
    players = db.session.execute(text("""
        SELECT p.id, p.display_name, p.is_organiser,
               COALESCE(SUM(a.points_earned), 0) as total_points,
               COALESCE(SUM(a.bonus_earned), 0) as total_bonus,
               COUNT(CASE WHEN a.is_correct THEN 1 END) as correct_count
        FROM team_session_players p
        LEFT JOIN team_session_answers a ON p.id = a.player_id
        WHERE p.session_id = :session_id AND p.status = 'active'
        GROUP BY p.id, p.display_name, p.is_organiser
        ORDER BY (COALESCE(SUM(a.points_earned), 0) + COALESCE(SUM(a.bonus_earned), 0)) DESC
    """), {'session_id': session_data.id}).fetchall()
    
    # Count matching questions
    agreement_count = db.session.execute(text("""
        SELECT COUNT(DISTINCT question_number) as count
        FROM team_session_answers
        WHERE session_id = :session_id
        GROUP BY question_number
        HAVING COUNT(DISTINCT answer) = 1 AND COUNT(*) = (
            SELECT COUNT(*) FROM team_session_players 
            WHERE session_id = :session_id AND status = 'active'
        )
    """), {'session_id': session_data.id}).fetchall()
    
    agreement_rate = (len(agreement_count) / session_data.question_count * 100) if session_data.question_count else 0
    
    results = []
    for i, p in enumerate(players):
        results.append({
            'rank': i + 1,
            'name': p.display_name,
            'is_organiser': bool(p.is_organiser),
            'points': p.total_points + p.total_bonus,
            'base_points': p.total_points,
            'bonus_points': p.total_bonus,
            'correct': p.correct_count,
            'total': session_data.question_count
        })
    
    total_bonus = sum(p.total_bonus for p in players)
    
    return jsonify({
        'topic': session_data.topic,
        'question_count': session_data.question_count,
        'agreement_rate': round(agreement_rate),
        'total_team_bonus': total_bonus,
        'results': results
    })


# ==================== RECENT PLAYERS ====================

@team_play_bp.route('/api/team/recent-players', methods=['GET'])
@require_team_play_eligible
def get_recent_players():
    """Get list of recent players for invitation suggestions"""
    from sqlalchemy import text
    
    user_id, guest_code = get_user_identifier()
    
    # Get players from recent sessions this user was in
    recent = db.session.execute(text("""
        SELECT DISTINCT p2.display_name, p2.user_id, p2.guest_code
        FROM team_session_players p1
        JOIN team_session_players p2 ON p1.session_id = p2.session_id
        WHERE p1.user_id = :user_id OR p1.guest_code = :guest_code
        AND (p2.user_id != :user_id OR p2.guest_code != :guest_code)
        AND p2.display_name IS NOT NULL
        ORDER BY p2.display_name
        LIMIT 10
    """), {'user_id': user_id, 'guest_code': guest_code}).fetchall()
    
    return jsonify({
        'recent_players': [{'name': r.display_name} for r in recent]
    })


# ==================== REGISTRATION ====================

def register_team_play_routes(app, database):
    """Register Team Play routes with Flask app"""
    global db
    db = database
    app.register_blueprint(team_play_bp)
    print("✅ Team Play routes registered")
