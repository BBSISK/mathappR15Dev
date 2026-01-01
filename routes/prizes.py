# routes/prizes.py
# Prize shop, school rep, and prize PIN features for AgentMath
# Extracted from app.py for better maintainability
#
# Revision: 1.0.1
# Date: 2025-12-31
# Phase 11: Prizes extraction
#
# Fixes in 1.0.1:
# - Fixed url_for('student_app') → redirect('/app') 
# - Fixed url_for('dashboard') → redirect('/app') or url_for('teacher.teacher_dashboard')
# - These caused redirects to fail, sending users to wrong page
#
# Contains 18 routes for:
# - Student Prize Shop (7 routes) - /prizes, /api/prizes/*
# - School Rep Dashboard (7 routes) - /school-rep, /api/school-rep/*
# - Prize PIN System (4 routes) - /api/prize-pin/*

from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for, flash, current_app
from datetime import datetime, timedelta
from sqlalchemy import text

# Create blueprint
prizes_bp = Blueprint('prizes', __name__)

# Import database and models
from models import db, User, UserStats, Prize, PrizeRedemption, PrizeSchool, SchoolPrize, SchoolRequest, SystemSetting

# Import decorators from utils
from utils import login_required, guest_or_login_required, approved_required


# ==================== STUDENT PRIZE SHOP ROUTES ====================

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

# Student-facing prize shop and redemption

@prizes_bp.route('/prizes')
@login_required
@approved_required
def student_prize_shop():
    """Student prize shop page"""
    if not FEATURE_FLAGS.get('PRIZE_SYSTEM_ENABLED', False):
        flash('Prize shop is not available yet.', 'info')
        return redirect('/app')  # Hardcoded - student_app is in main app.py
    
    # Check if PIN verification is required
    from sqlalchemy import text
    threshold = int(SystemSetting.get('prize_pin_threshold', '2000'))
    
    # Get user's points and PIN status
    requires_pin = False
    has_pin = False
    pin_hint = ''
    points = 0
    
    if 'guest_code' in session:
        # Guest code user
        guest_code = session['guest_code']
        result = db.session.execute(
            text("SELECT total_score, prize_pin, prize_pin_hint FROM guest_users WHERE guest_code = :code"),
            {'code': guest_code}
        ).fetchone()
        
        if result:
            points = result[0] or 0
            has_pin = bool(result[1])
            pin_hint = result[2] or ''
    
    elif 'user_id' in session and 'is_guest' not in session:
        # Registered user
        user_id = session['user_id']
        stats = UserStats.query.filter_by(user_id=user_id).first()
        
        if stats:
            points = stats.total_points or 0
            has_pin = bool(stats.prize_pin)
            pin_hint = stats.prize_pin_hint or ''
    
    # Check if PIN is required
    if points >= threshold:
        requires_pin = True
        
        # Check if already verified in this session
        if not session.get('prize_pin_verified'):
            # Redirect to PIN verification page
            return render_template('prize_pin_required.html', 
                                   needs_setup=not has_pin,
                                   hint=pin_hint,
                                   points=points,
                                   threshold=threshold)

    return render_template('prize_shop.html')


@prizes_bp.route('/api/prizes/available')
@login_required
@approved_required
def get_available_prizes():
    """Get prizes available to the current student"""
    if not FEATURE_FLAGS.get('PRIZE_SYSTEM_ENABLED', False):
        return jsonify({'error': 'Prize system not enabled'}), 403

    user_id = session.get('user_id')

    # Get student's school (if set)
    user = User.query.get(user_id)
    school_id = session.get('prize_school_id')
    
    # If not in session, try to load from user's default
    if not school_id and user and not user.email.startswith('guest_'):
        try:
            from sqlalchemy import text
            result = db.session.execute(text("""
                SELECT default_school_id FROM users WHERE id = :user_id
            """), {'user_id': user_id}).fetchone()
            if result and result.default_school_id:
                school_id = result.default_school_id
                session['prize_school_id'] = school_id
        except:
            pass
    
    school = PrizeSchool.query.get(school_id) if school_id else None

    # Get student's points and level
    # Check if this is a repeat guest first
    if 'guest_code' in session:
        from sqlalchemy import text
        guest_code = session['guest_code']
        guest_stats = db.session.execute(text("""
            SELECT total_score, quizzes_completed
            FROM guest_users
            WHERE guest_code = :code
        """), {"code": guest_code}).fetchone()
        
        student_points = guest_stats.total_score if guest_stats else 0
        student_level = (student_points // 100) + 1 if guest_stats else 1
    else:
        # Regular users and casual guests use UserStats
        stats = UserStats.query.filter_by(user_id=user_id).first()
        
        # Create UserStats if it doesn't exist (e.g., for guest users)
        if not stats:
            stats = UserStats(user_id=user_id, total_points=0, level=1)
            db.session.add(stats)
            try:
                db.session.commit()
            except:
                db.session.rollback()
                # Try to fetch again in case of race condition
                stats = UserStats.query.filter_by(user_id=user_id).first()
        
        student_points = stats.total_points if stats else 0
        student_level = stats.level if stats else 1

    # Get global multiplier and level lock setting
    global_multiplier = float(SystemSetting.get('global_points_multiplier', 5.0))
    level_lock_enabled = SystemSetting.get('prize_level_lock_enabled', 'false') == 'true'

    # Get all active prizes
    prizes = Prize.query.filter_by(is_active=True).order_by(Prize.tier, Prize.sort_order).all()

    result = []
    for prize in prizes:
        if school:
            # Check if disabled for this school
            override = SchoolPrize.query.filter_by(school_id=school.id, prize_id=prize.id).first()
            if override and not override.is_enabled:
                continue
            point_cost = prize.get_cost_for_school(school)
            stock = override.stock_available if override else None
        else:
            # No school selected - use global multiplier only
            point_cost = int(prize.base_point_cost * global_multiplier)
            stock = None

        # Check level requirement
        min_level = prize.minimum_level or 0
        meets_level = student_level >= min_level if level_lock_enabled else True

        result.append({
            'id': prize.id,
            'name': prize.name,
            'description': prize.description,
            'emoji': prize.emoji,
            'tier': prize.tier,
            'prize_type': prize.prize_type,
            'point_cost': point_cost,
            'can_afford': student_points >= point_cost,
            'minimum_level': min_level,
            'meets_level': meets_level,
            'level_lock_enabled': level_lock_enabled,
            'stock_available': stock
        })

    # Get school-specific prizes if school is selected
    school_specific = []
    if school:
        custom_prizes = SchoolPrize.query.filter_by(
            school_id=school.id,
            prize_id=None,
            is_enabled=True
        ).all()

        for sp in custom_prizes:
            school_specific.append({
                'id': None,
                'school_prize_id': sp.id,
                'name': sp.custom_name,
                'description': sp.custom_description,
                'emoji': sp.custom_emoji or '🎁',
                'tier': 'school',
                'prize_type': 'physical',
                'point_cost': sp.point_cost_override,
                'can_afford': student_points >= (sp.point_cost_override or 0),
                'stock_available': sp.stock_available,
                'is_school_specific': True
            })

    return jsonify({
        'prizes': result,
        'school_prizes': school_specific,
        'student_points': student_points,
        'student_level': student_level,
        'level_lock_enabled': level_lock_enabled,
        'school': school.to_dict() if school else None,
        'has_school': school is not None
    })


@prizes_bp.route('/api/prizes/schools')
@login_required
@approved_required
def get_prize_schools_for_student():
    """Get list of approved schools for student to select"""
    schools = PrizeSchool.query.filter_by(status='approved').order_by(PrizeSchool.county, PrizeSchool.name).all()

    return jsonify({
        'schools': [{'id': s.id, 'name': s.name, 'county': s.county} for s in schools]
    })


@prizes_bp.route('/api/prizes/select-school', methods=['POST'])
@login_required
@approved_required
def select_prize_school():
    """Student selects their school for prize redemption"""
    data = request.get_json()
    school_id = data.get('school_id')

    if school_id:
        school = PrizeSchool.query.get(school_id)
        if not school or school.status != 'approved':
            return jsonify({'error': 'Invalid school'}), 400

        # Save to session for immediate use
        session['prize_school_id'] = school_id
        
        # Save to user profile for persistence (registered users only)
        user_id = session.get('user_id')
        user = User.query.get(user_id)
        if user and not user.email.startswith('guest_'):
            try:
                from sqlalchemy import text
                db.session.execute(text("""
                    UPDATE users 
                    SET default_school_id = :school_id 
                    WHERE id = :user_id
                """), {'school_id': school_id, 'user_id': user_id})
                db.session.commit()
            except:
                # Column might not exist yet, ignore
                pass
        
        return jsonify({'success': True, 'school': school.to_dict()})
    else:
        session.pop('prize_school_id', None)
        return jsonify({'success': True, 'school': None})


@prizes_bp.route('/api/prizes/request-school', methods=['POST'])
@login_required
@approved_required
def request_new_school():
    """Student requests to add their school to the programme"""
    data = request.get_json()
    user_id = session.get('user_id')

    # Check for existing pending request from this user
    existing = SchoolRequest.query.filter_by(
        requested_by=user_id,
        status='pending'
    ).first()

    if existing:
        return jsonify({
            'error': 'You already have a pending school request',
            'existing_request': existing.to_dict()
        }), 400

    school_request = SchoolRequest(
        school_name=data['school_name'],
        county=data.get('county'),
        suggested_rep_email=data.get('suggested_rep_email'),
        requested_by=user_id
    )

    db.session.add(school_request)
    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'School request submitted! An admin will review it soon.',
        'request': school_request.to_dict()
    })


@prizes_bp.route('/api/prizes/redeem', methods=['POST'])
@login_required
@approved_required
def redeem_prize():
    """Student redeems points for a prize"""
    if not FEATURE_FLAGS.get('PRIZE_SYSTEM_ENABLED', False):
        return jsonify({'error': 'Prize system not enabled'}), 403

    data = request.get_json()
    user_id = session.get('user_id')
    school_id = session.get('prize_school_id')

    # Must have school selected
    if not school_id:
        return jsonify({'error': 'Please select your school first'}), 400

    school = PrizeSchool.query.get(school_id)
    if not school or school.status != 'approved':
        return jsonify({'error': 'Invalid school'}), 400

    # Get prize
    prize_id = data.get('prize_id')
    school_prize_id = data.get('school_prize_id')

    if prize_id:
        prize = Prize.query.get(prize_id)
        if not prize or not prize.is_active:
            return jsonify({'error': 'Prize not available'}), 400
        point_cost = prize.get_cost_for_school(school)
        prize_name = prize.name
    elif school_prize_id:
        school_prize = SchoolPrize.query.get(school_prize_id)
        if not school_prize or school_prize.school_id != school_id or not school_prize.is_enabled:
            return jsonify({'error': 'Prize not available'}), 400
        point_cost = school_prize.point_cost_override
        prize_name = school_prize.custom_name
        prize = None
    else:
        return jsonify({'error': 'No prize specified'}), 400

    # Check student has enough points and level
    stats = UserStats.query.filter_by(user_id=user_id).first()
    if not stats or stats.total_points < point_cost:
        return jsonify({'error': 'Not enough points'}), 400

    # Check level requirement (only for global prizes)
    level_lock_enabled = SystemSetting.get('prize_level_lock_enabled', 'false') == 'true'
    if prize_id and level_lock_enabled and prize:
        min_level = prize.minimum_level or 0
        student_level = stats.level if stats else 1
        if student_level < min_level:
            return jsonify({'error': f'You need to reach Level {min_level} to redeem this prize'}), 400

    # Check stock if applicable
    if school_prize_id:
        sp = SchoolPrize.query.get(school_prize_id)
        if sp.stock_available is not None and sp.stock_available <= 0:
            return jsonify({'error': 'Prize out of stock'}), 400
    elif prize_id:
        override = SchoolPrize.query.filter_by(school_id=school_id, prize_id=prize_id).first()
        if override and override.stock_available is not None and override.stock_available <= 0:
            return jsonify({'error': 'Prize out of stock at your school'}), 400

    # Generate token
    token = generate_prize_token()

    # Calculate expiry
    expiry_days = int(SystemSetting.get('prize_expiry_days', 30))
    expires_at = datetime.utcnow() + timedelta(days=expiry_days)

    # Create redemption
    redemption = PrizeRedemption(
        user_id=user_id,
        school_id=school_id,
        prize_id=prize_id,
        school_prize_id=school_prize_id if not prize_id else None,
        token=token,
        points_spent=point_cost,
        status='pending',
        expires_at=expires_at
    )

    # Deduct points
    stats.total_points -= point_cost

    # Decrease stock if applicable
    if school_prize_id:
        sp = SchoolPrize.query.get(school_prize_id)
        if sp.stock_available is not None:
            sp.stock_available -= 1
    elif prize_id:
        override = SchoolPrize.query.filter_by(school_id=school_id, prize_id=prize_id).first()
        if override and override.stock_available is not None:
            override.stock_available -= 1

    db.session.add(redemption)
    db.session.commit()

    return jsonify({
        'success': True,
        'token': token,
        'prize_name': prize_name,
        'points_spent': point_cost,
        'points_remaining': stats.total_points,
        'expires_at': expires_at.isoformat(),
        'school_name': school.name,
        'message': f'Show token {token} to your school rep to collect your prize!'
    })


@prizes_bp.route('/api/prizes/my-redemptions')
@login_required
@approved_required
def get_my_redemptions():
    """Get student's prize redemption history"""
    user_id = session.get('user_id')

    redemptions = PrizeRedemption.query.filter_by(user_id=user_id).order_by(
        PrizeRedemption.redeemed_at.desc()
    ).all()

    return jsonify({
        'redemptions': [r.to_dict() for r in redemptions]
    })


# ==================== SCHOOL REP ROUTES ====================
# School representative dashboard for managing prize fulfilment

def school_rep_required(f):
    """Decorator to ensure user is a school rep"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'error': 'Please log in first'}), 401

        user_id = session['user_id']
        user = User.query.get(user_id)

        if not user:
            return jsonify({'error': 'User not found'}), 401

        # Check if user is a rep for any school
        school = PrizeSchool.query.filter_by(rep_user_id=user_id, status='approved').first()

        # Also allow admins and teachers
        if not school and user.role not in ['admin', 'teacher']:
            return jsonify({'error': 'You are not authorized as a school rep'}), 403

        return f(*args, **kwargs)
    return decorated_function


@prizes_bp.route('/school-rep')
@login_required
def school_rep_dashboard():
    """School rep dashboard page"""
    if not FEATURE_FLAGS.get('PRIZE_SYSTEM_ENABLED', False):
        flash('Prize system is not enabled.', 'warning')
        return redirect(url_for('teacher.teacher_dashboard'))

    user_id = session.get('user_id')
    user = User.query.get(user_id)

    # Check if user is a school rep
    school = PrizeSchool.query.filter_by(rep_user_id=user_id, status='approved').first()

    # Allow admin/teacher to access (they can select school)
    if not school and user.role not in ['admin', 'teacher']:
        flash('You are not registered as a school rep.', 'warning')
        return redirect('/app')  # Students go back to student app

    return render_template('school_rep_dashboard.html')


@prizes_bp.route('/api/school-rep/my-schools')
@login_required
def get_rep_schools():
    """Get schools this user is a rep for"""
    user_id = session.get('user_id')
    user = User.query.get(user_id)

    # Reps see their assigned schools
    schools = PrizeSchool.query.filter_by(rep_user_id=user_id, status='approved').all()

    # Admins see all schools
    if user.role == 'admin':
        schools = PrizeSchool.query.filter_by(status='approved').all()

    return jsonify({
        'schools': [s.to_dict() for s in schools],
        'is_admin': user.role == 'admin'
    })


@prizes_bp.route('/api/school-rep/pending/<int:school_id>')
@login_required
def get_pending_redemptions(school_id):
    """Get pending redemptions for a school"""
    user_id = session.get('user_id')
    user = User.query.get(user_id)

    # Verify access
    school = PrizeSchool.query.get_or_404(school_id)
    if school.rep_user_id != user_id and user.role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    redemptions = PrizeRedemption.query.filter_by(
        school_id=school_id,
        status='pending'
    ).order_by(PrizeRedemption.redeemed_at.desc()).all()

    return jsonify({
        'school': school.to_dict(),
        'redemptions': [r.to_dict(include_user=True) for r in redemptions],
        'count': len(redemptions)
    })


@prizes_bp.route('/api/school-rep/search-token', methods=['POST'])
@login_required
def search_token():
    """Search for a redemption by token"""
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    data = request.get_json()

    token = data.get('token', '').strip().upper()

    if not token:
        return jsonify({'error': 'Please enter a token'}), 400

    redemption = PrizeRedemption.query.filter_by(token=token).first()

    if not redemption:
        return jsonify({'error': 'Token not found', 'found': False}), 404

    # Verify access to this school
    school = redemption.school
    if school.rep_user_id != user_id and user.role != 'admin':
        return jsonify({'error': 'This token belongs to a different school', 'found': False}), 403

    return jsonify({
        'found': True,
        'redemption': redemption.to_dict(include_user=True),
        'school': school.to_dict()
    })


@prizes_bp.route('/api/school-rep/fulfil/<int:redemption_id>', methods=['POST'])
@login_required
def fulfil_redemption(redemption_id):
    """Mark a redemption as fulfilled"""
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    data = request.get_json() or {}

    redemption = PrizeRedemption.query.get_or_404(redemption_id)
    school = redemption.school

    # Verify access
    if school.rep_user_id != user_id and user.role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    if redemption.status != 'pending':
        return jsonify({'error': f'Redemption already {redemption.status}'}), 400

    # Mark as fulfilled
    redemption.status = 'fulfilled'
    redemption.fulfilled_at = datetime.utcnow()
    redemption.fulfilled_by = user_id
    redemption.fulfilment_notes = data.get('notes', '')

    db.session.commit()

    return jsonify({
        'success': True,
        'message': 'Prize marked as delivered!',
        'redemption': redemption.to_dict()
    })


@prizes_bp.route('/api/school-rep/history/<int:school_id>')
@login_required
def get_fulfilment_history(school_id):
    """Get fulfilment history for a school"""
    user_id = session.get('user_id')
    user = User.query.get(user_id)

    # Verify access
    school = PrizeSchool.query.get_or_404(school_id)
    if school.rep_user_id != user_id and user.role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    # Get fulfilled redemptions
    redemptions = PrizeRedemption.query.filter_by(
        school_id=school_id,
        status='fulfilled'
    ).order_by(PrizeRedemption.fulfilled_at.desc()).limit(50).all()

    return jsonify({
        'school': school.to_dict(),
        'redemptions': [r.to_dict(include_user=True) for r in redemptions]
    })


@prizes_bp.route('/api/school-rep/stats/<int:school_id>')
@login_required
def get_school_rep_stats(school_id):
    """Get stats for a school"""
    user_id = session.get('user_id')
    user = User.query.get(user_id)

    # Verify access
    school = PrizeSchool.query.get_or_404(school_id)
    if school.rep_user_id != user_id and user.role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    from sqlalchemy import func

    pending = PrizeRedemption.query.filter_by(school_id=school_id, status='pending').count()
    fulfilled = PrizeRedemption.query.filter_by(school_id=school_id, status='fulfilled').count()
    expired = PrizeRedemption.query.filter_by(school_id=school_id, status='expired').count()

    total_points = db.session.query(func.sum(PrizeRedemption.points_spent)).filter_by(
        school_id=school_id, status='fulfilled'
    ).scalar() or 0

    return jsonify({
        'school': school.to_dict(),
        'stats': {
            'pending': pending,
            'fulfilled': fulfilled,
            'expired': expired,
            'total_points_redeemed': total_points
        }
    })



# =============================================================================
# PRIZE SHOP PIN PROTECTION API
# =============================================================================

@prizes_bp.route('/api/prize-pin/status')
@login_required
def get_prize_pin_status():
    """Check if user needs PIN for Prize Shop access"""
    from sqlalchemy import text
    
    # Get threshold from settings
    threshold = int(SystemSetting.get('prize_pin_threshold', '2000'))
    
    # Determine user type and get their data
    if 'guest_code' in session:
        # Guest code user
        guest_code = session['guest_code']
        result = db.session.execute(
            text("SELECT total_score, prize_pin, prize_pin_hint FROM guest_users WHERE guest_code = :code"),
            {'code': guest_code}
        ).fetchone()
        
        if not result:
            return jsonify({'requires_pin': False, 'has_pin': False, 'points': 0, 'threshold': threshold})
        
        points = result[0] or 0
        has_pin = bool(result[1])
        hint = result[2] or ''
        
    elif 'user_id' in session:
        # Registered user
        user_id = session['user_id']
        stats = UserStats.query.filter_by(user_id=user_id).first()
        
        if not stats:
            return jsonify({'requires_pin': False, 'has_pin': False, 'points': 0, 'threshold': threshold})
        
        points = stats.total_points or 0
        has_pin = bool(stats.prize_pin)
        hint = stats.prize_pin_hint or ''
    else:
        # Casual guest - no PIN needed
        return jsonify({'requires_pin': False, 'has_pin': False, 'points': 0, 'threshold': threshold})
    
    requires_pin = points >= threshold
    
    return jsonify({
        'requires_pin': requires_pin,
        'has_pin': has_pin,
        'needs_setup': requires_pin and not has_pin,
        'hint': hint if has_pin else '',
        'points': points,
        'threshold': threshold
    })


@prizes_bp.route('/api/prize-pin/set', methods=['POST'])
@login_required
def set_prize_pin():
    """Set or update the Prize Shop PIN"""
    from sqlalchemy import text
    
    data = request.json or {}
    pin = data.get('pin', '').strip().lower()  # Store lowercase for case-insensitive matching
    hint = data.get('hint', '').strip()
    
    # Validate PIN
    if not pin or len(pin) < 2:
        return jsonify({'error': 'PIN must be at least 2 characters'}), 400
    
    if len(pin) > 50:
        return jsonify({'error': 'PIN is too long (max 50 characters)'}), 400
    
    # Validate hint
    if not hint or len(hint) < 2:
        return jsonify({'error': 'Please provide a hint (at least 2 characters)'}), 400
    
    if len(hint) > 100:
        return jsonify({'error': 'Hint is too long (max 100 characters)'}), 400
    
    # Determine user type and save PIN
    if 'guest_code' in session:
        # Guest code user
        guest_code = session['guest_code']
        db.session.execute(
            text("UPDATE guest_users SET prize_pin = :pin, prize_pin_hint = :hint WHERE guest_code = :code"),
            {'pin': pin, 'hint': hint, 'code': guest_code}
        )
        db.session.commit()
        
    elif 'user_id' in session:
        # Registered user
        user_id = session['user_id']
        stats = UserStats.query.filter_by(user_id=user_id).first()
        
        if not stats:
            return jsonify({'error': 'User stats not found'}), 404
        
        stats.prize_pin = pin
        stats.prize_pin_hint = hint
        db.session.commit()
    else:
        return jsonify({'error': 'Not logged in'}), 401
    
    return jsonify({
        'success': True,
        'message': 'PIN set successfully! Remember your hint: ' + hint
    })


@prizes_bp.route('/api/prize-pin/verify', methods=['POST'])
@login_required
def verify_prize_pin():
    """Verify the Prize Shop PIN"""
    from sqlalchemy import text
    
    data = request.json or {}
    entered_pin = data.get('pin', '').strip().lower()  # Compare lowercase
    
    if not entered_pin:
        return jsonify({'success': False, 'error': 'Please enter your PIN'}), 400
    
    # Get stored PIN based on user type
    stored_pin = None
    
    if 'guest_code' in session:
        guest_code = session['guest_code']
        result = db.session.execute(
            text("SELECT prize_pin FROM guest_users WHERE guest_code = :code"),
            {'code': guest_code}
        ).fetchone()
        stored_pin = result[0] if result else None
        
    elif 'user_id' in session:
        user_id = session['user_id']
        stats = UserStats.query.filter_by(user_id=user_id).first()
        stored_pin = stats.prize_pin if stats else None
    
    if not stored_pin:
        return jsonify({'success': False, 'error': 'No PIN set'}), 400
    
    # Compare PINs (case-insensitive)
    if entered_pin == stored_pin.lower():
        # Store verification in session (expires with session)
        session['prize_pin_verified'] = True
        return jsonify({
            'success': True,
            'message': 'PIN verified! Welcome to the Prize Shop.'
        })
    else:
        return jsonify({
            'success': False,
            'error': 'Incorrect PIN. Check your hint and try again.'
        }), 401


@prizes_bp.route('/api/prize-pin/reset', methods=['POST'])
@login_required
def reset_prize_pin():
    """Reset/change the Prize Shop PIN (requires knowing current PIN)"""
    from sqlalchemy import text
    
    data = request.json or {}
    current_pin = data.get('current_pin', '').strip().lower()
    new_pin = data.get('new_pin', '').strip().lower()
    new_hint = data.get('new_hint', '').strip()
    
    # Validate inputs
    if not current_pin:
        return jsonify({'error': 'Current PIN is required'}), 400
    
    if not new_pin or len(new_pin) < 2:
        return jsonify({'error': 'New PIN must be at least 2 characters'}), 400
    
    if not new_hint or len(new_hint) < 2:
        return jsonify({'error': 'Please provide a hint for your new PIN'}), 400
    
    # Get and verify current PIN
    stored_pin = None
    
    if 'guest_code' in session:
        guest_code = session['guest_code']
        result = db.session.execute(
            text("SELECT prize_pin FROM guest_users WHERE guest_code = :code"),
            {'code': guest_code}
        ).fetchone()
        stored_pin = result[0] if result else None
        
        if stored_pin and current_pin == stored_pin.lower():
            db.session.execute(
                text("UPDATE guest_users SET prize_pin = :pin, prize_pin_hint = :hint WHERE guest_code = :code"),
                {'pin': new_pin, 'hint': new_hint, 'code': guest_code}
            )
            db.session.commit()
        else:
            return jsonify({'error': 'Current PIN is incorrect'}), 401
            
    elif 'user_id' in session:
        user_id = session['user_id']
        stats = UserStats.query.filter_by(user_id=user_id).first()
        stored_pin = stats.prize_pin if stats else None
        
        if stored_pin and current_pin == stored_pin.lower():
            stats.prize_pin = new_pin
            stats.prize_pin_hint = new_hint
            db.session.commit()
        else:
            return jsonify({'error': 'Current PIN is incorrect'}), 401
    else:
        return jsonify({'error': 'Not logged in'}), 401
    
    return jsonify({
        'success': True,
        'message': 'PIN changed successfully!'
    })


