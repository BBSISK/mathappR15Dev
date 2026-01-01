-- Maths Passport Database Migration
-- Run this script to create the passport tables

-- Student passport profile
CREATE TABLE IF NOT EXISTS student_passport (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    guest_code TEXT,
    target_curriculum TEXT,          -- 'JC', 'LC_HL', 'LC_OL', 'L1LP', 'L2LP', 'general'
    target_exam_date DATE,
    journey_started DATE DEFAULT CURRENT_DATE,
    total_distance INTEGER DEFAULT 0, -- Gamification: km travelled
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Index for faster lookups
CREATE INDEX IF NOT EXISTS idx_passport_user ON student_passport(user_id);
CREATE INDEX IF NOT EXISTS idx_passport_guest ON student_passport(guest_code);

-- Stamps earned
CREATE TABLE IF NOT EXISTS passport_stamps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    passport_id INTEGER NOT NULL,
    destination_id TEXT NOT NULL,             -- 'number_island', 'fraction_falls', etc.
    stamp_tier TEXT NOT NULL,                 -- 'bronze', 'silver', 'gold'
    level_start INTEGER,                      -- 1, 5, or 9
    level_end INTEGER,                        -- 4, 8, or 12
    earned_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    points_at_earn INTEGER,                   -- Points when stamp earned
    FOREIGN KEY (passport_id) REFERENCES student_passport(id),
    UNIQUE(passport_id, destination_id, stamp_tier)
);

CREATE INDEX IF NOT EXISTS idx_stamps_passport ON passport_stamps(passport_id);

-- Itinerary (planned journey)
CREATE TABLE IF NOT EXISTS passport_itinerary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    passport_id INTEGER NOT NULL,
    destination_id TEXT NOT NULL,
    stop_order INTEGER,                       -- 1, 2, 3...
    status TEXT DEFAULT 'planned',            -- 'planned', 'current', 'completed', 'skipped'
    suggested_start_level INTEGER,            -- From self-assessment
    priority TEXT DEFAULT 'normal',           -- 'high', 'normal', 'low'
    added_by TEXT DEFAULT 'student',          -- 'student', 'teacher', 'system'
    teacher_notes TEXT,                       -- If teacher modified
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (passport_id) REFERENCES student_passport(id),
    UNIQUE(passport_id, destination_id)
);

CREATE INDEX IF NOT EXISTS idx_itinerary_passport ON passport_itinerary(passport_id);

-- Self-assessment results
CREATE TABLE IF NOT EXISTS passport_self_assessment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    passport_id INTEGER NOT NULL,
    destination_id TEXT NOT NULL,
    confidence_rating INTEGER,                -- 1-5 (emoji scale)
    quick_check_score INTEGER,                -- Score from quick check (if taken)
    quick_check_questions INTEGER,            -- Total questions in quick check
    assessed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (passport_id) REFERENCES student_passport(id),
    UNIQUE(passport_id, destination_id)
);

CREATE INDEX IF NOT EXISTS idx_assessment_passport ON passport_self_assessment(passport_id);

-- Checkpoints/Milestones
CREATE TABLE IF NOT EXISTS passport_milestones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    passport_id INTEGER NOT NULL,
    title TEXT,
    milestone_date DATE,
    milestone_type TEXT,                      -- 'exam', 'mock', 'checkpoint', 'custom'
    target_stamps INTEGER,                    -- Target stamps by this date
    reached BOOLEAN DEFAULT 0,
    reached_at DATETIME,
    FOREIGN KEY (passport_id) REFERENCES student_passport(id)
);

CREATE INDEX IF NOT EXISTS idx_milestones_passport ON passport_milestones(passport_id);

-- Success message
SELECT 'Maths Passport tables created successfully!' as message;
