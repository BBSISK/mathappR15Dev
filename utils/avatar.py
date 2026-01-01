# utils/avatar.py
# Avatar helper functions for AgentMath
# Extracted from app.py for better maintainability
#
# Revision: 1.0.2
# Date: 2025-12-31
#
# Fixes in 1.0.2:
# - Fixed get_avatar_user_points to query guest_users table for guests
# - UserStats doesn't have guest_code column - guests use guest_users table
#
# Fix in 1.0.1: Corrected field names in get_equipped_avatar


def get_avatar_user_points(user_id=None, guest_code=None):
    """Get user's total points and level for avatar shop purchases"""
    from models import db, UserStats  # Late import
    from sqlalchemy import text
    
    if user_id:
        stats = UserStats.query.filter_by(user_id=user_id).first()
        if not stats:
            return 0, 1
        points = stats.total_points or 0
    elif guest_code:
        # Guests store points in guest_users table, not UserStats
        result = db.session.execute(
            text("SELECT total_score FROM guest_users WHERE guest_code = :code"),
            {'code': guest_code}
        ).fetchone()
        if not result:
            return 0, 1
        points = result[0] or 0
    else:
        return 0, 1

    level = (points // 1000) + 1  # Level up every 1000 points
    return points, level


def avatar_owns_item(item_id, user_id=None, guest_code=None):
    """Check if user owns an avatar item"""
    from models import UserAvatarInventory  # Late import
    
    if user_id:
        return UserAvatarInventory.query.filter_by(
            user_id=user_id, item_id=item_id
        ).first() is not None
    elif guest_code:
        return UserAvatarInventory.query.filter_by(
            guest_code=guest_code, item_id=item_id
        ).first() is not None
    return False


def get_equipped_avatar(user_id=None, guest_code=None):
    """Get currently equipped avatar configuration

    NOTE: guest_code takes priority because repeat guests have BOTH
    a shared user_id AND their unique guest_code in session.
    
    Returns the simple animal-based avatar config with:
    - animal: the base animal (panda, fox, etc.)
    - hat, glasses, background, accessory: equipped items
    """
    from models import UserAvatarEquipped  # Late import
    
    equipped = None

    # Check guest_code FIRST (repeat guests have both user_id and guest_code)
    if guest_code:
        equipped = UserAvatarEquipped.query.filter_by(guest_code=guest_code).first()
    elif user_id:
        equipped = UserAvatarEquipped.query.filter_by(user_id=user_id).first()

    if not equipped:
        return None

    # Return the simple avatar config using the model's to_dict()
    return equipped.to_dict()


def grant_default_avatar_items(user_id=None, guest_code=None):
    """Grant default avatar items to new users"""
    from models import db, AvatarItem, UserAvatarInventory, UserAvatarEquipped  # Late import
    
    # Get all default items
    default_items = AvatarItem.query.filter_by(is_default=True).all()

    for item in default_items:
        # Check if already owned
        if user_id:
            existing = UserAvatarInventory.query.filter_by(
                user_id=user_id, item_id=item.id
            ).first()
        else:
            existing = UserAvatarInventory.query.filter_by(
                guest_code=guest_code, item_id=item.id
            ).first()

        if not existing:
            inv = UserAvatarInventory(
                user_id=user_id,
                guest_code=guest_code,
                item_id=item.id
            )
            db.session.add(inv)

    db.session.commit()


def get_animal_from_guest_code(guest_code):
    """Extract animal name from guest code format like 'panda42'"""
    if not guest_code:
        return 'panda'

    # Match pattern: animal name followed by numbers
    import re
    match = re.match(r'^([a-z]+)(\d+)$', guest_code.lower())
    if match:
        return match.group(1)

    # Try just letters (in case no number)
    letters = ''.join(c for c in guest_code.lower() if c.isalpha())
    if letters:
        animals = ['panda', 'koala', 'fox', 'owl', 'bear', 'lion', 'tiger', 'wolf', 'eagle', 'hawk', 'dolphin', 'whale', 'penguin', 'rabbit', 'deer']
        if letters in animals:
            return letters

    # Default fallback
    return 'panda'
