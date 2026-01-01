-- =====================================================
-- GUEST TO ACCOUNT CONVERSION - DATABASE MIGRATION
-- AgentMath R15Dev
-- Run on PythonAnywhere: sqlite3 /home/bbsisk/mathappR15Dev/instance/mathquiz.db < this_file.sql
-- =====================================================

-- Step 1: Add columns to guest_users table for account linking
ALTER TABLE guest_users ADD COLUMN user_id INTEGER REFERENCES users(id);
ALTER TABLE guest_users ADD COLUMN converted_at DATETIME;
ALTER TABLE guest_users ADD COLUMN gdpr_consent_date DATE;
ALTER TABLE guest_users ADD COLUMN gdpr_parent_name TEXT;
ALTER TABLE guest_users ADD COLUMN full_name TEXT;
ALTER TABLE guest_users ADD COLUMN class_group TEXT;
ALTER TABLE guest_users ADD COLUMN teacher_id INTEGER REFERENCES users(id);
ALTER TABLE guest_users ADD COLUMN display_name TEXT;

-- Step 2: Create GDPR consent audit table
CREATE TABLE IF NOT EXISTS gdpr_consents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    guest_code TEXT NOT NULL,
    user_id INTEGER REFERENCES users(id),
    student_name TEXT NOT NULL,
    parent_name TEXT NOT NULL,
    consent_date DATE NOT NULL,
    form_received_date DATE NOT NULL,
    verified_by INTEGER NOT NULL REFERENCES users(id),
    consent_type TEXT DEFAULT 'parental',  -- 'parental' or 'self' (if 16+)
    email_updates_consent INTEGER DEFAULT 0,
    research_consent INTEGER DEFAULT 0,
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Step 3: Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_guest_users_teacher ON guest_users(teacher_id);
CREATE INDEX IF NOT EXISTS idx_guest_users_user ON guest_users(user_id);
CREATE INDEX IF NOT EXISTS idx_guest_users_converted ON guest_users(converted_at);
CREATE INDEX IF NOT EXISTS idx_gdpr_consents_guest ON gdpr_consents(guest_code);
CREATE INDEX IF NOT EXISTS idx_gdpr_consents_user ON gdpr_consents(user_id);

-- Step 4: Verify changes
SELECT sql FROM sqlite_master WHERE name = 'guest_users';
SELECT sql FROM sqlite_master WHERE name = 'gdpr_consents';

-- Show sample of guest_users with new columns
SELECT guest_code, total_score, last_active, user_id, converted_at, teacher_id 
FROM guest_users 
LIMIT 5;

-- =====================================================
-- NOTES:
-- - user_id: Links to users.id after conversion
-- - converted_at: When the conversion happened
-- - gdpr_consent_date: Date on the signed consent form
-- - gdpr_parent_name: Name of parent who signed
-- - full_name: Student's real name after conversion
-- - teacher_id: Which teacher manages this student
-- - display_name: Optional display name for the guest
-- =====================================================
