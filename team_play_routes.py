"""
Team Play Routes - AgentMath Collaborative Quiz Feature
Version 1.1 - December 2025

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
session_chats = {}

# In-memory current question tracking
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
    """Check if user is eligible for Team Play (account or repeat guest)"""
    if not session.get('is_guest'):
        return True  # Registered user
    guest_code = session.get('guest_code')
    return guest_code is not None and len(guest_code) > 0


def require_team_play_eligible(f):
    """Decorator to require Team Play eligibility"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_repeat_guest_or_account():
            return jsonify({'error': 'Team Play requires an account or repeat guest code'}), 403
        return f(*args, **kwargs)
    return decorated_function


def update_session_activity(session_code):
    """Update the last_activity timestamp for a session"""
    from sqlalchemy import text
    try:
        db.session.execute(text("""
            UPDATE team_sessions 
            SET last_activity = :now 
            WHERE session_code = :code
        """), {'now': datetime.utcnow(), 'code': session_code})
        db.session.commit()
        return True
    except:
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
    time_limit = data.get('time_limit_minutes')
    difficulty_levels = data.get('difficulty_levels', '1-12')
    
    if not topic:
        return jsonify({'error': 'Topic is required'}), 400
    
    user_id, guest_code = get_user_identifier()
    
    # Generate unique code
    code = None
    for _ in range(10):
        candidate = generate_session_code()
        existing = db.session.execute(text(
            "SELECT id FROM team_sessions WHERE session_code = :code"
        ), {'code': candidate}).fetchone()
        if not existing:
            code = candidate
            break
    
    if not code:
        return jsonify({'error': 'Could not generate unique code'}), 500
    
    # Create session
    now = datetime.utcnow()
    try:
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
    except Exception as e:
        db.session.rollback()
        print(f"Error creating session: {e}")
        return jsonify({'error': 'Database error creating session'}), 500
    
    # Get session ID
    result = db.session.execute(text(
        "SELECT id FROM team_sessions WHERE session_code = :code"
    ), {'code': code}).fetchone()
    session_id = result[0] if result else None
    
    if not session_id:
        return jsonify({'error': 'Session created but ID not found'}), 500
    
    # Add organiser as first player
    display_name = get_display_name()
    try:
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
    except Exception as e:
        db.session.rollback()
        print(f"Error adding organiser: {e}")
    
    # Initialize chat storage
    session_chats[code] = []
    
    return jsonify({
        'success': True,
        'session_code': code,
        'session_id': session_id
    })


@team_play_bp.route('/api/team/session/<code>', methods=['GET'])
def get_team_session(code):
    """Get session details"""
    from sqlalchemy import text
    
    code = code.upper()
    
    session_data = db.session.execute(text("""
        SELECT id, session_code, topic, difficulty_levels, question_count,
               time_limit_minutes, status, created_at, started_at
        FROM team_sessions WHERE session_code = :code
    """), {'code': code}).fetchone()
    
    if not session_data:
        return jsonify({'error': 'Session not found'}), 404
    
    # Get players
    players = db.session.execute(text("""
        SELECT id, display_name, is_organiser, status
        FROM team_session_players
        WHERE session_id = :session_id AND status = 'active'
        ORDER BY joined_at
    """), {'session_id': session_data[0]}).fetchall()
    
    return jsonify({
        'session_code': session_data[1],
        'topic': session_data[2],
        'difficulty_levels': session_data[3],
        'question_count': session_data[4],
        'time_limit_minutes': session_data[5],
        'status': session_data[6],
        'created_at': session_data[7].isoformat() if session_data[7] else None,
        'started_at': session_data[8].isoformat() if session_data[8] else None,
        'players': [{
            'id': p[0],
            'display_name': p[1],
            'is_organiser': bool(p[2]),
            'status': p[3]
        } for p in players]
    })


@team_play_bp.route('/api/team/session/<code>/join', methods=['POST'])
@require_team_play_eligible
def join_team_session(code):
    """Join an existing session"""
    from sqlalchemy import text
    
    code = code.upper()
    user_id, guest_code = get_user_identifier()
    
    # Check session exists and is waiting
    session_data = db.session.execute(text("""
        SELECT id, status FROM team_sessions WHERE session_code = :code
    """), {'code': code}).fetchone()
    
    if not session_data:
        return jsonify({'error': 'Session not found'}), 404
    
    if session_data[1] != 'waiting':
        return jsonify({'error': 'Session already started or ended'}), 400
    
    session_id = session_data[0]
    
    # Check if already in session
    existing = db.session.execute(text("""
        SELECT id FROM team_session_players
        WHERE session_id = :session_id
        AND (user_id = :user_id OR guest_code = :guest_code)
        AND status = 'active'
    """), {
        'session_id': session_id,
        'user_id': user_id,
        'guest_code': guest_code
    }).fetchone()
    
    if existing:
        return jsonify({'success': True, 'message': 'Already in session'})
    
    # Check player limit
    player_count = db.session.execute(text("""
        SELECT COUNT(*) FROM team_session_players
        WHERE session_id = :session_id AND status = 'active'
    """), {'session_id': session_id}).fetchone()[0]
    
    if player_count >= TEAM_PLAY_CONFIG['max_players']:
        return jsonify({'error': 'Session is full (max 4 players)'}), 400
    
    # Add player
    display_name = get_display_name()
    try:
        db.session.execute(text("""
            INSERT INTO team_session_players 
            (session_id, user_id, guest_code, display_name, is_organiser, joined_at, status)
            VALUES (:session_id, :user_id, :guest_code, :name, 0, :now, 'active')
        """), {
            'session_id': session_id,
            'user_id': user_id,
            'guest_code': guest_code if not user_id else None,
            'name': display_name,
            'now': datetime.utcnow()
        })
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error joining session: {e}")
        return jsonify({'error': 'Could not join session'}), 500
    
    update_session_activity(code)
    
    return jsonify({'success': True, 'session_code': code})


@team_play_bp.route('/api/team/session/<code>/leave', methods=['POST'])
def leave_team_session(code):
    """Leave a session"""
    from sqlalchemy import text
    
    code = code.upper()
    user_id, guest_code = get_user_identifier()
    
    # Get session
    session_data = db.session.execute(text("""
        SELECT id FROM team_sessions WHERE session_code = :code
    """), {'code': code}).fetchone()
    
    if not session_data:
        return jsonify({'error': 'Session not found'}), 404
    
    # Mark player as left
    try:
        db.session.execute(text("""
            UPDATE team_session_players 
            SET status = 'left'
            WHERE session_id = :session_id
            AND (user_id = :user_id OR guest_code = :guest_code)
        """), {
            'session_id': session_data[0],
            'user_id': user_id,
            'guest_code': guest_code
        })
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error leaving session: {e}")
    
    return jsonify({'success': True})


@team_play_bp.route('/api/team/session/<code>/status', methods=['GET'])
def get_session_status(code):
    """Poll for session updates"""
    from sqlalchemy import text
    
    code = code.upper()
    
    # Get session
    session_data = db.session.execute(text("""
        SELECT id, status, topic, question_count FROM team_sessions WHERE session_code = :code
    """), {'code': code}).fetchone()
    
    if not session_data:
        return jsonify({'error': 'Session not found'}), 404
    
    session_id = session_data[0]
    
    # Get players
    players = db.session.execute(text("""
        SELECT id, display_name, is_organiser, status
        FROM team_session_players
        WHERE session_id = :session_id AND status = 'active'
        ORDER BY joined_at
    """), {'session_id': session_id}).fetchall()
    
    # Get chat
    chat = session_chats.get(code, [])[-20:]  # Last 20 messages
    
    return jsonify({
        'status': session_data[1],
        'topic': session_data[2],
        'question_count': session_data[3],
        'players': [{
            'id': p[0],
            'display_name': p[1],
            'is_organiser': bool(p[2]),
            'status': p[3]
        } for p in players],
        'chat': chat,
        'player_count': len(players)
    })


@team_play_bp.route('/api/team/session/<code>/start', methods=['POST'])
@require_team_play_eligible
def start_team_session(code):
    """Start the quiz (organiser only)"""
    from sqlalchemy import text
    
    code = code.upper()
    user_id, guest_code = get_user_identifier()
    
    # Verify organiser
    session_data = db.session.execute(text("""
        SELECT ts.id, ts.status, ts.organiser_user_id, ts.organiser_guest_code
        FROM team_sessions ts
        WHERE ts.session_code = :code
    """), {'code': code}).fetchone()
    
    if not session_data:
        return jsonify({'error': 'Session not found'}), 404
    
    # Check if user is organiser
    is_org = (session_data[2] == user_id) or (session_data[3] == guest_code)
    if not is_org:
        return jsonify({'error': 'Only the host can start the quiz'}), 403
    
    if session_data[1] != 'waiting':
        return jsonify({'error': 'Session already started or ended'}), 400
    
    # Check player count
    player_count = db.session.execute(text("""
        SELECT COUNT(*) FROM team_session_players
        WHERE session_id = :session_id AND status = 'active'
    """), {'session_id': session_data[0]}).fetchone()[0]
    
    if player_count < TEAM_PLAY_CONFIG['min_players']:
        return jsonify({'error': f'Need at least {TEAM_PLAY_CONFIG["min_players"]} players to start'}), 400
    
    # Start session
    try:
        db.session.execute(text("""
            UPDATE team_sessions 
            SET status = 'active', started_at = :now, last_activity = :now
            WHERE session_code = :code
        """), {'now': datetime.utcnow(), 'code': code})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Could not start session'}), 500
    
    return jsonify({'success': True, 'status': 'active'})


@team_play_bp.route('/api/team/session/<code>/end', methods=['POST'])
@require_team_play_eligible
def end_team_session(code):
    """End the session (organiser only)"""
    from sqlalchemy import text
    
    code = code.upper()
    user_id, guest_code = get_user_identifier()
    
    # Verify organiser
    session_data = db.session.execute(text("""
        SELECT id, organiser_user_id, organiser_guest_code
        FROM team_sessions WHERE session_code = :code
    """), {'code': code}).fetchone()
    
    if not session_data:
        return jsonify({'error': 'Session not found'}), 404
    
    is_org = (session_data[1] == user_id) or (session_data[2] == guest_code)
    if not is_org:
        return jsonify({'error': 'Only the host can end the session'}), 403
    
    try:
        db.session.execute(text("""
            UPDATE team_sessions 
            SET status = 'ended', ended_at = :now
            WHERE session_code = :code
        """), {'now': datetime.utcnow(), 'code': code})
        db.session.commit()
    except:
        db.session.rollback()
    
    # Clean up chat
    if code in session_chats:
        del session_chats[code]
    
    return jsonify({'success': True})


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
    
    filtered_message = filter_chat_message(message)
    display_name = get_display_name()
    
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

@team_play_bp.route('/api/team/invitations', methods=['GET'])
@require_team_play_eligible
def get_invitations():
    """Check for pending invitations"""
    from sqlalchemy import text
    
    user_id, guest_code = get_user_identifier()
    
    # Get pending invitations
    invites = db.session.execute(text("""
        SELECT tsi.id, ts.session_code, tsp.display_name as from_player
        FROM team_session_invites tsi
        JOIN team_sessions ts ON tsi.session_id = ts.id
        JOIN team_session_players tsp ON ts.id = tsp.session_id AND tsp.is_organiser = 1
        WHERE (tsi.invited_user_id = :user_id OR tsi.invited_guest_code = :guest_code)
        AND tsi.status = 'pending'
        AND ts.status = 'waiting'
        AND (tsi.expires_at IS NULL OR tsi.expires_at > :now)
        ORDER BY tsi.created_at DESC
        LIMIT 5
    """), {
        'user_id': user_id,
        'guest_code': guest_code,
        'now': datetime.utcnow()
    }).fetchall()
    
    return jsonify({
        'invitations': [{
            'id': inv[0],
            'session_code': inv[1],
            'from_player': inv[2]
        } for inv in invites]
    })


@team_play_bp.route('/api/team/invitation/<int:invite_id>/accept', methods=['POST'])
@require_team_play_eligible
def accept_invitation(invite_id):
    """Accept an invitation"""
    from sqlalchemy import text
    
    user_id, guest_code = get_user_identifier()
    
    # Get invitation
    invite = db.session.execute(text("""
        SELECT tsi.session_id, ts.session_code
        FROM team_session_invites tsi
        JOIN team_sessions ts ON tsi.session_id = ts.id
        WHERE tsi.id = :invite_id
        AND (tsi.invited_user_id = :user_id OR tsi.invited_guest_code = :guest_code)
        AND tsi.status = 'pending'
    """), {
        'invite_id': invite_id,
        'user_id': user_id,
        'guest_code': guest_code
    }).fetchone()
    
    if not invite:
        return jsonify({'error': 'Invitation not found or expired'}), 404
    
    # Update invitation status
    db.session.execute(text("""
        UPDATE team_session_invites SET status = 'accepted' WHERE id = :id
    """), {'id': invite_id})
    db.session.commit()
    
    # Join session
    return join_team_session(invite[1])


@team_play_bp.route('/api/team/invitation/<int:invite_id>/decline', methods=['POST'])
@require_team_play_eligible
def decline_invitation(invite_id):
    """Decline an invitation"""
    from sqlalchemy import text
    
    user_id, guest_code = get_user_identifier()
    
    db.session.execute(text("""
        UPDATE team_session_invites SET status = 'declined' 
        WHERE id = :id
        AND (invited_user_id = :user_id OR invited_guest_code = :guest_code)
    """), {
        'id': invite_id,
        'user_id': user_id,
        'guest_code': guest_code
    })
    db.session.commit()
    
    return jsonify({'success': True})


# ==================== REGISTRATION ====================

def register_team_play_routes(app, database):
    """Register Team Play routes with Flask app"""
    global db
    db = database
    app.register_blueprint(team_play_bp)
    print("✅ Team Play routes registered")
