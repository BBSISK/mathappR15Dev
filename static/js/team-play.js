/**
 * Team Play - AgentMath Collaborative Quiz Feature
 * Version 1.1 - December 2025
 * Updated: All topics from Numeracy through Senior Cycle, bonus messaging
 */

// ==================== STATE ====================
const teamPlayState = {
    sessionCode: null,
    isOrganiser: false,
    currentQuestion: null,
    questionNumber: 0,
    totalQuestions: 10,
    myAnswer: null,
    isLockedIn: false,
    players: [],
    chat: [],
    pollInterval: null,
    lockInTimer: null,
    lockInSeconds: 15
};

// ==================== ALL TOPICS ====================
const TEAM_PLAY_TOPICS = {
    // Numeracy Strand
    'whole_numbers': 'Whole Numbers',
    'addition_subtraction': 'Addition & Subtraction',
    'multiplication_skills': 'Multiplication Skills',
    'division_skills': 'Division Skills',
    'basic_fractions': 'Basic Fractions',
    'basic_decimals': 'Basic Decimals',
    'basic_percentages': 'Basic Percentages',
    'time_and_clocks': 'Time & Clocks',
    'money_skills': 'Money Skills',
    'measurement': 'Measurement',
    'data_and_charts': 'Data & Charts',
    'number_patterns': 'Number Patterns',
    
    // L1LP Strand
    'awareness_of_environment': 'Awareness of Environment',
    'pattern_and_sequence': 'Pattern & Sequence',
    'developing_number_sense': 'Developing Number Sense',
    'shape_and_space': 'Shape & Space',
    'measure_and_data': 'Measure & Data',
    'time': 'Time',
    
    // L2LP Strand
    'l2_number_and_money': 'Number & Money (L2)',
    'l2_time_management': 'Time Management (L2)',
    'l2_measurement_location': 'Measurement & Location (L2)',
    'l2_shape_pattern_number': 'Shape, Pattern & Number (L2)',
    
    // Junior Cycle Strand
    'arithmetic': 'Arithmetic',
    'fractions': 'Fractions',
    'percentages': 'Percentages',
    'decimals': 'Decimals',
    'ratio': 'Ratio',
    'sets': 'Sets',
    'descriptive_statistics': 'Descriptive Statistics',
    'patterns': 'Patterns',
    'functions': 'Functions',
    'area_perimeter_volume': 'Area, Perimeter & Volume',
    'solving_equations': 'Solving Equations',
    'simultaneous_equations': 'Simultaneous Equations',
    'linear_inequalities': 'Linear Inequalities',
    'introductory_algebra': 'Introductory Algebra',
    'applied_arithmetic': 'Applied Arithmetic',
    'currency': 'Currency',
    'speed_distance_time': 'Speed, Distance & Time',
    'probability': 'Probability',
    'coordinate_geometry': 'Coordinate Geometry',
    'trigonometry': 'Trigonometry',
    'number_systems': 'Number Systems',
    'indices': 'Indices',
    'geometry': 'Geometry',
    'simplifying_expressions': 'Simplifying Expressions',
    'expanding_factorising': 'Expanding & Factorising',
    
    // Leaving Cert Higher Level
    'lc_hl_calculus_diff': 'Differentiation (HL)',
    'lc_hl_calculus_int': 'Integration (HL)',
    'lc_hl_algebra': 'Algebra (HL)',
    'lc_hl_sequences': 'Sequences & Series (HL)',
    'lc_hl_complex': 'Complex Numbers (HL)',
    'lc_hl_functions': 'Functions (HL)',
    'lc_hl_financial': 'Financial Maths (HL)',
    'lc_hl_proof': 'Proof (HL)',
    'lc_hl_probability': 'Probability (HL)',
    'lc_hl_statistics': 'Statistics (HL)',
    'lc_hl_coord_geom': 'Coordinate Geometry (HL)',
    'lc_hl_trigonometry': 'Trigonometry (HL)',
    'lc_hl_geometry': 'Geometry (HL)',
    'lc_hl_mensuration': 'Mensuration (HL)',
    'lc_hl_counting': 'Counting Principles (HL)',
    
    // Leaving Cert Ordinary Level
    'lc_ol_calculus': 'Calculus (OL)',
    'lc_ol_financial': 'Financial Maths (OL)',
    'lc_ol_trigonometry': 'Trigonometry (OL)',
    'lc_ol_mensuration': 'Mensuration (OL)',
    'lc_ol_statistics_desc': 'Descriptive Statistics (OL)',
    'lc_ol_probability': 'Probability (OL)',
    'lc_ol_applied_measure': 'Applied Measure (OL)',
    'lc_ol_sequences': 'Sequences & Series (OL)',
    'lc_ol_algebra': 'Algebra (OL)',
    'lc_ol_functions': 'Functions (OL)',
    'lc_ol_statistics_inf': 'Inferential Statistics (OL)',
    'lc_ol_coord_lines': 'Coordinate Geometry - Lines (OL)',
    'lc_ol_coord_circles': 'Coordinate Geometry - Circles (OL)',
    'lc_ol_complex': 'Complex Numbers (OL)',
    'lc_ol_geometry': 'Geometry (OL)'
};

// ==================== UI RENDERING ====================

function renderTeamPlayCard() {
    // This creates the Team Play card for the sidebar
    return `
        <div class="team-play-card" id="teamPlayCard">
            <div class="team-play-header">
                <span class="team-play-icon">👥</span>
                <span class="team-play-title">Team Play</span>
                <span class="team-play-badge">NEW</span>
            </div>
            <div class="team-play-bonus-banner">
                <span class="bonus-icon">🎁</span>
                <span class="bonus-text">Team Players earn <strong>up to 50% bonus points!</strong></span>
            </div>
            <div class="team-play-description">
                Play quizzes together with friends. Answer questions, chat live, and earn team bonuses!
            </div>
            <div class="team-play-bonus-details">
                <div class="bonus-tier"><span class="players">2 players</span><span class="bonus">+10%</span></div>
                <div class="bonus-tier"><span class="players">3 players</span><span class="bonus">+25%</span></div>
                <div class="bonus-tier"><span class="players">4 players</span><span class="bonus">+50%</span></div>
            </div>
            <div class="team-play-buttons">
                <button class="team-play-btn create" onclick="showTeamPlaySetup()">
                    <i class="fas fa-plus"></i> Create
                </button>
                <button class="team-play-btn join" onclick="showJoinTeamPlay()">
                    <i class="fas fa-sign-in-alt"></i> Join
                </button>
            </div>
        </div>
    `;
}

function showTeamPlaySetup() {
    const topicOptions = Object.entries(TEAM_PLAY_TOPICS)
        .map(([key, name]) => `<option value="${key}">${name}</option>`)
        .join('');
    
    const modal = document.createElement('div');
    modal.className = 'team-play-modal';
    modal.id = 'teamPlaySetupModal';
    modal.innerHTML = `
        <div class="team-play-modal-content">
            <div class="team-play-modal-header">
                <span>👥 Start Team Play</span>
                <button class="team-play-close" onclick="closeTeamPlayModal()">×</button>
            </div>
            <div class="team-play-modal-body">
                <div class="team-play-bonus-highlight">
                    <div class="bonus-highlight-icon">🏆</div>
                    <div class="bonus-highlight-text">
                        <strong>Team Bonus!</strong> Earn up to 50% extra points when everyone gets the answer right!
                    </div>
                </div>
                
                <div class="team-play-form-group">
                    <label>Topic</label>
                    <select id="teamPlayTopic">
                        <optgroup label="📊 Numeracy">
                            <option value="whole_numbers">Whole Numbers</option>
                            <option value="addition_subtraction">Addition & Subtraction</option>
                            <option value="multiplication_skills">Multiplication Skills</option>
                            <option value="division_skills">Division Skills</option>
                            <option value="basic_fractions">Basic Fractions</option>
                            <option value="basic_decimals">Basic Decimals</option>
                            <option value="basic_percentages">Basic Percentages</option>
                            <option value="time_and_clocks">Time & Clocks</option>
                            <option value="money_skills">Money Skills</option>
                            <option value="measurement">Measurement</option>
                            <option value="data_and_charts">Data & Charts</option>
                            <option value="number_patterns">Number Patterns</option>
                        </optgroup>
                        <optgroup label="🌱 L1 Learning Programme">
                            <option value="awareness_of_environment">Awareness of Environment</option>
                            <option value="pattern_and_sequence">Pattern & Sequence</option>
                            <option value="developing_number_sense">Developing Number Sense</option>
                            <option value="shape_and_space">Shape & Space</option>
                            <option value="measure_and_data">Measure & Data</option>
                            <option value="time">Time</option>
                        </optgroup>
                        <optgroup label="🌿 L2 Learning Programme">
                            <option value="l2_number_and_money">Number & Money</option>
                            <option value="l2_time_management">Time Management</option>
                            <option value="l2_measurement_location">Measurement & Location</option>
                            <option value="l2_shape_pattern_number">Shape, Pattern & Number</option>
                        </optgroup>
                        <optgroup label="📐 Junior Cycle">
                            <option value="arithmetic" selected>Arithmetic</option>
                            <option value="fractions">Fractions</option>
                            <option value="percentages">Percentages</option>
                            <option value="decimals">Decimals</option>
                            <option value="ratio">Ratio</option>
                            <option value="sets">Sets</option>
                            <option value="descriptive_statistics">Descriptive Statistics</option>
                            <option value="patterns">Patterns</option>
                            <option value="functions">Functions</option>
                            <option value="area_perimeter_volume">Area, Perimeter & Volume</option>
                            <option value="solving_equations">Solving Equations</option>
                            <option value="simultaneous_equations">Simultaneous Equations</option>
                            <option value="linear_inequalities">Linear Inequalities</option>
                            <option value="introductory_algebra">Introductory Algebra</option>
                            <option value="applied_arithmetic">Applied Arithmetic</option>
                            <option value="currency">Currency</option>
                            <option value="speed_distance_time">Speed, Distance & Time</option>
                            <option value="probability">Probability</option>
                            <option value="coordinate_geometry">Coordinate Geometry</option>
                            <option value="trigonometry">Trigonometry</option>
                            <option value="number_systems">Number Systems</option>
                            <option value="indices">Indices</option>
                            <option value="geometry">Geometry</option>
                            <option value="simplifying_expressions">Simplifying Expressions</option>
                            <option value="expanding_factorising">Expanding & Factorising</option>
                        </optgroup>
                        <optgroup label="🎓 Leaving Cert Higher Level">
                            <option value="lc_hl_calculus_diff">Differentiation</option>
                            <option value="lc_hl_calculus_int">Integration</option>
                            <option value="lc_hl_algebra">Algebra</option>
                            <option value="lc_hl_sequences">Sequences & Series</option>
                            <option value="lc_hl_complex">Complex Numbers</option>
                            <option value="lc_hl_functions">Functions</option>
                            <option value="lc_hl_financial">Financial Maths</option>
                            <option value="lc_hl_proof">Proof</option>
                            <option value="lc_hl_probability">Probability</option>
                            <option value="lc_hl_statistics">Statistics</option>
                            <option value="lc_hl_coord_geom">Coordinate Geometry</option>
                            <option value="lc_hl_trigonometry">Trigonometry</option>
                            <option value="lc_hl_geometry">Geometry</option>
                            <option value="lc_hl_mensuration">Mensuration</option>
                            <option value="lc_hl_counting">Counting Principles</option>
                        </optgroup>
                        <optgroup label="📚 Leaving Cert Ordinary Level">
                            <option value="lc_ol_calculus">Calculus</option>
                            <option value="lc_ol_financial">Financial Maths</option>
                            <option value="lc_ol_trigonometry">Trigonometry</option>
                            <option value="lc_ol_mensuration">Mensuration</option>
                            <option value="lc_ol_statistics_desc">Descriptive Statistics</option>
                            <option value="lc_ol_probability">Probability</option>
                            <option value="lc_ol_applied_measure">Applied Measure</option>
                            <option value="lc_ol_sequences">Sequences & Series</option>
                            <option value="lc_ol_algebra">Algebra</option>
                            <option value="lc_ol_functions">Functions</option>
                            <option value="lc_ol_statistics_inf">Inferential Statistics</option>
                            <option value="lc_ol_coord_lines">Coord Geometry - Lines</option>
                            <option value="lc_ol_coord_circles">Coord Geometry - Circles</option>
                            <option value="lc_ol_complex">Complex Numbers</option>
                            <option value="lc_ol_geometry">Geometry</option>
                        </optgroup>
                    </select>
                </div>
                
                <div class="team-play-form-group">
                    <label>Difficulty Levels</label>
                    <select id="teamPlayLevels">
                        <option value="1-12">All Levels (1-12)</option>
                        <option value="1-4">Beginner (1-4)</option>
                        <option value="5-8">Intermediate (5-8)</option>
                        <option value="9-12">Advanced (9-12)</option>
                    </select>
                </div>
                
                <div class="team-play-form-group">
                    <label>Number of Questions</label>
                    <select id="teamPlayQuestions">
                        <option value="5">5 Questions (Quick)</option>
                        <option value="10" selected>10 Questions (Standard)</option>
                        <option value="15">15 Questions (Extended)</option>
                        <option value="20">20 Questions (Marathon)</option>
                    </select>
                </div>
                
                <button class="team-play-create-btn" onclick="createTeamSession()">
                    Create Session
                </button>
            </div>
        </div>
    `;
    document.body.appendChild(modal);
}

function showJoinTeamPlay() {
    const modal = document.createElement('div');
    modal.className = 'team-play-modal';
    modal.id = 'teamPlayJoinModal';
    modal.innerHTML = `
        <div class="team-play-modal-content">
            <div class="team-play-modal-header">
                <span>🔗 Join Team Play</span>
                <button class="team-play-close" onclick="closeTeamPlayModal()">×</button>
            </div>
            <div class="team-play-modal-body">
                <div class="team-play-bonus-highlight">
                    <div class="bonus-highlight-icon">🎁</div>
                    <div class="bonus-highlight-text">
                        Join a team and earn <strong>bonus points</strong> when you all answer correctly!
                    </div>
                </div>
                
                <div class="team-play-form-group">
                    <label>Enter Session Code</label>
                    <input type="text" id="teamPlayCode" placeholder="e.g., FOX-247" 
                           maxlength="7" style="text-transform: uppercase; text-align: center; font-size: 1.5rem; letter-spacing: 2px;"
                           oninput="this.value = this.value.toUpperCase()">
                </div>
                
                <button class="team-play-join-btn" onclick="joinTeamSession()">
                    Join Session
                </button>
            </div>
        </div>
    `;
    document.body.appendChild(modal);
    
    // Focus on input
    setTimeout(() => {
        document.getElementById('teamPlayCode')?.focus();
    }, 100);
}

function closeTeamPlayModal() {
    const modals = document.querySelectorAll('.team-play-modal');
    modals.forEach(m => m.remove());
}

// ==================== API CALLS ====================

async function createTeamSession() {
    const topic = document.getElementById('teamPlayTopic').value;
    const levels = document.getElementById('teamPlayLevels').value;
    const questions = parseInt(document.getElementById('teamPlayQuestions').value);
    
    if (!topic) {
        alert('Please select a topic');
        return;
    }
    
    try {
        const response = await fetch('/api/team/create-session', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                topic: topic,
                difficulty_levels: levels,
                question_count: questions
            })
        });
        
        const data = await response.json();
        
        if (data.error) {
            alert(data.error);
            return;
        }
        
        if (data.session_code) {
            teamPlayState.sessionCode = data.session_code;
            teamPlayState.isOrganiser = true;
            teamPlayState.totalQuestions = questions;
            closeTeamPlayModal();
            showWaitingRoom(data.session_code);
        } else {
            alert('Failed to create session. Please try again.');
        }
    } catch (error) {
        console.error('Create session error:', error);
        alert('Failed to create session. Please try again.');
    }
}

async function joinTeamSession() {
    const code = document.getElementById('teamPlayCode').value.trim().toUpperCase();
    
    if (!code || code.length < 5) {
        alert('Please enter a valid session code');
        return;
    }
    
    try {
        const response = await fetch(`/api/team/session/${code}/join`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        
        const data = await response.json();
        
        if (data.error) {
            alert(data.error);
            return;
        }
        
        teamPlayState.sessionCode = code;
        teamPlayState.isOrganiser = false;
        closeTeamPlayModal();
        showWaitingRoom(code);
    } catch (error) {
        console.error('Join session error:', error);
        alert('Failed to join session. Please check the code and try again.');
    }
}

// ==================== WAITING ROOM ====================

function showWaitingRoom(code) {
    const modal = document.createElement('div');
    modal.className = 'team-play-modal team-play-fullscreen';
    modal.id = 'teamPlayWaitingRoom';
    modal.innerHTML = `
        <div class="team-play-waiting-room">
            <div class="waiting-room-header">
                <h2>👥 Team Play - Waiting Room</h2>
                <div class="session-code-display">
                    <span class="code-label">Session Code:</span>
                    <span class="code-value" onclick="copySessionCode('${code}')">${code}</span>
                    <button class="copy-btn" onclick="copySessionCode('${code}')">📋 Copy</button>
                </div>
            </div>
            
            <div class="waiting-room-content">
                <div class="players-section">
                    <h3>Players</h3>
                    <div id="waitingRoomPlayers" class="players-list">
                        <div class="loading">Loading players...</div>
                    </div>
                    <div class="bonus-reminder">
                        <span class="bonus-icon">💰</span>
                        <span>More players = bigger bonus! Up to 50% extra points with 4 players</span>
                    </div>
                </div>
                
                <div class="chat-section">
                    <h3>Team Chat</h3>
                    <div id="waitingRoomChat" class="chat-messages"></div>
                    <div class="chat-input-area">
                        <input type="text" id="chatInput" placeholder="Say hello to your team..." maxlength="150"
                               onkeypress="if(event.key==='Enter')sendChatMessage()">
                        <button onclick="sendChatMessage()">Send</button>
                    </div>
                </div>
            </div>
            
            <div class="waiting-room-footer">
                ${teamPlayState.isOrganiser ? `
                    <button class="start-quiz-btn" id="startQuizBtn" onclick="startTeamQuiz()" disabled>
                        Start Quiz (Need 2+ players)
                    </button>
                ` : `
                    <div class="waiting-message">Waiting for host to start the quiz...</div>
                `}
                <button class="leave-btn" onclick="leaveTeamSession()">Leave Session</button>
            </div>
        </div>
    `;
    document.body.appendChild(modal);
    
    // Start polling
    startPolling();
}

function copySessionCode(code) {
    navigator.clipboard.writeText(code).then(() => {
        // Show feedback
        const codeEl = document.querySelector('.code-value');
        if (codeEl) {
            const original = codeEl.textContent;
            codeEl.textContent = 'Copied!';
            setTimeout(() => { codeEl.textContent = original; }, 1500);
        }
    });
}

// ==================== POLLING ====================

function startPolling() {
    // Poll every 2 seconds
    teamPlayState.pollInterval = setInterval(pollSessionStatus, 2000);
    pollSessionStatus(); // Initial poll
}

function stopPolling() {
    if (teamPlayState.pollInterval) {
        clearInterval(teamPlayState.pollInterval);
        teamPlayState.pollInterval = null;
    }
}

async function pollSessionStatus() {
    if (!teamPlayState.sessionCode) return;
    
    try {
        const response = await fetch(`/api/team/session/${teamPlayState.sessionCode}/status`);
        const data = await response.json();
        
        if (data.error) {
            console.error('Poll error:', data.error);
            return;
        }
        
        // Update players
        teamPlayState.players = data.players || [];
        updatePlayersDisplay();
        
        // Update chat
        if (data.chat) {
            teamPlayState.chat = data.chat;
            updateChatDisplay();
        }
        
        // Check if quiz started
        if (data.status === 'active' && !teamPlayState.currentQuestion) {
            loadCurrentQuestion();
        }
        
        // Enable start button if enough players
        const startBtn = document.getElementById('startQuizBtn');
        if (startBtn && teamPlayState.isOrganiser) {
            const canStart = teamPlayState.players.length >= 2;
            startBtn.disabled = !canStart;
            startBtn.textContent = canStart ? 
                `Start Quiz (${teamPlayState.players.length} players)` : 
                `Start Quiz (Need 2+ players)`;
        }
        
    } catch (error) {
        console.error('Poll error:', error);
    }
}

function updatePlayersDisplay() {
    const container = document.getElementById('waitingRoomPlayers');
    if (!container) return;
    
    if (teamPlayState.players.length === 0) {
        container.innerHTML = '<div class="no-players">No players yet</div>';
        return;
    }
    
    const avatarColors = ['#8b5cf6', '#ec4899', '#06b6d4', '#22c55e', '#f59e0b'];
    
    container.innerHTML = teamPlayState.players.map((player, idx) => `
        <div class="player-item ${player.is_organiser ? 'organiser' : ''}">
            <div class="player-avatar" style="background: ${avatarColors[idx % avatarColors.length]}">
                ${player.display_name.charAt(0).toUpperCase()}
            </div>
            <div class="player-name">${player.display_name}</div>
            ${player.is_organiser ? '<span class="host-badge">Host</span>' : ''}
        </div>
    `).join('');
}

function updateChatDisplay() {
    const container = document.getElementById('waitingRoomChat');
    if (!container) return;
    
    container.innerHTML = teamPlayState.chat.map(msg => `
        <div class="chat-message">
            <span class="chat-player">${msg.player}:</span>
            <span class="chat-text">${msg.message}</span>
        </div>
    `).join('');
    
    // Scroll to bottom
    container.scrollTop = container.scrollHeight;
}

async function sendChatMessage() {
    const input = document.getElementById('chatInput');
    const message = input.value.trim();
    
    if (!message || !teamPlayState.sessionCode) return;
    
    try {
        await fetch(`/api/team/session/${teamPlayState.sessionCode}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        });
        input.value = '';
    } catch (error) {
        console.error('Chat error:', error);
    }
}

// ==================== QUIZ FLOW ====================

async function startTeamQuiz() {
    if (!teamPlayState.isOrganiser) return;
    
    try {
        const response = await fetch(`/api/team/session/${teamPlayState.sessionCode}/start`, {
            method: 'POST'
        });
        const data = await response.json();
        
        if (data.error) {
            alert(data.error);
            return;
        }
        
        loadCurrentQuestion();
    } catch (error) {
        console.error('Start quiz error:', error);
        alert('Failed to start quiz');
    }
}

async function loadCurrentQuestion() {
    // This would load the current question from the server
    // Implementation depends on how questions are served
    console.log('Loading current question...');
    // For now, close waiting room and show quiz UI
    closeTeamPlayModal();
    // The actual quiz UI would be shown here
}

async function leaveTeamSession() {
    if (!teamPlayState.sessionCode) return;
    
    if (!confirm('Are you sure you want to leave the session?')) return;
    
    try {
        await fetch(`/api/team/session/${teamPlayState.sessionCode}/leave`, {
            method: 'POST'
        });
    } catch (error) {
        console.error('Leave error:', error);
    }
    
    stopPolling();
    teamPlayState.sessionCode = null;
    teamPlayState.isOrganiser = false;
    teamPlayState.players = [];
    closeTeamPlayModal();
}

// ==================== INITIALIZATION ====================

function initTeamPlay() {
    console.log('Team Play initialized');
    // Check for pending invitations
    checkInvitations();
}

async function checkInvitations() {
    try {
        const response = await fetch('/api/team/invitations');
        const data = await response.json();
        
        if (data.invitations && data.invitations.length > 0) {
            showInvitationPopup(data.invitations[0]);
        }
    } catch (error) {
        // Silently fail - invitations are optional
    }
}

function showInvitationPopup(invitation) {
    const popup = document.createElement('div');
    popup.className = 'team-play-invitation-popup';
    popup.innerHTML = `
        <div class="invitation-content">
            <div class="invitation-icon">👥</div>
            <div class="invitation-text">
                <strong>${invitation.from_player}</strong> invited you to Team Play!
            </div>
            <div class="invitation-buttons">
                <button onclick="acceptInvitation(${invitation.id})">Join</button>
                <button onclick="declineInvitation(${invitation.id})" class="decline">Decline</button>
            </div>
        </div>
    `;
    document.body.appendChild(popup);
    
    // Auto-hide after 30 seconds
    setTimeout(() => popup.remove(), 30000);
}

async function acceptInvitation(inviteId) {
    try {
        const response = await fetch(`/api/team/invitation/${inviteId}/accept`, {
            method: 'POST'
        });
        const data = await response.json();
        
        if (data.session_code) {
            teamPlayState.sessionCode = data.session_code;
            document.querySelector('.team-play-invitation-popup')?.remove();
            showWaitingRoom(data.session_code);
        }
    } catch (error) {
        console.error('Accept invitation error:', error);
    }
}

async function declineInvitation(inviteId) {
    try {
        await fetch(`/api/team/invitation/${inviteId}/decline`, {
            method: 'POST'
        });
    } catch (error) {
        console.error('Decline invitation error:', error);
    }
    document.querySelector('.team-play-invitation-popup')?.remove();
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTeamPlay);
} else {
    initTeamPlay();
}
