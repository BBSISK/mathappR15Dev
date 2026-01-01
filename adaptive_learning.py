"""
Adaptive Learning System - Core Module
=======================================
Contains all algorithms and functions for the adaptive learning system.

To use, import the functions you need:
    from adaptive_learning import (
        calculate_mastery_level,
        update_spaced_repetition,
        get_recommended_difficulty,
        get_learning_recommendations,
        update_after_quiz
    )
"""

import json
import statistics
from datetime import datetime, timedelta
from functools import lru_cache

# ============================================================================
# CONFIGURATION
# ============================================================================

ADAPTIVE_CONFIG = {
    # Mastery thresholds
    'MASTERY_THRESHOLD': 0.85,          # 85% to be considered mastered
    'PROMOTION_THRESHOLD': 0.80,        # 80% to move up difficulty
    'DEMOTION_THRESHOLD': 0.40,         # Below 40% to move down
    'MIN_ATTEMPTS_PROMOTION': 20,       # Min questions before promotion
    'MIN_ATTEMPTS_DEMOTION': 10,        # Min questions before demotion
    
    # Spaced repetition (SM-2 algorithm)
    'INITIAL_REVIEW_INTERVAL': 1,       # Days
    'MAX_REVIEW_INTERVAL': 90,          # Days
    'EASE_FACTOR_DEFAULT': 2.5,
    'EASE_FACTOR_MIN': 1.3,
    
    # Recommendations
    'MAX_DAILY_RECOMMENDATIONS': 5,
    'RECOMMENDATION_EXPIRY_HOURS': 24,
    
    # Performance tracking
    'RECENT_SCORES_WINDOW': 10,         # Last N attempts for weighting
    'RECENCY_DECAY_RATE': 0.02,         # Per day
    
    # Feature flag
    'ENABLED': True,
}

# ============================================================================
# MASTERY CALCULATION
# ============================================================================

def calculate_mastery_level(total_attempts, correct_attempts, recent_scores=None, 
                            days_since_practice=0):
    """
    Calculate mastery level for a topic/difficulty combination.
    
    Args:
        total_attempts: Total questions attempted
        correct_attempts: Total correct answers
        recent_scores: List of recent scores (0.0-1.0) from most to least recent
        days_since_practice: Days since last practice session
    
    Returns:
        float: Mastery level from 0.0 to 1.0
    """
    if total_attempts == 0:
        return 0.0
    
    # Base accuracy
    base_accuracy = correct_attempts / total_attempts
    
    # Weight recent performance more heavily (exponential decay)
    if recent_scores and len(recent_scores) > 0:
        weights = [0.9 ** i for i in range(len(recent_scores))]
        weighted_recent = sum(s * w for s, w in zip(recent_scores, weights))
        weighted_recent /= sum(weights)
        # Blend: 30% historical, 70% recent
        base_accuracy = 0.3 * base_accuracy + 0.7 * weighted_recent
    
    # Consistency factor (penalise high variance)
    if recent_scores and len(recent_scores) >= 3:
        try:
            std_dev = statistics.stdev(recent_scores)
            consistency = max(0.7, 1 - std_dev)
        except:
            consistency = 0.85
    else:
        consistency = 0.85
    
    # Recency decay (slight penalty for not practicing)
    recency = max(0.8, 1 - (days_since_practice * ADAPTIVE_CONFIG['RECENCY_DECAY_RATE']))
    
    mastery = base_accuracy * consistency * recency
    return min(1.0, max(0.0, mastery))


def calculate_confidence_score(total_attempts, recent_scores=None):
    """
    Calculate confidence in the mastery level estimate.
    
    More attempts and consistent recent performance = higher confidence.
    
    Args:
        total_attempts: Total questions attempted
        recent_scores: List of recent scores
    
    Returns:
        float: Confidence score from 0.0 to 1.0
    """
    # Base confidence from attempt count (logarithmic growth)
    if total_attempts == 0:
        return 0.0
    
    attempt_confidence = min(1.0, (total_attempts / 50) ** 0.5)
    
    # Consistency confidence
    if recent_scores and len(recent_scores) >= 3:
        try:
            std_dev = statistics.stdev(recent_scores)
            consistency_confidence = max(0.5, 1 - std_dev * 2)
        except:
            consistency_confidence = 0.5
    else:
        consistency_confidence = 0.5
    
    return (attempt_confidence * 0.6 + consistency_confidence * 0.4)


# ============================================================================
# SPACED REPETITION (SM-2 Algorithm)
# ============================================================================

def update_spaced_repetition(mastery_record, score_percentage):
    """
    Update spaced repetition scheduling based on quiz performance.
    Uses modified SM-2 algorithm.
    
    Args:
        mastery_record: TopicMastery object (will be modified in place)
        score_percentage: Quiz score as percentage (0-100)
    
    Returns:
        dict: Updated values for the mastery record
    """
    # Convert to quality rating (0-5 scale for SM-2)
    quality = min(5, max(0, int(score_percentage / 20)))
    
    # Get current values with defaults
    current_interval = getattr(mastery_record, 'review_interval_days', 1) or 1
    current_ease = getattr(mastery_record, 'ease_factor', 2.5) or 2.5
    
    if quality >= 3:  # Correct/Good response
        if current_interval <= 1:
            new_interval = 1
        elif current_interval <= 3:
            new_interval = 3
        else:
            new_interval = int(current_interval * current_ease)
        
        # Update ease factor
        new_ease = current_ease + 0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)
        new_ease = max(ADAPTIVE_CONFIG['EASE_FACTOR_MIN'], new_ease)
    else:
        # Poor performance - reset
        new_interval = 1
        new_ease = max(ADAPTIVE_CONFIG['EASE_FACTOR_MIN'], current_ease - 0.2)
    
    # Cap maximum interval
    new_interval = min(ADAPTIVE_CONFIG['MAX_REVIEW_INTERVAL'], new_interval)
    
    # Calculate next review date
    next_review = datetime.utcnow() + timedelta(days=new_interval)
    
    return {
        'review_interval_days': new_interval,
        'ease_factor': round(new_ease, 2),
        'next_review_at': next_review
    }


def get_due_for_review(user_id, db_session, limit=10):
    """
    Get topics that are due for review based on spaced repetition.
    
    Args:
        user_id: User ID
        db_session: SQLAlchemy database session
        limit: Maximum number to return
    
    Returns:
        list: TopicMastery records due for review
    """
    from sqlalchemy import text
    
    now = datetime.utcnow()
    
    result = db_session.execute(text("""
        SELECT * FROM topic_mastery 
        WHERE user_id = :user_id 
        AND next_review_at IS NOT NULL 
        AND next_review_at <= :now
        AND mastery_level > 0
        ORDER BY next_review_at ASC
        LIMIT :limit
    """), {'user_id': user_id, 'now': now, 'limit': limit})
    
    return result.fetchall()


# ============================================================================
# ADAPTIVE DIFFICULTY SELECTION
# ============================================================================

def get_recommended_difficulty(user_id, topic, db_session):
    """
    Get the recommended difficulty level for a user on a specific topic.
    
    Args:
        user_id: User ID
        topic: Topic identifier
        db_session: SQLAlchemy database session
    
    Returns:
        str: Recommended difficulty ('beginner', 'intermediate', 'advanced')
    """
    from sqlalchemy import text
    
    # Get mastery records for all difficulties on this topic
    result = db_session.execute(text("""
        SELECT difficulty, mastery_level, total_attempts, streak_current
        FROM topic_mastery 
        WHERE user_id = :user_id AND topic = :topic
    """), {'user_id': user_id, 'topic': topic})
    
    records = {row[0]: {
        'mastery': row[1], 
        'attempts': row[2], 
        'streak': row[3]
    } for row in result.fetchall()}
    
    # No history - start at beginner
    if not records:
        return 'beginner'
    
    config = ADAPTIVE_CONFIG
    
    # Check promotion criteria (move UP)
    difficulty_order = ['beginner', 'intermediate', 'advanced']
    
    for i, level in enumerate(difficulty_order[:-1]):  # Skip advanced (can't promote from it)
        if level in records:
            r = records[level]
            next_level = difficulty_order[i + 1]
            
            # Ready for promotion?
            if (r['mastery'] >= config['PROMOTION_THRESHOLD'] and 
                r['attempts'] >= config['MIN_ATTEMPTS_PROMOTION'] and
                r['streak'] >= 3):
                
                # Only promote if next level not already strong
                if next_level not in records or records[next_level]['mastery'] < 0.60:
                    return next_level
    
    # Check demotion criteria (move DOWN)
    for i in range(len(difficulty_order) - 1, 0, -1):  # Skip beginner (can't demote from it)
        level = difficulty_order[i]
        if level in records:
            r = records[level]
            prev_level = difficulty_order[i - 1]
            
            # Should demote?
            if (r['mastery'] < config['DEMOTION_THRESHOLD'] and 
                r['attempts'] >= config['MIN_ATTEMPTS_DEMOTION']):
                return prev_level
    
    # Stay at current best level
    if 'advanced' in records and records['advanced']['mastery'] >= 0.50:
        return 'advanced'
    elif 'intermediate' in records and records['intermediate']['mastery'] >= 0.50:
        return 'intermediate'
    
    return 'beginner'


def check_prerequisites_met(user_id, topic, db_session, target_mastery=0.7):
    """
    Check if user has met prerequisites for a topic.
    
    Args:
        user_id: User ID
        topic: Topic to check prerequisites for
        db_session: SQLAlchemy database session
        target_mastery: Minimum mastery level required (default 0.7)
    
    Returns:
        tuple: (bool, list) - (prerequisites_met, list of unmet prerequisites)
    """
    from sqlalchemy import text
    
    # Get prerequisites for this topic
    prereq_result = db_session.execute(text("""
        SELECT prerequisite_topic, required_mastery_level 
        FROM skill_prerequisites 
        WHERE topic = :topic
    """), {'topic': topic})
    
    prerequisites = prereq_result.fetchall()
    
    if not prerequisites:
        return True, []
    
    unmet = []
    
    for prereq_topic, required_level in prerequisites:
        # Check user's mastery on prerequisite topic (best across all difficulties)
        mastery_result = db_session.execute(text("""
            SELECT MAX(mastery_level) 
            FROM topic_mastery 
            WHERE user_id = :user_id AND topic = :topic
        """), {'user_id': user_id, 'topic': prereq_topic})
        
        row = mastery_result.fetchone()
        user_mastery = row[0] if row and row[0] else 0.0
        
        if user_mastery < (required_level or target_mastery):
            unmet.append({
                'topic': prereq_topic,
                'required': required_level or target_mastery,
                'current': user_mastery
            })
    
    return len(unmet) == 0, unmet


# ============================================================================
# LEARNING RECOMMENDATIONS
# ============================================================================

def generate_recommendations(user_id, db_session, max_recommendations=5):
    """
    Generate personalised learning recommendations for a user.
    
    Args:
        user_id: User ID
        db_session: SQLAlchemy database session
        max_recommendations: Maximum recommendations to generate
    
    Returns:
        list: List of recommendation dicts
    """
    from sqlalchemy import text
    
    recommendations = []
    now = datetime.utcnow()
    expiry = now + timedelta(hours=ADAPTIVE_CONFIG['RECOMMENDATION_EXPIRY_HOURS'])
    
    # 1. Review recommendations (topics due for spaced repetition)
    review_due = db_session.execute(text("""
        SELECT topic, difficulty, mastery_level, next_review_at
        FROM topic_mastery 
        WHERE user_id = :user_id 
        AND next_review_at <= :now
        AND mastery_level >= 0.5
        ORDER BY next_review_at ASC
        LIMIT 3
    """), {'user_id': user_id, 'now': now})
    
    for row in review_due:
        days_overdue = (now - row[3]).days if row[3] else 0
        recommendations.append({
            'type': 'review',
            'topic': row[0],
            'difficulty': row[1],
            'priority': 1,
            'reason': f"Review needed - last practiced {days_overdue} days ago",
            'expires_at': expiry
        })
    
    # 2. Practice recommendations (topics where struggling)
    struggling = db_session.execute(text("""
        SELECT topic, difficulty, mastery_level
        FROM topic_mastery 
        WHERE user_id = :user_id 
        AND mastery_level > 0 
        AND mastery_level < 0.5
        AND total_attempts >= 5
        ORDER BY mastery_level ASC
        LIMIT 2
    """), {'user_id': user_id})
    
    for row in struggling:
        recommendations.append({
            'type': 'practice',
            'topic': row[0],
            'difficulty': row[1],
            'priority': 2,
            'reason': f"Need practice - current mastery {int(row[2]*100)}%",
            'expires_at': expiry
        })
    
    # 3. New topic recommendations (topics with prerequisites met but not started)
    # This is more complex - we need to check prerequisites
    if len(recommendations) < max_recommendations:
        # Get all topics user hasn't started
        all_topics_result = db_session.execute(text("""
            SELECT DISTINCT topic FROM questions
        """))
        all_topics = [row[0] for row in all_topics_result]
        
        started_result = db_session.execute(text("""
            SELECT DISTINCT topic FROM topic_mastery WHERE user_id = :user_id
        """), {'user_id': user_id})
        started_topics = [row[0] for row in started_result]
        
        not_started = [t for t in all_topics if t not in started_topics]
        
        for topic in not_started[:3]:
            prereqs_met, unmet = check_prerequisites_met(user_id, topic, db_session)
            if prereqs_met:
                recommendations.append({
                    'type': 'new_topic',
                    'topic': topic,
                    'difficulty': 'beginner',
                    'priority': 3,
                    'reason': "Ready to start - prerequisites met",
                    'expires_at': expiry
                })
                if len(recommendations) >= max_recommendations:
                    break
    
    # Sort by priority
    recommendations.sort(key=lambda x: x['priority'])
    
    return recommendations[:max_recommendations]


def get_smart_quiz_selection(user_id, db_session, mode='auto'):
    """
    Intelligently select topic and difficulty for a quiz.
    
    Args:
        user_id: User ID
        db_session: SQLAlchemy database session
        mode: Selection mode
            - 'auto': Balanced selection
            - 'review': Prioritise spaced repetition reviews
            - 'practice': Focus on weak areas
            - 'challenge': Push to harder topics/difficulties
    
    Returns:
        dict: {topic, difficulty, reason}
    """
    recommendations = generate_recommendations(user_id, db_session)
    
    if not recommendations:
        # Default recommendation for new users
        return {
            'topic': 'arithmetic',
            'difficulty': 'beginner',
            'reason': 'Start with the fundamentals'
        }
    
    if mode == 'review':
        # Prioritise review recommendations
        for rec in recommendations:
            if rec['type'] == 'review':
                return {
                    'topic': rec['topic'],
                    'difficulty': rec['difficulty'],
                    'reason': rec['reason']
                }
    
    elif mode == 'practice':
        # Prioritise struggling areas
        for rec in recommendations:
            if rec['type'] == 'practice':
                return {
                    'topic': rec['topic'],
                    'difficulty': rec['difficulty'],
                    'reason': rec['reason']
                }
    
    elif mode == 'challenge':
        # Find topic where user can be promoted
        for rec in recommendations:
            if rec['type'] == 'new_topic':
                return {
                    'topic': rec['topic'],
                    'difficulty': 'intermediate',  # Start higher
                    'reason': 'Challenge yourself with a new topic'
                }
    
    # Default: return highest priority recommendation
    rec = recommendations[0]
    return {
        'topic': rec['topic'],
        'difficulty': rec['difficulty'],
        'reason': rec['reason']
    }


# ============================================================================
# QUIZ INTEGRATION
# ============================================================================

def update_after_quiz(user_id, topic, difficulty, score, total_questions, 
                      time_taken, db_session, question_results=None):
    """
    Update all adaptive learning data after a quiz is completed.
    
    Args:
        user_id: User ID
        topic: Quiz topic
        difficulty: Quiz difficulty
        score: Questions answered correctly
        total_questions: Total questions in quiz
        time_taken: Time taken in seconds
        db_session: SQLAlchemy database session
        question_results: Optional list of per-question results
            [{question_id, correct, response_time}, ...]
    
    Returns:
        dict: Summary of updates made
    """
    from sqlalchemy import text
    
    if not ADAPTIVE_CONFIG['ENABLED']:
        return {'status': 'disabled'}
    
    score_percentage = (score / total_questions * 100) if total_questions > 0 else 0
    score_ratio = score / total_questions if total_questions > 0 else 0
    now = datetime.utcnow()
    
    updates = {'mastery_updated': False, 'spaced_rep_updated': False, 'new_mastery_level': 0}
    
    # 1. Get or create topic_mastery record
    result = db_session.execute(text("""
        SELECT id, mastery_level, total_attempts, correct_attempts, 
               recent_scores, streak_current, streak_best,
               review_interval_days, ease_factor
        FROM topic_mastery 
        WHERE user_id = :user_id AND topic = :topic AND difficulty = :difficulty
    """), {'user_id': user_id, 'topic': topic, 'difficulty': difficulty})
    
    record = result.fetchone()
    
    if record:
        # Update existing record
        mastery_id = record[0]
        total_attempts = record[2] + total_questions
        correct_attempts = record[3] + score
        
        # Update recent scores (keep last 10)
        try:
            recent_scores = json.loads(record[4]) if record[4] else []
        except:
            recent_scores = []
        recent_scores.insert(0, score_ratio)
        recent_scores = recent_scores[:ADAPTIVE_CONFIG['RECENT_SCORES_WINDOW']]
        
        # Update streak
        if score_ratio >= 0.7:  # 70% considered "correct" for streak
            streak_current = record[5] + 1
        else:
            streak_current = 0
        streak_best = max(record[6], streak_current)
        
        # Calculate new mastery level
        new_mastery = calculate_mastery_level(
            total_attempts, correct_attempts, recent_scores, 0
        )
        
        # Update spaced repetition
        sr_updates = update_spaced_repetition(
            type('obj', (object,), {
                'review_interval_days': record[7],
                'ease_factor': record[8]
            })(),
            score_percentage
        )
        
        # Check if mastered
        is_mastered = new_mastery >= ADAPTIVE_CONFIG['MASTERY_THRESHOLD']
        mastered_at = now if is_mastered and record[1] < ADAPTIVE_CONFIG['MASTERY_THRESHOLD'] else None
        
        # Update record
        db_session.execute(text("""
            UPDATE topic_mastery SET
                mastery_level = :mastery,
                total_attempts = :attempts,
                correct_attempts = :correct,
                recent_scores = :recent,
                streak_current = :streak,
                streak_best = :best_streak,
                last_attempt_at = :now,
                review_interval_days = :interval,
                ease_factor = :ease,
                next_review_at = :next_review,
                is_mastered = :is_mastered,
                mastered_at = COALESCE(:mastered_at, mastered_at),
                updated_at = :now
            WHERE id = :id
        """), {
            'mastery': new_mastery,
            'attempts': total_attempts,
            'correct': correct_attempts,
            'recent': json.dumps(recent_scores),
            'streak': streak_current,
            'best_streak': streak_best,
            'now': now,
            'interval': sr_updates['review_interval_days'],
            'ease': sr_updates['ease_factor'],
            'next_review': sr_updates['next_review_at'],
            'is_mastered': is_mastered,
            'mastered_at': mastered_at,
            'id': mastery_id
        })
        
        updates['new_mastery_level'] = new_mastery
        
    else:
        # Create new record
        recent_scores = [score_ratio]
        new_mastery = calculate_mastery_level(total_questions, score, recent_scores, 0)
        is_mastered = new_mastery >= ADAPTIVE_CONFIG['MASTERY_THRESHOLD']
        
        sr_updates = update_spaced_repetition(
            type('obj', (object,), {
                'review_interval_days': ADAPTIVE_CONFIG['INITIAL_REVIEW_INTERVAL'],
                'ease_factor': ADAPTIVE_CONFIG['EASE_FACTOR_DEFAULT']
            })(),
            score_percentage
        )
        
        db_session.execute(text("""
            INSERT INTO topic_mastery (
                user_id, topic, difficulty, mastery_level,
                total_attempts, correct_attempts, recent_scores,
                streak_current, streak_best, last_attempt_at,
                review_interval_days, ease_factor, next_review_at,
                is_mastered, mastered_at, created_at, updated_at
            ) VALUES (
                :user_id, :topic, :difficulty, :mastery,
                :attempts, :correct, :recent,
                :streak, :streak, :now,
                :interval, :ease, :next_review,
                :is_mastered, :mastered_at, :now, :now
            )
        """), {
            'user_id': user_id,
            'topic': topic,
            'difficulty': difficulty,
            'mastery': new_mastery,
            'attempts': total_questions,
            'correct': score,
            'recent': json.dumps(recent_scores),
            'streak': 1 if score_ratio >= 0.7 else 0,
            'now': now,
            'interval': sr_updates['review_interval_days'],
            'ease': sr_updates['ease_factor'],
            'next_review': sr_updates['next_review_at'],
            'is_mastered': is_mastered,
            'mastered_at': now if is_mastered else None
        })
        
        updates['new_mastery_level'] = new_mastery
    
    updates['mastery_updated'] = True
    updates['spaced_rep_updated'] = True
    
    # 2. Update per-question performance (if provided)
    if question_results:
        for qr in question_results:
            _update_question_performance(
                user_id, qr['question_id'], topic, difficulty,
                qr['correct'], qr.get('response_time'), db_session
            )
    
    db_session.commit()
    
    return updates


def _update_question_performance(user_id, question_id, topic, difficulty, 
                                 correct, response_time, db_session):
    """Update performance tracking for a single question."""
    from sqlalchemy import text
    
    now = datetime.utcnow()
    
    # Check if record exists
    result = db_session.execute(text("""
        SELECT id, attempts, correct, avg_response_time
        FROM question_performance 
        WHERE user_id = :user_id AND question_id = :question_id
    """), {'user_id': user_id, 'question_id': question_id})
    
    record = result.fetchone()
    
    if record:
        attempts = record[1] + 1
        correct_count = record[2] + (1 if correct else 0)
        
        # Update average response time
        if response_time and record[3]:
            avg_time = (record[3] * record[1] + response_time) / attempts
        else:
            avg_time = response_time
        
        # Flag as problematic if low accuracy with multiple attempts
        is_problematic = (correct_count / attempts) < 0.4 and attempts >= 3
        
        db_session.execute(text("""
            UPDATE question_performance SET
                attempts = :attempts,
                correct = :correct,
                last_attempt_at = :now,
                last_response_time = :response_time,
                avg_response_time = :avg_time,
                is_problematic = :problematic,
                updated_at = :now
            WHERE id = :id
        """), {
            'attempts': attempts,
            'correct': correct_count,
            'now': now,
            'response_time': response_time,
            'avg_time': avg_time,
            'problematic': is_problematic,
            'id': record[0]
        })
    else:
        db_session.execute(text("""
            INSERT INTO question_performance (
                user_id, question_id, topic, difficulty,
                attempts, correct, last_attempt_at, last_response_time,
                avg_response_time, is_problematic, created_at, updated_at
            ) VALUES (
                :user_id, :question_id, :topic, :difficulty,
                1, :correct, :now, :response_time,
                :response_time, 0, :now, :now
            )
        """), {
            'user_id': user_id,
            'question_id': question_id,
            'topic': topic,
            'difficulty': difficulty,
            'correct': 1 if correct else 0,
            'now': now,
            'response_time': response_time
        })


# ============================================================================
# STUDENT DASHBOARD DATA
# ============================================================================

def get_student_adaptive_dashboard(user_id, db_session):
    """
    Get all adaptive learning data for student dashboard.
    
    Args:
        user_id: User ID
        db_session: SQLAlchemy database session
    
    Returns:
        dict: Dashboard data
    """
    from sqlalchemy import text
    
    now = datetime.utcnow()
    
    # Overall mastery stats
    overall = db_session.execute(text("""
        SELECT 
            COUNT(*) as total_topics,
            SUM(CASE WHEN is_mastered = 1 THEN 1 ELSE 0 END) as mastered_topics,
            AVG(mastery_level) as avg_mastery,
            SUM(total_attempts) as total_questions
        FROM topic_mastery 
        WHERE user_id = :user_id
    """), {'user_id': user_id}).fetchone()
    
    # Topic mastery by strand
    topics = db_session.execute(text("""
        SELECT topic, difficulty, mastery_level, is_mastered, 
               streak_current, next_review_at, last_attempt_at
        FROM topic_mastery 
        WHERE user_id = :user_id
        ORDER BY topic, difficulty
    """), {'user_id': user_id}).fetchall()
    
    # Review queue
    review_due = db_session.execute(text("""
        SELECT topic, difficulty, next_review_at
        FROM topic_mastery 
        WHERE user_id = :user_id 
        AND next_review_at <= :now
        AND mastery_level >= 0.5
        ORDER BY next_review_at ASC
        LIMIT 5
    """), {'user_id': user_id, 'now': now}).fetchall()
    
    # Recommendations
    recommendations = generate_recommendations(user_id, db_session)
    
    # Struggling areas
    struggling = db_session.execute(text("""
        SELECT topic, difficulty, mastery_level
        FROM topic_mastery 
        WHERE user_id = :user_id 
        AND mastery_level > 0 
        AND mastery_level < 0.5
        AND total_attempts >= 5
        ORDER BY mastery_level ASC
        LIMIT 3
    """), {'user_id': user_id}).fetchall()
    
    return {
        'overall': {
            'total_topics': overall[0] or 0,
            'mastered_topics': overall[1] or 0,
            'avg_mastery': round((overall[2] or 0) * 100, 1),
            'total_questions': overall[3] or 0
        },
        'topics': [{
            'topic': t[0],
            'difficulty': t[1],
            'mastery': round(t[2] * 100, 1) if t[2] else 0,
            'is_mastered': bool(t[3]),
            'streak': t[4] or 0,
            'next_review': t[5].isoformat() if t[5] else None,
            'last_attempt': t[6].isoformat() if t[6] else None
        } for t in topics],
        'review_queue': [{
            'topic': r[0],
            'difficulty': r[1],
            'due_at': r[2].isoformat() if r[2] else None
        } for r in review_due],
        'recommendations': recommendations,
        'struggling': [{
            'topic': s[0],
            'difficulty': s[1],
            'mastery': round(s[2] * 100, 1)
        } for s in struggling]
    }


# ============================================================================
# TEACHER DATA
# ============================================================================

def get_class_mastery_overview(class_id, db_session):
    """
    Get class-wide mastery overview for teachers.
    
    Args:
        class_id: Class ID
        db_session: SQLAlchemy database session
    
    Returns:
        dict: Class mastery data
    """
    from sqlalchemy import text
    
    # Get all students in class
    students = db_session.execute(text("""
        SELECT u.id, u.full_name
        FROM users u
        JOIN class_enrollments ce ON u.id = ce.student_id
        WHERE ce.class_id = :class_id
        ORDER BY u.full_name
    """), {'class_id': class_id}).fetchall()
    
    if not students:
        return {'students': [], 'topics': [], 'heatmap': []}
    
    student_ids = [s[0] for s in students]
    
    # Get all topics with mastery data
    topics = db_session.execute(text("""
        SELECT DISTINCT topic 
        FROM topic_mastery 
        WHERE user_id IN :student_ids
        ORDER BY topic
    """), {'student_ids': tuple(student_ids)}).fetchall()
    
    topic_list = [t[0] for t in topics]
    
    # Build heatmap data
    heatmap = []
    for student_id, student_name in students:
        row = {'id': student_id, 'name': student_name, 'topics': {}}
        
        mastery_data = db_session.execute(text("""
            SELECT topic, MAX(mastery_level) as best_mastery
            FROM topic_mastery 
            WHERE user_id = :user_id
            GROUP BY topic
        """), {'user_id': student_id}).fetchall()
        
        for topic, mastery in mastery_data:
            row['topics'][topic] = round(mastery * 100, 1) if mastery else 0
        
        heatmap.append(row)
    
    # Class averages per topic
    topic_averages = {}
    for topic in topic_list:
        avg = db_session.execute(text("""
            SELECT AVG(mastery_level)
            FROM topic_mastery 
            WHERE user_id IN :student_ids AND topic = :topic
        """), {'student_ids': tuple(student_ids), 'topic': topic}).fetchone()
        topic_averages[topic] = round((avg[0] or 0) * 100, 1)
    
    # Identify struggling areas (topics where class average is low)
    struggling_topics = [
        {'topic': t, 'avg': topic_averages[t]}
        for t in topic_list if topic_averages[t] < 50
    ]
    struggling_topics.sort(key=lambda x: x['avg'])
    
    return {
        'students': [{'id': s[0], 'name': s[1]} for s in students],
        'topics': topic_list,
        'heatmap': heatmap,
        'topic_averages': topic_averages,
        'struggling_topics': struggling_topics[:5]
    }
