# ==================== FEEDBACK SYSTEM ====================
# Add this model after the other models (around line 920)

class Feedback(db.Model):
    """User feedback submissions"""
    __tablename__ = 'feedback'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    guest_code = db.Column(db.String(50), nullable=True)
    username = db.Column(db.String(100))
    
    # Feedback content
    rating = db.Column(db.Integer)  # 1-5 stars
    category = db.Column(db.String(50), default='general')
    feedback_text = db.Column(db.Text, nullable=False)
    
    # Context
    page_context = db.Column(db.String(100))
    topic_context = db.Column(db.String(100))
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Admin review
    status = db.Column(db.String(20), default='new')
    admin_notes = db.Column(db.Text)
    reviewed_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    reviewed_at = db.Column(db.DateTime)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'guest_code': self.guest_code,
            'username': self.username,
            'rating': self.rating,
            'category': self.category,
            'feedback_text': self.feedback_text,
            'page_context': self.page_context,
            'topic_context': self.topic_context,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'status': self.status,
            'admin_notes': self.admin_notes,
            'reviewed_by': self.reviewed_by,
            'reviewed_at': self.reviewed_at.isoformat() if self.reviewed_at else None
        }


# ==================== FEEDBACK API ENDPOINTS ====================
# Add these routes in the API section

@app.route('/api/feedback', methods=['POST'])
@guest_or_login_required
def submit_feedback():
    """Submit user feedback with rate limiting (3 per day)"""
    from datetime import datetime, timedelta
    from sqlalchemy import func
    
    data = request.get_json()
    
    if not data or not data.get('feedback_text', '').strip():
        return jsonify({'error': 'Feedback text is required'}), 400
    
    # Get user info
    user_id = session.get('user_id') if not session.get('is_guest') else None
    guest_code = session.get('guest_code') if session.get('is_guest') else None
    
    # Get username for easy reference
    username = None
    if user_id:
        user = User.query.get(user_id)
        if user:
            username = user.username
    elif guest_code:
        username = f"Guest ({guest_code[:8]}...)"
    
    # Rate limiting: max 3 feedback per day per user
    today_start = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    
    if user_id:
        today_count = Feedback.query.filter(
            Feedback.user_id == user_id,
            Feedback.created_at >= today_start
        ).count()
    elif guest_code:
        today_count = Feedback.query.filter(
            Feedback.guest_code == guest_code,
            Feedback.created_at >= today_start
        ).count()
    else:
        today_count = 0
    
    if today_count >= 3:
        return jsonify({
            'error': 'Rate limit reached',
            'message': 'You can submit up to 3 feedback items per day. Please try again tomorrow!'
        }), 429
    
    try:
        feedback = Feedback(
            user_id=user_id,
            guest_code=guest_code,
            username=username,
            rating=data.get('rating'),
            category=data.get('category', 'general'),
            feedback_text=data.get('feedback_text', '').strip(),
            page_context=data.get('page_context'),
            topic_context=data.get('topic_context'),
            status='new'
        )
        
        db.session.add(feedback)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Thank you for your feedback!',
            'remaining_today': 3 - today_count - 1
        })
        
    except Exception as e:
        db.session.rollback()
        print(f"Error submitting feedback: {e}")
        return jsonify({'error': 'Failed to submit feedback'}), 500


@app.route('/api/admin/feedback', methods=['GET'])
@login_required
@admin_required
def get_feedback_list():
    """Get all feedback for admin review"""
    status_filter = request.args.get('status', 'all')
    category_filter = request.args.get('category', 'all')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    
    query = Feedback.query
    
    if status_filter != 'all':
        query = query.filter(Feedback.status == status_filter)
    
    if category_filter != 'all':
        query = query.filter(Feedback.category == category_filter)
    
    # Order by newest first, but new status items first
    query = query.order_by(
        db.case(
            (Feedback.status == 'new', 0),
            else_=1
        ),
        Feedback.created_at.desc()
    )
    
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    
    # Get counts by status
    status_counts = db.session.query(
        Feedback.status, func.count(Feedback.id)
    ).group_by(Feedback.status).all()
    
    counts = {status: count for status, count in status_counts}
    
    return jsonify({
        'feedback': [f.to_dict() for f in pagination.items],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page,
        'counts': {
            'new': counts.get('new', 0),
            'reviewed': counts.get('reviewed', 0),
            'in_progress': counts.get('in_progress', 0),
            'resolved': counts.get('resolved', 0),
            'dismissed': counts.get('dismissed', 0)
        }
    })


@app.route('/api/admin/feedback/<int:feedback_id>', methods=['PUT'])
@login_required
@admin_required
def update_feedback(feedback_id):
    """Update feedback status and notes"""
    from datetime import datetime
    
    feedback = Feedback.query.get_or_404(feedback_id)
    data = request.get_json()
    
    if 'status' in data:
        feedback.status = data['status']
    
    if 'admin_notes' in data:
        feedback.admin_notes = data['admin_notes']
    
    feedback.reviewed_by = session.get('user_id')
    feedback.reviewed_at = datetime.utcnow()
    
    try:
        db.session.commit()
        return jsonify({
            'success': True,
            'feedback': feedback.to_dict()
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/api/admin/feedback/<int:feedback_id>', methods=['DELETE'])
@login_required
@admin_required
def delete_feedback(feedback_id):
    """Delete feedback (hard delete)"""
    feedback = Feedback.query.get_or_404(feedback_id)
    
    try:
        db.session.delete(feedback)
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# ==================== ADMIN FEEDBACK PAGE ROUTE ====================
# Add this route in the admin routes section

@app.route('/admin/feedback')
@login_required
@admin_required
def admin_feedback():
    """Admin feedback management page"""
    return render_template('admin_feedback.html')
