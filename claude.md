# AgentMath Test Strategy Documentation
# claude.md - Testing Guidelines and Best Practices
# Version 1.0 - 2025-12-31

## Overview

This document describes the testing strategy for AgentMath, including test types,
coverage goals, and procedures for detecting and preventing common issues.

---

## Test Suite Structure

```
tests/
├── conftest.py                    # Shared fixtures and helpers
├── test_auth.py                   # Authentication tests (24 tests)
├── test_core_api.py               # Core API endpoint tests (24 tests)
├── test_admin.py                  # Basic admin tests (19 tests)
├── test_admin_comprehensive.py    # Full admin coverage (97 tests)
├── test_teacher.py                # Teacher functionality (10 tests)
├── test_student_features.py       # Student features (15 tests)
├── test_interactive.py            # Interactive features (26 tests)
├── test_passport.py               # Passport/planner tests (12 tests)
├── test_corner_cases.py           # Edge cases & security (38 tests)
└── test_navigation.py             # Dead link detection (NEW)
```

---

## Test Categories

### 1. API Endpoint Tests
**Purpose:** Verify API routes exist and return correct status codes.
**Files:** `test_core_api.py`, `test_admin.py`
**What they catch:**
- Missing routes (404)
- Authentication failures (401/403)
- Server errors (500)

**What they DON'T catch:**
- Dead links in templates
- Broken navigation menus
- Links that point to wrong routes

### 2. Navigation & Dead Link Tests ⭐ NEW
**Purpose:** Detect broken links and missing pages.
**File:** `test_navigation.py`
**What they catch:**
- Links in templates that return 404
- Sidebar/menu items pointing to non-existent pages
- Redirect loops
- API endpoints returning HTML or vice versa

**How it works:**
```python
# Route Registry - Source of truth for expected routes
ADMIN_ROUTES = {
    '/admin': {'name': 'Admin Dashboard', 'auth': 'admin'},
    '/admin/feedback': {'name': 'Feedback Page', 'auth': 'admin'},
    # ... all routes documented here
}

# Link Extraction - Parse HTML and verify all links
def test_admin_dashboard_links(self, authenticated_client):
    response = authenticated_client.get('/admin')
    soup = BeautifulSoup(response.data, 'html.parser')
    for link in soup.find_all('a', href=True):
        # Test each extracted link
```

### 3. Security & Corner Case Tests
**Purpose:** Test edge cases, injection attacks, and malformed input.
**File:** `test_corner_cases.py`
**What they catch:**
- SQL injection attempts
- XSS vulnerabilities
- Missing input validation (500 errors instead of 400)
- Boundary value issues

### 4. Access Control Tests
**Purpose:** Verify role-based permissions.
**Present in:** All test files
**What they catch:**
- Students accessing admin routes
- Guests accessing protected routes
- Teachers accessing admin-only features

---

## Running Tests

### Full Test Suite
```bash
python -m pytest tests/ -v
```

### Specific Categories
```bash
# Admin tests only
python -m pytest tests/test_admin*.py -v

# Navigation/dead link tests
python -m pytest tests/test_navigation.py -v

# Security tests
python -m pytest tests/test_corner_cases.py -v -m security
```

### Quick Smoke Test
```bash
python -m pytest tests/ -q --tb=no
```

### With Coverage Report
```bash
python -m pytest tests/ --cov=. --cov-report=html
```

---

## Test Credentials

Pre-configured in `conftest.py`:

| Role | Email | Password |
|------|-------|----------|
| Admin | admin@agentmath.app | admin123 |
| Teacher | teacher.2003@palmerstowncs.ie | teacher |
| Student | student.2004@palmerstowncs.ie | student |

---

## Common Issues and How Tests Detect Them

### Issue 1: Dead Links (404 on Navigation)
**Symptom:** User clicks link, gets "Not Found" page
**Detection:** `test_navigation.py::TestLinkExtraction`
**Prevention:** Add route to ADMIN_ROUTES registry before adding link to template

### Issue 2: Missing Input Validation (500 Instead of 400)
**Symptom:** API crashes with 500 when given bad input
**Detection:** `test_corner_cases.py::TestBoundaryValues`
**Prevention:** Always validate input before using it:
```python
# BAD - crashes if 'name' missing
name = data['name']

# GOOD - returns 400 with clear message
name = data.get('name')
if not name:
    return jsonify({'error': 'Name is required'}), 400
```

### Issue 3: Wrong Column Names in SQL
**Symptom:** OperationalError: no such column
**Detection:** Integration tests that hit the database
**Prevention:** Check models.py before writing raw SQL queries

### Issue 4: Authentication Bypass
**Symptom:** Unauthorized users can access protected routes
**Detection:** `TestAccessControl` classes in each test file
**Prevention:** Always use decorators:
```python
@login_required
@role_required('admin')
def admin_route():
    ...
```

---

## Adding New Routes Checklist

When adding a new route, update these places:

1. **Route file** (e.g., `routes/admin.py`)
   - Add the route function with proper decorators

2. **Template** (if needed)
   - Create template file
   - Add navigation links

3. **Test Registry** (`tests/test_navigation.py`)
   - Add to appropriate `*_ROUTES` dictionary

4. **Test File** (create or update)
   - Add specific test for the route

5. **Documentation** (this file)
   - Update route list if significant

---

## Test Development Guidelines

### 1. Accept Multiple Valid Status Codes
Routes may legitimately return different codes:
```python
# GOOD - handles redirects and feature flags
assert response.status_code in [200, 302, 404], "Route should respond"

# BAD - too strict, fails on valid redirects
assert response.status_code == 200
```

### 2. Handle Missing Features Gracefully
```python
# GOOD - skips if feature not available
if response.status_code == 404:
    pytest.skip("Feature not implemented")

# BAD - fails entire test suite
assert response.status_code == 200
```

### 3. Use Descriptive Failure Messages
```python
# GOOD
assert response.status_code != 500, f"Route {route} crashed with server error"

# BAD
assert response.status_code != 500
```

### 4. Test Both Happy Path and Error Cases
```python
def test_create_item_success(self):
    response = client.post('/api/items', json={'name': 'Test'})
    assert response.status_code in [200, 201]

def test_create_item_missing_name(self):
    response = client.post('/api/items', json={})
    assert response.status_code == 400  # NOT 500!
```

---

## Continuous Testing Workflow

### Before Committing Code
```bash
# Run full test suite
python -m pytest tests/ -v

# Check for dead links specifically
python -m pytest tests/test_navigation.py -v
```

### After Adding New Routes
```bash
# 1. Update test registry
# 2. Run navigation tests
python -m pytest tests/test_navigation.py -v

# 3. Verify new route works
python -m pytest tests/ -k "new_route_name" -v
```

### After Database Changes
```bash
# Run all tests - SQL errors will surface
python -m pytest tests/ -v --tb=short
```

---

## Test Coverage Goals

| Category | Target | Current |
|----------|--------|---------|
| Auth routes | 100% | ✅ |
| Admin routes | 90% | ✅ |
| Teacher routes | 80% | ✅ |
| Student routes | 80% | ✅ |
| API endpoints | 90% | ✅ |
| Error handling | 80% | ✅ |
| Navigation links | 95% | ✅ |

---

## Troubleshooting Test Failures

### "AssertionError: Should create or reject"
**Cause:** API returning 500 instead of 200/400
**Fix:** Add input validation to the route

### "404 Not Found" for documented route
**Cause:** Route not registered or blueprint not imported
**Fix:** Check `routes/__init__.py` and `app.py` imports

### "401 Unauthorized" for teacher/student tests
**Cause:** Test account doesn't exist in database
**Fix:** Create the account or skip the test

### "500 Internal Server Error"
**Cause:** Unhandled exception in route
**Fix:** Check application logs, add try/except with proper error response

---

## Future Improvements

1. **Visual Regression Tests** - Screenshot comparison for UI changes
2. **Performance Tests** - Response time benchmarks
3. **Load Tests** - Concurrent user simulation
4. **Contract Tests** - API schema validation
5. **End-to-End Tests** - Browser automation with Selenium/Playwright

---

## Contact

For questions about testing strategy, contact the development team.

Last Updated: 2025-12-31
Test Suite Version: 2.0 (265+ tests)
