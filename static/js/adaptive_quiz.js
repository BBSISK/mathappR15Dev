/**
 * AgentMath - Adaptive Quiz System
 * Extracted from student_app.html for better maintainability
 * 
 * Revision: 1.0.0
 * Date: 2025-12-27
 * Source: student_app.html Revision 3.25.0
 * 
 * This file contains:
 * - Adaptive Quiz System (10-Level Progression)
 * - Interactive Number Games (Pyramids, Flow Sums, Times Tables, etc.)
 * - Code Breaker, Ordering, Place Value activities
 * - Double Trouble, Addition Blitz, Bonds games
 */

// ============================================================
// ADAPTIVE QUIZ SYSTEM - 10-Level Progression
// ============================================================

let adaptiveQuizState = {
    topic: null,
    topicName: null,
    numQuestions: 10,
    currentQuestion: null,
    questionNumber: 0,
    score: 0,
    currentLevel: 1,
    startingLevel: 1,
    streak: 0,
    selectedAnswer: null,
    isAnswered: false
};

const LEVEL_NAMES = {
    1: 'Foundation',
    2: 'Building Basics',
    3: 'Gaining Confidence',
    4: 'Developing Skills',
    5: 'Intermediate',
    6: 'Advancing',
    7: 'Strong Progress',
    8: 'Near Mastery',
    9: 'Expert Level',
    10: 'Champion!'
};

const TOPIC_ICONS = {
    // Numeracy Strand
    'whole_numbers': '🔢',
    'addition_subtraction': '➕',
    'multiplication_skills': '✖️',
    'division_skills': '➗',
    'basic_fractions': '🥧',
    'basic_decimals': '🔵',
    'basic_percentages': '💯',
    'time_and_clocks': '🕐',
    'money_skills': '💶',
    'measurement': '📏',
    'data_and_charts': '📊',
    'number_patterns': '🔄',
    // JC Exam Topics
    'arithmetic': '➕',
    'solving_equations': '🔢',
    'simultaneous_equations': '⚖️',
    'linear_inequalities': '≤',
    'fractions': '🥧',
    'percentages': '💯',
    'decimals': '🔢',
    'ratio': '⚖️',
    'sets': '⭕',
    'descriptive_statistics': '📊',
    'patterns': '🔷',
    'functions': '📈',
    'area_perimeter_volume': '📐',
    'probability': '🎲',
    'introductory_algebra': '📐',
    'applied_arithmetic': '💰',
    'currency': '💱',
    'speed_distance_time': '🏃',
    'simplifying_expressions': '📝',
    'expanding_factorising': '🔓',
    // LC Higher Level Strand
    'lc_hl_calculus_diff': '📈',
    'lc_hl_calculus_int': '📉',
    'lc_hl_algebra': '🔤',
    'lc_hl_sequences': '🔢',
    'lc_hl_complex': '🌀',
    'lc_hl_functions': '📊',
    'lc_hl_financial': '💰',
    'lc_hl_proof': '✓',
    'lc_hl_probability': '🎲',
    'lc_hl_statistics': '📊',
    'lc_hl_coord_geom': '📐',
    'lc_hl_trigonometry': '📐',
    'lc_hl_geometry': '🔺',
    'lc_hl_mensuration': '📦',
    'lc_hl_counting': '🔄'
};

const TOPIC_DISPLAY_NAMES = {
    // Numeracy Strand
    'whole_numbers': 'Whole Numbers',
    'addition_subtraction': 'Addition & Subtraction',
    'multiplication_skills': 'Multiplication',
    'division_skills': 'Division',
    'basic_fractions': 'Basic Fractions',
    'basic_decimals': 'Basic Decimals',
    'basic_percentages': 'Basic Percentages',
    'time_and_clocks': 'Time & Clocks',
    'money_skills': 'Money Skills',
    'measurement': 'Measurement',
    'data_and_charts': 'Data & Charts',
    'number_patterns': 'Number Patterns',
    'flow_sums': 'Flow Sums',
    'number_pyramids': 'Number Pyramids',
    'code_breaker': 'Code Breaker',
    'mastering_counting': 'Mastering Counting',
    'words_to_numbers': 'Words & Numbers',
    'ordering_magnitude': 'Ordering & Number Lines',
    'number_bonds': 'Number Bonds Pop',
    'place_value': 'Place Value Builder',
    'double_trouble': 'Double Trouble',
    'addition_blitz': 'Addition Blitz',
    'times_tables_blitz': 'Times Tables Blitz',
    // JC Exam Topics
    'arithmetic': 'Arithmetic',
    'solving_equations': 'Solving Equations',
    'simultaneous_equations': 'Simultaneous Equations',
    'linear_inequalities': 'Linear Inequalities',
    'fractions': 'Fractions',
    'percentages': 'Percentages',
    'decimals': 'Decimals',
    'ratio': 'Ratio',
    'sets': 'Sets & Venn Diagrams',
    'descriptive_statistics': 'Descriptive Statistics',
    'patterns': 'Patterns & Sequences',
    'functions': 'Functions',
    'area_perimeter_volume': 'Area, Perimeter & Volume',
    'probability': 'Probability',
    'introductory_algebra': 'Algebra',
    'applied_arithmetic': 'Applied Arithmetic',
    'currency': 'Currency',
    'speed_distance_time': 'Speed, Distance & Time',
    'simplifying_expressions': 'Simplifying Expressions',
    'expanding_factorising': 'Expanding & Factorising',
    // LC Higher Level Strand
    'lc_hl_calculus_diff': 'Calculus - Differentiation',
    'lc_hl_calculus_int': 'Calculus - Integration',
    'lc_hl_algebra': 'Algebra',
    'lc_hl_sequences': 'Sequences & Series',
    'lc_hl_complex': 'Complex Numbers',
    'lc_hl_functions': 'Functions',
    'lc_hl_financial': 'Financial Maths',
    'lc_hl_proof': 'Proof',
    'lc_hl_probability': 'Probability',
    'lc_hl_statistics': 'Statistics',
    'lc_hl_coord_geom': 'Coordinate Geometry',
    'lc_hl_trigonometry': 'Trigonometry',
    'lc_hl_geometry': 'Geometry',
    'lc_hl_mensuration': 'Mensuration',
    'lc_hl_counting': 'Counting & Combinatorics'
};

// Show guest message
function showAdaptiveQuizGuestMessage() {
    alert('🔒 Adaptive Quiz requires a Guest Code!\n\nAdaptive Quiz tracks your progress through 10 levels of difficulty.\n\nClick "Return with Code" on the home page to get your personal guest code, or register for a full account!');
}

// Show guest message for Team Play
function showTeamPlayGuestMessage() {
    alert('🔒 Team Play requires a Guest Code!\n\nTeam Play lets you quiz with friends and earn team bonuses.\n\nClick "Return with Code" on the home page to get your personal guest code, or register for a full account!');
}

// Open the modal
function showAdaptiveQuizModal() {
    document.getElementById('adaptiveQuizModal').classList.remove('hidden');
    loadAdaptiveTopics();
}

// Close the modal
function closeAdaptiveQuizModal() {
    document.getElementById('adaptiveQuizModal').classList.add('hidden');
    // Reset selection
    adaptiveQuizState.topic = null;
    document.getElementById('adaptiveTopicInfo').classList.add('hidden');
    document.getElementById('adaptiveOptionsSection').classList.add('hidden');
    document.getElementById('startAdaptiveBtn').disabled = true;
}

// Load available topics
async function loadAdaptiveTopics() {
    const grid = document.getElementById('adaptiveTopicGrid');
    
    try {
        const response = await fetch('/api/quiz-adaptive/topics');
        const data = await response.json();
        
        if (data.topics && data.topics.length > 0) {
            grid.innerHTML = data.topics.map(t => `
                <div class="adaptive-topic-card" onclick="selectAdaptiveTopic('${t.topic}', ${t.question_count})" data-topic="${t.topic}">
                    <div class="topic-icon">${TOPIC_ICONS[t.topic] || '📚'}</div>
                    <div class="topic-name">${TOPIC_DISPLAY_NAMES[t.topic] || t.topic}</div>
                    <div class="topic-questions">${t.question_count} questions</div>
                    <div class="topic-level">Levels ${t.min_level}-${t.max_level}</div>
                </div>
            `).join('');
        } else {
            grid.innerHTML = `
                <div class="text-center py-8 text-gray-500">
                    <div class="text-4xl mb-2">📭</div>
                    <p>No adaptive topics available yet.</p>
                    <p class="text-sm mt-2">Ask your teacher to generate adaptive questions!</p>
                </div>
            `;
        }
    } catch (error) {
        console.error('Error loading topics:', error);
        grid.innerHTML = `
            <div class="text-center py-8 text-red-500">
                <div class="text-4xl mb-2">⚠️</div>
                <p>Error loading topics</p>
            </div>
        `;
    }
}

// Select a topic
async function selectAdaptiveTopic(topic, questionCount) {
    // Update UI selection
    document.querySelectorAll('.adaptive-topic-card').forEach(card => {
        card.classList.remove('selected');
    });
    document.querySelector(`.adaptive-topic-card[data-topic="${topic}"]`).classList.add('selected');
    
    adaptiveQuizState.topic = topic;
    adaptiveQuizState.topicName = TOPIC_DISPLAY_NAMES[topic] || topic;
    
    // Get recommended level
    try {
        const response = await fetch(`/api/quiz-adaptive/recommended-level/${topic}`);
        const data = await response.json();
        
        adaptiveQuizState.startingLevel = data.level;
        adaptiveQuizState.currentLevel = data.level;
        
        // Update info display
        document.getElementById('adaptiveStartLevel').textContent = `Level ${data.level}`;
        document.getElementById('adaptiveQuestionCount').textContent = adaptiveQuizState.numQuestions;
        
        // Update level preview dots
        const previewContainer = document.getElementById('adaptiveLevelPreview');
        previewContainer.innerHTML = Array.from({length: 10}, (_, i) => {
            const level = i + 1;
            let dotClass = 'w-4 h-4 rounded-full ';
            if (level < data.level) {
                dotClass += 'bg-green-400';
            } else if (level === data.level) {
                dotClass += 'bg-purple-500 ring-2 ring-purple-300';
            } else {
                dotClass += 'bg-gray-200';
            }
            return `<div class="${dotClass}" title="Level ${level}"></div>`;
        }).join('');
        
    } catch (error) {
        console.error('Error getting recommended level:', error);
        adaptiveQuizState.startingLevel = 1;
        adaptiveQuizState.currentLevel = 1;
        document.getElementById('adaptiveStartLevel').textContent = 'Level 1';
    }
    
    // Show info sections
    document.getElementById('adaptiveTopicInfo').classList.remove('hidden');
    document.getElementById('adaptiveOptionsSection').classList.remove('hidden');
    document.getElementById('startAdaptiveBtn').disabled = false;
}

// Set question count
function setAdaptiveQuestionCount(count) {
    adaptiveQuizState.numQuestions = count;
    document.getElementById('adaptiveQuestionCount').textContent = count;
    
    // Update button styles
    document.querySelectorAll('.adaptive-count-btn').forEach(btn => {
        if (parseInt(btn.dataset.count) === count) {
            btn.classList.remove('border-gray-200');
            btn.classList.add('border-purple-400', 'bg-purple-50');
        } else {
            btn.classList.add('border-gray-200');
            btn.classList.remove('border-purple-400', 'bg-purple-50');
        }
    });
}

// Start the adaptive quiz
async function startAdaptiveQuiz() {
    if (!adaptiveQuizState.topic) return;
    
    try {
        const response = await fetch('/api/quiz-adaptive/start', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                topic: adaptiveQuizState.topic,
                num_questions: adaptiveQuizState.numQuestions,
                mode: 'adaptive'
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            // Update state
            adaptiveQuizState.currentLevel = data.starting_level;
            adaptiveQuizState.startingLevel = data.starting_level;
            adaptiveQuizState.questionNumber = 1;
            adaptiveQuizState.score = 0;
            adaptiveQuizState.streak = 0;
            adaptiveQuizState.currentQuestion = data.question;
            
            // Close modal, show quiz screen
            closeAdaptiveQuizModal();
            document.getElementById('adaptiveQuizScreen').classList.remove('hidden');
            
            // Initialize UI
            updateAdaptiveQuizUI();
            renderAdaptiveQuestion(data.question);
            renderLevelBar();
        } else {
            alert('Error starting quiz: ' + (data.error || 'Unknown error'));
        }
    } catch (error) {
        console.error('Error starting adaptive quiz:', error);
        alert('Could not start adaptive quiz. Please try again.');
    }
}

// Update quiz UI elements
function updateAdaptiveQuizUI() {
    document.getElementById('adaptiveQuizTitle').textContent = adaptiveQuizState.topicName;
    document.getElementById('adaptiveQuestionNum').textContent = adaptiveQuizState.questionNumber;
    document.getElementById('adaptiveTotalQuestions').textContent = adaptiveQuizState.numQuestions;
    document.getElementById('adaptiveCurrentLevel').textContent = adaptiveQuizState.currentLevel;
    document.getElementById('adaptiveScore').textContent = adaptiveQuizState.score;
    document.getElementById('adaptiveMaxScore').textContent = adaptiveQuizState.numQuestions;
    document.getElementById('adaptiveBannerLevel').textContent = adaptiveQuizState.currentLevel;
    document.getElementById('adaptiveLevelName').textContent = LEVEL_NAMES[adaptiveQuizState.currentLevel] || '';
    document.getElementById('adaptiveStreak').textContent = adaptiveQuizState.streak;
}

// Render level progress bar
function renderLevelBar() {
    const bar = document.getElementById('adaptiveLevelBar');
    bar.innerHTML = Array.from({length: 10}, (_, i) => {
        const level = i + 1;
        let classes = 'adaptive-level-dot';
        if (level < adaptiveQuizState.currentLevel) {
            classes += ' completed';
        } else if (level === adaptiveQuizState.currentLevel) {
            classes += ' active';
        }
        return `<div class="${classes}" title="Level ${level}"></div>`;
    }).join('');
}

// Render a question
function renderAdaptiveQuestion(question) {
    adaptiveQuizState.currentQuestion = question;
    adaptiveQuizState.selectedAnswer = null;
    adaptiveQuizState.isAnswered = false;
    
    // Handle image (SVG graphics)
    const imageContainer = document.getElementById('adaptiveQuestionImage');
    if (question.image_svg) {
        imageContainer.innerHTML = question.image_svg;
        imageContainer.classList.remove('hidden');
    } else {
        imageContainer.innerHTML = '';
        imageContainer.classList.add('hidden');
    }
    
    document.getElementById('adaptiveQuestionText').textContent = question.text;
    
    const container = document.getElementById('adaptiveOptionsContainer');
    container.innerHTML = question.options.map((opt, idx) => `
        <button class="adaptive-option w-full text-left p-4 rounded-xl border-2 border-gray-200 hover:border-purple-400 hover:bg-purple-50 transition-all flex items-center gap-3"
                onclick="selectAdaptiveAnswer(${idx})" data-index="${idx}">
            <span class="w-8 h-8 rounded-full bg-gray-200 flex items-center justify-center font-bold text-gray-600">
                ${String.fromCharCode(65 + idx)}
            </span>
            <span class="flex-1">${opt}</span>
        </button>
    `).join('');
    
    // Hide feedback and next button
    document.getElementById('adaptiveFeedback').classList.add('hidden');
    document.getElementById('adaptiveNextBtn').classList.add('hidden');
}

// Select an answer
function selectAdaptiveAnswer(index) {
    if (adaptiveQuizState.isAnswered) return;
    
    adaptiveQuizState.selectedAnswer = index;
    
    // Update button styles
    document.querySelectorAll('.adaptive-option').forEach((btn, i) => {
        btn.classList.remove('border-purple-500', 'bg-purple-100');
        if (i === index) {
            btn.classList.add('border-purple-500', 'bg-purple-100');
        }
    });
    
    // Submit the answer
    submitAdaptiveAnswer();
}

// Submit answer
async function submitAdaptiveAnswer() {
    if (adaptiveQuizState.selectedAnswer === null) return;
    
    adaptiveQuizState.isAnswered = true;
    const previousLevel = adaptiveQuizState.currentLevel;
    
    try {
        const response = await fetch('/api/quiz-adaptive/submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                answer: adaptiveQuizState.selectedAnswer,
                time_taken: 30
            })
        });
        
        const data = await response.json();
        
        // Update score
        if (data.correct) {
            adaptiveQuizState.score++;
            adaptiveQuizState.streak++;
        } else {
            adaptiveQuizState.streak = 0;
        }
        
        // Update level
        adaptiveQuizState.currentLevel = data.current_level;
        
        // Show feedback
        showAdaptiveFeedback(data);
        
        // Update UI
        updateAdaptiveQuizUI();
        renderLevelBar();
        
        // Highlight correct/incorrect answers
        document.querySelectorAll('.adaptive-option').forEach((btn, i) => {
            btn.classList.remove('hover:border-purple-400', 'hover:bg-purple-50');
            btn.style.cursor = 'default';
            
            if (i === data.correct_answer) {
                btn.classList.remove('border-gray-200', 'border-purple-500', 'bg-purple-100');
                btn.classList.add('border-green-500', 'bg-green-100');
                btn.querySelector('span:first-child').classList.remove('bg-gray-200');
                btn.querySelector('span:first-child').classList.add('bg-green-500', 'text-white');
            } else if (i === adaptiveQuizState.selectedAnswer && !data.correct) {
                btn.classList.remove('border-gray-200', 'border-purple-500', 'bg-purple-100');
                btn.classList.add('border-red-500', 'bg-red-100');
                btn.querySelector('span:first-child').classList.remove('bg-gray-200');
                btn.querySelector('span:first-child').classList.add('bg-red-500', 'text-white');
            }
        });
        
        // Show level change animation
        if (data.current_level !== previousLevel) {
            showLevelChangeToast(previousLevel, data.current_level);
        }
        
        // Check if quiz complete
        if (data.quiz_complete) {
            console.log('Quiz complete! Showing results...', data);
            // Hide next button, show results after a short delay
            document.getElementById('adaptiveNextBtn').classList.add('hidden');
            setTimeout(() => {
                showAdaptiveResults(data);
            }, 2500);
        } else {
            // Store next question
            adaptiveQuizState.currentQuestion = data.next_question;
            document.getElementById('adaptiveNextBtn').classList.remove('hidden');
        }
        
    } catch (error) {
        console.error('Error submitting answer:', error);
        alert('Error submitting answer. Please try again.');
    }
}

// Show feedback
function showAdaptiveFeedback(data) {
    const feedback = document.getElementById('adaptiveFeedback');
    const icon = document.getElementById('adaptiveFeedbackIcon');
    const title = document.getElementById('adaptiveFeedbackTitle');
    const explanation = document.getElementById('adaptiveFeedbackExplanation');
    
    feedback.classList.remove('hidden', 'bg-green-100', 'bg-red-100');
    
    if (data.correct) {
        feedback.classList.add('bg-green-100');
        icon.textContent = '✅';
        title.textContent = 'Correct! ' + getEncouragement(adaptiveQuizState.streak);
        title.className = 'font-bold text-lg mb-2 text-green-800';
    } else {
        feedback.classList.add('bg-red-100');
        icon.textContent = '❌';
        title.textContent = 'Not quite...';
        title.className = 'font-bold text-lg mb-2 text-red-800';
    }
    
    explanation.textContent = data.explanation;
}

// Get encouragement text
function getEncouragement(streak) {
    if (streak >= 5) return '🔥 On Fire!';
    if (streak >= 3) return '⭐ Great streak!';
    if (streak >= 2) return '👍 Keep it up!';
    return '';
}

// Show level change toast
function showLevelChangeToast(fromLevel, toLevel) {
    const isUp = toLevel > fromLevel;
    
    const toast = document.createElement('div');
    toast.className = `level-change-toast ${isUp ? 'level-up' : 'level-down'}`;
    toast.innerHTML = `
        <div class="text-5xl mb-3">${isUp ? '🚀' : '📚'}</div>
        <div class="text-2xl font-bold ${isUp ? 'text-green-600' : 'text-amber-600'}">
            ${isUp ? 'Level Up!' : 'Level Adjusted'}
        </div>
        <div class="text-4xl font-bold mt-2">
            ${fromLevel} → ${toLevel}
        </div>
        <div class="text-gray-600 mt-2">
            ${isUp ? LEVEL_NAMES[toLevel] : 'Let\'s practice more!'}
        </div>
    `;
    
    document.body.appendChild(toast);
    
    // Remove after animation
    setTimeout(() => {
        toast.style.animation = 'levelPopOut 0.3s ease forwards';
        setTimeout(() => toast.remove(), 300);
    }, 2000);
}

// Next question
function adaptiveNextQuestion() {
    if (adaptiveQuizState.currentQuestion) {
        adaptiveQuizState.questionNumber++;
        updateAdaptiveQuizUI();
        renderAdaptiveQuestion(adaptiveQuizState.currentQuestion);
    }
}

// Show results
function showAdaptiveResults(data) {
    document.getElementById('adaptiveQuizScreen').classList.add('hidden');
    document.getElementById('adaptiveResultsScreen').classList.remove('hidden');
    
    const percent = data.final_percentage;
    document.getElementById('adaptiveFinalScore').textContent = data.final_score;
    document.getElementById('adaptiveFinalTotal').textContent = adaptiveQuizState.numQuestions;
    document.getElementById('adaptiveFinalPercent').textContent = Math.round(percent);
    
    // Emoji based on performance
    let emoji = '🎉';
    if (percent >= 90) emoji = '🏆';
    else if (percent >= 70) emoji = '⭐';
    else if (percent >= 50) emoji = '👍';
    else emoji = '💪';
    document.getElementById('adaptiveResultEmoji').textContent = emoji;
    
    // Level progress
    document.getElementById('adaptiveStartLevelResult').textContent = data.starting_level;
    document.getElementById('adaptiveEndLevelResult').textContent = data.ending_level;
    
    const levelChange = data.ending_level - data.starting_level;
    const levelText = document.getElementById('adaptiveLevelChangeText');
    if (levelChange > 0) {
        levelText.textContent = `+${levelChange} Level${levelChange > 1 ? 's' : ''}! 🚀`;
        levelText.className = 'text-sm text-green-600 font-medium mt-2';
    } else if (levelChange < 0) {
        levelText.textContent = `${levelChange} Level${levelChange < -1 ? 's' : ''} - Keep practicing!`;
        levelText.className = 'text-sm text-amber-600 font-medium mt-2';
    } else {
        levelText.textContent = 'Steady progress! 💪';
        levelText.className = 'text-sm text-blue-600 font-medium mt-2';
    }
}

// Restart quiz
function restartAdaptiveQuiz() {
    document.getElementById('adaptiveResultsScreen').classList.add('hidden');
    showAdaptiveQuizModal();
}

// Close results
function closeAdaptiveResults() {
    document.getElementById('adaptiveResultsScreen').classList.add('hidden');
}

// Abandon quiz
async function abandonAdaptiveQuiz() {
    if (confirm('Are you sure you want to exit? Your progress will be lost.')) {
        try {
            await fetch('/api/quiz-adaptive/abandon', { method: 'POST' });
        } catch (e) {
            // Ignore errors
        }
        document.getElementById('adaptiveQuizScreen').classList.add('hidden');
    }
}

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

// =====================================================
// NUMBER BONDS POP - Interactive Activity
// =====================================================

const bondsState = {
    active: false, level: 1, puzzle: null,
    selectedBubble: null, pairsFound: 0, totalPairs: 0,
    startTime: null, timerInterval: null, savedLevel: 1
};

async function startBonds(level = null) {
    // If no level specified, fetch saved level
    if (level === null) {
        try {
            const response = await fetch('/api/interactive/get-level/number_bonds');
            const data = await response.json();
            level = data.level || 1;
            bondsState.savedLevel = level;
        } catch (e) {
            level = 1;
            bondsState.savedLevel = 1;
        }
    }
    
    bondsState.level = level;
    bondsState.pairsFound = 0;
    bondsState.selectedBubble = null;
    bondsState.active = true;
    bondsState.startTime = Date.now();
    
    document.getElementById('bondsLevel').textContent = `Level ${level}`;
    document.getElementById('bondsTime').textContent = '0:00';
    
    if (bondsState.timerInterval) clearInterval(bondsState.timerInterval);
    bondsState.timerInterval = setInterval(updateBondsTimer, 1000);
    
    try {
        const response = await fetch(`/api/number-bonds/question/${level}`);
        const data = await response.json();
        if (data.success) {
            bondsState.puzzle = data.puzzle;
            bondsState.totalPairs = data.puzzle.total_pairs;
            document.getElementById('bondsTarget').textContent = `Target: ${data.puzzle.target}`;
            document.getElementById('bondsPairsFound').textContent = `0/${bondsState.totalPairs}`;
            renderBondsBubbles();
        }
    } catch (error) {
        console.error('Error loading bonds puzzle:', error);
    }
    
    document.getElementById('bondsContainer').classList.add('active');
    if (typeof playSound === 'function') playSound('start');
}

function renderBondsBubbles() {
    const area = document.getElementById('bondsGameArea');
    const colors = ['#f472b6', '#c084fc', '#60a5fa', '#34d399', '#fbbf24', '#fb923c'];
    
    area.innerHTML = bondsState.puzzle.bubbles.map((b, i) => `
        <div class="bonds-bubble ${b.size}" 
             id="bubble-${b.id}"
             data-id="${b.id}" 
             data-value="${b.value}"
             style="left: ${b.x}%; top: ${b.y}%; background: ${colors[i % colors.length]}; animation-delay: ${i * 0.1}s;"
             onclick="selectBondsBubble(${b.id}, ${b.value})">
            ${b.value}
        </div>
    `).join('');
}

function selectBondsBubble(id, value) {
    const bubble = document.getElementById(`bubble-${id}`);
    if (!bubble || bubble.classList.contains('popping')) return;
    
    if (bondsState.selectedBubble === null) {
        bondsState.selectedBubble = { id, value };
        bubble.classList.add('selected');
        if (typeof playSound === 'function') playSound('click');
    } else {
        if (bondsState.selectedBubble.id === id) {
            bubble.classList.remove('selected');
            bondsState.selectedBubble = null;
            return;
        }
        
        const sum = bondsState.selectedBubble.value + value;
        if (sum === bondsState.puzzle.target) {
            // Correct pair!
            const firstBubble = document.getElementById(`bubble-${bondsState.selectedBubble.id}`);
            firstBubble.classList.remove('selected');
            firstBubble.classList.add('popping');
            bubble.classList.add('popping');
            
            bondsState.pairsFound++;
            document.getElementById('bondsPairsFound').textContent = `${bondsState.pairsFound}/${bondsState.totalPairs}`;
            
            if (typeof playSound === 'function') playSound('correct');
            
            if (bondsState.pairsFound >= bondsState.totalPairs) {
                setTimeout(showBondsCelebration, 500);
            }
        } else {
            // Wrong pair
            const firstBubble = document.getElementById(`bubble-${bondsState.selectedBubble.id}`);
            firstBubble.classList.remove('selected');
            firstBubble.classList.add('wrong');
            bubble.classList.add('wrong');
            if (typeof playSound === 'function') playSound('incorrect');
            setTimeout(() => {
                firstBubble.classList.remove('wrong');
                bubble.classList.remove('wrong');
            }, 400);
        }
        bondsState.selectedBubble = null;
    }
}

function updateBondsTimer() {
    if (!bondsState.startTime) return;
    const elapsed = Math.floor((Date.now() - bondsState.startTime) / 1000);
    const mins = Math.floor(elapsed / 60);
    const secs = elapsed % 60;
    document.getElementById('bondsTime').textContent = `${mins}:${secs.toString().padStart(2, '0')}`;
}

async function showBondsCelebration() {
    if (bondsState.timerInterval) clearInterval(bondsState.timerInterval);
    const timeTaken = Math.floor((Date.now() - bondsState.startTime) / 1000);
    const nextLevel = Math.min(bondsState.level + 1, 12);
    
    // Save level progress
    try {
        await fetch('/api/interactive/save-level', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic: 'number_bonds', level: nextLevel })
        });
        bondsState.savedLevel = nextLevel;
    } catch (e) {
        console.log('Could not save level progress');
    }
    
    try {
        const response = await fetch('/api/number-bonds/complete', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                level: bondsState.level,
                pairs_found: bondsState.pairsFound,
                total_pairs: bondsState.totalPairs,
                time_taken: timeTaken
            })
        });
        const data = await response.json();
        document.getElementById('bondsCelebrationSubtitle').textContent = `Completed in ${timeTaken} seconds!`;
        document.getElementById('bondsCelebrationPoints').textContent = `+${data.points_earned} Points`;
    } catch (e) {
        document.getElementById('bondsCelebrationSubtitle').textContent = `Completed in ${timeTaken} seconds!`;
        document.getElementById('bondsCelebrationPoints').textContent = `+${5 + bondsState.level * 2} Points`;
    }
    
    document.getElementById('bondsCelebration').classList.add('active');
    if (typeof confetti === 'function') confetti({ particleCount: 150, spread: 90 });
}

function nextBonds() {
    document.getElementById('bondsCelebration').classList.remove('active');
    startBonds(Math.min(bondsState.level + 1, 12));
}

async function resetBondsLevel() {
    if (confirm('Reset to Level 1? Your progress will be saved but you\'ll start from the beginning.')) {
        try {
            await fetch('/api/interactive/reset-level', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: 'number_bonds' })
            });
            bondsState.savedLevel = 1;
            startBonds(1);
        } catch (e) {
            startBonds(1);
        }
    }
}

function closeBonds() {
    bondsState.active = false;
    if (bondsState.timerInterval) clearInterval(bondsState.timerInterval);
    document.getElementById('bondsContainer').classList.remove('active');
    document.getElementById('bondsCelebration').classList.remove('active');
}

// =====================================================
// PLACE VALUE BUILDER - Interactive Activity
// =====================================================

const placevalueState = {
    active: false, level: 1, puzzle: null,
    selectedDigit: null, filledSlots: {}, attempts: 0,
    startTime: null, savedLevel: 1
};

async function startPlaceValue(level = null) {
    // If no level specified, fetch saved level
    if (level === null) {
        try {
            const response = await fetch('/api/interactive/get-level/place_value');
            const data = await response.json();
            level = data.level || 1;
            placevalueState.savedLevel = level;
        } catch (e) {
            level = 1;
            placevalueState.savedLevel = 1;
        }
    }
    
    placevalueState.level = level;
    placevalueState.selectedDigit = null;
    placevalueState.filledSlots = {};
    placevalueState.attempts = 0;
    placevalueState.active = true;
    placevalueState.startTime = Date.now();
    
    document.getElementById('placevalueLevelBadge').textContent = `Level ${level}`;
    
    try {
        const response = await fetch(`/api/place-value/question/${level}`);
        const data = await response.json();
        if (data.success) {
            placevalueState.puzzle = data.puzzle;
            document.getElementById('placevalueClue').textContent = data.puzzle.clue;
            renderPlaceValueColumns();
            renderPlaceValueDigits();
        }
    } catch (error) {
        console.error('Error loading place value puzzle:', error);
    }
    
    document.getElementById('placevalueContainer').classList.add('active');
    if (typeof playSound === 'function') playSound('start');
}

function renderPlaceValueColumns() {
    const puzzle = placevalueState.puzzle;
    const container = document.getElementById('placevalueColumns');
    
    let html = '';
    puzzle.places.forEach((place, idx) => {
        if (puzzle.has_decimal && place === 'tenths') {
            html += `<div class="placevalue-column"><div class="placevalue-column-label"></div><div class="placevalue-slot decimal-point">.</div></div>`;
        }
        const shortLabel = place.replace('_', ' ').split(' ').map(w => w[0].toUpperCase()).join('');
        const slotValue = placevalueState.filledSlots[place] !== undefined ? placevalueState.filledSlots[place].value : '?';
        html += `
            <div class="placevalue-column">
                <div class="placevalue-column-label">${shortLabel}</div>
                <div class="placevalue-slot" data-place="${place}" onclick="placeDigitInSlot('${place}')">${slotValue}</div>
            </div>
        `;
    });
    container.innerHTML = html;
    updatePlaceValueCheckButton();
}

function renderPlaceValueDigits() {
    const puzzle = placevalueState.puzzle;
    const container = document.getElementById('placevalueDigits');
    const usedIndices = Object.values(placevalueState.filledSlots).map(v => v.index).filter(i => i !== undefined);
    
    container.innerHTML = puzzle.available_digits.map((d, idx) => `
        <div class="placevalue-digit ${usedIndices.includes(idx) ? 'used' : ''}" 
             data-index="${idx}" 
             data-value="${d}"
             onclick="selectPlaceValueDigit(${idx}, ${d})">
            ${d}
        </div>
    `).join('');
}

function selectPlaceValueDigit(index, value) {
    const digits = document.querySelectorAll('.placevalue-digit');
    digits.forEach(d => d.classList.remove('selected'));
    
    const usedIndices = Object.values(placevalueState.filledSlots).map(v => v.index).filter(i => i !== undefined);
    if (usedIndices.includes(index)) return;
    
    document.querySelector(`.placevalue-digit[data-index="${index}"]`).classList.add('selected');
    placevalueState.selectedDigit = { index, value };
    if (typeof playSound === 'function') playSound('click');
}

function placeDigitInSlot(place) {
    if (placevalueState.selectedDigit === null) return;
    
    // If slot already filled, return old digit
    if (placevalueState.filledSlots[place] !== undefined) {
        delete placevalueState.filledSlots[place];
    }
    
    placevalueState.filledSlots[place] = {
        value: placevalueState.selectedDigit.value,
        index: placevalueState.selectedDigit.index
    };
    
    placevalueState.selectedDigit = null;
    renderPlaceValueColumns();
    renderPlaceValueDigits();
    if (typeof playSound === 'function') playSound('click');
}

function updatePlaceValueCheckButton() {
    const puzzle = placevalueState.puzzle;
    const allFilled = puzzle.places.every(p => placevalueState.filledSlots[p] !== undefined);
    document.getElementById('placevalueCheckBtn').disabled = !allFilled;
}

async function checkPlaceValue() {
    const puzzle = placevalueState.puzzle;
    placevalueState.attempts++;
    
    let allCorrect = true;
    puzzle.places.forEach(place => {
        const slot = document.querySelector(`.placevalue-slot[data-place="${place}"]`);
        const userValue = placevalueState.filledSlots[place]?.value;
        const correctValue = puzzle.digits[place];
        
        if (userValue === correctValue) {
            slot.classList.add('correct');
            slot.classList.remove('wrong');
        } else {
            slot.classList.add('wrong');
            slot.classList.remove('correct');
            allCorrect = false;
        }
    });
    
    if (allCorrect) {
        if (typeof playSound === 'function') playSound('correct');
        setTimeout(() => showPlaceValueCelebration(true), 500);
    } else {
        if (typeof playSound === 'function') playSound('incorrect');
        setTimeout(() => {
            document.querySelectorAll('.placevalue-slot.wrong').forEach(slot => {
                const place = slot.dataset.place;
                delete placevalueState.filledSlots[place];
            });
            renderPlaceValueColumns();
            renderPlaceValueDigits();
        }, 1000);
    }
}

async function showPlaceValueCelebration(correct) {
    const timeTaken = Math.floor((Date.now() - placevalueState.startTime) / 1000);
    const nextLevel = Math.min(placevalueState.level + 1, 12);
    
    // Save level progress
    if (correct) {
        try {
            await fetch('/api/interactive/save-level', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: 'place_value', level: nextLevel })
            });
            placevalueState.savedLevel = nextLevel;
        } catch (e) {
            console.log('Could not save level progress');
        }
    }
    
    try {
        const response = await fetch('/api/place-value/complete', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                level: placevalueState.level,
                correct: correct,
                time_taken: timeTaken,
                attempts: placevalueState.attempts
            })
        });
        const data = await response.json();
        document.getElementById('placevalueCelebrationSubtitle').textContent = `Built ${placevalueState.puzzle.target_number} in ${timeTaken}s!`;
        document.getElementById('placevalueCelebrationPoints').textContent = `+${data.points_earned} Points`;
    } catch (e) {
        document.getElementById('placevalueCelebrationSubtitle').textContent = `Built ${placevalueState.puzzle.target_number}!`;
        document.getElementById('placevalueCelebrationPoints').textContent = `+${5 + placevalueState.level * 2} Points`;
    }
    
    document.getElementById('placevalueCelebration').classList.add('active');
    if (typeof confetti === 'function') confetti({ particleCount: 150, spread: 90 });
}

function nextPlaceValue() {
    document.getElementById('placevalueCelebration').classList.remove('active');
    startPlaceValue(Math.min(placevalueState.level + 1, 12));
}

async function resetPlaceValueLevel() {
    if (confirm('Reset to Level 1? Your progress will be saved but you\'ll start from the beginning.')) {
        try {
            await fetch('/api/interactive/reset-level', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: 'place_value' })
            });
            placevalueState.savedLevel = 1;
            startPlaceValue(1);
        } catch (e) {
            startPlaceValue(1);
        }
    }
}

function closePlaceValue() {
    placevalueState.active = false;
    document.getElementById('placevalueContainer').classList.remove('active');
    document.getElementById('placevalueCelebration').classList.remove('active');
}

// =====================================================
// DOUBLE TROUBLE - Interactive Activity
// =====================================================

const doubleState = {
    active: false, level: 1, puzzle: null,
    currentIndex: 0, correctCount: 0, streak: 0, maxStreak: 0,
    startTime: null, questionTimer: null, timePerQuestion: 6, savedLevel: 1
};

async function startDouble(level = null) {
    // If no level specified, fetch saved level
    if (level === null) {
        try {
            const response = await fetch('/api/interactive/get-level/double_trouble');
            const data = await response.json();
            level = data.level || 1;
            doubleState.savedLevel = level;
        } catch (e) {
            level = 1;
            doubleState.savedLevel = 1;
        }
    }
    
    doubleState.level = level;
    doubleState.currentIndex = 0;
    doubleState.correctCount = 0;
    doubleState.streak = 0;
    doubleState.maxStreak = 0;
    doubleState.active = true;
    doubleState.startTime = Date.now();
    
    document.getElementById('doubleLevelStat').textContent = `Level ${level}`;
    document.getElementById('doubleCorrect').textContent = '0';
    document.getElementById('doubleStreakStat').textContent = '0';
    
    try {
        const response = await fetch(`/api/double-trouble/question/${level}`);
        const data = await response.json();
        if (data.success) {
            doubleState.puzzle = data.puzzle;
            doubleState.timePerQuestion = data.puzzle.time_per_question;
            showDoubleQuestion();
        }
    } catch (error) {
        console.error('Error loading double trouble:', error);
    }
    
    document.getElementById('doubleContainer').classList.add('active');
    if (typeof playSound === 'function') playSound('start');
}

function showDoubleQuestion() {
    const q = doubleState.puzzle.questions[doubleState.currentIndex];
    document.getElementById('doubleProgress').textContent = `Q ${doubleState.currentIndex + 1}/${doubleState.puzzle.total_questions}`;
    document.getElementById('doubleQuestion').textContent = q.question_text + ' = ?';
    document.getElementById('doubleInput').value = '';
    document.getElementById('doubleInput').className = 'double-input';
    document.getElementById('doubleInput').focus();
    document.getElementById('doubleStreak').textContent = doubleState.streak > 0 ? `🔥 ${doubleState.streak} streak!` : '';
    
    startDoubleTimer();
}

function startDoubleTimer() {
    if (doubleState.questionTimer) clearInterval(doubleState.questionTimer);
    
    let timeLeft = doubleState.timePerQuestion * 10;
    const fill = document.getElementById('doubleTimerFill');
    fill.style.width = '100%';
    fill.className = 'double-timer-fill';
    
    doubleState.questionTimer = setInterval(() => {
        timeLeft--;
        const percent = (timeLeft / (doubleState.timePerQuestion * 10)) * 100;
        fill.style.width = percent + '%';
        
        if (percent < 30) fill.className = 'double-timer-fill danger';
        else if (percent < 60) fill.className = 'double-timer-fill warning';
        
        if (timeLeft <= 0) {
            clearInterval(doubleState.questionTimer);
            handleDoubleTimeout();
        }
    }, 100);
}

function handleDoubleTimeout() {
    doubleState.streak = 0;
    document.getElementById('doubleStreakStat').textContent = '0';
    document.getElementById('doubleInput').classList.add('wrong');
    if (typeof playSound === 'function') playSound('incorrect');
    
    setTimeout(nextDoubleQuestion, 800);
}

function submitDoubleAnswer() {
    if (doubleState.questionTimer) clearInterval(doubleState.questionTimer);
    
    const input = document.getElementById('doubleInput');
    const userAnswer = parseFloat(input.value);
    const q = doubleState.puzzle.questions[doubleState.currentIndex];
    
    if (isNaN(userAnswer)) {
        handleDoubleTimeout();
        return;
    }
    
    if (Math.abs(userAnswer - q.answer) < 0.01) {
        input.classList.add('correct');
        doubleState.correctCount++;
        doubleState.streak++;
        if (doubleState.streak > doubleState.maxStreak) doubleState.maxStreak = doubleState.streak;
        document.getElementById('doubleCorrect').textContent = doubleState.correctCount;
        document.getElementById('doubleStreakStat').textContent = doubleState.streak;
        if (typeof playSound === 'function') playSound('correct');
    } else {
        input.classList.add('wrong');
        doubleState.streak = 0;
        document.getElementById('doubleStreakStat').textContent = '0';
        if (typeof playSound === 'function') playSound('incorrect');
    }
    
    setTimeout(nextDoubleQuestion, 600);
}

function nextDoubleQuestion() {
    doubleState.currentIndex++;
    if (doubleState.currentIndex >= doubleState.puzzle.total_questions) {
        showDoubleCelebration();
    } else {
        showDoubleQuestion();
    }
}

async function showDoubleCelebration() {
    const totalTime = Math.floor((Date.now() - doubleState.startTime) / 1000);
    const nextLevel = Math.min(doubleState.level + 1, 12);
    const accuracy = doubleState.correctCount / doubleState.puzzle.total_questions;
    
    // Save level progress if passed (70%+ accuracy)
    if (accuracy >= 0.7) {
        try {
            await fetch('/api/interactive/save-level', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: 'double_trouble', level: nextLevel })
            });
            doubleState.savedLevel = nextLevel;
        } catch (e) {
            console.log('Could not save level progress');
        }
    }
    
    try {
        const response = await fetch('/api/double-trouble/complete', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                level: doubleState.level,
                correct_count: doubleState.correctCount,
                total_questions: doubleState.puzzle.total_questions,
                total_time: totalTime
            })
        });
        const data = await response.json();
        const accuracyPct = Math.round(accuracy * 100);
        document.getElementById('doubleCelebrationSubtitle').textContent = `${doubleState.correctCount}/${doubleState.puzzle.total_questions} correct (${accuracyPct}%) • Best streak: ${doubleState.maxStreak}`;
        document.getElementById('doubleCelebrationPoints').textContent = `+${data.points_earned} Points`;
    } catch (e) {
        document.getElementById('doubleCelebrationSubtitle').textContent = `${doubleState.correctCount}/${doubleState.puzzle.total_questions} correct`;
        document.getElementById('doubleCelebrationPoints').textContent = `+${5 + doubleState.level * 2} Points`;
    }
    
    document.getElementById('doubleCelebration').classList.add('active');
    if (doubleState.correctCount >= doubleState.puzzle.total_questions && typeof confetti === 'function') {
        confetti({ particleCount: 200, spread: 100 });
    }
}

function nextDouble() {
    document.getElementById('doubleCelebration').classList.remove('active');
    startDouble(Math.min(doubleState.level + 1, 12));
}

async function resetDoubleLevel() {
    if (confirm('Reset to Level 1? Your progress will be saved but you\'ll start from the beginning.')) {
        try {
            await fetch('/api/interactive/reset-level', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: 'double_trouble' })
            });
            doubleState.savedLevel = 1;
            startDouble(1);
        } catch (e) {
            startDouble(1);
        }
    }
}

function closeDouble() {
    doubleState.active = false;
    if (doubleState.questionTimer) clearInterval(doubleState.questionTimer);
    document.getElementById('doubleContainer').classList.remove('active');
    document.getElementById('doubleCelebration').classList.remove('active');
}

// =====================================================
// ADDITION BLITZ - Speed Addition Tables Practice
// =====================================================

const additionBlitzState = {
    active: false, level: 1, savedLevel: 1, puzzle: null,
    currentIndex: 0, correctCount: 0, streak: 0, maxStreak: 0,
    startTime: null, questionTimer: null, timePerQuestion: 6
};

async function startAdditionBlitz(level = null) {
    // If no level specified, fetch saved level
    if (level === null) {
        try {
            const response = await fetch('/api/interactive/get-level/addition_blitz');
            const data = await response.json();
            level = data.level || 1;
            additionBlitzState.savedLevel = level;
        } catch (e) {
            level = 1;
            additionBlitzState.savedLevel = 1;
        }
    }
    
    additionBlitzState.level = level;
    additionBlitzState.currentIndex = 0;
    additionBlitzState.correctCount = 0;
    additionBlitzState.streak = 0;
    additionBlitzState.maxStreak = 0;
    additionBlitzState.active = true;
    additionBlitzState.startTime = Date.now();
    
    document.getElementById('additionBlitzLevelStat').textContent = `Level ${level}`;
    document.getElementById('additionBlitzCorrect').textContent = '0';
    document.getElementById('additionBlitzStreakStat').textContent = '0';
    
    try {
        const response = await fetch(`/api/addition-blitz/question/${level}`);
        const data = await response.json();
        if (data.success) {
            additionBlitzState.puzzle = data.puzzle;
            additionBlitzState.timePerQuestion = data.puzzle.time_per_question;
            showAdditionBlitzQuestion();
        }
    } catch (error) {
        console.error('Error loading addition blitz:', error);
    }
    
    document.getElementById('additionBlitzContainer').classList.add('active');
    if (typeof playSound === 'function') playSound('start');
}

function showAdditionBlitzQuestion() {
    const q = additionBlitzState.puzzle.questions[additionBlitzState.currentIndex];
    document.getElementById('additionBlitzQuestion').textContent = q.question_text;
    document.getElementById('additionBlitzProgress').textContent = 
        `${additionBlitzState.currentIndex + 1}/${additionBlitzState.puzzle.total_questions}`;
    
    const input = document.getElementById('additionBlitzInput');
    input.value = '';
    input.classList.remove('correct', 'wrong');
    input.focus();
    
    // Reset and start timer
    const timerFill = document.getElementById('additionBlitzTimerFill');
    timerFill.style.width = '100%';
    timerFill.classList.remove('warning', 'danger');
    
    if (additionBlitzState.questionTimer) clearInterval(additionBlitzState.questionTimer);
    
    const totalTime = additionBlitzState.timePerQuestion * 1000;
    const startTime = Date.now();
    
    additionBlitzState.questionTimer = setInterval(() => {
        const elapsed = Date.now() - startTime;
        const remaining = Math.max(0, totalTime - elapsed);
        const percent = (remaining / totalTime) * 100;
        
        timerFill.style.width = `${percent}%`;
        
        if (percent <= 30) {
            timerFill.classList.add('danger');
            timerFill.classList.remove('warning');
        } else if (percent <= 60) {
            timerFill.classList.add('warning');
        }
        
        if (remaining <= 0) {
            handleAdditionBlitzTimeout();
        }
    }, 100);
}

function submitAdditionBlitzAnswer() {
    const input = document.getElementById('additionBlitzInput');
    const userAnswer = parseFloat(input.value);
    const q = additionBlitzState.puzzle.questions[additionBlitzState.currentIndex];
    
    if (isNaN(userAnswer)) return;
    
    if (additionBlitzState.questionTimer) clearInterval(additionBlitzState.questionTimer);
    
    const correct = Math.abs(userAnswer - q.answer) < 0.01;
    
    if (correct) {
        input.classList.add('correct');
        additionBlitzState.correctCount++;
        additionBlitzState.streak++;
        additionBlitzState.maxStreak = Math.max(additionBlitzState.maxStreak, additionBlitzState.streak);
        document.getElementById('additionBlitzCorrect').textContent = additionBlitzState.correctCount;
        document.getElementById('additionBlitzStreakStat').textContent = additionBlitzState.streak + ' 🔥';
        if (typeof playSound === 'function') playSound('correct');
    } else {
        input.classList.add('wrong');
        additionBlitzState.streak = 0;
        document.getElementById('additionBlitzStreakStat').textContent = '0';
        if (typeof playSound === 'function') playSound('wrong');
    }
    
    setTimeout(() => nextAdditionBlitzQuestion(), 500);
}

function handleAdditionBlitzTimeout() {
    if (additionBlitzState.questionTimer) clearInterval(additionBlitzState.questionTimer);
    additionBlitzState.streak = 0;
    document.getElementById('additionBlitzStreakStat').textContent = '0';
    document.getElementById('additionBlitzInput').classList.add('wrong');
    if (typeof playSound === 'function') playSound('wrong');
    setTimeout(() => nextAdditionBlitzQuestion(), 500);
}

function nextAdditionBlitzQuestion() {
    additionBlitzState.currentIndex++;
    if (additionBlitzState.currentIndex >= additionBlitzState.puzzle.total_questions) {
        showAdditionBlitzCelebration();
    } else {
        showAdditionBlitzQuestion();
    }
}

async function showAdditionBlitzCelebration() {
    const totalTime = Math.floor((Date.now() - additionBlitzState.startTime) / 1000);
    const nextLevel = Math.min(additionBlitzState.level + 1, 12);
    const accuracy = additionBlitzState.correctCount / additionBlitzState.puzzle.total_questions;
    
    // Save level progress if passed (70%+ accuracy)
    if (accuracy >= 0.7) {
        try {
            await fetch('/api/interactive/save-level', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: 'addition_blitz', level: nextLevel })
            });
            additionBlitzState.savedLevel = nextLevel;
        } catch (e) {
            console.log('Could not save level progress');
        }
    }
    
    try {
        const response = await fetch('/api/addition-blitz/complete', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                level: additionBlitzState.level,
                correct_count: additionBlitzState.correctCount,
                total_questions: additionBlitzState.puzzle.total_questions,
                total_time: totalTime
            })
        });
        const data = await response.json();
        const accuracyPct = Math.round(accuracy * 100);
        document.getElementById('additionBlitzCelebrationSubtitle').textContent = 
            `${additionBlitzState.correctCount}/${additionBlitzState.puzzle.total_questions} correct (${accuracyPct}%) • Best streak: ${additionBlitzState.maxStreak}`;
        document.getElementById('additionBlitzCelebrationPoints').textContent = `+${data.points_earned} Points`;
    } catch (e) {
        document.getElementById('additionBlitzCelebrationSubtitle').textContent = 
            `${additionBlitzState.correctCount}/${additionBlitzState.puzzle.total_questions} correct`;
        document.getElementById('additionBlitzCelebrationPoints').textContent = `+${5 + additionBlitzState.level * 2} Points`;
    }
    
    document.getElementById('additionBlitzCelebration').classList.add('active');
    if (additionBlitzState.correctCount >= additionBlitzState.puzzle.total_questions && typeof confetti === 'function') {
        confetti({ particleCount: 200, spread: 100 });
    }
}

function nextAdditionBlitz() {
    document.getElementById('additionBlitzCelebration').classList.remove('active');
    startAdditionBlitz(Math.min(additionBlitzState.level + 1, 12));
}

async function resetAdditionBlitzLevel() {
    if (confirm('Reset to Level 1? Your progress will be saved but you\'ll start from the beginning.')) {
        try {
            await fetch('/api/interactive/reset-level', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: 'addition_blitz' })
            });
            additionBlitzState.savedLevel = 1;
            startAdditionBlitz(1);
        } catch (e) {
            startAdditionBlitz(1);
        }
    }
}

function closeAdditionBlitz() {
    additionBlitzState.active = false;
    if (additionBlitzState.questionTimer) clearInterval(additionBlitzState.questionTimer);
    document.getElementById('additionBlitzContainer').classList.remove('active');
    document.getElementById('additionBlitzCelebration').classList.remove('active');
}

// =====================================================
// TIMES TABLES BLITZ - Speed Multiplication Tables Practice
// =====================================================

const timesTablesState = {
    active: false, level: 1, savedLevel: 1, puzzle: null,
    currentIndex: 0, correctCount: 0, streak: 0, maxStreak: 0,
    startTime: null, questionTimer: null, timePerQuestion: 6
};

async function startTimesTablesBlitz(level = null) {
    // If no level specified, fetch saved level
    if (level === null) {
        try {
            const response = await fetch('/api/interactive/get-level/times_tables_blitz');
            const data = await response.json();
            level = data.level || 1;
            timesTablesState.savedLevel = level;
        } catch (e) {
            level = 1;
            timesTablesState.savedLevel = 1;
        }
    }
    
    timesTablesState.level = level;
    timesTablesState.currentIndex = 0;
    timesTablesState.correctCount = 0;
    timesTablesState.streak = 0;
    timesTablesState.maxStreak = 0;
    timesTablesState.active = true;
    timesTablesState.startTime = Date.now();
    
    document.getElementById('timesTablesLevelStat').textContent = `Level ${level}`;
    document.getElementById('timesTablesCorrect').textContent = '0';
    document.getElementById('timesTablesStreakStat').textContent = '0';
    
    try {
        const response = await fetch(`/api/times-tables/question/${level}`);
        const data = await response.json();
        if (data.success) {
            timesTablesState.puzzle = data.puzzle;
            timesTablesState.timePerQuestion = data.puzzle.time_per_question;
            showTimesTablesQuestion();
        }
    } catch (error) {
        console.error('Error loading times tables:', error);
    }
    
    document.getElementById('timesTablesContainer').classList.add('active');
    if (typeof playSound === 'function') playSound('start');
}

function showTimesTablesQuestion() {
    const q = timesTablesState.puzzle.questions[timesTablesState.currentIndex];
    document.getElementById('timesTablesQuestion').textContent = q.question_text;
    document.getElementById('timesTablesProgress').textContent = 
        `${timesTablesState.currentIndex + 1}/${timesTablesState.puzzle.total_questions}`;
    
    const input = document.getElementById('timesTablesInput');
    input.value = '';
    input.classList.remove('correct', 'wrong');
    input.focus();
    
    // Reset and start timer
    const timerFill = document.getElementById('timesTablesTimerFill');
    timerFill.style.width = '100%';
    timerFill.classList.remove('warning', 'danger');
    
    if (timesTablesState.questionTimer) clearInterval(timesTablesState.questionTimer);
    
    const totalTime = timesTablesState.timePerQuestion * 1000;
    const startTime = Date.now();
    
    timesTablesState.questionTimer = setInterval(() => {
        const elapsed = Date.now() - startTime;
        const remaining = Math.max(0, totalTime - elapsed);
        const percent = (remaining / totalTime) * 100;
        
        timerFill.style.width = `${percent}%`;
        
        if (percent <= 30) {
            timerFill.classList.add('danger');
            timerFill.classList.remove('warning');
        } else if (percent <= 60) {
            timerFill.classList.add('warning');
        }
        
        if (remaining <= 0) {
            handleTimesTablesTimeout();
        }
    }, 100);
}

function submitTimesTablesAnswer() {
    const input = document.getElementById('timesTablesInput');
    const userAnswer = parseFloat(input.value);
    const q = timesTablesState.puzzle.questions[timesTablesState.currentIndex];
    
    if (isNaN(userAnswer)) return;
    
    if (timesTablesState.questionTimer) clearInterval(timesTablesState.questionTimer);
    
    const correct = Math.abs(userAnswer - q.answer) < 0.01;
    
    if (correct) {
        input.classList.add('correct');
        timesTablesState.correctCount++;
        timesTablesState.streak++;
        timesTablesState.maxStreak = Math.max(timesTablesState.maxStreak, timesTablesState.streak);
        document.getElementById('timesTablesCorrect').textContent = timesTablesState.correctCount;
        document.getElementById('timesTablesStreakStat').textContent = timesTablesState.streak + ' 🔥';
        if (typeof playSound === 'function') playSound('correct');
    } else {
        input.classList.add('wrong');
        timesTablesState.streak = 0;
        document.getElementById('timesTablesStreakStat').textContent = '0';
        if (typeof playSound === 'function') playSound('wrong');
    }
    
    setTimeout(() => nextTimesTablesQuestion(), 500);
}

function handleTimesTablesTimeout() {
    if (timesTablesState.questionTimer) clearInterval(timesTablesState.questionTimer);
    timesTablesState.streak = 0;
    document.getElementById('timesTablesStreakStat').textContent = '0';
    document.getElementById('timesTablesInput').classList.add('wrong');
    if (typeof playSound === 'function') playSound('wrong');
    setTimeout(() => nextTimesTablesQuestion(), 500);
}

function nextTimesTablesQuestion() {
    timesTablesState.currentIndex++;
    if (timesTablesState.currentIndex >= timesTablesState.puzzle.total_questions) {
        showTimesTablesCelebration();
    } else {
        showTimesTablesQuestion();
    }
}

async function showTimesTablesCelebration() {
    const totalTime = Math.floor((Date.now() - timesTablesState.startTime) / 1000);
    const nextLevel = Math.min(timesTablesState.level + 1, 12);
    const accuracy = timesTablesState.correctCount / timesTablesState.puzzle.total_questions;
    
    // Save level progress if passed (70%+ accuracy)
    if (accuracy >= 0.7) {
        try {
            await fetch('/api/interactive/save-level', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: 'times_tables_blitz', level: nextLevel })
            });
            timesTablesState.savedLevel = nextLevel;
        } catch (e) {
            console.log('Could not save level progress');
        }
    }
    
    try {
        const response = await fetch('/api/times-tables/complete', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                level: timesTablesState.level,
                correct_count: timesTablesState.correctCount,
                total_questions: timesTablesState.puzzle.total_questions,
                total_time: totalTime
            })
        });
        const data = await response.json();
        const accuracyPct = Math.round(accuracy * 100);
        document.getElementById('timesTablesCelebrationSubtitle').textContent = 
            `${timesTablesState.correctCount}/${timesTablesState.puzzle.total_questions} correct (${accuracyPct}%) • Best streak: ${timesTablesState.maxStreak}`;
        document.getElementById('timesTablesCelebrationPoints').textContent = `+${data.points_earned} Points`;
    } catch (e) {
        document.getElementById('timesTablesCelebrationSubtitle').textContent = 
            `${timesTablesState.correctCount}/${timesTablesState.puzzle.total_questions} correct`;
        document.getElementById('timesTablesCelebrationPoints').textContent = `+${5 + timesTablesState.level * 2} Points`;
    }
    
    document.getElementById('timesTablesCelebration').classList.add('active');
    if (timesTablesState.correctCount >= timesTablesState.puzzle.total_questions && typeof confetti === 'function') {
        confetti({ particleCount: 200, spread: 100 });
    }
}

function nextTimesTables() {
    document.getElementById('timesTablesCelebration').classList.remove('active');
    startTimesTablesBlitz(Math.min(timesTablesState.level + 1, 12));
}

async function resetTimesTablesLevel() {
    if (confirm('Reset to Level 1? Your progress will be saved but you\'ll start from the beginning.')) {
        try {
            await fetch('/api/interactive/reset-level', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: 'times_tables_blitz' })
            });
            timesTablesState.savedLevel = 1;
            startTimesTablesBlitz(1);
        } catch (e) {
            startTimesTablesBlitz(1);
        }
    }
}

function closeTimesTables() {
    timesTablesState.active = false;
    if (timesTablesState.questionTimer) clearInterval(timesTablesState.questionTimer);
    document.getElementById('timesTablesContainer').classList.remove('active');
    document.getElementById('timesTablesCelebration').classList.remove('active');
}

// =====================================================
// END NEW GAMES
// =====================================================

