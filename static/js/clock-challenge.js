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
