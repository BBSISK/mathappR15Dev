# New Development note being added
# Project MathappDevelpoment 2026
# app.py
# AgentMath Main Flask Application
# Revision 2.9.2 - 2025-12-31 - Feature flags fix
# 
# Fixes in this revision:
# - Added app.config['FEATURE_FLAGS'] = FEATURE_FLAGS so blueprints can access flags
# - This fixes Avatar and Prize buttons not working (they couldn't read feature flags)
#
# Revision 2.9.1 - Bug fixes from automated testing:
# - Fixed topics query in /api/init to use correct schema (display_name, strand join)
# - Fixed quiz_attempts queries to use completed_at instead of created_at
# - Added proper input validation to /api/create-quiz-attempt
#
# Previous: Revision 2.9.0 - Student features extracted to routes/student_features.py

from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash, send_from_directory
from functools import wraps
from datetime import datetime, timedelta, date
import os
import random
import re
import uuid
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import json

# Import database and all models from models.py
from models import (
    db,
    User, Class, ClassEnrollment,
    Question, QuestionFlag, AdaptiveQuestionFlag, QuestionEdit,
    QuizAttempt, Badge, UserBadge, UserStats, TopicProgress,
    AvatarItem, UserAvatarInventory, UserAvatarEquipped, AvatarPurchaseLog,
    SystemSetting, PrizeSchool, Prize, SchoolPrize, PrizeRedemption, SchoolRequest, RaffleDraw,
    TeacherDomainAccess, DomainAccessRequest,
    WeeklyPuzzle, PuzzleUserStatus,
    BonusQuestion, BonusQuestionAttempt,
    UserQuestionHistory, UserAdaptiveQuestionHistory
)

# Import utility functions from utils/
from utils import (
    # Authentication decorators
    login_required, role_required, approved_required, guest_or_login_required,
    # Avatar helpers
    get_avatar_user_points, avatar_owns_item, get_equipped_avatar,
    grant_default_avatar_items, get_animal_from_guest_code,
    # Badge helpers
    initialize_user_stats, update_user_stats_after_quiz,
    update_topic_progress, check_and_award_badges,
    # Domain helpers
    extract_domain, get_all_domains_in_system, teacher_has_domain_access,
    get_teacher_accessible_domains, filter_students_by_domain_access,
    get_teacher_domain_statistics
)


# Import route blueprints
from routes import register_blueprints



# Import Irish school calendar for streak tracking
try:
    from irish_school_calendar import (
        is_school_day, is_consecutive_school_day, should_reset_streak,
        get_streak_milestone, get_next_milestone, STREAK_MILESTONES
    )
    IRISH_CALENDAR_ENABLED = True
except ImportError:
    IRISH_CALENDAR_ENABLED = False
    print("Warning: irish_school_calendar.py not found - using simple streak logic")

# Import Adaptive Learning System
try:
    from adaptive_learning_routes import register_adaptive_routes, update_adaptive_after_quiz
    ADAPTIVE_LEARNING_AVAILABLE = True
except ImportError:
    ADAPTIVE_LEARNING_AVAILABLE = False
    print("Note: Adaptive Learning System not available")

# Import Adaptive Question System (parallel system with _adaptive suffix)
try:
    from question_generator_adaptive import register_adaptive_generator_routes
    ADAPTIVE_GENERATOR_AVAILABLE = True
except ImportError:
    ADAPTIVE_GENERATOR_AVAILABLE = False
    print("Note: Adaptive Question Generator not available")

try:
    from adaptive_quiz_engine import register_adaptive_quiz_routes
    ADAPTIVE_QUIZ_ENGINE_AVAILABLE = True
except ImportError:
    ADAPTIVE_QUIZ_ENGINE_AVAILABLE = False
    print("Note: Adaptive Quiz Engine not available")

# Import Team Play System
try:
    from team_play_routes import register_team_play_routes
    TEAM_PLAY_AVAILABLE = True
except ImportError:
    TEAM_PLAY_AVAILABLE = False
    print("Note: Team Play System not available")

app = Flask(__name__)

# ==================== FEATURE FLAGS ====================
# Avatar system can be disabled instantly by setting these to False
# Set via environment variables or change defaults here
FEATURE_FLAGS = {
    'AVATAR_SYSTEM_ENABLED': os.environ.get('AVATAR_SYSTEM_ENABLED', 'true').lower() == 'true',
    'AVATAR_SHOP_ENABLED': os.environ.get('AVATAR_SHOP_ENABLED', 'false').lower() == 'true',
    'AVATAR_ON_QUIZ_ENABLED': os.environ.get('AVATAR_ON_QUIZ_ENABLED', 'false').lower() == 'true',
    'AVATAR_ON_LEADERBOARD_ENABLED': os.environ.get('AVATAR_ON_LEADERBOARD_ENABLED', 'false').lower() == 'true',
    'PRIZE_SYSTEM_ENABLED': os.environ.get('PRIZE_SYSTEM_ENABLED', 'true').lower() == 'true',
}

def get_feature_flag(flag_name):
    """Get a feature flag value"""
    return FEATURE_FLAGS.get(flag_name, False)
# ==================== FALLBACK TOPIC CONFIGURATION ====================
# FALLBACK ONLY - Primary source is the `topics` database table
# This list is used ONLY when database is unavailable
# To add new topics, use Admin Dashboard > Topic Management
FALLBACK_TOPICS = [
    # Number Strand
    'arithmetic', 'fractions', 'decimals', 'multiplication_division',
    'number_systems', 'bodmas', 'sets', 'surds',

    # Algebra and Functions Strand
    'introductory_algebra', 'functions', 'patterns', 'solving_equations',
    'simplifying_expressions', 'expanding_factorising',
    'complex_numbers_intro', 'complex_numbers_expanded', 'simultaneous_equations',

    # Geometry and Trigonometry Strand
    'coordinate_geometry', 'trigonometry',

    # Statistics and Probability Strand
    'probability', 'descriptive_statistics',
]

VALID_DIFFICULTIES = ['beginner', 'intermediate', 'advanced']

# Cache for database topics (refreshed periodically)
_topics_cache = {'topics': None, 'timestamp': None}
_CACHE_DURATION_SECONDS = 300  # 5 minutes

def get_valid_topics_from_db():
    """
    Get valid topics from the database `topics` table.
    Returns list of topic_id strings that are visible.
    Falls back to FALLBACK_TOPICS if database unavailable.

    This is the SINGLE SOURCE OF TRUTH for topic validation.
    When you add a topic via Admin Dashboard, it automatically becomes valid everywhere.
    """
    import time
    from sqlalchemy import text

    # Check cache first
    current_time = time.time()
    if (_topics_cache['topics'] is not None and
        _topics_cache['timestamp'] is not None and
        current_time - _topics_cache['timestamp'] < _CACHE_DURATION_SECONDS):
        return _topics_cache['topics']

    try:
        # Query visible topics from database
        result = db.session.execute(text(
            "SELECT topic_id FROM topics WHERE is_visible = 1"
        )).fetchall()

        if result:
            topics = [row[0] for row in result]
            # Update cache
            _topics_cache['topics'] = topics
            _topics_cache['timestamp'] = current_time
            return topics
        else:
            # No topics in database, use fallback
            return FALLBACK_TOPICS

    except Exception as e:
        # Database error, use fallback
        print(f"Warning: Could not load topics from database: {e}")
        return FALLBACK_TOPICS

def invalidate_topics_cache():
    """Call this after adding/removing topics via admin to refresh cache immediately"""
    _topics_cache['topics'] = None
    _topics_cache['timestamp'] = None


app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-change-this-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mathquiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Session configuration for guest mode
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_COOKIE_SECURE'] = False  # Set to True in production with HTTPS
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# Make feature flags available to blueprints via app.config
app.config['FEATURE_FLAGS'] = FEATURE_FLAGS

# ==================== EMAIL CONFIGURATION (Gmail SMTP) ====================
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'barry.b.sisk@gmail.com'
app.config['MAIL_PASSWORD'] = 'uutfogzyhoyepzis'
app.config['MAIL_DEFAULT_SENDER'] = ('AgentMath', 'barry.b.sisk@gmail.com')


# ==================== WHO AM I CONFIGURATION ====================
UPLOAD_FOLDER = 'static/who_am_i_images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Initialize database with Flask app
db.init_app(app)

# Register route blueprints (auth, pwa)
register_blueprints(app)



# ==================== TEMPLATE CONTEXT PROCESSOR ====================
@app.context_processor
def inject_feature_flags():
    """Make feature flags available in all templates"""
    return {
        'feature_flags': FEATURE_FLAGS,
        'avatar_enabled': FEATURE_FLAGS.get('AVATAR_SYSTEM_ENABLED', False)
    }
# ==================== SESSION SECURITY ====================
@app.after_request
def add_no_cache_headers(response):
    """Add no-cache headers to authenticated pages to prevent back-button session resumption"""
    # Only add headers to HTML responses (not API calls or static files)
    if 'text/html' in response.content_type:
        # Check if this is an authenticated route (has user_id in session)
        if 'user_id' in session or 'is_guest' in session:
            response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
            response.headers['Pragma'] = 'no-cache'
            response.headers['Expires'] = '0'
    return response



# ==================== ROUTES ====================

def generate_options_for_answer(correct_answer, count=4, range_size=10, allow_negative=False):
    """
    Helper function to generate multiple choice options

    Args:
        correct_answer: The correct answer
        count: Number of options to generate (default 4)
        range_size: Range for generating wrong answers
        allow_negative: Whether to allow negative wrong answers

    Returns:
        List of options shuffled with correct answer included
    """
    options = [correct_answer]

    # Generate wrong answers
    attempts = 0
    max_attempts = 100

    while len(options) < count and attempts < max_attempts:
        attempts += 1

        # Create wrong answer within range
        offset = random.randint(-range_size, range_size)
        if offset == 0:
            offset = random.choice([-1, 1]) * random.randint(1, range_size)

        wrong_answer = correct_answer + offset

        # Apply negative restriction if needed
        if not allow_negative and wrong_answer < 0:
            wrong_answer = abs(wrong_answer)

        # Ensure unique and not zero (unless correct answer is zero)
        if wrong_answer not in options and (wrong_answer != 0 or correct_answer == 0):
            options.append(wrong_answer)

    # If we couldn't generate enough unique options, add some calculated ones
    while len(options) < count:
        # Generate wrong answers based on common mistakes
        if correct_answer > 0:
            wrong = correct_answer + random.choice([1, -1, 2, -2, 5, -5, 10, -10])
        else:
            wrong = correct_answer + random.choice([1, -1, 2, -2])

        if wrong not in options:
            options.append(wrong)

    # Shuffle so correct answer isn't always first
    random.shuffle(options)

    return options


def generate_multiplication_division_beginner():
    """
    Generate beginner level multiplication and division questions
    - Single digit × single digit (2 × 3 = ?)
    - Simple division with no remainders (6 ÷ 2 = ?)
    - NO NEGATIVE NUMBERS
    """
    operation = random.choice(['multiply', 'divide'])

    if operation == 'multiply':
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        answer = a * b
        question = f"{a} × {b}"
    else:  # divide
        divisor = random.randint(1, 10)
        quotient = random.randint(1, 10)
        dividend = divisor * quotient
        answer = quotient
        question = f"{dividend} ÷ {divisor}"

    options = generate_options_for_answer(answer, count=4, range_size=10)

    return {
        'question': question,
        'answer': answer,
        'options': options,
        'explanation': f"The correct answer is {answer}"
    }


def generate_multiplication_division_intermediate():
    """
    Generate intermediate level multiplication and division questions
    - INCLUDES SINGLE NEGATIVE NUMBERS with low value integers
    """
    operation = random.choice(['multiply', 'divide'])
    include_negative = random.choice([True, False])

    if operation == 'multiply':
        if include_negative:
            a = random.choice(list(range(-10, 0)) + list(range(1, 11)))
            b = random.choice(list(range(-10, 0)) + list(range(1, 11)))

            # Ensure only ONE is negative
            if a < 0 and b < 0:
                b = abs(b)
            elif a > 0 and b > 0:
                if random.choice([True, False]):
                    a = -a
                else:
                    b = -b
        else:
            a = random.randint(10, 25)
            b = random.randint(2, 12)

        answer = a * b
        question = f"{a} × {b}"
    else:  # divide
        if include_negative:
            divisor = random.choice(list(range(-10, 0)) + list(range(2, 11)))
            quotient = random.choice(list(range(-10, 0)) + list(range(1, 11)))

            # Ensure only ONE is negative
            if divisor < 0 and quotient < 0:
                quotient = abs(quotient)
            elif divisor > 0 and quotient > 0:
                if random.choice([True, False]):
                    divisor = -divisor
                else:
                    quotient = -quotient

            dividend = divisor * quotient
            answer = quotient
        else:
            divisor = random.randint(2, 12)
            quotient = random.randint(10, 50)
            dividend = divisor * quotient
            answer = quotient

        question = f"{dividend} ÷ {divisor}"

    options = generate_options_for_answer(answer, count=4, range_size=20, allow_negative=True)

    return {
        'question': question,
        'answer': answer,
        'options': options,
        'explanation': f"The correct answer is {answer}"
    }


def generate_multiplication_division_advanced():
    """
    Generate advanced level multiplication and division questions
    - DOUBLE NEGATIVE CALCULATIONS
    - THREE DIGIT COMPUTATIONS
    """
    operation = random.choice(['multiply', 'divide', 'mixed', 'three_digit'])

    if operation == 'multiply':
        neg_type = random.choices(['double_neg', 'single_neg', 'positive'], weights=[0.4, 0.4, 0.2])[0]

        if neg_type == 'double_neg':
            a = random.randint(-50, -10)
            b = random.randint(-20, -2)
            answer = a * b
            question = f"({a}) × ({b})"
        elif neg_type == 'single_neg':
            a = random.randint(10, 50)
            b = random.randint(2, 25)
            if random.choice([True, False]):
                a = -a
            else:
                b = -b
            answer = a * b
            question = f"{a} × {b}"
        else:
            a = random.randint(20, 99)
            b = random.randint(11, 25)
            answer = a * b
            question = f"{a} × {b}"

    elif operation == 'divide':
        neg_type = random.choices(['double_neg', 'single_neg', 'positive'], weights=[0.4, 0.4, 0.2])[0]

        if neg_type == 'double_neg':
            divisor = random.randint(-25, -2)
            quotient = random.randint(-50, -5)
            dividend = divisor * quotient
            answer = quotient
            question = f"({dividend}) ÷ ({divisor})"
        elif neg_type == 'single_neg':
            divisor = random.randint(2, 25)
            quotient = random.randint(5, 50)
            if random.choice([True, False]):
                divisor = -divisor
            else:
                quotient = -quotient
            dividend = divisor * quotient
            answer = quotient
            question = f"{dividend} ÷ {divisor}"
        else:
            divisor = random.randint(11, 25)
            quotient = random.randint(20, 100)
            dividend = divisor * quotient
            answer = quotient
            question = f"{dividend} ÷ {divisor}"

    elif operation == 'mixed':
        mix_type = random.choice(['mult_then_div', 'div_then_mult'])

        if mix_type == 'mult_then_div':
            a = random.randint(-30, 30)
            if a == 0:
                a = random.choice([-15, 15])
            b = random.randint(2, 10)
            c = random.randint(-10, 10)
            if c == 0:
                c = random.choice([-5, 5])

            temp = a * b
            if temp % c != 0:
                quotient = temp // c
                temp = quotient * c
                a = temp // b

            answer = (a * b) // c
            a_str = f"({a})" if a < 0 else str(a)
            b_str = f"({b})" if b < 0 else str(b)
            c_str = f"({c})" if c < 0 else str(c)
            question = f"({a_str} × {b_str}) ÷ {c_str}"
        else:
            a = random.randint(-100, 100)
            if a == 0:
                a = random.choice([-48, 48])
            b = random.randint(-10, 10)
            if b == 0:
                b = random.choice([-6, 6])
            quotient = random.randint(-20, 20)
            if quotient == 0:
                quotient = random.choice([-8, 8])
            a = quotient * b
            c = random.randint(-10, 10)
            if c == 0:
                c = random.choice([-3, 3])

            answer = (a // b) * c
            a_str = f"({a})" if a < 0 else str(a)
            b_str = f"({b})" if b < 0 else str(b)
            c_str = f"({c})" if c < 0 else str(c)
            question = f"({a_str} ÷ {b_str}) × {c_str}"

    else:  # three_digit
        sub_type = random.choice(['mult_3digit', 'div_3digit'])

        if sub_type == 'mult_3digit':
            a = random.randint(100, 999)
            b = random.randint(10, 99)
            answer = a * b
            question = f"{a} × {b}"
        else:
            divisor = random.randint(10, 99)
            quotient = random.randint(10, 99)
            dividend = divisor * quotient
            answer = quotient
            question = f"{dividend} ÷ {divisor}"

    options = generate_options_for_answer(answer, count=4, range_size=50, allow_negative=True)

    return {
        'question': question,
        'answer': answer,
        'options': options,
        'explanation': f"The correct answer is {answer}"
    }

# ==================== AUTHENTICATION ROUTES ====================

@app.route('/')
def index():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user:
            if user.role == 'admin':
                return redirect(url_for('admin.admin_dashboard'))
            elif user.role == 'teacher':
                if not user.is_approved:
                    return render_template('pending_approval.html')
                return redirect(url_for('teacher.teacher_dashboard'))
            else:
                return render_template('student_app.html')

    # Check if full account login is enabled (default: False for GDPR)
    full_account_enabled = SystemSetting.get('FULL_ACCOUNT_LOGIN_ENABLED', False)
    # Convert string 'true'/'false' to boolean if needed
    if isinstance(full_account_enabled, str):
        full_account_enabled = full_account_enabled.lower() == 'true'

    return render_template('login.html', full_account_enabled=full_account_enabled)

# ==================== FIXED GUEST ROUTES ====================
# REPLACE your existing guest routes (lines ~1185-1208) with these:

@app.route('/api/guest-start', methods=['POST'])
def guest_start():
    """Initialize guest session with proper user_id"""
    import uuid

    try:
        session.clear()

        # Get or create the guest user in database
        guest_user = User.query.filter_by(email='guest@agentmath.app').first()

        if not guest_user:
            # Create guest user if it doesn't exist
            guest_user = User(
                email='guest@agentmath.app',
                password_hash='no_password_required',
                full_name='Guest User',
                role='student',
                is_approved=True
            )
            db.session.add(guest_user)
            db.session.commit()

        # Set up guest session properly
        session['is_guest'] = True
        session['guest_session_id'] = str(uuid.uuid4())
        session['user_id'] = guest_user.id  # CRITICAL: Set user_id
        session['role'] = 'student'

        # Try to create guest_sessions table if it doesn't exist
        try:
            from sqlalchemy import text
            db.session.execute(text("""
                CREATE TABLE IF NOT EXISTS guest_sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT UNIQUE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    quiz_attempts INTEGER DEFAULT 0
                )
            """))

            # Insert this guest session
            db.session.execute(
                text("INSERT OR IGNORE INTO guest_sessions (session_id) VALUES (:sid)"),
                {"sid": session['guest_session_id']}
            )
            db.session.commit()
        except Exception as e:
            print(f"Note: Could not create guest_sessions table: {e}")
            # Not critical, continue anyway

        return jsonify({
            'success': True,
            'message': 'Guest session started',
            'redirect': '/student'
        }), 200

    except Exception as e:
        print(f"Error starting guest session: {e}")
        db.session.rollback()
        return jsonify({'error': f'Failed to start guest session: {str(e)}'}), 500


@app.route('/guest')
def guest_app():
    """Guest mode redirect - initializes session if needed"""
    import uuid

    # If not already a guest, set up guest session
    if 'is_guest' not in session or 'user_id' not in session:
        try:
            # Get or create guest user
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

            # Set up session
            session['is_guest'] = True
            session['guest_session_id'] = str(uuid.uuid4())
            session['user_id'] = guest_user.id
            session['role'] = 'student'

        except Exception as e:
            print(f"Error setting up guest session: {e}")
            return redirect('/')

    # Redirect to student app
    return redirect('/student')


@app.route('/api/guest-info')
def guest_info():
    """Return guest session information"""
    if session.get('is_guest'):
        return jsonify({
            'is_guest': True,
            'guest_id': session.get('guest_session_id', 'unknown'),
            'user_id': session.get('user_id')
        }), 200
    return jsonify({'is_guest': False}), 200


@app.route('/api/change-password', methods=['POST'])
@login_required
def change_password():
    """Allow users to change their own password"""
    data = request.json
    current_password = data.get('current_password', '')
    new_password = data.get('new_password', '')
    confirm_password = data.get('confirm_password', '')

    # Validation
    if not current_password or not new_password or not confirm_password:
        return jsonify({'error': 'All fields are required'}), 400

    if new_password != confirm_password:
        return jsonify({'error': 'New passwords do not match'}), 400

    if len(new_password) < 6:
        return jsonify({'error': 'Password must be at least 6 characters long'}), 400

    # Get current user
    user = User.query.get(session['user_id'])

    # Verify current password
    if not user.check_password(current_password):
        return jsonify({'error': 'Current password is incorrect'}), 401

    # Update password
    user.set_password(new_password)
    db.session.commit()

    return jsonify({'message': 'Password changed successfully'}), 200

@app.route('/api/current-user')
def current_user():
    """Get current user info - supports both regular and guest users"""
    if 'is_guest' in session:
        return jsonify({
            'is_guest': True,
            'guest_type': session.get('guest_type', 'casual'),
            'guest_code': session.get('guest_code'),
            'full_name': 'Guest User',
            'email': 'guest@example.com',
            'role': 'student'
        }), 200

    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401

    user = User.query.get(session['user_id'])
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict()), 200


# ==================== COMBINED INIT ENDPOINT ====================
# This endpoint returns ALL data needed for initial page load in ONE request
# Reduces 10+ API calls to 1, saving ~5-8 seconds of server latency

@app.route('/api/init')
@guest_or_login_required
@approved_required
def api_init():
    """
    Combined endpoint that returns ALL data needed for initial page load.
    Reduces 10+ API calls to just 1, dramatically improving load time.

    Returns: user, mastery, topics, progress, badges, online_count, resources, weekly_challenge
    """
    from sqlalchemy import text
    from datetime import datetime, timedelta

    result = {
        'success': True,
        'user': None,
        'mastery': {},
        'topics': [],
        'strands': {},
        'strand_info': {},
        'progress': {},
        'badges': {'earned': [], 'available': [], 'total_points': 0, 'level': 1},
        'online_count': 1,
        'resources': [],
        'weekly_challenge': None,
        'adaptive_progress': {}
    }

    try:
        user_id = session.get('user_id')
        is_guest = session.get('is_guest', False)
        guest_code = session.get('guest_code')

        # ===== 1. CURRENT USER =====
        if is_guest:
            result['user'] = {
                'is_guest': True,
                'guest_type': session.get('guest_type', 'casual'),
                'guest_code': guest_code,
                'full_name': 'Guest User',
                'email': 'guest@example.com',
                'role': 'student'
            }
        elif user_id:
            user = User.query.get(user_id)
            if user:
                result['user'] = user.to_dict()

        # ===== 2. TOPICS (with strand grouping) =====
        try:
            # Query topics using actual schema: topic_id, display_name, strand_id with strands join
            topics_result = db.session.execute(text("""
                SELECT t.id, t.topic_id, t.display_name, t.description, t.icon, t.color, 
                       COALESCE(s.name, 'Other') as strand,
                       t.is_new, t.beta_only, t.is_visible, t.sort_order, t.jc_levels
                FROM topics t
                LEFT JOIN strands s ON t.strand_id = s.id
                WHERE t.is_visible = 1
                ORDER BY t.sort_order, t.display_name
            """)).fetchall()

            strands = {}
            for row in topics_result:
                topic_data = {
                    'id': row[0],
                    'topic_id': row[1],
                    'name': row[2],  # display_name mapped to name for compatibility
                    'description': row[3],
                    'icon': row[4],
                    'color': row[5],
                    'strand': row[6],
                    'is_new': bool(row[7]) if row[7] is not None else False,
                    'beta_only': bool(row[8]) if row[8] is not None else False,
                    'jc_levels': row[11]
                }
                result['topics'].append(topic_data)

                strand = row[6] or 'Other'
                if strand not in strands:
                    strands[strand] = []
                strands[strand].append(topic_data)

            result['strands'] = strands

            # Strand info
            result['strand_info'] = {
                'Number': {'icon': 'fa-calculator', 'color': 'blue', 'order': 1},
                'Algebra and Functions': {'icon': 'fa-superscript', 'color': 'purple', 'order': 2},
                'Geometry and Trigonometry': {'icon': 'fa-shapes', 'color': 'green', 'order': 3},
                'Statistics and Probability': {'icon': 'fa-chart-bar', 'color': 'orange', 'order': 4}
            }
        except Exception as e:
            print(f"Init - topics error: {e}")

        # ===== 3. MASTERY DATA =====
        try:
            topics_list = get_valid_topics_from_db()
            difficulties = VALID_DIFFICULTIES

            if guest_code:
                mastery_query = text("""
                    SELECT topic, difficulty, MAX(CAST(score AS FLOAT) / total_questions * 100) as best_score
                    FROM guest_quiz_attempts
                    WHERE guest_code = :code
                    GROUP BY topic, difficulty
                """)
                mastery_results = db.session.execute(mastery_query, {'code': guest_code}).fetchall()
            elif user_id and not is_guest:
                mastery_query = text("""
                    SELECT topic, difficulty, MAX(percentage) as best_score
                    FROM quiz_attempts
                    WHERE user_id = :user_id
                    GROUP BY topic, difficulty
                """)
                mastery_results = db.session.execute(mastery_query, {'user_id': user_id}).fetchall()
            else:
                mastery_results = []

            # Build lookup
            best_scores = {}
            for row in mastery_results:
                topic, difficulty, best_score = row
                if topic not in best_scores:
                    best_scores[topic] = {}
                best_scores[topic][difficulty] = best_score or 0

            # Build mastery data structure
            for topic in topics_list:
                result['mastery'][topic] = {
                    'difficulties': {},
                    'topic_mastered': False
                }
                mastered_count = 0
                for difficulty in difficulties:
                    best_score = best_scores.get(topic, {}).get(difficulty, 0)
                    result['mastery'][topic]['difficulties'][difficulty] = {
                        'mastered': best_score > 80,
                        'best_score': round(best_score, 1) if best_score else 0
                    }
                    if best_score > 80:
                        mastered_count += 1
                result['mastery'][topic]['topic_mastered'] = (mastered_count == 3)
        except Exception as e:
            print(f"Init - mastery error: {e}")

        # ===== 4. ADAPTIVE PROGRESS (all topics at once) =====
        try:
            adaptive_topics = ['arithmetic', 'fractions', 'percentages', 'decimals', 'ratio',
                             'sets', 'descriptive_statistics', 'patterns', 'functions',
                             'area_perimeter_volume', 'solving_equations', 'simultaneous_equations',
                             'linear_inequalities', 'introductory_algebra', 'applied_arithmetic',
                             'currency', 'speed_distance_time', 'probability', 'coordinate_geometry',
                             'trigonometry', 'number_systems', 'indices', 'geometry',
                             'simplifying_expressions', 'expanding_factorising']

            if user_id and not is_guest:
                adaptive_query = text("""
                    SELECT topic, current_level, current_points, total_questions, correct_answers
                    FROM adaptive_progress
                    WHERE user_id = :user_id
                """)
                adaptive_results = db.session.execute(adaptive_query, {'user_id': user_id}).fetchall()
            elif guest_code:
                adaptive_query = text("""
                    SELECT topic, current_level, current_points, total_questions, correct_answers
                    FROM adaptive_progress
                    WHERE guest_code = :guest_code
                """)
                adaptive_results = db.session.execute(adaptive_query, {'guest_code': guest_code}).fetchall()
            else:
                adaptive_results = []

            # Build adaptive progress dict
            for row in adaptive_results:
                result['adaptive_progress'][row[0]] = {
                    'current_level': row[1],
                    'current_points': row[2],
                    'total_questions': row[3],
                    'correct_answers': row[4]
                }

            # Fill in defaults for topics without progress
            for topic in adaptive_topics:
                if topic not in result['adaptive_progress']:
                    result['adaptive_progress'][topic] = {
                        'current_level': 1,
                        'current_points': 0,
                        'total_questions': 0,
                        'correct_answers': 0
                    }
        except Exception as e:
            print(f"Init - adaptive progress error: {e}")

        # ===== 5. BADGES =====
        try:
            total_points = 0
            level = 1

            if guest_code:
                # Get guest stats
                guest_stats = db.session.execute(text("""
                    SELECT total_score FROM guest_users WHERE guest_code = :code
                """), {'code': guest_code}).fetchone()

                if guest_stats:
                    total_points = guest_stats[0] or 0
                    level = (total_points // 100) + 1

                # Get guest badges
                try:
                    guest_badges = db.session.execute(text("""
                        SELECT badge_name, earned_at FROM guest_badges
                        WHERE guest_code = :code ORDER BY earned_at DESC
                    """), {'code': guest_code}).fetchall()

                    for badge_row in guest_badges:
                        badge = Badge.query.filter_by(name=badge_row[0]).first()
                        if badge:
                            result['badges']['earned'].append({
                                'name': badge.name,
                                'description': badge.description,
                                'icon': badge.icon,
                                'earned_at': badge_row[1].isoformat() if badge_row[1] else None
                            })
                except:
                    pass

            elif user_id and not is_guest:
                user = User.query.get(user_id)
                if user:
                    stats = UserStats.query.filter_by(user_id=user_id).first()
                    if stats:
                        total_points = stats.total_points or 0
                        level = stats.level or 1

                    # Get user badges
                    user_badges = UserBadge.query.filter_by(user_id=user_id).all()
                    for ub in user_badges:
                        if ub.badge:
                            result['badges']['earned'].append({
                                'name': ub.badge.name,
                                'description': ub.badge.description,
                                'icon': ub.badge.icon,
                                'earned_at': ub.earned_at.isoformat() if ub.earned_at else None
                            })

            result['badges']['total_points'] = total_points
            result['badges']['level'] = level
        except Exception as e:
            print(f"Init - badges error: {e}")

        # ===== 6. ONLINE COUNT =====
        try:
            five_minutes_ago = datetime.utcnow() - timedelta(minutes=5)

            registered_count = db.session.execute(text("""
                SELECT COUNT(DISTINCT user_id) FROM quiz_attempts WHERE completed_at > :since
            """), {'since': five_minutes_ago}).fetchone()[0] or 0

            guest_count = db.session.execute(text("""
                SELECT COUNT(*) FROM guest_users WHERE last_active > :since
            """), {'since': five_minutes_ago}).fetchone()[0] or 0

            result['online_count'] = max(1, registered_count + guest_count)
        except Exception as e:
            print(f"Init - online count error: {e}")
            result['online_count'] = 1

        # ===== 7. RESOURCES =====
        try:
            resources_result = db.session.execute(text("""
                SELECT id, button_text, link_url, popup_text, image_filename, display_order, category
                FROM additional_resources
                WHERE is_active = 1
                ORDER BY display_order, id
            """)).fetchall()

            for row in resources_result:
                image_url = f'/static/resources/{row[4]}' if row[4] else None
                result['resources'].append({
                    'id': row[0],
                    'button_text': row[1],
                    'link_url': row[2],
                    'popup_text': row[3],
                    'image_url': image_url,
                    'display_order': row[5],
                    'category': row[6]
                })
        except Exception as e:
            print(f"Init - resources error: {e}")

        # ===== 8. WEEKLY CHALLENGE =====
        try:
            today = datetime.utcnow().date()
            start_of_week = today - timedelta(days=today.weekday())

            if guest_code:
                quiz_count = db.session.execute(text("""
                    SELECT COUNT(*) FROM guest_quiz_attempts
                    WHERE guest_code = :code AND DATE(completed_at) >= :start
                """), {'code': guest_code, 'start': start_of_week}).fetchone()[0]

                high_score_count = db.session.execute(text("""
                    SELECT COUNT(*) FROM guest_quiz_attempts
                    WHERE guest_code = :code AND DATE(completed_at) >= :start AND percentage >= 80
                """), {'code': guest_code, 'start': start_of_week}).fetchone()[0]
            elif user_id:
                quiz_count = db.session.execute(text("""
                    SELECT COUNT(*) FROM quiz_attempts
                    WHERE user_id = :uid AND DATE(completed_at) >= :start
                """), {'uid': user_id, 'start': start_of_week}).fetchone()[0]

                high_score_count = db.session.execute(text("""
                    SELECT COUNT(*) FROM quiz_attempts
                    WHERE user_id = :uid AND DATE(completed_at) >= :start AND percentage >= 80
                """), {'uid': user_id, 'start': start_of_week}).fetchone()[0]
            else:
                quiz_count = 0
                high_score_count = 0

            result['weekly_challenge'] = {
                'goals': [
                    {'id': 'goal1', 'target': 5, 'current': quiz_count, 'points': 50, 'type': 'quizzes'},
                    {'id': 'goal2', 'target': 3, 'current': high_score_count, 'points': 75, 'type': 'highscores'},
                    {'id': 'goal3', 'target': 5, 'current': 0, 'points': 100, 'type': 'streak'}
                ],
                'week_start': start_of_week.isoformat()
            }
        except Exception as e:
            print(f"Init - weekly challenge error: {e}")

        return jsonify(result)

    except Exception as e:
        print(f"Init endpoint error: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'error': str(e)}), 500


# ==================== STUDENT ROUTES ====================

@app.route('/student')
@login_required
@approved_required
def student_redirect():
    """Redirect /student to /app for backwards compatibility"""
    return redirect(url_for('student_app'))

@app.route('/app')
@login_required
@approved_required
def student_app():
    # Handle repeat guests (they don't have user_id)
    if 'guest_code' in session:
        return render_template('student_app.html')

    # Handle full accounts and casual guests
    user = User.query.get(session['user_id'])
    if user.role != 'student':
        return redirect(url_for('index'))
    return render_template('student_app.html')



@app.route('/api/topics')
@guest_or_login_required
@approved_required
def get_topics():
    """Get topics grouped by strands - reads from topics table (admin managed)"""
    from sqlalchemy import text

    # Strand colors and descriptions
    strand_info = {
        'Numeracy': {
            'color': '#10b981',
            'icon': '🧮',
            'description': 'Build strong number skills for everyday maths'
        },
        'L1LP': {
            'color': '#8b5cf6',
            'icon': '🌟',
            'description': 'Level 1 Learning Programme - Accessible numeracy for all learners'
        },
        'L2LP': {
            'color': '#f97316',
            'icon': '⭐',
            'description': 'Level 2 Learning Programme - Building numeracy for independent living'
        },
        'Number': {
            'color': '#667eea',
            'icon': '📊',
            'description': 'Master the fundamentals of numbers and operations'
        },
        'Algebra and Functions': {
            'color': '#f093fb',
            'icon': '🔢',
            'description': 'Discover patterns, equations, and functions'
        },
        'Statistics and Probability': {
            'color': '#4facfe',
            'icon': '📈',
            'description': 'Analyze data and understand probability'
        },
        'Senior Cycle - Algebra': {
            'color': '#fa709a',
            'icon': '🎓',
            'description': 'Advanced algebraic concepts for senior students'
        },
        'Geometry and Trigonometry': {
            'color': '#764ba2',
            'icon': '📐',
            'description': 'Explore shapes, measurements, and spatial reasoning'
        },
        'LC Higher Level': {
            'color': '#3b82f6',
            'icon': '🎓',
            'description': 'Leaving Certificate Higher Level Mathematics (SEC aligned)'
        },
        'LC Ordinary Level': {
            'color': '#10b981',
            'icon': '📗',
            'description': 'Leaving Certificate Ordinary Level Mathematics (SEC aligned)'
        }
    }

    strands = {}
    topics_flat = {}

    try:
        # Query topics from the topics table (managed by admin)
        # Only get visible topics, ordered by strand and sort_order
        topics_query = db.session.execute(text("""
            SELECT t.topic_id, t.display_name, t.icon, s.name as strand_name, t.sort_order
            FROM topics t
            LEFT JOIN strands s ON t.strand_id = s.id
            WHERE t.is_visible = 1
            ORDER BY
                CASE s.name
                    WHEN 'Numeracy' THEN 0
                    WHEN 'L1LP' THEN 1
                    WHEN 'L2LP' THEN 2
                    WHEN 'Number' THEN 3
                    WHEN 'Algebra and Functions' THEN 4
                    WHEN 'Statistics and Probability' THEN 5
                    WHEN 'Senior Cycle - Algebra' THEN 6
                    WHEN 'Geometry and Trigonometry' THEN 7
                    WHEN 'LC Ordinary Level' THEN 8
                    WHEN 'LC Higher Level' THEN 9
                    ELSE 10
                END,
                t.sort_order,
                t.display_name
        """)).fetchall()

        if topics_query:
            for topic_id, display_name, icon, strand_name, sort_order in topics_query:
                # Use strand name or 'Other' for unassigned topics
                strand = strand_name or 'Other'

                if strand not in strands:
                    strands[strand] = []

                # Add topic to strand list
                strands[strand].append(topic_id)

                # Add topic metadata to flat dict
                topics_flat[topic_id] = {
                    'title': display_name,
                    'icon': icon or 'book'
                }

            # Add any new strands to strand_info with default styling
            for strand_name in strands.keys():
                if strand_name not in strand_info:
                    strand_info[strand_name] = {
                        'color': '#6b7280',
                        'icon': '📚',
                        'description': f'Topics in {strand_name}'
                    }
        else:
            # No topics in database, use fallback
            raise Exception("No topics found in topics table")

    except Exception as e:
        # Fallback: Query from questions table (old method)
        topic_info = {
            'arithmetic': {'title': 'Arithmetic', 'icon': 'calculator'},
            'fractions': {'title': 'Fractions', 'icon': 'divide'},
            'decimals': {'title': 'Decimals', 'icon': 'percent'},
            'multiplication_division': {'title': 'Multiplication & Division', 'icon': 'x'},
            'number_systems': {'title': 'Number Systems', 'icon': 'hash'},
            'bodmas': {'title': 'BODMAS', 'icon': 'book'},
            'introductory_algebra': {'title': 'Introductory Algebra', 'icon': 'book-open'},
            'functions': {'title': 'Functions', 'icon': 'chart'},
            'patterns': {'title': 'Patterns', 'icon': 'trending-up'},
            'solving_equations': {'title': 'Solving Equations', 'icon': 'equals'},
            'simplifying_expressions': {'title': 'Simplifying Expressions', 'icon': 'calculator'},
            'expanding_factorising': {'title': 'Expanding & Factorising', 'icon': 'brackets'},
            'probability': {'title': 'Probability', 'icon': 'dice'},
            'descriptive_statistics': {'title': 'Descriptive Statistics', 'icon': 'chart-bar'},
            'sets': {'title': 'Sets', 'icon': 'layers'},
            'surds': {'title': 'Surds', 'icon': 'radical'},
            'complex_numbers_intro': {'title': 'Complex Numbers Intro', 'icon': 'infinity'},
            'complex_numbers_expanded': {'title': 'Complex Numbers - Expanded', 'icon': 'rotate'},
            'percentages': {'title': 'Percentages', 'icon': 'percent'},
            'geometry': {'title': 'Geometry', 'icon': 'shapes'},
            'trigonometry': {'title': 'Trigonometry', 'icon': 'ruler'}
        }

        try:
            # Try to get topics from questions table
            topics_query = db.session.execute(text("""
                SELECT DISTINCT topic, strand
                FROM questions
                WHERE strand IS NOT NULL
                ORDER BY strand, topic
            """)).fetchall()

            for topic, strand in topics_query:
                if strand not in strands:
                    strands[strand] = []
                strands[strand].append(topic)

                if topic in topic_info:
                    topics_flat[topic] = topic_info[topic]
                else:
                    topics_flat[topic] = {
                        'title': topic.replace('_', ' ').title(),
                        'icon': 'book'
                    }
        except:
            # Ultimate fallback - hardcoded
            strands = {
                'Number': ['arithmetic', 'multiplication_division', 'number_systems',
                          'bodmas', 'fractions', 'decimals', 'sets'],
                'Algebra and Functions': ['introductory_algebra', 'functions', 'patterns',
                                         'solving_equations', 'simplifying_expressions',
                                         'expanding_factorising'],
                'Statistics and Probability': ['probability', 'descriptive_statistics'],
                'Senior Cycle - Algebra': ['surds', 'complex_numbers_intro',
                                           'complex_numbers_expanded']
            }
            topics_flat = topic_info

    return jsonify({
        'topics': topics_flat,
        'strands': strands,
        'strand_info': strand_info
    })

@app.route('/api/questions/<topic>/<difficulty>')
@guest_or_login_required
@approved_required
def get_questions(topic, difficulty):
    """
    Get 25 random questions from the pool, excluding questions the user has already seen.
    If fewer than 25 unseen questions are available, returns all available unseen questions.
    This ensures users never see duplicate questions, even if the quiz is shorter.
    Questions are marked as seen immediately when fetched.
    """
    from sqlalchemy import text

    # Get user identifier
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')

    # Get IDs of questions this user has already seen for this topic/difficulty
    seen_question_ids = set()

    try:
        if user_id:
            seen = db.session.execute(text("""
                SELECT question_id FROM user_question_history
                WHERE user_id = :user_id AND topic = :topic AND difficulty = :difficulty
            """), {'user_id': user_id, 'topic': topic, 'difficulty': difficulty}).fetchall()
            seen_question_ids = {row.question_id for row in seen}
        elif guest_code:
            seen = db.session.execute(text("""
                SELECT question_id FROM user_question_history
                WHERE guest_code = :guest_code AND topic = :topic AND difficulty = :difficulty
            """), {'guest_code': guest_code, 'topic': topic, 'difficulty': difficulty}).fetchall()
            seen_question_ids = {row.question_id for row in seen}
    except Exception as e:
        # Table might not exist yet - proceed without filtering
        print(f"Note: Could not check question history (table may not exist): {e}")
        seen_question_ids = set()

    # Get all questions for this topic/difficulty
    questions = Question.query.filter_by(topic=topic, difficulty=difficulty).all()

    # Filter out seen questions
    unseen_questions = [q for q in questions if q.id not in seen_question_ids]

    # If no unseen questions, reset history for this topic/difficulty and use all questions
    if len(unseen_questions) == 0 and len(questions) > 0:
        try:
            if user_id:
                db.session.execute(text("""
                    DELETE FROM user_question_history
                    WHERE user_id = :user_id AND topic = :topic AND difficulty = :difficulty
                """), {'user_id': user_id, 'topic': topic, 'difficulty': difficulty})
            elif guest_code:
                db.session.execute(text("""
                    DELETE FROM user_question_history
                    WHERE guest_code = :guest_code AND topic = :topic AND difficulty = :difficulty
                """), {'guest_code': guest_code, 'topic': topic, 'difficulty': difficulty})
            db.session.commit()
            unseen_questions = questions  # All questions are now "unseen" again
            print(f"Reset question history for {user_id or guest_code} on {topic}/{difficulty}")
        except Exception as e:
            print(f"Could not reset question history: {e}")
            unseen_questions = questions

    # Convert to dict and shuffle
    questions_list = [q.to_dict() for q in unseen_questions]
    random.shuffle(questions_list)

    # Return up to 25 questions (or fewer if not enough unseen)
    selected_questions = questions_list[:25]

    # Record these questions as seen
    if selected_questions:
        try:
            for q in selected_questions:
                if user_id:
                    db.session.execute(text("""
                        INSERT OR IGNORE INTO user_question_history
                        (user_id, question_id, topic, difficulty, seen_at)
                        VALUES (:user_id, :question_id, :topic, :difficulty, CURRENT_TIMESTAMP)
                    """), {
                        'user_id': user_id,
                        'question_id': q['id'],
                        'topic': topic,
                        'difficulty': difficulty
                    })
                elif guest_code:
                    db.session.execute(text("""
                        INSERT OR IGNORE INTO user_question_history
                        (guest_code, question_id, topic, difficulty, seen_at)
                        VALUES (:guest_code, :question_id, :topic, :difficulty, CURRENT_TIMESTAMP)
                    """), {
                        'guest_code': guest_code,
                        'question_id': q['id'],
                        'topic': topic,
                        'difficulty': difficulty
                    })
            db.session.commit()
        except Exception as e:
            # Don't fail the request if tracking fails
            print(f"Could not record question history: {e}")
            db.session.rollback()

    # Log if quiz will be shorter than usual
    if len(selected_questions) < 25 and len(questions) >= 25:
        print(f"Quiz for {user_id or guest_code}: {len(selected_questions)} unseen questions available (of {len(questions)} total)")

    return jsonify(selected_questions)



# =====================================================
# END CLOCK CHALLENGE ROUTES
# =====================================================

@app.route('/api/create-quiz-attempt', methods=['POST'])
@login_required
@approved_required
def create_quiz_attempt():
    """
    Create a quiz attempt and return the ID for Who Am I tracking.
    Called when student starts a quiz in student_app.html.
    """
    data = request.json
    
    # Validate input is a dict
    if not isinstance(data, dict):
        return jsonify({'error': 'Invalid request format - expected JSON object'}), 400
    
    # Extract and validate required fields
    topic = data.get('topic')
    difficulty = data.get('difficulty')
    
    # Validate topic is provided and is a string
    if topic is None:
        return jsonify({'error': 'Topic is required'}), 400
    if not isinstance(topic, str):
        return jsonify({'error': 'Topic must be a string'}), 400
    topic = topic.strip().lower()
    if not topic:
        return jsonify({'error': 'Topic cannot be empty'}), 400
    
    # Validate difficulty is provided and is a string
    if difficulty is None:
        return jsonify({'error': 'Difficulty is required'}), 400
    if not isinstance(difficulty, str):
        return jsonify({'error': 'Difficulty must be a string'}), 400
    difficulty = difficulty.strip().lower()
    if not difficulty:
        return jsonify({'error': 'Difficulty cannot be empty'}), 400
    
    # Validate against allowed values
    valid_topics = get_valid_topics_from_db()
    if topic not in valid_topics:
        return jsonify({'error': f'Invalid topic: {topic}'}), 400
    
    if difficulty not in VALID_DIFFICULTIES:
        return jsonify({'error': f'Invalid difficulty: {difficulty}'}), 400

    try:
        # Create new quiz attempt record
        quiz_attempt = QuizAttempt(
            user_id=session['user_id'],
            topic=topic,
            difficulty=difficulty,
            score=0,  # Will be updated when quiz completes
            total_questions=0,
            percentage=0
        )
        db.session.add(quiz_attempt)
        db.session.commit()

        return jsonify({
            'success': True,
            'quiz_attempt_id': quiz_attempt.id
        })

    except Exception as e:
        db.session.rollback()
        import traceback
        error_details = traceback.format_exc()
        print(f"Error creating quiz attempt: {e}")
        print(f"Full traceback: {error_details}")
        return jsonify({'error': str(e), 'details': error_details}), 500

@app.route('/api/submit-quiz', methods=['POST'])
@guest_or_login_required
@approved_required
def submit_quiz():
    """Submit quiz - works for guests, repeat guests, and registered users"""
    data = request.json

    # Normalize topic and difficulty to lowercase
    topic = data.get('topic', '').lower().strip()
    difficulty = data.get('difficulty', '').lower().strip()
    score = data.get('score', 0)
    total = data.get('total_questions', 25)
    percentage = data.get('percentage', 0)
    time_taken = data.get('time_taken', 0)

    # Validate topic and difficulty - reads from database
    valid_topics = get_valid_topics_from_db()  # Database-driven!
    valid_difficulties = VALID_DIFFICULTIES

    if topic not in valid_topics:
        return jsonify({'error': f'Invalid topic: {topic}'}), 400

    if difficulty not in valid_difficulties:
        return jsonify({'error': f'Invalid difficulty: {difficulty}'}), 400

    # Handle repeat guests - save to guest tables
    if 'guest_code' in session:
        from sqlalchemy import text
        guest_code = session['guest_code']

        # Get all bonus points
        who_am_i_bonus = data.get('who_am_i_bonus', 0)
        milestone_points = data.get('milestone_points', 0)  # NEW: In-quiz milestone points
        total_points = score + who_am_i_bonus + milestone_points  # Score + all bonuses!

        # Save quiz attempt (try with bonus columns, fallback without them)
        try:
            db.session.execute(text("""
                INSERT INTO guest_quiz_attempts (guest_code, topic, difficulty, score, total_questions, time_spent, who_am_i_bonus, milestone_points)
                VALUES (:code, :topic, :diff, :score, :total, :time, :bonus, :milestone)
            """), {
                "code": guest_code,
                "topic": topic,
                "diff": difficulty,
                "score": score,
                "total": total,
                "time": time_taken,
                "bonus": who_am_i_bonus,
                "milestone": milestone_points
            })
        except:
            # Fallback: table doesn't have bonus columns
            try:
                db.session.execute(text("""
                    INSERT INTO guest_quiz_attempts (guest_code, topic, difficulty, score, total_questions, time_spent, who_am_i_bonus)
                    VALUES (:code, :topic, :diff, :score, :total, :time, :bonus)
                """), {
                    "code": guest_code,
                    "topic": topic,
                    "diff": difficulty,
                    "score": score,
                    "total": total,
                    "time": time_taken,
                    "bonus": who_am_i_bonus
                })
            except:
                # Final fallback: no bonus columns at all
                db.session.execute(text("""
                    INSERT INTO guest_quiz_attempts (guest_code, topic, difficulty, score, total_questions, time_spent)
                    VALUES (:code, :topic, :diff, :score, :total, :time)
                """), {
                    "code": guest_code,
                    "topic": topic,
                    "diff": difficulty,
                    "score": score,
                    "total": total,
                    "time": time_taken
                })

        # Update guest stats (including ALL bonuses!)
        db.session.execute(text("""
            UPDATE guest_users
            SET total_score = total_score + :total_points,
                quizzes_completed = quizzes_completed + 1,
                last_active = :now
            WHERE guest_code = :code
        """), {
            "total_points": total_points,  # Score + who_am_i_bonus + milestone_points!
            "now": datetime.utcnow(),
            "code": guest_code
        })

        db.session.commit()

        return jsonify({
            'message': 'Quiz completed!',
            'score': score,
            'total': total,
            'percentage': percentage,
            'who_am_i_bonus': who_am_i_bonus,
            'milestone_points': milestone_points,
            'total_points_earned': total_points,
            'is_repeat_guest': True
        }), 200

    # For casual guests, save to UserStats so points persist during session
    if 'is_guest' in session:
        user_id = session.get('user_id')
        if user_id:
            # Get or create UserStats for guest user
            stats = UserStats.query.filter_by(user_id=user_id).first()
            if not stats:
                stats = UserStats(user_id=user_id, total_points=0, level=1)
                db.session.add(stats)
                db.session.commit()

            # Update points
            stats.total_points += score
            stats.total_quizzes += 1
            stats.total_questions_answered += total
            stats.total_correct_answers += score
            db.session.commit()

        return jsonify({
            'message': 'Quiz completed!',
            'score': score,
            'total': total,
            'percentage': percentage,
            'total_points': score,
            'is_guest': True,
            'prompt_register': True
        }), 200

    # For registered users, save to database
    # WHO AM I: Get quiz_attempt_id and bonus if provided
    quiz_attempt_id = data.get('quiz_attempt_id')
    who_am_i_bonus = data.get('who_am_i_bonus', 0)

    # If quiz_attempt_id is provided, update that record instead of creating new
    if quiz_attempt_id:
        attempt = QuizAttempt.query.get(quiz_attempt_id)
        if attempt and attempt.user_id == session['user_id']:
            # Update existing quiz attempt
            attempt.score = score
            attempt.total_questions = total
            attempt.percentage = percentage
            attempt.time_taken = time_taken
            attempt.who_am_i_bonus = who_am_i_bonus
            attempt.completed_at = datetime.utcnow()
        else:
            # Quiz attempt not found or doesn't belong to user, create new
            attempt = QuizAttempt(
                user_id=session['user_id'],
                topic=topic,
                difficulty=difficulty,
                score=score,
                total_questions=total,
                percentage=percentage,
                time_taken=time_taken,
                who_am_i_bonus=who_am_i_bonus
            )
            db.session.add(attempt)
    else:
        # Create new quiz attempt
        attempt = QuizAttempt(
            user_id=session['user_id'],
            topic=topic,
            difficulty=difficulty,
            score=score,
            total_questions=total,
            percentage=percentage,
            time_taken=time_taken,
            who_am_i_bonus=who_am_i_bonus
        )
        db.session.add(attempt)

    db.session.commit()

    # Update stats and check for badges
    stats, newly_earned_badges = update_user_stats_after_quiz(session['user_id'], attempt)

    # Update Adaptive Learning System
    adaptive_result = None
    if ADAPTIVE_LEARNING_AVAILABLE:
        try:
            # Get question-level results if provided
            question_results = data.get('question_results', None)
            adaptive_result = update_adaptive_after_quiz(
                user_id=session['user_id'],
                topic=topic,
                difficulty=difficulty,
                score=score,
                total_questions=total,
                time_taken=time_taken,
                question_results=question_results
            )
        except Exception as e:
            print(f"Adaptive learning update error: {e}")
            adaptive_result = None

    return jsonify({
        'message': 'Quiz submitted successfully',
        'attempt': attempt.to_dict(),
        'stats': stats.to_dict(),
        'newly_earned_badges': newly_earned_badges,
        'adaptive': adaptive_result
    }), 201

@app.route('/api/my-progress')
@guest_or_login_required
def my_progress():
    from sqlalchemy import text

    guest_code = session.get('guest_code')
    user_id = session.get('user_id')

    # Check if this is a guest user with data in guest_quiz_attempts
    if guest_code:
        try:
            attempts = db.session.execute(text("""
                SELECT id, topic, difficulty, score, total_questions, time_spent, completed_at
                FROM guest_quiz_attempts
                WHERE guest_code = :code
                ORDER BY completed_at DESC
                LIMIT 100
            """), {'code': guest_code}).fetchall()

            if attempts:
                return jsonify([{
                    'id': a.id,
                    'topic': a.topic,
                    'difficulty': a.difficulty,
                    'score': a.score,
                    'total_questions': a.total_questions,
                    'percentage': round((a.score / a.total_questions * 100), 1) if a.total_questions > 0 else 0,
                    'time_taken': a.time_spent,
                    'completed_at': a.completed_at if isinstance(a.completed_at, str) else (a.completed_at.isoformat() if a.completed_at else None)
                } for a in attempts])
        except Exception as e:
            print(f"Error loading guest progress: {e}")

    # Fallback: check for registered user quiz attempts
    if user_id and not session.get('is_guest'):
        attempts = QuizAttempt.query.filter_by(user_id=user_id).order_by(QuizAttempt.completed_at.desc()).all()
        return jsonify([a.to_dict() for a in attempts])

    return jsonify([]), 200

# ==================== TOPIC MANAGEMENT MODULE ====================
# Import and register topic management routes
try:
    from topic_management import register_topic_routes
    register_topic_routes(app, db)
except ImportError:
    print("Warning: topic_management.py not found - topic management disabled")
except Exception as e:
    print(f"Warning: Could not load topic management: {e}")

# ==================== QUESTION GENERATOR MODULE ====================
# Import and register AI question generator routes
try:
    from question_generator import register_generator_routes
    register_generator_routes(app, db)
except ImportError:
    print("Warning: question_generator.py not found - question generator disabled")
except Exception as e:
    print(f"Warning: Could not load question generator: {e}")

# ==================== CHART QUESTION GENERATOR MODULE ====================
# Import and register chart-based question generator routes
try:
    from chart_question_generator import register_chart_generator_routes

    # Create admin_required_api decorator for the chart generator
    def admin_required_api_wrapper(f):
        from functools import wraps
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return jsonify({'error': 'Login required'}), 401
            user = User.query.get(session['user_id'])
            if not user or user.role != 'admin':
                return jsonify({'error': 'Admin access required'}), 403
            return f(*args, **kwargs)
        return decorated_function

    register_chart_generator_routes(app, db, Question, admin_required_api_wrapper)
    print("✓ Chart question generator loaded successfully")
except ImportError:
    print("Warning: chart_question_generator.py not found - chart generator disabled")
except Exception as e:
    print(f"Warning: Could not load chart generator: {e}")

# ==================== GEOMETRY QUESTION GENERATOR MODULE ====================
# Import and register geometry-based question generator routes
try:
    from geometry_question_generator import register_geometry_generator_routes

    # Create admin_required_api decorator for the geometry generator
    def admin_required_api_geom(f):
        from functools import wraps
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return jsonify({'error': 'Login required'}), 401
            user = User.query.get(session['user_id'])
            if not user or user.role != 'admin':
                return jsonify({'error': 'Admin access required'}), 403
            return f(*args, **kwargs)
        return decorated_function

    register_geometry_generator_routes(app, db, Question, admin_required_api_geom)
    print("✓ Geometry question generator loaded successfully")
except ImportError:
    print("Warning: geometry_question_generator.py not found - geometry generator disabled")
except Exception as e:
    print(f"Warning: Could not load geometry generator: {e}")

# ==================== PATTERN QUESTION GENERATOR MODULE ====================
# Import and register pattern-based question generator routes
try:
    from pattern_question_generator import register_pattern_generator_routes

    # Create admin_required_api decorator for the pattern generator
    def admin_required_api_pattern(f):
        from functools import wraps
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return jsonify({'error': 'Login required'}), 401
            user = User.query.get(session['user_id'])
            if not user or user.role != 'admin':
                return jsonify({'error': 'Admin access required'}), 403
            return f(*args, **kwargs)
        return decorated_function

    register_pattern_generator_routes(app, db, Question, admin_required_api_pattern)
    print("✓ Pattern question generator loaded successfully")
except ImportError:
    print("Warning: pattern_question_generator.py not found - pattern generator disabled")
except Exception as e:
    print(f"Warning: Could not load pattern generator: {e}")

# ==================== PATTERNS QUESTION GENERATOR MODULE ====================
# Import and register visual patterns question generator routes
try:
    from patterns_question_generator import register_patterns_generator_routes

    # Create admin_required_api decorator for the patterns generator
    def admin_required_api_patterns(f):
        from functools import wraps
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return jsonify({'error': 'Login required'}), 401
            user = User.query.get(session['user_id'])
            if not user or user.role != 'admin':
                return jsonify({'error': 'Admin access required'}), 403
            return f(*args, **kwargs)
        return decorated_function

    register_patterns_generator_routes(app, db, Question, admin_required_api_patterns)
    print("✓ Patterns question generator loaded successfully")
except ImportError:
    print("Warning: patterns_question_generator.py not found - patterns generator disabled")
except Exception as e:
    print(f"Warning: Could not load patterns generator: {e}")

# ==================== COORDINATE GEOMETRY QUESTION GENERATOR MODULE ====================
# Import and register coordinate geometry question generator routes
try:
    from coordinate_question_generator import register_coordinate_generator_routes

    # Create admin_required_api decorator for the coordinate generator
    def admin_required_api_coordinate(f):
        from functools import wraps
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return jsonify({'error': 'Login required'}), 401
            user = User.query.get(session['user_id'])
            if not user or user.role != 'admin':
                return jsonify({'error': 'Admin access required'}), 403
            return f(*args, **kwargs)
        return decorated_function

    register_coordinate_generator_routes(app, db, Question, admin_required_api_coordinate)
    print("✓ Coordinate geometry question generator loaded successfully")
except ImportError:
    print("Warning: coordinate_question_generator.py not found - coordinate generator disabled")
except Exception as e:
    print(f"Warning: Could not load coordinate generator: {e}")


# ==================== SPEED, DISTANCE, TIME QUESTION GENERATOR MODULE ====================
# Import and register SDT question generator routes
try:
    from speed_distance_time_generator import register_sdt_generator_routes

    # Create admin_required_api decorator for the SDT generator
    def admin_required_api_sdt(f):
        from functools import wraps
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return jsonify({'error': 'Login required'}), 401
            user = User.query.get(session['user_id'])
            if not user or user.role != 'admin':
                return jsonify({'error': 'Admin access required'}), 403
            return f(*args, **kwargs)
        return decorated_function

    register_sdt_generator_routes(app, db, Question, admin_required_api_sdt)
    print("✓ Speed, Distance, Time question generator loaded successfully")
except ImportError:
    print("Warning: speed_distance_time_generator.py not found - SDT generator disabled")
except Exception as e:
    print(f"Warning: Could not load SDT generator: {e}")

# ==================== CURRENCY QUESTION GENERATOR MODULE ====================
# Import and register currency question generator routes
try:
    from currency_question_generator import register_currency_generator_routes

    # Create admin_required_api decorator for the currency generator
    def admin_required_api_currency(f):
        from functools import wraps
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return jsonify({'error': 'Login required'}), 401
            user = User.query.get(session['user_id'])
            if not user or user.role != 'admin':
                return jsonify({'error': 'Admin access required'}), 403
            return f(*args, **kwargs)
        return decorated_function

    register_currency_generator_routes(app, db, Question, admin_required_api_currency)
    print("✓ Currency question generator loaded successfully")
except ImportError:
    print("Warning: currency_question_generator.py not found - currency generator disabled")
except Exception as e:
    print(f"Warning: Could not load currency generator: {e}")





@app.route('/api/cron/raffle-auto-draw')
def api_cron_raffle_auto_draw():
    """Endpoint for PythonAnywhere scheduled task to trigger auto-draws

    Security: Uses a secret key to prevent unauthorized access.
    Set up in PythonAnywhere Scheduled Tasks to run every hour or at specific times.

    Example scheduled task command:
    curl "https://yourdomain.com/api/cron/raffle-auto-draw?key=YOUR_SECRET_KEY"
    """
    from sqlalchemy import text
    from routes.admin import check_and_run_auto_draws

    # Check for secret key
    provided_key = request.args.get('key', '')

    # Get the secret key from settings or environment
    try:
        secret_key = SystemSetting.get('raffle_cron_secret', '')
    except:
        secret_key = ''

    # If no key is set, allow access (for initial setup)
    # Once set, require the key
    if secret_key and provided_key != secret_key:
        return jsonify({'error': 'Unauthorized'}), 403

    results = check_and_run_auto_draws()

    # Log the run
    print(f"[CRON] Raffle auto-draw completed: {results.get('drawn', 0)} drawn, {results.get('skipped', 0)} skipped")

    return jsonify(results)









# =====================================================




# =====================================================
# REGISTER ADAPTIVE LEARNING ROUTES
# =====================================================
if ADAPTIVE_LEARNING_AVAILABLE:
    register_adaptive_routes(app, db)

# =====================================================
# REGISTER ADAPTIVE QUESTION SYSTEM ROUTES
# =====================================================
if ADAPTIVE_GENERATOR_AVAILABLE:
    register_adaptive_generator_routes(app, db)

if ADAPTIVE_QUIZ_ENGINE_AVAILABLE:
    register_adaptive_quiz_routes(app, db)

# =====================================================
# REGISTER TEAM PLAY ROUTES
# =====================================================
if TEAM_PLAY_AVAILABLE:
    register_team_play_routes(app, db)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
