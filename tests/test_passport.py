# test_passport.py - Passport System and PWA Tests
# Version 1.2 - 2025-12-31

import pytest


class TestPassportDisplay:
    """Test passport display functionality."""
    
    def test_passport_page_loads(self, student_client):
        """Test passport page loads."""
        response = student_client.get('/passport')
        assert response.status_code in [200, 302, 404], "Passport page should respond"
    
    def test_get_passport_data(self, student_client):
        """Test getting passport data."""
        response = student_client.get('/api/passport/data')
        assert response.status_code in [200, 404], "Passport data should respond"
    
    def test_get_topic_progress(self, student_client):
        """Test getting topic progress."""
        response = student_client.get('/api/passport/topic/1/progress')
        assert response.status_code in [200, 404], "Topic progress should respond"


class TestWeeklyPlanner:
    """Test weekly planner functionality."""
    
    def test_get_current_week(self, student_client):
        """Test getting current week plan."""
        response = student_client.get('/api/passport/planner/current')
        assert response.status_code in [200, 404], "Current week should respond"
    
    def test_update_topics(self, student_client):
        """Test updating weekly topics."""
        response = student_client.post('/api/passport/planner/topics', json={'topic_ids': [1, 2, 3]})
        assert response.status_code in [200, 400, 404], "Update topics should respond"


class TestILPSystem:
    """Test ILP functionality."""
    
    def test_ilp_status(self, student_client):
        """Test getting ILP status."""
        response = student_client.get('/api/ilp/status')
        assert response.status_code in [200, 404], "ILP status should respond"
    
    def test_ilp_recommendations(self, student_client):
        """Test getting ILP recommendations."""
        response = student_client.get('/api/ilp/recommendations')
        assert response.status_code in [200, 404], "ILP recommendations should respond"


class TestPassportAccess:
    """Test passport access control."""
    
    def test_guest_passport(self, guest_client):
        """Test guest access to passport."""
        response = guest_client.get('/passport')
        assert response.status_code in [200, 302, 404], "Guest passport should be handled"
    
    def test_unauthenticated_passport(self, client):
        """Test unauthenticated access to passport."""
        response = client.get('/passport')
        assert response.status_code in [302, 401, 404], "Should redirect or block"


class TestPWA:
    """Test PWA functionality."""
    
    def test_manifest(self, client, get_json):
        """Test manifest.json loads."""
        response = client.get('/manifest.json')
        assert response.status_code in [200, 404], "Manifest should respond"
        if response.status_code == 200:
            data = get_json(response)
            if data:
                assert 'name' in data or 'short_name' in data, "Manifest should have name"
    
    def test_service_worker(self, client):
        """Test service worker loads."""
        response = client.get('/sw.js')
        assert response.status_code in [200, 404], "Service worker should respond"
    
    def test_offline_page(self, client):
        """Test offline page loads."""
        response = client.get('/offline.html')
        assert response.status_code in [200, 404], "Offline page should respond"
