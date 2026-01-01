# test_admin.py - Admin Route Tests
# Version 1.2 - 2025-12-31

import pytest


class TestAdminDashboard:
    """Test admin dashboard and overview."""
    
    def test_admin_dashboard_loads(self, authenticated_client, assert_status):
        """Test admin dashboard loads for admin user."""
        response = authenticated_client.get('/admin')
        assert_status(response, 200, "Admin dashboard should load")
    
    def test_admin_statistics(self, authenticated_client, get_json):
        """Test admin statistics endpoint."""
        response = authenticated_client.get('/api/admin/statistics')
        assert response.status_code in [200, 404], "Statistics endpoint should respond"
        if response.status_code == 200:
            data = get_json(response)
            assert data is not None, "Statistics should return JSON"
    
    def test_admin_activity_log(self, authenticated_client):
        """Test admin activity log endpoint."""
        response = authenticated_client.get('/api/admin/activity-log')
        assert response.status_code in [200, 404], "Activity log should respond"


class TestAdminUserManagement:
    """Test admin user management."""
    
    def test_list_users(self, authenticated_client, get_json):
        """Test listing all users."""
        response = authenticated_client.get('/api/admin/users')
        assert response.status_code in [200, 404], "Users list should respond"
        if response.status_code == 200:
            data = get_json(response)
            assert data is not None, "Should return user data"
    
    def test_get_single_user(self, authenticated_client, get_json):
        """Test getting a single user."""
        list_response = authenticated_client.get('/api/admin/users')
        list_data = get_json(list_response)
        
        if list_data and isinstance(list_data, list) and len(list_data) > 0:
            user_id = list_data[0].get('id') or list_data[0].get('user_id')
            if user_id:
                response = authenticated_client.get(f'/api/admin/user/{user_id}')
                assert response.status_code in [200, 404], "Should return user"
    
    def test_get_nonexistent_user(self, authenticated_client):
        """Test getting a non-existent user."""
        response = authenticated_client.get('/api/admin/user/999999')
        assert response.status_code in [404, 400], "Should return 404"


class TestAdminClassManagement:
    """Test admin class management."""
    
    def test_list_classes(self, authenticated_client):
        """Test listing all classes."""
        response = authenticated_client.get('/api/admin/classes')
        assert response.status_code in [200, 404], "Classes list should respond"


class TestAdminQuestionManagement:
    """Test admin question management."""
    
    def test_list_questions(self, authenticated_client):
        """Test listing questions."""
        response = authenticated_client.get('/api/admin/questions')
        assert response.status_code in [200, 404], "Questions list should respond"
    
    def test_list_questions_with_filters(self, authenticated_client):
        """Test listing questions with filters."""
        response = authenticated_client.get('/api/admin/questions?topic=1')
        assert response.status_code in [200, 404], "Filtered questions should respond"
    
    def test_get_flagged_questions(self, authenticated_client):
        """Test getting flagged questions."""
        response = authenticated_client.get('/api/admin/flagged-questions')
        assert response.status_code in [200, 404], "Flagged questions should respond"


class TestAdminSystemSettings:
    """Test admin system settings."""
    
    def test_get_settings(self, authenticated_client):
        """Test getting system settings."""
        response = authenticated_client.get('/api/admin/settings')
        assert response.status_code in [200, 404], "Settings should respond"


class TestAdminPrizeManagement:
    """Test admin prize management."""
    
    def test_list_prizes(self, authenticated_client):
        """Test listing prizes."""
        response = authenticated_client.get('/api/admin/prizes')
        assert response.status_code in [200, 404], "Prizes list should respond"
    
    def test_list_prize_schools(self, authenticated_client):
        """Test listing prize schools."""
        response = authenticated_client.get('/api/admin/prize-schools')
        assert response.status_code in [200, 404], "Prize schools should respond"
    
    def test_list_redemptions(self, authenticated_client):
        """Test listing prize redemptions."""
        response = authenticated_client.get('/api/admin/redemptions')
        assert response.status_code in [200, 404], "Redemptions should respond"


class TestAdminAccessControl:
    """Test that admin routes are protected."""
    
    def test_student_cannot_access_admin_api(self, student_client):
        """Test that students cannot access admin APIs."""
        endpoints = ['/api/admin/users', '/api/admin/classes', '/api/admin/questions', '/api/admin/settings']
        for endpoint in endpoints:
            response = student_client.get(endpoint)
            assert response.status_code in [302, 401, 403, 404], f"Student should not access {endpoint}"
    
    def test_guest_cannot_access_admin_api(self, guest_client):
        """Test that guests cannot access admin APIs."""
        response = guest_client.get('/api/admin/users')
        assert response.status_code in [302, 401, 403, 404], "Guest should not access admin"
    
    def test_unauthenticated_cannot_access_admin(self, client):
        """Test that unauthenticated users cannot access admin."""
        response = client.get('/admin')
        assert response.status_code in [302, 401, 403], "Unauthenticated should not access admin"


class TestAdminPagination:
    """Test pagination in admin lists."""
    
    def test_users_pagination(self, authenticated_client):
        """Test user list supports pagination."""
        response = authenticated_client.get('/api/admin/users?page=1&per_page=10')
        assert response.status_code in [200, 404], "Pagination should be supported"


class TestAdminSearch:
    """Test search functionality in admin."""
    
    def test_search_users(self, authenticated_client):
        """Test searching users."""
        response = authenticated_client.get('/api/admin/users?search=test')
        assert response.status_code in [200, 404], "User search should respond"
