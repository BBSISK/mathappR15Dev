# AgentMath Automated Test Suite

## Version 1.0 - 2025-12-31

A comprehensive automated test suite for the AgentMath application after the Phase 7-11 refactoring.

---

## Overview

This test suite covers:
- **357 routes** across 10 blueprints
- **Authentication & Authorization** tests
- **Core Quiz API** tests
- **Admin, Teacher, Student** functionality tests
- **Interactive Learning** tests (Adaptive Quiz, Flow Sums, Pyramids, Code Breaker)
- **Games** tests (Clock Challenge, Racing Car)
- **Prize System** tests
- **Engagement** tests (Flagging, Leaderboards, Weekly Challenge)
- **Passport/ILP** tests
- **Corner Cases & Security** tests (SQL Injection, XSS, Boundary Values)

---

## Quick Start

### 1. Upload Test Suite to PythonAnywhere

Upload the entire `agentmath_tests/` folder to:
```
/home/bbsisk/mathappR15Dev/
```

Your structure should look like:
```
/home/bbsisk/mathappR15Dev/
├── app.py
├── models.py
├── routes/
├── tests/                    # ← Upload this folder
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_core_api.py
│   ├── test_admin.py
│   ├── test_teacher.py
│   ├── test_student_features.py
│   ├── test_interactive.py
│   ├── test_passport.py
│   └── test_corner_cases.py
├── run_tests.py              # ← Upload this file
└── requirements_test.txt     # ← Upload this file
```

### 2. Install Dependencies

In PythonAnywhere Bash console:
```bash
cd /home/bbsisk/mathappR15Dev
pip install -r requirements_test.txt --break-system-packages
```

### 3. Configure Test Credentials

Edit `tests/conftest.py` and update the test account credentials:
```python
# In authenticated_client fixture:
client.post('/api/login', json={
    'username': 'admin',           # Your actual admin username
    'password': 'admin123'         # Your actual admin password
})

# In teacher_client fixture:
client.post('/api/login', json={
    'username': 'teacher_test',    # Your actual teacher username
    'password': 'teacher123'       # Your actual teacher password
})

# In student_client fixture:
client.post('/api/login', json={
    'username': 'student_test',    # Your actual student username
    'password': 'student123'       # Your actual student password
})
```

### 4. Run Tests

```bash
cd /home/bbsisk/mathappR15Dev
python run_tests.py
```

---

## Command Line Options

```bash
# Run all tests
python run_tests.py

# Run with verbose output
python run_tests.py --verbose

# Run quick tests (skip slow ones)
python run_tests.py --quick

# Run only security tests
python run_tests.py --security

# Run only corner case tests
python run_tests.py --corner-cases

# Generate HTML report
python run_tests.py --html

# Run specific test file
python run_tests.py --specific auth
python run_tests.py --specific admin
python run_tests.py --specific core_api
python run_tests.py --specific corner_cases

# Stop on first failure
python run_tests.py --stop-on-fail

# Combine options
python run_tests.py --verbose --html --security
```

---

## Test Files

| File | Tests | Description |
|------|-------|-------------|
| `test_auth.py` | ~25 | Login, logout, registration, guest access, role-based access |
| `test_core_api.py` | ~20 | Topics, questions, quiz attempts, progress tracking |
| `test_admin.py` | ~25 | Admin dashboard, user/class/question management |
| `test_teacher.py` | ~15 | Teacher dashboard, class management, student progress |
| `test_student_features.py` | ~20 | Badges, avatar, Who Am I, bonus questions |
| `test_interactive.py` | ~30 | Adaptive quiz, Flow Sums, Pyramids, Code Breaker, Games |
| `test_passport.py` | ~15 | Passport display, weekly planner, ILP, PWA |
| `test_corner_cases.py` | ~60 | SQL injection, XSS, boundary values, malformed requests |

**Total: ~210 automated tests**

---

## Test Categories

Tests are marked with categories for selective running:

| Marker | Description | Command |
|--------|-------------|---------|
| `@pytest.mark.security` | Security-related tests | `--security` |
| `@pytest.mark.corner_case` | Edge case tests | `--corner-cases` |
| `@pytest.mark.slow` | Slow-running tests | `--quick` excludes these |
| `@pytest.mark.auth` | Authentication tests | |
| `@pytest.mark.api` | API endpoint tests | |

---

## Understanding Test Results

### Passed (.)
Test completed successfully.

### Failed (F)
Test assertion failed. Review the output for details.

### Error (E)
Test encountered an exception. Usually indicates a bug or configuration issue.

### Skipped (s)
Test was skipped (usually due to missing prerequisites).

### Expected Status Codes

Tests accept multiple valid status codes because:
- Some endpoints may return `404` if features are disabled
- Some may return `400` vs `422` for validation errors
- Redirects (`302`) and direct blocks (`401`/`403`) are both valid

---

## Interpreting Failures

### Common Causes

1. **Wrong credentials in conftest.py**
   - Update username/password values

2. **Feature flags disabled**
   - Some tests may fail if features are turned off

3. **Empty database tables**
   - Some tests expect existing data

4. **Route not implemented**
   - Check if endpoint exists in routes/

### Severity Guide

| Status | Meaning |
|--------|---------|
| 500 | **CRITICAL** - Server error, indicates a bug |
| 404 | May be OK if feature is disabled |
| 403 | May be OK for access control tests |
| 400 | Expected for invalid input tests |

---

## HTML Reports

Generate an HTML report for easy viewing:

```bash
python run_tests.py --html
```

This creates a file like `test_report_20251231_143000.html` that you can download and view in a browser.

---

## Running Individual Test Classes

```bash
# Run specific test class
python -m pytest tests/test_auth.py::TestLoginLogout -v

# Run specific test method
python -m pytest tests/test_auth.py::TestLoginLogout::test_login_with_valid_credentials -v
```

---

## Adding New Tests

1. Create a new test file in `tests/` (e.g., `test_new_feature.py`)
2. Import fixtures from `conftest.py`
3. Create test classes and methods
4. Run to verify

Example:
```python
# tests/test_new_feature.py
import pytest
from conftest import assert_status, get_json

class TestNewFeature:
    def test_feature_works(self, student_client):
        response = student_client.get('/api/new-feature')
        assert_status(response, 200, "New feature should work")
```

---

## Troubleshooting

### "Module not found" errors
```bash
pip install pytest pytest-html --break-system-packages
```

### "Import error for app"
Make sure you're running from `/home/bbsisk/mathappR15Dev/`

### Tests hang
Some tests may timeout on slow connections. Use `--timeout=30` if needed.

### "No tests collected"
Check that test files follow naming convention: `test_*.py`

---

## Maintenance

After adding new routes or features:
1. Add corresponding tests
2. Update test credentials if accounts change
3. Run full suite before deployment

---

*Test Suite Version: 1.0*
*Created: 2025-12-31*
*For: AgentMath Post-Refactoring (Phases 7-11)*
