#!/usr/bin/env python3
# run_tests.py - AgentMath Automated Test Runner
# Version 1.0 - 2025-12-31
#
# Usage:
#   python run_tests.py                    # Run all tests
#   python run_tests.py --quick            # Run only critical tests
#   python run_tests.py --security         # Run only security tests
#   python run_tests.py --verbose          # Verbose output
#   python run_tests.py --html             # Generate HTML report
#   python run_tests.py --specific test_auth  # Run specific test file

import subprocess
import sys
import os
import argparse
from datetime import datetime


def check_dependencies():
    """Check if required packages are installed."""
    required = ['pytest', 'pytest-html']
    missing = []
    
    for package in required:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"⚠️  Missing packages: {', '.join(missing)}")
        print(f"   Install with: pip install {' '.join(missing)} --break-system-packages")
        return False
    return True


def run_tests(args):
    """Run the test suite with appropriate options."""
    
    # Build pytest command
    cmd = ['python', '-m', 'pytest', 'tests/']
    
    # Add verbosity
    if args.verbose:
        cmd.append('-v')
    else:
        cmd.append('-q')
    
    # Show print statements
    cmd.append('-s')
    
    # Continue on failures
    if not args.stop_on_fail:
        cmd.append('--tb=short')
    else:
        cmd.append('-x')
    
    # Add markers for specific test types
    if args.quick:
        cmd.extend(['-m', 'not slow'])
    elif args.security:
        cmd.extend(['-m', 'security'])
    elif args.corner_cases:
        cmd.extend(['-m', 'corner_case'])
    
    # Run specific test file
    if args.specific:
        cmd = ['python', '-m', 'pytest', f'tests/test_{args.specific}.py', '-v']
    
    # Generate HTML report
    if args.html:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_path = f'test_report_{timestamp}.html'
        cmd.extend(['--html', report_path, '--self-contained-html'])
        print(f"📊 HTML report will be saved to: {report_path}")
    
    # Show test collection first
    if args.collect_only:
        cmd.append('--collect-only')
    
    # Print command for debugging
    print(f"🧪 Running: {' '.join(cmd)}")
    print("=" * 60)
    
    # Run tests
    result = subprocess.run(cmd, cwd=os.path.dirname(os.path.abspath(__file__)))
    
    return result.returncode


def print_summary(return_code):
    """Print test summary."""
    print("\n" + "=" * 60)
    if return_code == 0:
        print("✅ ALL TESTS PASSED!")
    elif return_code == 1:
        print("❌ SOME TESTS FAILED")
    elif return_code == 2:
        print("⚠️  TEST EXECUTION INTERRUPTED")
    elif return_code == 3:
        print("⚠️  INTERNAL ERROR")
    elif return_code == 4:
        print("⚠️  PYTEST USAGE ERROR")
    elif return_code == 5:
        print("⚠️  NO TESTS COLLECTED")
    else:
        print(f"⚠️  UNKNOWN EXIT CODE: {return_code}")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description='AgentMath Automated Test Runner',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python run_tests.py                    Run all tests
  python run_tests.py --quick            Quick test (skip slow tests)
  python run_tests.py --security         Security tests only
  python run_tests.py --corner-cases     Corner case tests only
  python run_tests.py --html             Generate HTML report
  python run_tests.py --specific auth    Run only auth tests
  python run_tests.py -v --html          Verbose with HTML report
        '''
    )
    
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Verbose output')
    parser.add_argument('--quick', '-q', action='store_true',
                        help='Run quick tests only (skip slow)')
    parser.add_argument('--security', '-s', action='store_true',
                        help='Run security tests only')
    parser.add_argument('--corner-cases', '-c', action='store_true',
                        help='Run corner case tests only')
    parser.add_argument('--html', action='store_true',
                        help='Generate HTML report')
    parser.add_argument('--specific', type=str,
                        help='Run specific test file (e.g., auth, admin, core_api)')
    parser.add_argument('--stop-on-fail', '-x', action='store_true',
                        help='Stop on first failure')
    parser.add_argument('--collect-only', action='store_true',
                        help='Only collect tests, do not run')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🎓 AgentMath Automated Test Suite")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Check dependencies
    if not check_dependencies():
        print("\n❌ Cannot run tests without required packages")
        sys.exit(1)
    
    # Run tests
    return_code = run_tests(args)
    
    # Print summary
    print_summary(return_code)
    
    sys.exit(return_code)


if __name__ == '__main__':
    main()
