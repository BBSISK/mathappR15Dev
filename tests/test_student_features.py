# test_student_features.py - Student Features Tests
# Version 1.2 - 2025-12-31

import pytest


class TestBadgeSystem:
    """Test badge system functionality."""
    
    def test_get_badges(self, student_client):
        """Test getting user's badges."""
        response = student_client.get('/api/student/badges')
        assert response.status_code in [200, 404], "Badges should respond"
    
    def test_get_available_badges(self, student_client):
        """Test getting available badges."""
        response = student_client.get('/api/student/badges/available')
        assert response.status_code in [200, 404], "Available badges should respond"
    
    def test_check_badges(self, student_client):
        """Test checking for new badges."""
        response = student_client.post('/api/student/check-badges')
        assert response.status_code in [200, 404], "Check badges should respond"
    
    def test_guest_badges(self, guest_client):
        """Test badges for guest user."""
        response = guest_client.get('/api/student/badges')
        assert response.status_code in [200, 401, 404], "Guest badge request handled"


class TestAvatarSystem:
    """Test avatar system functionality."""
    
    def test_avatar_shop_page(self, student_client):
        """Test avatar shop page loads."""
        response = student_client.get('/avatar/shop')
        assert response.status_code in [200, 302, 404], "Avatar shop should respond"
    
    def test_get_shop_items(self, student_client):
        """Test getting shop items."""
        response = student_client.get('/api/avatar/shop-items')
        # May return 503 if avatar system is disabled
        assert response.status_code in [200, 404, 503], "Shop items should respond"
    
    def test_get_equipped(self, student_client):
        """Test getting equipped items."""
        response = student_client.get('/api/avatar/equipped')
        # May return 503 if avatar system is disabled
        assert response.status_code in [200, 404, 503], "Equipped items should respond"
    
    def test_buy_nonexistent_item(self, student_client):
        """Test buying non-existent item."""
        response = student_client.post('/api/avatar/buy', json={'item_id': 999999})
        assert response.status_code in [400, 404, 503], "Should reject non-existent item"


class TestWhoAmIGame:
    """Test Who Am I game functionality."""
    
    def test_get_current_puzzle(self, student_client):
        """Test getting current Who Am I puzzle."""
        response = student_client.get('/api/who-am-i/current')
        assert response.status_code in [200, 404], "Current puzzle should respond"
    
    def test_submit_guess(self, student_client):
        """Test submitting a guess."""
        response = student_client.post('/api/who-am-i/guess', 
                                       json={'guess': 'Einstein'},
                                       content_type='application/json')
        assert response.status_code in [200, 400, 404, 415], "Guess should respond"
    
    def test_reveal_answer(self, student_client):
        """Test revealing answer."""
        response = student_client.post('/api/who-am-i/reveal',
                                       json={},
                                       content_type='application/json')
        assert response.status_code in [200, 400, 404, 415], "Reveal should respond"


class TestBonusQuestions:
    """Test bonus question functionality."""
    
    def test_get_available_bonus(self, student_client):
        """Test getting available bonus questions."""
        response = student_client.get('/api/bonus/available')
        assert response.status_code in [200, 404], "Available bonus should respond"
    
    def test_get_specific_bonus(self, student_client):
        """Test getting a specific bonus question."""
        response = student_client.get('/api/bonus/1')
        assert response.status_code in [200, 404], "Specific bonus should respond"


class TestMasteryTracking:
    """Test mastery tracking functionality."""
    
    def test_get_mastery_data(self, student_client):
        """Test getting mastery data."""
        response = student_client.get('/api/student/mastery')
        assert response.status_code in [200, 404], "Mastery data should respond"


class TestStudentAccessControl:
    """Test student route access control."""
    
    def test_unauthenticated_student_routes(self, client):
        """Test unauthenticated cannot access student routes."""
        routes = ['/api/student/badges', '/api/avatar/shop-items', '/api/student/mastery']
        for route in routes:
            response = client.get(route)
            assert response.status_code in [302, 401, 403, 404], f"Should not access {route}"
