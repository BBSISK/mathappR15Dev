/**
 * AgentMath - Ordering
 * Extracted from student_app.html - 2025-12-27
 * Self-contained mini-game module
 */

// =====================================================
// ORDERING & NUMBER LINES - Interactive Activity
// =====================================================

const orderingState = {
    active: false,
    level: 1,
    savedLevel: 1,
    puzzle: null,
    mode: 'sort',
    placedCount: 0,
    totalCount: 0,
    correctCount: 0,
    startTime: null,
    timerInterval: null,
    // Sort mode
    sortSlots: [],
    // Line mode
    selectedNumber: null,
    placedMarkers: {}
};

async function startOrdering(level = null) {
    // If no level specified, fetch saved level
    if (level === null) {
        try {
            const response = await fetch('/api/interactive/get-level/ordering_magnitude');
            const data = await response.json();
            level = data.level || 1;
            orderingState.savedLevel = level;
        } catch (e) {
            level = 1;
            orderingState.savedLevel = 1;
        }
    }
    
    orderingState.level = level;
    orderingState.placedCount = 0;
    orderingState.correctCount = 0;
    orderingState.sortSlots = [];
    orderingState.selectedNumber = null;
    orderingState.placedMarkers = {};
    orderingState.active = true;
    orderingState.startTime = Date.now();
    
    document.getElementById('orderingLevelBadge').textContent = `Level ${level}`;
    document.getElementById('orderingProgressFill').style.width = '0%';
    document.getElementById('orderingStatsTime').textContent = '0:00';
    
    // Start timer
    if (orderingState.timerInterval) clearInterval(orderingState.timerInterval);
    orderingState.timerInterval = setInterval(updateOrderingTimer, 1000);
    
    // Fetch puzzle
    try {
        const response = await fetch(`/api/ordering/question/${level}`);
        const data = await response.json();
        
        if (data.success) {
            orderingState.puzzle = data.puzzle;
            orderingState.mode = data.puzzle.mode;
            orderingState.totalCount = data.puzzle.count;
            
            document.getElementById('orderingInstruction').textContent = data.puzzle.instruction;
            document.getElementById('orderingStatsPlaced').textContent = `0/${orderingState.totalCount}`;
            
            renderOrderingGame();
        }
    } catch (error) {
        console.error('Error loading ordering puzzle:', error);
    }
    
    document.getElementById('orderingContainer').classList.add('active');
    if (typeof playSound === 'function') playSound('start');
}

function renderOrderingGame() {
    if (orderingState.mode === 'sort') {
        renderSortMode();
    } else {
        renderLineMode();
    }
}

// ===== SORT MODE =====
function renderSortMode() {
    const puzzle = orderingState.puzzle;
    const shuffled = [...puzzle.numbers];
    // Shuffle
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    
    orderingState.sortSlots = new Array(puzzle.count).fill(null);
    
    const gameArea = document.getElementById('orderingGameArea');
    gameArea.innerHTML = `
        <div class="ordering-sort-area">
            <div class="ordering-sort-source" id="orderingSortSource">
                ${shuffled.map(num => `
                    <div class="ordering-number-chip" data-number="${num}" onclick="selectSortNumber(this, ${num})">
                        ${num}
                    </div>
                `).join('')}
            </div>
            <div class="ordering-sort-target" id="orderingSortTarget">
                ${puzzle.numbers.map((_, idx) => `
                    <div class="ordering-sort-slot" data-slot="${idx}" onclick="placeInSlot(${idx})">?</div>
                    ${idx < puzzle.count - 1 ? '<span class="ordering-sort-arrow">→</span>' : ''}
                `).join('')}
            </div>
        </div>
    `;
}

let selectedSortChip = null;
let selectedSortNumber = null;

function selectSortNumber(element, number) {
    if (element.classList.contains('placed')) return;
    
    // Deselect previous
    document.querySelectorAll('.ordering-number-chip').forEach(el => el.style.boxShadow = '');
    
    selectedSortChip = element;
    selectedSortNumber = number;
    element.style.boxShadow = '0 0 0 4px rgba(20, 184, 166, 0.5)';
}

function placeInSlot(slotIndex) {
    if (selectedSortNumber === null) return;
    
    const slot = document.querySelector(`.ordering-sort-slot[data-slot="${slotIndex}"]`);
    
    // If slot already filled, return the number to source
    if (orderingState.sortSlots[slotIndex] !== null) {
        const oldNumber = orderingState.sortSlots[slotIndex];
        const sourceArea = document.getElementById('orderingSortSource');
        const chip = document.createElement('div');
        chip.className = 'ordering-number-chip';
        chip.dataset.number = oldNumber;
        chip.onclick = () => selectSortNumber(chip, oldNumber);
        chip.textContent = oldNumber;
        sourceArea.appendChild(chip);
        orderingState.placedCount--;
    }
    
    // Place the number
    orderingState.sortSlots[slotIndex] = selectedSortNumber;
    slot.textContent = selectedSortNumber;
    slot.classList.add('filled');
    slot.classList.remove('correct', 'wrong');
    
    // Mark chip as placed
    selectedSortChip.classList.add('placed');
    selectedSortChip.style.boxShadow = '';
    
    orderingState.placedCount++;
    updateOrderingProgress();
    
    // Reset selection
    selectedSortChip = null;
    selectedSortNumber = null;
    
    // Check if all placed
    if (orderingState.placedCount >= orderingState.totalCount) {
        checkSortOrder();
    }
}

function checkSortOrder() {
    const puzzle = orderingState.puzzle;
    let allCorrect = true;
    
    orderingState.sortSlots.forEach((num, idx) => {
        const slot = document.querySelector(`.ordering-sort-slot[data-slot="${idx}"]`);
        if (num === puzzle.correct_order[idx]) {
            slot.classList.add('correct');
            slot.classList.remove('wrong');
            orderingState.correctCount++;
        } else {
            slot.classList.add('wrong');
            slot.classList.remove('correct');
            allCorrect = false;
        }
    });
    
    if (typeof playSound === 'function') {
        playSound(allCorrect ? 'correct' : 'incorrect');
    }
    
    if (allCorrect) {
        setTimeout(showOrderingCelebration, 500);
    } else {
        // Allow retry after showing wrong answers
        setTimeout(() => {
            // Reset for retry
            orderingState.sortSlots.forEach((num, idx) => {
                const slot = document.querySelector(`.ordering-sort-slot[data-slot="${idx}"]`);
                if (!slot.classList.contains('correct')) {
                    // Return wrong numbers to source
                    const sourceArea = document.getElementById('orderingSortSource');
                    const chip = document.createElement('div');
                    chip.className = 'ordering-number-chip';
                    chip.dataset.number = num;
                    chip.onclick = () => selectSortNumber(chip, num);
                    chip.textContent = num;
                    sourceArea.appendChild(chip);
                    
                    slot.textContent = '?';
                    slot.classList.remove('filled', 'wrong');
                    orderingState.sortSlots[idx] = null;
                    orderingState.placedCount--;
                }
            });
            updateOrderingProgress();
        }, 1500);
    }
}

// ===== LINE MODE =====
function renderLineMode() {
    const puzzle = orderingState.puzzle;
    const shuffled = [...puzzle.numbers];
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    
    const gameArea = document.getElementById('orderingGameArea');
    gameArea.innerHTML = `
        <div class="ordering-line-area">
            <div class="ordering-numbers-to-place" id="orderingNumbersToPlace">
                ${shuffled.map(num => `
                    <div class="ordering-line-chip" data-number="${num}" onclick="selectLineNumber(this, ${num})">
                        ${num}
                    </div>
                `).join('')}
            </div>
            <div class="ordering-numberline-wrapper">
                <div class="ordering-numberline" id="orderingNumberLine">
                    ${puzzle.ticks.map(tick => {
                        const percent = ((tick - puzzle.line_min) / (puzzle.line_max - puzzle.line_min)) * 100;
                        return `
                            <div class="ordering-numberline-tick" style="left: ${percent}%"></div>
                            <div class="ordering-numberline-label" style="left: ${percent}%">${tick}</div>
                        `;
                    }).join('')}
                    <div class="ordering-line-clickzone" onclick="placeOnLine(event)"></div>
                </div>
            </div>
            <div style="text-align: center; color: #6b7280; font-size: 0.9rem; margin-top: 10px;">
                Click a number above, then click on the line to place it
            </div>
        </div>
    `;
}

function selectLineNumber(element, number) {
    if (element.classList.contains('placed')) return;
    
    document.querySelectorAll('.ordering-line-chip').forEach(el => el.classList.remove('selected'));
    element.classList.add('selected');
    orderingState.selectedNumber = number;
}

function placeOnLine(event) {
    if (orderingState.selectedNumber === null) return;
    
    const puzzle = orderingState.puzzle;
    const number = orderingState.selectedNumber;
    const line = document.getElementById('orderingNumberLine');
    const rect = line.getBoundingClientRect();
    
    // Calculate click position as percentage
    const clickX = event.clientX - rect.left;
    const clickPercent = (clickX / rect.width) * 100;
    
    // Get correct position
    const correctPercent = puzzle.positions[number];
    const tolerance = puzzle.tolerance || 5;
    
    // Check if correct
    const isCorrect = Math.abs(clickPercent - correctPercent) <= tolerance;
    
    // Place marker
    const markerPercent = isCorrect ? correctPercent : clickPercent;
    
    // Remove existing marker for this number if any
    const existingMarker = document.getElementById(`marker-${number}`);
    if (existingMarker) existingMarker.remove();
    
    // Create marker
    const marker = document.createElement('div');
    marker.className = `ordering-placed-marker ${isCorrect ? '' : 'wrong'}`;
    marker.id = `marker-${number}`;
    marker.style.left = `${markerPercent}%`;
    marker.innerHTML = `
        <div class="marker-number">${number}</div>
        <div class="marker-arrow"></div>
    `;
    line.appendChild(marker);
    
    // Mark chip
    const chip = document.querySelector(`.ordering-line-chip[data-number="${number}"]`);
    if (isCorrect) {
        chip.classList.add('placed');
        chip.classList.remove('selected');
        orderingState.placedMarkers[number] = true;
        orderingState.placedCount++;
        orderingState.correctCount++;
        if (typeof playSound === 'function') playSound('correct');
    } else {
        chip.classList.remove('selected');
        if (typeof playSound === 'function') playSound('incorrect');
        // Remove wrong marker after delay
        setTimeout(() => {
            marker.remove();
        }, 1000);
    }
    
    orderingState.selectedNumber = null;
    updateOrderingProgress();
    
    // Check completion
    if (orderingState.placedCount >= orderingState.totalCount) {
        setTimeout(showOrderingCelebration, 500);
    }
}

// ===== SHARED FUNCTIONS =====
function updateOrderingProgress() {
    const progress = (orderingState.placedCount / orderingState.totalCount) * 100;
    document.getElementById('orderingProgressFill').style.width = `${progress}%`;
    document.getElementById('orderingStatsPlaced').textContent = `${orderingState.placedCount}/${orderingState.totalCount}`;
}

function updateOrderingTimer() {
    if (!orderingState.startTime) return;
    const elapsed = Math.floor((Date.now() - orderingState.startTime) / 1000);
    const minutes = Math.floor(elapsed / 60);
    const seconds = elapsed % 60;
    document.getElementById('orderingStatsTime').textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
}

function showOrderingCelebration() {
    if (orderingState.timerInterval) clearInterval(orderingState.timerInterval);
    
    const timeTaken = Math.floor((Date.now() - orderingState.startTime) / 1000);
    let points = 5 + (orderingState.level * 2);
    if (timeTaken < 30) points += 5;
    else if (timeTaken < 60) points += 2;
    
    document.getElementById('orderingCelebrationSubtitle').textContent = 
        `Completed in ${timeTaken} seconds!`;
    document.getElementById('orderingCelebrationPoints').textContent = `+${points} Points`;
    
    document.getElementById('orderingCelebration').classList.add('active');
    
    if (typeof confetti === 'function') {
        confetti({ particleCount: 150, spread: 90, origin: { y: 0.6 } });
    }
    
    saveOrderingProgress();
}

function nextOrdering() {
    document.getElementById('orderingCelebration').classList.remove('active');
    const nextLevel = Math.min(orderingState.level + 1, 12);
    startOrdering(nextLevel);
}

async function resetOrderingLevel() {
    if (confirm('Reset to Level 1? Your progress will be saved but you\'ll start from the beginning.')) {
        try {
            await fetch('/api/interactive/reset-level', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: 'ordering_magnitude' })
            });
            orderingState.savedLevel = 1;
            startOrdering(1);
        } catch (e) {
            startOrdering(1);
        }
    }
}

function closeOrdering() {
    orderingState.active = false;
    if (orderingState.timerInterval) clearInterval(orderingState.timerInterval);
    document.getElementById('orderingContainer').classList.remove('active');
    document.getElementById('orderingCelebration').classList.remove('active');
}

async function saveOrderingProgress() {
    const nextLevel = Math.min(orderingState.level + 1, 12);
    
    // Save level progress
    try {
        await fetch('/api/interactive/save-level', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic: 'ordering_magnitude', level: nextLevel })
        });
        orderingState.savedLevel = nextLevel;
    } catch (e) {
        console.log('Could not save level progress');
    }
    
    try {
        await fetch('/api/ordering/complete', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                level: orderingState.level,
                correct_count: orderingState.correctCount,
                total_count: orderingState.totalCount,
                time_taken: Math.floor((Date.now() - orderingState.startTime) / 1000)
            })
        });
    } catch (error) {
        console.log('Could not save ordering progress:', error);
    }
}

// =====================================================
// END ORDERING
// =====================================================
