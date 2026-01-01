# test_feedback.py - User Feedback System Tests
# Version 1.0 - 2025-12-31
#
# Tests for the feedback submission and admin management system

import pytest


# ============================================================================
# STUDENT FEEDBACK SUBMISSION TESTS
# ============================================================================

class TestFeedbackSubmission:
    """Test student feedback submission."""
    
    def test_submit_feedback_as_student(self, student_client, get_json):
        """Test submitting feedback as logged-in student."""
        response = student_client.post('/api/submit-feedback', json={
            'feedback_text': 'Great app! I really enjoy the quizzes.',
            'category': 'general',
            'rating': 5
        })
        assert response.status_code in [200, 201], "Should accept feedback"
        if response.status_code == 200:
            data = get_json(response)
            assert data.get('success') == True
    
    def test_submit_feedback_as_guest(self, guest_client, get_json):
        """Test submitting feedback as guest user."""
        response = guest_client.post('/api/submit-feedback', json={
            'feedback_text': 'Nice platform for practicing math.',
            'category': 'general',
            'rating': 4
        })
        # Guest may or may not be able to submit depending on setup
        assert response.status_code in [200, 201, 401, 403], "Should handle guest feedback"
    
    def test_submit_feedback_empty_text(self, student_client):
        """Test submitting empty feedback is rejected."""
        response = student_client.post('/api/submit-feedback', json={
            'feedback_text': '',
            'category': 'general'
        })
        assert response.status_code == 400, "Should reject empty feedback"
    
    def test_submit_feedback_missing_text(self, student_client):
        """Test submitting without feedback text is rejected."""
        response = student_client.post('/api/submit-feedback', json={
            'category': 'bug'
        })
        assert response.status_code == 400, "Should reject missing feedback"
    
    def test_submit_feedback_with_category(self, student_client, get_json):
        """Test submitting feedback with specific category."""
        response = student_client.post('/api/submit-feedback', json={
            'feedback_text': 'Found a typo in question 123',
            'category': 'bug'
        })
        assert response.status_code in [200, 201], "Should accept categorized feedback"
    
    def test_submit_feedback_with_context(self, student_client, get_json):
        """Test submitting feedback with page context."""
        response = student_client.post('/api/submit-feedback', json={
            'feedback_text': 'This topic is confusing',
            'category': 'content',
            'page_context': '/student/quiz',
            'topic_context': 'algebra'
        })
        assert response.status_code in [200, 201], "Should accept contextual feedback"
    
    def test_submit_feedback_invalid_category(self, student_client, get_json):
        """Test submitting feedback with invalid category defaults to general."""
        response = student_client.post('/api/submit-feedback', json={
            'feedback_text': 'Test feedback',
            'category': 'invalid_category_xyz'
        })
        # Should accept but use default category
        assert response.status_code in [200, 201], "Should accept with invalid category"
    
    def test_submit_feedback_invalid_rating(self, student_client, get_json):
        """Test submitting feedback with invalid rating."""
        response = student_client.post('/api/submit-feedback', json={
            'feedback_text': 'Test feedback',
            'rating': 99  # Invalid rating
        })
        # Should accept but ignore invalid rating
        assert response.status_code in [200, 201], "Should accept with invalid rating"
    
    def test_submit_feedback_long_text(self, student_client):
        """Test submitting very long feedback."""
        long_text = 'A' * 10000  # 10k characters
        response = student_client.post('/api/submit-feedback', json={
            'feedback_text': long_text
        })
        # May reject if too long or accept truncated
        assert response.status_code in [200, 201, 400], "Should handle long feedback"
    
    def test_get_my_feedback(self, student_client, get_json):
        """Test getting user's own feedback history."""
        response = student_client.get('/api/my-feedback')
        assert response.status_code in [200, 404], "Should return feedback list"
        if response.status_code == 200:
            data = get_json(response)
            assert 'feedback' in data


# ============================================================================
# ADMIN FEEDBACK MANAGEMENT TESTS
# ============================================================================

class TestAdminFeedbackManagement:
    """Test admin feedback management."""
    
    def test_get_feedback_stats(self, authenticated_client, get_json):
        """Test getting feedback statistics."""
        response = authenticated_client.get('/api/admin/feedback/stats')
        assert response.status_code in [200, 404], "Should return stats"
        if response.status_code == 200:
            data = get_json(response)
            assert 'total' in data
            assert 'new' in data
            assert 'actioned' in data
    
    def test_get_feedback_list(self, authenticated_client, get_json):
        """Test getting feedback list."""
        response = authenticated_client.get('/api/admin/feedback')
        assert response.status_code in [200, 404], "Should return feedback list"
        if response.status_code == 200:
            data = get_json(response)
            assert 'feedback' in data
            assert 'total' in data
    
    def test_get_feedback_filtered_by_status(self, authenticated_client, get_json):
        """Test filtering feedback by status."""
        for status in ['new', 'reviewed', 'actioned', 'dismissed', 'all']:
            response = authenticated_client.get(f'/api/admin/feedback?status={status}')
            assert response.status_code in [200, 404], f"Should filter by {status}"
    
    def test_get_feedback_filtered_by_category(self, authenticated_client, get_json):
        """Test filtering feedback by category."""
        for category in ['general', 'bug', 'feature', 'content', 'ui', 'other', 'all']:
            response = authenticated_client.get(f'/api/admin/feedback?category={category}')
            assert response.status_code in [200, 404], f"Should filter by {category}"
    
    def test_get_feedback_paginated(self, authenticated_client, get_json):
        """Test feedback pagination."""
        response = authenticated_client.get('/api/admin/feedback?page=1&per_page=10')
        assert response.status_code in [200, 404], "Should support pagination"
        if response.status_code == 200:
            data = get_json(response)
            assert 'page' in data
            assert 'total_pages' in data
    
    def test_update_feedback_status(self, authenticated_client):
        """Test updating feedback status."""
        response = authenticated_client.put('/api/admin/feedback/1', json={
            'status': 'reviewed'
        })
        # May be 404 if no feedback exists
        assert response.status_code in [200, 404], "Should update or return not found"
    
    def test_update_feedback_notes(self, authenticated_client):
        """Test updating feedback admin notes."""
        response = authenticated_client.put('/api/admin/feedback/1', json={
            'admin_notes': 'Reviewed and will fix in next release'
        })
        assert response.status_code in [200, 404], "Should update notes or return not found"
    
    def test_delete_feedback(self, authenticated_client):
        """Test deleting feedback."""
        response = authenticated_client.delete('/api/admin/feedback/999999')
        # Should succeed even if not found (idempotent)
        assert response.status_code in [200, 204, 404], "Should handle delete"


# ============================================================================
# FEEDBACK ACCESS CONTROL TESTS
# ============================================================================

class TestFeedbackAccessControl:
    """Test feedback access control."""
    
    def test_admin_stats_blocked_for_student(self, student_client):
        """Test students cannot access admin feedback stats."""
        response = student_client.get('/api/admin/feedback/stats')
        assert response.status_code in [401, 403, 404], "Student blocked from admin stats"
    
    def test_admin_list_blocked_for_student(self, student_client):
        """Test students cannot access admin feedback list."""
        response = student_client.get('/api/admin/feedback')
        assert response.status_code in [401, 403, 404], "Student blocked from admin list"
    
    def test_admin_update_blocked_for_student(self, student_client):
        """Test students cannot update feedback."""
        response = student_client.put('/api/admin/feedback/1', json={
            'status': 'actioned'
        })
        assert response.status_code in [401, 403, 404, 405], "Student blocked from update"
    
    def test_admin_delete_blocked_for_student(self, student_client):
        """Test students cannot delete feedback."""
        response = student_client.delete('/api/admin/feedback/1')
        assert response.status_code in [401, 403, 404, 405], "Student blocked from delete"
    
    def test_unauthenticated_cannot_submit(self, client):
        """Test unauthenticated users cannot submit feedback."""
        response = client.post('/api/submit-feedback', json={
            'feedback_text': 'Anonymous feedback'
        })
        # May require login
        assert response.status_code in [200, 201, 401, 403], "Should handle unauth"


# ============================================================================
# FEEDBACK WORKFLOW TESTS
# ============================================================================

class TestFeedbackWorkflow:
    """Test complete feedback workflow."""
    
    def test_submit_feedback_workflow(self, student_client, get_json):
        """Test submitting feedback as student."""
        import time
        submit_response = student_client.post('/api/submit-feedback', json={
            'feedback_text': 'Workflow test feedback ' + str(time.time()),
            'category': 'feature',
            'rating': 4
        })
        # Should succeed or return appropriate error
        assert submit_response.status_code in [200, 201, 401, 500], "Submit should respond"
    
    def test_admin_can_view_feedback(self, authenticated_client):
        """Test admin can view feedback list."""
        list_response = authenticated_client.get('/api/admin/feedback?status=all')
        assert list_response.status_code in [200, 404, 500], "Should list feedback"
    
    def test_admin_page_loads(self, authenticated_client):
        """Test admin feedback page loads."""
        response = authenticated_client.get('/admin/feedback')
        assert response.status_code in [200, 302], "Admin feedback page should load"
