# utils/auth.py
# Authentication decorators for AgentMath
# Extracted from app.py for better maintainability
#
# Revision: 1.0.0
# Date: 2025-12-27

from functools import wraps
from flask import session, jsonify


def login_required(f):
    """Require user to be logged in (full account or guest)"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Allow full accounts (user_id), casual guests (is_guest + user_id), and repeat guests (guest_code)
        if 'user_id' not in session and 'guest_code' not in session:
            return jsonify({'error': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated_function


def role_required(*roles):
    """Require user to have one of the specified roles"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            from models import User  # Late import to avoid circular dependency
            
            # Repeat guests are considered students
            if 'guest_code' in session and 'student' in roles:
                return f(*args, **kwargs)

            # Full accounts and casual guests
            if 'user_id' not in session:
                return jsonify({'error': 'Authentication required'}), 401
            user = User.query.get(session['user_id'])
            if not user or user.role not in roles:
                return jsonify({'error': 'Insufficient permissions'}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def approved_required(f):
    """Require teacher to be approved"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        from models import User  # Late import to avoid circular dependency
        
        # Allow casual guests through
        if 'is_guest' in session:
            return f(*args, **kwargs)

        # Allow repeat guests through
        if 'guest_code' in session:
            return f(*args, **kwargs)

        # For regular users, check authentication and approval
        if 'user_id' not in session:
            return jsonify({'error': 'Authentication required'}), 401
        user = User.query.get(session['user_id'])
        if not user:
            return jsonify({'error': 'User not found'}), 404
        if user.role == 'teacher' and not user.is_approved:
            return jsonify({'error': 'Teacher account pending approval'}), 403
        return f(*args, **kwargs)
    return decorated_function


def guest_or_login_required(f):
    """Allow both guest users and logged-in users"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'is_guest' not in session and 'user_id' not in session and 'guest_code' not in session:
            return jsonify({'error': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated_function
