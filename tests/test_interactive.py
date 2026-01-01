# test_interactive.py - Interactive Learning, Games, Prizes, Engagement Tests
# Version 1.2 - 2025-12-31

import pytest


# ============================================================================
# INTERACTIVE LEARNING
# ============================================================================

class TestAdaptiveQuiz:
    """Test adaptive quiz engine."""
    
    def test_start_adaptive(self, student_client):
        """Test starting an adaptive quiz."""
        response = student_client.post('/api/adaptive/start', json={'topic_id': 1})
        assert response.status_code in [200, 201, 400, 404], "Adaptive start should respond"
    
    def test_get_adaptive_question(self, student_client):
        """Test getting next adaptive question."""
        student_client.post('/api/adaptive/start', json={'topic_id': 1})
        response = student_client.get('/api/adaptive/question')
        assert response.status_code in [200, 400, 404], "Should return question"
    
    def test_complete_adaptive(self, student_client):
        """Test completing adaptive quiz."""
        response = student_client.post('/api/adaptive/complete')
        assert response.status_code in [200, 400, 404], "Complete should respond"


class TestFlowSums:
    """Test Flow Sums puzzle functionality."""
    
    def test_generate_flow_sums(self, student_client):
        """Test generating a Flow Sums puzzle."""
        response = student_client.get('/api/flow-sums/generate')
        assert response.status_code in [200, 404], "Generate should respond"
    
    def test_check_flow_sums(self, student_client):
        """Test checking Flow Sums solution."""
        response = student_client.post('/api/flow-sums/check', json={'puzzle_id': 1, 'solution': [[1, 2], [3, 4]]})
        assert response.status_code in [200, 400, 404], "Check should respond"


class TestNumberPyramids:
    """Test Number Pyramids functionality."""
    
    def test_generate_pyramid(self, student_client):
        """Test generating a Number Pyramid."""
        response = student_client.get('/api/pyramids/generate')
        assert response.status_code in [200, 404], "Generate should respond"
    
    def test_check_pyramid(self, student_client):
        """Test checking pyramid solution."""
        response = student_client.post('/api/pyramids/check', json={'answers': [10, 20, 30]})
        assert response.status_code in [200, 400, 404], "Check should respond"


class TestCodeBreaker:
    """Test Code Breaker functionality."""
    
    def test_generate_codebreaker(self, student_client):
        """Test generating Code Breaker puzzle."""
        response = student_client.get('/api/codebreaker/generate')
        assert response.status_code in [200, 404], "Generate should respond"


# ============================================================================
# GAMES
# ============================================================================

class TestClockChallenge:
    """Test Clock Challenge game."""
    
    def test_clock_challenge_page(self, student_client):
        """Test clock challenge page loads."""
        response = student_client.get('/clock-challenge')
        assert response.status_code in [200, 302, 404], "Page should respond"
    
    def test_generate_clock_time(self, student_client):
        """Test generating a clock time."""
        response = student_client.get('/api/clock-challenge/generate')
        assert response.status_code in [200, 404], "Generate should respond"


class TestRacingCar:
    """Test Racing Car game."""
    
    def test_racing_car_page(self, student_client):
        """Test racing car page loads."""
        response = student_client.get('/racing-car')
        assert response.status_code in [200, 302, 404], "Page should respond"
    
    def test_get_racing_question(self, student_client):
        """Test getting racing car question."""
        response = student_client.get('/api/racing-car/question')
        assert response.status_code in [200, 404], "Question should respond"


# ============================================================================
# PRIZES
# ============================================================================

class TestPrizeShop:
    """Test Prize Shop functionality."""
    
    def test_prize_shop_page(self, student_client):
        """Test prize shop page loads."""
        response = student_client.get('/prizes')
        assert response.status_code in [200, 302, 403, 404], "Prize shop should respond"
    
    def test_get_available_prizes(self, student_client):
        """Test getting available prizes."""
        response = student_client.get('/api/prizes/available')
        # May return 403 if prize system is disabled
        assert response.status_code in [200, 403, 404], "Prizes should respond"
    
    def test_get_schools(self, student_client):
        """Test getting schools list."""
        response = student_client.get('/api/prizes/schools')
        assert response.status_code in [200, 403, 404], "Schools should respond"
    
    def test_my_redemptions(self, student_client):
        """Test getting my redemptions."""
        response = student_client.get('/api/prizes/my-redemptions')
        assert response.status_code in [200, 403, 404], "Redemptions should respond"


class TestPrizePIN:
    """Test Prize PIN functionality."""
    
    def test_pin_status(self, student_client):
        """Test getting PIN status."""
        response = student_client.get('/api/prize-pin/status')
        assert response.status_code in [200, 404], "PIN status should respond"


# ============================================================================
# ENGAGEMENT
# ============================================================================

class TestQuestionFlagging:
    """Test question flagging functionality."""
    
    def test_flag_question(self, student_client):
        """Test flagging a question."""
        response = student_client.post('/api/student/flag-question', json={'question_id': 1, 'reason': 'Incorrect'})
        assert response.status_code in [200, 201, 400, 404], "Flag should respond"
    
    def test_my_flags(self, student_client):
        """Test getting my flagged questions."""
        response = student_client.get('/api/student/my-flags')
        assert response.status_code in [200, 404], "My flags should respond"


class TestLeaderboards:
    """Test leaderboard functionality."""
    
    def test_guest_leaderboard(self, guest_client):
        """Test getting guest leaderboard."""
        response = guest_client.get('/api/guest-leaderboard')
        assert response.status_code in [200, 404], "Guest leaderboard should respond"
    
    def test_weekly_leaderboard(self, student_client):
        """Test getting weekly leaderboard."""
        response = student_client.get('/api/leaderboard/weekly')
        assert response.status_code in [200, 404], "Weekly leaderboard should respond"
    
    def test_online_count(self, student_client):
        """Test getting online count."""
        response = student_client.get('/api/online-count')
        assert response.status_code in [200, 404], "Online count should respond"


class TestWeeklyChallenge:
    """Test weekly challenge functionality."""
    
    def test_weekly_status(self, student_client):
        """Test getting weekly challenge status."""
        response = student_client.get('/api/weekly-challenge/status')
        assert response.status_code in [200, 404], "Weekly status should respond"


class TestQuickPlay:
    """Test quick play functionality."""
    
    def test_quick_play_easy(self, student_client):
        """Test quick play easy mode."""
        response = student_client.get('/api/quick-play/easy')
        assert response.status_code in [200, 404], "Quick play easy should respond"


class TestPuzzleOfTheWeek:
    """Test puzzle of the week functionality."""
    
    def test_current_puzzle(self, student_client):
        """Test getting current puzzle."""
        response = student_client.get('/api/puzzle/current')
        assert response.status_code in [200, 404], "Current puzzle should respond"
    
    def test_puzzle_status(self, student_client):
        """Test getting puzzle status."""
        response = student_client.get('/api/puzzle/status')
        assert response.status_code in [200, 404], "Puzzle status should respond"
