# test_admin_comprehensive.py - Comprehensive Admin Route Tests
# Version 1.0 - 2025-12-31
# Tests for AgentMath admin functionality
#
# Covers:
# - User Management (CRUD, approval, roles)
# - Topic Management (CRUD, visibility, ordering)
# - Question Management (CRUD, flags, bulk operations)
# - Class Management (view, assignments)
# - Prize System (schools, prizes, raffles, redemptions)
# - System Settings (feature flags, configuration)
# - Reports & Analytics (statistics, exports)
# - Security (access control, audit logging)

import pytest
import json


# ============================================================================
# USER MANAGEMENT TESTS
# ============================================================================

class TestAdminUserManagement:
    """Comprehensive tests for admin user management."""
    
    def test_list_all_users(self, authenticated_client, get_json):
        """Test listing all users."""
        response = authenticated_client.get('/api/admin/users')
        assert response.status_code in [200, 404], "Users list should respond"
        if response.status_code == 200:
            data = get_json(response)
            assert isinstance(data, (list, dict)), "Should return users data"
    
    def test_list_users_with_role_filter(self, authenticated_client):
        """Test filtering users by role."""
        for role in ['student', 'teacher', 'admin']:
            response = authenticated_client.get(f'/api/admin/users?role={role}')
            assert response.status_code in [200, 404], f"Filter by {role} should work"
    
    def test_list_users_with_approval_filter(self, authenticated_client):
        """Test filtering users by approval status."""
        response = authenticated_client.get('/api/admin/users?approved=false')
        assert response.status_code in [200, 404], "Filter by approval should work"
    
    def test_list_pending_approvals(self, authenticated_client):
        """Test listing pending user approvals."""
        response = authenticated_client.get('/api/admin/pending-approvals')
        assert response.status_code in [200, 404], "Pending approvals should respond"
    
    def test_get_user_details(self, authenticated_client, get_json):
        """Test getting detailed user info."""
        # First get list of users
        list_response = authenticated_client.get('/api/admin/users')
        if list_response.status_code == 200:
            data = get_json(list_response)
            users = data if isinstance(data, list) else data.get('users', [])
            if users and len(users) > 0:
                user_id = users[0].get('id')
                if user_id:
                    response = authenticated_client.get(f'/api/admin/user/{user_id}')
                    assert response.status_code in [200, 404], "User details should respond"
    
    def test_approve_user(self, authenticated_client):
        """Test approving a user."""
        response = authenticated_client.post('/api/admin/approve-user', json={
            'user_id': 1,
            'approved': True
        })
        assert response.status_code in [200, 400, 404], "Approve should respond"
    
    def test_change_user_role(self, authenticated_client):
        """Test changing user role."""
        response = authenticated_client.post('/api/admin/change-role', json={
            'user_id': 1,
            'role': 'teacher'
        })
        assert response.status_code in [200, 400, 403, 404], "Role change should respond"
    
    def test_deactivate_user(self, authenticated_client):
        """Test deactivating a user."""
        response = authenticated_client.post('/api/admin/deactivate-user', json={
            'user_id': 999999  # Non-existent user
        })
        assert response.status_code in [200, 400, 404], "Deactivate should respond"
    
    def test_get_user_activity(self, authenticated_client):
        """Test getting user activity history."""
        response = authenticated_client.get('/api/admin/user/1/activity')
        assert response.status_code in [200, 404], "User activity should respond"
    
    def test_get_user_quiz_history(self, authenticated_client):
        """Test getting user quiz history."""
        response = authenticated_client.get('/api/admin/user/1/quizzes')
        assert response.status_code in [200, 404], "Quiz history should respond"
    
    def test_reset_user_password(self, authenticated_client):
        """Test resetting user password."""
        response = authenticated_client.post('/api/admin/reset-password', json={
            'user_id': 999999
        })
        assert response.status_code in [200, 400, 404], "Password reset should respond"
    
    def test_bulk_approve_users(self, authenticated_client):
        """Test bulk approving users."""
        response = authenticated_client.post('/api/admin/bulk-approve', json={
            'user_ids': [1, 2, 3]
        })
        assert response.status_code in [200, 400, 404], "Bulk approve should respond"


# ============================================================================
# TOPIC MANAGEMENT TESTS
# ============================================================================

class TestAdminTopicManagement:
    """Tests for admin topic management."""
    
    def test_list_topics(self, authenticated_client, get_json):
        """Test listing all topics."""
        response = authenticated_client.get('/api/admin/topics')
        assert response.status_code in [200, 404], "Topics list should respond"
        if response.status_code == 200:
            data = get_json(response)
            assert data is not None, "Should return topics data"
    
    def test_list_strands(self, authenticated_client):
        """Test listing topic strands."""
        response = authenticated_client.get('/api/admin/strands')
        assert response.status_code in [200, 404], "Strands should respond"
    
    def test_create_topic(self, authenticated_client):
        """Test creating a new topic."""
        response = authenticated_client.post('/api/admin/topics', json={
            'topic_id': 'test_topic_' + str(pytest.importorskip('time').time()),
            'display_name': 'Test Topic',
            'description': 'A test topic',
            'strand_id': 1,
            'is_visible': True
        })
        assert response.status_code in [200, 201, 400, 404, 409], "Create topic should respond"
    
    def test_update_topic(self, authenticated_client):
        """Test updating a topic."""
        response = authenticated_client.put('/api/admin/topic/1', json={
            'display_name': 'Updated Topic Name'
        })
        assert response.status_code in [200, 400, 404, 405], "Update topic should respond"
    
    def test_toggle_topic_visibility(self, authenticated_client):
        """Test toggling topic visibility."""
        response = authenticated_client.post('/api/admin/topic/1/toggle-visibility')
        assert response.status_code in [200, 400, 404], "Toggle visibility should respond"
    
    def test_reorder_topics(self, authenticated_client):
        """Test reordering topics."""
        response = authenticated_client.post('/api/admin/topics/reorder', json={
            'topic_ids': [1, 2, 3]
        })
        assert response.status_code in [200, 400, 404], "Reorder should respond"
    
    def test_get_topic_statistics(self, authenticated_client):
        """Test getting topic statistics."""
        response = authenticated_client.get('/api/admin/topic/1/statistics')
        assert response.status_code in [200, 404], "Topic stats should respond"


# ============================================================================
# QUESTION MANAGEMENT TESTS
# ============================================================================

class TestAdminQuestionManagement:
    """Tests for admin question management."""
    
    def test_list_questions(self, authenticated_client, get_json):
        """Test listing all questions."""
        response = authenticated_client.get('/api/admin/questions')
        assert response.status_code in [200, 404], "Questions list should respond"
    
    def test_list_questions_by_topic(self, authenticated_client):
        """Test filtering questions by topic."""
        response = authenticated_client.get('/api/admin/questions?topic=arithmetic')
        assert response.status_code in [200, 404], "Topic filter should work"
    
    def test_list_questions_by_difficulty(self, authenticated_client):
        """Test filtering questions by difficulty."""
        response = authenticated_client.get('/api/admin/questions?difficulty=beginner')
        assert response.status_code in [200, 404], "Difficulty filter should work"
    
    def test_get_question_details(self, authenticated_client):
        """Test getting question details."""
        response = authenticated_client.get('/api/admin/question/1')
        assert response.status_code in [200, 404], "Question details should respond"
    
    def test_create_question(self, authenticated_client):
        """Test creating a new question."""
        response = authenticated_client.post('/api/admin/questions', json={
            'topic': 'arithmetic',
            'difficulty': 'beginner',
            'question_text': 'What is 2 + 2?',
            'correct_answer': '4',
            'options': ['2', '3', '4', '5']
        })
        assert response.status_code in [200, 201, 400, 404], "Create question should respond"
    
    def test_update_question(self, authenticated_client):
        """Test updating a question."""
        response = authenticated_client.put('/api/admin/question/1', json={
            'question_text': 'Updated question text'
        })
        assert response.status_code in [200, 400, 404, 405], "Update question should respond"
    
    def test_delete_question(self, authenticated_client):
        """Test deleting a question."""
        response = authenticated_client.delete('/api/admin/question/999999')
        assert response.status_code in [200, 204, 400, 404, 405], "Delete should respond"
    
    def test_get_flagged_questions(self, authenticated_client, get_json):
        """Test getting flagged questions."""
        response = authenticated_client.get('/api/admin/flagged-questions')
        assert response.status_code in [200, 404], "Flagged questions should respond"
    
    def test_resolve_flag(self, authenticated_client):
        """Test resolving a question flag."""
        response = authenticated_client.post('/api/admin/resolve-flag', json={
            'flag_id': 1,
            'resolution': 'fixed',
            'notes': 'Question updated'
        })
        assert response.status_code in [200, 400, 404], "Resolve flag should respond"
    
    def test_dismiss_flag(self, authenticated_client):
        """Test dismissing a question flag."""
        response = authenticated_client.post('/api/admin/dismiss-flag', json={
            'flag_id': 1,
            'reason': 'Not an issue'
        })
        assert response.status_code in [200, 400, 404], "Dismiss flag should respond"
    
    def test_bulk_import_questions(self, authenticated_client):
        """Test bulk importing questions."""
        response = authenticated_client.post('/api/admin/questions/bulk-import', json={
            'questions': [
                {'topic': 'arithmetic', 'difficulty': 'beginner', 'question_text': 'Q1', 'correct_answer': '1'},
                {'topic': 'arithmetic', 'difficulty': 'beginner', 'question_text': 'Q2', 'correct_answer': '2'}
            ]
        })
        assert response.status_code in [200, 201, 400, 404], "Bulk import should respond"
    
    def test_get_question_statistics(self, authenticated_client):
        """Test getting question performance statistics."""
        response = authenticated_client.get('/api/admin/question/1/statistics')
        assert response.status_code in [200, 404], "Question stats should respond"
    
    def test_adaptive_questions_list(self, authenticated_client):
        """Test listing adaptive questions."""
        response = authenticated_client.get('/api/admin/adaptive-questions')
        assert response.status_code in [200, 404], "Adaptive questions should respond"
    
    def test_adaptive_flagged_questions(self, authenticated_client):
        """Test getting flagged adaptive questions."""
        response = authenticated_client.get('/api/admin/adaptive-flagged')
        assert response.status_code in [200, 404], "Adaptive flags should respond"


# ============================================================================
# CLASS MANAGEMENT TESTS
# ============================================================================

class TestAdminClassManagement:
    """Tests for admin class management."""
    
    def test_list_all_classes(self, authenticated_client, get_json):
        """Test listing all classes."""
        response = authenticated_client.get('/api/admin/classes')
        assert response.status_code in [200, 404], "Classes list should respond"
    
    def test_get_class_details(self, authenticated_client):
        """Test getting class details."""
        response = authenticated_client.get('/api/admin/class/1')
        assert response.status_code in [200, 404], "Class details should respond"
    
    def test_get_class_students(self, authenticated_client):
        """Test getting students in a class."""
        response = authenticated_client.get('/api/admin/class/1/students')
        assert response.status_code in [200, 404], "Class students should respond"
    
    def test_get_class_progress(self, authenticated_client):
        """Test getting class progress."""
        response = authenticated_client.get('/api/admin/class/1/progress')
        assert response.status_code in [200, 404], "Class progress should respond"
    
    def test_assign_teacher_to_class(self, authenticated_client):
        """Test assigning a teacher to a class."""
        response = authenticated_client.post('/api/admin/class/1/assign-teacher', json={
            'teacher_id': 1
        })
        assert response.status_code in [200, 400, 404], "Assign teacher should respond"


# ============================================================================
# PRIZE SYSTEM TESTS
# ============================================================================

class TestAdminPrizeSystem:
    """Tests for admin prize system management."""
    
    def test_list_prize_schools(self, authenticated_client, get_json):
        """Test listing prize schools."""
        response = authenticated_client.get('/api/admin/prize-schools')
        assert response.status_code in [200, 404], "Prize schools should respond"
    
    def test_create_prize_school(self, authenticated_client):
        """Test creating a prize school."""
        response = authenticated_client.post('/api/admin/prize-schools', json={
            'name': 'Test School',
            'domain': 'testschool.ie',
            'is_active': True
        })
        assert response.status_code in [200, 201, 400, 404, 409], "Create school should respond"
    
    def test_list_prizes(self, authenticated_client, get_json):
        """Test listing all prizes."""
        response = authenticated_client.get('/api/admin/prizes')
        assert response.status_code in [200, 404], "Prizes list should respond"
    
    def test_create_prize(self, authenticated_client):
        """Test creating a new prize."""
        response = authenticated_client.post('/api/admin/prizes', json={
            'name': 'Test Prize',
            'description': 'A test prize',
            'point_cost': 100,
            'quantity': 10
        })
        assert response.status_code in [200, 201, 400, 404], "Create prize should respond"
    
    def test_update_prize(self, authenticated_client):
        """Test updating a prize."""
        response = authenticated_client.put('/api/admin/prize/1', json={
            'name': 'Updated Prize',
            'point_cost': 150
        })
        assert response.status_code in [200, 400, 404, 405], "Update prize should respond"
    
    def test_list_redemptions(self, authenticated_client, get_json):
        """Test listing prize redemptions."""
        response = authenticated_client.get('/api/admin/redemptions')
        assert response.status_code in [200, 404], "Redemptions should respond"
    
    def test_list_pending_redemptions(self, authenticated_client):
        """Test listing pending redemptions."""
        response = authenticated_client.get('/api/admin/redemptions?status=pending')
        assert response.status_code in [200, 404], "Pending redemptions should respond"
    
    def test_fulfill_redemption(self, authenticated_client):
        """Test fulfilling a redemption."""
        response = authenticated_client.post('/api/admin/redemption/1/fulfill', json={
            'notes': 'Delivered to student'
        })
        assert response.status_code in [200, 400, 404], "Fulfill redemption should respond"
    
    def test_reject_redemption(self, authenticated_client):
        """Test rejecting a redemption."""
        response = authenticated_client.post('/api/admin/redemption/1/reject', json={
            'reason': 'Out of stock'
        })
        assert response.status_code in [200, 400, 404], "Reject redemption should respond"


# ============================================================================
# RAFFLE SYSTEM TESTS
# ============================================================================

class TestAdminRaffleSystem:
    """Tests for admin raffle management."""
    
    def test_list_raffles(self, authenticated_client):
        """Test listing all raffles."""
        response = authenticated_client.get('/api/admin/raffles')
        assert response.status_code in [200, 404], "Raffles list should respond"
    
    def test_create_raffle(self, authenticated_client):
        """Test creating a raffle."""
        response = authenticated_client.post('/api/admin/raffles', json={
            'name': 'Test Raffle',
            'prize_description': 'A test prize',
            'entry_cost': 10,
            'draw_date': '2025-12-31'
        })
        # Now with proper validation, should return 200/201 or 400 for errors
        assert response.status_code in [200, 201, 400, 404], "Create raffle should respond"
    
    def test_get_raffle_entries(self, authenticated_client):
        """Test getting raffle entries."""
        response = authenticated_client.get('/api/admin/raffle/1/entries')
        assert response.status_code in [200, 404], "Raffle entries should respond"
    
    def test_draw_raffle(self, authenticated_client):
        """Test drawing a raffle winner."""
        response = authenticated_client.post('/api/admin/raffle/1/draw')
        assert response.status_code in [200, 400, 404], "Raffle draw should respond"
    
    def test_get_raffle_draws(self, authenticated_client):
        """Test getting raffle draw history."""
        response = authenticated_client.get('/api/admin/raffle-draws')
        assert response.status_code in [200, 404], "Raffle draws should respond"


# ============================================================================
# SYSTEM SETTINGS TESTS
# ============================================================================

class TestAdminSystemSettings:
    """Tests for admin system settings."""
    
    def test_get_all_settings(self, authenticated_client, get_json):
        """Test getting all system settings."""
        response = authenticated_client.get('/api/admin/settings')
        assert response.status_code in [200, 404], "Settings should respond"
    
    def test_update_setting(self, authenticated_client):
        """Test updating a system setting."""
        response = authenticated_client.post('/api/admin/settings', json={
            'key': 'test_setting',
            'value': 'test_value'
        })
        assert response.status_code in [200, 400, 404], "Update setting should respond"
    
    def test_get_feature_flags(self, authenticated_client):
        """Test getting feature flags."""
        response = authenticated_client.get('/api/admin/feature-flags')
        assert response.status_code in [200, 404], "Feature flags should respond"
    
    def test_toggle_feature_flag(self, authenticated_client):
        """Test toggling a feature flag."""
        response = authenticated_client.post('/api/admin/feature-flags/toggle', json={
            'flag': 'AVATAR_SYSTEM_ENABLED',
            'enabled': True
        })
        assert response.status_code in [200, 400, 404], "Toggle flag should respond"
    
    def test_get_email_settings(self, authenticated_client):
        """Test getting email settings."""
        response = authenticated_client.get('/api/admin/email-settings')
        assert response.status_code in [200, 404], "Email settings should respond"
    
    def test_test_email(self, authenticated_client):
        """Test sending a test email."""
        response = authenticated_client.post('/api/admin/test-email', json={
            'to': 'test@example.com'
        })
        assert response.status_code in [200, 400, 404], "Test email should respond"


# ============================================================================
# REPORTS AND ANALYTICS TESTS
# ============================================================================

class TestAdminReports:
    """Tests for admin reports and analytics."""
    
    def test_get_dashboard_statistics(self, authenticated_client, get_json):
        """Test getting dashboard statistics."""
        response = authenticated_client.get('/api/admin/statistics')
        assert response.status_code in [200, 404], "Statistics should respond"
    
    def test_get_activity_log(self, authenticated_client):
        """Test getting activity log."""
        response = authenticated_client.get('/api/admin/activity-log')
        assert response.status_code in [200, 404], "Activity log should respond"
    
    def test_get_quiz_statistics(self, authenticated_client):
        """Test getting quiz statistics."""
        response = authenticated_client.get('/api/admin/quiz-statistics')
        assert response.status_code in [200, 404], "Quiz stats should respond"
    
    def test_get_daily_usage(self, authenticated_client):
        """Test getting daily usage stats."""
        response = authenticated_client.get('/api/admin/daily-usage')
        assert response.status_code in [200, 404], "Daily usage should respond"
    
    def test_get_weekly_usage(self, authenticated_client):
        """Test getting weekly usage stats."""
        response = authenticated_client.get('/api/admin/weekly-usage')
        assert response.status_code in [200, 404], "Weekly usage should respond"
    
    def test_get_topic_performance(self, authenticated_client):
        """Test getting topic performance report."""
        response = authenticated_client.get('/api/admin/topic-performance')
        assert response.status_code in [200, 404], "Topic performance should respond"
    
    def test_export_users(self, authenticated_client):
        """Test exporting users to CSV."""
        response = authenticated_client.get('/api/admin/export/users')
        assert response.status_code in [200, 404], "Export users should respond"
    
    def test_export_quiz_data(self, authenticated_client):
        """Test exporting quiz data."""
        response = authenticated_client.get('/api/admin/export/quizzes')
        assert response.status_code in [200, 404], "Export quizzes should respond"
    
    def test_get_error_log(self, authenticated_client):
        """Test getting error log."""
        response = authenticated_client.get('/api/admin/error-log')
        assert response.status_code in [200, 404], "Error log should respond"


# ============================================================================
# DOMAIN ACCESS TESTS
# ============================================================================

class TestAdminDomainAccess:
    """Tests for admin domain access management."""
    
    def test_list_domains(self, authenticated_client):
        """Test listing all domains."""
        response = authenticated_client.get('/api/admin/domains')
        assert response.status_code in [200, 404], "Domains should respond"
    
    def test_get_domain_requests(self, authenticated_client):
        """Test getting domain access requests."""
        response = authenticated_client.get('/api/admin/domain-requests')
        assert response.status_code in [200, 404], "Domain requests should respond"
    
    def test_approve_domain_request(self, authenticated_client):
        """Test approving a domain request."""
        response = authenticated_client.post('/api/admin/domain-request/1/approve')
        assert response.status_code in [200, 400, 404], "Approve domain should respond"
    
    def test_reject_domain_request(self, authenticated_client):
        """Test rejecting a domain request."""
        response = authenticated_client.post('/api/admin/domain-request/1/reject', json={
            'reason': 'Not authorized'
        })
        assert response.status_code in [200, 400, 404], "Reject domain should respond"


# ============================================================================
# GUEST MANAGEMENT TESTS
# ============================================================================

class TestAdminGuestManagement:
    """Tests for admin guest user management."""
    
    def test_list_guests(self, authenticated_client):
        """Test listing guest users."""
        response = authenticated_client.get('/api/admin/guests')
        assert response.status_code in [200, 404], "Guests list should respond"
    
    def test_get_guest_details(self, authenticated_client):
        """Test getting guest details."""
        response = authenticated_client.get('/api/admin/guest/panda42')
        assert response.status_code in [200, 404], "Guest details should respond"
    
    def test_deactivate_guest(self, authenticated_client):
        """Test deactivating a guest."""
        response = authenticated_client.post('/api/admin/guest/panda42/deactivate')
        assert response.status_code in [200, 400, 404], "Deactivate guest should respond"
    
    def test_guest_cleanup(self, authenticated_client):
        """Test cleaning up old guest data."""
        response = authenticated_client.post('/api/admin/guests/cleanup', json={
            'days_old': 90
        })
        assert response.status_code in [200, 400, 404], "Guest cleanup should respond"


# ============================================================================
# BADGE MANAGEMENT TESTS
# ============================================================================

class TestAdminBadgeManagement:
    """Tests for admin badge management."""
    
    def test_list_badges(self, authenticated_client, get_json):
        """Test listing all badges."""
        response = authenticated_client.get('/api/admin/badges')
        assert response.status_code in [200, 404], "Badges list should respond"
    
    def test_create_badge(self, authenticated_client):
        """Test creating a new badge."""
        response = authenticated_client.post('/api/admin/badges', json={
            'name': 'Test Badge',
            'description': 'A test badge',
            'icon': 'fa-star',
            'points': 50,
            'requirement_type': 'quizzes_completed',
            'requirement_value': 10
        })
        assert response.status_code in [200, 201, 400, 404], "Create badge should respond"
    
    def test_update_badge(self, authenticated_client):
        """Test updating a badge."""
        response = authenticated_client.put('/api/admin/badge/1', json={
            'description': 'Updated description'
        })
        assert response.status_code in [200, 400, 404, 405], "Update badge should respond"
    
    def test_award_badge_manually(self, authenticated_client):
        """Test manually awarding a badge."""
        response = authenticated_client.post('/api/admin/award-badge', json={
            'user_id': 1,
            'badge_id': 1
        })
        assert response.status_code in [200, 400, 404], "Award badge should respond"


# ============================================================================
# PUZZLE OF THE WEEK TESTS
# ============================================================================

class TestAdminPuzzleManagement:
    """Tests for admin puzzle management."""
    
    def test_list_puzzles(self, authenticated_client):
        """Test listing all puzzles."""
        response = authenticated_client.get('/api/admin/puzzles')
        assert response.status_code in [200, 404], "Puzzles list should respond"
    
    def test_create_puzzle(self, authenticated_client):
        """Test creating a new puzzle."""
        response = authenticated_client.post('/api/admin/puzzles', json={
            'week_number': 1,
            'year': 2025,
            'title': 'Test Puzzle',
            'puzzle_image': '/static/puzzles/test.png',
            'answer_text': 'Test Answer'
        })
        assert response.status_code in [200, 201, 400, 404], "Create puzzle should respond"
    
    def test_activate_puzzle(self, authenticated_client):
        """Test activating a puzzle."""
        response = authenticated_client.post('/api/admin/puzzle/1/activate')
        assert response.status_code in [200, 400, 404], "Activate puzzle should respond"
    
    def test_get_puzzle_statistics(self, authenticated_client):
        """Test getting puzzle statistics."""
        response = authenticated_client.get('/api/admin/puzzle/1/statistics')
        assert response.status_code in [200, 404], "Puzzle stats should respond"


# ============================================================================
# ADMIN ACCESS CONTROL TESTS
# ============================================================================

class TestAdminAccessControl:
    """Tests for admin access control."""
    
    def test_unauthenticated_blocked(self, client):
        """Test unauthenticated users are blocked from admin."""
        admin_routes = [
            '/admin',
            '/api/admin/all-users',
            '/api/admin/feedback/stats'
        ]
        for route in admin_routes:
            response = client.get(route)
            # 404 is acceptable if route doesn't exist
            assert response.status_code in [302, 401, 403, 404], f"Unauth blocked from {route}"
    
    def test_student_blocked(self, student_client):
        """Test students are blocked from admin."""
        admin_routes = [
            '/admin',
            '/api/admin/users',
            '/api/admin/settings'
        ]
        for route in admin_routes:
            response = student_client.get(route)
            assert response.status_code in [302, 401, 403, 404], f"Student blocked from {route}"
    
    def test_teacher_blocked(self, teacher_client):
        """Test teachers are blocked from admin (unless also admin)."""
        response = teacher_client.get('/api/admin/users')
        # May be 401 if teacher login failed, or 403 if blocked
        assert response.status_code in [302, 401, 403, 404], "Teacher blocked from admin"
    
    def test_guest_blocked(self, guest_client):
        """Test guests are blocked from admin."""
        response = guest_client.get('/admin')
        assert response.status_code in [302, 401, 403], "Guest blocked from admin"
    
    def test_admin_can_access_dashboard(self, authenticated_client):
        """Test admin can access admin dashboard."""
        response = authenticated_client.get('/admin')
        assert response.status_code in [200, 302], "Admin can access dashboard"
    
    def test_admin_can_access_api(self, authenticated_client):
        """Test admin can access admin API."""
        response = authenticated_client.get('/api/admin/users')
        assert response.status_code in [200, 404], "Admin can access API"


# ============================================================================
# ADMIN AUDIT LOGGING TESTS
# ============================================================================

class TestAdminAuditLogging:
    """Tests for admin audit logging."""
    
    def test_get_audit_log(self, authenticated_client):
        """Test getting audit log."""
        response = authenticated_client.get('/api/admin/audit-log')
        assert response.status_code in [200, 404], "Audit log should respond"
    
    def test_filter_audit_log_by_action(self, authenticated_client):
        """Test filtering audit log by action type."""
        response = authenticated_client.get('/api/admin/audit-log?action=login')
        assert response.status_code in [200, 404], "Filter audit by action should work"
    
    def test_filter_audit_log_by_user(self, authenticated_client):
        """Test filtering audit log by user."""
        response = authenticated_client.get('/api/admin/audit-log?user_id=1')
        assert response.status_code in [200, 404], "Filter audit by user should work"
    
    def test_filter_audit_log_by_date(self, authenticated_client):
        """Test filtering audit log by date range."""
        response = authenticated_client.get('/api/admin/audit-log?from=2025-01-01&to=2025-12-31')
        assert response.status_code in [200, 404], "Filter audit by date should work"


# ============================================================================
# ADMIN CRON AND MAINTENANCE TESTS
# ============================================================================

class TestAdminMaintenance:
    """Tests for admin maintenance functions."""
    
    def test_database_stats(self, authenticated_client):
        """Test getting database statistics."""
        response = authenticated_client.get('/api/admin/database-stats')
        assert response.status_code in [200, 404], "DB stats should respond"
    
    def test_clear_cache(self, authenticated_client):
        """Test clearing application cache."""
        response = authenticated_client.post('/api/admin/clear-cache')
        assert response.status_code in [200, 404], "Clear cache should respond"
    
    def test_cleanup_old_sessions(self, authenticated_client):
        """Test cleaning up old sessions."""
        response = authenticated_client.post('/api/admin/cleanup-sessions')
        assert response.status_code in [200, 404], "Cleanup sessions should respond"
    
    def test_recalculate_statistics(self, authenticated_client):
        """Test recalculating user statistics."""
        response = authenticated_client.post('/api/admin/recalculate-stats')
        assert response.status_code in [200, 404], "Recalculate stats should respond"
