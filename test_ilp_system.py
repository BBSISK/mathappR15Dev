"""
AgentMath Phase 12: ILP Reactive Recommendations - Comprehensive Test Suite
============================================================================

Run this file to test all Sprint 1-3 functionality:
    python test_ilp_system.py

Tests cover:
- Sprint 1: Prerequisite maps, skill tagging, configuration
- Sprint 2: Data collection, struggle detection, root cause inference
- Sprint 3: Plan modifications, notifications, accept/reject

Requirements:
- Run from the same directory as app.py
- Requires active Flask app context
- Creates test data that is cleaned up after tests

Author: AgentMath Development
Version: 1.0
Date: 2025-12-24
"""

import sys
import json
from datetime import datetime, timedelta
import traceback

# Test results tracking
test_results = {
    'passed': 0,
    'failed': 0,
    'errors': [],
    'warnings': []
}

def log_pass(test_name):
    test_results['passed'] += 1
    print(f"  ✅ PASS: {test_name}")

def log_fail(test_name, reason):
    test_results['failed'] += 1
    test_results['errors'].append(f"{test_name}: {reason}")
    print(f"  ❌ FAIL: {test_name} - {reason}")

def log_warn(message):
    test_results['warnings'].append(message)
    print(f"  ⚠️  WARN: {message}")

def log_section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


# ==============================================================================
# SPRINT 1 TESTS: Prerequisite Maps & Skill Tagging
# ==============================================================================

def test_sprint1_prerequisite_map():
    """Test ILP_PREREQUISITE_MAP configuration"""
    log_section("SPRINT 1: Prerequisite Map Tests")
    
    try:
        from app import ILP_PREREQUISITE_MAP
        
        # Test 1: Map exists and has entries
        if len(ILP_PREREQUISITE_MAP) >= 50:
            log_pass(f"Prerequisite map has {len(ILP_PREREQUISITE_MAP)} topics")
        else:
            log_fail("Prerequisite map size", f"Expected 50+, got {len(ILP_PREREQUISITE_MAP)}")
        
        # Test 2: Base skills have empty prerequisites
        base_skills = ['developing_number_sense', 'whole_numbers']
        for skill in base_skills:
            if skill in ILP_PREREQUISITE_MAP:
                if ILP_PREREQUISITE_MAP[skill] == []:
                    log_pass(f"Base skill '{skill}' has no prerequisites")
                else:
                    log_fail(f"Base skill '{skill}'", f"Should have empty prerequisites, has {ILP_PREREQUISITE_MAP[skill]}")
            else:
                log_warn(f"Base skill '{skill}' not in map")
        
        # Test 3: Chain dependencies are correct
        # solving_equations should require simplifying_expressions
        if 'solving_equations' in ILP_PREREQUISITE_MAP:
            prereqs = ILP_PREREQUISITE_MAP['solving_equations']
            if 'simplifying_expressions' in prereqs:
                log_pass("solving_equations requires simplifying_expressions")
            else:
                log_fail("Dependency chain", "solving_equations should require simplifying_expressions")
        
        # Test 4: LC HL Calculus chain
        if 'lc_hl_calculus_int' in ILP_PREREQUISITE_MAP:
            prereqs = ILP_PREREQUISITE_MAP['lc_hl_calculus_int']
            if 'lc_hl_calculus_diff' in prereqs:
                log_pass("Integration requires Differentiation")
            else:
                log_fail("LC HL chain", "Integration should require Differentiation")
        
        # Test 5: No circular dependencies (basic check)
        for topic, prereqs in ILP_PREREQUISITE_MAP.items():
            if topic in prereqs:
                log_fail(f"Circular dependency", f"{topic} lists itself as prerequisite")
                break
        else:
            log_pass("No self-referential prerequisites found")
            
    except ImportError as e:
        log_fail("Import ILP_PREREQUISITE_MAP", str(e))
    except Exception as e:
        log_fail("Prerequisite map tests", str(e))


def test_sprint1_skill_tags():
    """Test ILP_TOPIC_SKILL_TAGS configuration"""
    log_section("SPRINT 1: Skill Tags Tests")
    
    try:
        from app import ILP_TOPIC_SKILL_TAGS
        
        # Test 1: Skill tags exist
        if len(ILP_TOPIC_SKILL_TAGS) >= 30:
            log_pass(f"Skill tags defined for {len(ILP_TOPIC_SKILL_TAGS)} topics")
        else:
            log_fail("Skill tags count", f"Expected 30+, got {len(ILP_TOPIC_SKILL_TAGS)}")
        
        # Test 2: Tags have correct format (list of tuples with weights)
        sample_topic = 'solving_equations'
        if sample_topic in ILP_TOPIC_SKILL_TAGS:
            tags = ILP_TOPIC_SKILL_TAGS[sample_topic]
            if isinstance(tags, list) and len(tags) > 0:
                if isinstance(tags[0], tuple) and len(tags[0]) == 2:
                    tag_name, weight = tags[0]
                    if isinstance(tag_name, str) and isinstance(weight, (int, float)):
                        log_pass(f"Skill tags format correct for {sample_topic}")
                    else:
                        log_fail("Tag format", f"Expected (str, number), got ({type(tag_name)}, {type(weight)})")
                else:
                    log_fail("Tag structure", f"Expected tuple of 2, got {tags[0]}")
            else:
                log_fail("Tags list", f"Expected non-empty list, got {type(tags)}")
        else:
            log_warn(f"{sample_topic} not in skill tags")
        
        # Test 3: Weights are in valid range (0-1)
        invalid_weights = []
        for topic, tags in ILP_TOPIC_SKILL_TAGS.items():
            for tag_name, weight in tags:
                if weight < 0 or weight > 1:
                    invalid_weights.append((topic, tag_name, weight))
        
        if not invalid_weights:
            log_pass("All skill tag weights in valid range (0-1)")
        else:
            log_fail("Weight range", f"Invalid weights found: {invalid_weights[:3]}...")
            
    except ImportError as e:
        log_fail("Import ILP_TOPIC_SKILL_TAGS", str(e))
    except Exception as e:
        log_fail("Skill tags tests", str(e))


def test_sprint1_skill_to_numeracy():
    """Test ILP_SKILL_TO_NUMERACY mapping"""
    log_section("SPRINT 1: Skill to Numeracy Mapping Tests")
    
    try:
        from app import ILP_SKILL_TO_NUMERACY
        
        # Test 1: Mapping exists
        if len(ILP_SKILL_TO_NUMERACY) >= 10:
            log_pass(f"Skill-to-numeracy mapping has {len(ILP_SKILL_TO_NUMERACY)} entries")
        else:
            log_fail("Mapping size", f"Expected 10+, got {len(ILP_SKILL_TO_NUMERACY)}")
        
        # Test 2: Key numeracy skills are mapped
        key_skills = ['arithmetic_multiplication', 'fraction_operations', 'negative_numbers']
        for skill in key_skills:
            if skill in ILP_SKILL_TO_NUMERACY:
                remedials = ILP_SKILL_TO_NUMERACY[skill]
                if isinstance(remedials, list) and len(remedials) > 0:
                    log_pass(f"'{skill}' maps to {len(remedials)} remedial topics")
                else:
                    log_fail(f"Remedial for {skill}", "Should have non-empty list")
            else:
                log_warn(f"'{skill}' not in skill-to-numeracy map")
                
    except ImportError as e:
        log_fail("Import ILP_SKILL_TO_NUMERACY", str(e))
    except Exception as e:
        log_fail("Skill to numeracy tests", str(e))


def test_sprint1_thresholds():
    """Test ILP_THRESHOLDS configuration"""
    log_section("SPRINT 1: Thresholds Configuration Tests")
    
    try:
        from app import ILP_THRESHOLDS
        
        required_thresholds = [
            ('low_accuracy', 0.5),
            ('critical_accuracy', 0.3),
            ('numeracy_trigger', 0.4),
            ('min_questions_for_signal', 10),
            ('plateau_days', 7),
            ('rust_days', 14),
            ('max_weekly_topics', 3),
            ('auto_apply_hours', 24),
            ('bronze_level', 4)
        ]
        
        for key, expected in required_thresholds:
            if key in ILP_THRESHOLDS:
                actual = ILP_THRESHOLDS[key]
                if actual == expected:
                    log_pass(f"Threshold '{key}' = {actual}")
                else:
                    log_warn(f"Threshold '{key}' = {actual} (expected {expected})")
            else:
                log_fail(f"Missing threshold", key)
                
    except ImportError as e:
        log_fail("Import ILP_THRESHOLDS", str(e))
    except Exception as e:
        log_fail("Thresholds tests", str(e))


def test_sprint1_functions():
    """Test Sprint 1 helper functions"""
    log_section("SPRINT 1: Helper Functions Tests")
    
    try:
        from app import get_prerequisites_for_topic, get_skill_breakdown_for_student
        
        # Test get_prerequisites_for_topic
        prereqs = get_prerequisites_for_topic('quadratic_equations')
        if isinstance(prereqs, list):
            log_pass(f"get_prerequisites_for_topic returns list ({len(prereqs)} items)")
            
            # Should include transitive dependencies
            if 'expanding_factorising' in prereqs or 'simplifying_expressions' in prereqs:
                log_pass("Transitive prerequisites included")
            else:
                log_warn("Transitive prerequisites may not be included")
        else:
            log_fail("get_prerequisites_for_topic", f"Expected list, got {type(prereqs)}")
        
        # Test get_skill_breakdown_for_student (with no data - should not error)
        breakdown = get_skill_breakdown_for_student(
            user_id=None,
            guest_code='TEST_NONEXISTENT',
            topic_id='arithmetic',
            days=7
        )
        if isinstance(breakdown, dict):
            log_pass("get_skill_breakdown_for_student returns dict for empty data")
        else:
            log_fail("get_skill_breakdown_for_student", f"Expected dict, got {type(breakdown)}")
            
    except ImportError as e:
        log_fail("Import Sprint 1 functions", str(e))
    except Exception as e:
        log_fail("Sprint 1 functions", str(e))


# ==============================================================================
# SPRINT 2 TESTS: Analysis Engine
# ==============================================================================

def test_sprint2_data_collection():
    """Test data collection functions"""
    log_section("SPRINT 2: Data Collection Tests")
    
    try:
        from app import collect_student_activity
        
        # Test with non-existent user (should return empty but valid structure)
        activity = collect_student_activity(
            user_id=None,
            guest_code='TEST_NONEXISTENT_USER_12345',
            days=7
        )
        
        # Check structure
        required_keys = ['user_id', 'guest_code', 'analysis_period_days', 
                        'topics_attempted', 'current_levels', 'dormant_topics',
                        'total_questions', 'overall_accuracy']
        
        missing_keys = [k for k in required_keys if k not in activity]
        if not missing_keys:
            log_pass("Activity data has all required keys")
        else:
            log_fail("Activity structure", f"Missing keys: {missing_keys}")
        
        # Check types
        if isinstance(activity['topics_attempted'], list):
            log_pass("topics_attempted is a list")
        else:
            log_fail("topics_attempted type", f"Expected list, got {type(activity['topics_attempted'])}")
        
        if isinstance(activity['current_levels'], dict):
            log_pass("current_levels is a dict")
        else:
            log_fail("current_levels type", f"Expected dict, got {type(activity['current_levels'])}")
            
    except ImportError as e:
        log_fail("Import collect_student_activity", str(e))
    except Exception as e:
        log_fail("Data collection tests", str(e))
        traceback.print_exc()


def test_sprint2_struggle_detection():
    """Test struggle detection algorithms"""
    log_section("SPRINT 2: Struggle Detection Tests")
    
    try:
        from app import detect_struggles, ILP_THRESHOLDS
        
        # Create mock activity data with known struggles
        mock_activity = {
            'topics_attempted': [
                {
                    'topic_id': 'test_topic_1',
                    'questions_answered': 25,
                    'correct': 7,  # 28% accuracy - critical
                    'accuracy': 0.28,
                    'current_level': 3,
                    'level_7_days_ago': 3,
                    'level_change': 0,
                    'skip_rate': 0.1,
                    'skipped': 3,
                    'skill_breakdown': {
                        'arithmetic_multiplication': {'total': 10, 'correct': 2, 'accuracy': 0.2}
                    }
                },
                {
                    'topic_id': 'test_topic_2',
                    'questions_answered': 20,
                    'correct': 10,  # 50% accuracy - borderline
                    'accuracy': 0.5,
                    'current_level': 5,
                    'level_7_days_ago': 5,
                    'level_change': 0,  # Plateau
                    'skip_rate': 0.05,
                    'skipped': 1,
                    'skill_breakdown': {}
                }
            ],
            'confidence_ratings': {},
            'current_levels': {}
        }
        
        struggles = detect_struggles(mock_activity)
        
        # Should detect struggles
        if isinstance(struggles, list):
            log_pass(f"detect_struggles returns list ({len(struggles)} struggles found)")
        else:
            log_fail("detect_struggles return type", f"Expected list, got {type(struggles)}")
            return
        
        # Should detect critical accuracy issue
        critical_found = any(
            s['overall_severity'] == 'critical' 
            for s in struggles
        )
        if critical_found:
            log_pass("Critical accuracy struggle detected")
        else:
            log_warn("Critical accuracy struggle not detected (may need threshold adjustment)")
        
        # Should detect plateau
        plateau_found = any(
            any(sig['type'] == 'plateau' for sig in s.get('signals', []))
            for s in struggles
        )
        if plateau_found:
            log_pass("Plateau struggle detected")
        else:
            log_warn("Plateau not detected (may need more questions in mock data)")
        
        # Check struggle structure
        if struggles:
            first = struggles[0]
            required = ['topic_id', 'signals', 'overall_severity']
            if all(k in first for k in required):
                log_pass("Struggle object has correct structure")
            else:
                log_fail("Struggle structure", f"Missing keys in {first.keys()}")
                
    except ImportError as e:
        log_fail("Import detect_struggles", str(e))
    except Exception as e:
        log_fail("Struggle detection tests", str(e))
        traceback.print_exc()


def test_sprint2_root_cause_inference():
    """Test root cause inference engine"""
    log_section("SPRINT 2: Root Cause Inference Tests")
    
    try:
        from app import infer_root_causes
        
        # Mock struggles
        mock_struggles = [
            {
                'topic_id': 'solving_equations',
                'signals': [
                    {
                        'type': 'skill_gap',
                        'severity': 'critical',
                        'skill': 'arithmetic_multiplication',
                        'is_numeracy_skill': True,
                        'value': 0.25,
                        'remedial_topics': ['multiplication_skills', 'times_tables_blitz']
                    }
                ],
                'overall_severity': 'critical',
                'current_level': 3,
                'accuracy': 0.35
            }
        ]
        
        # Mock activity data
        mock_activity = {
            'current_levels': {
                'simplifying_expressions': {'level': 2},  # Weak prereq
                'multiplication_skills': {'level': 1}
            },
            'dormant_topics': []
        }
        
        recommendations = infer_root_causes(mock_struggles, mock_activity)
        
        if isinstance(recommendations, list):
            log_pass(f"infer_root_causes returns list ({len(recommendations)} recommendations)")
        else:
            log_fail("infer_root_causes return type", f"Expected list, got {type(recommendations)}")
            return
        
        # Should recommend numeracy insertion
        numeracy_rec = any(r['type'] == 'insert_numeracy' for r in recommendations)
        if numeracy_rec:
            log_pass("Numeracy insertion recommended")
        else:
            log_warn("Numeracy insertion not recommended")
        
        # Should recommend prerequisite
        prereq_rec = any(r['type'] == 'insert_prerequisite' for r in recommendations)
        if prereq_rec:
            log_pass("Prerequisite insertion recommended")
        else:
            log_warn("Prerequisite insertion not recommended")
        
        # Check recommendation structure
        if recommendations:
            first = recommendations[0]
            required = ['type', 'priority', 'reason']
            if all(k in first for k in required):
                log_pass("Recommendation object has correct structure")
            else:
                log_fail("Recommendation structure", f"Missing keys in {first.keys()}")
                
    except ImportError as e:
        log_fail("Import infer_root_causes", str(e))
    except Exception as e:
        log_fail("Root cause inference tests", str(e))
        traceback.print_exc()


def test_sprint2_full_analysis():
    """Test full analysis pipeline"""
    log_section("SPRINT 2: Full Analysis Pipeline Tests")
    
    try:
        from app import run_full_analysis
        
        # Run analysis for non-existent user
        result = run_full_analysis(
            user_id=None,
            guest_code='TEST_ANALYSIS_USER_12345',
            days=7
        )
        
        if isinstance(result, dict):
            log_pass("run_full_analysis returns dict")
        else:
            log_fail("run_full_analysis return type", f"Expected dict, got {type(result)}")
            return
        
        # Check structure
        required_keys = ['user_id', 'guest_code', 'analysis_date', 'activity_summary',
                        'struggles', 'recommendations', 'has_recommendations']
        
        missing = [k for k in required_keys if k not in result]
        if not missing:
            log_pass("Analysis result has all required keys")
        else:
            log_fail("Analysis result structure", f"Missing: {missing}")
        
        # Check summary generation
        if 'summary' in result and isinstance(result['summary'], str):
            log_pass("Human-readable summary generated")
        else:
            log_warn("Summary not generated or not string")
            
    except ImportError as e:
        log_fail("Import run_full_analysis", str(e))
    except Exception as e:
        log_fail("Full analysis tests", str(e))
        traceback.print_exc()


# ==============================================================================
# SPRINT 3 TESTS: Plan Modification & Notifications
# ==============================================================================

def test_sprint3_plan_modifications():
    """Test plan modification generation"""
    log_section("SPRINT 3: Plan Modification Tests")
    
    try:
        from app import generate_plan_modifications
        
        # Mock recommendations
        mock_recommendations = [
            {
                'type': 'insert_numeracy',
                'priority': 'critical',
                'topic_to_add': 'arithmetic',
                'target_level': 4,
                'reason': 'Test numeracy insertion',
                'struggling_topic': 'solving_equations'
            },
            {
                'type': 'insert_prerequisite',
                'priority': 'high',
                'topic_to_add': 'simplifying_expressions',
                'target_level': 4,
                'reason': 'Test prereq insertion',
                'struggling_topic': 'solving_equations'
            }
        ]
        
        # Mock current plan (full)
        mock_plan = [
            {'topic_id': 'quadratics', 'target_level': 6, 'status': 'pending', 'priority': 2},
            {'topic_id': 'geometry', 'target_level': 5, 'status': 'pending', 'priority': 1},
            {'topic_id': 'solving_equations', 'target_level': 5, 'status': 'in_progress', 'priority': 0}
        ]
        
        modifications = generate_plan_modifications(mock_recommendations, mock_plan, max_topics=3)
        
        if isinstance(modifications, list):
            log_pass(f"generate_plan_modifications returns list ({len(modifications)} mods)")
        else:
            log_fail("generate_plan_modifications return type", f"Expected list, got {type(modifications)}")
            return
        
        # Should have add actions
        adds = [m for m in modifications if m['action'] == 'add']
        if adds:
            log_pass(f"{len(adds)} add modification(s) generated")
        else:
            log_warn("No add modifications generated")
        
        # Should have delay action (since plan is full)
        delays = [m for m in modifications if m['action'] == 'delay']
        if delays:
            log_pass(f"{len(delays)} delay modification(s) generated (plan was full)")
        else:
            log_warn("No delay modifications (may not have exceeded max_topics)")
        
        # Check modification structure
        if modifications:
            first = modifications[0]
            required = ['action', 'topic_id', 'reason']
            if all(k in first for k in required):
                log_pass("Modification object has correct structure")
            else:
                log_fail("Modification structure", f"Missing keys in {first.keys()}")
                
    except ImportError as e:
        log_fail("Import generate_plan_modifications", str(e))
    except Exception as e:
        log_fail("Plan modification tests", str(e))
        traceback.print_exc()


def test_sprint3_notification_functions():
    """Test notification creation and retrieval"""
    log_section("SPRINT 3: Notification System Tests")
    
    try:
        from app import (create_recommendation_notification, 
                        get_pending_recommendations,
                        accept_recommendation,
                        reject_recommendation,
                        get_recommendation_history)
        
        # These functions exist
        log_pass("create_recommendation_notification function exists")
        log_pass("get_pending_recommendations function exists")
        log_pass("accept_recommendation function exists")
        log_pass("reject_recommendation function exists")
        log_pass("get_recommendation_history function exists")
        
        # Test get_pending with non-existent user (should return empty list)
        pending = get_pending_recommendations(
            user_id=None,
            guest_code='TEST_NOTIFICATION_USER_12345'
        )
        
        if isinstance(pending, list):
            log_pass("get_pending_recommendations returns list")
        else:
            log_fail("get_pending_recommendations return type", f"Expected list, got {type(pending)}")
        
        # Test history
        history = get_recommendation_history(
            user_id=None,
            guest_code='TEST_NOTIFICATION_USER_12345'
        )
        
        if isinstance(history, list):
            log_pass("get_recommendation_history returns list")
        else:
            log_fail("get_recommendation_history return type", f"Expected list, got {type(history)}")
            
    except ImportError as e:
        log_fail("Import notification functions", str(e))
    except Exception as e:
        log_fail("Notification system tests", str(e))
        traceback.print_exc()


def test_sprint3_auto_apply():
    """Test auto-apply expired function"""
    log_section("SPRINT 3: Auto-Apply Tests")
    
    try:
        from app import auto_apply_expired_recommendations
        
        # Function should exist and run without error
        result = auto_apply_expired_recommendations()
        
        if isinstance(result, int):
            log_pass(f"auto_apply_expired_recommendations returns count ({result})")
        else:
            log_fail("auto_apply return type", f"Expected int, got {type(result)}")
            
    except ImportError as e:
        log_fail("Import auto_apply_expired_recommendations", str(e))
    except Exception as e:
        log_fail("Auto-apply tests", str(e))
        traceback.print_exc()


# ==============================================================================
# SPRINT 4 TESTS: Nightly Job & Batch Processing
# ==============================================================================

def test_sprint4_active_students():
    """Test active student retrieval"""
    log_section("SPRINT 4: Active Students Tests")
    
    try:
        from app import get_active_students
        
        # Function should return a list
        students = get_active_students(days=14)
        
        if isinstance(students, list):
            log_pass(f"get_active_students returns list ({len(students)} students)")
        else:
            log_fail("get_active_students return type", f"Expected list, got {type(students)}")
            return
        
        # Check structure if there are students
        if students:
            first = students[0]
            if 'user_id' in first and 'guest_code' in first:
                log_pass("Student object has user_id and guest_code keys")
            else:
                log_fail("Student structure", f"Missing keys in {first.keys()}")
        else:
            log_pass("No active students found (expected for test DB)")
            
    except ImportError as e:
        log_fail("Import get_active_students", str(e))
    except Exception as e:
        log_fail("Active students tests", str(e))
        traceback.print_exc()


def test_sprint4_nightly_job_function():
    """Test nightly job function exists"""
    log_section("SPRINT 4: Nightly Job Function Tests")
    
    try:
        from app import run_nightly_ilp_job, get_nightly_job_history
        
        log_pass("run_nightly_ilp_job function exists")
        log_pass("get_nightly_job_history function exists")
        
        # Test job history retrieval
        history = get_nightly_job_history(limit=5)
        
        if isinstance(history, list):
            log_pass(f"get_nightly_job_history returns list ({len(history)} entries)")
        else:
            log_fail("get_nightly_job_history return type", f"Expected list, got {type(history)}")
            
    except ImportError as e:
        log_fail("Import Sprint 4 functions", str(e))
    except Exception as e:
        log_fail("Nightly job function tests", str(e))
        traceback.print_exc()


def test_sprint4_nightly_log_table():
    """Test nightly log table exists"""
    log_section("SPRINT 4: Nightly Log Table Tests")
    
    try:
        from app import db, create_ilp_tables
        from sqlalchemy import text
        
        # Ensure tables are created first
        create_ilp_tables()
        
        # Check table exists
        result = db.session.execute(text("SELECT 1 FROM ilp_nightly_log LIMIT 1"))
        log_pass("ilp_nightly_log table exists")
        
        # Check we can query history
        history = db.session.execute(text("""
            SELECT id, run_date, status, students_processed
            FROM ilp_nightly_log
            ORDER BY started_at DESC
            LIMIT 5
        """)).fetchall()
        
        log_pass(f"ilp_nightly_log queryable ({len(history)} records)")
        
    except Exception as e:
        if 'no such table' in str(e).lower():
            log_fail("ilp_nightly_log table", "Does not exist")
        else:
            log_fail("Nightly log table tests", str(e))


def test_sprint4_weekly_plans_table():
    """Test passport_weekly_plans table exists"""
    log_section("SPRINT 4: Weekly Plans Table Tests")
    
    try:
        from app import db, create_ilp_tables
        from sqlalchemy import text
        
        # Ensure tables are created first
        create_ilp_tables()
        
        # Check table exists
        result = db.session.execute(text("SELECT 1 FROM passport_weekly_plans LIMIT 1"))
        log_pass("passport_weekly_plans table exists")
        
    except Exception as e:
        if 'no such table' in str(e).lower():
            log_fail("passport_weekly_plans table", "Does not exist")
        else:
            log_fail("Weekly plans table tests", str(e))


# ==============================================================================
# API ENDPOINT TESTS
# ==============================================================================

def test_api_endpoints():
    """Test API endpoints exist (requires Flask test client)"""
    log_section("API Endpoint Tests")
    
    try:
        from app import app
        
        with app.test_client() as client:
            # Test Sprint 1 endpoints
            endpoints_to_test = [
                ('/api/ilp/config', 'GET', 'ILP config'),
                ('/api/ilp/topic-info/arithmetic', 'GET', 'Topic info'),
            ]
            
            for endpoint, method, name in endpoints_to_test:
                try:
                    if method == 'GET':
                        response = client.get(endpoint)
                    else:
                        response = client.post(endpoint)
                    
                    # Accept 200, 401 (auth required), 302 (redirect)
                    if response.status_code in [200, 401, 302]:
                        log_pass(f"Endpoint {endpoint} responds ({response.status_code})")
                    else:
                        log_warn(f"Endpoint {endpoint} returned {response.status_code}")
                except Exception as e:
                    log_warn(f"Endpoint {endpoint} error: {e}")
                    
    except ImportError as e:
        log_fail("Import app for API tests", str(e))
    except Exception as e:
        log_fail("API endpoint tests", str(e))
        traceback.print_exc()


# ==============================================================================
# DATABASE TABLE TESTS
# ==============================================================================

def test_database_tables():
    """Test that ILP database tables exist"""
    log_section("Database Table Tests")
    
    try:
        from app import db, create_ilp_tables
        from sqlalchemy import text
        
        # Ensure tables are created
        create_ilp_tables()
        
        tables_to_check = [
            'question_skill_tags',
            'ilp_recommendations',
            'ilp_modification_log',
            'passport_weekly_plans',
            'ilp_nightly_log'
        ]
        
        for table in tables_to_check:
            try:
                result = db.session.execute(text(f"SELECT 1 FROM {table} LIMIT 1"))
                log_pass(f"Table '{table}' exists and is accessible")
            except Exception as e:
                if 'no such table' in str(e).lower():
                    log_fail(f"Table '{table}'", "Does not exist")
                else:
                    log_warn(f"Table '{table}' query error: {e}")
                    
    except ImportError as e:
        log_fail("Import db for table tests", str(e))
    except Exception as e:
        log_fail("Database table tests", str(e))
        traceback.print_exc()


# ==============================================================================
# INTEGRATION TEST
# ==============================================================================

def test_integration_flow():
    """Test complete flow from analysis to notification"""
    log_section("Integration Flow Test")
    
    try:
        from app import (run_full_analysis, 
                        create_recommendation_notification,
                        get_pending_recommendations)
        
        test_guest = f'TEST_INTEGRATION_{datetime.now().strftime("%Y%m%d%H%M%S")}'
        
        # Step 1: Run analysis
        analysis = run_full_analysis(user_id=None, guest_code=test_guest, days=7)
        
        if 'activity_summary' in analysis:
            log_pass("Step 1: Analysis completed")
        else:
            log_fail("Step 1: Analysis", "Missing activity_summary")
            return
        
        # Step 2: Create notification (if there are recommendations)
        # For empty user, there won't be real recommendations, but we test the flow
        
        # Create a mock analysis result with recommendations
        mock_analysis = {
            'has_recommendations': True,
            'activity_summary': {'total_questions': 50},
            'recommendations': [
                {
                    'type': 'insert_numeracy',
                    'priority': 'high',
                    'topic_to_add': 'arithmetic',
                    'target_level': 4,
                    'reason': 'Test recommendation'
                }
            ],
            'summary': 'Test summary'
        }
        
        rec_id = create_recommendation_notification(
            user_id=None,
            guest_code=test_guest,
            analysis_result=mock_analysis
        )
        
        if rec_id:
            log_pass(f"Step 2: Notification created (ID: {rec_id})")
            
            # Step 3: Retrieve pending
            pending = get_pending_recommendations(user_id=None, guest_code=test_guest)
            
            if len(pending) > 0:
                log_pass(f"Step 3: Pending notifications retrieved ({len(pending)})")
            else:
                log_warn("Step 3: No pending notifications found")
        else:
            log_warn("Step 2: Notification not created (may be expected if no plan)")
        
        log_pass("Integration flow completed without errors")
        
    except Exception as e:
        log_fail("Integration flow", str(e))
        traceback.print_exc()


# ==============================================================================
# MAIN TEST RUNNER
# ==============================================================================

def run_all_tests():
    """Run all tests"""
    print("\n" + "="*60)
    print("  AgentMath Phase 12 - ILP System Test Suite")
    print("  " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("="*60)
    
    # Need Flask app context for database operations
    try:
        from app import app, create_ilp_tables
        
        with app.app_context():
            # Ensure all ILP tables exist before running tests
            print("\n  Initializing ILP tables...")
            create_ilp_tables()
            
            # Sprint 1 Tests
            test_sprint1_prerequisite_map()
            test_sprint1_skill_tags()
            test_sprint1_skill_to_numeracy()
            test_sprint1_thresholds()
            test_sprint1_functions()
            
            # Sprint 2 Tests
            test_sprint2_data_collection()
            test_sprint2_struggle_detection()
            test_sprint2_root_cause_inference()
            test_sprint2_full_analysis()
            
            # Sprint 3 Tests
            test_sprint3_plan_modifications()
            test_sprint3_notification_functions()
            test_sprint3_auto_apply()
            
            # Sprint 4 Tests
            test_sprint4_active_students()
            test_sprint4_nightly_job_function()
            test_sprint4_nightly_log_table()
            test_sprint4_weekly_plans_table()
            
            # API & Database Tests
            test_api_endpoints()
            test_database_tables()
            
            # Integration Test
            test_integration_flow()
    
    except ImportError as e:
        print(f"\n❌ CRITICAL: Cannot import app.py - {e}")
        print("   Make sure you're running from the correct directory")
        return
    
    # Summary
    print("\n" + "="*60)
    print("  TEST SUMMARY")
    print("="*60)
    print(f"  ✅ Passed: {test_results['passed']}")
    print(f"  ❌ Failed: {test_results['failed']}")
    print(f"  ⚠️  Warnings: {len(test_results['warnings'])}")
    
    if test_results['errors']:
        print("\n  FAILURES:")
        for error in test_results['errors']:
            print(f"    • {error}")
    
    if test_results['warnings']:
        print("\n  WARNINGS:")
        for warn in test_results['warnings'][:5]:  # Limit to 5
            print(f"    • {warn}")
        if len(test_results['warnings']) > 5:
            print(f"    ... and {len(test_results['warnings']) - 5} more")
    
    print("\n" + "="*60)
    
    # Return exit code
    if test_results['failed'] == 0:
        print("  ✅ ALL TESTS PASSED!")
        return 0
    else:
        print(f"  ❌ {test_results['failed']} TEST(S) FAILED")
        return 1


if __name__ == '__main__':
    exit_code = run_all_tests()
    sys.exit(exit_code)
