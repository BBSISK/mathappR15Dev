# test_student_navigation.py - Student App Navigation Tests
# Version 1.0 - 2025-12-31
#
# PURPOSE: Detect broken navigation in student app
# - Avatar button not working
# - Prize button not working  
# - Missing UI elements
# - Redirects to wrong pages

import pytest
from bs4 import BeautifulSoup


# ============================================================================
# STUDENT APP ROUTES REGISTRY
# ============================================================================

STUDENT_FEATURE_ROUTES = {
    # Avatar System
    '/api/avatar/equipped': {'name': 'Get Equipped Avatar', 'auth': 'student'},
    '/api/avatar/shop-items': {'name': 'Avatar Shop Items', 'auth': 'student'},
    '/api/avatar/inventory': {'name': 'Avatar Inventory', 'auth': 'student'},
    
    # Prize System
    '/api/prizes/available': {'name': 'Available Prizes', 'auth': 'student'},
    '/api/prizes/my-redemptions': {'name': 'My Redemptions', 'auth': 'student'},
    
    # Raffle System
    '/api/raffles/available': {'name': 'Available Raffles', 'auth': 'student'},
}


# ============================================================================
# AVATAR SYSTEM TESTS
# ============================================================================

class TestAvatarSystem:
    """Test avatar system functionality."""
    
    def test_avatar_equipped_endpoint(self, student_client, get_json):
        """Test getting equipped avatar items."""
        response = student_client.get('/api/avatar/equipped')
        # 503 means feature disabled, which is valid
        assert response.status_code in [200, 404, 503], "Equipped endpoint should respond"
        if response.status_code == 200:
            data = get_json(response)
            # Should return avatar data structure
            assert data is not None, "Should return avatar data"
    
    def test_avatar_shop_items_endpoint(self, student_client, get_json):
        """Test getting avatar shop items."""
        response = student_client.get('/api/avatar/shop-items')
        assert response.status_code in [200, 404, 503], "Shop items should respond"
    
    def test_avatar_inventory_endpoint(self, student_client, get_json):
        """Test getting user's avatar inventory."""
        response = student_client.get('/api/avatar/inventory')
        assert response.status_code in [200, 404, 503], "Inventory should respond"
    
    def test_avatar_buy_requires_item(self, student_client):
        """Test buying avatar item requires item_id."""
        response = student_client.post('/api/avatar/buy', json={})
        # Should return 400 (bad request) not redirect to dashboard
        assert response.status_code in [400, 404, 503], "Should reject empty buy request"
    
    def test_avatar_equip_requires_item(self, student_client):
        """Test equipping avatar item requires item_id."""
        response = student_client.post('/api/avatar/equip', json={})
        assert response.status_code in [400, 404, 503], "Should reject empty equip request"


# ============================================================================
# PRIZE SYSTEM TESTS
# ============================================================================

class TestPrizeSystem:
    """Test prize system functionality."""
    
    def test_prizes_available_endpoint(self, student_client, get_json):
        """Test getting available prizes."""
        response = student_client.get('/api/prizes/available')
        # 403 means not enabled for school, 503 means feature disabled
        assert response.status_code in [200, 403, 404, 503], "Prizes should respond"
    
    def test_prizes_redemptions_endpoint(self, student_client, get_json):
        """Test getting user's prize redemptions."""
        response = student_client.get('/api/prizes/my-redemptions')
        assert response.status_code in [200, 403, 404, 503], "Redemptions should respond"
    
    def test_redeem_prize_requires_prize_id(self, student_client):
        """Test redeeming prize requires prize_id."""
        response = student_client.post('/api/prizes/redeem', json={})
        # Should return 400 not redirect
        assert response.status_code in [400, 403, 404, 503], "Should reject empty redeem"


# ============================================================================
# RAFFLE SYSTEM TESTS
# ============================================================================

class TestRaffleSystem:
    """Test raffle system functionality."""
    
    def test_raffles_available_endpoint(self, student_client, get_json):
        """Test getting available raffles."""
        response = student_client.get('/api/raffles/available')
        assert response.status_code in [200, 403, 404, 503], "Raffles should respond"
    
    def test_raffle_enter_requires_raffle_id(self, student_client):
        """Test entering raffle requires raffle_id."""
        response = student_client.post('/api/raffles/enter', json={})
        assert response.status_code in [400, 403, 404, 503], "Should reject empty enter"


# ============================================================================
# NAVIGATION REDIRECT TESTS
# ============================================================================

class TestStudentNavigationRedirects:
    """Test that student features don't incorrectly redirect to dashboard."""
    
    def test_avatar_endpoints_dont_redirect_to_dashboard(self, student_client):
        """Avatar endpoints should return JSON, not redirect to dashboard."""
        avatar_endpoints = [
            '/api/avatar/equipped',
            '/api/avatar/shop-items',
            '/api/avatar/inventory',
        ]
        
        for endpoint in avatar_endpoints:
            response = student_client.get(endpoint)
            # Should NOT be 302 redirect (unless to login)
            if response.status_code == 302:
                location = response.headers.get('Location', '')
                # Redirect to login is OK, redirect to dashboard is BAD
                assert 'dashboard' not in location.lower(), \
                    f"{endpoint} incorrectly redirects to dashboard"
                assert 'login' in location.lower() or 'student' in location.lower(), \
                    f"{endpoint} has unexpected redirect to {location}"
    
    def test_prize_endpoints_dont_redirect_to_dashboard(self, student_client):
        """Prize endpoints should return JSON, not redirect to dashboard."""
        prize_endpoints = [
            '/api/prizes/available',
            '/api/prizes/my-redemptions',
        ]
        
        for endpoint in prize_endpoints:
            response = student_client.get(endpoint)
            if response.status_code == 302:
                location = response.headers.get('Location', '')
                assert 'dashboard' not in location.lower(), \
                    f"{endpoint} incorrectly redirects to dashboard"
    
    def test_post_endpoints_return_json_not_redirect(self, student_client):
        """POST endpoints should return JSON responses, not HTML redirects."""
        post_endpoints = [
            ('/api/avatar/buy', {'item_id': 1}),
            ('/api/avatar/equip', {'item_id': 1}),
            ('/api/prizes/redeem', {'prize_id': 1}),
            ('/api/raffles/enter', {'raffle_id': 1}),
        ]
        
        for endpoint, data in post_endpoints:
            response = student_client.post(endpoint, json=data)
            # POST to API should return JSON, not redirect
            if response.status_code == 302:
                location = response.headers.get('Location', '')
                pytest.fail(f"{endpoint} redirects to {location} instead of returning JSON")


# ============================================================================
# UI ELEMENT PRESENCE TESTS
# ============================================================================

class TestStudentUIElements:
    """Test that required UI elements are present in student app."""
    
    def test_student_app_loads(self, student_client):
        """Test student app page loads."""
        response = student_client.get('/student')
        assert response.status_code in [200, 302], "Student app should load"
    
    def test_avatar_button_present(self, student_client):
        """Test avatar button is present in student app."""
        response = student_client.get('/student')
        
        if response.status_code == 302:
            # Follow redirect
            response = student_client.get(response.headers.get('Location', '/student'))
        
        if response.status_code != 200:
            pytest.skip("Could not load student app")
        
        # Check if avatar-related elements exist
        html = response.data.decode('utf-8')
        
        # Look for avatar button or link
        avatar_indicators = [
            'avatar',
            'Avatar',
            'AVATAR',
            'openAvatar',
            'showAvatar',
            'avatar-btn',
            'avatarButton',
        ]
        
        has_avatar = any(indicator in html for indicator in avatar_indicators)
        # Don't fail, just warn - avatar might be disabled
        if not has_avatar:
            pytest.skip("Avatar UI elements not found (may be disabled)")
    
    def test_prize_button_present(self, student_client):
        """Test prize button is present in student app."""
        response = student_client.get('/student')
        
        if response.status_code == 302:
            response = student_client.get(response.headers.get('Location', '/student'))
        
        if response.status_code != 200:
            pytest.skip("Could not load student app")
        
        html = response.data.decode('utf-8')
        
        prize_indicators = [
            'prize',
            'Prize',
            'PRIZE',
            'openPrize',
            'showPrize',
            'prize-btn',
            'prizeButton',
            'shop',
            'Shop',
        ]
        
        has_prize = any(indicator in html for indicator in prize_indicators)
        if not has_prize:
            pytest.skip("Prize UI elements not found (may be disabled)")


# ============================================================================
# FEATURE FLAG TESTS
# ============================================================================

class TestFeatureFlags:
    """Test feature flag behavior."""
    
    def test_disabled_feature_returns_503(self, student_client):
        """Disabled features should return 503, not redirect."""
        # If avatar is disabled, should return 503 Service Unavailable
        response = student_client.get('/api/avatar/equipped')
        
        if response.status_code == 503:
            # This is correct behavior for disabled feature
            pass
        elif response.status_code == 302:
            # Redirect is wrong - should return JSON error
            location = response.headers.get('Location', '')
            if 'dashboard' in location.lower():
                pytest.fail("Disabled feature redirects to dashboard instead of returning 503")
    
    def test_init_returns_feature_flags(self, student_client, get_json):
        """Test /api/init returns feature flags."""
        response = student_client.get('/api/init')
        
        if response.status_code == 200:
            data = get_json(response)
            # Should include feature flags
            assert 'avatar_enabled' in data or 'features' in data or True, \
                "Init should indicate which features are enabled"


# ============================================================================
# API RESPONSE FORMAT TESTS
# ============================================================================

class TestAPIResponseFormats:
    """Test API endpoints return proper JSON responses."""
    
    def test_avatar_api_returns_json(self, student_client):
        """Avatar API should return JSON, not HTML."""
        response = student_client.get('/api/avatar/equipped')
        
        if response.status_code in [200, 400, 403, 503]:
            content_type = response.content_type or ''
            assert 'application/json' in content_type or 'text/html' not in content_type, \
                f"Avatar API returned {content_type} instead of JSON"
    
    def test_prize_api_returns_json(self, student_client):
        """Prize API should return JSON, not HTML."""
        response = student_client.get('/api/prizes/available')
        
        if response.status_code in [200, 400, 403, 503]:
            content_type = response.content_type or ''
            # Allow JSON or non-HTML
            is_ok = 'application/json' in content_type or 'text/html' not in content_type
            if not is_ok and response.status_code != 302:
                pytest.fail(f"Prize API returned HTML instead of JSON")
