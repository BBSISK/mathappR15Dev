/**
 * AgentMath - Words To Numbers
 * Extracted from student_app.html - 2025-12-27
 * Self-contained mini-game module
 */

// =====================================================
// WORDS TO NUMBERS - Multi-Mode Matching Game
// =====================================================

const wordsState = {
    active: false,
    level: 1,
    savedLevel: 1,
    mode: 'chain',
    puzzle: null,
    matchedCount: 0,
    totalPairs: 0,
    selectedWord: null,
    selectedNumber: null,
    startTime: null,
    timerInterval: null,
    timeRemaining: 90,
    timeLimit: 90
};

async function startWords(level = null) {
    // If no level specified, fetch saved level
    if (level === null) {
        try {
            const response = await fetch('/api/interactive/get-level/words_to_numbers');
            const data = await response.json();
            level = data.level || 1;
            wordsState.savedLevel = level;
        } catch (e) {
            level = 1;
            wordsState.savedLevel = 1;
        }
    }
    
    wordsState.level = level;
    wordsState.matchedCount = 0;
    wordsState.selectedWord = null;
    wordsState.selectedNumber = null;
    wordsState.active = true;
    
    // Update UI
    document.getElementById('wordsLevelBadge').textContent = `Level ${level}`;
    document.getElementById('wordsProgressFill').style.width = '0%';
    
    // Load puzzle
    await loadWordsPuzzle();
    
    // Show container
    document.getElementById('wordsContainer').classList.add('active');
    if (typeof playSound === 'function') playSound('start');
}

async function loadWordsPuzzle() {
    try {
        const response = await fetch(`/api/words-to-numbers/question/${wordsState.level}?mode=${wordsState.mode}`);
        const data = await response.json();
        
        if (data.success) {
            wordsState.puzzle = data.puzzle;
            wordsState.totalPairs = data.puzzle.total_pairs;
            wordsState.timeLimit = data.puzzle.time_limit;
            wordsState.timeRemaining = data.puzzle.time_limit;
            wordsState.matchedCount = 0;
            wordsState.selectedWord = null;
            wordsState.selectedNumber = null;
            wordsState.startTime = Date.now();
            
            document.getElementById('wordsInstruction').textContent = data.puzzle.instruction;
            document.getElementById('wordsMatchedValue').textContent = `0/${wordsState.totalPairs}`;
            updateWordsTimer();
            
            // Start timer
            if (wordsState.timerInterval) clearInterval(wordsState.timerInterval);
            wordsState.timerInterval = setInterval(tickWordsTimer, 1000);
            
            renderWordsGame();
        }
    } catch (error) {
        console.error('Error loading words puzzle:', error);
    }
}

function setWordsMode(mode) {
    wordsState.mode = mode;
    
    // Update mode buttons
    document.querySelectorAll('.words-mode-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.mode === mode);
    });
    
    // Reload puzzle with new mode
    loadWordsPuzzle();
}

function renderWordsGame() {
    const gameArea = document.getElementById('wordsGameArea');
    
    if (wordsState.mode === 'chain') {
        renderChainMode(gameArea);
    } else if (wordsState.mode === 'jigsaw') {
        renderJigsawMode(gameArea);
    } else if (wordsState.mode === 'balloon') {
        renderBalloonMode(gameArea);
    }
}

// ===== CHAIN MODE =====
function renderChainMode(container) {
    const puzzle = wordsState.puzzle;
    
    container.innerHTML = `
        <div class="words-chain-area">
            <div class="words-chain-row" id="wordsChainWords">
                ${puzzle.words.map(word => `
                    <div class="words-chain-item words-chain-word" 
                         data-word="${word}" 
                         onclick="selectChainWord('${word}')">
                        ${word}
                    </div>
                `).join('')}
            </div>
            <div class="words-chain-link" id="wordsChainLink" style="display: none;">
                <div class="words-chain-link-visual">
                    <span id="chainLinkWord" class="words-chain-link-item" style="background: #fde68a;">?</span>
                    <span>🔗</span>
                    <span id="chainLinkNumber" class="words-chain-link-item" style="background: #bfdbfe;">?</span>
                </div>
            </div>
            <div class="words-chain-row" id="wordsChainNumbers">
                ${puzzle.values.map(val => `
                    <div class="words-chain-item words-chain-number" 
                         data-value="${val}" 
                         onclick="selectChainNumber('${val}')">
                        ${val}
                    </div>
                `).join('')}
            </div>
        </div>
    `;
}

function selectChainWord(word) {
    const item = document.querySelector(`.words-chain-word[data-word="${word}"]`);
    if (!item || item.classList.contains('matched')) return;
    
    // Clear previous selection
    document.querySelectorAll('.words-chain-word').forEach(el => el.classList.remove('selected'));
    
    item.classList.add('selected');
    wordsState.selectedWord = word;
    
    // Update link display
    document.getElementById('wordsChainLink').style.display = 'flex';
    document.getElementById('chainLinkWord').textContent = word;
    
    // If number already selected, check match
    if (wordsState.selectedNumber) {
        checkChainMatch();
    }
}

function selectChainNumber(value) {
    const item = document.querySelector(`.words-chain-number[data-value="${value}"]`);
    if (!item || item.classList.contains('matched')) return;
    
    // Clear previous selection
    document.querySelectorAll('.words-chain-number').forEach(el => el.classList.remove('selected'));
    
    item.classList.add('selected');
    wordsState.selectedNumber = value;
    
    // Update link display
    document.getElementById('wordsChainLink').style.display = 'flex';
    document.getElementById('chainLinkNumber').textContent = value;
    
    // If word already selected, check match
    if (wordsState.selectedWord) {
        checkChainMatch();
    }
}

function checkChainMatch() {
    const puzzle = wordsState.puzzle;
    const word = wordsState.selectedWord;
    const value = wordsState.selectedNumber;
    
    if (puzzle.answer_key[word] === value) {
        // Correct match!
        const wordEl = document.querySelector(`.words-chain-word[data-word="${word}"]`);
        const numEl = document.querySelector(`.words-chain-number[data-value="${value}"]`);
        
        wordEl.classList.remove('selected');
        numEl.classList.remove('selected');
        wordEl.classList.add('matched');
        numEl.classList.add('matched');
        
        wordsState.matchedCount++;
        updateWordsProgress();
        
        if (typeof playSound === 'function') playSound('correct');
        
        // Check if complete
        if (wordsState.matchedCount >= wordsState.totalPairs) {
            setTimeout(showWordsCelebration, 500);
        }
    } else {
        // Wrong match
        if (typeof playSound === 'function') playSound('incorrect');
        
        // Brief shake animation would go here
        document.querySelectorAll('.words-chain-item.selected').forEach(el => {
            el.style.animation = 'balloonWobble 0.3s ease';
            setTimeout(() => el.style.animation = '', 300);
        });
    }
    
    // Clear selections
    wordsState.selectedWord = null;
    wordsState.selectedNumber = null;
    document.querySelectorAll('.words-chain-item').forEach(el => el.classList.remove('selected'));
    document.getElementById('wordsChainLink').style.display = 'none';
}

// ===== JIGSAW MODE =====
function renderJigsawMode(container) {
    const puzzle = wordsState.puzzle;
    
    // Interleave words and numbers
    const pieces = [];
    puzzle.words.forEach(word => pieces.push({ type: 'word', value: word }));
    puzzle.values.forEach(val => pieces.push({ type: 'number', value: val }));
    
    // Shuffle
    for (let i = pieces.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [pieces[i], pieces[j]] = [pieces[j], pieces[i]];
    }
    
    container.innerHTML = `
        <div class="words-jigsaw-area" id="wordsJigsawArea">
            ${pieces.map((piece, idx) => `
                <div class="words-jigsaw-piece words-jigsaw-${piece.type}" 
                     data-type="${piece.type}"
                     data-value="${piece.value}"
                     data-index="${idx}"
                     onclick="selectJigsawPiece(this)">
                    ${piece.value}
                </div>
            `).join('')}
        </div>
    `;
}

function selectJigsawPiece(element) {
    if (element.classList.contains('matched')) return;
    
    const type = element.dataset.type;
    const value = element.dataset.value;
    
    if (type === 'word') {
        document.querySelectorAll('.words-jigsaw-word').forEach(el => el.classList.remove('selected'));
        element.classList.add('selected');
        wordsState.selectedWord = value;
    } else {
        document.querySelectorAll('.words-jigsaw-number').forEach(el => el.classList.remove('selected'));
        element.classList.add('selected');
        wordsState.selectedNumber = value;
    }
    
    // Check for match
    if (wordsState.selectedWord && wordsState.selectedNumber) {
        checkJigsawMatch();
    }
}

function checkJigsawMatch() {
    const puzzle = wordsState.puzzle;
    const word = wordsState.selectedWord;
    const value = wordsState.selectedNumber;
    
    if (puzzle.answer_key[word] === value) {
        // Match!
        const wordEl = document.querySelector(`.words-jigsaw-word[data-value="${word}"]`);
        const numEl = document.querySelector(`.words-jigsaw-number[data-value="${value}"]`);
        
        wordEl.classList.remove('selected');
        numEl.classList.remove('selected');
        wordEl.classList.add('matched');
        numEl.classList.add('matched');
        
        // Move them together visually
        wordEl.style.order = wordsState.matchedCount * 2;
        numEl.style.order = wordsState.matchedCount * 2 + 1;
        
        wordsState.matchedCount++;
        updateWordsProgress();
        
        if (typeof playSound === 'function') playSound('correct');
        
        if (wordsState.matchedCount >= wordsState.totalPairs) {
            setTimeout(showWordsCelebration, 500);
        }
    } else {
        if (typeof playSound === 'function') playSound('incorrect');
        
        document.querySelectorAll('.words-jigsaw-piece.selected').forEach(el => {
            el.style.animation = 'balloonWobble 0.3s ease';
            setTimeout(() => {
                el.style.animation = '';
                el.classList.remove('selected');
            }, 300);
        });
    }
    
    wordsState.selectedWord = null;
    wordsState.selectedNumber = null;
}

// ===== BALLOON MODE =====
function renderBalloonMode(container) {
    const puzzle = wordsState.puzzle;
    
    // Create balloons with random animation delays
    const balloons = [];
    puzzle.words.forEach(word => balloons.push({ type: 'word', value: word }));
    puzzle.values.forEach(val => balloons.push({ type: 'number', value: val }));
    
    // Shuffle
    for (let i = balloons.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [balloons[i], balloons[j]] = [balloons[j], balloons[i]];
    }
    
    container.innerHTML = `
        <div class="words-balloon-area" id="wordsBalloonArea">
            ${balloons.map((balloon, idx) => `
                <div class="words-balloon words-balloon-${balloon.type}" 
                     data-type="${balloon.type}"
                     data-value="${balloon.value}"
                     style="animation-delay: ${idx * 0.2}s"
                     onclick="selectBalloon(this)">
                    ${balloon.value}
                </div>
            `).join('')}
        </div>
    `;
}

function selectBalloon(element) {
    if (element.classList.contains('matched')) return;
    
    const type = element.dataset.type;
    const value = element.dataset.value;
    
    if (type === 'word') {
        document.querySelectorAll('.words-balloon-word').forEach(el => el.classList.remove('selected'));
        element.classList.add('selected');
        wordsState.selectedWord = value;
    } else {
        document.querySelectorAll('.words-balloon-number').forEach(el => el.classList.remove('selected'));
        element.classList.add('selected');
        wordsState.selectedNumber = value;
    }
    
    if (wordsState.selectedWord && wordsState.selectedNumber) {
        checkBalloonMatch();
    }
}

function checkBalloonMatch() {
    const puzzle = wordsState.puzzle;
    const word = wordsState.selectedWord;
    const value = wordsState.selectedNumber;
    
    if (puzzle.answer_key[word] === value) {
        // Pop both balloons!
        const wordEl = document.querySelector(`.words-balloon-word[data-value="${word}"]`);
        const numEl = document.querySelector(`.words-balloon-number[data-value="${value}"]`);
        
        wordEl.classList.remove('selected');
        numEl.classList.remove('selected');
        wordEl.classList.add('matched');
        numEl.classList.add('matched');
        
        // Remove after animation
        setTimeout(() => {
            wordEl.style.visibility = 'hidden';
            numEl.style.visibility = 'hidden';
        }, 400);
        
        wordsState.matchedCount++;
        updateWordsProgress();
        
        if (typeof playSound === 'function') playSound('correct');
        
        if (wordsState.matchedCount >= wordsState.totalPairs) {
            setTimeout(showWordsCelebration, 500);
        }
    } else {
        if (typeof playSound === 'function') playSound('incorrect');
        
        const selectedEls = document.querySelectorAll('.words-balloon.selected');
        selectedEls.forEach(el => {
            el.classList.add('wrong');
            setTimeout(() => {
                el.classList.remove('wrong', 'selected');
            }, 400);
        });
    }
    
    wordsState.selectedWord = null;
    wordsState.selectedNumber = null;
}

// ===== SHARED FUNCTIONS =====
function updateWordsProgress() {
    const progress = (wordsState.matchedCount / wordsState.totalPairs) * 100;
    document.getElementById('wordsProgressFill').style.width = `${progress}%`;
    document.getElementById('wordsMatchedValue').textContent = `${wordsState.matchedCount}/${wordsState.totalPairs}`;
}

function updateWordsTimer() {
    const minutes = Math.floor(wordsState.timeRemaining / 60);
    const seconds = wordsState.timeRemaining % 60;
    document.getElementById('wordsTimerValue').textContent = 
        `${minutes}:${seconds.toString().padStart(2, '0')}`;
    
    // Change color when low
    const timerEl = document.getElementById('wordsTimerValue');
    if (wordsState.timeRemaining <= 10) {
        timerEl.style.color = '#ef4444';
    } else if (wordsState.timeRemaining <= 30) {
        timerEl.style.color = '#f59e0b';
    } else {
        timerEl.style.color = '#7c3aed';
    }
}

function tickWordsTimer() {
    if (!wordsState.active) return;
    
    wordsState.timeRemaining--;
    updateWordsTimer();
    
    if (wordsState.timeRemaining <= 0) {
        // Time's up!
        clearInterval(wordsState.timerInterval);
        if (wordsState.matchedCount > 0) {
            showWordsCelebration();
        } else {
            alert('Time\'s up! Try again.');
            closeWords();
        }
    }
}

function showWordsCelebration() {
    if (wordsState.timerInterval) {
        clearInterval(wordsState.timerInterval);
    }
    
    const timeTaken = wordsState.timeLimit - wordsState.timeRemaining;
    let points = 5 + (wordsState.level * 2);
    
    // Time bonus
    if (wordsState.mode === 'balloon' && timeTaken < 30) {
        points += 5;
    } else if (timeTaken < 45) {
        points += 3;
    } else if (timeTaken < 60) {
        points += 1;
    }
    
    const perfect = wordsState.matchedCount >= wordsState.totalPairs;
    
    document.getElementById('wordsCelebrationSubtitle').textContent = 
        perfect ? `All ${wordsState.totalPairs} pairs matched! 🎯` : 
                  `${wordsState.matchedCount}/${wordsState.totalPairs} pairs matched`;
    document.getElementById('wordsCelebrationPoints').textContent = `+${points} Points`;
    
    document.getElementById('wordsCelebration').classList.add('active');
    
    if (typeof confetti === 'function' && perfect) {
        confetti({ particleCount: 150, spread: 90, origin: { y: 0.6 } });
    }
    
    saveWordsProgress(points);
}

function nextWords() {
    document.getElementById('wordsCelebration').classList.remove('active');
    const nextLevel = Math.min(wordsState.level + 1, 12);
    startWords(nextLevel);
}

async function resetWordsLevel() {
    if (confirm('Reset to Level 1? Your progress will be saved but you\'ll start from the beginning.')) {
        try {
            await fetch('/api/interactive/reset-level', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: 'words_to_numbers' })
            });
            wordsState.savedLevel = 1;
            startWords(1);
        } catch (e) {
            startWords(1);
        }
    }
}

function closeWords() {
    wordsState.active = false;
    
    if (wordsState.timerInterval) {
        clearInterval(wordsState.timerInterval);
    }
    
    document.getElementById('wordsContainer').classList.remove('active');
    document.getElementById('wordsCelebration').classList.remove('active');
}

async function saveWordsProgress(points) {
    const nextLevel = Math.min(wordsState.level + 1, 12);
    
    // Save level progress
    try {
        await fetch('/api/interactive/save-level', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic: 'words_to_numbers', level: nextLevel })
        });
        wordsState.savedLevel = nextLevel;
    } catch (e) {
        console.log('Could not save level progress');
    }
    
    try {
        await fetch('/api/words-to-numbers/complete', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                level: wordsState.level,
                mode: wordsState.mode,
                total_pairs: wordsState.totalPairs,
                correct_count: wordsState.matchedCount,
                time_taken: wordsState.timeLimit - wordsState.timeRemaining
            })
        });
    } catch (error) {
        console.log('Could not save words progress:', error);
    }
}

// =====================================================
// END WORDS TO NUMBERS
// =====================================================
