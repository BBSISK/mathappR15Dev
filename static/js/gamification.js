/**
 * AgentMath Gamification Module
 * Hot streaks, achievements, confetti, and milestone celebrations
 * Rev 3.0.11 - 2025-12-12
 */

// =====================================================
// HOT STREAK INDICATOR
// =====================================================

function updateHotStreakDisplay(streak) {
    const streakDisplay = document.getElementById('streakDisplay');
    const streakCount = document.getElementById('streakCount');
    const streakFlame = document.querySelector('.streak-flame');
    
    if (!streakDisplay || !streakCount) return;
    
    streakCount.textContent = streak;
    
    // Update visual state based on streak
    if (streak >= 10) {
        streakDisplay.className = 'hot-streak-display streak-blazing';
        if (streakFlame) streakFlame.textContent = '🔥';
    } else if (streak >= 5) {
        streakDisplay.className = 'hot-streak-display streak-hot';
        if (streakFlame) streakFlame.textContent = '🔥';
    } else if (streak >= 3) {
        streakDisplay.className = 'hot-streak-display streak-warm';
        if (streakFlame) streakFlame.textContent = '🔥';
    } else {
        streakDisplay.className = 'hot-streak-display streak-cold';
        if (streakFlame) streakFlame.textContent = '💨';
    }
    
    // Animate on milestone streaks
    if (streak === 3 || streak === 5 || streak === 10) {
        streakDisplay.style.animation = 'none';
        streakDisplay.offsetHeight; // Trigger reflow
        streakDisplay.style.animation = 'streakPulse 0.5s ease-out';
    }
}

// Update streak display for adaptive quiz
function updateAdaptiveStreakDisplay() {
    const streakDisplay = document.getElementById('adaptiveStreakDisplay');
    const streakCount = document.getElementById('adaptiveStreakCount');
    const streakFlame = streakDisplay?.querySelector('.streak-flame');
    
    if (!streakDisplay || !streakCount) return;
    
    const streak = adaptiveState?.sessionStreak || 0;
    streakCount.textContent = streak;
    
    // Update visual state based on streak
    if (streak >= 10) {
        streakDisplay.className = 'hot-streak-display streak-blazing';
        if (streakFlame) streakFlame.textContent = '🔥';
    } else if (streak >= 5) {
        streakDisplay.className = 'hot-streak-display streak-hot';
        if (streakFlame) streakFlame.textContent = '🔥';
    } else if (streak >= 3) {
        streakDisplay.className = 'hot-streak-display streak-warm';
        if (streakFlame) streakFlame.textContent = '🔥';
    } else {
        streakDisplay.className = 'hot-streak-display streak-cold';
        if (streakFlame) streakFlame.textContent = '💨';
    }
    
    // Animate on milestone streaks
    if (streak === 3 || streak === 5 || streak === 10) {
        streakDisplay.style.animation = 'none';
        streakDisplay.offsetHeight; // Trigger reflow
        streakDisplay.style.animation = 'streakPulse 0.5s ease-out';
    }
}

// =====================================================
// CONFETTI EFFECT
// =====================================================

function createConfetti(container) {
    const colors = ['#fbbf24', '#f59e0b', '#22c55e', '#3b82f6', '#8b5cf6', '#ec4899'];
    const confettiCount = 100;
    
    for (let i = 0; i < confettiCount; i++) {
        const confetti = document.createElement('div');
        confetti.style.cssText = `
            position: absolute;
            width: ${Math.random() * 10 + 5}px;
            height: ${Math.random() * 10 + 5}px;
            background: ${colors[Math.floor(Math.random() * colors.length)]};
            left: ${Math.random() * 100}%;
            top: -10px;
            opacity: ${Math.random() * 0.5 + 0.5};
            border-radius: ${Math.random() > 0.5 ? '50%' : '0'};
            transform: rotate(${Math.random() * 360}deg);
        `;
        container.appendChild(confetti);
        
        // Animate falling
        const duration = Math.random() * 2 + 2;
        const xDrift = (Math.random() - 0.5) * 200;
        confetti.animate([
            { transform: `translateY(0) translateX(0) rotate(0deg)`, opacity: 1 },
            { transform: `translateY(${container.offsetHeight + 50}px) translateX(${xDrift}px) rotate(${Math.random() * 720}deg)`, opacity: 0 }
        ], {
            duration: duration * 1000,
            easing: 'ease-out'
        });
        
        // Remove after animation
        setTimeout(() => confetti.remove(), duration * 1000);
    }
}

function createAchievementConfetti(container) {
    const colors = ['#fbbf24', '#f59e0b', '#22c55e', '#3b82f6', '#8b5cf6', '#ec4899', '#ef4444'];
    const confettiCount = 50;
    
    for (let i = 0; i < confettiCount; i++) {
        const confetti = document.createElement('div');
        const size = Math.random() * 8 + 4;
        const isCircle = Math.random() > 0.5;
        
        confetti.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size}px;
            background: ${colors[Math.floor(Math.random() * colors.length)]};
            left: 50%;
            top: 50%;
            opacity: 1;
            border-radius: ${isCircle ? '50%' : '2px'};
            pointer-events: none;
        `;
        container.appendChild(confetti);
        
        // Explode outward from center
        const angle = (Math.PI * 2 * i) / confettiCount + Math.random() * 0.5;
        const distance = 100 + Math.random() * 150;
        const duration = 800 + Math.random() * 400;
        
        confetti.animate([
            { 
                transform: 'translate(-50%, -50%) scale(0) rotate(0deg)', 
                opacity: 1 
            },
            { 
                transform: `translate(calc(-50% + ${Math.cos(angle) * distance}px), calc(-50% + ${Math.sin(angle) * distance}px)) scale(1) rotate(${Math.random() * 360}deg)`, 
                opacity: 0 
            }
        ], {
            duration: duration,
            easing: 'cubic-bezier(0, 0.5, 0.5, 1)'
        });
        
        setTimeout(() => confetti.remove(), duration);
    }
}

// =====================================================
// MILESTONE MODAL
// =====================================================

function showMilestoneModal(badges) {
    // Create modal
    const modal = document.createElement('div');
    modal.id = 'milestoneModal';
    modal.style.cssText = `
        position: fixed;
        inset: 0;
        background: rgba(0, 0, 0, 0.85);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 10000;
        animation: fadeIn 0.3s ease-out;
    `;
    
    let badgesHtml = badges.map(badge => `
        <div style="display: flex; align-items: center; gap: 15px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 10px;">
            <span style="font-size: 2.5rem;">${getBadgeEmoji(badge.icon)}</span>
            <div>
                <div style="font-weight: 700; color: #fbbf24;">${badge.name}</div>
                <div style="font-size: 0.9rem; color: #a5b4fc;">${badge.description}</div>
            </div>
        </div>
    `).join('');
    
    modal.innerHTML = `
        <div style="background: linear-gradient(135deg, #1e1b4b, #312e81); border-radius: 24px; padding: 40px; max-width: 450px; width: 90%; text-align: center; color: white; position: relative; overflow: hidden;">
            <div id="confettiContainer" style="position: absolute; inset: 0; pointer-events: none; overflow: hidden;"></div>
            
            <div style="font-size: 4rem; margin-bottom: 20px; animation: bounce 0.6s ease-out;">🏆</div>
            
            <h2 style="font-size: 1.8rem; margin-bottom: 10px; color: #fbbf24;">Milestone Achieved!</h2>
            <p style="color: #c7d2fe; margin-bottom: 25px;">You've earned new badges:</p>
            
            <div style="margin-bottom: 25px; text-align: left;">
                ${badgesHtml}
            </div>
            
            <button onclick="closeMilestoneModal()" style="padding: 15px 40px; background: linear-gradient(135deg, #fbbf24, #f59e0b); color: #1e1b4b; border: none; border-radius: 12px; font-size: 1.1rem; font-weight: 700; cursor: pointer;">
                Awesome! 🎉
            </button>
        </div>
    `;
    
    document.body.appendChild(modal);
    
    // Add confetti
    const confettiContainer = document.getElementById('confettiContainer');
    createConfetti(confettiContainer);
    
    // Play sound
    playAchievementSound();
}

function closeMilestoneModal() {
    const modal = document.getElementById('milestoneModal');
    if (modal) {
        modal.style.animation = 'fadeOut 0.2s ease-out';
        setTimeout(() => modal.remove(), 200);
    }
}

function playAchievementSound() {
    if (typeof playSound === 'function') {
        playSound('levelUp');
    }
}

// =====================================================
// ACHIEVEMENT POPUP
// =====================================================

function showAchievementPopup(achievement) {
    // Remove any existing popup
    const existing = document.getElementById('achievementPopup');
    if (existing) existing.remove();
    
    const popup = document.createElement('div');
    popup.id = 'achievementPopup';
    popup.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: linear-gradient(135deg, #1e1b4b, #312e81);
        border-radius: 16px;
        padding: 20px 25px;
        color: white;
        z-index: 9999;
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        animation: slideInRight 0.5s ease-out;
        max-width: 320px;
        overflow: hidden;
    `;
    
    popup.innerHTML = `
        <div id="achievementConfetti" style="position: absolute; inset: 0; pointer-events: none;"></div>
        <div style="display: flex; align-items: center; gap: 15px; position: relative; z-index: 1;">
            <div style="font-size: 3rem; animation: pulse 1s ease-in-out infinite;">${achievement.emoji || '🏆'}</div>
            <div>
                <div style="color: #fbbf24; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">Achievement Unlocked!</div>
                <div style="font-size: 1.2rem; font-weight: 700; margin-top: 5px;">${achievement.name}</div>
                <div style="color: #a5b4fc; font-size: 0.85rem; margin-top: 3px;">${achievement.description}</div>
            </div>
        </div>
    `;
    
    document.body.appendChild(popup);
    
    // Add confetti burst
    const confettiContainer = document.getElementById('achievementConfetti');
    createAchievementConfetti(confettiContainer);
    
    // Play sound
    if (typeof playSound === 'function') {
        playSound('levelUp');
    }
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        popup.style.animation = 'slideOutRight 0.5s ease-in';
        setTimeout(() => popup.remove(), 500);
    }, 5000);
}

// =====================================================
// LEVEL CHANGE TOAST
// =====================================================

function showLevelChangeToast(fromLevel, toLevel) {
    const toast = document.createElement('div');
    toast.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: linear-gradient(135deg, #8b5cf6, #7c3aed);
        color: white;
        padding: 30px 50px;
        border-radius: 20px;
        font-size: 1.5rem;
        font-weight: 700;
        z-index: 10000;
        box-shadow: 0 20px 60px rgba(139, 92, 246, 0.5);
        animation: levelUpPop 0.6s ease-out;
        text-align: center;
    `;
    
    if (toLevel > fromLevel) {
        toast.innerHTML = `
            <div style="font-size: 3rem; margin-bottom: 10px;">🎉</div>
            <div>Level Up!</div>
            <div style="font-size: 2rem; margin-top: 10px;">Level ${toLevel}</div>
        `;
    } else {
        toast.innerHTML = `
            <div style="font-size: 3rem; margin-bottom: 10px;">💪</div>
            <div>Keep Going!</div>
            <div style="font-size: 1rem; margin-top: 10px; opacity: 0.8;">Level ${toLevel}</div>
        `;
    }
    
    document.body.appendChild(toast);
    
    // Play level up sound
    if (typeof playSound === 'function') {
        playSound('levelUp');
    }
    
    setTimeout(() => {
        toast.style.animation = 'fadeOut 0.3s ease-out';
        setTimeout(() => toast.remove(), 300);
    }, 2000);
}

// =====================================================
// HELPER FUNCTIONS
// =====================================================

function getBadgeEmoji(iconClass) {
    const emojiMap = {
        'fa-star': '⭐',
        'fa-fire': '🔥',
        'fa-trophy': '🏆',
        'fa-medal': '🏅',
        'fa-crown': '👑',
        'fa-gem': '💎',
        'fa-bolt': '⚡',
        'fa-rocket': '🚀',
        'fa-brain': '🧠',
        'fa-graduation-cap': '🎓'
    };
    return emojiMap[iconClass] || '🏆';
}

// =====================================================
// ANIMATION STYLES
// =====================================================

// Add animation styles if not already present
if (!document.getElementById('gamificationAnimationStyles')) {
    const style = document.createElement('style');
    style.id = 'gamificationAnimationStyles';
    style.textContent = `
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes fadeOut {
            from { opacity: 1; }
            to { opacity: 0; }
        }
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }
        @keyframes slideInRight {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        @keyframes slideOutRight {
            from { transform: translateX(0); opacity: 1; }
            to { transform: translateX(100%); opacity: 0; }
        }
        @keyframes levelUpPop {
            0% { transform: translate(-50%, -50%) scale(0); opacity: 0; }
            50% { transform: translate(-50%, -50%) scale(1.1); }
            100% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
        }
        @keyframes streakPulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }
        
        .streak-cold { 
            background: rgba(156, 163, 175, 0.3); 
        }
        .streak-warm { 
            background: linear-gradient(135deg, #fbbf24, #f59e0b); 
            animation: streakGlow 1s ease-in-out infinite;
        }
        .streak-hot { 
            background: linear-gradient(135deg, #f97316, #ea580c); 
            animation: streakGlow 0.8s ease-in-out infinite;
        }
        .streak-blazing { 
            background: linear-gradient(135deg, #ef4444, #dc2626); 
            animation: streakGlow 0.5s ease-in-out infinite;
        }
        
        @keyframes streakGlow {
            0%, 100% { box-shadow: 0 0 10px rgba(251, 191, 36, 0.5); }
            50% { box-shadow: 0 0 20px rgba(251, 191, 36, 0.8); }
        }
    `;
    document.head.appendChild(style);
}

// =====================================================
// END GAMIFICATION MODULE
// =====================================================

console.log('🎮 Gamification module loaded');
