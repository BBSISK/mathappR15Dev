# routes/teacher.py
# Teacher routes for AgentMath
# Extracted from app.py for better maintainability
#
# Revision: 1.0.1
# Date: 2025-12-31 - Added FEATURE_FLAGS proxy
#
# Contains:
# - Teacher dashboard and class management
# - Student enrollment and progress monitoring
# - Domain access management
# - Real-time class dashboard
# - Guest management for teachers
# - Total: 35 routes

from flask import Blueprint, request, jsonify, session, render_template, redirect, url_for, flash
from models import db, User, Class, ClassEnrollment, QuizAttempt, UserStats, TeacherDomainAccess, DomainAccessRequest, Question, Prize, PrizeSchool, PrizeRedemption
from datetime import datetime, timedelta
from sqlalchemy import text

# Create blueprint
teacher_bp = Blueprint('teacher', __name__)

# Import decorators
from utils.auth import login_required, role_required, approved_required
from utils.domain import (
    get_teacher_accessible_domains,
    filter_students_by_domain_access,
    teacher_has_domain_access
)


# ==================== FEATURE FLAGS ACCESS ====================
from flask import current_app

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


# ==================== TEACHER ROUTES ====================

@teacher_bp.route('/teacher')
@login_required
@role_required('teacher')
@approved_required
def teacher_dashboard():
    """Redirect to the new visual class selector"""
    return redirect(url_for('teacher_classes_page'))

@teacher_bp.route('/teacher-classes')
def teacher_classes_redirect():
    """Redirect old hyphenated URL to correct format"""
    return redirect('/teacher/classes')

@teacher_bp.route('/teacher/class-monitor')
@login_required
@role_required('teacher')
@approved_required
def class_monitor():
    """
    Class Monitor Dashboard - Live monitoring view for teachers
    Shows performance matrix for all students in teacher's classes
    """
    return render_template('class_monitor.html')

@teacher_bp.route('/api/teacher/my-classes')
@login_required
@role_required('teacher')
@approved_required
def teacher_classes():
    classes = Class.query.filter_by(teacher_id=session['user_id']).all()
    return jsonify([c.to_dict() for c in classes])

@teacher_bp.route('/api/teacher/create-class', methods=['POST'])
@login_required
@role_required('teacher')
@approved_required
def create_class():
    data = request.json
    name = data.get('name', '').strip()

    if not name:
        return jsonify({'error': 'Class name is required'}), 400

    new_class = Class(
        name=name,
        teacher_id=session['user_id']
    )

    db.session.add(new_class)
    db.session.commit()

    return jsonify({
        'message': 'Class created successfully',
        'class': new_class.to_dict()
    }), 201

@teacher_bp.route('/api/teacher/students/search')
@login_required
@role_required('teacher')
@approved_required
def search_students():
    """Search for students (filtered by teacher's domain access)"""
    query = request.args.get('q', '').strip()
    teacher_id = session['user_id']
    if len(query) < 2:
        return jsonify([])
    students_query = User.query.filter(
        User.role == 'student',
        (User.email.ilike(f'%{query}%')) | (User.full_name.ilike(f'%{query}%'))
    )
    accessible_domains = get_teacher_accessible_domains(teacher_id)
    if accessible_domains is not None:
        filtered_ids = []
        for student in students_query.all():
            student_domain = extract_domain(student.email)
            if student_domain in accessible_domains:
                filtered_ids.append(student.id)
        students_query = students_query.filter(User.id.in_(filtered_ids)) if filtered_ids else students_query.filter(User.id == -1)
    students = students_query.limit(20).all()
    return jsonify([s.to_dict() for s in students])
@teacher_bp.route('/api/teacher/class/<int:class_id>/enroll', methods=['POST'])
@login_required
@role_required('teacher')
@approved_required
def enroll_student(class_id):
    """Enroll a student in a class (with domain access check)"""
    class_obj = Class.query.get_or_404(class_id)
    teacher_id = session['user_id']
    if class_obj.teacher_id != teacher_id:
        return jsonify({'error': 'Unauthorized'}), 403
    data = request.json
    student_id = data.get('student_id')
    if not student_id:
        return jsonify({'error': 'Student ID required'}), 400
    student = User.query.get(student_id)
    if not student or student.role != 'student':
        return jsonify({'error': 'Invalid student'}), 400
    student_domain = extract_domain(student.email)
    if not teacher_has_domain_access(teacher_id, student_domain):
        return jsonify({'error': f'Access denied. You do not have permission to enroll students from the domain: {student_domain}. Please request access from an administrator.'}), 403
    existing = ClassEnrollment.query.filter_by(class_id=class_id, student_id=student_id).first()
    if existing:
        return jsonify({'error': 'Student already enrolled'}), 400
    enrollment = ClassEnrollment(class_id=class_id, student_id=student_id)
    db.session.add(enrollment)
    db.session.commit()
    return jsonify({'message': 'Student enrolled successfully'}), 201

@teacher_bp.route('/api/teacher/class/<int:class_id>/students')
@login_required
@role_required('teacher')
@approved_required
def class_students(class_id):
    """Get students in class - FILTERED BY DOMAIN ACCESS"""
    class_obj = Class.query.get_or_404(class_id)
    teacher_id = session['user_id']

    if class_obj.teacher_id != teacher_id:
        return jsonify({'error': 'Unauthorized'}), 403

    enrollments = ClassEnrollment.query.filter_by(class_id=class_id).all()

    # Filter by domain access
    accessible_domains = get_teacher_accessible_domains(teacher_id)
    if accessible_domains is not None:
        filtered_enrollments = []
        for enrollment in enrollments:
            student = enrollment.student
            if student:
                student_domain = extract_domain(student.email)
                if student_domain in accessible_domains:
                    filtered_enrollments.append(enrollment)
        enrollments = filtered_enrollments

    students_data = []
    for enrollment in enrollments:
        student = enrollment.student
        if not student:  # Safety check
            continue
        attempts = QuizAttempt.query.filter_by(user_id=student.id).all()

        students_data.append({
            'id': student.id,
            'full_name': student.full_name,
            'email': student.email,
            'enrolled_at': enrollment.enrolled_at.isoformat(),
            'total_quizzes': len(attempts),
            'average_score': sum(a.percentage for a in attempts) / len(attempts) if attempts else 0,
            'last_activity': max([a.completed_at for a in attempts]).isoformat() if attempts else None
        })

    return jsonify(students_data)

@teacher_bp.route('/api/teacher/class/<int:class_id>/progress')
@login_required
@role_required('teacher')
@approved_required
def class_progress(class_id):
    class_obj = Class.query.get_or_404(class_id)

    if class_obj.teacher_id != session['user_id']:
        return jsonify({'error': 'Unauthorized'}), 403

    enrollments = ClassEnrollment.query.filter_by(class_id=class_id).all()
    student_ids = [e.student_id for e in enrollments]

    # Get all attempts for students in this class
    attempts = QuizAttempt.query.filter(QuizAttempt.user_id.in_(student_ids)).order_by(QuizAttempt.completed_at.desc()).all()

    return jsonify([a.to_dict() for a in attempts])

@teacher_bp.route('/api/teacher/class/<int:class_id>/remove-student/<int:student_id>', methods=['DELETE'])
@login_required
@role_required('teacher')
@approved_required
def remove_student(class_id, student_id):
    class_obj = Class.query.get_or_404(class_id)

    if class_obj.teacher_id != session['user_id']:
        return jsonify({'error': 'Unauthorized'}), 403

    enrollment = ClassEnrollment.query.filter_by(class_id=class_id, student_id=student_id).first()
    if not enrollment:
        return jsonify({'error': 'Enrollment not found'}), 404

    db.session.delete(enrollment)
    db.session.commit()

    return jsonify({'message': 'Student removed successfully'})

# ==================== NEW ENHANCED TEACHER ROUTES ====================

@teacher_bp.route('/teacher/classes')
@login_required
@role_required('teacher')
@approved_required
def teacher_classes_page():
    """Visual class selector page"""
    return render_template('teacher_classes_selector.html')

@teacher_bp.route('/api/teacher/classes', methods=['GET', 'POST'])
@login_required
@role_required('teacher')
@approved_required
def teacher_classes_api():
    """Get all classes for teacher or create new class"""
    teacher_id = session['user_id']

    if request.method == 'GET':
        # Get all classes for this teacher
        classes = Class.query.filter_by(teacher_id=teacher_id).order_by(Class.created_at.desc()).all()
        teacher = User.query.get(teacher_id)

        return jsonify({
            'classes': [c.to_dict() for c in classes],
            'teacher': teacher.to_dict() if teacher else None
        })

    elif request.method == 'POST':
        # Create new class
        data = request.json
        class_name = data.get('name', '').strip()

        if not class_name:
            return jsonify({'error': 'Class name is required'}), 400

        new_class = Class(
            name=class_name,
            teacher_id=teacher_id
        )

        db.session.add(new_class)
        db.session.commit()

        return jsonify({
            'message': 'Class created successfully',
            'class': new_class.to_dict()
        }), 201

@teacher_bp.route('/api/teacher/class/<int:class_id>')
@login_required
@role_required('teacher')
@approved_required
def get_class_info(class_id):
    """Get basic class information"""
    class_obj = Class.query.get_or_404(class_id)

    # Verify teacher owns this class
    if class_obj.teacher_id != session['user_id']:
        return jsonify({'error': 'Unauthorized'}), 403

    return jsonify(class_obj.to_dict())

@teacher_bp.route('/teacher/class-manage/<int:class_id>')
@login_required
@role_required('teacher')
@approved_required
def class_manage_page(class_id):
    """Student management page for a class"""
    class_obj = Class.query.get_or_404(class_id)

    # Verify teacher owns this class
    if class_obj.teacher_id != session['user_id']:
        flash('Unauthorized access to class', 'error')
        return redirect(url_for('teacher_classes_page'))

    return render_template('teacher_class_manage_students.html',
                         class_id=class_id,
                         class_name=class_obj.name)

@teacher_bp.route('/api/teacher/available-students/<int:class_id>')
@login_required
@role_required('teacher')
@approved_required
def get_available_students(class_id):
    """Get all students NOT enrolled in this class (filtered by domain access)"""
    class_obj = Class.query.get_or_404(class_id)
    teacher_id = session['user_id']
    if class_obj.teacher_id != teacher_id:
        return jsonify({'error': 'Unauthorized'}), 403
    enrolled_ids = db.session.query(ClassEnrollment.student_id).filter_by(class_id=class_id).all()
    enrolled_ids = [e[0] for e in enrolled_ids]
    available_students_query = User.query.filter(User.role == 'student').filter(~User.id.in_(enrolled_ids))
    accessible_domains = get_teacher_accessible_domains(teacher_id)
    if accessible_domains is not None:
        filtered_ids = []
        for student in available_students_query.all():
            student_domain = extract_domain(student.email)
            if student_domain in accessible_domains:
                filtered_ids.append(student.id)
        available_students_query = available_students_query.filter(User.id.in_(filtered_ids)) if filtered_ids else available_students_query.filter(User.id == -1)
    available_students = available_students_query.order_by(User.full_name).all()
    return jsonify([{'id': s.id, 'full_name': s.full_name, 'email': s.email} for s in available_students])

@teacher_bp.route('/api/teacher/class/<int:class_id>/enroll-bulk', methods=['POST'])
@login_required
@role_required('teacher')
@approved_required
def enroll_students_bulk(class_id):
    """Enroll multiple students at once (with domain access checks)"""
    class_obj = Class.query.get_or_404(class_id)
    teacher_id = session['user_id']
    if class_obj.teacher_id != teacher_id:
        return jsonify({'error': 'Unauthorized'}), 403
    data = request.json
    student_ids = data.get('student_ids', [])
    if not student_ids:
        return jsonify({'error': 'No students selected'}), 400
    enrolled_count = 0
    already_enrolled = 0
    access_denied = []
    for student_id in student_ids:
        student = User.query.get(student_id)
        if student:
            student_domain = extract_domain(student.email)
            if not teacher_has_domain_access(teacher_id, student_domain):
                access_denied.append({'id': student_id, 'name': student.full_name, 'domain': student_domain})
                continue
        existing = ClassEnrollment.query.filter_by(class_id=class_id, student_id=student_id).first()
        if existing:
            already_enrolled += 1
            continue
        enrollment = ClassEnrollment(class_id=class_id, student_id=student_id)
        db.session.add(enrollment)
        enrolled_count += 1
    db.session.commit()
    response = {'message': f'Enrolled {enrolled_count} students', 'enrolled_count': enrolled_count, 'already_enrolled': already_enrolled}
    if access_denied:
        response['access_denied'] = access_denied
        response['access_denied_count'] = len(access_denied)
    return jsonify(response)

@teacher_bp.route('/api/teacher/class/<int:class_id>/students-list')
@login_required
@role_required('teacher')
@approved_required
def get_class_students_list(class_id):
    """Get detailed list of students in a class with their progress (filtered by domain)"""
    class_obj = Class.query.get_or_404(class_id)
    teacher_id = session['user_id']
    if class_obj.teacher_id != teacher_id:
        return jsonify({'error': 'Unauthorized'}), 403
    enrollments = ClassEnrollment.query.filter_by(class_id=class_id).all()
    accessible_domains = get_teacher_accessible_domains(teacher_id)
    if accessible_domains is not None:
        filtered_enrollments = []
        for enrollment in enrollments:
            student = User.query.get(enrollment.student_id)
            if student:
                student_domain = extract_domain(student.email)
                if student_domain in accessible_domains:
                    filtered_enrollments.append(enrollment)
        enrollments = filtered_enrollments
    students_data = []
    for enrollment in enrollments:
        student = User.query.get(enrollment.student_id)
        if not student:
            continue
        attempts = QuizAttempt.query.filter_by(user_id=student.id).all()
        total_quizzes = len(attempts)
        if attempts:
            avg_score = sum(a.percentage for a in attempts) / len(attempts)
            recent_attempts = sorted(attempts, key=lambda x: x.completed_at, reverse=True)[:5]
        else:
            avg_score = 0
            recent_attempts = []
        students_data.append({'id': student.id, 'full_name': student.full_name, 'email': student.email, 'total_quizzes': total_quizzes, 'avg_score': round(avg_score, 1), 'recent_attempts': [a.to_dict() for a in recent_attempts], 'enrolled_at': enrollment.enrolled_at.isoformat()})
    return jsonify({'class': class_obj.to_dict(), 'students': students_data})

@teacher_bp.route('/api/teacher/class/<int:class_id>/performance-matrix')
@login_required
@role_required('teacher')
@approved_required
def get_class_performance_matrix(class_id):
    """
    Get performance matrix for all students in a class
    Returns: percentage correct and attempts for each topic/difficulty combination
    Used by: Class Monitor Dashboard for live performance tracking
    """
    # Verify teacher owns this class
    class_obj = Class.query.filter_by(id=class_id, teacher_id=session['user_id']).first()
    if not class_obj:
        return jsonify({'error': 'Class not found or access denied'}), 403

    # Get all students in class
    enrollments = ClassEnrollment.query.filter_by(class_id=class_id).all()
    student_ids = [e.student_id for e in enrollments]
    students = User.query.filter(User.id.in_(student_ids)).all()

    # Get all topics and difficulties
    topics = get_valid_topics_from_db()  # Database-driven!
    difficulties = VALID_DIFFICULTIES

    students_data = []

    for student in students:
        performance = {}

        for topic in topics:
            for difficulty in difficulties:
                key = f"{topic}_{difficulty}"

                # Get all attempts for this topic/difficulty
                attempts = QuizAttempt.query.filter_by(
                    user_id=student.id,
                    topic=topic,
                    difficulty=difficulty
                ).all()

                if attempts:
                    # Calculate average percentage
                    avg_percentage = sum(a.percentage for a in attempts) / len(attempts)
                    performance[key] = {
                        'percentage': round(avg_percentage, 1),
                        'attempts': len(attempts)
                    }
                else:
                    performance[key] = {
                        'percentage': None,
                        'attempts': 0
                    }

        students_data.append({
            'student_id': student.id,
            'student_name': student.full_name,
            'performance': performance
        })

    return jsonify({
        'class_name': class_obj.name,
        'total_students': len(students_data),
        'students': students_data,
        'topics': topics,
        'difficulties': difficulties
    })

# ==================== TEACHER DOMAIN ACCESS ROUTES ====================

@teacher_bp.route('/api/teacher/my-domain-access')
@login_required
@role_required('teacher')
@approved_required
def get_my_domain_access():
    """Get current teacher's domain access information"""
    teacher_id = session['user_id']
    access_records = TeacherDomainAccess.query.filter_by(teacher_id=teacher_id).all()
    stats = get_teacher_domain_statistics(teacher_id)
    pending_requests = DomainAccessRequest.query.filter_by(teacher_id=teacher_id, status='pending').all()
    all_domains = get_all_domains_in_system()
    assigned_domains = [r.email_domain for r in access_records]
    requested_domains = [r.email_domain for r in pending_requests]
    available_to_request = [d for d in all_domains if d['domain'] not in assigned_domains and d['domain'] not in requested_domains]
    return jsonify({
        'has_restrictions': stats['has_restrictions'],
        'assigned_domains': [r.to_dict() for r in access_records],
        'accessible_student_count': stats['accessible_student_count'],
        'restricted_domains': stats['restricted_domains'],
        'pending_requests': [r.to_dict() for r in pending_requests],
        'available_to_request': available_to_request
    })


@teacher_bp.route('/api/teacher/request-domain-access', methods=['POST'])
@login_required
@role_required('teacher')
@approved_required
def request_domain_access():
    """Request access to a specific email domain"""
    teacher_id = session['user_id']
    data = request.json
    domain = data.get('domain', '').strip().lower()
    reason = data.get('reason', '').strip()
    if not domain:
        return jsonify({'error': 'Domain is required'}), 400
    if not reason:
        return jsonify({'error': 'Please provide a reason for this request'}), 400
    if '.' not in domain or '@' in domain:
        return jsonify({'error': 'Invalid domain format. Use format like: school.edu'}), 400
    existing_access = TeacherDomainAccess.query.filter_by(teacher_id=teacher_id, email_domain=domain).first()
    if existing_access:
        return jsonify({'error': 'You already have access to this domain'}), 400
    existing_request = DomainAccessRequest.query.filter_by(teacher_id=teacher_id, email_domain=domain, status='pending').first()
    if existing_request:
        return jsonify({'error': 'You already have a pending request for this domain'}), 400
    access_request = DomainAccessRequest(teacher_id=teacher_id, email_domain=domain, reason=reason)
    db.session.add(access_request)
    db.session.commit()
    return jsonify({'message': 'Domain access request submitted successfully', 'request': access_request.to_dict()}), 201


@teacher_bp.route('/api/teacher/domain-requests')
@login_required
@role_required('teacher')
@approved_required
def get_my_domain_requests():
    """Get all domain access requests by the current teacher"""
    teacher_id = session['user_id']
    requests = DomainAccessRequest.query.filter_by(teacher_id=teacher_id).order_by(DomainAccessRequest.requested_at.desc()).all()
    return jsonify({'requests': [r.to_dict() for r in requests]})


@teacher_bp.route('/api/teacher/domain-requests/<int:request_id>', methods=['DELETE'])
@login_required
@role_required('teacher')
@approved_required
def cancel_domain_request(request_id):
    """Cancel a pending domain access request"""
    teacher_id = session['user_id']
    access_request = DomainAccessRequest.query.get_or_404(request_id)
    if access_request.teacher_id != teacher_id:
        return jsonify({'error': 'Unauthorized'}), 403
    if access_request.status != 'pending':
        return jsonify({'error': 'Can only cancel pending requests'}), 400
    db.session.delete(access_request)
    db.session.commit()
    return jsonify({'message': 'Request cancelled successfully'})


@teacher_bp.route('/api/admin/statistics')
@login_required
@role_required('admin')
def admin_statistics():
    stats = {
        'total_students': User.query.filter_by(role='student').count(),
        'total_teachers': User.query.filter_by(role='teacher', is_approved=True).count(),
        'pending_teachers': User.query.filter_by(role='teacher', is_approved=False).count(),
        'total_classes': Class.query.count(),
        'total_quizzes': QuizAttempt.query.count(),
        'total_questions': Question.query.count()
    }

    # Add prize system statistics if enabled
    if FEATURE_FLAGS.get('PRIZE_SYSTEM_ENABLED', False):
        try:
            stats['prize_stats'] = {
                'active_prizes': Prize.query.filter_by(is_active=True).count(),
                'total_schools': PrizeSchool.query.filter_by(status='approved').count(),  # Use status column
                'pending_redemptions': PrizeRedemption.query.filter_by(status='pending').count(),
                'total_redemptions': PrizeRedemption.query.count()
            }
        except Exception as e:
            print(f"Error getting prize stats: {e}")
            stats['prize_stats'] = {
                'active_prizes': 0,
                'total_schools': 0,
                'pending_redemptions': 0,
                'total_redemptions': 0
            }

    return jsonify(stats)


@teacher_bp.route('/api/admin/topics-list')
@login_required
@role_required('admin')
def admin_topics_list():
    """
    Get all topics for dropdown - combines topics from:
    1. The topics table (admin-managed, authoritative)
    2. The questions table (for topics with questions but not yet in topics table)
    
    This ensures new topics added via Admin Dashboard appear immediately.
    """
    from sqlalchemy import func, text
    
    topics_dict = {}  # Use dict to avoid duplicates
    
    # First, get all topics from the topics table (admin-managed)
    try:
        db_topics = db.session.execute(text("""
            SELECT t.topic_id, t.display_name, 
                   (SELECT COUNT(*) FROM questions q WHERE q.topic = t.topic_id) as question_count
            FROM topics t
            WHERE t.is_visible = 1
            ORDER BY t.sort_order, t.display_name
        """)).fetchall()
        
        for topic_id, display_name, count in db_topics:
            topics_dict[topic_id] = {
                'value': topic_id,
                'name': display_name,
                'count': count or 0
            }
    except Exception as e:
        print(f"Warning: Could not load from topics table: {e}")
    
    # Also get topics from questions table (for any topics not yet in topics table)
    try:
        questions_topics = db.session.query(
            Question.topic,
            func.count(Question.id).label('count')
        ).group_by(Question.topic).all()
        
        for topic, count in questions_topics:
            if topic not in topics_dict:
                # Topic exists in questions but not in topics table
                topics_dict[topic] = {
                    'value': topic,
                    'name': topic.replace('_', ' ').title(),
                    'count': count
                }
            else:
                # Update count if questions table has more (shouldn't happen, but safety)
                if count > topics_dict[topic]['count']:
                    topics_dict[topic]['count'] = count
    except Exception as e:
        print(f"Warning: Could not load from questions table: {e}")
    
    # Convert to list and sort
    topics = sorted(topics_dict.values(), key=lambda x: x['name'])
    
    return jsonify({'topics': topics})


@teacher_bp.route('/api/admin/question-counts/<topic>')
@login_required
@role_required('admin')
def admin_question_counts(topic):
    """Get question counts by difficulty for a specific topic"""
    from sqlalchemy import text
    
    counts = {}
    for difficulty in ['beginner', 'intermediate', 'advanced']:
        result = db.session.execute(text(
            "SELECT COUNT(*) FROM questions WHERE topic = :topic AND difficulty = :difficulty"
        ), {'topic': topic, 'difficulty': difficulty}).fetchone()
        counts[difficulty] = result[0] if result else 0
    
    return jsonify(counts)


# ==================== REAL-TIME CLASS DASHBOARD ROUTES ====================

@teacher_bp.route('/teacher/class-dashboard/<int:class_id>')
@login_required
@role_required('teacher')
@approved_required
def class_dashboard(class_id):
    """
    Enhanced Class Performance Dashboard
    - Shows ALL students by default
    - Smart search and filtering
    - Student selection for export
    - Hover tooltips with recommendations
    """
    class_obj = Class.query.get_or_404(class_id)

    # Verify teacher owns this class
    if class_obj.teacher_id != session['user_id']:
        flash('Unauthorized access to class', 'error')
        return redirect(url_for('teacher_classes_page'))

    return render_template('teacher_class_dashboard_v2.html',
                         class_id=class_id,
                         class_name=class_obj.name)

@teacher_bp.route('/api/teacher/class/<int:class_id>/matrix-data')
@login_required
@role_required('teacher')
@approved_required
def get_class_matrix_data(class_id):
    """Get matrix data for class dashboard with Junior Cycle strands"""
    class_obj = Class.query.get_or_404(class_id)

    # Verify teacher owns this class
    if class_obj.teacher_id != session['user_id']:
        return jsonify({'error': 'Unauthorized'}), 403

    # Get all students in class
    enrollments = ClassEnrollment.query.filter_by(class_id=class_id).all()

    # NEW: Get topics grouped by strand from database
    try:
        from sqlalchemy import text
        topics_query = db.session.execute(text("""
            SELECT DISTINCT strand, topic
            FROM questions
            WHERE strand IS NOT NULL
            ORDER BY
                CASE strand
                    WHEN 'Number' THEN 1
                    WHEN 'Algebra and Functions' THEN 2
                    WHEN 'Statistics and Probability' THEN 3
                    WHEN 'Senior Cycle - Algebra' THEN 4
                    WHEN 'Geometry and Trigonometry' THEN 5
                    ELSE 6
                END,
                CASE topic
                    -- Order for Number strand
                    WHEN 'arithmetic' THEN 1
                    WHEN 'multiplication_division' THEN 2
                    WHEN 'number_systems' THEN 3
                    WHEN 'bodmas' THEN 4
                    WHEN 'fractions' THEN 5
                    WHEN 'decimals' THEN 6
                    WHEN 'sets' THEN 7
                    -- Order for Algebra and Functions strand (Junior Cycle)
                    WHEN 'introductory_algebra' THEN 1
                    WHEN 'functions' THEN 2
                    WHEN 'patterns' THEN 3
                    WHEN 'solving_equations' THEN 4
                    WHEN 'simplifying_expressions' THEN 5
                    WHEN 'expanding_factorising' THEN 6
                    -- Order for Statistics and Probability strand
                    WHEN 'probability' THEN 1
                    WHEN 'descriptive_statistics' THEN 2
                    -- Order for Senior Cycle - Algebra strand
                    WHEN 'surds' THEN 1
                    WHEN 'complex_numbers_intro' THEN 2
                    WHEN 'complex_numbers_expanded' THEN 3
                    -- Default order for other topics
                    ELSE 10
                END,
                topic
        """)).fetchall()
    except Exception as e:
        print(f"Warning: Could not query strand column in matrix-data: {e}")
        topics_query = []

    # Build strands structure
    strands = {}
    all_topics = []

    for strand, topic in topics_query:
        if strand not in strands:
            strands[strand] = []
        strands[strand].append(topic)
        all_topics.append(topic)

    # If no strands found (strands not yet added), fall back to hardcoded list
    if not all_topics:
        all_topics = get_valid_topics_from_db()  # Database-driven fallback!
        # Default strands for fallback
        strands = {
            'Number': [t for t in all_topics if t in ['arithmetic', 'fractions', 'decimals', 
                      'multiplication_division', 'number_systems', 'bodmas', 'sets', 'surds']],
            'Algebra and Functions': [t for t in all_topics if t in ['introductory_algebra', 
                      'functions', 'patterns', 'solving_equations', 'simplifying_expressions', 
                      'expanding_factorising', 'complex_numbers_intro', 'complex_numbers_expanded', 
                      'simultaneous_equations']],
            'Geometry and Trigonometry': [t for t in all_topics if t in ['coordinate_geometry', 'trigonometry']],
            'Statistics and Probability': [t for t in all_topics if t in ['probability', 'descriptive_statistics']],
        }

    difficulties = ['beginner', 'intermediate', 'advanced']

    # Build matrix data
    matrix_data = []

    for enrollment in enrollments:
        student = enrollment.student

        # Get student stats
        stats = UserStats.query.filter_by(user_id=student.id).first()

        student_data = {
            'student_id': student.id,
            'student_name': student.full_name,
            'total_points': stats.total_points if stats else 0,
            'level': stats.level if stats else 1,
            'modules': {},  # Legacy practice data
            'adaptive': {}  # Adaptive quiz data
        }

        # ==================== LEGACY PRACTICE DATA ====================
        # For each topic/difficulty combination
        for topic in all_topics:
            for difficulty in difficulties:
                module_key = f"{topic}_{difficulty}"

                # Get all attempts for this module
                attempts = QuizAttempt.query.filter_by(
                    user_id=student.id,
                    topic=topic,
                    difficulty=difficulty
                ).all()

                if attempts:
                    # Calculate average percentage
                    avg_percentage = sum(a.percentage for a in attempts) / len(attempts)
                    total_attempts = len(attempts)

                    # Determine color based on performance
                    if avg_percentage < 20:
                        color = 'grey'
                    elif avg_percentage <= 80:
                        color = 'yellow'
                    else:
                        color = 'green'

                    student_data['modules'][module_key] = {
                        'percentage': round(avg_percentage, 1),
                        'attempts': total_attempts,
                        'color': color,
                        'completed': True
                    }
                else:
                    # Not attempted yet
                    student_data['modules'][module_key] = {
                        'percentage': 0,
                        'attempts': 0,
                        'color': 'grey',
                        'completed': False
                    }

        # ==================== ADAPTIVE QUIZ DATA ====================
        try:
            # Get adaptive progress for this student
            # Check both user_id AND any linked guest_code
            adaptive_rows = []
            
            # First try by user_id
            try:
                user_rows = db.session.execute(text("""
                    SELECT topic, current_level, current_points, updated_at
                    FROM adaptive_progress
                    WHERE user_id = :user_id
                """), {'user_id': student.id}).fetchall()
                adaptive_rows.extend(user_rows)
            except Exception as e:
                print(f"Error querying adaptive_progress by user_id: {e}")
            
            # Also check if this user was converted from a guest
            # Get their guest_code from guest_users table
            try:
                guest_info = db.session.execute(text("""
                    SELECT guest_code FROM guest_users WHERE user_id = :user_id
                """), {'user_id': student.id}).fetchone()
                
                if guest_info:
                    guest_code = guest_info[0]
                    # Get adaptive progress by guest_code
                    guest_rows = db.session.execute(text("""
                        SELECT topic, current_level, current_points, updated_at
                        FROM adaptive_progress
                        WHERE guest_code = :guest_code
                    """), {'guest_code': guest_code}).fetchall()
                    adaptive_rows.extend(guest_rows)
            except Exception as e:
                print(f"Error checking guest_code for adaptive progress: {e}")
            
            # Process all found rows
            for row in adaptive_rows:
                if hasattr(row, '_mapping'):
                    data = dict(row._mapping)
                else:
                    data = {
                        'topic': row[0],
                        'current_level': row[1],
                        'current_points': row[2],
                        'updated_at': row[3]
                    }
                
                topic = data['topic']
                current_level = data['current_level'] or 1
                current_points = data['current_points'] or 0
                
                # Only update if this is better progress (in case of duplicates)
                existing = student_data['adaptive'].get(topic)
                if existing and existing['level'] >= current_level:
                    continue
                
                # Calculate percentage based on level (1-12, so level 12 = 100%)
                level_percentage = round((current_level / 12) * 100, 1)
                
                # Color based on level
                if current_level <= 3:
                    color = 'grey'
                elif current_level <= 8:
                    color = 'yellow'
                else:
                    color = 'green'
                
                student_data['adaptive'][topic] = {
                    'level': current_level,
                    'points': current_points,
                    'percentage': level_percentage,
                    'color': color,
                    'completed': current_level > 1
                }
            
            # Get question count from adaptive history (check both user_id and guest_code)
            try:
                question_counts = db.session.execute(text("""
                    SELECT topic, COUNT(*) as count
                    FROM user_adaptive_question_history
                    WHERE user_id = :user_id
                    GROUP BY topic
                """), {'user_id': student.id}).fetchall()
                
                for row in question_counts:
                    if hasattr(row, '_mapping'):
                        topic = row._mapping['topic']
                        count = row._mapping['count']
                    else:
                        topic = row[0]
                        count = row[1]
                    
                    if topic in student_data['adaptive']:
                        student_data['adaptive'][topic]['questions_answered'] = count
            except:
                pass  # Table might not exist
                
        except Exception as e:
            print(f"Error getting adaptive progress for student {student.id}: {e}")

        matrix_data.append(student_data)

    # Get list of topics that have adaptive content WITH strand info
    adaptive_topics = []
    adaptive_strands = {}  # Map topics to strands for adaptive
    
    # Define topic-to-strand mapping (based on curriculum)
    topic_strand_map = {
        # Number strand
        'arithmetic': 'Number',
        'addition_subtraction': 'Number',
        'applied_arithmetic': 'Number',
        'basic_decimals': 'Number',
        'basic_fractions': 'Number',
        'basic_percentages': 'Number',
        'decimals': 'Number',
        'fractions': 'Number',
        'percentages': 'Number',
        'division_skills': 'Number',
        'multiplication_division': 'Number',
        'number_systems': 'Number',
        'bodmas': 'Number',
        'ratio': 'Number',
        'developing_number_sense': 'Number',
        'financial_maths': 'Number',
        'sets': 'Number',
        'surds': 'Number',
        # Algebra and Functions strand
        'introductory_algebra': 'Algebra and Functions',
        'algebra': 'Algebra and Functions',
        'functions': 'Algebra and Functions',
        'patterns': 'Algebra and Functions',
        'solving_equations': 'Algebra and Functions',
        'simplifying_expressions': 'Algebra and Functions',
        'expanding_factorising': 'Algebra and Functions',
        'expanding_expressions': 'Algebra and Functions',
        'factorising_expressions': 'Algebra and Functions',
        'simultaneous_equations': 'Algebra and Functions',
        'complex_numbers_intro': 'Algebra and Functions',
        'complex_numbers_expanded': 'Algebra and Functions',
        'indices': 'Algebra and Functions',
        'logarithms': 'Algebra and Functions',
        'quadratic_equations': 'Algebra and Functions',
        # Statistics and Probability strand
        'probability': 'Statistics and Probability',
        'descriptive_statistics': 'Statistics and Probability',
        'statistics': 'Statistics and Probability',
        'data_and_charts': 'Statistics and Probability',
        # Geometry and Trigonometry strand
        'coordinate_geometry': 'Geometry and Trigonometry',
        'trigonometry': 'Geometry and Trigonometry',
        'geometry': 'Geometry and Trigonometry',
        'area_perimeter_volume': 'Geometry and Trigonometry',
        'measurement': 'Geometry and Trigonometry',
        'mensuration': 'Geometry and Trigonometry',
        # L1LP / L2LP / Numeracy
        'awareness_of_environment': 'Numeracy',
        'money_skills': 'Numeracy',
        'time_skills': 'Numeracy',
        'shape_and_space': 'Numeracy',
    }
    
    # Try multiple sources for adaptive topics
    try:
        # Source 1: Try questions_adaptive table first
        try:
            adaptive_topic_rows = db.session.execute(text("""
                SELECT DISTINCT topic FROM questions_adaptive ORDER BY topic
            """)).fetchall()
            if adaptive_topic_rows:
                for row in adaptive_topic_rows:
                    topic = row[0]
                    if topic and topic not in adaptive_topics:
                        adaptive_topics.append(topic)
                print(f"Got {len(adaptive_topics)} topics from questions_adaptive")
        except Exception as e:
            print(f"questions_adaptive query failed: {e}")
        
        # Source 2: If no topics yet, try adaptive_progress table
        if not adaptive_topics:
            try:
                progress_rows = db.session.execute(text("""
                    SELECT DISTINCT topic FROM adaptive_progress ORDER BY topic
                """)).fetchall()
                if progress_rows:
                    for row in progress_rows:
                        topic = row[0]
                        if topic and topic not in adaptive_topics:
                            adaptive_topics.append(topic)
                    print(f"Got {len(adaptive_topics)} topics from adaptive_progress")
            except Exception as e:
                print(f"adaptive_progress query failed: {e}")
        
        # Source 3: If still no topics, use hardcoded list of common adaptive topics
        if not adaptive_topics:
            adaptive_topics = [
                'arithmetic', 'fractions', 'decimals', 'percentages', 'ratio',
                'introductory_algebra', 'functions', 'probability', 'descriptive_statistics',
                'coordinate_geometry', 'trigonometry', 'area_perimeter_volume'
            ]
            print(f"Using hardcoded list of {len(adaptive_topics)} topics")
        
        # Now build strand groupings from topics
        for topic in adaptive_topics:
            strand = topic_strand_map.get(topic, 'Other')
            
            if strand not in adaptive_strands:
                adaptive_strands[strand] = []
            if topic not in adaptive_strands[strand]:
                adaptive_strands[strand].append(topic)
        
        print(f"Built adaptive_strands: {list(adaptive_strands.keys())}")
                    
    except Exception as e:
        print(f"Error getting adaptive topics: {e}")
        import traceback
        traceback.print_exc()

    return jsonify({
        'students': matrix_data,
        'topics': all_topics,
        'difficulties': difficulties,
        'strands': strands,  # Include strand grouping for legacy
        'adaptive_topics': adaptive_topics,  # Topics with adaptive content
        'adaptive_strands': adaptive_strands,  # Strand grouping for adaptive
        'class_name': class_obj.name,
        'total_students': len(matrix_data)
    })

@teacher_bp.route('/api/teacher/class/<int:class_id>/dashboard-settings', methods=['GET', 'POST'])
@login_required
@role_required('teacher')
@approved_required
def dashboard_settings(class_id):
    """Save/load dashboard display settings"""
    class_obj = Class.query.get_or_404(class_id)

    # Verify teacher owns this class
    if class_obj.teacher_id != session['user_id']:
        return jsonify({'error': 'Unauthorized'}), 403

    if request.method == 'POST':
        settings = request.json
        return jsonify({'message': 'Settings saved', 'settings': settings})
    else:
        # Return default settings
        return jsonify({
            'visible_modules': {
                'arithmetic': True,
                'fractions': True,
                'decimals': True,
                'bodmas': True,
                'functions': True,
                'sets': True
            },
            'visible_difficulties': {
                'beginner': True,
                'intermediate': True,
                'advanced': True
            },
            'refresh_rate': 10,
            'students_per_page': 12
        })

# ==================== GUEST MANAGEMENT FOR TEACHERS ====================
# APIs for viewing and converting guest students to full accounts

def safe_date_str(val):
    """Safely convert a date/datetime value to ISO string"""
    if val is None:
        return None
    if isinstance(val, str):
        return val  # Already a string
    if hasattr(val, 'isoformat'):
        return val.isoformat()
    return str(val)

@teacher_bp.route('/api/teacher/guest-students')
@login_required
@role_required('teacher')
@approved_required
def get_teacher_guest_students():
    """Get all guest students with their progress - for teacher dashboard"""
    from sqlalchemy import text
    
    try:
        # Use SELECT * to avoid column name issues
        rows = db.session.execute(text("""
            SELECT * FROM guest_users 
            WHERE is_active = 1
            ORDER BY last_active DESC
            LIMIT 500
        """)).fetchall()
        
        guests = []
        for row in rows:
            # Safely extract data using _mapping if available
            if hasattr(row, '_mapping'):
                data = dict(row._mapping)
            else:
                # Fallback for older SQLAlchemy - use column indices
                # guest_users columns: id, guest_code, created_at, last_active, is_active, total_score, ...
                data = {
                    'guest_code': row[1] if len(row) > 1 else str(row[0]),
                    'total_score': row[5] if len(row) > 5 else 0,
                    'created_at': row[2] if len(row) > 2 else None,
                    'last_active': row[3] if len(row) > 3 else None,
                }
            
            guest_code = data.get('guest_code', '')
            
            guests.append({
                'guest_code': guest_code,
                'display_name': data.get('display_name') or guest_code,
                'total_score': data.get('total_score') or 0,
                'created_at': safe_date_str(data.get('created_at')),
                'last_active': safe_date_str(data.get('last_active')),
                'is_converted': data.get('user_id') is not None,
                'converted_at': safe_date_str(data.get('converted_at')),
                'full_name': data.get('full_name'),
                'teacher_id': data.get('teacher_id')
            })
        
        return jsonify({
            'guests': guests,
            'total': len(guests)
        })
        
    except Exception as e:
        print(f"Error getting guest students: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e), 'guests': [], 'total': 0}), 500


@teacher_bp.route('/api/teacher/guest-student/<guest_code>')
@login_required
@role_required('teacher')
@approved_required
def get_guest_student_details(guest_code):
    """Get detailed info about a specific guest student"""
    from sqlalchemy import text
    
    try:
        # Get guest user info
        guest = db.session.execute(text("""
            SELECT * FROM guest_users WHERE guest_code = :code
        """), {'code': guest_code.lower()}).fetchone()
        
        if not guest:
            return jsonify({'error': 'Guest code not found'}), 404
        
        if hasattr(guest, '_mapping'):
            data = dict(guest._mapping)
        else:
            data = {'guest_code': guest[0]}
        
        # Get quiz attempts count (handle missing table)
        quiz_count = 0
        try:
            quiz_count = db.session.execute(text("""
                SELECT COUNT(*) FROM user_question_history WHERE guest_code = :code
            """), {'code': guest_code.lower()}).scalar() or 0
        except:
            pass  # Table may not exist
        
        # Get adaptive level info (handle missing table)
        topic_levels = {}
        try:
            levels = db.session.execute(text("""
                SELECT topic, difficulty_level 
                FROM user_adaptive_level 
                WHERE guest_code = :code
            """), {'code': guest_code.lower()}).fetchall()
            
            for level in levels:
                if hasattr(level, '_mapping'):
                    level_data = dict(level._mapping)
                else:
                    level_data = {'topic': level[0], 'difficulty_level': level[1]}
                topic_levels[level_data['topic']] = level_data['difficulty_level']
        except:
            pass  # Table may not exist
        
        created = data.get('created_at')
        last_active = data.get('last_active')
        converted = data.get('converted_at')
        
        return jsonify({
            'guest_code': data.get('guest_code'),
            'display_name': data.get('display_name') or data.get('guest_code'),
            'total_score': data.get('total_score') or 0,
            'created_at': safe_date_str(created),
            'last_active': safe_date_str(last_active),
            'is_active': data.get('is_active', 1) == 1,
            'quiz_attempts': quiz_count,
            'topic_levels': topic_levels,
            'is_converted': data.get('user_id') is not None,
            'converted_at': safe_date_str(converted),
            'full_name': data.get('full_name'),
            'class_group': data.get('class_group'),
            'user_id': data.get('user_id'),
            'gdpr_parent_name': data.get('gdpr_parent_name'),
            'gdpr_parent_email': data.get('gdpr_parent_email')
        })
        
    except Exception as e:
        print(f"Error getting guest details: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@teacher_bp.route('/api/teacher/convert-guest', methods=['POST'])
@login_required
@role_required('teacher')
@approved_required
def convert_guest_to_account():
    """Convert a guest code to a full student account"""
    from sqlalchemy import text
    
    data = request.json
    guest_code = data.get('guest_code', '').strip().lower()
    full_name = data.get('full_name', '').strip()
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')
    class_group = data.get('class_group', '').strip()
    gdpr_consent_date = data.get('gdpr_consent_date')
    gdpr_parent_name = data.get('gdpr_parent_name', '').strip()
    gdpr_parent_email = data.get('gdpr_parent_email', '').strip().lower() if data.get('gdpr_parent_email') else None
    
    # Validation
    if not guest_code:
        return jsonify({'error': 'Guest code is required'}), 400
    if not full_name:
        return jsonify({'error': 'Student full name is required'}), 400
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    if not password or len(password) < 6:
        return jsonify({'error': 'Password must be at least 6 characters'}), 400
    if not gdpr_consent_date:
        return jsonify({'error': 'GDPR consent date is required'}), 400
    if not gdpr_parent_name:
        return jsonify({'error': 'Parent/guardian name is required'}), 400
    
    # Check email format - allow parentheses, plus signs, and other valid characters
    if not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email):
        return jsonify({'error': 'Invalid email format'}), 400
    
    try:
        # Check if guest code exists
        guest = db.session.execute(text("""
            SELECT guest_code, user_id, total_score FROM guest_users WHERE guest_code = :code
        """), {'code': guest_code}).fetchone()
        
        if not guest:
            return jsonify({'error': 'Guest code not found'}), 404
        
        if hasattr(guest, '_mapping'):
            guest_data = dict(guest._mapping)
        else:
            guest_data = {'guest_code': guest[0], 'user_id': guest[1], 'total_score': guest[2]}
        
        # Check if already converted
        if guest_data.get('user_id'):
            return jsonify({'error': 'This guest code has already been converted to an account'}), 400
        
        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'error': 'This email is already registered'}), 400
        
        # Create new user account
        new_user = User(
            email=email,
            full_name=full_name,
            role='student',
            is_approved=True
        )
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.flush()  # Get the new user ID
        
        teacher_id = session['user_id']
        
        # Update guest_users to link to new account
        db.session.execute(text("""
            UPDATE guest_users 
            SET user_id = :user_id,
                converted_at = :now,
                full_name = :full_name,
                class_group = :class_group,
                teacher_id = :teacher_id,
                gdpr_consent_date = :consent_date,
                gdpr_parent_name = :parent_name,
                gdpr_parent_email = :parent_email
            WHERE guest_code = :code
        """), {
            'user_id': new_user.id,
            'now': datetime.utcnow(),
            'full_name': full_name,
            'class_group': class_group,
            'teacher_id': teacher_id,
            'consent_date': gdpr_consent_date,
            'parent_name': gdpr_parent_name,
            'parent_email': gdpr_parent_email,
            'code': guest_code
        })
        
        # Create GDPR consent record
        db.session.execute(text("""
            INSERT INTO gdpr_consents 
            (guest_code, user_id, student_name, parent_name, parent_email, consent_date, 
             form_received_date, verified_by, consent_type)
            VALUES 
            (:guest_code, :user_id, :student_name, :parent_name, :parent_email, :consent_date,
             :received_date, :verified_by, 'parental')
        """), {
            'guest_code': guest_code,
            'user_id': new_user.id,
            'student_name': full_name,
            'parent_name': gdpr_parent_name,
            'parent_email': gdpr_parent_email,
            'consent_date': gdpr_consent_date,
            'received_date': datetime.utcnow().date(),
            'verified_by': teacher_id
        })
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': f'Successfully converted {guest_code} to account for {full_name}',
            'user': {
                'id': new_user.id,
                'email': new_user.email,
                'full_name': new_user.full_name
            },
            'points_preserved': guest_data.get('total_score') or 0
        }), 201
        
    except Exception as e:
        db.session.rollback()
        print(f"Error converting guest: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@teacher_bp.route('/api/teacher/lookup-guest/<guest_code>')
@login_required
@role_required('teacher')
@approved_required
def lookup_guest_for_enrollment(guest_code):
    """Look up a guest code to find the converted user for enrollment"""
    from sqlalchemy import text
    
    try:
        guest = db.session.execute(text("""
            SELECT guest_code, user_id, full_name, total_score, converted_at
            FROM guest_users 
            WHERE guest_code = :code
        """), {'code': guest_code.lower()}).fetchone()
        
        if not guest:
            return jsonify({'error': 'Guest code not found'}), 404
        
        if hasattr(guest, '_mapping'):
            data = dict(guest._mapping)
        else:
            data = {
                'guest_code': guest[0], 
                'user_id': guest[1], 
                'full_name': guest[2],
                'total_score': guest[3],
                'converted_at': guest[4]
            }
        
        if not data.get('user_id'):
            return jsonify({
                'found': True,
                'converted': False,
                'guest_code': data['guest_code'],
                'total_score': data.get('total_score') or 0,
                'message': 'This guest has not been converted to a full account yet'
            })
        
        # Get the user details
        user = User.query.get(data['user_id'])
        if not user:
            return jsonify({'error': 'Linked user account not found'}), 404
        
        converted = data.get('converted_at')
        
        return jsonify({
            'found': True,
            'converted': True,
            'guest_code': data['guest_code'],
            'user_id': user.id,
            'full_name': user.full_name,
            'email': user.email,
            'total_score': data.get('total_score') or 0,
            'converted_at': safe_date_str(converted)
        })
        
    except Exception as e:
        print(f"Error looking up guest: {e}")
        return jsonify({'error': str(e)}), 500


@teacher_bp.route('/api/teacher/class/<int:class_id>/enroll-by-guest-code', methods=['POST'])
@login_required
@role_required('teacher')
@approved_required
def enroll_student_by_guest_code(class_id):
    """Enroll a converted guest student by their guest code"""
    from sqlalchemy import text
    
    class_obj = Class.query.get_or_404(class_id)
    teacher_id = session['user_id']
    
    if class_obj.teacher_id != teacher_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.json
    guest_code = data.get('guest_code', '').strip().lower()
    
    if not guest_code:
        return jsonify({'error': 'Guest code is required'}), 400
    
    try:
        # Look up the guest to get linked user_id
        guest = db.session.execute(text("""
            SELECT user_id, full_name FROM guest_users WHERE guest_code = :code
        """), {'code': guest_code}).fetchone()
        
        if not guest:
            return jsonify({'error': 'Guest code not found'}), 404
        
        if hasattr(guest, '_mapping'):
            guest_data = dict(guest._mapping)
        else:
            guest_data = {'user_id': guest[0], 'full_name': guest[1]}
        
        user_id = guest_data.get('user_id')
        
        if not user_id:
            return jsonify({
                'error': 'This guest has not been converted to a full account yet. Please convert first.'
            }), 400
        
        # Check if already enrolled
        existing = ClassEnrollment.query.filter_by(
            class_id=class_id, 
            student_id=user_id
        ).first()
        
        if existing:
            return jsonify({
                'error': f'{guest_data.get("full_name") or guest_code} is already enrolled in this class'
            }), 400
        
        # Enroll the student
        enrollment = ClassEnrollment(
            class_id=class_id,
            student_id=user_id
        )
        db.session.add(enrollment)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': f'Successfully enrolled {guest_data.get("full_name") or guest_code} in {class_obj.name}',
            'enrollment': {
                'class_id': class_id,
                'student_id': user_id,
                'guest_code': guest_code
            }
        })
        
    except Exception as e:
        db.session.rollback()
        print(f"Error enrolling by guest code: {e}")
        return jsonify({'error': str(e)}), 500


@teacher_bp.route('/api/teacher/edit-converted-student', methods=['POST'])
@login_required
@role_required('teacher')
@approved_required
def edit_converted_student():
    """Edit details of a converted student account"""
    from sqlalchemy import text
    
    data = request.json
    guest_code = data.get('guest_code', '').strip().lower()
    full_name = data.get('full_name', '').strip()
    email = data.get('email', '').strip().lower()
    new_password = data.get('new_password', '').strip()  # Optional
    class_group = data.get('class_group', '').strip()
    gdpr_parent_email = data.get('gdpr_parent_email', '').strip().lower() if data.get('gdpr_parent_email') else None
    
    if not guest_code:
        return jsonify({'error': 'Guest code is required'}), 400
    if not full_name:
        return jsonify({'error': 'Student name is required'}), 400
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    
    # Check email format - allow parentheses, plus signs, and other valid characters
    if not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email):
        return jsonify({'error': 'Invalid email format'}), 400
    
    try:
        # Get the guest record to find linked user_id
        guest = db.session.execute(text("""
            SELECT user_id FROM guest_users WHERE guest_code = :code
        """), {'code': guest_code}).fetchone()
        
        if not guest:
            return jsonify({'error': 'Guest code not found'}), 404
        
        if hasattr(guest, '_mapping'):
            guest_data = dict(guest._mapping)
        else:
            guest_data = {'user_id': guest[0]}
        
        user_id = guest_data.get('user_id')
        
        if not user_id:
            return jsonify({'error': 'This guest has not been converted yet'}), 400
        
        # Get the user
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User account not found'}), 404
        
        # Check if new email is already taken by another user
        if email != user.email:
            existing = User.query.filter_by(email=email).first()
            if existing and existing.id != user_id:
                return jsonify({'error': 'This email is already in use by another account'}), 400
        
        # Update user details
        user.full_name = full_name
        user.email = email
        
        # Update password if provided
        if new_password:
            if len(new_password) < 6:
                return jsonify({'error': 'Password must be at least 6 characters'}), 400
            user.set_password(new_password)
        
        # Update guest_users record too (including parent email)
        db.session.execute(text("""
            UPDATE guest_users 
            SET full_name = :full_name,
                class_group = :class_group,
                gdpr_parent_email = :parent_email
            WHERE guest_code = :code
        """), {
            'full_name': full_name,
            'class_group': class_group,
            'parent_email': gdpr_parent_email,
            'code': guest_code
        })
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': f'Successfully updated {full_name}',
            'user': {
                'id': user.id,
                'email': user.email,
                'full_name': user.full_name
            },
            'password_changed': bool(new_password)
        })
        
    except Exception as e:
        db.session.rollback()
        print(f"Error editing converted student: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@teacher_bp.route('/api/teacher/guest-stats')
@login_required
@role_required('teacher')
@approved_required
def get_guest_stats():
    """Get summary statistics about guest students"""
    from sqlalchemy import text
    
    try:
        stats = {}
        
        # Total active guests
        stats['total_guests'] = db.session.execute(text(
            "SELECT COUNT(*) FROM guest_users WHERE is_active = 1"
        )).scalar() or 0
        
        # Converted guests
        stats['converted_guests'] = db.session.execute(text(
            "SELECT COUNT(*) FROM guest_users WHERE user_id IS NOT NULL"
        )).scalar() or 0
        
        # Pending conversion (active but not converted)
        stats['pending_conversion'] = db.session.execute(text(
            "SELECT COUNT(*) FROM guest_users WHERE is_active = 1 AND user_id IS NULL"
        )).scalar() or 0
        
        # Active in last 7 days
        seven_days_ago = datetime.utcnow() - timedelta(days=7)
        stats['active_last_7_days'] = db.session.execute(text(
            "SELECT COUNT(*) FROM guest_users WHERE last_active > :since"
        ), {'since': seven_days_ago}).scalar() or 0
        
        # Active in last 30 days
        thirty_days_ago = datetime.utcnow() - timedelta(days=30)
        stats['active_last_30_days'] = db.session.execute(text(
            "SELECT COUNT(*) FROM guest_users WHERE last_active > :since"
        ), {'since': thirty_days_ago}).scalar() or 0
        
        return jsonify(stats)
        
    except Exception as e:
        print(f"Error getting guest stats: {e}")
        return jsonify({'error': str(e)}), 500




# ============================================================
# Minimal class actions via simple HTML forms (stable)
# ============================================================

@teacher_bp.route('/teacher/class/<int:class_id>/rename', methods=['POST'], endpoint='teacher_simple_rename_class')
@login_required
@role_required('teacher')
@approved_required
def teacher_simple_rename_class(class_id):
    from flask import flash
    class_obj = Class.query.get_or_404(class_id)
    if class_obj.teacher_id != session.get('user_id'):
        return jsonify({'error': 'Unauthorized'}), 403

    new_name = (request.form.get('new_name') or '').strip()
    if not new_name:
        flash('Class name cannot be empty.', 'error')
        return redirect('/teacher/classes')

    existing = Class.query.filter(
        Class.teacher_id == session['user_id'],
        Class.name == new_name,
        Class.id != class_id
    ).first()
    if existing:
        flash('You already have a class with that name.', 'error')
        return redirect('/teacher/classes')

    class_obj.name = new_name
    db.session.commit()
    flash('Class renamed successfully.', 'success')
    return redirect('/teacher/classes')


@teacher_bp.route('/teacher/class/<int:class_id>/delete', methods=['POST'], endpoint='teacher_simple_delete_class')
@login_required
@role_required('teacher')
@approved_required
def teacher_simple_delete_class(class_id):
    from flask import flash
    class_obj = Class.query.get_or_404(class_id)
    if class_obj.teacher_id != session.get('user_id'):
        return jsonify({'error': 'Unauthorized'}), 403

    ClassEnrollment.query.filter_by(class_id=class_id).delete()
    db.session.delete(class_obj)
    db.session.commit()
    flash('Class deleted.', 'success')
    return redirect('/teacher/classes')
