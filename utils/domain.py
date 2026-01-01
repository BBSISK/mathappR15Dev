# utils/domain.py
# Domain restriction helper functions for AgentMath
# Extracted from app.py for better maintainability
#
# Revision: 1.0.0
# Date: 2025-12-27


def extract_domain(email):
    """Extract domain from email address"""
    if not email or '@' not in email:
        return None
    return email.split('@')[1].lower()


def get_all_domains_in_system():
    """Get all unique email domains from both students and teachers"""
    from models import User, TeacherDomainAccess  # Late import
    
    domains = {}

    # Get student domains
    students = User.query.filter_by(role='student').all()
    for student in students:
        domain = extract_domain(student.email)
        if domain:
            if domain not in domains:
                domains[domain] = {
                    'domain': domain,
                    'student_count': 0,
                    'teacher_count': 0,
                    'teachers_with_access': []
                }
            domains[domain]['student_count'] += 1

    # Get teacher domains
    teachers = User.query.filter_by(role='teacher').all()
    for teacher in teachers:
        domain = extract_domain(teacher.email)
        if domain:
            if domain not in domains:
                domains[domain] = {
                    'domain': domain,
                    'student_count': 0,
                    'teacher_count': 0,
                    'teachers_with_access': []
                }
            domains[domain]['teacher_count'] += 1

    # Get teachers with access to each domain
    for domain_name in domains.keys():
        access_records = TeacherDomainAccess.query.filter_by(email_domain=domain_name).all()
        for record in access_records:
            domains[domain_name]['teachers_with_access'].append({
                'id': record.teacher_id,
                'name': record.teacher.full_name,
                'email': record.teacher.email
            })

    return list(domains.values())


def teacher_has_domain_access(teacher_id, domain):
    """Check if a teacher has access to a specific domain"""
    from models import TeacherDomainAccess  # Late import
    
    if not domain:
        return True

    # Check if teacher has any domain restrictions
    has_any_restrictions = TeacherDomainAccess.query.filter_by(teacher_id=teacher_id).first()

    # If teacher has NO restrictions at all, they can see ALL students (backward compatible)
    if not has_any_restrictions:
        return True

    # If teacher has restrictions, check if they have access to THIS specific domain
    access = TeacherDomainAccess.query.filter_by(
        teacher_id=teacher_id,
        email_domain=domain
    ).first()

    return access is not None


def get_teacher_accessible_domains(teacher_id):
    """Get all domains a teacher has access to"""
    from models import TeacherDomainAccess  # Late import
    
    # Check if teacher has any restrictions
    restrictions = TeacherDomainAccess.query.filter_by(teacher_id=teacher_id).all()

    if not restrictions:
        # No restrictions = access to all domains
        return None  # None means "all domains"

    # Return list of accessible domains
    return [r.email_domain for r in restrictions]


def filter_students_by_domain_access(students_query, teacher_id):
    """Filter a students query based on teacher's domain access"""
    from models import User, TeacherDomainAccess  # Late import
    
    # Get teacher's accessible domains
    accessible = get_teacher_accessible_domains(teacher_id)

    if accessible is None:
        # No restrictions - return all students
        return students_query

    # Filter by domains
    # This is a bit complex because we need to filter by email domain
    filtered_ids = []
    for student in students_query.all():
        domain = extract_domain(student.email)
        if domain in accessible:
            filtered_ids.append(student.id)

    return User.query.filter(User.id.in_(filtered_ids)) if filtered_ids else User.query.filter(False)


def get_teacher_domain_statistics(teacher_id):
    """Get domain access statistics for a teacher"""
    from models import User, TeacherDomainAccess  # Late import
    
    accessible = get_teacher_accessible_domains(teacher_id)

    if accessible is None:
        # Full access
        total_students = User.query.filter_by(role='student').count()
        return {
            'has_restrictions': False,
            'accessible_domains': [],
            'total_accessible_students': total_students,
            'message': 'Full access to all students'
        }

    # Count students in accessible domains
    students = User.query.filter_by(role='student').all()
    accessible_count = 0
    domain_counts = {}

    for student in students:
        domain = extract_domain(student.email)
        if domain in accessible:
            accessible_count += 1
            domain_counts[domain] = domain_counts.get(domain, 0) + 1

    return {
        'has_restrictions': True,
        'accessible_domains': accessible,
        'domain_student_counts': domain_counts,
        'total_accessible_students': accessible_count,
        'message': f'Access to {len(accessible)} domain(s)'
    }
