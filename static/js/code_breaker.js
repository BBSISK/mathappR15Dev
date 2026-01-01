/**
 * AgentMath - Code Breaker
 * Extracted from student_app.html - 2025-12-27
 * Self-contained mini-game module
 */

// =====================================================
// CODE BREAKER - Logic and Numeracy Puzzle
// =====================================================

const codeBreakerState = {
    active: false,
    level: 1,
    savedLevel: 1,
    puzzle: null,
    guessesUsed: 0,
    maxGuesses: 8,
    history: [],
    startTime: null,
    timerInterval: null,
    solved: false
};

async function startCodeBreaker(level = null) {
    // If no level specified, fetch saved level
    if (level === null) {
        try {
            const response = await fetch('/api/interactive/get-level/code_breaker');
            const data = await response.json();
            level = data.level || 1;
            codeBreakerState.savedLevel = level;
        } catch (e) {
            level = 1;
            codeBreakerState.savedLevel = 1;
        }
    }
    
    codeBreakerState.level = level;
    codeBreakerState.guessesUsed = 0;
    codeBreakerState.history = [];
    codeBreakerState.startTime = Date.now();
    codeBreakerState.solved = false;
    codeBreakerState.active = true;
    
    // Update UI
    document.getElementById('codeBreakerLevelBadge').textContent = `Level ${level}`;
    document.getElementById('codeBreakerHistory').innerHTML = '<div style="color: #9ca3af; text-align: center; padding: 10px;">No guesses yet</div>';
    document.getElementById('codeBreakerFailed').style.display = 'none';
    document.getElementById('codeBreakerSubmitBtn').disabled = false;
    document.getElementById('codeBreakerStatsTime').textContent = '0:00';
    
    // Start timer
    if (codeBreakerState.timerInterval) clearInterval(codeBreakerState.timerInterval);
    codeBreakerState.timerInterval = setInterval(updateCodeBreakerTimer, 1000);
    
    // Fetch puzzle
    try {
        const response = await fetch(`/api/code-breaker/question/${level}`);
        const data = await response.json();
        
        if (data.success) {
            codeBreakerState.puzzle = data.puzzle;
            codeBreakerState.maxGuesses = data.puzzle.max_guesses;
            renderCodeBreaker();
        } else {
            throw new Error('Failed to load puzzle');
        }
    } catch (error) {
        console.error('Error loading code breaker:', error);
        alert('Could not load puzzle. Please try again.');
        return;
    }
    
    // Show container
    document.getElementById('codeBreakerContainer').classList.add('active');
    if (typeof playSound === 'function') playSound('start');
}

function renderCodeBreaker() {
    const puzzle = codeBreakerState.puzzle;
    
    // Render clues
    const cluesDiv = document.getElementById('codeBreakerClues');
    cluesDiv.innerHTML = puzzle.clues.map(clue => 
        `<div class="code-breaker-clue">${clue.text}</div>`
    ).join('');
    
    // Render tip
    document.getElementById('codeBreakerTip').textContent = puzzle.tip;
    
    // Render digit inputs
    const inputArea = document.getElementById('codeBreakerInputArea');
    inputArea.innerHTML = '';
    for (let i = 0; i < puzzle.digits; i++) {
        const input = document.createElement('input');
        input.type = 'number';
        input.min = puzzle.digit_range[0];
        input.max = puzzle.digit_range[1];
        input.className = 'code-digit-input';
        input.id = `codeDigit${i}`;
        input.maxLength = 1;
        input.placeholder = '?';
        
        // Auto-advance to next input
        input.addEventListener('input', (e) => {
            const val = e.target.value;
            if (val.length >= 1) {
                // Keep only last digit
                e.target.value = val.slice(-1);
                // Move to next input
                const nextInput = document.getElementById(`codeDigit${i + 1}`);
                if (nextInput) nextInput.focus();
            }
        });
        
        // Handle backspace
        input.addEventListener('keydown', (e) => {
            if (e.key === 'Backspace' && e.target.value === '') {
                const prevInput = document.getElementById(`codeDigit${i - 1}`);
                if (prevInput) prevInput.focus();
            }
            if (e.key === 'Enter') {
                submitCodeGuess();
            }
        });
        
        inputArea.appendChild(input);
    }
    
    // Update stats
    document.getElementById('codeBreakerStatsGuesses').textContent = `0/${puzzle.max_guesses}`;
    
    // Focus first input
    document.getElementById('codeDigit0').focus();
}

async function submitCodeGuess() {
    if (codeBreakerState.solved || codeBreakerState.guessesUsed >= codeBreakerState.maxGuesses) return;
    
    const puzzle = codeBreakerState.puzzle;
    const guess = [];
    
    // Collect digits
    for (let i = 0; i < puzzle.digits; i++) {
        const input = document.getElementById(`codeDigit${i}`);
        const val = parseInt(input.value);
        if (isNaN(val) || val < puzzle.digit_range[0] || val > puzzle.digit_range[1]) {
            input.focus();
            input.style.borderColor = '#ef4444';
            setTimeout(() => input.style.borderColor = '#cbd5e1', 500);
            return;
        }
        guess.push(val);
    }
    
    // Submit guess
    try {
        const response = await fetch('/api/code-breaker/guess', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ guess })
        });
        const data = await response.json();
        
        if (data.success) {
            codeBreakerState.guessesUsed++;
            codeBreakerState.history.push({ guess, result: data.result });
            
            // Update inputs with feedback
            updateCodeInputFeedback(data.result.feedback);
            
            // Update history
            renderCodeBreakerHistory();
            
            // Update stats
            document.getElementById('codeBreakerStatsGuesses').textContent = 
                `${codeBreakerState.guessesUsed}/${codeBreakerState.maxGuesses}`;
            
            if (data.result.is_solved) {
                // Solved!
                codeBreakerState.solved = true;
                if (typeof playSound === 'function') playSound('levelup');
                setTimeout(() => showCodeBreakerCelebration(), 500);
            } else if (codeBreakerState.guessesUsed >= codeBreakerState.maxGuesses) {
                // Out of guesses
                if (typeof playSound === 'function') playSound('incorrect');
                await revealCode();
            } else {
                // Continue playing
                if (typeof playSound === 'function') playSound('incorrect');
                // Clear inputs for next guess after a delay
                setTimeout(clearCodeInputs, 1000);
            }
        }
    } catch (error) {
        console.error('Error checking guess:', error);
    }
}

function updateCodeInputFeedback(feedback) {
    feedback.forEach(f => {
        const input = document.getElementById(`codeDigit${f.position}`);
        input.classList.remove('correct', 'wrong-position', 'not-in-code');
        input.classList.add(f.status.replace('_', '-'));
        input.disabled = true;
    });
}

function clearCodeInputs() {
    const puzzle = codeBreakerState.puzzle;
    for (let i = 0; i < puzzle.digits; i++) {
        const input = document.getElementById(`codeDigit${i}`);
        input.value = '';
        input.disabled = false;
        input.classList.remove('correct', 'wrong-position', 'not-in-code');
    }
    document.getElementById('codeDigit0').focus();
}

function renderCodeBreakerHistory() {
    const historyDiv = document.getElementById('codeBreakerHistory');
    
    if (codeBreakerState.history.length === 0) {
        historyDiv.innerHTML = '<div style="color: #9ca3af; text-align: center; padding: 10px;">No guesses yet</div>';
        return;
    }
    
    historyDiv.innerHTML = codeBreakerState.history.map((h, idx) => {
        const digits = h.guess.map((d, i) => {
            const status = h.result.feedback[i].status.replace('_', '-');
            return `<div class="code-history-digit ${status}">${d}</div>`;
        }).join('');
        
        return `<div class="code-history-row">
            <span style="color: #9ca3af; font-size: 0.8rem; width: 20px;">${idx + 1}.</span>
            ${digits}
            <span style="margin-left: auto; font-size: 0.8rem;">
                🟢${h.result.correct_count} 🟡${h.result.wrong_position_count}
            </span>
        </div>`;
    }).join('');
}

async function revealCode() {
    try {
        const response = await fetch('/api/code-breaker/reveal', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        const data = await response.json();
        
        if (data.success) {
            document.getElementById('codeBreakerRevealedCode').textContent = data.code.join(' ');
            document.getElementById('codeBreakerFailed').style.display = 'block';
            document.getElementById('codeBreakerSubmitBtn').disabled = true;
            
            // Save with failed status
            saveCodeBreakerProgress(false);
        }
    } catch (error) {
        console.error('Error revealing code:', error);
    }
}

function showCodeBreakerCelebration() {
    if (codeBreakerState.timerInterval) {
        clearInterval(codeBreakerState.timerInterval);
    }
    
    // Calculate points
    const level = codeBreakerState.level;
    const guessesUsed = codeBreakerState.guessesUsed;
    const maxGuesses = codeBreakerState.maxGuesses;
    const basePoints = 5 + (level * 2);
    const guessBonus = (maxGuesses - guessesUsed) * 2;
    const points = basePoints + guessBonus;
    
    // Update celebration modal
    const guessWord = guessesUsed === 1 ? 'guess' : 'guesses';
    document.getElementById('codeBreakerCelebrationSubtitle').textContent = 
        `Cracked in ${guessesUsed} ${guessWord}!`;
    document.getElementById('codeBreakerCelebrationPoints').textContent = `+${points} Points`;
    
    document.getElementById('codeBreakerCelebration').classList.add('active');
    
    if (typeof confetti === 'function') {
        confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
    }
    
    saveCodeBreakerProgress(true);
}

function updateCodeBreakerTimer() {
    if (!codeBreakerState.startTime || codeBreakerState.solved) return;
    
    const elapsed = Math.floor((Date.now() - codeBreakerState.startTime) / 1000);
    const minutes = Math.floor(elapsed / 60);
    const seconds = elapsed % 60;
    document.getElementById('codeBreakerStatsTime').textContent = 
        `${minutes}:${seconds.toString().padStart(2, '0')}`;
}

function nextCodeBreaker() {
    document.getElementById('codeBreakerCelebration').classList.remove('active');
    const nextLevel = Math.min(codeBreakerState.level + 1, 12);
    startCodeBreaker(nextLevel);
}

async function resetCodeBreakerLevel() {
    if (confirm('Reset to Level 1? Your progress will be saved but you\'ll start from the beginning.')) {
        try {
            await fetch('/api/interactive/reset-level', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: 'code_breaker' })
            });
            codeBreakerState.savedLevel = 1;
            startCodeBreaker(1);
        } catch (e) {
            startCodeBreaker(1);
        }
    }
}

function closeCodeBreaker() {
    codeBreakerState.active = false;
    
    if (codeBreakerState.timerInterval) {
        clearInterval(codeBreakerState.timerInterval);
    }
    
    document.getElementById('codeBreakerContainer').classList.remove('active');
    document.getElementById('codeBreakerCelebration').classList.remove('active');
}

async function saveCodeBreakerProgress(solved) {
    // Only save level progress if solved
    if (solved) {
        const nextLevel = Math.min(codeBreakerState.level + 1, 12);
        try {
            await fetch('/api/interactive/save-level', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: 'code_breaker', level: nextLevel })
            });
            codeBreakerState.savedLevel = nextLevel;
        } catch (e) {
            console.log('Could not save level progress');
        }
    }
    
    try {
        await fetch('/api/code-breaker/complete', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                level: codeBreakerState.level,
                guesses_used: codeBreakerState.guessesUsed,
                max_guesses: codeBreakerState.maxGuesses,
                solved: solved,
                time_taken: Math.floor((Date.now() - codeBreakerState.startTime) / 1000)
            })
        });
    } catch (error) {
        console.log('Could not save Code Breaker progress:', error);
    }
}

// =====================================================
// END CODE BREAKER
// =====================================================
