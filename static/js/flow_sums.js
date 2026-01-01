/**
 * AgentMath - Flow Sums
 * Extracted from student_app.html - 2025-12-27
 * Self-contained mini-game module
 */

// =====================================================
// FLOW SUMS - Interactive Arithmetic Chains
// =====================================================

const flowSumsState = {
    active: false,
    level: 1,
    savedLevel: 1,
    currentQuestion: null,
    currentStepIndex: 0,
    stepAttempts: [],
    hintsUsed: 0,
    totalAttempts: 0,
    startTime: null,
    timerInterval: null,
    completed: false
};

async function startFlowSums(level = null) {
    // If no level specified, fetch saved level
    if (level === null) {
        try {
            const response = await fetch('/api/interactive/get-level/flow_sums');
            const data = await response.json();
            level = data.level || 1;
            flowSumsState.savedLevel = level;
        } catch (e) {
            level = 1;
            flowSumsState.savedLevel = 1;
        }
    }
    
    flowSumsState.level = level;
    flowSumsState.currentStepIndex = 0;
    flowSumsState.stepAttempts = [];
    flowSumsState.hintsUsed = 0;
    flowSumsState.totalAttempts = 0;
    flowSumsState.startTime = Date.now();
    flowSumsState.completed = false;
    flowSumsState.active = true;
    
    document.getElementById('flowSumsLevelBadge').textContent = `Level ${level}`;
    document.getElementById('flowStatsHints').textContent = '0';
    document.getElementById('flowStatsAttempts').textContent = '0';
    document.getElementById('flowStatsTime').textContent = '0:00';
    document.getElementById('flowProgressFill').style.width = '0%';
    document.getElementById('flowFinalAnswer').style.display = 'none';
    
    if (flowSumsState.timerInterval) clearInterval(flowSumsState.timerInterval);
    flowSumsState.timerInterval = setInterval(updateFlowTimer, 1000);
    
    try {
        const response = await fetch(`/api/flow-sums/question/${level}`);
        const data = await response.json();
        
        if (data.success) {
            flowSumsState.currentQuestion = data.question;
            flowSumsState.stepAttempts = new Array(data.question.steps.length).fill(0);
            renderFlowSum(data.question);
        } else {
            throw new Error('Failed to load question');
        }
    } catch (error) {
        console.error('Error loading Flow Sum:', error);
        alert('Could not load Flow Sum question. Please try again.');
        return;
    }
    
    document.getElementById('flowSumsContainer').classList.add('active');
    if (typeof playSound === 'function') playSound('start');
}

function renderFlowSum(question) {
    document.getElementById('flowGatewayNumber').textContent = question.gateway_number;
    
    const container = document.getElementById('flowStepsContainer');
    container.className = `flow-steps-container layout-${question.layout}`;
    container.innerHTML = '';
    
    question.steps.forEach((step, index) => {
        const stepDiv = document.createElement('div');
        stepDiv.className = 'flow-step' + (index === 0 ? ' active' : '');
        stepDiv.id = `flowStep${index}`;
        stepDiv.innerHTML = `
            <div class="flow-step-number">${index + 1}</div>
            <button class="flow-hint-btn" onclick="showFlowHint(${index})" title="Get a hint">?</button>
            <div class="flow-hint-tooltip" id="flowHint${index}">${step.hint}</div>
            <div class="flow-step-operation">${step.operation}</div>
            <div class="flow-step-input-area">
                <input type="number" 
                       class="flow-step-input" 
                       id="flowInput${index}" 
                       placeholder="?"
                       ${index !== 0 ? 'disabled' : ''}
                       onkeypress="if(event.key === 'Enter') submitFlowStep(${index})">
                <button class="flow-step-submit" 
                        id="flowSubmit${index}" 
                        onclick="submitFlowStep(${index})"
                        ${index !== 0 ? 'disabled' : ''}>✓</button>
            </div>
            <div class="flow-attempts" id="flowAttempts${index}"></div>
        `;
        
        if (index < question.steps.length - 1 && 
            (question.layout === 'arrow_down' || question.layout === 'arrow_up')) {
            const arrow = document.createElement('div');
            arrow.className = 'flow-arrow';
            arrow.textContent = question.layout === 'arrow_down' ? '↓' : '↑';
            
            if (question.layout === 'arrow_up') {
                container.insertBefore(arrow, container.firstChild);
                container.insertBefore(stepDiv, container.firstChild);
            } else {
                container.appendChild(stepDiv);
                container.appendChild(arrow);
            }
        } else {
            if (question.layout === 'arrow_up') {
                container.insertBefore(stepDiv, container.firstChild);
            } else {
                container.appendChild(stepDiv);
            }
        }
    });
    
    setTimeout(() => {
        const firstInput = document.getElementById('flowInput0');
        if (firstInput) firstInput.focus();
    }, 100);
}

function submitFlowStep(stepIndex) {
    if (flowSumsState.completed) return;
    
    const input = document.getElementById(`flowInput${stepIndex}`);
    const userAnswer = parseInt(input.value);
    const step = flowSumsState.currentQuestion.steps[stepIndex];
    const expected = step.expected_value;
    
    if (isNaN(userAnswer)) {
        input.classList.add('incorrect');
        setTimeout(() => input.classList.remove('incorrect'), 500);
        return;
    }
    
    flowSumsState.stepAttempts[stepIndex]++;
    flowSumsState.totalAttempts++;
    document.getElementById('flowStatsAttempts').textContent = flowSumsState.totalAttempts;
    
    if (userAnswer === expected) {
        handleCorrectFlowStep(stepIndex);
    } else {
        handleIncorrectFlowStep(stepIndex, expected);
    }
}

function handleCorrectFlowStep(stepIndex) {
    const stepDiv = document.getElementById(`flowStep${stepIndex}`);
    const input = document.getElementById(`flowInput${stepIndex}`);
    const submit = document.getElementById(`flowSubmit${stepIndex}`);
    
    stepDiv.classList.remove('active', 'incorrect');
    stepDiv.classList.add('completed');
    input.classList.add('correct');
    input.disabled = true;
    submit.disabled = true;
    
    if (typeof playSound === 'function') playSound('correct');
    
    const progress = ((stepIndex + 1) / flowSumsState.currentQuestion.steps.length) * 100;
    document.getElementById('flowProgressFill').style.width = `${progress}%`;
    
    if (stepIndex === flowSumsState.currentQuestion.steps.length - 1) {
        completeFlowSum();
    } else {
        flowSumsState.currentStepIndex = stepIndex + 1;
        const nextStep = document.getElementById(`flowStep${stepIndex + 1}`);
        const nextInput = document.getElementById(`flowInput${stepIndex + 1}`);
        const nextSubmit = document.getElementById(`flowSubmit${stepIndex + 1}`);
        
        nextStep.classList.add('active');
        nextInput.disabled = false;
        nextSubmit.disabled = false;
        nextInput.focus();
    }
}

function handleIncorrectFlowStep(stepIndex, expected) {
    const stepDiv = document.getElementById(`flowStep${stepIndex}`);
    const input = document.getElementById(`flowInput${stepIndex}`);
    const attemptsDiv = document.getElementById(`flowAttempts${stepIndex}`);
    const attempts = flowSumsState.stepAttempts[stepIndex];
    
    stepDiv.classList.add('incorrect');
    input.classList.add('incorrect');
    setTimeout(() => {
        stepDiv.classList.remove('incorrect');
        input.classList.remove('incorrect');
    }, 500);
    
    if (typeof playSound === 'function') playSound('incorrect');
    
    const remaining = 3 - attempts;
    if (remaining > 0) {
        attemptsDiv.textContent = `${remaining} attempt${remaining !== 1 ? 's' : ''} remaining`;
        attemptsDiv.className = 'flow-attempts' + (remaining === 1 ? ' warning' : '');
        input.value = '';
        input.focus();
    } else {
        revealFlowAnswer(stepIndex, expected);
    }
}

function revealFlowAnswer(stepIndex, expected) {
    const stepDiv = document.getElementById(`flowStep${stepIndex}`);
    const input = document.getElementById(`flowInput${stepIndex}`);
    const attemptsDiv = document.getElementById(`flowAttempts${stepIndex}`);
    
    stepDiv.classList.remove('incorrect');
    stepDiv.classList.add('revealed', 'completed');
    input.value = expected;
    input.classList.add('correct');
    input.disabled = true;
    document.getElementById(`flowSubmit${stepIndex}`).disabled = true;
    attemptsDiv.textContent = 'Answer revealed';
    attemptsDiv.className = 'flow-attempts';
    
    const progress = ((stepIndex + 1) / flowSumsState.currentQuestion.steps.length) * 100;
    document.getElementById('flowProgressFill').style.width = `${progress}%`;
    
    setTimeout(() => {
        if (stepIndex === flowSumsState.currentQuestion.steps.length - 1) {
            completeFlowSum();
        } else {
            flowSumsState.currentStepIndex = stepIndex + 1;
            const nextStep = document.getElementById(`flowStep${stepIndex + 1}`);
            const nextInput = document.getElementById(`flowInput${stepIndex + 1}`);
            const nextSubmit = document.getElementById(`flowSubmit${stepIndex + 1}`);
            
            nextStep.classList.add('active');
            nextInput.disabled = false;
            nextSubmit.disabled = false;
            nextInput.focus();
        }
    }, 1000);
}

function showFlowHint(stepIndex) {
    const tooltip = document.getElementById(`flowHint${stepIndex}`);
    const isVisible = tooltip.classList.contains('visible');
    
    document.querySelectorAll('.flow-hint-tooltip').forEach(t => t.classList.remove('visible'));
    
    if (!isVisible) {
        tooltip.classList.add('visible');
        flowSumsState.hintsUsed++;
        document.getElementById('flowStatsHints').textContent = flowSumsState.hintsUsed;
        
        setTimeout(() => {
            tooltip.classList.remove('visible');
        }, 5000);
    }
}

function updateFlowTimer() {
    if (!flowSumsState.startTime || flowSumsState.completed) return;
    
    const elapsed = Math.floor((Date.now() - flowSumsState.startTime) / 1000);
    const minutes = Math.floor(elapsed / 60);
    const seconds = elapsed % 60;
    document.getElementById('flowStatsTime').textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
}

function completeFlowSum() {
    flowSumsState.completed = true;
    
    if (flowSumsState.timerInterval) {
        clearInterval(flowSumsState.timerInterval);
    }
    
    const finalAnswerDiv = document.getElementById('flowFinalAnswer');
    const finalValue = document.getElementById('flowFinalValue');
    finalAnswerDiv.style.display = 'block';
    finalValue.textContent = flowSumsState.currentQuestion.final_answer;
    finalValue.classList.remove('pending');
    
    const level = flowSumsState.level;
    const basePoints = 5 + (level * 2);
    const hintPenalty = flowSumsState.hintsUsed * 2;
    const attemptPenalty = Math.max(0, (flowSumsState.totalAttempts - flowSumsState.currentQuestion.steps.length) * 1);
    const points = Math.max(1, basePoints - hintPenalty - attemptPenalty);
    
    setTimeout(() => {
        showFlowCelebration(points);
    }, 500);
    
    if (typeof playSound === 'function') playSound('levelup');
    saveFlowSumsProgress(points);
}

function showFlowCelebration(points) {
    const celebration = document.getElementById('flowCelebration');
    const subtitle = document.getElementById('flowCelebrationSubtitle');
    const pointsDiv = document.getElementById('flowCelebrationPoints');
    
    const hintsUsed = flowSumsState.hintsUsed;
    const extraAttempts = flowSumsState.totalAttempts - flowSumsState.currentQuestion.steps.length;
    
    if (hintsUsed === 0 && extraAttempts === 0) {
        subtitle.textContent = 'Perfect! No hints and no mistakes! 🌟';
    } else if (hintsUsed <= 1 && extraAttempts <= 2) {
        subtitle.textContent = 'Great work on this Flow Sum! 👏';
    } else {
        subtitle.textContent = 'You completed the Flow Sum! Keep practicing! 💪';
    }
    
    pointsDiv.textContent = `+${points} Points`;
    celebration.classList.add('active');
    
    if (typeof confetti === 'function') {
        confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
    }
}

function nextFlowSum() {
    document.getElementById('flowCelebration').classList.remove('active');
    const nextLevel = Math.min(flowSumsState.level + 1, 12);
    startFlowSums(nextLevel);
}

async function resetFlowSumsLevel() {
    if (confirm('Reset to Level 1? Your progress will be saved but you\'ll start from the beginning.')) {
        try {
            await fetch('/api/interactive/reset-level', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: 'flow_sums' })
            });
            flowSumsState.savedLevel = 1;
            startFlowSums(1);
        } catch (e) {
            startFlowSums(1);
        }
    }
}

function closeFlowSums() {
    flowSumsState.active = false;
    flowSumsState.completed = true;
    
    if (flowSumsState.timerInterval) {
        clearInterval(flowSumsState.timerInterval);
    }
    
    document.getElementById('flowSumsContainer').classList.remove('active');
    document.getElementById('flowCelebration').classList.remove('active');
}

async function saveFlowSumsProgress(points) {
    const nextLevel = Math.min(flowSumsState.level + 1, 12);
    
    // Save level progress
    try {
        await fetch('/api/interactive/save-level', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic: 'flow_sums', level: nextLevel })
        });
        flowSumsState.savedLevel = nextLevel;
    } catch (e) {
        console.log('Could not save level progress');
    }
    
    try {
        await fetch('/api/flow-sums/complete', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                level: flowSumsState.level,
                hints_used: flowSumsState.hintsUsed,
                total_attempts: flowSumsState.totalAttempts,
                time_taken: Math.floor((Date.now() - flowSumsState.startTime) / 1000),
                steps_count: flowSumsState.currentQuestion.steps.length,
                points_earned: points
            })
        });
    } catch (error) {
        console.log('Could not save Flow Sums progress:', error);
    }
}
// =====================================================
// END FLOW SUMS
// =====================================================
