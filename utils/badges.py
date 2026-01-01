# utils/badges.py
# Badge system helper functions for AgentMath
# Extracted from app.py for better maintainability
#
# Revision: 1.0.0
# Date: 2025-12-27

from datetime import datetime, timedelta


def initialize_user_stats(user_id):
    """Create initial stats record for a user if it doesn't exist"""
    from models import db, UserStats  # Late import
    
    stats = UserStats.query.filter_by(user_id=user_id).first()
    if not stats:
        stats = UserStats(
            user_id=user_id,
            total_quizzes=0,
            total_questions_answered=0,
            total_correct_answers=0,
            current_streak_days=0,
            longest_streak_days=0,
            total_points=0,
            level=1,
            topics_mastered=0,
            perfect_scores=0
        )
        db.session.add(stats)
        db.session.commit()
    return stats


def update_user_stats_after_quiz(user_id, quiz_attempt):
    """Update user stats after completing a quiz"""
    from datetime import date
    from models import db, TopicProgress  # Late import

    stats = initialize_user_stats(user_id)

    # Update basic stats
    stats.total_quizzes += 1
    stats.total_questions_answered += quiz_attempt.total_questions
    stats.total_correct_answers += quiz_attempt.score

    # Points: 10 per correct, bonus for perfect
    points_earned = quiz_attempt.score * 10
    if quiz_attempt.score == quiz_attempt.total_questions:
        stats.perfect_scores += 1
        points_earned += 50  # Perfect bonus

    stats.total_points += points_earned

    # Level: 1 level per 100 points
    stats.level = (stats.total_points // 100) + 1

    # Track streak
    today = date.today()
    if stats.last_activity_date:
        if stats.last_activity_date == today:
            pass  # Same day, no streak change
        elif stats.last_activity_date == today - timedelta(days=1):
            stats.current_streak_days += 1
        else:
            stats.current_streak_days = 1
    else:
        stats.current_streak_days = 1

    stats.last_activity_date = today
    stats.longest_streak_days = max(stats.longest_streak_days, stats.current_streak_days)

    # Update topics mastered
    if quiz_attempt.percentage >= 80:
        topic_progress = TopicProgress.query.filter_by(
            user_id=user_id,
            topic=quiz_attempt.topic
        ).first()
        if not topic_progress:
            topic_progress = TopicProgress(
                user_id=user_id,
                topic=quiz_attempt.topic,
                best_score=quiz_attempt.percentage
            )
            db.session.add(topic_progress)
        elif quiz_attempt.percentage > topic_progress.best_score:
            topic_progress.best_score = quiz_attempt.percentage

        # Count mastered topics (80%+ best score)
        mastered = TopicProgress.query.filter(
            TopicProgress.user_id == user_id,
            TopicProgress.best_score >= 80
        ).count()
        stats.topics_mastered = mastered

    db.session.commit()
    return points_earned


def update_topic_progress(user_id, quiz_attempt):
    """Update progress for a specific topic/difficulty"""
    from models import db, TopicProgress, UserStats  # Late import
    
    progress = TopicProgress.query.filter_by(
        user_id=user_id,
        topic=quiz_attempt.topic,
        difficulty=quiz_attempt.difficulty
    ).first()

    if not progress:
        progress = TopicProgress(
            user_id=user_id,
            topic=quiz_attempt.topic,
            difficulty=quiz_attempt.difficulty,
            attempts=0,
            best_score=0,
            best_percentage=0,
            total_questions_answered=0,
            total_correct=0,
            is_mastered=False
        )
        db.session.add(progress)

    progress.attempts += 1
    progress.total_questions_answered += quiz_attempt.total_questions
    progress.total_correct += quiz_attempt.score

    # Update best score
    if quiz_attempt.score > progress.best_score:
        progress.best_score = quiz_attempt.score
    if quiz_attempt.percentage > progress.best_percentage:
        progress.best_percentage = quiz_attempt.percentage

    progress.last_attempt_at = datetime.utcnow()

    # Check for mastery (90%+ accuracy with 5+ attempts)
    if progress.attempts >= 5:
        accuracy = (progress.total_correct / progress.total_questions_answered) * 100
        if accuracy >= 90 and not progress.is_mastered:
            progress.is_mastered = True

            # Update user's mastered topics count
            stats = UserStats.query.filter_by(user_id=user_id).first()
            if stats:
                # Count total mastered topics across all difficulties
                mastered_count = TopicProgress.query.filter_by(
                    user_id=user_id,
                    is_mastered=True
                ).count()
                stats.topics_mastered = mastered_count

    db.session.commit()
    return progress


def check_and_award_badges(user_id):
    """Check and award any earned badges after quiz completion"""
    from models import db, Badge, UserBadge, QuizAttempt  # Late import

    stats = initialize_user_stats(user_id)
    earned_badges = UserBadge.query.filter_by(user_id=user_id).all()
    earned_ids = [ub.badge_id for ub in earned_badges]

    # Get badges not yet earned
    available_badges = Badge.query.filter(Badge.id.notin_(earned_ids) if earned_ids else True).all()

    newly_earned = []

    for badge in available_badges:
        earned = False

        if badge.requirement_type == 'quiz_count':
            earned = stats.total_quizzes >= badge.requirement_value

        elif badge.requirement_type == 'perfect_score':
            earned = stats.perfect_scores >= badge.requirement_value

        elif badge.requirement_type == 'points':
            earned = stats.total_points >= badge.requirement_value

        elif badge.requirement_type == 'level':
            earned = stats.level >= badge.requirement_value

        elif badge.requirement_type == 'accuracy':
            accuracy = stats.total_correct_answers / max(stats.total_questions_answered, 1) * 100
            earned = accuracy >= badge.requirement_value and stats.total_quizzes >= 5

        elif badge.requirement_type == 'high_scores':
            # Count quizzes with 90%+
            high_scores = QuizAttempt.query.filter(
                QuizAttempt.user_id == user_id,
                QuizAttempt.percentage >= 90
            ).count()
            earned = high_scores >= badge.requirement_value

        elif badge.requirement_type == 'streak_days':
            earned = stats.current_streak_days >= badge.requirement_value

        elif badge.requirement_type == 'topics_mastered':
            earned = stats.topics_mastered >= badge.requirement_value

        if earned:
            # Award the badge
            user_badge = UserBadge(
                user_id=user_id,
                badge_id=badge.id,
                progress=100
            )
            db.session.add(user_badge)

            # Award points
            stats.total_points += badge.points

            newly_earned.append(badge.to_dict())

    if newly_earned:
        db.session.commit()

    return newly_earned
