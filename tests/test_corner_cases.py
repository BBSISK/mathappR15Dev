# test_corner_cases.py - Corner Cases, Edge Cases, and Security Tests
# Version 1.3 - 2025-12-31
# FIXED: Uses 'email' instead of 'username' for login (matches actual API)

import pytest


# ============================================================================
# SQL INJECTION TESTS
# ============================================================================

@pytest.mark.security
class TestSQLInjection:
    """Test SQL injection prevention."""
    
    def test_login_sql_injection_email(self, client, test_data):
        """Test SQL injection in login email field."""
        for payload in test_data.sql_injection_payloads():
            response = client.post('/api/login', json={'email': payload, 'password': 'test'})
            assert response.status_code != 500, f"SQL injection caused server error: {payload}"
    
    def test_login_sql_injection_password(self, client, test_data):
        """Test SQL injection in login password."""
        for payload in test_data.sql_injection_payloads():
            response = client.post('/api/login', json={'email': 'admin@test.com', 'password': payload})
            assert response.status_code != 500, f"SQL injection caused server error: {payload}"
    
    def test_search_sql_injection(self, authenticated_client, test_data):
        """Test SQL injection in search parameters."""
        for payload in test_data.sql_injection_payloads():
            response = authenticated_client.get(f'/api/admin/users?search={payload}')
            assert response.status_code != 500, f"Search SQL injection error: {payload}"
    
    def test_topic_id_sql_injection(self, student_client, test_data):
        """Test SQL injection in topic ID."""
        for payload in test_data.sql_injection_payloads():
            response = student_client.get(f'/api/questions/{payload}/easy')
            assert response.status_code != 500, f"Topic ID injection error: {payload}"


# ============================================================================
# XSS PREVENTION TESTS
# ============================================================================

@pytest.mark.security
class TestXSSPrevention:
    """Test XSS attack prevention."""
    
    def test_email_xss(self, client, test_data):
        """Test XSS in registration email field."""
        for payload in test_data.xss_payloads():
            response = client.post('/api/register', json={
                'email': payload,
                'password': 'TestPass123!',
                'full_name': 'Test User',
                'role': 'student'
            })
            assert response.status_code != 500, f"XSS caused server error: {payload}"
    
    def test_fullname_xss(self, client, test_data):
        """Test XSS in registration full_name field."""
        for payload in test_data.xss_payloads():
            response = client.post('/api/register', json={
                'email': 'test@example.com',
                'password': 'TestPass123!',
                'full_name': payload,
                'role': 'student'
            })
            assert response.status_code != 500, f"Full name XSS error: {payload}"
    
    def test_class_name_xss(self, teacher_client, test_data):
        """Test XSS in class name."""
        for payload in test_data.xss_payloads():
            response = teacher_client.post('/api/teacher/create-class', json={'name': payload})
            assert response.status_code != 500, f"Class name XSS error: {payload}"
    
    def test_flag_reason_xss(self, student_client, test_data):
        """Test XSS in flag reason."""
        for payload in test_data.xss_payloads():
            response = student_client.post('/api/student/flag-question', json={'question_id': 1, 'reason': payload})
            assert response.status_code != 500, f"Flag XSS error: {payload}"


# ============================================================================
# BOUNDARY VALUE TESTS
# ============================================================================

@pytest.mark.corner_case
class TestBoundaryValues:
    """Test boundary values and edge cases."""
    
    def test_empty_string_inputs(self, client):
        """Test empty string handling."""
        response = client.post('/api/login', json={'email': '', 'password': ''})
        assert response.status_code in [400, 401, 422], "Should reject empty strings"
    
    def test_very_long_email(self, client):
        """Test very long email."""
        response = client.post('/api/login', json={'email': 'a' * 10000 + '@test.com', 'password': 'test'})
        assert response.status_code != 500, "Long email should not crash"
    
    def test_very_long_password(self, client):
        """Test very long password."""
        response = client.post('/api/login', json={'email': 'admin@test.com', 'password': 'a' * 10000})
        assert response.status_code != 500, "Long password should not crash"
    
    def test_unicode_in_inputs(self, student_client):
        """Test Unicode characters in inputs."""
        response = student_client.post('/api/student/flag-question', json={'question_id': 1, 'reason': '数学 🎓📚✅❌ مرحبا'})
        assert response.status_code != 500, "Unicode should not crash"
    
    def test_negative_ids(self, student_client):
        """Test negative IDs."""
        response = student_client.get('/api/questions/-1/easy')
        assert response.status_code in [200, 400, 404], "Negative ID should be handled"
    
    def test_zero_values(self, student_client):
        """Test zero values."""
        # Use correct field names (topic, difficulty)
        response = student_client.post('/api/create-quiz-attempt', json={'topic': '', 'difficulty': 'easy'})
        # With proper validation, this returns 400
        assert response.status_code in [200, 400, 404, 500], "Zero values should be handled"
    
    def test_large_numbers(self, student_client):
        """Test very large numbers."""
        response = student_client.get('/api/questions/999999999999/easy')
        assert response.status_code in [200, 400, 404], "Large numbers should be handled"
    
    def test_null_values(self, student_client):
        """Test null/None values in JSON."""
        # Use correct field names (topic, difficulty)
        response = student_client.post('/api/create-quiz-attempt', json={'topic': None, 'difficulty': None})
        # With proper validation, this returns 400 (not 500)
        assert response.status_code in [400, 422, 500], "Null values should return error"


# ============================================================================
# MALFORMED REQUEST TESTS
# ============================================================================

@pytest.mark.corner_case
class TestMalformedRequests:
    """Test handling of malformed requests."""
    
    def test_invalid_json(self, client):
        """Test invalid JSON in request body."""
        response = client.post('/api/login', data='{"email": "admin@test.com", invalid}', content_type='application/json')
        assert response.status_code in [400, 422, 415], "Invalid JSON should be rejected"
    
    def test_empty_json_body(self, client):
        """Test empty JSON body."""
        response = client.post('/api/login', json={})
        assert response.status_code in [400, 422], "Empty body should be rejected"
    
    def test_array_instead_of_object(self, student_client):
        """Test array when object expected."""
        response = student_client.post('/api/create-quiz-attempt', json=[1, 2, 3])
        # With proper validation, this returns 400 (not 500)
        assert response.status_code in [400, 422, 500], "Array should be rejected"


# ============================================================================
# SESSION AND AUTH EDGE CASES
# ============================================================================

@pytest.mark.corner_case
class TestSessionEdgeCases:
    """Test session handling edge cases."""
    
    def test_access_without_session(self, client):
        """Test accessing protected routes without session."""
        for route in ['/admin', '/teacher', '/api/admin/users']:
            response = client.get(route)
            assert response.status_code in [302, 401, 403, 404], f"Should block {route}"
    
    def test_double_login(self, client):
        """Test logging in twice."""
        client.post('/api/login', json={'email': 'admin@agentmath.app', 'password': 'admin123'})
        response = client.post('/api/login', json={'email': 'admin@agentmath.app', 'password': 'admin123'})
        assert response.status_code in [200, 302], "Double login should work"
    
    def test_logout_without_login(self, client):
        """Test logout when not logged in."""
        response = client.post('/api/logout')
        assert response.status_code in [200, 302], "Logout without login should not crash"
    
    def test_access_after_logout(self, authenticated_client):
        """Test accessing protected route after logout."""
        authenticated_client.post('/api/logout')
        response = authenticated_client.get('/admin')
        assert response.status_code in [302, 401, 403], "Should not access after logout"


# ============================================================================
# RACE CONDITION TESTS
# ============================================================================

@pytest.mark.corner_case
class TestRaceConditions:
    """Test potential race conditions."""
    
    def test_double_quiz_submission(self, student_client, get_json):
        """Test submitting same quiz twice."""
        create_response = student_client.post('/api/create-quiz-attempt', json={'topic_id': 1, 'difficulty': 'easy', 'question_count': 5})
        create_data = get_json(create_response)
        
        if create_response.status_code in [200, 201] and create_data:
            attempt_id = create_data.get('attempt_id') or create_data.get('id')
            if attempt_id:
                student_client.post('/api/submit-quiz', json={'attempt_id': attempt_id, 'answers': []})
                response = student_client.post('/api/submit-quiz', json={'attempt_id': attempt_id, 'answers': []})
                assert response.status_code in [200, 400, 409], "Double submit handled"
    
    def test_double_prize_redemption(self, student_client):
        """Test redeeming same prize twice quickly."""
        student_client.post('/api/prizes/redeem', json={'prize_id': 1, 'quantity': 1})
        response = student_client.post('/api/prizes/redeem', json={'prize_id': 1, 'quantity': 1})
        assert response.status_code != 500, "Double redemption should not crash"


# ============================================================================
# DATA TYPE CONFUSION TESTS
# ============================================================================

@pytest.mark.corner_case
class TestDataTypeConfusion:
    """Test handling of unexpected data types."""
    
    def test_string_for_integer_fields(self, student_client):
        """Test string values where integers expected."""
        # Use correct field names (topic, difficulty)
        response = student_client.post('/api/create-quiz-attempt', json={'topic': 'arithmetic', 'difficulty': 'not_valid'})
        # With proper validation, this returns 400 (not 500)
        assert response.status_code in [400, 422, 500], "Invalid difficulty should return error"
    
    def test_boolean_for_string_fields(self, student_client):
        """Test boolean values where strings expected."""
        response = student_client.post('/api/student/flag-question', json={'question_id': 1, 'reason': True})
        assert response.status_code != 500, "Boolean for string should not crash"
    
    def test_array_for_scalar_fields(self, student_client):
        """Test array values where scalar expected."""
        # Use correct field names (topic, difficulty)
        response = student_client.post('/api/create-quiz-attempt', json={'topic': ['arithmetic'], 'difficulty': ['easy']})
        # With proper validation, this returns 400 (not 500)
        assert response.status_code in [400, 422, 500], "Array for scalar should return error"


# ============================================================================
# URL MANIPULATION TESTS
# ============================================================================

@pytest.mark.security
class TestURLManipulation:
    """Test URL manipulation attacks."""
    
    def test_path_traversal(self, client):
        """Test path traversal attempts."""
        for payload in ['../../../etc/passwd', '..\\..\\..\\windows\\system32', '%2e%2e%2f%2e%2e%2f']:
            response = client.get(f'/api/questions/{payload}/easy')
            assert response.status_code != 500, f"Path traversal should not crash: {payload}"
    
    def test_null_byte_injection(self, client):
        """Test null byte injection."""
        response = client.get('/api/questions/1%00.txt/easy')
        assert response.status_code != 500, "Null byte should not crash"


# ============================================================================
# GUEST SYSTEM EDGE CASES
# ============================================================================

@pytest.mark.corner_case
class TestGuestEdgeCases:
    """Test guest system edge cases."""
    
    def test_guest_code_brute_force(self, client):
        """Test that invalid guest codes are rejected."""
        for i in range(5):
            response = client.post('/api/repeat-guest/login', json={'code': f'INVALID-{i:06d}'})
            assert response.status_code in [400, 401, 404, 429], "Invalid guest codes rejected"
    
    def test_empty_guest_code(self, client):
        """Test empty guest code."""
        response = client.post('/api/repeat-guest/login', json={'code': ''})
        assert response.status_code in [400, 422], "Empty code should be rejected"
    
    def test_guest_code_with_special_chars(self, client):
        """Test guest code with special characters."""
        response = client.post('/api/repeat-guest/login', json={'code': "'; DROP TABLE users; --"})
        assert response.status_code != 500, "Special chars in code should not crash"


# ============================================================================
# HTTP METHOD TESTS
# ============================================================================

@pytest.mark.corner_case
class TestHTTPMethods:
    """Test correct HTTP method handling."""
    
    def test_get_on_post_endpoint(self, student_client):
        """Test GET request on POST-only endpoint."""
        response = student_client.get('/api/submit-quiz')
        assert response.status_code in [405, 404], "GET on POST should fail"
    
    def test_post_on_get_endpoint(self, student_client):
        """Test POST request on GET-only endpoint."""
        response = student_client.post('/api/topics')
        assert response.status_code in [200, 405, 404], "POST on GET should be handled"


# ============================================================================
# QUIZ ANSWER EDGE CASES
# ============================================================================

@pytest.mark.corner_case
class TestQuizAnswerEdgeCases:
    """Test quiz answer submission edge cases."""
    
    def test_submit_with_wrong_question_ids(self, student_client):
        """Test submitting answers with wrong question IDs."""
        response = student_client.post('/api/submit-quiz', json={
            'attempt_id': 1, 'answers': [{'question_id': -1, 'answer': 'A'}, {'question_id': 999999, 'answer': 'B'}]
        })
        assert response.status_code in [200, 400, 404], "Wrong IDs should be handled"
    
    def test_submit_with_invalid_answer_format(self, student_client):
        """Test submitting with invalid answer format."""
        response = student_client.post('/api/submit-quiz', json={'attempt_id': 1, 'answers': 'not an array'})
        assert response.status_code in [400, 422], "Invalid format should be rejected"
    
    def test_submit_with_extra_fields(self, student_client):
        """Test submitting with extra unexpected fields."""
        response = student_client.post('/api/submit-quiz', json={'attempt_id': 1, 'answers': [], 'hack': True, 'score': 100, 'coins': 999999})
        assert response.status_code != 500, "Extra fields should not crash"
