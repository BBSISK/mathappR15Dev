# utils/__init__.py
# Utility functions for AgentMath
# Extracted from app.py for better maintainability
#
# Revision: 1.0.0
# Date: 2025-12-27

# Authentication decorators
from utils.auth import (
    login_required,
    role_required,
    approved_required,
    guest_or_login_required
)

# Avatar helper functions
from utils.avatar import (
    get_avatar_user_points,
    avatar_owns_item,
    get_equipped_avatar,
    grant_default_avatar_items,
    get_animal_from_guest_code
)

# Badge helper functions
from utils.badges import (
    initialize_user_stats,
    update_user_stats_after_quiz,
    update_topic_progress,
    check_and_award_badges
)

# Domain restriction helper functions
from utils.domain import (
    extract_domain,
    get_all_domains_in_system,
    teacher_has_domain_access,
    get_teacher_accessible_domains,
    filter_students_by_domain_access,
    get_teacher_domain_statistics
)
