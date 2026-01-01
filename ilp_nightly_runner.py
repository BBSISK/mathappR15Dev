#!/usr/bin/env python3
"""
AgentMath ILP Nightly Job Runner
================================

This script is designed to be run by PythonAnywhere's scheduled tasks.

Setup Instructions:
-------------------
1. Upload this file to: /home/bbsisk/mathappR15Dev/ilp_nightly_runner.py
2. Go to PythonAnywhere Dashboard → Tasks
3. Create a new scheduled task with:
   - Command: /home/bbsisk/.virtualenvs/myenv/bin/python /home/bbsisk/mathappR15Dev/ilp_nightly_runner.py
   - Time: Choose a low-traffic time (e.g., 3:00 AM Irish time)
   - Frequency: Daily

Alternative command if not using virtualenv:
   python3 /home/bbsisk/mathappR15Dev/ilp_nightly_runner.py

What This Script Does:
----------------------
1. Auto-applies any pending recommendations that have expired (past 24 hours)
2. Finds all students active in the past 14 days
3. Runs ILP analysis for each student
4. Creates new recommendation notifications for students who need plan adjustments
5. Logs all activity to ilp_nightly_log table

Output:
-------
The script prints progress to stdout, which PythonAnywhere captures in task logs.
Check the Tasks page to see output from previous runs.

Manual Testing:
---------------
To test manually, SSH into PythonAnywhere and run:
    cd ~/mathappR15Dev
    python ilp_nightly_runner.py

Or via the web interface:
    POST /api/ilp/nightly-job

Author: AgentMath Development
Version: 1.0
Date: 2025-12-24
"""

import sys
import os

# Add the app directory to the path
app_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, app_dir)

# Change to app directory
os.chdir(app_dir)

def main():
    """Main entry point for nightly job"""
    print("\n" + "="*60)
    print("  AgentMath ILP Nightly Job Runner")
    print("="*60)
    
    try:
        # Import the app and run with context
        from app import app, run_nightly_ilp_job
        
        with app.app_context():
            stats = run_nightly_ilp_job()
            
            # Exit with appropriate code
            if stats.get('errors'):
                print(f"\nCompleted with {len(stats['errors'])} error(s)")
                sys.exit(1)
            else:
                print("\nCompleted successfully")
                sys.exit(0)
                
    except ImportError as e:
        print(f"\n❌ CRITICAL: Cannot import app - {e}")
        print("   Check that app.py is in the same directory")
        sys.exit(2)
        
    except Exception as e:
        print(f"\n❌ CRITICAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(3)


if __name__ == '__main__':
    main()
