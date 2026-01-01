/**
 * AgentMath Combined Modules
 * Rev 3.1.3 - 2025-12-13
 * 
 * This single file contains:
 * - Sound Effects System
 * - Clock Challenge System  
 * - Day 1 Features (Online Counter, Hot Streak)
 * - Day 2 Features (Quick Play, Smart Quiz, Leaderboard)
 * - Milestone/Confetti/Achievement System
 * - Tutorial Data
 * - Adaptive Help Content
 * 
 * Combined to minimize HTTP requests for better performance
 */


// =====================================================
// SOUND EFFECTS SYSTEM  
// =====================================================

let soundEnabled = localStorage.getItem('agentmath_sound') !== 'false';

const soundEffects = {
    correct: null,
    incorrect: null,
    streak3: null,
    streak5: null,
    streak10: null,
    levelUp: null
};

let audioContext = null;

function initSoundSystem() {
    try {
        audioContext = new (window.AudioContext || window.webkitAudioContext)();
        console.log('🔊 Sound system initialized');
    } catch (e) {
        console.log('⚠️ Web Audio API not supported');
    }
    updateSoundToggleUI();
}

function playSound(type) {
    if (!soundEnabled || !audioContext) return;
    
    try {
        const oscillator = audioContext.createOscillator();
        const gainNode = audioContext.createGain();
        
        oscillator.connect(gainNode);
        gainNode.connect(audioContext.destination);
        
        switch(type) {
            case 'correct':
                oscillator.frequency.setValueAtTime(523.25, audioContext.currentTime);
                oscillator.frequency.setValueAtTime(659.25, audioContext.currentTime + 0.1);
                gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.3);
                oscillator.start(audioContext.currentTime);
                oscillator.stop(audioContext.currentTime + 0.3);
                break;
                
            case 'incorrect':
                oscillator.frequency.setValueAtTime(200, audioContext.currentTime);
                oscillator.frequency.setValueAtTime(150, audioContext.currentTime + 0.1);
                oscillator.type = 'sawtooth';
                gainNode.gain.setValueAtTime(0.2, audioContext.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.3);
                oscillator.start(audioContext.currentTime);
                oscillator.stop(audioContext.currentTime + 0.3);
                break;
                
            case 'streak3':
                playArpeggio([523.25, 659.25, 783.99], 0.1, 0.3);
                break;
                
            case 'streak5':
                playArpeggio([523.25, 659.25, 783.99, 1046.50], 0.08, 0.4);
                break;
                
            case 'streak10':
                playArpeggio([523.25, 659.25, 783.99, 1046.50, 1318.51], 0.06, 0.5);
                break;
                
            case 'levelUp':
                playArpeggio([261.63, 329.63, 392.00, 523.25, 659.25, 783.99], 0.1, 0.8);
                break;
        }
    } catch (e) {
        console.log('Sound play error:', e);
    }
}

function playArpeggio(frequencies, noteLength, totalDuration) {
    if (!audioContext) return;
    
    frequencies.forEach((freq, index) => {
        const osc = audioContext.createOscillator();
        const gain = audioContext.createGain();
        osc.connect(gain);
        gain.connect(audioContext.destination);
        
        osc.frequency.value = freq;
        osc.type = 'sine';
        
        const startTime = audioContext.currentTime + (index * noteLength);
        gain.gain.setValueAtTime(0.2, startTime);
        gain.gain.exponentialRampToValueAtTime(0.01, startTime + noteLength * 1.5);
        
        osc.start(startTime);
        osc.stop(startTime + noteLength * 2);
    });
}

function toggleSoundEffects() {
    soundEnabled = !soundEnabled;
    localStorage.setItem('agentmath_sound', soundEnabled);
    updateSoundToggleUI();
    
    if (soundEnabled) {
        if (audioContext && audioContext.state === 'suspended') {
            audioContext.resume();
        }
        playSound('correct');
    }
}

function updateSoundToggleUI() {
    const btn1 = document.getElementById('soundToggleBtn');
    const btn2 = document.getElementById('soundToggleBtnQuiz');
    const icon1 = document.getElementById('soundIcon');
    const icon2 = document.getElementById('soundIconQuiz');
    
    [btn1, btn2].forEach(btn => {
        if (btn) {
            if (soundEnabled) {
                btn.classList.remove('muted');
            } else {
                btn.classList.add('muted');
            }
        }
    });
    
    [icon1, icon2].forEach(icon => {
        if (icon) {
            icon.className = soundEnabled ? 'fas fa-volume-up' : 'fas fa-volume-mute';
        }
    });
}

console.log('🔊 Sound effects loaded');



/**
 * AgentMath Clock Challenge Module
 * Beat the Clock timed challenge for Levels 6-10
 * Extracted from student_app.html Rev 3.1.0
 * 
 * Dependencies: Requires adaptiveState and continueAdaptiveQuizBeta from main page
 */


// =====================================================
// CLOCK CHALLENGE (Beat the Clock) - Rev 3.0
// =====================================================

const CLOCK_CONFIG = {
    // Time allowed per level (seconds)
    timeAllowed: {
        6: 120,   // 2 minutes
        7: 150,   // 2.5 minutes
        8: 180,   // 3 minutes
        9: 210,   // 3.5 minutes
        10: 240   // 4 minutes
    },
    // Wrong answer penalty (seconds)
    wrongPenalty: {
        6: 10,
        7: 10,
        8: 15,
        9: 15,
        10: 20
    },
    // Bonus tiers
    bonusTiers: {
        lightning: { minPercent: 40, points: 50, emoji: '⚡', name: 'Lightning Fast' },
        fast: { minPercent: 20, points: 35, emoji: '🔥', name: 'Speed Demon' },
        on_time: { minPercent: 1, points: 20, emoji: '✅', name: 'Beat the Clock' }
    },
    // Lifelines (pre-purchase) - Rev 3.0.9
    lifelines: {
        timeBoost: { 
            id: 'timeBoost',
            name: 'Time Boost', 
            emoji: '⏰', 
            description: '+30 seconds starting time',
            cost: { 6: 30, 7: 35, 8: 40, 9: 45, 10: 50 },
            effect: 'extraTime',
            value: 30
        },
        timeShield: { 
            id: 'timeShield',
            name: 'Time Shield', 
            emoji: '🛡️', 
            description: 'Wrong answers cost half time',
            cost: { 6: 25, 7: 30, 8: 35, 9: 40, 10: 45 },
            effect: 'halfPenalty',
            value: 0.5
        },
        secondChance: { 
            id: 'secondChance',
            name: 'Second Chance', 
            emoji: '🎯', 
            description: 'First wrong answer is free',
            cost: { 6: 20, 7: 25, 8: 30, 9: 35, 10: 40 },
            effect: 'freeWrong',
            value: 1
        }
    },
    // Emergency buy (during challenge) - Rev 3.0.9
    emergencyBuy: {
        triggerAt: 30,  // Show when time drops below 30 seconds
        extraTime: 30,  // Buy 30 seconds
        cost: { 6: 40, 7: 50, 8: 60, 9: 70, 10: 80 }
    }
};

// Check if user has seen clock intro
async function checkAndShowClockIntro() {
    try {
        const response = await fetch('/api/clock-challenge/intro-seen');
        const data = await response.json();
        if (!data.seen) {
            showClockIntroModal();
        }
    } catch (error) {
        console.log('Could not check clock intro status:', error);
    }
}

// Clock intro modal (shown once at Level 6)
function showClockIntroModal() {
    const modal = document.createElement('div');
    modal.id = 'clockIntroModal';
    modal.innerHTML = `
        <div style="position: fixed; inset: 0; background: rgba(0,0,0,0.7); z-index: 10000; display: flex; align-items: flex-start; justify-content: center; padding: 20px; overflow-y: auto; -webkit-overflow-scrolling: touch;">
            <div style="background: linear-gradient(135deg, #1e1b4b, #312e81); border-radius: 20px; padding: 25px; max-width: 480px; width: 100%; color: white; text-align: center; box-shadow: 0 25px 50px rgba(0,0,0,0.5); animation: clockModalPop 0.4s ease-out; margin: auto 0;">
                
                <div style="font-size: 4rem; margin-bottom: 15px; animation: clockPulse 1.5s ease-in-out infinite;">⏱️</div>
                
                <h2 style="font-size: 1.8rem; margin-bottom: 10px; background: linear-gradient(90deg, #fbbf24, #f59e0b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800;">
                    CLOCK CHALLENGE UNLOCKED!
                </h2>
                
                <p style="color: #c7d2fe; margin-bottom: 20px; font-size: 1.1rem;">
                    Congratulations on reaching Level 6!
                </p>
                
                <div style="background: rgba(255,255,255,0.1); border-radius: 12px; padding: 20px; margin-bottom: 20px; text-align: left;">
                    <h3 style="color: #fbbf24; font-size: 1rem; margin-bottom: 12px; text-align: center;">HOW IT WORKS</h3>
                    
                    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
                        <span style="font-size: 1.5rem;">⏱️</span>
                        <span style="color: #e0e7ff;">Complete the level before time runs out</span>
                    </div>
                    
                    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
                        <span style="font-size: 1.5rem;">✅</span>
                        <span style="color: #e0e7ff;">Correct answers earn points as normal</span>
                    </div>
                    
                    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
                        <span style="font-size: 1.5rem;">❌</span>
                        <span style="color: #e0e7ff;">Wrong answers cost you time!</span>
                    </div>
                    
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <span style="font-size: 1.5rem;">🏆</span>
                        <span style="color: #e0e7ff;">Finish on time = <strong style="color: #fbbf24;">BONUS POINTS!</strong></span>
                    </div>
                </div>
                
                <div style="background: rgba(0,0,0,0.2); border-radius: 10px; padding: 15px; margin-bottom: 25px; font-size: 0.9rem; color: #a5b4fc;">
                    <strong>If time runs out:</strong><br>
                    You keep all points earned and continue in normal mode.<br>
                    Clock mode unlocks again after you complete the level!
                </div>
                
                <label style="display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 20px; cursor: pointer; color: #a5b4fc; font-size: 0.9rem;">
                    <input type="checkbox" id="clockIntroDontShow" style="width: 18px; height: 18px; cursor: pointer;">
                    Don't show this again
                </label>
                
                <button onclick="closeClockIntroModal()" style="padding: 15px 40px; background: linear-gradient(135deg, #fbbf24, #f59e0b); color: #1e1b4b; border: none; border-radius: 12px; font-size: 1.1rem; font-weight: 700; cursor: pointer; transition: transform 0.2s, box-shadow 0.2s;">
                    👍 Got it!
                </button>
            </div>
        </div>
    `;
    document.body.appendChild(modal);
}

async function closeClockIntroModal() {
    console.log('🕐 closeClockIntroModal called');
    const dontShow = document.getElementById('clockIntroDontShow')?.checked;
    if (dontShow) {
        try {
            await fetch('/api/clock-challenge/intro-seen', { method: 'POST' });
        } catch (error) {
            console.log('Could not save intro preference:', error);
        }
    }
    const modal = document.getElementById('clockIntroModal');
    if (modal) {
        modal.style.opacity = '0';
        modal.style.transition = 'opacity 0.3s';
        setTimeout(async () => {
            modal.remove();
            console.log('🕐 Intro modal removed, now calling showClockOptInModal');
            console.log('🕐 adaptiveState.currentLevel:', adaptiveState.currentLevel);
            // Directly show opt-in modal after intro closes (Rev 3.0.3 fix)
            // This provides a clear flow: Intro → Opt-in → Accept/Decline
            const result = await showClockOptInModal(adaptiveState.currentLevel);
            console.log('🕐 showClockOptInModal returned:', result);
            
            // Hide the feedback panel since we're handling the flow here
            document.getElementById('adaptiveFeedbackBeta')?.classList.add('hidden');
            
            if (result.start) {
                console.log('🕐 User accepted, starting clock challenge with lifelines:', result.lifelines);
                // Start clock challenge with selected lifelines
                await startClockChallenge(adaptiveState.currentLevel, result.lifelines, result.cost);
            } else {
                console.log('🕐 User declined or not available, continuing normal mode');
            }
            // Continue to next question (whether accepted or declined)
            continueAdaptiveQuizBeta();
        }, 300);
    }
}

// Clock opt-in modal (shown each time reaching L6-10) - Updated Rev 3.0.9 with lifelines
async function showClockOptInModal(level) {
    console.log('🕐 showClockOptInModal called with level:', level, 'topic:', adaptiveState.topic);
    try {
        const url = `/api/clock-challenge/check?topic=${adaptiveState.topic}&level=${level}`;
        console.log('🕐 Fetching:', url);
        const response = await fetch(url);
        console.log('🕐 Response status:', response.status);
        const data = await response.json();
        console.log('🕐 API Response:', JSON.stringify(data));
        
        if (!data.available) {
            console.log('🕐 Clock NOT available, reason:', data.reason || data.error || 'unknown');
            return { start: false };
        }
        
        console.log('🕐 Clock IS available, showing opt-in modal');
        const timeAllowed = data.config?.time_allowed || CLOCK_CONFIG.timeAllowed[level];
        const wrongPenalty = data.config?.wrong_penalty || CLOCK_CONFIG.wrongPenalty[level];
        const minutes = Math.floor(timeAllowed / 60);
        const seconds = timeAllowed % 60;
        const timeStr = seconds > 0 ? `${minutes}:${seconds.toString().padStart(2, '0')}` : `${minutes} minute${minutes > 1 ? 's' : ''}`;
        
        const bestTimeStr = data.best_time_remaining ? 
            `Personal best: ${Math.floor(data.best_time_remaining / 60)}:${(data.best_time_remaining % 60).toString().padStart(2, '0')} remaining` : 
            '🌟 First attempt!';
        
        // Get user's current points
        const userPoints = adaptiveState.sessionPointsEarned || 0;
        
        // Build lifeline options HTML
        const lifelines = CLOCK_CONFIG.lifelines;
        let lifelinesHtml = '';
        for (const [key, lifeline] of Object.entries(lifelines)) {
            const cost = lifeline.cost[level];
            const canAfford = userPoints >= cost;
            const opacity = canAfford ? '1' : '0.5';
            const cursor = canAfford ? 'pointer' : 'not-allowed';
            lifelinesHtml += `
                <label style="display: flex; align-items: center; gap: 10px; padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px; cursor: ${cursor}; opacity: ${opacity}; transition: all 0.2s;" 
                       onmouseover="this.style.background='rgba(255,255,255,0.1)'" 
                       onmouseout="this.style.background='rgba(255,255,255,0.05)'">
                    <input type="checkbox" id="lifeline_${key}" class="lifeline-checkbox" data-lifeline="${key}" data-cost="${cost}" ${canAfford ? '' : 'disabled'} style="width: 18px; height: 18px; accent-color: #fbbf24;">
                    <span style="font-size: 1.3rem;">${lifeline.emoji}</span>
                    <div style="flex: 1; text-align: left;">
                        <div style="font-weight: 600; color: #e0e7ff; font-size: 0.9rem;">${lifeline.name}</div>
                        <div style="color: #a5b4fc; font-size: 0.75rem;">${lifeline.description}</div>
                    </div>
                    <div style="color: #fbbf24; font-weight: 600; font-size: 0.85rem;">💰 ${cost}</div>
                </label>
            `;
        }
        
        return new Promise((resolve) => {
            const modal = document.createElement('div');
            modal.id = 'clockOptInModal';
            modal.innerHTML = `
                <div style="position: fixed; inset: 0; background: rgba(0,0,0,0.8); z-index: 10000; display: flex; align-items: flex-start; justify-content: center; padding: 20px; overflow-y: auto; -webkit-overflow-scrolling: touch;">
                    <div style="background: linear-gradient(135deg, #1e1b4b, #312e81); border-radius: 20px; padding: 25px; max-width: 450px; width: 100%; color: white; text-align: center; box-shadow: 0 25px 50px rgba(0,0,0,0.5); animation: clockModalPop 0.3s ease-out; margin: auto 0;">
                        
                        <div style="font-size: 3rem; margin-bottom: 10px; animation: clockPulse 1s ease-in-out infinite;">⏱️</div>
                        
                        <h2 style="font-size: 1.5rem; margin-bottom: 5px; color: #fbbf24; font-weight: 700;">
                            CLOCK CHALLENGE
                        </h2>
                        
                        <div style="color: #a5b4fc; font-size: 1.2rem; margin-bottom: 15px;">
                            Level ${level}
                        </div>
                        
                        <div style="background: rgba(255,255,255,0.1); border-radius: 12px; padding: 15px; margin-bottom: 15px;">
                            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: center;">
                                <div>
                                    <div style="font-size: 1.5rem;">⏱️</div>
                                    <div style="color: #fbbf24; font-weight: 600;">${timeStr}</div>
                                    <div style="color: #a5b4fc; font-size: 0.75rem;">Time</div>
                                </div>
                                <div>
                                    <div style="font-size: 1.5rem;">❌</div>
                                    <div style="color: #f87171; font-weight: 600;">-${wrongPenalty}s</div>
                                    <div style="color: #a5b4fc; font-size: 0.75rem;">Wrong Penalty</div>
                                </div>
                                <div>
                                    <div style="font-size: 1.5rem;">🏆</div>
                                    <div style="color: #4ade80; font-weight: 600;">Up to +50</div>
                                    <div style="color: #a5b4fc; font-size: 0.75rem;">Bonus Points</div>
                                </div>
                            </div>
                        </div>
                        
                        <div style="color: #818cf8; font-size: 0.85rem; margin-bottom: 15px;">
                            ${bestTimeStr}
                        </div>
                        
                        <!-- Lifelines Section -->
                        <div style="background: rgba(0,0,0,0.2); border-radius: 12px; padding: 15px; margin-bottom: 20px; text-align: left;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                                <div style="color: #fbbf24; font-weight: 700; font-size: 0.9rem;">⚡ POWER-UPS (Optional)</div>
                                <div style="color: #a5b4fc; font-size: 0.8rem;">Your points: 💰 <span id="lifelineUserPoints">${userPoints}</span></div>
                            </div>
                            <div style="display: flex; flex-direction: column; gap: 8px;">
                                ${lifelinesHtml}
                            </div>
                            <div style="margin-top: 10px; text-align: center; color: #818cf8; font-size: 0.8rem;">
                                Total cost: 💰 <span id="lifelineTotalCost">0</span> points
                            </div>
                        </div>
                        
                        <div style="display: flex; flex-direction: column; gap: 12px;">
                            <button id="clockStartBtn" style="padding: 15px 30px; background: linear-gradient(135deg, #fbbf24, #f59e0b); color: #1e1b4b; border: none; border-radius: 12px; font-size: 1.1rem; font-weight: 700; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px;">
                                ⏱️ Start Clock Challenge
                            </button>
                            
                            <button id="clockSkipBtn" style="padding: 12px 25px; background: rgba(255,255,255,0.1); color: #a5b4fc; border: 2px solid rgba(255,255,255,0.2); border-radius: 10px; font-size: 1rem; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px;">
                                📚 Normal Mode
                            </button>
                        </div>
                    </div>
                </div>
            `;
            document.body.appendChild(modal);
            
            // Update total cost when checkboxes change
            const checkboxes = modal.querySelectorAll('.lifeline-checkbox');
            const totalCostEl = document.getElementById('lifelineTotalCost');
            checkboxes.forEach(cb => {
                cb.addEventListener('change', () => {
                    let total = 0;
                    checkboxes.forEach(c => {
                        if (c.checked) total += parseInt(c.dataset.cost);
                    });
                    totalCostEl.textContent = total;
                });
            });
            
            document.getElementById('clockStartBtn').onclick = () => {
                // Collect selected lifelines
                const selectedLifelines = { timeBoost: false, timeShield: false, secondChance: false };
                let totalCost = 0;
                checkboxes.forEach(cb => {
                    if (cb.checked) {
                        selectedLifelines[cb.dataset.lifeline] = true;
                        totalCost += parseInt(cb.dataset.cost);
                    }
                });
                
                // Check if user can afford
                if (totalCost > userPoints) {
                    alert('Not enough points for selected power-ups!');
                    return;
                }
                
                modal.remove();
                resolve({ start: true, lifelines: selectedLifelines, cost: totalCost });
            };
            
            document.getElementById('clockSkipBtn').onclick = () => {
                modal.remove();
                resolve({ start: false });
            };
        });
        
    } catch (error) {
        console.error('🕐 ERROR in showClockOptInModal:', error);
        console.error('🕐 Error stack:', error.stack);
        return { start: false };
    }
}

// Start clock challenge - Updated Rev 3.0.9 with lifelines
async function startClockChallenge(level, lifelines = {}, lifelineCost = 0) {
    try {
        const response = await fetch('/api/clock-challenge/start', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                topic: adaptiveState.topic,
                level: level
            })
        });
        
        const data = await response.json();
        if (!data.success) {
            console.error('Failed to start clock challenge:', data.error);
            return false;
        }
        
        // Calculate time with Time Boost lifeline
        let timeAllowed = data.time_allowed;
        if (lifelines.timeBoost) {
            const boost = CLOCK_CONFIG.lifelines.timeBoost.value;
            timeAllowed += boost;
            console.log(`⏰ Time Boost applied: +${boost}s`);
        }
        
        // Calculate penalty with Time Shield lifeline
        let wrongPenalty = data.wrong_penalty;
        if (lifelines.timeShield) {
            wrongPenalty = Math.floor(wrongPenalty * CLOCK_CONFIG.lifelines.timeShield.value);
            console.log(`🛡️ Time Shield applied: penalty reduced to ${wrongPenalty}s`);
        }
        
        // Deduct lifeline cost from session points
        if (lifelineCost > 0) {
            adaptiveState.sessionPointsEarned -= lifelineCost;
            document.getElementById('adaptiveSessionPoints').textContent = adaptiveState.sessionPointsEarned;
            console.log(`💰 Lifeline cost deducted: ${lifelineCost} points`);
        }
        
        // Initialize clock state
        adaptiveState.clockMode = true;
        adaptiveState.clockSessionId = data.session_id;
        adaptiveState.clockTimeRemaining = timeAllowed;
        adaptiveState.clockTimeAllowed = timeAllowed;
        adaptiveState.clockWrongPenalty = wrongPenalty;
        adaptiveState.clockPenaltiesApplied = 0;
        adaptiveState.clockQuestionsAnswered = 0;
        adaptiveState.clockQuestionsCorrect = 0;
        adaptiveState.clockLevelStartPoints = adaptiveState.currentPoints;
        
        // Store active lifelines (Rev 3.0.9)
        adaptiveState.clockLifelines = {
            timeBoost: lifelines.timeBoost || false,
            timeShield: lifelines.timeShield || false,
            secondChance: lifelines.secondChance || false
        };
        adaptiveState.clockSecondChanceUsed = false;
        adaptiveState.clockEmergencyBuyUsed = false;
        adaptiveState.clockEmergencyBuyShown = false;
        
        showClockTimerUI();
        startClockTimer();
        
        // Log active lifelines
        const activeLifelines = Object.entries(adaptiveState.clockLifelines)
            .filter(([k, v]) => v)
            .map(([k]) => k);
        console.log(`⏱️ Clock challenge started! ${timeAllowed}s, -${wrongPenalty}s penalty`);
        if (activeLifelines.length > 0) {
            console.log(`⚡ Active lifelines: ${activeLifelines.join(', ')}`);
        }
        return true;
        
    } catch (error) {
        console.error('Error starting clock challenge:', error);
        return false;
    }
}

// Clock timer UI - Updated Rev 3.0.9 with lifeline indicators
function showClockTimerUI() {
    console.log('⏱️ showClockTimerUI called');
    let timerBar = document.getElementById('clockTimerBar');
    if (!timerBar) {
        console.log('⏱️ Creating new timer bar');
        timerBar = document.createElement('div');
        timerBar.id = 'clockTimerBar';
        
        // Build lifeline indicators
        let lifelineHtml = '';
        if (adaptiveState.clockLifelines.timeBoost) {
            lifelineHtml += '<span title="Time Boost Active" style="font-size: 1rem;">⏰</span>';
        }
        if (adaptiveState.clockLifelines.timeShield) {
            lifelineHtml += '<span title="Time Shield Active" style="font-size: 1rem;">🛡️</span>';
        }
        if (adaptiveState.clockLifelines.secondChance && !adaptiveState.clockSecondChanceUsed) {
            lifelineHtml += '<span id="secondChanceIndicator" title="Second Chance Ready" style="font-size: 1rem;">🎯</span>';
        }
        
        timerBar.innerHTML = `
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.5rem;" id="clockEmoji">⏱️</span>
                    <span style="font-weight: 700; font-size: 1.3rem;" id="clockTimeDisplay">0:00</span>
                </div>
                <div style="display: flex; align-items: center; gap: 8px;">
                    <div id="clockLifelineIndicators" style="display: flex; gap: 5px;">${lifelineHtml}</div>
                    <span style="font-size: 0.85rem; color: #fbbf24; font-weight: 600;">⚡ CLOCK MODE</span>
                </div>
            </div>
            <div style="height: 8px; background: rgba(255,255,255,0.2); border-radius: 4px; overflow: hidden;">
                <div id="clockProgressBar" style="height: 100%; background: linear-gradient(90deg, #22c55e, #4ade80); width: 100%; transition: width 0.3s, background 0.3s; border-radius: 4px;"></div>
            </div>
        `;
        timerBar.style.cssText = 'background: linear-gradient(135deg, #1e1b4b, #312e81); padding: 15px 20px; border-radius: 12px; margin-bottom: 20px; color: white;';
        
        // Try multiple insertion points for different quiz interfaces
        // 1. BETA interface: Insert before the question content area
        const questionTopBar = document.getElementById('adaptiveQuestionTopBar');
        if (questionTopBar) {
            questionTopBar.parentNode.insertBefore(timerBar, questionTopBar);
            console.log('⏱️ Timer bar inserted before question top bar (BETA interface)');
        } else {
            // 2. Old interface: Insert after level banner
            const levelBanner = document.getElementById('adaptiveLevelBanner');
            if (levelBanner) {
                levelBanner.parentNode.insertBefore(timerBar, levelBanner.nextSibling);
                console.log('⏱️ Timer bar inserted after level banner (old interface)');
            } else {
                // 3. Fallback: Insert at start of adaptive-question-area
                const questionArea = document.querySelector('.adaptive-question-area');
                if (questionArea) {
                    questionArea.insertBefore(timerBar, questionArea.firstChild);
                    console.log('⏱️ Timer bar inserted at start of question area (fallback)');
                } else {
                    console.error('⏱️ Could not find insertion point for timer bar!');
                }
            }
        }
    }
    timerBar.style.display = 'block';
    console.log('⏱️ Timer bar display set to block');
    updateClockDisplay();
}

function hideClockTimerUI() {
    const timerBar = document.getElementById('clockTimerBar');
    if (timerBar) timerBar.style.display = 'none';
}

function updateClockDisplay() {
    const timeDisplay = document.getElementById('clockTimeDisplay');
    const progressBar = document.getElementById('clockProgressBar');
    const clockEmoji = document.getElementById('clockEmoji');
    const timerBar = document.getElementById('clockTimerBar');
    
    if (!timeDisplay || !progressBar) return;
    
    const time = adaptiveState.clockTimeRemaining;
    const total = adaptiveState.clockTimeAllowed;
    const minutes = Math.floor(time / 60);
    const seconds = time % 60;
    const percent = (time / total) * 100;
    
    timeDisplay.textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
    progressBar.style.width = `${percent}%`;
    
    // Color progression
    if (percent > 50) {
        progressBar.style.background = 'linear-gradient(90deg, #22c55e, #4ade80)';
        clockEmoji.textContent = '⏱️';
        clockEmoji.style.animation = '';
    } else if (percent > 20) {
        progressBar.style.background = 'linear-gradient(90deg, #eab308, #fbbf24)';
        clockEmoji.textContent = '⏱️';
    } else if (percent > 10) {
        progressBar.style.background = 'linear-gradient(90deg, #f97316, #fb923c)';
        clockEmoji.textContent = '⚠️';
    } else {
        progressBar.style.background = 'linear-gradient(90deg, #ef4444, #f87171)';
        clockEmoji.textContent = '🚨';
        clockEmoji.style.animation = 'clockPulse 0.5s ease-in-out infinite';
    }
    
    // Flash when very low
    if (timerBar) {
        timerBar.style.animation = (time <= 10 && time > 0) ? 'clockFlash 0.5s ease-in-out infinite' : '';
    }
}

function startClockTimer() {
    if (adaptiveState.clockTimerInterval) {
        clearInterval(adaptiveState.clockTimerInterval);
    }
    
    adaptiveState.clockTimerInterval = setInterval(() => {
        if (adaptiveState.clockTimeRemaining > 0) {
            adaptiveState.clockTimeRemaining--;
            updateClockDisplay();
            
            // Check for Emergency Buy trigger (Rev 3.0.9)
            const triggerAt = CLOCK_CONFIG.emergencyBuy.triggerAt;
            if (adaptiveState.clockTimeRemaining === triggerAt && 
                !adaptiveState.clockEmergencyBuyUsed && 
                !adaptiveState.clockEmergencyBuyShown) {
                showEmergencyBuyModal();
            }
            
            if (adaptiveState.clockTimeRemaining <= 0) {
                clockTimeout();
            }
        }
    }, 1000);
}

function stopClockTimer() {
    if (adaptiveState.clockTimerInterval) {
        clearInterval(adaptiveState.clockTimerInterval);
        adaptiveState.clockTimerInterval = null;
    }
}

// Emergency Buy Modal (Rev 3.0.9)
function showEmergencyBuyModal() {
    adaptiveState.clockEmergencyBuyShown = true;
    
    const level = adaptiveState.currentLevel;
    const cost = CLOCK_CONFIG.emergencyBuy.cost[level];
    const extraTime = CLOCK_CONFIG.emergencyBuy.extraTime;
    const userPoints = adaptiveState.sessionPointsEarned || 0;
    const canAfford = userPoints >= cost;
    
    // Pause the timer while modal is shown
    stopClockTimer();
    
    const modal = document.createElement('div');
    modal.id = 'emergencyBuyModal';
    modal.innerHTML = `
        <div style="position: fixed; inset: 0; background: rgba(0,0,0,0.85); z-index: 10002; display: flex; align-items: center; justify-content: center; padding: 20px;">
            <div style="background: linear-gradient(135deg, #7f1d1d, #991b1b); border-radius: 20px; padding: 30px; max-width: 380px; width: 100%; color: white; text-align: center; box-shadow: 0 25px 50px rgba(0,0,0,0.5); animation: clockModalPop 0.3s ease-out;">
                
                <div style="font-size: 4rem; margin-bottom: 15px; animation: clockPulse 0.5s ease-in-out infinite;">⚠️</div>
                
                <h2 style="font-size: 1.6rem; margin-bottom: 10px; color: #fecaca; font-weight: 700;">
                    RUNNING LOW ON TIME!
                </h2>
                
                <p style="color: #fca5a5; font-size: 1.1rem; margin-bottom: 20px;">
                    Only <strong style="color: #fbbf24;">${adaptiveState.clockTimeRemaining}</strong> seconds left!
                </p>
                
                <div style="background: rgba(0,0,0,0.3); border-radius: 12px; padding: 20px; margin-bottom: 20px;">
                    <div style="font-size: 1.3rem; color: #fbbf24; font-weight: 700; margin-bottom: 10px;">
                        💰 Buy +${extraTime} seconds?
                    </div>
                    <div style="font-size: 2rem; font-weight: 800; color: white;">
                        ${cost} points
                    </div>
                    <div style="color: #fca5a5; font-size: 0.9rem; margin-top: 8px;">
                        Your points: ${userPoints}
                    </div>
                </div>
                
                <div style="display: flex; flex-direction: column; gap: 12px;">
                    <button id="emergencyBuyBtn" ${canAfford ? '' : 'disabled'} style="padding: 15px 30px; background: ${canAfford ? 'linear-gradient(135deg, #fbbf24, #f59e0b)' : '#6b7280'}; color: ${canAfford ? '#1e1b4b' : '#9ca3af'}; border: none; border-radius: 12px; font-size: 1.1rem; font-weight: 700; cursor: ${canAfford ? 'pointer' : 'not-allowed'}; display: flex; align-items: center; justify-content: center; gap: 8px;">
                        ${canAfford ? `⏰ Buy +${extraTime} Seconds` : '❌ Not Enough Points'}
                    </button>
                    
                    <button id="emergencySkipBtn" style="padding: 12px 25px; background: rgba(255,255,255,0.1); color: #fecaca; border: 2px solid rgba(255,255,255,0.2); border-radius: 10px; font-size: 1rem; cursor: pointer;">
                        Keep Going
                    </button>
                </div>
            </div>
        </div>
    `;
    document.body.appendChild(modal);
    
    document.getElementById('emergencyBuyBtn').onclick = () => {
        if (canAfford) {
            // Deduct points
            adaptiveState.sessionPointsEarned -= cost;
            document.getElementById('adaptiveSessionPoints').textContent = adaptiveState.sessionPointsEarned;
            
            // Add time
            adaptiveState.clockTimeRemaining += extraTime;
            adaptiveState.clockEmergencyBuyUsed = true;
            
            console.log(`💰 Emergency Buy: +${extraTime}s for ${cost} points`);
            
            // Show confirmation toast
            const toast = document.createElement('div');
            toast.style.cssText = `
                position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
                background: linear-gradient(135deg, #22c55e, #16a34a); color: white;
                padding: 15px 30px; border-radius: 12px; font-size: 1.3rem; font-weight: 700;
                z-index: 10003; animation: penaltyPop 0.8s ease-out forwards;
                box-shadow: 0 10px 30px rgba(34,197,94,0.5);
            `;
            toast.textContent = `+${extraTime} seconds!`;
            document.body.appendChild(toast);
            setTimeout(() => toast.remove(), 800);
            
            updateClockDisplay();
        }
        modal.remove();
        startClockTimer(); // Resume timer
    };
    
    document.getElementById('emergencySkipBtn').onclick = () => {
        modal.remove();
        startClockTimer(); // Resume timer
    };
}

function applyClockPenalty() {
    if (!adaptiveState.clockMode) return;
    
    // Check for Second Chance lifeline (Rev 3.0.9)
    if (adaptiveState.clockLifelines.secondChance && !adaptiveState.clockSecondChanceUsed) {
        adaptiveState.clockSecondChanceUsed = true;
        console.log('🎯 Second Chance used! No penalty this time.');
        
        // Update indicator to show it's used
        const indicator = document.getElementById('secondChanceIndicator');
        if (indicator) {
            indicator.style.opacity = '0.3';
            indicator.title = 'Second Chance Used';
        }
        
        // Show "Second Chance" toast
        const toast = document.createElement('div');
        toast.style.cssText = `
            position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
            background: linear-gradient(135deg, #8b5cf6, #7c3aed); color: white;
            padding: 15px 30px; border-radius: 12px; font-size: 1.3rem; font-weight: 700;
            z-index: 10001; animation: penaltyPop 0.6s ease-out forwards;
            box-shadow: 0 10px 30px rgba(139,92,246,0.5);
        `;
        toast.innerHTML = '🎯 Second Chance!<br><span style="font-size: 0.9rem; opacity: 0.9;">No penalty!</span>';
        document.body.appendChild(toast);
        setTimeout(() => toast.remove(), 1000);
        return; // No penalty applied
    }
    
    const penalty = adaptiveState.clockWrongPenalty;
    adaptiveState.clockTimeRemaining = Math.max(0, adaptiveState.clockTimeRemaining - penalty);
    adaptiveState.clockPenaltiesApplied += penalty;
    
    // Visual penalty feedback
    const timerBar = document.getElementById('clockTimerBar');
    if (timerBar) {
        timerBar.style.background = 'linear-gradient(135deg, #7f1d1d, #991b1b)';
        setTimeout(() => {
            timerBar.style.background = 'linear-gradient(135deg, #1e1b4b, #312e81)';
        }, 300);
    }
    
    // Show penalty toast
    const toast = document.createElement('div');
    toast.style.cssText = `
        position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
        background: linear-gradient(135deg, #dc2626, #b91c1c); color: white;
        padding: 15px 30px; border-radius: 12px; font-size: 1.3rem; font-weight: 700;
        z-index: 10001; animation: penaltyPop 0.6s ease-out forwards;
        box-shadow: 0 10px 30px rgba(220,38,38,0.5);
    `;
    toast.textContent = `-${penalty} seconds!`;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 600);
    
    updateClockDisplay();
    
    if (adaptiveState.clockTimeRemaining <= 0) {
        clockTimeout();
    }
}

// Clock timeout
function clockTimeout() {
    stopClockTimer();
    completeClockChallenge(false);
    
    const modal = document.createElement('div');
    modal.id = 'clockTimeoutModal';
    modal.innerHTML = `
        <div style="position: fixed; inset: 0; background: rgba(0,0,0,0.8); z-index: 10000; display: flex; align-items: flex-start; justify-content: center; padding: 20px; overflow-y: auto; -webkit-overflow-scrolling: touch;">
            <div style="background: linear-gradient(135deg, #7f1d1d, #991b1b); border-radius: 20px; padding: 25px; max-width: 400px; width: 100%; color: white; text-align: center; box-shadow: 0 25px 50px rgba(0,0,0,0.5); animation: clockModalPop 0.3s ease-out; margin: auto 0;">
                
                <div style="font-size: 4rem; margin-bottom: 15px;">⏰</div>
                
                <h2 style="font-size: 1.8rem; margin-bottom: 15px; font-weight: 700;">TIME'S UP!</h2>
                
                <p style="color: #fecaca; font-size: 1.1rem; margin-bottom: 10px;">
                    You answered <strong>${adaptiveState.clockQuestionsCorrect}</strong> of <strong>${adaptiveState.clockQuestionsAnswered}</strong> correctly
                </p>
                
                <div style="background: rgba(0,0,0,0.2); border-radius: 10px; padding: 15px; margin: 20px 0; color: #fca5a5; font-size: 0.95rem;">
                    <p>💰 You keep all points earned!</p>
                    <p style="margin-top: 8px;">🔓 Complete Level ${adaptiveState.currentLevel} normally to unlock Clock Challenge again.</p>
                </div>
                
                <button onclick="closeClockTimeoutModal()" style="padding: 15px 35px; background: white; color: #991b1b; border: none; border-radius: 12px; font-size: 1.1rem; font-weight: 700; cursor: pointer;">
                    Continue in Normal Mode
                </button>
            </div>
        </div>
    `;
    document.body.appendChild(modal);
}

function closeClockTimeoutModal() {
    const modal = document.getElementById('clockTimeoutModal');
    if (modal) modal.remove();
    hideClockTimerUI();
    adaptiveState.clockMode = false;
    adaptiveState.clockSessionId = null;
    
    // Continue to next question in normal mode
    console.log('🕐 Timeout - continuing in normal mode at level:', adaptiveState.currentLevel);
    continueAdaptiveQuizBeta();
}

// Clock success
function clockSuccess() {
    stopClockTimer();
    
    const timeRemaining = adaptiveState.clockTimeRemaining;
    const timeAllowed = adaptiveState.clockTimeAllowed;
    const percent = (timeRemaining / timeAllowed) * 100;
    
    let bonusTier = null, bonusPoints = 0, bonusEmoji = '', bonusName = '';
    
    if (percent >= 40) {
        bonusTier = 'lightning'; bonusPoints = 50; bonusEmoji = '⚡'; bonusName = 'Lightning Fast';
    } else if (percent >= 20) {
        bonusTier = 'fast'; bonusPoints = 35; bonusEmoji = '🔥'; bonusName = 'Speed Demon';
    } else if (percent >= 1) {
        bonusTier = 'on_time'; bonusPoints = 20; bonusEmoji = '✅'; bonusName = 'Beat the Clock';
    }
    
    completeClockChallenge(true);
    
    const minutes = Math.floor(timeRemaining / 60);
    const seconds = timeRemaining % 60;
    const timeStr = `${minutes}:${seconds.toString().padStart(2, '0')}`;
    
    const tierColors = {
        lightning: { bg: 'linear-gradient(135deg, #fbbf24, #f59e0b)', text: '#1e1b4b' },
        fast: { bg: 'linear-gradient(135deg, #f97316, #ea580c)', text: 'white' },
        on_time: { bg: 'linear-gradient(135deg, #22c55e, #16a34a)', text: 'white' }
    };
    const colors = tierColors[bonusTier] || tierColors.on_time;
    
    const modal = document.createElement('div');
    modal.id = 'clockSuccessModal';
    modal.innerHTML = `
        <div style="position: fixed; inset: 0; background: rgba(0,0,0,0.8); z-index: 10000; display: flex; align-items: flex-start; justify-content: center; padding: 20px; overflow-y: auto; -webkit-overflow-scrolling: touch;">
            <div style="background: ${colors.bg}; border-radius: 20px; padding: 25px; max-width: 420px; width: 100%; color: ${colors.text}; text-align: center; box-shadow: 0 25px 50px rgba(0,0,0,0.5); animation: clockSuccessPop 0.5s ease-out; margin: auto 0;">
                
                <div style="font-size: 5rem; margin-bottom: 10px; animation: clockBounce 0.6s ease-out;">${bonusEmoji}</div>
                
                <h2 style="font-size: 2rem; margin-bottom: 5px; font-weight: 800;">${bonusName.toUpperCase()}!</h2>
                
                <p style="font-size: 1.2rem; margin-bottom: 20px; opacity: 0.9;">You beat the clock!</p>
                
                <div style="background: rgba(0,0,0,0.15); border-radius: 15px; padding: 20px; margin-bottom: 20px;">
                    <div style="font-size: 3rem; font-weight: 800; margin-bottom: 5px;">+${bonusPoints}</div>
                    <div style="font-size: 1rem; opacity: 0.9;">BONUS POINTS!</div>
                </div>
                
                <div style="display: flex; justify-content: center; gap: 20px; margin-bottom: 25px; font-size: 0.95rem;">
                    <div>
                        <div style="font-weight: 600;">⏱️ ${timeStr}</div>
                        <div style="opacity: 0.8; font-size: 0.85rem;">Time Left</div>
                    </div>
                    <div>
                        <div style="font-weight: 600;">✅ ${adaptiveState.clockQuestionsCorrect}/${adaptiveState.clockQuestionsAnswered}</div>
                        <div style="opacity: 0.8; font-size: 0.85rem;">Correct</div>
                    </div>
                </div>
                
                <button onclick="closeClockSuccessModal()" style="padding: 15px 35px; background: rgba(0,0,0,0.2); color: inherit; border: 2px solid rgba(0,0,0,0.1); border-radius: 12px; font-size: 1.1rem; font-weight: 700; cursor: pointer;">
                    Awesome! Continue →
                </button>
            </div>
        </div>
    `;
    document.body.appendChild(modal);
    
    // Refresh stats
    if (typeof loadBadgeWidget === 'function') loadBadgeWidget();
}

async function closeClockSuccessModal() {
    const modal = document.getElementById('clockSuccessModal');
    if (modal) modal.remove();
    hideClockTimerUI();
    adaptiveState.clockMode = false;
    adaptiveState.clockSessionId = null;
    
    // Check if next level is eligible for Clock Challenge (L6-10)
    const nextLevelEligible = adaptiveState.currentLevel >= 6 && adaptiveState.currentLevel <= 10;
    console.log('🕐 After clock success, currentLevel:', adaptiveState.currentLevel, 'eligible for next clock:', nextLevelEligible);
    
    if (nextLevelEligible) {
        // Offer clock challenge for the new level
        const result = await showClockOptInModal(adaptiveState.currentLevel);
        if (result.start) {
            await startClockChallenge(adaptiveState.currentLevel, result.lifelines, result.cost);
        }
    }
    
    continueAdaptiveQuizBeta();
}

// Complete clock challenge API call
async function completeClockChallenge(completed) {
    try {
        await fetch('/api/clock-challenge/complete', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                topic: adaptiveState.topic,
                level: adaptiveState.currentLevel,
                session_id: adaptiveState.clockSessionId,
                time_remaining: adaptiveState.clockTimeRemaining,
                questions_answered: adaptiveState.clockQuestionsAnswered,
                questions_correct: adaptiveState.clockQuestionsCorrect,
                penalties_applied: adaptiveState.clockPenaltiesApplied,
                completed: completed
            })
        });
    } catch (error) {
        console.error('Error completing clock challenge:', error);
    }
}

// Unlock clock challenge for a level after normal completion (Rev 3.0.8)
async function unlockClockChallenge(level) {
    try {
        console.log(`🔓 Unlocking Clock Challenge for Level ${level}`);
        const response = await fetch('/api/clock-challenge/unlock', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                topic: adaptiveState.topic,
                level: level
            })
        });
        const data = await response.json();
        if (data.success) {
            console.log(`🔓 Clock Challenge unlocked for Level ${level}`);
        }
    } catch (error) {
        console.log('Could not unlock clock challenge:', error);
    }
}

// =====================================================
// END CLOCK CHALLENGE
// =====================================================

// Offer clock challenge from level-up screen (Rev 3.0)
async function offerClockChallenge() {
    // Hide the feedback panel
    document.getElementById('adaptiveFeedbackBeta').classList.add('hidden');
    
    // Show opt-in modal
    const result = await showClockOptInModal(adaptiveState.currentLevel);
    
    if (result.start) {
        await startClockChallenge(adaptiveState.currentLevel, result.lifelines, result.cost);
    }
    
    // Continue to next question either way
    continueAdaptiveQuizBeta();
}


console.log("⏱️ Clock Challenge module loaded");

// =====================================================
// DAY 1 FEATURES - Online Counter, Hot Streak
// =====================================================

// === WHO'S ONLINE COUNTER ===
let onlineCountInterval = null;

async function fetchOnlineCount() {
    try {
        const response = await fetch('/api/online-count');
        if (response.ok) {
            const data = await response.json();
            updateOnlineDisplay(data.count || data.online_count || 0);
        }
    } catch (e) {
        console.log('Could not fetch online count');
    }
}

function updateOnlineDisplay(count) {
    const el1 = document.getElementById('onlineCount');
    const el2 = document.getElementById('onlineCountMini');
    
    if (el1) el1.textContent = count;
    if (el2) el2.textContent = count;
}

function startOnlineCounter() {
    fetchOnlineCount(); // Fetch immediately
    onlineCountInterval = setInterval(fetchOnlineCount, 30000); // Update every 30 seconds
}

function stopOnlineCounter() {
    if (onlineCountInterval) {
        clearInterval(onlineCountInterval);
        onlineCountInterval = null;
    }
}

// === ENHANCED HOT STREAK INDICATOR ===
let currentStreak = 0;

function updateHotStreakDisplay(streak) {
    currentStreak = streak;
    const display = document.getElementById('hotStreakDisplay');
    const countEl = document.getElementById('streakCount');
    const labelEl = document.getElementById('streakLabel');
    const multiplierEl = document.getElementById('streakMultiplierBadge');
    
    if (!display) return;
    
    countEl.textContent = streak;
    
    // Remove all streak classes
    display.classList.remove('streak-cold', 'streak-warming', 'streak-hot', 'streak-fire', 'streak-legendary');
    
    // Apply appropriate class based on streak level
    if (streak === 0) {
        display.classList.add('streak-cold');
        labelEl.textContent = 'streak';
        multiplierEl.style.display = 'none';
    } else if (streak < 3) {
        display.classList.add('streak-warming');
        labelEl.textContent = 'in a row!';
        multiplierEl.style.display = 'none';
    } else if (streak < 5) {
        display.classList.add('streak-hot');
        labelEl.textContent = 'HOT!';
        multiplierEl.textContent = '1.5x';
        multiplierEl.style.display = 'inline';
        // Play streak sound on reaching 3
        if (streak === 3) playSound('streak3');
    } else if (streak < 10) {
        display.classList.add('streak-fire');
        labelEl.textContent = 'ON FIRE!';
        multiplierEl.textContent = '2x';
        multiplierEl.style.display = 'inline';
        // Play streak sound on reaching 5
        if (streak === 5) playSound('streak5');
    } else {
        display.classList.add('streak-legendary');
        labelEl.textContent = 'LEGENDARY!';
        multiplierEl.textContent = '3x';
        multiplierEl.style.display = 'inline';
        // Play streak sound on reaching 10
        if (streak === 10) playSound('streak10');
    }
    
    // Update the old streak badge for compatibility
    const oldBadge = document.getElementById('compactStreakBadge');
    if (oldBadge) {
        if (streak >= 3) {
            let multiplier = streak >= 10 ? '3x' : (streak >= 5 ? '2x' : '1.5x');
            oldBadge.innerHTML = `🔥 ${multiplier}`;
            oldBadge.classList.add('visible');
        } else {
            oldBadge.classList.remove('visible');
        }
    }
}

// Initialize Day 1 features on page load
function initDay1Features() {
    initSoundSystem();
    startOnlineCounter();
    updateHotStreakDisplay(0);
    console.log('🚀 Day 1 features initialized: Sound Effects, Online Counter, Hot Streak');
}

// ==================== END DAY 1 FEATURES ====================

// =====================================================
// DAY 2 FEATURES - Quick Play, Weekly Challenge, Leaderboard
// =====================================================

// ==================== DAY 2 FEATURES ====================
// Quick Play, Weekly Challenge, Enhanced Leaderboard

// === QUICK PLAY MODE ===
let quickPlayDifficulty = 'intermediate';
let isQuickPlayMode = false;

function showQuickPlayModal() {
    document.getElementById('quickPlayModal').classList.remove('hidden');
    document.getElementById('quickPlayModal').classList.add('flex');
}

function closeQuickPlayModal() {
    document.getElementById('quickPlayModal').classList.add('hidden');
    document.getElementById('quickPlayModal').classList.remove('flex');
}


// === SMART QUIZ SYSTEM (Adaptive Learning) ===
let smartQuizMode = 'auto';  // auto, review, practice, challenge
let smartQuizData = null;

function showSmartQuizGuestMessage() {
    alert('🔒 Smart Quiz requires a Guest Code!\n\nSmart Quiz uses AI to personalise your learning based on your quiz history.\n\nClick "Return with Code" on the home page to get your personal guest code, or register for a full account!');
}

function showSmartQuizModal() {
    // First fetch the recommendation
    fetchSmartQuizRecommendation('auto');
    document.getElementById('smartQuizModal').classList.remove('hidden');
    document.getElementById('smartQuizModal').classList.add('flex');
}

function closeSmartQuizModal() {
    document.getElementById('smartQuizModal').classList.add('hidden');
    document.getElementById('smartQuizModal').classList.remove('flex');
}

function setSmartQuizMode(mode) {
    smartQuizMode = mode;
    // Update button states
    document.querySelectorAll('.smart-mode-btn').forEach(btn => {
        if (btn.dataset.mode === mode) {
            btn.classList.add('border-green-400', 'bg-green-50');
            btn.classList.remove('border-gray-200');
        } else {
            btn.classList.remove('border-green-400', 'bg-green-50');
            btn.classList.add('border-gray-200');
        }
    });
    // Fetch new recommendation for this mode
    fetchSmartQuizRecommendation(mode);
}

async function fetchSmartQuizRecommendation(mode) {
    const loadingEl = document.getElementById('smartQuizLoading');
    const contentEl = document.getElementById('smartQuizContent');
    const errorEl = document.getElementById('smartQuizError');
    
    loadingEl.classList.remove('hidden');
    contentEl.classList.add('hidden');
    errorEl.classList.add('hidden');
    
    try {
        const response = await fetch('/api/adaptive/smart-quiz', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ mode: mode })
        });
        
        if (!response.ok) {
            const err = await response.json();
            throw new Error(err.error || 'Failed to get recommendation');
        }
        
        smartQuizData = await response.json();
        
        // Update the UI
        document.getElementById('smartQuizTopic').textContent = formatTopicName(smartQuizData.topic);
        document.getElementById('smartQuizDifficulty').textContent = capitalise(smartQuizData.difficulty);
        document.getElementById('smartQuizReason').textContent = smartQuizData.reason || 'Recommended for you';
        
        // Set difficulty badge color
        const diffBadge = document.getElementById('smartQuizDifficulty');
        diffBadge.className = 'px-3 py-1 rounded-full text-sm font-medium';
        if (smartQuizData.difficulty === 'beginner') {
            diffBadge.classList.add('bg-green-100', 'text-green-700');
        } else if (smartQuizData.difficulty === 'intermediate') {
            diffBadge.classList.add('bg-yellow-100', 'text-yellow-700');
        } else {
            diffBadge.classList.add('bg-red-100', 'text-red-700');
        }
        
        // Show mastery if available
        if (smartQuizData.mastery_level !== undefined) {
            document.getElementById('smartQuizMastery').textContent = 
                `Current mastery: ${Math.round(smartQuizData.mastery_level)}%`;
            document.getElementById('smartQuizMasteryContainer').classList.remove('hidden');
        } else {
            document.getElementById('smartQuizMasteryContainer').classList.add('hidden');
        }
        
        loadingEl.classList.add('hidden');
        contentEl.classList.remove('hidden');
        
    } catch (error) {
        console.error('Smart Quiz error:', error);
        loadingEl.classList.add('hidden');
        errorEl.textContent = error.message || 'Could not load recommendation';
        errorEl.classList.remove('hidden');
    }
}

function formatTopicName(topic) {
    if (!topic) return 'Unknown Topic';
    return topic.split('_').map(word => 
        word.charAt(0).toUpperCase() + word.slice(1)
    ).join(' ');
}

function capitalise(str) {
    if (!str) return '';
    return str.charAt(0).toUpperCase() + str.slice(1);
}

async function startSmartQuiz() {
    if (!smartQuizData || !smartQuizData.topic) {
        alert('Please wait for the recommendation to load.');
        return;
    }
    
    closeSmartQuizModal();
    
    // Store the topic and difficulty
    currentTopic = smartQuizData.topic;
    currentDifficulty = smartQuizData.difficulty;
    
    // Show loading
    document.getElementById('topicScreen').classList.add('hidden');
    document.getElementById('loadingScreen').classList.remove('hidden');
    
    try {
        // Fetch questions for the recommended topic/difficulty
        const response = await fetch(`/api/questions/${currentTopic}/${currentDifficulty}`);
        
        if (!response.ok) {
            throw new Error('Failed to load questions');
        }
        
        questions = await response.json();
        
        if (questions.length === 0) {
            alert('No questions available for this topic. Try another!');
            document.getElementById('loadingScreen').classList.add('hidden');
            document.getElementById('topicScreen').classList.remove('hidden');
            return;
        }
        
        // Shuffle and limit to quiz size
        questions = questions.sort(() => Math.random() - 0.5).slice(0, 20);
        
        // Set up quiz state
        currentQuestionIndex = 0;
        score = 0;
        answered = false;
        startTime = Date.now();
        isQuickPlayMode = false;
        
        // Reset tracking
        consecutiveCorrect = 0;
        maxConsecutiveCorrect = 0;
        questionsAnsweredInQuiz = 0;
        shownMilestones.clear();
        totalMilestonePoints = 0;
        currentStreak = 0;
        hintUsedThisQuestion = false;
        updateHotStreakDisplay(0);
        
        // Show quiz
        document.getElementById('loadingScreen').classList.add('hidden');
        document.getElementById('quizScreen').classList.remove('hidden');
        document.body.classList.add('quiz-active');
        
        // Update header with Smart Quiz indicator
        document.getElementById('compactTopicTitle').textContent = 
            '🧠 ' + formatTopicName(currentTopic);
        
        showQuestion();
        
    } catch (error) {
        console.error('Smart Quiz start error:', error);
        alert('Could not start Smart Quiz. Please try again.');
        document.getElementById('loadingScreen').classList.add('hidden');
        document.getElementById('topicScreen').classList.remove('hidden');
    }
}

function setQuickPlayDifficulty(diff) {
    quickPlayDifficulty = diff;
    // Update button states
    document.querySelectorAll('.quick-diff-btn').forEach(btn => {
        if (btn.dataset.diff === diff) {
            btn.classList.add('border-orange-400', 'bg-orange-50');
            btn.classList.remove('border-gray-200');
        } else {
            btn.classList.remove('border-orange-400', 'bg-orange-50');
            btn.classList.add('border-gray-200');
        }
    });
}

async function startQuickPlay() {
    closeQuickPlayModal();
    isQuickPlayMode = true;
    
    // Show loading
    document.getElementById('topicScreen').classList.add('hidden');
    document.getElementById('loadingScreen').classList.remove('hidden');
    
    try {
        // Fetch 10 random questions from various topics
        const response = await fetch(`/api/quick-play/${quickPlayDifficulty}`);
        
        if (!response.ok) {
            throw new Error('Failed to load quick play questions');
        }
        
        questions = await response.json();
        
        if (questions.length === 0) {
            alert('No questions available for Quick Play. Try a regular quiz!');
            document.getElementById('loadingScreen').classList.add('hidden');
            document.getElementById('topicScreen').classList.remove('hidden');
            isQuickPlayMode = false;
            return;
        }
        
        // Set up quiz state
        currentTopic = 'quick_play';
        currentDifficulty = quickPlayDifficulty;
        currentQuestionIndex = 0;
        score = 0;
        answered = false;
        startTime = Date.now();
        
        // Reset tracking
        consecutiveCorrect = 0;
        maxConsecutiveCorrect = 0;
        questionsAnsweredInQuiz = 0;
        shownMilestones.clear();
        totalMilestonePoints = 0;
        currentStreak = 0;
        hintUsedThisQuestion = false;
        updateHotStreakDisplay(0);
        
        // Show quiz
        document.getElementById('loadingScreen').classList.add('hidden');
        document.getElementById('quizScreen').classList.remove('hidden');
        document.body.classList.add('quiz-active');
        
        // Update header
        document.getElementById('compactTopicTitle').textContent = '⚡ Quick Play';
        
        showQuestion();
        
    } catch (error) {
        console.error('Quick Play error:', error);
        alert('Could not start Quick Play. Please try again.');
        document.getElementById('loadingScreen').classList.add('hidden');
        document.getElementById('topicScreen').classList.remove('hidden');
        isQuickPlayMode = false;
    }
}

// === WEEKLY CHALLENGE SYSTEM ===
let weeklyChallenge = {
    quizzesCompleted: 0,
    highScoreCount: 0,
    maxStreak: 0,
    goals: [
        { id: 'goal1', target: 5, current: 0, points: 50, type: 'quizzes' },
        { id: 'goal2', target: 3, current: 0, points: 75, type: 'highscores' },
        { id: 'goal3', target: 5, current: 0, points: 100, type: 'streak' }
    ]
};

async function loadWeeklyChallenge() {
    try {
        const response = await fetch('/api/weekly-challenge/status');
        if (response.ok) {
            const data = await response.json();
            weeklyChallenge = data.challenge || weeklyChallenge;
        }
    } catch (e) {
        console.log('Weekly challenge status not available');
    }
    updateWeeklyChallengeUI();
}

function updateWeeklyChallengeUI() {
    // Update progress bar
    const completedGoals = weeklyChallenge.goals.filter(g => g.current >= g.target).length;
    const progressPercent = (completedGoals / 3) * 100;
    
    // Update mini sidebar version
    const progressBarMini = document.getElementById('challengeProgressBarMini');
    const progressTextMini = document.getElementById('challengeProgressTextMini');
    
    if (progressBarMini) {
        progressBarMini.style.width = progressPercent + '%';
    }
    if (progressTextMini) {
        progressTextMini.textContent = `${completedGoals}/3 Goals`;
    }
    
    // Update individual goals (mini version)
    weeklyChallenge.goals.forEach((goal, index) => {
        const goalEl = document.getElementById(`goal${index + 1}Mini`);
        if (goalEl) {
            if (goal.current >= goal.target) {
                goalEl.classList.add('completed');
            }
        }
    });
    
    // Update timer
    updateChallengeTimer();
}

function updateChallengeTimer() {
    const now = new Date();
    const endOfWeek = new Date();
    endOfWeek.setDate(now.getDate() + (7 - now.getDay())); // Next Sunday
    endOfWeek.setHours(23, 59, 59, 999);
    
    const diff = endOfWeek - now;
    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    
    const timerStr = days > 0 ? `${days}d ${hours}h` : `${hours}h`;
    
    // Update mini version
    const timerElMini = document.getElementById('challengeTimeLeftMini');
    if (timerElMini) {
        timerElMini.textContent = timerStr;
    }
}

// Update challenge progress after quiz completion
function updateChallengeProgress(quizScore, percentage, maxStreakAchieved) {
    // Goal 1: Complete quizzes
    weeklyChallenge.goals[0].current++;
    
    // Goal 2: Score 80%+
    if (percentage >= 80) {
        weeklyChallenge.goals[1].current++;
    }
    
    // Goal 3: Get 5-streak
    if (maxStreakAchieved >= 5) {
        weeklyChallenge.goals[2].current = Math.max(weeklyChallenge.goals[2].current, maxStreakAchieved);
    }
    
    updateWeeklyChallengeUI();
    
    // Save to server
    fetch('/api/weekly-challenge/update', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            quizzes: weeklyChallenge.goals[0].current,
            highscores: weeklyChallenge.goals[1].current,
            max_streak: weeklyChallenge.goals[2].current
        })
    }).catch(e => console.log('Could not save challenge progress'));
}

// === ENHANCED LEADERBOARD ===
let currentLeaderboardType = 'weekly';
let leaderboardExpanded = false;
let fullLeaderboardData = [];

async function loadLeaderboard(type = 'weekly') {
    currentLeaderboardType = type;
    const listEl = document.getElementById('leaderboardListMini');
    
    if (!listEl) return;
    
    listEl.innerHTML = '<div class="text-center text-gray-400 py-2" style="font-size:11px;"><i class="fas fa-spinner fa-spin"></i></div>';
    
    try {
        const response = await fetch(`/api/leaderboard/${type}`);
        if (!response.ok) throw new Error('Failed to load');
        
        const data = await response.json();
        fullLeaderboardData = data.leaderboard || [];
        renderLeaderboardMini(fullLeaderboardData, data.my_position);
    } catch (e) {
        console.log('Leaderboard load error:', e);
        listEl.innerHTML = '<div class="text-center text-gray-400 py-2" style="font-size:11px;">Could not load</div>';
    }
}

function renderLeaderboardMini(leaderboard, myPosition) {
    const listEl = document.getElementById('leaderboardListMini');
    const expandedEl = document.getElementById('leaderboardListExpanded');
    if (!listEl) return;
    
    if (leaderboard.length === 0) {
        listEl.innerHTML = '<div class="text-center text-gray-400 py-2" style="font-size:11px;">No data yet</div>';
        return;
    }
    
    // Get current user's guest code for highlighting
    const myGuestCode = document.body.dataset.guestCode || '';
    
    // Render top 3
    let topHtml = '';
    leaderboard.slice(0, 3).forEach((player, index) => {
        const rank = index + 1;
        const isMe = player.guest_code === myGuestCode || player.is_current_user;
        
        let rankClass = rank === 1 ? 'gold' : (rank === 2 ? 'silver' : 'bronze');
        let rankDisplay = rank === 1 ? '🥇' : (rank === 2 ? '🥈' : '🥉');
        let itemClass = `lb-mini-item top-${rank}${isMe ? ' is-me' : ''}`;
        
        topHtml += `
            <div class="${itemClass}">
                <span class="lb-mini-rank ${rankClass}">${rankDisplay}</span>
                <span class="lb-mini-name">${player.name || player.guest_code || 'Anon'}${isMe ? ' (You)' : ''}</span>
                <span class="lb-mini-score">${player.points || player.total_score || 0}</span>
            </div>
        `;
    });
    
    // If user is not in top 3 but we have their position, show it
    const userInTop3 = leaderboard.slice(0, 3).some(p => p.is_current_user || p.guest_code === myGuestCode);
    if (!userInTop3 && myPosition) {
        topHtml += `
            <div class="lb-mini-divider">···</div>
            <div class="lb-mini-item is-me">
                <span class="lb-mini-rank">#${myPosition.rank}</span>
                <span class="lb-mini-name">${myPosition.name} (You)</span>
                <span class="lb-mini-score">${myPosition.points || 0}</span>
            </div>
        `;
    }
    
    listEl.innerHTML = topHtml;
    
    // Render expanded (4-20)
    if (expandedEl && leaderboard.length > 3) {
        let expandedHtml = '';
        leaderboard.slice(3, 20).forEach((player, index) => {
            const rank = index + 4;
            const isMe = player.guest_code === myGuestCode || player.is_current_user;
            let itemClass = `lb-mini-item${isMe ? ' is-me' : ''}`;
            
            expandedHtml += `
                <div class="${itemClass}">
                    <span class="lb-mini-rank">${rank}</span>
                    <span class="lb-mini-name">${player.name || player.guest_code || 'Anon'}${isMe ? ' (You)' : ''}</span>
                    <span class="lb-mini-score">${player.points || player.total_score || 0}</span>
                </div>
            `;
        });
        
        // If user is not in top 20 but we have their position, show at bottom of expanded
        const userInTop20 = leaderboard.some(p => p.is_current_user || p.guest_code === myGuestCode);
        if (!userInTop20 && myPosition && myPosition.rank > 20) {
            expandedHtml += `
                <div class="lb-mini-divider">···</div>
                <div class="lb-mini-item is-me">
                    <span class="lb-mini-rank">#${myPosition.rank}</span>
                    <span class="lb-mini-name">${myPosition.name} (You)</span>
                    <span class="lb-mini-score">${myPosition.points || 0}</span>
                </div>
            `;
        }
        
        expandedEl.innerHTML = expandedHtml;
    }
}

function toggleLeaderboardExpand() {
    leaderboardExpanded = !leaderboardExpanded;
    const expandedEl = document.getElementById('leaderboardListExpanded');
    const btn = document.querySelector('.leaderboard-expand-btn');
    
    if (expandedEl) {
        if (leaderboardExpanded) {
            expandedEl.classList.remove('hidden');
            btn?.classList.add('expanded');
        } else {
            expandedEl.classList.add('hidden');
            btn?.classList.remove('expanded');
        }
    }
}

function switchLeaderboard(type, event) {
    // Update tabs
    document.querySelectorAll('.lb-tab-mini').forEach(tab => {
        tab.classList.remove('active');
    });
    if (event && event.target) {
        event.target.classList.add('active');
    }
    
    loadLeaderboard(type);
}

// Initialize Day 2 features
function initDay2Features() {
    loadWeeklyChallenge();
    loadLeaderboard('weekly');
    console.log('📊 Day 2 features initialized: Quick Play, Weekly Challenge, Leaderboard');
}

// ==================== END DAY 2 FEATURES ====================

// =====================================================
// MILESTONE & ACHIEVEMENT SYSTEM
// =====================================================

// ========================================
// MILESTONE CELEBRATION SYSTEM
// ========================================

function createConfetti(container) {
    const canvas = document.createElement('canvas');
    canvas.className = 'confetti-canvas';
    canvas.width = container.offsetWidth;
    canvas.height = container.offsetHeight;
    
    const ctx = canvas.getContext('2d');
    const pieces = [];
    const numberOfPieces = 100;
    const colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#feca57', '#ee5a6f', '#c7ecee', '#ffd700', '#ff85c0'];
    
    class ConfettiPiece {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height - canvas.height;
            this.size = Math.random() * 8 + 4;
            this.speedY = Math.random() * 3 + 2;
            this.speedX = Math.random() * 2 - 1;
            this.color = colors[Math.floor(Math.random() * colors.length)];
            this.rotation = Math.random() * 360;
            this.rotationSpeed = Math.random() * 10 - 5;
        }
        
        update() {
            this.y += this.speedY;
            this.x += this.speedX;
            this.rotation += this.rotationSpeed;
            
            if (this.y > canvas.height) {
                this.y = -10;
                this.x = Math.random() * canvas.width;
            }
        }
        
        draw() {
            ctx.save();
            ctx.translate(this.x, this.y);
            ctx.rotate(this.rotation * Math.PI / 180);
            ctx.fillStyle = this.color;
            ctx.fillRect(-this.size/2, -this.size/2, this.size, this.size);
            ctx.restore();
        }
    }
    
    for (let i = 0; i < numberOfPieces; i++) {
        pieces.push(new ConfettiPiece());
    }
    
    let animationId;
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        pieces.forEach(piece => {
            piece.update();
            piece.draw();
        });
        animationId = requestAnimationFrame(animate);
    }
    
    animate();
    
    // Stop after 5 seconds
    setTimeout(() => {
        cancelAnimationFrame(animationId);
        canvas.remove();
    }, 5000);
    
    return canvas;
}

function showMilestoneModal(badges) {
    if (!badges || badges.length === 0) return;
    
    console.log('🎉 Showing milestone modal for badges:', badges);
    
    // Create overlay
    const overlay = document.createElement('div');
    overlay.className = 'milestone-overlay';
    overlay.id = 'milestone-overlay';
    
    // Create modal
    const modal = document.createElement('div');
    modal.className = 'milestone-modal';
    
    // Check if this is a special achievement (perfect score, mastery, etc)
    const isSpecial = badges.some(b => 
        b.name.includes('Perfect') || 
        b.name.includes('Flawless') ||
        b.name.includes('Master') || 
        b.name.includes('Genius') ||
        b.name.includes('Excellence')
    );
    
    if (isSpecial) {
        modal.classList.add('perfect-score');
    }
    
    // Get appropriate icon
    const getIcon = (badge) => {
        if (badge.icon && badge.icon !== 'null') return badge.icon;
        // Default icons based on badge name
        if (badge.name.includes('Perfect') || badge.name.includes('Flawless')) return '💯';
        if (badge.name.includes('Master') || badge.name.includes('Genius')) return '🎓';
        if (badge.name.includes('Streak') || badge.name.includes('Warrior')) return '🔥';
        if (badge.name.includes('First')) return '🌟';
        if (badge.name.includes('Sharp')) return '🎯';
        return '🏆';
    };
    
    const mainIcon = badges.length === 1 ? getIcon(badges[0]) : (badges.length > 1 ? '🎉' : '🏆');
    
    // Build modal content
    modal.innerHTML = `
        <div class="milestone-icon">${mainIcon}</div>
        <div class="milestone-title">
            ${badges.length === 1 ? 'Achievement Unlocked!' : badges.length + ' Achievements!'}
        </div>
        <div class="milestone-subtitle">
            You've earned ${badges.length === 1 ? 'a new badge' : badges.length + ' new badges'}!
        </div>
        
        <div class="milestone-badges-container">
            ${badges.map(badge => `
                <div class="milestone-badge">
                    <div class="milestone-badge-icon">${getIcon(badge)}</div>
                    <div class="milestone-badge-name">${badge.name}</div>
                    <div class="milestone-badge-description">${badge.description}</div>
                    <div class="milestone-badge-points">+${badge.points} points</div>
                </div>
            `).join('')}
        </div>
        
        <button class="milestone-continue-btn" onclick="closeMilestoneModal()">
            Continue
        </button>
    `;
    
    overlay.appendChild(modal);
    document.body.appendChild(overlay);
    
    // Add confetti for special achievements
    if (isSpecial) {
        const confettiCanvas = createConfetti(modal);
        modal.insertBefore(confettiCanvas, modal.firstChild);
    }
    
    // Play achievement sound (optional)
    playAchievementSound();
}

function closeMilestoneModal() {
    const overlay = document.getElementById('milestone-overlay');
    if (overlay) {
        overlay.style.animation = 'fadeIn 0.3s ease-out reverse';
        setTimeout(() => overlay.remove(), 300);
    }
}

function playAchievementSound() {
    // Optional: Add achievement sound
    // You can add an audio file and play it here
    try {
        // const audio = new Audio('/static/achievement.mp3');
        // audio.volume = 0.3;
        // audio.play().catch(e => console.log('Could not play sound:', e));
    } catch (e) {
        // Sound playback failed, that's okay
    }
}

// ==================== CLIENT-SIDE ACHIEVEMENT POPUPS ====================
// High-contrast celebration popups for ALL users (guests and logged-in)

function showAchievementPopup(achievement) {
    console.log('🎉 Showing achievement popup:', achievement);
    
    // Track milestone points
    if (achievement.points) {
        totalMilestonePoints += achievement.points;
        console.log(`💰 Milestone points earned: +${achievement.points} (Total milestones: ${totalMilestonePoints})`);
    }
    
    // Create overlay
    const overlay = document.createElement('div');
    overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.85);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 10000;
        animation: fadeIn 0.3s ease-out;
    `;
    
    // Create modal
    const modal = document.createElement('div');
    modal.style.cssText = `
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 40px;
        max-width: 500px;
        width: 90%;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
        text-align: center;
        position: relative;
        animation: slideUp 0.5s ease-out;
        color: #ffffff;
    `;
    
    modal.innerHTML = `
        <div style="font-size: 80px; margin-bottom: 20px; animation: bounce 1s ease-in-out infinite;">
            ${achievement.icon}
        </div>
        <h2 style="
            color: #ffffff;
            font-size: 32px;
            font-weight: bold;
            margin: 20px 0;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        ">
            ${achievement.title}
        </h2>
        <p style="
            color: #ffffff;
            font-size: 18px;
            margin: 15px 0;
            line-height: 1.6;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
        ">
            ${achievement.description}
        </p>
        <div style="
            background: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            padding: 15px;
            margin: 20px 0;
        ">
            <div style="
                color: #ffffff;
                font-size: 16px;
                font-weight: 600;
                text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
            ">
                Achievement Points
            </div>
            <div style="
                color: #ffd700;
                font-size: 36px;
                font-weight: bold;
                margin-top: 5px;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            ">
                +${achievement.points}
            </div>
        </div>
        <button onclick="this.closest('.achievement-overlay').remove()" style="
            background: rgba(255, 255, 255, 0.9);
            color: #667eea;
            border: none;
            padding: 12px 30px;
            font-size: 16px;
            font-weight: 600;
            border-radius: 25px;
            cursor: pointer;
            margin-top: 10px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        " 
        onmouseover="this.style.background='#ffffff'; this.style.transform='scale(1.05)';"
        onmouseout="this.style.background='rgba(255, 255, 255, 0.9)'; this.style.transform='scale(1)';">
            Awesome! ✨
        </button>
    `;
    
    overlay.className = 'achievement-overlay';
    overlay.appendChild(modal);
    
    // Add confetti
    createAchievementConfetti(overlay);
    
    document.body.appendChild(overlay);
    
    // Add animations if not already added
    if (!document.getElementById('achievement-animations')) {
        const style = document.createElement('style');
        style.id = 'achievement-animations';
        style.textContent = `
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            @keyframes slideUp {
                from {
                    transform: translateY(50px);
                    opacity: 0;
                }
                to {
                    transform: translateY(0);
                    opacity: 1;
                }
            }
            @keyframes bounce {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-20px); }
            }
            @keyframes confettiFall {
                to {
                    transform: translateY(100vh) rotate(360deg);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }
}

function createAchievementConfetti(container) {
    const colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#f9ca24', '#ff9ff3'];
    const confettiCount = 50;
    
    for (let i = 0; i < confettiCount; i++) {
        const confetti = document.createElement('div');
        confetti.style.cssText = `
            position: fixed;
            width: 10px;
            height: 10px;
            background: ${colors[Math.floor(Math.random() * colors.length)]};
            top: -10px;
            left: ${Math.random() * 100}%;
            opacity: ${Math.random() * 0.7 + 0.3};
            animation: confettiFall ${Math.random() * 3 + 2}s linear forwards;
            animation-delay: ${Math.random() * 0.5}s;
            border-radius: ${Math.random() > 0.5 ? '50%' : '0'};
            z-index: 9999;
        `;
        container.appendChild(confetti);
        
        // Remove confetti after animation
        setTimeout(() => confetti.remove(), 5000);
    }
}

console.log('✅ Client-side achievement system loaded!');

// =====================================================
// TUTORIAL DATA STRUCTURE
// =====================================================

/**
 * TUTORIAL DATA STRUCTURE
 * 
 * This file contains all tutorial content for topics.
 * To add a new topic tutorial, simply add a new entry to the TUTORIALS object.
 * 
 * Structure:
 * TUTORIALS = {
 *   'topic_name': {
 *     'beginner': { title, introduction, principles, examples, tips },
 *     'intermediate': { ... },
 *     'advanced': { ... }
 *   }
 * }
 */

const TUTORIALS = {
    // Introductory Algebra Tutorial Content
    'introductory_algebra': {
        'beginner': {
            title: 'Collecting Like Terms',
            introduction: 'In this level, you\'ll learn to <strong>collect like terms</strong> - combining terms that have the same letter.',
            
            principles: [
                {
                    title: 'Like Terms',
                    content: '<strong>Like terms</strong> have exactly the same letter part.<br>• 3x and 5x are like terms (both have \'x\')<br>• 4y and 2y are like terms (both have \'y\')<br>• 3x and 5y are NOT like terms (different letters)'
                },
                {
                    title: 'How to Collect',
                    content: 'Think of it like fruit: 3 apples + 5 apples = 8 apples<br>Just add the numbers, keep the letter!'
                }
            ],
            
            examples: [
                {
                    question: 'Simplify: 4x + 3x',
                    steps: [
                        'Both terms have \'x\' - they are like terms ✓',
                        'Add the numbers: 4 + 3 = 7',
                        'Keep the letter: x'
                    ],
                    answer: '7x'
                },
                {
                    question: 'Simplify: 5y + 2y',
                    steps: [
                        'Both terms have \'y\' - they are like terms ✓',
                        'Add the numbers: 5 + 2 = 7',
                        'Keep the letter: y'
                    ],
                    answer: '7y'
                }
            ],
            
            tips: [
                '✅ Always keep the letter - it doesn\'t change!',
                '✅ Just add the numbers - ignore the letters when adding',
                '⚠️ Don\'t forget the letter: 4x + 3x = 7x (not 7)',
                '⚠️ Don\'t multiply: 2y + 3y = 5y (not 6y)'
            ]
        },
        
        'intermediate': {
            title: 'Substitution (One Variable)',
            introduction: 'In this level, you\'ll learn <strong>substitution</strong> - finding the value of expressions when you know what x equals.',
            
            principles: [
                {
                    title: 'What is Substitution?',
                    content: '<strong>Substitution</strong> means replacing a letter with its number value.<br>Example: If x = 5, then x + 3 means 5 + 3 = 8'
                },
                {
                    title: 'Use Brackets!',
                    content: 'Always use brackets when substituting.<br>If x = 4, write 3(4) not 34'
                }
            ],
            
            examples: [
                {
                    question: 'If x = 4, find the value of x + 7',
                    steps: [
                        'Write the expression: x + 7',
                        'Replace x with 4: (4) + 7',
                        'Calculate: 4 + 7'
                    ],
                    answer: '11'
                },
                {
                    question: 'If x = 5, find the value of 2x',
                    steps: [
                        'Write the expression: 2x (means 2 times x)',
                        'Replace x with 5 (use brackets!): 2(5)',
                        'Calculate: 2 × 5'
                    ],
                    answer: '10'
                }
            ],
            
            tips: [
                '✅ Always use brackets when substituting',
                '✅ Remember 2x means 2 × x (multiply!)',
                '✅ Follow BOMDAS - multiply before adding',
                '⚠️ Don\'t just stick numbers together: 3x when x=4 is 12, not 34'
            ]
        },
        
        'advanced': {
            title: 'Substitution (Two Variables)',
            introduction: 'In this level, you\'ll substitute <strong>two different variables</strong> (like x and y) in the same expression.',
            
            principles: [
                {
                    title: 'Multiple Variables',
                    content: 'Each letter can represent a different number!<br>Example: If x = 3 and y = 5, then x + y means 3 + 5 = 8'
                },
                {
                    title: 'Multiply First',
                    content: 'When you see 2x or 3y, multiply BEFORE adding/subtracting (BOMDAS!)'
                }
            ],
            
            examples: [
                {
                    question: 'If x = 4 and y = 3, find x + y',
                    steps: [
                        'Write: x + y',
                        'Replace both letters: (4) + (3)',
                        'Calculate: 4 + 3'
                    ],
                    answer: '7'
                },
                {
                    question: 'If x = 5 and y = 4, find 2x + y',
                    steps: [
                        'Write: 2x + y',
                        'Replace: 2(5) + (4)',
                        'Multiply first: 10 + 4',
                        'Then add: 14'
                    ],
                    answer: '14'
                }
            ],
            
            tips: [
                '✅ Keep track of which value goes with which letter',
                '✅ Use brackets for both variables',
                '✅ Multiply before you add/subtract (BOMDAS!)',
                '⚠️ Don\'t mix up the values: x=4, y=3 means x+y = 4+3, not 3+4... well, same answer, but you get the idea!'
            ]
        }
    },
    
    // ============================================
    // SOLVING EQUATIONS
    // ============================================
    'solving_equations': {
        'beginner': {
            title: 'One-Step Equations',
            introduction: 'Learn to solve <strong>one-step equations</strong> like x + 5 = 12. You\'ll discover how to "undo" addition to find the value of x.',
            
            principles: [
                {
                    title: 'What is an Equation?',
                    content: 'An <strong>equation</strong> is like a balance scale - both sides must be equal.<br>Example: x + 3 = 10 means "something plus 3 equals 10"<br>Our job is to find what that "something" (x) is!'
                },
                {
                    title: 'The Golden Rule',
                    content: '<strong>Whatever you do to one side, do to the other!</strong><br>Think of it like a seesaw - if you take weight off one side, you must take the same weight off the other side to keep it balanced.'
                },
                {
                    title: 'Undoing Addition',
                    content: 'To solve x + 3 = 10, we need to <strong>undo</strong> the +3<br>• Addition is undone by subtraction<br>• Subtract 3 from BOTH sides<br>• x + 3 - 3 = 10 - 3<br>• x = 7'
                }
            ],
            
            examples: [
                {
                    question: 'Solve: x + 3 = 10',
                    steps: [
                        'We need to get x by itself (isolate x)',
                        'The +3 is attached to x, so we undo it',
                        'Subtract 3 from BOTH sides: x + 3 - 3 = 10 - 3',
                        'Left side: x + 3 - 3 = x (the 3s cancel out!)',
                        'Right side: 10 - 3 = 7',
                        'Therefore: x = 7'
                    ],
                    answer: 'x = 7'
                },
                {
                    question: 'Solve: x + 9 = 29',
                    steps: [
                        'We need to remove the +9 to isolate x',
                        'Subtract 9 from BOTH sides: x + 9 - 9 = 29 - 9',
                        'Left side: x + 9 - 9 = x',
                        'Right side: 29 - 9 = 20',
                        'Therefore: x = 20'
                    ],
                    answer: 'x = 20'
                },
                {
                    question: 'Solve: x + 14 = 18',
                    steps: [
                        'Subtract 14 from BOTH sides: x + 14 - 14 = 18 - 14',
                        'Left side simplifies to: x',
                        'Right side: 18 - 14 = 4',
                        'Therefore: x = 4'
                    ],
                    answer: 'x = 4'
                }
            ],
            
            tips: [
                '✅ Always do the SAME thing to both sides of the equation',
                '✅ Check your answer by substituting back: if x = 7, does 7 + 3 = 10? Yes! ✓',
                '✅ Think: "What number + [this number] = [that number]?"',
                '⚠️ Don\'t just subtract from the right side - do BOTH sides!',
                '⚠️ Remember to actually subtract - don\'t just remove the number'
            ]
        },
        
        'intermediate': {
            title: 'Two-Step Equations',
            introduction: 'Master <strong>two-step equations</strong> like 2x + 4 = 18. These need TWO operations to solve - but don\'t worry, we\'ll take it step by step!',
            
            principles: [
                {
                    title: 'Two Steps to Freedom!',
                    content: 'In 2x + 4 = 18, x is trapped by TWO operations:<br>1. It\'s being <strong>multiplied</strong> by 2<br>2. Then 4 is being <strong>added</strong><br><br>We need to undo BOTH operations to free x!'
                },
                {
                    title: 'Order Matters - Work Backwards!',
                    content: 'Use <strong>reverse BOMDAS</strong>:<br>• Addition/Subtraction was done LAST, so undo it FIRST<br>• Multiplication/Division was done FIRST, so undo it LAST<br><br>Think of getting dressed: you put socks on first, then shoes. To undress, you take shoes off FIRST, then socks!'
                },
                {
                    title: 'The Two-Step Process',
                    content: '<strong>Step 1:</strong> Undo addition/subtraction (get 2x = something)<br><strong>Step 2:</strong> Undo multiplication/division (get x = something)'
                }
            ],
            
            examples: [
                {
                    question: 'Solve: 2x + 4 = 18',
                    steps: [
                        '<strong>STEP 1 - Remove the +4:</strong>',
                        'Subtract 4 from both sides: 2x + 4 - 4 = 18 - 4',
                        'Simplifies to: 2x = 14',
                        '',
                        '<strong>STEP 2 - Remove the ×2:</strong>',
                        'Divide both sides by 2: 2x ÷ 2 = 14 ÷ 2',
                        'Simplifies to: x = 7',
                        '',
                        '<strong>CHECK:</strong> Does 2(7) + 4 = 18? → 14 + 4 = 18 ✓'
                    ],
                    answer: 'x = 7'
                },
                {
                    question: 'Solve: 6x + 6 = 72',
                    steps: [
                        '<strong>STEP 1 - Remove the +6:</strong>',
                        'Subtract 6 from both sides: 6x + 6 - 6 = 72 - 6',
                        'Simplifies to: 6x = 66',
                        '',
                        '<strong>STEP 2 - Remove the ×6:</strong>',
                        'Divide both sides by 6: 6x ÷ 6 = 66 ÷ 6',
                        'Simplifies to: x = 11',
                        '',
                        '<strong>CHECK:</strong> Does 6(11) + 6 = 72? → 66 + 6 = 72 ✓'
                    ],
                    answer: 'x = 11'
                },
                {
                    question: 'Solve: 4x + 1 = 45',
                    steps: [
                        '<strong>STEP 1:</strong> Subtract 1 from both sides',
                        '4x = 44',
                        '',
                        '<strong>STEP 2:</strong> Divide both sides by 4',
                        'x = 11',
                        '',
                        '<strong>CHECK:</strong> 4(11) + 1 = 44 + 1 = 45 ✓'
                    ],
                    answer: 'x = 11'
                }
            ],
            
            tips: [
                '✅ ALWAYS do addition/subtraction FIRST, multiplication/division SECOND',
                '✅ Write out each step clearly - rushing causes mistakes!',
                '✅ Check your answer by substituting back into the original equation',
                '⚠️ Don\'t divide before subtracting - order matters!',
                '⚠️ Remember: "Undo" means do the opposite operation'
            ]
        },
        
        'advanced': {
            title: 'Equations with Brackets',
            introduction: 'Tackle <strong>equations with brackets</strong> like 2(x + 3) = 14. You\'ll learn to expand brackets first, then solve the resulting two-step equation.',
            
            principles: [
                {
                    title: 'Brackets First - Always!',
                    content: 'When you see brackets like 2(x + 3), you MUST expand them first.<br><strong>Expanding</strong> means multiplying everything inside the bracket by the number outside.<br>2(x + 3) becomes 2×x + 2×3 = 2x + 6'
                },
                {
                    title: 'The Three-Step Process',
                    content: '<strong>Step 1:</strong> Expand the brackets (multiply out)<br><strong>Step 2:</strong> Subtract/add to isolate the x term<br><strong>Step 3:</strong> Divide/multiply to find x'
                },
                {
                    title: 'Expanding Brackets',
                    content: 'Multiply the number OUTSIDE by EVERY term inside:<br>• 2(x + 3) = 2×x + 2×3 = 2x + 6<br>• 5(x + 2) = 5×x + 5×2 = 5x + 10<br>• 4(x + 1) = 4×x + 4×1 = 4x + 4'
                }
            ],
            
            examples: [
                {
                    question: 'Solve: 2(x + 3) = 14',
                    steps: [
                        '<strong>STEP 1 - Expand the brackets:</strong>',
                        'Multiply 2 by everything inside: 2×x + 2×3',
                        'This gives us: 2x + 6 = 14',
                        '',
                        '<strong>STEP 2 - Remove the +6:</strong>',
                        'Subtract 6 from both sides: 2x + 6 - 6 = 14 - 6',
                        'Simplifies to: 2x = 8',
                        '',
                        '<strong>STEP 3 - Remove the ×2:</strong>',
                        'Divide both sides by 2: 2x ÷ 2 = 8 ÷ 2',
                        'Therefore: x = 4',
                        '',
                        '<strong>CHECK:</strong> Does 2(4 + 3) = 14? → 2(7) = 14 ✓'
                    ],
                    answer: 'x = 4'
                },
                {
                    question: 'Solve: 5(x + 2) = 20',
                    steps: [
                        '<strong>STEP 1 - Expand brackets:</strong>',
                        '5×x + 5×2 = 5x + 10',
                        'Equation becomes: 5x + 10 = 20',
                        '',
                        '<strong>STEP 2 - Subtract 10:</strong>',
                        '5x + 10 - 10 = 20 - 10',
                        '5x = 10',
                        '',
                        '<strong>STEP 3 - Divide by 5:</strong>',
                        'x = 2',
                        '',
                        '<strong>CHECK:</strong> 5(2 + 2) = 5(4) = 20 ✓'
                    ],
                    answer: 'x = 2'
                },
                {
                    question: 'Solve: 4(x + 1) = 32',
                    steps: [
                        '<strong>STEP 1:</strong> Expand: 4x + 4 = 32',
                        '',
                        '<strong>STEP 2:</strong> Subtract 4: 4x = 28',
                        '',
                        '<strong>STEP 3:</strong> Divide by 4: x = 7',
                        '',
                        '<strong>CHECK:</strong> 4(7 + 1) = 4(8) = 32 ✓'
                    ],
                    answer: 'x = 7'
                }
            ],
            
            tips: [
                '✅ ALWAYS expand brackets FIRST - this is the most important step!',
                '✅ Multiply the outside number by EVERY term inside the brackets',
                '✅ After expanding, you have a two-step equation - follow the two-step process',
                '✅ Check by substituting your answer back into the ORIGINAL equation (with brackets)',
                '⚠️ Don\'t forget to multiply the number outside by BOTH terms inside',
                '⚠️ Common mistake: 2(x + 3) ≠ 2x + 3 (you must multiply the 3 too!)'
            ]
        }
    },
    
    // ============================================
    // 3. SIMPLIFYING EXPRESSIONS  
    // ============================================
    'simplifying_expressions': {
        'beginner': {
            title: 'Collecting Like Terms',
            introduction: 'Learn to <strong>combine like terms</strong> by adding terms with the same variable: 6x + 9x = 15x',
            principles: [
                {title: 'Like Terms', content: 'Terms with the same letter can be combined. 6x and 9x are like terms.'},
                {title: 'How to Combine', content: 'Add the numbers, keep the letter: 6x + 9x = 15x'}
            ],
            examples: [
                {question: 'Simplify: 6x + 9x', steps: ['Both have x','Add: 6 + 9 = 15', 'Keep x'], answer: '15x'},
                {question: 'Simplify: 5x + 5x', steps: ['Add: 5 + 5 = 10'], answer: '10x'}
            ],
            tips: ['✅ Only combine same letters', '⚠️ Keep the letter in answer']
        },
        'intermediate': {
            title: 'Variables and Constants',
            introduction: 'Simplify expressions with <strong>both variables and numbers</strong>: 5x + 4 + 2x + 2',
            principles: [
                {title: 'Two Types', content: 'Variable terms (5x) and constants (4). Collect each separately.'}
            ],
            examples: [
                {question: '5x + 4 + 2x + 2', steps: ['x terms: 5x + 2x = 7x', 'Constants: 4 + 2 = 6'], answer: '7x + 6'}
            ],
            tips: ['✅ Keep variables and numbers separate']
        },
        'advanced': {
            title: 'Expressions with Powers',
            introduction: 'Simplify expressions with <strong>x²</strong> terms: 4x² + 7x + 2x²',
            principles: [
                {title: 'Different Powers', content: 'x² and x are different! Combine x² with x², x with x.'}
            ],
            examples: [
                {question: '4x² + 7x + 2x² + 1x', steps: ['x²: 4x² + 2x² = 6x²', 'x: 7x + 1x = 8x'], answer: '6x² + 8x'}
            ],
            tips: ['✅ x² and x are NOT the same', '✅ Write highest power first']
        }
    },
    
    // ============================================
    // 4. EXPANDING & FACTORISING
    // ============================================
    'expanding_factorising': {
        'beginner': {
            title: 'Expanding Brackets',
            introduction: 'Multiply everything inside by the outside number: 6(x + 9) = 6x + 54',
            principles: [
                {title: 'Distribution', content: 'Multiply outside number by EACH term inside'}
            ],
            examples: [
                {question: '6(x + 9)', steps: ['6 × x = 6x', '6 × 9 = 54'], answer: '6x + 54'}
            ],
            tips: ['✅ Multiply ALL terms inside']
        },
        'intermediate': {
            title: 'Factorising',
            introduction: 'Find common factor and put outside brackets: 8x + 80 = 8(x + 10)',
            principles: [
                {title: 'Common Factor', content: 'Find biggest number that divides both terms'}
            ],
            examples: [
                {question: '8x + 80', steps: ['Common factor: 8', '8x ÷ 8 = x', '80 ÷ 8 = 10'], answer: '8(x + 10)'}
            ],
            tips: ['✅ Check by expanding back']
        },
        'advanced': {
            title: 'Double Brackets (FOIL)',
            introduction: 'Expand using FOIL method: (x + 1)(x + 4) = x² + 5x + 4',
            principles: [
                {title: 'FOIL', content: 'First, Outer, Inner, Last - multiply all combinations'}
            ],
            examples: [
                {question: '(x + 1)(x + 4)', steps: ['F: x×x = x²', 'O: x×4 = 4x', 'I: 1×x = 1x', 'L: 1×4 = 4', 'Combine: x² + 5x + 4'], answer: 'x² + 5x + 4'}
            ],
            tips: ['✅ Combine middle terms']
        }
    },
    
    // ============================================
    // 5. FUNCTIONS
    // ============================================
    'functions': {
        'beginner': {
            title: 'Function Notation',
            introduction: 'Learn what f(x) means. If f(x) = x + 5, find f(3).',
            principles: [
                {title: 'Functions', content: 'f(x) is a rule. f(3) means substitute 3 for x'}
            ],
            examples: [
                {question: 'f(x) = x + 5, find f(3)', steps: ['Replace x with 3', 'f(3) = 3 + 5 = 8'], answer: '8'}
            ],
            tips: ['✅ Replace ALL x with the number']
        },
        'intermediate': {
            title: 'Evaluating Functions',
            introduction: 'Evaluate functions with multiplication: f(x) = 2x + 3',
            principles: [
                {title: 'BOMDAS', content: 'Multiply before adding'}
            ],
            examples: [
                {question: 'f(x) = 2x + 3, find f(4)', steps: ['f(4) = 2(4) + 3', '= 8 + 3 = 11'], answer: '11'}
            ],
            tips: ['✅ Use brackets when substituting']
        },
        'advanced': {
            title: 'Complex Functions',
            introduction: 'Functions with powers: f(x) = x² + 2x - 3',
            principles: [
                {title: 'Multiple Terms', content: 'Calculate each term separately'}
            ],
            examples: [
                {question: 'f(x) = x² + 2x - 3, find f(-1)', steps: ['f(-1) = (-1)² + 2(-1) - 3', '= 1 - 2 - 3 = -4'], answer: '-4'}
            ],
            tips: ['✅ Use brackets for negative numbers']
        }
    },
    
    // ============================================
    // 6. PATTERNS
    // ============================================
    'patterns': {
        'beginner': {
            title: 'Visual Patterns',
            introduction: 'Identify and continue patterns: 🌟 🌙 🌟 🌙 ?',
            principles: [
                {title: 'Repeating Patterns', content: 'Look for what repeats'}
            ],
            examples: [
                {question: '🌟 🌙 🌟 🌙 ?', steps: ['Pattern alternates', 'After 🌙 comes 🌟'], answer: '🌟'}
            ],
            tips: ['✅ Look for repeats']
        },
        'intermediate': {
            title: 'Number Sequences',
            introduction: 'Find the pattern in number sequences: 3, 7, 11, 15...',
            principles: [
                {title: 'Common Difference', content: 'What do you add each time?'}
            ],
            examples: [
                {question: '3, 7, 11, 15, ?', steps: ['Difference: +4 each time', '15 + 4 = 19'], answer: '19'}
            ],
            tips: ['✅ Check the difference between terms']
        },
        'advanced': {
            title: 'nth Term Formula',
            introduction: 'Find patterns in special sequences: 1, 4, 9, 16...',
            principles: [
                {title: 'Special Sequences', content: 'Square numbers: 1², 2², 3², 4²...'}
            ],
            examples: [
                {question: '1, 4, 9, 16, ?', steps: ['These are squares', '1², 2², 3², 4², 5²', 'Next: 5² = 25'], answer: '25'}
            ],
            tips: ['✅ Look for squares, doubles, triangular numbers']
        }
    },
    
    // ============================================
    // 7. ARITHMETIC
    // ============================================
    'arithmetic': {
        'beginner': {
            title: 'Basic Addition',
            introduction: 'Master basic addition: 8 + 4 = 12',
            principles: [
                {title: 'Adding', content: 'Count forward from the first number'}
            ],
            examples: [
                {question: '8 + 4', steps: ['Start at 8', 'Count forward 4: 9, 10, 11, 12'], answer: '12'}
            ],
            tips: ['✅ Count carefully']
        },
        'intermediate': {
            title: 'Adding Negative Numbers',
            introduction: 'Add positive and negative: -7 + 14',
            principles: [
                {title: 'Negatives', content: 'Adding negative = subtracting'}
            ],
            examples: [
                {question: '-7 + 14', steps: ['14 - 7 = 7'], answer: '7'}
            ],
            tips: ['✅ Think of it as subtraction']
        },
        'advanced': {
            title: 'Adding Two Negatives',
            introduction: 'Add two negative numbers: (-5) + (-12)',
            principles: [
                {title: 'Two Negatives', content: 'Result gets more negative'}
            ],
            examples: [
                {question: '(-5) + (-12)', steps: ['Add magnitudes: 5 + 12 = 17', 'Make negative: -17'], answer: '-17'}
            ],
            tips: ['✅ Both negative = more negative result']
        }
    },
    
    // ============================================
    // 8. BODMAS
    // ============================================
    'bodmas': {
        'beginner': {
            title: 'Order of Operations Basics',
            introduction: 'Learn BODMAS: Brackets, Order, Multiply/Divide, Add/Subtract',
            principles: [
                {title: 'BODMAS', content: 'Multiply before you add'}
            ],
            examples: [
                {question: '5 + 3 × 2', steps: ['Multiply first: 3 × 2 = 6', 'Then add: 5 + 6 = 11'], answer: '11'}
            ],
            tips: ['✅ Always multiply/divide before add/subtract']
        },
        'intermediate': {
            title: 'Multiple Operations',
            introduction: 'Handle complex expressions: 20 - 4 × 3 + 2',
            principles: [
                {title: 'Order Matters', content: 'Follow BODMAS strictly'}
            ],
            examples: [
                {question: '20 - 4 × 3 + 2', steps: ['Multiply: 4 × 3 = 12', '20 - 12 + 2', 'Left to right: 10'], answer: '10'}
            ],
            tips: ['✅ Multiplication first']
        },
        'advanced': {
            title: 'With Powers',
            introduction: 'BODMAS with indices: 3 + 2² × 5',
            principles: [
                {title: 'Powers First', content: 'After brackets, do powers (Order)'}
            ],
            examples: [
                {question: '3 + 2² × 5', steps: ['Power: 2² = 4', 'Multiply: 4 × 5 = 20', 'Add: 3 + 20 = 23'], answer: '23'}
            ],
            tips: ['✅ Powers before multiplication']
        }
    },
    
    // ============================================
    // 9. FRACTIONS
    // ============================================
    'fractions': {
        'beginner': {
            title: 'Adding Fractions',
            introduction: 'Add fractions with same denominator: 1/4 + 1/4',
            principles: [
                {title: 'Same Denominator', content: 'Add numerators, keep denominator'}
            ],
            examples: [
                {question: '1/4 + 1/4', steps: ['Add tops: 1 + 1 = 2', 'Keep bottom: 4', 'Result: 2/4 = 1/2'], answer: '1/2'}
            ],
            tips: ['✅ Simplify answer']
        },
        'intermediate': {
            title: 'Multiplying Fractions',
            introduction: 'Multiply fractions: 2/3 × 3/4',
            principles: [
                {title: 'Multiply Across', content: 'Top × top, bottom × bottom'}
            ],
            examples: [
                {question: '2/3 × 3/4', steps: ['2 × 3 = 6', '3 × 4 = 12', '6/12 = 1/2'], answer: '1/2'}
            ],
            tips: ['✅ Simplify final answer']
        },
        'advanced': {
            title: 'Complex Fraction Operations',
            introduction: 'Combine operations with fractions',
            principles: [
                {title: 'BODMAS with Fractions', content: 'Follow operation order'}
            ],
            examples: [
                {question: '(2/3 + 1/4) × 3/5', steps: ['Brackets first: 2/3 + 1/4 = 11/12', '11/12 × 3/5 = 11/20'], answer: '11/20'}
            ],
            tips: ['✅ Brackets first']
        }
    },
    
    // ============================================
    // 10. DECIMALS
    // ============================================
    'decimals': {
        'beginner': {
            title: 'Adding Decimals',
            introduction: 'Add decimal numbers: 4.5 + 1.0',
            principles: [
                {title: 'Line Up Points', content: 'Decimal points must line up vertically'}
            ],
            examples: [
                {question: '4.5 + 1.0', steps: ['Line up: 4.5', '       + 1.0', '       = 5.5'], answer: '5.5'}
            ],
            tips: ['✅ Always line up decimal points']
        },
        'intermediate': {
            title: 'Multiplying Decimals',
            introduction: 'Multiply decimals by whole numbers: 4.9 × 6',
            principles: [
                {title: 'Multiply Normally', content: 'Then place decimal point'}
            ],
            examples: [
                {question: '4.9 × 6', steps: ['49 × 6 = 294', 'One decimal place: 29.4'], answer: '29.4'}
            ],
            tips: ['✅ Count decimal places']
        },
        'advanced': {
            title: 'Decimal × Decimal',
            introduction: 'Multiply two decimals: 6.0 × 0.8',
            principles: [
                {title: 'Count Places', content: 'Total decimal places in answer'}
            ],
            examples: [
                {question: '6.0 × 0.8', steps: ['60 × 8 = 480', 'Two places total: 4.80 = 4.8'], answer: '4.8'}
            ],
            tips: ['✅ Add up all decimal places']
        }
    },
    
    // ============================================
    // 11. MULTIPLICATION & DIVISION
    // ============================================
    'multiplication_division': {
        'beginner': {
            title: 'Basic Multiplication',
            introduction: 'Master times tables: 2 × 5 = 10',
            principles: [
                {title: 'Multiplication', content: 'Repeated addition'}
            ],
            examples: [
                {question: '2 × 5', steps: ['2 + 2 + 2 + 2 + 2 = 10'], answer: '10'}
            ],
            tips: ['✅ Learn times tables']
        },
        'intermediate': {
            title: 'Negative Number Rules',
            introduction: 'Multiply and divide with negatives',
            principles: [
                {title: 'Sign Rules', content: 'Positive × Negative = Negative<br>Negative × Negative = Positive'}
            ],
            examples: [
                {question: '-4 × 5', steps: ['Different signs = negative', 'Answer: -20'], answer: '-20'}
            ],
            tips: ['✅ Remember sign rules']
        },
        'advanced': {
            title: 'Two Negatives',
            introduction: 'Multiply two negative numbers',
            principles: [
                {title: 'Negative × Negative', content: 'Always gives positive'}
            ],
            examples: [
                {question: '(-17) × (-18)', steps: ['17 × 18 = 306', 'Both negative = positive'], answer: '306'}
            ],
            tips: ['✅ Negative × Negative = Positive']
        }
    },
    
    // ============================================
    // 12. NUMBER SYSTEMS
    // ============================================
    'number_systems': {
        'beginner': {
            title: 'Natural Numbers',
            introduction: 'Learn about natural numbers: 1, 2, 3, 4...',
            principles: [
                {title: 'Natural Numbers', content: 'Counting numbers starting from 1'}
            ],
            examples: [
                {question: 'Smallest natural number?', steps: ['Natural numbers: 1, 2, 3...', 'Smallest is 1'], answer: '1'}
            ],
            tips: ['✅ Start from 1']
        },
        'intermediate': {
            title: 'Integers and Operations',
            introduction: 'Work with positive and negative integers',
            principles: [
                {title: 'Integers', content: 'Include negative numbers, zero, positives'}
            ],
            examples: [
                {question: 'What is -8 + (-5)?', steps: ['Both negative', 'Add magnitudes: 8 + 5 = 13', 'Make negative: -13'], answer: '-13'}
            ],
            tips: ['✅ Watch signs carefully']
        },
        'advanced': {
            title: 'Temperature Problems',
            introduction: 'Apply integers to real situations',
            principles: [
                {title: 'Real Applications', content: 'Temperature can go below zero'}
            ],
            examples: [
                {question: '3° colder than -5°C?', steps: ['-5 - 3 = -8'], answer: '-8°C'}
            ],
            tips: ['✅ Colder = subtract']
        }
    },
    
    // ============================================
    // 13. SURDS
    // ============================================
    'surds': {
        'beginner': {
            title: 'Multiplying Surds',
            introduction: 'Multiply square roots: √7 × √5',
            principles: [
                {title: 'Multiplication', content: '√a × √b = √(a×b)'}
            ],
            examples: [
                {question: '√7 × √5', steps: ['√7 × √5 = √(7×5)', '= √35'], answer: '√35'}
            ],
            tips: ['✅ Multiply under the root']
        },
        'intermediate': {
            title: 'Surds with Coefficients',
            introduction: 'Multiply surds with numbers: 3√2 × 2√2',
            principles: [
                {title: 'Multiply Separately', content: 'Numbers together, surds together'}
            ],
            examples: [
                {question: '3√2 × 2√2', steps: ['3 × 2 = 6', '√2 × √2 = 2', '6 × 2 = 12'], answer: '12'}
            ],
            tips: ['✅ √2 × √2 = 2']
        },
        'advanced': {
            title: 'Expanding with Surds',
            introduction: 'Use FOIL with surds: (3 + √2)(5 + √2)',
            principles: [
                {title: 'FOIL Method', content: 'Multiply all combinations'}
            ],
            examples: [
                {question: '(3 + √2)(5 + √2)', steps: ['F: 3×5 = 15', 'O: 3×√2 = 3√2', 'I: √2×5 = 5√2', 'L: √2×√2 = 2', 'Sum: 17 + 8√2'], answer: '17 + 8√2'}
            ],
            tips: ['✅ Remember √2 × √2 = 2']
        }
    },
    
    // ============================================
    // 14. COMPLEX NUMBERS INTRO
    // ============================================
    'complex_numbers_intro': {
        'beginner': {
            title: 'Imaginary Unit',
            introduction: 'Meet i, the imaginary unit: i = √(-1)',
            principles: [
                {title: 'Definition', content: 'i is defined as √(-1)<br>i² = -1'}
            ],
            examples: [
                {question: 'What is i²?', steps: ['By definition', 'i² = -1'], answer: '-1'}
            ],
            tips: ['✅ i² always equals -1']
        },
        'intermediate': {
            title: 'Adding Complex Numbers',
            introduction: 'Add complex numbers: (2 + 3i) + (4 + 5i)',
            principles: [
                {title: 'Add Parts', content: 'Add real parts, add imaginary parts separately'}
            ],
            examples: [
                {question: '(2 + 3i) + (4 + 5i)', steps: ['Real: 2 + 4 = 6', 'Imaginary: 3i + 5i = 8i'], answer: '6 + 8i'}
            ],
            tips: ['✅ Keep real and imaginary separate']
        },
        'advanced': {
            title: 'Dividing Complex Numbers',
            introduction: 'Divide complex numbers',
            principles: [
                {title: 'Simplification', content: 'Divide real and imaginary parts'}
            ],
            examples: [
                {question: '(6 + 3i) ÷ 3', steps: ['6/3 = 2', '3i/3 = i'], answer: '2 + i'}
            ],
            tips: ['✅ Divide each part']
        }
    },
    
    // ============================================
    // 15. COMPLEX NUMBERS EXPANDED
    // ============================================
    'complex_numbers_expanded': {
        'beginner': {
            title: 'Argand Diagram',
            introduction: 'Plot complex numbers on Argand diagram',
            principles: [
                {title: 'Axes', content: 'Horizontal = real, Vertical = imaginary'}
            ],
            examples: [
                {question: 'Which axis is real?', steps: ['Real = horizontal (x-axis)'], answer: 'x-axis'}
            ],
            tips: ['✅ x = real, y = imaginary']
        },
        'intermediate': {
            title: 'Multiplication by i',
            introduction: 'Understand i × (complex number)',
            principles: [
                {title: 'Rotation', content: 'Multiplying by i rotates 90° counterclockwise'}
            ],
            examples: [
                {question: 'i × (1 + 0i)', steps: ['i × 1 = i'], answer: 'i'}
            ],
            tips: ['✅ i rotates 90°']
        },
        'advanced': {
            title: 'Conjugates',
            introduction: 'Find conjugate of complex numbers',
            principles: [
                {title: 'Conjugate', content: 'Change sign of imaginary part'}
            ],
            examples: [
                {question: 'Conjugate of 4 + 7i?', steps: ['Change imaginary sign', '4 - 7i'], answer: '4 - 7i'}
            ],
            tips: ['✅ Flip imaginary sign only']
        }
    },
    
    // ============================================
    // 16. DESCRIPTIVE STATISTICS
    // ============================================
    'descriptive_statistics': {
        'beginner': {
            title: '📊 Levels 1-3: Reading Data & Basic Measures',
            introduction: 'Learn to read charts and find mode/range from data',
            principles: [
                {title: 'Mode', content: 'The value that appears most often'},
                {title: 'Range', content: 'Range = Maximum - Minimum'},
                {title: 'Reading Charts', content: 'Pictograms, tally charts, and bar charts show data visually'}
            ],
            examples: [
                {question: 'Mode of: 3, 5, 7, 5, 8, 5, 2', steps: ['Count each value:', '3→1, 5→3, 7→1, 8→1, 2→1', '5 appears most (3 times)'], answer: 'Mode = 5'},
                {question: 'Range of: 4, 9, 2, 7, 5', steps: ['Maximum = 9', 'Minimum = 2', 'Range = 9 - 2 = 7'], answer: 'Range = 7'}
            ],
            tips: ['✅ Mode = most frequent', '✅ Range = highest minus lowest']
        },
        'intermediate': {
            title: '📊 Levels 4-8: Median, Mean & Frequency Tables',
            introduction: 'Calculate median, mean, and use frequency tables',
            principles: [
                {title: 'Median (Odd)', content: 'Middle value when data is ordered'},
                {title: 'Median (Even)', content: 'Average of the two middle values'},
                {title: 'Mean', content: 'Mean = Sum of values ÷ Number of values'},
                {title: 'Mean from Freq Table', content: 'Mean = Σ(f × x) ÷ Σf'}
            ],
            examples: [
                {question: 'Median of: 4, 7, 2, 9, 5', steps: ['Order: 2, 4, 5, 7, 9', '5 values → middle is 3rd', 'Median = 5'], answer: '5'},
                {question: 'Mean of: 6, 4, 8, 10, 7', steps: ['Sum = 6+4+8+10+7 = 35', 'Count = 5', 'Mean = 35÷5 = 7'], answer: '7'},
                {question: 'Mean from table (val:freq) 1:3, 2:5, 3:2', steps: ['Σfx = 3+10+6 = 19', 'Σf = 10', 'Mean = 1.9'], answer: '1.9'}
            ],
            tips: ['✅ Always order data first for median', '✅ For frequency tables: multiply value × frequency']
        },
        'advanced': {
            title: '📊 Levels 9-12: Histograms, Stem-and-Leaf & Comparisons',
            introduction: 'Interpret grouped data and compare distributions',
            principles: [
                {title: 'Histogram', content: 'Bars touch, shows grouped/continuous data'},
                {title: 'Modal Class', content: 'The interval with highest frequency'},
                {title: 'Stem-and-Leaf', content: 'Key shows how to read: 4|3 means 43'},
                {title: 'Which Average?', content: 'Median better when outliers present'}
            ],
            examples: [
                {question: 'Find median interval (30 items, groups 0-10:8, 10-20:12, 20-30:7, 30-40:3)', steps: ['Position = (30+1)/2 = 15.5th', 'Cumulative: 8, 20, 27, 30', '15.5th is in 10-20 (positions 9-20)'], answer: '10-20'},
                {question: 'Stem-leaf: 3|2 5 7, 4|1 4 → Find range', steps: ['Smallest = 32', 'Largest = 44', 'Range = 44-32 = 12'], answer: '12'},
                {question: 'Salaries €30k, €32k, €35k, €200k - best average?', steps: ['Mean = €74k (pulled up by outlier)', 'Median = €33.5k (typical value)'], answer: 'Median'}
            ],
            tips: ['✅ Count leaves to find n in stem-leaf', '✅ Median resists outliers', '✅ Modal class = tallest histogram bar']
        }
    },
    
    // ============================================
    // 17. PROBABILITY
    // ============================================
    'probability': {
        'beginner': {
            title: 'Simple Probability',
            introduction: 'Calculate basic probabilities: coin flips, dice',
            principles: [
                {title: 'Probability', content: 'P = favorable outcomes / total outcomes'}
            ],
            examples: [
                {question: 'P(heads on coin flip)?', steps: ['Favorable: 1 (heads)', 'Total: 2 (heads or tails)', 'P = 1/2'], answer: '1/2'}
            ],
            tips: ['✅ Count carefully']
        },
        'intermediate': {
            title: 'Compound Probability',
            introduction: 'Two or more events: multiply probabilities',
            principles: [
                {title: 'AND Rule', content: 'P(A and B) = P(A) × P(B)'}
            ],
            examples: [
                {question: 'Two heads in a row?', steps: ['P(H) = 1/2', 'P(H and H) = 1/2 × 1/2 = 1/4'], answer: '1/4'}
            ],
            tips: ['✅ Multiply for "and"']
        },
        'advanced': {
            title: 'Conditional Probability',
            introduction: 'Probability that depends on previous events',
            principles: [
                {title: 'Without Replacement', content: 'Probability changes after first draw'}
            ],
            examples: [
                {question: 'Two aces without replacement', steps: ['P(1st ace) = 4/52', 'P(2nd ace) = 3/51', 'P(both) = 4/52 × 3/51 = 1/221'], answer: '1/221'}
            ],
            tips: ['✅ Update probabilities after each event']
        }
    },
    
    // ============================================
    // 18. SETS
    // ============================================
    'sets': {
        'beginner': {
            title: 'Union and Intersection',
            introduction: 'Combine sets or find common elements',
            principles: [
                {title: 'Union (∪)', content: 'All elements from both sets'},
                {title: 'Intersection (∩)', content: 'Only common elements'}
            ],
            examples: [
                {question: '{1,2,3} ∪ {3,4,5}?', steps: ['Combine all', 'Remove duplicates'], answer: '{1,2,3,4,5}'},
                {question: '{1,2,3} ∩ {3,4,5}?', steps: ['Only common'], answer: '{3}'}
            ],
            tips: ['✅ Union = all, Intersection = common']
        },
        'intermediate': {
            title: 'Set Difference',
            introduction: 'Elements in A but not in B: A - B',
            principles: [
                {title: 'Difference', content: 'In first set but not second'}
            ],
            examples: [
                {question: 'A={1,2,3,4}, B={3,4,5,6}, A-B?', steps: ['In A: 1,2,3,4', 'Remove what is in B: remove 3,4'], answer: '{1,2}'}
            ],
            tips: ['✅ Start with first set, remove second']
        },
        'advanced': {
            title: 'Cardinality Formulas',
            introduction: 'Count elements using formulas',
            principles: [
                {title: 'Formula', content: '|A ∪ B| = |A| + |B| - |A ∩ B|'}
            ],
            examples: [
                {question: '|A|=5, |B|=7, |A∩B|=3, |A∪B|?', steps: ['5 + 7 - 3 = 9'], answer: '9'}
            ],
            tips: ['✅ Subtract intersection to avoid double counting']
        }
    },
    
    // FUTURE TOPICS - Just add them here following the same structure:
    /*
    'patterns': {
        'beginner': { ... },
        'intermediate': { ... },
        'advanced': { ... }
    },
    'functions': {
        'beginner': { ... },
        'intermediate': { ... },
        'advanced': { ... }
    }
    */
    
    // Linear Inequalities Tutorial Content
    'linear_inequalities': {
        'beginner': {
            title: 'Understanding Inequality Symbols',
            introduction: 'In this level, you\'ll learn the <strong>inequality symbols</strong> (<, >, ≤, ≥) and what they mean. These symbols compare values and show which is larger or smaller.',
            
            principles: [
                {
                    title: 'The Four Inequality Symbols',
                    content: '<strong><</strong> means "less than"<br><strong>></strong> means "greater than"<br><strong>≤</strong> means "less than or equal to"<br><strong>≥</strong> means "greater than or equal to"'
                },
                {
                    title: 'Reading Number Lines',
                    content: 'On a number line:<br>• <strong>Hollow circle</strong> ○ means value NOT included (< or >)<br>• <strong>Filled circle</strong> ● means value IS included (≤ or ≥)<br>• <strong>Arrow direction</strong> shows which values work'
                }
            ],
            
            examples: [
                {
                    question: 'What does x > 5 mean?',
                    steps: [
                        'The symbol > means "greater than"',
                        'x > 5 means "x is greater than 5"',
                        'Values like 6, 7, 8, 10, 100 all work'
                    ],
                    answer: 'x is any number bigger than 5 (but not 5 itself)'
                },
                {
                    question: 'What does x ≤ 3 mean?',
                    steps: [
                        'The symbol ≤ means "less than or equal to"',
                        'x ≤ 3 means "x is at most 3"',
                        'Values like 3, 2, 1, 0, -1 all work'
                    ],
                    answer: 'x can be 3 or any number smaller than 3'
                }
            ],
            
            tips: [
                '✅ The "open" end of < or > points to the bigger value',
                '✅ A line under (≤ ≥) means "or equal to" - include the number',
                '⚠️ "At least 5" means ≥ 5 (includes 5)',
                '⚠️ "At most 5" means ≤ 5 (includes 5)'
            ]
        },
        
        'intermediate': {
            title: 'Solving Linear Inequalities',
            introduction: 'In this level, you\'ll learn to <strong>solve inequalities</strong> just like equations - but with one important rule about negative numbers!',
            
            principles: [
                {
                    title: 'Solving Steps',
                    content: 'Solve inequalities like equations:<br>• Add/subtract the same from both sides<br>• Multiply/divide both sides by the same positive number<br>• <strong>FLIP RULE:</strong> When multiplying or dividing by a NEGATIVE, flip the inequality sign!'
                },
                {
                    title: 'The Flip Rule',
                    content: '<strong>⚠️ CRITICAL:</strong> When you multiply or divide by a negative number, FLIP the sign!<br>Example: -2x < 6 → x > -3 (< becomes >)'
                }
            ],
            
            examples: [
                {
                    question: 'Solve: 2x + 3 < 11',
                    steps: [
                        'Subtract 3 from both sides: 2x < 8',
                        'Divide both sides by 2: x < 4',
                        'Check: if x = 3, then 2(3) + 3 = 9 < 11 ✓'
                    ],
                    answer: 'x < 4'
                },
                {
                    question: 'Solve: -3x ≥ 12',
                    steps: [
                        'Divide both sides by -3',
                        'FLIP the sign because dividing by negative!',
                        'x ≤ -4'
                    ],
                    answer: 'x ≤ -4 (note: sign flipped!)'
                }
            ],
            
            tips: [
                '✅ Treat it like an equation until the last step',
                '✅ Always check your answer by substituting a value',
                '⚠️ NEVER forget to flip when dividing by negative!',
                '⚠️ SEC style: "where x ∈ ℤ" means list integer solutions'
            ]
        },
        
        'advanced': {
            title: 'Compound Inequalities & Applications',
            introduction: 'In this level, you\'ll work with <strong>compound inequalities</strong> (like -2 < x ≤ 4) and real-world applications including rounding and tolerance.',
            
            principles: [
                {
                    title: 'Compound Inequalities',
                    content: 'A compound inequality has TWO bounds:<br>• -2 < x ≤ 4 means "x is greater than -2 AND at most 4"<br>• Graph shows shading BETWEEN the two values<br>• Check endpoint circles carefully!'
                },
                {
                    title: 'Rounding Inequalities (SEC Style)',
                    content: 'When a value is rounded to nearest whole number:<br>• Displayed value of 18 means actual is 17.5 ≤ x < 18.5<br>• Lower bound is INCLUDED (rounds up to 18)<br>• Upper bound is EXCLUDED (would round to 19)'
                }
            ],
            
            examples: [
                {
                    question: 'Graph: -2 < x ≤ 4, x ∈ ℤ',
                    steps: [
                        'x must be greater than -2 (not including -2)',
                        'x must be at most 4 (including 4)',
                        'x must be an integer',
                        'Solutions: -1, 0, 1, 2, 3, 4'
                    ],
                    answer: 'Six dots at -1, 0, 1, 2, 3, 4'
                },
                {
                    question: 'Temperature shows 18°C (nearest whole). Find actual range.',
                    steps: [
                        'Values from 17.5 round UP to 18',
                        'Values at 18.5 round UP to 19',
                        '17.5 ≤ T < 18.5'
                    ],
                    answer: '17.5 ≤ T < 18.5'
                }
            ],
            
            tips: [
                '✅ For x ∈ ℤ, use DOTS on number line, not a continuous line',
                '✅ For x ∈ ℕ, remember natural numbers start at 1',
                '⚠️ Rounding: lower bound INCLUDED, upper EXCLUDED',
                '🏆 SEC loves rounding inequalities - practice these!'
            ]
        }
    }
};


// Make TUTORIALS available globally for TutorialManager
window.TUTORIALS = TUTORIALS;

console.log('📚 Tutorials data loaded');
console.log('✅ All AgentMath modules loaded');

