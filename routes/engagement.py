# routes/engagement.py
# Student engagement features for AgentMath
# Extracted from app.py for better maintainability
#
# Revision: 1.0.3
# Date: 2025-12-31
# Phase 11: Engagement features extraction
#
# Fixes in 1.0.3:
# - Added /api/submit-feedback route for student feedback submission
# - Added /api/my-feedback route for users to view their submitted feedback
#
# Fix in 1.0.2: Added missing uuid import for casual guest sessions
#
# Contains 23 routes for:
# - Question Flagging (3 routes) - /api/student/flag-*, /api/student/my-flags
# - Guest System (7 routes) - logout, casual/repeat guest routes
# - Quick Play & Weekly Challenge (5 routes) - /api/quick-play/*, /api/weekly-challenge/*, /api/leaderboard/*
# - Puzzle of the Week (6 routes) - /api/puzzle/*
# - User Feedback (2 routes) - /api/submit-feedback, /api/my-feedback

from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for, flash, current_app
from datetime import datetime, timedelta
from sqlalchemy import text
import random
import secrets
import string
import uuid

# Create blueprint
engagement_bp = Blueprint('engagement', __name__)

# Import database and models
from models import (
    db, User, UserStats, QuestionFlag, QuizAttempt, TopicProgress,
    WeeklyPuzzle, PuzzleUserStatus, UserAvatarEquipped
)

# Import decorators from utils
from utils import login_required, guest_or_login_required, approved_required

# Import helper functions
from utils import check_and_award_badges, get_animal_from_guest_code, grant_default_avatar_items


# Import helper functions
from utils import check_and_award_badges, get_animal_from_guest_code


# ==================== PUZZLE HELPER FUNCTIONS ====================

def get_current_week_year():
    """Get the current ISO week number and year"""
    now = datetime.now()
    week_number = now.isocalendar()[1]
    year = now.isocalendar()[0]
    return week_number, year


def get_active_puzzle():
    """Get the currently active puzzle for this week"""
    week_number, year = get_current_week_year()
    
    # First try to find active puzzle for current week
    puzzle = WeeklyPuzzle.query.filter_by(
        week_number=week_number,
        year=year,
        is_active=True
    ).first()
    
    if puzzle:
        return puzzle
    
    # If no current week puzzle, find any active puzzle
    return WeeklyPuzzle.query.filter_by(is_active=True).first()


def get_user_puzzle_status(puzzle_id, user_id=None, guest_code=None, session_id=None):
    """Get or create a puzzle status record for a user"""
    if not any([user_id, guest_code, session_id]):
        return None
    
    # Try to find existing status
    if user_id:
        status = PuzzleUserStatus.query.filter_by(puzzle_id=puzzle_id, user_id=user_id).first()
    elif guest_code:
        status = PuzzleUserStatus.query.filter_by(puzzle_id=puzzle_id, guest_code=guest_code).first()
    elif session_id:
        status = PuzzleUserStatus.query.filter_by(puzzle_id=puzzle_id, session_id=session_id).first()
    else:
        status = None
    
    # Create if not exists
    if not status:
        try:
            status = PuzzleUserStatus(
                puzzle_id=puzzle_id,
                user_id=user_id,
                guest_code=guest_code,
                session_id=session_id
            )
            db.session.add(status)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error creating puzzle status: {e}")
            return None
    
    return status


# ==================== QUESTION FLAGGING ROUTES ====================

# ==================== FEATURE FLAGS ACCESS ====================
class FeatureFlagsProxy:
    """Proxy class to access feature flags from app config"""
    def get(self, key, default=False):
        try:
            flags = current_app.config.get('FEATURE_FLAGS', {})
            return flags.get(key, default)
        except:
            return default
    
    def __getitem__(self, key):
        return self.get(key, False)

FEATURE_FLAGS = FeatureFlagsProxy()


@engagement_bp.route('/api/student/flag-question', methods=['POST'])
def flag_question():
    """Flag a question - works for both registered and guest users"""
    data = request.json

    question_id = data.get('question_id')
    flag_type = data.get('flag_type')
    description = data.get('description', '').strip()
    guest_email = data.get('guest_email', '').strip()  # Optional for guests

    if not all([question_id, flag_type, description]):
        return jsonify({'error': 'Question ID, flag type, and description are required'}), 400

    if flag_type not in ['incorrect', 'ambiguous', 'typo', 'other']:
        return jsonify({'error': 'Invalid flag type'}), 400

    question = Question.query.get(question_id)
    if not question:
        return jsonify({'error': 'Question not found'}), 404

    # Check if user is logged in
    if 'user_id' in session:
        # Registered user
        flag = QuestionFlag(
            question_id=question_id,
            user_id=session['user_id'],
            flag_type=flag_type,
            description=description
        )
    else:
        # Guest user - use IP address or session ID as identifier
        import hashlib
        guest_id = request.remote_addr or 'unknown'
        # Create a hash of IP + user agent for better privacy
        user_agent = request.headers.get('User-Agent', '')
        guest_identifier = hashlib.md5(f"{guest_id}{user_agent}".encode()).hexdigest()[:16]

        flag = QuestionFlag(
            question_id=question_id,
            user_id=None,
            guest_identifier=guest_identifier,
            guest_email=guest_email if guest_email else None,
            flag_type=flag_type,
            description=description
        )

    db.session.add(flag)
    db.session.commit()

    return jsonify({
        'message': 'Question flagged successfully. An administrator will review it.',
        'flag': flag.to_dict()
    }), 201


@engagement_bp.route('/api/student/flag-adaptive-question', methods=['POST'])
def flag_adaptive_question():
    """Flag an adaptive quiz question - works for both registered and guest users"""
    from sqlalchemy import text
    
    data = request.json

    question_id = data.get('question_id')
    topic = data.get('topic', '')
    flag_type = data.get('flag_type')
    description = data.get('description', '').strip()
    question_text = data.get('question_text', '')

    if not all([question_id, flag_type, description]):
        return jsonify({'error': 'Question ID, flag type, and description are required'}), 400

    if flag_type not in ['incorrect', 'ambiguous', 'typo', 'other']:
        return jsonify({'error': 'Invalid flag type'}), 400

    # Verify the adaptive question exists
    result = db.session.execute(text(
        "SELECT id, question_text FROM questions_adaptive WHERE id = :qid"
    ), {'qid': question_id}).fetchone()
    
    if not result:
        return jsonify({'error': 'Adaptive question not found'}), 404
    
    # Use stored question text if not provided
    if not question_text:
        question_text = result[1]

    # Check if user is logged in
    if 'user_id' in session:
        # Registered user
        flag = AdaptiveQuestionFlag(
            question_id=question_id,
            topic=topic,
            user_id=session['user_id'],
            flag_type=flag_type,
            description=description,
            question_text=question_text
        )
    else:
        # Guest user
        import hashlib
        guest_id = request.remote_addr or 'unknown'
        user_agent = request.headers.get('User-Agent', '')
        guest_identifier = hashlib.md5(f"{guest_id}{user_agent}".encode()).hexdigest()[:16]

        flag = AdaptiveQuestionFlag(
            question_id=question_id,
            topic=topic,
            user_id=None,
            guest_identifier=guest_identifier,
            flag_type=flag_type,
            description=description,
            question_text=question_text
        )

    db.session.add(flag)
    db.session.commit()

    return jsonify({
        'message': 'Question flagged successfully. An administrator will review it.',
        'flag': flag.to_dict()
    }), 201


@engagement_bp.route('/api/student/my-flags')
def get_my_flags():
    """Get all flags submitted by current user or guest"""
    if 'user_id' in session:
        # Registered user
        flags = QuestionFlag.query.filter_by(user_id=session['user_id']).order_by(QuestionFlag.created_at.desc()).all()
    else:
        # Guest user - use their identifier
        import hashlib
        guest_id = request.remote_addr or 'unknown'
        user_agent = request.headers.get('User-Agent', '')
        guest_identifier = hashlib.md5(f"{guest_id}{user_agent}".encode()).hexdigest()[:16]

        flags = QuestionFlag.query.filter_by(guest_identifier=guest_identifier).order_by(QuestionFlag.created_at.desc()).all()
    return jsonify([f.to_dict() for f in flags])



if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # Create default admin if doesn't exist
        admin = User.query.filter_by(email='admin@agentmath.app').first()
        if not admin:
            admin = User(
                email='admin@agentmath.app',
                full_name='System Administrator',
                role='admin',
                is_approved=True
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("Default admin created: admin@agentmath.app / admin123")

        # Create default badges if they don't exist
        if Badge.query.count() == 0:
            default_badges = [
                # Beginner badges
                Badge(name='First Steps', description='Complete your first quiz', icon='fa-star',
                      category='beginner', requirement_type='quizzes_completed', requirement_value=1,
                      points=10, color='yellow'),
                Badge(name='Curious Learner', description='Complete 5 quizzes', icon='fa-book',
                      category='progress', requirement_type='quizzes_completed', requirement_value=5,
                      points=20, color='blue'),
                Badge(name='Dedicated Student', description='Complete 10 quizzes', icon='fa-graduation-cap',
                      category='progress', requirement_type='quizzes_completed', requirement_value=10,
                      points=30, color='purple'),
                Badge(name='Math Enthusiast', description='Complete 25 quizzes', icon='fa-heart',
                      category='progress', requirement_type='quizzes_completed', requirement_value=25,
                      points=50, color='red'),
                Badge(name='Quiz Master', description='Complete 50 quizzes', icon='fa-trophy',
                      category='progress', requirement_type='quizzes_completed', requirement_value=50,
                      points=100, color='gold'),

                # Streak badges
                Badge(name='Week Warrior', description='Practice 7 days in a row', icon='fa-bolt',
                      category='streak', requirement_type='streak_days', requirement_value=7,
                      points=40, color='orange'),
                Badge(name='Unstoppable', description='Practice 14 days in a row', icon='fa-rocket',
                      category='streak', requirement_type='streak_days', requirement_value=14,
                      points=75, color='red'),

                # Mastery badges
                Badge(name='Topic Master', description='Master any topic (all 3 difficulties)', icon='fa-certificate',
                      category='mastery', requirement_type='topics_mastered', requirement_value=1,
                      points=30, color='green'),
                Badge(name='Subject Expert', description='Master 3 different topics', icon='fa-brain',
                      category='mastery', requirement_type='topics_mastered', requirement_value=3,
                      points=75, color='purple'),
                Badge(name='Mathematics Genius', description='Master 5 different topics', icon='fa-infinity',
                      category='mastery', requirement_type='topics_mastered', requirement_value=5,
                      points=150, color='gold'),

                # Accuracy badges
                Badge(name='Perfect Score', description='Get 100% on a quiz', icon='fa-gem',
                      category='accuracy', requirement_type='perfect_scores', requirement_value=1,
                      points=15, color='cyan'),
                Badge(name='Perfectionist', description='Get 5 perfect scores', icon='fa-star',
                      category='accuracy', requirement_type='perfect_scores', requirement_value=5,
                      points=50, color='gold'),
                Badge(name='High Achiever', description='Score 90%+ on 10 quizzes', icon='fa-bullseye',
                      category='accuracy', requirement_type='high_scores', requirement_value=10,
                      points=40, color='green'),
                Badge(name='Excellence Personified', description='Score 90%+ on 25 quizzes', icon='fa-crown',
                      category='accuracy', requirement_type='high_scores', requirement_value=25,
                      points=100, color='gold'),
            ]

            for badge in default_badges:
                db.session.add(badge)

            db.session.commit()
            print(f"✅ Created {len(default_badges)} default badges")

    app.run(debug=True)


# ============================================================
# Minimal class actions via simple HTML forms (stable)
# ============================================================


@engagement_bp.route('/logout', methods=['GET'])
def logout_simple():
    """Simple logout route with proper session invalidation"""
    session.clear()
    try:
        response = redirect(url_for('index') + '?logged_out=1')
    except Exception:
        response = redirect('/?logged_out=1')
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.delete_cookie('session')
    return response


# ==================== DUAL GUEST SYSTEM ====================
# Supports both casual guests and repeat guests with codes

# Animal codes for repeat guests
# Curated list of avatar-friendly animals for guest codes
# These all have matching avatar images in the shop
AVATAR_ANIMALS = [
    'panda', 'fox', 'cat', 'owl', 'lion', 'bear', 'wolf', 'rabbit', 'tiger', 'penguin',
    'koala', 'elephant', 'monkey', 'dog', 'dolphin', 'horse', 'deer', 'eagle', 'parrot', 'turtle'
]

# Legacy list for reference - DO NOT USE for new codes
# These were the old animals, some of which don't make good avatars
LEGACY_ANIMALS = [
    'ant', 'ape', 'bat', 'bear', 'bee', 'bird', 'cat', 'clam', 'cod', 'cow',
    'crab', 'crow', 'deer', 'dog', 'dove', 'duck', 'eagle', 'eel', 'elk', 'fish',
    'fly', 'fox', 'frog', 'gnat', 'goat', 'goose', 'hawk', 'hog', 'horse', 'jay',
    'lark', 'lion', 'loon', 'lynx', 'mink', 'mole', 'moth', 'mouse', 'mule', 'newt',
    'orca', 'owl', 'ox', 'panda', 'pig', 'puma', 'rat', 'ray', 'seal', 'shark',
    'sheep', 'shrew', 'sloth', 'slug', 'snail', 'snake', 'swan', 'tiger', 'toad', 'trout',
    'viper', 'vole', 'wasp', 'whale', 'wolf', 'worm', 'yak', 'zebra', 'bison', 'boar',
    'bunny', 'camel', 'cobra', 'coral', 'crane', 'dingo', 'drake', 'gecko', 'hippo', 'hyena',
    'koala', 'lemur', 'llama', 'moose', 'otter', 'pony', 'quail', 'raven', 'rhino', 'robin',
    'skunk', 'squid', 'stork', 'tapir', 'tern', 'tuna', 'weasel', 'betta', 'finch', 'guppy'
]

# Use AVATAR_ANIMALS for new guest codes
ANIMALS = AVATAR_ANIMALS

def generate_guest_code():
    """Generate unique animal code (e.g., panda42)"""
    max_attempts = 100

    for _ in range(max_attempts):
        animal = random.choice(ANIMALS)
        number = random.randint(0, 99)
        code = f"{animal}{number:02d}"

        # Check if code is already taken
        from sqlalchemy import text
        existing = db.session.execute(
            text("SELECT 1 FROM guest_users WHERE guest_code = :code"),
            {"code": code}
        ).fetchone()

        if not existing:
            return code

    raise Exception("Could not generate unique guest code. Please try again.")


def get_current_user_info():
    """
    Get user info for either full account, repeat guest, or casual guest
    Returns dict with user data or None
    """
    # Check full account
    if 'user_id' in session and 'guest_code' not in session and not session.get('is_guest'):
        user = User.query.get(session['user_id'])
        if user and user.email != 'guest@agentmath.app':
            return {
                'type': 'full',
                'id': user.id,
                'name': user.full_name,
                'email': user.email,
                'role': user.role,
                'total_score': getattr(user, 'total_score', 0),
                'quizzes_completed': getattr(user, 'quizzes_completed', 0)
            }

    # Check repeat guest
    if 'guest_code' in session:
        from sqlalchemy import text
        result = db.session.execute(
            text("""SELECT guest_code, total_score, quizzes_completed, created_at, last_active
               FROM guest_users WHERE guest_code = :code AND is_active = 1"""),
            {"code": session['guest_code']}
        ).fetchone()

        if result:
            return {
                'type': 'repeat_guest',
                'guest_code': result[0],
                'name': f"Guest {result[0].title()}",
                'total_score': result[1] or 0,
                'quizzes_completed': result[2] or 0,
                'created_at': result[3],
                'last_active': result[4]
            }

    # Check casual guest (shared guest@agentmath.app user)
    if session.get('is_guest') and 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user and user.email == 'guest@agentmath.app':
            return {
                'type': 'casual_guest',
                'name': 'Guest User',
                'session_id': session.get('guest_session_id', 'unknown')
            }

    return None


def update_guest_last_active(guest_code):
    """Update last_active timestamp for repeat guest"""
    from sqlalchemy import text
    db.session.execute(
        text("UPDATE guest_users SET last_active = :now WHERE guest_code = :code"),
        {"now": datetime.utcnow(), "code": guest_code}
    )
    db.session.commit()


# ==================== CASUAL GUEST ROUTES ====================

@engagement_bp.route('/api/casual-guest-start', methods=['POST'])
def casual_guest_start():
    """Initialize casual guest session (temporary, no code)"""
    try:
        session.clear()

        # Get or create the shared casual guest user
        guest_user = User.query.filter_by(email='guest@agentmath.app').first()

        if not guest_user:
            guest_user = User(
                email='guest@agentmath.app',
                password_hash='no_password_required',
                full_name='Guest User',
                role='student',
                is_approved=True
            )
            db.session.add(guest_user)
            db.session.commit()

        # Set up casual guest session
        session['is_guest'] = True
        session['guest_session_id'] = str(uuid.uuid4())
        session['user_id'] = guest_user.id
        session['role'] = 'student'
        session['guest_type'] = 'casual'

        return jsonify({
            'success': True,
            'message': 'Casual guest session started',
            'redirect': '/student'
        }), 200

    except Exception as e:
        print(f"Error starting casual guest session: {e}")
        db.session.rollback()
        return jsonify({'error': f'Failed to start guest session: {str(e)}'}), 500


# ==================== REPEAT GUEST ROUTES ====================

@engagement_bp.route('/api/repeat-guest/generate', methods=['POST'])
def generate_repeat_guest():
    """Generate new repeat guest code"""
    try:
        from sqlalchemy import text

        # Generate unique code
        code = generate_guest_code()

        # Create guest user in database
        db.session.execute(text("""
            INSERT INTO guest_users (guest_code, created_at, last_active)
            VALUES (:code, :now, :now)
        """), {"code": code, "now": datetime.utcnow()})
        db.session.commit()

        # AVATAR: Auto-setup avatar for new guest
        animal = get_animal_from_guest_code(code)
        avatar_animal = animal if animal else 'panda'

        if FEATURE_FLAGS.get('AVATAR_SYSTEM_ENABLED', False):
            try:
                # Grant default items to new guest
                grant_default_avatar_items(guest_code=code)

                # Create equipped avatar with their animal
                equipped = UserAvatarEquipped(
                    guest_code=code,
                    animal_key=avatar_animal,
                    hat_key='none',
                    glasses_key='none',
                    background_key='none',
                    accessory_key='none'
                )
                db.session.add(equipped)
                db.session.commit()
            except Exception as avatar_error:
                print(f"Avatar setup error (non-fatal): {avatar_error}")
                # Don't fail the guest creation if avatar setup fails

        return jsonify({
            'success': True,
            'guest_code': code,
            'message': f'Your code is: {code}',
            'animal': avatar_animal  # Return animal for frontend display
        }), 200

    except Exception as e:
        print(f"Error generating guest code: {e}")
        db.session.rollback()
        return jsonify({'error': 'Failed to generate code. Please try again.'}), 500


@engagement_bp.route('/api/repeat-guest/login', methods=['POST'])
def repeat_guest_login():
    """Login with repeat guest code"""
    try:
        from sqlalchemy import text
        data = request.json
        code = data.get('guest_code', '').strip().lower()

        if not code:
            return jsonify({'error': 'Please enter your guest code'}), 400

        # Check if code exists and is active
        result = db.session.execute(
            text("SELECT guest_code FROM guest_users WHERE guest_code = :code AND is_active = 1"),
            {"code": code}
        ).fetchone()

        if not result:
            return jsonify({'error': 'Code not found. Please check and try again.'}), 404

        # Get or create the shared guest user for repeat guests
        guest_user = User.query.filter_by(email='guest@agentmath.app').first()

        if not guest_user:
            guest_user = User(
                email='guest@agentmath.app',
                password_hash='no_password_required',
                full_name='Guest User',
                role='student',
                is_approved=True
            )
            db.session.add(guest_user)
            db.session.commit()

        # Set up repeat guest session
        session.clear()
        session['is_guest'] = True  # CRITICAL: Must be True for adaptive progress to save correctly
        session['guest_code'] = code
        session['user_id'] = guest_user.id  # CRITICAL: Set user_id for @login_required
        session['role'] = 'student'
        session['guest_type'] = 'repeat'

        # Update last active
        update_guest_last_active(code)

        # AVATAR: Ensure returning guest has avatar setup
        animal = get_animal_from_guest_code(code)
        if FEATURE_FLAGS.get('AVATAR_SYSTEM_ENABLED', False):
            try:
                # Check if guest has equipped avatar
                existing_equipped = UserAvatarEquipped.query.filter_by(guest_code=code).first()

                if not existing_equipped:
                    # First time with avatar system - set up defaults
                    grant_default_avatar_items(guest_code=code)

                    equipped = UserAvatarEquipped(
                        guest_code=code,
                        animal_key=animal if animal else 'panda',
                        hat_key='none',
                        glasses_key='none',
                        background_key='none',
                        accessory_key='none'
                    )
                    db.session.add(equipped)
                    db.session.commit()
            except Exception as avatar_error:
                print(f"Avatar setup error (non-fatal): {avatar_error}")

        return jsonify({
            'success': True,
            'message': 'Welcome back!',
            'redirect': '/student',
            'animal': animal  # Return animal for frontend display
        }), 200

    except Exception as e:
        print(f"Error logging in guest: {e}")
        db.session.rollback()
        return jsonify({'error': 'Login failed. Please try again.'}), 500


@engagement_bp.route('/api/repeat-guest/stats')
def repeat_guest_stats():
    """Get stats for current repeat guest"""
    if 'guest_code' not in session:
        return jsonify({'error': 'Not logged in'}), 401

    try:
        from sqlalchemy import text
        code = session['guest_code']

        # Get stats
        result = db.session.execute(text("""
            SELECT
                total_score,
                quizzes_completed,
                (SELECT COUNT(*) FROM guest_badges WHERE guest_code = :code) as badges_earned
            FROM guest_users
            WHERE guest_code = :code
        """), {"code": code}).fetchone()

        if result:
            return jsonify({
                'total_score': result[0] or 0,
                'quizzes_completed': result[1] or 0,
                'badges_earned': result[2] or 0
            }), 200

        return jsonify({'error': 'Stats not found'}), 404

    except Exception as e:
        print(f"Error getting guest stats: {e}")
        return jsonify({'error': 'Failed to load stats'}), 500


@engagement_bp.route('/api/repeat-guest/convert', methods=['POST'])
def convert_guest_to_full():
    """Convert repeat guest to full account"""
    if 'guest_code' not in session:
        return jsonify({'error': 'Not logged in as guest'}), 401

    try:
        from sqlalchemy import text
        data = request.json

        email = data.get('email', '').strip()
        password = data.get('password', '').strip()
        full_name = data.get('full_name', '').strip()

        # Validation
        if not email or not password or not full_name:
            return jsonify({'error': 'All fields required'}), 400

        if len(password) < 6:
            return jsonify({'error': 'Password must be at least 6 characters'}), 400

        # Check if email already exists
        existing = User.query.filter_by(email=email).first()
        if existing:
            return jsonify({'error': 'Email already registered'}), 400

        guest_code = session['guest_code']

        # Get guest data
        guest_data = db.session.execute(text("""
            SELECT total_score, quizzes_completed
            FROM guest_users
            WHERE guest_code = :code
        """), {"code": guest_code}).fetchone()

        # Create new full user account
        new_user = User(
            email=email,
            full_name=full_name,
            role='student',
            is_approved=True
        )
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.flush()

        # Migrate quiz attempts
        db.session.execute(text("""
            INSERT INTO quiz_attempts (user_id, topic, difficulty, score, total_questions, completed_at)
            SELECT :user_id, topic, difficulty, score, total_questions, completed_at
            FROM guest_quiz_attempts
            WHERE guest_code = :code
        """), {"user_id": new_user.id, "code": guest_code})

        # Migrate badges
        db.session.execute(text("""
            INSERT INTO user_badges (user_id, badge_id, earned_at)
            SELECT :user_id, badge_id, earned_at
            FROM guest_badges
            WHERE guest_code = :code
        """), {"user_id": new_user.id, "code": guest_code})

        # Deactivate guest account
        db.session.execute(
            text("UPDATE guest_users SET is_active = 0 WHERE guest_code = :code"),
            {"code": guest_code}
        )

        db.session.commit()

        # Switch session to full account
        session.clear()
        session['user_id'] = new_user.id
        session['role'] = 'student'

        return jsonify({
            'success': True,
            'message': 'Account upgraded successfully!',
            'redirect': '/student'
        }), 200

    except Exception as e:
        db.session.rollback()
        print(f"Error converting guest account: {e}")
        return jsonify({'error': 'Upgrade failed. Please try again.'}), 500


@engagement_bp.route('/api/guest-leaderboard')
def guest_leaderboard():
    """
    Universal leaderboard showing top 20 guest users across all codes.
    Ranked by total score (sum of all correct answers).
    Public endpoint - no authentication required.
    """
    try:
        from sqlalchemy import text

        # Query to get aggregated stats for each guest_code
        query = text("""
            SELECT
                guest_code,
                COUNT(*) as total_quizzes,
                SUM(score) as total_score,
                SUM(total_questions) as total_questions_attempted,
                ROUND(AVG(CAST(score AS FLOAT) / CAST(total_questions AS FLOAT) * 100), 1) as avg_percentage,
                MIN(completed_at) as first_quiz_date,
                MAX(completed_at) as last_quiz_date
            FROM guest_quiz_attempts
            WHERE guest_code IS NOT NULL
            GROUP BY guest_code
            HAVING COUNT(*) > 0
            ORDER BY total_score DESC
            LIMIT 20
        """)

        results = db.session.execute(query).fetchall()

        leaderboard = []
        for rank, row in enumerate(results, start=1):
            # Generate guest display name from code
            # Uses first 6 characters of code for anonymity
            guest_display = f"Guest-{row.guest_code[:6]}" if len(row.guest_code) > 6 else f"Guest-{row.guest_code}"

            leaderboard.append({
                'rank': rank,
                'guest_code': row.guest_code,  # Full code (not displayed to others)
                'display_name': guest_display,  # Public display name
                'total_quizzes': row.total_quizzes,
                'total_score': row.total_score,
                'total_questions': row.total_questions_attempted,
                'avg_percentage': float(row.avg_percentage) if row.avg_percentage else 0.0,
                'first_quiz': row.first_quiz_date[:10] if row.first_quiz_date else None,  # Extract date part from string
                'last_quiz': row.last_quiz_date[:10] if row.last_quiz_date else None  # Extract date part from string
            })

        return jsonify({
            'success': True,
            'leaderboard': leaderboard,
            'total_guests': len(leaderboard)
        })

    except Exception as e:
        print(f"❌ Error fetching guest leaderboard: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Unable to load leaderboard',
            'leaderboard': []
        }), 500


def cleanup_inactive_guests(days=30):
    """
    Delete guest accounts that haven't been used in X days
    Returns number of deleted accounts
    """
    from sqlalchemy import text
    cutoff_date = datetime.utcnow() - timedelta(days=days)

    result = db.session.execute(text("""
        DELETE FROM guest_users
        WHERE last_active < :cutoff AND is_active = 1
    """), {"cutoff": cutoff_date})

    db.session.commit()
    return result.rowcount




# ==================== WHO'S ONLINE COUNTER ====================

@engagement_bp.route('/api/online-count')
def get_online_count():
    """Get count of users active in the last 5 minutes"""
    from sqlalchemy import text
    from datetime import datetime, timedelta
    
    try:
        five_minutes_ago = datetime.utcnow() - timedelta(minutes=5)
        
        # Count registered users active recently
        registered_count = 0
        try:
            result = db.session.execute(text("""
                SELECT COUNT(DISTINCT user_id) FROM quiz_attempts 
                WHERE created_at > :since
            """), {'since': five_minutes_ago}).fetchone()
            registered_count = result[0] if result else 0
        except:
            pass
        
        # Count guest users active recently
        guest_count = 0
        try:
            result = db.session.execute(text("""
                SELECT COUNT(*) FROM guest_users 
                WHERE last_active > :since
            """), {'since': five_minutes_ago}).fetchone()
            guest_count = result[0] if result else 0
        except:
            pass
        
        total_online = registered_count + guest_count
        
        # Add some variability/minimum to make it look active
        # During low activity, show at least 1 (the current user)
        if total_online == 0:
            total_online = 1
        
        return jsonify({
            'count': total_online,
            'online_count': total_online,
            'registered': registered_count,
            'guests': guest_count
        })
        
    except Exception as e:
        print(f"Error getting online count: {e}")
        return jsonify({'count': 1, 'online_count': 1})


# ==================== DAY 2: QUICK PLAY API ====================

@engagement_bp.route('/api/quick-play/<difficulty>')
@login_required
def get_quick_play_questions(difficulty):
    """Get 10 random questions from Junior Cycle topics only for Quick Play mode"""
    from sqlalchemy import text
    
    try:
        # Get 10 random questions from Junior Cycle strands only
        # Exclude any strand containing 'Senior' in the name
        result = db.session.execute(text("""
            SELECT q.id, q.question_text, q.option_a, q.option_b, q.option_c, q.option_d,
                   q.correct_answer, q.explanation, q.hint_text, q.topic, q.difficulty,
                   q.image_url, q.image_caption, q.strand
            FROM questions q
            WHERE LOWER(q.difficulty) = LOWER(:difficulty)
            AND (q.strand IS NULL OR LOWER(q.strand) NOT LIKE '%senior%')
            ORDER BY RANDOM()
            LIMIT 10
        """), {'difficulty': difficulty}).fetchall()
        
        questions = []
        for row in result:
            questions.append({
                'id': row.id,
                'question': row.question_text,
                'options': [row.option_a, row.option_b, row.option_c, row.option_d],
                'correct': row.correct_answer,
                'explanation': row.explanation,
                'hint': row.hint_text,
                'topic': row.topic,
                'difficulty': row.difficulty,
                'image_url': row.image_url,
                'image_caption': row.image_caption
            })
        
        return jsonify(questions)
        
    except Exception as e:
        print(f"Quick Play error: {e}")
        return jsonify([]), 500


# ==================== DAY 2: WEEKLY CHALLENGE API ====================

@engagement_bp.route('/api/weekly-challenge/status')
@login_required
def get_weekly_challenge_status():
    """Get user's weekly challenge progress"""
    from sqlalchemy import text
    from datetime import datetime, timedelta
    
    guest_code = session.get('guest_code')
    user_id = session.get('user_id')
    
    # Get start of current week (Monday)
    today = datetime.utcnow().date()
    start_of_week = today - timedelta(days=today.weekday())
    
    try:
        # Count quizzes this week
        if guest_code:
            quiz_count = db.session.execute(text("""
                SELECT COUNT(*) FROM guest_quiz_attempts
                WHERE guest_code = :code AND DATE(completed_at) >= :start
            """), {'code': guest_code, 'start': start_of_week}).fetchone()[0]
            
            high_score_count = db.session.execute(text("""
                SELECT COUNT(*) FROM guest_quiz_attempts
                WHERE guest_code = :code AND DATE(completed_at) >= :start AND percentage >= 80
            """), {'code': guest_code, 'start': start_of_week}).fetchone()[0]
        else:
            quiz_count = db.session.execute(text("""
                SELECT COUNT(*) FROM quiz_attempts
                WHERE user_id = :uid AND DATE(created_at) >= :start
            """), {'uid': user_id, 'start': start_of_week}).fetchone()[0]
            
            high_score_count = db.session.execute(text("""
                SELECT COUNT(*) FROM quiz_attempts
                WHERE user_id = :uid AND DATE(created_at) >= :start AND percentage >= 80
            """), {'uid': user_id, 'start': start_of_week}).fetchone()[0]
        
        # For streak, we'd need to track max streak per quiz - simplified for now
        max_streak = 0
        
        return jsonify({
            'challenge': {
                'goals': [
                    {'id': 'goal1', 'target': 5, 'current': quiz_count, 'points': 50, 'type': 'quizzes'},
                    {'id': 'goal2', 'target': 3, 'current': high_score_count, 'points': 75, 'type': 'highscores'},
                    {'id': 'goal3', 'target': 5, 'current': max_streak, 'points': 100, 'type': 'streak'}
                ]
            },
            'week_start': start_of_week.isoformat()
        })
        
    except Exception as e:
        print(f"Weekly challenge error: {e}")
        return jsonify({'challenge': None, 'error': str(e)})


@engagement_bp.route('/api/weekly-challenge/update', methods=['POST'])
@login_required
def update_weekly_challenge():
    """Update weekly challenge progress (called after quiz completion)"""
    # Progress is tracked via quiz_attempts, so this is mainly for acknowledgment
    return jsonify({'success': True})


# ==================== DAY 2: ENHANCED LEADERBOARD API ====================

@engagement_bp.route('/api/leaderboard/<period>')
@login_required
def get_leaderboard(period):
    """Get leaderboard - weekly or all-time, includes user position even if not in top 20"""
    from sqlalchemy import text
    from datetime import datetime, timedelta
    
    current_guest = session.get('guest_code')
    
    try:
        if period == 'weekly':
            # Get start of current week
            today = datetime.utcnow().date()
            start_of_week = today - timedelta(days=today.weekday())
            
            # Weekly leaderboard from guest_quiz_attempts - top 20
            result = db.session.execute(text("""
                SELECT guest_code, SUM(score) as total_score,
                       COUNT(*) as quiz_count
                FROM guest_quiz_attempts
                WHERE DATE(completed_at) >= :start
                GROUP BY guest_code
                ORDER BY total_score DESC
                LIMIT 20
            """), {'start': start_of_week}).fetchall()
            
            # Get current user's position if not in top 20
            user_position = None
            user_score = None
            if current_guest:
                # Get user's rank
                rank_result = db.session.execute(text("""
                    SELECT COUNT(*) + 1 as rank, 
                           (SELECT SUM(score) FROM guest_quiz_attempts 
                            WHERE guest_code = :code AND DATE(completed_at) >= :start) as my_score
                    FROM (
                        SELECT guest_code, SUM(score) as total_score
                        FROM guest_quiz_attempts
                        WHERE DATE(completed_at) >= :start
                        GROUP BY guest_code
                    ) rankings
                    WHERE total_score > COALESCE(
                        (SELECT SUM(score) FROM guest_quiz_attempts 
                         WHERE guest_code = :code AND DATE(completed_at) >= :start), 0
                    )
                """), {'code': current_guest, 'start': start_of_week}).fetchone()
                if rank_result:
                    user_position = rank_result.rank
                    user_score = rank_result.my_score or 0
            
        else:  # all-time
            # All-time leaderboard from guest_users - top 20
            result = db.session.execute(text("""
                SELECT guest_code, total_score, quizzes_completed as quiz_count
                FROM guest_users
                WHERE is_active = 1
                ORDER BY total_score DESC
                LIMIT 20
            """)).fetchall()
            
            # Get current user's position if not in top 20
            user_position = None
            user_score = None
            if current_guest:
                rank_result = db.session.execute(text("""
                    SELECT COUNT(*) + 1 as rank,
                           (SELECT total_score FROM guest_users WHERE guest_code = :code) as my_score
                    FROM guest_users
                    WHERE is_active = 1 
                    AND total_score > COALESCE(
                        (SELECT total_score FROM guest_users WHERE guest_code = :code), 0
                    )
                """), {'code': current_guest}).fetchone()
                if rank_result:
                    user_position = rank_result.rank
                    user_score = rank_result.my_score or 0
        
        leaderboard = []
        user_in_top20 = False
        
        for row in result:
            is_current = row.guest_code == current_guest
            if is_current:
                user_in_top20 = True
            leaderboard.append({
                'guest_code': row.guest_code,
                'name': row.guest_code.capitalize() if row.guest_code else 'Anonymous',
                'total_score': row.total_score or 0,
                'points': row.total_score or 0,
                'quiz_count': row.quiz_count or 0,
                'is_current_user': is_current
            })
        
        # Build response
        response_data = {
            'leaderboard': leaderboard,
            'period': period
        }
        
        # Add user position if not in top 20
        if current_guest and not user_in_top20 and user_position:
            response_data['my_position'] = {
                'rank': user_position,
                'guest_code': current_guest,
                'name': current_guest.capitalize(),
                'points': user_score,
                'is_current_user': True
            }
        
        return jsonify(response_data)
        
    except Exception as e:
        print(f"Leaderboard error: {e}")
        return jsonify({'leaderboard': [], 'error': str(e)})




# =============================================================================
# PUZZLE HELPER FUNCTIONS
# =============================================================================

def get_current_week_year():
    """Get the current ISO week number and year"""
    from datetime import datetime
    now = datetime.now()
    week_number = now.isocalendar()[1]
    year = now.isocalendar()[0]
    return week_number, year


def get_active_puzzle():
    """Get the currently active puzzle for this week"""
    from models import WeeklyPuzzle
    
    week_number, year = get_current_week_year()
    
    # First try to find active puzzle for current week
    puzzle = WeeklyPuzzle.query.filter_by(
        week_number=week_number,
        year=year,
        is_active=True
    ).first()
    
    if puzzle:
        return puzzle
    
    # If no current week puzzle, find any active puzzle
    return WeeklyPuzzle.query.filter_by(is_active=True).first()


def get_user_puzzle_status(puzzle_id, user_id=None, guest_code=None, session_id=None):
    """Get or create a puzzle status record for a user"""
    from models import db, PuzzleUserStatus
    from sqlalchemy import text
    
    if not any([user_id, guest_code, session_id]):
        return None
    
    # Try to find existing status
    if user_id:
        status = PuzzleUserStatus.query.filter_by(puzzle_id=puzzle_id, user_id=user_id).first()
    elif guest_code:
        status = PuzzleUserStatus.query.filter_by(puzzle_id=puzzle_id, guest_code=guest_code).first()
    elif session_id:
        status = PuzzleUserStatus.query.filter_by(puzzle_id=puzzle_id, session_id=session_id).first()
    else:
        status = None
    
    # Create if not exists
    if not status:
        try:
            status = PuzzleUserStatus(
                puzzle_id=puzzle_id,
                user_id=user_id,
                guest_code=guest_code,
                session_id=session_id
            )
            db.session.add(status)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error creating puzzle status: {e}")
            return None
    
    return status


# =============================================================================
# PUZZLE OF THE WEEK - STUDENT/USER API ROUTES
# =============================================================================

@engagement_bp.route('/api/puzzle/current')
def get_current_puzzle():
    """Get the current week's active puzzle"""
    puzzle = get_active_puzzle()
    
    if not puzzle:
        return jsonify({'puzzle': None, 'message': 'No active puzzle this week'})
    
    # Increment view count
    puzzle.view_count += 1
    db.session.commit()
    
    return jsonify({
        'puzzle': puzzle.to_dict(include_answer=False),
        'week': puzzle.week_number,
        'year': puzzle.year
    })


@engagement_bp.route('/api/puzzle/status')
def get_puzzle_status():
    """Check user's puzzle status - should they see popup? Can reveal answer?"""
    puzzle = get_active_puzzle()
    
    if not puzzle:
        return jsonify({
            'has_puzzle': False,
            'show_popup': False,
            'can_reveal_answer': False
        })
    
    # Determine user identity
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    session_id = session.get('session_id', request.cookies.get('session_id'))
    
    # Get or create status
    status = get_user_puzzle_status(
        puzzle.id,
        user_id=user_id,
        guest_code=guest_code,
        session_id=session_id
    )
    
    if not status:
        # No way to track this user, show puzzle anyway
        return jsonify({
            'has_puzzle': True,
            'show_popup': True,
            'can_reveal_answer': True,
            'already_revealed': False,
            'hint_available': bool(puzzle.hint),
            'puzzle': puzzle.to_dict(include_answer=False)
        })
    
    return jsonify({
        'has_puzzle': True,
        'show_popup': not status.dismissed_popup,
        'can_reveal_answer': not status.dismissed_answer,
        'already_revealed': status.revealed_answer,
        'hint_viewed': status.hint_viewed,
        'hint_available': bool(puzzle.hint),
        'puzzle': puzzle.to_dict(include_answer=status.revealed_answer)
    })


@engagement_bp.route('/api/puzzle/dismiss-popup', methods=['POST'])
def dismiss_puzzle_popup():
    """User dismisses the puzzle splash popup for this week"""
    puzzle = get_active_puzzle()
    if not puzzle:
        return jsonify({'success': False, 'error': 'No active puzzle'})
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    session_id = session.get('session_id', request.cookies.get('session_id'))
    
    status = get_user_puzzle_status(
        puzzle.id,
        user_id=user_id,
        guest_code=guest_code,
        session_id=session_id
    )
    
    if status:
        status.dismissed_popup = True
        db.session.commit()
    
    return jsonify({'success': True})


@engagement_bp.route('/api/puzzle/dismiss-answer', methods=['POST'])
def dismiss_puzzle_answer():
    """User declines to ever see the answer this week"""
    puzzle = get_active_puzzle()
    if not puzzle:
        return jsonify({'success': False, 'error': 'No active puzzle'})
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    session_id = session.get('session_id', request.cookies.get('session_id'))
    
    status = get_user_puzzle_status(
        puzzle.id,
        user_id=user_id,
        guest_code=guest_code,
        session_id=session_id
    )
    
    if status:
        status.dismissed_answer = True
        db.session.commit()
    
    return jsonify({'success': True})


@engagement_bp.route('/api/puzzle/reveal-answer', methods=['POST'])
def reveal_puzzle_answer():
    """User requests to see the puzzle answer"""
    puzzle = get_active_puzzle()
    if not puzzle:
        return jsonify({'success': False, 'error': 'No active puzzle'})
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    session_id = session.get('session_id', request.cookies.get('session_id'))
    
    status = get_user_puzzle_status(
        puzzle.id,
        user_id=user_id,
        guest_code=guest_code,
        session_id=session_id
    )
    
    if status:
        status.revealed_answer = True
        status.answer_revealed_at = datetime.utcnow()
        status.dismissed_answer = True  # Don't offer again
        db.session.commit()
    
    # Increment puzzle reveal count
    puzzle.reveal_count += 1
    db.session.commit()
    
    return jsonify({
        'success': True,
        'answer_image': puzzle.answer_image,
        'answer_text': puzzle.answer_text
    })


@engagement_bp.route('/api/puzzle/view-hint', methods=['POST'])
def view_puzzle_hint():
    """User views the puzzle hint"""
    puzzle = get_active_puzzle()
    if not puzzle or not puzzle.hint:
        return jsonify({'success': False, 'error': 'No hint available'})
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    session_id = session.get('session_id', request.cookies.get('session_id'))
    
    status = get_user_puzzle_status(
        puzzle.id,
        user_id=user_id,
        guest_code=guest_code,
        session_id=session_id
    )
    
    if status:
        status.hint_viewed = True
        db.session.commit()
    
    # Increment puzzle hint view count
    puzzle.hint_view_count += 1
    db.session.commit()
    
    return jsonify({
        'success': True,
        'hint': puzzle.hint
    })


# ==================== USER FEEDBACK ====================

@engagement_bp.route('/api/submit-feedback', methods=['POST'])
@guest_or_login_required
def submit_feedback():
    """Submit user feedback from student app"""
    
    data = request.json
    
    # Validate required field
    if not data or not data.get('feedback_text', '').strip():
        return jsonify({'error': 'Feedback text is required'}), 400
    
    feedback_text = data.get('feedback_text', '').strip()
    
    # Limit feedback length
    if len(feedback_text) > 5000:
        return jsonify({'error': 'Feedback too long (max 5000 characters)'}), 400
    
    # Get user info
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    user_name = None
    user_email = None
    
    if user_id:
        user = User.query.get(user_id)
        if user:
            user_name = user.full_name
            user_email = user.email
    elif guest_code:
        user_name = f"Guest ({guest_code})"
    
    # Get optional fields
    category = data.get('category', 'general')
    valid_categories = ['general', 'bug', 'feature', 'content', 'ui', 'other']
    if category not in valid_categories:
        category = 'general'
    
    rating = data.get('rating')
    if rating is not None:
        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                rating = None
        except (ValueError, TypeError):
            rating = None
    
    page_context = data.get('page_context', '')[:255] if data.get('page_context') else None
    topic_context = data.get('topic_context', '')[:255] if data.get('topic_context') else None
    
    try:
        # Ensure table exists
        db.session.execute(text("""
            CREATE TABLE IF NOT EXISTS user_feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                user_name VARCHAR(100),
                user_email VARCHAR(255),
                feedback_text TEXT NOT NULL,
                category VARCHAR(50) DEFAULT 'general',
                rating INTEGER,
                status VARCHAR(20) DEFAULT 'new',
                page_context VARCHAR(255),
                topic_context VARCHAR(255),
                admin_notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """))
        
        # Insert feedback
        db.session.execute(text("""
            INSERT INTO user_feedback (
                user_id, user_name, user_email, feedback_text,
                category, rating, status, page_context, topic_context
            ) VALUES (
                :user_id, :user_name, :user_email, :feedback_text,
                :category, :rating, 'new', :page_context, :topic_context
            )
        """), {
            'user_id': user_id,
            'user_name': user_name,
            'user_email': user_email,
            'feedback_text': feedback_text,
            'category': category,
            'rating': rating,
            'page_context': page_context,
            'topic_context': topic_context
        })
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Thank you for your feedback!'
        })
        
    except Exception as e:
        db.session.rollback()
        print(f"Error submitting feedback: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': 'Failed to submit feedback'}), 500


@engagement_bp.route('/api/my-feedback')
@guest_or_login_required
def get_my_feedback():
    """Get current user's submitted feedback"""
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'feedback': []})
    
    try:
        # Check if table exists
        table_check = db.session.execute(text("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='user_feedback'
        """)).fetchone()
        
        if not table_check:
            return jsonify({'feedback': []})
        
        if user_id:
            results = db.session.execute(text("""
                SELECT id, feedback_text, category, rating, status, created_at
                FROM user_feedback 
                WHERE user_id = :user_id
                ORDER BY created_at DESC
                LIMIT 20
            """), {'user_id': user_id}).fetchall()
        else:
            # For guests, match by name pattern
            results = db.session.execute(text("""
                SELECT id, feedback_text, category, rating, status, created_at
                FROM user_feedback 
                WHERE user_name LIKE :guest_pattern
                ORDER BY created_at DESC
                LIMIT 20
            """), {'guest_pattern': f'%{guest_code}%'}).fetchall()
        
        feedback_list = [{
            'id': r[0],
            'feedback_text': r[1][:100] + '...' if len(r[1]) > 100 else r[1],
            'category': r[2],
            'rating': r[3],
            'status': r[4],
            'created_at': r[5].isoformat() if r[5] else None
        } for r in results]
        
        return jsonify({'feedback': feedback_list})
        
    except Exception as e:
        print(f"Error getting my feedback: {e}")
        return jsonify({'feedback': []})






