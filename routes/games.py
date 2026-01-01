# routes/games.py
# Gaming/Challenge features for AgentMath
# Extracted from app.py for better maintainability
#
# Revision: 1.0.0
# Date: 2025-12-31
# Phase 9: Games/Challenges extraction
#
# Contains 18 routes for:
# - Clock Challenge (Beat the Clock) - 6 routes
# - Racing Car Challenge - 12 routes
#   - Phase 1: Basic car building
#   - Phase 2: Upgrade shop
#   - Phase 3: Weekly races & championships

from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for, flash
from datetime import datetime, timedelta
import random

# Create blueprint
games_bp = Blueprint('games', __name__)

# Import database and models
from models import db, User, UserStats, SystemSetting

# Import decorators from utils
from utils import login_required, guest_or_login_required, approved_required

# Import badge checking
from utils import check_and_award_badges


# =====================================================
# CLOCK CHALLENGE ROUTES (Beat the Clock) - Rev 3.0
# =====================================================

# Clock challenge configuration
CLOCK_CHALLENGE_CONFIG = {
    # Time allowed per level (in seconds)
    'time_allowed': {
        6: 120,   # 2 minutes
        7: 150,   # 2.5 minutes
        8: 180,   # 3 minutes
        9: 210,   # 3.5 minutes
        10: 240,  # 4 minutes
    },
    # Wrong answer penalty (in seconds)
    'wrong_penalty': {
        6: 10,
        7: 10,
        8: 15,
        9: 15,
        10: 20,
    },
    # Bonus tiers (percentage of time remaining)
    'bonus_tiers': {
        'lightning': {'min_percent': 40, 'points': 50},
        'fast': {'min_percent': 20, 'points': 35},
        'on_time': {'min_percent': 1, 'points': 20},
    }
}


@games_bp.route('/api/clock-challenge/intro-seen', methods=['GET'])
@guest_or_login_required
def check_clock_intro_seen():
    """Check if user has seen the clock challenge intro"""
    from sqlalchemy import text
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    try:
        if guest_code:
            result = db.session.execute(text(
                "SELECT 1 FROM clock_challenge_intro_seen WHERE guest_code = :code"
            ), {'code': guest_code}).fetchone()
        elif user_id:
            result = db.session.execute(text(
                "SELECT 1 FROM clock_challenge_intro_seen WHERE user_id = :uid"
            ), {'uid': user_id}).fetchone()
        else:
            return jsonify({'seen': False})
        
        return jsonify({'seen': result is not None})
    except Exception as e:
        print(f"Error checking clock intro: {e}")
        return jsonify({'seen': False})


@games_bp.route('/api/clock-challenge/intro-seen', methods=['POST'])
@guest_or_login_required
def mark_clock_intro_seen():
    """Mark that user has seen the clock challenge intro"""
    from sqlalchemy import text
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    try:
        if guest_code:
            db.session.execute(text("""
                INSERT OR IGNORE INTO clock_challenge_intro_seen (guest_code)
                VALUES (:code)
            """), {'code': guest_code})
        elif user_id:
            db.session.execute(text("""
                INSERT OR IGNORE INTO clock_challenge_intro_seen (user_id)
                VALUES (:uid)
            """), {'uid': user_id})
        
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        db.session.rollback()
        print(f"Error marking clock intro seen: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@games_bp.route('/api/clock-challenge/check', methods=['GET'])
@guest_or_login_required
def check_clock_challenge():
    """Check if clock challenge is available for user at given topic/level"""
    from sqlalchemy import text
    
    topic = request.args.get('topic')
    level = request.args.get('level', type=int)
    
    if not topic or not level:
        return jsonify({'error': 'Missing topic or level'}), 400
    
    if level < 6 or level > 10:
        return jsonify({'available': False, 'reason': 'Clock challenge only for levels 6-10'})
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    try:
        if guest_code:
            state = db.session.execute(text("""
                SELECT clock_available, clock_completed, attempts, best_time_remaining
                FROM clock_challenge_state 
                WHERE guest_code = :code AND topic = :topic AND level = :level
            """), {'code': guest_code, 'topic': topic, 'level': level}).fetchone()
        elif user_id:
            state = db.session.execute(text("""
                SELECT clock_available, clock_completed, attempts, best_time_remaining
                FROM clock_challenge_state 
                WHERE user_id = :uid AND topic = :topic AND level = :level
            """), {'uid': user_id, 'topic': topic, 'level': level}).fetchone()
        else:
            return jsonify({'available': False, 'reason': 'Not authenticated'})
        
        if not state:
            available, completed, attempts, best_time = True, False, 0, None
        else:
            available, completed, attempts, best_time = bool(state[0]), bool(state[1]), state[2] or 0, state[3]
        
        config = {
            'time_allowed': CLOCK_CHALLENGE_CONFIG['time_allowed'].get(level, 180),
            'wrong_penalty': CLOCK_CHALLENGE_CONFIG['wrong_penalty'].get(level, 15),
            'bonus_tiers': CLOCK_CHALLENGE_CONFIG['bonus_tiers']
        }
        
        return jsonify({
            'available': available, 'completed': completed, 'attempts': attempts,
            'best_time_remaining': best_time, 'config': config
        })
        
    except Exception as e:
        print(f"Error checking clock challenge: {e}")
        return jsonify({'available': False, 'error': str(e)}), 500


@games_bp.route('/api/clock-challenge/start', methods=['POST'])
@guest_or_login_required
def start_clock_challenge():
    """Start a clock challenge session"""
    from sqlalchemy import text
    import uuid
    
    data = request.get_json()
    topic = data.get('topic')
    level = int(data.get('level', 0))
    
    if not topic or level < 6 or level > 10:
        return jsonify({'error': 'Invalid topic or level'}), 400
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    session_id = str(uuid.uuid4())[:8]
    time_allowed = CLOCK_CHALLENGE_CONFIG['time_allowed'].get(level, 180)
    
    try:
        if guest_code:
            db.session.execute(text("""
                INSERT INTO clock_challenge_timing (guest_code, topic, level, session_id, time_allowed, started_at)
                VALUES (:code, :topic, :level, :sid, :time, :now)
            """), {'code': guest_code, 'topic': topic, 'level': level, 'sid': session_id, 'time': time_allowed, 'now': datetime.utcnow()})
            
            db.session.execute(text("""
                INSERT INTO clock_challenge_state (guest_code, topic, level, clock_available, attempts, last_attempt_at, updated_at)
                VALUES (:code, :topic, :level, 0, 1, :now, :now)
                ON CONFLICT(guest_code, topic, level) DO UPDATE SET clock_available = 0, attempts = attempts + 1, last_attempt_at = :now, updated_at = :now
            """), {'code': guest_code, 'topic': topic, 'level': level, 'now': datetime.utcnow()})
        elif user_id:
            db.session.execute(text("""
                INSERT INTO clock_challenge_timing (user_id, topic, level, session_id, time_allowed, started_at)
                VALUES (:uid, :topic, :level, :sid, :time, :now)
            """), {'uid': user_id, 'topic': topic, 'level': level, 'sid': session_id, 'time': time_allowed, 'now': datetime.utcnow()})
            
            db.session.execute(text("""
                INSERT INTO clock_challenge_state (user_id, topic, level, clock_available, attempts, last_attempt_at, updated_at)
                VALUES (:uid, :topic, :level, 0, 1, :now, :now)
                ON CONFLICT(user_id, topic, level) DO UPDATE SET clock_available = 0, attempts = attempts + 1, last_attempt_at = :now, updated_at = :now
            """), {'uid': user_id, 'topic': topic, 'level': level, 'now': datetime.utcnow()})
        
        db.session.commit()
        print(f"⏱️ Clock challenge started: {topic} L{level} - Session {session_id}")
        
        return jsonify({
            'success': True, 'session_id': session_id,
            'time_allowed': time_allowed,
            'wrong_penalty': CLOCK_CHALLENGE_CONFIG['wrong_penalty'].get(level, 15)
        })
        
    except Exception as e:
        db.session.rollback()
        print(f"Error starting clock challenge: {e}")
        return jsonify({'error': str(e)}), 500


@games_bp.route('/api/clock-challenge/complete', methods=['POST'])
@guest_or_login_required
def complete_clock_challenge():
    """Complete (or timeout) a clock challenge, award bonus if successful"""
    from sqlalchemy import text
    
    data = request.get_json()
    topic, level, session_id = data.get('topic'), int(data.get('level', 0)), data.get('session_id')
    time_remaining = max(0, int(data.get('time_remaining', 0)))
    questions_answered = data.get('questions_answered', 0)
    questions_correct = data.get('questions_correct', 0)
    penalties_applied = data.get('penalties_applied', 0)
    completed = data.get('completed', False)
    
    time_allowed = CLOCK_CHALLENGE_CONFIG['time_allowed'].get(level, 180)
    time_used = time_allowed - time_remaining
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    # Calculate bonus
    bonus_tier, bonus_points = None, 0
    if completed and time_remaining > 0:
        time_percent = (time_remaining / time_allowed) * 100
        if time_percent >= 40:
            bonus_tier, bonus_points = 'lightning', 50
        elif time_percent >= 20:
            bonus_tier, bonus_points = 'fast', 35
        elif time_percent >= 1:
            bonus_tier, bonus_points = 'on_time', 20
    
    try:
        # Update timing record
        update_params = {
            'qa': questions_answered, 'qc': questions_correct, 'used': time_used,
            'remaining': time_remaining, 'penalties': penalties_applied,
            'completed': 1 if completed else 0, 'tier': bonus_tier, 'bonus': bonus_points,
            'now': datetime.utcnow(), 'sid': session_id
        }
        
        if guest_code:
            update_params['code'] = guest_code
            db.session.execute(text("""
                UPDATE clock_challenge_timing SET questions_answered = :qa, questions_correct = :qc,
                time_used = :used, time_remaining = :remaining, wrong_answer_penalties = :penalties,
                completed = :completed, bonus_tier = :tier, bonus_points = :bonus, ended_at = :now
                WHERE guest_code = :code AND session_id = :sid
            """), update_params)
            
            if completed:
                db.session.execute(text("""
                    UPDATE clock_challenge_state SET clock_completed = 1, clock_available = 1,
                    best_time_remaining = CASE WHEN best_time_remaining IS NULL OR :remaining > best_time_remaining THEN :remaining ELSE best_time_remaining END,
                    best_bonus_earned = CASE WHEN best_bonus_earned IS NULL OR :bonus > best_bonus_earned THEN :bonus ELSE best_bonus_earned END,
                    first_completed_at = COALESCE(first_completed_at, :now), updated_at = :now
                    WHERE guest_code = :code AND topic = :topic AND level = :level
                """), {'remaining': time_remaining, 'bonus': bonus_points, 'now': datetime.utcnow(), 'code': guest_code, 'topic': topic, 'level': level})
                
                if bonus_points > 0:
                    db.session.execute(text("UPDATE guest_users SET total_score = total_score + :bonus WHERE guest_code = :code"), {'bonus': bonus_points, 'code': guest_code})
            else:
                db.session.execute(text("UPDATE clock_challenge_state SET clock_available = 0, updated_at = :now WHERE guest_code = :code AND topic = :topic AND level = :level"), {'now': datetime.utcnow(), 'code': guest_code, 'topic': topic, 'level': level})
                
        elif user_id:
            update_params['uid'] = user_id
            db.session.execute(text("""
                UPDATE clock_challenge_timing SET questions_answered = :qa, questions_correct = :qc,
                time_used = :used, time_remaining = :remaining, wrong_answer_penalties = :penalties,
                completed = :completed, bonus_tier = :tier, bonus_points = :bonus, ended_at = :now
                WHERE user_id = :uid AND session_id = :sid
            """), update_params)
            
            if completed:
                db.session.execute(text("""
                    UPDATE clock_challenge_state SET clock_completed = 1, clock_available = 1,
                    best_time_remaining = CASE WHEN best_time_remaining IS NULL OR :remaining > best_time_remaining THEN :remaining ELSE best_time_remaining END,
                    best_bonus_earned = CASE WHEN best_bonus_earned IS NULL OR :bonus > best_bonus_earned THEN :bonus ELSE best_bonus_earned END,
                    first_completed_at = COALESCE(first_completed_at, :now), updated_at = :now
                    WHERE user_id = :uid AND topic = :topic AND level = :level
                """), {'remaining': time_remaining, 'bonus': bonus_points, 'now': datetime.utcnow(), 'uid': user_id, 'topic': topic, 'level': level})
                
                if bonus_points > 0:
                    stats = UserStats.query.filter_by(user_id=user_id).first()
                    if stats:
                        stats.total_points += bonus_points
            else:
                db.session.execute(text("UPDATE clock_challenge_state SET clock_available = 0, updated_at = :now WHERE user_id = :uid AND topic = :topic AND level = :level"), {'now': datetime.utcnow(), 'uid': user_id, 'topic': topic, 'level': level})
        
        db.session.commit()
        
        result_msg = f"⏱️ Clock challenge {'COMPLETED' if completed else 'TIMEOUT'}: {topic} L{level}"
        if bonus_points > 0:
            result_msg += f" - {bonus_tier.upper()} +{bonus_points} bonus!"
        print(result_msg)
        
        return jsonify({'success': True, 'completed': completed, 'bonus_tier': bonus_tier, 'bonus_points': bonus_points, 'time_remaining': time_remaining, 'time_used': time_used})
        
    except Exception as e:
        db.session.rollback()
        print(f"Error completing clock challenge: {e}")
        return jsonify({'error': str(e)}), 500


@games_bp.route('/api/clock-challenge/unlock', methods=['POST'])
@guest_or_login_required
def unlock_clock_challenge():
    """Re-enable clock challenge for a level after normal completion"""
    from sqlalchemy import text
    
    data = request.get_json()
    topic, level = data.get('topic'), int(data.get('level', 0))
    
    if level < 6 or level > 10:
        return jsonify({'success': True, 'message': 'Not a clock level'})
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    try:
        if guest_code:
            db.session.execute(text("""
                INSERT INTO clock_challenge_state (guest_code, topic, level, clock_available, updated_at)
                VALUES (:code, :topic, :level, 1, :now)
                ON CONFLICT(guest_code, topic, level) DO UPDATE SET clock_available = 1, updated_at = :now
            """), {'code': guest_code, 'topic': topic, 'level': level, 'now': datetime.utcnow()})
        elif user_id:
            db.session.execute(text("""
                INSERT INTO clock_challenge_state (user_id, topic, level, clock_available, updated_at)
                VALUES (:uid, :topic, :level, 1, :now)
                ON CONFLICT(user_id, topic, level) DO UPDATE SET clock_available = 1, updated_at = :now
            """), {'uid': user_id, 'topic': topic, 'level': level, 'now': datetime.utcnow()})
        
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500



# =====================================================
# RACING CAR CHALLENGE ROUTES
# =====================================================

@games_bp.route('/racing-car')
@guest_or_login_required
def racing_car_page():
    """Racing Car 3D viewer page"""
    return render_template('racing_car.html')


@games_bp.route('/api/racing-car/status')
@guest_or_login_required
def get_racing_car_status():
    """Get the user's racing car status including parts unlocked, points, next part"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    # Get current points
    current_points = 0
    if guest_code:
        result = db.session.execute(text(
            "SELECT total_score FROM guest_users WHERE guest_code = :code"
        ), {"code": guest_code}).fetchone()
        current_points = result[0] if result else 0
    elif user_id:
        stats = UserStats.query.filter_by(user_id=user_id).first()
        current_points = stats.total_points if stats else 0
    
    # Get or create user's race car record
    try:
        if guest_code:
            car = db.session.execute(text(
                "SELECT id, user_id, guest_code, parts_unlocked, highest_points_seen, car_name, primary_color, secondary_color FROM user_race_cars WHERE guest_code = :code"
            ), {"code": guest_code}).fetchone()
            
            if not car:
                db.session.execute(text("""
                    INSERT INTO user_race_cars (guest_code, parts_unlocked, highest_points_seen, created_at, updated_at)
                    VALUES (:code, 0, :points, :now, :now)
                """), {"code": guest_code, "points": current_points, "now": datetime.utcnow()})
                db.session.commit()
                car = db.session.execute(text(
                    "SELECT id, user_id, guest_code, parts_unlocked, highest_points_seen, car_name, primary_color, secondary_color FROM user_race_cars WHERE guest_code = :code"
                ), {"code": guest_code}).fetchone()
        else:
            car = db.session.execute(text(
                "SELECT id, user_id, guest_code, parts_unlocked, highest_points_seen, car_name, primary_color, secondary_color FROM user_race_cars WHERE user_id = :uid"
            ), {"uid": user_id}).fetchone()
            
            if not car:
                db.session.execute(text("""
                    INSERT INTO user_race_cars (user_id, parts_unlocked, highest_points_seen, created_at, updated_at)
                    VALUES (:uid, 0, :points, :now, :now)
                """), {"uid": user_id, "points": current_points, "now": datetime.utcnow()})
                db.session.commit()
                car = db.session.execute(text(
                    "SELECT id, user_id, guest_code, parts_unlocked, highest_points_seen, car_name, primary_color, secondary_color FROM user_race_cars WHERE user_id = :uid"
                ), {"uid": user_id}).fetchone()
    except Exception as e:
        return jsonify({'error': f'Database error: {str(e)}', 'parts_unlocked': 0, 'current_points': current_points, 'all_parts': []})
    
    car_columns = ['id', 'user_id', 'guest_code', 'parts_unlocked', 'highest_points_seen', 'car_name', 'primary_color', 'secondary_color']
    car_dict = dict(zip(car_columns, car)) if car else {}
    
    # Calculate parts that should be unlocked (1 part per 1000 points)
    parts_should_have = min(50, current_points // 1000)
    current_parts = car_dict.get('parts_unlocked', 0)
    
    # Check for new unlocks
    new_unlocks = []
    if parts_should_have > current_parts:
        try:
            new_parts = db.session.execute(text("""
                SELECT part_number, part_name, category, description, points_required
                FROM car_parts
                WHERE part_number > :current AND part_number <= :new
                ORDER BY part_number
            """), {"current": current_parts, "new": parts_should_have}).fetchall()
            
            for part in new_parts:
                new_unlocks.append({
                    'part_number': part[0],
                    'part_name': part[1],
                    'category': part[2],
                    'description': part[3],
                    'points_required': part[4]
                })
                
                # Record unlock
                try:
                    if guest_code:
                        db.session.execute(text("""
                            INSERT INTO car_part_unlocks (guest_code, part_id, unlocked_at, points_at_unlock)
                            SELECT :code, id, :now, :points FROM car_parts WHERE part_number = :pnum
                        """), {"code": guest_code, "now": datetime.utcnow(), "points": current_points, "pnum": part[0]})
                    else:
                        db.session.execute(text("""
                            INSERT INTO car_part_unlocks (user_id, part_id, unlocked_at, points_at_unlock)
                            SELECT :uid, id, :now, :points FROM car_parts WHERE part_number = :pnum
                        """), {"uid": user_id, "now": datetime.utcnow(), "points": current_points, "pnum": part[0]})
                except:
                    pass
            
            # Update car record
            if guest_code:
                db.session.execute(text("""
                    UPDATE user_race_cars 
                    SET parts_unlocked = :parts, highest_points_seen = :points, updated_at = :now
                    WHERE guest_code = :code
                """), {"parts": parts_should_have, "points": current_points, "now": datetime.utcnow(), "code": guest_code})
            else:
                db.session.execute(text("""
                    UPDATE user_race_cars 
                    SET parts_unlocked = :parts, highest_points_seen = :points, updated_at = :now
                    WHERE user_id = :uid
                """), {"parts": parts_should_have, "points": current_points, "now": datetime.utcnow(), "uid": user_id})
            
            db.session.commit()
            current_parts = parts_should_have
        except Exception as e:
            print(f"Error updating parts: {e}")
    
    # Get next part
    next_part = None
    if current_parts < 50:
        try:
            next_result = db.session.execute(text("""
                SELECT part_number, part_name, category, description, points_required
                FROM car_parts WHERE part_number = :next_num
            """), {"next_num": current_parts + 1}).fetchone()
            
            if next_result:
                next_part = {
                    'part_number': next_result[0],
                    'part_name': next_result[1],
                    'category': next_result[2],
                    'description': next_result[3],
                    'points_required': next_result[4]
                }
        except:
            pass
    
    # Get all parts
    all_parts_list = []
    try:
        all_parts = db.session.execute(text("""
            SELECT part_number, part_name, category, description, points_required
            FROM car_parts ORDER BY part_number
        """)).fetchall()
        
        all_parts_list = [{
            'part_number': p[0],
            'part_name': p[1],
            'category': p[2],
            'description': p[3],
            'points_required': p[4]
        } for p in all_parts]
    except:
        pass
    
    return jsonify({
        'parts_unlocked': current_parts,
        'current_points': current_points,
        'car_name': car_dict.get('car_name') or 'Your F1 Car',
        'primary_color': car_dict.get('primary_color', '#e10600'),
        'secondary_color': car_dict.get('secondary_color', '#1e1e1e'),
        'next_part': next_part,
        'new_unlocks': new_unlocks,
        'all_parts': all_parts_list,
        'completion_percentage': round((current_parts / 50) * 100, 1)
    })


@games_bp.route('/api/racing-car/parts')
@guest_or_login_required
def get_racing_car_parts():
    """Get the full catalog of car parts"""
    from sqlalchemy import text
    
    try:
        parts = db.session.execute(text("""
            SELECT part_number, part_name, category, description, points_required, model_component
            FROM car_parts ORDER BY part_number
        """)).fetchall()
        
        return jsonify({
            'parts': [{
                'part_number': p[0],
                'part_name': p[1],
                'category': p[2],
                'description': p[3],
                'points_required': p[4],
                'model_component': p[5]
            } for p in parts]
        })
    except Exception as e:
        return jsonify({'error': str(e), 'parts': []})


@games_bp.route('/api/racing-car/customize', methods=['POST'])
@guest_or_login_required
def customize_racing_car():
    """Update car name and colors"""
    from sqlalchemy import text
    import re
    
    data = request.get_json()
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    car_name = data.get('car_name', '')[:100]
    primary_color = data.get('primary_color', '#e10600')
    secondary_color = data.get('secondary_color', '#1e1e1e')
    
    hex_pattern = re.compile(r'^#[0-9A-Fa-f]{6}$')
    if not hex_pattern.match(primary_color):
        primary_color = '#e10600'
    if not hex_pattern.match(secondary_color):
        secondary_color = '#1e1e1e'
    
    try:
        if guest_code:
            db.session.execute(text("""
                UPDATE user_race_cars 
                SET car_name = :name, primary_color = :pc, secondary_color = :sc, updated_at = :now
                WHERE guest_code = :code
            """), {"name": car_name, "pc": primary_color, "sc": secondary_color, 
                   "now": datetime.utcnow(), "code": guest_code})
        else:
            db.session.execute(text("""
                UPDATE user_race_cars 
                SET car_name = :name, primary_color = :pc, secondary_color = :sc, updated_at = :now
                WHERE user_id = :uid
            """), {"name": car_name, "pc": primary_color, "sc": secondary_color,
                   "now": datetime.utcnow(), "uid": user_id})
        
        db.session.commit()
        return jsonify({'success': True, 'message': 'Car customization saved'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# =====================================================
# END RACING CAR ROUTES

# =====================================================
# RACING CAR PHASE 2 - UPGRADE SHOP ROUTES
# =====================================================

UPGRADE_BUDGET = 20000  # Maximum points user can spend on upgrades


@games_bp.route('/api/racing-car/upgrades')
@guest_or_login_required
def get_racing_car_upgrades():
    """Get all available upgrades and user's current purchases"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    # TEST MODE: Allow ?test=upgrades to bypass car completion check
    test_mode = request.args.get('test') == 'upgrades'
    
    # Check if car is complete (50 parts)
    try:
        if guest_code:
            car = db.session.execute(text(
                "SELECT parts_unlocked, upgrade_budget_used FROM user_race_cars WHERE guest_code = :code"
            ), {"code": guest_code}).fetchone()
        else:
            car = db.session.execute(text(
                "SELECT parts_unlocked, upgrade_budget_used FROM user_race_cars WHERE user_id = :uid"
            ), {"uid": user_id}).fetchone()
        
        if not car:
            return jsonify({'error': 'No car found', 'car_complete': False})
        
        parts_unlocked = car[0] or 0
        budget_used = car[1] or 0
        
        # Allow access if car complete OR test mode
        if parts_unlocked < 50 and not test_mode:
            return jsonify({
                'car_complete': False,
                'parts_unlocked': parts_unlocked,
                'parts_needed': 50 - parts_unlocked,
                'message': f'Complete your car first! {50 - parts_unlocked} parts remaining.'
            })
    except Exception as e:
        return jsonify({'error': str(e), 'car_complete': False})
    
    # Get all upgrades
    try:
        upgrades = db.session.execute(text("""
            SELECT id, upgrade_number, category, name, description, cost, performance_boost, icon, stat_key
            FROM car_upgrades ORDER BY category, upgrade_number
        """)).fetchall()
    except Exception as e:
        return jsonify({'error': f'Failed to load upgrades: {str(e)}', 'car_complete': True})
    
    # Get user's purchased upgrades
    try:
        if guest_code:
            purchased = db.session.execute(text(
                "SELECT upgrade_id FROM user_car_upgrades WHERE guest_code = :code"
            ), {"code": guest_code}).fetchall()
        else:
            purchased = db.session.execute(text(
                "SELECT upgrade_id FROM user_car_upgrades WHERE user_id = :uid"
            ), {"uid": user_id}).fetchall()
        purchased_ids = [p[0] for p in purchased]
    except:
        purchased_ids = []
    
    # Format upgrades by category
    upgrades_by_category = {}
    total_boost = 0
    
    for u in upgrades:
        cat = u[2]
        if cat not in upgrades_by_category:
            upgrades_by_category[cat] = []
        
        is_owned = u[0] in purchased_ids
        if is_owned:
            total_boost += u[6]
        
        upgrades_by_category[cat].append({
            'id': u[0], 'number': u[1], 'category': u[2], 'name': u[3],
            'description': u[4], 'cost': u[5], 'boost': u[6],
            'icon': u[7], 'stat_key': u[8], 'owned': is_owned
        })
    
    return jsonify({
        'car_complete': True,
        'budget_total': UPGRADE_BUDGET,
        'budget_used': budget_used,
        'budget_remaining': UPGRADE_BUDGET - budget_used,
        'total_performance_boost': total_boost,
        'upgrades_by_category': upgrades_by_category,
        'purchased_count': len(purchased_ids),
        'total_upgrades': len(upgrades)
    })


@games_bp.route('/api/racing-car/upgrades/buy', methods=['POST'])
@guest_or_login_required
def buy_racing_car_upgrade():
    """Purchase an upgrade"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    data = request.get_json()
    upgrade_id = data.get('upgrade_id')
    test_mode = data.get('test_mode', False)
    
    if not upgrade_id:
        return jsonify({'error': 'No upgrade specified'}), 400
    
    try:
        upgrade = db.session.execute(text(
            "SELECT id, name, cost, performance_boost FROM car_upgrades WHERE id = :uid"
        ), {"uid": upgrade_id}).fetchone()
        
        if not upgrade:
            return jsonify({'error': 'Upgrade not found'}), 404
        
        upgrade_cost = upgrade[2]
        
        if guest_code:
            car = db.session.execute(text(
                "SELECT parts_unlocked, upgrade_budget_used FROM user_race_cars WHERE guest_code = :code"
            ), {"code": guest_code}).fetchone()
        else:
            car = db.session.execute(text(
                "SELECT parts_unlocked, upgrade_budget_used FROM user_race_cars WHERE user_id = :uid"
            ), {"uid": user_id}).fetchone()
        
        # Allow if car complete OR test mode
        if not car or (car[0] < 50 and not test_mode):
            return jsonify({'error': 'Car must be complete to buy upgrades'}), 400
        
        budget_used = car[1] or 0
        budget_remaining = UPGRADE_BUDGET - budget_used
        
        if upgrade_cost > budget_remaining:
            return jsonify({'error': 'Not enough budget', 'cost': upgrade_cost, 'budget_remaining': budget_remaining}), 400
        
        # Check if already owned
        if guest_code:
            existing = db.session.execute(text(
                "SELECT id FROM user_car_upgrades WHERE guest_code = :code AND upgrade_id = :uid"
            ), {"code": guest_code, "uid": upgrade_id}).fetchone()
        else:
            existing = db.session.execute(text(
                "SELECT id FROM user_car_upgrades WHERE user_id = :uid AND upgrade_id = :upid"
            ), {"uid": user_id, "upid": upgrade_id}).fetchone()
        
        if existing:
            return jsonify({'error': 'Upgrade already owned'}), 400
        
        # Purchase
        if guest_code:
            db.session.execute(text("""
                INSERT INTO user_car_upgrades (guest_code, upgrade_id, purchased_at, points_spent)
                VALUES (:code, :uid, :now, :cost)
            """), {"code": guest_code, "uid": upgrade_id, "now": datetime.utcnow(), "cost": upgrade_cost})
            db.session.execute(text("""
                UPDATE user_race_cars SET upgrade_budget_used = upgrade_budget_used + :cost, updated_at = :now
                WHERE guest_code = :code
            """), {"cost": upgrade_cost, "now": datetime.utcnow(), "code": guest_code})
        else:
            db.session.execute(text("""
                INSERT INTO user_car_upgrades (user_id, upgrade_id, purchased_at, points_spent)
                VALUES (:uid, :upid, :now, :cost)
            """), {"uid": user_id, "upid": upgrade_id, "now": datetime.utcnow(), "cost": upgrade_cost})
            db.session.execute(text("""
                UPDATE user_race_cars SET upgrade_budget_used = upgrade_budget_used + :cost, updated_at = :now
                WHERE user_id = :uid
            """), {"cost": upgrade_cost, "now": datetime.utcnow(), "uid": user_id})
        
        db.session.commit()
        return jsonify({'success': True, 'message': f'Purchased {upgrade[1]}!', 'upgrade_name': upgrade[1],
                       'cost': upgrade_cost, 'boost': upgrade[3], 'budget_remaining': budget_remaining - upgrade_cost})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@games_bp.route('/api/racing-car/upgrades/sell', methods=['POST'])
@guest_or_login_required
def sell_racing_car_upgrade():
    """Sell an upgrade for full refund"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    data = request.get_json()
    upgrade_id = data.get('upgrade_id')
    
    if not upgrade_id:
        return jsonify({'error': 'No upgrade specified'}), 400
    
    try:
        upgrade = db.session.execute(text(
            "SELECT id, name, cost FROM car_upgrades WHERE id = :uid"
        ), {"uid": upgrade_id}).fetchone()
        
        if not upgrade:
            return jsonify({'error': 'Upgrade not found'}), 404
        
        upgrade_cost = upgrade[2]
        
        if guest_code:
            owned = db.session.execute(text(
                "SELECT id FROM user_car_upgrades WHERE guest_code = :code AND upgrade_id = :uid"
            ), {"code": guest_code, "uid": upgrade_id}).fetchone()
        else:
            owned = db.session.execute(text(
                "SELECT id FROM user_car_upgrades WHERE user_id = :uid AND upgrade_id = :upid"
            ), {"uid": user_id, "upid": upgrade_id}).fetchone()
        
        if not owned:
            return jsonify({'error': 'You do not own this upgrade'}), 400
        
        if guest_code:
            db.session.execute(text(
                "DELETE FROM user_car_upgrades WHERE guest_code = :code AND upgrade_id = :uid"
            ), {"code": guest_code, "uid": upgrade_id})
            db.session.execute(text("""
                UPDATE user_race_cars SET upgrade_budget_used = MAX(0, upgrade_budget_used - :cost), updated_at = :now
                WHERE guest_code = :code
            """), {"cost": upgrade_cost, "now": datetime.utcnow(), "code": guest_code})
        else:
            db.session.execute(text(
                "DELETE FROM user_car_upgrades WHERE user_id = :uid AND upgrade_id = :upid"
            ), {"uid": user_id, "upid": upgrade_id})
            db.session.execute(text("""
                UPDATE user_race_cars SET upgrade_budget_used = MAX(0, upgrade_budget_used - :cost), updated_at = :now
                WHERE user_id = :uid
            """), {"cost": upgrade_cost, "now": datetime.utcnow(), "uid": user_id})
        
        db.session.commit()
        return jsonify({'success': True, 'message': f'Sold {upgrade[1]}', 'refund': upgrade_cost})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@games_bp.route('/api/racing-car/upgrades/reset', methods=['POST'])
@guest_or_login_required
def reset_racing_car_upgrades():
    """Reset all upgrades and refund budget"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    try:
        if guest_code:
            db.session.execute(text("DELETE FROM user_car_upgrades WHERE guest_code = :code"), {"code": guest_code})
            db.session.execute(text("""
                UPDATE user_race_cars SET upgrade_budget_used = 0, updated_at = :now WHERE guest_code = :code
            """), {"now": datetime.utcnow(), "code": guest_code})
        else:
            db.session.execute(text("DELETE FROM user_car_upgrades WHERE user_id = :uid"), {"uid": user_id})
            db.session.execute(text("""
                UPDATE user_race_cars SET upgrade_budget_used = 0, updated_at = :now WHERE user_id = :uid
            """), {"now": datetime.utcnow(), "uid": user_id})
        
        db.session.commit()
        return jsonify({'success': True, 'message': 'All upgrades reset!', 'budget_remaining': UPGRADE_BUDGET})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# =====================================================
# END RACING CAR PHASE 2 ROUTES
# =====================================================

# =====================================================




# =====================================================
# RACING CAR PHASE 3 - WEEKLY RACES
# =====================================================

import random
from datetime import datetime, timedelta

# Points for finishing positions
RACE_POINTS = {1: 500, 2: 350, 3: 250, 4: 180, 5: 140, 6: 110, 7: 85, 8: 65, 9: 50, 10: 25}


def calculate_car_performance(user_id=None, guest_code=None):
    """Calculate total car performance from upgrades"""
    from sqlalchemy import text
    
    base_performance = 50  # Base from completed car
    
    try:
        if guest_code:
            result = db.session.execute(text("""
                SELECT COALESCE(SUM(u.performance_boost), 0)
                FROM user_car_upgrades uc
                JOIN car_upgrades u ON uc.upgrade_id = u.id
                WHERE uc.guest_code = :code
            """), {"code": guest_code}).fetchone()
        else:
            result = db.session.execute(text("""
                SELECT COALESCE(SUM(u.performance_boost), 0)
                FROM user_car_upgrades uc
                JOIN car_upgrades u ON uc.upgrade_id = u.id
                WHERE uc.user_id = :uid
            """), {"uid": user_id}).fetchone()
        
        upgrade_bonus = result[0] if result else 0
        return base_performance + upgrade_bonus
    except:
        return base_performance


def get_upgrade_breakdown(user_id=None, guest_code=None):
    """Get performance breakdown by category"""
    from sqlalchemy import text
    
    breakdown = {'driver': 0, 'aero': 0, 'engine': 0, 'tyres': 0, 'team': 0}
    
    try:
        if guest_code:
            results = db.session.execute(text("""
                SELECT u.category, SUM(u.performance_boost)
                FROM user_car_upgrades uc
                JOIN car_upgrades u ON uc.upgrade_id = u.id
                WHERE uc.guest_code = :code
                GROUP BY u.category
            """), {"code": guest_code}).fetchall()
        else:
            results = db.session.execute(text("""
                SELECT u.category, SUM(u.performance_boost)
                FROM user_car_upgrades uc
                JOIN car_upgrades u ON uc.upgrade_id = u.id
                WHERE uc.user_id = :uid
                GROUP BY u.category
            """), {"uid": user_id}).fetchall()
        
        for cat, boost in results:
            if cat in breakdown:
                breakdown[cat] = boost
    except:
        pass
    
    return breakdown


def simulate_race(user_performance, user_breakdown, race, ai_drivers, is_wet):
    """
    Simulate a race and return results.
    Returns list of (position, name, is_player, performance_score, highlight)
    """
    results = []
    
    # Calculate player's race score
    player_score = calculate_race_score(
        base_perf=user_performance,
        breakdown=user_breakdown,
        race=race,
        is_wet=is_wet,
        is_ai=False
    )
    results.append({
        'name': 'YOU',
        'is_player': True,
        'score': player_score,
        'team': 'Your Team',
        'flag': '🏁'
    })
    
    # Calculate AI scores
    for ai in ai_drivers:
        ai_breakdown = {
            'driver': ai['base_skill'] * 0.4,
            'aero': 30 + random.randint(-5, 5),
            'engine': 30 + random.randint(-5, 5),
            'tyres': ai['tyre_management'] * 0.3,
            'team': 25 + random.randint(-5, 5)
        }
        
        ai_base = 50 + (ai['base_skill'] - 80) * 2  # Scale AI skill to performance
        
        ai_score = calculate_race_score(
            base_perf=ai_base,
            breakdown=ai_breakdown,
            race=race,
            is_wet=is_wet,
            is_ai=True,
            ai_data=ai
        )
        
        results.append({
            'name': ai['name'],
            'is_player': False,
            'score': ai_score,
            'team': ai['team'],
            'flag': ai['flag'],
            'ai_id': ai['id']
        })
    
    # Sort by score (higher is better)
    results.sort(key=lambda x: x['score'], reverse=True)
    
    # Assign positions and generate highlights
    for i, r in enumerate(results):
        r['position'] = i + 1
        r['points'] = RACE_POINTS.get(i + 1, 10)
        r['highlight'] = generate_highlight(r, i + 1, is_wet, race)
    
    return results


def calculate_race_score(base_perf, breakdown, race, is_wet, is_ai=False, ai_data=None):
    """Calculate race performance score"""
    
    # Base score from car performance
    score = base_perf * 10
    
    # Apply track factors
    score += breakdown.get('aero', 0) * race['aero_factor'] * 20
    score += breakdown.get('engine', 0) * race['engine_factor'] * 20
    score += breakdown.get('driver', 0) * race['driver_factor'] * 20
    score += breakdown.get('tyres', 0) * race['tyre_factor'] * 20
    score += breakdown.get('team', 0) * race['team_factor'] * 20
    
    # Weather effect
    if is_wet:
        if is_ai and ai_data:
            wet_bonus = (ai_data['wet_skill'] - 80) * 3
            score += wet_bonus
        else:
            # Player wet performance based on driver upgrades
            driver_skill = breakdown.get('driver', 0)
            wet_bonus = (driver_skill - 20) * 2
            score += wet_bonus
    
    # Consistency factor (AI only)
    if is_ai and ai_data:
        consistency = ai_data['consistency']
        variance = (100 - consistency) * 2
        score += random.randint(-variance, variance)
    
    # Random race events (luck factor)
    luck = random.randint(-50, 50)
    score += luck
    
    # Small random variance
    score += random.randint(-20, 20)
    
    return max(0, score)


def generate_highlight(result, position, is_wet, race):
    """Generate a race highlight text"""
    name = result['name']
    
    if result['is_player']:
        if position == 1:
            highlights = [
                "🏆 VICTORY! Incredible drive from start to finish!",
                "🏆 WINNER! You dominated the {track}!",
                "🏆 P1! A masterclass performance today!"
            ]
        elif position <= 3:
            highlights = [
                f"🥈 P{position}! Brilliant podium finish!",
                f"🥉 P{position}! Fought hard for that podium!",
                f"🏅 P{position}! Great result at {race['name']}!"
            ]
        elif position <= 6:
            highlights = [
                f"✓ P{position} - Solid points finish",
                f"✓ P{position} - Good pace throughout",
                f"✓ P{position} - Consistent drive"
            ]
        else:
            highlights = [
                f"P{position} - Struggled with pace today",
                f"P{position} - Tough race, but finished",
                f"P{position} - More upgrades needed!"
            ]
    else:
        if position == 1:
            highlights = [f"{name} takes victory!", f"{name} wins at {race['name']}!"]
        elif position <= 3:
            highlights = [f"{name} claims P{position}", f"{name} on the podium"]
        else:
            highlights = [f"{name} finishes P{position}", f"{name} in P{position}"]
    
    text = random.choice(highlights)
    return text.format(track=race['name'])


@games_bp.route('/api/racing-car/race/current')
@guest_or_login_required  
def get_current_race():
    """Get the current race information"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    current_year = datetime.now().year
    
    # TEST MODE
    test_mode = request.args.get('test') == 'race'
    
    try:
        # Get current race from calendar
        race = db.session.execute(text("""
            SELECT rc.id, rc.race_number, rc.name, rc.country, rc.flag, rc.track_type,
                   rc.aero_factor, rc.engine_factor, rc.driver_factor, rc.tyre_factor, 
                   rc.team_factor, rc.rain_chance, rc.description, rc.race_date
            FROM race_calendar rc
            JOIN race_season_status rs ON rc.season_year = rs.season_year
            WHERE rc.season_year = :year AND rc.race_number = rs.current_race_number
        """), {"year": current_year}).fetchone()
        
        if not race:
            return jsonify({'error': 'No active race found', 'has_race': False})
        
        # Check if user already raced this
        if guest_code:
            existing = db.session.execute(text(
                "SELECT id, finish_position, points_earned FROM race_results WHERE race_id = :rid AND guest_code = :code"
            ), {"rid": race[0], "code": guest_code}).fetchone()
        else:
            existing = db.session.execute(text(
                "SELECT id, finish_position, points_earned FROM race_results WHERE race_id = :rid AND user_id = :uid"
            ), {"rid": race[0], "uid": user_id}).fetchone()
        
        already_raced = existing is not None
        
        # Get user's car performance
        car_performance = calculate_car_performance(user_id, guest_code)
        breakdown = get_upgrade_breakdown(user_id, guest_code)
        
        # Check if car is complete (or test mode)
        if guest_code:
            car = db.session.execute(text(
                "SELECT parts_unlocked FROM user_race_cars WHERE guest_code = :code"
            ), {"code": guest_code}).fetchone()
        else:
            car = db.session.execute(text(
                "SELECT parts_unlocked FROM user_race_cars WHERE user_id = :uid"
            ), {"uid": user_id}).fetchone()
        
        car_complete = (car and car[0] >= 50) or test_mode
        
        return jsonify({
            'has_race': True,
            'race': {
                'id': race[0],
                'number': race[1],
                'name': race[2],
                'country': race[3],
                'flag': race[4],
                'track_type': race[5],
                'factors': {
                    'aero': race[6],
                    'engine': race[7],
                    'driver': race[8],
                    'tyres': race[9],
                    'team': race[10]
                },
                'rain_chance': race[11],
                'description': race[12],
                'date': race[13]
            },
            'already_raced': already_raced,
            'previous_result': {
                'position': existing[1],
                'points': existing[2]
            } if existing else None,
            'car_complete': car_complete,
            'car_performance': car_performance,
            'performance_breakdown': breakdown
        })
        
    except Exception as e:
        return jsonify({'error': str(e), 'has_race': False})


@games_bp.route('/api/racing-car/race/start', methods=['POST'])
@guest_or_login_required
def start_race():
    """Start/simulate a race"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    data = request.get_json()
    
    race_id = data.get('race_id')
    tyre_choice = data.get('tyre_choice', 'medium')  # soft, medium, hard
    test_mode = data.get('test_mode', False)
    
    if not race_id:
        return jsonify({'error': 'No race specified'}), 400
    
    try:
        # Get race details
        race_row = db.session.execute(text("""
            SELECT id, race_number, name, country, flag, track_type,
                   aero_factor, engine_factor, driver_factor, tyre_factor, 
                   team_factor, rain_chance, description
            FROM race_calendar WHERE id = :rid
        """), {"rid": race_id}).fetchone()
        
        if not race_row:
            return jsonify({'error': 'Race not found'}), 404
        
        race = {
            'id': race_row[0], 'number': race_row[1], 'name': race_row[2],
            'country': race_row[3], 'flag': race_row[4], 'track_type': race_row[5],
            'aero_factor': race_row[6], 'engine_factor': race_row[7],
            'driver_factor': race_row[8], 'tyre_factor': race_row[9],
            'team_factor': race_row[10], 'rain_chance': race_row[11],
            'description': race_row[12]
        }
        
        # Check if already raced
        if guest_code:
            existing = db.session.execute(text(
                "SELECT id FROM race_results WHERE race_id = :rid AND guest_code = :code"
            ), {"rid": race_id, "code": guest_code}).fetchone()
        else:
            existing = db.session.execute(text(
                "SELECT id FROM race_results WHERE race_id = :rid AND user_id = :uid"
            ), {"rid": race_id, "uid": user_id}).fetchone()
        
        if existing:
            return jsonify({'error': 'Already raced this week!'}), 400
        
        # Determine weather
        is_wet = random.randint(1, 100) <= race['rain_chance']
        
        # Get AI drivers
        ai_rows = db.session.execute(text("""
            SELECT id, name, team, nationality, flag, driving_style,
                   base_skill, consistency, aggression, wet_skill, tyre_management
            FROM ai_race_drivers
        """)).fetchall()
        
        ai_drivers = [{
            'id': a[0], 'name': a[1], 'team': a[2], 'nationality': a[3],
            'flag': a[4], 'driving_style': a[5], 'base_skill': a[6],
            'consistency': a[7], 'aggression': a[8], 'wet_skill': a[9],
            'tyre_management': a[10]
        } for a in ai_rows]
        
        # Get user's car performance
        car_performance = calculate_car_performance(user_id, guest_code)
        breakdown = get_upgrade_breakdown(user_id, guest_code)
        
        # Apply tyre choice bonus
        tyre_bonus = {'soft': 15, 'medium': 8, 'hard': 0}
        breakdown['tyres'] = breakdown.get('tyres', 0) + tyre_bonus.get(tyre_choice, 8)
        
        # Simulate the race!
        results = simulate_race(car_performance, breakdown, race, ai_drivers, is_wet)
        
        # Find player result
        player_result = next(r for r in results if r['is_player'])
        position = player_result['position']
        points = player_result['points']
        highlight = player_result['highlight']
        
        # Save player result
        if guest_code:
            db.session.execute(text("""
                INSERT INTO race_results 
                (race_id, guest_code, finish_position, points_earned, tyre_choice, 
                 is_wet_race, race_performance_score, highlight_text, created_at)
                VALUES (:rid, :code, :pos, :pts, :tyre, :wet, :score, :highlight, :now)
            """), {
                "rid": race_id, "code": guest_code, "pos": position, "pts": points,
                "tyre": tyre_choice, "wet": is_wet, "score": player_result['score'],
                "highlight": highlight, "now": datetime.utcnow()
            })
        else:
            db.session.execute(text("""
                INSERT INTO race_results 
                (race_id, user_id, finish_position, points_earned, tyre_choice, 
                 is_wet_race, race_performance_score, highlight_text, created_at)
                VALUES (:rid, :uid, :pos, :pts, :tyre, :wet, :score, :highlight, :now)
            """), {
                "rid": race_id, "uid": user_id, "pos": position, "pts": points,
                "tyre": tyre_choice, "wet": is_wet, "score": player_result['score'],
                "highlight": highlight, "now": datetime.utcnow()
            })
        
        # Update championship standings
        current_year = datetime.now().year
        if guest_code:
            db.session.execute(text("""
                INSERT INTO championship_standings (season_year, guest_code, total_points, races_entered, wins, podiums, best_finish, last_updated)
                VALUES (:year, :code, :pts, 1, :wins, :podiums, :pos, :now)
                ON CONFLICT(season_year, guest_code) DO UPDATE SET
                    total_points = total_points + :pts,
                    races_entered = races_entered + 1,
                    wins = wins + :wins,
                    podiums = podiums + :podiums,
                    best_finish = CASE WHEN :pos < best_finish OR best_finish = 0 THEN :pos ELSE best_finish END,
                    last_updated = :now
            """), {
                "year": current_year, "code": guest_code, "pts": points,
                "wins": 1 if position == 1 else 0,
                "podiums": 1 if position <= 3 else 0,
                "pos": position, "now": datetime.utcnow()
            })
        else:
            db.session.execute(text("""
                INSERT INTO championship_standings (season_year, user_id, total_points, races_entered, wins, podiums, best_finish, last_updated)
                VALUES (:year, :uid, :pts, 1, :wins, :podiums, :pos, :now)
                ON CONFLICT(season_year, user_id) DO UPDATE SET
                    total_points = total_points + :pts,
                    races_entered = races_entered + 1,
                    wins = wins + :wins,
                    podiums = podiums + :podiums,
                    best_finish = CASE WHEN :pos < best_finish OR best_finish = 0 THEN :pos ELSE best_finish END,
                    last_updated = :now
            """), {
                "year": current_year, "uid": user_id, "pts": points,
                "wins": 1 if position == 1 else 0,
                "podiums": 1 if position <= 3 else 0,
                "pos": position, "now": datetime.utcnow()
            })
        
        # Award points to user's total score
        if guest_code:
            db.session.execute(text(
                "UPDATE guest_users SET total_score = total_score + :pts WHERE guest_code = :code"
            ), {"pts": points, "code": guest_code})
        else:
            db.session.execute(text(
                "UPDATE user_stats SET total_points = total_points + :pts WHERE user_id = :uid"
            ), {"pts": points, "uid": user_id})
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'race_name': race['name'],
            'is_wet': is_wet,
            'weather': 'Wet' if is_wet else 'Dry',
            'results': results,
            'player_position': position,
            'player_points': points,
            'player_highlight': highlight,
            'tyre_choice': tyre_choice
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@games_bp.route('/api/racing-car/championship')
@guest_or_login_required
def get_championship_standings():
    """Get championship standings"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    current_year = datetime.now().year
    
    try:
        # Get user's standing
        if guest_code:
            user_standing = db.session.execute(text("""
                SELECT total_points, races_entered, wins, podiums, best_finish
                FROM championship_standings
                WHERE season_year = :year AND guest_code = :code
            """), {"year": current_year, "code": guest_code}).fetchone()
        else:
            user_standing = db.session.execute(text("""
                SELECT total_points, races_entered, wins, podiums, best_finish
                FROM championship_standings
                WHERE season_year = :year AND user_id = :uid
            """), {"year": current_year, "uid": user_id}).fetchone()
        
        # Get race history
        if guest_code:
            history = db.session.execute(text("""
                SELECT rc.name, rc.flag, rr.finish_position, rr.points_earned, rr.is_wet_race, rr.highlight_text
                FROM race_results rr
                JOIN race_calendar rc ON rr.race_id = rc.id
                WHERE rr.guest_code = :code AND rc.season_year = :year
                ORDER BY rc.race_number
            """), {"code": guest_code, "year": current_year}).fetchall()
        else:
            history = db.session.execute(text("""
                SELECT rc.name, rc.flag, rr.finish_position, rr.points_earned, rr.is_wet_race, rr.highlight_text
                FROM race_results rr
                JOIN race_calendar rc ON rr.race_id = rc.id
                WHERE rr.user_id = :uid AND rc.season_year = :year
                ORDER BY rc.race_number
            """), {"uid": user_id, "year": current_year}).fetchall()
        
        return jsonify({
            'season': current_year,
            'standing': {
                'total_points': user_standing[0] if user_standing else 0,
                'races_entered': user_standing[1] if user_standing else 0,
                'wins': user_standing[2] if user_standing else 0,
                'podiums': user_standing[3] if user_standing else 0,
                'best_finish': user_standing[4] if user_standing else 0
            },
            'race_history': [{
                'name': h[0],
                'flag': h[1],
                'position': h[2],
                'points': h[3],
                'wet': h[4],
                'highlight': h[5]
            } for h in history]
        })
        
    except Exception as e:
        return jsonify({'error': str(e)})


@games_bp.route('/api/racing-car/ai-drivers')
@guest_or_login_required
def get_ai_drivers():
    """Get list of AI competitors"""
    from sqlalchemy import text
    
    try:
        drivers = db.session.execute(text("""
            SELECT id, name, team, nationality, flag, driving_style, 
                   base_skill, personality_desc, avatar_color
            FROM ai_race_drivers
            ORDER BY base_skill DESC
        """)).fetchall()
        
        return jsonify({
            'drivers': [{
                'id': d[0],
                'name': d[1],
                'team': d[2],
                'nationality': d[3],
                'flag': d[4],
                'style': d[5],
                'skill': d[6],
                'description': d[7],
                'color': d[8]
            } for d in drivers]
        })
    except Exception as e:
        return jsonify({'error': str(e), 'drivers': []})

# =====================================================
# END RACING CAR PHASE 3 ROUTES
