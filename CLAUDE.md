# AgentMath Project Context

> **Upload this file at the start of each conversation to give Claude full project context.**

---

## 🎯 Project Overview

| Item | Detail |
|------|--------|
| **Project** | AgentMath.app - Educational Mathematics Platform |
| **Purpose** | Adaptive learning platform for Irish secondary school students |
| **Host** | PythonAnywhere |
| **Path** | `/home/bbsisk/mathappR15Dev` |
| **Live URL** | https://agentmath.app (or bbsisk.pythonanywhere.com) |
| **Developer** | Barry Sisk - ICT Coordinator & Maths Teacher, Palmerstown Community School |

---

## ⚙️ Developer Preferences (CRITICAL)

### File Handling
- **NO PATCHING** - Always provide complete files ready for upload
- **No partial edits** - If a file needs changes, provide the entire updated file
- **Request files** - If a file is needed but not in context, ask for it to be uploaded

### Version Control
- Use revision comments at top of HTML files: `<!-- Revision X.X - YYYY-MM-DD - Description -->`
- Use revision comments at top of JS files: `/* Revision X.X - YYYY-MM-DD - Description */`
- Example: `<!-- Revision 3.25.0 - 2025-12-27 - Main JS extracted to student_app_main.js -->`
- Increment version numbers appropriately (major.minor.patch)

### Code Style
- **Mathematical Notation**: Use superscript for exponents (x², x³, x⁴) - NEVER use ^ symbol
  - Correct: `x² + 2x + 1` or `x<sup>2</sup>` in HTML
  - Incorrect: `x^2 + 2x + 1`
  - Common superscripts: ⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁿ
  - Common subscripts: ₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉
- **Date Format**: European format (DD/MM/YYYY) - e.g., 23/12/2025
- **Irish English spelling**: colour, centre, metres, organisation, etc.
- **Irish curriculum terminology**: Junior Cycle (not Middle School), Leaving Cert (not A-Levels), Honours/Ordinary (not Higher/Foundation)

### Irish Education System Standards
- **Junior Cycle**: 1st, 2nd, 3rd Year (ages 12-15)
- **Senior Cycle**: 5th, 6th Year (ages 16-18) - Note: Transition Year (4th Year) optional
- **Exam Bodies**: SEC (State Examinations Commission)
- **Levels**: Higher Level (HL), Ordinary Level (OL), Foundation Level (FL) for Junior Cycle
- **Leaving Cert**: Higher Level (H1-H8), Ordinary Level (O1-O8)
- **Grading**: Percentage-based internally, Grade bands for state exams
- **School Year**: September to May/June (exams in June)
- **Terms**: September-December, January-Easter, Easter-June

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python 3.x, Flask |
| **Database** | SQLite (mathquiz.db) |
| **ORM** | Flask-SQLAlchemy |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **CSS Framework** | Tailwind CSS (CDN) |
| **Icons** | Font Awesome 6.x |
| **Fonts** | Poppins (Google Fonts) |

---

## 📁 Modular File Structure (IMPORTANT)

### File Size Guidelines
To maintain code quality and ease of editing:
- **HTML files**: Target <3,000 lines (extract CSS/JS to external files)
- **JavaScript files**: Target <5,000 lines per file
- **CSS files**: Target <2,000 lines per file
- **Python files**: app.py is an exception (~26,000 lines) - future refactor planned

### Current File Structure

#### Core Application
| File | Purpose | Lines | Notes |
|------|---------|-------|-------|
| `app.py` | Main Flask application | ~26,000 | Future: Extract to blueprints |
| `mathquiz.db` | SQLite database | - | |
| `irish_school_calendar.py` | School holidays, streak logic | ~200 | |

#### Student Interface (Modular)
| File | Purpose | Lines |
|------|---------|-------|
| `templates/student_app.html` | Main student dashboard | ~7,500 |
| `static/css/student_app.css` | Student app styles | ~7,000 |
| `static/js/student_app_main.js` | Core quiz functionality | ~18,200 |
| `static/js/agentmath-modules.js` | Shared modules (sound, clock, tutorials) | ~3,300 |
| `static/js/quiz_milestones.js` | Milestone celebrations | ~230 |
| `static/js/who_am_i.js` | Who Am I puzzle | ~630 |
| `static/js/avatar.js` | Avatar system | ~500 |
| `static/js/team-play.js` | Team Play feature | ~650 |

#### Extraction Status (student_app.html)
| Component | Status | Lines | Location |
|-----------|--------|-------|----------|
| Main CSS | ✅ Extracted | 7,000 | `static/css/student_app.css` |
| Main JavaScript | ✅ Extracted | 18,200 | `static/js/student_app_main.js` |
| Adaptive Quiz | ⏳ TODO | 4,332 | Still inline |
| Password Modal | ⏳ TODO | 100 | Still inline |
| Tutorial Manager | ⏳ TODO | 245 | Still inline |
| Feedback System | ⏳ TODO | 145 | Still inline |
| Puzzle System | ⏳ TODO | 244 | Still inline |
| Prize PIN | ⏳ TODO | 193 | Still inline |

### Extraction Rules
When extracting code to external files:

1. **Check for Template Variables First**
   - Search for `{{` in the code block
   - If found inside JS code (not just `<script src>`), the code CANNOT be directly extracted
   - Template variables in `<script src="">` tags are OK - they stay in HTML

2. **File Naming Convention**
   - CSS: `static/css/{feature}.css`
   - JavaScript: `static/js/{feature}.js`
   - Keep names descriptive and lowercase with hyphens

3. **Loading Order Matters**
   - External JS files load asynchronously by default
   - Use `defer` attribute to maintain execution order
   - Dependencies must load before dependents

4. **After Extraction Checklist**
   - [ ] Update HTML to reference external file
   - [ ] Test all functionality
   - [ ] Check browser console for 404 errors
   - [ ] Verify no template variable errors
   - [ ] Update CLAUDE.md file structure table

---

## 🗄️ Database Models (32 tables)

### Core User System
- `users` - Student/teacher/admin accounts
- `classes` - Teacher-created classes
- `class_enrollment` - Student-class relationships

### Questions & Quizzes
- `questions` - Main question bank (50,000+ questions)
- `quiz_attempts` - Student quiz history
- `question_flags` - Flagged questions for review
- `user_question_history` - Tracks seen questions

### Progress & Gamification
- `user_stats` - Points, streaks, totals
- `badges` / `user_badges` - Achievement system
- `topic_progress` - Per-topic mastery levels
- `adaptive_progress` - Adaptive difficulty levels (L1-L12)

### Passport/ILP System
- `student_passport` - Passport metadata
- `passport_stamps` - Bronze/Silver/Gold per destination
- `passport_itinerary` - Learning journey stops
- `passport_self_assessment` - Confidence ratings
- `passport_milestones` - Exam dates, targets
- `passport_weekly_plan` - v2 weekly planner data
- `passport_plan_topics` - Topics assigned to weeks

### Special Features
- `weekly_puzzles` / `puzzle_user_status` - Puzzle of the Week
- `bonus_questions` / `bonus_question_attempts` - Bonus challenges
- `avatar_items` / `user_avatar_*` - Avatar system (feature flagged)
- `prizes` / `prize_redemptions` - Prize system (feature flagged)

---

## 🎓 Curriculum Structure

### Strands (Irish Curriculum)
| Strand | Icon | Topics |
|--------|------|--------|
| Numeracy | 🔢 | Arithmetic, Place Value, Rounding |
| Number | 🔢 | Fractions, Decimals, Percentages, Ratios |
| Algebra | 📐 | Expressions, Equations, Functions |
| Geometry | 📐 | Shapes, Coordinate Geometry, Trigonometry |
| Statistics | 📊 | Data, Probability, Distributions |
| Financial | 💰 | Interest, Tax, Budgeting |

### Difficulty Levels
- **L1-L4**: Foundation (Bronze stamp)
- **L5-L8**: Intermediate (Silver stamp)
- **L9-L12**: Advanced (Gold stamp)

### Curricula Supported
| Code | Name | Target |
|------|------|--------|
| L1LP | Level 1 Learning Programme | Students with significant learning needs |
| L2LP | Level 2 Learning Programme | Students with moderate learning needs |
| JC | Junior Cycle | 1st-3rd Year |
| LC_OL | Leaving Cert Ordinary Level | 5th-6th Year |
| LC_HL | Leaving Cert Higher Level | 5th-6th Year |

---

## 🛂 Individualised Learning Plan (ILP) / Maths Passport

### Current Status (Revision 3.2 - December 2025)

#### ✅ Completed Features
- 5-step Setup Wizard (curriculum, exam date, strands, entry levels, diagnostics)
- Weekly Planner v2 with Irish school calendar integration
- Drag & drop topic reordering
- Pin/unpin topics to specific weeks
- Passport cover with destinations grid
- Progress tracking per destination
- 19+ API endpoints (`/api/passport/*` and `/api/passport/v2/*`)

#### ⚠️ In Progress / Placeholder
- Stamps page (shows mocked data)
- World map visualization
- Teacher dashboard integration

#### 🔮 Planned
- Real-time reactive recommendations
- PDF export for parent meetings
- Teacher view/edit of student passports
- Misconception detection

### Key Passport Tables
```sql
student_passport          -- Core passport record
passport_stamps           -- Bronze/Silver/Gold per destination
passport_itinerary        -- Learning journey stops
passport_self_assessment  -- Confidence ratings
passport_milestones       -- Exam dates, targets
passport_weekly_plan      -- v2 generated plans
passport_plan_topics      -- Topics per week
```

---

## 🎮 Feature Flags

Controlled via environment variables or `FEATURE_FLAGS` dict in app.py:

| Flag | Default | Purpose |
|------|---------|---------|
| `AVATAR_SYSTEM_ENABLED` | false | Avatar customization |
| `AVATAR_SHOP_ENABLED` | false | Buying avatar items |
| `PRIZE_SYSTEM_ENABLED` | false | School prize redemptions |

---

## 🔗 Key API Endpoints (335 total routes)

### Student APIs
- `GET /api/questions/<topic>` - Get quiz questions
- `POST /api/submit` - Submit quiz answers
- `GET /api/adaptive/progress` - Get adaptive levels
- `GET /api/stats` - Get student statistics

### Passport APIs
- `GET /api/passport` - Get passport data
- `POST /api/passport/setup` - Initialize passport
- `GET /api/passport/v2/plan` - Get weekly plan
- `POST /api/passport/v2/generate-plan` - Generate study plan
- `POST /api/passport/v2/move-topic` - Drag/drop topic

### Admin APIs
- `GET /api/admin/stats` - System statistics
- `POST /api/admin/question` - Add/edit questions
- `GET /api/admin/users` - User management

---

## 📋 Current Priorities (December 2025)

1. **ILP/Passport** - Complete stamps system, teacher integration
2. **LC Higher Level** - Finish remaining topic generators
3. **Interactive Activities** - Flow Sums, Number Pyramids, Code Breaker
4. **Code Optimisation** - Continue extracting inline JS from HTML files
5. **VSware Integration** - Future roadmap item

---

## 🔧 Common Tasks

### Adding a New Topic
1. Admin Dashboard → Topic Management → Add Topic
2. Create question generator file if needed
3. Add to relevant curriculum mapping

### Database Sync (Dev ↔ Production)
- Use established sync workflow
- Preserve user activity during sync
- Verify data integrity after sync

### Testing New Features
1. Test on dev instance first
2. Check mobile responsiveness
3. Verify with guest and logged-in users

### Extracting Inline Code to External Files
1. Identify the code block in the HTML file
2. Check for `{{` template variables - if found in JS code, cannot extract directly
3. Create new file in appropriate `static/` directory
4. Add `<script src="">` or `<link href="">` in HTML
5. Remove inline code from HTML
6. Test thoroughly - check browser console for errors
7. Update this CLAUDE.md with new file structure

---

## 📝 Notes for Claude

- Barry prefers complete file uploads over patching
- Include verification steps and rollback procedures
- Use Irish cultural references where appropriate
- Maintain revision numbering in HTML/JS/CSS files
- The platform serves real students - prioritize stability
- When modifying files, check current line counts against targets
- Suggest extractions when files exceed size guidelines

---

## 🚀 Future Refactoring Roadmap

### app.py Blueprint Extraction (Planned)
The current monolithic app.py (~26,000 lines) should eventually be split into Flask Blueprints. This requires:
1. First: Extract models to `models.py`
2. Then: Extract helper functions to `utils.py`
3. Finally: Extract route groups to blueprints

Estimated effort: 4-6 hours of careful work

### student_app.html Further Extraction (Ready Now)
Can reduce from ~7,500 lines to ~2,300 lines by extracting:
- Adaptive Quiz System (4,332 lines) → `static/js/adaptive_quiz.js`
- Smaller modules (~927 lines) → `static/js/student_app_utils.js`

---

*Last Updated: 27 December 2025*
