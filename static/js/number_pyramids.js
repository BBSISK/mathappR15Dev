/**
 * AgentMath - Number Pyramids
 * Extracted from student_app.html - 2025-12-27
 * Self-contained mini-game module
 */

// =====================================================
// NUMBER PYRAMIDS - Interactive Addition Puzzles
// =====================================================

const pyramidState = {
    active: false,
    level: 1,
    savedLevel: 1,
    puzzle: null,
    selectedCell: null,  // {row, col}
    userAnswers: [],     // 2D array mirroring pyramid
    correctCount: 0,
    hintsUsed: 0,
    totalAttempts: 0,
    attemptsPerCell: [],  // 2D array tracking attempts
    startTime: null,
    timerInterval: null,
    completed: false
};

async function startPyramid(level = null) {
    // If no level specified, fetch saved level
    if (level === null) {
        try {
            const response = await fetch('/api/interactive/get-level/number_pyramids');
            const data = await response.json();
            level = data.level || 1;
            pyramidState.savedLevel = level;
        } catch (e) {
            level = 1;
            pyramidState.savedLevel = 1;
        }
    }
    
    pyramidState.level = level;
    pyramidState.selectedCell = null;
    pyramidState.correctCount = 0;
    pyramidState.hintsUsed = 0;
    pyramidState.totalAttempts = 0;
    pyramidState.startTime = Date.now();
    pyramidState.completed = false;
    pyramidState.active = true;
    
    // Update UI
    document.getElementById('pyramidLevelBadge').textContent = `Level ${level}`;
    document.getElementById('pyramidStatsCorrect').textContent = '0';
    document.getElementById('pyramidStatsHints').textContent = '0';
    document.getElementById('pyramidStatsTime').textContent = '0:00';
    document.getElementById('pyramidProgressFill').style.width = '0%';
    document.getElementById('pyramidInputField').value = '';
    document.getElementById('pyramidInputField').disabled = true;
    document.getElementById('pyramidSubmitBtn').disabled = true;
    document.getElementById('pyramidHintText').textContent = 'Click a blank cell to select it';
    
    // Start timer
    if (pyramidState.timerInterval) clearInterval(pyramidState.timerInterval);
    pyramidState.timerInterval = setInterval(updatePyramidTimer, 1000);
    
    // Fetch puzzle
    try {
        const response = await fetch(`/api/number-pyramids/question/${level}`);
        const data = await response.json();
        
        if (data.success) {
            pyramidState.puzzle = data.puzzle;
            // Initialize user answers (null for blanks, value for given)
            pyramidState.userAnswers = data.puzzle.pyramid.map((row, r) =>
                row.map((val, c) => data.puzzle.blanks[r][c] ? null : val)
            );
            // Initialize attempts tracking
            pyramidState.attemptsPerCell = data.puzzle.blanks.map(row => 
                row.map(isBlank => isBlank ? 0 : -1)  // -1 for given cells
            );
            renderPyramid();
        } else {
            throw new Error('Failed to load puzzle');
        }
    } catch (error) {
        console.error('Error loading pyramid:', error);
        alert('Could not load pyramid puzzle. Please try again.');
        return;
    }
    
    // Show container
    document.getElementById('pyramidContainer').classList.add('active');
    if (typeof playSound === 'function') playSound('start');
}

function renderPyramid() {
    const puzzle = pyramidState.puzzle;
    const grid = document.getElementById('pyramidGrid');
    grid.innerHTML = '';
    
    puzzle.pyramid.forEach((row, rowIndex) => {
        const rowDiv = document.createElement('div');
        rowDiv.className = 'pyramid-row';
        
        row.forEach((value, colIndex) => {
            const cell = document.createElement('div');
            const isBlank = puzzle.blanks[rowIndex][colIndex];
            const userAnswer = pyramidState.userAnswers[rowIndex][colIndex];
            
            cell.className = 'pyramid-cell';
            cell.dataset.row = rowIndex;
            cell.dataset.col = colIndex;
            
            if (!isBlank) {
                // Given cell
                cell.classList.add('given');
                cell.textContent = value;
            } else {
                // Blank cell
                cell.classList.add('blank');
                if (userAnswer !== null) {
                    cell.textContent = userAnswer;
                    if (userAnswer === value) {
                        cell.classList.add('correct');
                    }
                }
                cell.onclick = () => selectPyramidCell(rowIndex, colIndex);
                
                // Add hint button
                const hintBtn = document.createElement('button');
                hintBtn.className = 'hint-btn';
                hintBtn.textContent = '?';
                hintBtn.onclick = (e) => {
                    e.stopPropagation();
                    showPyramidHint(rowIndex, colIndex);
                };
                cell.appendChild(hintBtn);
            }
            
            rowDiv.appendChild(cell);
        });
        
        grid.appendChild(rowDiv);
    });
}

function selectPyramidCell(row, col) {
    if (pyramidState.completed) return;
    
    const puzzle = pyramidState.puzzle;
    const userAnswer = pyramidState.userAnswers[row][col];
    
    // Don't select already correct cells
    if (userAnswer === puzzle.pyramid[row][col]) return;
    
    // Deselect previous
    document.querySelectorAll('.pyramid-cell.active').forEach(c => c.classList.remove('active'));
    
    // Select new
    const cell = document.querySelector(`.pyramid-cell[data-row="${row}"][data-col="${col}"]`);
    if (cell) {
        cell.classList.add('active');
        pyramidState.selectedCell = { row, col };
        
        // Enable input
        document.getElementById('pyramidInputField').disabled = false;
        document.getElementById('pyramidInputField').value = '';
        document.getElementById('pyramidInputField').focus();
        document.getElementById('pyramidSubmitBtn').disabled = false;
        
        // Show hint text
        updatePyramidHintText(row, col);
    }
}

function updatePyramidHintText(row, col) {
    const puzzle = pyramidState.puzzle;
    const rows = puzzle.rows;
    let hint = '';
    
    // Check what cells are adjacent
    if (row < rows - 1) {
        // Has cells below
        const leftBelow = pyramidState.userAnswers[row + 1]?.[col];
        const rightBelow = pyramidState.userAnswers[row + 1]?.[col + 1];
        if (leftBelow !== null && rightBelow !== null) {
            hint = `Add the two cells below: ${leftBelow} + ${rightBelow}`;
        }
    }
    
    if (!hint && row > 0) {
        // Check if can deduce from above
        const above = pyramidState.userAnswers[row - 1]?.[col] || pyramidState.userAnswers[row - 1]?.[col - 1];
        if (above !== null) {
            hint = 'This cell is part of a sum. Work backwards!';
        }
    }
    
    if (!hint) {
        hint = 'Use the pyramid rules: each cell = sum of two below';
    }
    
    document.getElementById('pyramidHintText').textContent = hint;
}

function submitPyramidAnswer() {
    if (!pyramidState.selectedCell || pyramidState.completed) return;
    
    const { row, col } = pyramidState.selectedCell;
    const input = document.getElementById('pyramidInputField');
    const userAnswer = parseInt(input.value);
    const correctAnswer = pyramidState.puzzle.pyramid[row][col];
    
    if (isNaN(userAnswer)) {
        input.classList.add('incorrect');
        setTimeout(() => input.classList.remove('incorrect'), 500);
        return;
    }
    
    pyramidState.totalAttempts++;
    pyramidState.attemptsPerCell[row][col]++;
    
    const cell = document.querySelector(`.pyramid-cell[data-row="${row}"][data-col="${col}"]`);
    
    if (userAnswer === correctAnswer) {
        // Correct!
        pyramidState.userAnswers[row][col] = userAnswer;
        pyramidState.correctCount++;
        
        cell.classList.remove('active', 'incorrect');
        cell.classList.add('correct');
        cell.textContent = userAnswer;
        
        if (typeof playSound === 'function') playSound('correct');
        
        // Update progress
        const blanks = pyramidState.puzzle.blank_count;
        const progress = (pyramidState.correctCount / blanks) * 100;
        document.getElementById('pyramidProgressFill').style.width = `${progress}%`;
        document.getElementById('pyramidStatsCorrect').textContent = pyramidState.correctCount;
        
        // Clear selection
        pyramidState.selectedCell = null;
        input.value = '';
        input.disabled = true;
        document.getElementById('pyramidSubmitBtn').disabled = true;
        document.getElementById('pyramidHintText').textContent = 'Click another blank cell';
        
        // Check completion
        if (pyramidState.correctCount >= blanks) {
            completePyramid();
        }
    } else {
        // Incorrect
        cell.classList.add('incorrect');
        setTimeout(() => cell.classList.remove('incorrect'), 500);
        
        if (typeof playSound === 'function') playSound('incorrect');
        
        // Check if reveal after 3 attempts
        if (pyramidState.attemptsPerCell[row][col] >= 3) {
            revealPyramidCell(row, col, correctAnswer);
        } else {
            const remaining = 3 - pyramidState.attemptsPerCell[row][col];
            document.getElementById('pyramidHintText').textContent = 
                `Not quite! ${remaining} attempt${remaining !== 1 ? 's' : ''} remaining`;
            input.value = '';
            input.focus();
        }
    }
}

function revealPyramidCell(row, col, answer) {
    pyramidState.userAnswers[row][col] = answer;
    pyramidState.correctCount++;
    
    const cell = document.querySelector(`.pyramid-cell[data-row="${row}"][data-col="${col}"]`);
    cell.classList.remove('active', 'incorrect', 'blank');
    cell.classList.add('revealed');
    cell.textContent = answer;
    
    // Update progress
    const blanks = pyramidState.puzzle.blank_count;
    const progress = (pyramidState.correctCount / blanks) * 100;
    document.getElementById('pyramidProgressFill').style.width = `${progress}%`;
    document.getElementById('pyramidStatsCorrect').textContent = pyramidState.correctCount;
    
    // Clear selection
    pyramidState.selectedCell = null;
    document.getElementById('pyramidInputField').value = '';
    document.getElementById('pyramidInputField').disabled = true;
    document.getElementById('pyramidSubmitBtn').disabled = true;
    document.getElementById('pyramidHintText').textContent = 'Answer revealed. Click another blank cell.';
    
    // Check completion
    if (pyramidState.correctCount >= blanks) {
        setTimeout(() => completePyramid(), 500);
    }
}

function showPyramidHint(row, col) {
    pyramidState.hintsUsed++;
    document.getElementById('pyramidStatsHints').textContent = pyramidState.hintsUsed;
    
    const puzzle = pyramidState.puzzle;
    const rows = puzzle.rows;
    let hintText = '';
    
    // Generate helpful hint
    if (row < rows - 1) {
        const leftBelow = pyramidState.userAnswers[row + 1]?.[col];
        const rightBelow = pyramidState.userAnswers[row + 1]?.[col + 1];
        if (leftBelow !== null && rightBelow !== null) {
            hintText = `💡 This cell = ${leftBelow} + ${rightBelow} = ?`;
        } else {
            hintText = '💡 Fill in the cells below first, then add them!';
        }
    } else if (row > 0) {
        // Bottom row - need to work backwards
        const above = pyramidState.userAnswers[row - 1]?.[col];
        const adjacent = pyramidState.userAnswers[row]?.[col - 1] || pyramidState.userAnswers[row]?.[col + 1];
        if (above !== null && adjacent !== null) {
            hintText = `💡 The cell above is ${above}. Subtract the adjacent cell!`;
        } else {
            hintText = '💡 Work backwards from the cells above!';
        }
    }
    
    if (!hintText) {
        hintText = '💡 Each cell equals the sum of the two cells directly below it';
    }
    
    document.getElementById('pyramidHintText').textContent = hintText;
    
    // Select the cell if not already selected
    if (!pyramidState.selectedCell || pyramidState.selectedCell.row !== row || pyramidState.selectedCell.col !== col) {
        selectPyramidCell(row, col);
    }
}

function updatePyramidTimer() {
    if (!pyramidState.startTime || pyramidState.completed) return;
    
    const elapsed = Math.floor((Date.now() - pyramidState.startTime) / 1000);
    const minutes = Math.floor(elapsed / 60);
    const seconds = elapsed % 60;
    document.getElementById('pyramidStatsTime').textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
}

function completePyramid() {
    pyramidState.completed = true;
    
    if (pyramidState.timerInterval) {
        clearInterval(pyramidState.timerInterval);
    }
    
    // Calculate points
    const level = pyramidState.level;
    const basePoints = 5 + (level * 2);
    const hintPenalty = pyramidState.hintsUsed * 2;
    const blanks = pyramidState.puzzle.blank_count;
    const attemptPenalty = Math.max(0, (pyramidState.totalAttempts - blanks) * 1);
    const points = Math.max(1, basePoints - hintPenalty - attemptPenalty);
    
    // Show celebration
    setTimeout(() => showPyramidCelebration(points), 300);
    
    if (typeof playSound === 'function') playSound('levelup');
    savePyramidProgress(points);
}

function showPyramidCelebration(points) {
    const celebration = document.getElementById('pyramidCelebration');
    const subtitle = document.getElementById('pyramidCelebrationSubtitle');
    const pointsDiv = document.getElementById('pyramidCelebrationPoints');
    
    const hintsUsed = pyramidState.hintsUsed;
    const extraAttempts = pyramidState.totalAttempts - pyramidState.puzzle.blank_count;
    
    if (hintsUsed === 0 && extraAttempts === 0) {
        subtitle.textContent = 'Perfect pyramid! No hints, no mistakes! 🌟';
    } else if (hintsUsed <= 1 && extraAttempts <= 2) {
        subtitle.textContent = 'Great work building that pyramid! 👏';
    } else {
        subtitle.textContent = 'Pyramid complete! Keep practicing! 💪';
    }
    
    pointsDiv.textContent = `+${points} Points`;
    celebration.classList.add('active');
    
    if (typeof confetti === 'function') {
        confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
    }
}

function nextPyramid() {
    document.getElementById('pyramidCelebration').classList.remove('active');
    const nextLevel = Math.min(pyramidState.level + 1, 12);
    startPyramid(nextLevel);
}

async function resetPyramidLevel() {
    if (confirm('Reset to Level 1? Your progress will be saved but you\'ll start from the beginning.')) {
        try {
            await fetch('/api/interactive/reset-level', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: 'number_pyramids' })
            });
            pyramidState.savedLevel = 1;
            startPyramid(1);
        } catch (e) {
            startPyramid(1);
        }
    }
}

function closePyramid() {
    pyramidState.active = false;
    pyramidState.completed = true;
    
    if (pyramidState.timerInterval) {
        clearInterval(pyramidState.timerInterval);
    }
    
    document.getElementById('pyramidContainer').classList.remove('active');
    document.getElementById('pyramidCelebration').classList.remove('active');
}

async function savePyramidProgress(points) {
    const nextLevel = Math.min(pyramidState.level + 1, 12);
    
    // Save level progress
    try {
        await fetch('/api/interactive/save-level', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic: 'number_pyramids', level: nextLevel })
        });
        pyramidState.savedLevel = nextLevel;
    } catch (e) {
        console.log('Could not save level progress');
    }
    
    try {
        await fetch('/api/number-pyramids/complete', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                level: pyramidState.level,
                hints_used: pyramidState.hintsUsed,
                total_attempts: pyramidState.totalAttempts,
                total_blanks: pyramidState.puzzle.blank_count,
                time_taken: Math.floor((Date.now() - pyramidState.startTime) / 1000),
                points_earned: points
            })
        });
    } catch (error) {
        console.log('Could not save pyramid progress:', error);
    }
}

// Handle Enter key in input field
document.addEventListener('DOMContentLoaded', function() {
    const pyramidInput = document.getElementById('pyramidInputField');
    if (pyramidInput) {
        pyramidInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                submitPyramidAnswer();
            }
        });
    }
});

// =====================================================
// END NUMBER PYRAMIDS
// =====================================================
