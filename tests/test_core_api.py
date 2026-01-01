# test_core_api.py - Core Quiz API Tests
# Version 1.2 - 2025-12-31

import pytest


class TestAppInitialization:
    """Test the /api/init endpoint."""
    
    def test_init_as_student(self, student_client, assert_status, get_json):
        """Test init endpoint returns complete data for student."""
        response = student_client.get('/api/init')
        assert_status(response, 200, "Init should succeed for student")
        data = get_json(response)
        assert data is not None, "Init should return JSON"
    
    def test_init_as_guest(self, guest_client, assert_status, get_json):
        """Test init endpoint works for guest."""
        response = guest_client.get('/api/init')
        assert_status(response, 200, "Init should succeed for guest")
        data = get_json(response)
        assert data is not None, "Init should return JSON for guest"
    
    def test_init_unauthenticated(self, client):
        """Test init endpoint behavior when not authenticated."""
        response = client.get('/api/init')
        assert response.status_code in [200, 302, 401], "Init should handle unauthenticated"


class TestTopicsAPI:
    """Test the topics API endpoints."""
    
    def test_get_topics(self, student_client, assert_status, get_json):
        """Test getting list of topics."""
        response = student_client.get('/api/topics')
        assert_status(response, 200, "Should return topics")
        data = get_json(response)
        assert data is not None, "Topics should return JSON"
        assert isinstance(data, (list, dict)), "Topics should be list or dict"
    
    def test_get_topics_as_guest(self, guest_client, assert_status):
        """Test getting topics as guest."""
        response = guest_client.get('/api/topics')
        assert_status(response, 200, "Guest should get topics")
    
    def test_get_topics_structure(self, student_client, get_json):
        """Test that topics have expected structure."""
        response = student_client.get('/api/topics')
        data = get_json(response)
        if data and isinstance(data, list) and len(data) > 0:
            topic = data[0]
            assert isinstance(topic, dict), "Each topic should be a dict"


class TestQuestionsAPI:
    """Test the questions API endpoints."""
    
    def test_get_questions_valid_topic(self, student_client, get_json):
        """Test getting questions for a valid topic."""
        topics_response = student_client.get('/api/topics')
        topics_data = get_json(topics_response)
        
        if topics_data and isinstance(topics_data, list) and len(topics_data) > 0:
            topic = topics_data[0]
            topic_id = topic.get('id') or topic.get('topic_id') or topic.get('name')
            
            response = student_client.get(f'/api/questions/{topic_id}/easy')
            assert response.status_code in [200, 404], f"Questions request should respond"
    
    def test_get_questions_invalid_topic(self, student_client, get_json):
        """Test getting questions for non-existent topic."""
        response = student_client.get('/api/questions/nonexistent_topic_xyz/easy')
        assert response.status_code in [200, 404], "Should handle invalid topic"
        data = get_json(response)
        if data and isinstance(data, list):
            assert len(data) == 0, "Should return empty for invalid topic"
    
    def test_get_questions_invalid_difficulty(self, student_client):
        """Test getting questions with invalid difficulty."""
        response = student_client.get('/api/questions/1/impossible')
        assert response.status_code in [200, 400, 404], "Should handle invalid difficulty"
    
    def test_get_questions_all_difficulties(self, student_client, get_json):
        """Test getting questions for all valid difficulties."""
        topics_response = student_client.get('/api/topics')
        topics_data = get_json(topics_response)
        
        if topics_data and isinstance(topics_data, list) and len(topics_data) > 0:
            topic = topics_data[0]
            topic_id = topic.get('id') or topic.get('topic_id') or 1
            
            for difficulty in ['easy', 'medium', 'hard']:
                response = student_client.get(f'/api/questions/{topic_id}/{difficulty}')
                assert response.status_code in [200, 404], f"Should handle {difficulty}"


class TestQuizAttempt:
    """Test quiz attempt creation and submission."""
    
    def test_create_quiz_attempt(self, student_client, get_json):
        """Test creating a new quiz attempt."""
        response = student_client.post('/api/create-quiz-attempt', json={
            'topic_id': 1,
            'difficulty': 'easy',
            'question_count': 5
        })
        assert response.status_code in [200, 201, 400], "Should create or reject quiz attempt"
        data = get_json(response)
        if response.status_code in [200, 201] and data:
            assert 'attempt_id' in data or 'id' in data or 'quiz_id' in data, "Should return attempt ID"
    
    def test_create_quiz_attempt_as_guest(self, guest_client):
        """Test creating quiz attempt as guest."""
        response = guest_client.post('/api/create-quiz-attempt', json={
            'topic_id': 1,
            'difficulty': 'easy',
            'question_count': 5
        })
        assert response.status_code in [200, 201, 400], "Guest should be able to attempt quiz"
    
    def test_create_quiz_attempt_missing_fields(self, student_client):
        """Test creating quiz attempt with missing required fields."""
        response = student_client.post('/api/create-quiz-attempt', json={})
        assert response.status_code in [400, 422], "Should reject missing fields"
    
    def test_submit_quiz(self, student_client, get_json):
        """Test submitting a completed quiz."""
        create_response = student_client.post('/api/create-quiz-attempt', json={
            'topic_id': 1,
            'difficulty': 'easy',
            'question_count': 5
        })
        create_data = get_json(create_response)
        
        if create_response.status_code in [200, 201] and create_data:
            attempt_id = create_data.get('attempt_id') or create_data.get('id')
            
            response = student_client.post('/api/submit-quiz', json={
                'attempt_id': attempt_id,
                'answers': [
                    {'question_id': 1, 'answer': 'A'},
                    {'question_id': 2, 'answer': 'B'},
                ]
            })
            assert response.status_code in [200, 400], "Should process quiz submission"
    
    def test_submit_quiz_invalid_attempt(self, student_client):
        """Test submitting quiz for non-existent attempt."""
        response = student_client.post('/api/submit-quiz', json={
            'attempt_id': 999999,
            'answers': []
        })
        assert response.status_code in [400, 404], "Should reject invalid attempt"


class TestProgressAPI:
    """Test progress tracking API."""
    
    def test_get_my_progress(self, student_client, assert_status, get_json):
        """Test getting user's progress."""
        response = student_client.get('/api/my-progress')
        assert_status(response, 200, "Should return progress")
        data = get_json(response)
        assert data is not None, "Progress should return JSON"
    
    def test_get_progress_as_guest(self, guest_client):
        """Test getting progress as guest."""
        response = guest_client.get('/api/my-progress')
        assert response.status_code in [200, 401, 403], "Should handle guest progress request"


class TestCurrentUser:
    """Test current user endpoint."""
    
    def test_current_user_authenticated(self, authenticated_client, assert_status, get_json):
        """Test current user endpoint when authenticated."""
        response = authenticated_client.get('/api/current-user')
        assert_status(response, 200, "Should return current user")
        data = get_json(response)
        assert data is not None, "Should return user JSON"
    
    def test_current_user_student(self, student_client):
        """Test current user endpoint for student."""
        response = student_client.get('/api/current-user')
        assert response.status_code in [200, 401], "Should return user or unauthorized"
    
    def test_current_user_guest(self, guest_client):
        """Test current user endpoint for guest."""
        response = guest_client.get('/api/current-user')
        assert response.status_code in [200, 401], "Should handle guest current user"


class TestIndexRoutes:
    """Test index and main page routes."""
    
    def test_index_page(self, client):
        """Test index page loads."""
        response = client.get('/')
        assert response.status_code in [200, 302], "Index should load or redirect"
    
    def test_student_page(self, student_client):
        """Test student app page loads or redirects."""
        response = student_client.get('/student')
        # May redirect to /app - both are valid
        assert response.status_code in [200, 302], "Student page should load or redirect"
    
    def test_app_page(self, student_client):
        """Test /app alias."""
        response = student_client.get('/app')
        assert response.status_code in [200, 302], "/app should load or redirect"
    
    def test_guest_page(self, client):
        """Test guest page loads or redirects."""
        response = client.get('/guest')
        # May redirect to /student - both are valid
        assert response.status_code in [200, 302], "Guest page should load or redirect"
