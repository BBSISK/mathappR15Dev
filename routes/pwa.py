# routes/pwa.py
# Progressive Web App routes for AgentMath
# Extracted from app.py for better maintainability
#
# Revision: 1.0.0
# Date: 2025-12-27

from flask import Blueprint, send_from_directory, current_app

# Create blueprint
pwa_bp = Blueprint('pwa', __name__)


@pwa_bp.route('/manifest.json')
def pwa_manifest():
    """Serve the PWA manifest file"""
    return send_from_directory(
        current_app.static_folder,
        'manifest.json',
        mimetype='application/manifest+json'
    )


@pwa_bp.route('/sw.js')
def pwa_service_worker():
    """Serve the service worker from root (required for scope)"""
    return send_from_directory(
        current_app.static_folder,
        'sw.js',
        mimetype='application/javascript'
    )


@pwa_bp.route('/offline.html')
def pwa_offline():
    """Serve the offline fallback page"""
    return send_from_directory(
        current_app.static_folder,
        'offline.html',
        mimetype='text/html'
    )
