# routes/auth.py
# Authentication routes for AgentMath
# Extracted from app.py for better maintainability
#
# Revision: 1.0.1
# Date: 2025-12-31 - Added /login GET route

import re
from flask import Blueprint, request, jsonify, session, render_template

# Create blueprint
auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET'])
def login_page():
    """Render the login page"""
    return render_template('login.html')


@auth_bp.route('/register', methods=['GET'])
def register_page():
    """Render the registration page"""
    return render_template('register.html')


@auth_bp.route('/api/register', methods=['POST'])
def register():
    """Register a new user account"""
    from models import db, User  # Late import
    
    data = request.json
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')
    full_name = data.get('full_name', '').strip()
    role = data.get('role', 'student')

    # Validation
    if not email or not password or not full_name:
        return jsonify({'error': 'All fields are required'}), 400

    # Allow parentheses, plus signs, and other valid email characters
    if not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email):
        return jsonify({'error': 'Invalid email format'}), 400

    if len(password) < 6:
        return jsonify({'error': 'Password must be at least 6 characters'}), 400

    if role not in ['student', 'teacher']:
        return jsonify({'error': 'Invalid role'}), 400

    # Check if user exists
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered'}), 400

    # Create user
    user = User(
        email=email,
        full_name=full_name,
        role=role,
        is_approved=(role == 'student')  # Students auto-approved, teachers need approval
    )
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    message = 'Registration successful!' if role == 'student' else 'Registration successful! Your teacher account is pending admin approval.'

    return jsonify({
        'message': message,
        'user': user.to_dict()
    }), 201


@auth_bp.route('/api/login', methods=['POST'])
def login():
    """Login with email and password"""
    from models import User  # Late import
    
    data = request.json
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({'error': 'Invalid email or password'}), 401

    session['user_id'] = user.id
    session['user_role'] = user.role
    session['user_name'] = user.full_name

    return jsonify({
        'message': 'Login successful',
        'role': user.role,
        'is_approved': user.is_approved,
        'user': user.to_dict()
    }), 200


@auth_bp.route('/api/logout', methods=['POST'])
def logout():
    """Logout API endpoint with proper session invalidation"""
    session.clear()
    response = jsonify({'message': 'Logged out successfully', 'redirect': '/login?logged_out=1'})
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.delete_cookie('session')
    return response, 200
