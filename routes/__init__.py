# routes/__init__.py
# Route blueprints for AgentMath
# Extracted from app.py for better maintainability
#
# Revision: 1.7.0
# Date: 2025-12-31
# Phase 11: Added prizes and engagement blueprints

from routes.auth import auth_bp
from routes.pwa import pwa_bp
from routes.passport import passport_bp
from routes.teacher import teacher_bp
from routes.admin import admin_bp
from routes.interactive import interactive_bp
from routes.games import games_bp
from routes.student_features import student_bp
from routes.prizes import prizes_bp
from routes.engagement import engagement_bp

# List of all blueprints for easy registration
all_blueprints = [
    (auth_bp, {}),         # Auth routes: /register, /api/register, /api/login, /api/logout
    (pwa_bp, {}),          # PWA routes: /manifest.json, /sw.js, /offline.html
    (passport_bp, {}),     # Passport routes: /passport, /api/passport/*, /api/ilp/*
    (teacher_bp, {}),      # Teacher routes: /teacher/*, /api/teacher/*
    (admin_bp, {}),        # Admin routes: /admin, /api/admin/*
    (interactive_bp, {}),  # Interactive routes: /api/adaptive/*, /api/flow-sums/*, etc.
    (games_bp, {}),        # Games routes: /api/clock-challenge/*, /racing-car/*
    (student_bp, {}),      # Student features: /api/student/badges, /avatar/*, /api/who-am-i/*
    (prizes_bp, {}),       # Prizes: /prizes, /api/prizes/*, /school-rep, /api/prize-pin/*
    (engagement_bp, {}),   # Engagement: guest system, flagging, leaderboard, puzzle
]


def register_blueprints(app):
    """Register all blueprints with the Flask app"""
    for blueprint, options in all_blueprints:
        app.register_blueprint(blueprint, **options)
