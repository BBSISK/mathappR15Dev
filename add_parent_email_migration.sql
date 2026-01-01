-- Migration: Add parent email column to guest_users and gdpr_consents tables
-- Date: 2025-12-18
-- Purpose: Store parent/guardian email for progress report notifications

-- Add gdpr_parent_email column to guest_users table
ALTER TABLE guest_users ADD COLUMN gdpr_parent_email TEXT;

-- Add parent_email column to gdpr_consents table (if it doesn't exist)
ALTER TABLE gdpr_consents ADD COLUMN parent_email TEXT;

-- Create index for future email queries
CREATE INDEX IF NOT EXISTS idx_guest_users_parent_email ON guest_users(gdpr_parent_email);
CREATE INDEX IF NOT EXISTS idx_gdpr_consents_parent_email ON gdpr_consents(parent_email);
