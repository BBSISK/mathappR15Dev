-- Migration: Email Reports System
-- Date: 2025-12-18
-- Purpose: Tables for email distribution lists and report configuration

-- Distribution list for email reports
CREATE TABLE IF NOT EXISTS email_distribution_list (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    recipient_name TEXT,
    report_type TEXT NOT NULL,  -- 'daily', 'weekly', 'monthly', 'all'
    is_active BOOLEAN DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_by INTEGER,
    UNIQUE(email, report_type)
);

-- Report configuration settings
CREATE TABLE IF NOT EXISTS report_settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    setting_key TEXT UNIQUE NOT NULL,
    setting_value TEXT,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_by INTEGER
);

-- Report send history/log
CREATE TABLE IF NOT EXISTS report_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    report_type TEXT NOT NULL,  -- 'daily', 'weekly', 'monthly'
    report_date DATE NOT NULL,
    recipients_count INTEGER,
    sent_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'sent',  -- 'sent', 'failed', 'partial'
    error_message TEXT,
    report_data TEXT  -- JSON snapshot of report metrics
);

-- Insert default settings
INSERT OR IGNORE INTO report_settings (setting_key, setting_value) VALUES 
    ('daily_report_enabled', 'true'),
    ('daily_report_time', '07:00'),
    ('weekly_report_enabled', 'true'),
    ('weekly_report_time', '07:00'),
    ('weekly_report_day', 'monday'),
    ('monthly_report_enabled', 'true'),
    ('monthly_report_time', '07:00'),
    ('report_timezone', 'Europe/Dublin'),
    ('include_charts', 'true'),
    ('school_name', 'Palmerstown Community School'),
    ('school_logo_url', ''),
    ('reply_to_email', '');

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_distribution_report_type ON email_distribution_list(report_type);
CREATE INDEX IF NOT EXISTS idx_distribution_active ON email_distribution_list(is_active);
CREATE INDEX IF NOT EXISTS idx_report_history_type ON report_history(report_type);
CREATE INDEX IF NOT EXISTS idx_report_history_date ON report_history(report_date);
