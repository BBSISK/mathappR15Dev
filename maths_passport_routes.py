# maths_passport_routes.py
# AgentMath Maths Passport System
# Travel-themed individualised learning journey

from flask import Blueprint, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from functools import wraps
import json

passport_bp = Blueprint('passport', __name__)

# Will be set when registering blueprint
db = None

# ==================== DESTINATION DATA ====================

DESTINATIONS = {
    # Junior Cycle Destinations
    'number_island': {
        'id': 'number_island',
        'display_name': 'Number Island',
        'tagline': 'Where digits come alive',
        'icon': '🏝️',
        'colour': '#3498db',
        'curriculum': ['JC', 'all'],
        'topics': ['arithmetic', 'multiplication_division', 'bodmas', 'number_systems', 'developing_number_sense'],
        'sort_order': 1
    },
    'fraction_falls': {
        'id': 'fraction_falls',
        'display_name': 'Fraction Falls',
        'tagline': 'Dive into parts of the whole',
        'icon': '🌊',
        'colour': '#9b59b6',
        'curriculum': ['JC', 'all'],
        'topics': ['fractions', 'basic_fractions'],
        'sort_order': 2
    },
    'decimal_desert': {
        'id': 'decimal_desert',
        'display_name': 'Decimal Desert',
        'tagline': 'Navigate the point',
        'icon': '🏜️',
        'colour': '#f39c12',
        'curriculum': ['JC', 'all'],
        'topics': ['decimals', 'basic_decimals'],
        'sort_order': 3
    },
    'percentage_peak': {
        'id': 'percentage_peak',
        'display_name': 'Percentage Peak',
        'tagline': 'Climb to 100%',
        'icon': '⛰️',
        'colour': '#1abc9c',
        'curriculum': ['JC', 'all'],
        'topics': ['percentages', 'basic_percentages', 'ratio'],
        'sort_order': 4
    },
    'algebra_alps': {
        'id': 'algebra_alps',
        'display_name': 'Algebra Alps',
        'tagline': 'Conquer the unknown',
        'icon': '🏔️',
        'colour': '#e74c3c',
        'curriculum': ['JC', 'LC', 'all'],
        'topics': ['introductory_algebra', 'solving_equations', 'simplifying_expressions', 'expanding_factorising', 'expanding_expressions', 'factorising_expressions'],
        'sort_order': 5
    },
    'function_forest': {
        'id': 'function_forest',
        'display_name': 'Function Forest',
        'tagline': 'Where patterns grow',
        'icon': '🌲',
        'colour': '#27ae60',
        'curriculum': ['JC', 'LC', 'all'],
        'topics': ['functions', 'patterns'],
        'sort_order': 6
    },
    'geometry_grove': {
        'id': 'geometry_grove',
        'display_name': 'Geometry Grove',
        'tagline': 'Shape your understanding',
        'icon': '📐',
        'colour': '#8e44ad',
        'curriculum': ['JC', 'LC', 'all'],
        'topics': ['area_perimeter_volume', 'coordinate_geometry', 'geometry'],
        'sort_order': 7
    },
    'statistics_city': {
        'id': 'statistics_city',
        'display_name': 'Statistics City',
        'tagline': 'Data comes to life',
        'icon': '🏙️',
        'colour': '#2c3e50',
        'curriculum': ['JC', 'LC', 'all'],
        'topics': ['descriptive_statistics', 'data_and_charts', 'statistics'],
        'sort_order': 8
    },
    'probability_port': {
        'id': 'probability_port',
        'display_name': 'Probability Port',
        'tagline': 'Set sail on chance',
        'icon': '🎲',
        'colour': '#16a085',
        'curriculum': ['JC', 'LC', 'all'],
        'topics': ['probability'],
        'sort_order': 9
    },
    'sets_sanctuary': {
        'id': 'sets_sanctuary',
        'display_name': 'Sets Sanctuary',
        'tagline': 'Where groups belong',
        'icon': '🔵',
        'colour': '#2980b9',
        'curriculum': ['JC', 'all'],
        'topics': ['sets'],
        'sort_order': 10
    },
    # Senior Cycle Additional
    'trigonometry_towers': {
        'id': 'trigonometry_towers',
        'display_name': 'Trigonometry Towers',
        'tagline': 'Angles of adventure',
        'icon': '🗼',
        'colour': '#c0392b',
        'curriculum': ['LC', 'all'],
        'topics': ['trigonometry'],
        'sort_order': 11
    },
    'complex_kingdom': {
        'id': 'complex_kingdom',
        'display_name': 'Complex Kingdom',
        'tagline': 'Beyond the real',
        'icon': '👑',
        'colour': '#7f8c8d',
        'curriculum': ['LC', 'all'],
        'topics': ['complex_numbers_intro', 'complex_numbers_expanded'],
        'sort_order': 12
    },
    'indices_inn': {
        'id': 'indices_inn',
        'display_name': 'Indices Inn',
        'tagline': 'Power up your skills',
        'icon': '🏨',
        'colour': '#e67e22',
        'curriculum': ['JC', 'LC', 'all'],
        'topics': ['indices', 'surds'],
        'sort_order': 13
    },
    'financial_district': {
        'id': 'financial_district',
        'display_name': 'Financial District',
        'tagline': 'Make your numbers count',
        'icon': '💰',
        'colour': '#f1c40f',
        'curriculum': ['LC', 'all'],
        'topics': ['financial_maths'],
        'sort_order': 14
    },
    # L1LP/L2LP/Numeracy
    'counting_cove': {
        'id': 'counting_cove',
        'display_name': 'Counting Cove',
        'tagline': 'Where every number matters',
        'icon': '🐚',
        'colour': '#3498db',
        'curriculum': ['L1LP', 'L2LP', 'Numeracy'],
        'topics': ['developing_number_sense', 'awareness_of_environment'],
        'sort_order': 20
    },
    'money_market': {
        'id': 'money_market',
        'display_name': 'Money Market',
        'tagline': 'Spend wisely, count carefully',
        'icon': '🛒',
        'colour': '#2ecc71',
        'curriculum': ['L1LP', 'L2LP', 'Numeracy'],
        'topics': ['money_skills'],
        'sort_order': 21
    },
    'time_town': {
        'id': 'time_town',
        'display_name': 'Time Town',
        'tagline': 'Every moment counts',
        'icon': '⏰',
        'colour': '#e67e22',
        'curriculum': ['L1LP', 'L2LP', 'Numeracy'],
        'topics': ['time_skills'],
        'sort_order': 22
    },
    'shape_shore': {
        'id': 'shape_shore',
        'display_name': 'Shape Shore',
        'tagline': 'Build with shapes',
        'icon': '🔷',
        'colour': '#9b59b6',
        'curriculum': ['L1LP', 'L2LP', 'Numeracy'],
        'topics': ['shape_and_space'],
        'sort_order': 23
    },
    'measure_meadow': {
        'id': 'measure_meadow',
        'display_name': 'Measure Meadow',
        'tagline': 'Size up the world',
        'icon': '📏',
        'colour': '#1abc9c',
        'curriculum': ['L1LP', 'L2LP', 'Numeracy', 'JC'],
        'topics': ['measurement', 'mensuration'],
        'sort_order': 24
    }
}

# Stamp tier definitions
STAMP_TIERS = {
    'bronze': {'name': 'Explorer', 'stars': 1, 'level_start': 1, 'level_end': 4, 'icon': '⭐'},
    'silver': {'name': 'Adventurer', 'stars': 2, 'level_start': 5, 'level_end': 8, 'icon': '⭐⭐'},
    'gold': {'name': 'Master', 'stars': 3, 'level_start': 9, 'level_end': 12, 'icon': '⭐⭐⭐'}
}


def get_destinations_for_curriculum(curriculum):
    """Get destinations available for a specific curriculum"""
    result = []
    for dest_id, dest in DESTINATIONS.items():
        if curriculum in dest['curriculum'] or 'all' in dest['curriculum']:
            result.append(dest)
    return sorted(result, key=lambda x: x['sort_order'])


def get_topic_to_destination_map():
    """Create a map from topic to destination"""
    topic_map = {}
    for dest_id, dest in DESTINATIONS.items():
        for topic in dest['topics']:
            topic_map[topic] = dest_id
    return topic_map


# ==================== DECORATORS ====================

def passport_login_required(f):
    """Allow both registered users and guests"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session and 'guest_code' not in session:
            return jsonify({'error': 'Please log in to access your passport'}), 401
        return f(*args, **kwargs)
    return decorated_function


# ==================== API ROUTES ====================

@passport_bp.route('/api/passport', methods=['GET'])
@passport_login_required
def get_passport():
    """Get or create student passport"""
    from sqlalchemy import text
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    try:
        # Check if passport exists for this user
        if user_id:
            passport = db.session.execute(text("""
                SELECT id, user_id, guest_code, target_curriculum, target_exam_date, 
                       journey_started, total_distance, created_at
                FROM student_passport WHERE user_id = :user_id
            """), {'user_id': user_id}).fetchone()
        else:
            passport = db.session.execute(text("""
                SELECT id, user_id, guest_code, target_curriculum, target_exam_date, 
                       journey_started, total_distance, created_at
                FROM student_passport WHERE guest_code = :guest_code
            """), {'guest_code': guest_code}).fetchone()
        
        if not passport:
            # Return empty passport - user needs to set up
            return jsonify({
                'exists': False,
                'message': 'No passport found. Please complete setup.',
                'destinations': get_destinations_for_curriculum('all')
            })
        
        # Get passport data
        passport_id = passport[0]
        passport_data = {
            'id': passport_id,
            'target_curriculum': passport[3],
            'target_exam_date': str(passport[4]) if passport[4] else None,
            'journey_started': str(passport[5]) if passport[5] else None,
            'total_distance': passport[6] or 0,
            'exists': True
        }
        
        # Get user info
        if user_id:
            from app import User
            user = User.query.get(user_id)
            passport_data['traveller_name'] = user.full_name if user else 'Traveller'
            passport_data['school'] = user.school if user else None
        else:
            passport_data['traveller_name'] = f'Guest ({guest_code})'
            passport_data['school'] = None
        
        # Get stamps
        stamps = db.session.execute(text("""
            SELECT destination_id, stamp_tier, level_start, level_end, 
                   earned_at, points_at_earn
            FROM passport_stamps WHERE passport_id = :passport_id
        """), {'passport_id': passport_id}).fetchall()
        
        passport_data['stamps'] = []
        for stamp in stamps:
            passport_data['stamps'].append({
                'destination_id': stamp[0],
                'tier': stamp[1],
                'level_start': stamp[2],
                'level_end': stamp[3],
                'earned_at': str(stamp[4]) if stamp[4] else None,
                'points': stamp[5] or 0
            })
        
        # Get itinerary
        itinerary = db.session.execute(text("""
            SELECT destination_id, stop_order, status, suggested_start_level,
                   priority, added_by, teacher_notes
            FROM passport_itinerary 
            WHERE passport_id = :passport_id
            ORDER BY stop_order
        """), {'passport_id': passport_id}).fetchall()
        
        passport_data['itinerary'] = []
        for stop in itinerary:
            passport_data['itinerary'].append({
                'destination_id': stop[0],
                'stop_order': stop[1],
                'status': stop[2],
                'suggested_start_level': stop[3],
                'priority': stop[4],
                'added_by': stop[5],
                'teacher_notes': stop[6]
            })
        
        # Get self-assessment
        assessments = db.session.execute(text("""
            SELECT destination_id, confidence_rating, quick_check_score,
                   quick_check_questions, assessed_at
            FROM passport_self_assessment WHERE passport_id = :passport_id
        """), {'passport_id': passport_id}).fetchall()
        
        passport_data['self_assessment'] = {}
        for assess in assessments:
            passport_data['self_assessment'][assess[0]] = {
                'confidence': assess[1],
                'quick_check_score': assess[2],
                'quick_check_questions': assess[3],
                'assessed_at': str(assess[4]) if assess[4] else None
            }
        
        # Get milestones
        milestones = db.session.execute(text("""
            SELECT id, title, milestone_date, milestone_type, target_stamps,
                   reached, reached_at
            FROM passport_milestones WHERE passport_id = :passport_id
            ORDER BY milestone_date
        """), {'passport_id': passport_id}).fetchall()
        
        passport_data['milestones'] = []
        for ms in milestones:
            passport_data['milestones'].append({
                'id': ms[0],
                'title': ms[1],
                'date': str(ms[2]) if ms[2] else None,
                'type': ms[3],
                'target_stamps': ms[4],
                'reached': bool(ms[5]),
                'reached_at': str(ms[6]) if ms[6] else None
            })
        
        # Get current adaptive progress to calculate destination progress
        passport_data['destination_progress'] = get_destination_progress(user_id, guest_code)
        
        # Add destinations for this curriculum
        passport_data['destinations'] = get_destinations_for_curriculum(
            passport_data['target_curriculum'] or 'all'
        )
        
        # Calculate stats
        passport_data['stats'] = calculate_passport_stats(passport_data)
        
        return jsonify(passport_data)
        
    except Exception as e:
        print(f"Error getting passport: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


def get_destination_progress(user_id, guest_code):
    """Get adaptive progress mapped to destinations"""
    from sqlalchemy import text
    
    topic_to_dest = get_topic_to_destination_map()
    progress = {}
    
    try:
        # Get adaptive progress
        if user_id:
            rows = db.session.execute(text("""
                SELECT topic, current_level FROM adaptive_progress
                WHERE user_id = :user_id
            """), {'user_id': user_id}).fetchall()
        elif guest_code:
            rows = db.session.execute(text("""
                SELECT topic, current_level FROM adaptive_progress
                WHERE guest_code = :guest_code
            """), {'guest_code': guest_code}).fetchall()
        else:
            rows = []
        
        # Map to destinations
        for row in rows:
            topic = row[0]
            level = row[1] or 1
            
            dest_id = topic_to_dest.get(topic)
            if dest_id:
                if dest_id not in progress:
                    progress[dest_id] = {
                        'topics': {},
                        'max_level': 0,
                        'avg_level': 0,
                        'total_topics': 0
                    }
                
                progress[dest_id]['topics'][topic] = level
                progress[dest_id]['max_level'] = max(progress[dest_id]['max_level'], level)
                progress[dest_id]['total_topics'] += 1
        
        # Calculate averages
        for dest_id in progress:
            levels = list(progress[dest_id]['topics'].values())
            if levels:
                progress[dest_id]['avg_level'] = sum(levels) / len(levels)
        
    except Exception as e:
        print(f"Error getting destination progress: {e}")
    
    return progress


def calculate_passport_stats(passport_data):
    """Calculate summary statistics for passport"""
    stats = {
        'total_stamps': len(passport_data.get('stamps', [])),
        'bronze_stamps': 0,
        'silver_stamps': 0,
        'gold_stamps': 0,
        'destinations_visited': 0,
        'destinations_completed': 0,
        'total_destinations': len(passport_data.get('destinations', [])),
        'days_until_exam': None
    }
    
    # Count stamp tiers
    destinations_with_stamps = set()
    destinations_completed = set()
    
    for stamp in passport_data.get('stamps', []):
        if stamp['tier'] == 'bronze':
            stats['bronze_stamps'] += 1
        elif stamp['tier'] == 'silver':
            stats['silver_stamps'] += 1
        elif stamp['tier'] == 'gold':
            stats['gold_stamps'] += 1
            destinations_completed.add(stamp['destination_id'])
        
        destinations_with_stamps.add(stamp['destination_id'])
    
    stats['destinations_visited'] = len(destinations_with_stamps)
    stats['destinations_completed'] = len(destinations_completed)
    
    # Calculate days until exam
    if passport_data.get('target_exam_date'):
        try:
            exam_date = datetime.strptime(passport_data['target_exam_date'], '%Y-%m-%d').date()
            today = date.today()
            stats['days_until_exam'] = (exam_date - today).days
        except:
            pass
    
    return stats


@passport_bp.route('/api/passport/setup', methods=['POST'])
@passport_login_required
def setup_passport():
    """Initial passport setup"""
    from sqlalchemy import text
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    data = request.json
    target_curriculum = data.get('target_curriculum', 'JC')
    target_exam_date = data.get('target_exam_date')
    
    try:
        # Check if passport already exists
        if user_id:
            existing = db.session.execute(text("""
                SELECT id FROM student_passport WHERE user_id = :user_id
            """), {'user_id': user_id}).fetchone()
        else:
            existing = db.session.execute(text("""
                SELECT id FROM student_passport WHERE guest_code = :guest_code
            """), {'guest_code': guest_code}).fetchone()
        
        if existing:
            # Update existing passport
            if user_id:
                db.session.execute(text("""
                    UPDATE student_passport 
                    SET target_curriculum = :curriculum, target_exam_date = :exam_date,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE user_id = :user_id
                """), {
                    'curriculum': target_curriculum,
                    'exam_date': target_exam_date,
                    'user_id': user_id
                })
            else:
                db.session.execute(text("""
                    UPDATE student_passport 
                    SET target_curriculum = :curriculum, target_exam_date = :exam_date,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE guest_code = :guest_code
                """), {
                    'curriculum': target_curriculum,
                    'exam_date': target_exam_date,
                    'guest_code': guest_code
                })
            
            passport_id = existing[0]
        else:
            # Create new passport
            if user_id:
                db.session.execute(text("""
                    INSERT INTO student_passport (user_id, target_curriculum, target_exam_date, journey_started)
                    VALUES (:user_id, :curriculum, :exam_date, CURRENT_DATE)
                """), {
                    'user_id': user_id,
                    'curriculum': target_curriculum,
                    'exam_date': target_exam_date
                })
            else:
                db.session.execute(text("""
                    INSERT INTO student_passport (guest_code, target_curriculum, target_exam_date, journey_started)
                    VALUES (:guest_code, :curriculum, :exam_date, CURRENT_DATE)
                """), {
                    'guest_code': guest_code,
                    'curriculum': target_curriculum,
                    'exam_date': target_exam_date
                })
            
            # Get the new passport ID
            if user_id:
                result = db.session.execute(text("""
                    SELECT id FROM student_passport WHERE user_id = :user_id
                """), {'user_id': user_id}).fetchone()
            else:
                result = db.session.execute(text("""
                    SELECT id FROM student_passport WHERE guest_code = :guest_code
                """), {'guest_code': guest_code}).fetchone()
            
            passport_id = result[0] if result else None
            
            # Create default itinerary based on curriculum
            if passport_id:
                destinations = get_destinations_for_curriculum(target_curriculum)
                for i, dest in enumerate(destinations):
                    db.session.execute(text("""
                        INSERT INTO passport_itinerary (passport_id, destination_id, stop_order, status, added_by)
                        VALUES (:passport_id, :dest_id, :order, 'planned', 'system')
                    """), {
                        'passport_id': passport_id,
                        'dest_id': dest['id'],
                        'order': i + 1
                    })
        
        db.session.commit()
        
        # Generate initial learning path
        generate_learning_path(passport_id, user_id, guest_code, target_curriculum)
        
        return jsonify({
            'success': True,
            'passport_id': passport_id,
            'message': 'Passport created successfully!'
        })
        
    except Exception as e:
        db.session.rollback()
        print(f"Error setting up passport: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/self-assessment', methods=['POST'])
@passport_login_required
def save_self_assessment():
    """Save self-assessment ratings"""
    from sqlalchemy import text
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    data = request.json
    assessments = data.get('assessments', {})  # {destination_id: confidence_rating}
    
    try:
        # Get passport ID
        if user_id:
            passport = db.session.execute(text("""
                SELECT id FROM student_passport WHERE user_id = :user_id
            """), {'user_id': user_id}).fetchone()
        else:
            passport = db.session.execute(text("""
                SELECT id FROM student_passport WHERE guest_code = :guest_code
            """), {'guest_code': guest_code}).fetchone()
        
        if not passport:
            return jsonify({'error': 'Passport not found'}), 404
        
        passport_id = passport[0]
        
        # Save each assessment
        for dest_id, confidence in assessments.items():
            # Check if exists
            existing = db.session.execute(text("""
                SELECT id FROM passport_self_assessment
                WHERE passport_id = :passport_id AND destination_id = :dest_id
            """), {'passport_id': passport_id, 'dest_id': dest_id}).fetchone()
            
            if existing:
                db.session.execute(text("""
                    UPDATE passport_self_assessment
                    SET confidence_rating = :confidence, assessed_at = CURRENT_TIMESTAMP
                    WHERE passport_id = :passport_id AND destination_id = :dest_id
                """), {
                    'confidence': confidence,
                    'passport_id': passport_id,
                    'dest_id': dest_id
                })
            else:
                db.session.execute(text("""
                    INSERT INTO passport_self_assessment (passport_id, destination_id, confidence_rating)
                    VALUES (:passport_id, :dest_id, :confidence)
                """), {
                    'passport_id': passport_id,
                    'dest_id': dest_id,
                    'confidence': confidence
                })
        
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Assessment saved'})
        
    except Exception as e:
        db.session.rollback()
        print(f"Error saving assessment: {e}")
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/itinerary', methods=['PUT'])
@passport_login_required
def update_itinerary():
    """Update itinerary order"""
    from sqlalchemy import text
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    data = request.json
    new_order = data.get('order', [])  # List of destination_ids in order
    
    try:
        # Get passport ID
        if user_id:
            passport = db.session.execute(text("""
                SELECT id FROM student_passport WHERE user_id = :user_id
            """), {'user_id': user_id}).fetchone()
        else:
            passport = db.session.execute(text("""
                SELECT id FROM student_passport WHERE guest_code = :guest_code
            """), {'guest_code': guest_code}).fetchone()
        
        if not passport:
            return jsonify({'error': 'Passport not found'}), 404
        
        passport_id = passport[0]
        
        # Update order
        for i, dest_id in enumerate(new_order):
            db.session.execute(text("""
                UPDATE passport_itinerary
                SET stop_order = :order
                WHERE passport_id = :passport_id AND destination_id = :dest_id
            """), {
                'order': i + 1,
                'passport_id': passport_id,
                'dest_id': dest_id
            })
        
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Itinerary updated'})
        
    except Exception as e:
        db.session.rollback()
        print(f"Error updating itinerary: {e}")
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/check-stamps', methods=['POST'])
@passport_login_required
def check_and_award_stamps():
    """Check if any stamps should be awarded based on current progress"""
    from sqlalchemy import text
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    try:
        # Get passport
        if user_id:
            passport = db.session.execute(text("""
                SELECT id FROM student_passport WHERE user_id = :user_id
            """), {'user_id': user_id}).fetchone()
        else:
            passport = db.session.execute(text("""
                SELECT id FROM student_passport WHERE guest_code = :guest_code
            """), {'guest_code': guest_code}).fetchone()
        
        if not passport:
            return jsonify({'error': 'Passport not found'}), 404
        
        passport_id = passport[0]
        
        # Get current progress
        progress = get_destination_progress(user_id, guest_code)
        
        # Get existing stamps
        existing_stamps = db.session.execute(text("""
            SELECT destination_id, stamp_tier FROM passport_stamps
            WHERE passport_id = :passport_id
        """), {'passport_id': passport_id}).fetchall()
        
        existing = {(s[0], s[1]) for s in existing_stamps}
        
        # Check each destination
        new_stamps = []
        
        for dest_id, dest_progress in progress.items():
            max_level = dest_progress.get('max_level', 0)
            
            # Check bronze (L1-4)
            if max_level >= 4 and (dest_id, 'bronze') not in existing:
                new_stamps.append({
                    'destination_id': dest_id,
                    'tier': 'bronze',
                    'level_start': 1,
                    'level_end': 4
                })
            
            # Check silver (L5-8)
            if max_level >= 8 and (dest_id, 'silver') not in existing:
                new_stamps.append({
                    'destination_id': dest_id,
                    'tier': 'silver',
                    'level_start': 5,
                    'level_end': 8
                })
            
            # Check gold (L9-12)
            if max_level >= 12 and (dest_id, 'gold') not in existing:
                new_stamps.append({
                    'destination_id': dest_id,
                    'tier': 'gold',
                    'level_start': 9,
                    'level_end': 12
                })
        
        # Award new stamps
        for stamp in new_stamps:
            db.session.execute(text("""
                INSERT INTO passport_stamps (passport_id, destination_id, stamp_tier, level_start, level_end)
                VALUES (:passport_id, :dest_id, :tier, :level_start, :level_end)
            """), {
                'passport_id': passport_id,
                'dest_id': stamp['destination_id'],
                'tier': stamp['tier'],
                'level_start': stamp['level_start'],
                'level_end': stamp['level_end']
            })
            
            # Add distance for gamification (100km per stamp)
            db.session.execute(text("""
                UPDATE student_passport SET total_distance = total_distance + 100
                WHERE id = :passport_id
            """), {'passport_id': passport_id})
        
        db.session.commit()
        
        # Add destination info to new stamps
        for stamp in new_stamps:
            if stamp['destination_id'] in DESTINATIONS:
                stamp['destination'] = DESTINATIONS[stamp['destination_id']]
        
        return jsonify({
            'success': True,
            'new_stamps': new_stamps,
            'message': f'{len(new_stamps)} new stamp(s) earned!' if new_stamps else 'No new stamps yet'
        })
        
    except Exception as e:
        db.session.rollback()
        print(f"Error checking stamps: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/destinations', methods=['GET'])
def get_destinations():
    """Get all destinations, optionally filtered by curriculum"""
    curriculum = request.args.get('curriculum', 'all')
    destinations = get_destinations_for_curriculum(curriculum)
    return jsonify({'destinations': destinations})


# ==================== TEACHER ROUTES ====================

@passport_bp.route('/api/teacher/student/<int:student_id>/passport', methods=['GET'])
def teacher_view_passport(student_id):
    """Teacher view of student passport"""
    from sqlalchemy import text
    
    # Verify teacher is logged in
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    # Could add check that teacher has this student in their class
    
    try:
        passport = db.session.execute(text("""
            SELECT id, target_curriculum, target_exam_date, journey_started, total_distance
            FROM student_passport WHERE user_id = :user_id
        """), {'user_id': student_id}).fetchone()
        
        if not passport:
            return jsonify({'exists': False, 'message': 'Student has not created a passport yet'})
        
        passport_id = passport[0]
        
        # Get stamps
        stamps = db.session.execute(text("""
            SELECT destination_id, stamp_tier, earned_at
            FROM passport_stamps WHERE passport_id = :passport_id
        """), {'passport_id': passport_id}).fetchall()
        
        # Get itinerary
        itinerary = db.session.execute(text("""
            SELECT destination_id, stop_order, status, priority, teacher_notes, added_by
            FROM passport_itinerary WHERE passport_id = :passport_id
            ORDER BY stop_order
        """), {'passport_id': passport_id}).fetchall()
        
        # Get student name
        from app import User
        student = User.query.get(student_id)
        
        return jsonify({
            'exists': True,
            'student_name': student.full_name if student else 'Unknown',
            'target_curriculum': passport[1],
            'target_exam_date': str(passport[2]) if passport[2] else None,
            'journey_started': str(passport[3]) if passport[3] else None,
            'total_distance': passport[4] or 0,
            'stamps': [{'destination_id': s[0], 'tier': s[1], 'earned_at': str(s[2])} for s in stamps],
            'itinerary': [{
                'destination_id': i[0],
                'stop_order': i[1],
                'status': i[2],
                'priority': i[3],
                'teacher_notes': i[4],
                'added_by': i[5]
            } for i in itinerary],
            'destinations': DESTINATIONS
        })
        
    except Exception as e:
        print(f"Error getting student passport: {e}")
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/teacher/student/<int:student_id>/itinerary', methods=['PUT'])
def teacher_update_itinerary(student_id):
    """Teacher updates student itinerary"""
    from sqlalchemy import text
    
    # Verify teacher is logged in
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.json
    
    try:
        # Get passport
        passport = db.session.execute(text("""
            SELECT id FROM student_passport WHERE user_id = :user_id
        """), {'user_id': student_id}).fetchone()
        
        if not passport:
            return jsonify({'error': 'Student passport not found'}), 404
        
        passport_id = passport[0]
        
        # Update order if provided
        if 'order' in data:
            for i, dest_id in enumerate(data['order']):
                db.session.execute(text("""
                    UPDATE passport_itinerary
                    SET stop_order = :order, added_by = 'teacher'
                    WHERE passport_id = :passport_id AND destination_id = :dest_id
                """), {
                    'order': i + 1,
                    'passport_id': passport_id,
                    'dest_id': dest_id
                })
        
        # Update priority if provided
        if 'priorities' in data:
            for dest_id, priority in data['priorities'].items():
                db.session.execute(text("""
                    UPDATE passport_itinerary
                    SET priority = :priority
                    WHERE passport_id = :passport_id AND destination_id = :dest_id
                """), {
                    'priority': priority,
                    'passport_id': passport_id,
                    'dest_id': dest_id
                })
        
        # Update notes if provided
        if 'notes' in data:
            for dest_id, note in data['notes'].items():
                db.session.execute(text("""
                    UPDATE passport_itinerary
                    SET teacher_notes = :note
                    WHERE passport_id = :passport_id AND destination_id = :dest_id
                """), {
                    'note': note,
                    'passport_id': passport_id,
                    'dest_id': dest_id
                })
        
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Itinerary updated'})
        
    except Exception as e:
        db.session.rollback()
        print(f"Error updating student itinerary: {e}")
        return jsonify({'error': str(e)}), 500


# ==================== PAGE ROUTE ====================

@passport_bp.route('/passport')
@passport_login_required
def passport_page():
    """Render the passport page"""
    return render_template('student_passport.html')


# ==================== EXAM WEIGHTINGS ====================
# How important each destination is for each exam (1-5 scale)

EXAM_WEIGHTINGS = {
    'JC': {
        'number_island': 5,      # Very important - foundation
        'fraction_falls': 5,     # Very important - appears everywhere
        'decimal_desert': 4,     # Important
        'percentage_peak': 5,    # Very important - real world applications
        'algebra_alps': 5,       # Very important - core JC topic
        'function_forest': 4,    # Important
        'geometry_grove': 4,     # Important
        'statistics_city': 4,    # Important - Paper 2
        'probability_port': 4,   # Important - Paper 2
        'sets_sanctuary': 3,     # Moderate
        'indices_inn': 3,        # Moderate
        'trigonometry_towers': 3, # Moderate at JC
    },
    'LC_HL': {
        'algebra_alps': 5,
        'function_forest': 5,
        'trigonometry_towers': 5,
        'geometry_grove': 4,
        'complex_kingdom': 4,
        'indices_inn': 4,
        'financial_district': 4,
        'statistics_city': 4,
        'probability_port': 4,
        'number_island': 3,
        'fraction_falls': 3,
        'percentage_peak': 3,
    },
    'LC_OL': {
        'algebra_alps': 5,
        'number_island': 5,
        'percentage_peak': 5,
        'financial_district': 5,
        'statistics_city': 4,
        'probability_port': 4,
        'geometry_grove': 4,
        'trigonometry_towers': 4,
        'function_forest': 3,
        'fraction_falls': 3,
        'indices_inn': 3,
    },
    'L1LP': {
        'counting_cove': 5,
        'money_market': 5,
        'time_town': 5,
        'shape_shore': 4,
        'measure_meadow': 4,
    },
    'L2LP': {
        'counting_cove': 5,
        'money_market': 5,
        'time_town': 5,
        'shape_shore': 4,
        'measure_meadow': 4,
        'number_island': 3,
    }
}


def calculate_entry_level(confidence, quiz_percentage):
    """
    Determine entry level based on confidence and quiz performance.
    
    Returns: 1, 4, 7, or 10
    """
    # If no quiz data, use confidence alone
    if quiz_percentage is None:
        if confidence >= 4:
            return 4  # Confident → skip basics
        elif confidence >= 3:
            return 1  # Neutral → start from beginning
        else:
            return 1  # Not confident → start from beginning
    
    # Combine quiz performance (weighted more heavily) with confidence
    # Quiz is reality, confidence is perception
    
    if quiz_percentage >= 80:
        # Strong performance
        if confidence >= 4:
            return 10  # Confirmed strong → near mastery entry
        else:
            return 7   # Underestimated themselves → upper intermediate
    elif quiz_percentage >= 60:
        # Good performance
        if confidence >= 4:
            return 7   # Slightly overconfident but OK
        else:
            return 4   # Accurate self-assessment
    elif quiz_percentage >= 40:
        # Moderate performance
        if confidence >= 4:
            return 4   # Overconfident → build foundations
        else:
            return 4   # Accurate → intermediate start
    else:
        # Weak performance
        return 1  # Always start from basics


def calculate_priority_score(confidence, quiz_percentage, exam_weight, has_existing_progress, current_level):
    """
    Calculate priority score for a destination.
    Higher score = higher priority (work on this first)
    
    Factors:
    - Gap size (inverse of quiz score)
    - Lack of confidence
    - Exam importance
    - Not started yet (bonus priority)
    """
    # Base scores
    gap_score = 0
    confidence_score = 0
    
    # Gap from quiz (0-10 points) - biggest factor
    if quiz_percentage is not None:
        gap_score = ((100 - quiz_percentage) / 100) * 10
    elif confidence is not None:
        # No quiz data, estimate from confidence
        gap_score = ((5 - confidence) / 5) * 8
    else:
        gap_score = 5  # Unknown, medium priority
    
    # Confidence gap (0-4 points)
    if confidence is not None:
        confidence_score = (5 - confidence) * 0.8
    
    # Exam weighting (0-5 points)
    exam_score = exam_weight if exam_weight else 3
    
    # Not started bonus (3 points if never attempted)
    not_started_bonus = 3 if not has_existing_progress else 0
    
    # Currently low level penalty (if started but still low)
    low_level_bonus = 0
    if has_existing_progress and current_level:
        if current_level <= 3:
            low_level_bonus = 2  # Needs work
        elif current_level <= 6:
            low_level_bonus = 1  # Making progress
    
    # Calculate total
    total = gap_score + confidence_score + exam_score + not_started_bonus + low_level_bonus
    
    return round(total, 2)


def generate_learning_path(passport_id, user_id, guest_code, curriculum):
    """
    Generate a prioritized learning path based on assessments.
    Updates the passport_itinerary with priorities and entry levels.
    """
    from sqlalchemy import text
    
    try:
        # Get self-assessments
        assessments = db.session.execute(text("""
            SELECT destination_id, confidence_rating, quick_check_score, quick_check_questions
            FROM passport_self_assessment
            WHERE passport_id = :passport_id
        """), {'passport_id': passport_id}).fetchall()
        
        assessment_data = {}
        for a in assessments:
            dest_id = a[0]
            confidence = a[1]
            qc_score = a[2]
            qc_total = a[3]
            
            quiz_pct = None
            if qc_score is not None and qc_total and qc_total > 0:
                quiz_pct = (qc_score / qc_total) * 100
            
            assessment_data[dest_id] = {
                'confidence': confidence,
                'quiz_percentage': quiz_pct
            }
        
        # Get existing adaptive progress
        progress_data = {}
        if user_id:
            progress_rows = db.session.execute(text("""
                SELECT topic, current_level FROM adaptive_progress
                WHERE user_id = :user_id
            """), {'user_id': user_id}).fetchall()
        elif guest_code:
            progress_rows = db.session.execute(text("""
                SELECT topic, current_level FROM adaptive_progress
                WHERE guest_code = :guest_code
            """), {'guest_code': guest_code}).fetchall()
        else:
            progress_rows = []
        
        # Map topics to destinations
        topic_to_dest = get_topic_to_destination_map()
        for row in progress_rows:
            topic = row[0]
            level = row[1] or 1
            dest_id = topic_to_dest.get(topic)
            if dest_id:
                if dest_id not in progress_data:
                    progress_data[dest_id] = {'max_level': 0}
                progress_data[dest_id]['max_level'] = max(progress_data[dest_id]['max_level'], level)
        
        # Get exam weightings
        exam_weights = EXAM_WEIGHTINGS.get(curriculum, EXAM_WEIGHTINGS.get('JC', {}))
        
        # Get destinations for this curriculum
        destinations = get_destinations_for_curriculum(curriculum)
        
        # Calculate priority and entry level for each destination
        path_items = []
        for dest in destinations:
            dest_id = dest['id']
            
            # Get assessment data
            assess = assessment_data.get(dest_id, {})
            confidence = assess.get('confidence')
            quiz_pct = assess.get('quiz_percentage')
            
            # Get progress data
            prog = progress_data.get(dest_id, {})
            has_progress = prog.get('max_level', 0) > 1
            current_level = prog.get('max_level', 0)
            
            # Get exam weight
            exam_weight = exam_weights.get(dest_id, 3)
            
            # Calculate entry level
            entry_level = calculate_entry_level(confidence, quiz_pct)
            
            # If they already have progress, don't go below their level
            if current_level > entry_level:
                entry_level = current_level
            
            # Calculate priority
            priority = calculate_priority_score(
                confidence, quiz_pct, exam_weight, has_progress, current_level
            )
            
            path_items.append({
                'destination_id': dest_id,
                'priority': priority,
                'entry_level': entry_level,
                'confidence': confidence,
                'quiz_percentage': quiz_pct,
                'current_level': current_level,
                'exam_weight': exam_weight
            })
        
        # Sort by priority (highest first)
        path_items.sort(key=lambda x: x['priority'], reverse=True)
        
        # Update itinerary in database
        for order, item in enumerate(path_items, 1):
            # Check if itinerary entry exists
            existing = db.session.execute(text("""
                SELECT id FROM passport_itinerary
                WHERE passport_id = :passport_id AND destination_id = :dest_id
            """), {'passport_id': passport_id, 'dest_id': item['destination_id']}).fetchone()
            
            if existing:
                db.session.execute(text("""
                    UPDATE passport_itinerary
                    SET stop_order = :order,
                        suggested_start_level = :entry_level,
                        priority = :priority_level,
                        status = CASE 
                            WHEN :current_level >= 12 THEN 'completed'
                            WHEN :current_level > 1 THEN 'current'
                            ELSE 'planned'
                        END
                    WHERE passport_id = :passport_id AND destination_id = :dest_id
                """), {
                    'order': order,
                    'entry_level': item['entry_level'],
                    'priority_level': 'high' if item['priority'] >= 12 else 'normal' if item['priority'] >= 8 else 'low',
                    'current_level': item['current_level'],
                    'passport_id': passport_id,
                    'dest_id': item['destination_id']
                })
            else:
                db.session.execute(text("""
                    INSERT INTO passport_itinerary 
                    (passport_id, destination_id, stop_order, suggested_start_level, priority, status, added_by)
                    VALUES (:passport_id, :dest_id, :order, :entry_level, :priority_level, :status, 'system')
                """), {
                    'passport_id': passport_id,
                    'dest_id': item['destination_id'],
                    'order': order,
                    'entry_level': item['entry_level'],
                    'priority_level': 'high' if item['priority'] >= 12 else 'normal' if item['priority'] >= 8 else 'low',
                    'status': 'completed' if item['current_level'] >= 12 else 'current' if item['current_level'] > 1 else 'planned'
                })
        
        db.session.commit()
        
        return {
            'success': True,
            'path': path_items,
            'message': f'Learning path generated with {len(path_items)} destinations'
        }
        
    except Exception as e:
        db.session.rollback()
        print(f"Error generating learning path: {e}")
        import traceback
        traceback.print_exc()
        return {'success': False, 'error': str(e)}


@passport_bp.route('/api/passport/generate-path', methods=['POST'])
@passport_login_required
def api_generate_path():
    """API endpoint to generate/regenerate learning path"""
    from sqlalchemy import text
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    try:
        # Get passport
        if user_id:
            passport = db.session.execute(text("""
                SELECT id, target_curriculum FROM student_passport WHERE user_id = :user_id
            """), {'user_id': user_id}).fetchone()
        else:
            passport = db.session.execute(text("""
                SELECT id, target_curriculum FROM student_passport WHERE guest_code = :guest_code
            """), {'guest_code': guest_code}).fetchone()
        
        if not passport:
            return jsonify({'error': 'Passport not found'}), 404
        
        passport_id = passport[0]
        curriculum = passport[1] or 'JC'
        
        result = generate_learning_path(passport_id, user_id, guest_code, curriculum)
        
        return jsonify(result)
        
    except Exception as e:
        print(f"Error in generate path API: {e}")
        return jsonify({'error': str(e)}), 500


# ==================== QUICK CHECK QUESTIONS ====================

QUICK_CHECK_QUESTIONS = {
    'JC': [
        {
            'id': 1,
            'skill': 'number_island',
            'question': 'Calculate: 17 × 8',
            'answer': '136',
            'type': 'numeric',
            'time_limit': 20
        },
        {
            'id': 2,
            'skill': 'number_island',
            'question': 'What is 5 + 3 × 4?',
            'answer': '17',
            'type': 'numeric',
            'hint': 'Remember BODMAS!',
            'time_limit': 20
        },
        {
            'id': 3,
            'skill': 'fraction_falls',
            'question': 'Calculate: ½ + ¼',
            'answer': '3/4',
            'alt_answers': ['0.75', '¾'],
            'type': 'text',
            'time_limit': 30
        },
        {
            'id': 4,
            'skill': 'decimal_desert',
            'question': 'Calculate: 0.3 × 0.2',
            'answer': '0.06',
            'type': 'numeric',
            'time_limit': 25
        },
        {
            'id': 5,
            'skill': 'percentage_peak',
            'question': 'What is 25% of 80?',
            'answer': '20',
            'type': 'numeric',
            'time_limit': 25
        },
        {
            'id': 6,
            'skill': 'algebra_alps',
            'question': 'Solve: 2x + 5 = 13',
            'answer': '4',
            'type': 'numeric',
            'time_limit': 30
        },
        {
            'id': 7,
            'skill': 'algebra_alps',
            'question': 'Simplify: 3x + 2x - x',
            'answer': '4x',
            'type': 'text',
            'time_limit': 25
        },
        {
            'id': 8,
            'skill': 'geometry_grove',
            'question': 'What is the area of a rectangle with length 6cm and width 4cm?',
            'answer': '24',
            'type': 'numeric',
            'unit': 'cm²',
            'time_limit': 25
        },
        {
            'id': 9,
            'skill': 'statistics_city',
            'question': 'Find the mean of: 4, 7, 3, 6, 5',
            'answer': '5',
            'type': 'numeric',
            'time_limit': 30
        },
        {
            'id': 10,
            'skill': 'probability_port',
            'question': 'A fair dice is rolled. What is P(even number)?',
            'answer': '1/2',
            'alt_answers': ['0.5', '50%', '3/6', '½'],
            'type': 'text',
            'time_limit': 30
        }
    ],
    'LC': [
        {
            'id': 1,
            'skill': 'algebra_alps',
            'question': 'Solve: 3x - 7 = 2x + 5',
            'answer': '12',
            'type': 'numeric',
            'time_limit': 30
        },
        {
            'id': 2,
            'skill': 'algebra_alps',
            'question': 'Expand: (x + 3)(x - 2)',
            'answer': 'x²+x-6',
            'alt_answers': ['x^2+x-6', 'x² + x - 6', 'x^2 + x - 6'],
            'type': 'text',
            'time_limit': 40
        },
        {
            'id': 3,
            'skill': 'trigonometry_towers',
            'question': 'What is sin(30°)?',
            'answer': '0.5',
            'alt_answers': ['1/2', '½'],
            'type': 'text',
            'time_limit': 20
        },
        {
            'id': 4,
            'skill': 'function_forest',
            'question': 'If f(x) = 2x + 3, find f(4)',
            'answer': '11',
            'type': 'numeric',
            'time_limit': 25
        },
        {
            'id': 5,
            'skill': 'geometry_grove',
            'question': 'Find the distance from (0,0) to (3,4)',
            'answer': '5',
            'type': 'numeric',
            'time_limit': 30
        },
        {
            'id': 6,
            'skill': 'indices_inn',
            'question': 'Simplify: 2³ × 2²',
            'answer': '32',
            'type': 'numeric',
            'time_limit': 25
        },
        {
            'id': 7,
            'skill': 'percentage_peak',
            'question': 'Increase 80 by 15%',
            'answer': '92',
            'type': 'numeric',
            'time_limit': 30
        },
        {
            'id': 8,
            'skill': 'statistics_city',
            'question': 'The median of 3, 7, 9, 12, 15 is?',
            'answer': '9',
            'type': 'numeric',
            'time_limit': 25
        },
        {
            'id': 9,
            'skill': 'complex_kingdom',
            'question': 'Simplify: (2 + 3i) + (4 - i)',
            'answer': '6+2i',
            'alt_answers': ['6 + 2i'],
            'type': 'text',
            'time_limit': 30
        },
        {
            'id': 10,
            'skill': 'financial_district',
            'question': '€1000 invested at 5% compound interest for 1 year becomes?',
            'answer': '1050',
            'type': 'numeric',
            'unit': '€',
            'time_limit': 30
        }
    ]
}


@passport_bp.route('/api/passport/quick-check', methods=['GET'])
@passport_login_required
def get_quick_check():
    """Get quick check questions for a curriculum"""
    curriculum = request.args.get('curriculum', 'JC')
    
    # Map curriculum codes to question sets
    if curriculum in ['LC_HL', 'LC_OL', 'LC']:
        questions = QUICK_CHECK_QUESTIONS.get('LC', [])
    else:
        questions = QUICK_CHECK_QUESTIONS.get('JC', [])
    
    # Return questions without answers
    safe_questions = []
    for q in questions:
        safe_q = {
            'id': q['id'],
            'skill': q['skill'],
            'question': q['question'],
            'type': q['type'],
            'time_limit': q.get('time_limit', 30),
            'hint': q.get('hint'),
            'unit': q.get('unit')
        }
        safe_questions.append(safe_q)
    
    return jsonify({
        'questions': safe_questions,
        'total': len(safe_questions),
        'curriculum': curriculum
    })


@passport_bp.route('/api/passport/quick-check', methods=['POST'])
@passport_login_required
def submit_quick_check():
    """Submit quick check answers and get results"""
    from sqlalchemy import text
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    data = request.json
    answers = data.get('answers', {})  # {question_id: answer}
    curriculum = data.get('curriculum', 'JC')
    
    # Get questions for this curriculum
    if curriculum in ['LC_HL', 'LC_OL', 'LC']:
        questions = QUICK_CHECK_QUESTIONS.get('LC', [])
    else:
        questions = QUICK_CHECK_QUESTIONS.get('JC', [])
    
    # Grade answers
    results = []
    skill_scores = {}  # {skill: {'correct': 0, 'total': 0}}
    
    for q in questions:
        q_id = str(q['id'])
        user_answer = str(answers.get(q_id, '')).strip().lower().replace(' ', '')
        correct_answer = str(q['answer']).strip().lower().replace(' ', '')
        
        # Check main answer and alternatives
        is_correct = (user_answer == correct_answer)
        if not is_correct and 'alt_answers' in q:
            for alt in q['alt_answers']:
                if user_answer == str(alt).strip().lower().replace(' ', ''):
                    is_correct = True
                    break
        
        # Track by skill
        skill = q['skill']
        if skill not in skill_scores:
            skill_scores[skill] = {'correct': 0, 'total': 0}
        skill_scores[skill]['total'] += 1
        if is_correct:
            skill_scores[skill]['correct'] += 1
        
        results.append({
            'question_id': q['id'],
            'correct': is_correct,
            'skill': skill
        })
    
    # Calculate overall score
    total_correct = sum(1 for r in results if r['correct'])
    total_questions = len(results)
    overall_percentage = round((total_correct / total_questions) * 100) if total_questions > 0 else 0
    
    # Generate recommendations based on skill scores
    recommendations = []
    for skill, scores in skill_scores.items():
        percentage = round((scores['correct'] / scores['total']) * 100) if scores['total'] > 0 else 0
        
        dest = DESTINATIONS.get(skill, {})
        dest_name = dest.get('display_name', skill)
        
        if percentage < 50:
            recommendations.append({
                'skill': skill,
                'destination': dest_name,
                'level': 'needs_work',
                'suggested_start': 1,
                'message': f'Start from the basics in {dest_name}'
            })
        elif percentage < 80:
            recommendations.append({
                'skill': skill,
                'destination': dest_name,
                'level': 'developing',
                'suggested_start': 4,
                'message': f'Good foundation in {dest_name}, build on it'
            })
        else:
            recommendations.append({
                'skill': skill,
                'destination': dest_name,
                'level': 'strong',
                'suggested_start': 7,
                'message': f'Strong skills in {dest_name}!'
            })
    
    # Save results to passport self-assessment
    try:
        # Get passport ID
        if user_id:
            passport = db.session.execute(text("""
                SELECT id FROM student_passport WHERE user_id = :user_id
            """), {'user_id': user_id}).fetchone()
        else:
            passport = db.session.execute(text("""
                SELECT id FROM student_passport WHERE guest_code = :guest_code
            """), {'guest_code': guest_code}).fetchone()
        
        if passport:
            passport_id = passport[0]
            
            # Update self-assessment with quick check scores
            for skill, scores in skill_scores.items():
                score = scores['correct']
                total = scores['total']
                
                # Check if exists
                existing = db.session.execute(text("""
                    SELECT id FROM passport_self_assessment
                    WHERE passport_id = :passport_id AND destination_id = :dest_id
                """), {'passport_id': passport_id, 'dest_id': skill}).fetchone()
                
                if existing:
                    db.session.execute(text("""
                        UPDATE passport_self_assessment
                        SET quick_check_score = :score, quick_check_questions = :total,
                            assessed_at = CURRENT_TIMESTAMP
                        WHERE passport_id = :passport_id AND destination_id = :dest_id
                    """), {
                        'score': score,
                        'total': total,
                        'passport_id': passport_id,
                        'dest_id': skill
                    })
                else:
                    db.session.execute(text("""
                        INSERT INTO passport_self_assessment 
                        (passport_id, destination_id, quick_check_score, quick_check_questions)
                        VALUES (:passport_id, :dest_id, :score, :total)
                    """), {
                        'passport_id': passport_id,
                        'dest_id': skill,
                        'score': score,
                        'total': total
                    })
            
            db.session.commit()
            
            # Generate learning path based on all assessment data
            path_result = generate_learning_path(passport_id, user_id, guest_code, curriculum)
        else:
            path_result = {'success': False}
            
    except Exception as e:
        print(f"Error saving quick check results: {e}")
        db.session.rollback()
        path_result = {'success': False}
    
    return jsonify({
        'success': True,
        'score': total_correct,
        'total': total_questions,
        'percentage': overall_percentage,
        'results': results,
        'skill_scores': {k: {'correct': v['correct'], 'total': v['total'], 
                            'percentage': round((v['correct']/v['total'])*100) if v['total'] > 0 else 0}
                        for k, v in skill_scores.items()},
        'recommendations': recommendations,
        'grade': 'A' if overall_percentage >= 80 else 'B' if overall_percentage >= 60 else 'C' if overall_percentage >= 40 else 'D',
        'path_generated': path_result.get('success', False)
    })


# ==================== REGISTRATION ====================

def create_passport_tables(database):
    """Create passport tables if they don't exist"""
    from sqlalchemy import text
    
    tables_sql = """
    CREATE TABLE IF NOT EXISTS student_passport (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        guest_code TEXT,
        target_curriculum TEXT,
        target_exam_date DATE,
        journey_started DATE DEFAULT CURRENT_DATE,
        total_distance INTEGER DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE TABLE IF NOT EXISTS passport_stamps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        passport_id INTEGER NOT NULL,
        destination_id TEXT NOT NULL,
        stamp_tier TEXT NOT NULL,
        level_start INTEGER,
        level_end INTEGER,
        earned_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        points_at_earn INTEGER
    );
    
    CREATE TABLE IF NOT EXISTS passport_itinerary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        passport_id INTEGER NOT NULL,
        destination_id TEXT NOT NULL,
        stop_order INTEGER,
        status TEXT DEFAULT 'planned',
        suggested_start_level INTEGER,
        priority TEXT DEFAULT 'normal',
        added_by TEXT DEFAULT 'student',
        teacher_notes TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE TABLE IF NOT EXISTS passport_self_assessment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        passport_id INTEGER NOT NULL,
        destination_id TEXT NOT NULL,
        confidence_rating INTEGER,
        quick_check_score INTEGER,
        quick_check_questions INTEGER,
        assessed_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE TABLE IF NOT EXISTS passport_milestones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        passport_id INTEGER NOT NULL,
        title TEXT,
        milestone_date DATE,
        milestone_type TEXT,
        target_stamps INTEGER,
        reached BOOLEAN DEFAULT 0,
        reached_at DATETIME
    );
    """
    
    try:
        # Execute each statement separately
        for statement in tables_sql.strip().split(';'):
            statement = statement.strip()
            if statement:
                database.session.execute(text(statement))
        database.session.commit()
        print("✅ Passport tables created/verified")
    except Exception as e:
        print(f"⚠️ Error creating passport tables: {e}")
        database.session.rollback()


def register_passport_routes(app, database):
    """Register passport blueprint with the Flask app"""
    global db
    db = database
    
    # Auto-create tables if they don't exist
    with app.app_context():
        create_passport_tables(database)
    
    app.register_blueprint(passport_bp)
    print("✅ Maths Passport routes registered")
