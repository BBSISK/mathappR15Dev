"""
ADAPTIVE QUESTIONS SCHEMA
=========================
Creates separate database tables for the adaptive learning question bank.
Completely independent from the existing 'questions' table.

Run this migration to set up the adaptive question system:
    python adaptive_questions_schema.py

Tables Created:
    - questions_adaptive: Enhanced question storage with 10 sub-levels
    - skill_tags_adaptive: Skill taxonomy for tagging questions  
    - question_skills_adaptive: Junction table for question-skill mapping
    - topic_progressions_adaptive: Defines learning ladders per topic
"""

import sqlite3
import os
from datetime import datetime

# Path to database
DB_PATH = 'instance/mathquiz.db'

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_adaptive_tables():
    """Create all adaptive learning tables"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    print("=" * 60)
    print("ADAPTIVE QUESTIONS SCHEMA MIGRATION")
    print("=" * 60)
    
    # =========================================================================
    # TABLE 1: questions_adaptive
    # Main question storage with enhanced difficulty tracking
    # =========================================================================
    print("\n1. Creating questions_adaptive table...")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions_adaptive (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            
            -- Core question data
            topic VARCHAR(50) NOT NULL,
            question_text TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_answer INTEGER NOT NULL,  -- 0=A, 1=B, 2=C, 3=D
            explanation TEXT NOT NULL,
            
            -- Enhanced difficulty system (1-10 scale)
            difficulty_level INTEGER NOT NULL CHECK(difficulty_level BETWEEN 1 AND 10),
            difficulty_band VARCHAR(20) NOT NULL DEFAULT 'beginner',  -- beginner/intermediate/advanced (for compatibility)
            
            -- Complexity metadata (JSON)
            complexity_factors TEXT,  -- JSON: {"num_terms": 2, "has_negatives": true, "has_fractions": false, ...}
            
            -- Learning metadata
            estimated_time_seconds INTEGER DEFAULT 30,
            hint_text TEXT,
            hint_penalty INTEGER DEFAULT 50,
            
            -- Question type classification
            question_type VARCHAR(50),  -- 'calculation', 'word_problem', 'conceptual', 'multi_step'
            
            -- Tracking
            times_shown INTEGER DEFAULT 0,
            times_correct INTEGER DEFAULT 0,
            avg_response_time REAL,
            
            -- Metadata
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_active BOOLEAN DEFAULT 1,
            
            -- Prevent exact duplicates
            UNIQUE(topic, difficulty_level, question_text)
        )
    """)
    
    # Create indexes for fast lookups
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_questions_adaptive_topic 
        ON questions_adaptive(topic, difficulty_level, is_active)
    """)
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_questions_adaptive_band 
        ON questions_adaptive(topic, difficulty_band, is_active)
    """)
    
    print("   ✓ questions_adaptive table created")
    
    # =========================================================================
    # TABLE 2: skill_tags_adaptive  
    # Taxonomy of mathematical skills for fine-grained tracking
    # =========================================================================
    print("\n2. Creating skill_tags_adaptive table...")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS skill_tags_adaptive (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tag_key VARCHAR(50) NOT NULL UNIQUE,
            tag_name VARCHAR(100) NOT NULL,
            tag_category VARCHAR(50),  -- 'number_type', 'operation', 'format', 'complexity'
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Insert default skill tags
    default_tags = [
        # Number types
        ('positive_integers', 'Positive Integers', 'number_type', 'Questions using only positive whole numbers'),
        ('negative_numbers', 'Negative Numbers', 'number_type', 'Questions involving negative numbers'),
        ('fractions', 'Fractions', 'number_type', 'Questions involving fractions'),
        ('decimals', 'Decimals', 'number_type', 'Questions involving decimal numbers'),
        ('mixed_numbers', 'Mixed Numbers', 'number_type', 'Questions with mixed number formats'),
        
        # Operations
        ('addition', 'Addition', 'operation', 'Questions involving addition'),
        ('subtraction', 'Subtraction', 'operation', 'Questions involving subtraction'),
        ('multiplication', 'Multiplication', 'operation', 'Questions involving multiplication'),
        ('division', 'Division', 'operation', 'Questions involving division'),
        ('exponents', 'Exponents/Powers', 'operation', 'Questions involving powers'),
        ('roots', 'Square Roots', 'operation', 'Questions involving roots'),
        
        # Algebraic complexity
        ('single_variable', 'Single Variable', 'algebra', 'One unknown variable'),
        ('multi_variable', 'Multiple Variables', 'algebra', 'Multiple unknown variables'),
        ('linear', 'Linear Expressions', 'algebra', 'First degree expressions'),
        ('quadratic', 'Quadratic Expressions', 'algebra', 'Second degree expressions'),
        ('brackets', 'Brackets/Parentheses', 'algebra', 'Requires expanding or factoring brackets'),
        
        # Problem format
        ('word_problem', 'Word Problem', 'format', 'Real-world context question'),
        ('pure_calculation', 'Pure Calculation', 'format', 'Direct mathematical calculation'),
        ('diagram_based', 'Diagram Based', 'format', 'Requires interpreting a diagram'),
        ('multi_step', 'Multi-Step', 'format', 'Requires multiple solution steps'),
        ('single_step', 'Single Step', 'format', 'Can be solved in one step'),
        
        # Complexity indicators
        ('mental_math', 'Mental Math Friendly', 'complexity', 'Can be solved without paper'),
        ('calculator_helpful', 'Calculator Helpful', 'complexity', 'Calculator would speed up solution'),
        ('large_numbers', 'Large Numbers', 'complexity', 'Uses numbers > 100'),
        ('small_numbers', 'Small Numbers', 'complexity', 'Uses numbers 1-20'),
    ]
    
    for tag in default_tags:
        try:
            cursor.execute("""
                INSERT OR IGNORE INTO skill_tags_adaptive (tag_key, tag_name, tag_category, description)
                VALUES (?, ?, ?, ?)
            """, tag)
        except:
            pass  # Skip if exists
    
    print("   ✓ skill_tags_adaptive table created with default tags")
    
    # =========================================================================
    # TABLE 3: question_skills_adaptive
    # Junction table linking questions to their skill tags
    # =========================================================================
    print("\n3. Creating question_skills_adaptive table...")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS question_skills_adaptive (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id INTEGER NOT NULL,
            skill_tag_id INTEGER NOT NULL,
            relevance REAL DEFAULT 1.0,  -- How strongly this skill applies (0-1)
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (question_id) REFERENCES questions_adaptive(id) ON DELETE CASCADE,
            FOREIGN KEY (skill_tag_id) REFERENCES skill_tags_adaptive(id) ON DELETE CASCADE,
            UNIQUE(question_id, skill_tag_id)
        )
    """)
    
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_question_skills_question 
        ON question_skills_adaptive(question_id)
    """)
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_question_skills_tag 
        ON question_skills_adaptive(skill_tag_id)
    """)
    
    print("   ✓ question_skills_adaptive junction table created")
    
    # =========================================================================
    # TABLE 4: topic_progressions_adaptive
    # Defines the learning ladder for each topic
    # =========================================================================
    print("\n4. Creating topic_progressions_adaptive table...")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS topic_progressions_adaptive (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic VARCHAR(50) NOT NULL,
            level INTEGER NOT NULL CHECK(level BETWEEN 1 AND 10),
            level_name VARCHAR(100) NOT NULL,
            level_description TEXT NOT NULL,
            target_skills TEXT,  -- JSON array of skill_tag_keys required at this level
            example_complexity TEXT,  -- Example of question complexity at this level
            min_questions INTEGER DEFAULT 20,  -- Minimum questions needed at this level
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(topic, level)
        )
    """)
    
    print("   ✓ topic_progressions_adaptive table created")
    
    # =========================================================================
    # TABLE 5: user_skill_mastery_adaptive
    # Tracks individual user mastery of specific skills
    # =========================================================================
    print("\n5. Creating user_skill_mastery_adaptive table...")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_skill_mastery_adaptive (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,  -- NULL for guest_code users
            guest_code VARCHAR(20),  -- NULL for registered users
            skill_tag_id INTEGER NOT NULL,
            topic VARCHAR(50) NOT NULL,
            
            -- Mastery metrics
            attempts INTEGER DEFAULT 0,
            correct INTEGER DEFAULT 0,
            mastery_score REAL DEFAULT 0.0,  -- 0.0 to 1.0
            
            -- Recent performance (JSON array of last 10 results)
            recent_results TEXT,
            
            -- Timestamps
            first_attempt_at TIMESTAMP,
            last_attempt_at TIMESTAMP,
            
            FOREIGN KEY (skill_tag_id) REFERENCES skill_tags_adaptive(id),
            UNIQUE(user_id, guest_code, skill_tag_id, topic)
        )
    """)
    
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_user_skill_mastery_user 
        ON user_skill_mastery_adaptive(user_id, topic)
    """)
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_user_skill_mastery_guest 
        ON user_skill_mastery_adaptive(guest_code, topic)
    """)
    
    print("   ✓ user_skill_mastery_adaptive table created")
    
    # =========================================================================
    # Commit and verify
    # =========================================================================
    conn.commit()
    
    print("\n" + "=" * 60)
    print("VERIFICATION")
    print("=" * 60)
    
    # Verify tables exist
    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name LIKE '%_adaptive'
        ORDER BY name
    """)
    tables = cursor.fetchall()
    print(f"\nAdaptive tables created: {len(tables)}")
    for t in tables:
        cursor.execute(f"SELECT COUNT(*) FROM {t['name']}")
        count = cursor.fetchone()[0]
        print(f"   ✓ {t['name']}: {count} rows")
    
    conn.close()
    
    print("\n" + "=" * 60)
    print("MIGRATION COMPLETE!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Run question_generator_adaptive.py to populate questions")
    print("2. Use /api/adaptive-quiz/* endpoints for adaptive quizzes")
    print("=" * 60)


def seed_topic_progressions():
    """Seed the topic progressions with example learning ladders"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    print("\nSeeding topic progressions...")
    
    # Example: Algebra progression
    algebra_progression = [
        (1, "Foundation", "Understand what variables represent", 
         '["single_variable", "positive_integers", "single_step"]',
         "x + 3 = 5"),
        (2, "Simple Equations", "Solve one-step equations with addition/subtraction",
         '["single_variable", "positive_integers", "addition", "subtraction"]',
         "x - 7 = 12"),
        (3, "Multiplication Equations", "Solve equations with multiplication/division",
         '["single_variable", "positive_integers", "multiplication", "division"]',
         "3x = 15"),
        (4, "Two-Step Equations", "Combine operations in two steps",
         '["single_variable", "positive_integers", "multi_step"]',
         "2x + 5 = 13"),
        (5, "Negative Numbers", "Work with negative coefficients and solutions",
         '["single_variable", "negative_numbers", "multi_step"]',
         "-3x + 4 = -8"),
        (6, "Brackets Introduction", "Expand simple brackets",
         '["single_variable", "brackets", "multi_step"]',
         "2(x + 3) = 14"),
        (7, "Complex Brackets", "Multiple terms and brackets",
         '["single_variable", "brackets", "negative_numbers"]',
         "3(x - 2) + 4 = 2x + 5"),
        (8, "Fractions in Equations", "Equations with fractional coefficients",
         '["single_variable", "fractions", "multi_step"]',
         "½x + 3 = 7"),
        (9, "Variables Both Sides", "Variables on both sides with complexity",
         '["single_variable", "brackets", "fractions", "negative_numbers"]',
         "2(3x - 1) = 4x + 6"),
        (10, "Challenge Level", "Multi-step with all complexity factors",
         '["multi_step", "brackets", "fractions", "negative_numbers"]',
         "-2(x + 3) + ½x = 3(1 - x) + 5"),
    ]
    
    for level, name, desc, skills, example in algebra_progression:
        try:
            cursor.execute("""
                INSERT OR REPLACE INTO topic_progressions_adaptive 
                (topic, level, level_name, level_description, target_skills, example_complexity)
                VALUES (?, ?, ?, ?, ?, ?)
            """, ('solving_equations', level, name, desc, skills, example))
        except Exception as e:
            print(f"   Warning: {e}")
    
    # Example: Fractions progression
    fractions_progression = [
        (1, "Understanding Fractions", "Identify and compare simple fractions",
         '["fractions", "single_step", "small_numbers"]',
         "Which is larger: ½ or ⅓?"),
        (2, "Equivalent Fractions", "Find equivalent fractions",
         '["fractions", "multiplication", "small_numbers"]',
         "Find a fraction equivalent to 2/4"),
        (3, "Adding Like Denominators", "Add fractions with same denominator",
         '["fractions", "addition", "single_step"]',
         "1/5 + 2/5 = ?"),
        (4, "Subtracting Like Denominators", "Subtract fractions with same denominator",
         '["fractions", "subtraction", "single_step"]',
         "4/7 - 2/7 = ?"),
        (5, "Unlike Denominators Simple", "Add/subtract with simple LCD",
         '["fractions", "addition", "subtraction", "multi_step"]',
         "1/2 + 1/4 = ?"),
        (6, "Unlike Denominators Complex", "Add/subtract requiring LCD calculation",
         '["fractions", "multi_step"]',
         "2/3 + 3/5 = ?"),
        (7, "Multiplying Fractions", "Multiply fractions and simplify",
         '["fractions", "multiplication"]',
         "2/3 × 3/4 = ?"),
        (8, "Dividing Fractions", "Divide fractions using reciprocal",
         '["fractions", "division", "multi_step"]',
         "3/4 ÷ 2/5 = ?"),
        (9, "Mixed Numbers", "Operations with mixed numbers",
         '["fractions", "mixed_numbers", "multi_step"]',
         "2½ + 1¾ = ?"),
        (10, "Complex Operations", "Multi-step with mixed operations",
         '["fractions", "mixed_numbers", "multi_step", "brackets"]',
         "(2/3 + 1/4) × 2½ = ?"),
    ]
    
    for level, name, desc, skills, example in fractions_progression:
        try:
            cursor.execute("""
                INSERT OR REPLACE INTO topic_progressions_adaptive 
                (topic, level, level_name, level_description, target_skills, example_complexity)
                VALUES (?, ?, ?, ?, ?, ?)
            """, ('fractions', level, name, desc, skills, example))
        except Exception as e:
            print(f"   Warning: {e}")
    
    conn.commit()
    conn.close()
    print("   ✓ Topic progressions seeded")


def rollback_adaptive_tables():
    """Remove all adaptive tables (for clean re-migration)"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    print("\n⚠️  ROLLING BACK ADAPTIVE TABLES...")
    
    tables = [
        'user_skill_mastery_adaptive',
        'question_skills_adaptive',
        'topic_progressions_adaptive',
        'skill_tags_adaptive',
        'questions_adaptive'
    ]
    
    for table in tables:
        try:
            cursor.execute(f"DROP TABLE IF EXISTS {table}")
            print(f"   ✓ Dropped {table}")
        except Exception as e:
            print(f"   ✗ Error dropping {table}: {e}")
    
    conn.commit()
    conn.close()
    print("\nRollback complete.")


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--rollback':
        rollback_adaptive_tables()
    else:
        create_adaptive_tables()
        seed_topic_progressions()
