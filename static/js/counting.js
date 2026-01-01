/**
 * AgentMath - Counting
 * Extracted from student_app.html - 2025-12-27
 * Self-contained mini-game module
 */

// =====================================================
// MASTERING COUNTING - Number Sequence Activity
// =====================================================

const countingState = {
    active: false,
    level: 1,
    savedLevel: 1,
    puzzle: null,
    correctCount: 0,
    totalBlanks: 0,
    streak: 0,
    maxStreak: 0,
    startTime: null,
    timerInterval: null,
    rowsCompleted: [],
    answers: {}  // Store correct answers for validation
};

async function startCounting(level = null) {
    // If no level specified, fetch saved level
    if (level === null) {
        try {
            const response = await fetch('/api/interactive/get-level/mastering_counting');
            const data = await response.json();
            level = data.level || 1;
            countingState.savedLevel = level;
        } catch (e) {
            level = 1;
            countingState.savedLevel = 1;
        }
    }
    
    countingState.level = level;
    countingState.correctCount = 0;
    countingState.streak = 0;
    countingState.maxStreak = 0;
    countingState.startTime = Date.now();
    countingState.rowsCompleted = [];
    countingState.answers = {};
    countingState.active = true;
    
    // Update UI
    document.getElementById('countingLevelBadge').textContent = `Level ${level}`;
    document.getElementById('countingStatsCorrect').textContent = '0';
    document.getElementById('countingStatsStreak').textContent = '0';
    document.getElementById('countingStatsTime').textContent = '0:00';
    document.getElementById('countingProgressFill').style.width = '0%';
    
    // Start timer
    if (countingState.timerInterval) clearInterval(countingState.timerInterval);
    countingState.timerInterval = setInterval(updateCountingTimer, 1000);
    
    // Fetch puzzle
    try {
        const response = await fetch(`/api/mastering-counting/question/${level}`);
        const data = await response.json();
        
        if (data.success) {
            countingState.puzzle = data.puzzle;
            countingState.totalBlanks = data.puzzle.total_blanks;
            document.getElementById('countingProgressText').textContent = `0 / ${countingState.totalBlanks}`;
            renderCountingGrid();
        } else {
            throw new Error('Failed to load puzzle');
        }
    } catch (error) {
        console.error('Error loading counting puzzle:', error);
        alert('Could not load puzzle. Please try again.');
        return;
    }
    
    // Show container
    document.getElementById('countingContainer').classList.add('active');
    if (typeof playSound === 'function') playSound('start');
}

function renderCountingGrid() {
    const puzzle = countingState.puzzle;
    const gridDiv = document.getElementById('countingGrid');
    
    // Update instruction
    document.getElementById('countingInstruction').textContent = puzzle.instruction;
    
    gridDiv.innerHTML = '';
    
    puzzle.rows.forEach((row, rowIndex) => {
        const rowDiv = document.createElement('div');
        rowDiv.className = 'counting-row';
        rowDiv.id = `countingRow${rowIndex}`;
        
        // Row number label
        const rowLabel = document.createElement('div');
        rowLabel.className = 'counting-row-number';
        rowLabel.textContent = `${rowIndex + 1}.`;
        rowDiv.appendChild(rowLabel);
        
        row.cells.forEach((cell, cellIndex) => {
            if (cell.is_blank) {
                // Input cell
                const input = document.createElement('input');
                input.type = 'text';
                input.inputMode = 'numeric';
                input.className = 'counting-cell-input';
                input.id = `counting-${rowIndex}-${cellIndex}`;
                input.dataset.row = rowIndex;
                input.dataset.cell = cellIndex;
                input.dataset.expected = cell.value;
                input.maxLength = 4; // Allow for negative numbers
                
                // Store answer for validation
                countingState.answers[`${rowIndex}-${cellIndex}`] = cell.value;
                
                // Auto-validate on input
                input.addEventListener('input', (e) => {
                    validateCountingInput(e.target, cell.value, rowIndex, cellIndex);
                });
                
                // Handle Enter key and navigation
                input.addEventListener('keydown', (e) => {
                    if (e.key === 'Enter') {
                        e.preventDefault();
                        moveToNextCountingInput(rowIndex, cellIndex);
                    } else if (e.key === 'ArrowRight') {
                        moveToNextCountingInput(rowIndex, cellIndex);
                    } else if (e.key === 'ArrowLeft') {
                        moveToPrevCountingInput(rowIndex, cellIndex);
                    }
                });
                
                rowDiv.appendChild(input);
            } else {
                // Hint cell (pre-filled)
                const hintDiv = document.createElement('div');
                hintDiv.className = 'counting-cell hint';
                hintDiv.textContent = cell.value;
                rowDiv.appendChild(hintDiv);
            }
        });
        
        gridDiv.appendChild(rowDiv);
    });
    
    // Focus first input
    const firstInput = gridDiv.querySelector('.counting-cell-input');
    if (firstInput) firstInput.focus();
}

function validateCountingInput(input, expected, rowIndex, cellIndex) {
    const value = input.value.trim();
    
    // Allow typing - only validate when there's input
    if (value === '') {
        input.classList.remove('correct', 'incorrect');
        return;
    }
    
    const numValue = parseInt(value);
    
    if (numValue === expected) {
        // Correct!
        if (!input.classList.contains('correct')) {
            input.classList.remove('incorrect');
            input.classList.add('correct');
            input.disabled = true;
            
            countingState.correctCount++;
            countingState.streak++;
            if (countingState.streak > countingState.maxStreak) {
                countingState.maxStreak = countingState.streak;
            }
            
            // Update stats
            document.getElementById('countingStatsCorrect').textContent = countingState.correctCount;
            document.getElementById('countingStatsStreak').textContent = countingState.streak;
            
            // Update progress bar
            const progress = (countingState.correctCount / countingState.totalBlanks) * 100;
            document.getElementById('countingProgressFill').style.width = `${progress}%`;
            document.getElementById('countingProgressText').textContent = 
                `${countingState.correctCount} / ${countingState.totalBlanks}`;
            
            // Sound effect
            if (typeof playSound === 'function') playSound('correct');
            
            // Check if row is complete
            checkCountingRowComplete(rowIndex);
            
            // Check if puzzle is complete
            if (countingState.correctCount >= countingState.totalBlanks) {
                setTimeout(showCountingCelebration, 500);
            } else {
                // Auto-move to next input after brief delay
                setTimeout(() => moveToNextCountingInput(rowIndex, cellIndex), 200);
            }
        }
    } else if (value.length >= String(expected).length || 
               (expected < 0 && value.length >= String(expected).length)) {
        // Wrong - only show after they've typed enough digits
        input.classList.remove('correct');
        input.classList.add('incorrect');
        countingState.streak = 0;
        document.getElementById('countingStatsStreak').textContent = '0';
        if (typeof playSound === 'function') playSound('incorrect');
    } else {
        // Still typing - remove incorrect class
        input.classList.remove('incorrect');
    }
}

function checkCountingRowComplete(rowIndex) {
    if (countingState.rowsCompleted.includes(rowIndex)) return;
    
    const puzzle = countingState.puzzle;
    const row = puzzle.rows[rowIndex];
    
    // Check if all blanks in this row are correct
    let allCorrect = true;
    row.cells.forEach((cell, cellIndex) => {
        if (cell.is_blank) {
            const input = document.getElementById(`counting-${rowIndex}-${cellIndex}`);
            if (!input || !input.classList.contains('correct')) {
                allCorrect = false;
            }
        }
    });
    
    if (allCorrect) {
        countingState.rowsCompleted.push(rowIndex);
        
        // Animate the row
        const rowDiv = document.getElementById(`countingRow${rowIndex}`);
        if (rowDiv) {
            rowDiv.classList.add('counting-row-complete');
        }
        
        // Show toast
        showCountingRowToast(rowIndex);
    }
}

function showCountingRowToast(rowIndex) {
    const toast = document.getElementById('countingRowToast');
    const messages = ['✓ Row Complete!', '🎯 Nice!', '⭐ Great!', '🔥 On Fire!'];
    toast.textContent = messages[rowIndex % messages.length];
    toast.classList.add('show');
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 800);
}

function moveToNextCountingInput(currentRow, currentCell) {
    const puzzle = countingState.puzzle;
    
    // Try to find next input in same row
    for (let c = currentCell + 1; c < puzzle.rows[currentRow].cells.length; c++) {
        const input = document.getElementById(`counting-${currentRow}-${c}`);
        if (input && !input.disabled) {
            input.focus();
            input.select();
            return;
        }
    }
    
    // Try next rows
    for (let r = currentRow + 1; r < puzzle.rows.length; r++) {
        for (let c = 0; c < puzzle.rows[r].cells.length; c++) {
            const input = document.getElementById(`counting-${r}-${c}`);
            if (input && !input.disabled) {
                input.focus();
                input.select();
                return;
            }
        }
    }
    
    // Wrap to beginning if needed
    for (let r = 0; r <= currentRow; r++) {
        const maxC = r === currentRow ? currentCell : puzzle.rows[r].cells.length;
        for (let c = 0; c < maxC; c++) {
            const input = document.getElementById(`counting-${r}-${c}`);
            if (input && !input.disabled) {
                input.focus();
                input.select();
                return;
            }
        }
    }
}

function moveToPrevCountingInput(currentRow, currentCell) {
    const puzzle = countingState.puzzle;
    
    // Try to find previous input in same row
    for (let c = currentCell - 1; c >= 0; c--) {
        const input = document.getElementById(`counting-${currentRow}-${c}`);
        if (input && !input.disabled) {
            input.focus();
            input.select();
            return;
        }
    }
    
    // Try previous rows
    for (let r = currentRow - 1; r >= 0; r--) {
        for (let c = puzzle.rows[r].cells.length - 1; c >= 0; c--) {
            const input = document.getElementById(`counting-${r}-${c}`);
            if (input && !input.disabled) {
                input.focus();
                input.select();
                return;
            }
        }
    }
}

function showCountingCelebration() {
    if (countingState.timerInterval) {
        clearInterval(countingState.timerInterval);
    }
    
    // Calculate points
    const level = countingState.level;
    const timeElapsed = Math.floor((Date.now() - countingState.startTime) / 1000);
    let points = 5 + (level * 2);
    
    // Time bonus
    if (timeElapsed < 60) {
        points += 3;
    } else if (timeElapsed < 90) {
        points += 1;
    }
    
    // Update celebration modal
    const timeStr = `${Math.floor(timeElapsed / 60)}:${(timeElapsed % 60).toString().padStart(2, '0')}`;
    document.getElementById('countingCelebrationSubtitle').textContent = 
        `Completed in ${timeStr} with a max streak of ${countingState.maxStreak}! 🔥`;
    document.getElementById('countingCelebrationPoints').textContent = `+${points} Points`;
    
    document.getElementById('countingCelebration').classList.add('active');
    
    if (typeof confetti === 'function') {
        confetti({ particleCount: 150, spread: 90, origin: { y: 0.6 } });
    }
    
    saveCountingProgress();
}

function updateCountingTimer() {
    if (!countingState.startTime) return;
    
    const elapsed = Math.floor((Date.now() - countingState.startTime) / 1000);
    const minutes = Math.floor(elapsed / 60);
    const seconds = elapsed % 60;
    document.getElementById('countingStatsTime').textContent = 
        `${minutes}:${seconds.toString().padStart(2, '0')}`;
}

function nextCounting() {
    document.getElementById('countingCelebration').classList.remove('active');
    
    // Progress to next level (max 12)
    const nextLevel = Math.min(countingState.level + 1, 12);
    startCounting(nextLevel);
}

async function resetCountingLevel() {
    if (confirm('Reset to Level 1? Your progress will be saved but you\'ll start from the beginning.')) {
        try {
            await fetch('/api/interactive/reset-level', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: 'mastering_counting' })
            });
            countingState.savedLevel = 1;
            startCounting(1);
        } catch (e) {
            startCounting(1);
        }
    }
}

function closeCounting() {
    countingState.active = false;
    
    if (countingState.timerInterval) {
        clearInterval(countingState.timerInterval);
    }
    
    document.getElementById('countingContainer').classList.remove('active');
    document.getElementById('countingCelebration').classList.remove('active');
}

async function saveCountingProgress() {
    const nextLevel = Math.min(countingState.level + 1, 12);
    
    // Save level progress
    try {
        await fetch('/api/interactive/save-level', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic: 'mastering_counting', level: nextLevel })
        });
        countingState.savedLevel = nextLevel;
    } catch (e) {
        console.log('Could not save level progress');
    }
    
    try {
        const timeElapsed = Math.floor((Date.now() - countingState.startTime) / 1000);
        await fetch('/api/mastering-counting/complete', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                level: countingState.level,
                total_blanks: countingState.totalBlanks,
                correct_count: countingState.correctCount,
                time_taken: timeElapsed,
                max_streak: countingState.maxStreak
            })
        });
    } catch (error) {
        console.log('Could not save counting progress:', error);
    }
}

// =====================================================
// END MASTERING COUNTING
// =====================================================
