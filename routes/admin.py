# routes/admin.py
# Admin routes for AgentMath
# Extracted from app.py for better maintainability
#
# Revision: 1.1.2
# Date: 2025-01-02
# Phase 7: Admin routes extraction
#
# Fixes in 1.1.2:
# - Fixed legacy questions table query - was missing times_shown/times_correct/is_active columns
# - Added COALESCE for image_url/question_image_svg in legacy table
# - Both tables use 0-indexed correct_answer (0=A, 1=B, 2=C, 3=D)
#
# Fixes in 1.1.1:
# - CRITICAL: Fixed correct_answer conversion - database uses 0-indexed (0-3), not 1-indexed (1-4)
#
# Fixes in 1.0.5:
# - Fixed datetime handling in feedback API (SQLite returns strings)
#
# Fixes in 1.0.4:
# - Fixed ALL url_for() calls to use blueprint prefix 'admin.'
# - url_for('admin_who_am_i') → url_for('admin.admin_who_am_i')
# - url_for('admin_dashboard') → url_for('admin.admin_dashboard')
#
# Fixes in 1.0.3:
# - Fixed admin_required decorator (duplicate return, wrong url_for references)
#
# Fixes in 1.0.2:
# - Added complete feedback API backend (stats, list, update, delete)
# - Auto-creates user_feedback table if it doesn't exist
#
# Fixes in 1.0.1:
# - Added /admin/feedback route (was missing, causing 404)
# - Added input validation to /api/admin/raffles POST endpoint
#
# Contains 137 admin routes across 13 sections:
# - Main Admin (dashboard, teachers, users, classes, domains)
# - Question Flag Management  
# - Prize System Admin
# - Who Am I Admin
# - Raffle Admin
# - Question History Admin
# - Analytics Admin
# - Site Settings Admin
# - Resources Admin
# - Puzzles Admin
# - Email Reports Admin

from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for, flash, current_app
from functools import wraps
from datetime import datetime, timedelta, date
from werkzeug.utils import secure_filename
import os
import json
import traceback
import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create blueprint
admin_bp = Blueprint('admin', __name__)

# Import database and models
from models import (
    db, User, Class, ClassEnrollment, Question, QuestionFlag,
    AdaptiveQuestionFlag, QuestionEdit, QuizAttempt, Badge, UserBadge,
    UserStats, TopicProgress, AvatarItem, UserAvatarInventory,
    UserAvatarEquipped, SystemSetting, PrizeSchool, Prize, SchoolPrize,
    PrizeRedemption, SchoolRequest, RaffleDraw, TeacherDomainAccess,
    DomainAccessRequest, WeeklyPuzzle, PuzzleUserStatus
)

# Import decorators from utils
from utils import login_required, role_required

# Import domain helpers
from utils import (
    extract_domain, get_all_domains_in_system, teacher_has_domain_access,
    get_teacher_accessible_domains, filter_students_by_domain_access,
    get_teacher_domain_statistics
)


# ==================== CONFIGURATION ====================
# Who Am I image upload configuration
UPLOAD_FOLDER = 'static/who_am_i_images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def allowed_file(filename):
    """Check if file extension is allowed for upload"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




def get_current_week_year():
    """Get the current ISO week number and year"""
    from datetime import datetime
    now = datetime.now()
    week_number = now.isocalendar()[1]
    year = now.isocalendar()[0]
    return week_number, year

# ==================== ADMIN ROUTES ====================

@admin_bp.route('/admin')
@login_required
@role_required('admin')
def admin_dashboard():
    return render_template('admin_dashboard.html')


@admin_bp.route('/admin/feedback')
@login_required
@role_required('admin')
def admin_feedback():
    """Admin page for viewing user feedback and flagged questions"""
    return render_template('admin_feedback.html')


# ==================== FEEDBACK API ROUTES ====================

@admin_bp.route('/api/admin/feedback/stats')
@login_required
@role_required('admin')
def api_admin_feedback_stats():
    """Get feedback statistics for dashboard cards"""
    from sqlalchemy import text
    
    try:
        # Check if user_feedback table exists
        table_check = db.session.execute(text("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='user_feedback'
        """)).fetchone()
        
        if not table_check:
            # Table doesn't exist yet - return empty stats
            return jsonify({
                'total': 0,
                'new': 0,
                'actioned': 0,
                'avg_rating': 0
            })
        
        stats = db.session.execute(text("""
            SELECT 
                COUNT(*) as total,
                SUM(CASE WHEN status = 'new' THEN 1 ELSE 0 END) as new_count,
                SUM(CASE WHEN status = 'actioned' THEN 1 ELSE 0 END) as actioned_count,
                AVG(CASE WHEN rating IS NOT NULL THEN rating ELSE NULL END) as avg_rating
            FROM user_feedback
        """)).fetchone()
        
        return jsonify({
            'total': stats[0] or 0,
            'new': stats[1] or 0,
            'actioned': stats[2] or 0,
            'avg_rating': round(stats[3], 1) if stats[3] else 0
        })
        
    except Exception as e:
        print(f"Error getting feedback stats: {e}")
        return jsonify({
            'total': 0,
            'new': 0,
            'actioned': 0,
            'avg_rating': 0
        })


@admin_bp.route('/api/admin/feedback')
@login_required
@role_required('admin')
def api_admin_feedback_list():
    """Get list of user feedback with filtering and pagination"""
    from sqlalchemy import text
    
    status = request.args.get('status', 'new')
    category = request.args.get('category', 'all')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 20))
    
    try:
        # Check if user_feedback table exists
        table_check = db.session.execute(text("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='user_feedback'
        """)).fetchone()
        
        if not table_check:
            # Table doesn't exist - create it
            db.session.execute(text("""
                CREATE TABLE IF NOT EXISTS user_feedback (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    user_name VARCHAR(100),
                    user_email VARCHAR(255),
                    feedback_text TEXT NOT NULL,
                    category VARCHAR(50) DEFAULT 'general',
                    rating INTEGER,
                    status VARCHAR(20) DEFAULT 'new',
                    page_context VARCHAR(255),
                    topic_context VARCHAR(255),
                    admin_notes TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """))
            db.session.commit()
            
            return jsonify({
                'feedback': [],
                'total': 0,
                'page': page,
                'per_page': per_page,
                'total_pages': 0
            })
        
        # Build query with filters
        where_clauses = []
        params = {}
        
        if status and status != 'all':
            where_clauses.append("status = :status")
            params['status'] = status
        
        if category and category != 'all':
            where_clauses.append("category = :category")
            params['category'] = category
        
        where_sql = "WHERE " + " AND ".join(where_clauses) if where_clauses else ""
        
        # Get total count
        count_query = f"SELECT COUNT(*) FROM user_feedback {where_sql}"
        total = db.session.execute(text(count_query), params).scalar() or 0
        
        # Get paginated results
        offset = (page - 1) * per_page
        params['limit'] = per_page
        params['offset'] = offset
        
        query = f"""
            SELECT id, user_id, user_name, user_email, feedback_text, 
                   category, rating, status, page_context, topic_context,
                   admin_notes, created_at, updated_at
            FROM user_feedback 
            {where_sql}
            ORDER BY created_at DESC
            LIMIT :limit OFFSET :offset
        """
        
        results = db.session.execute(text(query), params).fetchall()
        
        feedback_list = [{
            'id': r[0],
            'user_id': r[1],
            'user_name': r[2],
            'user_email': r[3],
            'feedback_text': r[4],
            'category': r[5],
            'rating': r[6],
            'status': r[7],
            'page_context': r[8],
            'topic_context': r[9],
            'admin_notes': r[10],
            # SQLite returns timestamps as strings, handle both cases
            'created_at': r[11] if isinstance(r[11], str) else (r[11].isoformat() if r[11] else None),
            'updated_at': r[12] if isinstance(r[12], str) else (r[12].isoformat() if r[12] else None)
        } for r in results]
        
        return jsonify({
            'feedback': feedback_list,
            'total': total,
            'page': page,
            'per_page': per_page,
            'total_pages': (total + per_page - 1) // per_page
        })
        
    except Exception as e:
        print(f"Error getting feedback list: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/admin/feedback/<int:feedback_id>', methods=['PUT'])
@login_required
@role_required('admin')
def api_admin_feedback_update(feedback_id):
    """Update feedback status or admin notes"""
    from sqlalchemy import text
    
    data = request.json
    
    try:
        update_fields = []
        params = {'feedback_id': feedback_id}
        
        if 'status' in data:
            update_fields.append("status = :status")
            params['status'] = data['status']
        
        if 'admin_notes' in data:
            update_fields.append("admin_notes = :admin_notes")
            params['admin_notes'] = data['admin_notes']
        
        if not update_fields:
            return jsonify({'error': 'No fields to update'}), 400
        
        update_fields.append("updated_at = CURRENT_TIMESTAMP")
        
        query = f"UPDATE user_feedback SET {', '.join(update_fields)} WHERE id = :feedback_id"
        db.session.execute(text(query), params)
        db.session.commit()
        
        return jsonify({'success': True})
        
    except Exception as e:
        db.session.rollback()
        print(f"Error updating feedback: {e}")
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/admin/feedback/<int:feedback_id>', methods=['DELETE'])
@login_required
@role_required('admin')
def api_admin_feedback_delete(feedback_id):
    """Delete a feedback entry"""
    from sqlalchemy import text
    
    try:
        db.session.execute(text(
            "DELETE FROM user_feedback WHERE id = :feedback_id"
        ), {'feedback_id': feedback_id})
        db.session.commit()
        
        return jsonify({'success': True})
        
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting feedback: {e}")
        return jsonify({'error': str(e)}), 500

@admin_bp.route('/api/admin/pending-teachers')
@login_required
@role_required('admin')
def pending_teachers():
    teachers = User.query.filter_by(role='teacher', is_approved=False).all()
    return jsonify([t.to_dict() for t in teachers])

@admin_bp.route('/api/admin/approve-teacher/<int:teacher_id>', methods=['POST'])
@login_required
@role_required('admin')
def approve_teacher(teacher_id):
    teacher = User.query.get_or_404(teacher_id)

    if teacher.role != 'teacher':
        return jsonify({'error': 'User is not a teacher'}), 400

    teacher.is_approved = True
    db.session.commit()

    return jsonify({'message': 'Teacher approved successfully'})

@admin_bp.route('/api/admin/all-users')
@login_required
@role_required('admin')
def all_users():
    role_filter = request.args.get('role')

    query = User.query
    if role_filter:
        query = query.filter_by(role=role_filter)

    users = query.all()
    return jsonify([u.to_dict() for u in users])

@admin_bp.route('/api/admin/all-classes')
@login_required
@role_required('admin')
def all_classes():
    classes = Class.query.all()
    return jsonify([c.to_dict() for c in classes])

@admin_bp.route('/api/admin/rename-class/<int:class_id>', methods=['PUT'])
@login_required
@role_required('admin')
def rename_class(class_id):
    class_obj = Class.query.get_or_404(class_id)
    data = request.json
    new_name = data.get('name', '').strip()

    if not new_name:
        return jsonify({'error': 'Class name required'}), 400

    class_obj.name = new_name
    db.session.commit()

    return jsonify({'message': 'Class renamed successfully', 'class': class_obj.to_dict()})

@admin_bp.route('/api/admin/reassign-student', methods=['POST'])
@login_required
@role_required('admin')
def reassign_student():
    data = request.json
    student_id = data.get('student_id')
    from_class_id = data.get('from_class_id')
    to_class_id = data.get('to_class_id')

    if not all([student_id, from_class_id, to_class_id]):
        return jsonify({'error': 'Missing required parameters'}), 400

    # Remove from old class
    old_enrollment = ClassEnrollment.query.filter_by(class_id=from_class_id, student_id=student_id).first()
    if old_enrollment:
        db.session.delete(old_enrollment)

    # Add to new class
    new_enrollment = ClassEnrollment(class_id=to_class_id, student_id=student_id)
    db.session.add(new_enrollment)
    db.session.commit()

    return jsonify({'message': 'Student reassigned successfully'})

@admin_bp.route('/api/admin/class-comparison')
@login_required
@role_required('admin')
def class_comparison():
    classes = Class.query.all()
    comparison_data = []

    for class_obj in classes:
        enrollments = ClassEnrollment.query.filter_by(class_id=class_obj.id).all()
        student_ids = [e.student_id for e in enrollments]

        attempts = QuizAttempt.query.filter(QuizAttempt.user_id.in_(student_ids)).all()

        avg_score = sum(a.percentage for a in attempts) / len(attempts) if attempts else 0

        comparison_data.append({
            'class_id': class_obj.id,
            'class_name': class_obj.name,
            'teacher_name': class_obj.teacher.full_name,
            'student_count': len(enrollments),
            'total_quizzes': len(attempts),
            'average_score': round(avg_score, 2)
        })

    return jsonify(comparison_data)


# ==================== USER MANAGEMENT ADMIN ROUTES ====================

@admin_bp.route('/admin/users')
@login_required
@role_required('admin')
def admin_user_management():
    """Admin page for managing all users"""
    return render_template('admin_user_management.html')

@admin_bp.route('/api/admin/user/<int:user_id>', methods=['GET'])
@login_required
@role_required('admin')
def get_user_details(user_id):
    """Get detailed user information"""
    user = User.query.get_or_404(user_id)

    # Get additional stats
    stats = UserStats.query.filter_by(user_id=user_id).first()
    quiz_count = QuizAttempt.query.filter_by(user_id=user_id).count()

    # Get class enrollments if student
    classes = []
    if user.role == 'student':
        enrollments = ClassEnrollment.query.filter_by(student_id=user_id).all()
        classes = [{'id': e.class_obj.id, 'name': e.class_obj.name,
                   'teacher': e.class_obj.teacher.full_name} for e in enrollments]

    # Get classes teaching if teacher
    elif user.role == 'teacher':
        teaching_classes = Class.query.filter_by(teacher_id=user_id).all()
        classes = [{'id': c.id, 'name': c.name,
                   'student_count': len(c.enrollments)} for c in teaching_classes]

    return jsonify({
        'user': user.to_dict(),
        'stats': {
            'total_points': stats.total_points if stats else 0,
            'level': stats.level if stats else 1,
            'quiz_count': quiz_count
        },
        'classes': classes
    })

@admin_bp.route('/api/admin/user/<int:user_id>', methods=['PUT'])
@login_required
@role_required('admin')
def update_user(user_id):
    """Update user details (name, email)"""
    user = User.query.get_or_404(user_id)
    data = request.json

    # Update name
    if 'full_name' in data:
        new_name = data['full_name'].strip()
        if new_name:
            user.full_name = new_name

    # Update email (check for duplicates)
    if 'email' in data:
        new_email = data['email'].strip().lower()
        if new_email and new_email != user.email:
            existing = User.query.filter_by(email=new_email).first()
            if existing:
                return jsonify({'error': 'Email already in use'}), 400
            user.email = new_email

    # Update approval status
    if 'is_approved' in data:
        user.is_approved = data['is_approved']

    db.session.commit()

    return jsonify({
        'message': 'User updated successfully',
        'user': user.to_dict()
    })

@admin_bp.route('/api/admin/user/<int:user_id>', methods=['DELETE'])
@login_required
@role_required('admin')
def delete_user(user_id):
    """Delete a user and all associated data"""
    try:
        user = User.query.get_or_404(user_id)

        # Don't allow deleting yourself
        if user.id == session['user_id']:
            return jsonify({'error': 'Cannot delete your own account'}), 400

        # Don't allow deleting other admins
        if user.role == 'admin':
            return jsonify({'error': 'Cannot delete admin accounts'}), 403

        # Delete associated data in proper order to avoid foreign key violations

        # 1. Quiz attempts
        QuizAttempt.query.filter_by(user_id=user_id).delete()

        # 2. User stats
        UserStats.query.filter_by(user_id=user_id).delete()

        # 3. Topic progress
        TopicProgress.query.filter_by(user_id=user_id).delete()

        # 4. User badges
        UserBadge.query.filter_by(user_id=user_id).delete()

        # 5. Question flags - BOTH as reporter AND as resolver
        QuestionFlag.query.filter_by(user_id=user_id).delete()
        # Set resolved_by to NULL for flags this user resolved
        QuestionFlag.query.filter_by(resolved_by=user_id).update({'resolved_by': None})

        # 6. Question edits - Set editor to NULL (keep edit history but anonymize)
        QuestionEdit.query.filter_by(edited_by=user_id).update({'edited_by': None})

        # 7. Domain access records (for teachers)
        TeacherDomainAccess.query.filter_by(teacher_id=user_id).delete()
        # Set granted_by to NULL for domain access this admin granted
        TeacherDomainAccess.query.filter_by(granted_by=user_id).update({'granted_by': None})

        # 8. Domain access requests
        DomainAccessRequest.query.filter_by(teacher_id=user_id).delete()
        # Set reviewed_by to NULL for requests this admin reviewed
        DomainAccessRequest.query.filter_by(reviewed_by=user_id).update({'reviewed_by': None})

        # 9. Class enrollments (if student)
        ClassEnrollment.query.filter_by(student_id=user_id).delete()

        # 10. Classes (if teacher) - also delete all enrollments
        if user.role == 'teacher':
            classes = Class.query.filter_by(teacher_id=user_id).all()
            for class_obj in classes:
                ClassEnrollment.query.filter_by(class_id=class_obj.id).delete()
                db.session.delete(class_obj)

        # Finally, delete the user
        db.session.delete(user)
        db.session.commit()

        return jsonify({
            'message': f'User {user.full_name} deleted successfully'
        })

    except Exception as e:
        db.session.rollback()
        print(f"Error deleting user {user_id}: {str(e)}")  # Log the error
        return jsonify({
            'error': f'Failed to delete user: {str(e)}'
        }), 500

@admin_bp.route('/api/admin/users/bulk-delete', methods=['POST'])
@login_required
@role_required('admin')
def bulk_delete_users():
    """Delete multiple users at once"""
    try:
        data = request.json
        user_ids = data.get('user_ids', [])

        if not user_ids:
            return jsonify({'error': 'No users selected'}), 400

        deleted_count = 0
        errors = []

        for user_id in user_ids:
            try:
                user = User.query.get(user_id)

                if not user:
                    errors.append(f"User {user_id} not found")
                    continue

                # Don't allow deleting yourself
                if user.id == session['user_id']:
                    errors.append(f"Cannot delete your own account")
                    continue

                # Don't allow deleting other admins
                if user.role == 'admin':
                    errors.append(f"Cannot delete admin account: {user.full_name}")
                    continue

                # Delete associated data (same as single delete)
                QuizAttempt.query.filter_by(user_id=user_id).delete()
                UserStats.query.filter_by(user_id=user_id).delete()
                TopicProgress.query.filter_by(user_id=user_id).delete()
                UserBadge.query.filter_by(user_id=user_id).delete()

                QuestionFlag.query.filter_by(user_id=user_id).delete()
                QuestionFlag.query.filter_by(resolved_by=user_id).update({'resolved_by': None})

                QuestionEdit.query.filter_by(edited_by=user_id).update({'edited_by': None})

                TeacherDomainAccess.query.filter_by(teacher_id=user_id).delete()
                TeacherDomainAccess.query.filter_by(granted_by=user_id).update({'granted_by': None})

                DomainAccessRequest.query.filter_by(teacher_id=user_id).delete()
                DomainAccessRequest.query.filter_by(reviewed_by=user_id).update({'reviewed_by': None})

                ClassEnrollment.query.filter_by(student_id=user_id).delete()

                if user.role == 'teacher':
                    classes = Class.query.filter_by(teacher_id=user_id).all()
                    for class_obj in classes:
                        ClassEnrollment.query.filter_by(class_id=class_obj.id).delete()
                        db.session.delete(class_obj)

                # Delete the user
                db.session.delete(user)
                deleted_count += 1

            except Exception as e:
                errors.append(f"Error deleting user {user_id}: {str(e)}")
                continue

        # Commit all deletions
        db.session.commit()

        response_data = {
            'deleted_count': deleted_count,
            'total_requested': len(user_ids)
        }

        if errors:
            response_data['errors'] = errors

        return jsonify(response_data)

    except Exception as e:
        db.session.rollback()
        print(f"Error in bulk delete: {str(e)}")
        return jsonify({
            'error': f'Failed to delete users: {str(e)}'
        }), 500

@admin_bp.route('/api/admin/user/<int:user_id>/toggle-approval', methods=['POST'])
@login_required
@role_required('admin')
def toggle_user_approval(user_id):
    """Toggle user approval status"""
    user = User.query.get_or_404(user_id)

    user.is_approved = not user.is_approved
    db.session.commit()

    status = 'approved' if user.is_approved else 'unapproved'

    return jsonify({
        'message': f'User {status} successfully',
        'is_approved': user.is_approved
    })



# ==================== DOMAIN MANAGEMENT ADMIN ROUTES ====================

@admin_bp.route('/api/admin/domains')
@login_required
@role_required('admin')
def get_all_domains():
    """Get all email domains in the system with statistics"""
    domains = get_all_domains_in_system()
    domains.sort(key=lambda x: x['student_count'], reverse=True)
    return jsonify({
        'domains': domains,
        'total_domains': len(domains)
    })


@admin_bp.route('/api/admin/teacher/<int:teacher_id>/domains')
@login_required
@role_required('admin')
def get_teacher_domains(teacher_id):
    """Get all domains assigned to a specific teacher"""
    teacher = User.query.get_or_404(teacher_id)
    if teacher.role != 'teacher':
        return jsonify({'error': 'User is not a teacher'}), 400
    access_records = TeacherDomainAccess.query.filter_by(teacher_id=teacher_id).all()
    stats = get_teacher_domain_statistics(teacher_id)
    all_domains = get_all_domains_in_system()
    return jsonify({
        'teacher': teacher.to_dict(),
        'assigned_domains': [r.to_dict() for r in access_records],
        'statistics': stats,
        'available_domains': all_domains
    })


@admin_bp.route('/api/admin/teacher/<int:teacher_id>/domains', methods=['POST'])
@login_required
@role_required('admin')
def assign_domain_to_teacher(teacher_id):
    """Assign a domain to a teacher"""
    teacher = User.query.get_or_404(teacher_id)
    if teacher.role != 'teacher':
        return jsonify({'error': 'User is not a teacher'}), 400
    data = request.json
    domain = data.get('domain', '').strip().lower()
    notes = data.get('notes', '').strip()
    if not domain:
        return jsonify({'error': 'Domain is required'}), 400
    if '.' not in domain or '@' in domain:
        return jsonify({'error': 'Invalid domain format. Use format like: school.edu'}), 400
    existing = TeacherDomainAccess.query.filter_by(teacher_id=teacher_id, email_domain=domain).first()
    if existing:
        return jsonify({'error': 'Domain already assigned to this teacher'}), 400
    access = TeacherDomainAccess(teacher_id=teacher_id, email_domain=domain, granted_by=session['user_id'], notes=notes)
    db.session.add(access)
    pending_request = DomainAccessRequest.query.filter_by(teacher_id=teacher_id, email_domain=domain, status='pending').first()
    if pending_request:
        pending_request.status = 'approved'
        pending_request.reviewed_by = session['user_id']
        pending_request.reviewed_at = datetime.utcnow()
        pending_request.admin_notes = 'Automatically approved when domain was granted'
    db.session.commit()
    return jsonify({'message': 'Domain access granted successfully', 'access': access.to_dict()}), 201


@admin_bp.route('/api/admin/teacher/<int:teacher_id>/domains/<domain>', methods=['DELETE'])
@login_required
@role_required('admin')
def revoke_domain_from_teacher(teacher_id, domain):
    """Revoke a domain from a teacher"""
    domain = domain.lower()
    access = TeacherDomainAccess.query.filter_by(teacher_id=teacher_id, email_domain=domain).first()
    if not access:
        return jsonify({'error': 'Domain access not found'}), 404
    db.session.delete(access)
    db.session.commit()
    return jsonify({'message': 'Domain access revoked successfully'})


@admin_bp.route('/api/admin/teacher/<int:teacher_id>/domains/bulk', methods=['POST'])
@login_required
@role_required('admin')
def assign_domains_bulk(teacher_id):
    """Assign multiple domains to a teacher at once"""
    teacher = User.query.get_or_404(teacher_id)
    if teacher.role != 'teacher':
        return jsonify({'error': 'User is not a teacher'}), 400
    data = request.json
    domains = data.get('domains', [])
    notes = data.get('notes', '').strip()
    if not domains:
        return jsonify({'error': 'No domains provided'}), 400
    added, already_assigned, invalid = [], [], []
    for domain in domains:
        domain = domain.strip().lower()
        if '.' not in domain or '@' in domain:
            invalid.append(domain)
            continue
        existing = TeacherDomainAccess.query.filter_by(teacher_id=teacher_id, email_domain=domain).first()
        if existing:
            already_assigned.append(domain)
            continue
        access = TeacherDomainAccess(teacher_id=teacher_id, email_domain=domain, granted_by=session['user_id'], notes=notes)
        db.session.add(access)
        added.append(domain)
        pending_request = DomainAccessRequest.query.filter_by(teacher_id=teacher_id, email_domain=domain, status='pending').first()
        if pending_request:
            pending_request.status = 'approved'
            pending_request.reviewed_by = session['user_id']
            pending_request.reviewed_at = datetime.utcnow()
            pending_request.admin_notes = 'Automatically approved in bulk assignment'
    db.session.commit()
    return jsonify({'message': f'Processed {len(domains)} domains', 'added': added, 'already_assigned': already_assigned, 'invalid': invalid, 'added_count': len(added)})


@admin_bp.route('/api/admin/domain-requests')
@login_required
@role_required('admin')
def get_domain_requests():
    """Get all domain access requests"""
    status_filter = request.args.get('status', 'pending')
    query = DomainAccessRequest.query
    if status_filter and status_filter != 'all':
        query = query.filter_by(status=status_filter)
    requests = query.order_by(DomainAccessRequest.requested_at.desc()).all()
    return jsonify({'requests': [r.to_dict() for r in requests], 'total': len(requests)})


@admin_bp.route('/api/admin/domain-requests/<int:request_id>/approve', methods=['POST'])
@login_required
@role_required('admin')
def approve_domain_request(request_id):
    """Approve a domain access request"""
    access_request = DomainAccessRequest.query.get_or_404(request_id)
    if access_request.status != 'pending':
        return jsonify({'error': 'Request is not pending'}), 400
    data = request.json
    admin_notes = data.get('admin_notes', '').strip()
    access = TeacherDomainAccess(teacher_id=access_request.teacher_id, email_domain=access_request.email_domain, granted_by=session['user_id'], notes=f"Requested: {access_request.reason}")
    access_request.status = 'approved'
    access_request.reviewed_by = session['user_id']
    access_request.reviewed_at = datetime.utcnow()
    access_request.admin_notes = admin_notes
    db.session.add(access)
    db.session.commit()
    return jsonify({'message': 'Domain access request approved', 'access': access.to_dict(), 'request': access_request.to_dict()})


@admin_bp.route('/api/admin/domain-requests/<int:request_id>/deny', methods=['POST'])
@login_required
@role_required('admin')
def deny_domain_request(request_id):
    """Deny a domain access request"""
    access_request = DomainAccessRequest.query.get_or_404(request_id)
    if access_request.status != 'pending':
        return jsonify({'error': 'Request is not pending'}), 400
    data = request.json
    admin_notes = data.get('admin_notes', '').strip()
    if not admin_notes:
        return jsonify({'error': 'Please provide a reason for denial'}), 400
    access_request.status = 'denied'
    access_request.reviewed_by = session['user_id']
    access_request.reviewed_at = datetime.utcnow()
    access_request.admin_notes = admin_notes
    db.session.commit()
    return jsonify({'message': 'Domain access request denied', 'request': access_request.to_dict()})


@admin_bp.route('/api/admin/teacher/<int:teacher_id>/remove-all-restrictions', methods=['POST'])
@login_required
@role_required('admin')
def remove_all_teacher_restrictions(teacher_id):
    """Remove all domain restrictions from a teacher (grant full access)"""
    teacher = User.query.get_or_404(teacher_id)
    if teacher.role != 'teacher':
        return jsonify({'error': 'User is not a teacher'}), 400
    TeacherDomainAccess.query.filter_by(teacher_id=teacher_id).delete()
    db.session.commit()
    return jsonify({'message': 'All domain restrictions removed. Teacher now has full access to all students.'})


@admin_bp.route('/api/admin/flags/pending')
@login_required
@role_required('admin')
def get_pending_flags():
    """Get all pending question flags (both standard and adaptive)"""
    # Standard question flags
    standard_flags = QuestionFlag.query.filter_by(status='pending').order_by(QuestionFlag.created_at.desc()).all()

    flags_with_questions = []
    for flag in standard_flags:
        flag_dict = flag.to_dict()
        flag_dict['question'] = flag.question.to_dict()
        flag_dict['is_adaptive'] = False
        flags_with_questions.append(flag_dict)
    
    # Adaptive question flags
    adaptive_flags = AdaptiveQuestionFlag.query.filter_by(status='pending').order_by(AdaptiveQuestionFlag.created_at.desc()).all()
    
    for flag in adaptive_flags:
        flag_dict = flag.to_dict()
        flag_dict['is_adaptive'] = True
        flags_with_questions.append(flag_dict)
    
    # Sort combined list by created_at
    flags_with_questions.sort(key=lambda x: x['created_at'], reverse=True)

    return jsonify(flags_with_questions)

@admin_bp.route('/api/admin/flags/all')
@login_required
@role_required('admin')
def get_all_flags():
    """Get all question flags (both standard and adaptive) with mode info for SEC questions"""
    from sqlalchemy import text
    
    status_filter = request.args.get('status')

    # Standard question flags
    query = QuestionFlag.query
    if status_filter:
        query = query.filter_by(status=status_filter)

    flags = query.order_by(QuestionFlag.created_at.desc()).all()

    flags_with_questions = []
    for flag in flags:
        flag_dict = flag.to_dict()
        question_data = flag.question.to_dict()
        question_data['mode'] = None  # Legacy questions don't have mode
        question_data['is_adaptive'] = False
        flag_dict['question'] = question_data
        flag_dict['is_adaptive'] = False
        flags_with_questions.append(flag_dict)
    
    # Adaptive question flags - fetch full question details including mode
    adaptive_query = AdaptiveQuestionFlag.query
    if status_filter:
        adaptive_query = adaptive_query.filter_by(status=status_filter)
    
    adaptive_flags = adaptive_query.order_by(AdaptiveQuestionFlag.created_at.desc()).all()
    
    for flag in adaptive_flags:
        flag_dict = flag.to_dict()
        
        # Fetch full question details from questions_adaptive including mode
        try:
            result = db.session.execute(text("""
                SELECT question_text, option_a, option_b, option_c, option_d, 
                       correct_answer, topic, COALESCE(mode, 'practice') as mode,
                       difficulty_level, difficulty_band
                FROM questions_adaptive WHERE id = :qid
            """), {'qid': flag.question_id}).fetchone()
            
            if result:
                # Handle correct answer format
                correct_raw = result[5]
                if isinstance(correct_raw, int) and 0 <= correct_raw <= 3:
                    correct_index = correct_raw
                elif str(correct_raw).upper() in ['A', 'B', 'C', 'D']:
                    correct_index = ['A', 'B', 'C', 'D'].index(str(correct_raw).upper())
                else:
                    correct_index = 0
                
                flag_dict['question'] = {
                    'id': flag.question_id,
                    'question': result[0] or 'Adaptive Question',
                    'topic': result[6],
                    'options': [result[1] or '', result[2] or '', result[3] or '', result[4] or ''],
                    'correct': correct_index,
                    'mode': result[7],  # 'practice' or 'jc_exam'
                    'difficulty_level': result[8],
                    'difficulty_band': result[9],
                    'is_adaptive': True
                }
            else:
                flag_dict['question'] = {
                    'id': flag.question_id,
                    'question': flag.question_text or '[Question deleted]',
                    'topic': flag.topic,
                    'options': [],
                    'correct': None,
                    'mode': 'practice',
                    'is_adaptive': True
                }
        except Exception as e:
            print(f"Error fetching adaptive question {flag.question_id}: {e}")
            flag_dict['question'] = {
                'id': flag.question_id,
                'question': flag.question_text or 'Adaptive Question',
                'topic': flag.topic,
                'options': [],
                'correct': None,
                'mode': 'practice',
                'is_adaptive': True
            }
        
        flag_dict['is_adaptive'] = True
        flags_with_questions.append(flag_dict)
    
    # Sort combined list by created_at
    flags_with_questions.sort(key=lambda x: x['created_at'], reverse=True)

    return jsonify(flags_with_questions)

@admin_bp.route('/api/admin/flag/<int:flag_id>/dismiss', methods=['POST'])
@login_required
@role_required('admin')
def dismiss_flag(flag_id):
    """Dismiss a flag without making changes"""
    data = request.json
    is_adaptive = data.get('is_adaptive', False)
    
    if is_adaptive:
        flag = AdaptiveQuestionFlag.query.get_or_404(flag_id)
    else:
        flag = QuestionFlag.query.get_or_404(flag_id)

    flag.status = 'dismissed'
    flag.admin_notes = data.get('notes', '')
    flag.resolved_at = datetime.utcnow()
    flag.resolved_by = session['user_id']

    db.session.commit()

    return jsonify({
        'message': 'Flag dismissed',
        'flag': flag.to_dict()
    })

@admin_bp.route('/api/admin/question/<int:question_id>')
@login_required
@role_required('admin')
def get_question_for_edit(question_id):
    """Get question details for editing"""
    question = Question.query.get_or_404(question_id)
    flags = QuestionFlag.query.filter_by(question_id=question_id).order_by(QuestionFlag.created_at.desc()).all()
    edits = QuestionEdit.query.filter_by(question_id=question_id).order_by(QuestionEdit.edited_at.desc()).all()

    return jsonify({
        'question': question.to_dict(),
        'flags': [f.to_dict() for f in flags],
        'edit_history': [e.to_dict() for e in edits]
    })

@admin_bp.route('/api/admin/all-questions')
@login_required
@role_required('admin')
def get_all_questions():
    """Get all questions with optional filters for management"""
    topic = request.args.get('topic', '')
    difficulty = request.args.get('difficulty', '')

    query = Question.query

    if topic:
        query = query.filter_by(topic=topic)
    if difficulty:
        query = query.filter_by(difficulty=difficulty)

    questions = query.order_by(Question.topic, Question.difficulty, Question.id).all()
    return jsonify([q.to_dict() for q in questions])


@admin_bp.route('/api/admin/adaptive-questions')
@login_required
@role_required('admin')
def get_all_adaptive_questions():
    """Get all adaptive questions with optional filters for management including mode (practice/jc_exam)"""
    from sqlalchemy import text
    
    topic = request.args.get('topic', '')
    level_band = request.args.get('level_band', '')  # This maps to difficulty_band in DB
    difficulty_band = request.args.get('difficulty_band', '')  # For SEC: foundation, ordinary, higher
    mode = request.args.get('mode', '')  # 'practice' or 'jc_exam'
    count_only = request.args.get('count_only', '')  # If set, return topic counts only
    
    try:
        # If count_only, return topic counts for the specified mode
        if count_only:
            count_query = """
                SELECT topic, COUNT(*) as count 
                FROM questions_adaptive 
                WHERE is_active = 1
            """
            params = {}
            
            if mode:
                count_query += " AND COALESCE(mode, 'practice') = :mode"
                params['mode'] = mode
            
            count_query += " GROUP BY topic ORDER BY topic"
            
            result = db.session.execute(text(count_query), params).fetchall()
            topics = [{'topic': row[0], 'count': row[1]} for row in result]
            return jsonify({'topics': topics})
        
        # Build query using correct column names from schema
        query = """SELECT id, topic, difficulty_band, difficulty_level, question_text, question_type, 
                          option_a, option_b, option_c, option_d, correct_answer,
                          image_svg, explanation, COALESCE(mode, 'practice') as mode
                   FROM questions_adaptive WHERE is_active = 1"""
        params = {}
        
        # Filter by mode (practice or jc_exam)
        if mode:
            query += " AND COALESCE(mode, 'practice') = :mode"
            params['mode'] = mode
        
        if topic:
            query += " AND topic = :topic"
            params['topic'] = topic
        
        # Filter by level_band (for adaptive practice questions)
        if level_band:
            query += " AND difficulty_band = :difficulty_band"
            params['difficulty_band'] = level_band
        
        # Filter by difficulty_band (for SEC questions - foundation, ordinary, higher)
        if difficulty_band:
            query += " AND difficulty_band = :difficulty_band"
            params['difficulty_band'] = difficulty_band
        
        query += " ORDER BY topic, difficulty_level, id LIMIT 500"
        
        result = db.session.execute(text(query), params).fetchall()
        
        questions = []
        for row in result:
            try:
                # Handle correct answer - stored as 0/1/2/3 in DB
                correct_answer_raw = row[10]
                if correct_answer_raw is not None:
                    if isinstance(correct_answer_raw, int):
                        correct_index = correct_answer_raw
                        correct_letter = ['A', 'B', 'C', 'D'][correct_index] if 0 <= correct_index <= 3 else 'A'
                    else:
                        correct_str = str(correct_answer_raw).upper().strip()
                        if correct_str in ['A', 'B', 'C', 'D']:
                            correct_index = ['A', 'B', 'C', 'D'].index(correct_str)
                            correct_letter = correct_str
                        elif correct_str in ['0', '1', '2', '3']:
                            correct_index = int(correct_str)
                            correct_letter = ['A', 'B', 'C', 'D'][correct_index]
                        else:
                            correct_index = 0
                            correct_letter = 'A'
                else:
                    correct_index = 0
                    correct_letter = 'A'
                
                questions.append({
                    'id': row[0],
                    'topic': str(row[1]) if row[1] else 'unknown',
                    'level_band': str(row[2]) if row[2] else 'beginner',  # difficulty_band -> level_band for frontend
                    'difficulty_band': str(row[2]) if row[2] else 'beginner',  # Also include as difficulty_band
                    'level': int(row[3]) if row[3] else 1,  # difficulty_level -> level for frontend
                    'question': str(row[4]) if row[4] else '',
                    'question_text': str(row[4]) if row[4] else '',
                    'question_type': str(row[5]) if row[5] else 'multiple_choice',
                    'options': [
                        str(row[6]) if row[6] else '',
                        str(row[7]) if row[7] else '',
                        str(row[8]) if row[8] else '',
                        str(row[9]) if row[9] else ''
                    ],
                    'option_a': str(row[6]) if row[6] else '',
                    'option_b': str(row[7]) if row[7] else '',
                    'option_c': str(row[8]) if row[8] else '',
                    'option_d': str(row[9]) if row[9] else '',
                    'correct': correct_index,
                    'correct_answer': correct_letter,
                    'has_svg': bool(row[11]),
                    'image_svg': row[11] if row[11] else None,
                    'explanation': str(row[12]) if row[12] else '',
                    'mode': str(row[13]) if row[13] else 'practice',  # 'practice' or 'jc_exam'
                    'is_adaptive': True,
                    'difficulty': str(row[2]) if row[2] else 'beginner'
                })
            except Exception as row_error:
                print(f"Error processing row {row[0]}: {row_error}")
                continue
        
        return jsonify(questions)
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Error loading adaptive questions: {error_detail}")
        return jsonify({'error': str(e), 'detail': error_detail}), 500


@admin_bp.route('/api/admin/adaptive-topics-list')
@login_required
@role_required('admin')
def get_adaptive_topics_list():
    """Get list of adaptive quiz topics with question counts"""
    from sqlalchemy import text
    
    try:
        result = db.session.execute(text("""
            SELECT topic, COUNT(*) as count 
            FROM questions_adaptive 
            WHERE is_active = 1
            GROUP BY topic 
            ORDER BY topic
        """)).fetchall()
        
        topics = [{'topic': row[0], 'count': row[1]} for row in result]
        return jsonify(topics)
    except Exception as e:
        print(f"Error loading adaptive topics: {e}")
        return jsonify({'error': str(e)}), 500

@admin_bp.route('/api/admin/question/<int:question_id>/edit', methods=['PUT'])
@login_required
@role_required('admin')
def edit_question(question_id):
    """Edit a question and track the changes"""
    question = Question.query.get_or_404(question_id)
    data = request.json

    edit_record = QuestionEdit(
        question_id=question_id,
        edited_by=session['user_id'],
        edit_type=data.get('edit_type', 'correction'),
        old_question_text=question.question_text,
        old_option_a=question.option_a,
        old_option_b=question.option_b,
        old_option_c=question.option_c,
        old_option_d=question.option_d,
        old_correct_answer=question.correct_answer,
        old_explanation=question.explanation,
        edit_notes=data.get('notes', '')
    )

    # Update topic if provided
    if 'topic' in data:
        question.topic = data['topic']

    # Update difficulty if provided
    if 'difficulty' in data:
        question.difficulty = data['difficulty']

    if 'question_text' in data:
        question.question_text = data['question_text']
        edit_record.new_question_text = data['question_text']
    else:
        edit_record.new_question_text = question.question_text

    if 'option_a' in data:
        question.option_a = data['option_a']
        edit_record.new_option_a = data['option_a']
    else:
        edit_record.new_option_a = question.option_a

    if 'option_b' in data:
        question.option_b = data['option_b']
        edit_record.new_option_b = data['option_b']
    else:
        edit_record.new_option_b = question.option_b

    if 'option_c' in data:
        question.option_c = data['option_c']
        edit_record.new_option_c = data['option_c']
    else:
        edit_record.new_option_c = question.option_c

    if 'option_d' in data:
        question.option_d = data['option_d']
        edit_record.new_option_d = data['option_d']
    else:
        edit_record.new_option_d = question.option_d

    if 'correct_answer' in data:
        question.correct_answer = data['correct_answer']
        edit_record.new_correct_answer = data['correct_answer']
    else:
        edit_record.new_correct_answer = question.correct_answer

    if 'explanation' in data:
        question.explanation = data['explanation']
        edit_record.new_explanation = data['explanation']
    else:
        edit_record.new_explanation = question.explanation

    # Phase 1: Image and hint support
    if 'image_url' in data:
        question.image_url = data['image_url'] if data['image_url'] else None
    if 'image_caption' in data:
        question.image_caption = data['image_caption'] if data['image_caption'] else None
    if 'hint_text' in data:
        question.hint_text = data['hint_text'] if data['hint_text'] else None
    if 'hint_penalty' in data:
        question.hint_penalty = int(data['hint_penalty']) if data['hint_penalty'] else 50

    db.session.add(edit_record)
    db.session.commit()

    if 'resolve_flag_ids' in data:
        for flag_id in data['resolve_flag_ids']:
            flag = QuestionFlag.query.get(flag_id)
            if flag and flag.question_id == question_id:
                flag.status = 'resolved'
                flag.resolved_at = datetime.utcnow()
                flag.resolved_by = session['user_id']
                flag.admin_notes = f"Question edited: {edit_record.edit_notes}"
        db.session.commit()

    return jsonify({
        'message': 'Question updated successfully',
        'question': question.to_dict(),
        'edit': edit_record.to_dict()
    })

@admin_bp.route('/api/admin/question/<int:question_id>/history')
@login_required
@role_required('admin')
def get_question_history(question_id):
    """Get complete edit history for a question"""
    question = Question.query.get_or_404(question_id)
    edits = QuestionEdit.query.filter_by(question_id=question_id).order_by(QuestionEdit.edited_at.desc()).all()

    return jsonify({
        'question': question.to_dict(),
        'edit_history': [e.to_dict() for e in edits]
    })


@admin_bp.route('/api/admin/adaptive-flag/<int:flag_id>/resolve', methods=['POST'])
@login_required
@role_required('admin')
def resolve_adaptive_flag(flag_id):
    """Resolve an adaptive question flag"""
    flag = AdaptiveQuestionFlag.query.get_or_404(flag_id)
    
    data = request.json or {}
    admin_notes = data.get('admin_notes', 'Resolved by admin')
    
    flag.status = 'resolved'
    flag.resolved_at = datetime.utcnow()
    flag.resolved_by = session['user_id']
    flag.admin_notes = admin_notes
    
    db.session.commit()
    
    return jsonify({
        'message': 'Flag resolved successfully',
        'flag': flag.to_dict()
    })


@admin_bp.route('/api/admin/adaptive-question/<int:question_id>', methods=['GET'])
@login_required
@role_required('admin')
def get_adaptive_question_admin(question_id):
    """Get adaptive question details for admin"""
    from sqlalchemy import text
    
    try:
        result = db.session.execute(text("""
            SELECT id, topic, difficulty_band, difficulty_level, question_text, question_type,
                   option_a, option_b, option_c, option_d, correct_answer
            FROM questions_adaptive WHERE id = :qid
        """), {'qid': question_id}).fetchone()
        
        if not result:
            return jsonify({'error': 'Question not found'}), 404
        
        # Get flags for this question
        flags = AdaptiveQuestionFlag.query.filter_by(question_id=question_id).order_by(AdaptiveQuestionFlag.created_at.desc()).all()
        
        # Handle correct answer conversion
        correct_raw = result[10]
        if isinstance(correct_raw, int) and 0 <= correct_raw <= 3:
            correct_letter = ['A', 'B', 'C', 'D'][correct_raw]
        else:
            correct_letter = str(correct_raw).upper() if correct_raw else 'A'
        
        return jsonify({
            'question': {
                'id': result[0],
                'topic': result[1],
                'level_band': result[2],  # difficulty_band -> level_band for frontend
                'level': result[3],  # difficulty_level -> level for frontend
                'question_text': result[4],
                'question_type': result[5],
                'option_a': result[6],
                'option_b': result[7],
                'option_c': result[8],
                'option_d': result[9],
                'correct_answer': correct_letter,
                'image_svg': None  # Not fetching SVG for now
            },
            'flags': [f.to_dict() for f in flags]
        })
    except Exception as e:
        print(f"Error fetching adaptive question {question_id}: {e}")
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/admin/adaptive-question/<int:question_id>', methods=['PUT'])
@login_required
@role_required('admin')
def update_adaptive_question_admin(question_id):
    """Update an adaptive question and optionally resolve flags"""
    from sqlalchemy import text
    
    data = request.json
    
    try:
        # Build update query
        updates = ["updated_at = CURRENT_TIMESTAMP"]
        params = {'qid': question_id}
        
        if 'question_text' in data:
            updates.append("question_text = :question_text")
            params['question_text'] = data['question_text']
        if 'option_a' in data:
            updates.append("option_a = :option_a")
            params['option_a'] = data['option_a']
        if 'option_b' in data:
            updates.append("option_b = :option_b")
            params['option_b'] = data['option_b']
        if 'option_c' in data:
            updates.append("option_c = :option_c")
            params['option_c'] = data['option_c']
        if 'option_d' in data:
            updates.append("option_d = :option_d")
            params['option_d'] = data['option_d']
        if 'correct_answer' in data:
            # Convert A/B/C/D to 0/1/2/3 for DB storage
            correct_letter = data['correct_answer'].upper()
            if correct_letter in ['A', 'B', 'C', 'D']:
                correct_index = ['A', 'B', 'C', 'D'].index(correct_letter)
            else:
                correct_index = 0
            updates.append("correct_answer = :correct_answer")
            params['correct_answer'] = correct_index
        
        query = f"UPDATE questions_adaptive SET {', '.join(updates)} WHERE id = :qid"
        db.session.execute(text(query), params)
        
        # Resolve specified flags
        if 'resolve_flag_ids' in data:
            for flag_id in data['resolve_flag_ids']:
                flag = AdaptiveQuestionFlag.query.get(flag_id)
                if flag and flag.question_id == question_id:
                    flag.status = 'resolved'
                    flag.resolved_at = datetime.utcnow()
                    flag.resolved_by = session['user_id']
                    flag.admin_notes = data.get('admin_notes', 'Question edited')
        
        db.session.commit()
        
        return jsonify({'message': 'Adaptive question updated successfully'})
    except Exception as e:
        db.session.rollback()
        print(f"Error updating adaptive question {question_id}: {e}")
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/admin/question/<int:question_id>/delete', methods=['DELETE'])
@login_required
@role_required('admin')
def delete_question(question_id):
    """Permanently delete a question"""
    from sqlalchemy import text
    
    question = Question.query.get_or_404(question_id)
    
    # Store question info for logging
    question_text = question.question_text[:100]
    topic = question.topic
    difficulty = question.difficulty
    
    try:
        # Delete related records first (flags, edits, responses)
        db.session.execute(text("DELETE FROM question_flags WHERE question_id = :qid"), {'qid': question_id})
        db.session.execute(text("DELETE FROM question_edits WHERE question_id = :qid"), {'qid': question_id})
        
        # Try to delete responses if table exists
        try:
            db.session.execute(text("DELETE FROM quiz_responses WHERE question_id = :qid"), {'qid': question_id})
        except:
            pass  # Table may not exist
        
        # Delete the question itself
        db.session.delete(question)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': f'Question deleted successfully',
            'deleted': {
                'id': question_id,
                'topic': topic,
                'difficulty': difficulty,
                'question_preview': question_text
            }
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@admin_bp.route('/api/admin/questions/bulk-delete', methods=['POST'])
@login_required
@role_required('admin')
def bulk_delete_questions():
    """Bulk delete multiple questions"""
    from sqlalchemy import text
    
    data = request.json
    question_ids = data.get('question_ids', [])
    
    if not question_ids:
        return jsonify({'success': False, 'error': 'No question IDs provided'}), 400
    
    if len(question_ids) > 100:
        return jsonify({'success': False, 'error': 'Maximum 100 questions can be deleted at once'}), 400
    
    deleted_count = 0
    failed_count = 0
    deleted_info = []
    
    for question_id in question_ids:
        try:
            question = Question.query.get(question_id)
            if not question:
                failed_count += 1
                continue
            
            # Store info before deletion
            question_text = question.question_text[:50]
            topic = question.topic
            
            # Delete related records
            db.session.execute(text("DELETE FROM question_flags WHERE question_id = :qid"), {'qid': question_id})
            db.session.execute(text("DELETE FROM question_edits WHERE question_id = :qid"), {'qid': question_id})
            
            try:
                db.session.execute(text("DELETE FROM quiz_responses WHERE question_id = :qid"), {'qid': question_id})
            except:
                pass
            
            # Delete the question
            db.session.delete(question)
            deleted_count += 1
            deleted_info.append({'id': question_id, 'topic': topic, 'preview': question_text})
            
        except Exception as e:
            failed_count += 1
            continue
    
    # Commit all deletions
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'error': f'Database error: {str(e)}'
        }), 500
    
    return jsonify({
        'success': True,
        'message': f'Deleted {deleted_count} question(s)',
        'deleted': deleted_count,
        'failed': failed_count,
        'deleted_questions': deleted_info
    })

@admin_bp.route('/api/admin/questions/find-duplicates')
@login_required
@role_required('admin')
def find_duplicate_questions():
    """Find duplicate questions based on question text"""
    topic_filter = request.args.get('topic', '')
    
    # Build query
    query = Question.query
    if topic_filter:
        query = query.filter_by(topic=topic_filter)
    
    # Get all questions
    questions = query.order_by(Question.id.asc()).all()
    total_scanned = len(questions)
    
    # Group by normalized question text (lowercase, stripped whitespace)
    text_groups = {}
    for q in questions:
        # Normalize the question text for comparison
        normalized = q.question_text.lower().strip()
        # Remove extra whitespace
        normalized = ' '.join(normalized.split())
        
        key = (q.topic, normalized)
        if key not in text_groups:
            text_groups[key] = []
        text_groups[key].append(q)
    
    # Find groups with more than one question (duplicates)
    duplicate_groups = []
    for (topic, text), questions_list in text_groups.items():
        if len(questions_list) > 1:
            # Sort by ID to show oldest first
            questions_list.sort(key=lambda x: x.id)
            
            duplicate_groups.append({
                'topic': topic,
                'question_text': questions_list[0].question_text,
                'count': len(questions_list),
                'questions': [{
                    'id': q.id,
                    'difficulty': q.difficulty,
                    'image_url': q.image_url,
                    'created_at': q.id  # Using ID as proxy for creation order
                } for q in questions_list]
            })
    
    # Sort by number of duplicates (most first)
    duplicate_groups.sort(key=lambda x: x['count'], reverse=True)
    
    return jsonify({
        'success': True,
        'total_scanned': total_scanned,
        'duplicate_groups': duplicate_groups,
        'total_duplicate_groups': len(duplicate_groups),
        'total_duplicate_questions': sum(g['count'] for g in duplicate_groups)
    })

@admin_bp.route('/api/admin/questions/flagged')
@login_required
@role_required('admin')
def get_flagged_questions():
    """Get all questions that have pending flags"""
    flagged_question_ids = db.session.query(QuestionFlag.question_id).filter_by(status='pending').distinct().all()
    question_ids = [q[0] for q in flagged_question_ids]

    questions_with_flags = []
    for qid in question_ids:
        question = Question.query.get(qid)
        flags = QuestionFlag.query.filter_by(question_id=qid, status='pending').all()

        questions_with_flags.append({
            'question': question.to_dict(),
            'flag_count': len(flags),
            'flags': [f.to_dict() for f in flags]
        })

    return jsonify(questions_with_flags)

@admin_bp.route('/api/admin/flags/statistics')
@login_required
@role_required('admin')
def flag_statistics():
    """Get statistics about question flags (both standard and adaptive)"""
    # Standard flags
    standard_total = QuestionFlag.query.count()
    standard_pending = QuestionFlag.query.filter_by(status='pending').count()
    standard_resolved = QuestionFlag.query.filter_by(status='resolved').count()
    standard_dismissed = QuestionFlag.query.filter_by(status='dismissed').count()
    
    # Adaptive flags
    adaptive_total = AdaptiveQuestionFlag.query.count()
    adaptive_pending = AdaptiveQuestionFlag.query.filter_by(status='pending').count()
    adaptive_resolved = AdaptiveQuestionFlag.query.filter_by(status='resolved').count()
    adaptive_dismissed = AdaptiveQuestionFlag.query.filter_by(status='dismissed').count()
    
    stats = {
        'total_flags': standard_total + adaptive_total,
        'pending_flags': standard_pending + adaptive_pending,
        'resolved_flags': standard_resolved + adaptive_resolved,
        'dismissed_flags': standard_dismissed + adaptive_dismissed,
        'flagged_questions': db.session.query(QuestionFlag.question_id).filter_by(status='pending').distinct().count(),
        'flagged_adaptive_questions': db.session.query(AdaptiveQuestionFlag.question_id).filter_by(status='pending').distinct().count(),
        'total_edits': QuestionEdit.query.count(),
        'by_flag_type': {},
        # Breakdown for display
        'standard_pending': standard_pending,
        'adaptive_pending': adaptive_pending
    }

    for flag_type in ['incorrect', 'ambiguous', 'typo', 'other']:
        standard_count = QuestionFlag.query.filter_by(flag_type=flag_type, status='pending').count()
        adaptive_count = AdaptiveQuestionFlag.query.filter_by(flag_type=flag_type, status='pending').count()
        stats['by_flag_type'][flag_type] = standard_count + adaptive_count

    return jsonify(stats)



# GET all users endpoint (frontend expects /api/admin/users plural)
@admin_bp.route('/api/admin/users', methods=['GET'])
@login_required
@role_required('admin')
def admin_get_all_users():
    """Get all users for admin management"""
    users = User.query.order_by(User.created_at.desc()).all()

    users_data = []
    for user in users:
        stats = UserStats.query.filter_by(user_id=user.id).first()
        quiz_count = QuizAttempt.query.filter_by(user_id=user.id).count()

        users_data.append({
            'id': user.id,
            'username': user.full_name,  # FIXED: Use full_name instead of username
            'email': user.email,
            'role': user.role,
            'is_approved': user.is_approved,
            'created_at': user.created_at.isoformat() if user.created_at else None,
            'total_quizzes': quiz_count,
            'total_points': stats.total_points if stats else 0,
            'level': stats.level if stats else 1
        })

    return jsonify(users_data), 200


# ==================== PRIZE SYSTEM ADMIN ROUTES ====================
# Admin interface for managing prizes, schools, and redemptions

@admin_bp.route('/admin/prizes')
@login_required
@role_required('admin')
def admin_prizes():
    """Prize system admin dashboard"""
    if not current_app.config.get('FEATURE_FLAGS', {}).get('PRIZE_SYSTEM_ENABLED', False):
        flash('Prize system is not enabled.', 'warning')
        return redirect(url_for('admin.admin_dashboard'))

    return render_template('admin_prizes.html')


@admin_bp.route('/api/admin/prizes/settings', methods=['GET'])
@login_required
@role_required('admin')
def get_prize_settings():
    """Get global prize system settings"""
    settings = {
        'global_points_multiplier': float(SystemSetting.get('global_points_multiplier', 5.0)),
        'prize_expiry_days': int(SystemSetting.get('prize_expiry_days', 30)),
        'raffle_enabled': SystemSetting.get('raffle_enabled', 'true') == 'true',
        'level_lock_enabled': SystemSetting.get('prize_level_lock_enabled', 'false') == 'true'
    }
    return jsonify(settings)


@admin_bp.route('/api/admin/prizes/settings', methods=['POST'])
@login_required
@role_required('admin')
def update_prize_settings():
    """Update global prize system settings"""
    data = request.get_json()
    user_id = session.get('user_id')

    if 'global_points_multiplier' in data:
        SystemSetting.set('global_points_multiplier', float(data['global_points_multiplier']),
                          'Global multiplier for prize point costs', user_id)

    if 'prize_expiry_days' in data:
        SystemSetting.set('prize_expiry_days', int(data['prize_expiry_days']),
                          'Days before unclaimed prizes expire', user_id)

    if 'raffle_enabled' in data:
        SystemSetting.set('raffle_enabled', 'true' if data['raffle_enabled'] else 'false',
                          'Whether raffle system is enabled', user_id)

    if 'level_lock_enabled' in data:
        SystemSetting.set('prize_level_lock_enabled', 'true' if data['level_lock_enabled'] else 'false',
                          'Whether prizes require minimum level to redeem', user_id)

    return jsonify({'success': True, 'message': 'Settings updated'})


# ----- Global Prize Catalogue -----

@admin_bp.route('/api/admin/prizes/catalogue', methods=['GET'])
@login_required
@role_required('admin')
def get_prize_catalogue():
    """Get all prizes in the global catalogue"""
    prizes = Prize.query.order_by(Prize.tier, Prize.sort_order, Prize.name).all()
    global_multiplier = float(SystemSetting.get('global_points_multiplier', 5.0))

    result = []
    for prize in prizes:
        p = prize.to_dict()
        p['effective_cost'] = int(prize.base_point_cost * global_multiplier)
        result.append(p)

    return jsonify({
        'prizes': result,
        'global_multiplier': global_multiplier
    })


@admin_bp.route('/api/admin/prizes/catalogue', methods=['POST'])
@login_required
@role_required('admin')
def create_prize():
    """Create a new prize in the global catalogue"""
    data = request.get_json()

    prize = Prize(
        name=data['name'],
        description=data.get('description', ''),
        base_point_cost=int(data['base_point_cost']),
        tier=data.get('tier', 'bronze'),
        prize_type=data.get('prize_type', 'physical'),
        minimum_level=int(data.get('minimum_level', 0)),
        emoji=data.get('emoji', '🎁'),
        sort_order=data.get('sort_order', 0),
        is_active=data.get('is_active', True)
    )

    db.session.add(prize)
    db.session.commit()

    return jsonify({'success': True, 'prize': prize.to_dict()})


@admin_bp.route('/api/admin/prizes/catalogue/<int:prize_id>', methods=['PUT'])
@login_required
@role_required('admin')
def update_prize(prize_id):
    """Update a prize in the global catalogue"""
    prize = Prize.query.get_or_404(prize_id)
    data = request.get_json()

    if 'name' in data:
        prize.name = data['name']
    if 'description' in data:
        prize.description = data['description']
    if 'base_point_cost' in data:
        prize.base_point_cost = int(data['base_point_cost'])
    if 'tier' in data:
        prize.tier = data['tier']
    if 'prize_type' in data:
        prize.prize_type = data['prize_type']
    if 'minimum_level' in data:
        prize.minimum_level = int(data['minimum_level'])
    if 'emoji' in data:
        prize.emoji = data['emoji']
    if 'sort_order' in data:
        prize.sort_order = int(data['sort_order'])
    if 'is_active' in data:
        prize.is_active = data['is_active']

    db.session.commit()

    return jsonify({'success': True, 'prize': prize.to_dict()})


@admin_bp.route('/api/admin/prizes/catalogue/<int:prize_id>', methods=['DELETE'])
@login_required
@role_required('admin')
def delete_prize(prize_id):
    """Delete a prize from the global catalogue (if no redemptions)"""
    prize = Prize.query.get_or_404(prize_id)

    # Check for redemptions
    redemption_count = PrizeRedemption.query.filter_by(prize_id=prize_id).count()
    if redemption_count > 0:
        return jsonify({
            'success': False,
            'error': f'Cannot delete: {redemption_count} redemptions exist for this prize. Deactivate instead.'
        }), 400

    # Delete school overrides first
    SchoolPrize.query.filter_by(prize_id=prize_id).delete()

    db.session.delete(prize)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Prize deleted'})


# ----- Schools Management -----

@admin_bp.route('/api/admin/prizes/schools', methods=['GET'])
@login_required
@role_required('admin')
def get_prize_schools():
    """Get all schools in the prize programme"""
    schools = PrizeSchool.query.order_by(PrizeSchool.name).all()
    return jsonify({'schools': [s.to_dict() for s in schools]})


@admin_bp.route('/api/admin/prizes/schools', methods=['POST'])
@login_required
@role_required('admin')
def create_prize_school():
    """Add a new school to the prize programme"""
    data = request.get_json()

    school = PrizeSchool(
        name=data['name'],
        roll_number=data.get('roll_number'),
        county=data.get('county'),
        address=data.get('address'),
        status='approved',  # Admin-created schools are auto-approved
        points_multiplier=float(data.get('points_multiplier', 1.0)),
        rep_name=data.get('rep_name'),
        rep_email=data.get('rep_email'),
        approved_at=datetime.utcnow(),
        approved_by=session.get('user_id')
    )

    db.session.add(school)
    db.session.commit()

    return jsonify({'success': True, 'school': school.to_dict()})


@admin_bp.route('/api/admin/prizes/schools/<int:school_id>', methods=['PUT'])
@login_required
@role_required('admin')
def update_prize_school(school_id):
    """Update a school in the prize programme"""
    school = PrizeSchool.query.get_or_404(school_id)
    data = request.get_json()

    if 'name' in data:
        school.name = data['name']
    if 'roll_number' in data:
        school.roll_number = data['roll_number']
    if 'county' in data:
        school.county = data['county']
    if 'address' in data:
        school.address = data['address']
    if 'status' in data:
        old_status = school.status
        school.status = data['status']
        if old_status != 'approved' and data['status'] == 'approved':
            school.approved_at = datetime.utcnow()
            school.approved_by = session.get('user_id')
    if 'points_multiplier' in data:
        school.points_multiplier = float(data['points_multiplier'])
    if 'rep_name' in data:
        school.rep_name = data['rep_name']
    if 'rep_email' in data:
        school.rep_email = data['rep_email']
    if 'notes' in data:
        school.notes = data['notes']

    db.session.commit()

    return jsonify({'success': True, 'school': school.to_dict()})


@admin_bp.route('/api/admin/prizes/schools/<int:school_id>', methods=['DELETE'])
@login_required
@role_required('admin')
def delete_prize_school(school_id):
    """Delete a school from the prize programme"""
    school = PrizeSchool.query.get_or_404(school_id)

    # Check for redemptions
    redemption_count = PrizeRedemption.query.filter_by(school_id=school_id).count()
    if redemption_count > 0:
        return jsonify({
            'success': False,
            'error': f'Cannot delete: {redemption_count} redemptions exist for this school. Suspend instead.'
        }), 400

    # Delete school prizes
    SchoolPrize.query.filter_by(school_id=school_id).delete()

    db.session.delete(school)
    db.session.commit()

    return jsonify({'success': True, 'message': 'School deleted'})


@admin_bp.route('/api/admin/prizes/schools/<int:school_id>/prizes', methods=['GET'])
@login_required
@role_required('admin')
def get_school_prizes(school_id):
    """Get all prizes available at a specific school (with overrides)"""
    school = PrizeSchool.query.get_or_404(school_id)

    # Get all global prizes
    global_prizes = Prize.query.filter_by(is_active=True).order_by(Prize.tier, Prize.sort_order).all()

    # Get school overrides
    overrides = {sp.prize_id: sp for sp in SchoolPrize.query.filter_by(school_id=school_id).all()}

    # Get school-specific prizes (where prize_id is NULL)
    school_specific = SchoolPrize.query.filter_by(school_id=school_id, prize_id=None).all()

    result = []

    # Add global prizes with override info
    for prize in global_prizes:
        override = overrides.get(prize.id)
        item = prize.to_dict(school=school)
        item['override'] = override.to_dict() if override else None
        item['is_enabled'] = override.is_enabled if override else True
        item['stock_available'] = override.stock_available if override else None
        result.append(item)

    # Add school-specific prizes
    for sp in school_specific:
        result.append({
            'id': None,
            'school_prize_id': sp.id,
            'name': sp.custom_name,
            'description': sp.custom_description,
            'emoji': sp.custom_emoji,
            'point_cost': sp.point_cost_override,
            'is_school_specific': True,
            'is_enabled': sp.is_enabled,
            'stock_available': sp.stock_available
        })

    return jsonify({
        'school': school.to_dict(),
        'prizes': result
    })


@admin_bp.route('/api/admin/prizes/schools/<int:school_id>/prizes', methods=['POST'])
@login_required
@role_required('admin')
def create_school_prize(school_id):
    """Create a school-specific prize or override"""
    school = PrizeSchool.query.get_or_404(school_id)
    data = request.get_json()

    school_prize = SchoolPrize(
        school_id=school_id,
        prize_id=data.get('prize_id'),  # NULL for school-specific
        custom_name=data.get('custom_name'),
        custom_description=data.get('custom_description'),
        custom_emoji=data.get('custom_emoji', '🎁'),
        point_cost_override=data.get('point_cost_override'),
        stock_available=data.get('stock_available'),
        is_enabled=data.get('is_enabled', True)
    )

    db.session.add(school_prize)
    db.session.commit()

    return jsonify({'success': True, 'school_prize': school_prize.to_dict()})


@admin_bp.route('/api/admin/prizes/schools/<int:school_id>/prizes/<int:school_prize_id>', methods=['PUT'])
@login_required
@role_required('admin')
def update_school_prize(school_id, school_prize_id):
    """Update a school-specific prize or override"""
    school_prize = SchoolPrize.query.get_or_404(school_prize_id)

    if school_prize.school_id != school_id:
        return jsonify({'error': 'Prize does not belong to this school'}), 400

    data = request.get_json()

    if 'custom_name' in data:
        school_prize.custom_name = data['custom_name']
    if 'custom_description' in data:
        school_prize.custom_description = data['custom_description']
    if 'custom_emoji' in data:
        school_prize.custom_emoji = data['custom_emoji']
    if 'point_cost_override' in data:
        school_prize.point_cost_override = data['point_cost_override']
    if 'stock_available' in data:
        school_prize.stock_available = data['stock_available']
    if 'is_enabled' in data:
        school_prize.is_enabled = data['is_enabled']

    db.session.commit()

    return jsonify({'success': True, 'school_prize': school_prize.to_dict()})


# ----- School Requests -----

@admin_bp.route('/api/admin/prizes/school-requests', methods=['GET'])
@login_required
@role_required('admin')
def get_school_requests():
    """Get all pending school requests"""
    requests = SchoolRequest.query.order_by(SchoolRequest.created_at.desc()).all()
    return jsonify({'requests': [r.to_dict() for r in requests]})


@admin_bp.route('/api/admin/prizes/school-requests/<int:request_id>/approve', methods=['POST'])
@login_required
@role_required('admin')
def approve_school_request(request_id):
    """Approve a school request and create the school"""
    school_request = SchoolRequest.query.get_or_404(request_id)
    data = request.get_json() or {}

    # Create the school
    school = PrizeSchool(
        name=data.get('name', school_request.school_name),
        county=data.get('county', school_request.county),
        status='approved',
        rep_email=data.get('rep_email', school_request.suggested_rep_email),
        rep_name=data.get('rep_name'),
        approved_at=datetime.utcnow(),
        approved_by=session.get('user_id')
    )

    db.session.add(school)
    db.session.flush()  # Get the school ID

    # Update the request
    school_request.status = 'approved'
    school_request.processed_at = datetime.utcnow()
    school_request.processed_by = session.get('user_id')
    school_request.created_school_id = school.id
    school_request.admin_notes = data.get('admin_notes')

    db.session.commit()

    return jsonify({'success': True, 'school': school.to_dict()})


@admin_bp.route('/api/admin/prizes/school-requests/<int:request_id>/reject', methods=['POST'])
@login_required
@role_required('admin')
def reject_school_request(request_id):
    """Reject a school request"""
    school_request = SchoolRequest.query.get_or_404(request_id)
    data = request.get_json() or {}

    school_request.status = 'rejected'
    school_request.processed_at = datetime.utcnow()
    school_request.processed_by = session.get('user_id')
    school_request.admin_notes = data.get('admin_notes', 'Request rejected')

    db.session.commit()

    return jsonify({'success': True})


# ----- Redemption Analytics -----

@admin_bp.route('/api/admin/prizes/stats', methods=['GET'])
@login_required
@role_required('admin')
def get_prize_stats():
    """Get prize system statistics"""
    from sqlalchemy import func

    total_schools = PrizeSchool.query.filter_by(status='approved').count()
    pending_schools = PrizeSchool.query.filter_by(status='pending').count()
    total_prizes = Prize.query.filter_by(is_active=True).count()

    total_redemptions = PrizeRedemption.query.count()
    pending_redemptions = PrizeRedemption.query.filter_by(status='pending').count()
    fulfilled_redemptions = PrizeRedemption.query.filter_by(status='fulfilled').count()

    total_points_spent = db.session.query(func.sum(PrizeRedemption.points_spent)).scalar() or 0

    # Recent redemptions
    recent = PrizeRedemption.query.order_by(PrizeRedemption.redeemed_at.desc()).limit(10).all()

    return jsonify({
        'schools': {
            'approved': total_schools,
            'pending': pending_schools
        },
        'prizes': {
            'active': total_prizes
        },
        'redemptions': {
            'total': total_redemptions,
            'pending': pending_redemptions,
            'fulfilled': fulfilled_redemptions,
            'total_points_spent': total_points_spent
        },
        'recent_redemptions': [r.to_dict() for r in recent]
    })


# ==================== WHO AM I? FEATURE ====================
# Progressive image reveal gamification feature

def admin_required(f):
    """Decorator to ensure only admins can access these routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in first.', 'warning')
            return redirect(url_for('auth.login'))

        user = User.query.get(session['user_id'])
        if not user or user.role != 'admin':
            flash('Admin access required.', 'danger')
            return redirect(url_for('admin.admin_dashboard'))

        return f(*args, **kwargs)
    return decorated_function


# Helper function for Who Am I answer variants - MUST BE BEFORE ROUTES
def auto_generate_variants(answer):
    """
    Auto-generate acceptable answer variants
    Returns a list of lowercase variants
    """
    variants = set()
    answer_lower = answer.lower().strip()
    variants.add(answer_lower)

    # Remove common titles
    titles = ['dr.', 'dr', 'sir', 'professor', 'prof.', 'prof', 'dame', 'lord', 'lady']
    for title in titles:
        if answer_lower.startswith(title + ' '):
            without_title = answer_lower.replace(title + ' ', '', 1).strip()
            variants.add(without_title)

    # Split into name parts
    parts = answer_lower.split()

    if len(parts) >= 2:
        # First name only
        variants.add(parts[0])

        # Last name only
        variants.add(parts[-1])

        # First and last (skip middle)
        if len(parts) > 2:
            variants.add(f"{parts[0]} {parts[-1]}")

        # Remove middle initials
        filtered_parts = [p for p in parts if len(p) > 2 or not p.endswith('.')]
        if len(filtered_parts) != len(parts):
            variants.add(' '.join(filtered_parts))

    # Remove punctuation variants
    import string
    no_punct = answer_lower.translate(str.maketrans('', '', string.punctuation))
    if no_punct != answer_lower:
        variants.add(no_punct)

    return sorted(list(variants))


@admin_bp.route('/admin/who-am-i')
@admin_required
def admin_who_am_i():
    """Display all Who Am I images with multi-topic support"""
    from sqlalchemy import text

    # Get all images with their topics - INCLUDE accepted_answers
    query = text("""
        SELECT
            i.id,
            i.difficulty,
            i.image_filename,
            i.answer,
            i.hint,
            i.active,
            i.created_at,
            i.topic as primary_topic,
            i.accepted_answers,
            GROUP_CONCAT(t.topic) as all_topics
        FROM who_am_i_images i
        LEFT JOIN who_am_i_image_topics t ON i.id = t.image_id
        GROUP BY i.id
        ORDER BY i.created_at DESC
    """)

    results = db.session.execute(query).fetchall()

    images = []
    for row in results:
        # Parse comma-separated topics
        topics = row.all_topics.split(',') if row.all_topics else []
        
        # Parse accepted answers to get count
        accepted_answers_count = 0
        if row.accepted_answers:
            try:
                accepted_answers_count = len(json.loads(row.accepted_answers))
            except:
                pass
        
        images.append({
            'id': row.id,
            'primary_topic': row.primary_topic,
            'topics': topics,
            'difficulty': row.difficulty,
            'image_filename': row.image_filename,
            'answer': row.answer,
            'hint': row.hint,
            'active': row.active,
            'created_at': row.created_at,
            'accepted_answers_count': accepted_answers_count
        })

    # Get ALL topics from questions table
    topics = db.session.execute(text("SELECT DISTINCT topic FROM questions ORDER BY topic")).fetchall()
    all_topics = [row.topic for row in topics]

    # Get enabled topics (topics that have at least one image)
    enabled_query = text("""
        SELECT DISTINCT topic
        FROM who_am_i_image_topics
        ORDER BY topic
    """)
    enabled_results = db.session.execute(enabled_query).fetchall()
    enabled_topics = [row.topic for row in enabled_results]

    return render_template('admin_who_am_i.html',
                         images=images,
                         all_topics=all_topics,
                         enabled_topics=enabled_topics)


@admin_bp.route('/admin/who-am-i/upload', methods=['POST'])
@admin_required
def admin_who_am_i_upload():
    """Handle image upload with multi-topic support"""
    from sqlalchemy import text

    # Validate form data
    if 'image' not in request.files:
        flash('No image file provided', 'danger')
        return redirect(url_for('admin.admin_who_am_i'))

    file = request.files['image']
    primary_topic = request.form.get('topic')  # Primary topic for backward compatibility
    selected_topics = request.form.getlist('topics[]')  # Multiple topics
    difficulty = request.form.get('difficulty')
    answer = request.form.get('answer')
    hint = request.form.get('hint', '')

    # Handle accepted answers
    accepted_answers_text = request.form.get('accepted_answers', '').strip()
    if accepted_answers_text:
        # Parse from textarea (one per line)
        variants = [v.strip() for v in accepted_answers_text.split('\n') if v.strip()]
        accepted_answers_json = json.dumps(variants)
    else:
        # Auto-generate if not provided
        variants = auto_generate_variants(answer)
        accepted_answers_json = json.dumps(variants)

    if file.filename == '':
        flash('No file selected', 'danger')
        return redirect(url_for('admin.admin_who_am_i'))

    # Handle both single topic and multi-topic selection
    if not selected_topics and not primary_topic:
        flash('At least one topic is required', 'danger')
        return redirect(url_for('admin.admin_who_am_i'))

    if not difficulty or not answer:
        flash('Difficulty and answer are required', 'danger')
        return redirect(url_for('admin.admin_who_am_i'))

    # If only single topic selected (old form), use it
    if not selected_topics and primary_topic:
        selected_topics = [primary_topic]
    # If multi-topics selected but no primary, use first as primary
    elif selected_topics and not primary_topic:
        primary_topic = selected_topics[0]

    if file and allowed_file(file.filename):
        # Create upload directory if it doesn't exist
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        # Generate secure filename
        filename = secure_filename(file.filename)
        # Add timestamp to avoid conflicts
        import time
        timestamp = int(time.time())
        name, ext = os.path.splitext(filename)
        filename = f"{name}_{timestamp}{ext}"

        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        # Save to database
        query = text("""
            INSERT INTO who_am_i_images (topic, difficulty, image_filename, answer, hint)
            VALUES (:topic, :difficulty, :filename, :answer, :hint)
        """)
        result = db.session.execute(query, {
            'topic': primary_topic,
            'difficulty': difficulty,
            'filename': filename,
            'answer': answer,
            'hint': hint
        })
        db.session.commit()

        # Get the new image ID
        image_id = result.lastrowid

        # Add topic associations
        for topic in selected_topics:
            db.session.execute(text("""
                INSERT OR IGNORE INTO who_am_i_image_topics (image_id, topic)
                VALUES (:image_id, :topic)
            """), {'image_id': image_id, 'topic': topic})

        db.session.commit()

        flash(f'Image uploaded successfully! Answer: {answer} | Topics: {", ".join(selected_topics)}', 'success')
    else:
        flash('Invalid file type. Allowed types: png, jpg, jpeg, gif, webp', 'danger')

    return redirect(url_for('admin.admin_who_am_i'))


@admin_bp.route('/admin/who-am-i/toggle/<int:image_id>', methods=['POST'])
@admin_required
def admin_who_am_i_toggle(image_id):
    """Toggle active status of an image"""
    from sqlalchemy import text

    result = db.session.execute(
        text("SELECT active FROM who_am_i_images WHERE id = :id"),
        {'id': image_id}
    ).fetchone()

    if result:
        new_status = 0 if result.active == 1 else 1
        db.session.execute(
            text("UPDATE who_am_i_images SET active = :status WHERE id = :id"),
            {'status': new_status, 'id': image_id}
        )
        db.session.commit()
        flash('Image status updated', 'success')
    else:
        flash('Image not found', 'danger')

    return redirect(url_for('admin.admin_who_am_i'))


@admin_bp.route('/admin/who-am-i/delete/<int:image_id>', methods=['POST'])
@admin_required
def admin_who_am_i_delete(image_id):
    """Delete an image"""
    from sqlalchemy import text

    result = db.session.execute(
        text("SELECT image_filename FROM who_am_i_images WHERE id = :id"),
        {'id': image_id}
    ).fetchone()

    if result:
        # Delete file
        filepath = os.path.join(UPLOAD_FOLDER, result.image_filename)
        if os.path.exists(filepath):
            os.remove(filepath)

        # Delete from database
        db.session.execute(
            text("DELETE FROM who_am_i_images WHERE id = :id"),
            {'id': image_id}
        )
        db.session.commit()
        flash('Image deleted successfully', 'success')
    else:
        flash('Image not found', 'danger')

    return redirect(url_for('admin.admin_who_am_i'))



@admin_bp.route('/admin/who-am-i/get/<int:image_id>')
@admin_required
def admin_who_am_i_get(image_id):
    """Get image details for editing (including accepted_answers)"""
    from sqlalchemy import text

    query = text("""
        SELECT
            i.id,
            i.answer,
            i.hint,
            i.difficulty,
            i.accepted_answers,
            i.active,
            GROUP_CONCAT(t.topic) as topics
        FROM who_am_i_images i
        LEFT JOIN who_am_i_image_topics t ON i.id = t.image_id
        WHERE i.id = :image_id
        GROUP BY i.id
    """)

    result = db.session.execute(query, {'image_id': image_id}).fetchone()

    if not result:
        return jsonify({'error': 'Image not found'}), 404

    topics = result.topics.split(',') if result.topics else []

    return jsonify({
        'id': result.id,
        'answer': result.answer,
        'hint': result.hint,
        'difficulty': result.difficulty,
        'accepted_answers': result.accepted_answers,
        'active': result.active,
        'topics': topics
    })


@admin_bp.route('/admin/who-am-i/edit/<int:image_id>', methods=['GET', 'POST'])
@admin_required
def admin_who_am_i_edit(image_id):
    """Edit image details including accepted_answers"""
    from sqlalchemy import text

    if request.method == 'GET':
        # Redirect to main page (handled by GET endpoint now)
        return redirect(url_for('admin.admin_who_am_i'))

    # POST - handle edit
    answer = request.form.get('answer')
    hint = request.form.get('hint', '')
    difficulty = request.form.get('difficulty')
    selected_topics = request.form.getlist('topics[]')

    # Handle accepted answers from form
    accepted_answers_json = request.form.get('accepted_answers')

    # If not provided or empty, auto-generate
    if not accepted_answers_json:
        variants = auto_generate_variants(answer)
        accepted_answers_json = json.dumps(variants)

    # Update image
    db.session.execute(text("""
        UPDATE who_am_i_images
        SET answer = :answer,
            hint = :hint,
            difficulty = :difficulty,
            accepted_answers = :accepted_answers
        WHERE id = :image_id
    """), {
        'answer': answer,
        'hint': hint,
        'difficulty': difficulty,
        'accepted_answers': accepted_answers_json,
        'image_id': image_id
    })

    # Update topics - delete old associations
    db.session.execute(text("""
        DELETE FROM who_am_i_image_topics WHERE image_id = :image_id
    """), {'image_id': image_id})

    # Insert new topic associations
    if selected_topics:
        for topic in selected_topics:
            db.session.execute(text("""
                INSERT INTO who_am_i_image_topics (image_id, topic)
                VALUES (:image_id, :topic)
            """), {'image_id': image_id, 'topic': topic})

    db.session.commit()

    flash('Image updated successfully', 'success')
    return jsonify({'success': True})

@admin_bp.route('/admin/who-am-i/bulk-assign', methods=['POST'])
@admin_required
def admin_who_am_i_bulk_assign():
    """Bulk assign images to topics"""
    from sqlalchemy import text

    data = request.json
    image_ids = data.get('image_ids', [])
    topics = data.get('topics', [])
    action = data.get('action', 'add')  # 'add' or 'replace'

    if not image_ids or not topics:
        return jsonify({'success': False, 'error': 'Image IDs and topics required'}), 400

    if action == 'replace':
        # Remove existing topics for these images
        for image_id in image_ids:
            db.session.execute(text("""
                DELETE FROM who_am_i_image_topics WHERE image_id = :id
            """), {'id': image_id})

    # Add new topic associations
    for image_id in image_ids:
        for topic in topics:
            db.session.execute(text("""
                INSERT OR IGNORE INTO who_am_i_image_topics (image_id, topic)
                VALUES (:image_id, :topic)
            """), {'image_id': image_id, 'topic': topic})

        # Update primary topic if replacing
        if action == 'replace' and topics:
            db.session.execute(text("""
                UPDATE who_am_i_images SET topic = :topic WHERE id = :id
            """), {'topic': topics[0], 'id': image_id})

    db.session.commit()

    action_text = 'replaced with' if action == 'replace' else 'added to'
    return jsonify({
        'success': True,
        'message': f'{len(image_ids)} images {action_text} {len(topics)} topics'
    })


@admin_bp.route('/admin/who-am-i/bulk-delete', methods=['POST'])
@admin_required
def admin_who_am_i_bulk_delete():
    """Bulk delete images"""
    from sqlalchemy import text

    data = request.json
    image_ids = data.get('image_ids', [])

    if not image_ids:
        return jsonify({'success': False, 'error': 'No images selected'}), 400

    # Get filenames for deletion
    placeholders = ','.join([':id' + str(i) for i in range(len(image_ids))])
    params = {f'id{i}': image_id for i, image_id in enumerate(image_ids)}

    results = db.session.execute(text(f"""
        SELECT image_filename FROM who_am_i_images WHERE id IN ({placeholders})
    """), params).fetchall()

    # Delete files
    for row in results:
        filepath = os.path.join(UPLOAD_FOLDER, row.image_filename)
        if os.path.exists(filepath):
            os.remove(filepath)

    # Delete from database
    db.session.execute(text(f"""
        DELETE FROM who_am_i_images WHERE id IN ({placeholders})
    """), params)

    db.session.commit()

    return jsonify({'success': True, 'message': f'{len(image_ids)} images deleted'})


@admin_bp.route('/admin/who-am-i/copy-topic', methods=['POST'])
@admin_required
def admin_who_am_i_copy_topic():
    """Copy all Who Am I images from one topic to another"""
    from sqlalchemy import text

    data = request.json
    source_topic = data.get('source_topic')
    destination_topic = data.get('destination_topic')

    if not source_topic or not destination_topic:
        return jsonify({'success': False, 'error': 'Source and destination topics required'}), 400

    if source_topic == destination_topic:
        return jsonify({'success': False, 'error': 'Source and destination must be different'}), 400

    # Get all image IDs associated with the source topic
    source_images = db.session.execute(text("""
        SELECT image_id FROM who_am_i_image_topics WHERE topic = :topic
    """), {'topic': source_topic}).fetchall()

    if not source_images:
        return jsonify({'success': False, 'error': f'No images found in topic: {source_topic}'}), 404

    image_ids = [row.image_id for row in source_images]

    # Count how many are already in destination (to avoid duplicates)
    existing = db.session.execute(text("""
        SELECT COUNT(*) as cnt FROM who_am_i_image_topics 
        WHERE topic = :topic AND image_id IN ({})
    """.format(','.join(str(id) for id in image_ids))), {'topic': destination_topic}).fetchone()
    
    already_exist = existing.cnt if existing else 0

    # Add topic associations for the destination topic
    added_count = 0
    for image_id in image_ids:
        try:
            db.session.execute(text("""
                INSERT OR IGNORE INTO who_am_i_image_topics (image_id, topic)
                VALUES (:image_id, :topic)
            """), {'image_id': image_id, 'topic': destination_topic})
            added_count += 1
        except Exception as e:
            print(f"Error adding image {image_id} to {destination_topic}: {e}")

    db.session.commit()

    # Calculate actual new additions
    new_additions = added_count - already_exist

    return jsonify({
        'success': True,
        'message': f'Copied {len(image_ids)} images from "{source_topic}" to "{destination_topic}"',
        'details': {
            'total_images': len(image_ids),
            'new_additions': new_additions,
            'already_existed': already_exist
        }
    })



# =============================================================================
# PHASE 4: RAFFLE SYSTEM (Student & Admin Routes)
# =============================================================================

# Admin Raffle Management Routes
@admin_bp.route('/api/admin/raffles', methods=['GET'])
@login_required
@role_required('admin')
def api_admin_get_raffles():
    """Get all raffles"""
    from sqlalchemy import text
    
    raffles = db.session.execute(text("""
        SELECT r.*, ps.name as school_name,
               (SELECT COUNT(*) FROM raffle_entries WHERE raffle_id = r.id AND is_active = 1) as active_entries
        FROM raffles r
        LEFT JOIN prize_schools ps ON r.school_id = ps.id
        ORDER BY r.created_at DESC
    """)).fetchall()
    
    return jsonify([{
        'id': r.id,
        'name': r.name,
        'description': r.description,
        'prize_description': r.prize_description,
        'emoji': r.emoji,
        'school_name': r.school_name or 'All Schools',
        'entry_cost': r.entry_cost,
        'max_entries_per_student': r.max_entries_per_student,
        'draw_frequency': r.draw_frequency,
        'is_active': bool(r.is_active),
        'auto_draw_enabled': bool(r.auto_draw_enabled),
        'total_entries': r.total_entries,
        'total_draws': r.total_draws,
        'active_entries': r.active_entries
    } for r in raffles])


@admin_bp.route('/api/admin/raffles', methods=['POST'])
@login_required
@role_required('admin')
def api_admin_create_raffle():
    """Create raffle"""
    from sqlalchemy import text
    
    data = request.json
    
    # Validate required fields
    if not isinstance(data, dict):
        return jsonify({'error': 'Invalid request format - expected JSON object'}), 400
    
    required_fields = ['name', 'prize_description', 'entry_cost']
    missing_fields = [f for f in required_fields if not data.get(f)]
    if missing_fields:
        return jsonify({'error': f'Missing required fields: {", ".join(missing_fields)}'}), 400
    
    # Validate entry_cost is a positive number
    try:
        entry_cost = int(data['entry_cost'])
        if entry_cost < 0:
            return jsonify({'error': 'Entry cost must be a positive number'}), 400
    except (ValueError, TypeError):
        return jsonify({'error': 'Entry cost must be a valid number'}), 400
    
    try:
        result = db.session.execute(text("""
            INSERT INTO raffles (
                name, description, prize_description, emoji,
                school_id, entry_cost, max_entries_per_student,
                draw_frequency, draw_day_of_week, draw_time,
                prize_type, prize_value,
                is_active, auto_draw_enabled, created_by
            ) VALUES (
                :name, :description, :prize_description, :emoji,
                :school_id, :entry_cost, :max_entries,
                :frequency, :day_of_week, :draw_time,
                :prize_type, :prize_value,
                :is_active, :auto_draw, :created_by
            )
        """), {
            'name': data['name'],
            'description': data.get('description'),
            'prize_description': data['prize_description'],
            'emoji': data.get('emoji', '🎟️'),
            'school_id': data.get('school_id'),
            'entry_cost': entry_cost,
            'max_entries': data.get('max_entries_per_student', 10),
            'frequency': data.get('draw_frequency', 'weekly'),
            'day_of_week': data.get('draw_day_of_week', 5),
            'draw_time': data.get('draw_time', '15:00:00'),
            'prize_type': data.get('prize_type', 'physical'),
            'prize_value': data.get('prize_value'),
            'is_active': data.get('is_active', True),
            'auto_draw': data.get('auto_draw_enabled', True),
            'created_by': session['user_id']
        })
        
        raffle_id = result.lastrowid
        db.session.commit()
        
        return jsonify({'success': True, 'raffle_id': raffle_id})
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/admin/raffles/<int:raffle_id>', methods=['PUT'])
@login_required
@role_required('admin')
def api_admin_update_raffle(raffle_id):
    """Update raffle"""
    from sqlalchemy import text
    
    data = request.json
    
    try:
        # Build update query dynamically based on provided fields
        update_fields = []
        params = {'raffle_id': raffle_id}
        
        field_mapping = {
            'name': 'name',
            'description': 'description',
            'prize_description': 'prize_description',
            'emoji': 'emoji',
            'entry_cost': 'entry_cost',
            'max_entries_per_student': 'max_entries_per_student',
            'draw_frequency': 'draw_frequency',
            'draw_day_of_week': 'draw_day_of_week',
            'draw_time': 'draw_time',
            'is_active': 'is_active',
            'auto_draw_enabled': 'auto_draw_enabled'
        }
        
        for json_key, db_key in field_mapping.items():
            if json_key in data:
                update_fields.append(f"{db_key} = :{json_key}")
                params[json_key] = data[json_key]
        
        if not update_fields:
            return jsonify({'error': 'No fields to update'}), 400
        
        query = f"UPDATE raffles SET {', '.join(update_fields)} WHERE id = :raffle_id"
        db.session.execute(text(query), params)
        db.session.commit()
        
        return jsonify({'success': True})
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/admin/raffles/<int:raffle_id>/entries')
@login_required
@role_required('admin')
def api_admin_get_raffle_entries(raffle_id):
    """Get all entries for a raffle"""
    from sqlalchemy import text
    
    try:
        entries = db.session.execute(text("""
            SELECT re.*, 
                   u.full_name as student_name,
                   re.guest_code
            FROM raffle_entries re
            LEFT JOIN users u ON re.student_id = u.id
            WHERE re.raffle_id = :raffle_id AND re.is_active = 1
            ORDER BY re.entered_at DESC
        """), {'raffle_id': raffle_id}).fetchall()
        
        return jsonify([{
            'id': e.id,
            'student_name': e.student_name,
            'guest_code': e.guest_code,
            'entered_at': e.entered_at.isoformat() if e.entered_at else None
        } for e in entries])
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/admin/raffles/winners')
@login_required
@role_required('admin')
def api_admin_get_raffle_winners():
    """Get recent raffle winners"""
    from sqlalchemy import text
    
    try:
        winners = db.session.execute(text("""
            SELECT rd.*, 
                   r.name as raffle_name,
                   r.emoji,
                   r.prize_description,
                   u.full_name as winner_name,
                   rd.winner_guest_code
            FROM raffle_draws rd
            JOIN raffles r ON rd.raffle_id = r.id
            LEFT JOIN users u ON rd.winner_id = u.id
            WHERE rd.status = 'drawn' AND rd.winner_id IS NOT NULL
            ORDER BY rd.drawn_at DESC
            LIMIT 20
        """)).fetchall()
        
        return jsonify([{
            'id': w.id,
            'raffle_name': w.raffle_name,
            'emoji': w.emoji,
            'prize_description': w.prize_description,
            'winner_name': w.winner_name or w.winner_guest_code or 'Unknown',
            'drawn_at': w.drawn_at.isoformat() if w.drawn_at else None,
            'total_entries': w.total_entries if hasattr(w, 'total_entries') else None
        } for w in winners])
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/admin/raffles/<int:raffle_id>/draw', methods=['POST'])
@login_required
@role_required('admin')
def api_admin_manual_draw(raffle_id):
    """Manual draw with winner info returned"""
    from sqlalchemy import text
    
    draw_id = perform_raffle_draw(raffle_id)
    
    if draw_id:
        # Get winner info from the draw
        try:
            winner_info = db.session.execute(text("""
                SELECT rd.*, 
                       r.name as raffle_name,
                       r.prize_description,
                       u.full_name as winner_name,
                       rd.winner_guest_code
                FROM raffle_draws rd
                JOIN raffles r ON rd.raffle_id = r.id
                LEFT JOIN users u ON rd.winner_id = u.id
                WHERE rd.id = :draw_id
            """), {'draw_id': draw_id}).fetchone()
            
            if winner_info:
                return jsonify({
                    'success': True, 
                    'draw_id': draw_id,
                    'winner': {
                        'name': winner_info.winner_name or winner_info.winner_guest_code or 'Unknown',
                        'class': None  # Could add class info if needed
                    },
                    'prize': winner_info.prize_description
                })
        except Exception as e:
            print(f"Error getting winner info: {e}")
        
        return jsonify({'success': True, 'draw_id': draw_id})
    else:
        return jsonify({'error': 'Draw failed - no entries or error occurred'}), 500


# Student Raffle Routes
@admin_bp.route('/api/raffles/available')
@login_required
def api_raffles_available():
    """Get available raffles for student (supports both registered and guest users)"""
    from sqlalchemy import text
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    try:
        # Build query based on user type
        if user_id:
            raffles = db.session.execute(text("""
                SELECT r.*,
                       (SELECT COUNT(*) FROM raffle_entries WHERE raffle_id = r.id AND student_id = :user_id AND is_active = 1) as my_entries,
                       (SELECT COUNT(*) FROM raffle_entries WHERE raffle_id = r.id AND is_active = 1) as total_entries
                FROM raffles r
                WHERE r.is_active = 1
                ORDER BY r.created_at DESC
            """), {'user_id': user_id}).fetchall()
        elif guest_code:
            raffles = db.session.execute(text("""
                SELECT r.*,
                       (SELECT COUNT(*) FROM raffle_entries WHERE raffle_id = r.id AND guest_code = :guest_code AND is_active = 1) as my_entries,
                       (SELECT COUNT(*) FROM raffle_entries WHERE raffle_id = r.id AND is_active = 1) as total_entries
                FROM raffles r
                WHERE r.is_active = 1
                ORDER BY r.created_at DESC
            """), {'guest_code': guest_code}).fetchall()
        else:
            return jsonify({'error': 'Not authenticated'}), 401
        
        return jsonify([{
            'id': r.id,
            'name': r.name,
            'description': r.description,
            'prize_description': r.prize_description,
            'emoji': r.emoji or '🎟️',
            'entry_cost': r.entry_cost,
            'max_entries_per_student': r.max_entries_per_student,
            'draw_frequency': r.draw_frequency,
            'my_entries': r.my_entries or 0,
            'total_entries': r.total_entries or 0
        } for r in raffles])
        
    except Exception as e:
        print(f"Error getting raffles: {e}")
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/raffles/<int:raffle_id>/enter', methods=['POST'])
@login_required
def api_raffle_enter(raffle_id):
    """Buy raffle entries - supports both registered users and guests"""
    from sqlalchemy import text
    
    data = request.json
    num_entries = data.get('entries', 1)
    
    guest_code = session.get('guest_code')
    user_id = session.get('user_id')
    
    # Determine if this is a guest user (has guest_code and points in guest_users)
    # or a registered user (has user_id and points in user_stats)
    is_guest_user = False
    if guest_code:
        # Check if this guest has points in guest_users table
        guest_check = db.session.execute(text("""
            SELECT total_score FROM guest_users WHERE guest_code = :guest_code
        """), {'guest_code': guest_code}).fetchone()
        if guest_check:
            is_guest_user = True
    
    if not user_id and not guest_code:
        return jsonify({'error': 'Not authenticated'}), 401
    
    try:
        # Get raffle info
        raffle = db.session.execute(text("""
            SELECT * FROM raffles WHERE id = :raffle_id AND is_active = 1
        """), {'raffle_id': raffle_id}).fetchone()
        
        if not raffle:
            return jsonify({'error': 'Raffle not found'}), 404
        
        # Check current entries for this user
        if is_guest_user:
            current = db.session.execute(text("""
                SELECT COUNT(*) as total
                FROM raffle_entries
                WHERE raffle_id = :raffle_id AND guest_code = :guest_code AND is_active = 1
            """), {'raffle_id': raffle_id, 'guest_code': guest_code}).fetchone()
        else:
            current = db.session.execute(text("""
                SELECT COUNT(*) as total
                FROM raffle_entries
                WHERE raffle_id = :raffle_id AND student_id = :user_id AND is_active = 1
            """), {'raffle_id': raffle_id, 'user_id': user_id}).fetchone()
        
        current_count = current.total if current else 0
        
        if current_count + num_entries > raffle.max_entries_per_student:
            return jsonify({'error': f'Maximum {raffle.max_entries_per_student} entries allowed. You have {current_count}.'}), 400
        
        cost = raffle.entry_cost * num_entries
        
        # Get and check user's points
        if is_guest_user:
            guest = db.session.execute(text("""
                SELECT total_score FROM guest_users WHERE guest_code = :guest_code
            """), {'guest_code': guest_code}).fetchone()
            points = guest.total_score if guest else 0
        else:
            stats = db.session.execute(text("""
                SELECT total_points FROM user_stats WHERE user_id = :user_id
            """), {'user_id': user_id}).fetchone()
            points = stats.total_points if stats else 0
        
        if points < cost:
            return jsonify({'error': f'Not enough points. Need {cost}, have {points}.'}), 400
        
        # Deduct points
        if is_guest_user:
            db.session.execute(text("""
                UPDATE guest_users SET total_score = total_score - :cost WHERE guest_code = :guest_code
            """), {'cost': cost, 'guest_code': guest_code})
        else:
            db.session.execute(text("""
                UPDATE user_stats SET total_points = total_points - :cost WHERE user_id = :user_id
            """), {'cost': cost, 'user_id': user_id})
        
        # Create entry records (one per entry for fair drawing)
        for _ in range(num_entries):
            db.session.execute(text("""
                INSERT INTO raffle_entries (
                    raffle_id, student_id, guest_code, points_spent, is_active
                ) VALUES (
                    :raffle_id, :student_id, :guest_code, :cost_per_entry, 1
                )
            """), {
                'raffle_id': raffle_id,
                'student_id': user_id if not is_guest_user else None,
                'guest_code': guest_code if is_guest_user else None,
                'cost_per_entry': raffle.entry_cost
            })
        
        # Update raffle total entries
        db.session.execute(text("""
            UPDATE raffles SET total_entries = total_entries + :entries
            WHERE id = :raffle_id
        """), {'entries': num_entries, 'raffle_id': raffle_id})
        
        db.session.commit()
        
        # Get updated entry count
        new_total = current_count + num_entries
        
        return jsonify({
            'success': True, 
            'entries_purchased': num_entries,
            'total_entries': new_total,
            'points_spent': cost,
            'remaining_points': points - cost
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/raffles/check-wins')
@login_required
def api_check_raffle_wins():
    """Check for unacknowledged wins - supports both registered users and guests"""
    from sqlalchemy import text
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    try:
        if user_id:
            wins = db.session.execute(text("""
                SELECT wn.*, rd.token, rd.token_expires_at,
                       r.name as raffle_name, r.prize_description, r.emoji
                FROM winner_notifications wn
                JOIN raffle_draws rd ON wn.draw_id = rd.id
                JOIN raffles r ON rd.raffle_id = r.id
                WHERE wn.winner_id = :user_id AND wn.acknowledged = 0
            """), {'user_id': user_id}).fetchall()
        elif guest_code:
            wins = db.session.execute(text("""
                SELECT wn.*, rd.token, rd.token_expires_at,
                       r.name as raffle_name, r.prize_description, r.emoji
                FROM winner_notifications wn
                JOIN raffle_draws rd ON wn.draw_id = rd.id
                JOIN raffles r ON rd.raffle_id = r.id
                WHERE wn.winner_guest_code = :guest_code AND wn.acknowledged = 0
            """), {'guest_code': guest_code}).fetchall()
        else:
            return jsonify([])
        
        return jsonify([{
            'id': w.id,
            'draw_id': w.draw_id,
            'raffle_name': w.raffle_name,
            'prize_description': w.prize_description,
            'emoji': w.emoji,
            'token': w.token,
            'expires_at': str(w.token_expires_at) if w.token_expires_at else None,
            'message': w.message
        } for w in wins])
        
    except Exception as e:
        print(f"Error checking wins: {e}")
        return jsonify([])


@admin_bp.route('/api/raffles/wins/<int:notification_id>/acknowledge', methods=['POST'])
@login_required
def api_acknowledge_win(notification_id):
    """Acknowledge winner notification"""
    from sqlalchemy import text
    
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code')
    
    if user_id:
        db.session.execute(text("""
            UPDATE winner_notifications
            SET acknowledged = 1, acknowledged_at = CURRENT_TIMESTAMP
            WHERE id = :notification_id AND winner_id = :user_id
        """), {'notification_id': notification_id, 'user_id': user_id})
    elif guest_code:
        db.session.execute(text("""
            UPDATE winner_notifications
            SET acknowledged = 1, acknowledged_at = CURRENT_TIMESTAMP
            WHERE id = :notification_id AND winner_guest_code = :guest_code
        """), {'notification_id': notification_id, 'guest_code': guest_code})
    
    db.session.commit()
    
    return jsonify({'success': True})


@admin_bp.route('/api/raffles/winners')
@login_required
def api_student_raffle_winners():
    """Get recent raffle winners for students to see"""
    from sqlalchemy import text
    
    try:
        winners = db.session.execute(text("""
            SELECT rd.id, rd.drawn_at, rd.total_entries,
                   r.name as raffle_name, r.emoji, r.prize_description,
                   CASE 
                       WHEN u.id IS NOT NULL THEN u.full_name
                       WHEN rd.winner_guest_code IS NOT NULL THEN 'Guest ' || SUBSTR(rd.winner_guest_code, 1, 4) || '***'
                       ELSE 'Anonymous'
                   END as winner_name
            FROM raffle_draws rd
            JOIN raffles r ON rd.raffle_id = r.id
            LEFT JOIN users u ON rd.winner_id = u.id
            WHERE rd.status = 'drawn' AND rd.winner_id IS NOT NULL
            ORDER BY rd.drawn_at DESC
            LIMIT 10
        """)).fetchall()
        
        return jsonify([{
            'id': w.id,
            'raffle_name': w.raffle_name,
            'emoji': w.emoji,
            'prize_description': w.prize_description,
            'winner_name': w.winner_name,
            'drawn_at': w.drawn_at.isoformat() if w.drawn_at else None,
            'total_entries': w.total_entries
        } for w in winners])
        
    except Exception as e:
        print(f"Error getting winners: {e}")
        return jsonify([])


# Remove old duplicate route
# @admin_bp.route('/api/raffles/acknowledge-win/<int:notification_id>', methods=['POST'])


# =============================================================================
# RAFFLE HELPER FUNCTIONS
# =============================================================================

def generate_raffle_token():
    """Generate unique token for raffle prize collection"""
    import secrets
    return secrets.token_urlsafe(12)


def get_user_school_id(user_id):
    """Get the school_id for a student"""
    from sqlalchemy import text
    result = db.session.execute(text("""
        SELECT school_id FROM prize_redemptions 
        WHERE user_id = :user_id 
        LIMIT 1
    """), {'user_id': user_id}).fetchone()
    
    if result:
        return result.school_id
    
    result = db.session.execute(text("""
        SELECT c.school_id 
        FROM class_enrollments ce
        JOIN classes c ON ce.class_id = c.id
        WHERE ce.student_id = :user_id
        LIMIT 1
    """), {'user_id': user_id}).fetchone()
    
    return result.school_id if result else None


def select_raffle_winner(raffle_id, draw_id):
    """Randomly select a winner from active entries (supports both users and guests)"""
    from sqlalchemy import text
    import random
    
    # Get all active entries - each row is one entry (ticket)
    entries = db.session.execute(text("""
        SELECT id, student_id, guest_code
        FROM raffle_entries
        WHERE raffle_id = :raffle_id 
        AND is_active = 1
    """), {'raffle_id': raffle_id}).fetchall()
    
    if not entries:
        return None, None, None
    
    # Each entry is already one ticket, so just pick randomly
    winning_entry = random.choice(entries)
    
    return winning_entry.student_id, winning_entry.guest_code, winning_entry.id


def perform_raffle_draw(raffle_id):
    """Perform a raffle draw - supports both registered users and guests"""
    from sqlalchemy import text
    from datetime import datetime, timedelta
    
    try:
        raffle = db.session.execute(text("""
            SELECT * FROM raffles WHERE id = :raffle_id
        """), {'raffle_id': raffle_id}).fetchone()
        
        if not raffle:
            print(f"Raffle {raffle_id} not found")
            return None
        
        # Check if there are any entries
        entry_count = db.session.execute(text("""
            SELECT COUNT(*) as cnt FROM raffle_entries
            WHERE raffle_id = :raffle_id AND is_active = 1
        """), {'raffle_id': raffle_id}).fetchone()
        
        if not entry_count or entry_count.cnt == 0:
            print(f"Raffle {raffle_id} has no entries - skipping draw")
            return None
        
        draw_date = datetime.now().date()
        draw_time = datetime.now()
        
        result = db.session.execute(text("""
            INSERT INTO raffle_draws (
                raffle_id, school_id, draw_date, draw_time,
                status, drawn_at, drawn_by
            ) VALUES (
                :raffle_id, :school_id, :draw_date, :draw_time,
                'drawing', CURRENT_TIMESTAMP, 'system'
            )
        """), {
            'raffle_id': raffle_id,
            'school_id': raffle.school_id if hasattr(raffle, 'school_id') else None,
            'draw_date': draw_date,
            'draw_time': draw_time
        })
        
        draw_id = result.lastrowid
        db.session.commit()
        
        # Select winner (returns user_id, guest_code, entry_id)
        winner_id, winner_guest_code, winning_entry_id = select_raffle_winner(raffle_id, draw_id)
        
        stats = db.session.execute(text("""
            SELECT COUNT(*) as total_entries,
                   COUNT(DISTINCT COALESCE(student_id, guest_code)) as total_participants
            FROM raffle_entries
            WHERE raffle_id = :raffle_id AND is_active = 1
        """), {'raffle_id': raffle_id}).fetchone()
        
        if winner_id or winner_guest_code:
            token = generate_raffle_token()
            token_expires = draw_time + timedelta(days=7)
            
            db.session.execute(text("""
                UPDATE raffle_draws
                SET winner_id = :winner_id,
                    winner_guest_code = :winner_guest_code,
                    winning_entry_id = :winning_entry_id,
                    total_entries = :total_entries,
                    total_participants = :total_participants,
                    token = :token,
                    token_expires_at = :token_expires,
                    status = 'drawn'
                WHERE id = :draw_id
            """), {
                'winner_id': winner_id,
                'winner_guest_code': winner_guest_code,
                'winning_entry_id': winning_entry_id,
                'total_entries': stats.total_entries,
                'total_participants': stats.total_participants,
                'token': token,
                'token_expires': token_expires,
                'draw_id': draw_id
            })
            
            # Mark all entries for this raffle as used
            db.session.execute(text("""
                UPDATE raffle_entries
                SET is_active = 0, draw_id = :draw_id
                WHERE raffle_id = :raffle_id AND is_active = 1
            """), {'draw_id': draw_id, 'raffle_id': raffle_id})
            
            # Create winner notification
            message = f"🎉 Congratulations! You won the {raffle.name}! Prize: {raffle.prize_description}"
            
            db.session.execute(text("""
                INSERT INTO winner_notifications (
                    draw_id, winner_id, winner_guest_code, notification_type, message, acknowledged
                ) VALUES (
                    :draw_id, :winner_id, :winner_guest_code, 'on_login', :message, 0
                )
            """), {
                'draw_id': draw_id,
                'winner_id': winner_id,
                'winner_guest_code': winner_guest_code,
                'message': message
            })
            
            db.session.commit()
            print(f"Raffle {raffle_id} draw complete - Winner: {winner_id or winner_guest_code}")
            
        else:
            db.session.execute(text("""
                UPDATE raffle_draws
                SET status = 'no_entries',
                    total_entries = 0,
                    total_participants = 0
                WHERE id = :draw_id
            """), {'draw_id': draw_id})
            db.session.commit()
            print(f"Raffle {raffle_id} draw complete - No winner (no valid entries)")
        
        # Update raffle total draws count
        db.session.execute(text("""
            UPDATE raffles
            SET total_draws = total_draws + 1
            WHERE id = :raffle_id
        """), {'raffle_id': raffle_id})
        db.session.commit()
        
        return draw_id
        
    except Exception as e:
        db.session.rollback()
        print(f"Error drawing raffle {raffle_id}: {e}")
        import traceback
        traceback.print_exc()
        return None


def check_and_run_auto_draws():
    """Check for raffles that need automatic draws and run them"""
    from sqlalchemy import text
    from datetime import datetime
    
    now = datetime.now()
    current_day = now.weekday()  # 0=Monday, 6=Sunday
    current_time = now.strftime('%H:%M')
    
    results = {
        'checked': 0,
        'drawn': 0,
        'skipped': 0,
        'errors': 0,
        'details': []
    }
    
    try:
        # Find raffles due for auto-draw
        # Weekly: check if today is the draw day and we haven't drawn this week
        # Monthly: check if today is the 1st and we haven't drawn this month
        
        raffles = db.session.execute(text("""
            SELECT r.* FROM raffles r
            WHERE r.is_active = 1 
            AND r.auto_draw_enabled = 1
            AND r.draw_frequency IN ('weekly', 'daily', 'monthly')
        """)).fetchall()
        
        results['checked'] = len(raffles)
        
        for raffle in raffles:
            try:
                should_draw = False
                reason = ""
                
                # Check if already drawn today
                today_draw = db.session.execute(text("""
                    SELECT id FROM raffle_draws 
                    WHERE raffle_id = :raffle_id 
                    AND DATE(drawn_at) = DATE('now')
                """), {'raffle_id': raffle.id}).fetchone()
                
                if today_draw:
                    results['skipped'] += 1
                    results['details'].append({
                        'raffle': raffle.name,
                        'action': 'skipped',
                        'reason': 'Already drawn today'
                    })
                    continue
                
                # Check draw frequency
                if raffle.draw_frequency == 'daily':
                    # Daily draws happen every day at the specified time
                    draw_time = raffle.draw_time or '15:00'
                    if current_time >= draw_time[:5]:
                        should_draw = True
                        reason = "Daily draw time reached"
                        
                elif raffle.draw_frequency == 'weekly':
                    # Weekly draws happen on the specified day
                    draw_day = raffle.draw_day_of_week if raffle.draw_day_of_week is not None else 4  # Default Friday
                    draw_time = raffle.draw_time or '15:00'
                    
                    if current_day == draw_day and current_time >= draw_time[:5]:
                        # Check if already drawn this week
                        week_start = now.date() - timedelta(days=current_day)
                        week_draw = db.session.execute(text("""
                            SELECT id FROM raffle_draws 
                            WHERE raffle_id = :raffle_id 
                            AND DATE(drawn_at) >= :week_start
                        """), {'raffle_id': raffle.id, 'week_start': week_start}).fetchone()
                        
                        if not week_draw:
                            should_draw = True
                            reason = f"Weekly draw day ({['Mon','Tue','Wed','Thu','Fri','Sat','Sun'][draw_day]})"
                            
                elif raffle.draw_frequency == 'monthly':
                    # Monthly draws happen on the 1st of each month
                    if now.day == 1:
                        draw_time = raffle.draw_time or '15:00'
                        if current_time >= draw_time[:5]:
                            # Check if already drawn this month
                            month_draw = db.session.execute(text("""
                                SELECT id FROM raffle_draws 
                                WHERE raffle_id = :raffle_id 
                                AND strftime('%Y-%m', drawn_at) = strftime('%Y-%m', 'now')
                            """), {'raffle_id': raffle.id}).fetchone()
                            
                            if not month_draw:
                                should_draw = True
                                reason = "Monthly draw (1st of month)"
                
                if should_draw:
                    # Check if there are entries
                    entry_count = db.session.execute(text("""
                        SELECT COUNT(*) as cnt FROM raffle_entries
                        WHERE raffle_id = :raffle_id AND is_active = 1
                    """), {'raffle_id': raffle.id}).fetchone()
                    
                    if entry_count and entry_count.cnt > 0:
                        draw_id = perform_raffle_draw(raffle.id)
                        if draw_id:
                            results['drawn'] += 1
                            results['details'].append({
                                'raffle': raffle.name,
                                'action': 'drawn',
                                'reason': reason,
                                'draw_id': draw_id,
                                'entries': entry_count.cnt
                            })
                        else:
                            results['errors'] += 1
                            results['details'].append({
                                'raffle': raffle.name,
                                'action': 'error',
                                'reason': 'Draw function failed'
                            })
                    else:
                        results['skipped'] += 1
                        results['details'].append({
                            'raffle': raffle.name,
                            'action': 'skipped',
                            'reason': 'No entries to draw from'
                        })
                else:
                    results['skipped'] += 1
                    
            except Exception as e:
                results['errors'] += 1
                results['details'].append({
                    'raffle': raffle.name if raffle else 'Unknown',
                    'action': 'error',
                    'reason': str(e)
                })
                print(f"Error checking raffle {raffle.id}: {e}")
                
        return results
        
    except Exception as e:
        print(f"Error in auto-draw check: {e}")
        import traceback
        traceback.print_exc()
        return {'error': str(e)}


@admin_bp.route('/api/admin/raffles/auto-draw', methods=['POST'])
@login_required
@role_required('admin')
def api_admin_trigger_auto_draws():
    """Manually trigger auto-draw check (for testing or manual runs)"""
    results = check_and_run_auto_draws()
    return jsonify(results)

# =============================================================================
# ADMIN QUESTION HISTORY MANAGEMENT
# =============================================================================

@admin_bp.route('/api/admin/question-history/stats')
@login_required
@role_required('admin')
def admin_question_history_stats():
    """Get statistics about question history tracking"""
    from sqlalchemy import text
    
    try:
        stats = {}
        
        # Total records
        total = db.session.execute(text(
            "SELECT COUNT(*) FROM user_question_history"
        )).fetchone()
        stats['total_records'] = total[0] if total else 0
        
        # Unique users
        users = db.session.execute(text(
            "SELECT COUNT(DISTINCT user_id) FROM user_question_history WHERE user_id IS NOT NULL"
        )).fetchone()
        stats['unique_users'] = users[0] if users else 0
        
        # Unique guests
        guests = db.session.execute(text(
            "SELECT COUNT(DISTINCT guest_code) FROM user_question_history WHERE guest_code IS NOT NULL"
        )).fetchone()
        stats['unique_guests'] = guests[0] if guests else 0
        
        # By topic
        by_topic = db.session.execute(text("""
            SELECT topic, COUNT(*) as count
            FROM user_question_history
            GROUP BY topic
            ORDER BY count DESC
        """)).fetchall()
        stats['by_topic'] = [{
            'topic': row.topic,
            'count': row.count
        } for row in by_topic]
        
        return jsonify(stats)
        
    except Exception as e:
        return jsonify({'error': str(e), 'message': 'Table may not exist yet'}), 200


@admin_bp.route('/api/admin/question-history/clear', methods=['POST'])
@login_required
@role_required('admin')
def admin_clear_question_history():
    """Clear question history - can clear for specific user or all"""
    from sqlalchemy import text
    
    data = request.json or {}
    user_id = data.get('user_id')
    guest_code = data.get('guest_code')
    topic = data.get('topic')
    clear_all = data.get('clear_all', False)
    
    try:
        if clear_all:
            db.session.execute(text("DELETE FROM user_question_history"))
            message = "Cleared all question history"
        elif user_id:
            if topic:
                db.session.execute(text("""
                    DELETE FROM user_question_history 
                    WHERE user_id = :user_id AND topic = :topic
                """), {'user_id': user_id, 'topic': topic})
                message = f"Cleared history for user {user_id} on topic {topic}"
            else:
                db.session.execute(text("""
                    DELETE FROM user_question_history WHERE user_id = :user_id
                """), {'user_id': user_id})
                message = f"Cleared all history for user {user_id}"
        elif guest_code:
            if topic:
                db.session.execute(text("""
                    DELETE FROM user_question_history 
                    WHERE guest_code = :guest_code AND topic = :topic
                """), {'guest_code': guest_code, 'topic': topic})
                message = f"Cleared history for guest {guest_code} on topic {topic}"
            else:
                db.session.execute(text("""
                    DELETE FROM user_question_history WHERE guest_code = :guest_code
                """), {'guest_code': guest_code})
                message = f"Cleared all history for guest {guest_code}"
        else:
            return jsonify({'error': 'Specify user_id, guest_code, or clear_all=true'}), 400
        
        db.session.commit()
        return jsonify({'success': True, 'message': message})
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# =============================================================================
# ADMIN ADAPTIVE QUESTION HISTORY MANAGEMENT
# =============================================================================

@admin_bp.route('/api/admin/adaptive-question-history/stats')
@login_required
@role_required('admin')
def admin_adaptive_question_history_stats():
    """Get statistics about adaptive question history tracking (Learning in Stages)"""
    from sqlalchemy import text
    
    try:
        stats = {}
        
        # Total records
        total = db.session.execute(text(
            "SELECT COUNT(*) FROM user_adaptive_question_history"
        )).fetchone()
        stats['total_records'] = total[0] if total else 0
        
        # Unique users
        users = db.session.execute(text(
            "SELECT COUNT(DISTINCT user_id) FROM user_adaptive_question_history WHERE user_id IS NOT NULL"
        )).fetchone()
        stats['unique_users'] = users[0] if users else 0
        
        # Unique guests
        guests = db.session.execute(text(
            "SELECT COUNT(DISTINCT guest_code) FROM user_adaptive_question_history WHERE guest_code IS NOT NULL"
        )).fetchone()
        stats['unique_guests'] = guests[0] if guests else 0
        
        # By topic
        by_topic = db.session.execute(text("""
            SELECT topic, COUNT(*) as count
            FROM user_adaptive_question_history
            GROUP BY topic
            ORDER BY count DESC
            LIMIT 20
        """)).fetchall()
        stats['by_topic'] = [{
            'topic': row.topic,
            'count': row.count
        } for row in by_topic]
        
        # By level
        by_level = db.session.execute(text("""
            SELECT difficulty_level, COUNT(*) as count
            FROM user_adaptive_question_history
            GROUP BY difficulty_level
            ORDER BY difficulty_level
        """)).fetchall()
        stats['by_level'] = [{
            'level': row.difficulty_level,
            'count': row.count
        } for row in by_level]
        
        return jsonify(stats)
        
    except Exception as e:
        return jsonify({'error': str(e), 'message': 'Table may not exist yet - run the CREATE TABLE script'}), 200


@admin_bp.route('/api/admin/adaptive-question-history/clear', methods=['POST'])
@login_required
@role_required('admin')
def admin_clear_adaptive_question_history():
    """Clear adaptive question history - can clear for specific user, topic, or all"""
    from sqlalchemy import text
    
    data = request.json or {}
    user_id = data.get('user_id')
    guest_code = data.get('guest_code')
    topic = data.get('topic')
    clear_all = data.get('clear_all', False)
    
    try:
        if clear_all:
            db.session.execute(text("DELETE FROM user_adaptive_question_history"))
            message = "Cleared all adaptive question history"
        elif user_id:
            if topic:
                db.session.execute(text("""
                    DELETE FROM user_adaptive_question_history 
                    WHERE user_id = :user_id AND topic = :topic
                """), {'user_id': user_id, 'topic': topic})
                message = f"Cleared adaptive history for user {user_id} on topic {topic}"
            else:
                db.session.execute(text("""
                    DELETE FROM user_adaptive_question_history WHERE user_id = :user_id
                """), {'user_id': user_id})
                message = f"Cleared all adaptive history for user {user_id}"
        elif guest_code:
            if topic:
                db.session.execute(text("""
                    DELETE FROM user_adaptive_question_history 
                    WHERE guest_code = :guest_code AND topic = :topic
                """), {'guest_code': guest_code, 'topic': topic})
                message = f"Cleared adaptive history for guest {guest_code} on topic {topic}"
            else:
                db.session.execute(text("""
                    DELETE FROM user_adaptive_question_history WHERE guest_code = :guest_code
                """), {'guest_code': guest_code})
                message = f"Cleared all adaptive history for guest {guest_code}"
        elif topic:
            db.session.execute(text("""
                DELETE FROM user_adaptive_question_history WHERE topic = :topic
            """), {'topic': topic})
            message = f"Cleared all adaptive history for topic {topic}"
        else:
            return jsonify({'error': 'Specify user_id, guest_code, topic, or clear_all=true'}), 400
        
        db.session.commit()
        return jsonify({'success': True, 'message': message})
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# =============================================================================
# ADMIN USER ANALYTICS & MANAGEMENT ROUTES
# =============================================================================

@admin_bp.route('/api/admin/analytics/overview')
@login_required
@role_required('admin')
def admin_analytics_overview():
    """Get overview statistics"""
    from sqlalchemy import text
    
    # Count registered users (exclude guest accounts)
    registered_count = db.session.execute(text("""
        SELECT COUNT(*) 
        FROM users 
        WHERE email NOT LIKE 'guest%@%' 
        AND role = 'student'
    """)).scalar()
    
    # Count repeat guests
    repeat_guests_count = db.session.execute(text("""
        SELECT COUNT(*) FROM guest_users
    """)).scalar() or 0
    
    # Count inactive guests (60+ days)
    sixty_days_ago = datetime.utcnow() - timedelta(days=60)
    inactive_guests = db.session.execute(text("""
        SELECT COUNT(*) 
        FROM guest_users 
        WHERE last_active < :cutoff
    """), {'cutoff': sixty_days_ago}).scalar() or 0
    
    # Count casual sessions today (approximate from guest_sessions if exists)
    try:
        casual_today = db.session.execute(text("""
            SELECT COUNT(*) 
            FROM guest_sessions 
            WHERE DATE(created_at) = DATE('now')
        """)).scalar() or 0
    except:
        casual_today = 0
    
    return jsonify({
        'registered_users': registered_count,
        'repeat_guests': repeat_guests_count,
        'inactive_guests': inactive_guests,
        'casual_sessions_today': casual_today
    })


@admin_bp.route('/api/admin/analytics/debug')
@login_required
@role_required('admin')
def admin_analytics_debug():
    """Debug endpoint to check table structure"""
    from sqlalchemy import text
    
    results = {}
    
    # Check guest_users columns
    try:
        # Get one row to see what columns exist
        sample = db.session.execute(text("SELECT * FROM guest_users LIMIT 1")).fetchone()
        if sample:
            results['guest_users_columns'] = list(sample._mapping.keys()) if hasattr(sample, '_mapping') else f"Row has {len(sample)} columns"
            results['guest_users_sample'] = [str(x) for x in sample]
        else:
            results['guest_users_columns'] = 'Table empty'
        results['guest_users_count'] = db.session.execute(text("SELECT COUNT(*) FROM guest_users")).scalar()
    except Exception as e:
        results['guest_users_error'] = str(e)
    
    # Check users table
    try:
        sample = db.session.execute(text("SELECT id, email, full_name, role FROM users WHERE role='student' LIMIT 1")).fetchone()
        if sample:
            results['users_sample'] = [str(x) for x in sample]
        results['users_student_count'] = db.session.execute(text("SELECT COUNT(*) FROM users WHERE role='student'")).scalar()
    except Exception as e:
        results['users_error'] = str(e)
    
    # Check user_stats table
    try:
        results['user_stats_count'] = db.session.execute(text("SELECT COUNT(*) FROM user_stats")).scalar()
    except Exception as e:
        results['user_stats_error'] = str(e)
    
    return jsonify(results)


@admin_bp.route('/api/admin/analytics/registered-users')
@login_required
@role_required('admin')
def admin_analytics_registered_users():
    """Get list of all registered users with stats"""
    from sqlalchemy import text
    
    try:
        # Count first
        count = db.session.execute(text("""
            SELECT COUNT(*) FROM users 
            WHERE email NOT LIKE 'guest%@%' AND role = 'student'
        """)).scalar()
        print(f"DEBUG: Found {count} registered students")
        
        if count == 0:
            return jsonify([])
        
        # Simple query
        rows = db.session.execute(text("""
            SELECT id, email, full_name, created_at
            FROM users
            WHERE email NOT LIKE 'guest%@%'
            AND role = 'student'
            ORDER BY created_at DESC
            LIMIT 200
        """)).fetchall()
        
        print(f"DEBUG: Query returned {len(rows)} rows")
        
        if rows:
            print(f"DEBUG: First row: {list(rows[0])}")
        
        result = []
        now = datetime.utcnow()
        
        for row in rows:
            row_data = list(row)
            user_id = row_data[0]
            email = row_data[1] if len(row_data) > 1 else 'unknown'
            full_name = row_data[2] if len(row_data) > 2 and row_data[2] else 'Unknown'
            created_at = row_data[3] if len(row_data) > 3 else None
            
            # Try to get stats
            points = 0
            last_active = created_at
            try:
                stats = db.session.execute(text(
                    "SELECT total_points, updated_at FROM user_stats WHERE user_id = :uid"
                ), {'uid': user_id}).fetchone()
                if stats:
                    points = stats[0] if stats[0] else 0
                    if stats[1]:
                        last_active = stats[1]
            except Exception as e:
                print(f"DEBUG: Error getting stats for user {user_id}: {e}")
            
            days_inactive = 0
            if last_active:
                try:
                    days_inactive = (now - last_active).days
                except:
                    pass
            
            result.append({
                'id': user_id,
                'email': str(email),
                'full_name': str(full_name),
                'points': points,
                'quizzes': 0,
                'last_active': last_active.isoformat() if last_active and hasattr(last_active, 'isoformat') else str(last_active) if last_active else None,
                'activity_status': 'active' if days_inactive < 7 else ('stale' if days_inactive < 30 else 'inactive'),
                'activity_label': 'Active' if days_inactive < 7 else ('Inactive' if days_inactive < 30 else f'{days_inactive}d ago')
            })
        
        print(f"DEBUG: Returning {len(result)} users")
        return jsonify(result)
        
    except Exception as e:
        import traceback
        error_msg = str(e)
        trace = traceback.format_exc()
        print(f"ERROR in registered-users: {error_msg}")
        print(trace)
        return jsonify({'error': error_msg, 'trace': trace})


@admin_bp.route('/api/admin/analytics/repeat-guests')
@login_required
@role_required('admin')
def admin_analytics_repeat_guests():
    """Get list of all repeat guests with stats"""
    from sqlalchemy import text
    
    try:
        # First, let's see what we're working with
        count = db.session.execute(text("SELECT COUNT(*) FROM guest_users")).scalar()
        print(f"DEBUG: guest_users has {count} rows")
        
        if count == 0:
            return jsonify([])
        
        # Get column names first
        try:
            # SQLite way to get column info
            columns_info = db.session.execute(text("PRAGMA table_info(guest_users)")).fetchall()
            column_names = [col[1] for col in columns_info]  # col[1] is the column name
            print(f"DEBUG: guest_users columns: {column_names}")
        except Exception as e:
            print(f"DEBUG: Could not get columns: {e}")
            column_names = []
        
        # Build SELECT based on available columns
        select_cols = ['guest_code']  # This must exist
        if 'total_score' in column_names:
            select_cols.append('total_score')
        if 'created_at' in column_names:
            select_cols.append('created_at')
        if 'last_active' in column_names:
            select_cols.append('last_active')
        if 'nickname' in column_names:
            select_cols.append('nickname')
        
        query = f"SELECT {', '.join(select_cols)} FROM guest_users ORDER BY last_active DESC LIMIT 200"
        print(f"DEBUG: Running query: {query}")
        
        rows = db.session.execute(text(query)).fetchall()
        print(f"DEBUG: Got {len(rows)} rows")
        
        if not rows:
            return jsonify([])
        
        # Print first row for debugging
        if rows:
            print(f"DEBUG: First row: {list(rows[0])}")
        
        result = []
        now = datetime.utcnow()
        
        for row in rows:
            row_data = list(row)  # Convert to list for index access
            
            # Map based on select_cols order
            guest_code = row_data[0] if len(row_data) > 0 else 'unknown'
            
            total_score = 0
            created_at = None
            last_active = None
            nickname = None
            
            col_idx = 1
            if 'total_score' in select_cols:
                total_score = row_data[col_idx] if len(row_data) > col_idx and row_data[col_idx] else 0
                col_idx += 1
            if 'created_at' in select_cols:
                created_at = row_data[col_idx] if len(row_data) > col_idx else None
                col_idx += 1
            if 'last_active' in select_cols:
                last_active = row_data[col_idx] if len(row_data) > col_idx else None
                col_idx += 1
            if 'nickname' in select_cols:
                nickname = row_data[col_idx] if len(row_data) > col_idx else None
            
            days_inactive = 0
            if last_active:
                try:
                    days_inactive = (now - last_active).days
                except:
                    pass
            
            result.append({
                'guest_code': str(guest_code),
                'nickname': nickname,
                'total_score': total_score or 0,
                'quizzes_completed': 0,
                'created_at': created_at.isoformat() if created_at and hasattr(created_at, 'isoformat') else str(created_at) if created_at else None,
                'last_active': last_active.isoformat() if last_active and hasattr(last_active, 'isoformat') else str(last_active) if last_active else None,
                'days_inactive': days_inactive,
                'activity_status': 'active' if days_inactive < 7 else ('stale' if days_inactive < 60 else 'inactive'),
                'activity_label': 'Active' if days_inactive < 7 else (f'{days_inactive}d ago' if days_inactive < 60 else f'Inactive {days_inactive}d')
            })
        
        print(f"DEBUG: Returning {len(result)} guests")
        return jsonify(result)
        
    except Exception as e:
        import traceback
        error_msg = str(e)
        trace = traceback.format_exc()
        print(f"ERROR in repeat-guests: {error_msg}")
        print(trace)
        return jsonify({'error': error_msg, 'trace': trace, 'debug': 'Check server logs'})


@admin_bp.route('/api/admin/analytics/inactive-users')
@login_required
@role_required('admin')
def admin_analytics_inactive_users():
    """Get list of inactive users (60+ days)"""
    from sqlalchemy import text
    
    try:
        sixty_days_ago = datetime.utcnow() - timedelta(days=60)
        
        # Use SELECT * for flexibility
        rows = db.session.execute(text("""
            SELECT * FROM guest_users
            WHERE last_active < :cutoff
            ORDER BY last_active ASC
        """), {'cutoff': sixty_days_ago}).fetchall()
        
        if not rows:
            return jsonify([])
        
        result = []
        now = datetime.utcnow()
        
        for row in rows:
            # Get data using _mapping if available
            if hasattr(row, '_mapping'):
                data = dict(row._mapping)
            else:
                data = {'guest_code': row[0]}
            
            guest_code = data.get('guest_code', str(row[0]))
            last_active = data.get('last_active')
            points = data.get('total_score', 0) or 0
            
            days_inactive = 0
            if last_active:
                try:
                    days_inactive = (now - last_active).days
                except:
                    days_inactive = 999
            
            result.append({
                'type': 'Guest',
                'identifier': guest_code,
                'last_active': last_active.isoformat() if last_active else None,
                'days_inactive': days_inactive,
                'points': points
            })
        
        return jsonify(result)
    except Exception as e:
        import traceback
        print(f"Error in inactive-users: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'error': str(e), 'trace': traceback.format_exc()})


@admin_bp.route('/api/admin/analytics/user-detail')
@login_required
@role_required('admin')
def admin_analytics_user_detail():
    """Get detailed info about a specific user"""
    from sqlalchemy import text
    
    user_type = request.args.get('type')
    user_id = request.args.get('id')
    
    if user_type == 'registered':
        # Get registered user details
        user = User.query.get(user_id)
        stats = UserStats.query.filter_by(user_id=user_id).first()
        
        # Get recent activity
        recent_attempts = db.session.execute(text("""
            SELECT topic, difficulty, score, total_questions, completed_at
            FROM quiz_attempts
            WHERE user_id = :user_id
            ORDER BY completed_at DESC
            LIMIT 10
        """), {'user_id': user_id}).fetchall()
        
        recent_activity_html = '<ul>' + ''.join([
            f'<li>{att.topic} ({att.difficulty}): {att.score}/{att.total_questions} - {att.completed_at.strftime("%Y-%m-%d")}</li>'
            for att in recent_attempts
        ]) + '</ul>' if recent_attempts else '<p>No recent activity</p>'
        
        return jsonify({
            'full_name': user.full_name,
            'email': user.email,
            'role': user.role,
            'points': stats.total_points if stats else 0,
            'level': stats.level if stats else 1,
            'quizzes': stats.total_quizzes if stats else 0,
            'accuracy': round((stats.total_correct_answers / stats.total_questions_answered * 100), 1) if stats and stats.total_questions_answered > 0 else 0,
            'streak': stats.current_streak_days if stats else 0,
            'recent_activity': recent_activity_html
        })
    
    else:  # guest
        try:
            # Get guest details
            guest = db.session.execute(text("""
                SELECT 
                    guest_code,
                    total_score,
                    created_at,
                    last_active
                FROM guest_users WHERE guest_code = :code
            """), {'code': user_id}).fetchone()
            
            if not guest:
                return jsonify({'error': 'Guest not found'}), 404
            
            # Access by index: 0=guest_code, 1=total_score, 2=created_at, 3=last_active
            guest_code = guest[0]
            total_score = guest[1] if guest[1] else 0
            created_at = guest[2]
            last_active = guest[3]
            
            # Get recent quizzes
            try:
                recent_quizzes = db.session.execute(text("""
                    SELECT topic, difficulty, score, total_questions, completed_at
                    FROM guest_quiz_attempts
                    WHERE guest_code = :code
                    ORDER BY completed_at DESC
                    LIMIT 10
                """), {'code': user_id}).fetchall()
                
                recent_quizzes_html = '<ul>' + ''.join([
                    f'<li>{q[0]} ({q[1]}): {q[2]}/{q[3]}</li>'
                    for q in recent_quizzes
                ]) + '</ul>' if recent_quizzes else '<p>No quizzes yet</p>'
            except:
                recent_quizzes_html = '<p>No quiz data available</p>'
            
            now = datetime.utcnow()
            days_old = (now - created_at).days if created_at else 0
            days_inactive = (now - last_active).days if last_active else 999
            
            return jsonify({
                'guest_code': guest_code,
                'nickname': None,
                'total_score': total_score,
                'quizzes_completed': 0,
                'days_old': days_old,
                'days_inactive': days_inactive,
                'recent_quizzes': recent_quizzes_html
            })
        except Exception as e:
            import traceback
            print(f"Error in user-detail guest: {str(e)}")
            print(traceback.format_exc())
            return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/admin/analytics/recycle-guest', methods=['POST'])
@login_required
@role_required('admin')
def admin_analytics_recycle_guest():
    """Manually recycle a guest code (delete all data)"""
    from sqlalchemy import text
    
    data = request.json
    guest_code = data.get('guest_code')
    
    try:
        # Delete guest quiz attempts
        db.session.execute(text("""
            DELETE FROM guest_quiz_attempts WHERE guest_code = :code
        """), {'code': guest_code})
        
        # Delete guest badges
        try:
            db.session.execute(text("""
                DELETE FROM guest_badges WHERE guest_code = :code
            """), {'code': guest_code})
        except:
            pass  # Table might not exist
        
        # Delete guest user record
        db.session.execute(text("""
            DELETE FROM guest_users WHERE guest_code = :code
        """), {'code': guest_code})
        
        db.session.commit()
        
        return jsonify({'success': True, 'message': f'Guest code {guest_code} recycled'})
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


@admin_bp.route('/api/admin/analytics/run-cleanup', methods=['POST'])
@login_required
@role_required('admin')
def admin_analytics_run_cleanup():
    """Run cleanup process now"""
    from sqlalchemy import text
    
    # Get cleanup threshold from settings (default 60 days)
    cleanup_days = int(SystemSetting.get('cleanup_days_threshold', '60'))
    cutoff_date = datetime.utcnow() - timedelta(days=cleanup_days)
    
    # Find inactive guest codes
    inactive_codes = db.session.execute(text("""
        SELECT guest_code 
        FROM guest_users 
        WHERE last_active < :cutoff
    """), {'cutoff': cutoff_date}).fetchall()
    
    recycled_count = 0
    
    for row in inactive_codes:
        guest_code = row.guest_code
        
        try:
            # Delete all related data
            db.session.execute(text("""
                DELETE FROM guest_quiz_attempts WHERE guest_code = :code
            """), {'code': guest_code})
            
            try:
                db.session.execute(text("""
                    DELETE FROM guest_badges WHERE guest_code = :code
                """), {'code': guest_code})
            except:
                pass
            
            db.session.execute(text("""
                DELETE FROM guest_users WHERE guest_code = :code
            """), {'code': guest_code})
            
            recycled_count += 1
        except Exception as e:
            print(f"Error recycling {guest_code}: {e}")
            continue
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'recycled_count': recycled_count,
        'message': f'Recycled {recycled_count} inactive guest codes'
    })


@admin_bp.route('/api/admin/analytics/cleanup-settings', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def admin_analytics_cleanup_settings():
    """Get or update cleanup settings"""
    
    if request.method == 'GET':
        return jsonify({
            'days_threshold': int(SystemSetting.get('cleanup_days_threshold', '60')),
            'auto_enabled': SystemSetting.get('auto_cleanup_enabled', 'false') == 'true'
        })
    
    else:  # POST
        data = request.json
        user_id = session.get('user_id')
        
        SystemSetting.set(
            'cleanup_days_threshold',
            str(data.get('days_threshold', 60)),
            'Days of inactivity before guest code cleanup',
            user_id
        )
        
        SystemSetting.set(
            'auto_cleanup_enabled',
            'true' if data.get('auto_enabled') else 'false',
            'Enable automatic daily cleanup',
            user_id
        )
        
        return jsonify({'success': True})


# =============================================================================
# SITE SETTINGS API (Admin)
# =============================================================================

@admin_bp.route('/api/admin/site-settings')
@login_required
@role_required('admin')
def admin_get_site_settings():
    """Get all site settings for admin dashboard"""
    return jsonify({
        'full_account_login_enabled': SystemSetting.get('FULL_ACCOUNT_LOGIN_ENABLED', False) in [True, 'true', 'True'],
        'cleanup_days_threshold': int(SystemSetting.get('cleanup_days_threshold', '60')),
        'auto_cleanup_enabled': SystemSetting.get('auto_cleanup_enabled', 'false') == 'true',
        'prize_pin_threshold': int(SystemSetting.get('prize_pin_threshold', '2000'))
    })


@admin_bp.route('/api/admin/site-settings/full-account-login', methods=['POST'])
@login_required
@role_required('admin')
def admin_toggle_full_account_login():
    """Toggle full account login visibility"""
    data = request.json or {}
    enabled = data.get('enabled', False)
    user_id = session.get('user_id')
    
    SystemSetting.set(
        'FULL_ACCOUNT_LOGIN_ENABLED',
        'true' if enabled else 'false',
        'Enable full account login on the login page (GDPR compliance)',
        user_id
    )
    
    return jsonify({
        'success': True,
        'enabled': enabled,
        'message': f'Full account login {"enabled" if enabled else "disabled"}'
    })


@admin_bp.route('/api/admin/site-settings/prize-pin-threshold', methods=['POST'])
@login_required
@role_required('admin')
def admin_set_prize_pin_threshold():
    """Set the points threshold for Prize Shop PIN protection"""
    data = request.json or {}
    threshold = int(data.get('threshold', 2000))
    user_id = session.get('user_id')
    
    # Validate threshold (minimum 500, maximum 10000)
    threshold = max(500, min(10000, threshold))
    
    SystemSetting.set(
        'prize_pin_threshold',
        str(threshold),
        'Points threshold for Prize Shop PIN protection',
        user_id
    )
    
    return jsonify({
        'success': True,
        'threshold': threshold,
        'message': f'Prize PIN threshold set to {threshold} points'
    })


# =============================================================================
# ADDITIONAL RESOURCES API
# =============================================================================

@admin_bp.route('/api/resources')
def get_resources():
    """Get all active resources for student display"""
    from sqlalchemy import text
    
    try:
        result = db.session.execute(text("""
            SELECT id, button_text, link_url, popup_text, image_filename, display_order, category
            FROM additional_resources
            WHERE is_active = 1
            ORDER BY display_order, id
        """)).fetchall()
        
        resources = []
        for row in result:
            image_url = None
            if row[4]:
                image_url = f'/static/resources/{row[4]}'
            
            resources.append({
                'id': row[0],
                'button_text': row[1],
                'link_url': row[2],
                'popup_text': row[3],
                'image_url': image_url,
                'display_order': row[5],
                'category': row[6]
            })
        
        return jsonify({'resources': resources})
    except Exception as e:
        print(f"Error loading resources: {e}")
        return jsonify({'resources': []})


@admin_bp.route('/api/admin/resources')
@login_required
@role_required('admin')
def admin_get_resources():
    """Get all resources for admin management"""
    from sqlalchemy import text
    
    try:
        result = db.session.execute(text("""
            SELECT id, button_text, link_url, popup_text, image_filename, 
                   display_order, is_active, created_at, updated_at, category
            FROM additional_resources
            ORDER BY display_order, id
        """)).fetchall()
        
        resources = []
        for row in result:
            image_url = None
            if row[4]:
                image_url = f'/static/resources/{row[4]}'
            
            resources.append({
                'id': row[0],
                'button_text': row[1],
                'link_url': row[2],
                'popup_text': row[3],
                'image_filename': row[4],
                'image_url': image_url,
                'display_order': row[5],
                'is_active': bool(row[6]),
                'created_at': row[7],
                'updated_at': row[8],
                'category': row[9]
            })
        
        return jsonify({'resources': resources})
    except Exception as e:
        print(f"Error loading admin resources: {e}")
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/admin/resources', methods=['POST'])
@login_required
@role_required('admin')
def admin_add_resource():
    """Add a new external resource"""
    from sqlalchemy import text
    import os
    from werkzeug.utils import secure_filename
    
    try:
        button_text = request.form.get('button_text', '').strip()
        link_url = request.form.get('link_url', '').strip()
        popup_text = request.form.get('popup_text', '').strip()
        category = request.form.get('category', '').strip()
        display_order = request.form.get('display_order', '1').strip()
        
        if not button_text or not link_url:
            return jsonify({'error': 'Button text and link URL are required'}), 400
        
        # Handle image upload
        image_filename = None
        if 'image' in request.files:
            file = request.files['image']
            if file.filename:
                # Create resources directory if it doesn't exist
                resources_dir = os.path.join(app.static_folder, 'resources')
                os.makedirs(resources_dir, exist_ok=True)
                
                # Generate unique filename
                ext = os.path.splitext(file.filename)[1].lower()
                safe_name = secure_filename(button_text.lower().replace(' ', '_'))
                image_filename = f"{safe_name}_{int(datetime.now().timestamp())}{ext}"
                
                # Save file
                file.save(os.path.join(resources_dir, image_filename))
        
        # Use provided display_order or get next available
        try:
            display_order = int(display_order)
        except:
            result = db.session.execute(text(
                "SELECT COALESCE(MAX(display_order), 0) + 1 FROM additional_resources"
            )).fetchone()
            display_order = result[0]
        
        # Insert resource
        user_id = session.get('user_id')
        db.session.execute(text("""
            INSERT INTO additional_resources 
            (button_text, link_url, popup_text, image_filename, display_order, is_active, created_by, category)
            VALUES (:button_text, :link_url, :popup_text, :image_filename, :display_order, 1, :created_by, :category)
        """), {
            'button_text': button_text,
            'link_url': link_url,
            'popup_text': popup_text,
            'image_filename': image_filename,
            'display_order': display_order,
            'created_by': user_id,
            'category': category
        })
        
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Resource added successfully'})
        
    except Exception as e:
        print(f"Error adding resource: {e}")
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/admin/resources/<int:resource_id>', methods=['PUT'])
@login_required
@role_required('admin')
def admin_update_resource(resource_id):
    """Update an existing resource"""
    from sqlalchemy import text
    import os
    from werkzeug.utils import secure_filename
    
    try:
        button_text = request.form.get('button_text', '').strip()
        link_url = request.form.get('link_url', '').strip()
        popup_text = request.form.get('popup_text', '').strip()
        category = request.form.get('category', '').strip()
        display_order = request.form.get('display_order', '1').strip()
        
        if not button_text or not link_url:
            return jsonify({'error': 'Button text and link URL are required'}), 400
        
        # Parse display_order
        try:
            display_order = int(display_order)
        except:
            display_order = 1
        
        # Check if resource exists
        existing = db.session.execute(text(
            "SELECT image_filename FROM additional_resources WHERE id = :id"
        ), {'id': resource_id}).fetchone()
        
        if not existing:
            return jsonify({'error': 'Resource not found'}), 404
        
        # Handle image upload
        image_filename = existing[0]  # Keep existing image by default
        if 'image' in request.files:
            file = request.files['image']
            if file.filename:
                # Create resources directory if it doesn't exist
                resources_dir = os.path.join(app.static_folder, 'resources')
                os.makedirs(resources_dir, exist_ok=True)
                
                # Delete old image if exists
                if image_filename:
                    old_path = os.path.join(resources_dir, image_filename)
                    if os.path.exists(old_path):
                        os.remove(old_path)
                
                # Generate unique filename
                ext = os.path.splitext(file.filename)[1].lower()
                safe_name = secure_filename(button_text.lower().replace(' ', '_'))
                image_filename = f"{safe_name}_{int(datetime.now().timestamp())}{ext}"
                
                # Save file
                file.save(os.path.join(resources_dir, image_filename))
        
        # Update resource
        db.session.execute(text("""
            UPDATE additional_resources 
            SET button_text = :button_text, 
                link_url = :link_url, 
                popup_text = :popup_text,
                image_filename = :image_filename,
                category = :category,
                display_order = :display_order,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = :id
        """), {
            'button_text': button_text,
            'link_url': link_url,
            'popup_text': popup_text,
            'image_filename': image_filename,
            'category': category,
            'display_order': display_order,
            'id': resource_id
        })
        
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Resource updated successfully'})
        
    except Exception as e:
        print(f"Error updating resource: {e}")
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/admin/resources/<int:resource_id>/toggle', methods=['POST'])
@login_required
@role_required('admin')
def admin_toggle_resource(resource_id):
    """Toggle resource active status"""
    from sqlalchemy import text
    
    try:
        db.session.execute(text("""
            UPDATE additional_resources 
            SET is_active = CASE WHEN is_active = 1 THEN 0 ELSE 1 END,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = :id
        """), {'id': resource_id})
        
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Resource status toggled'})
        
    except Exception as e:
        print(f"Error toggling resource: {e}")
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/admin/resources/<int:resource_id>', methods=['DELETE'])
@login_required
@role_required('admin')
def admin_delete_resource(resource_id):
    """Delete a resource"""
    from sqlalchemy import text
    import os
    
    try:
        # Get image filename before deletion
        result = db.session.execute(text(
            "SELECT image_filename FROM additional_resources WHERE id = :id"
        ), {'id': resource_id}).fetchone()
        
        if result and result[0]:
            # Delete image file
            image_path = os.path.join(app.static_folder, 'resources', result[0])
            if os.path.exists(image_path):
                os.remove(image_path)
        
        # Delete resource
        db.session.execute(text(
            "DELETE FROM additional_resources WHERE id = :id"
        ), {'id': resource_id})
        
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Resource deleted successfully'})
        
    except Exception as e:
        print(f"Error deleting resource: {e}")
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# =============================================================================
# PUZZLE OF THE WEEK - ADMIN API ROUTES
# =============================================================================

@admin_bp.route('/api/admin/puzzles')
@login_required
@role_required('admin')
def admin_list_puzzles():
    """List all puzzles"""
    from sqlalchemy import text
    
    try:
        # First, ensure tables exist
        try:
            db.session.execute(text("SELECT 1 FROM weekly_puzzles LIMIT 1"))
        except Exception as table_error:
            print(f"Puzzle tables don't exist, creating them...")
            # Create tables
            db.session.execute(text("""
                CREATE TABLE IF NOT EXISTS weekly_puzzles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title VARCHAR(200) NOT NULL,
                    description TEXT,
                    puzzle_type VARCHAR(20) DEFAULT 'image',
                    puzzle_image VARCHAR(500),
                    puzzle_text TEXT,
                    answer_image VARCHAR(500),
                    answer_text TEXT,
                    hint TEXT,
                    week_number INTEGER NOT NULL,
                    year INTEGER NOT NULL,
                    is_active BOOLEAN DEFAULT 0,
                    view_count INTEGER DEFAULT 0,
                    reveal_count INTEGER DEFAULT 0,
                    hint_view_count INTEGER DEFAULT 0,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    created_by INTEGER,
                    UNIQUE(week_number, year)
                )
            """))
            db.session.execute(text("""
                CREATE TABLE IF NOT EXISTS puzzle_user_status (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    puzzle_id INTEGER NOT NULL,
                    user_id INTEGER,
                    guest_code VARCHAR(20),
                    session_id VARCHAR(100),
                    dismissed_popup BOOLEAN DEFAULT 0,
                    dismissed_answer BOOLEAN DEFAULT 0,
                    revealed_answer BOOLEAN DEFAULT 0,
                    hint_viewed BOOLEAN DEFAULT 0,
                    view_count INTEGER DEFAULT 1,
                    first_viewed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    answer_revealed_at DATETIME,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (puzzle_id) REFERENCES weekly_puzzles(id)
                )
            """))
            db.session.commit()
            print("Puzzle tables created successfully!")
        
        puzzles = WeeklyPuzzle.query.order_by(
            WeeklyPuzzle.year.desc(),
            WeeklyPuzzle.week_number.desc()
        ).all()
        
        current_week, current_year = get_current_week_year()
        
        return jsonify({
            'puzzles': [p.to_dict(include_answer=True) for p in puzzles],
            'current_week': current_week,
            'current_year': current_year
        })
    except Exception as e:
        import traceback
        error_msg = str(e)
        print(f"ERROR listing puzzles: {error_msg}")
        print(traceback.format_exc())
        
        # If table doesn't exist, return empty with week info
        current_week, current_year = get_current_week_year()
        return jsonify({
            'puzzles': [],
            'current_week': current_week,
            'current_year': current_year,
            'error': error_msg
        })


@admin_bp.route('/api/admin/puzzles', methods=['POST'])
@login_required
@role_required('admin')
def admin_create_puzzle():
    """Create a new puzzle"""
    try:
        data = request.get_json() or {}
        
        print(f"DEBUG: Creating puzzle with data: {data}")
        
        # Validate required fields
        if not data.get('title'):
            return jsonify({'success': False, 'error': 'Title is required'}), 400
        if not data.get('week_number') or not data.get('year'):
            return jsonify({'success': False, 'error': 'Week and year are required'}), 400
        
        # Check for existing puzzle in that week
        existing = WeeklyPuzzle.query.filter_by(
            week_number=data['week_number'],
            year=data['year']
        ).first()
        
        if existing:
            return jsonify({
                'success': False, 
                'error': f'Puzzle already exists for Week {data["week_number"]}, {data["year"]}'
            }), 400
        
        puzzle = WeeklyPuzzle(
            title=data['title'],
            description=data.get('description'),
            puzzle_type=data.get('puzzle_type', 'image'),
            puzzle_image=data.get('puzzle_image'),
            puzzle_text=data.get('puzzle_text'),
            answer_image=data.get('answer_image'),
            answer_text=data.get('answer_text'),
            hint=data.get('hint'),
            week_number=data['week_number'],
            year=data['year'],
            is_active=data.get('is_active', False),
            created_by=session.get('user_id')
        )
        
        db.session.add(puzzle)
        db.session.commit()
        
        print(f"DEBUG: Puzzle created with ID: {puzzle.id}")
        
        return jsonify({
            'success': True,
            'puzzle': puzzle.to_dict(include_answer=True)
        })
    except Exception as e:
        import traceback
        error_msg = str(e)
        trace = traceback.format_exc()
        print(f"ERROR creating puzzle: {error_msg}")
        print(trace)
        db.session.rollback()
        return jsonify({'success': False, 'error': error_msg}), 500


@admin_bp.route('/api/admin/puzzles/<int:puzzle_id>', methods=['PUT'])
@login_required
@role_required('admin')
def admin_update_puzzle(puzzle_id):
    """Update an existing puzzle"""
    puzzle = WeeklyPuzzle.query.get_or_404(puzzle_id)
    data = request.get_json() or {}
    
    # Update fields
    if 'title' in data:
        puzzle.title = data['title']
    if 'description' in data:
        puzzle.description = data['description']
    if 'puzzle_type' in data:
        puzzle.puzzle_type = data['puzzle_type']
    if 'puzzle_image' in data:
        puzzle.puzzle_image = data['puzzle_image']
    if 'puzzle_text' in data:
        puzzle.puzzle_text = data['puzzle_text']
    if 'answer_image' in data:
        puzzle.answer_image = data['answer_image']
    if 'answer_text' in data:
        puzzle.answer_text = data['answer_text']
    if 'hint' in data:
        puzzle.hint = data['hint']
    if 'is_active' in data:
        puzzle.is_active = data['is_active']
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'puzzle': puzzle.to_dict(include_answer=True)
    })


@admin_bp.route('/api/admin/puzzles/<int:puzzle_id>', methods=['DELETE'])
@login_required
@role_required('admin')
def admin_delete_puzzle(puzzle_id):
    """Delete a puzzle"""
    puzzle = WeeklyPuzzle.query.get_or_404(puzzle_id)
    
    # Delete associated user statuses first
    PuzzleUserStatus.query.filter_by(puzzle_id=puzzle_id).delete()
    
    db.session.delete(puzzle)
    db.session.commit()
    
    return jsonify({'success': True})


@admin_bp.route('/api/admin/puzzles/<int:puzzle_id>/activate', methods=['POST'])
@login_required
@role_required('admin')
def admin_activate_puzzle(puzzle_id):
    """Activate a puzzle (deactivate others for same week)"""
    puzzle = WeeklyPuzzle.query.get_or_404(puzzle_id)
    
    # Deactivate any other puzzles for the same week
    WeeklyPuzzle.query.filter_by(
        week_number=puzzle.week_number,
        year=puzzle.year
    ).update({'is_active': False})
    
    # Activate this one
    puzzle.is_active = True
    db.session.commit()
    
    return jsonify({
        'success': True,
        'puzzle': puzzle.to_dict(include_answer=True)
    })


@admin_bp.route('/api/admin/puzzles/<int:puzzle_id>/deactivate', methods=['POST'])
@login_required
@role_required('admin')
def admin_deactivate_puzzle(puzzle_id):
    """Deactivate a puzzle"""
    puzzle = WeeklyPuzzle.query.get_or_404(puzzle_id)
    puzzle.is_active = False
    db.session.commit()
    
    return jsonify({
        'success': True,
        'puzzle': puzzle.to_dict(include_answer=True)
    })


@admin_bp.route('/api/admin/puzzles/<int:puzzle_id>/stats')
@login_required
@role_required('admin')
def admin_puzzle_stats(puzzle_id):
    """Get detailed stats for a puzzle"""
    puzzle = WeeklyPuzzle.query.get_or_404(puzzle_id)
    
    from sqlalchemy import func, case
    
    # Get stats from puzzle_user_status
    stats = db.session.query(
        func.count(PuzzleUserStatus.id).label('total_users'),
        func.sum(case((PuzzleUserStatus.revealed_answer == True, 1), else_=0)).label('reveals'),
        func.sum(case((PuzzleUserStatus.hint_viewed == True, 1), else_=0)).label('hints_viewed'),
        func.sum(case((PuzzleUserStatus.dismissed_popup == True, 1), else_=0)).label('dismissed')
    ).filter_by(puzzle_id=puzzle_id).first()
    
    return jsonify({
        'puzzle_id': puzzle_id,
        'title': puzzle.title,
        'week_number': puzzle.week_number,
        'year': puzzle.year,
        'is_active': puzzle.is_active,
        'view_count': puzzle.view_count,
        'reveal_count': puzzle.reveal_count,
        'hint_view_count': puzzle.hint_view_count,
        'unique_users': stats.total_users or 0,
        'answer_reveals': int(stats.reveals or 0),
        'hints_viewed': int(stats.hints_viewed or 0),
        'popup_dismissed': int(stats.dismissed or 0)
    })


@admin_bp.route('/api/admin/puzzles/upload-image', methods=['POST'])
@login_required
@role_required('admin')
def admin_upload_puzzle_image():
    """Upload a puzzle or answer image (800x600)"""
    import os
    from werkzeug.utils import secure_filename
    
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No file selected'}), 400
    
    # Validate file type
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    ext = file.filename.rsplit('.', 1)[1].lower() if '.' in file.filename else ''
    if ext not in allowed_extensions:
        return jsonify({'success': False, 'error': 'Invalid file type. Use PNG, JPG, GIF, or WEBP'}), 400
    
    # Create puzzles directory if needed
    upload_dir = os.path.join(app.static_folder, 'puzzles')
    os.makedirs(upload_dir, exist_ok=True)
    
    # Generate unique filename
    timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    image_type = request.form.get('type', 'puzzle')  # 'puzzle' or 'answer'
    filename = secure_filename(f"{image_type}_{timestamp}.{ext}")
    filepath = os.path.join(upload_dir, filename)
    
    # Save file
    file.save(filepath)
    
    # Return the URL path
    url_path = f"/static/puzzles/{filename}"
    
    return jsonify({
        'success': True,
        'path': url_path,
        'filename': filename
    })


# =============================================================================
# QUESTION IMAGE UPLOAD API
# =============================================================================

@admin_bp.route('/api/admin/questions/upload-image', methods=['POST'])
@login_required
@role_required('admin')
def admin_upload_question_image():
    """Upload an image for a question"""
    import os
    from werkzeug.utils import secure_filename
    
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No file selected'}), 400
    
    # Validate file type
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'svg'}
    ext = file.filename.rsplit('.', 1)[1].lower() if '.' in file.filename else ''
    if ext not in allowed_extensions:
        return jsonify({'success': False, 'error': 'Invalid file type. Use PNG, JPG, GIF, WEBP, or SVG'}), 400
    
    # Check file size (max 2MB)
    file.seek(0, 2)  # Seek to end
    size = file.tell()
    file.seek(0)  # Reset to beginning
    if size > 2 * 1024 * 1024:
        return jsonify({'success': False, 'error': 'File too large. Maximum 2MB'}), 400
    
    # Create question_images directory if needed
    upload_dir = os.path.join(app.static_folder, 'question_images')
    os.makedirs(upload_dir, exist_ok=True)
    
    # Generate unique filename
    timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    question_id = request.form.get('question_id', 'new')
    topic = request.form.get('topic', 'general')
    filename = secure_filename(f"q_{topic}_{question_id}_{timestamp}.{ext}")
    filepath = os.path.join(upload_dir, filename)
    
    # Save file
    file.save(filepath)
    
    # Return the URL path
    url_path = f"/static/question_images/{filename}"
    
    return jsonify({
        'success': True,
        'path': url_path,
        'filename': filename
    })


@admin_bp.route('/api/admin/questions/delete-image', methods=['POST'])
@login_required
@role_required('admin')
def admin_delete_question_image():
    """Delete a question image file"""
    import os
    
    data = request.json or {}
    image_path = data.get('image_path', '')
    
    if not image_path or not image_path.startswith('/static/question_images/'):
        return jsonify({'success': False, 'error': 'Invalid image path'}), 400
    
    # Get filename from path
    filename = image_path.replace('/static/question_images/', '')
    filepath = os.path.join(app.static_folder, 'question_images', filename)
    
    # Delete file if it exists
    if os.path.exists(filepath):
        os.remove(filepath)
        return jsonify({'success': True, 'message': 'Image deleted'})
    else:
        return jsonify({'success': False, 'error': 'Image not found'}), 404

# =====================================================
# EMAIL REPORTS SYSTEM
# =====================================================

def get_report_setting(key, default=None):
    """Get a report setting from the database"""
    from sqlalchemy import text
    try:
        result = db.session.execute(text("""
            SELECT setting_value FROM report_settings WHERE setting_key = :key
        """), {'key': key}).fetchone()
        return result[0] if result else default
    except:
        return default

def set_report_setting(key, value):
    """Set a report setting in the database"""
    from sqlalchemy import text
    try:
        db.session.execute(text("""
            INSERT INTO report_settings (setting_key, setting_value, updated_at)
            VALUES (:key, :value, CURRENT_TIMESTAMP)
            ON CONFLICT(setting_key) DO UPDATE SET
                setting_value = :value,
                updated_at = CURRENT_TIMESTAMP
        """), {'key': key, 'value': value})
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print(f"Error setting report setting: {e}")
        return False


@admin_bp.route('/api/admin/email-reports/distribution-list', methods=['GET'])
@login_required
@role_required('admin')
def get_distribution_list():
    """Get all email report recipients"""
    from sqlalchemy import text
    
    try:
        recipients = db.session.execute(text("""
            SELECT id, email, recipient_name, report_type, is_active, created_at
            FROM email_distribution_list
            ORDER BY recipient_name, email, report_type
        """)).fetchall()
        
        return jsonify({
            'recipients': [{
                'id': r[0],
                'email': r[1],
                'recipient_name': r[2],
                'report_type': r[3],
                'is_active': r[4],
                'created_at': str(r[5]) if r[5] else None
            } for r in recipients]
        })
    except Exception as e:
        print(f"Error getting distribution list: {e}")
        return jsonify({'recipients': []})


@admin_bp.route('/api/admin/email-reports/distribution-list', methods=['POST'])
@login_required
@role_required('admin')
def add_distribution_recipient():
    """Add a recipient to the distribution list"""
    from sqlalchemy import text
    
    data = request.json
    email = data.get('email', '').strip().lower()
    name = data.get('recipient_name', '').strip()
    daily = data.get('daily', False)
    weekly = data.get('weekly', False)
    monthly = data.get('monthly', False)
    
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    
    try:
        # Add entries for each selected report type
        report_types = []
        if daily:
            report_types.append('daily')
        if weekly:
            report_types.append('weekly')
        if monthly:
            report_types.append('monthly')
        
        for report_type in report_types:
            db.session.execute(text("""
                INSERT INTO email_distribution_list (email, recipient_name, report_type, is_active, created_by)
                VALUES (:email, :name, :report_type, 1, :created_by)
                ON CONFLICT(email, report_type) DO UPDATE SET
                    recipient_name = :name,
                    is_active = 1
            """), {
                'email': email,
                'name': name,
                'report_type': report_type,
                'created_by': session.get('user_id')
            })
        
        db.session.commit()
        return jsonify({'success': True, 'message': 'Recipient added'})
        
    except Exception as e:
        db.session.rollback()
        print(f"Error adding recipient: {e}")
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/admin/email-reports/distribution-list', methods=['DELETE'])
@login_required
@role_required('admin')
def delete_distribution_recipient():
    """Remove a recipient from all distribution lists"""
    from sqlalchemy import text
    
    data = request.json
    email = data.get('email', '').strip().lower()
    
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    
    try:
        db.session.execute(text("""
            DELETE FROM email_distribution_list WHERE email = :email
        """), {'email': email})
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/admin/email-reports/distribution-list/toggle', methods=['POST'])
@login_required
@role_required('admin')
def toggle_distribution_recipient():
    """Toggle active status for a recipient"""
    from sqlalchemy import text
    
    data = request.json
    email = data.get('email', '').strip().lower()
    
    try:
        db.session.execute(text("""
            UPDATE email_distribution_list 
            SET is_active = CASE WHEN is_active = 1 THEN 0 ELSE 1 END
            WHERE email = :email
        """), {'email': email})
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/admin/email-reports/settings', methods=['GET'])
@login_required
@role_required('admin')
def get_report_settings():
    """Get all report settings"""
    from sqlalchemy import text
    
    try:
        settings = db.session.execute(text("""
            SELECT setting_key, setting_value FROM report_settings
        """)).fetchall()
        
        return jsonify({row[0]: row[1] for row in settings})
    except:
        return jsonify({})


@admin_bp.route('/api/admin/email-reports/settings', methods=['POST'])
@login_required
@role_required('admin')
def save_report_settings():
    """Save report settings"""
    data = request.json
    
    for key, value in data.items():
        set_report_setting(key, value)
    
    return jsonify({'success': True})


@admin_bp.route('/api/admin/email-reports/history', methods=['GET'])
@login_required
@role_required('admin')
def get_report_history():
    """Get recent report send history"""
    from sqlalchemy import text
    
    try:
        history = db.session.execute(text("""
            SELECT id, report_type, report_date, recipients_count, sent_at, status
            FROM report_history
            ORDER BY sent_at DESC
            LIMIT 20
        """)).fetchall()
        
        return jsonify({
            'history': [{
                'id': h[0],
                'report_type': h[1],
                'report_date': str(h[2]) if h[2] else None,
                'recipients_count': h[3],
                'sent_at': str(h[4]) if h[4] else None,
                'status': h[5]
            } for h in history]
        })
    except:
        return jsonify({'history': []})


def generate_daily_report_data():
    """Generate data for the daily report"""
    from sqlalchemy import text
    from datetime import timedelta
    
    today = datetime.utcnow().date()
    yesterday = today - timedelta(days=1)
    two_days_ago = today - timedelta(days=2)
    
    report_data = {
        'report_date': str(yesterday),
        'generated_at': datetime.utcnow().isoformat(),
        'active_users': 0,
        'active_users_change': 0,
        'questions_answered': 0,
        'questions_change': 0,
        'points_earned': 0,
        'points_change': 0,
        'new_registrations': 0,
        'registrations_change': 0,
        'total_points_circulation': 0,
        'guest_users_active': 0,
        'teachers_active': 0,
        'badges_earned': 0,
        'popular_topic': 'N/A',
        'pending_teachers': 0,
        'inactive_students': 0
    }
    
    try:
        # Active users yesterday (from user_question_history using seen_at)
        try:
            active_users = db.session.execute(text("""
                SELECT COUNT(DISTINCT COALESCE(user_id, guest_code)) 
                FROM user_question_history 
                WHERE DATE(seen_at) = :date
            """), {'date': yesterday}).scalar() or 0
            
            prev_active = db.session.execute(text("""
                SELECT COUNT(DISTINCT COALESCE(user_id, guest_code)) 
                FROM user_question_history 
                WHERE DATE(seen_at) = :date
            """), {'date': two_days_ago}).scalar() or 0
            
            report_data['active_users'] = active_users
            report_data['active_users_change'] = active_users - prev_active
        except Exception as e:
            print(f"Error getting active users: {e}")
        
        # Questions seen yesterday
        try:
            questions_answered = db.session.execute(text("""
                SELECT COUNT(*) FROM user_question_history 
                WHERE DATE(seen_at) = :date
            """), {'date': yesterday}).scalar() or 0
            
            prev_questions = db.session.execute(text("""
                SELECT COUNT(*) FROM user_question_history 
                WHERE DATE(seen_at) = :date
            """), {'date': two_days_ago}).scalar() or 0
            
            report_data['questions_answered'] = questions_answered
            report_data['questions_change'] = questions_answered - prev_questions
        except Exception as e:
            print(f"Error getting questions answered: {e}")
        
        # Points earned yesterday (from quiz_attempts)
        try:
            points_earned = db.session.execute(text("""
                SELECT COALESCE(SUM(score), 0) FROM quiz_attempts 
                WHERE DATE(completed_at) = :date
            """), {'date': yesterday}).scalar() or 0
            
            prev_points = db.session.execute(text("""
                SELECT COALESCE(SUM(score), 0) FROM quiz_attempts 
                WHERE DATE(completed_at) = :date
            """), {'date': two_days_ago}).scalar() or 0
            
            report_data['points_earned'] = points_earned
            report_data['points_change'] = points_earned - prev_points
        except Exception as e:
            print(f"Error getting points earned: {e}")
        
        # New registrations yesterday
        try:
            new_registrations = db.session.execute(text("""
                SELECT COUNT(*) FROM users 
                WHERE DATE(created_at) = :date AND role = 'student'
            """), {'date': yesterday}).scalar() or 0
            
            prev_registrations = db.session.execute(text("""
                SELECT COUNT(*) FROM users 
                WHERE DATE(created_at) = :date AND role = 'student'
            """), {'date': two_days_ago}).scalar() or 0
            
            report_data['new_registrations'] = new_registrations
            report_data['registrations_change'] = new_registrations - prev_registrations
        except Exception as e:
            print(f"Error getting registrations: {e}")
        
        # Total points in circulation (from user_stats + guest_users)
        try:
            registered_points = db.session.execute(text("""
                SELECT COALESCE(SUM(total_points), 0) FROM user_stats
            """)).scalar() or 0
            
            guest_points = db.session.execute(text("""
                SELECT COALESCE(SUM(total_score), 0) FROM guest_users
            """)).scalar() or 0
            
            report_data['total_points_circulation'] = registered_points + guest_points
        except Exception as e:
            print(f"Error getting total points: {e}")
        
        # Guest users active yesterday
        try:
            guest_active = db.session.execute(text("""
                SELECT COUNT(*) FROM guest_users 
                WHERE DATE(last_active) = :date
            """), {'date': yesterday}).scalar() or 0
            report_data['guest_users_active'] = guest_active
        except Exception as e:
            print(f"Error getting guest active: {e}")
        
        # Teachers count (no last_login column, so just count approved teachers)
        try:
            teachers_active = db.session.execute(text("""
                SELECT COUNT(*) FROM users 
                WHERE role = 'teacher' AND is_approved = 1
            """)).scalar() or 0
            report_data['teachers_active'] = teachers_active
        except Exception as e:
            print(f"Error getting teachers count: {e}")
        
        # Badges earned yesterday
        try:
            badges_earned = db.session.execute(text("""
                SELECT COUNT(*) FROM user_badges 
                WHERE DATE(earned_at) = :date
            """), {'date': yesterday}).scalar() or 0
            report_data['badges_earned'] = badges_earned
        except Exception as e:
            print(f"Error getting badges: {e}")
        
        # Most popular topic yesterday
        try:
            popular_topic = db.session.execute(text("""
                SELECT topic, COUNT(*) as cnt FROM user_question_history 
                WHERE DATE(seen_at) = :date AND topic IS NOT NULL
                GROUP BY topic ORDER BY cnt DESC LIMIT 1
            """), {'date': yesterday}).fetchone()
            report_data['popular_topic'] = popular_topic[0] if popular_topic else 'N/A'
        except Exception as e:
            print(f"Error getting popular topic: {e}")
        
        # Pending teacher approvals
        try:
            pending_teachers = db.session.execute(text("""
                SELECT COUNT(*) FROM users 
                WHERE role = 'teacher' AND is_approved = 0
            """)).scalar() or 0
            report_data['pending_teachers'] = pending_teachers
        except Exception as e:
            print(f"Error getting pending teachers: {e}")
        
        # Inactive converted students (7+ days)
        try:
            inactive_students = db.session.execute(text("""
                SELECT COUNT(*) FROM guest_users 
                WHERE user_id IS NOT NULL 
                AND (last_active IS NULL OR DATE(last_active) < :cutoff)
            """), {'cutoff': today - timedelta(days=7)}).scalar() or 0
            report_data['inactive_students'] = inactive_students
        except Exception as e:
            print(f"Error getting inactive students: {e}")
        
    except Exception as e:
        print(f"Error generating daily report data: {e}")
        import traceback
        traceback.print_exc()
    
    return report_data


def generate_daily_report_html(report_data):
    """Generate HTML email for daily report"""
    
    school_name = get_report_setting('school_name', 'AgentMath')
    
    def format_change(value):
        if value > 0:
            return f'<span style="color: #22c55e;">▲ +{value}</span>'
        elif value < 0:
            return f'<span style="color: #ef4444;">▼ {value}</span>'
        else:
            return '<span style="color: #6b7280;">–</span>'
    
    html = f'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background-color: #f3f4f6;">
    <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
        <!-- Header -->
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px 12px 0 0; padding: 30px; text-align: center;">
            <h1 style="margin: 0; color: white; font-size: 28px;">📊 Daily Pulse Report</h1>
            <p style="margin: 10px 0 0 0; color: rgba(255,255,255,0.9); font-size: 16px;">{school_name}</p>
            <p style="margin: 5px 0 0 0; color: rgba(255,255,255,0.7); font-size: 14px;">{report_data.get('report_date', 'Yesterday')}</p>
        </div>
        
        <!-- Main Content -->
        <div style="background: white; padding: 30px; border-radius: 0 0 12px 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            
            <!-- Key Metrics Grid -->
            <h2 style="margin: 0 0 20px 0; font-size: 18px; color: #374151;">📈 Yesterday at a Glance</h2>
            
            <table style="width: 100%; border-collapse: collapse; margin-bottom: 30px;">
                <tr>
                    <td style="padding: 15px; background: #f0f9ff; border-radius: 8px; text-align: center; width: 50%;">
                        <div style="font-size: 32px; font-weight: bold; color: #3b82f6;">{report_data.get('active_users', 0)}</div>
                        <div style="font-size: 14px; color: #6b7280;">Active Users</div>
                        <div style="font-size: 12px; margin-top: 5px;">{format_change(report_data.get('active_users_change', 0))}</div>
                    </td>
                    <td style="width: 10px;"></td>
                    <td style="padding: 15px; background: #f0fdf4; border-radius: 8px; text-align: center; width: 50%;">
                        <div style="font-size: 32px; font-weight: bold; color: #22c55e;">{report_data.get('questions_answered', 0):,}</div>
                        <div style="font-size: 14px; color: #6b7280;">Questions Answered</div>
                        <div style="font-size: 12px; margin-top: 5px;">{format_change(report_data.get('questions_change', 0))}</div>
                    </td>
                </tr>
                <tr><td colspan="3" style="height: 10px;"></td></tr>
                <tr>
                    <td style="padding: 15px; background: #fefce8; border-radius: 8px; text-align: center;">
                        <div style="font-size: 32px; font-weight: bold; color: #eab308;">{report_data.get('points_earned', 0):,}</div>
                        <div style="font-size: 14px; color: #6b7280;">Points Earned</div>
                        <div style="font-size: 12px; margin-top: 5px;">{format_change(report_data.get('points_change', 0))}</div>
                    </td>
                    <td style="width: 10px;"></td>
                    <td style="padding: 15px; background: #fdf4ff; border-radius: 8px; text-align: center;">
                        <div style="font-size: 32px; font-weight: bold; color: #a855f7;">{report_data.get('new_registrations', 0)}</div>
                        <div style="font-size: 14px; color: #6b7280;">New Registrations</div>
                        <div style="font-size: 12px; margin-top: 5px;">{format_change(report_data.get('registrations_change', 0))}</div>
                    </td>
                </tr>
            </table>
            
            <!-- User Activity Section -->
            <h2 style="margin: 30px 0 15px 0; font-size: 18px; color: #374151;">👥 User Activity</h2>
            <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 10px 0; color: #6b7280;">Guest users active</td>
                    <td style="padding: 10px 0; text-align: right; font-weight: 600;">{report_data.get('guest_users_active', 0)}</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 10px 0; color: #6b7280;">Approved teachers</td>
                    <td style="padding: 10px 0; text-align: right; font-weight: 600;">{report_data.get('teachers_active', 0)}</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 10px 0; color: #6b7280;">Badges earned</td>
                    <td style="padding: 10px 0; text-align: right; font-weight: 600;">{report_data.get('badges_earned', 0)}</td>
                </tr>
                <tr>
                    <td style="padding: 10px 0; color: #6b7280;">Most popular topic</td>
                    <td style="padding: 10px 0; text-align: right; font-weight: 600;">{report_data.get('popular_topic', 'N/A')}</td>
                </tr>
            </table>
            
            <!-- Points Economy Section -->
            <h2 style="margin: 30px 0 15px 0; font-size: 18px; color: #374151;">💰 Points Economy</h2>
            <div style="background: linear-gradient(135deg, #fef3c7, #fde68a); padding: 20px; border-radius: 8px; text-align: center;">
                <div style="font-size: 14px; color: #92400e;">Total Points in Circulation</div>
                <div style="font-size: 36px; font-weight: bold; color: #b45309;">{report_data.get('total_points_circulation', 0):,}</div>
            </div>
            
            <!-- Alerts Section -->
            <h2 style="margin: 30px 0 15px 0; font-size: 18px; color: #374151;">⚠️ Alerts & Actions</h2>
            <div style="background: #fef2f2; border-left: 4px solid #ef4444; padding: 15px; border-radius: 0 8px 8px 0; margin-bottom: 10px;">
                <strong style="color: #dc2626;">Pending teacher approvals:</strong> {report_data.get('pending_teachers', 0)}
            </div>
            <div style="background: #fffbeb; border-left: 4px solid #f59e0b; padding: 15px; border-radius: 0 8px 8px 0;">
                <strong style="color: #d97706;">Inactive students (7+ days):</strong> {report_data.get('inactive_students', 0)}
            </div>
            
        </div>
        
        <!-- Footer -->
        <div style="text-align: center; padding: 20px; color: #9ca3af; font-size: 12px;">
            <p>This is an automated report from AgentMath</p>
            <p>© {datetime.now().year} {school_name}</p>
        </div>
    </div>
</body>
</html>
'''
    return html


def send_email_report(recipients, subject, html_content, report_type):
    """Send email report to recipients via Gmail SMTP"""
    from sqlalchemy import text
    
    sent_count = 0
    errors = []
    
    try:
        from flask_mail import Mail, Message
        mail = Mail(app)
        
        print(f"📧 Attempting to send {report_type} report to {len(recipients)} recipient(s)...")
        
        for recipient in recipients:
            try:
                msg = Message(
                    subject=subject,
                    recipients=[recipient['email']],
                    html=html_content
                )
                mail.send(msg)
                sent_count += 1
                print(f"✅ Email sent successfully to: {recipient['email']}")
            except Exception as e:
                error_msg = f"{recipient['email']}: {str(e)}"
                errors.append(error_msg)
                print(f"❌ Failed to send to {recipient['email']}: {e}")
                import traceback
                traceback.print_exc()
                
    except ImportError as e:
        print(f"❌ Flask-Mail not installed. Run: pip install flask-mail --user")
        print(f"   Error: {e}")
        errors.append("Flask-Mail not installed - run: pip install flask-mail --user")
    except Exception as e:
        print(f"❌ Email configuration error: {e}")
        import traceback
        traceback.print_exc()
        errors.append(f"Email config error: {str(e)}")
    
    # Log the report send
    try:
        db.session.execute(text("""
            INSERT INTO report_history (report_type, report_date, recipients_count, sent_at, status, error_message)
            VALUES (:report_type, :report_date, :recipients_count, CURRENT_TIMESTAMP, :status, :errors)
        """), {
            'report_type': report_type,
            'report_date': datetime.utcnow().date(),
            'recipients_count': sent_count,
            'status': 'sent' if not errors else 'partial' if sent_count > 0 else 'failed',
            'errors': '; '.join(errors) if errors else None
        })
        db.session.commit()
        print(f"📝 Report logged: {sent_count} sent, {len(errors)} errors")
    except Exception as e:
        db.session.rollback()
        print(f"⚠️ Failed to log report: {e}")
    
    return sent_count, errors


@admin_bp.route('/api/admin/email-reports/send-test', methods=['POST'])
@login_required
@role_required('admin')
def send_test_report():
    """Send a test report to a specific email"""
    
    data = request.json
    report_type = data.get('report_type', 'daily')
    email = data.get('email', '').strip()
    
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    
    try:
        # Generate the report data
        if report_type == 'daily':
            report_data = generate_daily_report_data()
            html_content = generate_daily_report_html(report_data)
            subject = f"📊 AgentMath Daily Pulse - {report_data.get('report_date', 'Test')}"
        else:
            # Weekly and monthly reports can be added later
            return jsonify({'error': 'Only daily reports are available currently'}), 400
        
        # Send the test email
        sent_count, errors = send_email_report(
            [{'email': email}],
            subject + " [TEST]",
            html_content,
            report_type
        )
        
        if sent_count > 0:
            return jsonify({
                'success': True,
                'message': f'Test report sent to {email}'
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to send email',
                'details': errors
            }), 500
            
    except Exception as e:
        print(f"Error sending test report: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@admin_bp.route('/api/admin/email-reports/send-daily', methods=['POST'])
@login_required
@role_required('admin')
def trigger_daily_report():
    """Manually trigger sending the daily report"""
    from sqlalchemy import text
    
    try:
        # Get active daily recipients
        recipients = db.session.execute(text("""
            SELECT email, recipient_name FROM email_distribution_list
            WHERE (report_type = 'daily' OR report_type = 'all') AND is_active = 1
        """)).fetchall()
        
        if not recipients:
            return jsonify({'error': 'No active recipients for daily reports'}), 400
        
        recipient_list = [{'email': r[0], 'name': r[1]} for r in recipients]
        
        # Generate and send report
        report_data = generate_daily_report_data()
        html_content = generate_daily_report_html(report_data)
        subject = f"📊 AgentMath Daily Pulse - {report_data.get('report_date', 'Today')}"
        
        sent_count, errors = send_email_report(recipient_list, subject, html_content, 'daily')
        
        return jsonify({
            'success': True,
            'sent_count': sent_count,
            'total_recipients': len(recipient_list),
            'errors': errors
        })
        
    except Exception as e:
        print(f"Error triggering daily report: {e}")
        return jsonify({'error': str(e)}), 500
# ==================== QUESTION VALIDATOR ROUTES ====================
# Add these routes to routes/admin.py
# Revision 1.0 - 2025-01-01
#
# Provides admin interface for validating questions by topic:
# - View questions exactly as students see them
# - Edit questions in real-time
# - Delete questions
# - Track validation progress per topic
# - Export validation reports

# Add this route for the page
@admin_bp.route('/admin/question-validator')
@login_required
@role_required('admin')
def admin_question_validator():
    """Admin question validation interface"""
    return render_template('admin_question_validator.html')


# API: Get topics with validation status
@admin_bp.route('/api/admin/question-validator/topics')
@login_required
@role_required('admin')
def get_validator_topics():
    """Get all topics with validation statistics from both questions tables"""
    from sqlalchemy import text
    
    try:
        # Drop and recreate tracking table if schema is wrong
        # Check if source_table column exists
        try:
            db.session.execute(text("SELECT source_table FROM question_validation_tracking LIMIT 1"))
        except:
            # Column doesn't exist - drop and recreate
            db.session.execute(text("DROP TABLE IF EXISTS question_validation_tracking"))
            db.session.commit()
        
        # Create validation tracking table
        db.session.execute(text("""
            CREATE TABLE IF NOT EXISTS question_validation_tracking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic VARCHAR(100) UNIQUE NOT NULL,
                source_table VARCHAR(50) DEFAULT 'questions',
                validated BOOLEAN DEFAULT 0,
                validated_at TIMESTAMP,
                validated_by INTEGER,
                reviewed_count INTEGER DEFAULT 0,
                edited_count INTEGER DEFAULT 0,
                deleted_count INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """))
        db.session.commit()
        
        # Get topics from BOTH questions and questions_adaptive tables
        # Simple JOIN on topic only (not source_table) for compatibility
        topics_query = text("""
            SELECT 
                combined.topic as name,
                combined.source_table,
                COALESCE(t.display_name, combined.topic) as display_name,
                COALESCE(s.name, 
                    CASE 
                        WHEN combined.topic LIKE 'lc_hl_%' THEN 'LC Higher Level'
                        WHEN combined.topic LIKE 'lc_ol_%' THEN 'LC Ordinary Level'
                        WHEN combined.topic LIKE 'l2_%' THEN 'L2LP'
                        WHEN combined.topic LIKE 'l1lp_%' THEN 'L1LP'
                        ELSE 'Other'
                    END
                ) as strand,
                combined.question_count,
                COALESCE(v.validated, 0) as validated,
                COALESCE(v.reviewed_count, 0) as reviewed_count,
                COALESCE(v.edited_count, 0) as edited_count,
                COALESCE(v.deleted_count, 0) as deleted_count
            FROM (
                SELECT topic, 'questions' as source_table, COUNT(*) as question_count
                FROM questions
                GROUP BY topic
                UNION ALL
                SELECT topic, 'questions_adaptive' as source_table, COUNT(*) as question_count
                FROM questions_adaptive
                GROUP BY topic
            ) combined
            LEFT JOIN topics t ON t.topic_id = combined.topic
            LEFT JOIN strands s ON s.id = t.strand_id
            LEFT JOIN question_validation_tracking v ON v.topic = combined.topic
            ORDER BY strand, display_name
        """)
        
        results = db.session.execute(topics_query).fetchall()
        
        topics = [{
            'name': r[0],
            'source_table': r[1],
            'display_name': r[2] or r[0],
            'strand': r[3] or 'Other',
            'question_count': r[4] or 0,
            'validated': bool(r[5]),
            'reviewed_count': r[6] or 0,
            'edited_count': r[7] or 0,
            'deleted_count': r[8] or 0
        } for r in results]
        
        return jsonify({'topics': topics})
        
    except Exception as e:
        print(f"Error getting validator topics: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


# API: Get questions for a topic
@admin_bp.route('/api/admin/question-validator/questions')
@login_required
@role_required('admin')
def get_validator_questions():
    """Get questions for a specific topic from either questions table"""
    from sqlalchemy import text
    
    topic = request.args.get('topic')
    source_table = request.args.get('source', 'questions')  # Default to questions table
    
    if not topic:
        return jsonify({'error': 'Topic required'}), 400
    
    # Validate source table to prevent SQL injection
    if source_table not in ['questions', 'questions_adaptive']:
        source_table = 'questions'
    
    try:
        # Different schemas for each table
        if source_table == 'questions':
            # Legacy questions table - different column names
            query = text("""
                SELECT 
                    id, topic, question_text, option_a, option_b, option_c, option_d,
                    correct_answer, explanation, difficulty, 
                    COALESCE(image_url, question_image_svg) as image_url,
                    0 as times_shown, 0 as times_correct, 1 as is_active
                FROM questions
                WHERE topic = :topic
                ORDER BY id
            """)
        else:
            # questions_adaptive has different column names
            query = text("""
                SELECT 
                    id, topic, question_text, option_a, option_b, option_c, option_d,
                    correct_answer, explanation, difficulty_level as difficulty, 
                    image_svg as image_url,
                    times_shown, times_correct, is_active
                FROM questions_adaptive
                WHERE topic = :topic
                ORDER BY id
            """)
        
        results = db.session.execute(query, {'topic': topic}).fetchall()
        
        # Convert correct_answer for both tables (0-3 → A-D, 0-indexed!)
        # Both questions and questions_adaptive use 0=A, 1=B, 2=C, 3=D
        def convert_answer(ans, source):
            if isinstance(ans, int):
                return ['A', 'B', 'C', 'D'][ans] if 0 <= ans <= 3 else 'A'
            return ans
        
        questions = [{
            'id': r[0],
            'topic': r[1],
            'question_text': r[2],
            'option_a': r[3],
            'option_b': r[4],
            'option_c': r[5],
            'option_d': r[6],
            'correct_answer': convert_answer(r[7], source_table),
            'explanation': r[8],
            'difficulty': r[9] or 1,
            'image_url': r[10],
            'times_shown': r[11] or 0,
            'times_correct': r[12] or 0,
            'is_active': bool(r[13]) if r[13] is not None else True,
            'reviewed': False,  # Client tracks this per session
            'source_table': source_table
        } for r in results]
        
        return jsonify({'questions': questions, 'topic': topic, 'source_table': source_table})
        
    except Exception as e:
        print(f"Error getting questions: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


# API: Get validation statistics
@admin_bp.route('/api/admin/question-validator/stats')
@login_required
@role_required('admin')
def get_validator_stats():
    """Get overall validation statistics from both question tables"""
    from sqlalchemy import text
    
    try:
        # Total questions from both tables
        total_questions = db.session.execute(text("SELECT COUNT(*) FROM questions")).scalar() or 0
        total_adaptive = db.session.execute(text("SELECT COUNT(*) FROM questions_adaptive")).scalar() or 0
        total = total_questions + total_adaptive
        
        # Topics stats
        topics_stats = db.session.execute(text("""
            SELECT 
                COUNT(*) as total_topics,
                SUM(CASE WHEN validated = 1 THEN 1 ELSE 0 END) as validated_topics,
                SUM(reviewed_count) as total_reviewed,
                SUM(edited_count) as total_edited,
                SUM(deleted_count) as total_deleted
            FROM question_validation_tracking
        """)).fetchone()
        
        return jsonify({
            'totalQuestions': total,
            'questionsTable': total_questions,
            'adaptiveTable': total_adaptive,
            'validated': topics_stats[2] or 0 if topics_stats else 0,
            'edited': topics_stats[3] or 0 if topics_stats else 0,
            'deleted': topics_stats[4] or 0 if topics_stats else 0,
            'topicsComplete': topics_stats[1] or 0 if topics_stats else 0,
            'totalTopics': topics_stats[0] or 0 if topics_stats else 0
        })
        
    except Exception as e:
        print(f"Error getting stats: {e}")
        return jsonify({
            'totalQuestions': 0,
            'validated': 0,
            'edited': 0,
            'deleted': 0,
            'topicsComplete': 0
        })


# API: Update a question
@admin_bp.route('/api/admin/question-validator/question/<int:question_id>', methods=['PUT'])
@login_required
@role_required('admin')
def update_validator_question(question_id):
    """Update a question in either questions table"""
    from sqlalchemy import text
    
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Get source table from request
    source_table = data.get('source_table', 'questions')
    if source_table not in ['questions', 'questions_adaptive']:
        source_table = 'questions'
    
    try:
        # Build update query - map fields to correct column names per table
        update_fields = []
        params = {'id': question_id}
        
        # Column name mapping differs between tables
        if source_table == 'questions':
            field_mapping = {
                'question_text': 'question_text',
                'option_a': 'option_a',
                'option_b': 'option_b',
                'option_c': 'option_c',
                'option_d': 'option_d',
                'correct_answer': 'correct_answer',
                'explanation': 'explanation',
                'difficulty': 'difficulty',
                'image_url': 'image_url'
            }
        else:
            # questions_adaptive has different column names
            field_mapping = {
                'question_text': 'question_text',
                'option_a': 'option_a',
                'option_b': 'option_b',
                'option_c': 'option_c',
                'option_d': 'option_d',
                'correct_answer': 'correct_answer',
                'explanation': 'explanation',
                'difficulty': 'difficulty_level',
                'image_url': 'image_svg'
            }
        
        for key, column in field_mapping.items():
            if key in data:
                value = data[key]
                # Convert correct_answer from A-D to 0-3 for both tables (0-indexed!)
                if key == 'correct_answer':
                    answer_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
                    value = answer_map.get(value, 0)
                update_fields.append(f"{column} = :{key}")
                params[key] = value
        
        if not update_fields:
            return jsonify({'error': 'No valid fields to update'}), 400
        
        query = f"UPDATE {source_table} SET {', '.join(update_fields)} WHERE id = :id"
        db.session.execute(text(query), params)
        
        # Get topic for this question
        topic_result = db.session.execute(
            text(f"SELECT topic FROM {source_table} WHERE id = :id"),
            {'id': question_id}
        ).fetchone()
        
        if topic_result:
            # Update edit count for topic (simple upsert by topic name)
            db.session.execute(text("""
                INSERT INTO question_validation_tracking (topic, edited_count)
                VALUES (:topic, 1)
                ON CONFLICT(topic) DO UPDATE SET 
                    edited_count = edited_count + 1,
                    updated_at = CURRENT_TIMESTAMP
            """), {'topic': topic_result[0]})
        
        db.session.commit()
        
        return jsonify({'success': True})
        
    except Exception as e:
        db.session.rollback()
        print(f"Error updating question: {e}")
        return jsonify({'error': str(e)}), 500


# API: Delete a question
@admin_bp.route('/api/admin/question-validator/question/<int:question_id>', methods=['DELETE'])
@login_required
@role_required('admin')
def delete_validator_question(question_id):
    """Delete a question from either questions table"""
    from sqlalchemy import text
    
    # Get source table from request args
    source_table = request.args.get('source', 'questions')
    if source_table not in ['questions', 'questions_adaptive']:
        source_table = 'questions'
    
    try:
        # Get topic before deleting
        topic_result = db.session.execute(
            text(f"SELECT topic FROM {source_table} WHERE id = :id"),
            {'id': question_id}
        ).fetchone()
        
        # Delete the question
        db.session.execute(
            text(f"DELETE FROM {source_table} WHERE id = :id"),
            {'id': question_id}
        )
        
        if topic_result:
            # Update delete count for topic
            db.session.execute(text("""
                INSERT INTO question_validation_tracking (topic, deleted_count)
                VALUES (:topic, 1)
                ON CONFLICT(topic) DO UPDATE SET 
                    deleted_count = deleted_count + 1,
                    updated_at = CURRENT_TIMESTAMP
            """), {'topic': topic_result[0]})
        
        db.session.commit()
        
        return jsonify({'success': True})
        
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting question: {e}")
        return jsonify({'error': str(e)}), 500


# API: Mark question as reviewed
@admin_bp.route('/api/admin/question-validator/question/<int:question_id>/reviewed', methods=['POST'])
@login_required
@role_required('admin')
def mark_question_reviewed(question_id):
    """Mark a question as reviewed"""
    from sqlalchemy import text
    
    # Get source table from request
    data = request.json or {}
    source_table = data.get('source_table', 'questions')
    if source_table not in ['questions', 'questions_adaptive']:
        source_table = 'questions'
    
    try:
        # Get topic
        topic_result = db.session.execute(
            text(f"SELECT topic FROM {source_table} WHERE id = :id"),
            {'id': question_id}
        ).fetchone()
        
        if topic_result:
            db.session.execute(text("""
                INSERT INTO question_validation_tracking (topic, reviewed_count)
                VALUES (:topic, 1)
                ON CONFLICT(topic) DO UPDATE SET 
                    reviewed_count = reviewed_count + 1,
                    updated_at = CURRENT_TIMESTAMP
            """), {'topic': topic_result[0]})
            db.session.commit()
        
        return jsonify({'success': True})
        
    except Exception as e:
        db.session.rollback()
        print(f"Error marking reviewed: {e}")
        return jsonify({'error': str(e)}), 500


# API: Mark topic as validated
@admin_bp.route('/api/admin/question-validator/topic/<topic_name>/validate', methods=['POST'])
@login_required
@role_required('admin')
def mark_topic_validated(topic_name):
    """Mark a topic as fully validated"""
    from sqlalchemy import text
    
    # Get source table from request
    data = request.json or {}
    source_table = data.get('source_table', 'questions')
    if source_table not in ['questions', 'questions_adaptive']:
        source_table = 'questions'
    
    try:
        user_id = session.get('user_id')
        
        db.session.execute(text("""
            INSERT INTO question_validation_tracking (topic, validated, validated_at, validated_by)
            VALUES (:topic, 1, CURRENT_TIMESTAMP, :user_id)
            ON CONFLICT(topic) DO UPDATE SET 
                validated = 1,
                validated_at = CURRENT_TIMESTAMP,
                validated_by = :user_id,
                updated_at = CURRENT_TIMESTAMP
        """), {'topic': topic_name, 'user_id': user_id})
        
        db.session.commit()
        
        return jsonify({'success': True})
        
    except Exception as e:
        db.session.rollback()
        print(f"Error validating topic: {e}")
        return jsonify({'error': str(e)}), 500


# API: Export validation report
@admin_bp.route('/api/admin/question-validator/export')
@login_required
@role_required('admin')
def export_validation_report():
    """Export validation report as CSV"""
    from sqlalchemy import text
    import csv
    import io
    
    try:
        query = text("""
            SELECT 
                q.topic as name,
                COALESCE(t.display_name, q.topic) as display_name,
                COALESCE(s.name, 'Other') as strand,
                COUNT(q.id) as question_count,
                COALESCE(v.validated, 0) as validated,
                v.validated_at,
                COALESCE(v.reviewed_count, 0) as reviewed_count,
                COALESCE(v.edited_count, 0) as edited_count,
                COALESCE(v.deleted_count, 0) as deleted_count
            FROM questions q
            LEFT JOIN topics t ON t.topic_id = q.topic
            LEFT JOIN strands s ON s.id = t.strand_id
            LEFT JOIN question_validation_tracking v ON v.topic = q.topic
            GROUP BY q.topic
            ORDER BY strand, display_name
        """)
        
        results = db.session.execute(query).fetchall()
        
        # Create CSV
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Topic', 'Display Name', 'Strand', 'Questions', 'Validated', 'Validated At', 
                        'Reviewed', 'Edited', 'Deleted'])
        
        for r in results:
            writer.writerow([
                r[0], r[1], r[2], r[3], 
                'Yes' if r[4] else 'No',
                r[5] or '',
                r[6], r[7], r[8]
            ])
        
        output.seek(0)
        
        from flask import Response
        return Response(
            output.getvalue(),
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment;filename=validation_report.csv'}
        )
        
    except Exception as e:
        print(f"Error exporting report: {e}")
        return jsonify({'error': str(e)}), 500
