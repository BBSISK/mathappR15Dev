# routes/student_features.py
# Student gamification features for AgentMath
# Extracted from app.py for better maintainability
#
# Revision: 1.0.2
# Date: 2025-12-31
# Phase 10: Student features extraction
#
# Fixes in 1.0.2:
# - Fixed url_for('student_app') → redirect('/app') in avatar_shop_page
# - Fixed url_for('login') → url_for('auth.login') in avatar_shop_page
# - These caused Avatar button to redirect to dashboard instead of avatar shop
#
# Fix in 1.0.1: Added missing topic configuration and FEATURE_FLAGS access
#
# Contains 27 routes for:
# - Badges API (5 routes) - badge display, stats, progress
# - Bonus Questions (10 routes) - random questions, submissions, archives
# - Who Am I? API (5 routes) - image reveal game
# - Avatar System (7 routes) - shop, inventory, purchase, equip

from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for, flash, current_app
from datetime import datetime, timedelta
import random
import os
import json
import time

# Create blueprint
student_bp = Blueprint('student_features', __name__)

# Import database and models
from models import (
    db, User, UserStats, TopicProgress, Badge, UserBadge, QuizAttempt,
    BonusQuestion, BonusQuestionAttempt, AvatarItem, UserAvatarInventory,
    UserAvatarEquipped, AvatarPurchaseLog, SystemSetting
)

# Import decorators from utils
from utils import login_required, guest_or_login_required, approved_required

# Import badge and avatar helpers
from utils import (
    check_and_award_badges, initialize_user_stats, update_user_stats_after_quiz,
    update_topic_progress, get_avatar_user_points, avatar_owns_item,
    get_equipped_avatar, grant_default_avatar_items
)


# ==================== TOPIC CONFIGURATION ====================
# Fallback topics when database unavailable
FALLBACK_TOPICS = [
    'arithmetic', 'fractions', 'decimals', 'multiplication_division',
    'number_systems', 'bodmas', 'sets', 'surds',
    'introductory_algebra', 'functions', 'patterns', 'solving_equations',
    'simplifying_expressions', 'expanding_factorising',
    'complex_numbers_intro', 'complex_numbers_expanded', 'simultaneous_equations',
    'coordinate_geometry', 'trigonometry',
    'probability', 'descriptive_statistics',
]

VALID_DIFFICULTIES = ['beginner', 'intermediate', 'advanced']

# Cache for database topics
_topics_cache = {'topics': None, 'timestamp': None}
_CACHE_DURATION_SECONDS = 300  # 5 minutes

def get_valid_topics_from_db():
    """Get valid topics from the database topics table."""
    from sqlalchemy import text
    
    current_time = time.time()
    if (_topics_cache['topics'] is not None and 
        _topics_cache['timestamp'] is not None and
        current_time - _topics_cache['timestamp'] < _CACHE_DURATION_SECONDS):
        return _topics_cache['topics']
    
    try:
        result = db.session.execute(text(
            "SELECT topic_id FROM topics WHERE is_visible = 1"
        )).fetchall()
        
        if result:
            topics = [row[0] for row in result]
            _topics_cache['topics'] = topics
            _topics_cache['timestamp'] = current_time
            return topics
        else:
            return FALLBACK_TOPICS
            
    except Exception as e:
        print(f"Warning: Could not load topics from database: {e}")
        return FALLBACK_TOPICS


# ==================== FEATURE FLAGS ACCESS ====================
def get_feature_flags():
    """Get feature flags from app config"""
    try:
        return current_app.config.get('FEATURE_FLAGS', {})
    except:
        return {}

# Property-like access for FEATURE_FLAGS
class FeatureFlagsProxy:
    def get(self, key, default=False):
        return get_feature_flags().get(key, default)
    
    def __getitem__(self, key):
        return get_feature_flags().get(key, False)

FEATURE_FLAGS = FeatureFlagsProxy()


@student_bp.route('/api/student/badges')
@login_required
@approved_required
def get_student_badges():
    """Get all badges (earned and available) for the current student"""
    from sqlalchemy import text

    # =====================================================================
    # CASUAL GUESTS - Quick Try users (now with session persistence!)
    # =====================================================================
    if 'is_guest' in session and 'guest_code' not in session:
        user_id = session.get('user_id')
        stats = UserStats.query.filter_by(user_id=user_id).first() if user_id else None
        
        return jsonify({
            'earned': [],
            'available': [],
            'level': stats.level if stats else 1,
            'total_points': stats.total_points if stats else 0,
            'total_badges': 0,
            'is_casual_guest': True
        }), 200

    # =====================================================================
    # REPEAT GUESTS - Users with guest_code (persistent points & badges)
    # =====================================================================
    if 'guest_code' in session:
        guest_code = session['guest_code']

        # DEBUG: Print start
        print(f"\n{'='*80}")
        print(f"🔍 LOADING BADGES FOR GUEST: {guest_code}")
        print(f"{'='*80}")

        # Ensure guest_badges table exists
        ensure_guest_badges_table()

        # Get guest stats with error handling
        try:
            guest_stats = db.session.execute(text("""
                SELECT total_score, quizzes_completed
                FROM guest_users
                WHERE guest_code = :code
            """), {"code": guest_code}).fetchone()
            print(f"📊 Guest stats: {guest_stats}")
        except Exception as e:
            # If query fails, return default values
            print(f"❌ Error getting guest stats: {e}")
            guest_stats = None

        # Get guest badges (simplified query - only essential columns)
        try:
            guest_badges = db.session.execute(text("""
                SELECT badge_name, earned_at
                FROM guest_badges
                WHERE guest_code = :code
                ORDER BY earned_at DESC
            """), {"code": guest_code}).fetchall()
            print(f"🏆 Existing badges in DB: {len(guest_badges)} badges")
            for b in guest_badges:
                print(f"   - {b[0]}")
        except Exception as e:
            # If guest_badges table doesn't exist or has issues, just return empty
            print(f"❌ Error getting guest badges: {e}")
            guest_badges = []

        # Calculate level (1 level per 100 points)
        total_points = guest_stats[0] if guest_stats else 0
        quizzes_completed = guest_stats[1] if guest_stats and len(guest_stats) > 1 else 0
        level = (total_points // 100) + 1

        # Format earned badges for frontend - need to look up full badge details!
        earned_badges_list = []
        earned_badge_names = set()
        
        # Create a lookup dict for badge details
        badge_lookup = {}
        try:
            all_badge_records = Badge.query.all()
            for b in all_badge_records:
                badge_lookup[b.name] = b
        except Exception as e:
            print(f"Warning: Could not load badge details: {e}")
        
        for badge in guest_badges:
            badge_name = badge[0]
            badge_details = badge_lookup.get(badge_name)
            
            earned_badges_list.append({
                'name': badge_name,
                'description': badge_details.description if badge_details else 'Achievement unlocked!',
                'points': badge_details.points if badge_details else 0,
                'icon': badge_details.icon if badge_details else 'fa-trophy',
                'category': badge_details.category if badge_details else 'achievement',
                'earned_at': badge[1] if badge[1] else None
            })
            earned_badge_names.add(badge_name)

        # GET ALL BADGES FROM DATABASE (same as registered users!)
        try:
            all_badges = Badge.query.all()
            print(f"\n🎯 Total badges in system: {len(all_badges)}")
        except Exception as e:
            print(f"❌ Error loading badges: {e}")
            all_badges = []

        available_badges_list = []

        print(f"\n🔄 Processing badges...")

        # Calculate progress for each badge (same logic as registered users)
        for badge in all_badges:
            # Skip if already earned
            if badge.name in earned_badge_names:
                print(f"  ⏭️  {badge.name}: Already earned, skipping")
                continue

            progress = 0

            print(f"\n  📍 Checking: {badge.name} ({badge.requirement_type})")

            # Calculate progress based on badge requirement
            if badge.requirement_type == 'quizzes_completed':
                progress = min(100, int((quizzes_completed / badge.requirement_value) * 100))
                print(f"     Progress: {quizzes_completed}/{badge.requirement_value} quizzes = {progress}%")
            elif badge.requirement_type == 'perfect_scores':
                # Count perfect scores from guest_quiz_attempts
                try:
                    perfect_count = db.session.execute(text("""
                        SELECT COUNT(*) FROM guest_quiz_attempts
                        WHERE guest_code = :code AND score = total_questions
                    """), {"code": guest_code}).fetchone()[0]
                    progress = min(100, int((perfect_count / badge.requirement_value) * 100))
                except:
                    progress = 0
            elif badge.requirement_type == 'streak_days':
                # Guests don't track daily streaks yet
                progress = 0
            elif badge.requirement_type == 'topics_mastered':
                # Count distinct topics with 90%+ average
                try:
                    topics_result = db.session.execute(text("""
                        SELECT topic, AVG(CAST(score AS FLOAT) / total_questions) as avg_score
                        FROM guest_quiz_attempts
                        WHERE guest_code = :code
                        GROUP BY topic
                        HAVING AVG(CAST(score AS FLOAT) / total_questions) >= 0.9
                    """), {"code": guest_code}).fetchall()
                    topics_mastered = len(topics_result)  # Count how many topics meet criteria
                    progress = min(100, int((topics_mastered / badge.requirement_value) * 100))
                except Exception as e:
                    print(f"Error calculating topics_mastered: {e}")
                    progress = 0
            elif badge.requirement_type == 'high_scores':
                # Count quizzes with 90%+ score
                try:
                    high_scores = db.session.execute(text("""
                        SELECT COUNT(*) FROM guest_quiz_attempts
                        WHERE guest_code = :code
                        AND CAST(score AS FLOAT) / total_questions >= 0.9
                    """), {"code": guest_code}).fetchone()[0]
                    progress = min(100, int((high_scores / badge.requirement_value) * 100))
                except:
                    progress = 0
            else:
                progress = 0

            # AUTO-AWARD: If progress is 100%, award the badge!
            if progress >= 100:
                print(f"     🎯 Badge at 100%! Attempting to award...")
                try:
                    # Check if badge already exists
                    existing = db.session.execute(text("""
                        SELECT COUNT(*) FROM guest_badges
                        WHERE guest_code = :code AND badge_name = :badge_name
                    """), {"code": guest_code, "badge_name": badge.name}).fetchone()[0]

                    print(f"     Existing count in DB: {existing}")

                    if existing == 0:
                        print(f"     → Inserting into guest_badges...")
                        # Award the badge!
                        db.session.execute(text("""
                            INSERT INTO guest_badges (guest_code, badge_name, earned_at)
                            VALUES (:code, :badge_name, :earned_at)
                        """), {
                            "code": guest_code,
                            "badge_name": badge.name,
                            "earned_at": datetime.utcnow()
                        })
                        db.session.commit()
                        print(f"     ✅ Committed to database!")

                        # Add to earned badges instead of available
                        earned_badges_list.append({
                            'name': badge.name,
                            'earned_at': datetime.utcnow().isoformat(),
                            'icon': badge.icon
                        })
                        earned_badge_names.add(badge.name)

                        print(f'     🎉 Auto-awarded badge: {badge.name} to guest {guest_code}')
                        print(f'     📝 Added to earned_badges_list (now {len(earned_badges_list)} badges)')
                        continue  # Skip adding to available badges
                    else:
                        print(f'     ⏭️  Badge {badge.name} already in DB, skipping')
                        continue  # Skip adding to available if already earned
                except Exception as e:
                    # Log error but don't crash
                    print(f'     ❌ Error auto-awarding badge {badge.name}: {str(e)}')
                    import traceback
                    traceback.print_exc()
                    # Fall through to add to available badges

            # Add to available badges
            available_badges_list.append({
                'id': badge.id,
                'name': badge.name,
                'description': badge.description,
                'icon': badge.icon,
                'category': badge.category,
                'requirement_type': badge.requirement_type,
                'requirement_value': badge.requirement_value,
                'points': badge.points,
                'color': badge.color,
                'progress': progress,
                'earned_at': None
            })

        print(f"\n{'='*80}")
        print(f"📊 FINAL RESULTS:")
        print(f"   Earned badges: {len(earned_badges_list)}")
        for b in earned_badges_list:
            print(f"      - {b['name']}")
        print(f"   Available badges: {len(available_badges_list)}")
        print(f"   Total points: {total_points}")
        print(f"   Level: {level}")
        print(f"{'='*80}\n")

        return jsonify({
            'earned': earned_badges_list,
            'available': available_badges_list,  # ALL badges from database!
            'level': level,
            'total_points': total_points,
            'total_badges': len(earned_badges_list) + len(available_badges_list),
            'is_repeat_guest': True
        }), 200

    # =====================================================================
    # REGISTERED USERS - Full badge system
    # =====================================================================
    user_id = session['user_id']

    # Get all badges
    all_badges = Badge.query.all()

    # Get earned badges
    earned_badges = UserBadge.query.filter_by(user_id=user_id).all()
    earned_badge_ids = {ub.badge_id for ub in earned_badges}

    # Get user stats for progress on unearned badges
    stats = UserStats.query.filter_by(user_id=user_id).first()
    if not stats:
        stats = initialize_user_stats(user_id)

    badges_data = {
        'earned': [],
        'available': [],
        'total_points': stats.total_points,
        'level': stats.level,
        'is_registered_user': True
    }

    for badge in all_badges:
        badge_dict = badge.to_dict()

        if badge.id in earned_badge_ids:
            # Badge is earned
            user_badge = next(ub for ub in earned_badges if ub.badge_id == badge.id)
            badge_dict['earned_at'] = user_badge.earned_at.isoformat()
            badge_dict['progress'] = 100
            badges_data['earned'].append(badge_dict)
        else:
            # Badge is available - calculate progress
            progress = 0

            if badge.requirement_type == 'quizzes_completed':
                progress = min(100, int((stats.total_quizzes / badge.requirement_value) * 100))
            elif badge.requirement_type == 'perfect_scores':
                progress = min(100, int((stats.perfect_scores / badge.requirement_value) * 100))
            elif badge.requirement_type == 'streak_days':
                progress = min(100, int((stats.current_streak_days / badge.requirement_value) * 100))
            elif badge.requirement_type == 'topics_mastered':
                progress = min(100, int((stats.topics_mastered / badge.requirement_value) * 100))
            elif badge.requirement_type == 'high_scores':
                high_scores = QuizAttempt.query.filter(
                    QuizAttempt.user_id == user_id,
                    QuizAttempt.percentage >= 90
                ).count()
                progress = min(100, int((high_scores / badge.requirement_value) * 100))

            badge_dict['progress'] = progress
            badge_dict['earned_at'] = None
            badges_data['available'].append(badge_dict)

    return jsonify(badges_data)

@student_bp.route('/api/student/stats')
@login_required
@approved_required
def get_student_stats():
    """Get detailed statistics for the current student"""

    # Handle repeat guests - fetch from guest tables
    if 'guest_code' in session:
        from sqlalchemy import text
        guest_code = session['guest_code']

        # Get guest stats
        guest_stats = db.session.execute(text("""
            SELECT total_score, quizzes_completed
            FROM guest_users
            WHERE guest_code = :code
        """), {"code": guest_code}).fetchone()

        # Get guest quiz attempts (recent 10 for display)
        attempts = db.session.execute(text("""
            SELECT topic, difficulty, score, total_questions, completed_at
            FROM guest_quiz_attempts
            WHERE guest_code = :code
            ORDER BY completed_at DESC
            LIMIT 10
        """), {"code": guest_code}).fetchall()

        # Calculate accuracy
        total_correct = sum(a[2] for a in attempts) if attempts else 0
        total_questions = sum(a[3] for a in attempts) if attempts else 0
        accuracy = (total_correct / total_questions * 100) if total_questions > 0 else 0

        # Get badge count
        try:
            badge_count = db.session.execute(text("""
                SELECT COUNT(*) FROM guest_badges WHERE guest_code = :code
            """), {"code": guest_code}).fetchone()[0]
        except:
            badge_count = 0

        # =====================================================
        # CALCULATE TOPIC PROGRESS FROM GUEST_QUIZ_ATTEMPTS
        # =====================================================
        # Try to include bonus columns if they exist, fallback to basic query
        try:
            topic_progress_data = db.session.execute(text("""
                SELECT 
                    topic,
                    difficulty,
                    COUNT(*) as attempts,
                    MAX(score) as best_score,
                    MAX(CAST(score AS FLOAT) / NULLIF(total_questions, 0) * 100) as best_percentage,
                    SUM(total_questions) as total_questions_answered,
                    SUM(score) as total_correct,
                    MAX(completed_at) as last_attempt,
                    MAX(score + COALESCE(who_am_i_bonus, 0) + COALESCE(milestone_points, 0)) as max_points
                FROM guest_quiz_attempts
                WHERE guest_code = :code
                GROUP BY topic, difficulty
                ORDER BY topic, 
                    CASE difficulty 
                        WHEN 'beginner' THEN 1 
                        WHEN 'intermediate' THEN 2 
                        WHEN 'advanced' THEN 3 
                        ELSE 4 
                    END
            """), {"code": guest_code}).fetchall()
        except:
            # Fallback: bonus columns don't exist yet
            topic_progress_data = db.session.execute(text("""
                SELECT 
                    topic,
                    difficulty,
                    COUNT(*) as attempts,
                    MAX(score) as best_score,
                    MAX(CAST(score AS FLOAT) / NULLIF(total_questions, 0) * 100) as best_percentage,
                    SUM(total_questions) as total_questions_answered,
                    SUM(score) as total_correct,
                    MAX(completed_at) as last_attempt,
                    MAX(score) as max_points
                FROM guest_quiz_attempts
                WHERE guest_code = :code
                GROUP BY topic, difficulty
                ORDER BY topic, 
                    CASE difficulty 
                        WHEN 'beginner' THEN 1 
                        WHEN 'intermediate' THEN 2 
                        WHEN 'advanced' THEN 3 
                        ELSE 4 
                    END
            """), {"code": guest_code}).fetchall()
        
        # Format topic progress for frontend
        topic_progress = []
        for row in topic_progress_data:
            topic, difficulty, attempt_count, best_score, best_pct, total_q, total_correct_topic, last_attempt, max_points = row
            
            # Calculate accuracy for this topic/difficulty
            topic_accuracy = (total_correct_topic / total_q * 100) if total_q > 0 else 0
            
            # Check if mastered (90%+ accuracy with 5+ attempts)
            is_mastered = (attempt_count >= 5 and topic_accuracy >= 90)
            
            # Format topic name for display
            display_name = topic.replace('_', ' ').title()
            
            topic_progress.append({
                'topic': display_name,
                'topic_id': topic,
                'difficulty': difficulty.title() if difficulty else 'Unknown',
                'attempts': attempt_count,
                'best_score': best_score or 0,
                'best_percentage': round(best_pct, 1) if best_pct else 0,
                'accuracy': round(topic_accuracy, 1),
                'is_mastered': is_mastered,
                'max_points': max_points or 0,
                'last_attempt_at': last_attempt
            })
        
        # Count perfect scores
        try:
            perfect_count = db.session.execute(text("""
                SELECT COUNT(*) FROM guest_quiz_attempts
                WHERE guest_code = :code AND score = total_questions AND total_questions > 0
            """), {"code": guest_code}).fetchone()[0]
        except:
            perfect_count = 0
        
        # Count topics mastered
        topics_mastered = sum(1 for tp in topic_progress if tp['is_mastered'])
        
        # Calculate level properly (1 level per 100 points)
        total_points = guest_stats[0] if guest_stats else 0
        level = (total_points // 100) + 1

        return jsonify({
            'stats': {
                'total_quizzes': guest_stats[1] if guest_stats else 0,
                'total_questions_answered': total_questions,
                'total_correct_answers': total_correct,
                'overall_accuracy': round(accuracy, 1),
                'current_streak_days': 0,
                'longest_streak_days': 0,
                'total_points': total_points,
                'level': level,
                'topics_mastered': topics_mastered,
                'perfect_scores': perfect_count,
                'badges_earned': badge_count
            },
            'topic_progress': topic_progress,
            'recent_attempts': [{
                'topic': a[0],
                'difficulty': a[1],
                'score': a[2],
                'total_questions': a[3],
                'completed_at': a[4]
            } for a in attempts]
        }), 200

    # Handle casual guests - no stats
    if 'is_guest' in session:
        return jsonify({
            'stats': {
                'total_quizzes': 0,
                'total_questions_answered': 0,
                'total_correct_answers': 0,
                'overall_accuracy': 0,
                'current_streak_days': 0,
                'longest_streak_days': 0,
                'total_points': 0,
                'level': 1,
                'topics_mastered': 0,
                'perfect_scores': 0
            },
            'topic_progress': [],
            'recent_attempts': []
        }), 200

    # Handle full accounts
    user_id = session['user_id']

    stats = UserStats.query.filter_by(user_id=user_id).first()
    if not stats:
        stats = initialize_user_stats(user_id)

    # Get topic progress
    topic_progress = TopicProgress.query.filter_by(user_id=user_id).all()

    # Get recent quiz attempts
    recent_attempts = QuizAttempt.query.filter_by(user_id=user_id).order_by(
        QuizAttempt.completed_at.desc()
    ).limit(10).all()

    # Get streak info (if Irish calendar enabled)
    streak_info = {}
    if IRISH_CALENDAR_ENABLED:
        next_milestone_days, next_milestone_info = get_next_milestone(stats.current_streak_days)
        streak_info = {
            'is_school_day_streak': True,
            'next_milestone_days': next_milestone_days,
            'next_milestone_name': next_milestone_info['name'] if next_milestone_info else None,
            'next_milestone_points': next_milestone_info['points'] if next_milestone_info else None,
            'days_until_next': (next_milestone_days - stats.current_streak_days) if next_milestone_days else None
        }

    stats_dict = stats.to_dict()
    stats_dict['streak_info'] = streak_info

    return jsonify({
        'stats': stats_dict,
        'topic_progress': [tp.to_dict() for tp in topic_progress],
        'recent_attempts': [qa.to_dict() for qa in recent_attempts]
    })

@student_bp.route('/api/student/progress/<topic>')
@login_required
@approved_required
def get_topic_progress(topic):
    """Get progress for a specific topic"""
    user_id = session['user_id']

    progress = TopicProgress.query.filter_by(user_id=user_id, topic=topic).all()

    return jsonify({
        'topic': topic,
        'progress': [p.to_dict() for p in progress]
    })

@student_bp.route('/api/student/mastery')
@login_required
@approved_required
def get_student_mastery():
    """
    Get student's mastery status for all topics and difficulties.
    Returns best score for each topic/difficulty combination.
    Mastery threshold: >80%
    OPTIMIZED: Single query instead of 36 separate queries
    Now supports both registered users AND guest_code users
    """
    from sqlalchemy import text
    
    # Casual guest users (no guest_code) don't have mastery data
    if 'is_guest' in session and 'guest_code' not in session:
        return jsonify({}), 200

    # Get all topics from database - automatically includes new topics
    topics = get_valid_topics_from_db()  # Database-driven!
    difficulties = VALID_DIFFICULTIES

    # Check if this is a guest_code user or registered user
    if 'guest_code' in session:
        # Guest code user - query guest_quiz_attempts table
        guest_code = session['guest_code']
        query = text("""
            SELECT topic, difficulty, MAX(CAST(score AS FLOAT) / total_questions * 100) as best_score
            FROM guest_quiz_attempts
            WHERE guest_code = :guest_code
            GROUP BY topic, difficulty
        """)
        results = db.session.execute(query, {'guest_code': guest_code}).fetchall()
    else:
        # Registered user - query quiz_attempts table
        user_id = session['user_id']
        query = text("""
            SELECT topic, difficulty, MAX(percentage) as best_score
            FROM quiz_attempts
            WHERE user_id = :user_id
            GROUP BY topic, difficulty
        """)
        results = db.session.execute(query, {'user_id': user_id}).fetchall()

    # Build lookup dictionary from query results
    best_scores = {}
    for row in results:
        topic, difficulty, best_score = row
        if topic not in best_scores:
            best_scores[topic] = {}
        best_scores[topic][difficulty] = best_score or 0

    # Build mastery data structure
    mastery_data = {}

    for topic in topics:
        mastery_data[topic] = {
            'difficulties': {},
            'topic_mastered': False
        }

        mastered_count = 0

        for difficulty in difficulties:
            best_score = best_scores.get(topic, {}).get(difficulty, 0)

            if best_score > 80:
                mastery_data[topic]['difficulties'][difficulty] = {
                    'mastered': True,
                    'best_score': round(best_score, 1)
                }
                mastered_count += 1
            else:
                mastery_data[topic]['difficulties'][difficulty] = {
                    'mastered': False,
                    'best_score': round(best_score, 1)
                }

        # Topic is mastered if all 3 difficulties are mastered
        mastery_data[topic]['topic_mastered'] = (mastered_count == 3)

    return jsonify(mastery_data)


# ==================== MANUAL BADGE AWARD ROUTE ====================
@student_bp.route('/api/award-badges-now')
@login_required
def award_badges_now():
    """
    Manually trigger badge awarding for current guest code user
    Useful for testing and fixing badges that should be earned
    """
    from sqlalchemy import text

    if 'guest_code' not in session:
        return jsonify({
            'error': 'Only available for guest code users',
            'message': 'Please log in with a guest code to use this feature'
        }), 400

    guest_code = session['guest_code']

    try:
        # Ensure guest_badges table exists
        ensure_guest_badges_table()

        # Get guest stats
        guest_stats = db.session.execute(text("""
            SELECT total_score, quizzes_completed
            FROM guest_users
            WHERE guest_code = :code
        """), {"code": guest_code}).fetchone()

        if not guest_stats:
            return jsonify({'error': 'Guest not found'}), 404

        quizzes = guest_stats[1]
        points = guest_stats[0]

        # Get all badges
        all_badges = Badge.query.all()

        awarded = []
        skipped = []
        errors = []

        for badge in all_badges:
            try:
                # Calculate if badge is earned
                earned = False
                progress = 0

                if badge.requirement_type == 'quizzes_completed':
                    progress = (quizzes / badge.requirement_value) * 100 if badge.requirement_value > 0 else 0
                    if quizzes >= badge.requirement_value:
                        earned = True

                elif badge.requirement_type == 'perfect_scores':
                    perfect_count = db.session.execute(text("""
                        SELECT COUNT(*) FROM guest_quiz_attempts
                        WHERE guest_code = :code AND score = total_questions
                    """), {"code": guest_code}).fetchone()[0]
                    progress = (perfect_count / badge.requirement_value) * 100 if badge.requirement_value > 0 else 0
                    if perfect_count >= badge.requirement_value:
                        earned = True

                elif badge.requirement_type == 'high_scores':
                    high_scores = db.session.execute(text("""
                        SELECT COUNT(*) FROM guest_quiz_attempts
                        WHERE guest_code = :code
                        AND CAST(score AS FLOAT) / total_questions >= 0.9
                    """), {"code": guest_code}).fetchone()[0]
                    progress = (high_scores / badge.requirement_value) * 100 if badge.requirement_value > 0 else 0
                    if high_scores >= badge.requirement_value:
                        earned = True

                elif badge.requirement_type == 'topics_mastered':
                    topics_result = db.session.execute(text("""
                        SELECT topic, AVG(CAST(score AS FLOAT) / total_questions) as avg_score
                        FROM guest_quiz_attempts
                        WHERE guest_code = :code
                        GROUP BY topic
                        HAVING AVG(CAST(score AS FLOAT) / total_questions) >= 0.9
                    """), {"code": guest_code}).fetchall()
                    topics_mastered = len(topics_result)
                    progress = (topics_mastered / badge.requirement_value) * 100 if badge.requirement_value > 0 else 0
                    if topics_mastered >= badge.requirement_value:
                        earned = True

                if earned:
                    # Check if already awarded
                    existing = db.session.execute(text("""
                        SELECT COUNT(*) FROM guest_badges
                        WHERE guest_code = :code AND badge_name = :name
                    """), {"code": guest_code, "name": badge.name}).fetchone()[0]

                    if existing == 0:
                        # Award it!
                        db.session.execute(text("""
                            INSERT INTO guest_badges (guest_code, badge_name, earned_at)
                            VALUES (:code, :name, :now)
                        """), {
                            "code": guest_code,
                            "name": badge.name,
                            "now": datetime.utcnow()
                        })
                        db.session.commit()
                        awarded.append({
                            'name': badge.name,
                            'progress': int(progress),
                            'requirement': f"{badge.requirement_type}: {badge.requirement_value}"
                        })
                    else:
                        skipped.append(f"{badge.name} (already earned)")

            except Exception as e:
                errors.append(f"{badge.name}: {str(e)}")

        return jsonify({
            'success': True,
            'message': 'Badge check complete!',
            'guest_code': guest_code,
            'quizzes_completed': quizzes,
            'total_points': points,
            'newly_awarded': awarded,
            'already_earned': skipped,
            'errors': errors if errors else None
        }), 200

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Failed to check badges. See error for details.'
        }), 500


def ensure_guest_badges_table():
    """
    Ensure the guest_badges table exists with correct structure
    Creates it if missing
    """
    from sqlalchemy import text

    try:
        # Check if table exists
        result = db.session.execute(text("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='guest_badges'
        """)).fetchone()

        if not result:
            print("⚠️  guest_badges table does NOT exist! Creating it now...")

            # Create the table
            db.session.execute(text("""
                CREATE TABLE guest_badges (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    guest_code TEXT NOT NULL,
                    badge_name TEXT NOT NULL,
                    earned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(guest_code, badge_name)
                )
            """))
            db.session.commit()
            print("✅ guest_badges table created successfully!")
        else:
            print("✅ guest_badges table exists")

    except Exception as e:
        print(f"❌ Error checking/creating guest_badges table: {e}")
        # Don't raise - just log the error



# ==================== BONUS QUESTION ROUTES ====================

@student_bp.route('/api/bonus-question/random')
@login_required
def get_random_bonus_question():
    """
    Get a random bonus question for high-scoring students
    Query params:
        - category: optional category filter (e.g., 'dinosaurs', 'flags')
        - exclude_id: optional ID to exclude (avoid repeats)
    """
    category = request.args.get('category', 'dinosaurs')  # Default to dinosaurs
    exclude_id = request.args.get('exclude_id', type=int)
    
    # Build query
    query = BonusQuestion.query.filter_by(category=category, is_active=True)
    
    if exclude_id:
        query = query.filter(BonusQuestion.id != exclude_id)
    
    # Get all matching questions
    questions = query.all()
    
    if not questions:
        return jsonify({'error': 'No bonus questions available', 'category': category}), 404
    
    # Select random question
    question = random.choice(questions)
    
    # Increment times shown
    question.times_shown += 1
    db.session.commit()
    
    return jsonify(question.to_dict())


@student_bp.route('/api/bonus-question/debug')
@login_required
def debug_bonus_questions():
    """
    Debug endpoint to check bonus question image URLs
    Access: /api/bonus-question/debug
    """
    from sqlalchemy import text
    
    try:
        # Get all bonus questions with their image URLs
        questions = db.session.execute(text("""
            SELECT id, category, correct_answer, image_url, is_active
            FROM bonus_questions
            ORDER BY category, id
            LIMIT 50
        """)).fetchall()
        
        results = []
        for q in questions:
            # Check if image_url looks valid
            image_url = q.image_url or ''
            
            # Determine potential issues
            issues = []
            if not image_url:
                issues.append('No image URL')
            elif not image_url.startswith('/') and not image_url.startswith('http'):
                issues.append('URL does not start with / or http')
            elif 'static/' not in image_url and not image_url.startswith('http'):
                issues.append('May be missing /static/ prefix')
            
            results.append({
                'id': q.id,
                'category': q.category,
                'answer': q.correct_answer,
                'image_url': image_url,
                'is_active': q.is_active,
                'issues': issues if issues else ['OK']
            })
        
        return jsonify({
            'total': len(results),
            'questions': results
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@student_bp.route('/api/bonus-question/test')
@login_required  
def test_bonus_question():
    """
    Test endpoint to simulate bonus question popup without completing quiz
    Access: /api/bonus-question/test
    This returns a bonus question that you can test the image loading with
    """
    category = request.args.get('category', 'dinosaurs')
    
    question = BonusQuestion.query.filter_by(category=category, is_active=True).first()
    
    if not question:
        return jsonify({'error': f'No bonus questions found for category: {category}'}), 404
    
    # Return in the same format as the random endpoint
    result = question.to_dict()
    
    # Add debug info
    result['_debug'] = {
        'raw_image_url': question.image_url,
        'category': question.category,
        'id': question.id,
        'test_image_tag': f'<img src="{question.image_url}" onerror="console.log(\'Image load failed:\', this.src)">'
    }
    
    return jsonify(result)


@student_bp.route('/test-dino-image')
@login_required
def test_dino_image_page():
    """
    Visual test page for bonus question images
    Access: /test-dino-image
    """
    from sqlalchemy import text
    
    # Get first few bonus questions
    questions = db.session.execute(text("""
        SELECT id, category, correct_answer, image_url
        FROM bonus_questions
        WHERE is_active = 1
        LIMIT 5
    """)).fetchall()
    
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dino Image Test</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; background: #f5f5f5; }
            .card { background: white; padding: 20px; margin: 20px 0; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
            .card h3 { margin-top: 0; }
            .image-container { 
                width: 300px; height: 300px; 
                background: #e0e0e0; 
                display: flex; align-items: center; justify-content: center;
                border-radius: 8px; overflow: hidden;
                margin: 10px 0;
            }
            .image-container img { max-width: 100%; max-height: 100%; }
            .url { font-family: monospace; background: #f0f0f0; padding: 5px 10px; border-radius: 4px; word-break: break-all; }
            .status { padding: 5px 10px; border-radius: 4px; display: inline-block; margin-top: 10px; }
            .status.loading { background: #fff3cd; color: #856404; }
            .status.success { background: #d4edda; color: #155724; }
            .status.error { background: #f8d7da; color: #721c24; }
        </style>
    </head>
    <body>
        <h1>🦕 Dino Image Test Page</h1>
        <p>This page tests whether bonus question images load correctly.</p>
    '''
    
    if not questions:
        html += '<div class="card"><p>No bonus questions found in database!</p></div>'
    else:
        for q in questions:
            html += f'''
            <div class="card">
                <h3>ID: {q.id} - {q.correct_answer}</h3>
                <p>Category: {q.category}</p>
                <p>Image URL: <span class="url">{q.image_url or 'NULL'}</span></p>
                <div class="image-container" id="container-{q.id}">
                    <img src="{q.image_url}" 
                         onload="document.getElementById('status-{q.id}').className='status success'; document.getElementById('status-{q.id}').textContent='✓ Image loaded successfully'"
                         onerror="document.getElementById('status-{q.id}').className='status error'; document.getElementById('status-{q.id}').textContent='✗ Image failed to load'; this.style.display='none'; document.getElementById('container-{q.id}').innerHTML='<span style=\\'color:red\\'>Image failed to load</span>'"
                         alt="{q.correct_answer}">
                </div>
                <div id="status-{q.id}" class="status loading">Loading...</div>
            </div>
            '''
    
    html += '''
        <div class="card">
            <h3>🔍 Debug Info</h3>
            <p>If images fail to load, check:</p>
            <ul>
                <li>Is the image URL correct? (should start with /static/ or be a full URL)</li>
                <li>Does the file exist in the static folder?</li>
                <li>Check browser Network tab (F12) for 404 errors</li>
            </ul>
            <p><a href="/api/bonus-question/debug">View all bonus question URLs (JSON)</a></p>
        </div>
    </body>
    </html>
    '''
    
    return html


@student_bp.route('/api/bonus-question/submit', methods=['POST'])
@login_required
def submit_bonus_answer():
    """
    Submit answer to bonus question
    Awards +100 points if correct
    """
    from sqlalchemy import text
    
    data = request.get_json()
    question_id = data.get('question_id')
    selected_answer = data.get('selected_answer')
    quiz_topic = data.get('quiz_topic')
    quiz_score = data.get('quiz_score')
    
    if not question_id or not selected_answer:
        return jsonify({'error': 'Missing question_id or selected_answer'}), 400
    
    # Get question
    question = BonusQuestion.query.get(question_id)
    if not question:
        return jsonify({'error': 'Question not found'}), 404
    
    # Check if correct
    is_correct = selected_answer.strip().lower() == question.correct_answer.strip().lower()
    points_earned = 100 if is_correct else 0
    
    # Update question stats
    if is_correct:
        question.times_correct += 1
    
    # Get user info
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    # Record attempt
    attempt = BonusQuestionAttempt(
        question_id=question_id,
        user_id=user_id,
        guest_code=guest_code,
        selected_answer=selected_answer,
        is_correct=is_correct,
        points_earned=points_earned,
        quiz_topic=quiz_topic,
        quiz_score=quiz_score
    )
    db.session.add(attempt)
    
    # Award points if correct
    if is_correct and points_earned > 0:
        if guest_code:
            # Update guest user points
            try:
                db.session.execute(text("""
                    UPDATE guest_users 
                    SET total_score = total_score + :points
                    WHERE guest_code = :code
                """), {"points": points_earned, "code": guest_code})
            except Exception as e:
                print(f"Error updating guest points: {e}")
        elif user_id:
            # Update registered user points
            stats = UserStats.query.filter_by(user_id=user_id).first()
            if stats:
                stats.total_points += points_earned
    
    db.session.commit()
    
    return jsonify({
        'correct': is_correct,
        'points_earned': points_earned,
        'correct_answer': question.correct_answer,
        'fun_fact': question.fun_fact,
        'era_or_region': question.era_or_region
    })


@student_bp.route('/api/bonus-question/categories')
@login_required
def get_bonus_categories():
    """Get available bonus question categories with counts"""
    from sqlalchemy import func
    
    categories = db.session.query(
        BonusQuestion.category,
        func.count(BonusQuestion.id).label('count')
    ).filter_by(is_active=True).group_by(BonusQuestion.category).all()
    
    return jsonify([{
        'category': cat,
        'count': count,
        'display_name': cat.title()
    } for cat, count in categories])


@student_bp.route('/api/bonus-question/test-submit')
@login_required
def test_submit_bonus_question():
    """
    Test endpoint to create a fake bonus question attempt for testing the archive.
    Access: /api/bonus-question/test-submit
    This creates a test entry so you can verify the Dino Archive works.
    """
    from sqlalchemy import text
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not logged in'}), 401
    
    # Get a random bonus question
    question = BonusQuestion.query.filter_by(category='dinosaurs', is_active=True).first()
    
    if not question:
        return jsonify({'error': 'No dinosaur questions found'}), 404
    
    # Create a test attempt (mark as correct for fun)
    attempt = BonusQuestionAttempt(
        question_id=question.id,
        user_id=user_id,
        guest_code=guest_code,
        selected_answer=question.correct_answer,  # Auto-correct answer
        is_correct=True,
        points_earned=100,
        quiz_topic='test',
        quiz_score=25
    )
    db.session.add(attempt)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': 'Test bonus attempt created!',
        'question': question.correct_answer,
        'attempt_id': attempt.id,
        'hint': 'Now check /api/bonus-question/archive or click the Dino Archive button'
    })


@student_bp.route('/api/bonus-question/archive')
@login_required
def get_bonus_question_archive():
    """Get user's bonus question history for the archive"""
    from sqlalchemy import text
    
    # Check guest_code FIRST (repeat guests have both user_id and guest_code)
    guest_code = session.get('guest_code')
    user_id = session.get('user_id')
    
    # For repeat guests, always use guest_code
    if guest_code:
        user_id = None  # Force guest_code lookup
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated', 'attempts': [], 'total': 0, 'correct': 0})
    
    try:
        # Build query based on user type - guest_code takes priority
        if guest_code:
            query = text("""
                SELECT 
                    bqa.id,
                    bqa.question_id,
                    bqa.selected_answer,
                    bqa.is_correct,
                    bqa.points_earned,
                    bqa.quiz_topic,
                    bqa.quiz_score,
                    bqa.attempted_at,
                    bq.correct_answer,
                    bq.image_url,
                    bq.fun_fact,
                    bq.era_or_region,
                    bq.category
                FROM bonus_question_attempts bqa
                JOIN bonus_questions bq ON bqa.question_id = bq.id
                WHERE bqa.guest_code = :guest_code
                ORDER BY bqa.attempted_at DESC
                LIMIT 100
            """)
            result = db.session.execute(query, {'guest_code': guest_code}).fetchall()
        else:
            query = text("""
                SELECT 
                    bqa.id,
                    bqa.question_id,
                    bqa.selected_answer,
                    bqa.is_correct,
                    bqa.points_earned,
                    bqa.quiz_topic,
                    bqa.quiz_score,
                    bqa.attempted_at,
                    bq.correct_answer,
                    bq.image_url,
                    bq.fun_fact,
                    bq.era_or_region,
                    bq.category
                FROM bonus_question_attempts bqa
                JOIN bonus_questions bq ON bqa.question_id = bq.id
                WHERE bqa.guest_code = :guest_code
                ORDER BY bqa.attempted_at DESC
                LIMIT 100
            """)
            result = db.session.execute(query, {'guest_code': guest_code}).fetchall()
        
        attempts = []
        total_correct = 0
        
        for row in result:
            if row.is_correct:
                total_correct += 1
            
            # Handle attempted_at - might be string from SQLite or datetime object
            attempted_at_str = None
            if row.attempted_at:
                if isinstance(row.attempted_at, str):
                    attempted_at_str = row.attempted_at
                else:
                    attempted_at_str = row.attempted_at.isoformat()
            
            attempts.append({
                'id': row.id,
                'question_id': row.question_id,
                'selected_answer': row.selected_answer,
                'is_correct': bool(row.is_correct),
                'points_earned': row.points_earned,
                'quiz_topic': row.quiz_topic,
                'quiz_score': row.quiz_score,
                'attempted_at': attempted_at_str,
                'correct_answer': row.correct_answer,
                'image_url': row.image_url,
                'fun_fact': row.fun_fact,
                'era_or_region': row.era_or_region,
                'category': row.category
            })
        
        return jsonify({
            'attempts': attempts,
            'total': len(attempts),
            'correct': total_correct
        })
        
    except Exception as e:
        print(f"Error getting bonus question archive: {e}")
        return jsonify({'error': str(e), 'attempts': [], 'total': 0, 'correct': 0})


@student_bp.route('/student/badges')
@login_required
@approved_required
def student_badges_page():
    """Student badges and progress dashboard page"""
    return render_template('student_badges_dashboard.html')

@student_bp.route('/api/class/<int:class_id>/leaderboard')
@login_required
@approved_required
def get_class_leaderboard(class_id):
    """Get leaderboard for a class"""
    # Verify user has access to this class
    user = User.query.get(session['user_id'])

    if user.role == 'teacher':
        # Verify teacher owns this class
        class_obj = Class.query.filter_by(id=class_id, teacher_id=user.id).first()
        if not class_obj:
            return jsonify({'error': 'Unauthorized'}), 403
    elif user.role == 'student':
        # Verify student is in this class
        enrollment = ClassEnrollment.query.filter_by(class_id=class_id, student_id=user.id).first()
        if not enrollment:
            return jsonify({'error': 'Unauthorized'}), 403
    else:
        return jsonify({'error': 'Unauthorized'}), 403

    # Get all students in class
    enrollments = ClassEnrollment.query.filter_by(class_id=class_id).all()
    student_ids = [e.student_id for e in enrollments]

    # Get stats for all students
    students_stats = []
    for student_id in student_ids:
        student = User.query.get(student_id)
        stats = UserStats.query.filter_by(user_id=student_id).first()

        if stats:
            students_stats.append({
                'student_name': student.full_name,
                'student_id': student_id,
                'total_points': stats.total_points,
                'level': stats.level,
                'total_quizzes': stats.total_quizzes,
                'current_streak': stats.current_streak_days,
                'badges_earned': UserBadge.query.filter_by(user_id=student_id).count()
            })

    # Sort by total points
    students_stats.sort(key=lambda x: x['total_points'], reverse=True)

    return jsonify({
        'class_id': class_id,
        'leaderboard': students_stats
    })



# ==================== WHO AM I? API ENDPOINTS ====================

@student_bp.route('/api/debug-session')
def debug_session():
    """Debug endpoint to check session state - REMOVE IN PRODUCTION"""
    return jsonify({
        'user_id': session.get('user_id'),
        'guest_code': session.get('guest_code'),
        'is_guest': session.get('is_guest'),
        'guest_type': session.get('guest_type'),
        'role': session.get('role'),
        'session_keys': list(session.keys())
    })

@student_bp.route('/api/debug-bonus-attempts')
def debug_bonus_attempts():
    """Debug endpoint to check bonus attempts in database"""
    from sqlalchemy import text
    
    guest_code = session.get('guest_code')
    user_id = session.get('user_id')
    
    results = {
        'session_guest_code': guest_code,
        'session_user_id': user_id,
        'attempts_by_guest_code': [],
        'attempts_by_user_id': [],
        'total_in_table': 0
    }
    
    try:
        # Count total attempts
        total = db.session.execute(text("SELECT COUNT(*) FROM bonus_question_attempts")).fetchone()
        results['total_in_table'] = total[0] if total else 0
        
        # Check attempts by guest_code
        if guest_code:
            by_guest = db.session.execute(text("""
                SELECT id, question_id, guest_code, user_id, is_correct, attempted_at 
                FROM bonus_question_attempts 
                WHERE guest_code = :code
                ORDER BY attempted_at DESC
                LIMIT 10
            """), {'code': guest_code}).fetchall()
            
            results['attempts_by_guest_code'] = [
                {'id': r[0], 'question_id': r[1], 'guest_code': r[2], 'user_id': r[3], 'is_correct': r[4], 'attempted_at': str(r[5])}
                for r in by_guest
            ]
        
        # Check attempts by user_id
        if user_id:
            by_user = db.session.execute(text("""
                SELECT id, question_id, guest_code, user_id, is_correct, attempted_at 
                FROM bonus_question_attempts 
                WHERE user_id = :uid
                ORDER BY attempted_at DESC
                LIMIT 10
            """), {'uid': user_id}).fetchall()
            
            results['attempts_by_user_id'] = [
                {'id': r[0], 'question_id': r[1], 'guest_code': r[2], 'user_id': r[3], 'is_correct': r[4], 'attempted_at': str(r[5])}
                for r in by_user
            ]
            
    except Exception as e:
        results['error'] = str(e)
    
    return jsonify(results)

@student_bp.route('/api/who-am-i/start', methods=['POST'])
def who_am_i_start():
    """Initialize a new Who Am I session for a quiz"""
    from sqlalchemy import text

    # Support both regular users and repeat guests
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    print(f"🔍 WHO AM I START - user_id: {user_id}, guest_code: {guest_code}")
    
    if not user_id and not guest_code:
        print("❌ WHO AM I START - No user_id or guest_code in session")
        return jsonify({'error': 'Not logged in'}), 401

    data = request.json
    topic = data.get('topic')
    difficulty = data.get('difficulty')
    quiz_attempt_id = data.get('quiz_attempt_id')
    
    print(f"🔍 WHO AM I START - topic: {topic}, difficulty: {difficulty}, quiz_attempt_id: {quiz_attempt_id}")

    # Get a random active image for this topic/difficulty
    # Now uses the junction table for multi-topic support
    # For adaptive quizzes, try 'adaptive' difficulty first, then fall back to any difficulty
    result = db.session.execute(text("""
        SELECT DISTINCT i.id, i.image_filename, i.answer, i.hint
        FROM who_am_i_images i
        JOIN who_am_i_image_topics t ON i.id = t.image_id
        WHERE t.topic = :topic AND i.difficulty = :difficulty AND i.active = 1
        ORDER BY RANDOM()
        LIMIT 1
    """), {'topic': topic, 'difficulty': difficulty}).fetchone()
    
    # Fallback: if difficulty is 'adaptive' and no images found, try any difficulty
    if not result and difficulty == 'adaptive':
        print(f"🔄 WHO AM I START - No 'adaptive' images, trying any difficulty for topic={topic}")
        result = db.session.execute(text("""
            SELECT DISTINCT i.id, i.image_filename, i.answer, i.hint
            FROM who_am_i_images i
            JOIN who_am_i_image_topics t ON i.id = t.image_id
            WHERE t.topic = :topic AND i.active = 1
            ORDER BY RANDOM()
            LIMIT 1
        """), {'topic': topic}).fetchone()
    
    # Second fallback: if still no images for specific topic, use any available image
    if not result and difficulty == 'adaptive':
        print(f"🔄 WHO AM I START - No images for topic={topic}, trying any available image")
        result = db.session.execute(text("""
            SELECT DISTINCT i.id, i.image_filename, i.answer, i.hint
            FROM who_am_i_images i
            WHERE i.active = 1
            ORDER BY RANDOM()
            LIMIT 1
        """)).fetchone()

    if not result:
        print(f"❌ WHO AM I START - No images found for topic={topic}, difficulty={difficulty}")
        return jsonify({'error': 'No images available for this topic/difficulty'}), 404

    image_id = result.id
    image_filename = result.image_filename
    answer = result.answer
    hint = result.hint
    
    print(f"✅ WHO AM I START - Found image: {image_id}, answer: {answer}")

    # Create session - include guest_code for repeat guests
    # First, ensure guest_code column exists (add it if missing)
    try:
        db.session.execute(text("SELECT guest_code FROM who_am_i_sessions LIMIT 1"))
    except:
        try:
            db.session.execute(text("ALTER TABLE who_am_i_sessions ADD COLUMN guest_code VARCHAR(50)"))
            db.session.commit()
            print("✅ Added guest_code column to who_am_i_sessions")
        except:
            db.session.rollback()
    
    try:
        insert_result = db.session.execute(text("""
            INSERT INTO who_am_i_sessions (user_id, guest_code, quiz_attempt_id, image_id, tiles_revealed, guesses_made)
            VALUES (:user_id, :guest_code, :quiz_attempt_id, :image_id, '[]', 0)
        """), {
            'user_id': user_id,
            'guest_code': guest_code,
            'quiz_attempt_id': quiz_attempt_id,
            'image_id': image_id
        })

        db.session.commit()
        session_id = insert_result.lastrowid
        print(f"✅ WHO AM I START - Created session: {session_id}")
    except Exception as e:
        print(f"❌ WHO AM I START - Error creating session: {e}")
        db.session.rollback()
        return jsonify({'error': f'Database error: {str(e)}'}), 500

    return jsonify({
        'session_id': session_id,
        'image_url': url_for('static', filename=f'who_am_i_images/{image_filename}'),
        'hint': hint,
        'total_tiles': 25
    })


@student_bp.route('/api/who-am-i/reveal', methods=['POST'])
def who_am_i_reveal():
    """Reveal a tile after correct answer"""
    from sqlalchemy import text

    # Support both regular users and repeat guests
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not logged in'}), 401

    data = request.json
    session_id = data.get('session_id')

    # Get current session - match on guest_code for repeat guests, user_id for others
    if guest_code:
        result = db.session.execute(text("""
            SELECT tiles_revealed FROM who_am_i_sessions
            WHERE id = :session_id AND guest_code = :guest_code
        """), {'session_id': session_id, 'guest_code': guest_code}).fetchone()
    else:
        result = db.session.execute(text("""
            SELECT tiles_revealed FROM who_am_i_sessions
            WHERE id = :session_id AND user_id = :user_id AND guest_code IS NULL
        """), {'session_id': session_id, 'user_id': user_id}).fetchone()

    if not result:
        return jsonify({'error': 'Session not found'}), 404

    tiles_revealed = json.loads(result.tiles_revealed)

    # Find next unrevealed tile
    all_tiles = list(range(16))
    available_tiles = [t for t in all_tiles if t not in tiles_revealed]

    if not available_tiles:
        return jsonify({'tiles_revealed': tiles_revealed, 'all_revealed': True})

    # Pick random tile to reveal
    new_tile = random.choice(available_tiles)
    tiles_revealed.append(new_tile)

    # Update session
    db.session.execute(text("""
        UPDATE who_am_i_sessions
        SET tiles_revealed = :tiles
        WHERE id = :session_id
    """), {'tiles': json.dumps(tiles_revealed), 'session_id': session_id})

    db.session.commit()

    return jsonify({
        'tiles_revealed': tiles_revealed,
        'new_tile': new_tile,
        'all_revealed': len(tiles_revealed) >= 25
    })


@student_bp.route('/api/who-am-i/guess', methods=['POST'])
def who_am_i_guess():
    """Submit a guess for Who Am I"""
    from sqlalchemy import text

    # Support both regular users and repeat guests
    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not logged in'}), 401

    data = request.json
    session_id = data.get('session_id')
    guess = data.get('guess', '').strip()

    # Get session and image details - match on guest_code for repeat guests
    if guest_code:
        result = db.session.execute(text("""
            SELECT s.tiles_revealed, s.guesses_made, s.correct_guess, s.quiz_attempt_id,
                   i.answer, i.accepted_answers
            FROM who_am_i_sessions s
            JOIN who_am_i_images i ON s.image_id = i.id
            WHERE s.id = :session_id AND s.guest_code = :guest_code
        """), {'session_id': session_id, 'guest_code': guest_code}).fetchone()
    else:
        result = db.session.execute(text("""
            SELECT s.tiles_revealed, s.guesses_made, s.correct_guess, s.quiz_attempt_id,
                   i.answer, i.accepted_answers
            FROM who_am_i_sessions s
            JOIN who_am_i_images i ON s.image_id = i.id
            WHERE s.id = :session_id AND s.user_id = :user_id AND s.guest_code IS NULL
        """), {'session_id': session_id, 'user_id': user_id}).fetchone()

    if not result:
        return jsonify({'error': 'Session not found'}), 404

    tiles_revealed = json.loads(result.tiles_revealed)
    guesses_made = result.guesses_made
    correct_guess = result.correct_guess
    quiz_attempt_id = result.quiz_attempt_id  # NOW IT'S RETRIEVED!
    correct_answer = result.answer
    accepted_answers_json = result.accepted_answers

    # Check if already guessed correctly
    if correct_guess:
        return jsonify({'error': 'Already guessed correctly'}), 400

    # Check guess limit
    if guesses_made >= 3:
        return jsonify({'error': 'No guesses remaining', 'correct': False, 'answer': correct_answer}), 400

    # Flexible answer checking with variants
    # Parse accepted answers
    accepted_answers = []
    if accepted_answers_json:
        try:
            accepted_answers = json.loads(accepted_answers_json)
        except:
            pass

    # If no variants defined, fall back to original answer only
    if not accepted_answers:
        accepted_answers = [correct_answer.lower().strip()]

    # Normalize guess
    guess_normalized = guess.lower().strip()

    # Check if guess matches any accepted variant
    is_correct = guess_normalized in [a.lower().strip() for a in accepted_answers]
    guesses_made += 1

    # Calculate bonus points if correct
    bonus_points = 0
    if is_correct:
        tiles_hidden = 25 - len(tiles_revealed)  # 5×5 grid = 25 tiles
        if tiles_hidden >= 20:      # Guessed with 80%+ hidden (very early)
            bonus_points = 100
        elif tiles_hidden >= 15:    # Guessed with 60-79% hidden (early)
            bonus_points = 75
        elif tiles_hidden >= 10:    # Guessed with 40-59% hidden (moderate)
            bonus_points = 50
        elif tiles_hidden >= 5:     # Guessed with 20-39% hidden (late)
            bonus_points = 25
        else:                        # Less than 5 tiles hidden (very late)
            bonus_points = 10

        # Update session
        db.session.execute(text("""
            UPDATE who_am_i_sessions
            SET guesses_made = :guesses, correct_guess = 1, bonus_points_earned = :bonus, completed_at = CURRENT_TIMESTAMP
            WHERE id = :session_id
        """), {'guesses': guesses_made, 'bonus': bonus_points, 'session_id': session_id})
    else:
        # Just increment guesses
        db.session.execute(text("""
            UPDATE who_am_i_sessions
            SET guesses_made = :guesses
            WHERE id = :session_id
        """), {'guesses': guesses_made, 'session_id': session_id})

    db.session.commit()

    # If correct, try to load another image automatically
    next_session_data = None
    if is_correct:
        try:
            # Get topic/difficulty - prefer from request (for adaptive quiz), fall back to quiz_attempts
            request_topic = data.get('topic')
            request_difficulty = data.get('difficulty')
            
            quiz_topic = None
            quiz_difficulty = None
            
            if request_topic and request_difficulty:
                # Use values from request (adaptive quiz passes these directly)
                quiz_topic = request_topic
                quiz_difficulty = request_difficulty
                print(f"🔍 Using topic/difficulty from request: {quiz_topic}, {quiz_difficulty}")
            else:
                # Fall back to quiz_attempts lookup (regular quiz)
                quiz_info = db.session.execute(text("""
                    SELECT topic, difficulty FROM quiz_attempts WHERE id = :quiz_id
                """), {'quiz_id': quiz_attempt_id}).fetchone()
                
                if quiz_info:
                    quiz_topic = quiz_info.topic
                    quiz_difficulty = quiz_info.difficulty
                    print(f"🔍 Using topic/difficulty from quiz_attempts: {quiz_topic}, {quiz_difficulty}")

            print(f"🔍 Looking for next image - quiz_id: {quiz_attempt_id}, topic: {quiz_topic}, difficulty: {quiz_difficulty}")

            if quiz_topic:
                # Get list of images already shown in this quiz
                shown_images = db.session.execute(text("""
                    SELECT image_id FROM who_am_i_sessions
                    WHERE quiz_attempt_id = :quiz_id
                """), {'quiz_id': quiz_attempt_id}).fetchall()

                shown_image_ids = [row.image_id for row in shown_images]
                print(f"🚫 Already shown image IDs: {shown_image_ids}")

                # Build query to exclude already-shown images
                if shown_image_ids:
                    # Create string of IDs for NOT IN clause
                    id_list = ','.join([str(id) for id in shown_image_ids])

                    print(f"🔎 Searching with: topic={quiz_topic}, difficulty={quiz_difficulty}, excluding IDs: {id_list}")

                    next_image = db.session.execute(text(f"""
                        SELECT DISTINCT i.id, i.image_filename, i.answer, i.hint
                        FROM who_am_i_images i
                        JOIN who_am_i_image_topics t ON i.id = t.image_id
                        WHERE t.topic = :topic
                        AND LOWER(i.difficulty) = LOWER(:difficulty)
                        AND i.active = 1
                        AND i.id NOT IN ({id_list})
                        ORDER BY RANDOM()
                        LIMIT 1
                    """), {
                        'topic': quiz_topic,
                        'difficulty': quiz_difficulty
                    }).fetchone()
                    
                    # FALLBACK: If 'adaptive' difficulty, try ANY difficulty for this topic
                    if not next_image and quiz_difficulty == 'adaptive':
                        print(f"🔄 No 'adaptive' images, trying any difficulty for topic={quiz_topic}")
                        next_image = db.session.execute(text(f"""
                            SELECT DISTINCT i.id, i.image_filename, i.answer, i.hint
                            FROM who_am_i_images i
                            JOIN who_am_i_image_topics t ON i.id = t.image_id
                            WHERE t.topic = :topic
                            AND i.active = 1
                            AND i.id NOT IN ({id_list})
                            ORDER BY RANDOM()
                            LIMIT 1
                        """), {
                            'topic': quiz_topic
                        }).fetchone()
                    
                    # FALLBACK 2: Try ANY active image not yet shown
                    if not next_image and quiz_difficulty == 'adaptive':
                        print(f"🔄 No topic images, trying any active image")
                        next_image = db.session.execute(text(f"""
                            SELECT DISTINCT i.id, i.image_filename, i.answer, i.hint
                            FROM who_am_i_images i
                            WHERE i.active = 1
                            AND i.id NOT IN ({id_list})
                            ORDER BY RANDOM()
                            LIMIT 1
                        """)).fetchone()
                else:
                    print(f"🔎 First image search with: topic={quiz_topic}, difficulty={quiz_difficulty}")
                    # First image, get any
                    next_image = db.session.execute(text("""
                        SELECT DISTINCT i.id, i.image_filename, i.answer, i.hint
                        FROM who_am_i_images i
                        JOIN who_am_i_image_topics t ON i.id = t.image_id
                        WHERE t.topic = :topic
                        AND LOWER(i.difficulty) = LOWER(:difficulty)
                        AND i.active = 1
                        ORDER BY RANDOM()
                        LIMIT 1
                    """), {
                        'topic': quiz_topic,
                        'difficulty': quiz_difficulty
                    }).fetchone()
                    
                    # FALLBACK for first image too
                    if not next_image and quiz_difficulty == 'adaptive':
                        next_image = db.session.execute(text("""
                            SELECT DISTINCT i.id, i.image_filename, i.answer, i.hint
                            FROM who_am_i_images i
                            WHERE i.active = 1
                            ORDER BY RANDOM()
                            LIMIT 1
                        """)).fetchone()

                if next_image:
                    print(f"✅ Next image found! ID: {next_image.id}, Answer: {next_image.answer}")
                    # Create new session for next image - include guest_code for repeat guests
                    new_session = db.session.execute(text("""
                        INSERT INTO who_am_i_sessions (user_id, guest_code, quiz_attempt_id, image_id, tiles_revealed, guesses_made)
                        VALUES (:user_id, :guest_code, :quiz_attempt_id, :image_id, '[]', 0)
                    """), {
                        'user_id': user_id,
                        'guest_code': guest_code,
                        'quiz_attempt_id': quiz_attempt_id,
                        'image_id': next_image.id
                    })
                    db.session.commit()

                    next_session_data = {
                        'session_id': new_session.lastrowid,
                        'image_url': url_for('static', filename=f'who_am_i_images/{next_image.image_filename}'),
                        'hint': next_image.hint,
                        'total_tiles': 25
                    }
                    print(f"✅ New session created: {new_session.lastrowid}")
                else:
                    print(f"ℹ️ No more images available for topic={quiz_topic}, difficulty={quiz_difficulty}")
        except Exception as e:
            # Log error but don't break the guess response
            print(f"❌ Error loading next Who Am I image: {e}")
            import traceback
            traceback.print_exc()

    response_data = {
        'correct': is_correct,
        'bonus_points': bonus_points,
        'guesses_remaining': 3 - guesses_made,
        'answer': correct_answer if is_correct or guesses_made >= 3 else None
    }

    # Add next session info if available
    if next_session_data:
        response_data['next_session'] = next_session_data

    return jsonify(response_data)


# ==================== AVATAR SYSTEM ROUTES ====================
# All avatar routes check FEATURE_FLAGS before executing
# BACKOUT: Set AVATAR_SYSTEM_ENABLED=false to disable all routes

@student_bp.route('/avatar/shop')
def avatar_shop_page():
    """Avatar customization shop page"""
    if not FEATURE_FLAGS.get('AVATAR_SYSTEM_ENABLED', False):
        flash('Avatar shop is currently unavailable', 'warning')
        return redirect('/app')  # student_app is in main app.py

    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    is_casual_guest = session.get('is_guest', False)

    if not user_id and not guest_code:
        flash('Please log in to access the avatar shop', 'warning')
        return redirect(url_for('auth.login'))

    # Get user info based on user type
    user_name = None
    display_name = None

    if guest_code:
        # Repeat guest with animal code - use guest_code as name
        display_name = guest_code
    elif is_casual_guest:
        # Casual guest (Quick Try) - show generic name
        display_name = "Quick Try Guest"
    elif user_id:
        # Regular registered user
        user = User.query.get(user_id)
        user_name = user.full_name if user else None
        display_name = user_name

    # Get points - prioritize guest_code for repeat guests
    if guest_code:
        points, level = get_avatar_user_points(None, guest_code)
    elif user_id and not is_casual_guest:
        points, level = get_avatar_user_points(user_id, None)
    else:
        # Casual guests don't have persistent points for avatar shop
        points, level = 0, 1

    return render_template('avatar_shop.html',
        user_name=display_name,
        guest_code=guest_code,
        points=points,
        level=level,
        is_casual_guest=is_casual_guest
    )

@student_bp.route('/api/avatar/items', methods=['GET'])
def api_avatar_items():
    """Get all available shop items"""
    if not FEATURE_FLAGS.get('AVATAR_SYSTEM_ENABLED', False):
        return jsonify({'success': False, 'message': 'Avatar system disabled'}), 503

    item_type = request.args.get('type')  # Optional filter

    query = AvatarItem.query.filter_by(is_active=True)
    if item_type:
        query = query.filter_by(item_type=item_type)

    items = query.order_by(AvatarItem.sort_order).all()

    return jsonify({
        'success': True,
        'items': [item.to_dict() for item in items]
    })

@student_bp.route('/api/avatar/inventory', methods=['GET'])
def api_avatar_inventory():
    """Get current user's inventory and points"""
    if not FEATURE_FLAGS.get('AVATAR_SYSTEM_ENABLED', False):
        return jsonify({'success': False, 'message': 'Avatar system disabled'}), 503

    user_id = session.get('user_id')
    guest_code = session.get('guest_code')
    is_casual_guest = session.get('is_guest', False)

    if not user_id and not guest_code:
        return jsonify({
            'success': False,
            'message': 'Not logged in',
            'inventory': [],
            'points': 0
        })

    # Get inventory based on user type
    query = UserAvatarInventory.query
    if guest_code:
        # Repeat guest - use guest_code
        query = query.filter_by(guest_code=guest_code)
        points, level = get_avatar_user_points(None, guest_code)
    elif user_id and not is_casual_guest:
        # Regular registered user
        query = query.filter_by(user_id=user_id)
        points, level = get_avatar_user_points(user_id, None)
    else:
        # Casual guest - no persistent inventory or points
        return jsonify({
            'success': True,
            'inventory': [],
            'points': 0,
            'level': 1,
            'is_casual_guest': True
        })

    inventory = query.all()

    return jsonify({
        'success': True,
        'inventory': [inv.to_dict() for inv in inventory],
        'points': points,
        'level': level
    })

@student_bp.route('/api/avatar/equipped', methods=['GET'])
def api_avatar_equipped():
    """Get currently equipped avatar configuration"""
    if not FEATURE_FLAGS.get('AVATAR_SYSTEM_ENABLED', False):
        return jsonify({'success': False, 'message': 'Avatar system disabled'}), 503

    user_id = session.get('user_id')
    guest_code = session.get('guest_code')

    # DEBUG: Log what we're looking for
    print(f"🔍 api_avatar_equipped called: user_id={user_id}, guest_code={guest_code}")

    equipped = get_equipped_avatar(user_id, guest_code)

    # DEBUG: Log what we found
    print(f"🎭 Returning equipped: {equipped}")

    return jsonify({
        'success': True,
        'equipped': equipped,
        '_debug': {
            'session_user_id': user_id,
            'session_guest_code': guest_code
        }
    })

@student_bp.route('/api/avatar/purchase', methods=['POST'])
def api_avatar_purchase():
    """Purchase an item"""
    if not FEATURE_FLAGS.get('AVATAR_SYSTEM_ENABLED', False):
        return jsonify({'success': False, 'message': 'Avatar system disabled'}), 503

    if not FEATURE_FLAGS.get('AVATAR_SHOP_ENABLED', False):
        return jsonify({'success': False, 'message': 'Avatar shop disabled'}), 503

    user_id = session.get('user_id')
    guest_code = session.get('guest_code')

    if not user_id and not guest_code:
        return jsonify({'success': False, 'message': 'You must be logged in to purchase items'}), 401

    data = request.get_json()
    item_id = data.get('item_id')

    if not item_id:
        return jsonify({'success': False, 'message': 'Item ID is required'}), 400

    # Get the item
    item = AvatarItem.query.get(item_id)
    if not item:
        return jsonify({'success': False, 'message': 'Item not found'}), 404

    if not item.is_active:
        return jsonify({'success': False, 'message': 'Item is not available'}), 400

    # Check if already owned
    if avatar_owns_item(item_id, user_id, guest_code):
        return jsonify({'success': False, 'message': 'You already own this item'}), 400

    # Check if it's a free/default item
    if item.is_default or item.point_cost == 0:
        # Just add to inventory, no points needed
        inventory_entry = UserAvatarInventory(
            user_id=user_id,
            guest_code=guest_code,
            item_id=item_id
        )
        db.session.add(inventory_entry)
        db.session.commit()
        return jsonify({
            'success': True,
            'message': f"Added {item.display_name} to your collection!",
            'new_points': None
        })

    # Get current points
    current_points, _ = get_avatar_user_points(user_id, guest_code)

    # Check if enough points
    if current_points < item.point_cost:
        return jsonify({
            'success': False,
            'message': f"Not enough points. You need {item.point_cost} but have {current_points}"
        }), 400

    # Deduct points
    from sqlalchemy import text
    new_points = current_points - item.point_cost

    # Deduct from correct table (guest_code takes priority)
    if guest_code:
        db.session.execute(text(
            "UPDATE guest_users SET total_score = :points WHERE guest_code = :code"
        ), {"points": new_points, "code": guest_code})
    elif user_id:
        db.session.execute(text(
            "UPDATE user_stats SET total_points = :points WHERE user_id = :uid"
        ), {"points": new_points, "uid": user_id})

    # Add to inventory (store both for tracking, but guest_code is primary for guests)
    inventory_entry = UserAvatarInventory(
        user_id=user_id if not guest_code else None,  # Only set user_id for actual registered users
        guest_code=guest_code,
        item_id=item_id
    )
    db.session.add(inventory_entry)

    # AUTO-EQUIP: Automatically equip the purchased item
    print(f"🛒 AUTO-EQUIP: user_id={user_id}, guest_code={guest_code}, item_type={item.item_type}, item_key={item.item_key}")

    if guest_code:
        equipped = UserAvatarEquipped.query.filter_by(guest_code=guest_code).first()
        print(f"🔍 Found equipped for guest_code={guest_code}: {equipped}")
        if not equipped:
            equipped = UserAvatarEquipped(guest_code=guest_code)
            db.session.add(equipped)
            print(f"📝 Created new equipped record for guest_code={guest_code}")
    elif user_id:
        equipped = UserAvatarEquipped.query.filter_by(user_id=user_id).first()
        print(f"🔍 Found equipped for user_id={user_id}: {equipped}")
        if not equipped:
            equipped = UserAvatarEquipped(user_id=user_id)
            db.session.add(equipped)
            print(f"📝 Created new equipped record for user_id={user_id}")
    else:
        equipped = None

    # Set the appropriate slot based on item type
    if equipped:
        print(f"📝 Before equip: animal={equipped.animal_key}, hat={equipped.hat_key}, glasses={equipped.glasses_key}")
        if item.item_type == 'animal':
            equipped.animal_key = item.item_key
        elif item.item_type == 'hat':
            equipped.hat_key = item.item_key
        elif item.item_type == 'glasses':
            equipped.glasses_key = item.item_key
        elif item.item_type == 'background':
            equipped.background_key = item.item_key
        elif item.item_type == 'accessory':
            equipped.accessory_key = item.item_key
        equipped.updated_at = datetime.utcnow()
        print(f"📝 After equip: animal={equipped.animal_key}, hat={equipped.hat_key}, glasses={equipped.glasses_key}")

    # Log the purchase
    purchase_log = AvatarPurchaseLog(
        user_id=user_id,
        guest_code=guest_code,
        item_id=item_id,
        points_spent=item.point_cost,
        points_before=current_points,
        points_after=new_points
    )
    db.session.add(purchase_log)

    db.session.commit()

    return jsonify({
        'success': True,
        'message': f"Purchased {item.display_name} for {item.point_cost} points!",
        'new_points': new_points
    })

@student_bp.route('/api/avatar/equip', methods=['POST'])
def api_avatar_equip():
    """Equip an item"""
    if not FEATURE_FLAGS.get('AVATAR_SYSTEM_ENABLED', False):
        return jsonify({'success': False, 'message': 'Avatar system disabled'}), 503

    user_id = session.get('user_id')
    guest_code = session.get('guest_code')

    if not user_id and not guest_code:
        return jsonify({'success': False, 'message': 'You must be logged in to equip items'}), 401

    data = request.get_json()
    item_type = data.get('item_type')
    item_key = data.get('item_key')

    if not item_type or not item_key:
        return jsonify({'success': False, 'message': 'Item type and key are required'}), 400

    # Verify item exists
    item = AvatarItem.query.filter_by(
        item_type=item_type,
        item_key=item_key
    ).first()

    if not item:
        return jsonify({'success': False, 'message': 'Item not found'}), 404

    # Check ownership (default items are always available)
    if not item.is_default and not avatar_owns_item(item.id, user_id, guest_code):
        return jsonify({'success': False, 'message': "You don't own this item"}), 400

    # Get or create equipped record (guest_code takes priority)
    if guest_code:
        equipped = UserAvatarEquipped.query.filter_by(guest_code=guest_code).first()
        if not equipped:
            equipped = UserAvatarEquipped(guest_code=guest_code)
            db.session.add(equipped)
    elif user_id:
        equipped = UserAvatarEquipped.query.filter_by(user_id=user_id).first()
        if not equipped:
            equipped = UserAvatarEquipped(user_id=user_id)
            db.session.add(equipped)
    else:
        return jsonify({'success': False, 'message': 'No user or guest identified'}), 400

    # Update the appropriate slot
    if item_type == 'animal':
        equipped.animal_key = item_key
    elif item_type == 'hat':
        equipped.hat_key = item_key
    elif item_type == 'glasses':
        equipped.glasses_key = item_key
    elif item_type == 'background':
        equipped.background_key = item_key
    elif item_type == 'accessory':
        equipped.accessory_key = item_key
    else:
        return jsonify({'success': False, 'message': f'Unknown item type: {item_type}'}), 400

    equipped.updated_at = datetime.utcnow()
    db.session.commit()

    return jsonify({
        'success': True,
        'message': f"Equipped {item.display_name}!"
    })

@student_bp.route('/api/avatar/grant-defaults', methods=['POST'])
def api_avatar_grant_defaults():
    """Grant default items to current user (call on first login)"""
    if not FEATURE_FLAGS.get('AVATAR_SYSTEM_ENABLED', False):
        return jsonify({'success': False, 'message': 'Avatar system disabled'}), 503

    user_id = session.get('user_id')
    guest_code = session.get('guest_code')

    if not user_id and not guest_code:
        return jsonify({'success': False, 'message': 'Not logged in'}), 401

    grant_default_avatar_items(user_id, guest_code)

    return jsonify({
        'success': True,
        'message': 'Default items granted'
    })

