# routes/passport.py
# Passport and ILP routes for AgentMath
# Extracted from app.py for better maintainability
#
# Revision: 1.0.0
# Date: 2025-12-27
#
# Contains:
# - /passport page route
# - All /api/passport/* routes (35 routes)
# - All /api/ilp/* routes (20 routes)
# - ILP helper functions
# - Total: 56 routes

from flask import Blueprint, request, jsonify, session, render_template
from models import db
from datetime import datetime, timedelta, date
from sqlalchemy import text

# Create blueprint
passport_bp = Blueprint('passport', __name__)

# Import config
from passport_config import (
    PASSPORT_DESTINATIONS,
    PASSPORT_TOPIC_STRANDS,
    CURRICULUM_HIERARCHY,
    PASSPORT_QUIZ_CONFIG,
    PASSPORT_PLAN_CONFIG,
    ILP_PREREQUISITE_MAP,
    ILP_TOPIC_SKILL_TAGS,
    ILP_SKILL_TO_NUMERACY,
    ILP_THRESHOLDS,
    ILP_PRIORITY_CONFIG,
    get_all_topics_for_curriculum,
    calculate_entry_level_v2,
    calculate_topic_priority_v2,
    calculate_target_level_v2,
    get_week_capacity_from_calendar
)

# Import decorators
from utils.auth import guest_or_login_required, approved_required, login_required, role_required


@passport_bp.route('/passport')
@guest_or_login_required
@approved_required
def student_passport():
    """Render the Maths Passport page for learning journey tracking"""
    return render_template('student_passport.html')


@passport_bp.route('/api/passport', methods=['GET'])
@guest_or_login_required
def get_passport():
    """Get passport data for current user"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    # Get destinations list
    destinations_list = list(PASSPORT_DESTINATIONS.values())
    
    try:
        # Check if passport exists (stored in localStorage primarily, but we track setup completion)
        if user_id:
            setup_check = db.session.execute(text("""
                SELECT value FROM user_preferences 
                WHERE user_id = :uid AND key = 'passport_setup_complete'
            """), {'uid': user_id}).fetchone()
        else:
            setup_check = db.session.execute(text("""
                SELECT value FROM guest_preferences 
                WHERE guest_code = :code AND key = 'passport_setup_complete'
            """), {'code': guest_code}).fetchone()
        
        passport_exists = setup_check is not None and setup_check[0] == '1'
        
        if not passport_exists:
            return jsonify({
                'exists': False,
                'destinations': destinations_list
            })
        
        # Load passport data from database
        if user_id:
            passport_row = db.session.execute(text("""
                SELECT value, created_at FROM user_preferences 
                WHERE user_id = :uid AND key = 'passport_curriculum'
            """), {'uid': user_id}).fetchone()
            
            # Get stamps
            stamps = db.session.execute(text("""
                SELECT destination_id, tier, earned_at FROM passport_stamps
                WHERE user_id = :uid
            """), {'uid': user_id}).fetchall()
            
            # Get itinerary
            itinerary_row = db.session.execute(text("""
                SELECT value FROM user_preferences 
                WHERE user_id = :uid AND key = 'passport_itinerary'
            """), {'uid': user_id}).fetchone()
        else:
            passport_row = db.session.execute(text("""
                SELECT value, created_at FROM guest_preferences 
                WHERE guest_code = :code AND key = 'passport_curriculum'
            """), {'code': guest_code}).fetchone()
            
            stamps = db.session.execute(text("""
                SELECT destination_id, tier, earned_at FROM passport_stamps
                WHERE guest_code = :code
            """), {'code': guest_code}).fetchall()
            
            itinerary_row = db.session.execute(text("""
                SELECT value FROM guest_preferences 
                WHERE guest_code = :code AND key = 'passport_itinerary'
            """), {'code': guest_code}).fetchone()
        
        # Build stamps array (frontend expects array with destination_id, tier, earned_at)
        stamps_list = []
        for s in stamps:
            stamps_list.append({
                'destination_id': s[0],
                'tier': s[1],
                'earned_at': str(s[2]) if s[2] else None
            })
        
        # Parse itinerary
        itinerary = []
        if itinerary_row and itinerary_row[0]:
            import json
            try:
                itinerary = json.loads(itinerary_row[0])
            except:
                itinerary = []
        
        # Get destination progress - find max level across topics for each destination
        destination_progress = {}
        for dest_id, dest in PASSPORT_DESTINATIONS.items():
            topics = dest.get('topics', [])
            max_level = 0
            total_level = 0
            topics_with_progress = 0
            
            for topic in topics:
                if user_id:
                    prog = db.session.execute(text("""
                        SELECT current_level FROM adaptive_progress
                        WHERE user_id = :uid AND topic = :topic
                    """), {'uid': user_id, 'topic': topic}).fetchone()
                else:
                    prog = db.session.execute(text("""
                        SELECT current_level FROM adaptive_progress
                        WHERE guest_code = :code AND topic = :topic
                    """), {'code': guest_code, 'topic': topic}).fetchone()
                
                if prog and prog[0]:
                    level = prog[0]
                    max_level = max(max_level, level)
                    total_level += level
                    topics_with_progress += 1
            
            avg_level = round(total_level / topics_with_progress) if topics_with_progress > 0 else 0
            
            destination_progress[dest_id] = {
                'max_level': max_level,
                'avg_level': avg_level,
                'topics_started': topics_with_progress,
                'total_topics': len(topics)
            }
        
        return jsonify({
            'exists': True,
            'destinations': destinations_list,
            'curriculum': passport_row[0] if passport_row else 'JC',
            'created_at': str(passport_row[1]) if passport_row else None,
            'stamps': stamps_list,
            'itinerary': itinerary,
            'destination_progress': destination_progress
        })
        
    except Exception as e:
        print(f"Error loading passport: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'exists': False,
            'destinations': destinations_list,
            'error': str(e)
        })


@passport_bp.route('/api/passport/student-progress', methods=['GET'])
@guest_or_login_required
def get_student_progress_for_passport():
    """Get student's existing progress across all topics for passport setup"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        # Get all topic progress
        progress_rows = []
        stats = []
        
        if user_id:
            try:
                progress_rows = db.session.execute(text("""
                    SELECT topic, current_level, current_points, updated_at
                    FROM adaptive_progress
                    WHERE user_id = :uid
                    ORDER BY current_level DESC
                """), {'uid': user_id}).fetchall()
            except:
                progress_rows = []
            
            # Get question history stats (may not exist)
            try:
                stats = db.session.execute(text("""
                    SELECT topic, COUNT(*) as questions, 
                           SUM(CASE WHEN score > 0 THEN 1 ELSE 0 END) as correct
                    FROM user_question_history
                    WHERE user_id = :uid
                    GROUP BY topic
                """), {'uid': user_id}).fetchall()
            except:
                stats = []
        else:
            try:
                progress_rows = db.session.execute(text("""
                    SELECT topic, current_level, current_points, updated_at
                    FROM adaptive_progress
                    WHERE guest_code = :code
                    ORDER BY current_level DESC
                """), {'code': guest_code}).fetchall()
            except:
                progress_rows = []
            
            # Get question history stats (may not have guest_code column)
            try:
                stats = db.session.execute(text("""
                    SELECT topic, COUNT(*) as questions,
                           SUM(CASE WHEN score > 0 THEN 1 ELSE 0 END) as correct
                    FROM user_question_history
                    WHERE guest_code = :code
                    GROUP BY topic
                """), {'code': guest_code}).fetchall()
            except:
                stats = []
        
        # Build topic progress dict
        topic_progress = {}
        for row in progress_rows:
            topic_progress[row[0]] = {
                'level': row[1],
                'points': row[2] or 0,
                'updated_at': str(row[3]) if row[3] else None
            }
        
        # Build stats dict
        topic_stats = {}
        for row in stats:
            topic_stats[row[0]] = {
                'questions_answered': row[1],
                'correct': row[2] or 0,
                'accuracy': round((row[2] or 0) / row[1] * 100) if row[1] > 0 else 0
            }
        
        # Calculate destination summaries
        destination_summaries = {}
        for dest_id, dest in PASSPORT_DESTINATIONS.items():
            topics = dest.get('topics', [])
            levels = []
            total_questions = 0
            total_correct = 0
            
            for topic in topics:
                if topic in topic_progress:
                    levels.append(topic_progress[topic]['level'])
                if topic in topic_stats:
                    total_questions += topic_stats[topic]['questions_answered']
                    total_correct += topic_stats[topic]['correct']
            
            max_level = max(levels) if levels else 0
            avg_level = round(sum(levels) / len(levels)) if levels else 0
            
            # Suggest confidence based on progress
            if avg_level >= 8:
                suggested_confidence = 5  # 😎
            elif avg_level >= 6:
                suggested_confidence = 4  # 🙂
            elif avg_level >= 4:
                suggested_confidence = 3  # 😐
            elif avg_level >= 2:
                suggested_confidence = 2  # 😕
            else:
                suggested_confidence = 1  # 😰
            
            destination_summaries[dest_id] = {
                'display_name': dest['display_name'],
                'icon': dest['icon'],
                'max_level': max_level,
                'avg_level': avg_level,
                'topics_practiced': len(levels),
                'total_topics': len(topics),
                'questions_answered': total_questions,
                'accuracy': round(total_correct / total_questions * 100) if total_questions > 0 else 0,
                'suggested_confidence': suggested_confidence
            }
        
        # Identify strengths and areas to improve
        strengths = [d for d, s in destination_summaries.items() if s['avg_level'] >= 6]
        needs_work = [d for d, s in destination_summaries.items() if s['avg_level'] < 4 and s['topics_practiced'] > 0]
        not_started = [d for d, s in destination_summaries.items() if s['topics_practiced'] == 0]
        
        return jsonify({
            'has_progress': len(topic_progress) > 0,
            'topic_progress': topic_progress,
            'topic_stats': topic_stats,
            'destination_summaries': destination_summaries,
            'strengths': strengths,
            'needs_work': needs_work,
            'not_started': not_started,
            'total_topics_practiced': len(topic_progress),
            'total_questions_answered': sum(s['questions_answered'] for s in topic_stats.values())
        })
        
    except Exception as e:
        print(f"Error getting student progress: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/setup', methods=['POST'])
@guest_or_login_required
def setup_passport():
    """Initialize passport with curriculum choice"""
    from sqlalchemy import text
    
    data = request.json
    curriculum = data.get('curriculum', 'JC')
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        if user_id:
            # Save curriculum
            db.session.execute(text("""
                INSERT INTO user_preferences (user_id, key, value)
                VALUES (:uid, 'passport_curriculum', :curr)
                ON CONFLICT(user_id, key) DO UPDATE SET value = :curr
            """), {'uid': user_id, 'curr': curriculum})
            
            # Mark setup complete
            db.session.execute(text("""
                INSERT INTO user_preferences (user_id, key, value)
                VALUES (:uid, 'passport_setup_complete', '1')
                ON CONFLICT(user_id, key) DO UPDATE SET value = '1'
            """), {'uid': user_id})
        else:
            db.session.execute(text("""
                INSERT INTO guest_preferences (guest_code, key, value)
                VALUES (:code, 'passport_curriculum', :curr)
                ON CONFLICT(guest_code, key) DO UPDATE SET value = :curr
            """), {'code': guest_code, 'curr': curriculum})
            
            db.session.execute(text("""
                INSERT INTO guest_preferences (guest_code, key, value)
                VALUES (:code, 'passport_setup_complete', '1')
                ON CONFLICT(guest_code, key) DO UPDATE SET value = '1'
            """), {'code': guest_code})
        
        db.session.commit()
        return jsonify({'success': True, 'curriculum': curriculum})
        
    except Exception as e:
        db.session.rollback()
        print(f"Error setting up passport: {e}")
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/self-assessment', methods=['POST'])
@guest_or_login_required
def save_self_assessment():
    """Save self-assessment results"""
    from sqlalchemy import text
    import json
    
    data = request.json
    assessment = data.get('assessment', {})
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        assessment_json = json.dumps(assessment)
        
        if user_id:
            db.session.execute(text("""
                INSERT INTO user_preferences (user_id, key, value)
                VALUES (:uid, 'passport_self_assessment', :data)
                ON CONFLICT(user_id, key) DO UPDATE SET value = :data
            """), {'uid': user_id, 'data': assessment_json})
        else:
            db.session.execute(text("""
                INSERT INTO guest_preferences (guest_code, key, value)
                VALUES (:code, 'passport_self_assessment', :data)
                ON CONFLICT(guest_code, key) DO UPDATE SET value = :data
            """), {'code': guest_code, 'data': assessment_json})
        
        db.session.commit()
        return jsonify({'success': True})
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/quick-check', methods=['GET'])
@guest_or_login_required
def get_quick_check_questions():
    """Get quick check diagnostic questions"""
    from sqlalchemy import text
    
    curriculum = request.args.get('curriculum', 'JC')
    
    # Generate diagnostic questions based on curriculum
    # These are simple questions to assess baseline level
    questions = []
    
    if curriculum in ['JC', 'LC_OL', 'LC_HL']:
        questions = [
            # Number Skills - Fractions
            {
                'id': 'qc1',
                'topic': 'fractions',
                'destination': 'number_explorers',
                'question': 'What is 1/2 + 1/4?',
                'options': ['1/4', '3/4', '2/6', '1/6'],
                'correct': 1,
                'level': 4,
                'skill_area': 'Fractions'
            },
            # Number Skills - Percentages  
            {
                'id': 'qc2',
                'topic': 'percentages',
                'destination': 'number_explorers',
                'question': 'What is 25% of 80?',
                'options': ['15', '20', '25', '40'],
                'correct': 1,
                'level': 4,
                'skill_area': 'Percentages'
            },
            # Algebra - Basic equations
            {
                'id': 'qc3',
                'topic': 'introductory_algebra',
                'destination': 'algebra_alps',
                'question': 'Solve: 2x + 3 = 11. What is x?',
                'options': ['3', '4', '5', '7'],
                'correct': 1,
                'level': 4,
                'skill_area': 'Algebra'
            },
            # Algebra - Simplifying
            {
                'id': 'qc4',
                'topic': 'simplifying_expressions',
                'destination': 'algebra_alps',
                'question': 'Simplify: 3x + 2x - x',
                'options': ['4x', '5x', '6x', '3x'],
                'correct': 0,
                'level': 4,
                'skill_area': 'Algebra'
            },
            # Geometry - Area
            {
                'id': 'qc5',
                'topic': 'geometry',
                'destination': 'geometry_gardens',
                'question': 'A rectangle is 6cm by 4cm. What is its area?',
                'options': ['10 sq cm', '20 sq cm', '24 sq cm', '48 sq cm'],
                'correct': 2,
                'level': 4,
                'skill_area': 'Geometry'
            },
            # Geometry - Angles
            {
                'id': 'qc6',
                'topic': 'angles',
                'destination': 'geometry_gardens',
                'question': 'What do the angles in a triangle add up to?',
                'options': ['90 degrees', '180 degrees', '270 degrees', '360 degrees'],
                'correct': 1,
                'level': 4,
                'skill_area': 'Geometry'
            },
            # Functions
            {
                'id': 'qc7',
                'topic': 'functions',
                'destination': 'function_factory',
                'question': 'If f(x) = 2x + 1, what is f(3)?',
                'options': ['5', '6', '7', '8'],
                'correct': 2,
                'level': 6,
                'skill_area': 'Functions'
            },
            # Statistics
            {
                'id': 'qc8',
                'topic': 'statistics',
                'destination': 'stats_station',
                'question': 'What is the mean of: 2, 4, 6, 8?',
                'options': ['4', '5', '6', '20'],
                'correct': 1,
                'level': 4,
                'skill_area': 'Statistics'
            },
            # Probability
            {
                'id': 'qc9',
                'topic': 'probability',
                'destination': 'stats_station',
                'question': 'A bag has 3 red and 2 blue balls. What is the probability of picking red?',
                'options': ['1/5', '2/5', '3/5', '3/2'],
                'correct': 2,
                'level': 4,
                'skill_area': 'Probability'
            },
            # Trigonometry - Pythagoras
            {
                'id': 'qc10',
                'topic': 'pythagoras',
                'destination': 'trig_towers',
                'question': 'In a right triangle with sides 3 and 4, what is the hypotenuse?',
                'options': ['5', '6', '7', '12'],
                'correct': 0,
                'level': 6,
                'skill_area': 'Trigonometry'
            }
        ]
    else:  # L1LP, L2LP
        questions = [
            {
                'id': 'qc1',
                'topic': 'addition',
                'destination': 'numeracy_nation',
                'question': 'What is 7 + 8?',
                'options': ['14', '15', '16', '17'],
                'correct': 1,
                'level': 1,
                'skill_area': 'Addition'
            },
            {
                'id': 'qc2',
                'topic': 'subtraction',
                'destination': 'numeracy_nation',
                'question': 'What is 15 - 7?',
                'options': ['6', '7', '8', '9'],
                'correct': 2,
                'level': 1,
                'skill_area': 'Subtraction'
            },
            {
                'id': 'qc3',
                'topic': 'multiplication',
                'destination': 'numeracy_nation',
                'question': 'What is 6 times 4?',
                'options': ['20', '22', '24', '26'],
                'correct': 2,
                'level': 4,
                'skill_area': 'Multiplication'
            },
            {
                'id': 'qc4',
                'topic': 'division',
                'destination': 'numeracy_nation',
                'question': 'What is 20 divided by 4?',
                'options': ['4', '5', '6', '8'],
                'correct': 1,
                'level': 4,
                'skill_area': 'Division'
            },
            {
                'id': 'qc5',
                'topic': 'fractions',
                'destination': 'number_explorers',
                'question': 'What is half of 10?',
                'options': ['2', '4', '5', '10'],
                'correct': 2,
                'level': 2,
                'skill_area': 'Fractions'
            }
        ]
    
    return jsonify({'questions': questions})


@passport_bp.route('/api/passport/quick-check', methods=['POST'])
@guest_or_login_required
def submit_quick_check():
    """Submit quick check answers and get entry levels"""
    from sqlalchemy import text
    import json
    
    data = request.json
    answers = data.get('answers', {})
    questions = data.get('questions', [])
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    # Calculate scores per topic
    topic_scores = {}
    for q in questions:
        topic = q.get('topic', 'general')
        q_id = q.get('id')
        correct = q.get('correct')
        user_answer = answers.get(q_id)
        
        if topic not in topic_scores:
            topic_scores[topic] = {'correct': 0, 'total': 0, 'max_level_passed': 0}
        
        topic_scores[topic]['total'] += 1
        
        if user_answer == correct:
            topic_scores[topic]['correct'] += 1
            level = q.get('level', 1)
            if level > topic_scores[topic]['max_level_passed']:
                topic_scores[topic]['max_level_passed'] = level
    
    # Determine entry levels
    entry_levels = {}
    destination_scores = {}
    total_correct = 0
    total_questions = len(questions)
    
    for topic, scores in topic_scores.items():
        if scores['total'] == 0:
            entry_levels[topic] = 1
        else:
            accuracy = scores['correct'] / scores['total']
            if accuracy >= 0.8:
                entry_levels[topic] = min(scores['max_level_passed'] + 3, 10)
            elif accuracy >= 0.5:
                entry_levels[topic] = scores['max_level_passed']
            else:
                entry_levels[topic] = max(1, scores['max_level_passed'] - 3)
        
        total_correct += scores['correct']
    
    # Calculate destination scores from questions
    for q in questions:
        dest = q.get('destination', 'general')
        q_id = q.get('id')
        correct_answer = q.get('correct')
        user_answer = answers.get(q_id)
        
        if dest not in destination_scores:
            destination_scores[dest] = {'correct': 0, 'total': 0}
        
        destination_scores[dest]['total'] += 1
        if user_answer == correct_answer:
            destination_scores[dest]['correct'] += 1
    
    # Calculate overall grade
    overall_percentage = (total_correct / total_questions * 100) if total_questions > 0 else 0
    if overall_percentage >= 80:
        grade = 'A'
    elif overall_percentage >= 60:
        grade = 'B'
    elif overall_percentage >= 40:
        grade = 'C'
    else:
        grade = 'D'
    
    # Build skill scores for display
    skill_scores = {}
    for dest_id, scores in destination_scores.items():
        percentage = (scores['correct'] / scores['total'] * 100) if scores['total'] > 0 else 0
        skill_scores[dest_id] = {
            'correct': scores['correct'],
            'total': scores['total'],
            'percentage': round(percentage)
        }
    
    # Build recommendations
    recommendations = []
    for dest_id, scores in destination_scores.items():
        percentage = (scores['correct'] / scores['total'] * 100) if scores['total'] > 0 else 0
        dest_info = PASSPORT_DESTINATIONS.get(dest_id, {})
        
        if percentage >= 80:
            level = 'strong'
            message = f"{dest_info.get('display_name', dest_id)}: Great foundation! Start at Level 7+"
        elif percentage >= 50:
            level = 'developing'
            message = f"{dest_info.get('display_name', dest_id)}: Building skills. Start at Level 4"
        else:
            level = 'focus'
            message = f"{dest_info.get('display_name', dest_id)}: Focus area. Start from basics"
        
        recommendations.append({
            'skill': dest_id,
            'level': level,
            'message': message
        })
    
    # Save results
    try:
        results_json = json.dumps({
            'answers': answers,
            'scores': topic_scores,
            'entry_levels': entry_levels
        })
        
        if user_id:
            db.session.execute(text("""
                INSERT INTO user_preferences (user_id, key, value)
                VALUES (:uid, 'passport_quick_check', :data)
                ON CONFLICT(user_id, key) DO UPDATE SET value = :data
            """), {'uid': user_id, 'data': results_json})
        else:
            db.session.execute(text("""
                INSERT INTO guest_preferences (guest_code, key, value)
                VALUES (:code, 'passport_quick_check', :data)
                ON CONFLICT(guest_code, key) DO UPDATE SET value = :data
            """), {'code': guest_code, 'data': results_json})
        
        db.session.commit()
        
    except Exception as e:
        print(f"Error saving quick check: {e}")
    
    return jsonify({
        'success': True,
        'score': total_correct,
        'total': total_questions,
        'grade': grade,
        'skill_scores': skill_scores,
        'recommendations': recommendations,
        'entry_levels': entry_levels
    })


@passport_bp.route('/api/passport/generate-path', methods=['POST'])
@guest_or_login_required
def generate_learning_path():
    """Generate personalized learning path based on assessment"""
    from sqlalchemy import text
    import json
    
    data = request.json or {}
    priorities = data.get('priorities', [])
    entry_levels = data.get('entry_levels', {})
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    # If no priorities provided, use all destinations in default order
    if not priorities:
        # Get curriculum to filter destinations
        try:
            if user_id:
                curr_row = db.session.execute(text("""
                    SELECT value FROM user_preferences 
                    WHERE user_id = :uid AND key = 'passport_curriculum'
                """), {'uid': user_id}).fetchone()
            else:
                curr_row = db.session.execute(text("""
                    SELECT value FROM guest_preferences 
                    WHERE guest_code = :code AND key = 'passport_curriculum'
                """), {'code': guest_code}).fetchone()
            
            curriculum = curr_row[0] if curr_row else 'JC'
        except:
            curriculum = 'JC'
        
        # Get destinations that match curriculum
        for dest_id, dest in PASSPORT_DESTINATIONS.items():
            if curriculum in dest.get('curriculum', []):
                priorities.append(dest_id)
    
    # If still no priorities, use all destinations
    if not priorities:
        priorities = list(PASSPORT_DESTINATIONS.keys())
    
    # Build itinerary from priorities
    itinerary = []
    order = 1
    
    for dest_id in priorities:
        dest = PASSPORT_DESTINATIONS.get(dest_id, {})
        topics = dest.get('topics', [])
        
        # Determine entry level for this destination
        entry_level = 1
        for topic in topics:
            if topic in entry_levels:
                entry_level = max(entry_level, entry_levels[topic])
        
        itinerary.append({
            'order': order,
            'destination_id': dest_id,
            'entry_level': entry_level,
            'status': 'not_started'
        })
        order += 1
    
    # Save itinerary
    try:
        itinerary_json = json.dumps(itinerary)
        
        if user_id:
            db.session.execute(text("""
                INSERT INTO user_preferences (user_id, key, value)
                VALUES (:uid, 'passport_itinerary', :data)
                ON CONFLICT(user_id, key) DO UPDATE SET value = :data
            """), {'uid': user_id, 'data': itinerary_json})
        else:
            db.session.execute(text("""
                INSERT INTO guest_preferences (guest_code, key, value)
                VALUES (:code, 'passport_itinerary', :data)
                ON CONFLICT(guest_code, key) DO UPDATE SET value = :data
            """), {'code': guest_code, 'data': itinerary_json})
        
        db.session.commit()
        
    except Exception as e:
        db.session.rollback()
        print(f"Error saving itinerary: {e}")
        return jsonify({'error': str(e)}), 500
    
    return jsonify({
        'success': True,
        'itinerary': itinerary
    })


@passport_bp.route('/api/passport/stamps', methods=['GET'])
@guest_or_login_required
def get_passport_stamps():
    """Get all stamps with progress information for each destination"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    stamps_data = []
    
    try:
        for dest_id, dest in PASSPORT_DESTINATIONS.items():
            topics = dest.get('topics', [])
            if not topics:
                continue
            
            # Get current stamp tier for this destination
            if user_id:
                existing = db.session.execute(text("""
                    SELECT tier, earned_at FROM passport_stamps
                    WHERE user_id = :uid AND destination_id = :dest
                """), {'uid': user_id, 'dest': dest_id}).fetchone()
            else:
                existing = db.session.execute(text("""
                    SELECT tier, earned_at FROM passport_stamps
                    WHERE guest_code = :code AND destination_id = :dest
                """), {'code': guest_code, 'dest': dest_id}).fetchone()
            
            current_tier = existing[0] if existing else None
            earned_at = existing[1].isoformat() if existing and existing[1] else None
            
            # Get progress for each topic in this destination
            topic_progress = []
            total_level = 0
            topics_with_progress = 0
            
            for topic in topics:
                if user_id:
                    level_row = db.session.execute(text("""
                        SELECT current_level FROM adaptive_progress
                        WHERE user_id = :uid AND topic = :topic
                    """), {'uid': user_id, 'topic': topic}).fetchone()
                else:
                    level_row = db.session.execute(text("""
                        SELECT current_level FROM adaptive_progress
                        WHERE guest_code = :code AND topic = :topic
                    """), {'code': guest_code, 'topic': topic}).fetchone()
                
                level = level_row[0] if level_row else 0
                topic_progress.append({
                    'topic_id': topic,
                    'current_level': level
                })
                
                if level > 0:
                    total_level += level
                    topics_with_progress += 1
            
            # Calculate average level (only for topics with progress)
            avg_level = total_level / topics_with_progress if topics_with_progress > 0 else 0
            
            # Calculate progress toward next tier
            # Bronze: avg >= 4, Silver: avg >= 7, Gold: avg >= 10
            if avg_level >= 10:
                next_tier = None
                progress_percent = 100
            elif avg_level >= 7:
                next_tier = 'gold'
                progress_percent = int(((avg_level - 7) / 3) * 100)
            elif avg_level >= 4:
                next_tier = 'silver'
                progress_percent = int(((avg_level - 4) / 3) * 100)
            else:
                next_tier = 'bronze'
                progress_percent = int((avg_level / 4) * 100)
            
            stamps_data.append({
                'destination_id': dest_id,
                'display_name': dest['display_name'],
                'icon': dest['icon'],
                'colour': dest['colour'],
                'tagline': dest['tagline'],
                'current_tier': current_tier,
                'earned_at': earned_at,
                'avg_level': round(avg_level, 1),
                'next_tier': next_tier,
                'progress_percent': progress_percent,
                'topics_count': len(topics),
                'topics_started': topics_with_progress,
                'topic_progress': topic_progress
            })
        
        # Sort by progress (most progress first)
        stamps_data.sort(key=lambda x: (
            {'gold': 3, 'silver': 2, 'bronze': 1, None: 0}.get(x['current_tier'], 0),
            x['avg_level']
        ), reverse=True)
        
    except Exception as e:
        print(f"Error fetching stamps: {e}")
        return jsonify({'error': str(e)}), 500
    
    return jsonify({
        'success': True,
        'stamps': stamps_data,
        'total_destinations': len(PASSPORT_DESTINATIONS),
        'bronze_count': sum(1 for s in stamps_data if s['current_tier'] == 'bronze'),
        'silver_count': sum(1 for s in stamps_data if s['current_tier'] == 'silver'),
        'gold_count': sum(1 for s in stamps_data if s['current_tier'] == 'gold')
    })


@passport_bp.route('/api/passport/check-stamps', methods=['POST'])
@guest_or_login_required
def check_passport_stamps():
    """Check if user has earned any new stamps based on progress"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    new_stamps = []
    
    try:
        # Check each destination
        for dest_id, dest in PASSPORT_DESTINATIONS.items():
            topics = dest.get('topics', [])
            if not topics:
                continue
            
            # Get current stamp for this destination
            if user_id:
                existing = db.session.execute(text("""
                    SELECT tier FROM passport_stamps
                    WHERE user_id = :uid AND destination_id = :dest
                """), {'uid': user_id, 'dest': dest_id}).fetchone()
            else:
                existing = db.session.execute(text("""
                    SELECT tier FROM passport_stamps
                    WHERE guest_code = :code AND destination_id = :dest
                """), {'code': guest_code, 'dest': dest_id}).fetchone()
            
            current_tier = existing[0] if existing else None
            
            # Get average level across topics for this destination
            levels = []
            for topic in topics:
                if user_id:
                    level_row = db.session.execute(text("""
                        SELECT current_level FROM adaptive_progress
                        WHERE user_id = :uid AND topic = :topic
                    """), {'uid': user_id, 'topic': topic}).fetchone()
                else:
                    level_row = db.session.execute(text("""
                        SELECT current_level FROM adaptive_progress
                        WHERE guest_code = :code AND topic = :topic
                    """), {'code': guest_code, 'topic': topic}).fetchone()
                
                if level_row:
                    levels.append(level_row[0])
            
            if not levels:
                continue
            
            avg_level = sum(levels) / len(levels)
            
            # Determine earned tier
            earned_tier = None
            if avg_level >= 10:
                earned_tier = 'gold'
            elif avg_level >= 7:
                earned_tier = 'silver'
            elif avg_level >= 4:
                earned_tier = 'bronze'
            
            if not earned_tier:
                continue
            
            # Check if this is a new/better tier
            tier_order = {'bronze': 1, 'silver': 2, 'gold': 3}
            current_order = tier_order.get(current_tier, 0)
            earned_order = tier_order.get(earned_tier, 0)
            
            if earned_order > current_order:
                # Award new stamp
                if user_id:
                    db.session.execute(text("""
                        INSERT INTO passport_stamps (user_id, destination_id, tier, earned_at)
                        VALUES (:uid, :dest, :tier, CURRENT_TIMESTAMP)
                        ON CONFLICT(user_id, destination_id) DO UPDATE SET
                            tier = :tier, earned_at = CURRENT_TIMESTAMP
                    """), {'uid': user_id, 'dest': dest_id, 'tier': earned_tier})
                else:
                    db.session.execute(text("""
                        INSERT INTO passport_stamps (guest_code, destination_id, tier, earned_at)
                        VALUES (:code, :dest, :tier, CURRENT_TIMESTAMP)
                        ON CONFLICT(guest_code, destination_id) DO UPDATE SET
                            tier = :tier, earned_at = CURRENT_TIMESTAMP
                    """), {'code': guest_code, 'dest': dest_id, 'tier': earned_tier})
                
                new_stamps.append({
                    'destination_id': dest_id,
                    'tier': earned_tier,
                    'destination': dest
                })
        
        if new_stamps:
            db.session.commit()
        
    except Exception as e:
        db.session.rollback()
        print(f"Error checking stamps: {e}")
    
    return jsonify({
        'new_stamps': new_stamps
    })


# =====================================================
# REACTIVE LEARNING ENGINE (Passport Option C)
# =====================================================
# Dynamically adjusts learning path based on quiz performance

REACTIVE_THRESHOLDS = {
    'struggling_accuracy': 0.50,      # Below 50% = struggling
    'excelling_accuracy': 0.85,       # Above 85% = excelling
    'min_questions_for_analysis': 5,  # Need at least 5 questions
    'lookback_questions': 10,         # Analyze last 10 questions
    'confidence_threshold': 0.7       # Confidence needed to recommend change
}

LEVEL_TIERS = {
    'foundation': [1, 2, 3],    # L1-3: Foundation
    'developing': [4, 5, 6],    # L4-6: Developing
    'proficient': [7, 8, 9],    # L7-9: Proficient
    'mastery': [10, 11, 12]     # L10-12: Mastery
}

def get_level_tier(level):
    """Get the tier name for a level"""
    for tier_name, levels in LEVEL_TIERS.items():
        if level in levels:
            return tier_name
    return 'foundation'

def get_tier_entry_level(tier_name):
    """Get the entry level for a tier"""
    tier_entries = {'foundation': 1, 'developing': 4, 'proficient': 7, 'mastery': 10}
    return tier_entries.get(tier_name, 1)

def get_next_tier_entry(current_level):
    """Get the entry level for the next tier up"""
    if current_level <= 3:
        return 4
    elif current_level <= 6:
        return 7
    elif current_level <= 9:
        return 10
    return current_level  # Already at top

def get_prev_tier_entry(current_level):
    """Get the entry level for the previous tier down"""
    if current_level >= 10:
        return 7
    elif current_level >= 7:
        return 4
    elif current_level >= 4:
        return 1
    return 1  # Already at bottom


@passport_bp.route('/api/passport/record-performance', methods=['POST'])
def record_passport_performance():
    """Record question-by-question performance for reactive analysis"""
    from sqlalchemy import text
    import uuid
    
    data = request.json
    topic = data.get('topic', '').lower().replace(' ', '_')
    level = data.get('level', 1)
    is_correct = data.get('is_correct', False)
    time_taken = data.get('time_taken_seconds', 0)
    question_number = data.get('question_number', 1)
    session_id = data.get('session_id', str(uuid.uuid4()))
    
    if not topic:
        return jsonify({'error': 'Topic is required'}), 400
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        if user_id:
            db.session.execute(text("""
                INSERT INTO passport_performance 
                (user_id, topic, level, question_number, is_correct, time_taken_seconds, session_id)
                VALUES (:user_id, :topic, :level, :q_num, :correct, :time, :session)
            """), {
                'user_id': user_id,
                'topic': topic,
                'level': level,
                'q_num': question_number,
                'correct': 1 if is_correct else 0,
                'time': time_taken,
                'session': session_id
            })
        else:
            db.session.execute(text("""
                INSERT INTO passport_performance 
                (guest_code, topic, level, question_number, is_correct, time_taken_seconds, session_id)
                VALUES (:guest_code, :topic, :level, :q_num, :correct, :time, :session)
            """), {
                'guest_code': guest_code,
                'topic': topic,
                'level': level,
                'q_num': question_number,
                'correct': 1 if is_correct else 0,
                'time': time_taken,
                'session': session_id
            })
        
        db.session.commit()
        return jsonify({'success': True, 'session_id': session_id})
        
    except Exception as e:
        db.session.rollback()
        print(f"Error recording performance: {e}")
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/analyze-performance/<topic>', methods=['GET'])
def analyze_passport_performance(topic):
    """Analyze recent performance and generate recommendation"""
    from sqlalchemy import text
    
    topic = topic.lower().replace(' ', '_')
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        # Get recent performance data
        if user_id:
            recent = db.session.execute(text("""
                SELECT level, is_correct, time_taken_seconds, created_at
                FROM passport_performance
                WHERE user_id = :user_id AND topic = :topic
                ORDER BY created_at DESC
                LIMIT :limit
            """), {
                'user_id': user_id,
                'topic': topic,
                'limit': REACTIVE_THRESHOLDS['lookback_questions']
            }).fetchall()
            
            # Get current adaptive level
            current_level_row = db.session.execute(text("""
                SELECT current_level FROM adaptive_progress
                WHERE user_id = :user_id AND topic = :topic
            """), {'user_id': user_id, 'topic': topic}).fetchone()
        else:
            recent = db.session.execute(text("""
                SELECT level, is_correct, time_taken_seconds, created_at
                FROM passport_performance
                WHERE guest_code = :guest_code AND topic = :topic
                ORDER BY created_at DESC
                LIMIT :limit
            """), {
                'guest_code': guest_code,
                'topic': topic,
                'limit': REACTIVE_THRESHOLDS['lookback_questions']
            }).fetchall()
            
            current_level_row = db.session.execute(text("""
                SELECT current_level FROM adaptive_progress
                WHERE guest_code = :guest_code AND topic = :topic
            """), {'guest_code': guest_code, 'topic': topic}).fetchone()
        
        current_level = current_level_row[0] if current_level_row else 1
        
        # Not enough data yet
        if len(recent) < REACTIVE_THRESHOLDS['min_questions_for_analysis']:
            return jsonify({
                'has_recommendation': False,
                'current_level': current_level,
                'questions_analyzed': len(recent),
                'min_required': REACTIVE_THRESHOLDS['min_questions_for_analysis'],
                'message': f"Need {REACTIVE_THRESHOLDS['min_questions_for_analysis'] - len(recent)} more questions for analysis"
            })
        
        # Calculate metrics
        correct_count = sum(1 for r in recent if r[1])
        accuracy = correct_count / len(recent)
        avg_time = sum(r[2] or 0 for r in recent) / len(recent) if recent else 0
        
        # Determine recommendation
        recommendation = analyze_and_recommend(
            current_level=current_level,
            accuracy=accuracy,
            question_count=len(recent),
            avg_time=avg_time
        )
        
        # Store recommendation if significant
        if recommendation['type'] != 'stay':
            store_recommendation(
                user_id=user_id,
                guest_code=guest_code,
                topic=topic,
                current_level=current_level,
                recommendation=recommendation
            )
        
        return jsonify({
            'has_recommendation': recommendation['type'] != 'stay',
            'current_level': current_level,
            'current_tier': get_level_tier(current_level),
            'questions_analyzed': len(recent),
            'accuracy': round(accuracy * 100, 1),
            'avg_time_seconds': round(avg_time, 1),
            'recommendation': recommendation
        })
        
    except Exception as e:
        print(f"Error analyzing performance: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


def analyze_and_recommend(current_level, accuracy, question_count, avg_time):
    """Generate a recommendation based on performance metrics"""
    
    current_tier = get_level_tier(current_level)
    
    # Check if struggling
    if accuracy < REACTIVE_THRESHOLDS['struggling_accuracy']:
        if current_level > 1:
            prev_tier_level = get_prev_tier_entry(current_level)
            confidence = min(1.0, (REACTIVE_THRESHOLDS['struggling_accuracy'] - accuracy) * 2 + 0.5)
            
            return {
                'type': 'level_down',
                'status': 'struggling',
                'recommended_level': prev_tier_level,
                'recommended_tier': get_level_tier(prev_tier_level),
                'confidence': round(confidence, 2),
                'reason': f"Accuracy of {round(accuracy*100)}% suggests this level may be too challenging. Consider building foundations at Level {prev_tier_level}.",
                'emoji': '🔄',
                'action_text': f'Drop to Level {prev_tier_level}',
                'encouragement': "It's smart to strengthen your foundation! You'll progress faster with solid basics."
            }
        else:
            return {
                'type': 'stay',
                'status': 'building',
                'recommended_level': current_level,
                'confidence': 0.5,
                'reason': "Keep practicing at this level to build your foundation.",
                'emoji': '💪',
                'action_text': 'Keep Practicing',
                'encouragement': "Every expert was once a beginner. Keep going!"
            }
    
    # Check if excelling
    if accuracy >= REACTIVE_THRESHOLDS['excelling_accuracy']:
        if current_level < 10:
            next_tier_level = get_next_tier_entry(current_level)
            confidence = min(1.0, (accuracy - REACTIVE_THRESHOLDS['excelling_accuracy']) * 3 + 0.6)
            
            # Bonus confidence if answering quickly
            if avg_time > 0 and avg_time < 15:  # Under 15 seconds average
                confidence = min(1.0, confidence + 0.1)
            
            return {
                'type': 'level_up',
                'status': 'excelling',
                'recommended_level': next_tier_level,
                'recommended_tier': get_level_tier(next_tier_level),
                'confidence': round(confidence, 2),
                'reason': f"Excellent! {round(accuracy*100)}% accuracy shows you've mastered this level. Ready for a bigger challenge!",
                'emoji': '🚀',
                'action_text': f'Jump to Level {next_tier_level}',
                'encouragement': "You're crushing it! Time to level up!"
            }
        else:
            return {
                'type': 'stay',
                'status': 'mastery',
                'recommended_level': current_level,
                'confidence': 0.9,
                'reason': "You're at the mastery level and performing excellently!",
                'emoji': '🏆',
                'action_text': 'Continue Mastery',
                'encouragement': "You've reached the top tier! Keep sharpening your skills."
            }
    
    # Steady progress - stay at current level
    return {
        'type': 'stay',
        'status': 'progressing',
        'recommended_level': current_level,
        'confidence': 0.8,
        'reason': f"Good progress with {round(accuracy*100)}% accuracy. Keep practicing to solidify your skills.",
        'emoji': '📈',
        'action_text': 'Keep Going',
        'encouragement': "You're making steady progress. Every question makes you stronger!"
    }


def store_recommendation(user_id, guest_code, topic, current_level, recommendation):
    """Store recommendation in database"""
    from sqlalchemy import text
    
    try:
        if user_id:
            db.session.execute(text("""
                INSERT INTO passport_recommendations 
                (user_id, topic, current_level, recommended_level, recommendation_type, confidence_score, reason)
                VALUES (:user_id, :topic, :current, :recommended, :type, :confidence, :reason)
                ON CONFLICT(user_id, topic) DO UPDATE SET
                    current_level = :current,
                    recommended_level = :recommended,
                    recommendation_type = :type,
                    confidence_score = :confidence,
                    reason = :reason,
                    is_acknowledged = 0,
                    created_at = CURRENT_TIMESTAMP
            """), {
                'user_id': user_id,
                'topic': topic,
                'current': current_level,
                'recommended': recommendation['recommended_level'],
                'type': recommendation['type'],
                'confidence': recommendation['confidence'],
                'reason': recommendation['reason']
            })
        else:
            db.session.execute(text("""
                INSERT INTO passport_recommendations 
                (guest_code, topic, current_level, recommended_level, recommendation_type, confidence_score, reason)
                VALUES (:guest_code, :topic, :current, :recommended, :type, :confidence, :reason)
                ON CONFLICT(guest_code, topic) DO UPDATE SET
                    current_level = :current,
                    recommended_level = :recommended,
                    recommendation_type = :type,
                    confidence_score = :confidence,
                    reason = :reason,
                    is_acknowledged = 0,
                    created_at = CURRENT_TIMESTAMP
            """), {
                'guest_code': guest_code,
                'topic': topic,
                'current': current_level,
                'recommended': recommendation['recommended_level'],
                'type': recommendation['type'],
                'confidence': recommendation['confidence'],
                'reason': recommendation['reason']
            })
        
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error storing recommendation: {e}")


@passport_bp.route('/api/passport/apply-recommendation', methods=['POST'])
def apply_passport_recommendation():
    """Apply a recommendation and adjust the learning level"""
    from sqlalchemy import text
    
    data = request.json
    topic = data.get('topic', '').lower().replace(' ', '_')
    new_level = data.get('new_level', 1)
    reason = data.get('reason', 'reactive_adjustment')
    
    if not topic:
        return jsonify({'error': 'Topic is required'}), 400
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        # Get current level
        if user_id:
            current = db.session.execute(text("""
                SELECT current_level FROM adaptive_progress
                WHERE user_id = :user_id AND topic = :topic
            """), {'user_id': user_id, 'topic': topic}).fetchone()
        else:
            current = db.session.execute(text("""
                SELECT current_level FROM adaptive_progress
                WHERE guest_code = :guest_code AND topic = :topic
            """), {'guest_code': guest_code, 'topic': topic}).fetchone()
        
        from_level = current[0] if current else 1
        
        # Update adaptive progress to new level
        if user_id:
            if current:
                db.session.execute(text("""
                    UPDATE adaptive_progress 
                    SET current_level = :level, updated_at = CURRENT_TIMESTAMP
                    WHERE user_id = :user_id AND topic = :topic
                """), {'level': new_level, 'user_id': user_id, 'topic': topic})
            else:
                db.session.execute(text("""
                    INSERT INTO adaptive_progress (user_id, topic, current_level, updated_at)
                    VALUES (:user_id, :topic, :level, CURRENT_TIMESTAMP)
                """), {'user_id': user_id, 'topic': topic, 'level': new_level})
            
            # Mark recommendation as acknowledged
            db.session.execute(text("""
                UPDATE passport_recommendations 
                SET is_acknowledged = 1, acknowledged_at = CURRENT_TIMESTAMP
                WHERE user_id = :user_id AND topic = :topic
            """), {'user_id': user_id, 'topic': topic})
            
            # Log the adjustment
            db.session.execute(text("""
                INSERT INTO passport_level_adjustments
                (user_id, topic, from_level, to_level, adjustment_reason)
                VALUES (:user_id, :topic, :from_level, :to_level, :reason)
            """), {
                'user_id': user_id,
                'topic': topic,
                'from_level': from_level,
                'to_level': new_level,
                'reason': reason
            })
        else:
            if current:
                db.session.execute(text("""
                    UPDATE adaptive_progress 
                    SET current_level = :level, updated_at = CURRENT_TIMESTAMP
                    WHERE guest_code = :guest_code AND topic = :topic
                """), {'level': new_level, 'guest_code': guest_code, 'topic': topic})
            else:
                db.session.execute(text("""
                    INSERT INTO adaptive_progress (guest_code, topic, current_level, updated_at)
                    VALUES (:guest_code, :topic, :level, CURRENT_TIMESTAMP)
                """), {'guest_code': guest_code, 'topic': topic, 'level': new_level})
            
            db.session.execute(text("""
                UPDATE passport_recommendations 
                SET is_acknowledged = 1, acknowledged_at = CURRENT_TIMESTAMP
                WHERE guest_code = :guest_code AND topic = :topic
            """), {'guest_code': guest_code, 'topic': topic})
            
            db.session.execute(text("""
                INSERT INTO passport_level_adjustments
                (guest_code, topic, from_level, to_level, adjustment_reason)
                VALUES (:guest_code, :topic, :from_level, :to_level, :reason)
            """), {
                'guest_code': guest_code,
                'topic': topic,
                'from_level': from_level,
                'to_level': new_level,
                'reason': reason
            })
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'topic': topic,
            'from_level': from_level,
            'to_level': new_level,
            'message': f"Level adjusted from {from_level} to {new_level}"
        })
        
    except Exception as e:
        db.session.rollback()
        print(f"Error applying recommendation: {e}")
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/get-recommendations', methods=['GET'])
def get_passport_recommendations():
    """Get all pending recommendations for the user"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        if user_id:
            recs = db.session.execute(text("""
                SELECT topic, current_level, recommended_level, recommendation_type, 
                       confidence_score, reason, is_acknowledged, created_at
                FROM passport_recommendations
                WHERE user_id = :user_id AND is_acknowledged = 0
                ORDER BY created_at DESC
            """), {'user_id': user_id}).fetchall()
        else:
            recs = db.session.execute(text("""
                SELECT topic, current_level, recommended_level, recommendation_type, 
                       confidence_score, reason, is_acknowledged, created_at
                FROM passport_recommendations
                WHERE guest_code = :guest_code AND is_acknowledged = 0
                ORDER BY created_at DESC
            """), {'guest_code': guest_code}).fetchall()
        
        return jsonify({
            'recommendations': [{
                'topic': r[0],
                'current_level': r[1],
                'recommended_level': r[2],
                'type': r[3],
                'confidence': r[4],
                'reason': r[5],
                'is_acknowledged': r[6],
                'created_at': str(r[7]) if r[7] else None
            } for r in recs]
        })
        
    except Exception as e:
        print(f"Error getting recommendations: {e}")
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/dismiss-recommendation', methods=['POST'])
def dismiss_passport_recommendation():
    """Dismiss a recommendation without applying it"""
    from sqlalchemy import text
    
    data = request.json
    topic = data.get('topic', '').lower().replace(' ', '_')
    
    if not topic:
        return jsonify({'error': 'Topic is required'}), 400
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        if user_id:
            db.session.execute(text("""
                UPDATE passport_recommendations 
                SET is_acknowledged = 1, acknowledged_at = CURRENT_TIMESTAMP
                WHERE user_id = :user_id AND topic = :topic
            """), {'user_id': user_id, 'topic': topic})
        else:
            db.session.execute(text("""
                UPDATE passport_recommendations 
                SET is_acknowledged = 1, acknowledged_at = CURRENT_TIMESTAMP
                WHERE guest_code = :guest_code AND topic = :topic
            """), {'guest_code': guest_code, 'topic': topic})
        
        db.session.commit()
        return jsonify({'success': True})
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/performance-summary/<topic>', methods=['GET'])
def get_passport_performance_summary(topic):
    """Get performance summary for a topic over time"""
    from sqlalchemy import text
    
    topic = topic.lower().replace(' ', '_')
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        # Get performance grouped by session
        if user_id:
            sessions = db.session.execute(text("""
                SELECT session_id, level,
                       COUNT(*) as questions,
                       SUM(CASE WHEN is_correct THEN 1 ELSE 0 END) as correct,
                       AVG(time_taken_seconds) as avg_time,
                       MIN(created_at) as started_at
                FROM passport_performance
                WHERE user_id = :user_id AND topic = :topic
                GROUP BY session_id
                ORDER BY started_at DESC
                LIMIT 10
            """), {'user_id': user_id, 'topic': topic}).fetchall()
            
            # Get level adjustment history
            adjustments = db.session.execute(text("""
                SELECT from_level, to_level, adjustment_reason, created_at
                FROM passport_level_adjustments
                WHERE user_id = :user_id AND topic = :topic
                ORDER BY created_at DESC
                LIMIT 5
            """), {'user_id': user_id, 'topic': topic}).fetchall()
        else:
            sessions = db.session.execute(text("""
                SELECT session_id, level,
                       COUNT(*) as questions,
                       SUM(CASE WHEN is_correct THEN 1 ELSE 0 END) as correct,
                       AVG(time_taken_seconds) as avg_time,
                       MIN(created_at) as started_at
                FROM passport_performance
                WHERE guest_code = :guest_code AND topic = :topic
                GROUP BY session_id
                ORDER BY started_at DESC
                LIMIT 10
            """), {'guest_code': guest_code, 'topic': topic}).fetchall()
            
            adjustments = db.session.execute(text("""
                SELECT from_level, to_level, adjustment_reason, created_at
                FROM passport_level_adjustments
                WHERE guest_code = :guest_code AND topic = :topic
                ORDER BY created_at DESC
                LIMIT 5
            """), {'guest_code': guest_code, 'topic': topic}).fetchall()
        
        return jsonify({
            'topic': topic,
            'sessions': [{
                'session_id': s[0],
                'level': s[1],
                'questions': s[2],
                'correct': s[3],
                'accuracy': round((s[3] / s[2]) * 100, 1) if s[2] > 0 else 0,
                'avg_time': round(s[4] or 0, 1),
                'started_at': str(s[5]) if s[5] else None
            } for s in sessions],
            'adjustments': [{
                'from_level': a[0],
                'to_level': a[1],
                'reason': a[2],
                'created_at': str(a[3]) if a[3] else None
            } for a in adjustments]
        })
        
    except Exception as e:
        print(f"Error getting performance summary: {e}")
        return jsonify({'error': str(e)}), 500


# =====================================================
# PASSPORT V2 - WEEKLY PLANNER APIS
# =====================================================

@passport_bp.route('/api/passport/v2/strands', methods=['GET'])
@guest_or_login_required
def get_passport_strands():
    """Get all topic strands available for the specified curriculum"""
    curriculum = request.args.get('curriculum', 'JC')
    
    if curriculum not in CURRICULUM_HIERARCHY:
        curriculum = 'JC'
    
    included_strand_ids = CURRICULUM_HIERARCHY[curriculum]['includes']
    strands = []
    
    for strand_id in included_strand_ids:
        if strand_id in PASSPORT_TOPIC_STRANDS:
            strand = PASSPORT_TOPIC_STRANDS[strand_id].copy()
            strands.append(strand)
    
    return jsonify({
        'success': True,
        'curriculum': curriculum,
        'curriculum_name': CURRICULUM_HIERARCHY[curriculum]['display_name'],
        'strands': strands,
        'total_topics': sum(len(s['topics']) for s in strands)
    })


@passport_bp.route('/api/passport/v2/progress', methods=['GET'])
@guest_or_login_required
def get_passport_v2_progress():
    """Get student's existing progress across all topics"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        if user_id:
            progress_rows = db.session.execute(text("""
                SELECT topic, current_level, current_points, updated_at
                FROM adaptive_progress WHERE user_id = :uid
            """), {'uid': user_id}).fetchall()
        else:
            progress_rows = db.session.execute(text("""
                SELECT topic, current_level, current_points, updated_at
                FROM adaptive_progress WHERE guest_code = :code
            """), {'code': guest_code}).fetchall()
        
        topic_progress = {}
        total_levels = 0
        
        for row in progress_rows:
            topic_progress[row[0]] = {
                'level': row[1],
                'points': row[2] or 0,
                'updated_at': str(row[3]) if row[3] else None
            }
            total_levels += row[1]
        
        try:
            if user_id:
                stats = db.session.execute(text("""
                    SELECT COUNT(*) as total, SUM(CASE WHEN score > 0 THEN 1 ELSE 0 END) as correct
                    FROM user_question_history WHERE user_id = :uid
                """), {'uid': user_id}).fetchone()
            else:
                stats = db.session.execute(text("""
                    SELECT COUNT(*) as total, SUM(CASE WHEN score > 0 THEN 1 ELSE 0 END) as correct
                    FROM user_question_history WHERE guest_code = :code
                """), {'code': guest_code}).fetchone()
            
            total_questions = stats[0] if stats else 0
            total_correct = stats[1] if stats else 0
            accuracy = round((total_correct / total_questions * 100)) if total_questions > 0 else 0
        except:
            total_questions = 0
            accuracy = 0
        
        strengths = [t for t, p in topic_progress.items() if p['level'] >= 7]
        weaknesses = [t for t, p in topic_progress.items() if p['level'] <= 3]
        
        return jsonify({
            'success': True,
            'has_progress': len(topic_progress) > 0,
            'topic_progress': topic_progress,
            'summary': {
                'topics_practiced': len(topic_progress),
                'total_questions': total_questions,
                'accuracy': accuracy,
                'average_level': round(total_levels / len(topic_progress), 1) if topic_progress else 0
            },
            'strengths': strengths[:5],
            'weaknesses': weaknesses[:5]
        })
        
    except Exception as e:
        print(f"Error fetching progress: {e}")
        return jsonify({
            'success': True,
            'has_progress': False,
            'topic_progress': {},
            'summary': {'topics_practiced': 0, 'total_questions': 0, 'accuracy': 0, 'average_level': 0},
            'strengths': [],
            'weaknesses': []
        })


@passport_bp.route('/api/passport/v2/setup', methods=['POST'])
@guest_or_login_required
def save_passport_v2_setup():
    """Save passport setup configuration - SQLite compatible"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400
            
        curriculum = data.get('curriculum', 'JC')
        exam_date = data.get('exam_date')
        study_hours = data.get('study_hours_per_week', 3.5)
        
        if curriculum not in CURRICULUM_HIERARCHY:
            curriculum = 'JC'
        
        # Use check-then-insert/update pattern for SQLite compatibility
        if user_id:
            existing = db.session.execute(text(
                "SELECT id FROM passport_setup WHERE user_id = :uid"
            ), {'uid': user_id}).fetchone()
            
            if existing:
                db.session.execute(text("""
                    UPDATE passport_setup 
                    SET curriculum = :curr, exam_date = :exam, study_hours_per_week = :hours, updated_at = CURRENT_TIMESTAMP
                    WHERE user_id = :uid
                """), {'uid': user_id, 'curr': curriculum, 'exam': exam_date, 'hours': study_hours})
            else:
                db.session.execute(text("""
                    INSERT INTO passport_setup (user_id, curriculum, exam_date, study_hours_per_week, setup_completed_at, updated_at)
                    VALUES (:uid, :curr, :exam, :hours, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                """), {'uid': user_id, 'curr': curriculum, 'exam': exam_date, 'hours': study_hours})
        else:
            existing = db.session.execute(text(
                "SELECT id FROM passport_setup WHERE guest_code = :code"
            ), {'code': guest_code}).fetchone()
            
            if existing:
                db.session.execute(text("""
                    UPDATE passport_setup 
                    SET curriculum = :curr, exam_date = :exam, study_hours_per_week = :hours, updated_at = CURRENT_TIMESTAMP
                    WHERE guest_code = :code
                """), {'code': guest_code, 'curr': curriculum, 'exam': exam_date, 'hours': study_hours})
            else:
                db.session.execute(text("""
                    INSERT INTO passport_setup (guest_code, curriculum, exam_date, study_hours_per_week, setup_completed_at, updated_at)
                    VALUES (:code, :curr, :exam, :hours, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                """), {'code': guest_code, 'curr': curriculum, 'exam': exam_date, 'hours': study_hours})
        
        db.session.commit()
        
        weeks_to_exam = None
        if exam_date:
            exam = datetime.strptime(exam_date, '%Y-%m-%d').date() if isinstance(exam_date, str) else exam_date
            today = date.today()
            weeks_to_exam = max(1, (exam - today).days // 7)
        
        return jsonify({
            'success': True,
            'curriculum': curriculum,
            'curriculum_name': CURRICULUM_HIERARCHY[curriculum]['display_name'],
            'exam_date': exam_date,
            'weeks_to_exam': weeks_to_exam,
            'study_hours_per_week': study_hours
        })
        
    except Exception as e:
        db.session.rollback()
        import traceback
        print(f"Error saving setup: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/v2/self-assessment', methods=['POST'])
@guest_or_login_required
def save_passport_v2_self_assessment():
    """Save self-assessment ratings - SQLite compatible"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400
            
        assessments = data.get('assessments', {})
        
        if not assessments:
            return jsonify({'error': 'No assessments provided'}), 400
        
        saved_count = 0
        
        for topic_id, rating_data in assessments.items():
            confidence = rating_data.get('confidence', 2)
            strand = rating_data.get('strand', '')
            confidence = max(1, min(3, int(confidence)))
            
            if user_id:
                existing = db.session.execute(text(
                    "SELECT id FROM passport_topic_assessment WHERE user_id = :uid AND topic = :topic"
                ), {'uid': user_id, 'topic': topic_id}).fetchone()
                
                if existing:
                    db.session.execute(text("""
                        UPDATE passport_topic_assessment 
                        SET confidence = :conf, strand = :strand, assessed_at = CURRENT_TIMESTAMP
                        WHERE user_id = :uid AND topic = :topic
                    """), {'uid': user_id, 'topic': topic_id, 'strand': strand, 'conf': confidence})
                else:
                    db.session.execute(text("""
                        INSERT INTO passport_topic_assessment (user_id, topic, strand, confidence, assessed_at)
                        VALUES (:uid, :topic, :strand, :conf, CURRENT_TIMESTAMP)
                    """), {'uid': user_id, 'topic': topic_id, 'strand': strand, 'conf': confidence})
            else:
                existing = db.session.execute(text(
                    "SELECT id FROM passport_topic_assessment WHERE guest_code = :code AND topic = :topic"
                ), {'code': guest_code, 'topic': topic_id}).fetchone()
                
                if existing:
                    db.session.execute(text("""
                        UPDATE passport_topic_assessment 
                        SET confidence = :conf, strand = :strand, assessed_at = CURRENT_TIMESTAMP
                        WHERE guest_code = :code AND topic = :topic
                    """), {'code': guest_code, 'topic': topic_id, 'strand': strand, 'conf': confidence})
                else:
                    db.session.execute(text("""
                        INSERT INTO passport_topic_assessment (guest_code, topic, strand, confidence, assessed_at)
                        VALUES (:code, :topic, :strand, :conf, CURRENT_TIMESTAMP)
                    """), {'code': guest_code, 'topic': topic_id, 'strand': strand, 'conf': confidence})
            
            saved_count += 1
        
        db.session.commit()
        return jsonify({'success': True, 'topics_assessed': saved_count})
        
    except Exception as e:
        db.session.rollback()
        import traceback
        print(f"Error saving self-assessment: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/v2/diagnostic/questions', methods=['GET'])
@guest_or_login_required
def get_diagnostic_questions():
    """Generate 25 diagnostic questions based on curriculum"""
    from sqlalchemy import text
    import random
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    curriculum = request.args.get('curriculum', 'JC')
    
    assessments = {}
    try:
        if user_id:
            rows = db.session.execute(text("""
                SELECT topic, confidence FROM passport_topic_assessment WHERE user_id = :uid
            """), {'uid': user_id}).fetchall()
        else:
            rows = db.session.execute(text("""
                SELECT topic, confidence FROM passport_topic_assessment WHERE guest_code = :code
            """), {'code': guest_code}).fetchall()
        for row in rows:
            assessments[row[0]] = row[1]
    except:
        pass
    
    if curriculum in PASSPORT_QUIZ_CONFIG['strand_distribution']:
        distribution = PASSPORT_QUIZ_CONFIG['strand_distribution'][curriculum]
    else:
        distribution = PASSPORT_QUIZ_CONFIG['strand_distribution']['JC']
    
    questions = []
    question_id = 1
    
    question_bank = {
        'numeracy_foundation': [
            {'q': 'What is 7 + 8?', 'options': ['13', '14', '15', '16'], 'correct': 2, 'difficulty': 'easy'},
            {'q': 'What is 15 - 9?', 'options': ['5', '6', '7', '8'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'What is 6 × 7?', 'options': ['36', '42', '48', '54'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'What is 56 ÷ 8?', 'options': ['6', '7', '8', '9'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'What is 123 + 456?', 'options': ['569', '579', '589', '679'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'What is 8 × 9?', 'options': ['63', '72', '81', '64'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'What is 144 ÷ 12?', 'options': ['10', '11', '12', '14'], 'correct': 2, 'difficulty': 'medium'},
            {'q': 'What is 25 × 4?', 'options': ['90', '100', '110', '120'], 'correct': 1, 'difficulty': 'easy'},
        ],
        'numeracy_activities': [
            {'q': 'What is 12 + 15?', 'options': ['25', '26', '27', '28'], 'correct': 2, 'difficulty': 'easy'},
            {'q': 'What is 9 × 8?', 'options': ['63', '72', '81', '64'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'What is 100 - 37?', 'options': ['63', '67', '73', '77'], 'correct': 0, 'difficulty': 'easy'},
            {'q': 'What is 7 × 6?', 'options': ['36', '42', '48', '54'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'What is 84 ÷ 7?', 'options': ['11', '12', '13', '14'], 'correct': 1, 'difficulty': 'medium'},
            {'q': 'What is 45 + 38?', 'options': ['73', '83', '93', '103'], 'correct': 1, 'difficulty': 'easy'},
        ],
        'number': [
            {'q': 'What is 1/2 + 1/4?', 'options': ['1/2', '2/4', '3/4', '1'], 'correct': 2, 'difficulty': 'medium'},
            {'q': 'Convert 0.75 to a fraction', 'options': ['1/2', '2/3', '3/4', '4/5'], 'correct': 2, 'difficulty': 'medium'},
            {'q': 'What is 25% of 80?', 'options': ['15', '20', '25', '30'], 'correct': 1, 'difficulty': 'medium'},
            {'q': 'Simplify the ratio 12:18', 'options': ['2:3', '3:4', '4:6', '6:9'], 'correct': 0, 'difficulty': 'medium'},
            {'q': 'What is 2/3 of 60?', 'options': ['30', '40', '45', '50'], 'correct': 1, 'difficulty': 'medium'},
            {'q': 'Convert 3/5 to a percentage', 'options': ['50%', '55%', '60%', '65%'], 'correct': 2, 'difficulty': 'medium'},
            {'q': 'What is 0.125 as a fraction?', 'options': ['1/4', '1/6', '1/8', '1/10'], 'correct': 2, 'difficulty': 'hard'},
            {'q': 'If 3:5 = x:20, what is x?', 'options': ['10', '12', '15', '18'], 'correct': 1, 'difficulty': 'hard'},
        ],
        'algebra': [
            {'q': 'Solve: x + 5 = 12', 'options': ['5', '6', '7', '8'], 'correct': 2, 'difficulty': 'easy'},
            {'q': 'Solve: 2x = 14', 'options': ['5', '6', '7', '8'], 'correct': 2, 'difficulty': 'easy'},
            {'q': 'Solve: 3x - 4 = 11', 'options': ['3', '4', '5', '6'], 'correct': 2, 'difficulty': 'medium'},
            {'q': 'Simplify: 3a + 2a', 'options': ['5a', '6a', '5a²', '6a²'], 'correct': 0, 'difficulty': 'easy'},
            {'q': 'Expand: 2(x + 3)', 'options': ['2x + 3', '2x + 5', '2x + 6', 'x + 6'], 'correct': 2, 'difficulty': 'medium'},
            {'q': 'Solve: x/4 = 3', 'options': ['7', '10', '12', '15'], 'correct': 2, 'difficulty': 'medium'},
            {'q': 'Factorise: 6x + 12', 'options': ['6(x + 2)', '3(2x + 4)', '2(3x + 6)', 'All of these'], 'correct': 3, 'difficulty': 'hard'},
            {'q': 'Solve: 2(x - 1) = 10', 'options': ['4', '5', '6', '7'], 'correct': 2, 'difficulty': 'hard'},
        ],
        'geometry': [
            {'q': 'Angles in a triangle sum to?', 'options': ['90°', '180°', '270°', '360°'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'Area of rectangle 5cm × 8cm?', 'options': ['13 cm²', '26 cm²', '40 cm²', '80 cm²'], 'correct': 2, 'difficulty': 'easy'},
            {'q': 'Perimeter of square with side 6cm?', 'options': ['12 cm', '18 cm', '24 cm', '36 cm'], 'correct': 2, 'difficulty': 'easy'},
            {'q': 'Angles on a straight line sum to?', 'options': ['90°', '180°', '270°', '360°'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'Area of triangle: base 10, height 6?', 'options': ['16', '30', '60', '120'], 'correct': 1, 'difficulty': 'medium'},
            {'q': 'What type has all sides equal?', 'options': ['Scalene', 'Isosceles', 'Equilateral', 'Right-angled'], 'correct': 2, 'difficulty': 'easy'},
            {'q': 'Angles in a quadrilateral sum to?', 'options': ['180°', '270°', '360°', '540°'], 'correct': 2, 'difficulty': 'medium'},
            {'q': 'Circumference formula uses?', 'options': ['2πr', 'πr²', '4πr', '2r'], 'correct': 0, 'difficulty': 'medium'},
        ],
        'statistics': [
            {'q': 'Mean of 2, 4, 6, 8, 10?', 'options': ['5', '6', '7', '8'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'Median of 3, 7, 9, 12, 15?', 'options': ['7', '9', '10', '12'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'Mode of 2, 3, 3, 5, 7, 3?', 'options': ['2', '3', '5', '7'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'Probability of heads on fair coin?', 'options': ['0.25', '0.5', '0.75', '1'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'Range of 4, 8, 15, 16, 23, 42?', 'options': ['36', '38', '40', '42'], 'correct': 1, 'difficulty': 'medium'},
            {'q': 'P(rolling 6 on fair die)?', 'options': ['1/2', '1/3', '1/4', '1/6'], 'correct': 3, 'difficulty': 'easy'},
        ],
        'complex_numbers': [
            {'q': 'What is √(-1)?', 'options': ['-1', '1', 'i', 'undefined'], 'correct': 2, 'difficulty': 'medium'},
            {'q': 'Simplify i²', 'options': ['1', '-1', 'i', '-i'], 'correct': 1, 'difficulty': 'medium'},
            {'q': 'What is (2 + 3i) + (1 - i)?', 'options': ['3 + 2i', '3 + 4i', '1 + 2i', '3 - 2i'], 'correct': 0, 'difficulty': 'medium'},
            {'q': 'Simplify √18', 'options': ['3√2', '2√3', '6√3', '9√2'], 'correct': 0, 'difficulty': 'medium'},
            {'q': 'Rationalise 1/√2', 'options': ['√2', '√2/2', '2/√2', '1/2'], 'correct': 1, 'difficulty': 'hard'},
        ],
        'l1lp': [
            {'q': 'What comes after 19?', 'options': ['18', '20', '21', '29'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'Which is bigger: 23 or 32?', 'options': ['23', '32', 'Same', 'Cannot tell'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'How many 10s in 50?', 'options': ['4', '5', '6', '10'], 'correct': 1, 'difficulty': 'easy'},
            {'q': '€2 + €3 = ?', 'options': ['€4', '€5', '€6', '€7'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'Count: 🍎🍎🍎🍎🍎', 'options': ['3', '4', '5', '6'], 'correct': 2, 'difficulty': 'easy'},
            {'q': 'What number is before 10?', 'options': ['8', '9', '11', '12'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'Which is smaller: 15 or 51?', 'options': ['15', '51', 'Same', 'Cannot tell'], 'correct': 0, 'difficulty': 'easy'},
            {'q': '5 + 3 = ?', 'options': ['6', '7', '8', '9'], 'correct': 2, 'difficulty': 'easy'},
        ],
        'l2lp': [
            {'q': 'Round 47 to nearest 10', 'options': ['40', '45', '50', '47'], 'correct': 2, 'difficulty': 'easy'},
            {'q': 'Half of 24 is?', 'options': ['10', '11', '12', '14'], 'correct': 2, 'difficulty': 'easy'},
            {'q': '1/4 of this shape means?', 'options': ['1 part of 2', '1 part of 3', '1 part of 4', '4 parts'], 'correct': 2, 'difficulty': 'easy'},
            {'q': '10% of 100 is?', 'options': ['1', '10', '20', '100'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'Quarter past 3 is?', 'options': ['3:00', '3:15', '3:30', '3:45'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'Round 83 to nearest 10', 'options': ['80', '85', '90', '83'], 'correct': 0, 'difficulty': 'easy'},
            {'q': 'Half of 50 is?', 'options': ['20', '25', '30', '35'], 'correct': 1, 'difficulty': 'easy'},
            {'q': '25% is the same as?', 'options': ['1/2', '1/3', '1/4', '1/5'], 'correct': 2, 'difficulty': 'medium'},
        ],
        'lc_hl': [
            {'q': 'Differentiate: x³', 'options': ['x²', '2x²', '3x²', '3x³'], 'correct': 2, 'difficulty': 'medium'},
            {'q': 'Integrate: 2x', 'options': ['x²', 'x² + c', '2x²', '2x² + c'], 'correct': 1, 'difficulty': 'medium'},
            {'q': 'What is log₁₀(100)?', 'options': ['1', '2', '10', '100'], 'correct': 1, 'difficulty': 'medium'},
            {'q': 'Sum of arithmetic series formula?', 'options': ['n/2(a+l)', 'n(a+l)', 'n/2(2a+d)', 'a+nd'], 'correct': 0, 'difficulty': 'hard'},
            {'q': 'If f(x)=x², then f\'(x)=?', 'options': ['x', '2x', 'x²', '2'], 'correct': 1, 'difficulty': 'medium'},
            {'q': 'sin²θ + cos²θ = ?', 'options': ['0', '1', '2', 'sinθcosθ'], 'correct': 1, 'difficulty': 'easy'},
            {'q': '⁵C₂ = ?', 'options': ['5', '10', '20', '25'], 'correct': 1, 'difficulty': 'medium'},
            {'q': 'Derivative of eˣ is?', 'options': ['x·eˣ', 'eˣ', 'e', 'xeˣ⁻¹'], 'correct': 1, 'difficulty': 'medium'},
            {'q': '∫x dx = ?', 'options': ['x', 'x²/2', 'x²/2 + c', '2x'], 'correct': 2, 'difficulty': 'medium'},
            {'q': 'Period of sin(x)?', 'options': ['π', '2π', 'π/2', '4π'], 'correct': 1, 'difficulty': 'medium'},
        ],
        'lc_ol': [
            {'q': 'Compound interest uses?', 'options': ['P(1+r)ⁿ', 'P×r×n', 'P+rn', 'Prn'], 'correct': 0, 'difficulty': 'medium'},
            {'q': 'Area of circle radius 5?', 'options': ['10π', '25π', '50π', '5π'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'tan(45°) = ?', 'options': ['0', '0.5', '1', '√2'], 'correct': 2, 'difficulty': 'medium'},
            {'q': 'Mean of 10, 20, 30?', 'options': ['15', '20', '25', '30'], 'correct': 1, 'difficulty': 'easy'},
            {'q': 'P(A or B) if mutually exclusive?', 'options': ['P(A)×P(B)', 'P(A)+P(B)', 'P(A)-P(B)', 'P(A)/P(B)'], 'correct': 1, 'difficulty': 'medium'},
            {'q': 'Volume of cylinder?', 'options': ['πr²h', '2πrh', 'πrh', '4/3πr³'], 'correct': 0, 'difficulty': 'medium'},
            {'q': 'Depreciation reduces value by?', 'options': ['Adding %', 'Multiplying', 'Subtracting %', 'Dividing'], 'correct': 2, 'difficulty': 'easy'},
        ],
    }
    
    for strand_id, count in distribution.items():
        if strand_id in question_bank:
            strand_questions = question_bank[strand_id].copy()
            random.shuffle(strand_questions)
            selected = strand_questions[:count]
            
            for q in selected:
                questions.append({
                    'id': f'q{question_id}',
                    'strand': strand_id,
                    'strand_name': PASSPORT_TOPIC_STRANDS.get(strand_id, {}).get('display_name', strand_id),
                    'strand_icon': PASSPORT_TOPIC_STRANDS.get(strand_id, {}).get('icon', '📝'),
                    'question': q['q'],
                    'options': q['options'],
                    'correct': q['correct'],
                    'difficulty': q['difficulty']
                })
                question_id += 1
    
    random.shuffle(questions)
    questions = questions[:25]
    
    for i, q in enumerate(questions):
        q['id'] = f'q{i+1}'
        q['number'] = i + 1
    
    return jsonify({
        'success': True,
        'total_questions': len(questions),
        'questions': questions,
        'time_estimate_minutes': 8
    })


@passport_bp.route('/api/passport/v2/diagnostic/submit', methods=['POST'])
@guest_or_login_required
def submit_diagnostic_quiz():
    """Submit diagnostic quiz answers and calculate per-topic scores"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    data = request.get_json()
    answers = data.get('answers', {})
    questions = data.get('questions', [])
    
    if not answers or not questions:
        return jsonify({'error': 'Missing answers or questions'}), 400
    
    try:
        strand_scores = {}
        total_correct = 0
        total_questions = len(questions)
        
        for q in questions:
            q_id = q['id']
            strand = q.get('strand', 'unknown')
            correct_idx = q.get('correct', 0)
            user_answer = answers.get(q_id)
            
            if strand not in strand_scores:
                strand_scores[strand] = {'correct': 0, 'total': 0}
            
            strand_scores[strand]['total'] += 1
            
            if user_answer is not None and int(user_answer) == correct_idx:
                strand_scores[strand]['correct'] += 1
                total_correct += 1
        
        strand_results = {}
        for strand, scores in strand_scores.items():
            percentage = round((scores['correct'] / scores['total']) * 100) if scores['total'] > 0 else 0
            
            if percentage >= 80:
                recommended_level = 7
            elif percentage >= 60:
                recommended_level = 5
            elif percentage >= 40:
                recommended_level = 3
            else:
                recommended_level = 1
            
            strand_results[strand] = {
                'correct': scores['correct'],
                'total': scores['total'],
                'percentage': percentage,
                'recommended_level': recommended_level
            }
            
            if strand in PASSPORT_TOPIC_STRANDS:
                for topic in PASSPORT_TOPIC_STRANDS[strand]['topics']:
                    topic_id = topic['id']
                    
                    # SQLite compatible: check then insert/update
                    if user_id:
                        existing = db.session.execute(text(
                            "SELECT id FROM passport_diagnostic WHERE user_id = :uid AND topic = :topic"
                        ), {'uid': user_id, 'topic': topic_id}).fetchone()
                        
                        if existing:
                            db.session.execute(text("""
                                UPDATE passport_diagnostic 
                                SET questions_asked = :asked, questions_correct = :correct, recommended_entry_level = :level, diagnosed_at = CURRENT_TIMESTAMP
                                WHERE user_id = :uid AND topic = :topic
                            """), {'uid': user_id, 'topic': topic_id, 'asked': scores['total'], 'correct': scores['correct'], 'level': recommended_level})
                        else:
                            db.session.execute(text("""
                                INSERT INTO passport_diagnostic (user_id, topic, strand, questions_asked, questions_correct, recommended_entry_level, diagnosed_at)
                                VALUES (:uid, :topic, :strand, :asked, :correct, :level, CURRENT_TIMESTAMP)
                            """), {'uid': user_id, 'topic': topic_id, 'strand': strand, 'asked': scores['total'], 'correct': scores['correct'], 'level': recommended_level})
                    else:
                        existing = db.session.execute(text(
                            "SELECT id FROM passport_diagnostic WHERE guest_code = :code AND topic = :topic"
                        ), {'code': guest_code, 'topic': topic_id}).fetchone()
                        
                        if existing:
                            db.session.execute(text("""
                                UPDATE passport_diagnostic 
                                SET questions_asked = :asked, questions_correct = :correct, recommended_entry_level = :level, diagnosed_at = CURRENT_TIMESTAMP
                                WHERE guest_code = :code AND topic = :topic
                            """), {'code': guest_code, 'topic': topic_id, 'asked': scores['total'], 'correct': scores['correct'], 'level': recommended_level})
                        else:
                            db.session.execute(text("""
                                INSERT INTO passport_diagnostic (guest_code, topic, strand, questions_asked, questions_correct, recommended_entry_level, diagnosed_at)
                                VALUES (:code, :topic, :strand, :asked, :correct, :level, CURRENT_TIMESTAMP)
                            """), {'code': guest_code, 'topic': topic_id, 'strand': strand, 'asked': scores['total'], 'correct': scores['correct'], 'level': recommended_level})
        
        db.session.commit()
        
        overall_percentage = round((total_correct / total_questions) * 100) if total_questions > 0 else 0
        if overall_percentage >= 80:
            grade = 'A'
        elif overall_percentage >= 60:
            grade = 'B'
        elif overall_percentage >= 40:
            grade = 'C'
        else:
            grade = 'D'
        
        return jsonify({
            'success': True,
            'score': total_correct,
            'total': total_questions,
            'percentage': overall_percentage,
            'grade': grade,
            'strand_results': strand_results
        })
        
    except Exception as e:
        db.session.rollback()
        print(f"Error submitting diagnostic: {e}")
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/v2/calculate-entry-levels', methods=['POST'])
@guest_or_login_required
def calculate_entry_levels():
    """Calculate final entry levels combining progress, self-assessment, and quiz results"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    data = request.get_json()
    curriculum = data.get('curriculum', 'JC')
    
    try:
        topics = get_all_topics_for_curriculum(curriculum)
        
        progress_levels = {}
        if user_id:
            rows = db.session.execute(text("SELECT topic, current_level FROM adaptive_progress WHERE user_id = :uid"), {'uid': user_id}).fetchall()
        else:
            rows = db.session.execute(text("SELECT topic, current_level FROM adaptive_progress WHERE guest_code = :code"), {'code': guest_code}).fetchall()
        for row in rows:
            progress_levels[row[0]] = row[1]
        
        assessments = {}
        if user_id:
            rows = db.session.execute(text("SELECT topic, confidence FROM passport_topic_assessment WHERE user_id = :uid"), {'uid': user_id}).fetchall()
        else:
            rows = db.session.execute(text("SELECT topic, confidence FROM passport_topic_assessment WHERE guest_code = :code"), {'code': guest_code}).fetchall()
        for row in rows:
            assessments[row[0]] = row[1]
        
        diagnostics = {}
        if user_id:
            rows = db.session.execute(text("SELECT topic, questions_asked, questions_correct, recommended_entry_level FROM passport_diagnostic WHERE user_id = :uid"), {'uid': user_id}).fetchall()
        else:
            rows = db.session.execute(text("SELECT topic, questions_asked, questions_correct, recommended_entry_level FROM passport_diagnostic WHERE guest_code = :code"), {'code': guest_code}).fetchall()
        for row in rows:
            if row[1] > 0:
                diagnostics[row[0]] = {'asked': row[1], 'correct': row[2], 'percentage': round((row[2] / row[1]) * 100), 'recommended': row[3]}
        
        entry_levels = {}
        
        for topic in topics:
            topic_id = topic['topic_id']
            strand_id = topic['strand_id']
            
            progress = progress_levels.get(topic_id, 0)
            confidence = assessments.get(topic_id, 2)
            
            quiz_score = None
            if topic_id in diagnostics:
                quiz_score = diagnostics[topic_id]['percentage']
            elif strand_id in diagnostics:
                quiz_score = diagnostics[strand_id]['percentage']
            
            entry = calculate_entry_level_v2(progress, confidence, quiz_score)
            priority = calculate_topic_priority_v2(entry, confidence)
            
            entry_levels[topic_id] = {
                'topic_id': topic_id,
                'topic_name': topic['topic_name'],
                'strand': strand_id,
                'progress_level': progress,
                'confidence': confidence,
                'quiz_score': quiz_score,
                'entry_level': entry,
                'priority_score': priority
            }
            
            # SQLite compatible: check then insert/update
            if user_id:
                existing = db.session.execute(text(
                    "SELECT id FROM passport_entry_levels WHERE user_id = :uid AND topic = :topic"
                ), {'uid': user_id, 'topic': topic_id}).fetchone()
                
                if existing:
                    db.session.execute(text("""
                        UPDATE passport_entry_levels 
                        SET progress_level = :progress, confidence_modifier = :conf, quiz_modifier = :quiz, final_entry_level = :entry, calculated_at = CURRENT_TIMESTAMP
                        WHERE user_id = :uid AND topic = :topic
                    """), {'uid': user_id, 'topic': topic_id, 'progress': progress, 'conf': confidence, 'quiz': quiz_score if quiz_score else 0, 'entry': entry})
                else:
                    db.session.execute(text("""
                        INSERT INTO passport_entry_levels (user_id, topic, progress_level, confidence_modifier, quiz_modifier, final_entry_level, calculated_at)
                        VALUES (:uid, :topic, :progress, :conf, :quiz, :entry, CURRENT_TIMESTAMP)
                    """), {'uid': user_id, 'topic': topic_id, 'progress': progress, 'conf': confidence, 'quiz': quiz_score if quiz_score else 0, 'entry': entry})
            else:
                existing = db.session.execute(text(
                    "SELECT id FROM passport_entry_levels WHERE guest_code = :code AND topic = :topic"
                ), {'code': guest_code, 'topic': topic_id}).fetchone()
                
                if existing:
                    db.session.execute(text("""
                        UPDATE passport_entry_levels 
                        SET progress_level = :progress, confidence_modifier = :conf, quiz_modifier = :quiz, final_entry_level = :entry, calculated_at = CURRENT_TIMESTAMP
                        WHERE guest_code = :code AND topic = :topic
                    """), {'code': guest_code, 'topic': topic_id, 'progress': progress, 'conf': confidence, 'quiz': quiz_score if quiz_score else 0, 'entry': entry})
                else:
                    db.session.execute(text("""
                        INSERT INTO passport_entry_levels (guest_code, topic, progress_level, confidence_modifier, quiz_modifier, final_entry_level, calculated_at)
                        VALUES (:code, :topic, :progress, :conf, :quiz, :entry, CURRENT_TIMESTAMP)
                    """), {'code': guest_code, 'topic': topic_id, 'progress': progress, 'conf': confidence, 'quiz': quiz_score if quiz_score else 0, 'entry': entry})
        
        db.session.commit()
        
        sorted_topics = sorted(entry_levels.values(), key=lambda x: x['priority_score'], reverse=True)
        
        return jsonify({
            'success': True,
            'curriculum': curriculum,
            'total_topics': len(entry_levels),
            'entry_levels': entry_levels,
            'priority_order': [t['topic_id'] for t in sorted_topics],
            'high_priority': [t for t in sorted_topics if t['priority_score'] > 15][:10],
            'summary': {
                'average_entry_level': round(sum(t['entry_level'] for t in entry_levels.values()) / len(entry_levels), 1) if entry_levels else 0,
                'topics_with_progress': len([t for t in entry_levels.values() if t['progress_level'] > 0]),
                'topics_needing_help': len([t for t in entry_levels.values() if t['confidence'] == 1])
            }
        })
        
    except Exception as e:
        db.session.rollback()
        print(f"Error calculating entry levels: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/v2/calendar', methods=['GET'])
@guest_or_login_required
def get_irish_calendar():
    """Get Irish school calendar events for planning"""
    from sqlalchemy import text
    
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    try:
        if start_date and end_date:
            rows = db.session.execute(text("""
                SELECT id, year, event_name, event_type, start_date, end_date, workload_modifier, notes
                FROM irish_school_calendar WHERE start_date >= :start AND end_date <= :end ORDER BY start_date
            """), {'start': start_date, 'end': end_date}).fetchall()
        else:
            rows = db.session.execute(text("""
                SELECT id, year, event_name, event_type, start_date, end_date, workload_modifier, notes
                FROM irish_school_calendar ORDER BY start_date
            """)).fetchall()
        
        events = []
        for row in rows:
            events.append({
                'id': row[0], 'year': row[1], 'event_name': row[2], 'event_type': row[3],
                'start_date': row[4], 'end_date': row[5], 'workload_modifier': row[6], 'notes': row[7]
            })
        
        return jsonify({'success': True, 'events': events, 'total': len(events)})
        
    except Exception as e:
        print(f"Error fetching calendar: {e}")
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/v2/generate-plan', methods=['POST'])
@guest_or_login_required
def generate_weekly_plan():
    """Generate the full weekly study plan based on entry levels and calendar"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    data = request.get_json()
    curriculum = data.get('curriculum', 'JC')
    exam_date_str = data.get('exam_date')
    
    try:
        if exam_date_str:
            exam_date = datetime.strptime(exam_date_str, '%Y-%m-%d').date()
        else:
            exam_date = date.today() + timedelta(weeks=52)
        
        today = date.today()
        days_to_exam = (exam_date - today).days
        weeks_to_exam = max(1, days_to_exam // 7)
        months_to_exam = days_to_exam / 30
        intensive_mode = months_to_exam < 9
        
        entry_levels = {}
        if user_id:
            rows = db.session.execute(text("SELECT topic, final_entry_level FROM passport_entry_levels WHERE user_id = :uid"), {'uid': user_id}).fetchall()
        else:
            rows = db.session.execute(text("SELECT topic, final_entry_level FROM passport_entry_levels WHERE guest_code = :code"), {'code': guest_code}).fetchall()
        for row in rows:
            entry_levels[row[0]] = row[1]
        
        confidence_ratings = {}
        if user_id:
            rows = db.session.execute(text("SELECT topic, confidence FROM passport_topic_assessment WHERE user_id = :uid"), {'uid': user_id}).fetchall()
        else:
            rows = db.session.execute(text("SELECT topic, confidence FROM passport_topic_assessment WHERE guest_code = :code"), {'code': guest_code}).fetchall()
        for row in rows:
            confidence_ratings[row[0]] = row[1]
        
        all_topics = get_all_topics_for_curriculum(curriculum)
        
        topic_priorities = []
        for topic in all_topics:
            topic_id = topic['topic_id']
            entry = entry_levels.get(topic_id, 1)
            confidence = confidence_ratings.get(topic_id, 2)
            gap_to_mastery = 12 - entry
            confidence_weight = (4 - confidence) * 3
            priority_score = gap_to_mastery + confidence_weight
            target = calculate_target_level_v2(entry, weeks_to_exam)
            
            topic_priorities.append({
                'topic_id': topic_id, 'topic_name': topic['topic_name'], 'strand_id': topic['strand_id'],
                'strand_icon': topic['strand_icon'], 'entry_level': entry, 'target_level': target,
                'confidence': confidence, 'priority_score': priority_score
            })
        
        topic_priorities.sort(key=lambda x: x['priority_score'], reverse=True)
        
        calendar_events = []
        rows = db.session.execute(text("""
            SELECT event_name, event_type, start_date, end_date, workload_modifier
            FROM irish_school_calendar WHERE start_date >= :start AND start_date <= :end
        """), {'start': today.isoformat(), 'end': exam_date.isoformat()}).fetchall()
        for row in rows:
            calendar_events.append({'event_name': row[0], 'event_type': row[1], 'start_date': row[2], 'end_date': row[3], 'workload_modifier': row[4]})
        
        if user_id:
            db.session.execute(text("DELETE FROM passport_week_topics WHERE user_id = :uid"), {'uid': user_id})
            db.session.execute(text("DELETE FROM passport_weekly_plan WHERE user_id = :uid"), {'uid': user_id})
        else:
            db.session.execute(text("DELETE FROM passport_week_topics WHERE guest_code = :code"), {'code': guest_code})
            db.session.execute(text("DELETE FROM passport_weekly_plan WHERE guest_code = :code"), {'code': guest_code})
        
        weekly_plan = []
        topic_index = 0
        revision_weeks = 2
        
        for week_num in range(1, weeks_to_exam + 1):
            week_start = today + timedelta(weeks=week_num - 1)
            week_end = week_start + timedelta(days=6)
            capacity = get_week_capacity_from_calendar(week_start, exam_date, calendar_events, intensive_mode)
            
            if week_num == 1:
                status = 'current'
            elif week_num > weeks_to_exam - revision_weeks:
                status = 'revision'
            else:
                status = 'upcoming'
            
            if user_id:
                result = db.session.execute(text("""
                    INSERT INTO passport_weekly_plan (user_id, week_number, week_start_date, week_end_date, focus_area, capacity_hours, capacity_type, holiday_name, status)
                    VALUES (:uid, :week, :start, :end, :focus, :hours, :type, :holiday, :status) RETURNING id
                """), {'uid': user_id, 'week': week_num, 'start': week_start.isoformat(), 'end': week_end.isoformat(), 'focus': capacity.get('focus_area', ''), 'hours': capacity['hours'], 'type': capacity['capacity_type'], 'holiday': capacity.get('holiday_name'), 'status': status})
            else:
                result = db.session.execute(text("""
                    INSERT INTO passport_weekly_plan (guest_code, week_number, week_start_date, week_end_date, focus_area, capacity_hours, capacity_type, holiday_name, status)
                    VALUES (:code, :week, :start, :end, :focus, :hours, :type, :holiday, :status) RETURNING id
                """), {'code': guest_code, 'week': week_num, 'start': week_start.isoformat(), 'end': week_end.isoformat(), 'focus': capacity.get('focus_area', ''), 'hours': capacity['hours'], 'type': capacity['capacity_type'], 'holiday': capacity.get('holiday_name'), 'status': status})
            
            week_plan_id = result.fetchone()[0]
            
            week_topics = []
            max_topics = capacity['max_topics']
            
            if status == 'revision':
                week_topics.append({'topic_id': 'revision', 'topic_name': 'Revision & Practice', 'strand_id': 'revision', 'strand_icon': '📝', 'entry_level': 1, 'target_level': 12, 'priority': 'high'})
            else:
                for i in range(max_topics):
                    if topic_index < len(topic_priorities):
                        topic = topic_priorities[topic_index]
                        priority = 'high' if topic['priority_score'] > 15 else 'normal'
                        week_topics.append({'topic_id': topic['topic_id'], 'topic_name': topic['topic_name'], 'strand_id': topic['strand_id'], 'strand_icon': topic['strand_icon'], 'entry_level': topic['entry_level'], 'target_level': topic['target_level'], 'priority': priority})
                        topic_index += 1
            
            for topic in week_topics:
                if user_id:
                    db.session.execute(text("""
                        INSERT INTO passport_week_topics (week_plan_id, user_id, topic, strand, entry_level, target_level, priority, status)
                        VALUES (:wpid, :uid, :topic, :strand, :entry, :target, :priority, 'not_started')
                    """), {'wpid': week_plan_id, 'uid': user_id, 'topic': topic['topic_id'], 'strand': topic['strand_id'], 'entry': topic['entry_level'], 'target': topic['target_level'], 'priority': topic['priority']})
                else:
                    db.session.execute(text("""
                        INSERT INTO passport_week_topics (week_plan_id, guest_code, topic, strand, entry_level, target_level, priority, status)
                        VALUES (:wpid, :code, :topic, :strand, :entry, :target, :priority, 'not_started')
                    """), {'wpid': week_plan_id, 'code': guest_code, 'topic': topic['topic_id'], 'strand': topic['strand_id'], 'entry': topic['entry_level'], 'target': topic['target_level'], 'priority': topic['priority']})
            
            weekly_plan.append({'week_number': week_num, 'week_start': week_start.isoformat(), 'week_end': week_end.isoformat(), 'capacity_type': capacity['capacity_type'], 'capacity_hours': capacity['hours'], 'holiday_name': capacity.get('holiday_name'), 'status': status, 'topics': week_topics})
        
        if user_id:
            db.session.execute(text("UPDATE passport_setup SET last_plan_generated_at = CURRENT_TIMESTAMP WHERE user_id = :uid"), {'uid': user_id})
        else:
            db.session.execute(text("UPDATE passport_setup SET last_plan_generated_at = CURRENT_TIMESTAMP WHERE guest_code = :code"), {'code': guest_code})
        
        db.session.commit()
        
        return jsonify({
            'success': True, 'curriculum': curriculum, 'exam_date': exam_date.isoformat(),
            'weeks_to_exam': weeks_to_exam, 'intensive_mode': intensive_mode,
            'total_topics': len(topic_priorities), 'topics_assigned': topic_index, 'weekly_plan': weekly_plan,
            'summary': {
                'normal_weeks': len([w for w in weekly_plan if w['capacity_type'] == 'normal']),
                'intensive_weeks': len([w for w in weekly_plan if w['capacity_type'] == 'intensive']),
                'light_weeks': len([w for w in weekly_plan if w['capacity_type'] == 'light']),
                'revision_weeks': len([w for w in weekly_plan if w['status'] == 'revision'])
            }
        })
        
    except Exception as e:
        db.session.rollback()
        print(f"Error generating plan: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500



# ============================================================================
# PASSPORT TOPIC REDISTRIBUTION (Added 2025-12-27)
# Automatically moves incomplete topics from past weeks to future weeks
# ============================================================================

def redistribute_incomplete_topics(user_id=None, guest_code=None):
    """
    Automatically redistribute incomplete topics from past weeks to future weeks.
    Strategy:
    1. Find all weeks that have ended with incomplete topics
    2. Collect all incomplete (non-completed, non-pinned) topics  
    3. Distribute to future weeks: spread evenly, one topic per week first
    4. If more topics than weeks, stack remaining in later weeks
    
    Returns: dict with redistribution summary
    """
    from sqlalchemy import text
    from datetime import date, datetime
    
    if not user_id and not guest_code:
        return {'redistributed': 0, 'error': 'No user/guest'}
    
    today = date.today()
    redistributed_count = 0
    
    try:
        # Get all weeks for this user
        if user_id:
            weeks = db.session.execute(text("""
                SELECT id, week_number, week_end_date 
                FROM passport_weekly_plan 
                WHERE user_id = :uid 
                ORDER BY week_number
            """), {'uid': user_id}).fetchall()
        else:
            weeks = db.session.execute(text("""
                SELECT id, week_number, week_end_date 
                FROM passport_weekly_plan 
                WHERE guest_code = :code 
                ORDER BY week_number
            """), {'code': guest_code}).fetchall()
        
        if not weeks:
            return {'redistributed': 0, 'message': 'No weeks found'}
        
        # Separate past and future weeks
        past_week_ids = []
        future_weeks = []  # List of (week_plan_id, week_number)
        
        for week in weeks:
            week_id, week_num, week_end = week
            # Parse date if string
            if isinstance(week_end, str):
                week_end = datetime.strptime(week_end, '%Y-%m-%d').date()
            
            if week_end < today:
                past_week_ids.append(week_id)
            else:
                future_weeks.append((week_id, week_num))
        
        if not past_week_ids:
            return {'redistributed': 0, 'message': 'No past weeks'}
        
        if not future_weeks:
            return {'redistributed': 0, 'message': 'No future weeks available'}
        
        # Find incomplete, non-pinned topics from past weeks
        placeholders = ','.join([':w' + str(i) for i in range(len(past_week_ids))])
        params = {f'w{i}': wid for i, wid in enumerate(past_week_ids)}
        
        if user_id:
            params['uid'] = user_id
            incomplete_topics = db.session.execute(text(f"""
                SELECT id, topic, week_plan_id
                FROM passport_week_topics 
                WHERE user_id = :uid 
                AND week_plan_id IN ({placeholders})
                AND (status IS NULL OR status != 'completed')
                AND (pinned IS NULL OR pinned = 0)
                ORDER BY week_plan_id, priority
            """), params).fetchall()
        else:
            params['code'] = guest_code
            incomplete_topics = db.session.execute(text(f"""
                SELECT id, topic, week_plan_id
                FROM passport_week_topics 
                WHERE guest_code = :code 
                AND week_plan_id IN ({placeholders})
                AND (status IS NULL OR status != 'completed')
                AND (pinned IS NULL OR pinned = 0)
                ORDER BY week_plan_id, priority
            """), params).fetchall()
        
        if not incomplete_topics:
            return {'redistributed': 0, 'message': 'No incomplete topics to redistribute'}
        
        print(f"[Passport] Found {len(incomplete_topics)} incomplete topics from {len(past_week_ids)} past weeks")
        print(f"[Passport] Available future weeks: {len(future_weeks)}")
        
        # Track how many topics already in each future week (to balance load)
        week_topic_counts = {}
        for fw_id, fw_num in future_weeks:
            if user_id:
                count = db.session.execute(text("""
                    SELECT COUNT(*) FROM passport_week_topics 
                    WHERE week_plan_id = :wid AND user_id = :uid
                """), {'wid': fw_id, 'uid': user_id}).scalar()
            else:
                count = db.session.execute(text("""
                    SELECT COUNT(*) FROM passport_week_topics 
                    WHERE week_plan_id = :wid AND guest_code = :code
                """), {'wid': fw_id, 'code': guest_code}).scalar()
            week_topic_counts[fw_id] = count or 0
        
        # Distribute topics: assign to week with fewest topics (spreads evenly)
        for topic in incomplete_topics:
            topic_id, topic_name, old_week_id = topic
            
            # Find the future week with fewest topics
            target_week_id = min(future_weeks, key=lambda w: week_topic_counts[w[0]])[0]
            target_week_num = [w[1] for w in future_weeks if w[0] == target_week_id][0]
            
            # Update the topic's week assignment
            db.session.execute(text("""
                UPDATE passport_week_topics 
                SET week_plan_id = :new_week_id, 
                    updated_at = CURRENT_TIMESTAMP
                WHERE id = :topic_id
            """), {'new_week_id': target_week_id, 'topic_id': topic_id})
            
            week_topic_counts[target_week_id] += 1
            redistributed_count += 1
            
            print(f"[Passport]   Moved '{topic_name}' to week {target_week_num}")
        
        db.session.commit()
        
        return {
            'redistributed': redistributed_count,
            'from_weeks': len(past_week_ids),
            'to_weeks': len(future_weeks),
            'message': f'Redistributed {redistributed_count} incomplete topics'
        }
        
    except Exception as e:
        db.session.rollback()
        print(f"[Passport] Error redistributing topics: {e}")
        import traceback
        traceback.print_exc()
        return {'redistributed': 0, 'error': str(e)}


@passport_bp.route('/api/passport/v2/plan', methods=['GET'])
@guest_or_login_required
def get_weekly_plan():
    """Get the user's existing weekly study plan"""
    from sqlalchemy import text
    
    # Clear any cached data to ensure fresh read
    db.session.expire_all()
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        # Auto-redistribute incomplete topics from past weeks
        redistribution_result = redistribute_incomplete_topics(user_id=user_id, guest_code=guest_code)
        if redistribution_result.get('redistributed', 0) > 0:
            print(f"[Passport] Auto-redistributed {redistribution_result['redistributed']} topics from past weeks")
        
        if user_id:
            setup = db.session.execute(text("SELECT curriculum, exam_date, study_hours_per_week, last_plan_generated_at FROM passport_setup WHERE user_id = :uid"), {'uid': user_id}).fetchone()
        else:
            setup = db.session.execute(text("SELECT curriculum, exam_date, study_hours_per_week, last_plan_generated_at FROM passport_setup WHERE guest_code = :code"), {'code': guest_code}).fetchone()
        
        if not setup:
            return jsonify({'success': True, 'has_plan': False, 'message': 'No plan found. Complete setup first.'})
        
        curriculum = setup[0]
        exam_date = setup[1]
        
        if user_id:
            weeks = db.session.execute(text("""
                SELECT id, week_number, week_start_date, week_end_date, focus_area, capacity_hours, capacity_type, holiday_name, status
                FROM passport_weekly_plan WHERE user_id = :uid ORDER BY week_number
            """), {'uid': user_id}).fetchall()
        else:
            weeks = db.session.execute(text("""
                SELECT id, week_number, week_start_date, week_end_date, focus_area, capacity_hours, capacity_type, holiday_name, status
                FROM passport_weekly_plan WHERE guest_code = :code ORDER BY week_number
            """), {'code': guest_code}).fetchall()
        
        if not weeks:
            return jsonify({'success': True, 'has_plan': False, 'message': 'No weekly plan generated yet.'})
        
        weekly_plan = []
        current_week = None
        today = date.today()
        
        for week in weeks:
            week_id = week[0]
            week_start = datetime.strptime(week[2], '%Y-%m-%d').date() if isinstance(week[2], str) else week[2]
            week_end = datetime.strptime(week[3], '%Y-%m-%d').date() if isinstance(week[3], str) else week[3]
            is_current = week_start <= today <= week_end
            if is_current:
                current_week = week[1]
            
            if user_id:
                topics = db.session.execute(text("""
                    SELECT id, topic, strand, entry_level, target_level, priority, current_level, questions_answered, accuracy_percent, status, pinned, pinned_at
                    FROM passport_week_topics WHERE week_plan_id = :wpid AND user_id = :uid
                """), {'wpid': week_id, 'uid': user_id}).fetchall()
            else:
                topics = db.session.execute(text("""
                    SELECT id, topic, strand, entry_level, target_level, priority, current_level, questions_answered, accuracy_percent, status, pinned, pinned_at
                    FROM passport_week_topics WHERE week_plan_id = :wpid AND guest_code = :code
                """), {'wpid': week_id, 'code': guest_code}).fetchall()
            
            week_topics = []
            for t in topics:
                topic_name = t[1]
                strand_icon = '📝'
                for strand_id, strand in PASSPORT_TOPIC_STRANDS.items():
                    for topic in strand['topics']:
                        if topic['id'] == t[1]:
                            topic_name = topic['name']
                            strand_icon = strand['icon']
                            break
                
                week_topics.append({
                    'id': t[0], 'topic_id': t[1], 'topic_name': topic_name, 'strand': t[2], 'strand_icon': strand_icon,
                    'entry_level': t[3], 'target_level': t[4], 'priority': t[5], 'current_level': t[6],
                    'questions_answered': t[7] or 0, 'accuracy': t[8], 'status': t[9], 'pinned': bool(t[10]), 'pinned_at': t[11]
                })
            
            weekly_plan.append({
                'id': week_id, 'week_number': week[1], 'week_start': week[2], 'week_end': week[3],
                'focus_area': week[4], 'capacity_hours': week[5], 'capacity_type': week[6],
                'holiday_name': week[7], 'status': 'current' if is_current else week[8], 'is_current': is_current, 'topics': week_topics
            })
        
        weeks_to_exam = len(weeks)
        if exam_date:
            exam_dt = datetime.strptime(exam_date, '%Y-%m-%d').date() if isinstance(exam_date, str) else exam_date
            weeks_to_exam = max(1, (exam_dt - today).days // 7)
        
        return jsonify({
            'success': True, 'has_plan': True, 'curriculum': curriculum,
            'curriculum_name': CURRICULUM_HIERARCHY.get(curriculum, {}).get('display_name', curriculum),
            'exam_date': exam_date, 'weeks_to_exam': weeks_to_exam, 'current_week': current_week,
            'total_weeks': len(weekly_plan), 'weekly_plan': weekly_plan,
            'redistribution': redistribution_result
        })
        
    except Exception as e:
        print(f"Error fetching plan: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/v2/unpin-topic', methods=['POST'])
@guest_or_login_required
def unpin_topic():
    """Unpin a topic so it can be auto-adjusted"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    data = request.get_json()
    topic_id = data.get('topic_id')
    
    if not topic_id:
        return jsonify({'error': 'Missing topic_id'}), 400
    
    try:
        if user_id:
            db.session.execute(text("UPDATE passport_week_topics SET pinned = 0, updated_at = CURRENT_TIMESTAMP WHERE id = :tid AND user_id = :uid"), {'tid': topic_id, 'uid': user_id})
            db.session.execute(text("INSERT INTO passport_adjustments (user_id, adjustment_type, topic, reason, is_auto) VALUES (:uid, 'unpin', :topic, 'Student unpinned topic', 0)"), {'uid': user_id, 'topic': str(topic_id)})
        else:
            db.session.execute(text("UPDATE passport_week_topics SET pinned = 0, updated_at = CURRENT_TIMESTAMP WHERE id = :tid AND guest_code = :code"), {'tid': topic_id, 'code': guest_code})
            db.session.execute(text("INSERT INTO passport_adjustments (guest_code, adjustment_type, topic, reason, is_auto) VALUES (:code, 'unpin', :topic, 'Student unpinned topic', 0)"), {'code': guest_code, 'topic': str(topic_id)})
        
        db.session.commit()
        return jsonify({'success': True, 'message': 'Topic unpinned - system can now auto-adjust if needed'})
        
    except Exception as e:
        db.session.rollback()
        print(f"Error unpinning topic: {e}")
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/v2/dashboard', methods=['GET'])
@guest_or_login_required
def get_passport_dashboard():
    """Get dashboard data for current week"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        today = date.today()
        
        if user_id:
            setup = db.session.execute(text("SELECT curriculum, exam_date FROM passport_setup WHERE user_id = :uid"), {'uid': user_id}).fetchone()
        else:
            setup = db.session.execute(text("SELECT curriculum, exam_date FROM passport_setup WHERE guest_code = :code"), {'code': guest_code}).fetchone()
        
        if not setup:
            return jsonify({'success': True, 'has_plan': False})
        
        if user_id:
            current_week = db.session.execute(text("""
                SELECT id, week_number, week_start_date, week_end_date, focus_area, capacity_hours, capacity_type, holiday_name
                FROM passport_weekly_plan WHERE user_id = :uid AND week_start_date <= :today AND week_end_date >= :today
            """), {'uid': user_id, 'today': today.isoformat()}).fetchone()
        else:
            current_week = db.session.execute(text("""
                SELECT id, week_number, week_start_date, week_end_date, focus_area, capacity_hours, capacity_type, holiday_name
                FROM passport_weekly_plan WHERE guest_code = :code AND week_start_date <= :today AND week_end_date >= :today
            """), {'code': guest_code, 'today': today.isoformat()}).fetchone()
        
        if not current_week:
            return jsonify({'success': True, 'has_plan': True, 'current_week': None, 'message': 'No current week found'})
        
        week_id = current_week[0]
        week_start = datetime.strptime(current_week[2], '%Y-%m-%d').date() if isinstance(current_week[2], str) else current_week[2]
        week_end = datetime.strptime(current_week[3], '%Y-%m-%d').date() if isinstance(current_week[3], str) else current_week[3]
        days_left = (week_end - today).days + 1
        
        if user_id:
            topics = db.session.execute(text("""
                SELECT wt.id, wt.topic, wt.strand, wt.entry_level, wt.target_level, wt.priority, wt.current_level, wt.questions_answered, wt.accuracy_percent, wt.status, wt.pinned, ap.current_level as actual_level
                FROM passport_week_topics wt LEFT JOIN adaptive_progress ap ON ap.topic = wt.topic AND ap.user_id = wt.user_id
                WHERE wt.week_plan_id = :wpid AND wt.user_id = :uid
            """), {'wpid': week_id, 'uid': user_id}).fetchall()
        else:
            topics = db.session.execute(text("""
                SELECT wt.id, wt.topic, wt.strand, wt.entry_level, wt.target_level, wt.priority, wt.current_level, wt.questions_answered, wt.accuracy_percent, wt.status, wt.pinned, ap.current_level as actual_level
                FROM passport_week_topics wt LEFT JOIN adaptive_progress ap ON ap.topic = wt.topic AND ap.guest_code = wt.guest_code
                WHERE wt.week_plan_id = :wpid AND wt.guest_code = :code
            """), {'wpid': week_id, 'code': guest_code}).fetchall()
        
        week_topics = []
        total_questions = 0
        completed_count = 0
        
        for t in topics:
            topic_name = t[1]
            strand_icon = '📝'
            for strand_id, strand in PASSPORT_TOPIC_STRANDS.items():
                for topic in strand['topics']:
                    if topic['id'] == t[1]:
                        topic_name = topic['name']
                        strand_icon = strand['icon']
                        break
            
            actual_level = t[11] or t[3]
            target = t[4]
            progress_pct = min(100, round(((actual_level - t[3]) / max(1, target - t[3])) * 100)) if target > t[3] else 100
            
            is_completed = actual_level >= target
            if is_completed:
                completed_count += 1
            
            questions = t[7] or 0
            total_questions += questions
            
            week_topics.append({
                'id': t[0], 'topic_id': t[1], 'topic_name': topic_name, 'strand': t[2], 'strand_icon': strand_icon,
                'entry_level': t[3], 'target_level': target, 'current_level': actual_level, 'priority': t[5],
                'questions_answered': questions, 'accuracy': t[8], 'status': 'completed' if is_completed else t[9],
                'pinned': bool(t[10]), 'progress_percent': progress_pct
            })
        
        target_questions = 100
        on_track = total_questions >= (target_questions * (1 - days_left / 7))
        
        if user_id:
            total_weeks = db.session.execute(text("SELECT COUNT(*) FROM passport_weekly_plan WHERE user_id = :uid"), {'uid': user_id}).fetchone()[0]
        else:
            total_weeks = db.session.execute(text("SELECT COUNT(*) FROM passport_weekly_plan WHERE guest_code = :code"), {'code': guest_code}).fetchone()[0]
        
        return jsonify({
            'success': True, 'has_plan': True, 'curriculum': setup[0], 'exam_date': setup[1],
            'current_week': {
                'week_number': current_week[1], 'total_weeks': total_weeks, 'week_start': current_week[2],
                'week_end': current_week[3], 'days_left': days_left, 'focus_area': current_week[4],
                'capacity_hours': current_week[5], 'capacity_type': current_week[6], 'holiday_name': current_week[7], 'topics': week_topics
            },
            'stats': {
                'topics_count': len(week_topics), 'completed_count': completed_count, 'questions_answered': total_questions,
                'questions_target': target_questions, 'on_track': on_track,
                'status': 'ahead' if total_questions > target_questions * 0.7 else ('on_track' if on_track else 'behind')
            }
        })
        
    except Exception as e:
        print(f"Error fetching dashboard: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


# =====================================================
# PASSPORT V2 - PHASE 6: PROGRESS SYNC & TRACKING
# =====================================================

@passport_bp.route('/api/passport/v2/sync-progress', methods=['POST'])
@guest_or_login_required
def sync_passport_progress():
    """Sync progress from adaptive_progress to passport_week_topics for current week"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        today = date.today()
        
        # Get current week's plan
        if user_id:
            current_week = db.session.execute(text("""
                SELECT id FROM passport_weekly_plan 
                WHERE user_id = :uid AND week_start_date <= :today AND week_end_date >= :today
            """), {'uid': user_id, 'today': today.isoformat()}).fetchone()
        else:
            current_week = db.session.execute(text("""
                SELECT id FROM passport_weekly_plan 
                WHERE guest_code = :code AND week_start_date <= :today AND week_end_date >= :today
            """), {'code': guest_code, 'today': today.isoformat()}).fetchone()
        
        if not current_week:
            # No current week - this is OK, not an error
            return jsonify({'success': True, 'synced': 0, 'completed': 0, 'message': 'No current week in plan'})
        
        week_id = current_week[0]
        synced_count = 0
        completed_count = 0
        
        # Get all topics for current week
        if user_id:
            week_topics = db.session.execute(text("""
                SELECT wt.id, wt.topic, wt.entry_level, wt.target_level, wt.status
                FROM passport_week_topics wt
                WHERE wt.week_plan_id = :wpid AND wt.user_id = :uid
            """), {'wpid': week_id, 'uid': user_id}).fetchall()
        else:
            week_topics = db.session.execute(text("""
                SELECT wt.id, wt.topic, wt.entry_level, wt.target_level, wt.status
                FROM passport_week_topics wt
                WHERE wt.week_plan_id = :wpid AND wt.guest_code = :code
            """), {'wpid': week_id, 'code': guest_code}).fetchall()
        
        if not week_topics:
            return jsonify({'success': True, 'synced': 0, 'completed': 0, 'message': 'No topics in current week'})
        
        for wt in week_topics:
            wt_id, topic_id, entry_level, target_level, current_status = wt
            
            # Get latest progress from adaptive_progress
            if user_id:
                progress = db.session.execute(text("""
                    SELECT current_level, current_points FROM adaptive_progress
                    WHERE user_id = :uid AND topic = :topic
                """), {'uid': user_id, 'topic': topic_id}).fetchone()
                
                # Get question count from history (no score column exists)
                stats = db.session.execute(text("""
                    SELECT COUNT(*) as total
                    FROM user_question_history 
                    WHERE user_id = :uid AND topic = :topic
                """), {'uid': user_id, 'topic': topic_id}).fetchone()
            else:
                progress = db.session.execute(text("""
                    SELECT current_level, current_points FROM adaptive_progress
                    WHERE guest_code = :code AND topic = :topic
                """), {'code': guest_code, 'topic': topic_id}).fetchone()
                
                stats = db.session.execute(text("""
                    SELECT COUNT(*) as total
                    FROM user_question_history 
                    WHERE guest_code = :code AND topic = :topic
                """), {'code': guest_code, 'topic': topic_id}).fetchone()
            
            if progress:
                current_level = progress[0]
                questions_answered = stats[0] if stats else 0
                accuracy = 0  # Not tracked in user_question_history
                
                # Determine status
                new_status = current_status
                if current_level >= target_level:
                    new_status = 'completed'
                    completed_count += 1
                elif questions_answered > 0:
                    new_status = 'in_progress'
                
                # Update passport_week_topics
                if user_id:
                    db.session.execute(text("""
                        UPDATE passport_week_topics 
                        SET current_level = :level, questions_answered = :questions, 
                            accuracy_percent = :accuracy, status = :status, updated_at = CURRENT_TIMESTAMP
                        WHERE id = :wt_id AND user_id = :uid
                    """), {'level': current_level, 'questions': questions_answered, 
                           'accuracy': accuracy, 'status': new_status, 'wt_id': wt_id, 'uid': user_id})
                else:
                    db.session.execute(text("""
                        UPDATE passport_week_topics 
                        SET current_level = :level, questions_answered = :questions, 
                            accuracy_percent = :accuracy, status = :status, updated_at = CURRENT_TIMESTAMP
                        WHERE id = :wt_id AND guest_code = :code
                    """), {'level': current_level, 'questions': questions_answered, 
                           'accuracy': accuracy, 'status': new_status, 'wt_id': wt_id, 'code': guest_code})
                
                synced_count += 1
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'synced': synced_count,
            'completed': completed_count,
            'message': f'Synced {synced_count} topics, {completed_count} completed'
        })
        
    except Exception as e:
        db.session.rollback()
        print(f"Error syncing progress: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/v2/record-activity', methods=['POST'])
@guest_or_login_required
def record_passport_activity():
    """Record quiz activity for a specific topic"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        topic_id = data.get('topic_id')
        questions_answered = data.get('questions_answered', 0)
        correct_answers = data.get('correct_answers', 0)
        new_level = data.get('new_level')
        
        if not topic_id:
            return jsonify({'error': 'topic_id required'}), 400
        
        today = date.today()
        
        # Find the topic in current week's plan
        if user_id:
            week_topic = db.session.execute(text("""
                SELECT wt.id, wt.target_level, wp.id as week_id
                FROM passport_week_topics wt
                JOIN passport_weekly_plan wp ON wp.id = wt.week_plan_id
                WHERE wt.user_id = :uid AND wt.topic = :topic
                AND wp.week_start_date <= :today AND wp.week_end_date >= :today
            """), {'uid': user_id, 'topic': topic_id, 'today': today.isoformat()}).fetchone()
        else:
            week_topic = db.session.execute(text("""
                SELECT wt.id, wt.target_level, wp.id as week_id
                FROM passport_week_topics wt
                JOIN passport_weekly_plan wp ON wp.id = wt.week_plan_id
                WHERE wt.guest_code = :code AND wt.topic = :topic
                AND wp.week_start_date <= :today AND wp.week_end_date >= :today
            """), {'code': guest_code, 'topic': topic_id, 'today': today.isoformat()}).fetchone()
        
        if not week_topic:
            return jsonify({'success': True, 'in_plan': False, 'message': 'Topic not in current week plan'})
        
        wt_id, target_level, week_id = week_topic
        
        # Calculate accuracy
        accuracy = round((correct_answers / questions_answered * 100)) if questions_answered > 0 else 0
        
        # Determine if completed
        is_completed = new_level >= target_level if new_level else False
        new_status = 'completed' if is_completed else 'in_progress'
        
        # Update the week topic record
        if user_id:
            # Get existing counts to add to
            existing = db.session.execute(text("""
                SELECT questions_answered, current_level FROM passport_week_topics WHERE id = :wt_id
            """), {'wt_id': wt_id}).fetchone()
            
            total_questions = (existing[0] or 0) + questions_answered
            current_level = new_level if new_level else (existing[1] or 1)
            
            db.session.execute(text("""
                UPDATE passport_week_topics 
                SET current_level = :level, questions_answered = :questions, 
                    accuracy_percent = :accuracy, status = :status, updated_at = CURRENT_TIMESTAMP
                WHERE id = :wt_id AND user_id = :uid
            """), {'level': current_level, 'questions': total_questions, 
                   'accuracy': accuracy, 'status': new_status, 'wt_id': wt_id, 'uid': user_id})
        else:
            existing = db.session.execute(text("""
                SELECT questions_answered, current_level FROM passport_week_topics WHERE id = :wt_id
            """), {'wt_id': wt_id}).fetchone()
            
            total_questions = (existing[0] or 0) + questions_answered
            current_level = new_level if new_level else (existing[1] or 1)
            
            db.session.execute(text("""
                UPDATE passport_week_topics 
                SET current_level = :level, questions_answered = :questions, 
                    accuracy_percent = :accuracy, status = :status, updated_at = CURRENT_TIMESTAMP
                WHERE id = :wt_id AND guest_code = :code
            """), {'level': current_level, 'questions': total_questions, 
                   'accuracy': accuracy, 'status': new_status, 'wt_id': wt_id, 'code': guest_code})
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'in_plan': True,
            'topic_id': topic_id,
            'current_level': current_level,
            'target_level': target_level,
            'is_completed': is_completed,
            'questions_total': total_questions,
            'accuracy': accuracy
        })
        
    except Exception as e:
        db.session.rollback()
        print(f"Error recording activity: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/v2/topic-progress/<topic_id>', methods=['GET'])
@guest_or_login_required
def get_passport_v2_topic_progress(topic_id):
    """Get detailed progress for a specific topic"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        # Get from adaptive_progress
        if user_id:
            progress = db.session.execute(text("""
                SELECT current_level, current_points, updated_at 
                FROM adaptive_progress WHERE user_id = :uid AND topic = :topic
            """), {'uid': user_id, 'topic': topic_id}).fetchone()
            
            stats = db.session.execute(text("""
                SELECT COUNT(*) as total, 
                       MAX(seen_at) as last_activity
                FROM user_question_history 
                WHERE user_id = :uid AND topic = :topic
            """), {'uid': user_id, 'topic': topic_id}).fetchone()
        else:
            progress = db.session.execute(text("""
                SELECT current_level, current_points, updated_at 
                FROM adaptive_progress WHERE guest_code = :code AND topic = :topic
            """), {'code': guest_code, 'topic': topic_id}).fetchone()
            
            stats = db.session.execute(text("""
                SELECT COUNT(*) as total, 
                       MAX(seen_at) as last_activity
                FROM user_question_history 
                WHERE guest_code = :code AND topic = :topic
            """), {'code': guest_code, 'topic': topic_id}).fetchone()
        
        current_level = progress[0] if progress else 1
        current_points = progress[1] if progress else 0
        questions_total = stats[0] if stats else 0
        questions_correct = 0  # Not tracked in user_question_history
        last_activity = stats[1] if stats else None
        accuracy = 0  # Not tracked in user_question_history
        
        # Get topic info
        topic_name = topic_id
        strand_name = ''
        strand_icon = '📝'
        for strand_id, strand in PASSPORT_TOPIC_STRANDS.items():
            for topic in strand['topics']:
                if topic['id'] == topic_id:
                    topic_name = topic['name']
                    strand_name = strand['display_name']
                    strand_icon = strand['icon']
                    break
        
        return jsonify({
            'success': True,
            'topic_id': topic_id,
            'topic_name': topic_name,
            'strand': strand_name,
            'strand_icon': strand_icon,
            'current_level': current_level,
            'current_points': current_points,
            'questions_total': questions_total,
            'questions_correct': questions_correct,
            'accuracy': accuracy,
            'last_activity': last_activity
        })
        
    except Exception as e:
        print(f"Error getting topic progress: {e}")
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/v2/weekly-summary', methods=['GET'])
@guest_or_login_required  
def get_weekly_summary():
    """Get summary stats for current week"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        today = date.today()
        week_start = today - timedelta(days=today.weekday())  # Monday
        
        # Get questions answered this week - user_question_history only tracks seen questions
        try:
            if user_id:
                week_stats = db.session.execute(text("""
                    SELECT COUNT(*) as total,
                           COUNT(DISTINCT topic) as topics_practiced
                    FROM user_question_history 
                    WHERE user_id = :uid AND DATE(seen_at) >= :week_start
                """), {'uid': user_id, 'week_start': week_start.isoformat()}).fetchone()
            else:
                week_stats = db.session.execute(text("""
                    SELECT COUNT(*) as total,
                           COUNT(DISTINCT topic) as topics_practiced
                    FROM user_question_history 
                    WHERE guest_code = :code AND DATE(seen_at) >= :week_start
                """), {'code': guest_code, 'week_start': week_start.isoformat()}).fetchone()
        except Exception as e:
            print(f"Error getting week stats: {e}")
            week_stats = (0, 0)
        
        # Get streak info - handle missing tables gracefully
        try:
            if user_id:
                streak = db.session.execute(text("""
                    SELECT current_streak, longest_streak FROM user_streaks WHERE user_id = :uid
                """), {'uid': user_id}).fetchone()
            else:
                streak = db.session.execute(text("""
                    SELECT current_streak, longest_streak FROM guest_streaks WHERE guest_code = :code
                """), {'code': guest_code}).fetchone()
        except Exception as e:
            print(f"Error getting streak: {e}")
            streak = None
        
        questions_total = week_stats[0] if week_stats and week_stats[0] else 0
        topics_practiced = week_stats[1] if week_stats and week_stats[1] else 0
        
        current_streak = streak[0] if streak else 0
        longest_streak = streak[1] if streak else 0
        
        return jsonify({
            'success': True,
            'week_start': week_start.isoformat(),
            'questions_answered': questions_total,
            'questions_correct': 0,  # Not tracked in this table
            'accuracy': 0,  # Not tracked in this table
            'topics_practiced': topics_practiced,
            'current_streak': current_streak,
            'longest_streak': longest_streak
        })
        
    except Exception as e:
        print(f"Error getting weekly summary: {e}")
        return jsonify({'error': str(e)}), 500


# =====================================================
# PASSPORT V2 - PHASE 7: DRAG & DROP / PIN TOPICS
# =====================================================

@passport_bp.route('/api/passport/v2/move-topic', methods=['POST'])
@guest_or_login_required
def move_passport_topic():
    """Move a topic to a different week or reorder within a week"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        topic_id = data.get('topic_id')
        from_week = data.get('from_week')  # week_number
        to_week = data.get('to_week')      # week_number
        new_position = data.get('position', 0)  # position within the week
        
        print(f"Move topic request: topic={topic_id}, from_week={from_week}, to_week={to_week}")
        
        if not topic_id or to_week is None:
            return jsonify({'error': 'topic_id and to_week required'}), 400
        
        # Get the week_plan_id for the target week
        if user_id:
            target_week = db.session.execute(text("""
                SELECT id FROM passport_weekly_plan 
                WHERE user_id = :uid AND week_number = :week_num
            """), {'uid': user_id, 'week_num': to_week}).fetchone()
            
            # Get the topic record - find by topic name
            topic_record = db.session.execute(text("""
                SELECT wt.id, wt.week_plan_id, wt.pinned, wp.week_number as current_week 
                FROM passport_week_topics wt
                JOIN passport_weekly_plan wp ON wp.id = wt.week_plan_id
                WHERE wt.user_id = :uid AND wt.topic = :topic
                ORDER BY wt.id LIMIT 1
            """), {'uid': user_id, 'topic': topic_id}).fetchone()
        else:
            target_week = db.session.execute(text("""
                SELECT id FROM passport_weekly_plan 
                WHERE guest_code = :code AND week_number = :week_num
            """), {'code': guest_code, 'week_num': to_week}).fetchone()
            
            topic_record = db.session.execute(text("""
                SELECT wt.id, wt.week_plan_id, wt.pinned, wp.week_number as current_week 
                FROM passport_week_topics wt
                JOIN passport_weekly_plan wp ON wp.id = wt.week_plan_id
                WHERE wt.guest_code = :code AND wt.topic = :topic
                ORDER BY wt.id LIMIT 1
            """), {'code': guest_code, 'topic': topic_id}).fetchone()
        
        if not target_week:
            return jsonify({'error': f'Week {to_week} not found'}), 404
        
        if not topic_record:
            return jsonify({'error': 'Topic not found in plan'}), 404
        
        print(f"Found topic record: id={topic_record[0]}, current_week_plan_id={topic_record[1]}, pinned={topic_record[2]}, current_week_num={topic_record[3]}")
        
        # Check if topic is pinned
        if topic_record[2]:  # pinned
            return jsonify({'error': 'Cannot move pinned topic. Unpin it first.'}), 400
        
        target_week_id = target_week[0]
        topic_wt_id = topic_record[0]
        
        print(f"Moving topic {topic_wt_id} to week_plan_id {target_week_id}")
        
        # Update the topic's week assignment using raw connection for immediate commit
        if user_id:
            db.session.execute(text("""
                UPDATE passport_week_topics 
                SET week_plan_id = :new_week_id, priority = :pos, updated_at = CURRENT_TIMESTAMP
                WHERE id = :wt_id
            """), {'new_week_id': target_week_id, 'pos': new_position, 'wt_id': topic_wt_id})
        else:
            db.session.execute(text("""
                UPDATE passport_week_topics 
                SET week_plan_id = :new_week_id, priority = :pos, updated_at = CURRENT_TIMESTAMP
                WHERE id = :wt_id
            """), {'new_week_id': target_week_id, 'pos': new_position, 'wt_id': topic_wt_id})
        
        # Force flush to database
        db.session.flush()
        db.session.commit()
        
        # Verify the update worked
        if user_id:
            verify = db.session.execute(text("""
                SELECT wt.week_plan_id, wp.week_number 
                FROM passport_week_topics wt
                JOIN passport_weekly_plan wp ON wp.id = wt.week_plan_id
                WHERE wt.id = :wt_id
            """), {'wt_id': topic_wt_id}).fetchone()
        else:
            verify = db.session.execute(text("""
                SELECT wt.week_plan_id, wp.week_number 
                FROM passport_week_topics wt
                JOIN passport_weekly_plan wp ON wp.id = wt.week_plan_id
                WHERE wt.id = :wt_id
            """), {'wt_id': topic_wt_id}).fetchone()
        
        if verify:
            print(f"Verified: topic now in week_plan_id={verify[0]}, week_number={verify[1]}")
        else:
            print(f"WARNING: Could not verify topic move!")
        
        print(f"Topic move committed successfully")
        
        return jsonify({
            'success': True,
            'topic_id': topic_id,
            'moved_to_week': to_week,
            'position': new_position,
            'verified_week': verify[1] if verify else None
        })
        
    except Exception as e:
        db.session.rollback()
        print(f"Error moving topic: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@passport_bp.route('/api/passport/v2/pin-topic', methods=['POST'])
@guest_or_login_required
def pin_passport_topic():
    """Pin or unpin a topic to lock it in place"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        topic_id = data.get('topic_id')
        pinned = data.get('pinned', True)  # True to pin, False to unpin
        
        if not topic_id:
            return jsonify({'error': 'topic_id required'}), 400
        
        # Update the pin status
        if user_id:
            result = db.session.execute(text("""
                UPDATE passport_week_topics 
                SET pinned = :pinned, updated_at = CURRENT_TIMESTAMP
                WHERE user_id = :uid AND topic = :topic
            """), {'pinned': 1 if pinned else 0, 'uid': user_id, 'topic': topic_id})
        else:
            result = db.session.execute(text("""
                UPDATE passport_week_topics 
                SET pinned = :pinned, updated_at = CURRENT_TIMESTAMP
                WHERE guest_code = :code AND topic = :topic
            """), {'pinned': 1 if pinned else 0, 'code': guest_code, 'topic': topic_id})
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'topic_id': topic_id,
            'pinned': pinned
        })
        
    except Exception as e:
        db.session.rollback()
        print(f"Error pinning topic: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500



@passport_bp.route('/api/passport/v2/redistribute', methods=['POST'])
@guest_or_login_required
def redistribute_past_topics():
    """Manually trigger redistribution of incomplete topics from past weeks"""
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    result = redistribute_incomplete_topics(user_id=user_id, guest_code=guest_code)
    
    return jsonify({
        'success': True,
        **result
    })


@passport_bp.route('/api/passport/v2/reorder-topics', methods=['POST'])
@guest_or_login_required
def reorder_passport_topics():
    """Reorder topics within a week"""
    from sqlalchemy import text
    
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        week_number = data.get('week_number')
        topic_order = data.get('topic_order', [])  # List of topic_ids in new order
        
        if week_number is None or not topic_order:
            return jsonify({'error': 'week_number and topic_order required'}), 400
        
        # Get week_plan_id
        if user_id:
            week = db.session.execute(text("""
                SELECT id FROM passport_weekly_plan WHERE user_id = :uid AND week_number = :week_num
            """), {'uid': user_id, 'week_num': week_number}).fetchone()
        else:
            week = db.session.execute(text("""
                SELECT id FROM passport_weekly_plan WHERE guest_code = :code AND week_number = :week_num
            """), {'code': guest_code, 'week_num': week_number}).fetchone()
        
        if not week:
            return jsonify({'error': f'Week {week_number} not found'}), 404
        
        week_id = week[0]
        
        # Update priorities based on new order
        for idx, topic_id in enumerate(topic_order):
            if user_id:
                db.session.execute(text("""
                    UPDATE passport_week_topics 
                    SET priority = :priority, updated_at = CURRENT_TIMESTAMP
                    WHERE week_plan_id = :week_id AND user_id = :uid AND topic = :topic
                """), {'priority': idx, 'week_id': week_id, 'uid': user_id, 'topic': topic_id})
            else:
                db.session.execute(text("""
                    UPDATE passport_week_topics 
                    SET priority = :priority, updated_at = CURRENT_TIMESTAMP
                    WHERE week_plan_id = :week_id AND guest_code = :code AND topic = :topic
                """), {'priority': idx, 'week_id': week_id, 'code': guest_code, 'topic': topic_id})
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'week_number': week_number,
            'new_order': topic_order
        })
        
    except Exception as e:
        db.session.rollback()
        print(f"Error reordering topics: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


# =====================================================
# ILP ENGINE - PHASE 12: REACTIVE RECOMMENDATIONS
# Sprint 1: Skill Tagging & Prerequisite Analysis
# =====================================================

def auto_tag_questions_for_topic(topic_id):
    """
    Auto-assign skill tags to all questions for a topic.
    Uses ILP_TOPIC_SKILL_TAGS configuration.
    Returns count of tags created.
    """
    from sqlalchemy import text
    
    if topic_id not in ILP_TOPIC_SKILL_TAGS:
        return 0
    
    skill_tags = ILP_TOPIC_SKILL_TAGS[topic_id]
    tags_created = 0
    
    try:
        # Get all question IDs for this topic
        questions = db.session.execute(text("""
            SELECT id FROM questions WHERE topic = :topic
        """), {'topic': topic_id}).fetchall()
        
        for q in questions:
            question_id = q[0]
            
            for skill_tag, weight in skill_tags:
                # Check if tag already exists
                existing = db.session.execute(text("""
                    SELECT id FROM question_skill_tags 
                    WHERE question_id = :qid AND skill_tag = :tag
                """), {'qid': question_id, 'tag': skill_tag}).fetchone()
                
                if not existing:
                    db.session.execute(text("""
                        INSERT INTO question_skill_tags (question_id, skill_tag, weight)
                        VALUES (:qid, :tag, :weight)
                    """), {'qid': question_id, 'tag': skill_tag, 'weight': weight})
                    tags_created += 1
        
        db.session.commit()
        
    except Exception as e:
        db.session.rollback()
        print(f"Error auto-tagging questions for {topic_id}: {e}")
        return 0
    
    return tags_created


def get_skill_breakdown_for_student(user_id=None, guest_code=None, topic_id=None, days=7):
    """
    Analyse a student's performance by skill tags.
    Returns breakdown of accuracy per skill for recent activity.
    """
    from sqlalchemy import text
    from datetime import datetime, timedelta
    
    cutoff_date = datetime.now() - timedelta(days=days)
    skill_stats = {}
    
    try:
        # Build query based on user type and optional topic filter
        if user_id:
            user_clause = "ua.user_id = :uid"
            params = {'uid': user_id, 'cutoff': cutoff_date}
        else:
            user_clause = "ua.guest_code = :code"
            params = {'code': guest_code, 'cutoff': cutoff_date}
        
        topic_clause = ""
        if topic_id:
            topic_clause = "AND ua.topic = :topic"
            params['topic'] = topic_id
        
        # Get all answers with skill tags
        results = db.session.execute(text(f"""
            SELECT 
                qst.skill_tag,
                qst.weight,
                ua.is_correct,
                ua.topic
            FROM user_answers ua
            JOIN question_skill_tags qst ON ua.question_id = qst.question_id
            WHERE {user_clause}
            AND ua.answered_at >= :cutoff
            {topic_clause}
        """), params).fetchall()
        
        # Aggregate by skill
        for row in results:
            skill_tag = row[0]
            weight = float(row[1])
            is_correct = row[2]
            topic = row[3]
            
            if skill_tag not in skill_stats:
                skill_stats[skill_tag] = {
                    'correct': 0,
                    'total': 0,
                    'weighted_correct': 0,
                    'weighted_total': 0,
                    'topics': set()
                }
            
            skill_stats[skill_tag]['total'] += 1
            skill_stats[skill_tag]['weighted_total'] += weight
            skill_stats[skill_tag]['topics'].add(topic)
            
            if is_correct:
                skill_stats[skill_tag]['correct'] += 1
                skill_stats[skill_tag]['weighted_correct'] += weight
        
        # Calculate accuracies and convert sets to lists
        for skill in skill_stats:
            stats = skill_stats[skill]
            stats['accuracy'] = stats['correct'] / stats['total'] if stats['total'] > 0 else 0
            stats['weighted_accuracy'] = stats['weighted_correct'] / stats['weighted_total'] if stats['weighted_total'] > 0 else 0
            stats['topics'] = list(stats['topics'])
        
    except Exception as e:
        print(f"Error getting skill breakdown: {e}")
        return {}
    
    return skill_stats


def get_prerequisites_for_topic(topic_id):
    """
    Get all prerequisites for a topic, including transitive dependencies.
    Returns list of prerequisite topic IDs ordered by dependency depth.
    """
    prerequisites = []
    visited = set()
    
    def collect_prereqs(tid, depth=0):
        if tid in visited:
            return
        visited.add(tid)
        
        direct_prereqs = ILP_PREREQUISITE_MAP.get(tid, [])
        for prereq in direct_prereqs:
            if prereq not in visited:
                prerequisites.append({'topic_id': prereq, 'depth': depth + 1})
                collect_prereqs(prereq, depth + 1)
    
    collect_prereqs(topic_id)
    
    # Sort by depth (deepest dependencies first)
    prerequisites.sort(key=lambda x: -x['depth'])
    
    return [p['topic_id'] for p in prerequisites]


def check_prerequisite_gaps(user_id=None, guest_code=None, topic_id=None):
    """
    Check if a student has gaps in prerequisites for a topic.
    Returns list of weak/untested prerequisites.
    """
    from sqlalchemy import text
    
    prerequisites = get_prerequisites_for_topic(topic_id)
    gaps = {'weak': [], 'untested': []}
    
    for prereq in prerequisites:
        # Get student's level in this prerequisite
        if user_id:
            level_row = db.session.execute(text("""
                SELECT current_level FROM adaptive_progress
                WHERE user_id = :uid AND topic = :topic
            """), {'uid': user_id, 'topic': prereq}).fetchone()
        else:
            level_row = db.session.execute(text("""
                SELECT current_level FROM adaptive_progress
                WHERE guest_code = :code AND topic = :topic
            """), {'code': guest_code, 'topic': prereq}).fetchone()
        
        if not level_row or level_row[0] == 0:
            gaps['untested'].append(prereq)
        elif level_row[0] < ILP_THRESHOLDS['bronze_level']:
            gaps['weak'].append({
                'topic_id': prereq,
                'current_level': level_row[0],
                'gap': ILP_THRESHOLDS['bronze_level'] - level_row[0]
            })
    
    return gaps


def identify_numeracy_needs(skill_breakdown):
    """
    Check if student needs numeracy reinforcement based on skill breakdown.
    Returns list of recommended numeracy topics.
    """
    numeracy_topics_needed = set()
    weak_skills = []
    
    threshold = ILP_THRESHOLDS['numeracy_trigger']
    min_questions = ILP_THRESHOLDS['min_questions_for_signal']
    
    for skill_tag, stats in skill_breakdown.items():
        if stats['total'] >= min_questions and stats['accuracy'] < threshold:
            weak_skills.append({
                'skill': skill_tag,
                'accuracy': stats['accuracy'],
                'total': stats['total']
            })
            
            # Map to numeracy topics
            if skill_tag in ILP_SKILL_TO_NUMERACY:
                for topic in ILP_SKILL_TO_NUMERACY[skill_tag]:
                    numeracy_topics_needed.add(topic)
    
    return {
        'weak_skills': weak_skills,
        'recommended_topics': list(numeracy_topics_needed)
    }


# =====================================================
# ILP ENGINE API ENDPOINTS
# =====================================================

@passport_bp.route('/api/ilp/skill-breakdown', methods=['GET'])
@guest_or_login_required
def get_ilp_skill_breakdown():
    """Get skill breakdown for current user"""
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    topic_id = request.args.get('topic')
    days = int(request.args.get('days', 7))
    
    breakdown = get_skill_breakdown_for_student(
        user_id=user_id,
        guest_code=guest_code,
        topic_id=topic_id,
        days=days
    )
    
    # Sort by accuracy (lowest first - biggest gaps)
    sorted_skills = sorted(
        [{'skill': k, **v} for k, v in breakdown.items()],
        key=lambda x: x['accuracy']
    )
    
    return jsonify({
        'success': True,
        'days': days,
        'topic': topic_id,
        'skill_count': len(breakdown),
        'skills': sorted_skills
    })


@passport_bp.route('/api/ilp/prerequisite-check/<topic_id>', methods=['GET'])
@guest_or_login_required
def get_ilp_prerequisite_check(topic_id):
    """Check prerequisite gaps for a specific topic"""
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    # Get all prerequisites
    all_prereqs = get_prerequisites_for_topic(topic_id)
    
    # Check for gaps
    gaps = check_prerequisite_gaps(
        user_id=user_id,
        guest_code=guest_code,
        topic_id=topic_id
    )
    
    return jsonify({
        'success': True,
        'topic_id': topic_id,
        'total_prerequisites': len(all_prereqs),
        'prerequisites': all_prereqs,
        'gaps': gaps,
        'has_gaps': len(gaps['weak']) > 0 or len(gaps['untested']) > 0
    })


@passport_bp.route('/api/ilp/numeracy-check', methods=['GET'])
@guest_or_login_required
def get_ilp_numeracy_check():
    """Check if student needs numeracy reinforcement"""
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    days = int(request.args.get('days', 7))
    
    # Get skill breakdown
    breakdown = get_skill_breakdown_for_student(
        user_id=user_id,
        guest_code=guest_code,
        days=days
    )
    
    # Check numeracy needs
    numeracy_needs = identify_numeracy_needs(breakdown)
    
    return jsonify({
        'success': True,
        'days': days,
        'threshold': ILP_THRESHOLDS['numeracy_trigger'],
        'weak_skills': numeracy_needs['weak_skills'],
        'recommended_numeracy_topics': numeracy_needs['recommended_topics'],
        'needs_numeracy': len(numeracy_needs['recommended_topics']) > 0
    })


@passport_bp.route('/api/ilp/auto-tag/<topic_id>', methods=['POST'])
@guest_or_login_required  
def run_auto_tag_for_topic(topic_id):
    """Run auto-tagger for a specific topic (admin function)"""
    # For now, allow anyone to trigger this - can add admin check later
    
    if topic_id not in ILP_TOPIC_SKILL_TAGS:
        return jsonify({
            'success': False,
            'error': f'No skill tags defined for topic: {topic_id}'
        }), 400
    
    tags_created = auto_tag_questions_for_topic(topic_id)
    
    return jsonify({
        'success': True,
        'topic_id': topic_id,
        'tags_created': tags_created,
        'skill_tags': [tag for tag, _ in ILP_TOPIC_SKILL_TAGS[topic_id]]
    })


@passport_bp.route('/api/ilp/auto-tag-all', methods=['POST'])
@guest_or_login_required
def run_auto_tag_all_topics():
    """Run auto-tagger for ALL topics (admin function)"""
    total_tags = 0
    topics_processed = []
    
    for topic_id in ILP_TOPIC_SKILL_TAGS.keys():
        tags = auto_tag_questions_for_topic(topic_id)
        if tags > 0:
            topics_processed.append({'topic': topic_id, 'tags': tags})
            total_tags += tags
    
    return jsonify({
        'success': True,
        'total_tags_created': total_tags,
        'topics_processed': len(topics_processed),
        'details': topics_processed
    })


@passport_bp.route('/api/ilp/config', methods=['GET'])
def get_ilp_config():
    """Get ILP configuration (public)"""
    return jsonify({
        'success': True,
        'thresholds': ILP_THRESHOLDS,
        'priority_levels': ILP_PRIORITY_CONFIG,
        'topics_with_skill_tags': list(ILP_TOPIC_SKILL_TAGS.keys()),
        'topics_with_prerequisites': list(ILP_PREREQUISITE_MAP.keys())
    })


@passport_bp.route('/api/ilp/topic-info/<topic_id>', methods=['GET'])
def get_ilp_topic_info(topic_id):
    """Get ILP info for a specific topic"""
    prereqs = ILP_PREREQUISITE_MAP.get(topic_id, [])
    skill_tags = ILP_TOPIC_SKILL_TAGS.get(topic_id, [])
    
    # Get topics that depend on this one
    dependents = [
        tid for tid, prereqs in ILP_PREREQUISITE_MAP.items()
        if topic_id in prereqs
    ]
    
    return jsonify({
        'success': True,
        'topic_id': topic_id,
        'prerequisites': prereqs,
        'prerequisite_count': len(prereqs),
        'skill_tags': [{'tag': tag, 'weight': weight} for tag, weight in skill_tags],
        'dependent_topics': dependents,
        'is_foundation': len(prereqs) == 0
    })


# =====================================================
# DATABASE SETUP FOR ILP ENGINE
# =====================================================

def create_ilp_tables():
    """Create ILP-related database tables if they don't exist"""
    from sqlalchemy import text
    
    try:
        # Question skill tags table
        db.session.execute(text("""
            CREATE TABLE IF NOT EXISTS question_skill_tags (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question_id INTEGER NOT NULL,
                skill_tag VARCHAR(50) NOT NULL,
                weight DECIMAL(3,2) DEFAULT 1.0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (question_id) REFERENCES questions(id)
            )
        """))
        
        # Create indexes
        try:
            db.session.execute(text("""
                CREATE INDEX IF NOT EXISTS idx_qst_question ON question_skill_tags(question_id)
            """))
        except:
            pass  # Index may already exist
            
        try:
            db.session.execute(text("""
                CREATE INDEX IF NOT EXISTS idx_qst_skill ON question_skill_tags(skill_tag)
            """))
        except:
            pass
        
        # ILP recommendations table
        db.session.execute(text("""
            CREATE TABLE IF NOT EXISTS ilp_recommendations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                guest_code VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                expires_at TIMESTAMP NOT NULL,
                status VARCHAR(20) DEFAULT 'pending',
                responded_at TIMESTAMP,
                analysis_data TEXT,
                recommendations TEXT,
                modifications TEXT,
                reason_summary TEXT,
                auto_applied BOOLEAN DEFAULT FALSE,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """))
        
        # Indexes for recommendations
        try:
            db.session.execute(text("""
                CREATE INDEX IF NOT EXISTS idx_ilp_rec_user ON ilp_recommendations(user_id)
            """))
        except:
            pass
            
        try:
            db.session.execute(text("""
                CREATE INDEX IF NOT EXISTS idx_ilp_rec_status ON ilp_recommendations(status)
            """))
        except:
            pass
        
        # Modification log table
        db.session.execute(text("""
            CREATE TABLE IF NOT EXISTS ilp_modification_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                recommendation_id INTEGER,
                user_id INTEGER,
                guest_code VARCHAR(50),
                action VARCHAR(30) NOT NULL,
                topic_id VARCHAR(50),
                details TEXT,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                reverted_at TIMESTAMP,
                FOREIGN KEY (recommendation_id) REFERENCES ilp_recommendations(id)
            )
        """))
        
        # Passport weekly plans table (for ILP plan modifications)
        db.session.execute(text("""
            CREATE TABLE IF NOT EXISTS passport_weekly_plans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                guest_code VARCHAR(50),
                topic_id VARCHAR(50) NOT NULL,
                target_level INTEGER DEFAULT 4,
                week_start DATE NOT NULL,
                status VARCHAR(20) DEFAULT 'pending',
                priority INTEGER DEFAULT 0,
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """))
        
        # Indexes for weekly plans
        try:
            db.session.execute(text("""
                CREATE INDEX IF NOT EXISTS idx_pwp_user ON passport_weekly_plans(user_id)
            """))
        except:
            pass
            
        try:
            db.session.execute(text("""
                CREATE INDEX IF NOT EXISTS idx_pwp_guest ON passport_weekly_plans(guest_code)
            """))
        except:
            pass
            
        try:
            db.session.execute(text("""
                CREATE INDEX IF NOT EXISTS idx_pwp_week ON passport_weekly_plans(week_start)
            """))
        except:
            pass
        
        # ILP nightly job log table
        db.session.execute(text("""
            CREATE TABLE IF NOT EXISTS ilp_nightly_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                run_date DATE NOT NULL,
                started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP,
                students_processed INTEGER DEFAULT 0,
                recommendations_created INTEGER DEFAULT 0,
                auto_applied INTEGER DEFAULT 0,
                errors TEXT,
                status VARCHAR(20) DEFAULT 'running'
            )
        """))
        
        db.session.commit()
        print("✅ ILP tables created successfully")
        return True
        
    except Exception as e:
        db.session.rollback()
        print(f"❌ Error creating ILP tables: {e}")
        return False




# =====================================================
# ILP ENGINE - SPRINT 2: ANALYSIS ENGINE
# 12C.1: Data Collection
# 12C.2: Struggle Detection
# 12C.3: Root Cause Inference
# =====================================================

def collect_student_activity(user_id=None, guest_code=None, days=7):
    """
    Collect comprehensive student activity data for analysis.
    Returns structured data about topics attempted, performance, and patterns.
    """
    from sqlalchemy import text
    from datetime import datetime, timedelta
    import json
    
    cutoff_date = datetime.now() - timedelta(days=days)
    
    activity_data = {
        'user_id': user_id,
        'guest_code': guest_code,
        'analysis_period_days': days,
        'analysis_date': datetime.now().isoformat(),
        'topics_attempted': [],
        'current_levels': {},
        'confidence_ratings': {},
        'dormant_topics': [],
        'total_questions': 0,
        'total_correct': 0,
        'overall_accuracy': 0
    }
    
    try:
        # Build user clause
        if user_id:
            user_clause = "user_id = :uid"
            user_params = {'uid': user_id}
        else:
            user_clause = "guest_code = :code"
            user_params = {'code': guest_code}
        
        # 1. Get all adaptive progress (current levels)
        levels_query = db.session.execute(text(f"""
            SELECT topic, current_level, current_points, updated_at
            FROM adaptive_progress
            WHERE {user_clause}
        """), user_params).fetchall()
        
        for row in levels_query:
            activity_data['current_levels'][row[0]] = {
                'level': row[1],
                'points': row[2],
                'last_updated': row[3].isoformat() if row[3] else None
            }
        
        # 2. Get self-assessment ratings from passport
        try:
            ratings_query = db.session.execute(text(f"""
                SELECT topic_id, confidence, updated_at
                FROM passport_self_assessment
                WHERE {user_clause}
            """), user_params).fetchall()
            
            for row in ratings_query:
                activity_data['confidence_ratings'][row[0]] = {
                    'rating': row[1],
                    'updated_at': row[2].isoformat() if row[2] else None
                }
        except Exception as e:
            # Table might not exist yet
            pass
        
        # 3. Get topic-level activity for the analysis period
        params = {**user_params, 'cutoff': cutoff_date}
        
        topics_query = db.session.execute(text(f"""
            SELECT 
                topic,
                COUNT(*) as questions_answered,
                SUM(CASE WHEN is_correct THEN 1 ELSE 0 END) as correct,
                AVG(CASE WHEN time_taken > 0 THEN time_taken ELSE NULL END) as avg_time,
                MIN(answered_at) as first_answer,
                MAX(answered_at) as last_answer
            FROM user_answers
            WHERE {user_clause}
            AND answered_at >= :cutoff
            GROUP BY topic
        """), params).fetchall()
        
        for row in topics_query:
            topic_id = row[0]
            questions = row[1]
            correct = row[2]
            avg_time = row[3]
            
            # Get level from 7 days ago for plateau detection
            level_7_days_ago = get_level_at_date(
                user_id=user_id, 
                guest_code=guest_code, 
                topic_id=topic_id,
                target_date=cutoff_date
            )
            
            current_level = activity_data['current_levels'].get(topic_id, {}).get('level', 0)
            
            # Get skill breakdown for this topic
            skill_breakdown = get_skill_breakdown_for_student(
                user_id=user_id,
                guest_code=guest_code,
                topic_id=topic_id,
                days=days
            )
            
            # Count skipped questions (if tracked)
            skipped = get_skipped_count(user_id, guest_code, topic_id, cutoff_date)
            
            topic_data = {
                'topic_id': topic_id,
                'questions_answered': questions,
                'correct': correct,
                'accuracy': correct / questions if questions > 0 else 0,
                'avg_time_seconds': round(avg_time, 1) if avg_time else None,
                'current_level': current_level,
                'level_7_days_ago': level_7_days_ago,
                'level_change': current_level - level_7_days_ago,
                'skipped': skipped,
                'skip_rate': skipped / (questions + skipped) if (questions + skipped) > 0 else 0,
                'skill_breakdown': skill_breakdown,
                'first_activity': row[4].isoformat() if row[4] else None,
                'last_activity': row[5].isoformat() if row[5] else None
            }
            
            activity_data['topics_attempted'].append(topic_data)
            activity_data['total_questions'] += questions
            activity_data['total_correct'] += correct
        
        # Calculate overall accuracy
        if activity_data['total_questions'] > 0:
            activity_data['overall_accuracy'] = activity_data['total_correct'] / activity_data['total_questions']
        
        # 4. Find dormant topics (have progress but no recent activity)
        for topic_id, level_info in activity_data['current_levels'].items():
            if level_info['level'] > 0:  # Has some progress
                # Check if in topics_attempted
                recently_active = any(t['topic_id'] == topic_id for t in activity_data['topics_attempted'])
                
                if not recently_active and level_info['last_updated']:
                    last_updated = datetime.fromisoformat(level_info['last_updated'].replace('Z', '+00:00')) if isinstance(level_info['last_updated'], str) else level_info['last_updated']
                    days_since = (datetime.now() - last_updated.replace(tzinfo=None)).days
                    
                    if days_since >= ILP_THRESHOLDS['rust_days']:
                        activity_data['dormant_topics'].append({
                            'topic_id': topic_id,
                            'days_since_activity': days_since,
                            'last_level': level_info['level']
                        })
        
    except Exception as e:
        print(f"Error collecting student activity: {e}")
        import traceback
        traceback.print_exc()
    
    return activity_data


def get_level_at_date(user_id=None, guest_code=None, topic_id=None, target_date=None):
    """
    Get the student's level for a topic at a specific date.
    Used for plateau detection.
    """
    from sqlalchemy import text
    
    try:
        if user_id:
            user_clause = "user_id = :uid"
            params = {'uid': user_id, 'topic': topic_id, 'date': target_date}
        else:
            user_clause = "guest_code = :code"
            params = {'code': guest_code, 'topic': topic_id, 'date': target_date}
        
        # Try to get from history table if it exists
        try:
            result = db.session.execute(text(f"""
                SELECT level FROM adaptive_progress_history
                WHERE {user_clause} AND topic = :topic
                AND recorded_at <= :date
                ORDER BY recorded_at DESC
                LIMIT 1
            """), params).fetchone()
            
            if result:
                return result[0]
        except:
            pass  # History table might not exist
        
        # Fallback: return current level (assumes no change if no history)
        result = db.session.execute(text(f"""
            SELECT current_level FROM adaptive_progress
            WHERE {user_clause} AND topic = :topic
        """), params).fetchone()
        
        return result[0] if result else 0
        
    except Exception as e:
        print(f"Error getting level at date: {e}")
        return 0


def get_skipped_count(user_id, guest_code, topic_id, cutoff_date):
    """
    Get count of skipped questions for a topic.
    Returns 0 if skip tracking isn't implemented.
    """
    from sqlalchemy import text
    
    try:
        if user_id:
            user_clause = "user_id = :uid"
            params = {'uid': user_id, 'topic': topic_id, 'cutoff': cutoff_date}
        else:
            user_clause = "guest_code = :code"
            params = {'code': guest_code, 'topic': topic_id, 'cutoff': cutoff_date}
        
        # Check if we have a skipped column or table
        result = db.session.execute(text(f"""
            SELECT COUNT(*) FROM user_answers
            WHERE {user_clause} AND topic = :topic
            AND answered_at >= :cutoff
            AND (skipped = 1 OR answer = '' OR answer IS NULL)
        """), params).fetchone()
        
        return result[0] if result else 0
        
    except:
        # Skipped tracking might not be implemented
        return 0


def detect_struggles(activity_data):
    """
    Detect various types of struggles from activity data.
    Returns list of struggle signals for each topic.
    """
    struggles = []
    thresholds = ILP_THRESHOLDS
    
    for topic in activity_data['topics_attempted']:
        topic_id = topic['topic_id']
        signals = []
        
        # Signal 1: LOW ACCURACY
        if topic['questions_answered'] >= thresholds['min_questions_for_signal']:
            if topic['accuracy'] < thresholds['critical_accuracy']:
                signals.append({
                    'type': 'low_accuracy',
                    'severity': 'critical',
                    'value': topic['accuracy'],
                    'threshold': thresholds['critical_accuracy'],
                    'detail': f"Only {topic['accuracy']*100:.0f}% correct over {topic['questions_answered']} questions",
                    'questions': topic['questions_answered']
                })
            elif topic['accuracy'] < thresholds['low_accuracy']:
                signals.append({
                    'type': 'low_accuracy',
                    'severity': 'high',
                    'value': topic['accuracy'],
                    'threshold': thresholds['low_accuracy'],
                    'detail': f"{topic['accuracy']*100:.0f}% correct over {topic['questions_answered']} questions",
                    'questions': topic['questions_answered']
                })
        
        # Signal 2: PLATEAU (stuck at level)
        if (topic['questions_answered'] >= thresholds['plateau_min_questions'] and 
            topic['level_change'] == 0 and 
            topic['current_level'] > 0 and
            topic['current_level'] < 12):  # Not already mastered
            signals.append({
                'type': 'plateau',
                'severity': 'medium',
                'value': topic['current_level'],
                'detail': f"Stuck at Level {topic['current_level']} despite {topic['questions_answered']} questions",
                'questions': topic['questions_answered']
            })
        
        # Signal 3: SKILL GAPS (specific weak skills)
        for skill_tag, stats in topic.get('skill_breakdown', {}).items():
            if stats['total'] >= 5:  # Need enough data
                if stats['accuracy'] < thresholds['numeracy_trigger']:
                    # Check if this is a numeracy skill
                    is_numeracy = skill_tag in ILP_SKILL_TO_NUMERACY
                    
                    signals.append({
                        'type': 'skill_gap',
                        'severity': 'critical' if is_numeracy and stats['accuracy'] < 0.3 else 'high',
                        'skill': skill_tag,
                        'is_numeracy_skill': is_numeracy,
                        'value': stats['accuracy'],
                        'threshold': thresholds['numeracy_trigger'],
                        'detail': f"{skill_tag}: {stats['accuracy']*100:.0f}% ({stats['correct']}/{stats['total']})",
                        'remedial_topics': ILP_SKILL_TO_NUMERACY.get(skill_tag, [])
                    })
        
        # Signal 4: HIGH SKIP RATE (avoidance)
        if topic['skip_rate'] > thresholds['skip_rate_threshold']:
            signals.append({
                'type': 'avoidance',
                'severity': 'medium',
                'value': topic['skip_rate'],
                'threshold': thresholds['skip_rate_threshold'],
                'detail': f"Skipping {topic['skip_rate']*100:.0f}% of questions",
                'skipped': topic['skipped']
            })
        
        # Signal 5: CONFIDENCE MISMATCH
        confidence = activity_data['confidence_ratings'].get(topic_id, {}).get('rating', 0)
        if confidence > 0:
            # Map confidence (1-5) to expected level range
            expected_level_min = (confidence - 1) * 3  # 1→0, 2→3, 3→6, 4→9, 5→12
            actual_level = topic['current_level']
            
            if confidence >= 4 and actual_level < expected_level_min - 2:
                signals.append({
                    'type': 'confidence_mismatch',
                    'severity': 'medium',
                    'confidence_rating': confidence,
                    'actual_level': actual_level,
                    'expected_min': expected_level_min,
                    'gap': expected_level_min - actual_level,
                    'detail': f"Rated self {confidence}/5 but at Level {actual_level}"
                })
        
        if signals:
            # Determine overall severity
            severity_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
            overall_severity = min(signals, key=lambda s: severity_order.get(s['severity'], 3))['severity']
            
            struggles.append({
                'topic_id': topic_id,
                'signals': signals,
                'signal_count': len(signals),
                'overall_severity': overall_severity,
                'current_level': topic['current_level'],
                'accuracy': topic['accuracy'],
                'questions_answered': topic['questions_answered']
            })
    
    # Sort by severity (critical first)
    severity_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
    struggles.sort(key=lambda s: severity_order.get(s['overall_severity'], 3))
    
    return struggles


def detect_dormant_topics(activity_data):
    """
    Detect topics that need spaced repetition (rust alerts).
    """
    rust_alerts = []
    threshold_days = ILP_THRESHOLDS['rust_days']
    
    for dormant in activity_data['dormant_topics']:
        rust_alerts.append({
            'type': 'rust_alert',
            'severity': 'low',
            'topic_id': dormant['topic_id'],
            'days_since_activity': dormant['days_since_activity'],
            'last_level': dormant['last_level'],
            'detail': f"No practice for {dormant['days_since_activity']} days (was at Level {dormant['last_level']})"
        })
    
    return rust_alerts


def infer_root_causes(struggles, activity_data):
    """
    Infer root causes of struggles and generate recommendations.
    This is the "brain" of the ILP engine.
    """
    recommendations = []
    current_levels = activity_data['current_levels']
    
    # Track topics already recommended to avoid duplicates
    topics_already_recommended = set()
    
    for struggle in struggles:
        topic_id = struggle['topic_id']
        
        # 1. CHECK PREREQUISITE GAPS
        prereqs = get_prerequisites_for_topic(topic_id)
        weak_prereqs = []
        untested_prereqs = []
        
        for prereq in prereqs:
            prereq_level = current_levels.get(prereq, {}).get('level', 0)
            
            if prereq_level == 0:
                untested_prereqs.append(prereq)
            elif prereq_level < ILP_THRESHOLDS['bronze_level']:
                weak_prereqs.append({
                    'topic_id': prereq,
                    'current_level': prereq_level,
                    'gap_to_bronze': ILP_THRESHOLDS['bronze_level'] - prereq_level
                })
        
        # 2. CHECK NUMERACY NEEDS
        numeracy_topics_needed = set()
        weak_numeracy_skills = []
        
        for signal in struggle['signals']:
            if signal['type'] == 'skill_gap' and signal.get('is_numeracy_skill'):
                weak_numeracy_skills.append(signal)
                for remedial in signal.get('remedial_topics', []):
                    numeracy_topics_needed.add(remedial)
        
        # 3. GENERATE RECOMMENDATIONS
        
        # Priority A: Critical numeracy gaps
        if weak_numeracy_skills:
            for numeracy_topic in numeracy_topics_needed:
                if numeracy_topic not in topics_already_recommended:
                    topic_level = current_levels.get(numeracy_topic, {}).get('level', 0)
                    
                    recommendations.append({
                        'type': 'insert_numeracy',
                        'priority': 'critical' if any(s['severity'] == 'critical' for s in weak_numeracy_skills) else 'high',
                        'topic_to_add': numeracy_topic,
                        'current_level': topic_level,
                        'target_level': max(ILP_THRESHOLDS['bronze_level'], topic_level + 2),
                        'struggling_topic': topic_id,
                        'reason': f"Numeracy skill gaps affecting {format_topic_name(topic_id)}",
                        'detail': f"Weak skills: {', '.join(s['skill'] for s in weak_numeracy_skills)}",
                        'evidence': weak_numeracy_skills
                    })
                    topics_already_recommended.add(numeracy_topic)
        
        # Priority B: Weak prerequisites
        if weak_prereqs:
            for prereq in weak_prereqs:
                prereq_id = prereq['topic_id']
                if prereq_id not in topics_already_recommended:
                    recommendations.append({
                        'type': 'insert_prerequisite',
                        'priority': 'high',
                        'topic_to_add': prereq_id,
                        'current_level': prereq['current_level'],
                        'target_level': ILP_THRESHOLDS['bronze_level'],
                        'struggling_topic': topic_id,
                        'reason': f"Foundation gap in {format_topic_name(prereq_id)}",
                        'detail': f"At Level {prereq['current_level']}, need Level {ILP_THRESHOLDS['bronze_level']} before continuing {format_topic_name(topic_id)}",
                        'evidence': {'gap_to_bronze': prereq['gap_to_bronze']}
                    })
                    topics_already_recommended.add(prereq_id)
        
        # Priority C: Untested prerequisites (need diagnostic)
        if untested_prereqs and not weak_prereqs and not weak_numeracy_skills:
            recommendations.append({
                'type': 'diagnostic_quiz',
                'priority': 'medium',
                'topics_to_test': untested_prereqs[:3],  # Limit to 3
                'struggling_topic': topic_id,
                'reason': f"Untested foundations for {format_topic_name(topic_id)}",
                'detail': f"Never assessed: {', '.join(format_topic_name(t) for t in untested_prereqs[:3])}",
                'evidence': {'untested_count': len(untested_prereqs)}
            })
        
        # Priority D: No prereq gaps - needs consolidation
        if not weak_prereqs and not untested_prereqs and not weak_numeracy_skills:
            # Check if it's a plateau vs low accuracy
            has_plateau = any(s['type'] == 'plateau' for s in struggle['signals'])
            has_low_accuracy = any(s['type'] == 'low_accuracy' for s in struggle['signals'])
            
            if has_plateau or has_low_accuracy:
                recommendations.append({
                    'type': 'extend_practice',
                    'priority': 'medium',
                    'topic': topic_id,
                    'current_level': struggle['current_level'],
                    'reason': f"More practice needed on {format_topic_name(topic_id)}",
                    'detail': f"Foundations OK but {'stuck at Level ' + str(struggle['current_level']) if has_plateau else 'accuracy at ' + str(round(struggle['accuracy']*100)) + '%'}",
                    'evidence': struggle['signals']
                })
    
    # 4. ADD RUST ALERTS (lower priority)
    rust_alerts = detect_dormant_topics(activity_data)
    for alert in rust_alerts:
        if alert['topic_id'] not in topics_already_recommended:
            recommendations.append({
                'type': 'spaced_repetition',
                'priority': 'low',
                'topic': alert['topic_id'],
                'days_inactive': alert['days_since_activity'],
                'last_level': alert['last_level'],
                'reason': f"Refresher needed for {format_topic_name(alert['topic_id'])}",
                'detail': alert['detail'],
                'evidence': alert
            })
    
    # Sort by priority
    priority_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
    recommendations.sort(key=lambda r: priority_order.get(r['priority'], 3))
    
    return recommendations


def format_topic_name(topic_id):
    """Convert topic_id to display name"""
    return topic_id.replace('_', ' ').title()


def run_full_analysis(user_id=None, guest_code=None, days=7):
    """
    Run complete ILP analysis for a student.
    This is the main entry point for the nightly job.
    """
    from datetime import datetime
    import json
    
    analysis_result = {
        'user_id': user_id,
        'guest_code': guest_code,
        'analysis_date': datetime.now().isoformat(),
        'period_days': days,
        'activity_summary': {},
        'struggles': [],
        'recommendations': [],
        'has_recommendations': False
    }
    
    try:
        # Step 1: Collect activity data
        activity_data = collect_student_activity(
            user_id=user_id,
            guest_code=guest_code,
            days=days
        )
        
        analysis_result['activity_summary'] = {
            'topics_attempted': len(activity_data['topics_attempted']),
            'total_questions': activity_data['total_questions'],
            'overall_accuracy': round(activity_data['overall_accuracy'], 3),
            'dormant_topics': len(activity_data['dormant_topics']),
            'topics_with_progress': len(activity_data['current_levels'])
        }
        
        # Step 2: Detect struggles
        struggles = detect_struggles(activity_data)
        analysis_result['struggles'] = struggles
        
        # Step 3: Infer root causes and generate recommendations
        if struggles or activity_data['dormant_topics']:
            recommendations = infer_root_causes(struggles, activity_data)
            analysis_result['recommendations'] = recommendations
            analysis_result['has_recommendations'] = len(recommendations) > 0
        
        # Step 4: Generate human-readable summary
        analysis_result['summary'] = generate_analysis_summary(analysis_result)
        
    except Exception as e:
        print(f"Error in full analysis: {e}")
        import traceback
        traceback.print_exc()
        analysis_result['error'] = str(e)
    
    return analysis_result


def generate_analysis_summary(analysis_result):
    """
    Generate human-readable summary of analysis for student notification.
    """
    lines = []
    
    # Activity summary
    summary = analysis_result.get('activity_summary', {})
    if summary.get('total_questions', 0) > 0:
        lines.append(f"📊 In the past {analysis_result['period_days']} days, you answered {summary['total_questions']} questions across {summary['topics_attempted']} topics with {summary['overall_accuracy']*100:.0f}% accuracy.")
    else:
        lines.append(f"📊 No activity detected in the past {analysis_result['period_days']} days.")
    
    # Struggles found
    struggles = analysis_result.get('struggles', [])
    if struggles:
        critical_count = sum(1 for s in struggles if s['overall_severity'] == 'critical')
        high_count = sum(1 for s in struggles if s['overall_severity'] == 'high')
        
        if critical_count > 0:
            lines.append(f"🚨 Found {critical_count} critical area(s) needing immediate attention.")
        if high_count > 0:
            lines.append(f"⚠️ Found {high_count} area(s) where you're struggling.")
    
    # Recommendations
    recs = analysis_result.get('recommendations', [])
    if recs:
        numeracy_recs = [r for r in recs if r['type'] == 'insert_numeracy']
        prereq_recs = [r for r in recs if r['type'] == 'insert_prerequisite']
        practice_recs = [r for r in recs if r['type'] == 'extend_practice']
        
        if numeracy_recs:
            topics = [r['topic_to_add'] for r in numeracy_recs]
            lines.append(f"🔢 Recommended numeracy strengthening: {', '.join(format_topic_name(t) for t in topics[:3])}")
        
        if prereq_recs:
            topics = [r['topic_to_add'] for r in prereq_recs]
            lines.append(f"📚 Foundation topics to add: {', '.join(format_topic_name(t) for t in topics[:3])}")
        
        if practice_recs:
            topics = [r['topic'] for r in practice_recs]
            lines.append(f"💪 More practice suggested for: {', '.join(format_topic_name(t) for t in topics[:3])}")
    else:
        lines.append("✅ No issues detected - keep up the great work!")
    
    return '\n'.join(lines)


# =====================================================
# ILP ENGINE - SPRINT 2 API ENDPOINTS
# =====================================================

@passport_bp.route('/api/ilp/analyse', methods=['GET', 'POST'])
@guest_or_login_required
def run_ilp_analysis_endpoint():
    """Run ILP analysis for current user"""
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    days = int(request.args.get('days', 7))
    
    result = run_full_analysis(
        user_id=user_id,
        guest_code=guest_code,
        days=days
    )
    
    return jsonify({
        'success': True,
        **result
    })


@passport_bp.route('/api/ilp/struggles', methods=['GET'])
@guest_or_login_required
def get_ilp_struggles():
    """Get detected struggles for current user"""
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    days = int(request.args.get('days', 7))
    
    # Collect and analyse
    activity_data = collect_student_activity(
        user_id=user_id,
        guest_code=guest_code,
        days=days
    )
    
    struggles = detect_struggles(activity_data)
    
    return jsonify({
        'success': True,
        'days': days,
        'struggle_count': len(struggles),
        'struggles': struggles,
        'activity_summary': {
            'topics_attempted': len(activity_data['topics_attempted']),
            'total_questions': activity_data['total_questions'],
            'overall_accuracy': round(activity_data['overall_accuracy'], 3)
        }
    })


@passport_bp.route('/api/ilp/recommendations', methods=['GET'])
@guest_or_login_required
def get_ilp_recommendations():
    """Get ILP recommendations for current user"""
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    days = int(request.args.get('days', 7))
    
    result = run_full_analysis(
        user_id=user_id,
        guest_code=guest_code,
        days=days
    )
    
    return jsonify({
        'success': True,
        'days': days,
        'has_recommendations': result['has_recommendations'],
        'recommendation_count': len(result['recommendations']),
        'recommendations': result['recommendations'],
        'summary': result.get('summary', ''),
        'struggles_found': len(result['struggles'])
    })


@passport_bp.route('/api/ilp/activity-summary', methods=['GET'])
@guest_or_login_required
def get_ilp_activity_summary():
    """Get activity summary for current user"""
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    days = int(request.args.get('days', 7))
    
    activity_data = collect_student_activity(
        user_id=user_id,
        guest_code=guest_code,
        days=days
    )
    
    return jsonify({
        'success': True,
        'days': days,
        'topics_attempted': activity_data['topics_attempted'],
        'current_levels': activity_data['current_levels'],
        'dormant_topics': activity_data['dormant_topics'],
        'total_questions': activity_data['total_questions'],
        'total_correct': activity_data['total_correct'],
        'overall_accuracy': round(activity_data['overall_accuracy'], 3)
    })


# =====================================================
# ILP ENGINE - SPRINT 3: PLAN MODIFICATION & NOTIFICATIONS
# 12D: Plan Modification Logic
# 12E: Student Notification & Approval System
# =====================================================

def get_current_weekly_plan(user_id=None, guest_code=None):
    """
    Get the student's current weekly plan from passport_weekly_plans.
    Returns list of planned topics with their target levels.
    """
    from sqlalchemy import text
    from datetime import datetime, timedelta
    
    try:
        # Get current week boundaries
        today = datetime.now().date()
        week_start = today - timedelta(days=today.weekday())  # Monday
        week_end = week_start + timedelta(days=6)  # Sunday
        
        if user_id:
            user_clause = "user_id = :uid"
            params = {'uid': user_id, 'week_start': week_start, 'week_end': week_end}
        else:
            user_clause = "guest_code = :code"
            params = {'code': guest_code, 'week_start': week_start, 'week_end': week_end}
        
        # Try to get from passport_weekly_plans
        results = db.session.execute(text(f"""
            SELECT topic_id, target_level, status, week_start, priority
            FROM passport_weekly_plans
            WHERE {user_clause}
            AND week_start >= :week_start
            AND week_start <= :week_end
            ORDER BY priority ASC, topic_id
        """), params).fetchall()
        
        plan = []
        for row in results:
            plan.append({
                'topic_id': row[0],
                'target_level': row[1],
                'status': row[2],
                'week_start': row[3].isoformat() if row[3] else None,
                'priority': row[4] if len(row) > 4 else 0
            })
        
        return plan
        
    except Exception as e:
        print(f"Error getting weekly plan: {e}")
        return []


def generate_plan_modifications(recommendations, current_plan, max_topics=3):
    """
    Generate specific plan modifications based on recommendations.
    Respects max_topics limit (default 2-3 per week).
    """
    from datetime import datetime, timedelta
    
    modifications = []
    current_topic_ids = [p['topic_id'] for p in current_plan]
    topics_to_add = []
    topics_to_delay = []
    
    # Count current active topics
    active_count = len([p for p in current_plan if p.get('status') != 'completed'])
    
    # Process recommendations by priority
    for rec in recommendations:
        rec_type = rec['type']
        
        if rec_type in ['insert_numeracy', 'insert_prerequisite']:
            topic_to_add = rec['topic_to_add']
            
            # Skip if already in plan
            if topic_to_add in current_topic_ids:
                continue
            
            # Check if we need to make room
            if active_count + len(topics_to_add) >= max_topics:
                # Find lowest priority topic to delay (not the one we're struggling with)
                for existing in reversed(current_plan):
                    if (existing['topic_id'] not in [r.get('struggling_topic') for r in recommendations] and
                        existing['topic_id'] not in topics_to_delay and
                        existing.get('status') != 'completed'):
                        topics_to_delay.append(existing['topic_id'])
                        break
            
            topics_to_add.append({
                'topic_id': topic_to_add,
                'target_level': rec.get('target_level', ILP_THRESHOLDS['bronze_level']),
                'priority': 'critical' if rec['priority'] == 'critical' else 'high',
                'reason': rec['reason'],
                'because_of': rec.get('struggling_topic')
            })
        
        elif rec_type == 'extend_practice':
            # Find the topic in current plan and mark for extension
            topic_id = rec['topic']
            if topic_id in current_topic_ids:
                modifications.append({
                    'action': 'extend',
                    'topic_id': topic_id,
                    'extra_sessions': 2,
                    'reason': rec['reason'],
                    'priority': rec['priority']
                })
        
        elif rec_type == 'diagnostic_quiz':
            # Add diagnostic quizzes (these don't count toward topic limit)
            for topic in rec.get('topics_to_test', [])[:2]:  # Limit to 2 diagnostics
                modifications.append({
                    'action': 'diagnostic',
                    'topic_id': topic,
                    'questions': 10,
                    'reason': rec['reason'],
                    'priority': rec['priority']
                })
    
    # Convert to modifications list
    for topic in topics_to_add:
        modifications.append({
            'action': 'add',
            'topic_id': topic['topic_id'],
            'target_level': topic['target_level'],
            'reason': topic['reason'],
            'because_of': topic.get('because_of'),
            'priority': topic['priority']
        })
    
    for topic_id in topics_to_delay:
        modifications.append({
            'action': 'delay',
            'topic_id': topic_id,
            'delay_weeks': 1,
            'reason': 'Making room for foundation work',
            'priority': 'medium'
        })
    
    return modifications


def apply_plan_modifications(user_id=None, guest_code=None, modifications=None, recommendation_id=None):
    """
    Apply plan modifications to the student's weekly plan.
    Returns list of applied changes.
    """
    from sqlalchemy import text
    from datetime import datetime, timedelta
    import json
    
    applied = []
    today = datetime.now().date()
    week_start = today - timedelta(days=today.weekday())
    next_week_start = week_start + timedelta(days=7)
    
    try:
        for mod in modifications:
            action = mod['action']
            topic_id = mod.get('topic_id')
            
            if user_id:
                user_clause = "user_id = :uid"
                params = {'uid': user_id}
            else:
                user_clause = "guest_code = :code"
                params = {'code': guest_code}
            
            if action == 'add':
                # Insert new topic into this week's plan
                params.update({
                    'topic': topic_id,
                    'target': mod.get('target_level', 4),
                    'week': week_start,
                    'priority': 0 if mod.get('priority') == 'critical' else 1
                })
                
                # Check if already exists
                existing = db.session.execute(text(f"""
                    SELECT id FROM passport_weekly_plans
                    WHERE {user_clause} AND topic_id = :topic AND week_start = :week
                """), params).fetchone()
                
                if not existing:
                    if user_id:
                        db.session.execute(text("""
                            INSERT INTO passport_weekly_plans 
                            (user_id, topic_id, target_level, week_start, status, priority, created_at)
                            VALUES (:uid, :topic, :target, :week, 'pending', :priority, CURRENT_TIMESTAMP)
                        """), params)
                    else:
                        db.session.execute(text("""
                            INSERT INTO passport_weekly_plans 
                            (guest_code, topic_id, target_level, week_start, status, priority, created_at)
                            VALUES (:code, :topic, :target, :week, 'pending', :priority, CURRENT_TIMESTAMP)
                        """), params)
                    
                    applied.append({
                        'action': 'added',
                        'topic_id': topic_id,
                        'target_level': mod.get('target_level', 4),
                        'week': week_start.isoformat()
                    })
            
            elif action == 'delay':
                # Move topic to next week
                params.update({
                    'topic': topic_id,
                    'week': week_start,
                    'next_week': next_week_start
                })
                
                db.session.execute(text(f"""
                    UPDATE passport_weekly_plans
                    SET week_start = :next_week, status = 'delayed'
                    WHERE {user_clause} AND topic_id = :topic AND week_start = :week
                """), params)
                
                applied.append({
                    'action': 'delayed',
                    'topic_id': topic_id,
                    'to_week': next_week_start.isoformat()
                })
            
            elif action == 'extend':
                # Mark topic for extended practice (update notes/status)
                params.update({'topic': topic_id, 'week': week_start})
                
                db.session.execute(text(f"""
                    UPDATE passport_weekly_plans
                    SET status = 'extended', notes = 'ILP: Extended practice recommended'
                    WHERE {user_clause} AND topic_id = :topic AND week_start = :week
                """), params)
                
                applied.append({
                    'action': 'extended',
                    'topic_id': topic_id
                })
            
            # Log the modification
            log_params = {
                'rec_id': recommendation_id,
                'action': action,
                'topic': topic_id,
                'details': json.dumps(mod)
            }
            
            if user_id:
                log_params['uid'] = user_id
                db.session.execute(text("""
                    INSERT INTO ilp_modification_log 
                    (recommendation_id, user_id, action, topic_id, details)
                    VALUES (:rec_id, :uid, :action, :topic, :details)
                """), log_params)
            else:
                log_params['code'] = guest_code
                db.session.execute(text("""
                    INSERT INTO ilp_modification_log 
                    (recommendation_id, guest_code, action, topic_id, details)
                    VALUES (:rec_id, :code, :action, :topic, :details)
                """), log_params)
        
        db.session.commit()
        
    except Exception as e:
        db.session.rollback()
        print(f"Error applying modifications: {e}")
        import traceback
        traceback.print_exc()
        return []
    
    return applied


def create_recommendation_notification(user_id=None, guest_code=None, analysis_result=None):
    """
    Create a pending recommendation notification for the student.
    Returns the recommendation ID.
    """
    from sqlalchemy import text
    from datetime import datetime, timedelta
    import json
    
    if not analysis_result or not analysis_result.get('has_recommendations'):
        return None
    
    try:
        # Determine expiry based on highest priority
        priorities = [r['priority'] for r in analysis_result['recommendations']]
        if 'critical' in priorities or 'high' in priorities:
            expire_hours = ILP_THRESHOLDS['auto_apply_hours']  # 24 hours
        else:
            expire_hours = 48  # 48 hours for lower priority
        
        expires_at = datetime.now() + timedelta(hours=expire_hours)
        
        # Get current plan for modification planning
        current_plan = get_current_weekly_plan(user_id=user_id, guest_code=guest_code)
        
        # Generate modifications
        modifications = generate_plan_modifications(
            analysis_result['recommendations'],
            current_plan,
            max_topics=ILP_THRESHOLDS['max_weekly_topics']
        )
        
        # Create the notification record
        if user_id:
            result = db.session.execute(text("""
                INSERT INTO ilp_recommendations 
                (user_id, expires_at, status, analysis_data, recommendations, modifications, reason_summary)
                VALUES (:uid, :expires, 'pending', :analysis, :recs, :mods, :summary)
            """), {
                'uid': user_id,
                'expires': expires_at,
                'analysis': json.dumps(analysis_result.get('activity_summary', {})),
                'recs': json.dumps(analysis_result['recommendations']),
                'mods': json.dumps(modifications),
                'summary': analysis_result.get('summary', '')
            })
        else:
            result = db.session.execute(text("""
                INSERT INTO ilp_recommendations 
                (guest_code, expires_at, status, analysis_data, recommendations, modifications, reason_summary)
                VALUES (:code, :expires, 'pending', :analysis, :recs, :mods, :summary)
            """), {
                'code': guest_code,
                'expires': expires_at,
                'analysis': json.dumps(analysis_result.get('activity_summary', {})),
                'recs': json.dumps(analysis_result['recommendations']),
                'mods': json.dumps(modifications),
                'summary': analysis_result.get('summary', '')
            })
        
        db.session.commit()
        
        # Get the inserted ID
        if user_id:
            rec = db.session.execute(text("""
                SELECT id FROM ilp_recommendations 
                WHERE user_id = :uid ORDER BY created_at DESC LIMIT 1
            """), {'uid': user_id}).fetchone()
        else:
            rec = db.session.execute(text("""
                SELECT id FROM ilp_recommendations 
                WHERE guest_code = :code ORDER BY created_at DESC LIMIT 1
            """), {'code': guest_code}).fetchone()
        
        return rec[0] if rec else None
        
    except Exception as e:
        db.session.rollback()
        print(f"Error creating recommendation notification: {e}")
        import traceback
        traceback.print_exc()
        return None


def get_pending_recommendations(user_id=None, guest_code=None):
    """
    Get all pending recommendation notifications for a student.
    """
    from sqlalchemy import text
    from datetime import datetime
    import json
    
    try:
        if user_id:
            user_clause = "user_id = :uid"
            params = {'uid': user_id}
        else:
            user_clause = "guest_code = :code"
            params = {'code': guest_code}
        
        results = db.session.execute(text(f"""
            SELECT id, created_at, expires_at, status, analysis_data, 
                   recommendations, modifications, reason_summary
            FROM ilp_recommendations
            WHERE {user_clause} AND status = 'pending'
            ORDER BY created_at DESC
        """), params).fetchall()
        
        pending = []
        now = datetime.now()
        
        for row in results:
            # Handle expires_at which might be string or datetime
            expires_at = row[2]
            if expires_at:
                if isinstance(expires_at, str):
                    try:
                        expires_at = datetime.fromisoformat(expires_at.replace('Z', '+00:00'))
                    except:
                        expires_at = datetime.strptime(expires_at, '%Y-%m-%d %H:%M:%S')
                time_remaining = (expires_at - now).total_seconds()
            else:
                time_remaining = 0
            hours_remaining = max(0, time_remaining / 3600)
            
            # Handle created_at which might be string or datetime
            created_at = row[1]
            if created_at and isinstance(created_at, str):
                try:
                    created_at = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                except:
                    try:
                        created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
                    except:
                        pass
            
            pending.append({
                'id': row[0],
                'created_at': created_at.isoformat() if hasattr(created_at, 'isoformat') else created_at,
                'expires_at': expires_at.isoformat() if hasattr(expires_at, 'isoformat') else expires_at,
                'hours_remaining': round(hours_remaining, 1),
                'status': row[3],
                'analysis_data': json.loads(row[4]) if row[4] else {},
                'recommendations': json.loads(row[5]) if row[5] else [],
                'modifications': json.loads(row[6]) if row[6] else [],
                'reason_summary': row[7]
            })
        
        return pending
        
    except Exception as e:
        print(f"Error getting pending recommendations: {e}")
        import traceback
        traceback.print_exc()
        return []


def accept_recommendation(recommendation_id, user_id=None, guest_code=None):
    """
    Accept and apply a recommendation.
    """
    from sqlalchemy import text
    from datetime import datetime
    import json
    
    try:
        # Get the recommendation
        if user_id:
            user_clause = "user_id = :uid"
            params = {'uid': user_id, 'rec_id': recommendation_id}
        else:
            user_clause = "guest_code = :code"
            params = {'code': guest_code, 'rec_id': recommendation_id}
        
        rec = db.session.execute(text(f"""
            SELECT id, modifications, status FROM ilp_recommendations
            WHERE id = :rec_id AND {user_clause}
        """), params).fetchone()
        
        if not rec:
            return {'success': False, 'error': 'Recommendation not found'}
        
        if rec[2] != 'pending':
            return {'success': False, 'error': f'Recommendation already {rec[2]}'}
        
        modifications = json.loads(rec[1]) if rec[1] else []
        
        # Apply the modifications
        applied = apply_plan_modifications(
            user_id=user_id,
            guest_code=guest_code,
            modifications=modifications,
            recommendation_id=recommendation_id
        )
        
        # Update status
        db.session.execute(text(f"""
            UPDATE ilp_recommendations
            SET status = 'accepted', responded_at = CURRENT_TIMESTAMP
            WHERE id = :rec_id AND {user_clause}
        """), params)
        
        db.session.commit()
        
        return {
            'success': True,
            'applied': applied,
            'modifications_count': len(applied)
        }
        
    except Exception as e:
        db.session.rollback()
        print(f"Error accepting recommendation: {e}")
        return {'success': False, 'error': str(e)}


def reject_recommendation(recommendation_id, user_id=None, guest_code=None):
    """
    Reject a recommendation (no changes applied).
    """
    from sqlalchemy import text
    
    try:
        if user_id:
            user_clause = "user_id = :uid"
            params = {'uid': user_id, 'rec_id': recommendation_id}
        else:
            user_clause = "guest_code = :code"
            params = {'code': guest_code, 'rec_id': recommendation_id}
        
        db.session.execute(text(f"""
            UPDATE ilp_recommendations
            SET status = 'rejected', responded_at = CURRENT_TIMESTAMP
            WHERE id = :rec_id AND {user_clause} AND status = 'pending'
        """), params)
        
        db.session.commit()
        
        return {'success': True}
        
    except Exception as e:
        db.session.rollback()
        print(f"Error rejecting recommendation: {e}")
        return {'success': False, 'error': str(e)}


def auto_apply_expired_recommendations():
    """
    Auto-apply any pending recommendations that have expired.
    Called by nightly job.
    """
    from sqlalchemy import text
    from datetime import datetime
    import json
    
    applied_count = 0
    
    try:
        # Find all expired pending recommendations
        now = datetime.now()
        
        expired = db.session.execute(text("""
            SELECT id, user_id, guest_code, modifications
            FROM ilp_recommendations
            WHERE status = 'pending' AND expires_at <= :now
        """), {'now': now}).fetchall()
        
        for rec in expired:
            rec_id = rec[0]
            user_id = rec[1]
            guest_code = rec[2]
            modifications = json.loads(rec[3]) if rec[3] else []
            
            if modifications:
                # Apply modifications
                applied = apply_plan_modifications(
                    user_id=user_id,
                    guest_code=guest_code,
                    modifications=modifications,
                    recommendation_id=rec_id
                )
                
                if applied:
                    applied_count += 1
            
            # Update status
            db.session.execute(text("""
                UPDATE ilp_recommendations
                SET status = 'auto_applied', auto_applied = TRUE, responded_at = CURRENT_TIMESTAMP
                WHERE id = :rec_id
            """), {'rec_id': rec_id})
        
        db.session.commit()
        
    except Exception as e:
        db.session.rollback()
        print(f"Error auto-applying recommendations: {e}")
    
    return applied_count


def get_recommendation_history(user_id=None, guest_code=None, limit=20):
    """
    Get history of past recommendations for a student.
    """
    from sqlalchemy import text
    import json
    
    try:
        if user_id:
            user_clause = "user_id = :uid"
            params = {'uid': user_id, 'limit': limit}
        else:
            user_clause = "guest_code = :code"
            params = {'code': guest_code, 'limit': limit}
        
        results = db.session.execute(text(f"""
            SELECT id, created_at, expires_at, status, responded_at,
                   reason_summary, auto_applied
            FROM ilp_recommendations
            WHERE {user_clause}
            ORDER BY created_at DESC
            LIMIT :limit
        """), params).fetchall()
        
        history = []
        for row in results:
            history.append({
                'id': row[0],
                'created_at': row[1].isoformat() if row[1] else None,
                'expires_at': row[2].isoformat() if row[2] else None,
                'status': row[3],
                'responded_at': row[4].isoformat() if row[4] else None,
                'reason_summary': row[5],
                'auto_applied': row[6]
            })
        
        return history
        
    except Exception as e:
        print(f"Error getting recommendation history: {e}")
        return []


# =====================================================
# ILP ENGINE - SPRINT 3 API ENDPOINTS
# =====================================================

@passport_bp.route('/api/ilp/pending', methods=['GET'])
@guest_or_login_required
def get_ilp_pending():
    """Get pending recommendations for current user"""
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    pending = get_pending_recommendations(user_id=user_id, guest_code=guest_code)
    
    return jsonify({
        'success': True,
        'pending_count': len(pending),
        'pending': pending
    })


@passport_bp.route('/api/ilp/accept/<int:rec_id>', methods=['POST'])
@guest_or_login_required
def accept_ilp_recommendation(rec_id):
    """Accept and apply a recommendation"""
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    result = accept_recommendation(rec_id, user_id=user_id, guest_code=guest_code)
    
    return jsonify(result)


@passport_bp.route('/api/ilp/reject/<int:rec_id>', methods=['POST'])
@guest_or_login_required
def reject_ilp_recommendation(rec_id):
    """Reject a recommendation"""
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    result = reject_recommendation(rec_id, user_id=user_id, guest_code=guest_code)
    
    return jsonify(result)


@passport_bp.route('/api/ilp/history', methods=['GET'])
@guest_or_login_required
def get_ilp_history():
    """Get recommendation history"""
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    limit = int(request.args.get('limit', 20))
    
    history = get_recommendation_history(user_id=user_id, guest_code=guest_code, limit=limit)
    
    return jsonify({
        'success': True,
        'count': len(history),
        'history': history
    })


@passport_bp.route('/api/ilp/create-notification', methods=['POST'])
@guest_or_login_required
def create_ilp_notification():
    """Run analysis and create notification if recommendations found"""
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    days = int(request.args.get('days', 7))
    
    # Run full analysis
    analysis_result = run_full_analysis(
        user_id=user_id,
        guest_code=guest_code,
        days=days
    )
    
    if not analysis_result.get('has_recommendations'):
        return jsonify({
            'success': True,
            'notification_created': False,
            'message': 'No recommendations needed - great work!',
            'summary': analysis_result.get('summary', '')
        })
    
    # Create notification
    rec_id = create_recommendation_notification(
        user_id=user_id,
        guest_code=guest_code,
        analysis_result=analysis_result
    )
    
    if rec_id:
        pending = get_pending_recommendations(user_id=user_id, guest_code=guest_code)
        return jsonify({
            'success': True,
            'notification_created': True,
            'recommendation_id': rec_id,
            'pending': pending[0] if pending else None,
            'summary': analysis_result.get('summary', '')
        })
    else:
        return jsonify({
            'success': False,
            'error': 'Failed to create notification'
        }), 500


@passport_bp.route('/api/ilp/run-nightly', methods=['POST'])
@guest_or_login_required
def run_ilp_nightly_for_user():
    """
    Manually trigger nightly analysis for current user.
    Useful for testing.
    """
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    # Auto-apply any expired recommendations first
    auto_applied = auto_apply_expired_recommendations()
    
    # Run analysis and create new notification
    analysis_result = run_full_analysis(user_id=user_id, guest_code=guest_code, days=7)
    
    rec_id = None
    if analysis_result.get('has_recommendations'):
        rec_id = create_recommendation_notification(
            user_id=user_id,
            guest_code=guest_code,
            analysis_result=analysis_result
        )
    
    return jsonify({
        'success': True,
        'auto_applied_count': auto_applied,
        'analysis': analysis_result,
        'new_recommendation_id': rec_id
    })


# =====================================================
# ILP ENGINE - SPRINT 4: NIGHTLY JOB & BATCH PROCESSING
# 12F: Batch Analysis for All Active Students
# 12G: PythonAnywhere Scheduled Task Integration
# 12H: Logging and Error Handling
# =====================================================

def get_active_students(days=14):
    """
    Get list of all students who have been active in the past N days.
    Returns list of dicts with user_id or guest_code.
    """
    from sqlalchemy import text
    from datetime import datetime, timedelta
    
    cutoff_date = datetime.now() - timedelta(days=days)
    active_students = []
    
    try:
        # Get active registered users
        users = db.session.execute(text("""
            SELECT DISTINCT user_id 
            FROM user_answers 
            WHERE user_id IS NOT NULL 
            AND answered_at >= :cutoff
        """), {'cutoff': cutoff_date}).fetchall()
        
        for row in users:
            active_students.append({'user_id': row[0], 'guest_code': None})
        
        # Get active guests
        guests = db.session.execute(text("""
            SELECT DISTINCT guest_code 
            FROM user_answers 
            WHERE guest_code IS NOT NULL 
            AND answered_at >= :cutoff
        """), {'cutoff': cutoff_date}).fetchall()
        
        for row in guests:
            active_students.append({'user_id': None, 'guest_code': row[0]})
        
    except Exception as e:
        print(f"Error getting active students: {e}")
    
    return active_students


def run_nightly_ilp_job():
    """
    Main nightly job function for ILP system.
    Processes all active students, creates recommendations, auto-applies expired ones.
    
    Call this from PythonAnywhere scheduled task:
        python -c "from app import run_nightly_ilp_job; run_nightly_ilp_job()"
    """
    from sqlalchemy import text
    from datetime import datetime, date
    import json
    
    job_start = datetime.now()
    today = date.today()
    
    stats = {
        'students_processed': 0,
        'recommendations_created': 0,
        'auto_applied': 0,
        'errors': []
    }
    
    print(f"\n{'='*60}")
    print(f"  ILP NIGHTLY JOB - {today}")
    print(f"  Started: {job_start.strftime('%H:%M:%S')}")
    print(f"{'='*60}\n")
    
    try:
        # Log job start
        db.session.execute(text("""
            INSERT INTO ilp_nightly_log (run_date, status)
            VALUES (:date, 'running')
        """), {'date': today})
        db.session.commit()
        
        # Get job ID
        job_row = db.session.execute(text("""
            SELECT id FROM ilp_nightly_log 
            WHERE run_date = :date AND status = 'running'
            ORDER BY started_at DESC LIMIT 1
        """), {'date': today}).fetchone()
        job_id = job_row[0] if job_row else None
        
    except Exception as e:
        print(f"Warning: Could not log job start: {e}")
        job_id = None
    
    try:
        # Step 1: Auto-apply any expired recommendations
        print("Step 1: Auto-applying expired recommendations...")
        stats['auto_applied'] = auto_apply_expired_recommendations()
        print(f"  ✓ Auto-applied: {stats['auto_applied']}")
        
        # Step 2: Get active students
        print("\nStep 2: Finding active students...")
        active_students = get_active_students(days=14)
        print(f"  ✓ Found {len(active_students)} active students")
        
        # Step 3: Process each student
        print("\nStep 3: Processing students...")
        
        for i, student in enumerate(active_students):
            user_id = student['user_id']
            guest_code = student['guest_code']
            student_ref = f"User {user_id}" if user_id else f"Guest {guest_code[:8]}..."
            
            try:
                # Check if student already has pending recommendation
                pending = get_pending_recommendations(user_id=user_id, guest_code=guest_code)
                
                if pending:
                    # Skip - already has pending notification
                    continue
                
                # Run analysis
                analysis = run_full_analysis(
                    user_id=user_id,
                    guest_code=guest_code,
                    days=7
                )
                
                stats['students_processed'] += 1
                
                # Create notification if recommendations found
                if analysis.get('has_recommendations'):
                    rec_id = create_recommendation_notification(
                        user_id=user_id,
                        guest_code=guest_code,
                        analysis_result=analysis
                    )
                    
                    if rec_id:
                        stats['recommendations_created'] += 1
                        print(f"  [{i+1}/{len(active_students)}] {student_ref}: Created recommendation #{rec_id}")
                    else:
                        print(f"  [{i+1}/{len(active_students)}] {student_ref}: Analysis done, no notification created")
                else:
                    # Print progress every 10 students
                    if (i + 1) % 10 == 0:
                        print(f"  [{i+1}/{len(active_students)}] Processed...")
                        
            except Exception as e:
                error_msg = f"{student_ref}: {str(e)}"
                stats['errors'].append(error_msg)
                print(f"  ⚠ Error processing {student_ref}: {e}")
        
        # Step 4: Summary
        job_end = datetime.now()
        duration = (job_end - job_start).total_seconds()
        
        print(f"\n{'='*60}")
        print(f"  JOB COMPLETE")
        print(f"{'='*60}")
        print(f"  Duration: {duration:.1f} seconds")
        print(f"  Students processed: {stats['students_processed']}")
        print(f"  Recommendations created: {stats['recommendations_created']}")
        print(f"  Auto-applied: {stats['auto_applied']}")
        print(f"  Errors: {len(stats['errors'])}")
        
        if stats['errors']:
            print(f"\n  Errors encountered:")
            for err in stats['errors'][:5]:
                print(f"    • {err}")
            if len(stats['errors']) > 5:
                print(f"    ... and {len(stats['errors']) - 5} more")
        
        # Update job log
        if job_id:
            try:
                db.session.execute(text("""
                    UPDATE ilp_nightly_log 
                    SET completed_at = :completed,
                        students_processed = :processed,
                        recommendations_created = :created,
                        auto_applied = :auto,
                        errors = :errors,
                        status = 'completed'
                    WHERE id = :job_id
                """), {
                    'completed': job_end,
                    'processed': stats['students_processed'],
                    'created': stats['recommendations_created'],
                    'auto': stats['auto_applied'],
                    'errors': json.dumps(stats['errors']) if stats['errors'] else None,
                    'job_id': job_id
                })
                db.session.commit()
            except Exception as e:
                print(f"Warning: Could not update job log: {e}")
        
        return stats
        
    except Exception as e:
        print(f"\n❌ CRITICAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        
        # Log failure
        if job_id:
            try:
                db.session.execute(text("""
                    UPDATE ilp_nightly_log 
                    SET completed_at = CURRENT_TIMESTAMP,
                        status = 'failed',
                        errors = :error
                    WHERE id = :job_id
                """), {'error': str(e), 'job_id': job_id})
                db.session.commit()
            except:
                pass
        
        stats['errors'].append(str(e))
        return stats


def get_nightly_job_history(limit=10):
    """
    Get history of nightly job runs.
    """
    from sqlalchemy import text
    
    try:
        results = db.session.execute(text("""
            SELECT id, run_date, started_at, completed_at, 
                   students_processed, recommendations_created, 
                   auto_applied, status, errors
            FROM ilp_nightly_log
            ORDER BY started_at DESC
            LIMIT :limit
        """), {'limit': limit}).fetchall()
        
        history = []
        for row in results:
            started = row[2]
            completed = row[3]
            duration = None
            
            if started and completed:
                if isinstance(started, str):
                    from datetime import datetime
                    started = datetime.fromisoformat(started.replace('Z', '+00:00'))
                if isinstance(completed, str):
                    completed = datetime.fromisoformat(completed.replace('Z', '+00:00'))
                duration = (completed - started).total_seconds()
            
            history.append({
                'id': row[0],
                'run_date': str(row[1]) if row[1] else None,
                'started_at': started.isoformat() if hasattr(started, 'isoformat') else started,
                'completed_at': completed.isoformat() if hasattr(completed, 'isoformat') else completed,
                'duration_seconds': round(duration, 1) if duration else None,
                'students_processed': row[4],
                'recommendations_created': row[5],
                'auto_applied': row[6],
                'status': row[7],
                'has_errors': bool(row[8])
            })
        
        return history
        
    except Exception as e:
        print(f"Error getting job history: {e}")
        return []


# =====================================================
# ILP ENGINE - SPRINT 4 API ENDPOINTS
# =====================================================

@passport_bp.route('/api/ilp/nightly-job', methods=['POST'])
def trigger_nightly_job():
    """
    Trigger the nightly ILP job manually.
    Requires admin authentication in production.
    """
    # In production, add admin authentication check here
    # if not current_user.is_admin:
    #     return jsonify({'error': 'Unauthorized'}), 403
    
    stats = run_nightly_ilp_job()
    
    return jsonify({
        'success': True,
        'stats': stats
    })


@passport_bp.route('/api/ilp/job-history', methods=['GET'])
def get_job_history():
    """Get history of nightly job runs"""
    limit = int(request.args.get('limit', 10))
    
    history = get_nightly_job_history(limit=limit)
    
    return jsonify({
        'success': True,
        'count': len(history),
        'history': history
    })


@passport_bp.route('/api/ilp/stats', methods=['GET'])
def get_ilp_stats():
    """Get overall ILP system statistics"""
    from sqlalchemy import text
    
    try:
        # Count recommendations by status
        status_counts = db.session.execute(text("""
            SELECT status, COUNT(*) as count
            FROM ilp_recommendations
            GROUP BY status
        """)).fetchall()
        
        by_status = {row[0]: row[1] for row in status_counts}
        
        # Recent activity
        recent_created = db.session.execute(text("""
            SELECT COUNT(*) FROM ilp_recommendations
            WHERE created_at >= datetime('now', '-7 days')
        """)).fetchone()[0]
        
        recent_accepted = db.session.execute(text("""
            SELECT COUNT(*) FROM ilp_recommendations
            WHERE status = 'accepted'
            AND responded_at >= datetime('now', '-7 days')
        """)).fetchone()[0]
        
        # Latest job run
        latest_job = db.session.execute(text("""
            SELECT run_date, status, students_processed, recommendations_created
            FROM ilp_nightly_log
            ORDER BY started_at DESC LIMIT 1
        """)).fetchone()
        
        return jsonify({
            'success': True,
            'recommendations': {
                'by_status': by_status,
                'total': sum(by_status.values()),
                'last_7_days': {
                    'created': recent_created,
                    'accepted': recent_accepted
                }
            },
            'latest_job': {
                'run_date': str(latest_job[0]) if latest_job else None,
                'status': latest_job[1] if latest_job else None,
                'students_processed': latest_job[2] if latest_job else 0,
                'recommendations_created': latest_job[3] if latest_job else 0
            } if latest_job else None
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

