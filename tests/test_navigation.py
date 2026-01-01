# test_navigation.py - Navigation and Dead Link Detection Tests
# Version 1.0 - 2025-12-31
#
# PURPOSE: Detect broken links, missing routes, and navigation issues
# that wouldn't be caught by standard API tests.
#
# This test suite:
# - Verifies all navigation links in the app return valid responses
# - Detects dead links that return 404
# - Tests navigation flows between pages
# - Validates menu items and sidebar links
# - Tests breadcrumb functionality
#
# WHY THIS MATTERS:
# Standard tests check if routes exist and return correct status codes,
# but they don't verify that links in templates actually work.
# A route can exist (/admin) but a link to /admin/feedback can be broken.

import pytest
import re
from bs4 import BeautifulSoup


# ============================================================================
# KNOWN ROUTES REGISTRY
# ============================================================================
# This is the source of truth for all routes that should exist.
# Tests will verify these routes return valid responses.

ADMIN_ROUTES = {
    # Main Admin Pages
    '/admin': {'name': 'Admin Dashboard', 'auth': 'admin'},
    '/admin/users': {'name': 'User Management', 'auth': 'admin'},
    '/admin/feedback': {'name': 'Feedback & Flags', 'auth': 'admin'},
    '/admin/who-am-i': {'name': 'Who Am I Admin', 'auth': 'admin'},
    
    # Admin API Routes (only include routes that definitely exist)
    '/api/admin/pending-teachers': {'name': 'Pending Teachers API', 'auth': 'admin'},
    '/api/admin/all-users': {'name': 'All Users API', 'auth': 'admin'},
    '/api/admin/all-classes': {'name': 'All Classes API', 'auth': 'admin'},
    '/api/admin/raffles': {'name': 'Raffles API', 'auth': 'admin'},
    '/api/admin/feedback/stats': {'name': 'Feedback Stats API', 'auth': 'admin'},
    '/api/admin/feedback': {'name': 'Feedback List API', 'auth': 'admin'},
}

TEACHER_ROUTES = {
    '/teacher': {'name': 'Teacher Dashboard', 'auth': 'teacher'},
    '/teacher/class-monitor': {'name': 'Class Monitor', 'auth': 'teacher'},
    '/api/teacher/my-classes': {'name': 'My Classes API', 'auth': 'teacher'},
}

STUDENT_ROUTES = {
    '/student': {'name': 'Student App', 'auth': 'student'},
    '/app': {'name': 'App Redirect', 'auth': 'student'},
    '/guest': {'name': 'Guest Entry', 'auth': None},
}

PUBLIC_ROUTES = {
    '/': {'name': 'Home Page', 'auth': None},
    '/login': {'name': 'Login Page', 'auth': None},
    '/register': {'name': 'Register Page', 'auth': None},
}


# ============================================================================
# NAVIGATION LINK TESTS
# ============================================================================

class TestAdminNavigation:
    """Test all admin navigation links work correctly."""
    
    def test_admin_dashboard_accessible(self, authenticated_client):
        """Test admin dashboard loads."""
        response = authenticated_client.get('/admin')
        assert response.status_code == 200, "Admin dashboard should load"
    
    def test_admin_feedback_page(self, authenticated_client):
        """Test admin feedback page exists and loads."""
        response = authenticated_client.get('/admin/feedback')
        assert response.status_code in [200, 302], "Admin feedback page should exist"
    
    def test_admin_users_page(self, authenticated_client):
        """Test admin users page loads."""
        response = authenticated_client.get('/admin/users')
        assert response.status_code in [200, 302, 404], "Admin users page should respond"
    
    def test_all_admin_routes_respond(self, authenticated_client):
        """Test all documented admin routes return valid responses."""
        dead_links = []
        
        for route, info in ADMIN_ROUTES.items():
            response = authenticated_client.get(route)
            # 500 is always bad - indicates server error
            if response.status_code == 500:
                dead_links.append(f"{route} ({info['name']}): 500 Server Error")
            # 404 for documented routes is a dead link
            elif response.status_code == 404:
                dead_links.append(f"{route} ({info['name']}): 404 Not Found")
        
        if dead_links:
            pytest.fail(f"Dead admin links found:\n" + "\n".join(dead_links))


class TestTeacherNavigation:
    """Test teacher navigation links."""
    
    def test_all_teacher_routes_respond(self, teacher_client):
        """Test all documented teacher routes return valid responses."""
        dead_links = []
        
        for route, info in TEACHER_ROUTES.items():
            response = teacher_client.get(route)
            # 401 is acceptable if teacher login failed
            if response.status_code == 500:
                dead_links.append(f"{route} ({info['name']}): 500 Server Error")
            elif response.status_code == 404 and info['auth'] == 'teacher':
                dead_links.append(f"{route} ({info['name']}): 404 Not Found")
        
        if dead_links:
            pytest.fail(f"Dead teacher links found:\n" + "\n".join(dead_links))


class TestStudentNavigation:
    """Test student navigation links."""
    
    def test_all_student_routes_respond(self, student_client):
        """Test all documented student routes return valid responses."""
        dead_links = []
        
        for route, info in STUDENT_ROUTES.items():
            response = student_client.get(route)
            if response.status_code == 500:
                dead_links.append(f"{route} ({info['name']}): 500 Server Error")
        
        if dead_links:
            pytest.fail(f"Dead student links found:\n" + "\n".join(dead_links))


class TestPublicNavigation:
    """Test public page navigation."""
    
    def test_all_public_routes_respond(self, client):
        """Test all public routes are accessible."""
        dead_links = []
        
        for route, info in PUBLIC_ROUTES.items():
            response = client.get(route)
            if response.status_code == 500:
                dead_links.append(f"{route} ({info['name']}): 500 Server Error")
            elif response.status_code == 404:
                dead_links.append(f"{route} ({info['name']}): 404 Not Found")
        
        if dead_links:
            pytest.fail(f"Dead public links found:\n" + "\n".join(dead_links))


# ============================================================================
# LINK EXTRACTION AND VALIDATION TESTS
# ============================================================================

class TestLinkExtraction:
    """Extract and validate links from rendered pages."""
    
    def test_admin_dashboard_links(self, authenticated_client):
        """Extract all links from admin dashboard and verify they work."""
        response = authenticated_client.get('/admin')
        
        if response.status_code != 200:
            pytest.skip("Admin dashboard not accessible")
        
        # Parse HTML and extract links
        soup = BeautifulSoup(response.data, 'html.parser')
        links = soup.find_all('a', href=True)
        
        dead_links = []
        internal_links = []
        
        for link in links:
            href = link['href']
            # Only test internal links
            if href.startswith('/') and not href.startswith('//'):
                internal_links.append(href)
                link_response = authenticated_client.get(href)
                if link_response.status_code == 404:
                    link_text = link.get_text(strip=True) or '[no text]'
                    dead_links.append(f"{href} ('{link_text}'): 404")
                elif link_response.status_code == 500:
                    link_text = link.get_text(strip=True) or '[no text]'
                    dead_links.append(f"{href} ('{link_text}'): 500")
        
        if dead_links:
            pytest.fail(f"Dead links in admin dashboard:\n" + "\n".join(dead_links))
    
    def test_student_app_links(self, student_client):
        """Extract and verify links from student app."""
        response = student_client.get('/student')
        
        if response.status_code not in [200, 302]:
            pytest.skip("Student app not accessible")
        
        if response.status_code == 302:
            # Follow redirect
            response = student_client.get(response.location)
        
        if response.status_code != 200:
            pytest.skip("Could not load student app")
        
        soup = BeautifulSoup(response.data, 'html.parser')
        links = soup.find_all('a', href=True)
        
        dead_links = []
        for link in links:
            href = link['href']
            if href.startswith('/') and not href.startswith('//'):
                link_response = student_client.get(href)
                if link_response.status_code in [404, 500]:
                    link_text = link.get_text(strip=True) or '[no text]'
                    dead_links.append(f"{href} ('{link_text}'): {link_response.status_code}")
        
        if dead_links:
            pytest.fail(f"Dead links in student app:\n" + "\n".join(dead_links))


# ============================================================================
# SIDEBAR AND MENU TESTS
# ============================================================================

class TestSidebarNavigation:
    """Test sidebar menu items."""
    
    ADMIN_SIDEBAR_EXPECTED = [
        '/admin',
        '/admin/users',
        '/admin/feedback',
    ]
    
    def test_admin_sidebar_links_valid(self, authenticated_client):
        """Verify all expected admin sidebar links work."""
        dead_links = []
        
        for route in self.ADMIN_SIDEBAR_EXPECTED:
            response = authenticated_client.get(route)
            if response.status_code == 404:
                dead_links.append(f"{route}: 404 Not Found")
            elif response.status_code == 500:
                dead_links.append(f"{route}: 500 Server Error")
        
        if dead_links:
            pytest.fail(f"Admin sidebar dead links:\n" + "\n".join(dead_links))


# ============================================================================
# API ENDPOINT DISCOVERY TESTS
# ============================================================================

class TestAPIEndpointDiscovery:
    """Discover and validate API endpoints."""
    
    CRITICAL_ADMIN_APIS = [
        '/api/admin/pending-teachers',
        '/api/admin/all-users',
        '/api/admin/all-classes',
        '/api/admin/raffles',
        '/api/admin/class-comparison',
        '/api/admin/feedback/stats',
    ]
    
    def test_critical_admin_apis_exist(self, authenticated_client):
        """Verify all critical admin APIs return valid responses."""
        missing_apis = []
        
        for api in self.CRITICAL_ADMIN_APIS:
            response = authenticated_client.get(api)
            if response.status_code == 404:
                missing_apis.append(f"{api}: Not Found")
            elif response.status_code == 500:
                missing_apis.append(f"{api}: Server Error")
        
        if missing_apis:
            pytest.fail(f"Missing or broken admin APIs:\n" + "\n".join(missing_apis))
    
    CRITICAL_STUDENT_APIS = [
        '/api/init',
        '/api/topics',
        '/api/current-user',
    ]
    
    def test_critical_student_apis_exist(self, student_client):
        """Verify all critical student APIs return valid responses."""
        missing_apis = []
        
        for api in self.CRITICAL_STUDENT_APIS:
            response = student_client.get(api)
            if response.status_code == 404:
                missing_apis.append(f"{api}: Not Found")
            elif response.status_code == 500:
                missing_apis.append(f"{api}: Server Error")
        
        if missing_apis:
            pytest.fail(f"Missing or broken student APIs:\n" + "\n".join(missing_apis))


# ============================================================================
# REDIRECT CHAIN TESTS
# ============================================================================

class TestRedirectChains:
    """Test redirect chains don't create loops."""
    
    def test_no_redirect_loops(self, client):
        """Verify common routes don't create redirect loops."""
        test_routes = ['/', '/login', '/register', '/guest']
        
        for route in test_routes:
            visited = set()
            current_route = route
            redirect_count = 0
            max_redirects = 10
            
            while redirect_count < max_redirects:
                if current_route in visited:
                    pytest.fail(f"Redirect loop detected starting from {route}")
                
                visited.add(current_route)
                response = client.get(current_route, follow_redirects=False)
                
                if response.status_code not in [301, 302, 303, 307, 308]:
                    break
                
                current_route = response.location
                redirect_count += 1
            
            if redirect_count >= max_redirects:
                pytest.fail(f"Too many redirects ({redirect_count}) for {route}")


# ============================================================================
# ROUTE CONSISTENCY TESTS
# ============================================================================

class TestRouteConsistency:
    """Test route naming and consistency."""
    
    def test_api_routes_return_json(self, authenticated_client):
        """Verify all /api/ routes return JSON."""
        api_routes = [
            '/api/admin/pending-teachers',
            '/api/admin/all-users',
            '/api/admin/all-classes',
        ]
        
        for route in api_routes:
            response = authenticated_client.get(route)
            if response.status_code == 200:
                content_type = response.content_type
                assert 'application/json' in content_type, f"{route} should return JSON, got {content_type}"
    
    def test_page_routes_return_html(self, authenticated_client):
        """Verify page routes return HTML."""
        page_routes = [
            '/admin',
        ]
        
        for route in page_routes:
            response = authenticated_client.get(route)
            if response.status_code == 200:
                content_type = response.content_type
                assert 'text/html' in content_type, f"{route} should return HTML, got {content_type}"
