#!/usr/bin/env python3
"""
AgentMath Email Reports Scheduler
=================================
This script is designed to run from PythonAnywhere's Task Scheduler.

Setup Instructions:
1. Upload this file to: /home/bbsisk/mathappR15Dev/send_reports.py
2. Go to PythonAnywhere → Tasks tab
3. Create a new scheduled task:
   - Time: 07:00 (7am Irish time - adjust for UTC if needed)
   - Command: /home/bbsisk/mathappR15Dev/venv/bin/python /home/bbsisk/mathappR15Dev/send_reports.py

The script automatically determines which reports to send based on the current date:
- Daily report: Sent every day
- Weekly report: Sent on Mondays only
- Monthly report: Sent on the 1st of each month

You can also run specific reports manually:
  python send_reports.py daily
  python send_reports.py weekly
  python send_reports.py monthly
  python send_reports.py all
"""

import sys
import os
from datetime import datetime, timedelta

# Add the app directory to the path
sys.path.insert(0, '/home/bbsisk/mathappR15Dev')
os.chdir('/home/bbsisk/mathappR15Dev')

# Import Flask app and dependencies
from app import app, db
from sqlalchemy import text

def get_report_setting(key, default=None):
    """Get a report setting from the database"""
    try:
        result = db.session.execute(text(
            "SELECT setting_value FROM report_settings WHERE setting_key = :key"
        ), {'key': key}).fetchone()
        return result[0] if result else default
    except:
        return default

def get_distribution_list(report_type):
    """Get active recipients for a specific report type"""
    try:
        recipients = db.session.execute(text("""
            SELECT email, recipient_name FROM email_distribution_list
            WHERE (report_type = :report_type OR report_type = 'all') AND is_active = 1
        """), {'report_type': report_type}).fetchall()
        return [{'email': r[0], 'name': r[1]} for r in recipients]
    except Exception as e:
        print(f"Error getting distribution list: {e}")
        return []

def generate_daily_report_data():
    """Generate data for the daily report"""
    today = datetime.utcnow().date()
    yesterday = today - timedelta(days=1)
    two_days_ago = today - timedelta(days=2)
    
    report_data = {
        'report_date': str(yesterday),
        'generated_at': datetime.utcnow().isoformat(),
        'active_users': 0,
        'active_users_change': 0,
        'questions_answered': 0,
        'questions_change': 0,
        'points_earned': 0,
        'points_change': 0,
        'new_registrations': 0,
        'registrations_change': 0,
        'total_points_circulation': 0,
        'guest_users_active': 0,
        'teachers_active': 0,
        'badges_earned': 0,
        'popular_topic': 'N/A',
        'pending_teachers': 0,
        'inactive_students': 0
    }
    
    try:
        # Active users yesterday
        try:
            active_users = db.session.execute(text("""
                SELECT COUNT(DISTINCT COALESCE(user_id, guest_code)) 
                FROM user_question_history 
                WHERE DATE(seen_at) = :date
            """), {'date': yesterday}).scalar() or 0
            
            prev_active = db.session.execute(text("""
                SELECT COUNT(DISTINCT COALESCE(user_id, guest_code)) 
                FROM user_question_history 
                WHERE DATE(seen_at) = :date
            """), {'date': two_days_ago}).scalar() or 0
            
            report_data['active_users'] = active_users
            report_data['active_users_change'] = active_users - prev_active
        except Exception as e:
            print(f"  Error getting active users: {e}")
        
        # Questions seen yesterday
        try:
            questions_answered = db.session.execute(text("""
                SELECT COUNT(*) FROM user_question_history 
                WHERE DATE(seen_at) = :date
            """), {'date': yesterday}).scalar() or 0
            
            prev_questions = db.session.execute(text("""
                SELECT COUNT(*) FROM user_question_history 
                WHERE DATE(seen_at) = :date
            """), {'date': two_days_ago}).scalar() or 0
            
            report_data['questions_answered'] = questions_answered
            report_data['questions_change'] = questions_answered - prev_questions
        except Exception as e:
            print(f"  Error getting questions: {e}")
        
        # Points earned yesterday
        try:
            points_earned = db.session.execute(text("""
                SELECT COALESCE(SUM(score), 0) FROM quiz_attempts 
                WHERE DATE(completed_at) = :date
            """), {'date': yesterday}).scalar() or 0
            
            prev_points = db.session.execute(text("""
                SELECT COALESCE(SUM(score), 0) FROM quiz_attempts 
                WHERE DATE(completed_at) = :date
            """), {'date': two_days_ago}).scalar() or 0
            
            report_data['points_earned'] = points_earned
            report_data['points_change'] = points_earned - prev_points
        except Exception as e:
            print(f"  Error getting points: {e}")
        
        # New registrations
        try:
            new_registrations = db.session.execute(text("""
                SELECT COUNT(*) FROM users 
                WHERE DATE(created_at) = :date AND role = 'student'
            """), {'date': yesterday}).scalar() or 0
            
            prev_registrations = db.session.execute(text("""
                SELECT COUNT(*) FROM users 
                WHERE DATE(created_at) = :date AND role = 'student'
            """), {'date': two_days_ago}).scalar() or 0
            
            report_data['new_registrations'] = new_registrations
            report_data['registrations_change'] = new_registrations - prev_registrations
        except Exception as e:
            print(f"  Error getting registrations: {e}")
        
        # Total points in circulation
        try:
            registered_points = db.session.execute(text("""
                SELECT COALESCE(SUM(total_points), 0) FROM user_stats
            """)).scalar() or 0
            
            guest_points = db.session.execute(text("""
                SELECT COALESCE(SUM(total_score), 0) FROM guest_users
            """)).scalar() or 0
            
            report_data['total_points_circulation'] = registered_points + guest_points
        except Exception as e:
            print(f"  Error getting total points: {e}")
        
        # Guest users active
        try:
            guest_active = db.session.execute(text("""
                SELECT COUNT(*) FROM guest_users 
                WHERE DATE(last_active) = :date
            """), {'date': yesterday}).scalar() or 0
            report_data['guest_users_active'] = guest_active
        except Exception as e:
            print(f"  Error getting guests: {e}")
        
        # Teachers count
        try:
            teachers_active = db.session.execute(text("""
                SELECT COUNT(*) FROM users 
                WHERE role = 'teacher' AND is_approved = 1
            """)).scalar() or 0
            report_data['teachers_active'] = teachers_active
        except Exception as e:
            print(f"  Error getting teachers: {e}")
        
        # Badges earned
        try:
            badges_earned = db.session.execute(text("""
                SELECT COUNT(*) FROM user_badges 
                WHERE DATE(earned_at) = :date
            """), {'date': yesterday}).scalar() or 0
            report_data['badges_earned'] = badges_earned
        except Exception as e:
            print(f"  Error getting badges: {e}")
        
        # Popular topic
        try:
            popular_topic = db.session.execute(text("""
                SELECT topic, COUNT(*) as cnt FROM user_question_history 
                WHERE DATE(seen_at) = :date AND topic IS NOT NULL
                GROUP BY topic ORDER BY cnt DESC LIMIT 1
            """), {'date': yesterday}).fetchone()
            report_data['popular_topic'] = popular_topic[0] if popular_topic else 'N/A'
        except Exception as e:
            print(f"  Error getting topic: {e}")
        
        # Pending teachers
        try:
            pending_teachers = db.session.execute(text("""
                SELECT COUNT(*) FROM users 
                WHERE role = 'teacher' AND is_approved = 0
            """)).scalar() or 0
            report_data['pending_teachers'] = pending_teachers
        except Exception as e:
            print(f"  Error getting pending: {e}")
        
        # Inactive students
        try:
            inactive_students = db.session.execute(text("""
                SELECT COUNT(*) FROM guest_users 
                WHERE user_id IS NOT NULL 
                AND (last_active IS NULL OR DATE(last_active) < :cutoff)
            """), {'cutoff': today - timedelta(days=7)}).scalar() or 0
            report_data['inactive_students'] = inactive_students
        except Exception as e:
            print(f"  Error getting inactive: {e}")
            
    except Exception as e:
        print(f"Error generating report data: {e}")
    
    return report_data

def generate_daily_report_html(report_data):
    """Generate HTML email for daily report"""
    school_name = get_report_setting('school_name', 'Palmerstown Community School')
    
    def format_change(value):
        if value > 0:
            return f'<span style="color: #22c55e;">▲ +{value}</span>'
        elif value < 0:
            return f'<span style="color: #ef4444;">▼ {value}</span>'
        else:
            return '<span style="color: #6b7280;">–</span>'
    
    html = f'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background-color: #f3f4f6;">
    <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
        <!-- Header -->
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px 12px 0 0; padding: 30px; text-align: center;">
            <h1 style="margin: 0; color: white; font-size: 28px;">📊 Daily Pulse Report</h1>
            <p style="margin: 10px 0 0 0; color: rgba(255,255,255,0.9); font-size: 16px;">{school_name}</p>
            <p style="margin: 5px 0 0 0; color: rgba(255,255,255,0.7); font-size: 14px;">{report_data.get('report_date', 'Yesterday')}</p>
        </div>
        
        <!-- Main Content -->
        <div style="background: white; padding: 30px; border-radius: 0 0 12px 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            
            <!-- Key Metrics Grid -->
            <h2 style="margin: 0 0 20px 0; font-size: 18px; color: #374151;">📈 Yesterday at a Glance</h2>
            
            <table style="width: 100%; border-collapse: collapse; margin-bottom: 30px;">
                <tr>
                    <td style="padding: 15px; background: #f0f9ff; border-radius: 8px; text-align: center; width: 50%;">
                        <div style="font-size: 32px; font-weight: bold; color: #3b82f6;">{report_data.get('active_users', 0)}</div>
                        <div style="font-size: 14px; color: #6b7280;">Active Users</div>
                        <div style="font-size: 12px; margin-top: 5px;">{format_change(report_data.get('active_users_change', 0))}</div>
                    </td>
                    <td style="width: 10px;"></td>
                    <td style="padding: 15px; background: #f0fdf4; border-radius: 8px; text-align: center; width: 50%;">
                        <div style="font-size: 32px; font-weight: bold; color: #22c55e;">{report_data.get('questions_answered', 0):,}</div>
                        <div style="font-size: 14px; color: #6b7280;">Questions Answered</div>
                        <div style="font-size: 12px; margin-top: 5px;">{format_change(report_data.get('questions_change', 0))}</div>
                    </td>
                </tr>
                <tr><td colspan="3" style="height: 10px;"></td></tr>
                <tr>
                    <td style="padding: 15px; background: #fefce8; border-radius: 8px; text-align: center;">
                        <div style="font-size: 32px; font-weight: bold; color: #eab308;">{report_data.get('points_earned', 0):,}</div>
                        <div style="font-size: 14px; color: #6b7280;">Points Earned</div>
                        <div style="font-size: 12px; margin-top: 5px;">{format_change(report_data.get('points_change', 0))}</div>
                    </td>
                    <td style="width: 10px;"></td>
                    <td style="padding: 15px; background: #fdf4ff; border-radius: 8px; text-align: center;">
                        <div style="font-size: 32px; font-weight: bold; color: #a855f7;">{report_data.get('new_registrations', 0)}</div>
                        <div style="font-size: 14px; color: #6b7280;">New Registrations</div>
                        <div style="font-size: 12px; margin-top: 5px;">{format_change(report_data.get('registrations_change', 0))}</div>
                    </td>
                </tr>
            </table>
            
            <!-- User Activity Section -->
            <h2 style="margin: 30px 0 15px 0; font-size: 18px; color: #374151;">👥 User Activity</h2>
            <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 10px 0; color: #6b7280;">Guest users active</td>
                    <td style="padding: 10px 0; text-align: right; font-weight: 600;">{report_data.get('guest_users_active', 0)}</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 10px 0; color: #6b7280;">Approved teachers</td>
                    <td style="padding: 10px 0; text-align: right; font-weight: 600;">{report_data.get('teachers_active', 0)}</td>
                </tr>
                <tr style="border-bottom: 1px solid #e5e7eb;">
                    <td style="padding: 10px 0; color: #6b7280;">Badges earned</td>
                    <td style="padding: 10px 0; text-align: right; font-weight: 600;">{report_data.get('badges_earned', 0)}</td>
                </tr>
                <tr>
                    <td style="padding: 10px 0; color: #6b7280;">Most popular topic</td>
                    <td style="padding: 10px 0; text-align: right; font-weight: 600;">{report_data.get('popular_topic', 'N/A')}</td>
                </tr>
            </table>
            
            <!-- Points Economy Section -->
            <h2 style="margin: 30px 0 15px 0; font-size: 18px; color: #374151;">💰 Points Economy</h2>
            <div style="background: linear-gradient(135deg, #fef3c7, #fde68a); padding: 20px; border-radius: 8px; text-align: center;">
                <div style="font-size: 14px; color: #92400e;">Total Points in Circulation</div>
                <div style="font-size: 36px; font-weight: bold; color: #b45309;">{report_data.get('total_points_circulation', 0):,}</div>
            </div>
            
            <!-- Alerts Section -->
            <h2 style="margin: 30px 0 15px 0; font-size: 18px; color: #374151;">⚠️ Alerts & Actions</h2>
            <div style="background: #fef2f2; border-left: 4px solid #ef4444; padding: 15px; border-radius: 0 8px 8px 0; margin-bottom: 10px;">
                <strong style="color: #dc2626;">Pending teacher approvals:</strong> {report_data.get('pending_teachers', 0)}
            </div>
            <div style="background: #fffbeb; border-left: 4px solid #f59e0b; padding: 15px; border-radius: 0 8px 8px 0;">
                <strong style="color: #d97706;">Inactive students (7+ days):</strong> {report_data.get('inactive_students', 0)}
            </div>
            
        </div>
        
        <!-- Footer -->
        <div style="text-align: center; padding: 20px; color: #9ca3af; font-size: 12px;">
            <p>This is an automated report from AgentMath</p>
            <p>© {datetime.now().year} {school_name}</p>
        </div>
    </div>
</body>
</html>
'''
    return html

def send_email(recipients, subject, html_content, report_type):
    """Send email to recipients"""
    from flask_mail import Mail, Message
    
    mail = Mail(app)
    sent_count = 0
    errors = []
    
    for recipient in recipients:
        try:
            msg = Message(
                subject=subject,
                recipients=[recipient['email']],
                html=html_content
            )
            mail.send(msg)
            sent_count += 1
            print(f"  ✅ Sent to: {recipient['email']}")
        except Exception as e:
            errors.append(f"{recipient['email']}: {str(e)}")
            print(f"  ❌ Failed: {recipient['email']} - {e}")
    
    # Log to database
    try:
        db.session.execute(text("""
            INSERT INTO report_history (report_type, report_date, recipients_count, sent_at, status, error_message)
            VALUES (:report_type, :report_date, :recipients_count, CURRENT_TIMESTAMP, :status, :errors)
        """), {
            'report_type': report_type,
            'report_date': datetime.utcnow().date(),
            'recipients_count': sent_count,
            'status': 'sent' if not errors else 'partial' if sent_count > 0 else 'failed',
            'errors': '; '.join(errors) if errors else None
        })
        db.session.commit()
    except Exception as e:
        print(f"  Warning: Could not log report: {e}")
        db.session.rollback()
    
    return sent_count, errors

def send_daily_report():
    """Generate and send daily report"""
    print("\n📊 Generating Daily Report...")
    
    # Check if enabled
    if get_report_setting('daily_report_enabled', 'true') == 'false':
        print("  Daily reports are disabled. Skipping.")
        return
    
    recipients = get_distribution_list('daily')
    if not recipients:
        print("  No recipients for daily reports. Skipping.")
        return
    
    print(f"  Found {len(recipients)} recipient(s)")
    
    report_data = generate_daily_report_data()
    html_content = generate_daily_report_html(report_data)
    subject = f"📊 AgentMath Daily Pulse - {report_data.get('report_date', 'Today')}"
    
    sent, errors = send_email(recipients, subject, html_content, 'daily')
    print(f"  📧 Daily report: {sent} sent, {len(errors)} errors")

def send_weekly_report():
    """Generate and send weekly report (placeholder - uses daily format for now)"""
    print("\n📈 Generating Weekly Report...")
    
    # Check if enabled
    if get_report_setting('weekly_report_enabled', 'true') == 'false':
        print("  Weekly reports are disabled. Skipping.")
        return
    
    recipients = get_distribution_list('weekly')
    if not recipients:
        print("  No recipients for weekly reports. Skipping.")
        return
    
    print(f"  Found {len(recipients)} recipient(s)")
    
    # For now, use daily report format - can be enhanced later
    report_data = generate_daily_report_data()
    report_data['report_date'] = f"Week ending {datetime.utcnow().date()}"
    html_content = generate_daily_report_html(report_data)
    subject = f"📈 AgentMath Weekly Digest - Week {datetime.utcnow().isocalendar()[1]}"
    
    sent, errors = send_email(recipients, subject, html_content, 'weekly')
    print(f"  📧 Weekly report: {sent} sent, {len(errors)} errors")

def send_monthly_report():
    """Generate and send monthly report (placeholder - uses daily format for now)"""
    print("\n📋 Generating Monthly Report...")
    
    # Check if enabled
    if get_report_setting('monthly_report_enabled', 'true') == 'false':
        print("  Monthly reports are disabled. Skipping.")
        return
    
    recipients = get_distribution_list('monthly')
    if not recipients:
        print("  No recipients for monthly reports. Skipping.")
        return
    
    print(f"  Found {len(recipients)} recipient(s)")
    
    # For now, use daily report format - can be enhanced later
    last_month = datetime.utcnow().replace(day=1) - timedelta(days=1)
    report_data = generate_daily_report_data()
    report_data['report_date'] = last_month.strftime('%B %Y')
    html_content = generate_daily_report_html(report_data)
    subject = f"📋 AgentMath Monthly Review - {last_month.strftime('%B %Y')}"
    
    sent, errors = send_email(recipients, subject, html_content, 'monthly')
    print(f"  📧 Monthly report: {sent} sent, {len(errors)} errors")

def main():
    """Main entry point"""
    today = datetime.utcnow()
    day_of_week = today.weekday()  # 0=Monday, 6=Sunday
    day_of_month = today.day
    
    print("=" * 50)
    print(f"AgentMath Email Reports - {today.strftime('%Y-%m-%d %H:%M:%S')} UTC")
    print("=" * 50)
    
    # Check for command line argument
    if len(sys.argv) > 1:
        report_type = sys.argv[1].lower()
        
        if report_type == 'daily':
            send_daily_report()
        elif report_type == 'weekly':
            send_weekly_report()
        elif report_type == 'monthly':
            send_monthly_report()
        elif report_type == 'all':
            send_daily_report()
            send_weekly_report()
            send_monthly_report()
        else:
            print(f"Unknown report type: {report_type}")
            print("Usage: python send_reports.py [daily|weekly|monthly|all]")
            sys.exit(1)
    else:
        # Auto-determine which reports to send based on date
        print(f"Day of week: {['Mon','Tue','Wed','Thu','Fri','Sat','Sun'][day_of_week]}")
        print(f"Day of month: {day_of_month}")
        
        # Always send daily
        send_daily_report()
        
        # Send weekly on Mondays
        if day_of_week == 0:  # Monday
            send_weekly_report()
        else:
            print("\n📈 Weekly Report: Skipping (not Monday)")
        
        # Send monthly on the 1st
        if day_of_month == 1:
            send_monthly_report()
        else:
            print("\n📋 Monthly Report: Skipping (not 1st of month)")
    
    print("\n" + "=" * 50)
    print("Done!")
    print("=" * 50)

if __name__ == '__main__':
    with app.app_context():
        main()
