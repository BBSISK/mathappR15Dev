# models.py
# AgentMath Database Models
# Extracted from app.py for better maintainability
#
# Revision: 1.0.1
# Date: 2025-12-31
#
# Fixes in 1.0.1:
# - Added import random (needed by BonusQuestion.to_dict() for shuffle)
#
# Contains all 31 SQLAlchemy model classes

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import random

# Create the SQLAlchemy instance
# This will be initialized with the Flask app in app.py using db.init_app(app)
db = SQLAlchemy()

# ==================== DATABASE MODELS ====================

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'student', 'teacher', 'admin'
    is_approved = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    quiz_attempts = db.relationship('QuizAttempt', backref='user', lazy=True)
    classes_enrolled = db.relationship('ClassEnrollment', backref='student', lazy=True)
    classes_teaching = db.relationship('Class', backref='teacher', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'full_name': self.full_name,
            'role': self.role,
            'is_approved': self.is_approved,
            'created_at': self.created_at.isoformat()
        }

class Class(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    enrollments = db.relationship('ClassEnrollment', backref='class_obj', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'teacher_id': self.teacher_id,
            'teacher_name': self.teacher.full_name if self.teacher else None,
            'student_count': len(self.enrollments),
            'created_at': self.created_at.isoformat()
        }

class ClassEnrollment(db.Model):
    __tablename__ = 'class_enrollments'
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    enrolled_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (db.UniqueConstraint('class_id', 'student_id', name='unique_enrollment'),)

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(50), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(100), nullable=False)
    option_b = db.Column(db.String(100), nullable=False)
    option_c = db.Column(db.String(100), nullable=False)
    option_d = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.Integer, nullable=False)
    explanation = db.Column(db.Text, nullable=False)
    # Phase 1: Image support
    image_url = db.Column(db.String(500), nullable=True)  # Path to image file
    image_caption = db.Column(db.String(200), nullable=True)  # Optional caption
    # Phase 1: Hints
    hint_text = db.Column(db.String(500), nullable=True)  # Optional hint
    hint_penalty = db.Column(db.Integer, default=50)  # Percentage of points lost for using hint

    def to_dict(self):
        return {
            'id': self.id,
            'topic': self.topic,
            'difficulty': self.difficulty,
            'question': self.question_text,
            'options': [self.option_a, self.option_b, self.option_c, self.option_d],
            'correct': self.correct_answer,
            'explanation': self.explanation,
            'image_url': self.image_url,
            'image_caption': self.image_caption,
            'hint_text': self.hint_text,
            'hint_penalty': self.hint_penalty or 50,
            'has_image': bool(self.image_url),
            'has_hint': bool(self.hint_text)
        }

class QuestionFlag(db.Model):
    """Track user-reported issues with questions - supports both registered and guest users"""
    __tablename__ = 'question_flags'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)  # Now nullable for guests
    guest_identifier = db.Column(db.String(100), nullable=True)  # For guest users
    guest_email = db.Column(db.String(120), nullable=True)  # Optional guest email
    flag_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='pending')
    admin_notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    resolved_at = db.Column(db.DateTime)
    resolved_by = db.Column(db.Integer, db.ForeignKey('users.id'))

    question = db.relationship('Question', backref='flags')
    reporter = db.relationship('User', foreign_keys=[user_id], backref='flags_reported')
    resolver = db.relationship('User', foreign_keys=[resolved_by], backref='flags_resolved')

    def to_dict(self):
        # Determine reporter name
        if self.user_id:
            reporter_name = self.reporter.full_name if self.reporter else 'Unknown User'
        else:
            reporter_name = f"Guest ({self.guest_identifier or 'Anonymous'})"

        return {
            'id': self.id,
            'question_id': self.question_id,
            'user_id': self.user_id,
            'user_name': reporter_name,
            'guest_email': self.guest_email,
            'flag_type': self.flag_type,
            'description': self.description,
            'status': self.status,
            'admin_notes': self.admin_notes,
            'created_at': self.created_at.isoformat(),
            'resolved_at': self.resolved_at.isoformat() if self.resolved_at else None,
            'resolver_name': self.resolver.full_name if self.resolver else None
        }


class AdaptiveQuestionFlag(db.Model):
    """Track user-reported issues with adaptive quiz questions"""
    __tablename__ = 'adaptive_question_flags'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, nullable=False)  # References questions_adaptive.id
    topic = db.Column(db.String(50), nullable=False)  # Topic for context
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    guest_identifier = db.Column(db.String(100), nullable=True)
    flag_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    question_text = db.Column(db.Text)  # Store question text for reference
    status = db.Column(db.String(20), default='pending')
    admin_notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    resolved_at = db.Column(db.DateTime)
    resolved_by = db.Column(db.Integer, db.ForeignKey('users.id'))

    reporter = db.relationship('User', foreign_keys=[user_id], backref='adaptive_flags_reported')
    resolver = db.relationship('User', foreign_keys=[resolved_by], backref='adaptive_flags_resolved')

    def to_dict(self):
        if self.user_id:
            reporter_name = self.reporter.full_name if self.reporter else 'Unknown User'
        else:
            reporter_name = f"Guest ({self.guest_identifier or 'Anonymous'})"

        return {
            'id': self.id,
            'question_id': self.question_id,
            'topic': self.topic,
            'user_id': self.user_id,
            'user_name': reporter_name,
            'flag_type': self.flag_type,
            'description': self.description,
            'question_text': self.question_text,
            'status': self.status,
            'admin_notes': self.admin_notes,
            'created_at': self.created_at.isoformat(),
            'resolved_at': self.resolved_at.isoformat() if self.resolved_at else None,
            'resolver_name': self.resolver.full_name if self.resolver else None,
            'is_adaptive': True
        }


class QuestionEdit(db.Model):
    """Track all edits made to questions"""
    __tablename__ = 'question_edits'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    edited_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    edit_type = db.Column(db.String(50), nullable=False)

    old_question_text = db.Column(db.Text)
    old_option_a = db.Column(db.String(100))
    old_option_b = db.Column(db.String(100))
    old_option_c = db.Column(db.String(100))
    old_option_d = db.Column(db.String(100))
    old_correct_answer = db.Column(db.Integer)
    old_explanation = db.Column(db.Text)

    new_question_text = db.Column(db.Text)
    new_option_a = db.Column(db.String(100))
    new_option_b = db.Column(db.String(100))
    new_option_c = db.Column(db.String(100))
    new_option_d = db.Column(db.String(100))
    new_correct_answer = db.Column(db.Integer)
    new_explanation = db.Column(db.Text)

    edit_notes = db.Column(db.Text)
    edited_at = db.Column(db.DateTime, default=datetime.utcnow)

    question = db.relationship('Question', backref='edit_history')
    editor = db.relationship('User', backref='question_edits')

    def to_dict(self):
        changes = {}
        if self.old_question_text != self.new_question_text:
            changes['question_text'] = {'old': self.old_question_text, 'new': self.new_question_text}
        if self.old_option_a != self.new_option_a:
            changes['option_a'] = {'old': self.old_option_a, 'new': self.new_option_a}
        if self.old_option_b != self.new_option_b:
            changes['option_b'] = {'old': self.old_option_b, 'new': self.new_option_b}
        if self.old_option_c != self.new_option_c:
            changes['option_c'] = {'old': self.old_option_c, 'new': self.new_option_c}
        if self.old_option_d != self.new_option_d:
            changes['option_d'] = {'old': self.old_option_d, 'new': self.new_option_d}
        if self.old_correct_answer != self.new_correct_answer:
            changes['correct_answer'] = {'old': self.old_correct_answer, 'new': self.new_correct_answer}
        if self.old_explanation != self.new_explanation:
            changes['explanation'] = {'old': self.old_explanation, 'new': self.new_explanation}

        return {
            'id': self.id,
            'question_id': self.question_id,
            'edited_by': self.editor.full_name,
            'edit_type': self.edit_type,
            'edit_notes': self.edit_notes,
            'edited_at': self.edited_at.isoformat(),
            'changes': changes
        }

class QuizAttempt(db.Model):
    __tablename__ = 'quiz_attempts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    topic = db.Column(db.String(50), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    percentage = db.Column(db.Float, nullable=False)
    time_taken = db.Column(db.Integer)  # seconds
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'user_name': self.user.full_name,
            'topic': self.topic,
            'difficulty': self.difficulty,
            'score': self.score,
            'total_questions': self.total_questions,
            'percentage': self.percentage,
            'time_taken': self.time_taken,
            'completed_at': self.completed_at.isoformat()
        }

# ==================== BADGES & PROGRESS TRACKING MODELS ====================

class Badge(db.Model):
    """Badge definitions"""
    __tablename__ = 'badges'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    icon = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # beginner, progress, accuracy, streak, mastery
    requirement_type = db.Column(db.String(50), nullable=False)
    requirement_value = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, default=10)
    color = db.Column(db.String(50), default='blue')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'icon': self.icon,
            'category': self.category,
            'requirement_type': self.requirement_type,
            'requirement_value': self.requirement_value,
            'points': self.points,
            'color': self.color
        }

class UserBadge(db.Model):
    """Tracks badges earned by users"""
    __tablename__ = 'user_badges'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    badge_id = db.Column(db.Integer, db.ForeignKey('badges.id'), nullable=False)
    earned_at = db.Column(db.DateTime, default=datetime.utcnow)
    progress = db.Column(db.Integer, default=0)

    __table_args__ = (db.UniqueConstraint('user_id', 'badge_id', name='unique_user_badge'),)

    badge = db.relationship('Badge', backref='earned_by')
    user = db.relationship('User', backref='earned_badges')

    def to_dict(self):
        return {
            'id': self.id,
            'badge': self.badge.to_dict(),
            'earned_at': self.earned_at.isoformat(),
            'progress': self.progress
        }

class UserStats(db.Model):
    """Overall user statistics and progress"""
    __tablename__ = 'user_stats'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    total_quizzes = db.Column(db.Integer, default=0)
    total_questions_answered = db.Column(db.Integer, default=0)
    total_correct_answers = db.Column(db.Integer, default=0)
    current_streak_days = db.Column(db.Integer, default=0)
    longest_streak_days = db.Column(db.Integer, default=0)
    last_quiz_date = db.Column(db.Date)
    total_points = db.Column(db.Integer, default=0)
    level = db.Column(db.Integer, default=1)
    topics_mastered = db.Column(db.Integer, default=0)
    perfect_scores = db.Column(db.Integer, default=0)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    # Prize Shop PIN protection
    prize_pin = db.Column(db.String(50), nullable=True)  # The passcode (stored lowercase)
    prize_pin_hint = db.Column(db.String(100), nullable=True)  # Hint like "Family" or "Pet"

    user = db.relationship('User', backref='stats', uselist=False)

    def to_dict(self):
        overall_accuracy = 0
        if self.total_questions_answered > 0:
            overall_accuracy = round((self.total_correct_answers / self.total_questions_answered) * 100, 1)

        return {
            'id': self.id,
            'user_id': self.user_id,
            'total_quizzes': self.total_quizzes,
            'total_questions_answered': self.total_questions_answered,
            'total_correct_answers': self.total_correct_answers,
            'overall_accuracy': overall_accuracy,
            'current_streak_days': self.current_streak_days,
            'longest_streak_days': self.longest_streak_days,
            'last_quiz_date': self.last_quiz_date.isoformat() if self.last_quiz_date else None,
            'total_points': self.total_points,
            'level': self.level,
            'topics_mastered': self.topics_mastered,
            'perfect_scores': self.perfect_scores,
            'updated_at': self.updated_at.isoformat()
        }

# ==================== AVATAR SYSTEM MODELS ====================
# These models support the avatar customization feature
# BACKOUT: Set AVATAR_SYSTEM_ENABLED=false to disable without removing code

class AvatarItem(db.Model):
    """Shop items - animals, hats, glasses, backgrounds, accessories"""
    __tablename__ = 'avatar_items'

    id = db.Column(db.Integer, primary_key=True)
    item_type = db.Column(db.String(50), nullable=False)  # 'animal', 'hat', 'glasses', 'background', 'accessory'
    item_key = db.Column(db.String(50), nullable=False)   # 'panda', 'crown', etc.
    display_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    point_cost = db.Column(db.Integer, nullable=False, default=0)
    rarity = db.Column(db.String(20), default='common')  # 'common', 'rare', 'epic', 'legendary'
    is_default = db.Column(db.Boolean, default=False)    # Free starter items
    is_active = db.Column(db.Boolean, default=True)      # Can hide items without deleting
    sort_order = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (db.UniqueConstraint('item_type', 'item_key', name='unique_item_type_key'),)

    def to_dict(self):
        return {
            'id': self.id,
            'item_type': self.item_type,
            'item_key': self.item_key,
            'display_name': self.display_name,
            'description': self.description,
            'point_cost': self.point_cost,
            'rarity': self.rarity,
            'is_default': self.is_default,
            'is_active': self.is_active,
            'sort_order': self.sort_order
        }

class UserAvatarInventory(db.Model):
    """Tracks which items users/guests have purchased"""
    __tablename__ = 'user_avatar_inventory'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    guest_code = db.Column(db.String(50), nullable=True)
    item_id = db.Column(db.Integer, db.ForeignKey('avatar_items.id'), nullable=False)
    purchased_at = db.Column(db.DateTime, default=datetime.utcnow)

    item = db.relationship('AvatarItem', backref='purchases')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'guest_code': self.guest_code,
            'item': self.item.to_dict() if self.item else None,
            'purchased_at': self.purchased_at.isoformat() if self.purchased_at else None
        }

class UserAvatarEquipped(db.Model):
    """Tracks currently equipped avatar configuration"""
    __tablename__ = 'user_avatar_equipped'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    guest_code = db.Column(db.String(50), nullable=True)
    animal_key = db.Column(db.String(50), default='panda')
    hat_key = db.Column(db.String(50), default='none')
    glasses_key = db.Column(db.String(50), default='none')
    background_key = db.Column(db.String(50), default='none')
    accessory_key = db.Column(db.String(50), default='none')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'guest_code': self.guest_code,
            'animal': self.animal_key,
            'hat': self.hat_key,
            'glasses': self.glasses_key,
            'background': self.background_key,
            'accessory': self.accessory_key,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class AvatarPurchaseLog(db.Model):
    """Audit log for all purchases - useful for debugging and potential refunds"""
    __tablename__ = 'avatar_purchase_log'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=True)
    guest_code = db.Column(db.String(50), nullable=True)
    item_id = db.Column(db.Integer, db.ForeignKey('avatar_items.id'), nullable=False)
    points_spent = db.Column(db.Integer, nullable=False)
    points_before = db.Column(db.Integer, nullable=False)
    points_after = db.Column(db.Integer, nullable=False)
    purchased_at = db.Column(db.DateTime, default=datetime.utcnow)

    item = db.relationship('AvatarItem')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'guest_code': self.guest_code,
            'item': self.item.to_dict() if self.item else None,
            'points_spent': self.points_spent,
            'points_before': self.points_before,
            'points_after': self.points_after,
            'purchased_at': self.purchased_at.isoformat() if self.purchased_at else None
        }

# ==================== PRIZE SYSTEM MODELS ====================
# Points for Prizes - students redeem points for physical rewards
# BACKOUT: Set PRIZE_SYSTEM_ENABLED=false to disable without removing code

class SystemSetting(db.Model):
    """Global system settings (key-value store)"""
    __tablename__ = 'system_settings'

    key = db.Column(db.String(100), primary_key=True)
    value = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    updated_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    @staticmethod
    def get(key, default=None):
        """Get a setting value"""
        setting = SystemSetting.query.get(key)
        if setting:
            # Try to parse as JSON for complex values
            try:
                import json
                return json.loads(setting.value)
            except:
                return setting.value
        return default

    @staticmethod
    def set(key, value, description=None, user_id=None):
        """Set a setting value"""
        import json
        setting = SystemSetting.query.get(key)
        if not setting:
            setting = SystemSetting(key=key)

        # Serialize complex values as JSON
        if isinstance(value, (dict, list)):
            setting.value = json.dumps(value)
        else:
            setting.value = str(value)

        if description:
            setting.description = description
        setting.updated_by = user_id
        setting.updated_at = datetime.utcnow()

        db.session.add(setting)
        db.session.commit()
        return setting


class PrizeSchool(db.Model):
    """Schools participating in the prize programme"""
    __tablename__ = 'prize_schools'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    roll_number = db.Column(db.String(20), unique=True, nullable=True)  # Irish school roll number
    county = db.Column(db.String(50))
    address = db.Column(db.Text)

    # Status
    status = db.Column(db.String(20), default='pending')  # pending, approved, suspended

    # School-specific settings
    points_multiplier = db.Column(db.Float, default=1.0)  # Multiplied with global multiplier

    # School rep (main contact)
    rep_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    rep_name = db.Column(db.String(100))
    rep_email = db.Column(db.String(100))

    # Admin tracking
    approved_at = db.Column(db.DateTime)
    approved_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text)

    # Relationships
    rep_user = db.relationship('User', foreign_keys=[rep_user_id], backref='rep_for_schools')
    approver = db.relationship('User', foreign_keys=[approved_by])

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'roll_number': self.roll_number,
            'county': self.county,
            'status': self.status,
            'points_multiplier': self.points_multiplier,
            'rep_name': self.rep_name,
            'rep_email': self.rep_email,
            'approved_at': self.approved_at.isoformat() if self.approved_at else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class Prize(db.Model):
    """Global prize catalogue (templates)"""
    __tablename__ = 'prizes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    # Points (base cost before multipliers)
    base_point_cost = db.Column(db.Integer, nullable=False)

    # Classification
    tier = db.Column(db.String(20), default='bronze')  # bronze, silver, gold, platinum
    prize_type = db.Column(db.String(20), default='physical')  # physical, raffle_entry, digital

    # Level requirement (0 = no requirement)
    minimum_level = db.Column(db.Integer, default=0)

    # Display
    emoji = db.Column(db.String(10), default='🎁')
    image_url = db.Column(db.String(255))
    sort_order = db.Column(db.Integer, default=0)

    # Availability
    is_active = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def get_cost_for_school(self, school):
        """Calculate actual point cost for this prize at a specific school"""
        # Check for school-specific override
        override = SchoolPrize.query.filter_by(
            school_id=school.id,
            prize_id=self.id
        ).first()

        if override and override.point_cost_override:
            return override.point_cost_override

        # Apply multipliers
        global_multiplier = float(SystemSetting.get('global_points_multiplier', 5.0))
        school_multiplier = school.points_multiplier or 1.0

        return int(self.base_point_cost * global_multiplier * school_multiplier)

    def to_dict(self, school=None):
        result = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'base_point_cost': self.base_point_cost,
            'tier': self.tier,
            'prize_type': self.prize_type,
            'minimum_level': self.minimum_level or 0,
            'emoji': self.emoji,
            'image_url': self.image_url,
            'is_active': self.is_active,
            'sort_order': self.sort_order
        }

        if school:
            result['point_cost'] = self.get_cost_for_school(school)

        return result


class SchoolPrize(db.Model):
    """School-specific prize overrides and custom prizes"""
    __tablename__ = 'school_prizes'

    id = db.Column(db.Integer, primary_key=True)
    school_id = db.Column(db.Integer, db.ForeignKey('prize_schools.id'), nullable=False)

    # If prize_id is set, this is an override for a global prize
    # If prize_id is NULL, this is a school-specific prize
    prize_id = db.Column(db.Integer, db.ForeignKey('prizes.id'), nullable=True)

    # Custom prize details (used when prize_id is NULL)
    custom_name = db.Column(db.String(100))
    custom_description = db.Column(db.Text)
    custom_emoji = db.Column(db.String(10), default='🎁')

    # Override settings
    point_cost_override = db.Column(db.Integer, nullable=True)  # NULL = use calculated cost
    stock_available = db.Column(db.Integer, nullable=True)  # NULL = unlimited
    is_enabled = db.Column(db.Boolean, default=True)  # Can disable for this school

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    school = db.relationship('PrizeSchool', backref='prize_overrides')
    prize = db.relationship('Prize', backref='school_overrides')

    def to_dict(self):
        return {
            'id': self.id,
            'school_id': self.school_id,
            'prize_id': self.prize_id,
            'custom_name': self.custom_name,
            'custom_description': self.custom_description,
            'custom_emoji': self.custom_emoji,
            'point_cost_override': self.point_cost_override,
            'stock_available': self.stock_available,
            'is_enabled': self.is_enabled,
            # Include global prize info if this is an override
            'prize': self.prize.to_dict() if self.prize else None
        }

    def get_display_name(self):
        """Get the display name (custom or from global prize)"""
        if self.custom_name:
            return self.custom_name
        elif self.prize:
            return self.prize.name
        return "Unknown Prize"

    def get_point_cost(self):
        """Get the point cost for this school prize"""
        if self.point_cost_override:
            return self.point_cost_override
        elif self.prize and self.school:
            return self.prize.get_cost_for_school(self.school)
        return 0


class PrizeRedemption(db.Model):
    """Student prize redemptions (token-based, no personal data)"""
    __tablename__ = 'prize_redemptions'

    id = db.Column(db.Integer, primary_key=True)

    # Who redeemed
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('prize_schools.id'), nullable=False)

    # What was redeemed
    prize_id = db.Column(db.Integer, db.ForeignKey('prizes.id'), nullable=True)  # Global prize
    school_prize_id = db.Column(db.Integer, db.ForeignKey('school_prizes.id'), nullable=True)  # School-specific

    # Token for collection (GDPR-safe: no student name stored)
    token = db.Column(db.String(20), unique=True, nullable=False)

    # Points
    points_spent = db.Column(db.Integer, nullable=False)

    # Status tracking
    status = db.Column(db.String(20), default='pending')  # pending, fulfilled, expired, cancelled

    # Timestamps
    redeemed_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime)  # Token expiry
    fulfilled_at = db.Column(db.DateTime)
    fulfilled_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    fulfilment_notes = db.Column(db.Text)

    # Relationships
    user = db.relationship('User', foreign_keys=[user_id], backref='prize_redemptions')
    school = db.relationship('PrizeSchool', backref='redemptions')
    prize = db.relationship('Prize', backref='redemptions')
    school_prize = db.relationship('SchoolPrize', backref='redemptions')
    fulfiller = db.relationship('User', foreign_keys=[fulfilled_by])

    def get_prize_name(self):
        """Get the name of the redeemed prize"""
        if self.school_prize:
            return self.school_prize.get_display_name()
        elif self.prize:
            return self.prize.name
        return "Unknown Prize"

    def get_prize_emoji(self):
        """Get the emoji for the redeemed prize"""
        if self.school_prize and self.school_prize.custom_emoji:
            return self.school_prize.custom_emoji
        elif self.prize:
            return self.prize.emoji
        return "🎁"

    def to_dict(self, include_user=False):
        result = {
            'id': self.id,
            'school_id': self.school_id,
            'school_name': self.school.name if self.school else None,
            'prize_name': self.get_prize_name(),
            'prize_emoji': self.get_prize_emoji(),
            'token': self.token,
            'points_spent': self.points_spent,
            'status': self.status,
            'redeemed_at': self.redeemed_at.isoformat() if self.redeemed_at else None,
            'expires_at': self.expires_at.isoformat() if self.expires_at else None,
            'fulfilled_at': self.fulfilled_at.isoformat() if self.fulfilled_at else None
        }

        if include_user and self.user:
            result['username'] = self.user.username

        return result


class SchoolRequest(db.Model):
    """Student requests to add their school to the programme"""
    __tablename__ = 'school_requests'

    id = db.Column(db.Integer, primary_key=True)

    # School info from student
    school_name = db.Column(db.String(200), nullable=False)
    county = db.Column(db.String(50))
    suggested_rep_email = db.Column(db.String(100))  # Optional: student suggests a teacher

    # Who requested
    requested_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Status
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected
    admin_notes = db.Column(db.Text)

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    processed_at = db.Column(db.DateTime)
    processed_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    # If approved, link to created school
    created_school_id = db.Column(db.Integer, db.ForeignKey('prize_schools.id'), nullable=True)

    # Relationships
    requester = db.relationship('User', foreign_keys=[requested_by], backref='school_requests')
    processor = db.relationship('User', foreign_keys=[processed_by])
    created_school = db.relationship('PrizeSchool')

    def to_dict(self):
        return {
            'id': self.id,
            'school_name': self.school_name,
            'county': self.county,
            'suggested_rep_email': self.suggested_rep_email,
            'requested_by_username': self.requester.username if self.requester else None,
            'status': self.status,
            'admin_notes': self.admin_notes,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'processed_at': self.processed_at.isoformat() if self.processed_at else None
        }


class RaffleDraw(db.Model):
    """Weekly raffle draws"""
    __tablename__ = 'raffle_draws'

    id = db.Column(db.Integer, primary_key=True)

    # Draw info
    draw_name = db.Column(db.String(100), nullable=False)
    prize_description = db.Column(db.Text, nullable=False)

    # Scheduling
    draw_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='scheduled')  # scheduled, completed, cancelled

    # Winner
    winner_redemption_id = db.Column(db.Integer, db.ForeignKey('prize_redemptions.id'), nullable=True)

    # Admin
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    drawn_at = db.Column(db.DateTime)

    # Relationships
    winner_redemption = db.relationship('PrizeRedemption')
    creator = db.relationship('User', foreign_keys=[created_by])

    def to_dict(self):
        return {
            'id': self.id,
            'draw_name': self.draw_name,
            'prize_description': self.prize_description,
            'draw_date': self.draw_date.isoformat() if self.draw_date else None,
            'status': self.status,
            'winner': self.winner_redemption.to_dict() if self.winner_redemption else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


# Helper function to generate prize tokens
def generate_prize_token():
    """Generate a unique prize redemption token"""
    import string
    chars = string.ascii_uppercase + string.digits
    while True:
        # Format: PRIZE-XXXX-XXXX
        token = 'PRIZE-' + ''.join(random.choices(chars, k=4)) + '-' + ''.join(random.choices(chars, k=4))
        # Check uniqueness
        existing = PrizeRedemption.query.filter_by(token=token).first()
        if not existing:
            return token


# ==================== DOMAIN RESTRICTION MODELS ====================

class TeacherDomainAccess(db.Model):
    """Tracks which email domains a teacher can access"""
    __tablename__ = 'teacher_domain_access'

    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    email_domain = db.Column(db.String(100), nullable=False)
    granted_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    granted_at = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text)

    # Relationships
    teacher = db.relationship('User', foreign_keys=[teacher_id], backref='domain_access')
    granter = db.relationship('User', foreign_keys=[granted_by], backref='domains_granted')

    # Unique constraint: one teacher can only have one record per domain
    __table_args__ = (db.UniqueConstraint('teacher_id', 'email_domain', name='unique_teacher_domain'),)

    def to_dict(self):
        return {
            'id': self.id,
            'teacher_id': self.teacher_id,
            'teacher_name': self.teacher.full_name,
            'teacher_email': self.teacher.email,
            'email_domain': self.email_domain,
            'granted_by': self.granter.full_name,
            'granted_at': self.granted_at.isoformat(),
            'notes': self.notes
        }

class DomainAccessRequest(db.Model):
    """Tracks teacher requests for domain access"""
    __tablename__ = 'domain_access_requests'

    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    email_domain = db.Column(db.String(100), nullable=False)
    reason = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, approved, denied
    requested_at = db.Column(db.DateTime, default=datetime.utcnow)
    reviewed_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    reviewed_at = db.Column(db.DateTime)
    admin_notes = db.Column(db.Text)

    # Relationships
    teacher = db.relationship('User', foreign_keys=[teacher_id], backref='domain_requests')
    reviewer = db.relationship('User', foreign_keys=[reviewed_by], backref='domain_requests_reviewed')

    def to_dict(self):
        return {
            'id': self.id,
            'teacher_id': self.teacher_id,
            'teacher_name': self.teacher.full_name,
            'teacher_email': self.teacher.email,
            'email_domain': self.email_domain,
            'reason': self.reason,
            'status': self.status,
            'requested_at': self.requested_at.isoformat(),
            'reviewed_by': self.reviewer.full_name if self.reviewer else None,
            'reviewed_at': self.reviewed_at.isoformat() if self.reviewed_at else None,
            'admin_notes': self.admin_notes
        }

class TopicProgress(db.Model):
    """Per-topic progress tracking"""
    __tablename__ = 'topic_progress'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    topic = db.Column(db.String(50), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)
    attempts = db.Column(db.Integer, default=0)
    best_score = db.Column(db.Integer, default=0)
    best_percentage = db.Column(db.Float, default=0)
    total_questions_answered = db.Column(db.Integer, default=0)
    total_correct = db.Column(db.Integer, default=0)
    is_mastered = db.Column(db.Boolean, default=False)
    last_attempt_at = db.Column(db.DateTime)

    __table_args__ = (db.UniqueConstraint('user_id', 'topic', 'difficulty', name='unique_topic_progress'),)

    user = db.relationship('User', backref='topic_progress')

    def to_dict(self):
        accuracy = 0
        if self.total_questions_answered > 0:
            accuracy = round((self.total_correct / self.total_questions_answered) * 100, 1)

        return {
            'id': self.id,
            'topic': self.topic,
            'difficulty': self.difficulty,
            'attempts': self.attempts,
            'best_score': self.best_score,
            'best_percentage': self.best_percentage,
            'accuracy': accuracy,
            'is_mastered': self.is_mastered,
            'last_attempt_at': self.last_attempt_at.isoformat() if self.last_attempt_at else None
        }


# ==================== PUZZLE OF THE WEEK MODELS ====================

class WeeklyPuzzle(db.Model):
    """Weekly puzzle for students"""
    __tablename__ = 'weekly_puzzles'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    
    # Puzzle content (either image or text)
    puzzle_type = db.Column(db.String(20), default='image')  # 'image' or 'text'
    puzzle_image = db.Column(db.String(500))  # Path to puzzle image (800x600)
    puzzle_text = db.Column(db.Text)  # Text-based puzzle content
    
    # Answer content
    answer_image = db.Column(db.String(500))  # Path to answer image
    answer_text = db.Column(db.Text)  # Text-based answer
    
    # Hint
    hint = db.Column(db.Text)
    
    # Scheduling
    week_number = db.Column(db.Integer, nullable=False)  # ISO week 1-52
    year = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    
    # Stats
    view_count = db.Column(db.Integer, default=0)
    reveal_count = db.Column(db.Integer, default=0)
    hint_view_count = db.Column(db.Integer, default=0)
    
    # Admin tracking
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    
    # Relationships
    creator = db.relationship('User', foreign_keys=[created_by])
    
    def to_dict(self, include_answer=False):
        data = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'puzzle_type': self.puzzle_type,
            'puzzle_image': self.puzzle_image,
            'puzzle_text': self.puzzle_text,
            'hint': self.hint,
            'week_number': self.week_number,
            'year': self.year,
            'is_active': self.is_active,
            'view_count': self.view_count,
            'reveal_count': self.reveal_count,
            'hint_view_count': self.hint_view_count,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
        if include_answer:
            data['answer_image'] = self.answer_image
            data['answer_text'] = self.answer_text
        return data


class PuzzleUserStatus(db.Model):
    """Tracks user interaction with puzzles"""
    __tablename__ = 'puzzle_user_status'
    
    id = db.Column(db.Integer, primary_key=True)
    puzzle_id = db.Column(db.Integer, db.ForeignKey('weekly_puzzles.id'), nullable=False)
    
    # User identification (one of these will be set)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    guest_code = db.Column(db.String(20), nullable=True)
    session_id = db.Column(db.String(100), nullable=True)
    
    # Status flags
    dismissed_popup = db.Column(db.Boolean, default=False)  # Don't show splash this week
    dismissed_answer = db.Column(db.Boolean, default=False)  # Don't offer answer reveal
    revealed_answer = db.Column(db.Boolean, default=False)  # Has seen the answer
    hint_viewed = db.Column(db.Boolean, default=False)  # Has viewed the hint
    
    # Stats
    view_count = db.Column(db.Integer, default=1)  # Times viewed puzzle
    
    # Timestamps
    first_viewed_at = db.Column(db.DateTime, default=datetime.utcnow)
    answer_revealed_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    puzzle = db.relationship('WeeklyPuzzle', backref='user_statuses')
    user = db.relationship('User', foreign_keys=[user_id])


# ==================== PUZZLE HELPER FUNCTIONS ====================

def get_current_week_year():
    """Get current ISO week number and year"""
    now = datetime.utcnow()
    iso_cal = now.isocalendar()
    return iso_cal[1], iso_cal[0]  # week_number, year


def get_active_puzzle():
    """Get the currently active puzzle for this week"""
    week, year = get_current_week_year()
    return WeeklyPuzzle.query.filter_by(
        week_number=week,
        year=year,
        is_active=True
    ).first()


def get_user_puzzle_status(puzzle_id, user_id=None, guest_code=None, session_id=None):
    """Get or create puzzle status for a user"""
    query = PuzzleUserStatus.query.filter_by(puzzle_id=puzzle_id)
    
    if user_id:
        status = query.filter_by(user_id=user_id).first()
        if not status:
            status = PuzzleUserStatus(puzzle_id=puzzle_id, user_id=user_id)
            db.session.add(status)
            db.session.commit()
    elif guest_code:
        status = query.filter_by(guest_code=guest_code).first()
        if not status:
            status = PuzzleUserStatus(puzzle_id=puzzle_id, guest_code=guest_code)
            db.session.add(status)
            db.session.commit()
    elif session_id:
        status = query.filter_by(session_id=session_id).first()
        if not status:
            status = PuzzleUserStatus(puzzle_id=puzzle_id, session_id=session_id)
            db.session.add(status)
            db.session.commit()
    else:
        return None
    
    return status


# ==================== BONUS QUESTION MODELS ====================

class BonusQuestion(db.Model):
    """Bonus questions for high-scoring students (dinosaurs, flags, etc.)"""
    __tablename__ = 'bonus_questions'
    
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)  # 'dinosaurs', 'flags', 'scientists', etc.
    correct_answer = db.Column(db.String(100), nullable=False)
    option_a = db.Column(db.String(100), nullable=False)
    option_b = db.Column(db.String(100), nullable=False)
    option_c = db.Column(db.String(100), nullable=False)
    option_d = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    fun_fact = db.Column(db.Text)
    difficulty = db.Column(db.String(20), default='medium')  # easy, medium, hard
    era_or_region = db.Column(db.String(100))  # For dinos: "Late Cretaceous", for flags: "Europe"
    is_active = db.Column(db.Boolean, default=True)
    times_shown = db.Column(db.Integer, default=0)
    times_correct = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        options = [self.option_a, self.option_b, self.option_c, self.option_d]
        # Shuffle options but remember correct answer
        random.shuffle(options)
        return {
            'id': self.id,
            'category': self.category,
            'correct_answer': self.correct_answer,
            'options': options,
            'image_url': self.image_url,
            'fun_fact': self.fun_fact,
            'era_or_region': self.era_or_region
        }
    
    def to_admin_dict(self):
        accuracy = 0
        if self.times_shown > 0:
            accuracy = round((self.times_correct / self.times_shown) * 100, 1)
        return {
            'id': self.id,
            'category': self.category,
            'correct_answer': self.correct_answer,
            'option_a': self.option_a,
            'option_b': self.option_b,
            'option_c': self.option_c,
            'option_d': self.option_d,
            'image_url': self.image_url,
            'fun_fact': self.fun_fact,
            'difficulty': self.difficulty,
            'era_or_region': self.era_or_region,
            'is_active': self.is_active,
            'times_shown': self.times_shown,
            'times_correct': self.times_correct,
            'accuracy': accuracy
        }


class BonusQuestionAttempt(db.Model):
    """Track bonus question attempts"""
    __tablename__ = 'bonus_question_attempts'
    
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('bonus_questions.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    guest_code = db.Column(db.String(20), nullable=True)
    selected_answer = db.Column(db.String(100), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    points_earned = db.Column(db.Integer, default=0)
    quiz_topic = db.Column(db.String(50))  # What quiz they just completed
    quiz_score = db.Column(db.Integer)  # Their quiz score that unlocked this
    attempted_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    question = db.relationship('BonusQuestion', backref='attempts')


class UserQuestionHistory(db.Model):
    """Track which questions each user has seen to prevent duplicates in quizzes"""
    __tablename__ = 'user_question_history'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    guest_code = db.Column(db.String(20), nullable=True)  # For guest users
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    topic = db.Column(db.String(50), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)
    seen_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Indexes for fast lookups
    __table_args__ = (
        db.Index('idx_user_question', 'user_id', 'question_id'),
        db.Index('idx_guest_question', 'guest_code', 'question_id'),
        db.Index('idx_user_topic_diff', 'user_id', 'topic', 'difficulty'),
        db.Index('idx_guest_topic_diff', 'guest_code', 'topic', 'difficulty'),
    )


class UserAdaptiveQuestionHistory(db.Model):
    """Track which adaptive questions each user has seen to prevent duplicates in Learning in Stages"""
    __tablename__ = 'user_adaptive_question_history'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    guest_code = db.Column(db.String(20), nullable=True)  # For guest users
    question_id = db.Column(db.Integer, nullable=False)  # References questions_adaptive.id
    topic = db.Column(db.String(50), nullable=False)
    difficulty_level = db.Column(db.Integer, nullable=False)  # 1-12
    seen_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Indexes for fast lookups
    __table_args__ = (
        db.Index('idx_adaptive_user_question', 'user_id', 'question_id'),
        db.Index('idx_adaptive_guest_question', 'guest_code', 'question_id'),
        db.Index('idx_adaptive_user_topic_level', 'user_id', 'topic', 'difficulty_level'),
        db.Index('idx_adaptive_guest_topic_level', 'guest_code', 'topic', 'difficulty_level'),
    )


