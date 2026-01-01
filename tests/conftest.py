# conftest.py - PyTest Configuration and Fixtures for AgentMath
# Version 1.3 - 2025-12-31
# 
# FIXED: Uses 'email' instead of 'username' for login (matches actual API)
# All fixtures and helpers are in this single file.

import pytest
import sys
import os

# Add parent directory and tests directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


# ============================================================================
# HELPER FUNCTIONS - Available as fixtures
# ============================================================================

def _get_json(response):
    """Safely extract JSON from response."""
    try:
        return response.get_json()
    except:
        return None


def _assert_status(response, expected_status, message=""):
    """Assert response has expected status code with helpful error."""
    actual = response.status_code
    if actual != expected_status:
        try:
            body = response.get_json() or response.data.decode('utf-8')[:200]
        except:
            body = str(response.data)[:200]
        raise AssertionError(
            f"{message}\nExpected status {expected_status}, got {actual}\nResponse: {body}"
        )


def _assert_json_success(response, message=""):
    """Assert response is successful JSON."""
    _assert_status(response, 200, message)
    data = _get_json(response)
    assert data is not None, f"{message}\nResponse is not valid JSON"
    success = (
        data.get('success') == True or 
        data.get('status') == 'success' or
        'error' not in data
    )
    if not success and 'error' in data:
        raise AssertionError(f"{message}\nAPI returned error: {data.get('error')}")


def _assert_json_error(response, expected_status=400, message=""):
    """Assert response is an error response."""
    _assert_status(response, expected_status, message)


class _TestDataGenerator:
    """Generate test data for various scenarios."""
    
    @staticmethod
    def valid_user_data():
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        return {
            'email': f'test_{timestamp}@example.com',
            'password': 'TestPass123!',
            'full_name': f'Test User {timestamp}',
            'role': 'student'
        }
    
    @staticmethod
    def invalid_emails():
        return ['', 'notanemail', '@nodomain.com', 'no@domain', 'spaces in@email.com', 'a' * 300 + '@example.com']
    
    @staticmethod
    def invalid_passwords():
        return ['', 'short', '12345678', 'abcdefgh']
    
    @staticmethod
    def sql_injection_payloads():
        return ["'; DROP TABLE users; --", "1' OR '1'='1", "admin'--", "1; DELETE FROM questions WHERE 1=1", "' UNION SELECT * FROM users --"]
    
    @staticmethod
    def xss_payloads():
        return ['<script>alert("xss")</script>', '<img src="x" onerror="alert(1)">', 'javascript:alert(1)', '<svg onload="alert(1)">', '"><script>alert(1)</script>']
    
    @staticmethod
    def boundary_values():
        return {
            'empty_string': '', 'single_char': 'a', 'max_length': 'a' * 10000,
            'unicode': '数学テスト', 'emoji': '🎓📚✅❌',
            'special_chars': '!@#$%^&*()_+-=[]{}|;:\'",.<>?/',
            'negative_number': -1, 'zero': 0, 'large_number': 999999999,
            'float': 3.14159, 'null_string': 'null', 'undefined_string': 'undefined',
        }


# ============================================================================
# FIXTURES FOR HELPER FUNCTIONS
# ============================================================================

@pytest.fixture
def get_json():
    """Provide get_json helper to tests."""
    return _get_json

@pytest.fixture
def assert_status():
    """Provide assert_status helper to tests."""
    return _assert_status

@pytest.fixture
def assert_json_success():
    """Provide assert_json_success helper to tests."""
    return _assert_json_success

@pytest.fixture
def assert_json_error():
    """Provide assert_json_error helper to tests."""
    return _assert_json_error

@pytest.fixture
def test_data():
    """Provide test data generator to tests."""
    return _TestDataGenerator()


# ============================================================================
# APPLICATION FIXTURES
# ============================================================================

@pytest.fixture(scope='session')
def app():
    """Create application for testing with test configuration."""
    from app import app as flask_app
    
    original_config = {
        'TESTING': flask_app.config.get('TESTING'),
        'WTF_CSRF_ENABLED': flask_app.config.get('WTF_CSRF_ENABLED'),
        'SQLALCHEMY_DATABASE_URI': flask_app.config.get('SQLALCHEMY_DATABASE_URI'),
    }
    
    flask_app.config['TESTING'] = True
    flask_app.config['WTF_CSRF_ENABLED'] = False
    flask_app.config['LOGIN_DISABLED'] = False
    
    yield flask_app
    
    for key, value in original_config.items():
        if value is not None:
            flask_app.config[key] = value


@pytest.fixture(scope='function')
def client(app):
    """Create a test client for each test function."""
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture(scope='function')
def authenticated_client(app):
    """Create an authenticated test client (admin user)."""
    with app.test_client() as client:
        with app.app_context():
            client.post('/api/login', json={
                'email': 'admin@agentmath.app',
                'password': 'admin123'
            })
            yield client


@pytest.fixture(scope='function')
def teacher_client(app):
    """Create a test client authenticated as teacher."""
    with app.test_client() as client:
        with app.app_context():
            client.post('/api/login', json={
                'email': 'teacher.2003@palmerstowncs.ie',
                'password': 'teacher'
            })
            yield client


@pytest.fixture(scope='function')
def student_client(app):
    """Create a test client authenticated as student."""
    with app.test_client() as client:
        with app.app_context():
            client.post('/api/login', json={
                'email': 'student.2004@palmerstowncs.ie',
                'password': 'student'
            })
            yield client


@pytest.fixture(scope='function')
def guest_client(app):
    """Create a test client with guest session."""
    with app.test_client() as client:
        with app.app_context():
            client.post('/api/casual-guest-start')
            yield client


# ============================================================================
# PYTEST CONFIGURATION
# ============================================================================

def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line("markers", "slow: marks tests as slow running")
    config.addinivalue_line("markers", "security: marks security-related tests")
    config.addinivalue_line("markers", "integration: marks integration tests")
    config.addinivalue_line("markers", "corner_case: marks corner case tests")
    config.addinivalue_line("markers", "auth: marks authentication tests")
    config.addinivalue_line("markers", "api: marks API endpoint tests")
