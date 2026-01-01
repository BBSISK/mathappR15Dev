/**
 * AgentMath Student App - Main JavaScript
 * Extracted from student_app.html for better maintainability
 * 
 * Revision: 1.0.0
 * Date: 2025-12-27
 * Source: student_app.html Revision 3.24.0
 * 
 * This file contains the core quiz functionality including:
 * - Topic selection and quiz loading
 * - Question display and answer handling
 * - Score tracking and progress saving
 * - Badge system integration
 * - Interactive activities (pyramids, flow sums, etc.)
 */

        let currentTopic = '';
        let currentDifficulty = '';
        let questions = [];
        let currentQuestionIndex = 0;
        let score = 0;
        let answered = false;
        let startTime = null;
        
        // Milestone Tracking (Client-Side for ALL users)
        let consecutiveCorrect = 0;
        let maxConsecutiveCorrect = 0;
        let questionsAnsweredInQuiz = 0;
        let shownMilestones = new Set(); // Track which milestones shown this quiz
        let totalMilestonePoints = 0; // Track total milestone points earned in this quiz
        
        // WHO AM I: Track quiz attempt ID and enable state
        let currentQuizAttemptId = null;
        let whoAmIEnabled = false;
        
        let masteryData = {}; // Stores mastery status for all topics/difficulties

        // ==================== DAY 1 FEATURES ====================
        // Sound Effects, Online Counter, Hot Streak Indicator
        

        // === SOUND EFFECTS - Now loaded from external file ===
        // See: /static/js/agentmath-modules.js

        

        // =====================================================
        // FEATURES MOVED TO EXTERNAL MODULE
        // Sound Effects, Day 1, Day 2 Features
        // See: /static/js/agentmath-modules.js
        // =====================================================

        
        // ==================== ADDITIONAL RESOURCES ====================
        
        // Resource category configuration
        const resourceCategoryConfig = {
            'online_tutorials': { label: '🎬 Online Tutorials', order: 0 },
            'maths_awareness': { label: '🧠 Maths Awareness', order: 1 },
            'workbooks': { label: '📚 Maths WorkBooks', order: 2 },
            'worksheets': { label: '📝 Proficiency Building', order: 3 },
            'exam_papers': { label: '📋 Past Papers & Exam Technique', order: 4 },
            'software_tools': { label: '🛠️ Useful Maths Software Tools', order: 5 }
        };
        
        async function loadAdditionalResources() {
            const container = document.getElementById('resourcesContainer');
            if (!container) return;
            
            try {
                const response = await fetch('/api/resources');
                const data = await response.json();
                
                if (data.resources && data.resources.length > 0) {
                    // Group resources by category
                    const categoryOrder = ['online_tutorials', 'maths_awareness', 'workbooks', 'worksheets', 'exam_papers', 'software_tools'];
                    const grouped = {};
                    
                    categoryOrder.forEach(cat => {
                        grouped[cat] = data.resources.filter(r => r.category === cat);
                    });
                    
                    // Also collect uncategorized resources
                    const uncategorized = data.resources.filter(r => !r.category || !categoryOrder.includes(r.category));
                    
                    let html = '';
                    
                    categoryOrder.forEach(cat => {
                        const resources = grouped[cat];
                        if (resources.length === 0) return;
                        
                        const catInfo = resourceCategoryConfig[cat];
                        html += `
                            <div class="resource-category">
                                <div class="resource-category-header">${catInfo.label}</div>
                                <div class="resource-category-items">
                        `;
                        
                        resources.forEach(resource => {
                            html += `
                                <div class="resource-btn-wrapper">
                                    <a href="${resource.link_url}" 
                                       target="_blank" 
                                       rel="noopener noreferrer"
                                       class="resource-btn">
                                        <span>${resource.button_text}</span>
                                        <i class="fas fa-external-link-alt"></i>
                                    </a>
                                    <div class="resource-popup">
                                        <div class="resource-popup-header">
                                            <h4>${resource.button_text}</h4>
                                            <p>${resource.popup_text || 'Click to visit this resource'}</p>
                                        </div>
                                        ${resource.image_url ? `
                                            <div class="resource-popup-image">
                                                <img src="${resource.image_url}" alt="${resource.button_text} preview">
                                            </div>
                                        ` : ''}
                                        <div class="resource-popup-footer">
                                            <span><i class="fas fa-external-link-alt"></i> Opens in new window</span>
                                        </div>
                                    </div>
                                </div>
                            `;
                        });
                        
                        html += '</div></div>';
                    });
                    
                    // Add uncategorized if any exist
                    if (uncategorized.length > 0) {
                        html += `
                            <div class="resource-category">
                                <div class="resource-category-header">📎 Other Resources</div>
                                <div class="resource-category-items">
                        `;
                        uncategorized.forEach(resource => {
                            html += `
                                <div class="resource-btn-wrapper">
                                    <a href="${resource.link_url}" 
                                       target="_blank" 
                                       rel="noopener noreferrer"
                                       class="resource-btn">
                                        <span>${resource.button_text}</span>
                                        <i class="fas fa-external-link-alt"></i>
                                    </a>
                                    <div class="resource-popup">
                                        <div class="resource-popup-header">
                                            <h4>${resource.button_text}</h4>
                                            <p>${resource.popup_text || 'Click to visit this resource'}</p>
                                        </div>
                                        ${resource.image_url ? `
                                            <div class="resource-popup-image">
                                                <img src="${resource.image_url}" alt="${resource.button_text} preview">
                                            </div>
                                        ` : ''}
                                        <div class="resource-popup-footer">
                                            <span><i class="fas fa-external-link-alt"></i> Opens in new window</span>
                                        </div>
                                    </div>
                                </div>
                            `;
                        });
                        html += '</div></div>';
                    }
                    
                    container.innerHTML = html;
                } else {
                    container.innerHTML = '<div class="text-sm text-gray-400 text-center py-2">No resources available</div>';
                }
            } catch (error) {
                console.error('Error loading resources:', error);
                container.innerHTML = '<div class="text-sm text-gray-400 text-center py-2">Resources unavailable</div>';
            }
        }
        
        // ==================== END ADDITIONAL RESOURCES ====================

        const iconMap = {
            'calculator': 'fa-calculator',
            'divide': 'fa-divide',
            'book': 'fa-book',
            'chart': 'fa-chart-line',
            'dice': 'fa-dice',
            'layers': 'fa-layer-group'
        };

        // Load mastery data from API
        async function loadMasteryData() {
            try {
                const response = await fetch('/api/student/mastery');
                masteryData = await response.json();
                console.log('✨ Mastery data loaded:', masteryData);
            } catch (error) {
                console.error('Error loading mastery data:', error);
                masteryData = {};
            }
        }

        
        // ==================== SESSION VALIDATION ====================
        // Prevent cached pages from resuming after logout
        
        // Check if session is still valid
        async function validateSession() {
            try {
                const response = await fetch('/api/current-user', {
                    method: 'GET',
                    credentials: 'include',
                    cache: 'no-store'
                });
                
                if (!response.ok) {
                    // Session expired or user logged out
                    console.log('Session invalid, redirecting to login...');
                    window.location.href = '/login?session_expired=1';
                    return false;
                }
                
                const user = await response.json();
                if (!user || (!user.id && !user.is_guest)) {
                    console.log('No valid user session, redirecting to login...');
                    window.location.href = '/login?session_expired=1';
                    return false;
                }
                
                return true;
            } catch (error) {
                console.error('Session validation error:', error);
                window.location.href = '/login?session_expired=1';
                return false;
            }
        }
        
        // Validate session when page is shown (catches back button navigation)
        window.addEventListener('pageshow', function(event) {
            // If page was restored from bfcache (back-forward cache)
            if (event.persisted) {
                console.log('Page restored from cache, validating session...');
                validateSession();
            }
        });
        
        // Also validate when tab becomes visible (catches tab switching)
        document.addEventListener('visibilitychange', function() {
            if (document.visibilityState === 'visible') {
                // Add small delay to avoid too many checks
                setTimeout(validateSession, 500);
            }
        });
        
        // Check for logged_out parameter in URL (set by logout redirect)
        if (window.location.search.includes('logged_out=1')) {
            // Clear any cached state and redirect to clean login
            sessionStorage.clear();
            localStorage.removeItem('mathmaster_session');
            window.location.href = '/login';
        }
        
        // ==================== END SESSION VALIDATION ====================

        window.onload = async function() {
            try {
                // Try combined /api/init endpoint first - ONE call instead of many!
                console.log('⚡ Trying fast /api/init endpoint...');
                const initResponse = await fetch('/api/init');
                
                if (initResponse.ok) {
                    const initData = await initResponse.json();
                    
                    if (initData.success) {
                        console.log('✅ Fast init successful!');
                        
                        // Set global data from combined response
                        currentUser = initData.user;
                        masteryData = initData.mastery || {};
                        topics = initData.topics || [];
                        
                        // Store adaptive progress in masteryData for topic cards
                        if (initData.adaptive_progress) {
                            for (const [topicKey, progress] of Object.entries(initData.adaptive_progress)) {
                                if (!masteryData[topicKey]) {
                                    masteryData[topicKey] = {};
                                }
                                masteryData[topicKey].adaptive_level = progress.current_level || 1;
                                masteryData[topicKey].adaptive_mastered = (progress.current_level || 1) >= 12;
                            }
                        }
                        
                        // Render the UI with the combined data
                        updateUserDisplay();
                        updateOnlineDisplay(initData.online_count || 1);
                        
                        // Render topics using the data
                        if (initData.strands && Object.keys(initData.strands).length > 0) {
                            renderTopicsFromInitData(initData);
                        } else {
                            // Fallback to loadTopics if strands not in init data
                            await loadTopics();
                        }
                        
                        // Render badges
                        if (initData.badges) {
                            renderBadgeWidgetFromInit(initData.badges);
                        }
                        
                        // Render resources
                        if (initData.resources && initData.resources.length > 0) {
                            renderResourcesFromInit(initData.resources);
                        }
                        
                        // Initialize features (no API calls)
                        initDay1Features();
                        initDay2Features();
                        
                        return; // Success - skip fallback
                    }
                }
            } catch (e) {
                console.log('⚠️ Fast init failed, using fallback:', e.message);
            }
            
            // Fallback to original loading method
            console.log('📦 Using fallback parallel loading...');
            const [user] = await Promise.all([
                loadCurrentUser()
            ]);
            
            await Promise.all([
                loadMasteryData(),
                loadTopics(),
                loadProgress(),
                loadBadgeWidget(),
                loadAdditionalResources()
            ]);
            
            initDay1Features();
            initDay2Features();
        };
        
        // Helper function to render topics from /api/init data
        function renderTopicsFromInitData(initData) {
            const topicsGrid = document.getElementById('topicsGrid');
            if (!topicsGrid) return;
            
            // This delegates to the existing renderTopics logic but with pre-loaded data
            // For now, we'll call loadTopics which will use the cached masteryData
            loadTopics();
        }
        
        // Helper function to render badge widget from /api/init data
        function renderBadgeWidgetFromInit(badgeData) {
            const badgeWidget = document.getElementById('badgeWidget');
            if (!badgeWidget) return;
            
            const earnedCount = badgeData.earned ? badgeData.earned.length : 0;
            const totalPoints = badgeData.total_points || 0;
            const level = badgeData.level || 1;
            
            // Update the badge widget display
            const badgeCountEl = document.getElementById('badgeCount');
            const totalPointsEl = document.getElementById('totalPoints');
            const levelEl = document.getElementById('userLevel');
            
            if (badgeCountEl) badgeCountEl.textContent = earnedCount;
            if (totalPointsEl) totalPointsEl.textContent = totalPoints;
            if (levelEl) levelEl.textContent = level;
        }
        
        // Helper function to render resources from /api/init data
        function renderResourcesFromInit(resources) {
            // The existing loadAdditionalResources function handles this
            // Just call it - it will make its own request but the data is similar
            loadAdditionalResources();
        }
        
        // Check for passport URL params and auto-start quiz if present
        // Self-executing with retry logic to ensure startAdaptiveQuizBeta is available
        (function checkPassportUrlParams() {
            const urlParams = new URLSearchParams(window.location.search);
            const topicParam = urlParams.get('topic');
            const levelParam = urlParams.get('level');
            const sourceParam = urlParams.get('source');
            
            if (!topicParam) {
                console.log('📝 No passport URL params');
                return;
            }
            
            console.log('🎫 Passport URL params detected:', { topic: topicParam, level: levelParam, source: sourceParam });
            
            // Store source for return navigation
            if (sourceParam === 'passport') {
                sessionStorage.setItem('returnToPassport', 'true');
            }
            
            // Format topic title nicely (convert snake_case to Title Case)
            const topicTitle = topicParam.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
            
            // Clear the URL params immediately
            window.history.replaceState({}, '', window.location.pathname);
            
            // Wait for startAdaptiveQuizBeta to be defined, then call it
            function tryStartQuiz(attempts) {
                if (typeof startAdaptiveQuizBeta === 'function') {
                    console.log('🚀 Auto-starting adaptive quiz:', topicParam, topicTitle);
                    startAdaptiveQuizBeta(topicParam, topicTitle);
                } else if (attempts < 50) {
                    // Retry every 100ms, up to 5 seconds
                    setTimeout(() => tryStartQuiz(attempts + 1), 100);
                } else {
                    console.error('❌ startAdaptiveQuizBeta not available after 5 seconds');
                }
            }
            
            // Start trying after a brief delay for page to initialize
            setTimeout(() => tryStartQuiz(0), 500);
        })();

        // Generate BLANK number line (for questions - no solution shown)
        function generateBlankNumberLine(questionText) {
            const match = questionText.match(/(\d+)\s*([+\-])\s*(\d+)/);
            if (!match) return null;

            const num1 = parseInt(match[1]);
            const num2 = parseInt(match[3]);
            const operation = match[2] === '+' ? 'addition' : 'subtraction';
            const result = operation === 'addition' ? num1 + num2 : num1 - num2;

            // Determine range
            let minNum, maxNum, stepSize;
            if (Math.max(num1, num2, result) > 30) {
                if (num2 <= 10) {
                    minNum = Math.max(0, Math.min(num1, result) - 3);
                    maxNum = Math.max(num1, result) + 3;
                    stepSize = 1;
                } else if (num2 <= 20) {
                    minNum = Math.max(0, Math.min(num1, result) - 5);
                    maxNum = Math.max(num1, result) + 5;
                    stepSize = 2;
                } else {
                    const padding = Math.ceil(num2 * 0.2);
                    minNum = Math.max(0, Math.floor((Math.min(num1, result) - padding) / 5) * 5);
                    maxNum = Math.ceil((Math.max(num1, result) + padding) / 5) * 5;
                    stepSize = (maxNum - minNum > 50) ? 10 : 5;
                }
            } else {
                minNum = Math.max(0, Math.min(num1, result) - 2);
                maxNum = Math.max(num1, result) + 2;
                stepSize = 1;
            }

            const range = maxNum - minNum;

            // Generate BLANK number line (no solution)
            let html = '<div class="number-line-container">';
            html += '<div class="number-line"><div class="number-line-base"></div>';

            for (let i = minNum; i <= maxNum; i += stepSize) {
                const position = ((i - minNum) / range) * 100;
                html += `<div class="number-line-tick" style="left: ${position}%"></div>`;
                html += `<div class="number-line-label" style="left: ${position}%">${i}</div>`;
            }

            html += '</div>';
            html += `<div class="number-line-instruction">💡 Use the number line to help solve: ${questionText}</div>`;
            html += '</div>';

            return html;
        }

        // Generate SOLUTION number line (for explanations - shows complete solution)
        function generateSolutionNumberLine(questionText) {
            const match = questionText.match(/(\d+)\s*([+\-])\s*(\d+)/);
            if (!match) return null;

            const num1 = parseInt(match[1]);
            const num2 = parseInt(match[3]);
            const operation = match[2] === '+' ? 'addition' : 'subtraction';
            const result = operation === 'addition' ? num1 + num2 : num1 - num2;

            // Same range logic as blank version
            let minNum, maxNum, stepSize;
            if (Math.max(num1, num2, result) > 30) {
                if (num2 <= 10) {
                    minNum = Math.max(0, Math.min(num1, result) - 3);
                    maxNum = Math.max(num1, result) + 3;
                    stepSize = 1;
                } else if (num2 <= 20) {
                    minNum = Math.max(0, Math.min(num1, result) - 5);
                    maxNum = Math.max(num1, result) + 5;
                    stepSize = 2;
                } else {
                    const padding = Math.ceil(num2 * 0.2);
                    minNum = Math.max(0, Math.floor((Math.min(num1, result) - padding) / 5) * 5);
                    maxNum = Math.ceil((Math.max(num1, result) + padding) / 5) * 5;
                    stepSize = (maxNum - minNum > 50) ? 10 : 5;
                }
            } else {
                minNum = Math.max(0, Math.min(num1, result) - 2);
                maxNum = Math.max(num1, result) + 2;
                stepSize = 1;
            }

            const range = maxNum - minNum;
            const startPos = ((num1 - minNum) / range) * 100;
            const endPos = ((result - minNum) / range) * 100;

            // Generate SOLUTION number line (with answer)
            let html = '<div class="number-line-container" style="margin-top:16px;background:linear-gradient(135deg,#f0f9ff 0%,#e0f2fe 100%);">';
            html += '<div class="number-line"><div class="number-line-base"></div>';

            // Ticks and labels
            for (let i = minNum; i <= maxNum; i += stepSize) {
                const position = ((i - minNum) / range) * 100;
                html += `<div class="number-line-tick" style="left:${position}%"></div>`;
                html += `<div class="number-line-label" style="left:${position}%">${i}</div>`;
            }

            // Special ticks for start and end
            if (num1 % stepSize !== 0 && num1 >= minNum && num1 <= maxNum) {
                const position = ((num1 - minNum) / range) * 100;
                html += `<div class="number-line-tick" style="left:${position}%;height:15px"></div>`;
                html += `<div class="number-line-label" style="left:${position}%;font-weight:bold">${num1}</div>`;
            }
            if (result % stepSize !== 0 && result >= minNum && result <= maxNum) {
                const position = ((result - minNum) / range) * 100;
                html += `<div class="number-line-tick" style="left:${position}%;height:15px"></div>`;
                html += `<div class="number-line-label" style="left:${position}%;font-weight:bold;color:#48bb78">${result}</div>`;
            }

            // Dots
            html += `<div class="number-line-start-dot" style="left:${startPos}%"></div>`;
            html += `<div class="number-line-end-dot" style="left:${endPos}%"></div>`;

            // Arc and arrow
            if (operation === 'addition') {
                const arcWidth = ((num2) / range) * 100;
                html += `<div class="number-line-arc" style="left:${startPos}%;width:${arcWidth}%"></div>`;
                const arrowPos = startPos + arcWidth / 2;
                html += `<div class="number-line-arrow" style="left:${arrowPos}%;top:5%">→</div>`;
                html += '</div>';
                html += `<div class="number-line-instruction" style="background:rgba(72,187,120,0.1);border-left:4px solid #48bb78;padding:12px">`;
                html += `✅ <strong>Solution:</strong> Start at <strong>${num1}</strong> (🟢), add <strong>${num2}</strong> by jumping forward → to reach <strong>${result}</strong> (🔴)`;
                html += '</div>';
            } else {
                const arcWidth = ((num2) / range) * 100;
                html += `<div class="number-line-arc" style="left:${startPos - arcWidth}%;width:${arcWidth}%;border-color:#f56565"></div>`;
                const arrowPos = startPos - arcWidth / 2;
                html += `<div class="number-line-arrow" style="left:${arrowPos}%;top:5%;color:#f56565">←</div>`;
                html += '</div>';
                html += `<div class="number-line-instruction" style="background:rgba(72,187,120,0.1);border-left:4px solid #48bb78;padding:12px">`;
                html += `✅ <strong>Solution:</strong> Start at <strong>${num1}</strong> (🟢), subtract <strong>${num2}</strong> by jumping back ← to reach <strong>${result}</strong> (🔴)`;
                html += '</div>';
            }

            html += '</div>';
            return html;
        }

        async function loadCurrentUser() {
            try {
                const response = await fetch('/api/current-user');
                const user = await response.json();
                
                // Check if user is a guest
                if (user.is_guest) {
                    document.getElementById('userName').textContent = 'Guest User';
                    const mobileUserName = document.getElementById('userNameMobile');
                    if (mobileUserName) mobileUserName.textContent = 'Guest';
                    
                    // Show guest banner ONLY for casual guests (not repeat guests with a code)
                    if (user.guest_type !== 'repeat') {
                        const guestBanner = document.getElementById('guestBanner');
                        if (guestBanner) {
                            guestBanner.style.display = 'block';
                        }
                    }
                    
                    // Hide features not available for guests
                    const changePasswordBtn = document.querySelector('button[onclick="openPasswordModal()"]');
                    if (changePasswordBtn) {
                        changePasswordBtn.style.display = 'none';
                    }
                    
                    // Hide mobile change password option for guests
                    const mobileChangePasswordBtns = document.querySelectorAll('.mobile-menu-item');
                    mobileChangePasswordBtns.forEach(btn => {
                        if (btn.textContent.includes('Change Password')) {
                            btn.style.display = 'none';
                        }
                    });
                    
                    // Hide badge widget for guests
                    const badgeWidget = document.getElementById('badge-widget');
                    if (badgeWidget) {
                        badgeWidget.style.display = 'none';
                    }
                } else {
                    document.getElementById('userName').textContent = user.full_name;
                    const mobileUserName = document.getElementById('userNameMobile');
                    if (mobileUserName) mobileUserName.textContent = user.full_name.split(' ')[0]; // First name only on mobile
                }
            } catch (error) {
                console.error('Error loading user:', error);
                // If we can't load user, session may have expired
                if (error.message && error.message.includes('401')) {
                    window.location.href = '/login?session_expired=1';
                }
            }
        }

        async function loadTopics() {
            try {
                const response = await fetch('/api/topics');
                const data = await response.json();
                topics = data.topics;
                const strands = data.strands || {};
                const strandInfo = data.strand_info || {};

                // Get mastery data
                const masteryResponse = await fetch('/api/student/mastery');
                masteryData = await masteryResponse.json();
                
                // Fetch adaptive progress for topics that have adaptive questions
                // Define which topics have adaptive questions - UPDATE THIS LIST when adding new adaptive topics
                const adaptiveTopicsList = ['whole_numbers', 'addition_subtraction', 'multiplication_skills', 'division_skills', 'basic_fractions', 'basic_decimals', 'basic_percentages', 'time_and_clocks', 'money_skills', 'measurement', 'data_and_charts', 'number_patterns', 'flow_sums', 'number_pyramids', 'code_breaker', 'mastering_counting', 'words_to_numbers', 'ordering_magnitude', 'number_bonds', 'place_value', 'double_trouble', 'addition_blitz', 'times_tables_blitz', 'awareness_of_environment', 'pattern_and_sequence', 'developing_number_sense', 'shape_and_space', 'measure_and_data', 'time', 'l2_number_and_money', 'l2_time_management', 'l2_measurement_location', 'l2_shape_pattern_number', 'arithmetic', 'fractions', 'percentages', 'decimals', 'ratio', 'sets', 'descriptive_statistics', 'patterns', 'functions', 'area_perimeter_volume', 'solving_equations', 'simultaneous_equations', 'linear_inequalities', 'introductory_algebra', 'applied_arithmetic', 'currency', 'speed_distance_time', 'probability', 'coordinate_geometry', 'trigonometry', 'number_systems', 'indices', 'geometry', 'simplifying_expressions', 'expanding_factorising', 'lc_hl_calculus_diff', 'lc_hl_calculus_int', 'lc_hl_algebra', 'lc_hl_sequences', 'lc_hl_complex', 'lc_hl_functions', 'lc_hl_financial', 'lc_hl_proof', 'lc_hl_probability', 'lc_hl_statistics', 'lc_hl_coord_geom', 'lc_hl_trigonometry', 'lc_hl_geometry', 'lc_hl_mensuration', 'lc_hl_counting', 'lc_ol_calculus', 'lc_ol_financial', 'lc_ol_trigonometry', 'lc_ol_mensuration', 'lc_ol_statistics_desc', 'lc_ol_probability', 'lc_ol_applied_measure', 'lc_ol_sequences', 'lc_ol_algebra', 'lc_ol_functions', 'lc_ol_statistics_inf', 'lc_ol_coord_lines', 'lc_ol_coord_circles', 'lc_ol_complex', 'lc_ol_geometry']; // Topics with adaptive questions
                
                // Fetch ALL adaptive progress in PARALLEL (was sequential - 25 calls x 500ms = 12+ seconds!)
                const adaptivePromises = adaptiveTopicsList.map(async (topicKey) => {
                    try {
                        const adaptiveResponse = await fetch(`/api/adaptive/progress/${topicKey}`);
                        if (adaptiveResponse.ok) {
                            const adaptiveData = await adaptiveResponse.json();
                            return { topicKey, data: adaptiveData };
                        }
                    } catch (e) {
                        // Silently fail for individual topics
                    }
                    return null;
                });
                
                const adaptiveResults = await Promise.all(adaptivePromises);
                
                // Process results
                adaptiveResults.forEach(result => {
                    if (result) {
                        if (!masteryData[result.topicKey]) {
                            masteryData[result.topicKey] = {};
                        }
                        masteryData[result.topicKey].adaptive_level = result.data.current_level || 1;
                        masteryData[result.topicKey].adaptive_mastered = (result.data.current_level || 1) >= 12;
                    }
                });

                // Icon mapping
                const iconMap = {
                    'calculator': 'fa-calculator',
                    'divide': 'fa-divide',
                    'percent': 'fa-percent',
                    'x': 'fa-xmark',
                    'hash': 'fa-hashtag',
                    'book': 'fa-book',
                    'chart': 'fa-chart-line',
                    'dice': 'fa-dice',
                    'layers': 'fa-layer-group',
                    'radical': 'fa-square-root-alt',
                    'infinity': 'fa-infinity',
                    'rotate': 'fa-rotate'
                };

                // Revision Slides - Thanks to Mr Notaro (Palmerstown CS)
                const revisionSlides = {
                    'Number': [
                        { title: 'Financial Maths', url: 'https://palmerstowncs-my.sharepoint.com/:p:/g/personal/anthony_notaro_palmerstowncs_ie/Eatb7k0qPBVDn14s_J4LNsIBYKXcieOEpYWJeW2y-2imQA?e=4RG012' },
                        { title: 'Sets & Venn Diagrams', url: 'https://palmerstowncs-my.sharepoint.com/:p:/g/personal/anthony_notaro_palmerstowncs_ie/Eap-N1PhTXRNpm4zPs1p1BUBcLnudS4KG2ywFQvnb-MxTw?e=Yxisb2' }
                    ],
                    'Algebra and Functions': [
                        { title: 'Algebra 1', url: 'https://palmerstowncs-my.sharepoint.com/:p:/g/personal/anthony_notaro_palmerstowncs_ie/EaqmYVzyKoBOp1yUuyJHTUIBOU-_1hGeENx2MbsR_0yaBw?e=PSnwt5' },
                        { title: 'Algebra 2', url: 'https://palmerstowncs-my.sharepoint.com/:p:/g/personal/anthony_notaro_palmerstowncs_ie/EQwc1csFFa9PnqstEeP5dsEBE5JF5Z82Br92PZoNWqYaLg?e=VOYikd' },
                        { title: 'Patterns & Sequences', url: 'https://palmerstowncs-my.sharepoint.com/:p:/g/personal/anthony_notaro_palmerstowncs_ie/ETvATshTfsFPsjtrG4h8hNUBeUXlPyThjrJEO0ES0PrnoA?e=vIUTJs' },
                        { title: 'Functions', url: 'https://palmerstowncs-my.sharepoint.com/:p:/g/personal/anthony_notaro_palmerstowncs_ie/EfL8_tLbb7JMh0-pmKQhrQEB8cmWIkgtm84UrXAEK3CFYw?e=c2TXMU' },
                        { title: 'Area & Volume', url: 'https://palmerstowncs-my.sharepoint.com/:p:/g/personal/anthony_notaro_palmerstowncs_ie/EdnyJMpNvlJGvWE0vY4NEVMBEDyJcFmOmSPdSoj1Nb4OsA?e=RPGemu' }
                    ],
                    'Statistics and Probability': [
                        { title: 'Probability', url: 'https://palmerstowncs-my.sharepoint.com/:p:/g/personal/anthony_notaro_palmerstowncs_ie/ESvWVFUaOPlCsx4V19UgVBABT_Xip2WnwHg3qo4GgwKQTw?e=QG7df9' },
                        { title: 'Statistics', url: 'https://palmerstowncs-my.sharepoint.com/:p:/g/personal/anthony_notaro_palmerstowncs_ie/Ebe_0FMGUR1Gr7LxXGPMFHcBh1V4lIgvh_bXRyg0wudLnQ?e=p3bW5i' }
                    ],
                    'Geometry and Trigonometry': [
                        { title: 'Coordinate Geometry', url: 'https://palmerstowncs-my.sharepoint.com/:p:/g/personal/anthony_notaro_palmerstowncs_ie/EfjWpSzzfkxDudQNA2qGo-4BP9qeA0LvpgLhdupk56vf3w?e=ENzJCo' },
                        { title: 'Geometry', url: 'https://palmerstowncs-my.sharepoint.com/:p:/g/personal/anthony_notaro_palmerstowncs_ie/EVE-3tnh5LhIhDwkRsgoNc4B-euRP31_rCsNm4WZzpXRMg?e=JisGOD' },
                        { title: 'Trigonometry', url: 'https://palmerstowncs-my.sharepoint.com/:p:/g/personal/anthony_notaro_palmerstowncs_ie/ERt6YHrKvvtMkIrFu8mQjXUBYnD3aZoMcSAUVxEmwixKRA?e=IH0z4J' }
                    ]
                };

                // Clear and build strands dynamically
                const container = document.getElementById('learningPathsContainer');
                container.innerHTML = '';

                // Sort strands: Numeracy first, L1LP second, L2LP third, Junior Cycle next, Senior Cycle, then LC OL, then LC Higher Level last
                const sortedStrands = Object.entries(strands).sort((a, b) => {
                    const aIsNumeracy = a[0].toLowerCase().includes('numeracy');
                    const bIsNumeracy = b[0].toLowerCase().includes('numeracy');
                    const aIsL1LP = a[0].toLowerCase() === 'l1lp';
                    const bIsL1LP = b[0].toLowerCase() === 'l1lp';
                    const aIsL2LP = a[0].toLowerCase() === 'l2lp';
                    const bIsL2LP = b[0].toLowerCase() === 'l2lp';
                    const aIsSenior = a[0].toLowerCase().includes('senior');
                    const bIsSenior = b[0].toLowerCase().includes('senior');
                    const aIsLcOl = a[0].toLowerCase().includes('lc ordinary');
                    const bIsLcOl = b[0].toLowerCase().includes('lc ordinary');
                    const aIsLcHl = a[0].toLowerCase().includes('lc higher');
                    const bIsLcHl = b[0].toLowerCase().includes('lc higher');
                    
                    // Numeracy always first
                    if (aIsNumeracy && !bIsNumeracy) return -1;
                    if (!aIsNumeracy && bIsNumeracy) return 1;
                    
                    // L1LP second (after Numeracy, before everything else)
                    if (aIsL1LP && !bIsL1LP && !bIsNumeracy) return -1;
                    if (!aIsL1LP && bIsL1LP && !aIsNumeracy) return 1;
                    
                    // L2LP third (after L1LP, before Junior Cycle)
                    if (aIsL2LP && !bIsL2LP && !bIsNumeracy && !bIsL1LP) return -1;
                    if (!aIsL2LP && bIsL2LP && !aIsNumeracy && !aIsL1LP) return 1;
                    
                    // LC Higher Level always last
                    if (aIsLcHl && !bIsLcHl) return 1;
                    if (!aIsLcHl && bIsLcHl) return -1;
                    
                    // LC Ordinary Level second to last (before LC HL)
                    if (aIsLcOl && !bIsLcOl && !bIsLcHl) return 1;
                    if (!aIsLcOl && bIsLcOl && !aIsLcHl) return -1;
                    
                    // Senior Cycle third to last (before LC OL and LC HL)
                    if (aIsSenior && !bIsSenior && !bIsLcHl && !bIsLcOl) return 1;
                    if (!aIsSenior && bIsSenior && !aIsLcHl && !aIsLcOl) return -1;
                    
                    return 0; // keep original order
                });

                // Iterate through strands in sorted order
                sortedStrands.forEach(([strandName, strandTopics], strandIndex) => {
                    // Hide SENIOR CYCLE - ALGEBRA strand
                    if (strandName.toLowerCase().includes('senior') && strandName.toLowerCase().includes('algebra')) {
                        return; // Skip this strand
                    }
                    
                    // Transform Junior Cycle strand display names
                    let displayStrandName = strandName;
                    const jcStrands = ['Algebra and Functions', 'Geometry and Trigonometry', 'Number', 'Statistics and Probability'];
                    if (jcStrands.includes(strandName)) {
                        displayStrandName = 'Junior Cycle - ' + strandName;
                    }
                    
                    const info = strandInfo[strandName] || {
                        icon: '📚',
                        color: '#667eea',
                        description: 'Learn and master these topics'
                    };
                    
                    const isSeniorCycle = strandName.toLowerCase().includes('senior') || strandName.toLowerCase().includes('lc higher') || strandName.toLowerCase().includes('lc ordinary');
                    
                    // Get revision slides count for this strand
                    const strandRevision = revisionSlides[strandName];
                    const revisionCount = (strandRevision && !isSeniorCycle) ? strandRevision.length : 0;
                    
                    // Calculate mastery statistics for this strand
                    let masteredCount = 0;
                    let inProgressCount = 0;
                    const totalTopics = strandTopics.filter(tk => topics[tk]).length;
                    
                    strandTopics.forEach(topicKey => {
                        if (topics[topicKey]) {
                            const hasAdaptive = adaptiveTopicsList.includes(topicKey);
                            const adaptiveLevel = masteryData[topicKey]?.adaptive_level || 1;
                            const adaptiveMastered = hasAdaptive && adaptiveLevel >= 12;
                            
                            const difficulties = masteryData[topicKey]?.difficulties || {};
                            const practiceComplete = (difficulties.beginner?.mastered || false) &&
                                                    (difficulties.intermediate?.mastered || false) &&
                                                    (difficulties.advanced?.mastered || false);
                            
                            // Count as mastered if both modes complete (for adaptive topics) or practice complete (for non-adaptive)
                            if (hasAdaptive) {
                                if (adaptiveMastered && practiceComplete) {
                                    masteredCount++;
                                } else if (adaptiveLevel > 1 || Object.keys(difficulties).some(d => difficulties[d]?.mastered)) {
                                    inProgressCount++;
                                }
                            } else {
                                if (practiceComplete) {
                                    masteredCount++;
                                } else if (Object.keys(difficulties).some(d => difficulties[d]?.mastered)) {
                                    inProgressCount++;
                                }
                            }
                        }
                    });
                    
                    const progressPercent = totalTopics > 0 ? Math.round((masteredCount / totalTopics) * 100) : 0;
                    const circumference = 2 * Math.PI * 20; // radius = 20
                    const strokeDashoffset = circumference - (progressPercent / 100) * circumference;
                    
                    // Create strand ID for collapsible
                    const strandId = 'strand-' + strandName.toLowerCase().replace(/[^a-z0-9]/g, '-');

                    // Create strand card
                    const strandCard = document.createElement('div');
                    strandCard.className = 'learning-path-card';
                    strandCard.id = strandId;
                    strandCard.style.borderTop = `4px solid ${info.color}`;
                    
                    // Create collapsible header
                    const collapseHeader = document.createElement('div');
                    collapseHeader.className = 'strand-collapse-header';
                    collapseHeader.onclick = function() { toggleStrand(strandId); };
                    
                    // Map emoji icons to Font Awesome icons
                    const emojiToFA = {
                        '📊': 'chart-bar',
                        '🔢': 'calculator', 
                        '📈': 'chart-line',
                        '🎓': 'graduation-cap',
                        '📐': 'ruler-combined',
                        '📚': 'book',
                        '🔷': 'shapes',
                        '🎲': 'dice',
                        '🧮': 'th'
                    };
                    const faIcon = emojiToFA[info.icon] || 'book';
                    
                    collapseHeader.innerHTML = `
                        <div class="strand-chevron">
                            <i class="fas fa-chevron-right"></i>
                        </div>
                        <div class="strand-header-info">
                            <div class="strand-header-icon" style="background: linear-gradient(135deg, ${info.color}, ${info.color}dd);">
                                <i class="fas fa-${faIcon}"></i>
                            </div>
                            <div class="strand-header-text">
                                <h3>${displayStrandName}</h3>
                                <p>${totalTopics} topics${revisionCount > 0 ? ' • ' + revisionCount + ' revision slides' : ''}</p>
                            </div>
                        </div>
                        <div class="strand-header-progress">
                            <div class="strand-progress-ring">
                                <svg width="48" height="48">
                                    <circle class="bg" cx="24" cy="24" r="20"></circle>
                                    <circle class="progress" cx="24" cy="24" r="20" 
                                            style="stroke: ${info.color};"
                                            stroke-dasharray="${circumference}" 
                                            stroke-dashoffset="${strokeDashoffset}"></circle>
                                </svg>
                                <span class="strand-progress-text">${progressPercent}%</span>
                            </div>
                            <div class="strand-stats">
                                <div class="strand-stats-main">${masteredCount}/${totalTopics} mastered</div>
                                <div class="strand-stats-sub">${inProgressCount > 0 ? inProgressCount + ' in progress' : 'Click to expand'}</div>
                            </div>
                        </div>
                    `;
                    strandCard.appendChild(collapseHeader);
                    
                    // Create collapsible content wrapper
                    const collapsibleContent = document.createElement('div');
                    collapsibleContent.className = 'strand-collapsible-content';
                    collapsibleContent.style.background = `linear-gradient(135deg, ${info.color} 0%, ${info.color}dd 100%)`;

                    // Strand header inside collapsible
                    const header = document.createElement('div');
                    header.className = 'path-header';
                    header.innerHTML = `
                        <div class="path-number" style="background: rgba(255,255,255,0.3)">${isSeniorCycle ? 'Senior Cycle' : 'Junior Cycle'}</div>
                    `;
                    collapsibleContent.appendChild(header);

                    // Topics flow container
                    const flow = document.createElement('div');
                    flow.className = 'path-flow';
                    
                    // Use adaptiveTopicsList (defined earlier in loadTopics)
                    const adaptiveAvailable = adaptiveTopicsList;
                    
                    // Topic emoji mapping
                    const topicEmojis = {
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
                        'flow_sums': '🌊',
                        'number_pyramids': '🔺',
                        'code_breaker': '🔐',
                        'mastering_counting': '🔢',
                        'words_to_numbers': '🔤',
                        'ordering_magnitude': '📏',
                        'number_bonds': '🫧',
                        'place_value': '🏗️',
                        'double_trouble': '⚡',
                        'addition_blitz': '➕',
                        'times_tables_blitz': '✖️',
                        // L1LP Strand
                        'awareness_of_environment': '👀',
                        'pattern_and_sequence': '🔄',
                        'developing_number_sense': '🔢',
                        'shape_and_space': '🔷',
                        'measure_and_data': '📏',
                        'time': '🕐',
                        // L2LP Strand (NCCA-aligned)
                        'l2_number_and_money': '💰',
                        'l2_time_management': '🕐',
                        'l2_measurement_location': '📍',
                        'l2_shape_pattern_number': '🔷',
                        // JC Exam Topics
                        'fractions': '🥧',
                        'percentages': '💯',
                        'ratio': '⚖️',
                        'sets': '⭕',
                        'decimals': '🔢',
                        'arithmetic': '➕',
                        'multiplication_division': '✖️',
                        'bodmas': '🔢',
                        'number_systems': '🔢',
                        'integers': '➕➖',
                        'indices': '📈',
                        'geometry': '📐',
                        'patterns': '🔷',
                        'introductory_algebra': '📐',
                        'functions': '📈',
                        'probability': '🎲',
                        'descriptive_statistics': '📊',
                        'area_perimeter_volume': '📏',
                        'solving_equations': '🔢',
                        'simultaneous_equations': '⚖️',
                        'linear_inequalities': '≤',
                        'applied_arithmetic': '💰',
                        'currency': '💱',
                        'speed_distance_time': '🏃',
                        'coordinate_geometry': '📍',
                        'trigonometry': '📐',
                        'surds': '√',
                        'complex_numbers_intro': '🔮',
                        'complex_numbers_expanded': '🔮',
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
                        'lc_hl_counting': '🔄',
                        // LC Ordinary Level Strand
                        'lc_ol_calculus': '📈',
                        'lc_ol_financial': '💰',
                        'lc_ol_trigonometry': '📐',
                        'lc_ol_mensuration': '📦',
                        'lc_ol_statistics_desc': '📊',
                        'lc_ol_probability': '🎲',
                        'lc_ol_applied_measure': '📏',
                        'lc_ol_sequences': '🔢',
                        'lc_ol_algebra': '🔤',
                        'lc_ol_functions': '📈',
                        'lc_ol_statistics_inf': '📉',
                        'lc_ol_coord_lines': '📍',
                        'lc_ol_coord_circles': '⭕',
                        'lc_ol_complex': '🌀',
                        'lc_ol_geometry': '🔺'
                    };

                    // Topic to Video URL mapping (Eddie Woo + Khan Academy for gaps)
                    const topicVideoUrls = {
                        'fractions': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5A3lQJK26JqkPC2HZPOb3-W',
                        'percentages': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5A3lQJK26JqkPC2HZPOb3-W',
                        'decimals': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5A3lQJK26JqkPC2HZPOb3-W',
                        'ratio': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5A3EpPzrcebR5Y8q8K25hTl',
                        'sets': 'https://www.khanacademy.org/math/statistics-probability/probability-library#basic-set-ops',
                        'descriptive_statistics': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5D5BS80FWHE_mH6ZTtGU3iQ',
                        'patterns': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5BGNGW5eVKndzk4BCdJE6kP',
                        'functions': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5CGGxg3mH3nMpPnuEzW-jXh',
                        'area_perimeter_volume': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5DtydLCjMby6JhKZmh-cbvh',
                        'solving_equations': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5DMdiBiiGeTIkaht6MBhhnC',
                        'simultaneous_equations': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5BflvNTYTtJski5eASSVFVt',
                        'linear_inequalities': 'https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:inequalities-systems-graphs',
                        'introductory_algebra': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5BTbgTCHTkwxUqfvg6MvNuJ',
                        'applied_arithmetic': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5D4-Axux8PcJmZXB0Yv2gi1',
                        'currency': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5D4-Axux8PcJmZXB0Yv2gi1',
                        'speed_distance_time': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5A3EpPzrcebR5Y8q8K25hTl',
                        'probability': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5ANrjJ0EEMzvxVKmnPNVYvf',
                        'coordinate_geometry': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5Dao4OjSGe8msbPBQ0y74Lr',
                        'trigonometry': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5DdtHcMLtodrdN7nr79GJIJ',
                        'number_systems': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5CyhzaViGUSFc164691gd0G',
                        'indices': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5CWmVgY_VVRmh_r_MJgE1uo',
                        'geometry': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5AtD-gkOyQMtLjR2TPMrJkQ',
                        'simplifying_expressions': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5BTbgTCHTkwxUqfvg6MvNuJ',
                        'expanding_factorising': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5ATGZobbZgt78rXma1cidQB'
                    };

                    strandTopics.forEach((topicKey, index) => {
                        if (topics[topicKey]) {
                            const topic = topics[topicKey];
                            const topicMastered = masteryData[topicKey]?.topic_mastered || false;
                            
                            // Practice mastery data
                            const difficulties = masteryData[topicKey]?.difficulties || {};
                            const beginnerMastered = difficulties.beginner?.mastered || false;
                            const intermediateMastered = difficulties.intermediate?.mastered || false;
                            const advancedMastered = difficulties.advanced?.mastered || false;
                            const practiceComplete = beginnerMastered && intermediateMastered && advancedMastered;
                            const practiceMasteredCount = [beginnerMastered, intermediateMastered, advancedMastered].filter(Boolean).length;
                            
                            // Check if adaptive is available for this topic
                            const hasAdaptive = adaptiveAvailable.includes(topicKey);
                            
                            // Get adaptive progress (fetched earlier in loadTopics)
                            const adaptiveLevel = masteryData[topicKey]?.adaptive_level || 1;
                            const adaptiveMastered = adaptiveLevel >= 12;
                            
                            // Check if this is a Numeracy, L1LP, or L2LP strand topic (no Practice mode)
                            const numeracyTopics = ['whole_numbers', 'addition_subtraction', 'multiplication_skills', 'division_skills', 'basic_fractions', 'basic_decimals', 'basic_percentages', 'time_and_clocks', 'money_skills', 'measurement', 'data_and_charts', 'number_patterns', 'awareness_of_environment', 'pattern_and_sequence', 'developing_number_sense', 'shape_and_space', 'measure_and_data', 'time', 'l2_number_and_money', 'l2_time_management', 'l2_measurement_location', 'l2_shape_pattern_number'];
                            const isNumeracyTopic = numeracyTopics.includes(topicKey);
                            
                            // Interactive-only topics (no Practice mode - they ARE the activity)
                            const interactiveOnlyTopics = ['flow_sums', 'number_pyramids', 'code_breaker', 'mastering_counting', 'words_to_numbers', 'ordering_magnitude', 'number_bonds', 'place_value', 'double_trouble', 'addition_blitz', 'times_tables_blitz'];
                            const isInteractiveTopic = interactiveOnlyTopics.includes(topicKey);
                            
                            // Check if this is an LC Higher Level topic (no Practice mode - adaptive only)
                            const isLcHlTopic = topicKey.startsWith('lc_hl_');
                            
                            // Check if this is an LC Ordinary Level topic (no Practice mode - adaptive only)
                            const isLcOlTopic = topicKey.startsWith('lc_ol_');
                            
                            // Check if both modes are mastered (Numeracy, Interactive, LC HL, and LC OL only need adaptive)
                            const allMastered = (isNumeracyTopic || isInteractiveTopic || isLcHlTopic || isLcOlTopic)
                                ? (adaptiveMastered && hasAdaptive)
                                : (practiceComplete && adaptiveMastered && hasAdaptive);
                            
                            // Get topic emoji
                            const emoji = topicEmojis[topicKey] || '📚';
                            
                            // Practice progress text
                            let practiceProgressText = 'Not started';
                            if (practiceComplete) {
                                practiceProgressText = '✓ Mastered';
                            } else if (practiceMasteredCount > 0) {
                                practiceProgressText = `${practiceMasteredCount}/3 complete`;
                            }
                            
                            // Adaptive progress
                            const adaptivePercent = hasAdaptive ? Math.round((adaptiveLevel / 12) * 100) : 0;
                            let adaptiveLevelText = hasAdaptive ? `Level ${adaptiveLevel} of 12` : (isNumeracyTopic ? '12 progressive levels' : '12 levels • SEC aligned');
                            if (adaptiveMastered && hasAdaptive) {
                                adaptiveLevelText = '✓ Level 12';
                            }
                            
                            // Create unified topic card
                            const card = document.createElement('div');
                            card.className = `unified-topic-card ${allMastered ? 'all-mastered' : ''}`;
                            card.setAttribute('data-topic', topicKey);
                            
                            card.innerHTML = `
                                ${allMastered ? '<div class="unified-mastery-badge">🏆</div>' : ''}
                                <div class="unified-topic-header">
                                    <div class="unified-topic-icon">${emoji}</div>
                                    <div class="unified-topic-title">${topic.title}</div>
                                </div>
                                <div class="unified-mode-options">
                                    <div class="unified-mode-option adaptive ${hasAdaptive ? '' : 'disabled'}" ${hasAdaptive ? `onclick="event.stopPropagation(); startAdaptiveQuizBeta('${topicKey}', '${topic.title.replace(/'/g, "\\'")}');"` : ''}>
                                        <div class="unified-mode-icon ${hasAdaptive ? 'adaptive' : 'disabled'}">
                                            <i class="fas fa-graduation-cap"></i>
                                        </div>
                                        <div class="unified-mode-info">
                                            <div class="unified-mode-label">
                                                Learning in Stages
                                                ${hasAdaptive ? '<span class="unified-recommended-badge">★ Recommended</span>' : '<span class="unified-coming-soon">Coming Soon</span>'}
                                            </div>
                                            ${hasAdaptive ? '<div class="unified-mode-subtitle">Progressive • 12 adaptive levels</div>' : ''}
                                            <div class="unified-mode-progress">
                                                ${hasAdaptive ? `
                                                    <div class="unified-level-indicator">
                                                        <div class="unified-level-bar">
                                                            <div class="unified-level-fill ${adaptiveMastered ? 'mastered' : ''}" style="width: ${adaptivePercent}%;"></div>
                                                        </div>
                                                        <span class="unified-level-text ${adaptiveMastered ? 'mastered' : ''}">${adaptiveLevelText}</span>
                                                    </div>
                                                ` : `
                                                    <span class="unified-progress-text" style="color: #9ca3af;">${adaptiveLevelText}</span>
                                                `}
                                            </div>
                                        </div>
                                        <i class="fas ${hasAdaptive ? 'fa-chevron-right unified-mode-arrow' : 'fa-lock unified-mode-arrow'}" style="${hasAdaptive ? '' : 'color: #d1d5db;'}"></i>
                                    </div>
                                    ${(!isNumeracyTopic && !isInteractiveTopic && !isLcHlTopic && !isLcOlTopic) ? `
                                    <div class="unified-mode-option practice" onclick="event.stopPropagation(); selectTopic('${topicKey}', '${topic.title.replace(/'/g, "\\'")}');">
                                        <div class="unified-mode-icon practice">
                                            <i class="fas fa-dumbbell"></i>
                                        </div>
                                        <div class="unified-mode-info">
                                            <div class="unified-mode-label">Practice Mode</div>
                                            <div class="unified-mode-progress">
                                                <div class="unified-diff-dots">
                                                    <div class="unified-diff-dot beginner ${beginnerMastered ? 'complete' : ''}" title="Beginner">B</div>
                                                    <div class="unified-diff-dot intermediate ${intermediateMastered ? 'complete' : ''}" title="Intermediate">I</div>
                                                    <div class="unified-diff-dot advanced ${advancedMastered ? 'complete' : ''}" title="Advanced">A</div>
                                                </div>
                                                <span class="unified-progress-text ${practiceComplete ? 'mastered' : ''}">${practiceProgressText}</span>
                                            </div>
                                        </div>
                                        <i class="fas fa-chevron-right unified-mode-arrow"></i>
                                    </div>
                                    ` : ''}
                                </div>
                                ${hasAdaptive ? getJCLevelPopupHTML(topicKey) : ''}
                            `;

                            // Add dynamic popup positioning on hover
                            if (hasAdaptive) {
                                card.addEventListener('mouseenter', function() {
                                    const popup = this.querySelector('.jc-level-popup');
                                    if (!popup) return;
                                    
                                    // CRITICAL: Raise parent strand card z-index so popup appears above other strands
                                    const strandCard = this.closest('.learning-path-card');
                                    if (strandCard) {
                                        strandCard.style.zIndex = '1000';
                                    }
                                    
                                    const cardRect = this.getBoundingClientRect();
                                    const popupHeight = 350;
                                    const viewportHeight = window.innerHeight;
                                    const spaceBelow = viewportHeight - cardRect.bottom;
                                    const spaceAbove = cardRect.top;
                                    
                                    if (spaceBelow < popupHeight && spaceAbove > spaceBelow) {
                                        popup.classList.add('position-above');
                                    } else {
                                        popup.classList.remove('position-above');
                                    }
                                });
                                
                                // Reset strand z-index on mouse leave
                                card.addEventListener('mouseleave', function() {
                                    const strandCard = this.closest('.learning-path-card');
                                    if (strandCard) {
                                        strandCard.style.zIndex = '';
                                    }
                                });
                            }

                            flow.appendChild(card);

                            // Add arrow between topics (except after last one)
                            if (index < strandTopics.length - 1) {
                                const arrow = document.createElement('div');
                                arrow.className = 'unified-flow-arrow';
                                arrow.innerHTML = '→';
                                flow.appendChild(arrow);
                            }
                        }
                    });

                    // Append flow to collapsible content
                    collapsibleContent.appendChild(flow);
                    
                    // Add Revision Slides section if available for this strand
                    if (strandRevision && strandRevision.length > 0 && !isSeniorCycle) {
                        // Divider
                        const divider = document.createElement('div');
                        divider.className = 'revision-divider';
                        divider.innerHTML = `
                            <div style="border-top: 2px dashed rgba(255,255,255,0.3); margin: 20px 0 15px 0;"></div>
                            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px;">
                                <span style="font-size: 1.25rem;">📖</span>
                                <span style="font-weight: 600; color: white;">Revision Slides (Thanks to Mr Notaro) - Click to view in a separate window</span>
                            </div>
                        `;
                        collapsibleContent.appendChild(divider);
                        
                        // Revision buttons container
                        const revisionContainer = document.createElement('div');
                        revisionContainer.style.cssText = 'display: flex; flex-wrap: wrap; gap: 10px; padding: 0 20px 20px 20px;';
                        
                        let buttonsHtml = '';
                        strandRevision.forEach((slide, index) => {
                            const escapedUrl = slide.url.replace(/'/g, "\\'");
                            buttonsHtml += `
                                <button type="button" 
                                    onclick="event.stopPropagation(); window.open('${escapedUrl}', '_blank'); return false;"
                                    style="display: inline-flex; align-items: center; gap: 6px; padding: 8px 14px; background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border: 1px solid #86efac; border-radius: 8px; color: #166534; font-size: 0.85rem; font-weight: 500; cursor: pointer; position: relative;"
                                    onmouseover="this.style.background='linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%)'; this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 6px rgba(0,0,0,0.1)';"
                                    onmouseout="this.style.background='linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%)'; this.style.transform='translateY(0)'; this.style.boxShadow='none';">
                                    <i class="fas fa-external-link-alt" style="font-size: 0.75rem;"></i> ${slide.title}
                                </button>
                            `;
                        });
                        revisionContainer.innerHTML = buttonsHtml;
                        
                        collapsibleContent.appendChild(revisionContainer);
                    }
                    
                    // Append collapsible content to strand card
                    strandCard.appendChild(collapsibleContent);
                    
                    // Add z-index handler for popup layering (JS fallback for browsers without :has())
                    strandCard.querySelectorAll('.unified-topic-card').forEach(card => {
                        card.addEventListener('mouseenter', function() {
                            strandCard.style.zIndex = '1000';
                        });
                        card.addEventListener('mouseleave', function() {
                            strandCard.style.zIndex = '';
                        });
                    });
                    
                    container.appendChild(strandCard);
                });
                
                // All strands start collapsed - do not restore saved states
                // loadStrandStates();

                // Show verification in console
                console.log('✅ Student dashboard loaded successfully');

                document.getElementById('loadingScreen').classList.add('hidden');
                document.getElementById('topicScreen').classList.remove('hidden');
            } catch (error) {
                console.error('Error loading topics:', error);
            }
        }

        // Helper function to get consistent icon colors
        // JC Exam Level Popup HTML Generator
        function getJCLevelPopupHTML(topicKey) {
            const levelData = getTopicLevelData(topicKey);
            if (!levelData) return '';
            
            // Check if this is an L2LP topic
            const isL2LP = topicKey.startsWith('l2_');
            // Check if this is an L1LP topic
            const isL1LP = ['awareness_of_environment', 'pattern_and_sequence', 'developing_number_sense', 'shape_and_space', 'measure_and_data', 'time'].includes(topicKey);
            // Check if this is a Numeracy strand topic
            const isNumeracy = ['whole_numbers', 'addition_subtraction', 'multiplication_skills', 'division_skills', 'basic_fractions', 'basic_decimals', 'basic_percentages', 'time_and_clocks', 'money_skills', 'measurement', 'data_and_charts', 'number_patterns'].includes(topicKey);
            // Check if this is a Leaving Certificate topic (OL or HL)
            const isLeavingCert = topicKey.startsWith('lc_ol_') || topicKey.startsWith('lc_hl_');
            
            let levelsHtml = '';
            levelData.forEach((level, index) => {
                const bandClass = level.band.toLowerCase();
                levelsHtml += `
                    <div class="jc-level-item ${bandClass}">
                        <div class="jc-level-num">L${index + 1}</div>
                        <div class="jc-level-title">${level.title}</div>
                    </div>
                `;
            });
            
            // Different badge and legend for L2LP/L1LP vs JC topics
            let curriculumBadge, bandLegend;
            if (isL2LP) {
                curriculumBadge = '<i class="fas fa-certificate"></i> NCCA L2LP Aligned';
                bandLegend = `
                    <div class="jc-band-item"><div class="jc-band-dot foundation"></div>Foundation</div>
                    <div class="jc-band-item"><div class="jc-band-dot developing"></div>Developing</div>
                    <div class="jc-band-item"><div class="jc-band-dot progressing"></div>Progressing</div>
                    <div class="jc-band-item"><div class="jc-band-dot consolidating"></div>Consolidating</div>
                `;
            } else if (isL1LP) {
                curriculumBadge = '<i class="fas fa-certificate"></i> NCCA L1LP Aligned';
                bandLegend = `
                    <div class="jc-band-item"><div class="jc-band-dot foundation"></div>Foundation</div>
                    <div class="jc-band-item"><div class="jc-band-dot developing"></div>Developing</div>
                    <div class="jc-band-item"><div class="jc-band-dot progressing"></div>Progressing</div>
                    <div class="jc-band-item"><div class="jc-band-dot consolidating"></div>Consolidating</div>
                `;
            } else if (isNumeracy) {
                curriculumBadge = '<i class="fas fa-certificate"></i> Numeracy Foundation';
                bandLegend = `
                    <div class="jc-band-item"><div class="jc-band-dot foundation"></div>Foundation</div>
                    <div class="jc-band-item"><div class="jc-band-dot ordinary"></div>Developing</div>
                    <div class="jc-band-item"><div class="jc-band-dot higher"></div>Proficient</div>
                    <div class="jc-band-item"><div class="jc-band-dot mastery"></div>Advanced</div>
                `;
            } else if (isLeavingCert) {
                curriculumBadge = '<i class="fas fa-certificate"></i> Irish Senior Cycle Aligned';
                bandLegend = `
                    <div class="jc-band-item"><div class="jc-band-dot foundation"></div>Foundation</div>
                    <div class="jc-band-item"><div class="jc-band-dot ordinary"></div>Ordinary</div>
                    <div class="jc-band-item"><div class="jc-band-dot higher"></div>Higher</div>
                    <div class="jc-band-item"><div class="jc-band-dot mastery"></div>Mastery</div>
                `;
            } else {
                curriculumBadge = '<i class="fas fa-certificate"></i> Irish Junior Cycle Aligned';
                bandLegend = `
                    <div class="jc-band-item"><div class="jc-band-dot foundation"></div>Foundation</div>
                    <div class="jc-band-item"><div class="jc-band-dot ordinary"></div>Ordinary</div>
                    <div class="jc-band-item"><div class="jc-band-dot higher"></div>Higher</div>
                    <div class="jc-band-item"><div class="jc-band-dot mastery"></div>Mastery</div>
                `;
            }
            
            return `
                <div class="jc-level-popup">
                    <div class="jc-popup-content">
                        <div class="jc-popup-header">
                            <h4><i class="fas fa-chart-line"></i> Progressive Learning</h4>
                            <p>Students advance through 12 levels based on success rate and response time. The system adapts to each student's learning pace.</p>
                            <div class="jc-curriculum-badge">
                                ${curriculumBadge}
                            </div>
                        </div>
                        <div class="jc-popup-levels">
                            <div class="jc-level-grid">
                                ${levelsHtml}
                            </div>
                        </div>
                        <div class="jc-band-legend">
                            ${bandLegend}
                        </div>
                    </div>
                    <div class="jc-popup-arrow"></div>
                </div>
            `;
        }
        
        // Get 12-level structure for each topic
        function getTopicLevelData(topicKey) {
            const topicLevels = {
                // ========== NUMERACY STRAND ==========
                'whole_numbers': [
                    {title: 'Reading Numbers', band: 'Foundation'},
                    {title: 'Place Value', band: 'Foundation'},
                    {title: 'Comparing Numbers', band: 'Foundation'},
                    {title: 'Ordering Numbers', band: 'Developing'},
                    {title: 'Rounding (10s, 100s)', band: 'Developing'},
                    {title: 'Rounding (1000s)', band: 'Developing'},
                    {title: 'Large Numbers', band: 'Proficient'},
                    {title: 'Millions', band: 'Proficient'},
                    {title: 'Estimation', band: 'Proficient'},
                    {title: 'Number Properties', band: 'Advanced'},
                    {title: 'Problem Solving', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'addition_subtraction': [
                    {title: 'Adding to 20', band: 'Foundation'},
                    {title: 'Subtracting to 20', band: 'Foundation'},
                    {title: 'Adding 2-Digit', band: 'Foundation'},
                    {title: 'Subtracting 2-Digit', band: 'Developing'},
                    {title: 'Adding 3-Digit', band: 'Developing'},
                    {title: 'Subtracting 3-Digit', band: 'Developing'},
                    {title: 'Word Problems (+)', band: 'Proficient'},
                    {title: 'Word Problems (−)', band: 'Proficient'},
                    {title: 'Mixed Operations', band: 'Proficient'},
                    {title: 'Multi-Step Problems', band: 'Advanced'},
                    {title: 'Estimation', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'multiplication_skills': [
                    {title: 'Times Tables (2,5,10)', band: 'Foundation'},
                    {title: 'Times Tables (3,4)', band: 'Foundation'},
                    {title: 'Times Tables (6,7,8,9)', band: 'Foundation'},
                    {title: 'Multiplying by 10,100', band: 'Developing'},
                    {title: '2-Digit × 1-Digit', band: 'Developing'},
                    {title: '2-Digit × 2-Digit', band: 'Developing'},
                    {title: 'Word Problems', band: 'Proficient'},
                    {title: 'Multi-Step Problems', band: 'Proficient'},
                    {title: 'Estimation', band: 'Proficient'},
                    {title: '3-Digit × 2-Digit', band: 'Advanced'},
                    {title: 'Problem Solving', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'division_skills': [
                    {title: 'Sharing Equally', band: 'Foundation'},
                    {title: 'Division Facts', band: 'Foundation'},
                    {title: 'Dividing by 2,5,10', band: 'Foundation'},
                    {title: 'Short Division', band: 'Developing'},
                    {title: 'Remainders', band: 'Developing'},
                    {title: 'Dividing by 10,100', band: 'Developing'},
                    {title: 'Long Division', band: 'Proficient'},
                    {title: 'Word Problems', band: 'Proficient'},
                    {title: 'Interpreting Remainders', band: 'Proficient'},
                    {title: 'Multi-Step Problems', band: 'Advanced'},
                    {title: 'Problem Solving', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'basic_fractions': [
                    {title: 'What is a Fraction?', band: 'Foundation'},
                    {title: 'Unit Fractions', band: 'Foundation'},
                    {title: 'Fractions of Shapes', band: 'Foundation'},
                    {title: 'Equivalent Fractions', band: 'Developing'},
                    {title: 'Comparing Fractions', band: 'Developing'},
                    {title: 'Simplifying Fractions', band: 'Developing'},
                    {title: 'Adding (Same Denom)', band: 'Proficient'},
                    {title: 'Subtracting (Same Denom)', band: 'Proficient'},
                    {title: 'Fractions of Amounts', band: 'Proficient'},
                    {title: 'Mixed Numbers', band: 'Advanced'},
                    {title: 'Word Problems', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'basic_decimals': [
                    {title: 'Understanding Tenths', band: 'Foundation'},
                    {title: 'Decimal Place Value', band: 'Foundation'},
                    {title: 'Decimals and Money', band: 'Foundation'},
                    {title: 'Understanding Hundredths', band: 'Developing'},
                    {title: 'Comparing Decimals', band: 'Developing'},
                    {title: 'Ordering Decimals', band: 'Developing'},
                    {title: 'Adding Decimals', band: 'Proficient'},
                    {title: 'Subtracting Decimals', band: 'Proficient'},
                    {title: 'Decimals ↔ Fractions', band: 'Proficient'},
                    {title: 'Rounding Decimals', band: 'Advanced'},
                    {title: 'Word Problems', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'basic_percentages': [
                    {title: 'What is Percent?', band: 'Foundation'},
                    {title: '50% and Halves', band: 'Foundation'},
                    {title: '25% and Quarters', band: 'Foundation'},
                    {title: '10% and Tenths', band: 'Developing'},
                    {title: 'Common Percentages', band: 'Developing'},
                    {title: '% ↔ Fractions', band: 'Developing'},
                    {title: '% ↔ Decimals', band: 'Proficient'},
                    {title: 'Finding % of Amount', band: 'Proficient'},
                    {title: 'Percentage Problems', band: 'Proficient'},
                    {title: 'Discounts', band: 'Advanced'},
                    {title: 'Word Problems', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'time_and_clocks': [
                    {title: "O'Clock Times", band: 'Foundation'},
                    {title: 'Half Past', band: 'Foundation'},
                    {title: 'Quarter Past/To', band: 'Foundation'},
                    {title: '5-Minute Intervals', band: 'Developing'},
                    {title: 'Reading Any Time', band: 'Developing'},
                    {title: 'Digital Time', band: 'Developing'},
                    {title: '24-Hour Clock', band: 'Proficient'},
                    {title: 'Elapsed Time', band: 'Proficient'},
                    {title: 'Timetables', band: 'Proficient'},
                    {title: 'Time Calculations', band: 'Advanced'},
                    {title: 'Scheduling Problems', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'money_skills': [
                    {title: 'Coins and Notes', band: 'Foundation'},
                    {title: 'Counting Money', band: 'Foundation'},
                    {title: 'Making Amounts', band: 'Foundation'},
                    {title: 'Adding Money', band: 'Developing'},
                    {title: 'Subtracting Money', band: 'Developing'},
                    {title: 'Giving Change', band: 'Developing'},
                    {title: 'Shopping Problems', band: 'Proficient'},
                    {title: 'Comparing Prices', band: 'Proficient'},
                    {title: 'Budgeting', band: 'Proficient'},
                    {title: 'Multi-Step Problems', band: 'Advanced'},
                    {title: 'Best Value', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'measurement': [
                    {title: 'Length (cm)', band: 'Foundation'},
                    {title: 'Length (m, km)', band: 'Foundation'},
                    {title: 'Measuring Length', band: 'Foundation'},
                    {title: 'Mass (g, kg)', band: 'Developing'},
                    {title: 'Capacity (ml, l)', band: 'Developing'},
                    {title: 'Comparing Measures', band: 'Developing'},
                    {title: 'Converting Length', band: 'Proficient'},
                    {title: 'Converting Mass', band: 'Proficient'},
                    {title: 'Converting Capacity', band: 'Proficient'},
                    {title: 'Mixed Conversions', band: 'Advanced'},
                    {title: 'Word Problems', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'data_and_charts': [
                    {title: 'Tally Charts', band: 'Foundation'},
                    {title: 'Pictograms', band: 'Foundation'},
                    {title: 'Reading Bar Charts', band: 'Foundation'},
                    {title: 'Reading Tables', band: 'Developing'},
                    {title: 'Creating Bar Charts', band: 'Developing'},
                    {title: 'Interpreting Data', band: 'Developing'},
                    {title: 'Finding Mode', band: 'Proficient'},
                    {title: 'Finding Mean', band: 'Proficient'},
                    {title: 'Comparing Data', band: 'Proficient'},
                    {title: 'Data Analysis', band: 'Advanced'},
                    {title: 'Survey Problems', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'number_patterns': [
                    {title: 'Counting Patterns', band: 'Foundation'},
                    {title: 'Adding Patterns', band: 'Foundation'},
                    {title: 'Subtracting Patterns', band: 'Foundation'},
                    {title: 'Times Table Patterns', band: 'Developing'},
                    {title: 'Finding the Rule', band: 'Developing'},
                    {title: 'Continuing Patterns', band: 'Developing'},
                    {title: 'Shape Patterns', band: 'Proficient'},
                    {title: 'Two-Step Patterns', band: 'Proficient'},
                    {title: 'Missing Numbers', band: 'Proficient'},
                    {title: 'Complex Patterns', band: 'Advanced'},
                    {title: 'Pattern Problems', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                // ========== L1LP STRAND ==========
                'awareness_of_environment': [
                    {title: 'Exploring Objects', band: 'Foundation'},
                    {title: 'Objects in Motion', band: 'Foundation'},
                    {title: 'Showing Preferences', band: 'Foundation'},
                    {title: 'Same or Different', band: 'Developing'},
                    {title: 'Matching Objects', band: 'Developing'},
                    {title: 'Sorting by One Thing', band: 'Developing'},
                    {title: 'Cause and Effect', band: 'Progressing'},
                    {title: 'What Happens Next', band: 'Progressing'},
                    {title: 'Object Permanence', band: 'Progressing'},
                    {title: 'Hidden Objects', band: 'Consolidating'},
                    {title: 'Multi-Attribute Sort', band: 'Consolidating'},
                    {title: 'Environment Challenge', band: 'Consolidating'}
                ],
                'pattern_and_sequence': [
                    {title: 'Sensory Patterns', band: 'Foundation'},
                    {title: 'Patterns Around Us', band: 'Foundation'},
                    {title: 'AB Patterns', band: 'Foundation'},
                    {title: 'ABB Patterns', band: 'Developing'},
                    {title: 'ABC Patterns', band: 'Developing'},
                    {title: 'What Comes Next', band: 'Developing'},
                    {title: 'Ordering & Sequencing', band: 'Progressing'},
                    {title: 'Daily Routines', band: 'Progressing'},
                    {title: 'Copying Patterns', band: 'Progressing'},
                    {title: 'First, Next, Last', band: 'Consolidating'},
                    {title: 'Familiar Activities', band: 'Consolidating'},
                    {title: 'Pattern Challenge', band: 'Consolidating'}
                ],
                'developing_number_sense': [
                    {title: 'Counting to 5', band: 'Foundation'},
                    {title: 'Counting to 10', band: 'Foundation'},
                    {title: 'Recognising Numerals', band: 'Foundation'},
                    {title: 'Matching Numbers', band: 'Developing'},
                    {title: 'More or Less', band: 'Developing'},
                    {title: 'Same Amount', band: 'Developing'},
                    {title: 'One More', band: 'Progressing'},
                    {title: 'One Less', band: 'Progressing'},
                    {title: 'Counting to 20', band: 'Progressing'},
                    {title: 'Simple Combining', band: 'Consolidating'},
                    {title: 'Simple Taking Away', band: 'Consolidating'},
                    {title: 'Number Challenge', band: 'Consolidating'}
                ],
                'shape_and_space': [
                    {title: 'Position Words', band: 'Foundation'},
                    {title: 'Movement Words', band: 'Foundation'},
                    {title: 'Circle & Square', band: 'Foundation'},
                    {title: 'Triangle & Rectangle', band: 'Developing'},
                    {title: 'Shapes Around Us', band: 'Developing'},
                    {title: '3D Shapes Intro', band: 'Developing'},
                    {title: 'Ball, Box, Can', band: 'Progressing'},
                    {title: 'Sorting Shapes', band: 'Progressing'},
                    {title: 'Shapes in Life', band: 'Progressing'},
                    {title: 'Sides & Corners', band: 'Consolidating'},
                    {title: 'Describing Shapes', band: 'Consolidating'},
                    {title: 'Shape Challenge', band: 'Consolidating'}
                ],
                'measure_and_data': [
                    {title: 'Big and Small', band: 'Foundation'},
                    {title: 'Long and Short', band: 'Foundation'},
                    {title: 'Heavy and Light', band: 'Foundation'},
                    {title: 'Full and Empty', band: 'Developing'},
                    {title: 'Ordering by Size', band: 'Developing'},
                    {title: 'Recognising Coins', band: 'Developing'},
                    {title: 'Which Costs More', band: 'Progressing'},
                    {title: 'Simple Shopping', band: 'Progressing'},
                    {title: 'Hot and Cold', band: 'Progressing'},
                    {title: 'Reading Pictographs', band: 'Consolidating'},
                    {title: 'Sorting Data', band: 'Consolidating'},
                    {title: 'Measure Challenge', band: 'Consolidating'}
                ],
                'time': [
                    {title: 'Morning & Night', band: 'Foundation'},
                    {title: 'Times of Day', band: 'Foundation'},
                    {title: 'Days of the Week', band: 'Foundation'},
                    {title: 'Daily Routines', band: 'Developing'},
                    {title: 'Seasons', band: 'Developing'},
                    {title: 'Special Events', band: 'Developing'},
                    {title: 'O\'Clock Times', band: 'Progressing'},
                    {title: 'Before and After', band: 'Progressing'},
                    {title: 'Using Timers', band: 'Progressing'},
                    {title: 'Waiting & Turns', band: 'Consolidating'},
                    {title: 'Visual Timetables', band: 'Consolidating'},
                    {title: 'Time Challenge', band: 'Consolidating'}
                ],
                // ========== L2LP STRAND (NCCA-Aligned: 4 Topics × 12 Levels) ==========
                'l2_number_and_money': [
                    {title: 'Numbers in Real Life', band: 'Foundation'},
                    {title: 'Counting Skills', band: 'Foundation'},
                    {title: 'Tens and Ones', band: 'Foundation'},
                    {title: 'Place Value', band: 'Developing'},
                    {title: 'Estimating Amounts', band: 'Developing'},
                    {title: 'Adding & Subtracting', band: 'Developing'},
                    {title: 'Recognising Money', band: 'Progressing'},
                    {title: 'Shopping & Transactions', band: 'Progressing'},
                    {title: 'Totals & Change', band: 'Progressing'},
                    {title: 'Estimating & Rounding', band: 'Consolidating'},
                    {title: 'Bills & Receipts', band: 'Consolidating'},
                    {title: 'Digital Payments', band: 'Consolidating'}
                ],
                'l2_time_management': [
                    {title: 'Time Instruments', band: 'Foundation'},
                    {title: 'Analogue Clocks', band: 'Foundation'},
                    {title: 'Digital Clocks', band: 'Foundation'},
                    {title: '12 and 24 Hour Time', band: 'Developing'},
                    {title: 'Time Language', band: 'Developing'},
                    {title: 'Units of Time', band: 'Developing'},
                    {title: 'Timelines & Timetables', band: 'Progressing'},
                    {title: 'Calculating Time', band: 'Progressing'},
                    {title: 'Time Management Skills', band: 'Progressing'},
                    {title: 'Daily Routines', band: 'Consolidating'},
                    {title: 'Calendars & Planning', band: 'Consolidating'},
                    {title: 'Journey Planning', band: 'Consolidating'}
                ],
                'l2_measurement_location': [
                    {title: 'Comparing Objects', band: 'Foundation'},
                    {title: 'Measurement Language', band: 'Foundation'},
                    {title: 'Metric Units', band: 'Foundation'},
                    {title: 'Measuring Length', band: 'Developing'},
                    {title: 'Comparing Measurements', band: 'Developing'},
                    {title: 'Using Measuring Tools', band: 'Developing'},
                    {title: 'Body in Space', band: 'Progressing'},
                    {title: 'Position Words', band: 'Progressing'},
                    {title: 'Simple Maps', band: 'Progressing'},
                    {title: 'Distance on Maps', band: 'Consolidating'},
                    {title: 'Grid References', band: 'Consolidating'},
                    {title: 'Planning Journeys', band: 'Consolidating'}
                ],
                'l2_shape_pattern_number': [
                    {title: '2D Shapes', band: 'Foundation'},
                    {title: '3D Shapes', band: 'Foundation'},
                    {title: 'Simple Patterns', band: 'Foundation'},
                    {title: 'Number Patterns', band: 'Developing'},
                    {title: 'Symmetry', band: 'Developing'},
                    {title: 'More 2D Shapes', band: 'Developing'},
                    {title: 'Odd & Even Numbers', band: 'Progressing'},
                    {title: 'Fractions', band: 'Progressing'},
                    {title: 'Multiplication Concepts', band: 'Progressing'},
                    {title: 'Division Concepts', band: 'Consolidating'},
                    {title: 'Number Properties', band: 'Consolidating'},
                    {title: 'Problem Solving', band: 'Consolidating'}
                ],
                // ========== JC EXAM TOPICS ==========
                'arithmetic': [
                    {title: 'Addition', band: 'Foundation'},
                    {title: 'Subtraction', band: 'Foundation'},
                    {title: 'Multiplication', band: 'Foundation'},
                    {title: 'Division', band: 'Ordinary'},
                    {title: 'Rounding', band: 'Ordinary'},
                    {title: 'Midpoints', band: 'Ordinary'},
                    {title: 'Factors', band: 'Higher'},
                    {title: 'LCM', band: 'Higher'},
                    {title: 'HCF', band: 'Higher'},
                    {title: 'Powers & Indices', band: 'Mastery'},
                    {title: 'Square & Cube Roots', band: 'Mastery'},
                    {title: 'BODMAS Mixed', band: 'Mastery'}
                ],
                'fractions': [
                    {title: 'Visualising Fractions', band: 'Foundation'},
                    {title: 'Equivalent Fractions', band: 'Foundation'},
                    {title: 'Simplifying Fractions', band: 'Foundation'},
                    {title: 'Comparing Fractions', band: 'Ordinary'},
                    {title: 'Adding Fractions', band: 'Ordinary'},
                    {title: 'Subtracting Fractions', band: 'Ordinary'},
                    {title: 'Multiplying Fractions', band: 'Higher'},
                    {title: 'Dividing Fractions', band: 'Higher'},
                    {title: 'Mixed Numbers', band: 'Higher'},
                    {title: 'Fractions & Decimals', band: 'Mastery'},
                    {title: 'Word Problems', band: 'Mastery'},
                    {title: 'Complex Problems', band: 'Mastery'}
                ],
                'percentages': [
                    {title: 'Understanding %', band: 'Foundation'},
                    {title: '% of Amounts', band: 'Foundation'},
                    {title: 'Common %', band: 'Foundation'},
                    {title: '% Increase/Decrease', band: 'Ordinary'},
                    {title: 'Finding Original', band: 'Ordinary'},
                    {title: '% Change', band: 'Ordinary'},
                    {title: 'Profit & Loss', band: 'Higher'},
                    {title: 'Simple Interest', band: 'Higher'},
                    {title: 'Compound Interest', band: 'Higher'},
                    {title: 'VAT & Tax', band: 'Mastery'},
                    {title: 'Multi-step Problems', band: 'Mastery'},
                    {title: 'Financial Maths', band: 'Mastery'}
                ],
                'decimals': [
                    {title: 'Place Value', band: 'Foundation'},
                    {title: 'Comparing Decimals', band: 'Foundation'},
                    {title: 'Add & Subtract', band: 'Foundation'},
                    {title: 'Multiply by Whole', band: 'Ordinary'},
                    {title: 'Divide by Whole', band: 'Ordinary'},
                    {title: 'Rounding', band: 'Ordinary'},
                    {title: 'Decimals ↔ Fractions', band: 'Higher'},
                    {title: 'Decimals ↔ Percent', band: 'Higher'},
                    {title: 'Multiply Decimals', band: 'Higher'},
                    {title: 'Divide Decimals', band: 'Mastery'},
                    {title: 'Estimation', band: 'Mastery'},
                    {title: 'Multi-step Problems', band: 'Mastery'}
                ],
                'ratio': [
                    {title: 'Understanding Ratio', band: 'Foundation'},
                    {title: 'Simplifying Ratios', band: 'Foundation'},
                    {title: 'Equivalent Ratios', band: 'Foundation'},
                    {title: 'Dividing in Ratio', band: 'Ordinary'},
                    {title: 'Ratio & Fractions', band: 'Ordinary'},
                    {title: 'Comparing Ratios', band: 'Ordinary'},
                    {title: 'Scale & Maps', band: 'Higher'},
                    {title: 'Ratio Problems', band: 'Higher'},
                    {title: 'Direct Proportion', band: 'Higher'},
                    {title: 'Inverse Proportion', band: 'Mastery'},
                    {title: 'Combined Ratios', band: 'Mastery'},
                    {title: 'Complex Problems', band: 'Mastery'}
                ],
                'sets': [
                    {title: 'Set Notation', band: 'Foundation'},
                    {title: 'Elements & Subsets', band: 'Foundation'},
                    {title: 'Venn Diagrams Intro', band: 'Foundation'},
                    {title: 'Union & Intersection', band: 'Ordinary'},
                    {title: 'Complement', band: 'Ordinary'},
                    {title: 'Two-Set Venns', band: 'Ordinary'},
                    {title: 'Three-Set Venns', band: 'Higher'},
                    {title: 'Set Builder Notation', band: 'Higher'},
                    {title: 'Counting with Sets', band: 'Higher'},
                    {title: 'Set Proofs', band: 'Mastery'},
                    {title: 'Problem Solving', band: 'Mastery'},
                    {title: 'Applications', band: 'Mastery'}
                ],
                'descriptive_statistics': [
                    {title: 'Mean', band: 'Foundation'},
                    {title: 'Median', band: 'Foundation'},
                    {title: 'Mode', band: 'Foundation'},
                    {title: 'Range', band: 'Ordinary'},
                    {title: 'Frequency Tables', band: 'Ordinary'},
                    {title: 'Grouped Data', band: 'Ordinary'},
                    {title: 'Quartiles', band: 'Higher'},
                    {title: 'IQR', band: 'Higher'},
                    {title: 'Standard Deviation', band: 'Higher'},
                    {title: 'Data Comparison', band: 'Mastery'},
                    {title: 'Outliers', band: 'Mastery'},
                    {title: 'Analysis', band: 'Mastery'}
                ],
                'patterns': [
                    {title: 'Recognising Patterns', band: 'Foundation'},
                    {title: 'Continuing Sequences', band: 'Foundation'},
                    {title: 'Visual Patterns', band: 'Foundation'},
                    {title: 'Linear Sequences', band: 'Ordinary'},
                    {title: 'Finding nth Term', band: 'Ordinary'},
                    {title: 'Using Formulae', band: 'Ordinary'},
                    {title: 'Quadratic Sequences', band: 'Higher'},
                    {title: 'Geometric Sequences', band: 'Higher'},
                    {title: 'Combined Patterns', band: 'Higher'},
                    {title: 'Sequence Proofs', band: 'Mastery'},
                    {title: 'Real-World Patterns', band: 'Mastery'},
                    {title: 'Complex Sequences', band: 'Mastery'}
                ],
                'functions': [
                    {title: 'Function Notation', band: 'Foundation'},
                    {title: 'Input/Output', band: 'Foundation'},
                    {title: 'Linear Functions', band: 'Foundation'},
                    {title: 'Graphing Lines', band: 'Ordinary'},
                    {title: 'Slope & Intercept', band: 'Ordinary'},
                    {title: 'Interpreting Graphs', band: 'Ordinary'},
                    {title: 'Quadratic Functions', band: 'Higher'},
                    {title: 'Graphing Parabolas', band: 'Higher'},
                    {title: 'Domain & Range', band: 'Higher'},
                    {title: 'Transformations', band: 'Mastery'},
                    {title: 'Composite Functions', band: 'Mastery'},
                    {title: 'Applications', band: 'Mastery'}
                ],
                'area_perimeter_volume': [
                    {title: 'Perimeter Basics', band: 'Foundation'},
                    {title: 'Area of Rectangles', band: 'Foundation'},
                    {title: 'Area of Triangles', band: 'Foundation'},
                    {title: 'Compound Shapes', band: 'Ordinary'},
                    {title: 'Circles: C & A', band: 'Ordinary'},
                    {title: 'Volume of Cuboids', band: 'Ordinary'},
                    {title: 'Volume of Prisms', band: 'Higher'},
                    {title: 'Volume of Cylinders', band: 'Higher'},
                    {title: 'Surface Area', band: 'Higher'},
                    {title: 'Cones & Spheres', band: 'Mastery'},
                    {title: 'Composite Solids', band: 'Mastery'},
                    {title: 'Problem Solving', band: 'Mastery'}
                ],
                'solving_equations': [
                    {title: 'One-Step Equations', band: 'Foundation'},
                    {title: 'Two-Step Equations', band: 'Foundation'},
                    {title: 'Equations with x', band: 'Foundation'},
                    {title: 'Brackets', band: 'Ordinary'},
                    {title: 'Variables Both Sides', band: 'Ordinary'},
                    {title: 'Forming Equations', band: 'Ordinary'},
                    {title: 'Simultaneous (Subst)', band: 'Higher'},
                    {title: 'Simultaneous (Elim)', band: 'Higher'},
                    {title: 'Quadratic Factoring', band: 'Higher'},
                    {title: 'Quadratic Formula', band: 'Mastery'},
                    {title: 'Inequalities', band: 'Mastery'},
                    {title: 'Problem Solving', band: 'Mastery'}
                ],
                'simultaneous_equations': [
                    {title: 'Understanding Systems', band: 'Foundation'},
                    {title: 'Solving by Inspection', band: 'Foundation'},
                    {title: 'Graphical Method', band: 'Foundation'},
                    {title: 'Elimination - Same', band: 'Ordinary'},
                    {title: 'Elimination - Mult One', band: 'Ordinary'},
                    {title: 'Elimination - Mult Both', band: 'Ordinary'},
                    {title: 'Substitution Simple', band: 'Higher'},
                    {title: 'Substitution Rearrange', band: 'Higher'},
                    {title: 'Choosing Method', band: 'Higher'},
                    {title: 'Word Problems Setup', band: 'Mastery'},
                    {title: 'Word Problems Solve', band: 'Mastery'},
                    {title: 'Complex Applications', band: 'Mastery'}
                ],
                'linear_inequalities': [
                    {title: 'Inequality Symbols', band: 'Foundation'},
                    {title: 'Reading Number Lines', band: 'Foundation'},
                    {title: 'Real-World Inequalities', band: 'Foundation'},
                    {title: 'Graphing (x ∈ ℝ)', band: 'Ordinary'},
                    {title: 'Integer Restrictions', band: 'Ordinary'},
                    {title: 'One-Step Solving', band: 'Ordinary'},
                    {title: 'Two-Step Solving', band: 'Higher'},
                    {title: 'Compound Inequalities', band: 'Higher'},
                    {title: 'Negative Coefficients', band: 'Higher'},
                    {title: 'Word Problems', band: 'Mastery'},
                    {title: 'Rounding & Tolerance', band: 'Mastery'},
                    {title: 'Multi-step Problems', band: 'Mastery'}
                ],
                'probability': [
                    {title: 'Likelihood Language', band: 'Foundation'},
                    {title: 'Probability Scale', band: 'Foundation'},
                    {title: 'Simple Probability', band: 'Foundation'},
                    {title: 'Sample Spaces', band: 'Ordinary'},
                    {title: 'Experimental Prob', band: 'Ordinary'},
                    {title: 'Expected Outcomes', band: 'Ordinary'},
                    {title: 'Two Events', band: 'Higher'},
                    {title: 'Tree Diagrams', band: 'Higher'},
                    {title: 'Without Replacement', band: 'Higher'},
                    {title: 'Conditional Prob', band: 'Mastery'},
                    {title: 'Combined Events', band: 'Mastery'},
                    {title: 'Problem Solving', band: 'Mastery'}
                ],
                'coordinate_geometry': [
                    {title: 'Plotting Points', band: 'Foundation'},
                    {title: 'Reading Coordinates', band: 'Foundation'},
                    {title: 'Distance: Counting', band: 'Foundation'},
                    {title: 'Midpoint', band: 'Ordinary'},
                    {title: 'Slope', band: 'Ordinary'},
                    {title: 'Distance Formula', band: 'Ordinary'},
                    {title: 'Equation of Line', band: 'Higher'},
                    {title: 'Parallel Lines', band: 'Higher'},
                    {title: 'Perpendicular Lines', band: 'Higher'},
                    {title: 'Line Intersection', band: 'Mastery'},
                    {title: 'Area from Coords', band: 'Mastery'},
                    {title: 'Problem Solving', band: 'Mastery'}
                ],
                'trigonometry': [
                    {title: 'Right Triangle Parts', band: 'Foundation'},
                    {title: 'Identifying Sides', band: 'Foundation'},
                    {title: 'Trig Ratios Intro', band: 'Foundation'},
                    {title: 'Finding Sides', band: 'Ordinary'},
                    {title: 'Finding Angles', band: 'Ordinary'},
                    {title: 'Pythagoras', band: 'Ordinary'},
                    {title: 'Multi-Step Problems', band: 'Higher'},
                    {title: 'Angles of Elevation', band: 'Higher'},
                    {title: 'Area of Triangle', band: 'Higher'},
                    {title: 'Sine Rule', band: 'Mastery'},
                    {title: 'Cosine Rule', band: 'Mastery'},
                    {title: 'Problem Solving', band: 'Mastery'}
                ],
                'number_systems': [
                    {title: 'Understanding Integers', band: 'Foundation'},
                    {title: 'Number Line', band: 'Foundation'},
                    {title: 'Adding Integers', band: 'Foundation'},
                    {title: 'Subtracting Integers', band: 'Ordinary'},
                    {title: 'Multiplying Integers', band: 'Ordinary'},
                    {title: 'Dividing Integers', band: 'Ordinary'},
                    {title: 'Order of Operations', band: 'Higher'},
                    {title: 'Absolute Value', band: 'Higher'},
                    {title: 'Factors & Multiples', band: 'Higher'},
                    {title: 'Prime Numbers', band: 'Mastery'},
                    {title: 'HCF & LCM', band: 'Mastery'},
                    {title: 'Problem Solving', band: 'Mastery'}
                ],
                'indices': [
                    {title: 'Index Notation', band: 'Foundation'},
                    {title: 'Squares & Cubes', band: 'Foundation'},
                    {title: 'Multiplication Law', band: 'Foundation'},
                    {title: 'Division Law', band: 'Ordinary'},
                    {title: 'Power of Power', band: 'Ordinary'},
                    {title: 'Zero & Negative', band: 'Ordinary'},
                    {title: 'Fractional Indices', band: 'Higher'},
                    {title: 'Scientific: Large', band: 'Higher'},
                    {title: 'Scientific: Small', band: 'Higher'},
                    {title: 'Sci Notation Calc', band: 'Mastery'},
                    {title: 'Mixed Problems', band: 'Mastery'},
                    {title: 'Applications', band: 'Mastery'}
                ],
                'geometry': [
                    {title: 'Naming Shapes', band: 'Foundation'},
                    {title: 'Angles in Triangle', band: 'Foundation'},
                    {title: 'Quadrilaterals', band: 'Foundation'},
                    {title: 'Parallel Lines', band: 'Ordinary'},
                    {title: 'Symmetry', band: 'Ordinary'},
                    {title: 'Constructions', band: 'Ordinary'},
                    {title: 'Pythagoras', band: 'Higher'},
                    {title: 'Similar Triangles', band: 'Higher'},
                    {title: 'Scale Drawings', band: 'Higher'},
                    {title: 'Circle Properties', band: 'Mastery'},
                    {title: 'Adv. Constructions', band: 'Mastery'},
                    {title: 'Proofs', band: 'Mastery'}
                ],
                'introductory_algebra': [
                    {title: 'Variables & Terms', band: 'Foundation'},
                    {title: 'Like Terms', band: 'Foundation'},
                    {title: 'Simplifying', band: 'Foundation'},
                    {title: 'Substitution', band: 'Ordinary'},
                    {title: 'Expanding Brackets', band: 'Ordinary'},
                    {title: 'Single Brackets', band: 'Ordinary'},
                    {title: 'Double Brackets', band: 'Higher'},
                    {title: 'Factorising', band: 'Higher'},
                    {title: 'Algebraic Fractions', band: 'Higher'},
                    {title: 'Complex Expressions', band: 'Mastery'},
                    {title: 'Problem Solving', band: 'Mastery'},
                    {title: 'SEC Exam Style', band: 'Mastery'}
                ],
                'simplifying_expressions': [
                    {title: 'Recognising Like Terms', band: 'Foundation'},
                    {title: 'Collecting Terms', band: 'Foundation'},
                    {title: 'Two Variables', band: 'Foundation'},
                    {title: 'Multiplying Terms', band: 'Ordinary'},
                    {title: 'Single Brackets', band: 'Ordinary'},
                    {title: 'Expand & Simplify', band: 'Ordinary'},
                    {title: 'Double Brackets', band: 'Higher'},
                    {title: 'Special Products', band: 'Higher'},
                    {title: 'Mixed Expanding', band: 'Higher'},
                    {title: 'Common Factor', band: 'Mastery'},
                    {title: 'Quadratic Factorising', band: 'Mastery'},
                    {title: 'Complex Expressions', band: 'Mastery'}
                ],
                'expanding_factorising': [
                    {title: 'Single Brackets', band: 'Foundation'},
                    {title: 'Subtraction', band: 'Foundation'},
                    {title: 'Negative Multiplier', band: 'Foundation'},
                    {title: 'Double Brackets', band: 'Ordinary'},
                    {title: 'Expand & Simplify', band: 'Ordinary'},
                    {title: 'Perfect Squares', band: 'Ordinary'},
                    {title: 'Common Factor', band: 'Higher'},
                    {title: 'Quadratic (Positive)', band: 'Higher'},
                    {title: 'Quadratic (Mixed)', band: 'Higher'},
                    {title: 'Difference of Squares', band: 'Mastery'},
                    {title: 'Factorise Fully', band: 'Mastery'},
                    {title: 'SEC Exam Style', band: 'Mastery'}
                ],
                'applied_arithmetic': [
                    {title: 'Bills & Receipts', band: 'Foundation'},
                    {title: 'Wages & Hours', band: 'Foundation'},
                    {title: 'Overtime Pay', band: 'Foundation'},
                    {title: 'Gross Pay', band: 'Ordinary'},
                    {title: 'Income Tax Basics', band: 'Ordinary'},
                    {title: 'Tax Credits', band: 'Ordinary'},
                    {title: 'Net Income', band: 'Higher'},
                    {title: 'PRSI', band: 'Higher'},
                    {title: 'Multi-rate Tax', band: 'Higher'},
                    {title: 'USC Bands', band: 'Mastery'},
                    {title: 'Complete Payslip', band: 'Mastery'},
                    {title: 'SEC Exam Style', band: 'Mastery'}
                ],
                'currency': [
                    {title: 'Exchange Rates', band: 'Foundation'},
                    {title: 'EUR to GBP', band: 'Foundation'},
                    {title: 'EUR to USD', band: 'Foundation'},
                    {title: 'Decimal Amounts', band: 'Ordinary'},
                    {title: 'Reverse Conversion', band: 'Ordinary'},
                    {title: 'USD Both Ways', band: 'Ordinary'},
                    {title: 'Price Comparison', band: 'Higher'},
                    {title: 'Multi-step', band: 'Higher'},
                    {title: 'Best Rate', band: 'Higher'},
                    {title: 'Commission & Fees', band: 'Mastery'},
                    {title: 'Travel Budget', band: 'Mastery'},
                    {title: 'Complex Currency', band: 'Mastery'}
                ],
                'speed_distance_time': [
                    {title: 'Understanding Formula', band: 'Foundation'},
                    {title: 'Finding Speed', band: 'Foundation'},
                    {title: 'Distance & Time', band: 'Foundation'},
                    {title: 'Time in Minutes', band: 'Ordinary'},
                    {title: 'Different Units', band: 'Ordinary'},
                    {title: 'Hours & Minutes', band: 'Ordinary'},
                    {title: 'Flight Problems', band: 'Higher'},
                    {title: 'Cycling/Running', band: 'Higher'},
                    {title: 'Two-Part Journeys', band: 'Higher'},
                    {title: 'Catching Up', band: 'Mastery'},
                    {title: 'D-T Graphs', band: 'Mastery'},
                    {title: 'Complex Problems', band: 'Mastery'}
                ],
                // ========== LC HIGHER LEVEL STRAND ==========
                'lc_hl_calculus_diff': [
                    {title: 'Power Rule', band: 'Foundation'},
                    {title: 'Chain Rule', band: 'Foundation'},
                    {title: 'Product Rule', band: 'Foundation'},
                    {title: 'Quotient Rule', band: 'Developing'},
                    {title: 'Trig Differentiation', band: 'Developing'},
                    {title: 'Exponential & Log', band: 'Developing'},
                    {title: 'Tangents & Normals', band: 'Proficient'},
                    {title: 'Related Rates', band: 'Proficient'},
                    {title: 'Max/Min Problems', band: 'Proficient'},
                    {title: 'First Principles', band: 'Advanced'},
                    {title: 'Applied Optimization', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_hl_calculus_int': [
                    {title: 'Basic Integration', band: 'Foundation'},
                    {title: 'Power Rule Integration', band: 'Foundation'},
                    {title: 'Trig Integration', band: 'Foundation'},
                    {title: 'Exponential Integration', band: 'Developing'},
                    {title: 'Definite Integrals', band: 'Developing'},
                    {title: 'Area Under Curve', band: 'Developing'},
                    {title: 'Area Between Curves', band: 'Proficient'},
                    {title: 'Average Value', band: 'Proficient'},
                    {title: 'Applied Integration', band: 'Proficient'},
                    {title: 'Optimization Setup', band: 'Advanced'},
                    {title: 'Complex Applications', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_hl_algebra': [
                    {title: 'Linear Equations', band: 'Foundation'},
                    {title: 'Quadratic Equations', band: 'Foundation'},
                    {title: 'Simultaneous (2 var)', band: 'Foundation'},
                    {title: 'Inequalities', band: 'Developing'},
                    {title: 'Modulus Equations', band: 'Developing'},
                    {title: 'Factor Theorem', band: 'Developing'},
                    {title: 'Discriminant', band: 'Proficient'},
                    {title: 'Polynomial Division', band: 'Proficient'},
                    {title: 'Indices & Logs', band: 'Proficient'},
                    {title: 'Simultaneous (3 var)', band: 'Advanced'},
                    {title: 'Complex Equations', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_hl_sequences': [
                    {title: 'Arithmetic Sequences', band: 'Foundation'},
                    {title: 'Arithmetic Series', band: 'Foundation'},
                    {title: 'Geometric Sequences', band: 'Foundation'},
                    {title: 'Geometric Series', band: 'Developing'},
                    {title: 'Sum to Infinity', band: 'Developing'},
                    {title: 'Sigma Notation', band: 'Developing'},
                    {title: 'Applied Arithmetic', band: 'Proficient'},
                    {title: 'Applied Geometric', band: 'Proficient'},
                    {title: 'Mixed Problems', band: 'Proficient'},
                    {title: 'Recursive Sequences', band: 'Advanced'},
                    {title: 'Complex Applications', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_hl_complex': [
                    {title: 'Complex Operations', band: 'Foundation'},
                    {title: 'Complex Division', band: 'Foundation'},
                    {title: 'Argand Diagram', band: 'Foundation'},
                    {title: 'Modulus & Argument', band: 'Developing'},
                    {title: 'Polar Form', band: 'Developing'},
                    {title: 'Polar Multiplication', band: 'Developing'},
                    {title: 'De Moivre Powers', band: 'Proficient'},
                    {title: 'Roots of Complex', band: 'Proficient'},
                    {title: 'Complex Equations', band: 'Proficient'},
                    {title: 'Identity Proofs', band: 'Advanced'},
                    {title: 'Argand Geometry', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_hl_functions': [
                    {title: 'Function Notation', band: 'Foundation'},
                    {title: 'Domain & Range', band: 'Foundation'},
                    {title: 'Composite Functions', band: 'Foundation'},
                    {title: 'Inverse Functions', band: 'Developing'},
                    {title: 'Exponential Functions', band: 'Developing'},
                    {title: 'Logarithmic Functions', band: 'Developing'},
                    {title: 'Transformations', band: 'Proficient'},
                    {title: 'Graphing Functions', band: 'Proficient'},
                    {title: 'Piecewise Functions', band: 'Proficient'},
                    {title: 'Exponential Models', band: 'Advanced'},
                    {title: 'Complex Functions', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_hl_financial': [
                    {title: 'Compound Interest', band: 'Foundation'},
                    {title: 'Depreciation', band: 'Foundation'},
                    {title: 'Percentage Change', band: 'Foundation'},
                    {title: 'Present Value', band: 'Developing'},
                    {title: 'Future Value', band: 'Developing'},
                    {title: 'Regular Savings', band: 'Developing'},
                    {title: 'Geometric Series', band: 'Proficient'},
                    {title: 'Loan Calculations', band: 'Proficient'},
                    {title: 'AER', band: 'Proficient'},
                    {title: 'Mortgage Problems', band: 'Advanced'},
                    {title: 'Complex Applications', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_hl_proof': [
                    {title: 'Direct Proof Basics', band: 'Foundation'},
                    {title: 'Algebraic Proof', band: 'Foundation'},
                    {title: 'Proof Structure', band: 'Foundation'},
                    {title: 'Induction Basics', band: 'Developing'},
                    {title: 'Induction - Series', band: 'Developing'},
                    {title: 'Induction - Divisibility', band: 'Developing'},
                    {title: 'Contradiction Basics', band: 'Proficient'},
                    {title: '√2 Irrational', band: 'Proficient'},
                    {title: 'Geometric Proofs', band: 'Proficient'},
                    {title: 'Complex Induction', band: 'Advanced'},
                    {title: 'Mixed Proof Types', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_hl_probability': [
                    {title: 'Basic Probability', band: 'Foundation'},
                    {title: 'Addition Rule', band: 'Foundation'},
                    {title: 'Multiplication Rule', band: 'Foundation'},
                    {title: 'Conditional Probability', band: 'Developing'},
                    {title: 'Tree Diagrams', band: 'Developing'},
                    {title: 'Independence', band: 'Developing'},
                    {title: 'Binomial Distribution', band: 'Proficient'},
                    {title: 'Expected Value', band: 'Proficient'},
                    {title: "Bayes' Theorem", band: 'Proficient'},
                    {title: 'Negative Binomial', band: 'Advanced'},
                    {title: 'Complex Applications', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_hl_statistics': [
                    {title: 'Descriptive Stats', band: 'Foundation'},
                    {title: 'Mean & Standard Dev', band: 'Foundation'},
                    {title: 'Quartiles & IQR', band: 'Foundation'},
                    {title: 'Normal Distribution', band: 'Developing'},
                    {title: 'Z-Scores', band: 'Developing'},
                    {title: 'Inverse Normal', band: 'Developing'},
                    {title: 'Confidence Intervals', band: 'Proficient'},
                    {title: 'Hypothesis Testing', band: 'Proficient'},
                    {title: 'P-Values', band: 'Proficient'},
                    {title: 'Sample Size', band: 'Advanced'},
                    {title: 'Two-Tailed Tests', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_hl_coord_geom': [
                    {title: 'Distance & Midpoint', band: 'Foundation'},
                    {title: 'Slope & Equations', band: 'Foundation'},
                    {title: 'Parallel & Perpendicular', band: 'Foundation'},
                    {title: 'Line Intersection', band: 'Developing'},
                    {title: 'Perpendicular Distance', band: 'Developing'},
                    {title: 'Division of Segment', band: 'Developing'},
                    {title: 'Circle Equation', band: 'Proficient'},
                    {title: 'Tangent to Circle', band: 'Proficient'},
                    {title: 'Circle & Line', band: 'Proficient'},
                    {title: 'Touching Circles', band: 'Advanced'},
                    {title: 'Complex Loci', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_hl_trigonometry': [
                    {title: 'Trig Ratios', band: 'Foundation'},
                    {title: 'Exact Values', band: 'Foundation'},
                    {title: 'Sine Rule', band: 'Foundation'},
                    {title: 'Cosine Rule', band: 'Developing'},
                    {title: 'Area of Triangle', band: 'Developing'},
                    {title: 'Trig Equations', band: 'Developing'},
                    {title: 'Compound Angles', band: 'Proficient'},
                    {title: 'Double Angles', band: 'Proficient'},
                    {title: '3D Trigonometry', band: 'Proficient'},
                    {title: 'Trig Proofs', band: 'Advanced'},
                    {title: 'Complex Applications', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_hl_geometry': [
                    {title: 'Basic Constructions', band: 'Foundation'},
                    {title: 'Triangle Properties', band: 'Foundation'},
                    {title: 'Circle Theorems', band: 'Foundation'},
                    {title: 'Congruent Triangles', band: 'Developing'},
                    {title: 'Similar Triangles', band: 'Developing'},
                    {title: 'Enlargement', band: 'Developing'},
                    {title: 'Orthocentre', band: 'Proficient'},
                    {title: 'Circumcentre', band: 'Proficient'},
                    {title: 'Centroid', band: 'Proficient'},
                    {title: 'Theorem Proofs', band: 'Advanced'},
                    {title: 'Complex Constructions', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_hl_mensuration': [
                    {title: 'Area of Shapes', band: 'Foundation'},
                    {title: 'Volume - Prisms', band: 'Foundation'},
                    {title: 'Volume - Cylinders', band: 'Foundation'},
                    {title: 'Volume - Cones', band: 'Developing'},
                    {title: 'Volume - Spheres', band: 'Developing'},
                    {title: 'Surface Area', band: 'Developing'},
                    {title: 'Composite Solids', band: 'Proficient'},
                    {title: 'Similar Solids', band: 'Proficient'},
                    {title: 'Cone Nets', band: 'Proficient'},
                    {title: 'Frustum', band: 'Advanced'},
                    {title: 'Inscribed Solids', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_hl_counting': [
                    {title: 'Counting Principle', band: 'Foundation'},
                    {title: 'Permutations', band: 'Foundation'},
                    {title: 'Combinations', band: 'Foundation'},
                    {title: 'nPr and nCr', band: 'Developing'},
                    {title: 'Arrangements', band: 'Developing'},
                    {title: 'Selections', band: 'Developing'},
                    {title: 'Constrained Counting', band: 'Proficient'},
                    {title: 'With Repetition', band: 'Proficient'},
                    {title: 'Grid Paths', band: 'Proficient'},
                    {title: 'Complex Constraints', band: 'Advanced'},
                    {title: 'Pairing Problems', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                // ========== LC ORDINARY LEVEL STRAND ==========
                'lc_ol_calculus': [
                    {title: 'Power Rule Basics', band: 'Foundation'},
                    {title: 'Differentiating Polynomials', band: 'Foundation'},
                    {title: 'Negative Indices', band: 'Foundation'},
                    {title: 'Finding Slopes', band: 'Developing'},
                    {title: 'Equations of Tangents', band: 'Developing'},
                    {title: 'Rate of Change', band: 'Developing'},
                    {title: 'Increasing/Decreasing', band: 'Proficient'},
                    {title: 'Max & Min Values', band: 'Proficient'},
                    {title: 'Second Derivative', band: 'Proficient'},
                    {title: 'Applied Max/Min', band: 'Advanced'},
                    {title: 'Optimisation Problems', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_ol_financial': [
                    {title: 'VAT Calculations', band: 'Foundation'},
                    {title: 'Percentage Increase', band: 'Foundation'},
                    {title: 'Percentage Decrease', band: 'Foundation'},
                    {title: 'Profit & Loss', band: 'Developing'},
                    {title: 'Margin & Markup', band: 'Developing'},
                    {title: 'Income Tax Bands', band: 'Developing'},
                    {title: 'Simple Interest', band: 'Proficient'},
                    {title: 'Compound Interest', band: 'Proficient'},
                    {title: 'Depreciation', band: 'Proficient'},
                    {title: 'Multi-Year Compound', band: 'Advanced'},
                    {title: 'Complex Tax Problems', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_ol_trigonometry': [
                    {title: 'Right Angle Trig', band: 'Foundation'},
                    {title: 'SOHCAHTOA', band: 'Foundation'},
                    {title: 'Finding Angles', band: 'Foundation'},
                    {title: 'Sine Rule', band: 'Developing'},
                    {title: 'Cosine Rule', band: 'Developing'},
                    {title: 'Area Formula ½abSinC', band: 'Developing'},
                    {title: 'Two Triangles', band: 'Proficient'},
                    {title: 'Navigation Problems', band: 'Proficient'},
                    {title: 'Elevation/Depression', band: 'Proficient'},
                    {title: 'Combined Triangles', band: 'Advanced'},
                    {title: 'Real-World Applications', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_ol_mensuration': [
                    {title: 'Volume - Cylinders', band: 'Foundation'},
                    {title: 'Surface Area - Cylinders', band: 'Foundation'},
                    {title: 'Volume - Cones', band: 'Foundation'},
                    {title: 'Volume - Spheres', band: 'Developing'},
                    {title: 'Surface Area - Cones', band: 'Developing'},
                    {title: 'Surface Area - Spheres', band: 'Developing'},
                    {title: 'Composite Solids', band: 'Proficient'},
                    {title: 'Sectors & Arcs', band: 'Proficient'},
                    {title: 'Similar Shapes', band: 'Proficient'},
                    {title: 'Scaling Volumes', band: 'Advanced'},
                    {title: 'Complex Composites', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_ol_statistics_desc': [
                    {title: 'Mean & Mode', band: 'Foundation'},
                    {title: 'Median & Range', band: 'Foundation'},
                    {title: 'Reading Charts', band: 'Foundation'},
                    {title: 'Standard Deviation', band: 'Developing'},
                    {title: 'Frequency Tables', band: 'Developing'},
                    {title: 'Histograms', band: 'Developing'},
                    {title: 'Quartiles & IQR', band: 'Proficient'},
                    {title: 'Box Plots', band: 'Proficient'},
                    {title: 'Comparing Data Sets', band: 'Proficient'},
                    {title: 'Outliers', band: 'Advanced'},
                    {title: 'Data Interpretation', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_ol_probability': [
                    {title: 'Basic Probability', band: 'Foundation'},
                    {title: 'Sample Spaces', band: 'Foundation'},
                    {title: 'Addition Rule', band: 'Foundation'},
                    {title: 'Multiplication Rule', band: 'Developing'},
                    {title: 'Tree Diagrams', band: 'Developing'},
                    {title: 'Counting Principle', band: 'Developing'},
                    {title: 'Without Replacement', band: 'Proficient'},
                    {title: 'Conditional Probability', band: 'Proficient'},
                    {title: 'Expected Value', band: 'Proficient'},
                    {title: 'Geometric Probability', band: 'Advanced'},
                    {title: 'Complex Tree Diagrams', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_ol_applied_measure': [
                    {title: 'Unit Conversions', band: 'Foundation'},
                    {title: 'Area Calculations', band: 'Foundation'},
                    {title: 'Perimeter', band: 'Foundation'},
                    {title: 'Trapezoidal Rule', band: 'Developing'},
                    {title: 'Scale Factors', band: 'Developing'},
                    {title: 'Proportion Problems', band: 'Developing'},
                    {title: 'Speed/Distance/Time', band: 'Proficient'},
                    {title: 'Work Rate Problems', band: 'Proficient'},
                    {title: 'Combined Rates', band: 'Proficient'},
                    {title: 'LCM Applications', band: 'Advanced'},
                    {title: 'Complex Conversions', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_ol_sequences': [
                    {title: 'Number Patterns', band: 'Foundation'},
                    {title: 'Arithmetic Sequences', band: 'Foundation'},
                    {title: 'Finding Tₙ', band: 'Foundation'},
                    {title: 'Tₙ = a + (n-1)d', band: 'Developing'},
                    {title: 'Finding n', band: 'Developing'},
                    {title: 'Arithmetic Series Sₙ', band: 'Developing'},
                    {title: 'Sₙ Formula', band: 'Proficient'},
                    {title: 'Quadratic Patterns', band: 'Proficient'},
                    {title: 'Pattern Problems', band: 'Proficient'},
                    {title: 'Finding Formula from Pattern', band: 'Advanced'},
                    {title: 'Applied Sequences', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_ol_algebra': [
                    {title: 'Linear Equations', band: 'Foundation'},
                    {title: 'Substitution', band: 'Foundation'},
                    {title: 'Transposing Formulae', band: 'Foundation'},
                    {title: 'Simultaneous (Linear)', band: 'Developing'},
                    {title: 'Quadratic Equations', band: 'Developing'},
                    {title: 'Using the Formula', band: 'Developing'},
                    {title: 'Linear + Quadratic', band: 'Proficient'},
                    {title: 'Inequalities', band: 'Proficient'},
                    {title: 'Forming Equations', band: 'Proficient'},
                    {title: 'Word Problems', band: 'Advanced'},
                    {title: 'Complex Simultaneous', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_ol_functions': [
                    {title: 'Function Notation', band: 'Foundation'},
                    {title: 'Evaluating f(x)', band: 'Foundation'},
                    {title: 'Linear Graphs', band: 'Foundation'},
                    {title: 'Quadratic Graphs', band: 'Developing'},
                    {title: 'Roots from Graphs', band: 'Developing'},
                    {title: 'Sketching Parabolas', band: 'Developing'},
                    {title: 'Graph Transformations', band: 'Proficient'},
                    {title: 'Exponential Graphs', band: 'Proficient'},
                    {title: 'Interpreting Graphs', band: 'Proficient'},
                    {title: 'Growth/Decay Models', band: 'Advanced'},
                    {title: 'Real-World Functions', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_ol_statistics_inf': [
                    {title: 'Sampling Basics', band: 'Foundation'},
                    {title: 'Types of Sampling', band: 'Foundation'},
                    {title: 'Bias in Sampling', band: 'Foundation'},
                    {title: 'Normal Distribution', band: 'Developing'},
                    {title: 'Z-Scores', band: 'Developing'},
                    {title: 'Using Tables', band: 'Developing'},
                    {title: 'Margin of Error', band: 'Proficient'},
                    {title: 'Confidence Intervals', band: 'Proficient'},
                    {title: 'Sample Proportion', band: 'Proficient'},
                    {title: 'Hypothesis Testing', band: 'Advanced'},
                    {title: 'Comparing Proportions', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_ol_coord_lines': [
                    {title: 'Distance Formula', band: 'Foundation'},
                    {title: 'Midpoint Formula', band: 'Foundation'},
                    {title: 'Slope Calculation', band: 'Foundation'},
                    {title: 'Equation y = mx + c', band: 'Developing'},
                    {title: 'Parallel Lines', band: 'Developing'},
                    {title: 'Perpendicular Lines', band: 'Developing'},
                    {title: 'Perpendicular Distance', band: 'Proficient'},
                    {title: 'Intersection Points', band: 'Proficient'},
                    {title: 'Dividing Segments', band: 'Proficient'},
                    {title: 'Area of Triangle', band: 'Advanced'},
                    {title: 'Applied Problems', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_ol_coord_circles': [
                    {title: 'Circle Equation', band: 'Foundation'},
                    {title: 'Centre & Radius', band: 'Foundation'},
                    {title: 'Point on Circle', band: 'Foundation'},
                    {title: 'General Form', band: 'Developing'},
                    {title: 'Converting Forms', band: 'Developing'},
                    {title: 'Tangent to Circle', band: 'Developing'},
                    {title: 'Line & Circle', band: 'Proficient'},
                    {title: 'External/Internal Points', band: 'Proficient'},
                    {title: 'Tangent from Point', band: 'Proficient'},
                    {title: 'Touching Circles', band: 'Advanced'},
                    {title: 'Circle Problems', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_ol_complex': [
                    {title: 'Introduction to i', band: 'Foundation'},
                    {title: 'Adding Complex', band: 'Foundation'},
                    {title: 'Subtracting Complex', band: 'Foundation'},
                    {title: 'Multiplying Complex', band: 'Developing'},
                    {title: 'Conjugates', band: 'Developing'},
                    {title: 'Dividing Complex', band: 'Developing'},
                    {title: 'Argand Diagram', band: 'Proficient'},
                    {title: 'Modulus', band: 'Proficient'},
                    {title: 'Solving Equations', band: 'Proficient'},
                    {title: 'Quadratic with Complex', band: 'Advanced'},
                    {title: 'Plotting & Interpreting', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ],
                'lc_ol_geometry': [
                    {title: 'Angle Properties', band: 'Foundation'},
                    {title: 'Triangle Properties', band: 'Foundation'},
                    {title: 'Parallel Lines', band: 'Foundation'},
                    {title: 'Constructions - Basics', band: 'Developing'},
                    {title: 'Perpendicular Bisector', band: 'Developing'},
                    {title: 'Angle Bisector', band: 'Developing'},
                    {title: 'Enlargement', band: 'Proficient'},
                    {title: 'Centre of Enlargement', band: 'Proficient'},
                    {title: 'Incentre/Circumcentre', band: 'Proficient'},
                    {title: 'Centroid Construction', band: 'Advanced'},
                    {title: 'Congruence Proofs', band: 'Advanced'},
                    {title: 'Mastery Challenge', band: 'Advanced'}
                ]
            };
            
            return topicLevels[topicKey] || null;
        }

        function getIconColor(topicKey) {
            const colors = {
                // Numeracy Strand - Green/Teal palette
                'whole_numbers': '#10b981',
                'addition_subtraction': '#14b8a6',
                'multiplication_skills': '#059669',
                'division_skills': '#0d9488',
                'basic_fractions': '#10b981',
                'basic_decimals': '#14b8a6',
                'basic_percentages': '#059669',
                'time_and_clocks': '#0d9488',
                'money_skills': '#10b981',
                'measurement': '#14b8a6',
                'data_and_charts': '#059669',
                'number_patterns': '#0d9488',
                // L1LP Strand - Purple palette
                'awareness_of_environment': '#8b5cf6',
                'pattern_and_sequence': '#7c3aed',
                'developing_number_sense': '#6d28d9',
                'shape_and_space': '#5b21b6',
                'measure_and_data': '#4c1d95',
                'time': '#9333ea',
                // L2LP Strand - Orange palette (NCCA-aligned)
                'l2_number_and_money': '#f97316',
                'l2_time_management': '#ea580c',
                'l2_measurement_location': '#dc2626',
                'l2_shape_pattern_number': '#c2410c',
                // JC Exam Topics
                'arithmetic': '#ef4444',
                'multiplication_division': '#3b82f6',
                'number_systems': '#06b6d4',
                'bodmas': '#10b981',
                'fractions': '#f59e0b',
                'decimals': '#14b8a6',
                'percentages': '#10b981',
                'ratio': '#8b5cf6',
                'sets': '#f97316',
                'probability': '#eab308',
                'descriptive_statistics': '#06b6d4',
                'patterns': '#8b5cf6',
                'functions': '#8b5cf6',
                'area_perimeter_volume': '#0d9488',
                'solving_equations': '#6366f1',
                'simultaneous_equations': '#4f46e5',
                'linear_inequalities': '#0891b2',
                'coordinate_geometry': '#0ea5e9',
                'trigonometry': '#dc2626',
                'integers': '#2563eb',
                'indices': '#7c3aed',
                'geometry': '#ec4899',
                'introductory_algebra': '#6366f1',
                'applied_arithmetic': '#059669',
                'currency': '#0d9488',
                'speed_distance_time': '#ea580c',
                'surds': '#a855f7',
                'complex_numbers_intro': '#ec4899',
                'complex_numbers_expanded': '#d946ef',
                'simplifying_expressions': '#7c3aed',
                'expanding_factorising': '#6366f1',
                // LC Higher Level Strand - Blue/Purple palette
                'lc_hl_calculus_diff': '#3b82f6',
                'lc_hl_calculus_int': '#6366f1',
                'lc_hl_algebra': '#8b5cf6',
                'lc_hl_sequences': '#a855f7',
                'lc_hl_complex': '#3b82f6',
                'lc_hl_functions': '#6366f1',
                'lc_hl_financial': '#8b5cf6',
                'lc_hl_proof': '#a855f7',
                'lc_hl_probability': '#3b82f6',
                'lc_hl_statistics': '#6366f1',
                'lc_hl_coord_geom': '#8b5cf6',
                'lc_hl_trigonometry': '#a855f7',
                'lc_hl_geometry': '#3b82f6',
                'lc_hl_mensuration': '#6366f1',
                'lc_hl_counting': '#8b5cf6',
                // LC Ordinary Level Strand - Green/Teal palette
                'lc_ol_calculus': '#10b981',
                'lc_ol_financial': '#059669',
                'lc_ol_trigonometry': '#14b8a6',
                'lc_ol_mensuration': '#0d9488',
                'lc_ol_statistics_desc': '#10b981',
                'lc_ol_probability': '#059669',
                'lc_ol_applied_measure': '#14b8a6',
                'lc_ol_sequences': '#0d9488',
                'lc_ol_algebra': '#10b981',
                'lc_ol_functions': '#059669',
                'lc_ol_statistics_inf': '#14b8a6',
                'lc_ol_coord_lines': '#0d9488',
                'lc_ol_coord_circles': '#10b981',
                'lc_ol_complex': '#059669',
                'lc_ol_geometry': '#14b8a6'
            };
            return colors[topicKey] || '#6b7280';
        }

        async function loadProgress() {
            try {
                const response = await fetch('/api/my-progress');
                const attempts = await response.json();

                const summary = document.getElementById('progressSummary');
                if (attempts.length === 0) {
                    summary.innerHTML = '<p>No quizzes completed yet. Start learning!</p>';
                } else {
                    const total = attempts.length;
                    const avgScore = (attempts.reduce((sum, a) => sum + a.percentage, 0) / total).toFixed(1);

                    summary.innerHTML = `
                        <div class="grid grid-cols-3 gap-4 text-center">
                            <div>
                                <div class="text-3xl font-bold text-purple-600">${total}</div>
                                <div class="text-sm">Quizzes Completed</div>
                            </div>
                            <div>
                                <div class="text-3xl font-bold text-green-600">${avgScore}%</div>
                                <div class="text-sm">Average Score</div>
                            </div>
                            <div>
                                <div class="text-3xl font-bold text-blue-600">${attempts[0].topic}</div>
                                <div class="text-sm">Last Topic</div>
                            </div>
                        </div>
                    `;
                }
            } catch (error) {
                console.error('Error loading progress:', error);
            }
        }

        async function loadBadgeWidget() {
            try {
                console.log('🔄 Loading badge widget...');
                
                // Fetch badge and stats data in parallel
                const [badgesResponse, statsResponse] = await Promise.all([
                    fetch('/api/student/badges'),
                    fetch('/api/student/stats')
                ]);

                console.log('📊 Badge response status:', badgesResponse.status);
                console.log('📊 Stats response status:', statsResponse.status);

                const badgesData = await badgesResponse.json();
                const statsData = await statsResponse.json();

                console.log('🎯 Badges data received:', badgesData);
                console.log('📈 Stats data received:', statsData);
                console.log('💰 Total points from API:', badgesData.total_points);
                console.log('🏆 Level from API:', badgesData.level);
                console.log('🎖️ Quizzes from API:', statsData.stats.total_quizzes);

                // Update widget values
                document.getElementById('stat-level').textContent = badgesData.level;
                document.getElementById('stat-points').textContent = badgesData.total_points;
                document.getElementById('stat-badges').textContent = badgesData.earned.length + '/' + (badgesData.earned.length + badgesData.available.length);
                document.getElementById('stat-quizzes').textContent = statsData.stats.total_quizzes;
                document.getElementById('stat-streak').textContent = statsData.stats.current_streak_days;
                document.getElementById('stat-accuracy').textContent = statsData.stats.overall_accuracy + '%';
                
                // Show next streak milestone if available
                const streakInfo = statsData.stats.streak_info;
                const streakMilestoneEl = document.getElementById('streak-next-milestone');
                if (streakInfo && streakInfo.days_until_next && streakMilestoneEl) {
                    streakMilestoneEl.textContent = `${streakInfo.days_until_next} more for +${streakInfo.next_milestone_points}pts`;
                    streakMilestoneEl.style.display = 'block';
                }
                
                // Add streak fire animation if streak > 0
                const streakBox = document.getElementById('streak-box');
                if (statsData.stats.current_streak_days >= 3 && streakBox) {
                    streakBox.style.background = 'linear-gradient(135deg, #ff6b35, #ff8c42)';
                    streakBox.style.color = 'white';
                }

                console.log('✅ Badge widget updated successfully');
                console.log('   - Points displayed:', document.getElementById('stat-points').textContent);
                console.log('   - Level displayed:', document.getElementById('stat-level').textContent);
                console.log('   - Quizzes displayed:', document.getElementById('stat-quizzes').textContent);

                // Show recent badges if any
                if (badgesData.earned.length > 0) {
                    const recentBadges = badgesData.earned.slice(-3).reverse(); // Last 3 badges
                    const recentBadgesHtml = recentBadges.map(badge => {
                        const emoji = getBadgeEmoji(badge.icon);
                        return `<span class="recent-badge-mini">${emoji} ${badge.name}</span>`;
                    }).join('');

                    document.getElementById('recent-badges').innerHTML = recentBadgesHtml;
                    document.getElementById('recent-badges-container').style.display = 'block';
                }

                // Show the widget
                document.getElementById('badge-widget').style.display = 'block';

            } catch (error) {
                console.error('❌ Error loading badge widget:', error);
                console.error('Error details:', error.message, error.stack);
                // Hide widget if there's an error
                document.getElementById('badge-widget').style.display = 'none';
            }
        }

        function getBadgeEmoji(iconClass) {
            const iconMap = {
                'fa-star': '⭐', 'fa-book': '📚', 'fa-graduation-cap': '🎓',
                'fa-heart': '❤️', 'fa-trophy': '🏆', 'fa-bullseye': '🎯',
                'fa-crown': '👑', 'fa-medal': '🥈', 'fa-gem': '💎',
                'fa-fire': '🔥', 'fa-bolt': '⚡', 'fa-rocket': '🚀',
                'fa-certificate': '📜', 'fa-brain': '🧠', 'fa-infinity': '♾️'
            };
            return iconMap[iconClass] || '🏅';
        }

        // ========================================
        // COLLAPSIBLE STRAND FUNCTIONS
        // ========================================
        
        function toggleStrand(strandId) {
            const strand = document.getElementById(strandId);
            if (strand) {
                strand.classList.toggle('expanded');
                saveStrandStates();
            }
        }

        function saveStrandStates() {
            const states = {};
            document.querySelectorAll('.learning-path-card[id^="strand-"]').forEach(card => {
                states[card.id] = card.classList.contains('expanded');
            });
            localStorage.setItem('agentmath_strand_states', JSON.stringify(states));
        }

        function loadStrandStates() {
            const saved = localStorage.getItem('agentmath_strand_states');
            if (saved) {
                try {
                    const states = JSON.parse(saved);
                    Object.entries(states).forEach(([id, expanded]) => {
                        const card = document.getElementById(id);
                        if (card && expanded) {
                            card.classList.add('expanded');
                        }
                    });
                } catch (e) {
                    console.warn('Could not load strand states:', e);
                }
            }
        }

        // ========================================

        function selectTopic(topic, title) {
            currentTopic = topic;
            document.getElementById('selectedTopicTitle').textContent = title;

            // Generate difficulty/section buttons based on topic
            const container = document.getElementById('difficultyButtonsContainer');
            container.innerHTML = '';

            // All topics now use standard 3 difficulty levels
            const difficulties = [
                {level: 'beginner', title: 'Beginner', icon: 'fa-seedling', color: 'bg-green-500', desc: 'Start with the basics'},
                {level: 'intermediate', title: 'Intermediate', icon: 'fa-chart-line', color: 'bg-yellow-500', desc: 'Challenge yourself more'},
                {level: 'advanced', title: 'Advanced', icon: 'fa-trophy', color: 'bg-red-500', desc: 'Master the topic'}
            ];

            // Use 3-column grid for standard difficulties
            container.className = 'grid md:grid-cols-3 gap-6';

            difficulties.forEach(diff => {
                const button = document.createElement('button');
                button.onclick = () => startQuiz(diff.level);

                // Check if this difficulty is mastered (>80%)
                const difficultyData = masteryData[topic]?.difficulties?.[diff.level];
                const isMastered = difficultyData?.mastered || false;
                const bestScore = difficultyData?.best_score || 0;

                // Add mastered class for dimmed styling
                button.className = `difficulty-button ${diff.color} hover:opacity-90 text-white rounded-2xl p-8 shadow-lg hover:shadow-2xl transform hover:scale-105 transition-all ${isMastered ? 'mastered' : ''}`;

                // Add trophy badge if mastered
                const masteryBadge = isMastered ? `
                    <div class="difficulty-mastery" title="Mastered with ${bestScore}%!">
                        <div class="trophy">🏆</div>
                        <div class="score">${bestScore}%</div>
                    </div>
                ` : '';

                // Show best score if attempted but not mastered
                const scoreDisplay = (bestScore > 0 && !isMastered) ?
                    `<div class="best-score-display">Best: ${bestScore}%</div>` : '';

                button.innerHTML = `
                    ${masteryBadge}
                    <i class="fas ${diff.icon} text-6xl mb-4"></i>
                    <h3 class="text-2xl font-bold mb-2">${diff.title}</h3>
                    <p class="text-white text-opacity-90">${diff.desc}</p>
                    <p class="mt-2 text-sm">25 questions</p>
                    ${scoreDisplay}
                `;
                container.appendChild(button);
            });

            document.getElementById('topicScreen').classList.add('hidden');
            document.getElementById('difficultyScreen').classList.remove('hidden');
        }

        // ===== ADAPTIVE QUIZ SYSTEM (BETA) =====
        // State tracking for adaptive quizzes
        let adaptiveState = {
            active: false,
            topic: null,
            topicTitle: null,
            currentLevel: 1,
            currentPoints: 0,
            questionStartTime: null,
            questionsAtLevel: 0,
            shownQuestionIds: [],  // Track shown questions to avoid repeats
            // Gamification fields
            sessionStreak: 0,           // Consecutive correct in session
            sessionPointsEarned: 0,     // Total points earned this session
            questionsAnswered: 0,       // Total questions this session
            correctAnswers: 0,          // Correct answers this session
            whoAmIEnabled: false,       // Whether Who Am I is active
            whoAmIAttemptId: null,      // Pseudo-attempt ID for Who Am I
            // Clock Challenge fields (Rev 3.0)
            clockMode: false,              // Is clock challenge active?
            clockSessionId: null,          // Current session ID
            clockTimeRemaining: 0,         // Seconds remaining
            clockTimeAllowed: 0,           // Total time allowed
            clockWrongPenalty: 0,          // Seconds penalty per wrong answer
            clockPenaltiesApplied: 0,      // Total penalties this session
            clockQuestionsAnswered: 0,     // Questions answered in clock mode
            clockQuestionsCorrect: 0,      // Correct answers in clock mode
            clockTimerInterval: null,      // Timer interval reference
            clockLevelStartPoints: 0,      // Points at start of clock level
            // Lifelines & Emergency Buy (Rev 3.0.9)
            clockLifelines: {              // Active lifelines for current challenge
                timeBoost: false,
                timeShield: false,
                secondChance: false
            },
            clockSecondChanceUsed: false,  // Has second chance been consumed?
            clockEmergencyBuyUsed: false,  // Has emergency buy been used?
            clockEmergencyBuyShown: false  // Has emergency modal been shown?
        };
        
        // Point values for adaptive quiz
        const ADAPTIVE_POINTS = {
            beginner: { base: 5, fast: 3 },      // Levels 1-3
            intermediate: { base: 8, fast: 4 },  // Levels 4-6
            advanced: { base: 12, fast: 6 },     // Levels 7-9
            mastery: { base: 15, fast: 8 }       // Level 10
        };
        
        // Progression thresholds
        const ADAPTIVE_CONFIG = {
            pointsToLevelUp: {
                beginner: 6,      // Levels 1-3 (doubled from 3)
                intermediate: 8,  // Levels 4-6 (doubled from 4)
                advanced: 10      // Levels 7-9 (doubled from 5)
            },
            fastTimeThreshold: {
                beginner: 15,     // Levels 1-3: under 15s = fast
                intermediate: 20, // Levels 4-6: under 20s = fast
                advanced: 25,     // Levels 7-9: under 25s = fast
                mastery: 30       // Level 10: under 30s = fast
            }
        };
        
        function getAdaptiveBand(level) {
            if (level <= 3) return 'beginner';
            if (level <= 6) return 'intermediate';
            if (level <= 9) return 'advanced';
            return 'mastery';
        }
        
        function getPointsRequired(level) {
            const band = getAdaptiveBand(level);
            return ADAPTIVE_CONFIG.pointsToLevelUp[band] || 5;
        }
        
        function getFastThreshold(level) {
            const band = getAdaptiveBand(level);
            return ADAPTIVE_CONFIG.fastTimeThreshold[band] || 25;
        }
        

        // =====================================================
        // CLOCK CHALLENGE - Now loaded from external file
        // See: /static/js/clock-challenge.js
        // =====================================================

        
        async function startAdaptiveQuizBeta(topicKey, topicTitle) {
            try {
                console.log('🧪 Starting Adaptive Quiz BETA:', topicKey, topicTitle);
                
                // FLOW SUMS: Special interactive mode - launch Flow Sums game instead
                if (topicKey === 'flow_sums') {
                    console.log('🌊 Launching Flow Sums interactive mode');
                    startFlowSums();  // Fetches saved level
                    return;
                }
                
                // NUMBER PYRAMIDS: Special interactive mode
                if (topicKey === 'number_pyramids') {
                    console.log('🔺 Launching Number Pyramids interactive mode');
                    startPyramid();  // Fetches saved level
                    return;
                }
                
                // CODE BREAKER: Special interactive mode
                if (topicKey === 'code_breaker') {
                    console.log('🔐 Launching Code Breaker interactive mode');
                    startCodeBreaker();  // Fetches saved level
                    return;
                }
                
                // MASTERING COUNTING: Special interactive mode
                if (topicKey === 'mastering_counting') {
                    console.log('🔢 Launching Mastering Counting interactive mode');
                    startCounting();  // Fetches saved level
                    return;
                }
                
                // WORDS TO NUMBERS: Special interactive mode
                if (topicKey === 'words_to_numbers') {
                    console.log('🔤 Launching Words to Numbers interactive mode');
                    startWords();  // Fetches saved level
                    return;
                }
                
                // ORDERING & NUMBER LINES: Special interactive mode
                if (topicKey === 'ordering_magnitude') {
                    console.log('📏 Launching Ordering & Number Lines interactive mode');
                    startOrdering();  // Fetches saved level
                    return;
                }
                
                // NUMBER BONDS POP: Special interactive mode
                if (topicKey === 'number_bonds') {
                    console.log('🫧 Launching Number Bonds Pop interactive mode');
                    startBonds();  // Fetches saved level
                    return;
                }
                
                // PLACE VALUE BUILDER: Special interactive mode
                if (topicKey === 'place_value') {
                    console.log('🏗️ Launching Place Value Builder interactive mode');
                    startPlaceValue();  // Fetches saved level
                    return;
                }
                
                // DOUBLE TROUBLE: Special interactive mode
                if (topicKey === 'double_trouble') {
                    console.log('⚡ Launching Double Trouble interactive mode');
                    startDouble();  // Fetches saved level
                    return;
                }
                
                // ADDITION BLITZ: Special interactive mode
                if (topicKey === 'addition_blitz') {
                    console.log('➕ Launching Addition Blitz interactive mode');
                    startAdditionBlitz();  // Fetches saved level
                    return;
                }
                
                // TIMES TABLES BLITZ: Special interactive mode
                if (topicKey === 'times_tables_blitz') {
                    console.log('✖️ Launching Times Tables Blitz interactive mode');
                    startTimesTablesBlitz();  // Fetches saved level
                    return;
                }
                
                // RESET DINO BONUS: Hide any lingering Dino bonus UI from previous topic
                const dinoBonusUnlock = document.getElementById('adaptive-dino-bonus-unlock');
                if (dinoBonusUnlock) {
                    dinoBonusUnlock.style.display = 'none';
                }
                showDinoBonusNotification(false);
                
                // Also reset legacy quiz Dino bonus if present
                const legacyDinoBonusUnlock = document.getElementById('dino-bonus-unlock');
                if (legacyDinoBonusUnlock) {
                    legacyDinoBonusUnlock.style.display = 'none';
                }
                
                // Load saved progress from server
                let savedLevel = 1;
                let savedPoints = 0;
                
                try {
                    const response = await fetch(`/api/adaptive/progress/${topicKey}`);
                    if (response.ok) {
                        const progress = await response.json();
                        savedLevel = progress.current_level || 1;
                        savedPoints = progress.current_points || 0;
                        console.log('📊 Loaded saved progress:', progress);
                    }
                } catch (error) {
                    console.log('Could not load progress, starting fresh:', error);
                }
                
                // Initialize adaptive state
                adaptiveState = {
                    active: true,
                    topic: topicKey,
                    topicTitle: topicTitle,
                    currentLevel: savedLevel,
                    currentPoints: savedPoints,
                    questionStartTime: null,
                    questionsAtLevel: 0,
                    shownQuestionIds: [],  // Reset shown questions for new session
                    // Gamification - reset for new session
                    sessionStreak: 0,
                    sessionPointsEarned: 0,
                    questionsAnswered: 0,
                    correctAnswers: 0,
                    whoAmIEnabled: false,
                    whoAmIAttemptId: null,
                    // Clock Challenge - reset for new session (Rev 3.0)
                    clockMode: false,
                    clockSessionId: null,
                    clockTimeRemaining: 0,
                    clockTimeAllowed: 0,
                    clockWrongPenalty: 0,
                    clockPenaltiesApplied: 0,
                    clockQuestionsAnswered: 0,
                    clockQuestionsCorrect: 0,
                    clockTimerInterval: null,
                    clockLevelStartPoints: 0
                };
                
                // Set current topic for compatibility
                currentTopic = topicKey;
                currentDifficulty = 'adaptive';
                
                // Show adaptive quiz screen FIRST (creates the container)
                showAdaptiveQuizScreen();
                
                // Initialize Who Am I using SAME approach as legacy quiz
                // Use the GLOBAL whoAmIEnabled and currentQuizAttemptId variables
                try {
                    if (typeof initializeWhoAmI === 'function') {
                        console.log('🎭 ADAPTIVE: Using legacy Who Am I initialization...');
                        
                        // Create a REAL quiz attempt (same as legacy quiz)
                        const attemptResponse = await fetch('/api/create-quiz-attempt', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({
                                topic: topicKey,
                                difficulty: 'adaptive'
                            })
                        });
                        const attemptData = await attemptResponse.json();
                        
                        if (attemptData.quiz_attempt_id) {
                            // USE GLOBAL VARIABLES (same as legacy quiz)
                            currentQuizAttemptId = attemptData.quiz_attempt_id;
                            whoAmIEnabled = true;
                            adaptiveState.whoAmIAttemptId = attemptData.quiz_attempt_id;
                            adaptiveState.whoAmIEnabled = true;
                            
                            console.log('✅ Real quiz attempt created:', currentQuizAttemptId);
                            
                            // Initialize Who Am I with the adaptive container
                            await initializeWhoAmI(topicKey, 'adaptive', currentQuizAttemptId, 'adaptive-who-am-i-container');
                            
                            // Check if it actually initialized
                            if (typeof whoAmIState !== 'undefined' && whoAmIState.imageUrl) {
                                console.log('🎭 Who Am I ENABLED - imageUrl:', whoAmIState.imageUrl);
                            } else {
                                whoAmIEnabled = false;
                                adaptiveState.whoAmIEnabled = false;
                                console.log('ℹ️ Who Am I not available for this topic');
                            }
                        } else {
                            console.log('⚠️ Could not create quiz attempt for Who Am I');
                        }
                    }
                } catch (whoAmIError) {
                    console.log('Who Am I not available:', whoAmIError);
                    whoAmIEnabled = false;
                    adaptiveState.whoAmIEnabled = false;
                }
            } catch (err) {
                alert('Error starting adaptive quiz: ' + err.message);
                console.error('Fatal error:', err);
            }
        }
        
        function showAdaptiveQuizScreen() {
            // Hide other screens
            document.getElementById('topicScreen').classList.add('hidden');
            document.getElementById('difficultyScreen').classList.add('hidden');
            
            // Check if BETA adaptive screen exists, create if not
            let adaptiveScreen = document.getElementById('adaptiveQuizScreenBeta');
            if (!adaptiveScreen) {
                createAdaptiveQuizScreen();
                adaptiveScreen = document.getElementById('adaptiveQuizScreenBeta');
            }
            
            // Update the screen with current state
            updateAdaptiveProgress();
            
            // Show the screen
            adaptiveScreen.classList.remove('hidden');
            
            // Load first question
            loadAdaptiveQuestion();
            
            // Check if should auto-show help for Level 1 (first time)
            checkAutoShowHelp();
        }
        
        function createAdaptiveQuizScreen() {
            const screen = document.createElement('div');
            screen.id = 'adaptiveQuizScreenBeta';
            screen.className = 'screen hidden';
            screen.innerHTML = `
                <div class="adaptive-quiz-container" style="max-width: 1200px; margin: 0 auto; padding: 20px;">
                    <!-- Header with level and progress -->
                    <div class="adaptive-header" style="background: linear-gradient(135deg, #8b5cf6, #a78bfa); border-radius: 16px; padding: 20px; margin-bottom: 20px; color: white;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                            <button onclick="exitAdaptiveQuizBeta()" style="background: rgba(255,255,255,0.2); border: none; color: white; padding: 8px 16px; border-radius: 8px; cursor: pointer; font-size: 0.9rem;">
                                <i class="fas fa-arrow-left"></i> Exit
                            </button>
                            <div style="display: flex; align-items: center; gap: 8px;">
                                <span style="font-size: 1.1rem; font-weight: 600;" id="adaptiveTopicTitle"></span>
                                <span style="background: rgba(255,255,255,0.2); padding: 4px 10px; border-radius: 6px; font-size: 0.8rem;">BETA</span>
                            </div>
                            <div style="display: flex; align-items: center; gap: 15px;">
                                <!-- Help button - prominent -->
                                <button onclick="showAdaptiveHelp()" id="adaptiveHelpBtn" style="background: linear-gradient(135deg, #fbbf24, #f59e0b); border: none; color: #1f2937; padding: 8px 16px; border-radius: 20px; cursor: pointer; font-size: 0.95rem; font-weight: 700; transition: all 0.2s; display: flex; align-items: center; gap: 6px; box-shadow: 0 2px 8px rgba(251, 191, 36, 0.4);" title="Level Help">
                                    <i class="fas fa-question-circle"></i> HELP
                                </button>
                                <!-- Watch Tutorial button -->
                                <button onclick="openTopicTutorial()" id="adaptiveTutorialBtn" style="background: linear-gradient(135deg, #ef4444, #dc2626); border: none; color: white; padding: 8px 16px; border-radius: 20px; cursor: pointer; font-size: 0.95rem; font-weight: 700; transition: all 0.2s; display: flex; align-items: center; gap: 6px; box-shadow: 0 2px 8px rgba(239, 68, 68, 0.4);" title="Watch Video Tutorial">
                                    <i class="fab fa-youtube"></i> TUTORIAL
                                </button>
                                <!-- Points earned this session -->
                                <div id="adaptivePointsDisplay" style="display: flex; align-items: center; gap: 4px; background: rgba(255,255,255,0.15); padding: 6px 12px; border-radius: 8px;">
                                    <span>💰</span>
                                    <span id="adaptiveSessionPoints">0</span>
                                </div>
                                <!-- Streak display -->
                                <div id="adaptiveStreakDisplay" class="hot-streak-display streak-cold" style="display: flex; align-items: center; gap: 4px; padding: 6px 12px; border-radius: 8px;">
                                    <span class="streak-flame">🔥</span>
                                    <span id="adaptiveStreakCount">0</span>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Level indicator -->
                        <div style="text-align: center; margin-bottom: 15px;">
                            <div style="font-size: 2.5rem; font-weight: 700;" id="adaptiveLevelNumber">1</div>
                            <div style="font-size: 0.9rem; opacity: 0.9;">Level <span id="adaptiveLevelBand">Beginner</span></div>
                        </div>
                        
                        <!-- Progress bar -->
                        <div style="background: rgba(255,255,255,0.2); border-radius: 10px; height: 20px; overflow: hidden; position: relative;">
                            <div id="adaptiveProgressBar" style="background: linear-gradient(90deg, #fbbf24, #f59e0b); height: 100%; width: 0%; transition: width 0.5s ease; border-radius: 10px;"></div>
                            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 0.75rem; font-weight: 600;">
                                <span id="adaptiveProgressText">0/3 to Level 2</span>
                            </div>
                        </div>
                        
                        <!-- Speed bonus hint -->
                        <div style="text-align: center; margin-top: 10px; font-size: 0.8rem; opacity: 0.8;">
                            <i class="fas fa-bolt"></i> Answer quickly for bonus progress!
                        </div>
                    </div>
                    
                    <!-- Main content area: Question + Who Am I side by side -->
                    <div class="adaptive-main-content" style="display: flex; gap: 20px; flex-wrap: wrap;">
                        
                        <!-- Who Am I Container (LEFT on desktop) -->
                        <div id="adaptive-who-am-i-container" class="who-am-i-container" style="display: none; flex: 0 0 320px; max-width: 320px; order: 1;">
                        </div>
                        
                        <!-- Question area (expands to fill space) -->
                        <div style="flex: 1; min-width: 300px; order: 2;">
                            <div class="adaptive-question-area" style="background: white; border-radius: 16px; padding: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); position: relative;">
                                
                                <!-- TOP BAR: Level Progress Pie + Who Am I Indicator + Next Button -->
                                <div id="adaptiveQuestionTopBar" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; padding-bottom: 15px; border-bottom: 1px solid #e5e7eb;">
                                    
                                    <!-- LEFT: Level Progress Pie Chart -->
                                    <div style="display: flex; align-items: center; gap: 10px;">
                                        <div id="levelProgressPie" style="width: 50px; height: 50px; position: relative;">
                                            <svg viewBox="0 0 36 36" style="transform: rotate(-90deg);">
                                                <!-- Background circle -->
                                                <circle cx="18" cy="18" r="15.9" fill="none" stroke="#e5e7eb" stroke-width="3"/>
                                                <!-- Progress circle (12 segments for 12 levels) -->
                                                <circle id="levelProgressCircle" cx="18" cy="18" r="15.9" fill="none" stroke="url(#levelGradient)" stroke-width="3" stroke-dasharray="0 100" stroke-linecap="round"/>
                                                <defs>
                                                    <linearGradient id="levelGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                                                        <stop offset="0%" style="stop-color:#8b5cf6"/>
                                                        <stop offset="100%" style="stop-color:#06b6d4"/>
                                                    </linearGradient>
                                                </defs>
                                            </svg>
                                            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 0.7rem; font-weight: 700; color: #8b5cf6;">
                                                <span id="levelPieText">1</span>/12
                                            </div>
                                        </div>
                                        <div style="font-size: 0.75rem; color: #6b7280;">
                                            <div style="font-weight: 600; color: #374151;">Level Progress</div>
                                            <div id="levelPieSubtext">Just started</div>
                                        </div>
                                    </div>
                                    
                                    <!-- CENTER: Dino Bonus Notification (hidden until unlocked) -->
                                    <div id="dinoBonusNotification" style="display: none; background: linear-gradient(135deg, #fef3c7, #fde68a); padding: 8px 16px; border-radius: 20px; animation: pulse-online 2s infinite; cursor: pointer; box-shadow: 0 2px 8px rgba(251,191,36,0.4);" onclick="document.getElementById('adaptive-dino-bonus-unlock').scrollIntoView({behavior: 'smooth'});">
                                        <span style="font-size: 0.85rem; color: #92400e; font-weight: 600;">
                                            🦕 Dino Bonus Ready! ↓
                                        </span>
                                    </div>
                                    
                                    <!-- RIGHT: Next Question Button (hidden until answered) -->
                                    <button id="topNextQuestionBtn" onclick="continueAdaptiveQuizBeta()" style="display: none; padding: 10px 20px; background: linear-gradient(135deg, #8b5cf6, #7c3aed); color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: 600; font-size: 0.9rem; box-shadow: 0 2px 8px rgba(139,92,246,0.3); transition: all 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                                        Next <i class="fas fa-arrow-right"></i>
                                    </button>
                                </div>
                                
                                <div id="adaptiveQuestionContent">
                                    <div style="text-align: center; padding: 40px;">
                                        <i class="fas fa-spinner fa-spin" style="font-size: 2rem; color: #8b5cf6;"></i>
                                        <p style="margin-top: 15px; color: #6b7280;">Loading question...</p>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Feedback area (hidden initially) -->
                            <div id="adaptiveFeedbackBeta" class="hidden" style="margin-top: 20px; border-radius: 16px; padding: 20px; text-align: center;">
                            </div>
                        </div>
                    </div>
                    
                    <!-- Dino Bonus Unlock Card (for adaptive quiz) -->
                    <div id="adaptive-dino-bonus-unlock" class="bonus-question-unlock" style="display: none; margin-top: 20px; background: linear-gradient(135deg, #fef3c7, #fde68a); border-radius: 16px; padding: 20px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                        <div style="font-size: 3rem; margin-bottom: 10px;">🦕</div>
                        <h3 style="color: #92400e; margin-bottom: 10px;">Dino Bonus Unlocked!</h3>
                        <p style="color: #a16207; margin-bottom: 15px;">5 correct in a row! Try a bonus question for extra points!</p>
                        <div style="display: flex; justify-content: center; gap: 10px;">
                            <button onclick="startBonusQuestion(); document.getElementById('adaptive-dino-bonus-unlock').style.display='none'; showDinoBonusNotification(false);" style="padding: 10px 20px; background: #22c55e; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: 600;">
                                <i class="fas fa-play"></i> Play Bonus
                            </button>
                            <button onclick="document.getElementById('adaptive-dino-bonus-unlock').style.display='none'; showDinoBonusNotification(false);" style="padding: 10px 20px; background: #9ca3af; color: white; border: none; border-radius: 8px; cursor: pointer;">
                                Skip
                            </button>
                        </div>
                    </div>
                    
                    <!-- Reset option -->
                    <div style="text-align: center; margin-top: 30px;">
                        <button onclick="confirmAdaptiveResetBeta()" style="background: none; border: none; color: #9ca3af; font-size: 0.85rem; cursor: pointer; text-decoration: underline;">
                            Reset progress and start from Level 1
                        </button>
                    </div>
                </div>
            `;
            document.body.appendChild(screen);
            
            // Create help modal if it doesn't exist
            createAdaptiveHelpModal();
        }
        
        // Create the adaptive help modal
        function createAdaptiveHelpModal() {
            if (document.getElementById('adaptiveHelpModal')) return;
            
            const modal = document.createElement('div');
            modal.id = 'adaptiveHelpModal';
            modal.className = 'adaptive-help-modal';
            modal.innerHTML = `
                <div class="adaptive-help-content">
                    <div class="adaptive-help-header">
                        <h2><i class="fas fa-graduation-cap"></i> Level <span id="helpLevelNumber">1</span> Help <span class="level-badge" id="helpLevelBand">Foundation</span></h2>
                        <p id="helpLevelTitle" style="opacity: 0.9; margin: 0;">Visual Fractions & Recognition</p>
                        <button class="adaptive-help-close" onclick="hideAdaptiveHelp()">
                            <i class="fas fa-times"></i>
                        </button>
                    </div>
                    <div class="adaptive-help-body" id="helpBodyContent">
                        <!-- Content loaded dynamically -->
                    </div>
                </div>
            `;
            modal.onclick = function(e) {
                if (e.target === modal) hideAdaptiveHelp();
            };
            document.body.appendChild(modal);
        }
        
        // Help content for all 12 levels
        const adaptiveHelpContent = {
            1: {
                title: "Visual Fractions & Recognition",
                band: "Foundation",
                description: "At this level, you'll learn to recognise fractions from pictures and diagrams. A fraction tells us how many parts we have out of the total number of equal parts.",
                keyPoints: [
                    "The <strong>numerator</strong> (top number) = how many parts we have",
                    "The <strong>denominator</strong> (bottom number) = total equal parts",
                    "All parts must be <strong>equal size</strong>"
                ],
                examples: [
                    {
                        question: "A pizza is cut into 8 equal slices. 3 slices are eaten. What fraction was eaten?",
                        visual: '<svg viewBox="0 0 100 100" width="120"><circle cx="50" cy="50" r="45" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/><path d="M50,50 L50,5 A45,45 0 0,1 88.2,28.5 Z" fill="#22c55e"/><path d="M50,50 L88.2,28.5 A45,45 0 0,1 88.2,71.5 Z" fill="#22c55e"/><path d="M50,50 L88.2,71.5 A45,45 0 0,1 50,95 Z" fill="#22c55e"/><line x1="50" y1="5" x2="50" y2="95" stroke="#d97706" stroke-width="1"/><line x1="5" y1="50" x2="95" y2="50" stroke="#d97706" stroke-width="1"/><line x1="18.2" y1="18.2" x2="81.8" y2="81.8" stroke="#d97706" stroke-width="1"/><line x1="81.8" y1="18.2" x2="18.2" y2="81.8" stroke="#d97706" stroke-width="1"/></svg>',
                        steps: [
                            "Count the total slices: <strong>8 equal parts</strong>",
                            "Count eaten slices (green): <strong>3 parts</strong>",
                            "Write as a fraction: parts eaten ÷ total parts"
                        ],
                        answer: "3/8 of the pizza was eaten"
                    }
                ],
                tip: "Always count ALL the parts first (denominator), then count the shaded or selected parts (numerator)."
            },
            2: {
                title: "Equivalent Fractions",
                band: "Foundation",
                description: "Equivalent fractions look different but represent the same amount. You can find them by multiplying or dividing both the numerator and denominator by the same number.",
                keyPoints: [
                    "Multiply top AND bottom by the same number",
                    "Divide top AND bottom by the same number",
                    "The value stays the same, only the 'pieces' change"
                ],
                examples: [
                    {
                        question: "Find a fraction equivalent to 1/2 with denominator 8.",
                        visual: '<div style="display: flex; gap: 20px; align-items: center; justify-content: center;"><div><svg viewBox="0 0 100 30" width="80"><rect x="5" y="5" width="90" height="20" fill="#e5e7eb" stroke="#6b7280"/><rect x="5" y="5" width="45" height="20" fill="#8b5cf6"/><line x1="50" y1="5" x2="50" y2="25" stroke="#6b7280" stroke-width="2"/></svg><div style="font-size:12px;margin-top:5px;">1/2</div></div><div style="font-size:24px;">=</div><div><svg viewBox="0 0 100 30" width="80"><rect x="5" y="5" width="90" height="20" fill="#e5e7eb" stroke="#6b7280"/><rect x="5" y="5" width="45" height="20" fill="#8b5cf6"/><line x1="16.25" y1="5" x2="16.25" y2="25" stroke="#6b7280"/><line x1="27.5" y1="5" x2="27.5" y2="25" stroke="#6b7280"/><line x1="38.75" y1="5" x2="38.75" y2="25" stroke="#6b7280"/><line x1="50" y1="5" x2="50" y2="25" stroke="#6b7280"/><line x1="61.25" y1="5" x2="61.25" y2="25" stroke="#6b7280"/><line x1="72.5" y1="5" x2="72.5" y2="25" stroke="#6b7280"/><line x1="83.75" y1="5" x2="83.75" y2="25" stroke="#6b7280"/></svg><div style="font-size:12px;margin-top:5px;">4/8</div></div></div>',
                        steps: [
                            "We need denominator 8, currently have 2",
                            "What × 2 = 8? Answer: <strong>4</strong>",
                            "Multiply top by 4 too: 1 × 4 = <strong>4</strong>"
                        ],
                        answer: "1/2 = 4/8"
                    }
                ],
                tip: "Whatever you do to the bottom, you MUST do to the top! Think of it as fair scaling."
            },
            3: {
                title: "Simplifying Fractions",
                band: "Foundation",
                description: "Simplifying means making the numbers as small as possible while keeping the same value. Divide both numbers by their highest common factor (HCF).",
                keyPoints: [
                    "Find a number that divides BOTH top and bottom evenly",
                    "Keep dividing until you can't anymore",
                    "The fraction is 'fully simplified' when HCF is 1"
                ],
                examples: [
                    {
                        question: "Write 15 minutes as a fraction of one hour in simplest form.",
                        visual: '<svg viewBox="0 0 100 100" width="100"><circle cx="50" cy="50" r="45" fill="#f3f4f6" stroke="#6b7280" stroke-width="2"/><path d="M50,50 L50,5 A45,45 0 0,1 95,50 Z" fill="#22c55e" opacity="0.7"/><circle cx="50" cy="50" r="3" fill="#1f2937"/><text x="50" y="15" text-anchor="middle" font-size="8">12</text><text x="85" y="53" text-anchor="middle" font-size="8">3</text><text x="50" y="92" text-anchor="middle" font-size="8">6</text><text x="15" y="53" text-anchor="middle" font-size="8">9</text></svg>',
                        steps: [
                            "15 minutes out of 60 minutes = <strong>15/60</strong>",
                            "Find HCF of 15 and 60: both divisible by <strong>15</strong>",
                            "Divide both: 15 ÷ 15 = 1, 60 ÷ 15 = 4"
                        ],
                        answer: "15/60 = 1/4 of an hour"
                    }
                ],
                tip: "SEC Exam Style! Time questions often ask for 'fraction of an hour'. Remember: 1 hour = 60 minutes."
            },
            4: {
                title: "Adding & Subtracting (Same Denominator)",
                band: "Foundation",
                description: "When fractions have the SAME denominator, just add or subtract the numerators. The denominator stays the same!",
                keyPoints: [
                    "Same denominator = same size pieces",
                    "Add/subtract the numerators only",
                    "Keep the denominator the same",
                    "Simplify your answer if possible"
                ],
                examples: [
                    {
                        question: "Emma eats 2/8 of a cake. Tom eats 3/8. What fraction did they eat altogether?",
                        visual: '<svg viewBox="0 0 100 40" width="180"><rect x="5" y="10" width="90" height="20" fill="#e5e7eb" stroke="#6b7280"/><rect x="5" y="10" width="22.5" height="20" fill="#ec4899"/><rect x="27.5" y="10" width="33.75" height="20" fill="#8b5cf6"/><line x1="16.25" y1="10" x2="16.25" y2="30" stroke="#6b7280"/><line x1="27.5" y1="10" x2="27.5" y2="30" stroke="#6b7280"/><line x1="38.75" y1="10" x2="38.75" y2="30" stroke="#6b7280"/><line x1="50" y1="10" x2="50" y2="30" stroke="#6b7280"/><line x1="61.25" y1="10" x2="61.25" y2="30" stroke="#6b7280"/><line x1="72.5" y1="10" x2="72.5" y2="30" stroke="#6b7280"/><line x1="83.75" y1="10" x2="83.75" y2="30" stroke="#6b7280"/><text x="16" y="7" font-size="6" fill="#ec4899">Emma</text><text x="40" y="7" font-size="6" fill="#8b5cf6">Tom</text></svg>',
                        steps: [
                            "Both fractions have denominator 8 ✓",
                            "Add numerators: 2 + 3 = <strong>5</strong>",
                            "Keep denominator: <strong>8</strong>"
                        ],
                        answer: "2/8 + 3/8 = 5/8 of the cake"
                    }
                ],
                tip: "Think of it like adding apples: 2 eighths + 3 eighths = 5 eighths. Same type of 'piece'!"
            },
            5: {
                title: "Adding & Subtracting (Different Denominators - Simple)",
                band: "Ordinary",
                description: "When denominators are different, find a common denominator first. At this level, one denominator is usually a multiple of the other (like 2 and 4, or 3 and 6).",
                keyPoints: [
                    "Find the Lowest Common Denominator (LCD)",
                    "Convert each fraction to equivalent fractions with the LCD",
                    "Then add or subtract the numerators",
                    "Simplify your final answer"
                ],
                examples: [
                    {
                        question: "Write as a single fraction in simplest form: 1/2 + 1/4",
                        visual: null,
                        steps: [
                            "LCD of 2 and 4 is <strong>4</strong> (since 4 is a multiple of 2)",
                            "Convert 1/2: multiply by 2/2 = <strong>2/4</strong>",
                            "1/4 stays as <strong>1/4</strong>",
                            "Add: 2/4 + 1/4 = <strong>3/4</strong>"
                        ],
                        answer: "1/2 + 1/4 = 3/4"
                    }
                ],
                tip: "SEC Exam wording! Questions often say 'Write as a single fraction in its simplest form'. This means find LCD, add/subtract, then simplify."
            },
            6: {
                title: "Adding & Subtracting (Different Denominators - Complex)",
                band: "Ordinary",
                description: "Now the denominators share no common factors (co-prime). You'll need to multiply denominators to find the LCD, like 2/3 + 1/5.",
                keyPoints: [
                    "LCD = multiply the denominators when they share no factors",
                    "For 2/3 + 1/5: LCD = 3 × 5 = 15",
                    "Convert BOTH fractions to the new denominator",
                    "Always simplify your final answer"
                ],
                examples: [
                    {
                        question: "Write as a single fraction: 2/3 + 1/4",
                        visual: null,
                        steps: [
                            "LCD of 3 and 4 is <strong>12</strong> (3 × 4)",
                            "Convert 2/3: × 4/4 = <strong>8/12</strong>",
                            "Convert 1/4: × 3/3 = <strong>3/12</strong>",
                            "Add: 8/12 + 3/12 = <strong>11/12</strong>"
                        ],
                        answer: "2/3 + 1/4 = 11/12"
                    }
                ],
                tip: "Check if your answer can be simplified! 11/12 cannot be simplified (11 is prime), but always check."
            },
            7: {
                title: "Multiplying Fractions",
                band: "Ordinary",
                description: "Multiplying fractions is straightforward: multiply the numerators together, multiply the denominators together. 'Of' means multiply!",
                keyPoints: [
                    "Multiply numerators: top × top",
                    "Multiply denominators: bottom × bottom",
                    "'Of' in word problems means <strong>multiply</strong>",
                    "Simplify before or after multiplying"
                ],
                examples: [
                    {
                        question: "Half a pizza remains. Sarah eats 2/3 of what's left. What fraction of the whole pizza did Sarah eat?",
                        visual: null,
                        steps: [
                            "'2/3 <strong>of</strong> 1/2' means 2/3 × 1/2",
                            "Multiply tops: 2 × 1 = <strong>2</strong>",
                            "Multiply bottoms: 3 × 2 = <strong>6</strong>",
                            "Simplify 2/6 = <strong>1/3</strong>"
                        ],
                        answer: "2/3 × 1/2 = 2/6 = 1/3 of the whole pizza"
                    }
                ],
                tip: "Cross-cancel before multiplying to make numbers smaller! In 2/3 × 3/4, the 3s cancel to give 2/1 × 1/4 = 2/4 = 1/2"
            },
            8: {
                title: "Dividing Fractions",
                band: "Ordinary",
                description: "To divide fractions, flip the second fraction (reciprocal) and multiply. 'How many X fit in Y' is division!",
                keyPoints: [
                    "Keep the first fraction the same",
                    "Flip the second fraction (reciprocal)",
                    "Change ÷ to ×",
                    "Then multiply as normal"
                ],
                examples: [
                    {
                        question: "A rope is 3/4 metre long. It's cut into pieces that are 1/4 metre each. How many pieces?",
                        visual: null,
                        steps: [
                            "'How many 1/4 fit in 3/4' = 3/4 ÷ 1/4",
                            "Keep, flip, change: 3/4 × <strong>4/1</strong>",
                            "Multiply: 3 × 4 = 12, 4 × 1 = 4",
                            "12/4 = <strong>3</strong>"
                        ],
                        answer: "3/4 ÷ 1/4 = 3 pieces"
                    }
                ],
                tip: "Remember: Keep-Flip-Change (KFC)! Keep the first, Flip the second, Change ÷ to ×"
            },
            9: {
                title: "Ratios & Proportions",
                band: "Higher",
                description: "Ratios compare quantities. You can convert between ratios and fractions. SEC exams love ratio problems with total amounts!",
                keyPoints: [
                    "Ratio a:b means 'a parts to b parts'",
                    "Total parts = add all ratio numbers",
                    "Each part = total amount ÷ total parts",
                    "Fraction = part ÷ whole"
                ],
                examples: [
                    {
                        question: "The ratio of fruit to yoghurt in a smoothie is 4:21. The total weight is 450g. How many grams of fruit?",
                        visual: null,
                        steps: [
                            "Total parts = 4 + 21 = <strong>25 parts</strong>",
                            "Each part = 450 ÷ 25 = <strong>18g</strong>",
                            "Fruit = 4 parts = 4 × 18 = <strong>72g</strong>"
                        ],
                        answer: "There are 72g of fruit"
                    }
                ],
                tip: "SEC 2023 Style! Always find 'one part' first, then multiply by how many parts you need."
            },
            10: {
                title: "Slope & Trigonometry",
                band: "Higher",
                description: "Give answers as fractions when asked! Slope = rise/run. Trig ratios (sin, cos, tan) are also fractions.",
                keyPoints: [
                    "Slope = (y₂ - y₁)/(x₂ - x₁) = rise/run",
                    "sin = opposite/hypotenuse",
                    "cos = adjacent/hypotenuse",
                    "tan = opposite/adjacent"
                ],
                examples: [
                    {
                        question: "Find the slope of the line through A(2, 1) and B(5, 7). Give your answer as a fraction.",
                        visual: null,
                        steps: [
                            "Slope = (y₂ - y₁)/(x₂ - x₁)",
                            "= (7 - 1)/(5 - 2)",
                            "= <strong>6/3</strong>",
                            "Simplify: 6/3 = <strong>2</strong> (or 2/1)"
                        ],
                        answer: "Slope = 6/3 = 2"
                    },
                    {
                        question: "In a right triangle, opposite = 5cm, hypotenuse = 13cm. Write sin A as a fraction.",
                        visual: null,
                        steps: [
                            "sin = opposite/hypotenuse",
                            "sin A = 5/13"
                        ],
                        answer: "sin A = 5/13"
                    }
                ],
                tip: "SEC Exam! Questions say 'Give your answer as a fraction' - don't convert to decimals! Keep it as a fraction."
            },
            11: {
                title: "Decimal & Percentage Conversions",
                band: "Higher",
                description: "Convert fluently between fractions, decimals, and percentages. Essential for real-world problems!",
                keyPoints: [
                    "Fraction → Decimal: divide top by bottom",
                    "Decimal → Fraction: use place value, then simplify",
                    "Decimal → %: multiply by 100",
                    "% → Decimal: divide by 100"
                ],
                examples: [
                    {
                        question: "Convert 3/8 to a percentage.",
                        visual: null,
                        steps: [
                            "First convert to decimal: 3 ÷ 8 = <strong>0.375</strong>",
                            "Multiply by 100: 0.375 × 100 = <strong>37.5%</strong>"
                        ],
                        answer: "3/8 = 37.5%"
                    },
                    {
                        question: "Write 0.75 as a fraction in simplest form.",
                        visual: null,
                        steps: [
                            "0.75 = 75/100 (75 hundredths)",
                            "Simplify: HCF of 75 and 100 is 25",
                            "75 ÷ 25 = 3, 100 ÷ 25 = 4"
                        ],
                        answer: "0.75 = 3/4"
                    }
                ],
                tip: "Know your common conversions: 1/2 = 50%, 1/4 = 25%, 3/4 = 75%, 1/5 = 20%, 1/8 = 12.5%"
            },
            12: {
                title: "Probability & Multi-Step Problems",
                band: "Mastery",
                description: "You've reached the top level! Apply all your fraction skills to complex, multi-step problems and probability.",
                keyPoints: [
                    "Probability = favourable outcomes/total outcomes",
                    "Multi-step: break into smaller steps",
                    "Combined operations: follow BIDMAS",
                    "Always simplify final answers"
                ],
                examples: [
                    {
                        question: "A school has 180 students. 1/3 are in sports clubs. Of those, 2/3 play football. How many play football?",
                        visual: null,
                        steps: [
                            "<strong>Step 1:</strong> Find students in sports clubs",
                            "1/3 of 180 = 180 × 1/3 = <strong>60 students</strong>",
                            "<strong>Step 2:</strong> Find footballers",
                            "2/3 of 60 = 60 × 2/3 = <strong>40 students</strong>"
                        ],
                        answer: "40 students play football"
                    },
                    {
                        question: "Calculate: (1/2 + 1/4) × 2/3",
                        visual: null,
                        steps: [
                            "<strong>Step 1:</strong> Brackets first: 1/2 + 1/4",
                            "= 2/4 + 1/4 = <strong>3/4</strong>",
                            "<strong>Step 2:</strong> Multiply: 3/4 × 2/3",
                            "= 6/12 = <strong>1/2</strong>"
                        ],
                        answer: "(1/2 + 1/4) × 2/3 = 1/2"
                    }
                ],
                tip: "🏆 You've mastered fractions! These Higher Level questions combine multiple skills. Take your time and show your working."
            }
        };
        
        // Arithmetic help content for all 12 levels
        const arithmeticHelpContent = {
            1: {
                title: "Addition",
                band: "Foundation",
                description: "At this level, you'll practice adding 2-digit and 3-digit numbers. This is a foundation skill that appears in SEC Q1(a).",
                keyPoints: [
                    "Line up digits by <strong>place value</strong> (units under units, tens under tens)",
                    "Add from <strong>right to left</strong>",
                    "Remember to <strong>carry over</strong> when a column totals 10 or more"
                ],
                examples: [
                    {
                        question: "Find the value of: 243 + 178",
                        steps: ["Add units: 3 + 8 = 11 (write 1, carry 1)", "Add tens: 4 + 7 + 1 = 12 (write 2, carry 1)", "Add hundreds: 2 + 1 + 1 = 4"],
                        answer: "421"
                    }
                ],
                tip: "SEC Tip: Q1(a)(i) often asks you to 'Find the value of' an addition. Show your working clearly."
            },
            2: {
                title: "Subtraction",
                band: "Foundation",
                description: "At this level, you'll practice subtracting 2-digit and 3-digit numbers. Watch for borrowing situations.",
                keyPoints: [
                    "Line up digits by <strong>place value</strong>",
                    "Subtract from <strong>right to left</strong>",
                    "<strong>Borrow</strong> from the next column when needed"
                ],
                examples: [
                    {
                        question: "Find the value of: 456 − 321",
                        steps: ["Subtract units: 6 - 1 = 5", "Subtract tens: 5 - 2 = 3", "Subtract hundreds: 4 - 3 = 1"],
                        answer: "135"
                    }
                ],
                tip: "Check your answer by adding: 135 + 321 = 456 ✓"
            },
            3: {
                title: "Multiplication",
                band: "Foundation",
                description: "At this level, you'll multiply whole numbers and decimals by single digits - a common SEC Q1(a) style.",
                keyPoints: [
                    "For <strong>decimal × whole</strong>: ignore the decimal, multiply, then place it back",
                    "SEC often uses patterns like <strong>3.4 × 7</strong> or <strong>7.2 × 6</strong>",
                    "Remember your <strong>times tables</strong>!"
                ],
                examples: [
                    {
                        question: "Find the value of: 3.4 × 7",
                        steps: ["Multiply as whole numbers: 34 × 7 = 238", "Count decimal places in question: 1", "Place decimal: 23.8"],
                        answer: "23.8"
                    }
                ],
                tip: "SEC Tip: Q1(a)(ii) often has decimal × whole number. Practice your 2-9 times tables!"
            },
            4: {
                title: "Division",
                band: "Ordinary",
                description: "At this level, you'll practice division with whole numbers, ensuring clean answers (no remainders yet).",
                keyPoints: [
                    "Division is the <strong>opposite of multiplication</strong>",
                    "Think: '__ × divisor = dividend'",
                    "Check by <strong>multiplying back</strong>"
                ],
                examples: [
                    {
                        question: "Find the value of: 72 ÷ 8",
                        steps: ["Think: what × 8 = 72?", "9 × 8 = 72 ✓"],
                        answer: "9"
                    }
                ],
                tip: "Use your times tables in reverse! If you know 8 × 9 = 72, then 72 ÷ 8 = 9."
            },
            5: {
                title: "Rounding",
                band: "Ordinary",
                description: "At this level, you'll round numbers to the nearest whole number, 10, or 100 - exactly as SEC Q1(b) asks.",
                keyPoints: [
                    "Look at the digit <strong>to the right</strong> of where you're rounding",
                    "If it's <strong>5 or more</strong>, round UP",
                    "If it's <strong>less than 5</strong>, round DOWN"
                ],
                examples: [
                    {
                        question: "Write down the whole number nearest to 15.8",
                        steps: ["The decimal part is .8", "Since 8 ≥ 5, round up"],
                        answer: "16"
                    }
                ],
                tip: "SEC Tip: 'Write down the whole number nearest to...' appears frequently. Practice with different decimals."
            },
            6: {
                title: "Midpoints",
                band: "Ordinary",
                description: "At this level, you'll find the number halfway between two values - another SEC Q1(c) favourite.",
                keyPoints: [
                    "To find halfway: <strong>Add</strong> the two numbers, then <strong>divide by 2</strong>",
                    "Formula: midpoint = (a + b) ÷ 2",
                    "This is the same as finding the <strong>average</strong>"
                ],
                examples: [
                    {
                        question: "What number is halfway between 16 and 30?",
                        steps: ["Add: 16 + 30 = 46", "Divide by 2: 46 ÷ 2 = 23"],
                        answer: "23"
                    }
                ],
                tip: "SEC Tip: 'What number is halfway between...' is a common Q1 question. Always add first, then halve."
            },
            7: {
                title: "Factors",
                band: "Higher",
                description: "At this level, you'll find all factors of a number. SEC Q1(b) and Q8 often ask about factors.",
                keyPoints: [
                    "A <strong>factor</strong> divides evenly into the number",
                    "Factors come in <strong>pairs</strong>: if 3 is a factor of 12, so is 12÷3=4",
                    "1 and the number itself are always factors"
                ],
                examples: [
                    {
                        question: "Find all factors of 12",
                        steps: ["1 × 12 = 12 → factors: 1, 12", "2 × 6 = 12 → factors: 2, 6", "3 × 4 = 12 → factors: 3, 4"],
                        answer: "1, 2, 3, 4, 6, 12"
                    }
                ],
                tip: "SEC Tip: 2024 Q1(b) asked for factors of 8, 12, and 16. Work systematically from 1 upwards."
            },
            8: {
                title: "LCM",
                band: "Higher",
                description: "At this level, you'll find the Lowest Common Multiple (LCM) of two numbers.",
                keyPoints: [
                    "<strong>Multiples</strong> are what you get when you multiply (e.g., multiples of 3: 3, 6, 9, 12...)",
                    "<strong>LCM</strong> = the smallest number that appears in both lists",
                    "List multiples of both numbers until you find a match"
                ],
                examples: [
                    {
                        question: "Find the LCM of 12 and 15",
                        steps: ["Multiples of 12: 12, 24, 36, 48, 60...", "Multiples of 15: 15, 30, 45, 60...", "First common multiple: 60"],
                        answer: "60"
                    }
                ],
                tip: "SEC Tip: 2025 Q8(a) asked for LCM of 12 and 15. List multiples systematically!"
            },
            9: {
                title: "HCF",
                band: "Higher",
                description: "At this level, you'll find the Highest Common Factor (HCF) of two or more numbers.",
                keyPoints: [
                    "<strong>HCF</strong> = the largest number that divides into both numbers",
                    "List all factors of each number, then find the biggest one they share",
                    "Also called Greatest Common Divisor (GCD)"
                ],
                examples: [
                    {
                        question: "Find the HCF of 8, 12, and 16",
                        steps: ["Factors of 8: 1, 2, 4, 8", "Factors of 12: 1, 2, 3, 4, 6, 12", "Factors of 16: 1, 2, 4, 8, 16", "Common factors: 1, 2, 4"],
                        answer: "4"
                    }
                ],
                tip: "SEC Tip: 2024 Q1(b) asked for HCF of 8, 12, and 16. Find factors of each, then pick the highest common one."
            },
            10: {
                title: "Powers & Indices",
                band: "Mastery",
                description: "At this level, you'll evaluate expressions with powers like 3⁴ or 2⁵ - common in SEC Q1(a).",
                keyPoints: [
                    "<strong>aⁿ</strong> means multiply 'a' by itself 'n' times",
                    "3⁴ = 3 × 3 × 3 × 3 = 81",
                    "Common powers to know: 2⁴=16, 3³=27, 5²=25"
                ],
                examples: [
                    {
                        question: "Find the value of 3⁴",
                        steps: ["3⁴ = 3 × 3 × 3 × 3", "= 9 × 3 × 3", "= 27 × 3"],
                        answer: "81"
                    }
                ],
                tip: "SEC Tip: Powers appear in Q1(a). Know your squares (2²=4, 3²=9...) and cubes (2³=8, 3³=27...)."
            },
            11: {
                title: "Square & Cube Roots",
                band: "Mastery",
                description: "At this level, you'll find square roots and cube roots, and use them in calculations like √9 × (7-3).",
                keyPoints: [
                    "<strong>√</strong> (square root): what number × itself = this?",
                    "<strong>∛</strong> (cube root): what number × itself × itself = this?",
                    "Know: √4=2, √9=3, √16=4, √25=5, √36=6..."
                ],
                examples: [
                    {
                        question: "Find the value of: √9 × (7 - 3)",
                        steps: ["√9 = 3", "(7 - 3) = 4", "3 × 4 = 12"],
                        answer: "12"
                    }
                ],
                tip: "SEC Tip: 2025 Q1(a)(iii) was √9 × (7 - 3). Always do roots and brackets first (BODMAS)."
            },
            12: {
                title: "BODMAS Mixed Operations",
                band: "Mastery",
                description: "At this level, you'll tackle SEC Q1(a) style questions with mixed operations, brackets, and indices.",
                keyPoints: [
                    "<strong>BODMAS</strong>: Brackets, Orders (powers/roots), Division, Multiplication, Addition, Subtraction",
                    "Always work through in this order",
                    "Common patterns: 24 ÷ (9-7), 32 ÷ (7-5)²"
                ],
                examples: [
                    {
                        question: "Find the value of: 32 ÷ (7 − 5)²",
                        steps: ["Brackets first: (7 - 5) = 2", "Orders (powers): 2² = 4", "Division: 32 ÷ 4 = 8"],
                        answer: "8"
                    }
                ],
                tip: "🏆 You've mastered Arithmetic! SEC Q1(a) typically has 3-4 parts just like these. Keep practising!"
            }
        };
        
        // Percentages help content for all 12 levels
        const percentagesHelpContent = {
            1: {
                title: "Visual Percentages",
                band: "Foundation",
                description: "At this level, you'll learn to recognise percentages from pictures and diagrams. Percent means 'per hundred' - so 25% means 25 out of every 100.",
                keyPoints: [
                    "<strong>Percent</strong> means 'out of 100'",
                    "A 10×10 grid has exactly <strong>100 squares</strong>",
                    "Count shaded squares to find the percentage"
                ],
                examples: [
                    {
                        question: "What percentage of this grid is shaded?",
                        visual: '<svg viewBox="0 0 110 110" width="100"><rect x="5" y="5" width="100" height="100" fill="#e5e7eb" stroke="#6b7280"/><rect x="5" y="5" width="50" height="100" fill="#3b82f6"/><text x="55" y="115" text-anchor="middle" font-size="10">50 squares shaded</text></svg>',
                        steps: [
                            "Total squares in grid: <strong>100</strong>",
                            "Count shaded squares: <strong>50</strong>",
                            "50 out of 100 = <strong>50%</strong>"
                        ],
                        answer: "50% of the grid is shaded"
                    }
                ],
                tip: "Remember: in a 10×10 grid, each column = 10%, each row = 10%!"
            },
            2: {
                title: "Percentage of an Amount (Simple)",
                band: "Foundation",
                description: "Calculate a percentage of a number by multiplying then dividing by 100. For example, 20% of 50 means '20 out of every 100' of 50.",
                keyPoints: [
                    "To find X% of Y: multiply X × Y, then divide by 100",
                    "Or: divide by 100 first, then multiply",
                    "10% = divide by 10, 50% = divide by 2"
                ],
                examples: [
                    {
                        question: "A class has 80 students. 25% study French. How many study French?",
                        visual: null,
                        steps: [
                            "25% of 80 = 25 × 80 ÷ 100",
                            "= 2000 ÷ 100",
                            "= <strong>20 students</strong>"
                        ],
                        answer: "20 students study French"
                    }
                ],
                tip: "For 25%, you can also divide by 4 (since 25% = 1/4)"
            },
            3: {
                title: "Percentage with Rounding",
                band: "Foundation",
                description: "In real-world problems, especially with money, you often need to round your answer. SEC exams frequently ask you to round to the nearest euro.",
                keyPoints: [
                    "Calculate the exact answer first",
                    "Round UP if decimal is .50 or more",
                    "Round DOWN if decimal is below .50"
                ],
                examples: [
                    {
                        question: "A meal costs €72. Calculate a 15% tip, rounded to the nearest euro.",
                        visual: null,
                        steps: [
                            "15% of €72 = 15 × 72 ÷ 100",
                            "= 1080 ÷ 100 = <strong>€10.80</strong>",
                            "Round to nearest euro: <strong>€11</strong>"
                        ],
                        answer: "The tip is €11"
                    }
                ],
                tip: "SEC Tip: Always show your unrounded answer first, then round as instructed!"
            },
            4: {
                title: "Fraction ↔ Percentage Conversion",
                band: "Ordinary",
                description: "Convert between fractions and percentages. To convert a fraction to a percentage, divide and multiply by 100.",
                keyPoints: [
                    "Fraction → %: divide top by bottom, × 100",
                    "% → Fraction: write over 100, then simplify",
                    "Know common ones: 1/2=50%, 1/4=25%, 3/4=75%"
                ],
                examples: [
                    {
                        question: "Convert 3/5 to a percentage",
                        visual: null,
                        steps: [
                            "Divide: 3 ÷ 5 = <strong>0.6</strong>",
                            "Multiply by 100: 0.6 × 100",
                            "= <strong>60%</strong>"
                        ],
                        answer: "3/5 = 60%"
                    }
                ],
                tip: "Memorise: 1/5=20%, 2/5=40%, 3/5=60%, 4/5=80%"
            },
            5: {
                title: "Decimal ↔ Percentage Conversion",
                band: "Ordinary",
                description: "Converting between decimals and percentages is straightforward: multiply or divide by 100.",
                keyPoints: [
                    "Decimal → %: multiply by 100 (move decimal 2 places right)",
                    "% → Decimal: divide by 100 (move decimal 2 places left)",
                    "0.5 = 50%, 0.25 = 25%, 0.1 = 10%"
                ],
                examples: [
                    {
                        question: "Convert 0.35 to a percentage",
                        visual: null,
                        steps: [
                            "Multiply by 100",
                            "0.35 × 100 = <strong>35%</strong>"
                        ],
                        answer: "0.35 = 35%"
                    }
                ],
                tip: "Think of it as 'sliding' the decimal point 2 places!"
            },
            6: {
                title: "Percentage Increase",
                band: "Ordinary",
                description: "To find percentage increase, calculate the change then divide by the ORIGINAL amount. This is a common SEC exam question.",
                keyPoints: [
                    "Formula: (New - Original) ÷ Original × 100",
                    "Always divide by the <strong>original</strong> (starting) value",
                    "The increase amount goes on top"
                ],
                examples: [
                    {
                        question: "Attendance rose from 80 to 100. Calculate the percentage increase.",
                        visual: null,
                        steps: [
                            "Find increase: 100 - 80 = <strong>20</strong>",
                            "Divide by original: 20 ÷ 80 = <strong>0.25</strong>",
                            "Multiply by 100: 0.25 × 100 = <strong>25%</strong>"
                        ],
                        answer: "25% increase"
                    }
                ],
                tip: "SEC Tip: The most common mistake is dividing by the new value instead of the original!"
            },
            7: {
                title: "Percentage Decrease & Discounts",
                band: "Higher",
                description: "Calculate discounts and percentage decreases. The formula is similar to increase, but we subtract new from original.",
                keyPoints: [
                    "Formula: (Original - New) ÷ Original × 100",
                    "To find sale price: Original × (100 - discount%) ÷ 100",
                    "Or: Original - (Original × discount% ÷ 100)"
                ],
                examples: [
                    {
                        question: "A jacket was €140, now €98. What is the percentage discount?",
                        visual: null,
                        steps: [
                            "Find decrease: €140 - €98 = <strong>€42</strong>",
                            "Divide by original: 42 ÷ 140 = <strong>0.3</strong>",
                            "Multiply by 100: 0.3 × 100 = <strong>30%</strong>"
                        ],
                        answer: "30% discount"
                    }
                ],
                tip: "To check: €140 × 0.70 = €98 ✓ (70% of original = 30% off)"
            },
            8: {
                title: "Comparing Percentage Changes",
                band: "Higher",
                description: "Compare which change represents a greater percentage. Calculate each percentage change separately, then compare.",
                keyPoints: [
                    "Calculate each percentage change individually",
                    "The larger percentage = greater proportional change",
                    "Absolute change ≠ percentage change!"
                ],
                examples: [
                    {
                        question: "Shop A: €100→€125. Shop B: €200→€240. Which had greater % increase?",
                        visual: null,
                        steps: [
                            "Shop A: (125-100)÷100 × 100 = <strong>25%</strong>",
                            "Shop B: (240-200)÷200 × 100 = <strong>20%</strong>",
                            "25% > 20%"
                        ],
                        answer: "Shop A had the greater percentage increase (25% vs 20%)"
                    }
                ],
                tip: "Even though Shop B's increase was €40 vs €25, Shop A had the bigger proportional change!"
            },
            9: {
                title: "Profit & Loss Percentage",
                band: "Higher",
                description: "Calculate profit or loss as a percentage of the COST price. This is how businesses measure their success.",
                keyPoints: [
                    "Profit % = (Selling Price - Cost) ÷ Cost × 100",
                    "Loss % = (Cost - Selling Price) ÷ Cost × 100",
                    "Always divide by <strong>cost price</strong>"
                ],
                examples: [
                    {
                        question: "Bought for €80, sold for €100. Calculate profit %.",
                        visual: null,
                        steps: [
                            "Profit = €100 - €80 = <strong>€20</strong>",
                            "Profit % = €20 ÷ €80 × 100",
                            "= 0.25 × 100 = <strong>25%</strong>"
                        ],
                        answer: "25% profit"
                    }
                ],
                tip: "SEC Tip: Profit is always calculated as % of cost price, not selling price!"
            },
            10: {
                title: "Reverse Percentages",
                band: "Application",
                description: "Find the original value when you know the final value after a percentage change. Work backwards!",
                keyPoints: [
                    "After increase: Original = Final ÷ (1 + rate)",
                    "After decrease: Original = Final ÷ (1 - rate)",
                    "Convert percentage to decimal first"
                ],
                examples: [
                    {
                        question: "After a 20% increase, the price is €120. What was the original?",
                        visual: null,
                        steps: [
                            "20% increase means final = 120% of original",
                            "120% = 1.20 as a decimal",
                            "Original = €120 ÷ 1.20 = <strong>€100</strong>"
                        ],
                        answer: "The original price was €100"
                    }
                ],
                tip: "Check: €100 + 20% = €100 + €20 = €120 ✓"
            },
            11: {
                title: "Simple Interest",
                band: "Application",
                description: "Simple interest is calculated using the formula I = P × r × t. Interest is earned only on the original principal.",
                keyPoints: [
                    "I = P × r × t (Interest = Principal × rate × time)",
                    "Rate must be a decimal (5% = 0.05)",
                    "Total amount = Principal + Interest"
                ],
                examples: [
                    {
                        question: "€500 invested at 4% for 3 years. Find the interest.",
                        visual: null,
                        steps: [
                            "I = P × r × t",
                            "I = €500 × 0.04 × 3",
                            "I = <strong>€60</strong>"
                        ],
                        answer: "Interest earned is €60"
                    }
                ],
                tip: "SEC Tip: To find rate, rearrange: r = I ÷ (P × t)"
            },
            12: {
                title: "Compound Interest & VAT",
                band: "Mastery",
                description: "Compound interest grows on the accumulated amount. VAT (23% in Ireland) is added to prices. These are Higher Level skills.",
                keyPoints: [
                    "Compound: A = P(1 + r)^n",
                    "VAT: Price with VAT = Price × 1.23",
                    "To find price before VAT: divide by 1.23"
                ],
                examples: [
                    {
                        question: "€1000 at 5% compound interest for 2 years.",
                        visual: null,
                        steps: [
                            "A = P(1 + r)^n",
                            "A = €1000 × (1.05)²",
                            "A = €1000 × 1.1025 = <strong>€1102.50</strong>"
                        ],
                        answer: "Total amount is €1102.50"
                    }
                ],
                tip: "🏆 You've mastered percentages! Compound interest gives MORE than simple interest over time."
            }
        };
        
        // Ratio Help Content - 12 Levels
        const ratioHelpContent = {
            1: {
                title: "Understanding Ratios",
                band: "Foundation",
                description: "A ratio compares two or more quantities. It tells us how much of one thing there is compared to another. We write ratios using a colon (:).",
                keyPoints: [
                    "A <strong>ratio</strong> compares quantities using a colon (:)",
                    "Order matters: 3:2 is different from 2:3",
                    "Count each type carefully before writing the ratio"
                ],
                examples: [
                    {
                        question: "There are 5 red balls and 3 blue balls. Write the ratio of red to blue.",
                        visual: '<svg viewBox="0 0 200 60" width="200"><circle cx="20" cy="30" r="12" fill="#ef4444"/><circle cx="50" cy="30" r="12" fill="#ef4444"/><circle cx="80" cy="30" r="12" fill="#ef4444"/><circle cx="110" cy="30" r="12" fill="#ef4444"/><circle cx="140" cy="30" r="12" fill="#ef4444"/><circle cx="170" cy="30" r="12" fill="#3b82f6"/><circle cx="200" cy="30" r="12" fill="#3b82f6"/><circle cx="230" cy="30" r="12" fill="#3b82f6"/><text x="80" y="55" font-size="10" fill="#ef4444">Red: 5</text><text x="170" y="55" font-size="10" fill="#3b82f6">Blue: 3</text></svg>',
                        steps: [
                            "Count red balls: <strong>5</strong>",
                            "Count blue balls: <strong>3</strong>",
                            "Write as ratio: red : blue"
                        ],
                        answer: "5:3"
                    }
                ],
                tip: "Always write the ratio in the order asked! 'Red to blue' means red number comes first."
            },
            2: {
                title: "Simplifying Ratios",
                band: "Foundation",
                description: "Simplify ratios by dividing both numbers by their highest common factor (HCF). This gives the simplest form.",
                keyPoints: [
                    "Find the <strong>HCF</strong> of both numbers",
                    "Divide BOTH parts by the HCF",
                    "The ratio is simplified when HCF is 1"
                ],
                examples: [
                    {
                        question: "Simplify the ratio 12:8",
                        visual: '<svg viewBox="0 0 280 80" width="280"><rect x="10" y="20" width="120" height="30" fill="#bfdbfe" stroke="#3b82f6" stroke-width="2" rx="4"/><text x="70" y="40" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e40af">12 : 8</text><text x="150" y="40" font-size="20" fill="#6b7280">→</text><rect x="170" y="20" width="90" height="30" fill="#bbf7d0" stroke="#22c55e" stroke-width="2" rx="4"/><text x="215" y="40" text-anchor="middle" font-size="14" font-weight="bold" fill="#166534">3 : 2</text><text x="70" y="65" font-size="10" fill="#6b7280">÷4  ÷4</text></svg>',
                        steps: [
                            "Find HCF of 12 and 8: <strong>4</strong>",
                            "Divide both: 12 ÷ 4 = 3",
                            "Divide both: 8 ÷ 4 = 2"
                        ],
                        answer: "12:8 = 3:2"
                    }
                ],
                tip: "Whatever you do to one part of the ratio, you must do to the other!"
            },
            3: {
                title: "Equivalent Ratios",
                band: "Foundation",
                description: "Equivalent ratios have the same value. Multiply or divide both parts by the same number to find them.",
                keyPoints: [
                    "Multiply BOTH parts by the same number",
                    "Equivalent ratios simplify to the same ratio",
                    "Use this to find missing values"
                ],
                examples: [
                    {
                        question: "If 2:3 = 6:?, find the missing number.",
                        visual: '<svg viewBox="0 0 280 60" width="280"><rect x="10" y="15" width="80" height="30" fill="#fef3c7" stroke="#f59e0b" stroke-width="2" rx="4"/><text x="50" y="35" text-anchor="middle" font-size="14" font-weight="bold" fill="#92400e">2 : 3</text><text x="110" y="35" font-size="16" fill="#6b7280">=</text><rect x="130" y="15" width="80" height="30" fill="#fef3c7" stroke="#f59e0b" stroke-width="2" rx="4"/><text x="170" y="35" text-anchor="middle" font-size="14" font-weight="bold" fill="#92400e">6 : ?</text><text x="50" y="55" font-size="10" fill="#059669">×3</text><text x="170" y="55" font-size="10" fill="#059669">×3</text></svg>',
                        steps: [
                            "2 × ? = 6, so multiplier is <strong>3</strong>",
                            "Apply same multiplier to second part",
                            "3 × 3 = <strong>9</strong>"
                        ],
                        answer: "The missing number is 9"
                    }
                ],
                tip: "Find how one number changed, then apply the same change to the other."
            },
            4: {
                title: "Sharing in a Ratio - Two Parts",
                band: "Ordinary",
                description: "When sharing an amount in a ratio, first find the total parts, then work out what one part is worth. SEC 2023 OL Q10(b) and 2025 OL Q2(b) test this skill!",
                keyPoints: [
                    "Add the ratio parts to get <strong>total parts</strong>",
                    "Divide the amount by total parts = <strong>one part</strong>",
                    "Multiply by each ratio number for each share"
                ],
                examples: [
                    {
                        question: "Liam and Ciara share €60 in the ratio 3:2. How much does each get?",
                        visual: '<svg viewBox="0 0 280 80" width="280"><rect x="10" y="10" width="260" height="25" fill="#e5e7eb" stroke="#6b7280" rx="4"/><rect x="10" y="10" width="156" height="25" fill="#3b82f6" rx="4"/><rect x="166" y="10" width="104" height="25" fill="#ef4444" rx="4"/><text x="88" y="27" text-anchor="middle" font-size="11" fill="white" font-weight="bold">Liam: 3 parts</text><text x="218" y="27" text-anchor="middle" font-size="11" fill="white" font-weight="bold">Ciara: 2 parts</text><text x="140" y="55" text-anchor="middle" font-size="12" fill="#374151">Total: €60 ÷ 5 parts = €12 per part</text><text x="88" y="75" font-size="11" fill="#1e40af">3 × €12 = €36</text><text x="218" y="75" font-size="11" fill="#b91c1c">2 × €12 = €24</text></svg>',
                        steps: [
                            "Total parts = 3 + 2 = <strong>5 parts</strong>",
                            "One part = €60 ÷ 5 = <strong>€12</strong>",
                            "Liam: 3 × €12 = €36, Ciara: 2 × €12 = €24"
                        ],
                        answer: "Liam gets €36, Ciara gets €24"
                    }
                ],
                tip: "Always check: do your answers add up to the original total?"
            },
            5: {
                title: "Sharing in a Ratio - Three Parts",
                band: "Ordinary",
                description: "The same method works for three or more parts. Add all parts, find one part's value, then calculate each share.",
                keyPoints: [
                    "Add ALL ratio parts together",
                    "Divide total amount by total parts",
                    "Multiply for each person's share"
                ],
                examples: [
                    {
                        question: "Anna, Ben and Clara share €120 in the ratio 2:3:1. How much does Ben get?",
                        visual: '<svg viewBox="0 0 280 80" width="280"><rect x="10" y="10" width="260" height="25" fill="#e5e7eb" stroke="#6b7280" rx="4"/><rect x="10" y="10" width="86" height="25" fill="#8b5cf6" rx="4"/><rect x="96" y="10" width="130" height="25" fill="#22c55e"/><rect x="226" y="10" width="44" height="25" fill="#f59e0b" rx="4"/><text x="53" y="27" text-anchor="middle" font-size="10" fill="white" font-weight="bold">Anna: 2</text><text x="161" y="27" text-anchor="middle" font-size="10" fill="white" font-weight="bold">Ben: 3</text><text x="248" y="27" text-anchor="middle" font-size="10" fill="white" font-weight="bold">Clara: 1</text><text x="140" y="55" text-anchor="middle" font-size="12" fill="#374151">Total: 2+3+1 = 6 parts, €120 ÷ 6 = €20/part</text><text x="140" y="75" text-anchor="middle" font-size="12" fill="#166534" font-weight="bold">Ben: 3 × €20 = €60</text></svg>',
                        steps: [
                            "Total parts = 2 + 3 + 1 = <strong>6 parts</strong>",
                            "One part = €120 ÷ 6 = <strong>€20</strong>",
                            "Ben gets 3 parts = 3 × €20 = <strong>€60</strong>"
                        ],
                        answer: "Ben gets €60"
                    }
                ],
                tip: "The person with the largest ratio number gets the largest share."
            },
            6: {
                title: "Finding Total from One Part",
                band: "Ordinary",
                description: "If you know one share, work backwards to find the total. Find what one part is worth, then multiply by total parts.",
                keyPoints: [
                    "Given share ÷ its ratio number = <strong>one part</strong>",
                    "One part × total parts = <strong>total amount</strong>",
                    "Check by sharing the total back"
                ],
                examples: [
                    {
                        question: "Two amounts are in ratio 3:5. The smaller is €24. Find the total.",
                        visual: '<svg viewBox="0 0 280 80" width="280"><rect x="10" y="15" width="90" height="30" fill="#fecaca" stroke="#ef4444" stroke-width="2" rx="4"/><text x="55" y="35" text-anchor="middle" font-size="12" font-weight="bold" fill="#991b1b">3 parts = €24</text><rect x="110" y="15" width="150" height="30" fill="#e5e7eb" stroke="#6b7280" stroke-width="2" rx="4"/><text x="185" y="35" text-anchor="middle" font-size="12" fill="#374151">5 parts = ?</text><text x="140" y="60" text-anchor="middle" font-size="11" fill="#059669">One part = €24 ÷ 3 = €8</text><text x="140" y="75" text-anchor="middle" font-size="11" fill="#1e40af">Total = 8 parts × €8 = €64</text></svg>',
                        steps: [
                            "3 parts = €24, so 1 part = €24 ÷ 3 = <strong>€8</strong>",
                            "Total parts = 3 + 5 = <strong>8 parts</strong>",
                            "Total = 8 × €8 = <strong>€64</strong>"
                        ],
                        answer: "The total is €64"
                    }
                ],
                tip: "Identify which ratio number matches the given amount first."
            },
            7: {
                title: "Ratio with Quantities",
                band: "Higher",
                description: "Apply ratios to real quantities like mixing drinks, paint, or ingredients. SEC 2024 HL Q4(a) tests mixing water and juice in a ratio!",
                keyPoints: [
                    "Same method: find total parts, then one part",
                    "Units matter: ml, g, kg - keep them consistent",
                    "The total amount = sum of all parts"
                ],
                examples: [
                    {
                        question: "Ciara makes orange drink by mixing water and juice in ratio 7:3. She makes 2 litres. How much juice?",
                        visual: '<svg viewBox="0 0 280 100" width="280"><rect x="20" y="10" width="40" height="70" fill="#bfdbfe" stroke="#3b82f6" stroke-width="2" rx="4"/><text x="40" y="50" text-anchor="middle" font-size="10" fill="#1e40af">Water</text><text x="40" y="65" text-anchor="middle" font-size="9" fill="#1e40af">7 parts</text><rect x="70" y="35" width="25" height="45" fill="#fed7aa" stroke="#f97316" stroke-width="2" rx="4"/><text x="82" y="55" text-anchor="middle" font-size="8" fill="#c2410c">Juice</text><text x="82" y="68" text-anchor="middle" font-size="8" fill="#c2410c">3 parts</text><text x="130" y="50" font-size="16" fill="#6b7280">=</text><rect x="150" y="20" width="50" height="60" fill="#bbf7d0" stroke="#22c55e" stroke-width="2" rx="4"/><text x="175" y="55" text-anchor="middle" font-size="10" fill="#166534">2 litres</text><text x="175" y="70" text-anchor="middle" font-size="8" fill="#166534">= 2000ml</text></svg>',
                        steps: [
                            "Total parts = 7 + 3 = <strong>10 parts</strong>",
                            "2 litres = 2000ml, One part = 2000 ÷ 10 = <strong>200ml</strong>",
                            "Juice = 3 parts = 3 × 200 = <strong>600ml</strong>"
                        ],
                        answer: "600ml of orange juice"
                    }
                ],
                tip: "Convert litres to ml if needed (1 litre = 1000ml) for easier calculation."
            },
            8: {
                title: "Mixing Problems",
                band: "Higher",
                description: "When you know one ingredient amount, use ratios to find the others. Set up the proportion correctly.",
                keyPoints: [
                    "Given amount ÷ its ratio part = multiplier",
                    "Multiply other ratio parts by the same multiplier",
                    "Works for any recipe or mixture"
                ],
                examples: [
                    {
                        question: "A drink is 5 parts water to 2 parts cordial. Using 400ml water, how much cordial?",
                        visual: '<svg viewBox="0 0 280 70" width="280"><text x="10" y="25" font-size="12" fill="#374151">Ratio:</text><text x="60" y="25" font-size="14" font-weight="bold" fill="#3b82f6">5</text><text x="75" y="25" font-size="14" fill="#6b7280">:</text><text x="90" y="25" font-size="14" font-weight="bold" fill="#f97316">2</text><text x="10" y="50" font-size="12" fill="#374151">Amount:</text><text x="60" y="50" font-size="14" font-weight="bold" fill="#3b82f6">400ml</text><text x="105" y="50" font-size="14" fill="#6b7280">:</text><text x="130" y="50" font-size="14" font-weight="bold" fill="#f97316">?</text><text x="170" y="35" font-size="11" fill="#059669">400 ÷ 5 = 80</text><text x="170" y="55" font-size="11" fill="#059669">2 × 80 = 160ml</text></svg>',
                        steps: [
                            "Water: 5 parts = 400ml",
                            "1 part = 400 ÷ 5 = <strong>80ml</strong>",
                            "Cordial: 2 parts = 2 × 80 = <strong>160ml</strong>"
                        ],
                        answer: "160ml of cordial"
                    }
                ],
                tip: "The ratio stays the same - only the amounts scale up or down."
            },
            9: {
                title: "Ratio with Fractions",
                band: "Higher",
                description: "SEC 2025 HL Q7(c) uses ratios like 1 : 3/2 : 5/3. Convert to whole numbers or work with fractions directly.",
                keyPoints: [
                    "Multiply all parts by the LCD to clear fractions",
                    "Or work directly with fraction arithmetic",
                    "The sum of parts still gives the total"
                ],
                examples: [
                    {
                        question: "Ingredients A, B, C are in ratio 1 : 3/2 : 5/3. In 1 litre, how much B?",
                        visual: '<svg viewBox="0 0 280 70" width="280"><text x="10" y="25" font-size="11" fill="#374151">Ratio: 1 : 3/2 : 5/3</text><text x="10" y="45" font-size="11" fill="#059669">= 6/6 : 9/6 : 10/6</text><text x="10" y="65" font-size="11" fill="#1e40af">= 6 : 9 : 10 (multiply by 6)</text><text x="180" y="35" font-size="11" fill="#374151">Total: 25 parts</text><text x="180" y="55" font-size="11" fill="#374151">B = 9/25 of 1000ml</text></svg>',
                        steps: [
                            "Clear fractions: multiply by 6 → <strong>6 : 9 : 10</strong>",
                            "Total parts = 6 + 9 + 10 = <strong>25</strong>",
                            "B = 9/25 × 1000 = <strong>360ml</strong>"
                        ],
                        answer: "360ml of ingredient B"
                    }
                ],
                tip: "Find the LCD of all fraction denominators to convert to whole number ratios."
            },
            10: {
                title: "Reverse Ratio Problems",
                band: "Higher",
                description: "Given one share or the difference between shares, work backwards to find the total or other shares.",
                keyPoints: [
                    "Use the known value to find one part",
                    "Difference between shares = difference in ratio parts × one part",
                    "Build up to find total"
                ],
                examples: [
                    {
                        question: "Money shared 4:7. The difference between shares is €30. Find the total.",
                        visual: '<svg viewBox="0 0 280 70" width="280"><rect x="10" y="15" width="80" height="25" fill="#bfdbfe" stroke="#3b82f6" stroke-width="2" rx="4"/><text x="50" y="32" text-anchor="middle" font-size="11" fill="#1e40af">4 parts</text><rect x="100" y="15" width="140" height="25" fill="#fecaca" stroke="#ef4444" stroke-width="2" rx="4"/><text x="170" y="32" text-anchor="middle" font-size="11" fill="#991b1b">7 parts</text><text x="140" y="55" font-size="11" fill="#374151">Difference: 7 - 4 = 3 parts = €30</text><text x="140" y="70" font-size="11" fill="#059669">1 part = €10, Total = 11 × €10 = €110</text></svg>',
                        steps: [
                            "Difference in parts = 7 - 4 = <strong>3 parts</strong>",
                            "3 parts = €30, so 1 part = <strong>€10</strong>",
                            "Total = 11 parts = 11 × €10 = <strong>€110</strong>"
                        ],
                        answer: "Total is €110"
                    }
                ],
                tip: "Difference problems give you the gap between ratio parts."
            },
            11: {
                title: "Real-world Applications",
                band: "Application",
                description: "Apply ratio skills to maps, recipes, scaling, and practical problems.",
                keyPoints: [
                    "Map scales are ratios (1:50000 means 1cm = 50000cm)",
                    "Recipes scale up or down proportionally",
                    "Unit conversions may be needed"
                ],
                examples: [
                    {
                        question: "A recipe for 4 people uses 300g flour. How much for 6 people?",
                        visual: '<svg viewBox="0 0 280 60" width="280"><text x="10" y="25" font-size="12" fill="#374151">4 people → 300g</text><text x="10" y="45" font-size="12" fill="#374151">6 people → ?</text><text x="150" y="25" font-size="11" fill="#059669">Scale factor: 6/4 = 1.5</text><text x="150" y="45" font-size="11" fill="#1e40af">300g × 1.5 = 450g</text></svg>',
                        steps: [
                            "Scale factor = 6 ÷ 4 = <strong>1.5</strong>",
                            "New amount = 300 × 1.5",
                            "= <strong>450g</strong> flour"
                        ],
                        answer: "450g of flour"
                    }
                ],
                tip: "Scale factor = new amount ÷ original amount"
            },
            12: {
                title: "Multi-step Ratio Problems",
                band: "Mastery",
                description: "Complex problems combining ratios with other concepts. Break down into steps and solve systematically.",
                keyPoints: [
                    "Read carefully - identify what's given and what's asked",
                    "Break into smaller steps",
                    "Check your answer makes sense"
                ],
                examples: [
                    {
                        question: "A:B = 2:3 and B:C = 4:5. Find A:B:C.",
                        visual: '<svg viewBox="0 0 280 70" width="280"><text x="10" y="20" font-size="11" fill="#374151">A:B = 2:3</text><text x="10" y="40" font-size="11" fill="#374151">B:C = 4:5</text><text x="120" y="20" font-size="11" fill="#059669">Make B same: 3×4=12</text><text x="120" y="40" font-size="11" fill="#059669">A:B = 8:12, B:C = 12:15</text><text x="10" y="60" font-size="12" font-weight="bold" fill="#1e40af">A:B:C = 8:12:15</text></svg>',
                        steps: [
                            "B appears in both - make B the same",
                            "A:B = 2:3 → multiply by 4 → <strong>8:12</strong>",
                            "B:C = 4:5 → multiply by 3 → <strong>12:15</strong>",
                            "Combine: A:B:C = <strong>8:12:15</strong>"
                        ],
                        answer: "A:B:C = 8:12:15"
                    }
                ],
                tip: "🏆 You've mastered ratios! The key is finding a common link between ratios."
            }
        };
        
        // Sets & Venn Diagrams Help Content - 12 Levels
        const setsHelpContent = {
            1: {
                title: "Understanding Sets",
                band: "Foundation",
                description: "A set is a collection of objects or numbers. We use curly brackets { } to list the elements of a set. The number of elements is written as #(A) or |A|.",
                keyPoints: [
                    "A <strong>set</strong> is written with curly brackets: {1, 2, 3}",
                    "<strong>#(A)</strong> means the number of elements in set A",
                    "Elements are listed once - no repeats!"
                ],
                examples: [
                    {
                        question: "List all even numbers less than 10. How many elements?",
                        visual: '<svg viewBox="0 0 200 60" width="200"><ellipse cx="100" cy="30" rx="90" ry="25" fill="#bfdbfe" stroke="#3b82f6" stroke-width="2"/><text x="100" y="35" text-anchor="middle" font-size="14" fill="#1e40af">{2, 4, 6, 8}</text><text x="100" y="55" font-size="10" fill="#374151">#(Set) = 4</text></svg>',
                        steps: [
                            "List even numbers: 2, 4, 6, 8",
                            "Write in set notation: {2, 4, 6, 8}",
                            "Count elements: <strong>4</strong>"
                        ],
                        answer: "#(Set) = 4"
                    }
                ],
                tip: "Remember: each element appears only once in a set, and order doesn't matter."
            },
            2: {
                title: "Set Membership",
                band: "Foundation",
                description: "The symbol ∈ means 'is an element of' or 'belongs to'. The symbol ∉ means 'is not an element of'.",
                keyPoints: [
                    "<strong>∈</strong> means 'is in the set'",
                    "<strong>∉</strong> means 'is NOT in the set'",
                    "Check if the number appears in the set"
                ],
                examples: [
                    {
                        question: "A = {3, 6, 9, 12}. Is 9 ∈ A?",
                        visual: '<svg viewBox="0 0 200 60" width="200"><ellipse cx="100" cy="30" rx="85" ry="25" fill="#bbf7d0" stroke="#22c55e" stroke-width="2"/><text x="100" y="35" text-anchor="middle" font-size="14" fill="#166534">{3, 6, 9, 12}</text><circle cx="140" cy="30" r="12" fill="#fbbf24" stroke="#f59e0b" stroke-width="2"/><text x="140" y="34" text-anchor="middle" font-size="10" font-weight="bold" fill="#92400e">9</text></svg>',
                        steps: [
                            "Look at set A: {3, 6, 9, 12}",
                            "Is 9 in the list? <strong>Yes!</strong>",
                            "So 9 ∈ A is <strong>True</strong>"
                        ],
                        answer: "Yes, 9 ∈ A"
                    }
                ],
                tip: "Simply scan through the set to see if the number is there."
            },
            3: {
                title: "Reading Venn Diagrams",
                band: "Foundation",
                description: "A Venn diagram shows sets as overlapping circles. The overlap (intersection) shows elements in BOTH sets. SEC papers frequently test reading values from Venn diagrams.",
                keyPoints: [
                    "Each circle represents a set",
                    "The <strong>overlap</strong> = elements in BOTH sets",
                    "Outside both circles = in NEITHER set"
                ],
                examples: [
                    {
                        question: "From the Venn diagram: How many like both Music AND Sport?",
                        visual: '<svg viewBox="0 0 200 100" width="200"><rect x="5" y="5" width="190" height="90" fill="#f3f4f6" stroke="#6b7280" rx="5"/><circle cx="70" cy="50" r="35" fill="#bfdbfe" fill-opacity="0.7" stroke="#3b82f6" stroke-width="2"/><circle cx="130" cy="50" r="35" fill="#fecaca" fill-opacity="0.7" stroke="#ef4444" stroke-width="2"/><text x="50" y="50" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e40af">15</text><text x="100" y="50" text-anchor="middle" font-size="14" font-weight="bold" fill="#7c3aed">8</text><text x="150" y="50" text-anchor="middle" font-size="14" font-weight="bold" fill="#b91c1c">12</text><text x="180" y="85" font-size="10" fill="#374151">7</text><text x="50" y="20" font-size="10" fill="#1e40af">M</text><text x="150" y="20" font-size="10" fill="#b91c1c">S</text></svg>',
                        steps: [
                            "Find the overlap region (middle)",
                            "This shows students in BOTH sets",
                            "The overlap contains <strong>8</strong>"
                        ],
                        answer: "8 students like both"
                    }
                ],
                tip: "The intersection (overlap) is always in the middle where circles meet."
            },
            4: {
                title: "Completing Venn Diagrams",
                band: "Ordinary",
                description: "SEC exams often give partial information and ask you to complete the diagram. Work from what you know - usually start with the intersection. SEC 2022 OL Q5 and 2025 OL Q5 test this!",
                keyPoints: [
                    "Start with the <strong>intersection</strong> (both)",
                    "Subtract intersection from each total for 'only' regions",
                    "Total - all regions = neither"
                ],
                examples: [
                    {
                        question: "120 students surveyed. 30 play both Sport and Games. 48 play Games total. How many play Games only?",
                        visual: '<svg viewBox="0 0 200 100" width="200"><rect x="5" y="5" width="190" height="90" fill="#fef3c7" stroke="#f59e0b" rx="5"/><circle cx="70" cy="50" r="35" fill="#bbf7d0" fill-opacity="0.7" stroke="#22c55e" stroke-width="2"/><circle cx="130" cy="50" r="35" fill="#fecaca" fill-opacity="0.7" stroke="#ef4444" stroke-width="2"/><text x="50" y="50" text-anchor="middle" font-size="12" fill="#166534">S only</text><text x="100" y="50" text-anchor="middle" font-size="14" font-weight="bold" fill="#7c3aed">30</text><text x="150" y="50" text-anchor="middle" font-size="14" font-weight="bold" fill="#dc2626">?</text><text x="50" y="20" font-size="10" fill="#166534">S</text><text x="150" y="20" font-size="10" fill="#dc2626">G</text></svg>',
                        steps: [
                            "Games total = 48",
                            "Both (intersection) = 30",
                            "Games only = 48 - 30 = <strong>18</strong>"
                        ],
                        answer: "18 play Games only"
                    }
                ],
                tip: "'A only' means in A but NOT in B. Calculate: Total in A minus intersection."
            },
            5: {
                title: "Finding Totals from Venn Diagrams",
                band: "Ordinary",
                description: "Add all four regions to find the total: A only + Both + B only + Neither = Total surveyed.",
                keyPoints: [
                    "Four regions: A only, Both, B only, Neither",
                    "Add all four to get the <strong>total</strong>",
                    "Check: does your total match the given information?"
                ],
                examples: [
                    {
                        question: "A only = 25, Both = 10, B only = 30, Neither = 15. What's the total?",
                        visual: '<svg viewBox="0 0 200 100" width="200"><rect x="5" y="5" width="190" height="90" fill="#e0f2fe" stroke="#0284c7" rx="5"/><circle cx="70" cy="50" r="35" fill="#c4b5fd" fill-opacity="0.7" stroke="#7c3aed" stroke-width="2"/><circle cx="130" cy="50" r="35" fill="#a5f3fc" fill-opacity="0.7" stroke="#06b6d4" stroke-width="2"/><text x="50" y="50" text-anchor="middle" font-size="14" font-weight="bold" fill="#5b21b6">25</text><text x="100" y="50" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f766e">10</text><text x="150" y="50" text-anchor="middle" font-size="14" font-weight="bold" fill="#0891b2">30</text><text x="180" y="85" font-size="12" font-weight="bold" fill="#374151">15</text></svg>',
                        steps: [
                            "Add all regions:",
                            "25 + 10 + 30 + 15",
                            "= <strong>80</strong>"
                        ],
                        answer: "Total = 80"
                    }
                ],
                tip: "Don't forget the 'neither' region outside both circles!"
            },
            6: {
                title: "Set Notation - Union & Intersection",
                band: "Ordinary",
                description: "A ∪ B (union) means A OR B or both. A ∩ B (intersection) means A AND B - elements in both sets.",
                keyPoints: [
                    "<strong>A ∪ B</strong> = union = elements in A OR B (or both)",
                    "<strong>A ∩ B</strong> = intersection = elements in BOTH A and B",
                    "∪ looks like a cup (holds everything), ∩ looks like a cap"
                ],
                examples: [
                    {
                        question: "A = {1, 2, 3, 4}, B = {3, 4, 5, 6}. Find #(A ∩ B).",
                        visual: '<svg viewBox="0 0 200 80" width="200"><circle cx="70" cy="40" r="30" fill="#bfdbfe" fill-opacity="0.6" stroke="#3b82f6" stroke-width="2"/><circle cx="130" cy="40" r="30" fill="#fecaca" fill-opacity="0.6" stroke="#ef4444" stroke-width="2"/><text x="45" y="40" font-size="10" fill="#1e40af">1,2</text><text x="100" y="40" text-anchor="middle" font-size="11" font-weight="bold" fill="#7c3aed">3,4</text><text x="155" y="40" font-size="10" fill="#b91c1c">5,6</text><text x="50" y="15" font-size="10" fill="#1e40af">A</text><text x="150" y="15" font-size="10" fill="#b91c1c">B</text></svg>',
                        steps: [
                            "Intersection = elements in BOTH sets",
                            "A has {1,2,3,4}, B has {3,4,5,6}",
                            "Common elements: {3, 4}, so #(A ∩ B) = <strong>2</strong>"
                        ],
                        answer: "#(A ∩ B) = 2"
                    }
                ],
                tip: "Intersection (∩) = the overlap. Union (∪) = everything in either circle."
            },
            7: {
                title: "Set Notation - A\\B (Set Difference)",
                band: "Higher",
                description: "A\\B means elements in A but NOT in B. This is called 'set difference' or 'A minus B'. SEC 2023 OL Q3 and 2025 OL Q5 test this notation!",
                keyPoints: [
                    "<strong>A\\B</strong> = in A but NOT in B = 'A only'",
                    "<strong>B\\A</strong> = in B but NOT in A = 'B only'",
                    "Read as 'A without B' or 'A minus B'"
                ],
                examples: [
                    {
                        question: "What does S\\M = 35 mean if S = Sport, M = Music?",
                        visual: '<svg viewBox="0 0 200 80" width="200"><circle cx="70" cy="40" r="30" fill="#bbf7d0" fill-opacity="0.7" stroke="#22c55e" stroke-width="2"/><circle cx="130" cy="40" r="30" fill="#fbbf24" fill-opacity="0.9" stroke="#f59e0b" stroke-width="2"/><text x="45" y="43" font-size="10" fill="#166534">M only</text><text x="100" y="43" text-anchor="middle" font-size="10" fill="#7c3aed">Both</text><text x="148" y="43" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">35</text><text x="50" y="15" font-size="10" fill="#166534">M</text><text x="150" y="15" font-size="10" fill="#92400e">S</text></svg>',
                        steps: [
                            "S\\M means 'in S but not in M'",
                            "This is the 'Sport only' region",
                            "35 students play Sport but NOT Music"
                        ],
                        answer: "35 students play Sport only (not Music)"
                    }
                ],
                tip: "Think of \\ as 'without' - A\\B = A without B."
            },
            8: {
                title: "Probability from Venn Diagrams",
                band: "Higher",
                description: "Find probability by dividing favourable outcomes by total outcomes. SEC 2022 OL Q5 and 2024 OL Q3 test probability from Venn diagrams!",
                keyPoints: [
                    "<strong>P(event) = favourable ÷ total</strong>",
                    "Count the region(s) asked for",
                    "Simplify your fraction"
                ],
                examples: [
                    {
                        question: "100 students: 30 in A only, 15 in both, 25 in B only, 30 in neither. Find P(in both).",
                        visual: '<svg viewBox="0 0 200 100" width="200"><rect x="5" y="5" width="190" height="90" fill="#fce7f3" stroke="#db2777" rx="5"/><circle cx="70" cy="50" r="30" fill="#c4b5fd" fill-opacity="0.7" stroke="#7c3aed" stroke-width="2"/><circle cx="130" cy="50" r="30" fill="#a5f3fc" fill-opacity="0.7" stroke="#06b6d4" stroke-width="2"/><text x="50" y="50" font-size="12" fill="#5b21b6">30</text><text x="100" y="50" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f766e">15</text><text x="150" y="50" font-size="12" fill="#0891b2">25</text><text x="175" y="85" font-size="11" fill="#374151">30</text><text x="100" y="95" font-size="10" fill="#374151">Total = 100</text></svg>',
                        steps: [
                            "Favourable = both = 15",
                            "Total = 100",
                            "P(both) = 15/100 = <strong>3/20</strong>"
                        ],
                        answer: "P(both) = 3/20"
                    }
                ],
                tip: "Always simplify your probability fraction to lowest terms!"
            },
            9: {
                title: "Venn Diagrams with Algebra",
                band: "Higher",
                description: "SEC Higher Level uses algebra in Venn diagrams. Set up an equation using the total, then solve for x. SEC 2022 HL Q6 and 2025 HL Q10 test this!",
                keyPoints: [
                    "Regions may be expressions like 'x' or '2x + 3'",
                    "Sum of all regions = total",
                    "Solve the equation to find x"
                ],
                examples: [
                    {
                        question: "88 students. D only = 40-x, both = x, C only = 37-x, neither = 37. Find x.",
                        visual: '<svg viewBox="0 0 200 100" width="200"><rect x="5" y="5" width="190" height="90" fill="#fdf2f8" stroke="#db2777" rx="5"/><circle cx="70" cy="50" r="30" fill="#c4b5fd" fill-opacity="0.6" stroke="#7c3aed" stroke-width="2"/><circle cx="130" cy="50" r="30" fill="#a5f3fc" fill-opacity="0.6" stroke="#06b6d4" stroke-width="2"/><text x="45" y="50" font-size="10" fill="#5b21b6">40-x</text><text x="100" y="50" text-anchor="middle" font-size="12" font-weight="bold" fill="#0f766e">x</text><text x="148" y="50" font-size="10" fill="#0891b2">37-x</text><text x="175" y="85" font-size="10" fill="#374151">37</text><text x="50" y="20" font-size="10" fill="#5b21b6">D</text><text x="150" y="20" font-size="10" fill="#0891b2">C</text></svg>',
                        steps: [
                            "Total: (40-x) + x + (37-x) + 37 = 88",
                            "Simplify: 114 - x = 88",
                            "Solve: x = <strong>26</strong>"
                        ],
                        answer: "x = 26"
                    }
                ],
                tip: "Write the equation: all regions added = total, then solve for x."
            },
            10: {
                title: "Three-Set Venn Diagrams",
                band: "Higher",
                description: "Three overlapping circles create 7 regions plus 'neither'. Work from the centre outwards - start with the region where all three overlap.",
                keyPoints: [
                    "Centre region = in ALL THREE sets",
                    "Work outwards from the centre",
                    "7 regions inside circles + 1 outside = 8 total regions"
                ],
                examples: [
                    {
                        question: "In a 3-set diagram: all three = 5, A∩B only = 8. How many in A∩B total?",
                        visual: '<svg viewBox="0 0 200 100" width="200"><circle cx="80" cy="40" r="30" fill="#bfdbfe" fill-opacity="0.5" stroke="#3b82f6" stroke-width="2"/><circle cx="120" cy="40" r="30" fill="#fecaca" fill-opacity="0.5" stroke="#ef4444" stroke-width="2"/><circle cx="100" cy="70" r="30" fill="#bbf7d0" fill-opacity="0.5" stroke="#22c55e" stroke-width="2"/><text x="100" y="50" text-anchor="middle" font-size="10" font-weight="bold" fill="#7c3aed">5</text><text x="100" y="30" text-anchor="middle" font-size="10" fill="#1e40af">8</text><text x="60" y="25" font-size="10" fill="#3b82f6">A</text><text x="140" y="25" font-size="10" fill="#ef4444">B</text><text x="100" y="95" font-size="10" fill="#22c55e">C</text></svg>',
                        steps: [
                            "A∩B total = (A∩B only) + (all three)",
                            "A∩B total = 8 + 5",
                            "= <strong>13</strong>"
                        ],
                        answer: "#(A∩B) = 13"
                    }
                ],
                tip: "A∩B includes both 'A∩B only' AND 'all three' - don't forget the centre!"
            },
            11: {
                title: "Word Problems with Sets",
                band: "Application",
                description: "Apply the inclusion-exclusion formula: #(A∪B) = #(A) + #(B) - #(A∩B). This avoids double-counting the intersection.",
                keyPoints: [
                    "<strong>#(A∪B) = #(A) + #(B) - #(A∩B)</strong>",
                    "Subtract intersection to avoid counting twice",
                    "Neither = Total - #(A∪B)"
                ],
                examples: [
                    {
                        question: "100 people: 60 own a car, 40 own a bike, 25 own both. How many own neither?",
                        visual: '<svg viewBox="0 0 200 80" width="200"><circle cx="70" cy="40" r="30" fill="#bfdbfe" fill-opacity="0.7" stroke="#3b82f6" stroke-width="2"/><circle cx="130" cy="40" r="30" fill="#fecaca" fill-opacity="0.7" stroke="#ef4444" stroke-width="2"/><text x="45" y="43" font-size="11" fill="#1e40af">35</text><text x="100" y="43" text-anchor="middle" font-size="11" font-weight="bold" fill="#7c3aed">25</text><text x="155" y="43" font-size="11" fill="#b91c1c">15</text><text x="50" y="15" font-size="10" fill="#1e40af">Car</text><text x="150" y="15" font-size="10" fill="#b91c1c">Bike</text></svg>',
                        steps: [
                            "#(Car∪Bike) = 60 + 40 - 25 = 75",
                            "Neither = Total - Union",
                            "Neither = 100 - 75 = <strong>25</strong>"
                        ],
                        answer: "25 own neither"
                    }
                ],
                tip: "The formula prevents double-counting people in BOTH sets."
            },
            12: {
                title: "Complex Set Problems",
                band: "Mastery",
                description: "Combine all your skills: algebra, probability, set notation, and multi-step reasoning. These are Higher Level exam style questions.",
                keyPoints: [
                    "Read carefully - identify ALL given information",
                    "Draw and label the Venn diagram",
                    "Use algebra if values are unknown"
                ],
                examples: [
                    {
                        question: "#(A) = 50, #(B) = 40, #(A∩B) = 15. Find #(A\\B) + #(B\\A).",
                        visual: '<svg viewBox="0 0 200 80" width="200"><circle cx="70" cy="40" r="30" fill="#fbbf24" fill-opacity="0.7" stroke="#f59e0b" stroke-width="2"/><circle cx="130" cy="40" r="30" fill="#fbbf24" fill-opacity="0.7" stroke="#f59e0b" stroke-width="2"/><text x="45" y="43" font-size="11" font-weight="bold" fill="#92400e">35</text><text x="100" y="43" text-anchor="middle" font-size="11" fill="#7c3aed">15</text><text x="155" y="43" font-size="11" font-weight="bold" fill="#92400e">25</text><text x="50" y="15" font-size="10" fill="#92400e">A</text><text x="150" y="15" font-size="10" fill="#92400e">B</text></svg>',
                        steps: [
                            "A\\B = #(A) - #(A∩B) = 50 - 15 = 35",
                            "B\\A = #(B) - #(A∩B) = 40 - 15 = 25",
                            "#(A\\B) + #(B\\A) = 35 + 25 = <strong>60</strong>"
                        ],
                        answer: "60"
                    }
                ],
                tip: "🏆 You've mastered Sets & Venn Diagrams! Remember: A\\B + A∩B + B\\A = A∪B."
            }
        };
        
        // Descriptive Statistics Help Content - 12 Levels
        const descriptiveStatisticsHelpContent = {
            1: {
                title: "Reading Data",
                band: "Foundation",
                description: "Learn to read data from tally charts, pictograms, and bar charts. These are common ways to display information visually.",
                keyPoints: [
                    "A <strong>tally chart</strong> uses marks (||||) to count - every 5th mark crosses the previous 4",
                    "A <strong>pictogram</strong> uses pictures to represent data - check the key!",
                    "A <strong>bar chart</strong> uses bars - read the height against the scale"
                ],
                examples: [
                    {
                        question: "A pictogram shows ⭐⭐⭐ for Monday. If ⭐ = 4 students, how many students?",
                        visual: '<svg viewBox="0 0 200 50" width="200"><text x="10" y="30" font-size="20">⭐⭐⭐</text><text x="120" y="30" font-size="12" fill="#374151">Key: ⭐ = 4</text></svg>',
                        steps: [
                            "Count the symbols: <strong>3 stars</strong>",
                            "Check the key: 1 star = 4 students",
                            "Calculate: 3 × 4 = <strong>12 students</strong>"
                        ],
                        answer: "12 students"
                    }
                ],
                tip: "Always check the key or scale before reading values!"
            },
            2: {
                title: "Mode from Lists & Tables",
                band: "Foundation",
                description: "The mode is the most common value - the one that appears most often. A data set can have no mode, one mode, or multiple modes.",
                keyPoints: [
                    "The <strong>mode</strong> is the value that appears most frequently",
                    "Count how many times each value appears",
                    "The value with the highest count is the mode"
                ],
                examples: [
                    {
                        question: "Find the mode: 3, 5, 7, 5, 8, 5, 2",
                        visual: '<svg viewBox="0 0 200 60" width="200"><text x="10" y="25" font-size="12" fill="#374151">3, 5, 7, 5, 8, 5, 2</text><text x="10" y="50" font-size="12" fill="#22c55e" font-weight="bold">5 appears 3 times ✓</text></svg>',
                        steps: [
                            "Count each value: 3(×1), 5(×3), 7(×1), 8(×1), 2(×1)",
                            "Which appears most? <strong>5 appears 3 times</strong>",
                            "Mode = <strong>5</strong>"
                        ],
                        answer: "Mode = 5"
                    }
                ],
                tip: "Mode = Most Often Data Entry"
            },
            3: {
                title: "Range from Lists & Tables",
                band: "Foundation",
                description: "The range tells us how spread out the data is. It's the difference between the largest and smallest values.",
                keyPoints: [
                    "<strong>Range = Largest − Smallest</strong>",
                    "First identify the highest and lowest values",
                    "A large range means data is spread out; small range means clustered"
                ],
                examples: [
                    {
                        question: "Find the range: 12, 8, 15, 3, 9",
                        visual: '<svg viewBox="0 0 220 50" width="220"><text x="10" y="20" font-size="11" fill="#ef4444">Smallest: 3</text><text x="10" y="40" font-size="11" fill="#3b82f6">Largest: 15</text><text x="120" y="30" font-size="14" fill="#374151">Range = 15 − 3 = 12</text></svg>',
                        steps: [
                            "Find largest value: <strong>15</strong>",
                            "Find smallest value: <strong>3</strong>",
                            "Range = 15 − 3 = <strong>12</strong>"
                        ],
                        answer: "Range = 12"
                    }
                ],
                tip: "Range = Highest − Lowest (always positive!)"
            },
            4: {
                title: "Median (Odd Datasets)",
                band: "Ordinary",
                description: "The median is the middle value when data is arranged in order. With an odd number of values, there's exactly one middle value.",
                keyPoints: [
                    "First <strong>arrange data in order</strong> (smallest to largest)",
                    "The <strong>median</strong> is the middle value",
                    "With n values, median is at position (n+1)/2"
                ],
                examples: [
                    {
                        question: "Find the median: 7, 2, 9, 4, 5",
                        visual: '<svg viewBox="0 0 250 50" width="250"><text x="10" y="20" font-size="11" fill="#374151">Ordered: 2, 4, 5, 7, 9</text><text x="10" y="40" font-size="11" fill="#22c55e" font-weight="bold">Middle value: 5 ✓</text></svg>',
                        steps: [
                            "Arrange in order: 2, 4, <strong>5</strong>, 7, 9",
                            "5 values, so middle is position 3",
                            "Median = <strong>5</strong>"
                        ],
                        answer: "Median = 5"
                    }
                ],
                tip: "Order first, then find the middle!"
            },
            5: {
                title: "Median (Even Datasets)",
                band: "Ordinary",
                description: "With an even number of values, there are two middle values. The median is their average.",
                keyPoints: [
                    "Arrange data in order first",
                    "Find the two middle values",
                    "<strong>Median = average of the two middle values</strong>"
                ],
                examples: [
                    {
                        question: "Find the median: 3, 8, 5, 12, 6, 9",
                        visual: '<svg viewBox="0 0 280 50" width="280"><text x="10" y="20" font-size="11" fill="#374151">Ordered: 3, 5, 6, 8, 9, 12</text><text x="10" y="40" font-size="11" fill="#22c55e">Middle two: 6 and 8 → (6+8)/2 = 7</text></svg>',
                        steps: [
                            "Order: 3, 5, <strong>6, 8</strong>, 9, 12",
                            "Two middle values: 6 and 8",
                            "Median = (6 + 8) ÷ 2 = <strong>7</strong>"
                        ],
                        answer: "Median = 7"
                    }
                ],
                tip: "Even count? Average the two middle values!"
            },
            6: {
                title: "Mean (Simple Averages)",
                band: "Ordinary",
                description: "The mean is what most people call 'the average'. Add all values and divide by how many there are.",
                keyPoints: [
                    "<strong>Mean = Sum of all values ÷ Number of values</strong>",
                    "Add up all the numbers first",
                    "Count how many values there are, then divide"
                ],
                examples: [
                    {
                        question: "Find the mean: 4, 7, 5, 8, 6",
                        visual: '<svg viewBox="0 0 250 60" width="250"><text x="10" y="20" font-size="11" fill="#374151">Sum: 4+7+5+8+6 = 30</text><text x="10" y="40" font-size="11" fill="#374151">Count: 5 values</text><text x="10" y="55" font-size="11" fill="#22c55e" font-weight="bold">Mean = 30 ÷ 5 = 6</text></svg>',
                        steps: [
                            "Add all values: 4+7+5+8+6 = <strong>30</strong>",
                            "Count values: <strong>5</strong>",
                            "Mean = 30 ÷ 5 = <strong>6</strong>"
                        ],
                        answer: "Mean = 6"
                    }
                ],
                tip: "Mean = Total ÷ Count"
            },
            7: {
                title: "Frequency Tables",
                band: "Higher",
                description: "Frequency tables organise data by showing how often each value appears. They're especially useful for large datasets.",
                keyPoints: [
                    "<strong>Frequency</strong> means how often a value occurs",
                    "The total frequency = total number of data points",
                    "Mode is the value with highest frequency"
                ],
                examples: [
                    {
                        question: "From a frequency table: Value 3 has frequency 5, Value 4 has frequency 8. What's the mode?",
                        visual: '<svg viewBox="0 0 200 70" width="200"><rect x="10" y="10" width="80" height="20" fill="#e5e7eb" stroke="#6b7280"/><text x="50" y="25" text-anchor="middle" font-size="10">Value</text><rect x="90" y="10" width="80" height="20" fill="#e5e7eb" stroke="#6b7280"/><text x="130" y="25" text-anchor="middle" font-size="10">Frequency</text><text x="50" y="45" text-anchor="middle" font-size="10">3</text><text x="130" y="45" text-anchor="middle" font-size="10">5</text><text x="50" y="60" text-anchor="middle" font-size="10">4</text><text x="130" y="60" text-anchor="middle" font-size="10" fill="#22c55e" font-weight="bold">8 ✓</text></svg>',
                        steps: [
                            "Compare frequencies: 5 vs 8",
                            "Highest frequency is <strong>8</strong>",
                            "Mode = value with frequency 8 = <strong>4</strong>"
                        ],
                        answer: "Mode = 4"
                    }
                ],
                tip: "Highest frequency → Mode value"
            },
            8: {
                title: "Mean from Frequency Tables",
                band: "Higher",
                description: "To find the mean from a frequency table, multiply each value by its frequency, add these products, then divide by total frequency.",
                keyPoints: [
                    "Calculate value × frequency for each row",
                    "Add all the products together",
                    "<strong>Mean = Sum of (value × frequency) ÷ Total frequency</strong>"
                ],
                examples: [
                    {
                        question: "Score 1 (freq 3), Score 2 (freq 5), Score 3 (freq 2). Find mean.",
                        visual: '<svg viewBox="0 0 250 50" width="250"><text x="10" y="20" font-size="10" fill="#374151">Σ(x×f) = 1×3 + 2×5 + 3×2 = 3+10+6 = 19</text><text x="10" y="40" font-size="10" fill="#374151">Total freq = 3+5+2 = 10, Mean = 19÷10 = 1.9</text></svg>',
                        steps: [
                            "Value × Freq: (1×3) + (2×5) + (3×2) = 3+10+6 = <strong>19</strong>",
                            "Total frequency: 3+5+2 = <strong>10</strong>",
                            "Mean = 19 ÷ 10 = <strong>1.9</strong>"
                        ],
                        answer: "Mean = 1.9"
                    }
                ],
                tip: "Mean = Σ(f×x) ÷ Σf"
            },
            9: {
                title: "Histograms & Grouped Data",
                band: "Higher",
                description: "Histograms show grouped continuous data. Bars touch each other and the height shows frequency. SEC commonly asks which interval contains the median.",
                keyPoints: [
                    "Groups are called <strong>class intervals</strong> (e.g., 0-10, 10-20)",
                    "For median interval, find where the middle value falls",
                    "Add frequencies from left until you pass the middle"
                ],
                examples: [
                    {
                        question: "30 values: 0-10 (8), 10-20 (12), 20-30 (10). Which interval contains median?",
                        visual: '<svg viewBox="0 0 250 60" width="250"><text x="10" y="20" font-size="10" fill="#374151">Total = 30, so median is 15th & 16th values</text><text x="10" y="40" font-size="10" fill="#374151">0-10 has 8 (positions 1-8)</text><text x="10" y="55" font-size="10" fill="#22c55e">10-20 has 12 (positions 9-20) ✓ contains 15th!</text></svg>',
                        steps: [
                            "Total = 30, median position = 15th/16th",
                            "Cumulative: 0-10 covers 1-8, 10-20 covers 9-20",
                            "15th value is in <strong>10-20 interval</strong>"
                        ],
                        answer: "10-20 interval"
                    }
                ],
                tip: "Count cumulative frequency to find median interval!"
            },
            10: {
                title: "Stem-and-Leaf Diagrams",
                band: "Higher",
                description: "Stem-and-leaf diagrams show individual data values while keeping them organised. The 'stem' is the tens digit, 'leaf' is the units.",
                keyPoints: [
                    "<strong>Stem</strong> = tens digit, <strong>Leaf</strong> = units digit",
                    "Key tells you what the digits mean (e.g., 3|5 = 35)",
                    "Data stays in order - easy to find median"
                ],
                examples: [
                    {
                        question: "Stem 4 | Leaves: 2, 5, 7. What are the values?",
                        visual: '<svg viewBox="0 0 200 60" width="200"><text x="10" y="20" font-size="12" fill="#374151">4 | 2 5 7</text><text x="10" y="40" font-size="11" fill="#6b7280">Key: 4|2 = 42</text><text x="10" y="55" font-size="11" fill="#22c55e">Values: 42, 45, 47</text></svg>',
                        steps: [
                            "Stem is 4 (tens digit)",
                            "Leaves are 2, 5, 7 (units)",
                            "Values: <strong>42, 45, 47</strong>"
                        ],
                        answer: "42, 45, 47"
                    }
                ],
                tip: "Read the key! It tells you how to interpret the diagram."
            },
            11: {
                title: "Comparing Measures",
                band: "Application",
                description: "SEC often asks 'Which average is better?' Mean is affected by outliers; median is more robust. Choose based on context.",
                keyPoints: [
                    "<strong>Mean</strong> uses all data but is affected by extreme values (outliers)",
                    "<strong>Median</strong> is not affected by outliers - good for skewed data",
                    "<strong>Mode</strong> is useful for categorical data (most popular choice)"
                ],
                examples: [
                    {
                        question: "Salaries: €30k, €32k, €35k, €200k. Which is better - mean or median?",
                        visual: '<svg viewBox="0 0 280 50" width="280"><text x="10" y="20" font-size="10" fill="#374151">Mean = (30+32+35+200)/4 = €74.25k</text><text x="10" y="40" font-size="10" fill="#22c55e">Median = (32+35)/2 = €33.5k ← More typical!</text></svg>',
                        steps: [
                            "€200k is an outlier (extreme value)",
                            "Mean = €74.25k (distorted by outlier)",
                            "<strong>Median = €33.5k</strong> is more representative"
                        ],
                        answer: "Median is better - not affected by the outlier"
                    }
                ],
                tip: "Outliers? Use median. Symmetric data? Mean is fine."
            },
            12: {
                title: "Problem Solving",
                band: "Mastery",
                description: "Complex problems involving back-to-back stem-and-leaf, finding missing values, or working backwards from given statistics.",
                keyPoints: [
                    "Back-to-back diagrams compare two datasets",
                    "If given mean/median/mode, work backwards to find missing values",
                    "Check all conditions are satisfied"
                ],
                examples: [
                    {
                        question: "5 numbers in order: 2, ?, ?, 10, ?. Mode=2, median=7, range=12. Find missing values.",
                        visual: '<svg viewBox="0 0 280 50" width="280"><text x="10" y="20" font-size="10" fill="#374151">Range=12: largest = 2+12 = 14</text><text x="10" y="35" font-size="10" fill="#374151">Mode=2: another 2 needed</text><text x="10" y="50" font-size="10" fill="#22c55e">Answer: 2, 2, 7, 10, 14</text></svg>',
                        steps: [
                            "Range=12, smallest=2, so largest=<strong>14</strong>",
                            "Mode=2, so another <strong>2</strong> needed",
                            "Median=7 (middle value), so: 2, 2, <strong>7</strong>, 10, 14"
                        ],
                        answer: "2, 2, 7, 10, 14"
                    }
                ],
                tip: "🏆 You've mastered Statistics! Use each condition systematically."
            }
        };
        
        // Patterns & Sequences Help Content - 12 Levels
        const patternsHelpContent = {
            1: {
                title: "Reading Visual Patterns",
                band: "Foundation",
                description: "Learn to identify patterns in sequences of shapes, dots, or objects. Count the elements in each term to spot the pattern.",
                keyPoints: [
                    "Count the objects in Pattern 1, Pattern 2, Pattern 3...",
                    "Look for what stays the same and what changes",
                    "Describe the pattern in words"
                ],
                examples: [
                    {
                        question: "Pattern 1 has 3 dots, Pattern 2 has 5 dots, Pattern 3 has 7 dots. How many in Pattern 4?",
                        visual: '<svg viewBox="0 0 250 50" width="250"><circle cx="20" cy="25" r="6" fill="#3b82f6"/><circle cx="35" cy="25" r="6" fill="#3b82f6"/><circle cx="50" cy="25" r="6" fill="#3b82f6"/><text x="35" y="45" text-anchor="middle" font-size="9">P1: 3</text><circle cx="90" cy="25" r="6" fill="#3b82f6"/><circle cx="105" cy="25" r="6" fill="#3b82f6"/><circle cx="120" cy="25" r="6" fill="#3b82f6"/><circle cx="135" cy="25" r="6" fill="#3b82f6"/><circle cx="150" cy="25" r="6" fill="#3b82f6"/><text x="120" y="45" text-anchor="middle" font-size="9">P2: 5</text><text x="200" y="25" font-size="12" fill="#22c55e">+2 each time</text></svg>',
                        steps: [
                            "Count: 3, 5, 7...",
                            "Pattern: adding <strong>2</strong> each time",
                            "Pattern 4: 7 + 2 = <strong>9 dots</strong>"
                        ],
                        answer: "9 dots"
                    }
                ],
                tip: "Always count carefully and look for the change between terms!"
            },
            2: {
                title: "Extending Visual Patterns",
                band: "Foundation",
                description: "Draw the next pattern in a sequence by understanding how the pattern grows or changes.",
                keyPoints: [
                    "Identify HOW the pattern grows (adding rows, columns, etc.)",
                    "Draw the next pattern following the same rule",
                    "Count to verify your answer"
                ],
                examples: [
                    {
                        question: "Squares form an L-shape: P1=2, P2=3, P3=4. Draw and describe P4.",
                        visual: '<svg viewBox="0 0 200 60" width="200"><rect x="10" y="30" width="15" height="15" fill="#8b5cf6" stroke="#6b7280"/><rect x="10" y="15" width="15" height="15" fill="#8b5cf6" stroke="#6b7280"/><rect x="60" y="30" width="15" height="15" fill="#8b5cf6" stroke="#6b7280"/><rect x="60" y="15" width="15" height="15" fill="#8b5cf6" stroke="#6b7280"/><rect x="75" y="30" width="15" height="15" fill="#8b5cf6" stroke="#6b7280"/><text x="130" y="35" font-size="11" fill="#374151">+1 square each time</text></svg>',
                        steps: [
                            "Pattern grows by adding 1 square",
                            "P4 = P3 + 1 = 4 + 1 = <strong>5 squares</strong>",
                            "Draw the L-shape with 5 squares"
                        ],
                        answer: "5 squares in L-shape"
                    }
                ],
                tip: "Describe the growth rule before drawing!"
            },
            3: {
                title: "Finding Differences",
                band: "Foundation",
                description: "Find the difference between consecutive terms. This tells you how much the sequence increases or decreases each step.",
                keyPoints: [
                    "<strong>Difference</strong> = next term − current term",
                    "A constant difference means it's a <strong>linear sequence</strong>",
                    "Write differences between each pair of terms"
                ],
                examples: [
                    {
                        question: "Find the differences: 4, 7, 10, 13, 16",
                        visual: '<svg viewBox="0 0 280 50" width="280"><text x="20" y="20" font-size="14">4</text><text x="60" y="20" font-size="14">7</text><text x="100" y="20" font-size="14">10</text><text x="145" y="20" font-size="14">13</text><text x="190" y="20" font-size="14">16</text><text x="40" y="40" font-size="11" fill="#22c55e">+3</text><text x="80" y="40" font-size="11" fill="#22c55e">+3</text><text x="122" y="40" font-size="11" fill="#22c55e">+3</text><text x="167" y="40" font-size="11" fill="#22c55e">+3</text></svg>',
                        steps: [
                            "7−4=3, 10−7=3, 13−10=3, 16−13=3",
                            "Constant difference = <strong>+3</strong>",
                            "This is a linear sequence"
                        ],
                        answer: "Common difference = 3"
                    }
                ],
                tip: "Same difference every time = linear sequence!"
            },
            4: {
                title: "Linear Sequences - Counting On",
                band: "Ordinary",
                description: "Continue a sequence by repeatedly adding (or subtracting) the common difference.",
                keyPoints: [
                    "Find the common difference first",
                    "Add (or subtract) it to get the next term",
                    "Check your answer by verifying the pattern"
                ],
                examples: [
                    {
                        question: "Find the next two terms: 5, 8, 11, 14, __, __",
                        visual: '<svg viewBox="0 0 280 50" width="280"><text x="10" y="25" font-size="12" fill="#374151">5, 8, 11, 14, <tspan fill="#22c55e" font-weight="bold">17, 20</tspan></text><text x="10" y="45" font-size="11" fill="#6b7280">Common difference: +3</text></svg>',
                        steps: [
                            "Difference: 8−5=3, 11−8=3, 14−11=3",
                            "Next: 14+3=<strong>17</strong>",
                            "After that: 17+3=<strong>20</strong>"
                        ],
                        answer: "17, 20"
                    }
                ],
                tip: "Find the difference, then keep adding!"
            },
            5: {
                title: "Common Difference",
                band: "Ordinary",
                description: "The common difference (d) is what you add each time. It can be positive (increasing) or negative (decreasing).",
                keyPoints: [
                    "Common difference <strong>d = T₂ − T₁</strong>",
                    "Positive d → sequence increases",
                    "Negative d → sequence decreases"
                ],
                examples: [
                    {
                        question: "Find the common difference: 20, 17, 14, 11, 8",
                        visual: '<svg viewBox="0 0 280 50" width="280"><text x="10" y="20" font-size="12" fill="#374151">20, 17, 14, 11, 8</text><text x="10" y="40" font-size="11" fill="#ef4444">−3, −3, −3, −3 (decreasing)</text></svg>',
                        steps: [
                            "17−20 = <strong>−3</strong>",
                            "Check: 14−17=−3, 11−14=−3, 8−11=−3",
                            "Common difference = <strong>−3</strong>"
                        ],
                        answer: "d = −3"
                    }
                ],
                tip: "Negative difference means the sequence goes down!"
            },
            6: {
                title: "Sequence Tables",
                band: "Ordinary",
                description: "Fill in tables showing term number (n) and term value. This helps you spot the relationship between position and value.",
                keyPoints: [
                    "n = position (1st, 2nd, 3rd...)",
                    "Tₙ = value of the nth term",
                    "Look for the pattern: Tₙ = something × n + something"
                ],
                examples: [
                    {
                        question: "Complete: n=1→3, n=2→5, n=3→7, n=4→?",
                        visual: '<svg viewBox="0 0 250 60" width="250"><text x="10" y="20" font-size="11" fill="#374151">n: 1, 2, 3, 4</text><text x="10" y="40" font-size="11" fill="#374151">T: 3, 5, 7, <tspan fill="#22c55e" font-weight="bold">9</tspan></text><text x="10" y="55" font-size="10" fill="#6b7280">Pattern: +2 each time</text></svg>',
                        steps: [
                            "Differences: 5−3=2, 7−5=2",
                            "Pattern: add 2 each time",
                            "T₄ = 7 + 2 = <strong>9</strong>"
                        ],
                        answer: "T₄ = 9"
                    }
                ],
                tip: "Tables make patterns easier to spot!"
            },
            7: {
                title: "Linear vs Non-Linear",
                band: "Ordinary",
                description: "Linear sequences have a constant difference. Non-linear sequences (quadratic, geometric) have changing differences.",
                keyPoints: [
                    "<strong>Linear</strong>: constant first difference",
                    "<strong>Quadratic</strong>: constant second difference",
                    "<strong>Geometric</strong>: multiply by same number each time"
                ],
                examples: [
                    {
                        question: "Is 1, 4, 9, 16, 25 linear or non-linear?",
                        visual: '<svg viewBox="0 0 280 60" width="280"><text x="10" y="20" font-size="11" fill="#374151">Sequence: 1, 4, 9, 16, 25</text><text x="10" y="35" font-size="10" fill="#6b7280">1st diff: 3, 5, 7, 9 (not constant!)</text><text x="10" y="50" font-size="10" fill="#22c55e">2nd diff: 2, 2, 2 (constant) → Quadratic</text></svg>',
                        steps: [
                            "1st differences: 3, 5, 7, 9 - not constant!",
                            "2nd differences: 2, 2, 2 - constant!",
                            "This is <strong>non-linear (quadratic)</strong>"
                        ],
                        answer: "Non-linear (quadratic: n²)"
                    }
                ],
                tip: "Check 1st differences first. Not constant? Try 2nd differences."
            },
            8: {
                title: "Using nth Term Formula",
                band: "Higher",
                description: "Use the formula Tₙ = dn + c to find any term directly without counting through all previous terms.",
                keyPoints: [
                    "<strong>Tₙ = dn + c</strong> where d is common difference",
                    "Substitute n to find any term",
                    "T₁₀₀ means put n=100 into the formula"
                ],
                examples: [
                    {
                        question: "Tₙ = 3n + 2. Find T₁₀.",
                        visual: '<svg viewBox="0 0 250 50" width="250"><text x="10" y="20" font-size="12" fill="#374151">Tₙ = 3n + 2</text><text x="10" y="40" font-size="12" fill="#22c55e">T₁₀ = 3(10) + 2 = 30 + 2 = 32</text></svg>',
                        steps: [
                            "Formula: Tₙ = 3n + 2",
                            "Substitute n = 10",
                            "T₁₀ = 3(10) + 2 = <strong>32</strong>"
                        ],
                        answer: "T₁₀ = 32"
                    }
                ],
                tip: "Just substitute the term number for n!"
            },
            9: {
                title: "Finding nth Term Formula",
                band: "Higher",
                description: "Work out the formula Tₙ = dn + c from a sequence. Find d (common difference), then find c.",
                keyPoints: [
                    "d = common difference (coefficient of n)",
                    "c = T₁ − d (the adjustment)",
                    "Formula: <strong>Tₙ = dn + c</strong>"
                ],
                examples: [
                    {
                        question: "Find formula for: 5, 8, 11, 14...",
                        visual: '<svg viewBox="0 0 280 60" width="280"><text x="10" y="20" font-size="11" fill="#374151">d = 8−5 = 3, so Tₙ = 3n + c</text><text x="10" y="40" font-size="11" fill="#374151">T₁ = 5: 3(1) + c = 5, so c = 2</text><text x="10" y="55" font-size="11" fill="#22c55e" font-weight="bold">Tₙ = 3n + 2</text></svg>',
                        steps: [
                            "d = 8−5 = <strong>3</strong>",
                            "c = T₁ − d = 5 − 3 = <strong>2</strong>",
                            "Formula: <strong>Tₙ = 3n + 2</strong>"
                        ],
                        answer: "Tₙ = 3n + 2"
                    }
                ],
                tip: "d = difference, c = first term minus d"
            },
            10: {
                title: "Quadratic Sequences",
                band: "Higher",
                description: "Quadratic sequences have formula Tₙ = an² + bn + c. The second difference tells you the value of 'a'.",
                keyPoints: [
                    "2nd difference = 2a, so <strong>a = (2nd diff) ÷ 2</strong>",
                    "Subtract an² from sequence, then find linear part",
                    "SEC asks to identify quadratic patterns"
                ],
                examples: [
                    {
                        question: "Next two terms: 1, 4, 9, 16, __, __",
                        visual: '<svg viewBox="0 0 250 50" width="250"><text x="10" y="20" font-size="11" fill="#374151">1, 4, 9, 16... (these are 1², 2², 3², 4²)</text><text x="10" y="40" font-size="11" fill="#22c55e">Next: 5² = 25, 6² = 36</text></svg>',
                        steps: [
                            "Pattern: 1², 2², 3², 4²...",
                            "Next: 5² = <strong>25</strong>",
                            "After: 6² = <strong>36</strong>"
                        ],
                        answer: "25, 36"
                    }
                ],
                tip: "Square numbers: 1, 4, 9, 16, 25, 36..."
            },
            11: {
                title: "Geometric Sequences",
                band: "Higher",
                description: "Geometric sequences multiply by the same number (common ratio) each time instead of adding.",
                keyPoints: [
                    "Common ratio <strong>r = T₂ ÷ T₁</strong>",
                    "Each term = previous term × r",
                    "Tₙ = a × r^(n-1) where a is first term"
                ],
                examples: [
                    {
                        question: "Next two terms: 3, 6, 12, 24, __, __",
                        visual: '<svg viewBox="0 0 280 50" width="280"><text x="10" y="20" font-size="12" fill="#374151">3, 6, 12, 24, <tspan fill="#22c55e" font-weight="bold">48, 96</tspan></text><text x="10" y="40" font-size="11" fill="#6b7280">×2 each time (doubling)</text></svg>',
                        steps: [
                            "Ratio: 6÷3=2, 12÷6=2, 24÷12=2",
                            "Common ratio r = <strong>2</strong>",
                            "Next: 24×2=<strong>48</strong>, then 48×2=<strong>96</strong>"
                        ],
                        answer: "48, 96"
                    }
                ],
                tip: "Multiply (not add) by the common ratio!"
            },
            12: {
                title: "Problem Solving",
                band: "Mastery",
                description: "Apply sequence skills to real-world problems. Find specific terms, determine if a number is in a sequence, and solve pattern puzzles.",
                keyPoints: [
                    "To check if x is in sequence: solve Tₙ = x for n",
                    "n must be a positive whole number",
                    "Connect patterns to real situations"
                ],
                examples: [
                    {
                        question: "Tₙ = 4n + 1. Is 50 a term in the sequence?",
                        visual: '<svg viewBox="0 0 280 50" width="280"><text x="10" y="20" font-size="11" fill="#374151">4n + 1 = 50</text><text x="10" y="35" font-size="11" fill="#374151">4n = 49</text><text x="10" y="50" font-size="11" fill="#ef4444">n = 12.25 (not whole!) → Not in sequence</text></svg>',
                        steps: [
                            "Set 4n + 1 = 50",
                            "4n = 49, n = 12.25",
                            "n is not a whole number → <strong>No</strong>"
                        ],
                        answer: "No - 50 is not in the sequence"
                    }
                ],
                tip: "🏆 You've mastered Patterns! n must be a positive integer."
            }
        };
        
        // Functions Help Content - 12 Levels
        const functionsHelpContent = {
            1: {
                title: "Understanding Function Notation",
                band: "Foundation",
                description: "A function is a rule that takes an input and produces an output. f(x) means 'the function f, applied to x'.",
                keyPoints: [
                    "<strong>f(x)</strong> is read as 'f of x'",
                    "x is the <strong>input</strong>, f(x) is the <strong>output</strong>",
                    "The function tells you what to do to the input"
                ],
                examples: [
                    {
                        question: "If f(x) = x + 3, what does f(5) mean?",
                        visual: '<svg viewBox="0 0 250 60" width="250"><rect x="10" y="20" width="50" height="30" fill="#bfdbfe" stroke="#3b82f6" rx="5"/><text x="35" y="40" text-anchor="middle" font-size="12">5</text><text x="80" y="40" font-size="14">→</text><rect x="100" y="15" width="80" height="40" fill="#fef3c7" stroke="#f59e0b" rx="5"/><text x="140" y="40" text-anchor="middle" font-size="11">f(x) = x + 3</text><text x="200" y="40" font-size="14">→</text><rect x="220" y="20" width="50" height="30" fill="#bbf7d0" stroke="#22c55e" rx="5"/><text x="245" y="40" text-anchor="middle" font-size="12">8</text></svg>',
                        steps: [
                            "f(5) means 'put 5 into function f'",
                            "f(x) = x + 3, so replace x with 5",
                            "f(5) = 5 + 3 = <strong>8</strong>"
                        ],
                        answer: "f(5) = 8"
                    }
                ],
                tip: "Think of a function as a machine: input goes in, output comes out!"
            },
            2: {
                title: "Evaluating Simple Functions",
                band: "Foundation",
                description: "To evaluate a function, substitute the given value for x and calculate the result.",
                keyPoints: [
                    "Replace x with the given number",
                    "Use brackets when substituting",
                    "Follow order of operations (BOMDAS)"
                ],
                examples: [
                    {
                        question: "f(x) = x − 4. Find f(9).",
                        visual: '<svg viewBox="0 0 200 50" width="200"><text x="10" y="20" font-size="12" fill="#374151">f(x) = x − 4</text><text x="10" y="40" font-size="12" fill="#22c55e">f(9) = 9 − 4 = 5</text></svg>',
                        steps: [
                            "f(x) = x − 4",
                            "f(9) = (9) − 4",
                            "f(9) = <strong>5</strong>"
                        ],
                        answer: "f(9) = 5"
                    }
                ],
                tip: "Just swap x for the number and calculate!"
            },
            3: {
                title: "Evaluating with Multiplication",
                band: "Foundation",
                description: "When the function involves multiplication (like 2x), remember that 2x means 2 × x.",
                keyPoints: [
                    "<strong>2x means 2 × x</strong>",
                    "Substitute first, then multiply",
                    "Be careful with negative numbers"
                ],
                examples: [
                    {
                        question: "f(x) = 3x. Find f(4).",
                        visual: '<svg viewBox="0 0 200 50" width="200"><text x="10" y="20" font-size="12" fill="#374151">f(x) = 3x means 3 × x</text><text x="10" y="40" font-size="12" fill="#22c55e">f(4) = 3 × 4 = 12</text></svg>',
                        steps: [
                            "f(x) = 3x means 3 times x",
                            "f(4) = 3 × 4",
                            "f(4) = <strong>12</strong>"
                        ],
                        answer: "f(4) = 12"
                    }
                ],
                tip: "No sign between number and x means multiply!"
            },
            4: {
                title: "Linear Functions f(x) = ax + b",
                band: "Ordinary",
                description: "Linear functions have the form f(x) = ax + b. They give a straight line when graphed. SEC commonly uses this form!",
                keyPoints: [
                    "f(x) = ax + b is a <strong>linear function</strong>",
                    "a is the <strong>slope</strong> (rate of change)",
                    "b is the <strong>y-intercept</strong> (starting value)"
                ],
                examples: [
                    {
                        question: "f(x) = 2x − 1. Find f(3).",
                        visual: '<svg viewBox="0 0 220 50" width="220"><text x="10" y="20" font-size="12" fill="#374151">f(x) = 2x − 1</text><text x="10" y="40" font-size="12" fill="#22c55e">f(3) = 2(3) − 1 = 6 − 1 = 5</text></svg>',
                        steps: [
                            "f(3) = 2(3) − 1",
                            "= 6 − 1",
                            "= <strong>5</strong>"
                        ],
                        answer: "f(3) = 5"
                    }
                ],
                tip: "This is the most common SEC function type!"
            },
            5: {
                title: "Finding Input from Output",
                band: "Ordinary",
                description: "Sometimes you know f(x) and need to find x. Set up an equation and solve it.",
                keyPoints: [
                    "Given f(x) = value, solve for x",
                    "Replace f(x) with the output value",
                    "Solve the equation step by step"
                ],
                examples: [
                    {
                        question: "f(x) = 2x − 1. If f(x) = 9, find x.",
                        visual: '<svg viewBox="0 0 250 60" width="250"><text x="10" y="20" font-size="11" fill="#374151">2x − 1 = 9</text><text x="10" y="40" font-size="11" fill="#374151">2x = 10</text><text x="10" y="55" font-size="11" fill="#22c55e">x = 5</text></svg>',
                        steps: [
                            "Set 2x − 1 = 9",
                            "Add 1: 2x = 10",
                            "Divide by 2: x = <strong>5</strong>"
                        ],
                        answer: "x = 5"
                    }
                ],
                tip: "Working backwards: output → equation → input"
            },
            6: {
                title: "Completing Function Tables",
                band: "Ordinary",
                description: "Fill in tables of x and f(x) values. This helps you plot the function graph.",
                keyPoints: [
                    "Substitute each x value into the function",
                    "Calculate f(x) for each",
                    "Check your pattern is consistent"
                ],
                examples: [
                    {
                        question: "f(x) = x + 2. Complete: x = −1, 0, 1, 2",
                        visual: '<svg viewBox="0 0 280 60" width="280"><text x="10" y="20" font-size="11" fill="#374151">x: −1, 0, 1, 2</text><text x="10" y="40" font-size="11" fill="#22c55e">f(x): 1, 2, 3, 4</text><text x="10" y="55" font-size="10" fill="#6b7280">(each f(x) = x + 2)</text></svg>',
                        steps: [
                            "f(−1) = −1 + 2 = 1",
                            "f(0) = 0 + 2 = 2",
                            "f(1) = 1 + 2 = 3, f(2) = 2 + 2 = 4"
                        ],
                        answer: "f(x) values: 1, 2, 3, 4"
                    }
                ],
                tip: "Tables prepare you for graphing!"
            },
            7: {
                title: "Finding Constants",
                band: "Higher",
                description: "If you're given a function with unknown constant (like k) and one point, you can find the constant. SEC 2023 HL Q11(c) tests this!",
                keyPoints: [
                    "Substitute the known point into the function",
                    "Solve for the unknown constant",
                    "Verify by substituting back"
                ],
                examples: [
                    {
                        question: "g(x) = 3x + k. If g(2) = 11, find k.",
                        visual: '<svg viewBox="0 0 250 60" width="250"><text x="10" y="20" font-size="11" fill="#374151">g(2) = 3(2) + k = 11</text><text x="10" y="40" font-size="11" fill="#374151">6 + k = 11</text><text x="10" y="55" font-size="11" fill="#22c55e">k = 5</text></svg>',
                        steps: [
                            "g(2) = 3(2) + k = 11",
                            "6 + k = 11",
                            "k = <strong>5</strong>"
                        ],
                        answer: "k = 5"
                    }
                ],
                tip: "One point + function with unknown = solve for unknown!"
            },
            8: {
                title: "Reading Function Graphs",
                band: "Higher",
                description: "Read values from function graphs. Find f(x) given x, or find x given f(x).",
                keyPoints: [
                    "To find f(a): go to x=a, read y-value",
                    "To solve f(x)=b: go to y=b, read x-value",
                    "Use gridlines for accuracy"
                ],
                examples: [
                    {
                        question: "From a graph, if the line passes through (3, 7), what is f(3)?",
                        visual: '<svg viewBox="0 0 200 80" width="200"><line x1="20" y1="60" x2="180" y2="60" stroke="#6b7280"/><line x1="40" y1="10" x2="40" y2="70" stroke="#6b7280"/><line x1="40" y1="60" x2="140" y2="20" stroke="#3b82f6" stroke-width="2"/><circle cx="100" cy="40" r="4" fill="#ef4444"/><text x="105" y="38" font-size="10" fill="#374151">(3,7)</text></svg>',
                        steps: [
                            "Point (3, 7) means when x=3, y=7",
                            "f(3) = the y-value at x=3",
                            "f(3) = <strong>7</strong>"
                        ],
                        answer: "f(3) = 7"
                    }
                ],
                tip: "x along the corridor, y up the stairs!"
            },
            9: {
                title: "Quadratic Functions",
                band: "Higher",
                description: "Quadratic functions have x² terms. They create curved (parabola) graphs, not straight lines.",
                keyPoints: [
                    "f(x) = ax² + bx + c is quadratic",
                    "Remember: x² means x × x",
                    "Negative × negative = positive!"
                ],
                examples: [
                    {
                        question: "f(x) = x² − 3. Find f(4).",
                        visual: '<svg viewBox="0 0 220 50" width="220"><text x="10" y="20" font-size="12" fill="#374151">f(x) = x² − 3</text><text x="10" y="40" font-size="12" fill="#22c55e">f(4) = 4² − 3 = 16 − 3 = 13</text></svg>',
                        steps: [
                            "f(4) = (4)² − 3",
                            "= 16 − 3",
                            "= <strong>13</strong>"
                        ],
                        answer: "f(4) = 13"
                    }
                ],
                tip: "Square first, then do the rest!"
            },
            10: {
                title: "Composite Functions",
                band: "Higher",
                description: "A composite function applies one function, then another. f(g(x)) means 'do g first, then f'.",
                keyPoints: [
                    "<strong>f(g(x))</strong>: apply g first, then f",
                    "Work from the inside out",
                    "The output of g becomes input of f"
                ],
                examples: [
                    {
                        question: "f(x) = 2x, g(x) = x + 3. Find f(g(2)).",
                        visual: '<svg viewBox="0 0 280 50" width="280"><text x="10" y="20" font-size="11" fill="#374151">First: g(2) = 2 + 3 = 5</text><text x="10" y="40" font-size="11" fill="#22c55e">Then: f(5) = 2(5) = 10</text></svg>',
                        steps: [
                            "First find g(2) = 2 + 3 = <strong>5</strong>",
                            "Then find f(5) = 2(5) = <strong>10</strong>",
                            "So f(g(2)) = <strong>10</strong>"
                        ],
                        answer: "f(g(2)) = 10"
                    }
                ],
                tip: "Inside function first, outside function second!"
            },
            11: {
                title: "Real-World Graphs",
                band: "Application",
                description: "Interpret graphs that represent real situations like temperature, distance, or cost over time. SEC 2025 HL Q9 uses this!",
                keyPoints: [
                    "Increasing section = going up",
                    "Decreasing section = going down",
                    "Horizontal = staying constant"
                ],
                examples: [
                    {
                        question: "A temperature graph is horizontal from x=2 to x=5. What does this mean?",
                        visual: '<svg viewBox="0 0 200 60" width="200"><line x1="20" y1="50" x2="180" y2="50" stroke="#6b7280"/><line x1="20" y1="10" x2="20" y2="50" stroke="#6b7280"/><polyline points="20,40 50,30 80,30 140,30 170,20" fill="none" stroke="#3b82f6" stroke-width="2"/><text x="80" y="45" font-size="9" fill="#22c55e">constant here</text></svg>',
                        steps: [
                            "Horizontal line = no change in y",
                            "Temperature stayed the same",
                            "From x=2 to x=5: <strong>constant temperature</strong>"
                        ],
                        answer: "Temperature was constant"
                    }
                ],
                tip: "Connect graph shape to real meaning!"
            },
            12: {
                title: "Problem Solving",
                band: "Mastery",
                description: "Complex problems combining multiple function skills. Match functions to graph sections, find equations, solve real problems.",
                keyPoints: [
                    "Break complex problems into steps",
                    "Identify which function skill is needed",
                    "Check your answer makes sense in context"
                ],
                examples: [
                    {
                        question: "A graph rises with slope 3 from (0,2). What function matches?",
                        visual: '<svg viewBox="0 0 250 50" width="250"><text x="10" y="20" font-size="11" fill="#374151">Slope = 3, y-intercept = 2</text><text x="10" y="40" font-size="11" fill="#22c55e">f(x) = 3x + 2</text></svg>',
                        steps: [
                            "Slope (m) = 3",
                            "y-intercept (c) = 2",
                            "Function: <strong>f(x) = 3x + 2</strong>"
                        ],
                        answer: "f(x) = 3x + 2"
                    }
                ],
                tip: "🏆 You've mastered Functions! Slope and intercept define a linear function."
            }
        };
        
        // Area, Perimeter & Volume Help Content - 12 Levels
        const areaHelpContent = {
            1: {
                title: "Counting Squares for Area",
                band: "Foundation",
                description: "Area measures the space inside a shape. For shapes on a grid, count the squares inside.",
                keyPoints: [
                    "<strong>Area</strong> = space inside a shape",
                    "Count complete squares",
                    "Units are <strong>square units</strong> (cm², m²)"
                ],
                examples: [
                    {
                        question: "A rectangle covers 12 squares on a grid. What is its area?",
                        visual: '<svg viewBox="0 0 200 80" width="200"><rect x="10" y="10" width="120" height="60" fill="#bfdbfe" stroke="#3b82f6"/><line x1="40" y1="10" x2="40" y2="70" stroke="#93c5fd"/><line x1="70" y1="10" x2="70" y2="70" stroke="#93c5fd"/><line x1="100" y1="10" x2="100" y2="70" stroke="#93c5fd"/><line x1="10" y1="40" x2="130" y2="40" stroke="#93c5fd"/><text x="70" y="45" text-anchor="middle" font-size="12" fill="#1e40af">12 squares</text></svg>',
                        steps: [
                            "Count all the squares inside",
                            "12 complete squares",
                            "Area = <strong>12 square units</strong>"
                        ],
                        answer: "12 square units"
                    }
                ],
                tip: "Count carefully - don't miss any squares!"
            },
            2: {
                title: "Perimeter of Rectangles",
                band: "Foundation",
                description: "Perimeter is the total distance around the outside of a shape. Add all the sides.",
                keyPoints: [
                    "<strong>Perimeter</strong> = distance around the edge",
                    "Rectangle: P = 2 × length + 2 × width",
                    "Or P = 2(length + width)"
                ],
                examples: [
                    {
                        question: "Rectangle: length 8 cm, width 5 cm. Find perimeter.",
                        visual: '<svg viewBox="0 0 200 80" width="200"><rect x="20" y="15" width="120" height="50" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/><text x="80" y="10" text-anchor="middle" font-size="10" fill="#92400e">8 cm</text><text x="150" y="45" font-size="10" fill="#92400e">5 cm</text></svg>',
                        steps: [
                            "P = 2 × length + 2 × width",
                            "P = 2 × 8 + 2 × 5",
                            "P = 16 + 10 = <strong>26 cm</strong>"
                        ],
                        answer: "Perimeter = 26 cm"
                    }
                ],
                tip: "Add all four sides, or use P = 2(l + w)"
            },
            3: {
                title: "Area of Rectangles",
                band: "Foundation",
                description: "For rectangles, multiply length by width. This is much faster than counting squares!",
                keyPoints: [
                    "<strong>Area = length × width</strong>",
                    "Make sure both measurements use same units",
                    "Answer in square units (cm², m²)"
                ],
                examples: [
                    {
                        question: "Rectangle: 7 cm by 4 cm. Find area.",
                        visual: '<svg viewBox="0 0 200 80" width="200"><rect x="20" y="15" width="105" height="50" fill="#bbf7d0" stroke="#22c55e" stroke-width="2"/><text x="72" y="10" text-anchor="middle" font-size="10" fill="#166534">7 cm</text><text x="135" y="45" font-size="10" fill="#166534">4 cm</text><text x="72" y="45" text-anchor="middle" font-size="11" fill="#166534">Area = 28 cm²</text></svg>',
                        steps: [
                            "Area = length × width",
                            "Area = 7 × 4",
                            "Area = <strong>28 cm²</strong>"
                        ],
                        answer: "28 cm²"
                    }
                ],
                tip: "Length × Width - simple!"
            },
            4: {
                title: "Area of Triangles",
                band: "Ordinary",
                description: "A triangle's area is half the base times the height. The height must be perpendicular to the base.",
                keyPoints: [
                    "<strong>Area = ½ × base × height</strong>",
                    "Height is perpendicular (at right angle) to base",
                    "A triangle is half a rectangle"
                ],
                examples: [
                    {
                        question: "Triangle: base 12 cm, height 8 cm. Find area.",
                        visual: '<svg viewBox="0 0 200 80" width="200"><polygon points="20,70 140,70 80,15" fill="#ddd6fe" stroke="#8b5cf6" stroke-width="2"/><line x1="80" y1="70" x2="80" y2="15" stroke="#8b5cf6" stroke-dasharray="4"/><text x="80" y="80" text-anchor="middle" font-size="10" fill="#5b21b6">12 cm</text><text x="90" y="45" font-size="10" fill="#5b21b6">8 cm</text></svg>',
                        steps: [
                            "Area = ½ × base × height",
                            "Area = ½ × 12 × 8",
                            "Area = <strong>48 cm²</strong>"
                        ],
                        answer: "48 cm²"
                    }
                ],
                tip: "Half of base × height (triangle = half rectangle)"
            },
            5: {
                title: "Area of Circles",
                band: "Ordinary",
                description: "Circle area uses π (pi ≈ 3.14). The formula involves the radius squared.",
                keyPoints: [
                    "<strong>Area = πr²</strong>",
                    "r = radius (distance from centre to edge)",
                    "π ≈ 3.14 or use π button on calculator"
                ],
                examples: [
                    {
                        question: "Circle with radius 7 cm. Find area to nearest cm².",
                        visual: '<svg viewBox="0 0 150 80" width="150"><circle cx="75" cy="40" r="35" fill="#fecaca" stroke="#ef4444" stroke-width="2"/><line x1="75" y1="40" x2="110" y2="40" stroke="#ef4444" stroke-width="2"/><text x="92" y="35" font-size="10" fill="#991b1b">7 cm</text></svg>',
                        steps: [
                            "Area = πr² = π × 7²",
                            "= π × 49 = 153.94...",
                            "≈ <strong>154 cm²</strong>"
                        ],
                        answer: "≈ 154 cm²"
                    }
                ],
                tip: "πr² - pi times radius squared!"
            },
            6: {
                title: "Circumference of Circles",
                band: "Ordinary",
                description: "Circumference is the perimeter (distance around) a circle. It equals π times the diameter.",
                keyPoints: [
                    "<strong>Circumference = πd = 2πr</strong>",
                    "d = diameter (across the circle through centre)",
                    "r = radius (d = 2r)"
                ],
                examples: [
                    {
                        question: "Circle with diameter 10 cm. Find circumference.",
                        visual: '<svg viewBox="0 0 150 80" width="150"><circle cx="75" cy="40" r="35" fill="none" stroke="#3b82f6" stroke-width="2"/><line x1="40" y1="40" x2="110" y2="40" stroke="#3b82f6" stroke-width="2"/><text x="75" y="35" text-anchor="middle" font-size="10" fill="#1e40af">10 cm</text></svg>',
                        steps: [
                            "C = πd = π × 10",
                            "= 31.4159...",
                            "≈ <strong>31.4 cm</strong>"
                        ],
                        answer: "≈ 31.4 cm"
                    }
                ],
                tip: "πd for diameter, 2πr for radius"
            },
            7: {
                title: "Composite Shapes - Area",
                band: "Higher",
                description: "Composite shapes are made of simpler shapes. Break them apart, find each area, then add (or subtract).",
                keyPoints: [
                    "Split into rectangles, triangles, circles, etc.",
                    "Find each area separately",
                    "Add areas together (or subtract for holes)"
                ],
                examples: [
                    {
                        question: "L-shape: 10×6 rectangle with 4×3 cut from corner. Find area.",
                        visual: '<svg viewBox="0 0 200 80" width="200"><path d="M10,10 L100,10 L100,40 L55,40 L55,70 L10,70 Z" fill="#a5f3fc" stroke="#0891b2" stroke-width="2"/><text x="55" y="8" font-size="9" fill="#0e7490">10</text><text x="105" y="30" font-size="9" fill="#0e7490">6</text></svg>',
                        steps: [
                            "Full rectangle: 10 × 6 = 60",
                            "Cut out: 4 × 3 = 12",
                            "Area = 60 − 12 = <strong>48 cm²</strong>"
                        ],
                        answer: "48 cm²"
                    }
                ],
                tip: "Break it down, calculate each part, combine!"
            },
            8: {
                title: "Volume of Cuboids",
                band: "Higher",
                description: "Volume is the space inside a 3D shape. For cuboids (boxes), multiply length × width × height.",
                keyPoints: [
                    "<strong>Volume = length × width × height</strong>",
                    "Units are <strong>cubic</strong> (cm³, m³)",
                    "Cuboid = rectangular box shape"
                ],
                examples: [
                    {
                        question: "Box: 8 cm × 5 cm × 3 cm. Find volume.",
                        visual: '<svg viewBox="0 0 200 80" width="200"><path d="M30,60 L30,25 L80,10 L130,25 L130,60 L80,75 Z" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/><path d="M30,25 L80,40 L130,25" fill="none" stroke="#f59e0b"/><path d="M80,40 L80,75" stroke="#f59e0b"/><text x="55" y="75" font-size="9" fill="#92400e">8</text><text x="135" y="45" font-size="9" fill="#92400e">3</text><text x="105" y="15" font-size="9" fill="#92400e">5</text></svg>',
                        steps: [
                            "V = length × width × height",
                            "V = 8 × 5 × 3",
                            "V = <strong>120 cm³</strong>"
                        ],
                        answer: "120 cm³"
                    }
                ],
                tip: "l × w × h - three dimensions for 3D!"
            },
            9: {
                title: "Volume of Cylinders",
                band: "Higher",
                description: "A cylinder is like a circular prism. Its volume is the area of the circular base times the height.",
                keyPoints: [
                    "<strong>Volume = πr²h</strong>",
                    "πr² is the circular base area",
                    "h is the height (length of cylinder)"
                ],
                examples: [
                    {
                        question: "Cylinder: radius 4 cm, height 10 cm. Find volume.",
                        visual: '<svg viewBox="0 0 150 90" width="150"><ellipse cx="75" cy="20" rx="35" ry="12" fill="#bfdbfe" stroke="#3b82f6" stroke-width="2"/><line x1="40" y1="20" x2="40" y2="70" stroke="#3b82f6" stroke-width="2"/><line x1="110" y1="20" x2="110" y2="70" stroke="#3b82f6" stroke-width="2"/><ellipse cx="75" cy="70" rx="35" ry="12" fill="#bfdbfe" stroke="#3b82f6" stroke-width="2"/><text x="75" y="25" text-anchor="middle" font-size="9" fill="#1e40af">r=4</text><text x="120" y="50" font-size="9" fill="#1e40af">h=10</text></svg>',
                        steps: [
                            "V = πr²h = π × 4² × 10",
                            "= π × 16 × 10 = 160π",
                            "≈ <strong>502.7 cm³</strong>"
                        ],
                        answer: "≈ 502.7 cm³"
                    }
                ],
                tip: "Base area (πr²) times height!"
            },
            10: {
                title: "Surface Area",
                band: "Higher",
                description: "Surface area is the total area of all faces of a 3D shape. Think about wrapping the shape.",
                keyPoints: [
                    "Add areas of ALL faces",
                    "Cuboid: 2(lw + lh + wh)",
                    "Cylinder: 2πr² + 2πrh"
                ],
                examples: [
                    {
                        question: "Cube with side 5 cm. Find surface area.",
                        visual: '<svg viewBox="0 0 150 80" width="150"><path d="M30,55 L30,25 L60,10 L90,25 L90,55 L60,70 Z" fill="#d1fae5" stroke="#22c55e" stroke-width="2"/><path d="M30,25 L60,40 L90,25" fill="none" stroke="#22c55e"/><path d="M60,40 L60,70" stroke="#22c55e"/><text x="60" y="80" font-size="9" fill="#166534">5 cm</text></svg>',
                        steps: [
                            "Cube has 6 identical square faces",
                            "Each face = 5 × 5 = 25 cm²",
                            "Total = 6 × 25 = <strong>150 cm²</strong>"
                        ],
                        answer: "150 cm²"
                    }
                ],
                tip: "Count all faces and add their areas!"
            },
            11: {
                title: "Tiles & Slabs Problems",
                band: "Application",
                description: "SEC frequently asks: How many tiles/slabs fit in an area? Divide the total area by one tile's area.",
                keyPoints: [
                    "Find total area to cover",
                    "Find area of one tile",
                    "Number of tiles = total area ÷ tile area"
                ],
                examples: [
                    {
                        question: "Floor: 5.6m × 4.2m. Tiles: 0.7m × 0.7m. How many tiles?",
                        visual: '<svg viewBox="0 0 250 60" width="250"><text x="10" y="20" font-size="10" fill="#374151">Floor = 5.6 × 4.2 = 23.52 m²</text><text x="10" y="40" font-size="10" fill="#374151">Tile = 0.7 × 0.7 = 0.49 m²</text><text x="10" y="55" font-size="10" fill="#22c55e">Tiles needed = 23.52 ÷ 0.49 = 48</text></svg>',
                        steps: [
                            "Floor area = 5.6 × 4.2 = 23.52 m²",
                            "Tile area = 0.7 × 0.7 = 0.49 m²",
                            "Tiles = 23.52 ÷ 0.49 = <strong>48 tiles</strong>"
                        ],
                        answer: "48 tiles"
                    }
                ],
                tip: "Total area ÷ one tile area = number of tiles"
            },
            12: {
                title: "Multi-step Problems",
                band: "Mastery",
                description: "Complex problems combining area, perimeter, volume, and real-world contexts like costs.",
                keyPoints: [
                    "Read carefully - identify all required steps",
                    "Work systematically through each part",
                    "Check units match and answer is sensible"
                ],
                examples: [
                    {
                        question: "Garden 8m × 6m, path 1m wide around edge. Find path area.",
                        visual: '<svg viewBox="0 0 250 60" width="250"><text x="10" y="20" font-size="10" fill="#374151">Outer: (8+2) × (6+2) = 80 m²</text><text x="10" y="35" font-size="10" fill="#374151">Inner: 8 × 6 = 48 m²</text><text x="10" y="50" font-size="10" fill="#22c55e">Path = 80 − 48 = 32 m²</text></svg>',
                        steps: [
                            "Outer rectangle: 10 × 8 = 80 m²",
                            "Inner (garden): 8 × 6 = 48 m²",
                            "Path area = 80 − 48 = <strong>32 m²</strong>"
                        ],
                        answer: "32 m²"
                    }
                ],
                tip: "🏆 You've mastered Area, Perimeter & Volume! Break complex problems into parts."
            }
        };
        
        // Solving Equations Help Content - 12 Levels
        const solvingEquationsHelpContent = {
            1: {
                title: "One-Step Equations: Add/Subtract",
                band: "Foundation",
                description: "Learn to solve equations where you add or subtract to find x. Whatever you do to one side, you must do to the other!",
                keyPoints: [
                    "An equation is like a <strong>balance</strong> - both sides must stay equal",
                    "To 'undo' addition, use <strong>subtraction</strong>",
                    "To 'undo' subtraction, use <strong>addition</strong>"
                ],
                examples: [
                    {
                        question: "Solve: x + 5 = 12",
                        visual: '<svg viewBox="0 0 250 50" width="250"><text x="10" y="20" font-size="12" fill="#374151">x + 5 = 12</text><text x="10" y="40" font-size="12" fill="#22c55e">x = 12 - 5 = 7</text></svg>',
                        steps: [
                            "We need to get x on its own",
                            "Subtract 5 from both sides",
                            "x = 12 - 5 = <strong>7</strong>"
                        ],
                        answer: "x = 7"
                    }
                ],
                tip: "Think: What's been done to x? Do the opposite to both sides!"
            },
            2: {
                title: "One-Step Equations: Multiply/Divide",
                band: "Foundation",
                description: "Solve equations involving multiplication or division. Use the inverse operation to isolate x.",
                keyPoints: [
                    "To 'undo' multiplication, use <strong>division</strong>",
                    "To 'undo' division, use <strong>multiplication</strong>",
                    "3x means 3 × x"
                ],
                examples: [
                    {
                        question: "Solve: 4x = 20",
                        visual: '<svg viewBox="0 0 250 50" width="250"><text x="10" y="20" font-size="12" fill="#374151">4x = 20</text><text x="10" y="40" font-size="12" fill="#22c55e">x = 20 ÷ 4 = 5</text></svg>',
                        steps: [
                            "4x means 4 times x",
                            "Divide both sides by 4",
                            "x = 20 ÷ 4 = <strong>5</strong>"
                        ],
                        answer: "x = 5"
                    }
                ],
                tip: "If x is multiplied, divide. If x is divided, multiply!"
            },
            3: {
                title: "Two-Step Equations",
                band: "Foundation",
                description: "These equations need two steps to solve. Deal with addition/subtraction first, then multiplication/division.",
                keyPoints: [
                    "Step 1: Add or subtract to isolate the x term",
                    "Step 2: Multiply or divide to find x",
                    "Always do the same to both sides"
                ],
                examples: [
                    {
                        question: "Solve: 3x + 4 = 19",
                        visual: '<svg viewBox="0 0 280 60" width="280"><text x="10" y="20" font-size="11" fill="#374151">3x + 4 = 19</text><text x="10" y="35" font-size="11" fill="#3b82f6">3x = 19 - 4 = 15</text><text x="10" y="50" font-size="11" fill="#22c55e">x = 15 ÷ 3 = 5</text></svg>',
                        steps: [
                            "Subtract 4 from both sides: 3x = 15",
                            "Divide both sides by 3: x = 5"
                        ],
                        answer: "x = 5"
                    }
                ],
                tip: "UNDO operations in reverse order: +/- first, then ×/÷"
            },
            4: {
                title: "Equations with Negatives",
                band: "Ordinary",
                description: "Handle equations with negative numbers. Remember the rules: negative × negative = positive.",
                keyPoints: [
                    "-x means -1 × x",
                    "Negative ÷ negative = <strong>positive</strong>",
                    "Be careful with signs when moving terms"
                ],
                examples: [
                    {
                        question: "Solve: -2x = 10",
                        visual: '<svg viewBox="0 0 250 50" width="250"><text x="10" y="20" font-size="12" fill="#374151">-2x = 10</text><text x="10" y="40" font-size="12" fill="#22c55e">x = 10 ÷ (-2) = -5</text></svg>',
                        steps: [
                            "Divide both sides by -2",
                            "10 ÷ (-2) = -5",
                            "x = <strong>-5</strong>"
                        ],
                        answer: "x = -5"
                    }
                ],
                tip: "Positive ÷ negative = negative!"
            },
            5: {
                title: "Variables on Both Sides",
                band: "Ordinary",
                description: "When x appears on both sides, collect all x terms on one side first. SEC commonly asks this type!",
                keyPoints: [
                    "Move all x terms to <strong>one side</strong>",
                    "Move all number terms to the <strong>other side</strong>",
                    "Then solve as normal"
                ],
                examples: [
                    {
                        question: "Solve: 5x + 3 = 2x + 12",
                        visual: '<svg viewBox="0 0 280 60" width="280"><text x="10" y="20" font-size="11" fill="#374151">5x + 3 = 2x + 12</text><text x="10" y="35" font-size="11" fill="#3b82f6">5x - 2x = 12 - 3</text><text x="10" y="50" font-size="11" fill="#22c55e">3x = 9, so x = 3</text></svg>',
                        steps: [
                            "Subtract 2x from both sides: 3x + 3 = 12",
                            "Subtract 3: 3x = 9",
                            "Divide by 3: x = <strong>3</strong>"
                        ],
                        answer: "x = 3"
                    }
                ],
                tip: "Get all x's on the side with MORE x's!"
            },
            6: {
                title: "Equations with Brackets",
                band: "Ordinary",
                description: "Expand brackets first, then collect like terms and solve. SEC 2024 OL Q7 uses this style!",
                keyPoints: [
                    "<strong>Expand</strong> brackets first: a(b + c) = ab + ac",
                    "Collect <strong>like terms</strong>",
                    "Then solve the equation"
                ],
                examples: [
                    {
                        question: "Solve: 3(x + 2) = 15",
                        visual: '<svg viewBox="0 0 280 60" width="280"><text x="10" y="20" font-size="11" fill="#374151">3(x + 2) = 15</text><text x="10" y="35" font-size="11" fill="#3b82f6">3x + 6 = 15</text><text x="10" y="50" font-size="11" fill="#22c55e">3x = 9, x = 3</text></svg>',
                        steps: [
                            "Expand: 3 × x + 3 × 2 = 3x + 6",
                            "So 3x + 6 = 15",
                            "3x = 9, x = <strong>3</strong>"
                        ],
                        answer: "x = 3"
                    }
                ],
                tip: "Multiply EVERYTHING inside the bracket!"
            },
            7: {
                title: "Equations with Fractions",
                band: "Higher",
                description: "Clear fractions by multiplying both sides by the denominator. This makes the equation easier to solve.",
                keyPoints: [
                    "Multiply both sides by the <strong>denominator</strong>",
                    "This 'clears' the fraction",
                    "Then solve as normal"
                ],
                examples: [
                    {
                        question: "Solve: x/4 + 3 = 7",
                        visual: '<svg viewBox="0 0 280 60" width="280"><text x="10" y="20" font-size="11" fill="#374151">x/4 + 3 = 7</text><text x="10" y="35" font-size="11" fill="#3b82f6">x/4 = 4</text><text x="10" y="50" font-size="11" fill="#22c55e">x = 4 × 4 = 16</text></svg>',
                        steps: [
                            "Subtract 3: x/4 = 4",
                            "Multiply by 4: x = 16"
                        ],
                        answer: "x = 16"
                    }
                ],
                tip: "Clear fractions early to make life easier!"
            },
            8: {
                title: "Forming Equations from Words",
                band: "Higher",
                description: "Turn word problems into equations, then solve. SEC commonly tests this skill with 'think of a number' problems!",
                keyPoints: [
                    "Read carefully - identify what x represents",
                    "Translate words into <strong>mathematical symbols</strong>",
                    "'is' means = , 'more than' means +, 'times' means ×"
                ],
                examples: [
                    {
                        question: "I think of a number, multiply by 3, then add 5. Answer is 20. Find the number.",
                        visual: '<svg viewBox="0 0 280 50" width="280"><text x="10" y="20" font-size="11" fill="#374151">Let the number be x</text><text x="10" y="40" font-size="11" fill="#22c55e">3x + 5 = 20, so x = 5</text></svg>',
                        steps: [
                            "Let the number = x",
                            "Multiply by 3: 3x, Add 5: 3x + 5",
                            "3x + 5 = 20, so 3x = 15, x = <strong>5</strong>"
                        ],
                        answer: "The number is 5"
                    }
                ],
                tip: "Define x first, then build the equation step by step."
            },
            9: {
                title: "Simultaneous Equations - Elimination",
                band: "Higher",
                description: "Solve two equations together by eliminating one variable. Match coefficients, then add or subtract equations.",
                keyPoints: [
                    "Make coefficients of one variable the <strong>same</strong>",
                    "<strong>Add or subtract</strong> equations to eliminate",
                    "Solve for one variable, then substitute back"
                ],
                examples: [
                    {
                        question: "Solve: 2x + y = 7 and x + y = 4",
                        visual: '<svg viewBox="0 0 200 50" width="200"><text x="10" y="20" font-size="11" fill="#3b82f6">2x + y = 7</text><text x="10" y="40" font-size="11" fill="#8b5cf6">x + y = 4</text></svg>',
                        steps: [
                            "Subtract: (2x + y) - (x + y) = 7 - 4",
                            "x = 3",
                            "Substitute: 3 + y = 4, so y = 1"
                        ],
                        answer: "x = 3, y = 1"
                    }
                ],
                tip: "Elimination works when you can match coefficients!"
            },
            10: {
                title: "Simultaneous Equations - Substitution",
                band: "Higher",
                description: "When one equation is already solved for y (like y = 2x + 1), substitute into the other equation.",
                keyPoints: [
                    "If y = expression, <strong>substitute</strong> that expression",
                    "Replace y with the expression in the other equation",
                    "Solve for x, then find y"
                ],
                examples: [
                    {
                        question: "Solve: y = 2x + 1 and 3x + y = 11",
                        visual: '<svg viewBox="0 0 220 50" width="220"><text x="10" y="20" font-size="11" fill="#3b82f6">y = 2x + 1</text><text x="10" y="40" font-size="11" fill="#8b5cf6">3x + y = 11</text></svg>',
                        steps: [
                            "Substitute y = 2x + 1 into second equation",
                            "3x + (2x + 1) = 11 → 5x + 1 = 11",
                            "5x = 10, x = 2, then y = 2(2) + 1 = <strong>5</strong>"
                        ],
                        answer: "x = 2, y = 5"
                    }
                ],
                tip: "Substitution is best when one variable is already isolated!"
            },
            11: {
                title: "Quadratic Equations",
                band: "Higher",
                description: "Equations with x² terms. Factorise and use the fact that if ab = 0, then a = 0 or b = 0.",
                keyPoints: [
                    "Rearrange to form = 0",
                    "<strong>Factorise</strong> into two brackets",
                    "If (x - a)(x - b) = 0, then x = a or x = b"
                ],
                examples: [
                    {
                        question: "Solve: x² - 5x + 6 = 0",
                        visual: '<svg viewBox="0 0 280 50" width="280"><text x="10" y="20" font-size="12" fill="#374151">x² - 5x + 6 = 0</text><text x="10" y="40" font-size="12" fill="#22c55e">(x - 2)(x - 3) = 0 → x = 2 or 3</text></svg>',
                        steps: [
                            "Find two numbers that multiply to 6 and add to -5",
                            "Numbers are -2 and -3",
                            "x = <strong>2</strong> or x = <strong>3</strong>"
                        ],
                        answer: "x = 2 or x = 3"
                    }
                ],
                tip: "For x² + bx + c: find numbers that multiply to c and add to b."
            },
            12: {
                title: "Problem Solving & Applications",
                band: "Mastery",
                description: "Apply equation-solving to real problems: areas, ages, consecutive numbers, speed/distance/time.",
                keyPoints: [
                    "Read the problem carefully",
                    "Define your variable clearly",
                    "Form the equation and solve"
                ],
                examples: [
                    {
                        question: "A rectangle has width x and length (x + 4). Area is 45. Find x.",
                        visual: '<svg viewBox="0 0 280 50" width="280"><text x="10" y="20" font-size="11" fill="#374151">Area = x(x + 4) = 45</text><text x="10" y="40" font-size="11" fill="#22c55e">x² + 4x - 45 = 0 → x = 5</text></svg>',
                        steps: [
                            "Area = length × width = x(x + 4) = 45",
                            "x² + 4x - 45 = 0",
                            "Factorise: (x + 9)(x - 5) = 0, x = <strong>5</strong> (positive)"
                        ],
                        answer: "x = 5"
                    }
                ],
                tip: "🏆 You've mastered Solving Equations! Always check your answer makes sense in context."
            }
        };
        
        // Simultaneous Equations Help Content (12 levels)
        const simultaneousEquationsHelpContent = {
            1: {
                title: "Level 1: Understanding Systems",
                band: "Foundation",
                description: "Learn what a system of equations is - two equations with two unknowns that we solve together.",
                keyPoints: [
                    "A <strong>system</strong> has two equations with two variables (usually x and y)",
                    "We need to find values that work in <strong>both</strong> equations",
                    "The solution is written as an ordered pair (x, y)"
                ],
                examples: [
                    {
                        question: "Does x=3, y=2 solve: x + y = 5 and x - y = 1?",
                        steps: [
                            "Check equation 1: 3 + 2 = 5 ✓",
                            "Check equation 2: 3 - 2 = 1 ✓",
                            "Both work, so (3, 2) is the solution"
                        ],
                        answer: "Yes, (3, 2) is the solution"
                    }
                ],
                tip: "Always check your answer works in BOTH equations!"
            },
            2: {
                title: "Level 2: Solving by Inspection",
                band: "Foundation",
                description: "Find solutions by testing values or using tables. Good for simple equations with small numbers.",
                keyPoints: [
                    "Try small positive and negative integers",
                    "Use a <strong>table of values</strong> to organise your guesses",
                    "Look for patterns in the equations"
                ],
                examples: [
                    {
                        question: "Solve: x + y = 4, x - y = 2",
                        steps: [
                            "Try x = 3: 3 + y = 4, so y = 1",
                            "Check: 3 - 1 = 2 ✓",
                            "Solution: x = 3, y = 1"
                        ],
                        answer: "x = 3, y = 1"
                    }
                ],
                tip: "Add the equations: (x+y) + (x-y) = 4+2 gives 2x = 6!"
            },
            3: {
                title: "Level 3: Graphical Method",
                band: "Foundation",
                description: "Solve by drawing both lines and finding where they cross.",
                keyPoints: [
                    "Each equation represents a <strong>straight line</strong>",
                    "The solution is where the lines <strong>intersect</strong>",
                    "Read off the x and y coordinates of the crossing point"
                ],
                examples: [
                    {
                        question: "Solve graphically: y = x + 1, y = 3",
                        steps: [
                            "Draw line y = x + 1 (slope 1, intercept 1)",
                            "Draw line y = 3 (horizontal line)",
                            "They cross at (2, 3)"
                        ],
                        answer: "x = 2, y = 3"
                    }
                ],
                tip: "Plot at least 3 points for each line to draw accurately."
            },
            4: {
                title: "Level 4: Elimination - Same Coefficients",
                band: "Ordinary",
                description: "When coefficients are the same, add or subtract equations to eliminate a variable.",
                keyPoints: [
                    "If same sign, <strong>subtract</strong> equations",
                    "If opposite signs, <strong>add</strong> equations",
                    "Then solve for the remaining variable"
                ],
                examples: [
                    {
                        question: "Solve: 2x + y = 7, x + y = 4",
                        steps: [
                            "Subtract: (2x + y) - (x + y) = 7 - 4",
                            "This gives: x = 3",
                            "Substitute: 3 + y = 4, so y = 1"
                        ],
                        answer: "x = 3, y = 1"
                    }
                ],
                tip: "Circle the matching coefficients - then decide: add or subtract?"
            },
            5: {
                title: "Level 5: Elimination - Multiply One Equation",
                band: "Ordinary",
                description: "Multiply one equation to create matching coefficients, then eliminate.",
                keyPoints: [
                    "Multiply <strong>every term</strong> in the equation",
                    "Choose which variable to eliminate first",
                    "Then add or subtract as before"
                ],
                examples: [
                    {
                        question: "Solve: 2x + y = 8, x + y = 5",
                        steps: [
                            "Multiply equation 2 by 2: 2x + 2y = 10",
                            "Subtract: (2x + y) - (2x + 2y) = 8 - 10",
                            "-y = -2, so y = 2, then x = 3"
                        ],
                        answer: "x = 3, y = 2"
                    }
                ],
                tip: "Ask: 'What do I multiply by to match the other coefficient?'"
            },
            6: {
                title: "Level 6: Elimination - Multiply Both",
                band: "Ordinary",
                description: "Sometimes you need to multiply both equations to create matching coefficients.",
                keyPoints: [
                    "Find the <strong>LCM</strong> of the coefficients",
                    "Multiply each equation by the appropriate number",
                    "Then add or subtract to eliminate"
                ],
                examples: [
                    {
                        question: "Solve: 3x + 2y = 12, 2x + 3y = 13",
                        steps: [
                            "×2: 6x + 4y = 24 and ×3: 6x + 9y = 39",
                            "Subtract: -5y = -15, so y = 3",
                            "Sub back: 3x + 6 = 12, x = 2"
                        ],
                        answer: "x = 2, y = 3"
                    }
                ],
                tip: "LCM of 2 and 3 is 6 - multiply to get 6x in both!"
            },
            7: {
                title: "Level 7: Substitution - Simple",
                band: "Higher",
                description: "When one equation gives you x= or y=, substitute it into the other.",
                keyPoints: [
                    "If you have y = ..., replace y in the other equation",
                    "Solve the resulting equation for one variable",
                    "Then find the other variable"
                ],
                examples: [
                    {
                        question: "Solve: y = 2x, x + y = 9",
                        steps: [
                            "Substitute y = 2x into equation 2",
                            "x + 2x = 9, so 3x = 9, x = 3",
                            "Then y = 2(3) = 6"
                        ],
                        answer: "x = 3, y = 6"
                    }
                ],
                tip: "Look for equations already in the form x = ... or y = ..."
            },
            8: {
                title: "Level 8: Substitution - Rearranging",
                band: "Higher",
                description: "First rearrange one equation to get x= or y=, then substitute.",
                keyPoints: [
                    "Choose the equation that's <strong>easiest to rearrange</strong>",
                    "Rearrange to make x or y the subject",
                    "Then substitute and solve"
                ],
                examples: [
                    {
                        question: "Solve: x + 2y = 7, 3x - y = 7",
                        steps: [
                            "From eq 1: x = 7 - 2y",
                            "Substitute: 3(7 - 2y) - y = 7",
                            "21 - 6y - y = 7, so y = 2, x = 3"
                        ],
                        answer: "x = 3, y = 2"
                    }
                ],
                tip: "Pick the variable with coefficient 1 to avoid fractions!"
            },
            9: {
                title: "Level 9: Choosing the Best Method",
                band: "Higher",
                description: "Learn when to use elimination vs substitution for efficiency.",
                keyPoints: [
                    "<strong>Elimination</strong>: good when coefficients are similar",
                    "<strong>Substitution</strong>: good when one variable is already isolated",
                    "Either method will work - choose the quicker one!"
                ],
                examples: [
                    {
                        question: "Which method for: y = 3x + 1, 2x + y = 11?",
                        steps: [
                            "y is already isolated → use substitution",
                            "2x + (3x + 1) = 11",
                            "5x = 10, x = 2, y = 7"
                        ],
                        answer: "Substitution: x = 2, y = 7"
                    }
                ],
                tip: "Coefficient of 1? → Substitution. Similar coefficients? → Elimination"
            },
            10: {
                title: "Level 10: Word Problems - Setup",
                band: "Mastery",
                description: "Convert word problems into simultaneous equations. Define variables first!",
                keyPoints: [
                    "Read carefully - identify the <strong>two unknowns</strong>",
                    "Define variables: Let x = ... Let y = ...",
                    "Write <strong>two equations</strong> from the information given"
                ],
                examples: [
                    {
                        question: "5 apples and 3 oranges cost €4.70. 3 apples and 5 oranges cost €4.30. Find the cost of each.",
                        steps: [
                            "Let a = cost of apple, o = cost of orange",
                            "Equation 1: 5a + 3o = 4.70",
                            "Equation 2: 3a + 5o = 4.30"
                        ],
                        answer: "5a + 3o = 4.70, 3a + 5o = 4.30"
                    }
                ],
                tip: "Underline the key information in word problems!"
            },
            11: {
                title: "Level 11: Word Problems - Solve",
                band: "Mastery",
                description: "Set up AND solve word problems completely. Remember to answer in context!",
                keyPoints: [
                    "Set up the equations from the word problem",
                    "Solve using elimination or substitution",
                    "Write answer with <strong>correct units</strong> and context"
                ],
                examples: [
                    {
                        question: "Áine bought 2 coffees and 3 muffins for €11. Cian bought 4 coffees and 2 muffins for €14. Find prices.",
                        steps: [
                            "2c + 3m = 11, 4c + 2m = 14",
                            "×2: 4c + 6m = 22, subtract: 4m = 8, m = 2",
                            "2c + 6 = 11, c = 2.50"
                        ],
                        answer: "Coffee €2.50, Muffin €2"
                    }
                ],
                tip: "Always answer the actual question asked - with units!"
            },
            12: {
                title: "Level 12: Complex Applications",
                band: "Mastery",
                description: "Advanced problems including age problems, distance-rate-time, and algebraic fractions.",
                keyPoints: [
                    "Age problems: think about 'now' vs 'x years ago/later'",
                    "Speed problems: distance = speed × time",
                    "May involve fractions or larger numbers"
                ],
                examples: [
                    {
                        question: "A father is 3 times as old as his son. In 10 years, he'll be twice as old. Find their ages.",
                        steps: [
                            "Now: f = 3s. In 10 years: f + 10 = 2(s + 10)",
                            "Substitute: 3s + 10 = 2s + 20",
                            "s = 10, f = 30"
                        ],
                        answer: "Son is 10, Father is 30"
                    }
                ],
                tip: "Draw a timeline for age problems - 'now' and 'then'!"
            }
        };
        
        // Linear Inequalities Help Content (12 levels)
        const linearInequalitiesHelpContent = {
            1: {
                title: "Level 1: Inequality Symbols",
                band: "Foundation",
                description: "Learn the four inequality symbols and what they mean.",
                keyPoints: [
                    "<strong><</strong> means 'less than'",
                    "<strong>></strong> means 'greater than'",
                    "<strong>≤</strong> means 'less than or equal to'",
                    "<strong>≥</strong> means 'greater than or equal to'"
                ],
                examples: [
                    {
                        question: "What does 5 < 8 mean?",
                        steps: [
                            "The symbol < means 'less than'",
                            "5 is less than 8",
                            "This statement is TRUE"
                        ],
                        answer: "5 is less than 8"
                    }
                ],
                tip: "The symbol always points to the SMALLER number - like a hungry mouth eating the bigger one!"
            },
            2: {
                title: "Level 2: Reading Number Lines",
                band: "Foundation",
                description: "Understand how inequalities are shown on number lines.",
                keyPoints: [
                    "<strong>Open circle (○)</strong> = boundary NOT included (< or >)",
                    "<strong>Closed circle (●)</strong> = boundary IS included (≤ or ≥)",
                    "Arrow points toward the solution region"
                ],
                examples: [
                    {
                        question: "Describe x > 3 on a number line",
                        steps: [
                            "Open circle at 3 (3 not included)",
                            "Arrow points RIGHT (larger values)",
                            "All numbers greater than 3"
                        ],
                        answer: "Open circle at 3, shading right"
                    }
                ],
                tip: "Open = not included (O for Open, Out!), Closed = included (filled in = full membership!)"
            },
            3: {
                title: "Level 3: Real-World Inequalities",
                band: "Foundation",
                description: "Interpret inequalities in everyday contexts like temperature, age, and speed.",
                keyPoints: [
                    "Speed limits: S ≤ 50 means 'at most 50 km/h'",
                    "Age requirements: A ≥ 18 means '18 or older'",
                    "Temperature: T < 0 means 'below freezing'"
                ],
                examples: [
                    {
                        question: "A ride requires height ≥ 120cm. Can someone 118cm ride?",
                        steps: [
                            "H ≥ 120 means height must be 120 or more",
                            "118 < 120",
                            "No, 118cm is not enough"
                        ],
                        answer: "No - must be at least 120cm"
                    }
                ],
                tip: "Look for key words: 'at least' (≥), 'at most' (≤), 'more than' (>), 'less than' (<)"
            },
            4: {
                title: "Level 4: Graphing (x ∈ ℝ)",
                band: "Ordinary",
                description: "Draw inequalities on number lines for real numbers (continuous line).",
                keyPoints: [
                    "For x ∈ ℝ (real numbers), shade continuously",
                    "Use correct circle type at the boundary",
                    "Arrow shows the solution extends infinitely"
                ],
                examples: [
                    {
                        question: "Graph x ≤ 4 where x ∈ ℝ",
                        steps: [
                            "Closed circle at 4 (included)",
                            "Shade LEFT toward smaller numbers",
                            "Arrow at the left end"
                        ],
                        answer: "Closed circle at 4, line going left"
                    }
                ],
                tip: "Always label your number line and mark key values!"
            },
            5: {
                title: "Level 5: Integer Restrictions",
                band: "Ordinary",
                description: "Graph inequalities for integers (ℤ), natural numbers (ℕ), and whole numbers.",
                keyPoints: [
                    "<strong>x ∈ ℤ</strong> = integers (..., -2, -1, 0, 1, 2, ...)",
                    "<strong>x ∈ ℕ</strong> = natural numbers (1, 2, 3, ...)",
                    "Show individual DOTS, not a continuous line"
                ],
                examples: [
                    {
                        question: "List solutions: x < 3 where x ∈ ℕ",
                        steps: [
                            "Natural numbers are 1, 2, 3, ...",
                            "Must be less than 3",
                            "Solutions: 1, 2"
                        ],
                        answer: "{1, 2}"
                    }
                ],
                tip: "ℕ starts at 1, not 0! (Some books include 0 - check with your teacher)"
            },
            6: {
                title: "Level 6: One-Step Solving",
                band: "Ordinary",
                description: "Solve inequalities with one operation (add, subtract, multiply, divide).",
                keyPoints: [
                    "Same rules as equations: do the same to both sides",
                    "x + 5 > 8 → subtract 5 → x > 3",
                    "3x ≤ 12 → divide by 3 → x ≤ 4"
                ],
                examples: [
                    {
                        question: "Solve: x - 4 ≥ 7",
                        steps: [
                            "Add 4 to both sides",
                            "x - 4 + 4 ≥ 7 + 4",
                            "x ≥ 11"
                        ],
                        answer: "x ≥ 11"
                    }
                ],
                tip: "Whatever you do to one side, do EXACTLY the same to the other side!"
            },
            7: {
                title: "Level 7: Two-Step Solving",
                band: "Higher",
                description: "Solve inequalities like 2x - 3 ≥ 5 (SEC exam style).",
                keyPoints: [
                    "Step 1: Deal with addition/subtraction first",
                    "Step 2: Then multiplication/division",
                    "Same approach as solving equations"
                ],
                examples: [
                    {
                        question: "Solve: 3x + 2 < 14",
                        steps: [
                            "Subtract 2: 3x < 12",
                            "Divide by 3: x < 4",
                            "Solution: x < 4"
                        ],
                        answer: "x < 4"
                    }
                ],
                tip: "This is exactly like SEC paper questions! Practice the format."
            },
            8: {
                title: "Level 8: Compound Inequalities",
                band: "Higher",
                description: "Work with double inequalities like -2 < x ≤ 4.",
                keyPoints: [
                    "Read as 'x is greater than -2 AND less than or equal to 4'",
                    "Two boundaries - check circle type at each",
                    "Solution is the overlap region"
                ],
                examples: [
                    {
                        question: "Graph: 1 ≤ x < 5",
                        steps: [
                            "Closed circle at 1 (included)",
                            "Open circle at 5 (not included)",
                            "Shade between 1 and 5"
                        ],
                        answer: "Closed at 1, open at 5, shade between"
                    }
                ],
                tip: "Both conditions must be true - x must be in BOTH ranges!"
            },
            9: {
                title: "Level 9: Negative Coefficients",
                band: "Higher",
                description: "The critical rule: FLIP the inequality when multiplying/dividing by a negative!",
                keyPoints: [
                    "<strong>FLIP</strong> the sign when × or ÷ by negative",
                    "-2x > 6 → divide by -2 → x < -3",
                    "This is the most common mistake - watch out!"
                ],
                examples: [
                    {
                        question: "Solve: -3x ≤ 9",
                        steps: [
                            "Divide both sides by -3",
                            "FLIP the inequality sign!",
                            "x ≥ -3"
                        ],
                        answer: "x ≥ -3"
                    }
                ],
                tip: "Memory trick: Negative flips everything upside down - including the inequality!"
            },
            10: {
                title: "Level 10: Word Problems",
                band: "Mastery",
                description: "Translate real-world problems into inequalities and solve them.",
                keyPoints: [
                    "Identify the variable and what it represents",
                    "Look for keywords: 'at least', 'no more than', 'minimum'",
                    "Write the inequality, then solve"
                ],
                examples: [
                    {
                        question: "Cian has €50. Books cost €8 each. How many can he buy?",
                        steps: [
                            "Let n = number of books",
                            "8n ≤ 50",
                            "n ≤ 6.25, so n ≤ 6 books"
                        ],
                        answer: "At most 6 books"
                    }
                ],
                tip: "Always check: does your answer make sense in the real world?"
            },
            11: {
                title: "Level 11: Rounding & Tolerance",
                band: "Mastery",
                description: "Find the range of values that round to a displayed number (SEC exam style).",
                keyPoints: [
                    "If 18°C shown (nearest whole), actual could be 17.5 ≤ t < 18.5",
                    "Lower bound: value - 0.5",
                    "Upper bound: value + 0.5 (not included)"
                ],
                examples: [
                    {
                        question: "A thermometer shows 23°C (nearest degree). Find the range.",
                        steps: [
                            "Lower bound: 23 - 0.5 = 22.5",
                            "Upper bound: 23 + 0.5 = 23.5",
                            "22.5 ≤ t < 23.5"
                        ],
                        answer: "22.5 ≤ t < 23.5"
                    }
                ],
                tip: "The upper bound uses < not ≤ (values AT 23.5 would round UP to 24)"
            },
            12: {
                title: "Level 12: Multi-step Problems",
                band: "Mastery",
                description: "Complex problems combining inequalities with area, perimeter, profit, or multiple conditions.",
                keyPoints: [
                    "Break into steps - identify what you know",
                    "Set up the inequality from the constraint",
                    "Solve and interpret in context"
                ],
                examples: [
                    {
                        question: "Rectangle length 8m, area at least 40m². Find width w.",
                        steps: [
                            "Area = length × width",
                            "8w ≥ 40",
                            "w ≥ 5"
                        ],
                        answer: "w ≥ 5m"
                    }
                ],
                tip: "Draw diagrams for geometry problems - visualise the constraint!"
            }
        };
        
        // Probability Help Content (12 levels)
        const probabilityHelpContent = {
            1: {
                title: "Level 1: Probability Language",
                band: "Foundation",
                description: "Learn to describe how likely events are using probability words.",
                keyPoints: [
                    "Certain = will definitely happen (probability = 1)",
                    "Impossible = cannot happen (probability = 0)",
                    "Equally likely = 50/50 chance (probability = 0.5)",
                    "Likely = probably will happen (probability > 0.5)",
                    "Unlikely = probably won't happen (probability < 0.5)"
                ],
                examples: [
                    {
                        question: "The sun rising tomorrow",
                        answer: "Certain"
                    },
                    {
                        question: "Rolling a 7 on a standard dice",
                        answer: "Impossible"
                    }
                ],
                tip: "💡 Think: Could this EVER happen? If yes, could it happen MORE than half the time?"
            },
            2: {
                title: "Level 2: Simple Probability as Fractions",
                band: "Foundation",
                description: "Calculate probability of single events using the formula.",
                keyPoints: [
                    "P(event) = favourable outcomes ÷ total outcomes",
                    "Always write as a fraction in simplest form",
                    "Count carefully - don't miss any outcomes!",
                    "Dice has 6 sides: 1, 2, 3, 4, 5, 6"
                ],
                examples: [
                    {
                        question: "P(even number on dice)?",
                        answer: "3/6 = 1/2 (three evens: 2, 4, 6)"
                    },
                    {
                        question: "Bag: 3 red, 5 blue. P(red)?",
                        answer: "3/8"
                    }
                ],
                tip: "💡 SEC Tip: Always simplify your fraction! 4/8 = 1/2"
            },
            3: {
                title: "Level 3: Probability from Lists & Tables",
                band: "Foundation",
                description: "Find probabilities from frequency tables and data lists.",
                keyPoints: [
                    "Find total by adding all frequencies",
                    "P(category) = frequency of category ÷ total",
                    "Read tables carefully - check row/column totals",
                    "SEC often gives survey or class data"
                ],
                examples: [
                    {
                        question: "Maths:12, English:8, Science:10. P(chose Maths)?",
                        answer: "12/30 = 2/5"
                    }
                ],
                tip: "💡 Always find the TOTAL first, then the specific category count."
            },
            4: {
                title: "Level 4: Complement - P(NOT happening)",
                band: "Ordinary",
                description: "Find probability an event does NOT happen.",
                keyPoints: [
                    "P(not A) = 1 - P(A)",
                    "All probabilities add to 1",
                    "If P(rain) = 3/5, then P(no rain) = 2/5",
                    "Complement means 'everything else'"
                ],
                examples: [
                    {
                        question: "P(win) = 2/7. P(not win)?",
                        answer: "1 - 2/7 = 5/7"
                    }
                ],
                tip: "💡 Quick check: P(A) + P(not A) must equal 1!"
            },
            5: {
                title: "Level 5: Expected Outcomes",
                band: "Ordinary",
                description: "Calculate how many times an event should happen over many trials.",
                keyPoints: [
                    "Expected = probability × number of trials",
                    "This gives the AVERAGE expectation",
                    "Actual results may differ slightly",
                    "SEC 2023: Spinner expected outcomes question"
                ],
                examples: [
                    {
                        question: "P(red) = 1/4. In 80 spins, expected reds?",
                        answer: "1/4 × 80 = 20"
                    }
                ],
                tip: "💡 Multiply the fraction by the number of trials. Simplify first if possible!"
            },
            6: {
                title: "Level 6: Two-Way Tables & Sample Space",
                band: "Ordinary",
                description: "Find probabilities from two dice or two-way tables.",
                keyPoints: [
                    "Two dice = 36 total outcomes (6 × 6)",
                    "Sample space lists ALL possible outcomes",
                    "For sum of 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 ways",
                    "Two-way tables: add row/column carefully"
                ],
                examples: [
                    {
                        question: "Two dice. P(sum = 7)?",
                        answer: "6/36 = 1/6"
                    },
                    {
                        question: "P(getting a double)?",
                        answer: "6/36 = 1/6"
                    }
                ],
                tip: "💡 Draw the 6×6 grid for two dice - it helps you count correctly!"
            },
            7: {
                title: "Level 7: Relative Frequency",
                band: "Higher",
                description: "Calculate experimental probability from actual results.",
                keyPoints: [
                    "Relative frequency = observed outcomes ÷ total trials",
                    "This is EXPERIMENTAL probability",
                    "More trials → closer to theoretical probability",
                    "SEC often compares experimental vs theoretical"
                ],
                examples: [
                    {
                        question: "Coin tossed 50 times, 23 heads. Rel. freq?",
                        answer: "23/50"
                    }
                ],
                tip: "💡 Relative frequency is what ACTUALLY happened, not what SHOULD happen."
            },
            8: {
                title: "Level 8: Combined Events - OR Rule",
                band: "Higher",
                description: "Find probability of either event happening.",
                keyPoints: [
                    "P(A or B) - count outcomes in A OR B",
                    "Don't double count overlaps!",
                    "For mutually exclusive: P(A or B) = P(A) + P(B)",
                    "Example: P(even or 5) on dice = P(2,4,5,6) = 4/6"
                ],
                examples: [
                    {
                        question: "Dice: P(even or greater than 4)?",
                        answer: "P(2,4,5,6) = 4/6 = 2/3"
                    }
                ],
                tip: "💡 'OR' means either one or the other (or both). List the outcomes!"
            },
            9: {
                title: "Level 9: Combined Events - AND Rule",
                band: "Higher",
                description: "Find probability of both events happening.",
                keyPoints: [
                    "For independent events: P(A and B) = P(A) × P(B)",
                    "Independent = first event doesn't affect second",
                    "Coins and dice throws are independent",
                    "Multiply the individual probabilities"
                ],
                examples: [
                    {
                        question: "Two coins: P(both heads)?",
                        answer: "1/2 × 1/2 = 1/4"
                    },
                    {
                        question: "Two dice: P(both show 6)?",
                        answer: "1/6 × 1/6 = 1/36"
                    }
                ],
                tip: "💡 'AND' means MULTIPLY. 'OR' usually means ADD."
            },
            10: {
                title: "Level 10: Tree Diagrams",
                band: "Mastery",
                description: "Use tree diagrams to find probabilities of combined events.",
                keyPoints: [
                    "Draw branches for each stage",
                    "Write probability on each branch",
                    "Multiply along branches (AND)",
                    "Add different paths (OR)",
                    "SEC 2024 HL: Tree diagram question"
                ],
                examples: [
                    {
                        question: "P(A)=1/3, P(B)=1/4. P(both happen)?",
                        answer: "1/3 × 1/4 = 1/12"
                    },
                    {
                        question: "P(neither happens)?",
                        answer: "2/3 × 3/4 = 6/12 = 1/2"
                    }
                ],
                tip: "💡 Tree diagrams make complex problems visual. Label everything!"
            },
            11: {
                title: "Level 11: Without Replacement",
                band: "Mastery",
                description: "Calculate probability when items are NOT replaced.",
                keyPoints: [
                    "First pick: normal probability",
                    "Second pick: total reduced by 1!",
                    "If same colour: numerator also reduces",
                    "Key difference from WITH replacement"
                ],
                examples: [
                    {
                        question: "Bag: 4 red, 3 blue. Two picked. P(both red)?",
                        answer: "4/7 × 3/6 = 12/42 = 2/7"
                    }
                ],
                tip: "💡 WITHOUT replacement: the second fraction changes! Both top and bottom."
            },
            12: {
                title: "Level 12: Problem Solving",
                band: "Mastery",
                description: "Apply probability to real-world problems and games.",
                keyPoints: [
                    "Fair game: P(win) = 1/2",
                    "Expected value: multiply outcomes by probabilities",
                    "P(at least one) = 1 - P(none)",
                    "Working backwards: use algebra"
                ],
                examples: [
                    {
                        question: "P(success) = 1/5. In 2 tries, P(at least one)?",
                        answer: "1 - (4/5)² = 1 - 16/25 = 9/25"
                    }
                ],
                tip: "🏆 You've mastered Probability! The complement trick P(at least one) = 1 - P(none) is very powerful!"
            }
        };
        
        // Coordinate Geometry Help Content (12 levels)
        const coordinateGeometryHelpContent = {
            1: {
                title: "Level 1: Plotting & Reading Points",
                band: "Foundation",
                description: "Learn to read and plot coordinates on a grid.",
                keyPoints: [
                    "Coordinates are written as (x, y)",
                    "x = horizontal position (left/right)",
                    "y = vertical position (up/down)",
                    "Origin is at (0, 0)",
                    "Quadrant 1: (+, +), Q2: (-, +), Q3: (-, -), Q4: (+, -)"
                ],
                examples: [
                    {
                        question: "What are the coordinates of point P at 3 right and 2 up?",
                        answer: "(3, 2)"
                    }
                ],
                tip: "💡 Remember: x comes first (across), then y (up/down). 'Along the corridor, then up the stairs!'"
            },
            2: {
                title: "Level 2: Horizontal & Vertical Distance",
                band: "Foundation",
                description: "Find distances along the axes.",
                keyPoints: [
                    "Horizontal distance: same y-coordinate",
                    "Vertical distance: same x-coordinate",
                    "Distance = |difference of coordinates|",
                    "Always give distance as positive"
                ],
                examples: [
                    {
                        question: "Distance from (2, 3) to (7, 3)?",
                        answer: "|7 - 2| = 5 units"
                    }
                ],
                tip: "💡 When one coordinate is the same, just subtract the other coordinates!"
            },
            3: {
                title: "Level 3: Distance Formula",
                band: "Foundation",
                description: "Use the distance formula for diagonal distances.",
                keyPoints: [
                    "d = √[(x₂-x₁)² + (y₂-y₁)²]",
                    "Based on Pythagoras' theorem",
                    "Works for any two points",
                    "Common answers: 5 (3-4-5), 10 (6-8-10), 13 (5-12-13)"
                ],
                examples: [
                    {
                        question: "Distance from (0, 0) to (3, 4)?",
                        answer: "√(9 + 16) = √25 = 5"
                    }
                ],
                tip: "💡 Look for Pythagorean triples: 3-4-5, 5-12-13, 6-8-10"
            },
            4: {
                title: "Level 4: Midpoint Formula",
                band: "Ordinary",
                description: "Find the point exactly halfway between two points.",
                keyPoints: [
                    "M = ((x₁+x₂)/2, (y₁+y₂)/2)",
                    "Average of x-coordinates, average of y-coordinates",
                    "Midpoint lies on the line segment",
                    "Used to find centre of circle from diameter"
                ],
                examples: [
                    {
                        question: "Midpoint of (2, 4) and (6, 8)?",
                        answer: "((2+6)/2, (4+8)/2) = (4, 6)"
                    }
                ],
                tip: "💡 Just find the average of x's and the average of y's!"
            },
            5: {
                title: "Level 5: Slope/Gradient - Concept",
                band: "Ordinary",
                description: "Understand what slope means and identify types.",
                keyPoints: [
                    "Slope = steepness of a line",
                    "Positive slope: uphill (left to right)",
                    "Negative slope: downhill (left to right)",
                    "Zero slope: horizontal line",
                    "Undefined slope: vertical line"
                ],
                examples: [
                    {
                        question: "A line goes uphill from left to right. Slope type?",
                        answer: "Positive"
                    }
                ],
                tip: "💡 Think of walking: uphill = positive, downhill = negative!"
            },
            6: {
                title: "Level 6: Slope/Gradient - Calculations",
                band: "Ordinary",
                description: "Calculate slope using the formula.",
                keyPoints: [
                    "m = (y₂ - y₁)/(x₂ - x₁)",
                    "m = rise/run",
                    "Always simplify the fraction",
                    "Order of points doesn't matter"
                ],
                examples: [
                    {
                        question: "Slope through (1, 2) and (3, 6)?",
                        answer: "m = (6-2)/(3-1) = 4/2 = 2"
                    }
                ],
                tip: "💡 Rise (y-change) over run (x-change). Keep the order consistent!"
            },
            7: {
                title: "Level 7: Equation of Line y = mx + c",
                band: "Higher",
                description: "Understand the slope-intercept form.",
                keyPoints: [
                    "y = mx + c is slope-intercept form",
                    "m = slope (coefficient of x)",
                    "c = y-intercept (where line crosses y-axis)",
                    "y-intercept is the point (0, c)"
                ],
                examples: [
                    {
                        question: "What is the slope of y = 3x - 2?",
                        answer: "Slope = 3, y-intercept = -2"
                    }
                ],
                tip: "💡 In y = mx + c: m is slope, c is where it crosses the y-axis!"
            },
            8: {
                title: "Level 8: Rearranging to y = mx + c",
                band: "Higher",
                description: "Convert equations to slope-intercept form.",
                keyPoints: [
                    "Get y alone on one side",
                    "ax + by = c → y = (-a/b)x + (c/b)",
                    "Identify m and c from rearranged form",
                    "Check by substituting a point"
                ],
                examples: [
                    {
                        question: "Rearrange 2x + y = 6 to find slope",
                        answer: "y = -2x + 6, so slope = -2"
                    }
                ],
                tip: "💡 Always isolate y first, then read off m and c!"
            },
            9: {
                title: "Level 9: Parallel & Perpendicular Lines",
                band: "Higher",
                description: "Understand relationships between line slopes.",
                keyPoints: [
                    "Parallel lines: same slope (m₁ = m₂)",
                    "Perpendicular lines: m₁ × m₂ = -1",
                    "Perpendicular slope = negative reciprocal",
                    "If m₁ = 2, perpendicular m₂ = -½"
                ],
                examples: [
                    {
                        question: "Line has slope 3. Perpendicular slope?",
                        answer: "-1/3 (negative reciprocal)"
                    }
                ],
                tip: "💡 Parallel = same slope. Perpendicular = flip and change sign!"
            },
            10: {
                title: "Level 10: Equation from Two Points",
                band: "Mastery",
                description: "Find the equation of a line through two given points.",
                keyPoints: [
                    "Step 1: Find slope m = (y₂-y₁)/(x₂-x₁)",
                    "Step 2: Use y = mx + c with one point",
                    "Step 3: Solve for c",
                    "Step 4: Write final equation"
                ],
                examples: [
                    {
                        question: "Equation through (1, 3) and (3, 7)?",
                        answer: "m = 4/2 = 2. c = 3 - 2(1) = 1. y = 2x + 1"
                    }
                ],
                tip: "💡 Find slope first, then substitute a point to find c!"
            },
            11: {
                title: "Level 11: Equation from Point and Slope",
                band: "Mastery",
                description: "Find equation using point-slope form.",
                keyPoints: [
                    "Use y - y₁ = m(x - x₁)",
                    "For parallel: use same slope as given line",
                    "For perpendicular: use negative reciprocal",
                    "Simplify to y = mx + c form"
                ],
                examples: [
                    {
                        question: "Line through (2, 5) with slope 3?",
                        answer: "y - 5 = 3(x - 2) → y = 3x - 1"
                    }
                ],
                tip: "💡 Point-slope form is quick: y - y₁ = m(x - x₁)"
            },
            12: {
                title: "Level 12: Problem Solving",
                band: "Mastery",
                description: "Apply coordinate geometry to solve problems.",
                keyPoints: [
                    "Collinear points: same slope between all pairs",
                    "Area of triangle: ½ × base × height",
                    "x-intercept: set y = 0 and solve",
                    "Intersection: solve equations simultaneously"
                ],
                examples: [
                    {
                        question: "x-intercept of y = 2x - 4?",
                        answer: "0 = 2x - 4 → x = 2. Point: (2, 0)"
                    }
                ],
                tip: "🏆 You've mastered Coordinate Geometry! Combine formulas to solve complex problems."
            }
        };
        
        // Introductory Algebra Help Content (12 levels)
        const introductoryAlgebraHelpContent = {
            1: {
                title: "Understanding Variables",
                band: "Foundation",
                description: "Learn what variables are and how they represent unknown numbers. Solve shape algebra puzzles!",
                keyPoints: [
                    "A <strong>variable</strong> (like x, y, n) represents an unknown number",
                    "Shape algebra: if ○ + ○ + ○ = 21, then ○ = 7",
                    "We can use any letter to represent unknowns"
                ],
                examples: [
                    {
                        question: "If △ + △ + △ = 18, what is △?",
                        answer: "△ = 18 ÷ 3 = 6"
                    }
                ],
                tip: "Think of variables as empty boxes waiting to hold a number!"
            },
            2: {
                title: "Writing Simple Expressions",
                band: "Foundation",
                description: "Convert words into algebraic expressions and work with number walls.",
                keyPoints: [
                    "'Five more than x' becomes x + 5",
                    "'Double n' becomes 2n",
                    "In number walls, each block = sum of two blocks below"
                ],
                examples: [
                    {
                        question: "Write 'three less than p' as an expression",
                        answer: "p - 3"
                    }
                ],
                tip: "SEC Exam style! Cost €3n means 3 times n euros."
            },
            3: {
                title: "Collecting Like Terms (Basic)",
                band: "Foundation",
                description: "Combine terms that have the same variable - just add or subtract the coefficients!",
                keyPoints: [
                    "<strong>Like terms</strong> have the same letter part (e.g., 3x and 5x)",
                    "Add/subtract the numbers, keep the letter: 3x + 5x = 8x",
                    "5a + 3b - 2a + 7b = 3a + 10b (group like terms)"
                ],
                examples: [
                    {
                        question: "Simplify: 5a + 3b - 2a + 7b",
                        answer: "= (5a - 2a) + (3b + 7b) = 3a + 10b"
                    }
                ],
                tip: "SEC 2022 OL Q13(a) style! Think of variables like different fruits - you can only add apples to apples."
            },
            4: {
                title: "Substitution",
                band: "Ordinary",
                description: "Replace variables with given values and calculate the result.",
                keyPoints: [
                    "Substitution means replacing letters with numbers",
                    "Use brackets when substituting: if x = 4, write 3(4) not 34",
                    "Follow BOMDAS after substituting"
                ],
                examples: [
                    {
                        question: "Find 2a + 3b when a = 5, b = 7",
                        answer: "= 2(5) + 3(7) = 10 + 21 = 31"
                    }
                ],
                tip: "SEC 2024 OL Q12(a) style! Always use brackets when substituting."
            },
            5: {
                title: "Expanding Single Brackets",
                band: "Ordinary",
                description: "Multiply everything inside the bracket by the number outside.",
                keyPoints: [
                    "Multiply the outside by EACH term inside",
                    "5(2x + 3) = 5×2x + 5×3 = 10x + 15",
                    "Watch signs: 3(x - 2) = 3x - 6"
                ],
                examples: [
                    {
                        question: "Expand: 3(4x - 2)",
                        answer: "= 3 × 4x - 3 × 2 = 12x - 6"
                    }
                ],
                tip: "SEC 2024 OL Q12(b) style! The number outside 'touches' everything inside."
            },
            6: {
                title: "Expanding and Simplifying",
                band: "Ordinary",
                description: "Expand two brackets then collect like terms.",
                keyPoints: [
                    "Expand each bracket separately first",
                    "Then collect like terms",
                    "Watch minus signs: -(2x - 3) = -2x + 3"
                ],
                examples: [
                    {
                        question: "Expand: 4(x + 3) + 2(3x - 5)",
                        answer: "= 4x + 12 + 6x - 10 = 10x + 2"
                    }
                ],
                tip: "SEC 2023 OL Q14(c) style! Be careful with minus signs before brackets."
            },
            7: {
                title: "Collecting Terms (Advanced)",
                band: "Higher",
                description: "Work with terms containing xy, x², and multiple variables.",
                keyPoints: [
                    "xy and x are NOT like terms",
                    "x² and x are NOT like terms",
                    "5xy + 3x - 2xy + 7x = 3xy + 10x"
                ],
                examples: [
                    {
                        question: "Simplify: 5xy + 3x - 2xy + 7x",
                        answer: "= (5xy - 2xy) + (3x + 7x) = 3xy + 10x"
                    }
                ],
                tip: "SEC 2022 HL Q9(a) style! Group terms with the same variable combination."
            },
            8: {
                title: "Substitution with Powers",
                band: "Higher",
                description: "Substitute into expressions containing squares and higher powers.",
                keyPoints: [
                    "x² means x × x (not 2x!)",
                    "If p = 4, then 3p² = 3 × 4² = 3 × 16 = 48",
                    "Calculate powers BEFORE multiplying by coefficients"
                ],
                examples: [
                    {
                        question: "Find 3p² - 2q when p = 4, q = 5",
                        answer: "= 3(4)² - 2(5) = 3(16) - 10 = 48 - 10 = 38"
                    }
                ],
                tip: "SEC 2024 HL Q11(a) style! Remember: p² means p × p, not p × 2."
            },
            9: {
                title: "Forming Expressions",
                band: "Higher",
                description: "Create algebraic expressions from word problems and contexts.",
                keyPoints: [
                    "Perimeter of rectangle: 2l + 2w",
                    "Area of rectangle: l × w",
                    "Consecutive numbers: n, n+1, n+2"
                ],
                examples: [
                    {
                        question: "Rectangle has length x cm, width 5 cm. Write perimeter.",
                        answer: "Perimeter = 2x + 2(5) = 2x + 10"
                    }
                ],
                tip: "Read word problems carefully to identify what the variable represents."
            },
            10: {
                title: "Simplifying Complex Expressions",
                band: "Application",
                description: "Simplify expressions with multiple terms including squares.",
                keyPoints: [
                    "Group x² terms together, x terms together",
                    "5x² - 7x + 3x² - 6x = 8x² - 13x",
                    "Be careful with signs when collecting"
                ],
                examples: [
                    {
                        question: "Simplify: 5x² - 7x + 3x² - 6x",
                        answer: "= (5 + 3)x² + (-7 - 6)x = 8x² - 13x"
                    }
                ],
                tip: "SEC 2025 HL Q11(a) style! Organise your working clearly."
            },
            11: {
                title: "Factorising (Common Factor)",
                band: "Application",
                description: "Take out the highest common factor from an expression.",
                keyPoints: [
                    "Find the HCF of all terms",
                    "6x + 12 = 6(x + 2)",
                    "5x² + 3x = x(5x + 3)"
                ],
                examples: [
                    {
                        question: "Factorise: 6x² - 9xy",
                        answer: "HCF is 3x. Answer: 3x(2x - 3y)"
                    }
                ],
                tip: "SEC 2022 HL Q9(b) style! Find what ALL terms have in common."
            },
            12: {
                title: "Quadratic Factorising",
                band: "Mastery",
                description: "Factorise quadratic expressions into two brackets.",
                keyPoints: [
                    "x² + 5x + 6 = (x + 2)(x + 3)",
                    "Find two numbers that multiply to the constant and add to the middle",
                    "x² - 10x + 21 = (x - 3)(x - 7)"
                ],
                examples: [
                    {
                        question: "Factorise: x² - 10x + 21",
                        answer: "Numbers: -3 and -7 (multiply to 21, add to -10). Answer: (x - 3)(x - 7)"
                    }
                ],
                tip: "🏆 SEC 2025 OL Q10(d) style! You've mastered Introductory Algebra!"
            }
        };
        
        // Applied Arithmetic (Financial Maths) Help Content (12 levels)
        const appliedArithmeticHelpContent = {
            1: {
                title: "Level 1: Money Calculations",
                band: "Foundation",
                description: "Basic money calculations - adding costs and giving change.",
                keyPoints: [
                    "Add up item prices to find total cost",
                    "Change = Amount Paid − Total Cost",
                    "Cost per item = Total Cost ÷ Number of items",
                    "Always check your decimal places (cents)"
                ],
                examples: [
                    {
                        question: "Milk €2.49, Bread €1.79, Cheese €3.50. Total?",
                        answer: "€2.49 + €1.79 + €3.50 = €7.78"
                    },
                    {
                        question: "Bill is €17.35, pay with €20. Change?",
                        answer: "€20 − €17.35 = €2.65"
                    }
                ],
                tip: "💡 SEC 2024 OL Q2(a) style! Line up decimals when adding."
            },
            2: {
                title: "Level 2: Profit and Loss",
                band: "Foundation",
                description: "Calculate profit, cost price, and selling price.",
                keyPoints: [
                    "Profit = Selling Price − Cost Price",
                    "Selling Price = Cost Price + Profit",
                    "Cost Price = Selling Price − Profit",
                    "If Selling < Cost, it's a LOSS"
                ],
                examples: [
                    {
                        question: "Cost €75, Selling €110. Profit?",
                        answer: "Profit = €110 − €75 = €35"
                    },
                    {
                        question: "Cost €120, Profit €45. Selling price?",
                        answer: "Selling = €120 + €45 = €165"
                    }
                ],
                tip: "💡 SEC 2022 OL Q9(a-b) style! Remember: Profit is what you GAIN."
            },
            3: {
                title: "Level 3: Wages - Basic",
                band: "Foundation",
                description: "Calculate earnings from hours and hourly rate.",
                keyPoints: [
                    "Earnings = Hours Worked × Hourly Rate",
                    "Hours = Earnings ÷ Hourly Rate",
                    "Hourly Rate = Earnings ÷ Hours",
                    "Weekly wage = Days × Hours per day × Rate"
                ],
                examples: [
                    {
                        question: "8 hours at €15/hour?",
                        answer: "8 × €15 = €120"
                    },
                    {
                        question: "Earned €195 at €13/hour. Hours?",
                        answer: "€195 ÷ €13 = 15 hours"
                    }
                ],
                tip: "💡 Think of it as a rectangle: Hours × Rate = Total Pay"
            },
            4: {
                title: "Level 4: Overtime & Pay Increases",
                band: "Ordinary",
                description: "Calculate overtime rates and percentage pay increases.",
                keyPoints: [
                    "Time and a half = Rate × 1.5",
                    "Double time = Rate × 2",
                    "Pay rise: New = Old + (Old × Percentage)",
                    "SEC 2024 OL Q2(b): '50% extra' means × 1.5"
                ],
                examples: [
                    {
                        question: "€16/hour, time and a half for Sunday. 6 hours?",
                        answer: "Overtime rate = €16 × 1.5 = €24. Earnings = 6 × €24 = €144"
                    },
                    {
                        question: "€14/hour, 5% rise. New rate?",
                        answer: "€14 × 0.05 = €0.70. New = €14.70"
                    }
                ],
                tip: "💡 SEC 2024 OL Q2(b)(ii) style! 50% extra means multiply by 1.5"
            },
            5: {
                title: "Level 5: Simple Interest",
                band: "Ordinary",
                description: "Calculate interest on savings using the simple interest formula.",
                keyPoints: [
                    "Interest = Principal × Rate × Time",
                    "For 1 year: Interest = Principal × Rate%",
                    "Total Amount = Principal + Interest",
                    "To find rate: Rate = (Interest ÷ Principal) × 100"
                ],
                examples: [
                    {
                        question: "€130 at 3% for 1 year?",
                        answer: "Interest = €130 × 0.03 = €3.90"
                    },
                    {
                        question: "€120 becomes €124.56 after 1 year. Rate?",
                        answer: "Interest = €4.56. Rate = (4.56 ÷ 120) × 100 = 3.8%"
                    }
                ],
                tip: "💡 SEC 2025 OL Q9(b-c) style! Convert percentage to decimal: 3% = 0.03"
            },
            6: {
                title: "Level 6: Currency Conversion",
                band: "Ordinary",
                description: "Convert between Euro, Sterling, and US Dollars.",
                keyPoints: [
                    "€ to £: Multiply by exchange rate (e.g., €1 = £0.90)",
                    "£ to €: Divide by exchange rate",
                    "€ to $: Multiply by rate (e.g., €1 = $1.20)",
                    "To compare prices: Convert to SAME currency first"
                ],
                examples: [
                    {
                        question: "€200 to £ at €1 = £0.90?",
                        answer: "200 × 0.90 = £180"
                    },
                    {
                        question: "£15.95 to € at €1 = £0.90?",
                        answer: "15.95 ÷ 0.90 = €17.72"
                    }
                ],
                tip: "💡 SEC 2022 OL Q3(d) style! Think: Am I getting MORE or FEWER units?"
            },
            7: {
                title: "Level 7: Percentage Profit/Discount",
                band: "Higher",
                description: "Calculate percentage profit, loss, and discount.",
                keyPoints: [
                    "% Profit = (Profit ÷ Cost Price) × 100",
                    "% Discount = (Discount ÷ Original Price) × 100",
                    "SEC asks for profit as % of COST, not selling price",
                    "To find original: Original = Sale Price ÷ (1 − discount%)"
                ],
                examples: [
                    {
                        question: "Cost €320, Profit €80. % Profit?",
                        answer: "(80 ÷ 320) × 100 = 25%"
                    },
                    {
                        question: "€140 reduced to €93.80. % Discount?",
                        answer: "Discount = €46.20. (46.20 ÷ 140) × 100 = 33%"
                    }
                ],
                tip: "💡 SEC 2025 HL Q1(b) style! % Profit uses COST as the base, not selling!"
            },
            8: {
                title: "Level 8: Income Tax - Basic",
                band: "Higher",
                description: "Calculate tax and net income with tax credits.",
                keyPoints: [
                    "Gross Tax = Gross Income × Tax Rate",
                    "Tax Due = Gross Tax − Tax Credits",
                    "Net Income = Gross Income − Tax Due",
                    "SEC 2024 OL uses 20% tax rate"
                ],
                examples: [
                    {
                        question: "Gross €1900, Tax 20%, Credits €312.50?",
                        answer: "Gross tax = €380. Tax due = €380 − €312.50 = €67.50. Net = €1832.50"
                    }
                ],
                tip: "💡 SEC 2024 OL Q2(c) style! Tax Credits REDUCE your tax bill, not your income."
            },
            9: {
                title: "Level 9: VAT Calculations",
                band: "Higher",
                description: "Add VAT to prices and find pre-VAT amounts.",
                keyPoints: [
                    "VAT = Pre-VAT Price × VAT Rate",
                    "Total = Pre-VAT + VAT (or Pre-VAT × 1.23 for 23%)",
                    "Pre-VAT = Total ÷ (1 + VAT Rate)",
                    "Irish VAT: Standard 23%, Reduced 13.5%, Lower 9%"
                ],
                examples: [
                    {
                        question: "€100 + 13.5% VAT?",
                        answer: "VAT = €13.50. Total = €113.50"
                    },
                    {
                        question: "€123 including 23% VAT. Pre-VAT price?",
                        answer: "€123 ÷ 1.23 = €100"
                    }
                ],
                tip: "💡 SEC 2025 HL Q3 style! For 13.5% VAT, multiply by 1.135"
            },
            10: {
                title: "Level 10: Compound Interest",
                band: "Application",
                description: "Calculate compound interest over multiple years.",
                keyPoints: [
                    "Year 1: Same as simple interest",
                    "Year 2+: Interest calculated on NEW total",
                    "Formula: A = P × (1 + r)^n",
                    "Compound > Simple because interest earns interest"
                ],
                examples: [
                    {
                        question: "€2500 at 3.2% for 2 years compound?",
                        answer: "Year 1: €2580. Year 2: €2580 × 1.032 = €2662.56"
                    },
                    {
                        question: "Or use formula: €2500 × (1.032)² = €2662.56",
                        answer: "The compound interest is €162.56"
                    }
                ],
                tip: "💡 SEC 2024 HL Q3(c) style! Each year, interest is added before calculating next year."
            },
            11: {
                title: "Level 11: Income Tax Bands",
                band: "Application",
                description: "Calculate tax using two tax bands and credits.",
                keyPoints: [
                    "Standard band (€44,300) taxed at 20%",
                    "Income above standard band taxed at 40%",
                    "Tax Credits reduce total tax owed",
                    "Net Pay = Gross − (Tax After Credits)"
                ],
                examples: [
                    {
                        question: "€56,000 income, €3,300 credits?",
                        answer: "Tax: €44,300×20% + €11,700×40% = €8,860 + €4,680 = €13,540. After credits: €10,240"
                    }
                ],
                tip: "💡 SEC 2022 HL Q1(b) style! Split income into two parts: standard band and higher band."
            },
            12: {
                title: "Level 12: USC & Complex Tax",
                band: "Mastery",
                description: "Calculate USC with multiple bands.",
                keyPoints: [
                    "USC Band 1: First €12,012 at 0.5%",
                    "USC Band 2: Next €10,908 at 2%",
                    "USC Band 3: Above €22,920 at 4%",
                    "Total deductions = Income Tax + USC + PRSI"
                ],
                examples: [
                    {
                        question: "USC on €30,000?",
                        answer: "€12,012×0.5% + €10,908×2% + €7,080×4% = €60.06 + €218.16 + €283.20 = €561.42"
                    }
                ],
                tip: "🏆 SEC 2023 HL Q10 style! You've mastered Financial Maths!"
            }
        };
        
        // Currency Help Content (12 levels)
        const currencyHelpContent = {
            1: {
                title: "Level 1: Understanding Exchange Rates",
                band: "Foundation",
                description: "Learn what exchange rates mean and how to read them.",
                keyPoints: [
                    "€1 = £0.90 means 1 euro equals 0.90 pounds",
                    "The euro (€) is used in Ireland",
                    "The pound (£) is used in the UK",
                    "The dollar ($) is used in the USA"
                ],
                examples: [
                    {
                        question: "What does €1 = £0.85 mean?",
                        answer: "1 euro can be exchanged for 0.85 British pounds"
                    }
                ],
                tip: "💡 The exchange board tells you how much foreign currency you get for €1."
            },
            2: {
                title: "Level 2: Euro to Sterling (Simple)",
                band: "Foundation",
                description: "Convert euro to British pounds using simple multiplication.",
                keyPoints: [
                    "To convert € to £: Multiply by the rate",
                    "€100 at €1 = £0.90 gives £90",
                    "Higher rate = more pounds for your euros",
                    "Always multiply euro amount by rate"
                ],
                examples: [
                    {
                        question: "€50 to £ at €1 = £0.85?",
                        answer: "€50 × 0.85 = £42.50"
                    }
                ],
                tip: "💡 Think: Euro × Rate = Pounds"
            },
            3: {
                title: "Level 3: Euro to Dollar (Simple)",
                band: "Foundation",
                description: "Convert euro to US dollars.",
                keyPoints: [
                    "€ to $ conversion: Multiply by rate",
                    "Rates like €1 = $1.15 mean euros buy MORE dollars",
                    "€100 at €1 = $1.20 gives $120",
                    "The dollar rate is usually above 1.00"
                ],
                examples: [
                    {
                        question: "€200 to $ at €1 = $1.15?",
                        answer: "€200 × 1.15 = $230"
                    }
                ],
                tip: "💡 SEC 2022 HL Q1(a) style! Multiply euros by the rate."
            },
            4: {
                title: "Level 4: Decimal Amounts",
                band: "Ordinary",
                description: "Convert amounts with decimals, round to nearest cent.",
                keyPoints: [
                    "Same method: Multiply by rate",
                    "Round to 2 decimal places (nearest cent)",
                    "€157.50 × 0.87 = £137.025 ≈ £137.03",
                    "Always show 2 decimal places for money"
                ],
                examples: [
                    {
                        question: "€245.80 to £ at €1 = £0.88?",
                        answer: "€245.80 × 0.88 = £216.30"
                    }
                ],
                tip: "💡 Round to nearest cent (2 decimal places)."
            },
            5: {
                title: "Level 5: Reverse Conversion (£ to €)",
                band: "Ordinary",
                description: "Convert British pounds back to euro by dividing.",
                keyPoints: [
                    "To convert £ to €: DIVIDE by rate",
                    "This is the reverse operation",
                    "£50 at €1 = £0.90 means €50 ÷ 0.90 = €55.56",
                    "SEC 2022 OL Q3(d) style question"
                ],
                examples: [
                    {
                        question: "£15.95 to € at €1 = £0.90?",
                        answer: "£15.95 ÷ 0.90 = €17.72"
                    }
                ],
                tip: "💡 SEC 2022 OL Q3(d) style! To go backwards, DIVIDE by the rate."
            },
            6: {
                title: "Level 6: Dollar Both Ways",
                band: "Ordinary",
                description: "Convert between euro and dollars in both directions.",
                keyPoints: [
                    "€ to $: Multiply by rate",
                    "$ to €: Divide by rate",
                    "Rate €1 = $1.20 means euros worth more",
                    "SEC 2022 HL Q1(a) style"
                ],
                examples: [
                    {
                        question: "€350 to $ at €1 = $1.20?",
                        answer: "€350 × 1.20 = $420"
                    },
                    {
                        question: "$240 to € at €1 = $1.20?",
                        answer: "$240 ÷ 1.20 = €200"
                    }
                ],
                tip: "💡 € to foreign = multiply. Foreign to € = divide."
            },
            7: {
                title: "Level 7: Price Comparison",
                band: "Higher",
                description: "Compare prices in different currencies to find better value.",
                keyPoints: [
                    "Convert both prices to SAME currency",
                    "Usually convert foreign price to euro",
                    "Then compare directly",
                    "SEC 2025 OL Q12(c) style"
                ],
                examples: [
                    {
                        question: "Pizza: €14 in Dublin, £12 in London. Rate €1 = £0.93. Which is cheaper?",
                        answer: "£12 ÷ 0.93 = €12.90. Dublin (€14) is more expensive. London is cheaper by €1.10"
                    }
                ],
                tip: "💡 SEC 2025 OL Q12(c) style! Convert to same currency first."
            },
            8: {
                title: "Level 8: Multi-step Problems",
                band: "Higher",
                description: "Solve problems involving conversion then calculation.",
                keyPoints: [
                    "Convert currency first",
                    "Then do the calculation (add, subtract, etc.)",
                    "Budget problems: Convert spending to euro",
                    "Check if you can afford items"
                ],
                examples: [
                    {
                        question: "You have €200 and £50. Rate €1 = £0.90. Total in euro?",
                        answer: "£50 ÷ 0.90 = €55.56. Total = €200 + €55.56 = €255.56"
                    }
                ],
                tip: "💡 Break into steps: Convert first, then calculate."
            },
            9: {
                title: "Level 9: Best Exchange Rate",
                band: "Higher",
                description: "Compare exchange rates to find the best deal.",
                keyPoints: [
                    "Higher rate = more foreign currency per euro",
                    "Compare: €1 = £0.90 vs €1 = £0.87",
                    "0.90 is better (you get more pounds)",
                    "Calculate difference for large amounts"
                ],
                examples: [
                    {
                        question: "Bank A: €1 = £0.88, Bank B: €1 = £0.92. Better for €500?",
                        answer: "Bank B gives €500 × 0.92 = £460 vs £440. Bank B is £20 better."
                    }
                ],
                tip: "💡 For € to £/$: Higher rate = better deal."
            },
            10: {
                title: "Level 10: Commission & Fees",
                band: "Application",
                description: "Calculate currency exchange with fees deducted.",
                keyPoints: [
                    "Flat fee: Subtract before converting",
                    "Commission %: Calculate and subtract",
                    "Compare: Good rate + fee vs bad rate + no fee",
                    "Sometimes no-fee option is better!"
                ],
                examples: [
                    {
                        question: "€300 with €5 fee at €1 = £0.90?",
                        answer: "(€300 - €5) × 0.90 = €295 × 0.90 = £265.50"
                    }
                ],
                tip: "💡 Subtract fee first, then convert the remainder."
            },
            11: {
                title: "Level 11: Travel Budget",
                band: "Application",
                description: "Plan travel budgets with currency conversion.",
                keyPoints: [
                    "Daily budget × days = total needed",
                    "Convert total to euro to know how much to bring",
                    "Return trip: Convert leftover back",
                    "Rate may change between trips"
                ],
                examples: [
                    {
                        question: "5 days in UK, £60/day budget. Rate €1 = £0.90. Euro needed?",
                        answer: "Total: 5 × £60 = £300. In euro: £300 ÷ 0.90 = €333.33"
                    }
                ],
                tip: "💡 Calculate total foreign currency needed, then convert to euro."
            },
            12: {
                title: "Level 12: Complex Multi-Currency",
                band: "Mastery",
                description: "Advanced problems with multiple currencies and cross rates.",
                keyPoints: [
                    "Cross rate: Use two rates to find a third",
                    "Rate changes affect your money",
                    "Buy/sell rates may differ",
                    "Profit/loss from rate changes"
                ],
                examples: [
                    {
                        question: "If €1 = £0.85 and €1 = $1.15, what is £1 in $?",
                        answer: "£1 = €1.18 (1÷0.85), €1.18 = $1.36 (1.18×1.15). So £1 = $1.35"
                    }
                ],
                tip: "🏆 You've mastered Currency! Cross rates use two conversions."
            }
        };
        
        // Speed, Distance & Time Help Content (12 levels)
        const speedDistanceTimeHelpContent = {
            1: {
                title: "Level 1: Understanding the Formula",
                band: "Foundation",
                description: "Learn the Speed-Distance-Time triangle.",
                keyPoints: [
                    "Speed = Distance ÷ Time",
                    "Distance = Speed × Time",
                    "Time = Distance ÷ Speed",
                    "Use the triangle: cover what you want to find"
                ],
                examples: [
                    {
                        question: "A car travels 60 km in 2 hours. What is its speed?",
                        answer: "Speed = 60 ÷ 2 = 30 km/h"
                    }
                ],
                tip: "Remember the triangle: D at the top, S and T at the bottom. Cover what you want to find!"
            },
            2: {
                title: "Level 2: Finding Speed",
                band: "Foundation",
                description: "Calculate speed from distance and time.",
                keyPoints: [
                    "Speed = Distance ÷ Time",
                    "Units: km/h means kilometres per hour",
                    "Answer should make sense (cars ~50-120 km/h)"
                ],
                examples: [
                    {
                        question: "Journey of 150 km takes 3 hours. Speed?",
                        answer: "Speed = 150 ÷ 3 = 50 km/h"
                    }
                ],
                tip: "Speed tells you how far you travel in one hour (or one second, etc.)."
            },
            3: {
                title: "Level 3: Finding Distance & Time",
                band: "Foundation",
                description: "Calculate distance or time given the other values.",
                keyPoints: [
                    "Distance = Speed × Time",
                    "Time = Distance ÷ Speed",
                    "Check: Distance should increase with time"
                ],
                examples: [
                    {
                        question: "Travelling at 60 km/h for 3 hours. Distance?",
                        answer: "Distance = 60 × 3 = 180 km"
                    }
                ],
                tip: "Use the triangle: cover D (multiply S×T) or cover T (divide D÷S)."
            },
            4: {
                title: "Level 4: Time in Minutes",
                band: "Ordinary",
                description: "SEC 2024 OL Q4 style - convert minutes to hours.",
                keyPoints: [
                    "Convert minutes to hours: divide by 60",
                    "45 minutes = 45/60 = 0.75 hours",
                    "Then use Speed = Distance ÷ Time (in hours)",
                    "Answer in km/h (kilometres PER HOUR)"
                ],
                examples: [
                    {
                        question: "60 km in 45 minutes. Speed in km/h?",
                        answer: "Time = 45÷60 = 0.75 hours. Speed = 60÷0.75 = 80 km/h"
                    }
                ],
                tip: "SEC 2024 OL Q4 style! Always convert minutes to hours first when finding speed in km/h."
            },
            5: {
                title: "Level 5: Different Units (m/s, m/min)",
                band: "Ordinary",
                description: "SEC 2022 OL Q3(b) style - metres per minute/second.",
                keyPoints: [
                    "m/s = metres per second",
                    "m/min = metres per minute",
                    "To convert km/h to m/s: divide by 3.6",
                    "Match your units: metres with metres, etc."
                ],
                examples: [
                    {
                        question: "Swim 250 m in 5 minutes. Speed in m/min?",
                        answer: "Speed = 250 ÷ 5 = 50 m/min"
                    }
                ],
                tip: "SEC 2022 OL Q3(b) style! Keep your units consistent."
            },
            6: {
                title: "Level 6: Time in Hours & Minutes",
                band: "Ordinary",
                description: "Express time answers in hours and minutes.",
                keyPoints: [
                    "0.5 hours = 30 minutes",
                    "0.75 hours = 45 minutes",
                    "Multiply decimal by 60 to get minutes",
                    "1.5 hours = 1 hour 30 minutes"
                ],
                examples: [
                    {
                        question: "Travel 120 km at 80 km/h. Time?",
                        answer: "Time = 120÷80 = 1.5 hours = 1 hour 30 minutes"
                    }
                ],
                tip: "Convert decimal hours to minutes by multiplying by 60."
            },
            7: {
                title: "Level 7: Flight Problems",
                band: "Higher",
                description: "SEC 2023 HL Q8(c)(ii) style - flight times in minutes.",
                keyPoints: [
                    "Flight times often given in minutes",
                    "Convert to hours before calculating",
                    "Flight speeds: typically 400-900 km/h",
                    "Be careful with decimals"
                ],
                examples: [
                    {
                        question: "Flight: 360 km in 45 minutes. Speed?",
                        answer: "Time = 45÷60 = 0.75 hours. Speed = 360÷0.75 = 480 km/h"
                    }
                ],
                tip: "SEC 2023 HL Q8(c)(ii) style! Flight problems need careful unit conversion."
            },
            8: {
                title: "Level 8: Cycling & Running",
                band: "Higher",
                description: "SEC 2025 OL Q13(a) style - short journey times.",
                keyPoints: [
                    "Cycling speeds: 12-30 km/h",
                    "Running speeds: 8-15 km/h",
                    "Walking speeds: 4-6 km/h",
                    "Short times in minutes - convert!"
                ],
                examples: [
                    {
                        question: "Cycle 3 km in 10 minutes. Speed in km/h?",
                        answer: "Time = 10÷60 = 1/6 hour. Speed = 3÷(1/6) = 18 km/h"
                    }
                ],
                tip: "SEC 2025 OL Q13(a) style! Check your answer makes sense for the activity."
            },
            9: {
                title: "Level 9: Two-Part Journeys",
                band: "Higher",
                description: "Calculate average speed for whole journeys.",
                keyPoints: [
                    "Average speed = Total distance ÷ Total time",
                    "You CANNOT just average two speeds!",
                    "Find time for each part separately",
                    "Add distances and add times"
                ],
                examples: [
                    {
                        question: "100 km at 50 km/h, then 100 km at 100 km/h. Average speed?",
                        answer: "Time 1: 2h, Time 2: 1h. Total: 200 km in 3h = 66.7 km/h (NOT 75!)"
                    }
                ],
                tip: "Common mistake: averaging speeds. Always use Total Distance ÷ Total Time!"
            },
            10: {
                title: "Level 10: Catching Up Problems",
                band: "Application",
                description: "SEC 2022 HL Q10 style - when does someone catch up?",
                keyPoints: [
                    "Head start distance = speed × head start time",
                    "Closing speed = faster speed - slower speed",
                    "Time to catch up = Head start ÷ Closing speed",
                    "Meeting point problems similar logic"
                ],
                examples: [
                    {
                        question: "A runs at 10 km/h, B starts 30 min later at 15 km/h. When does B catch A?",
                        answer: "A's head start: 10×0.5 = 5 km. Closing speed: 15-10 = 5 km/h. Time: 5÷5 = 1 hour"
                    }
                ],
                tip: "SEC 2022 HL Q10 style! Draw a diagram to help visualize the problem."
            },
            11: {
                title: "Level 11: Distance-Time Graphs",
                band: "Application",
                description: "SEC 2025 OL Q13(b) style - interpret and analyse graphs.",
                keyPoints: [
                    "Horizontal line = stationary (not moving)",
                    "Steeper line = faster speed",
                    "Gradient = speed",
                    "Return journey: line goes back to zero"
                ],
                examples: [
                    {
                        question: "Which is faster: going or returning?",
                        answer: "Compare the steepness (gradient). Steeper = faster."
                    }
                ],
                tip: "SEC 2025 OL Q13(b) style! Horizontal = stopped. Steeper = faster."
            },
            12: {
                title: "Level 12: Complex Problems",
                band: "Mastery",
                description: "Multi-step real-world speed problems.",
                keyPoints: [
                    "Break complex problems into steps",
                    "Required speed to arrive on time",
                    "Account for delays",
                    "Calculate arrival times"
                ],
                examples: [
                    {
                        question: "Left 15 min late for 100 km trip, usually takes 2 hours. Speed needed?",
                        answer: "Time available: 2h - 0.25h = 1.75h. Speed: 100÷1.75 = 57.1 km/h"
                    }
                ],
                tip: "🏆 You've mastered Speed, Distance & Time! Always check your answer is realistic."
            }
        };
        
        // Combined help content by topic
        
        // Indices & Scientific Notation Help Content (12 levels)
        const indicesHelpContent = {
            1: {
                title: "Level 1: Index Notation",
                band: "Foundation",
                description: "Understand what indices (powers) mean.",
                keyPoints: [
                    "2³ means 2 × 2 × 2 (2 multiplied 3 times)",
                    "The base is the number being multiplied",
                    "The index/exponent tells you how many times",
                    "Read 5⁴ as '5 to the power of 4'"
                ],
                examples: [
                    {
                        question: "Write 3 × 3 × 3 × 3 using index notation",
                        answer: "3⁴ (base 3, exponent 4)"
                    }
                ],
                tip: "💡 The small number (index) tells you how many times to multiply the base!"
            },
            2: {
                title: "Level 2: Squares and Cubes",
                band: "Foundation",
                description: "Calculate squares (²) and cubes (³).",
                keyPoints: [
                    "Square: n² = n × n",
                    "Cube: n³ = n × n × n",
                    "Perfect squares: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100...",
                    "Perfect cubes: 1, 8, 27, 64, 125..."
                ],
                examples: [
                    {
                        question: "Calculate 7²",
                        answer: "7² = 7 × 7 = 49"
                    }
                ],
                tip: "💡 Learn your square numbers up to 12² = 144!"
            },
            3: {
                title: "Level 3: Multiplying Powers",
                band: "Foundation",
                description: "Multiply powers with the same base - ADD the indices.",
                keyPoints: [
                    "aᵐ × aⁿ = aᵐ⁺ⁿ",
                    "Keep the base, ADD the powers",
                    "Only works when bases are the SAME",
                    "Example: 2³ × 2⁴ = 2⁷"
                ],
                examples: [
                    {
                        question: "Simplify: x⁵ × x³",
                        answer: "x⁵⁺³ = x⁸"
                    }
                ],
                tip: "💡 Same base? Multiplying? ADD the powers!"
            },
            4: {
                title: "Level 4: Dividing Powers",
                band: "Ordinary",
                description: "Divide powers with the same base - SUBTRACT the indices.",
                keyPoints: [
                    "aᵐ ÷ aⁿ = aᵐ⁻ⁿ",
                    "Keep the base, SUBTRACT the powers",
                    "Top power minus bottom power",
                    "Example: 5⁸ ÷ 5³ = 5⁵"
                ],
                examples: [
                    {
                        question: "Simplify: y⁷ ÷ y²",
                        answer: "y⁷⁻² = y⁵"
                    }
                ],
                tip: "💡 Same base? Dividing? SUBTRACT the powers!"
            },
            5: {
                title: "Level 5: Power of a Power",
                band: "Ordinary",
                description: "Raise a power to another power - MULTIPLY the indices.",
                keyPoints: [
                    "(aᵐ)ⁿ = aᵐˣⁿ",
                    "MULTIPLY the powers together",
                    "Example: (2³)⁴ = 2¹²",
                    "Brackets mean 'all of this' to the power"
                ],
                examples: [
                    {
                        question: "Simplify: (x²)⁵",
                        answer: "(x²)⁵ = x²ˣ⁵ = x¹⁰"
                    }
                ],
                tip: "💡 Power of a power? MULTIPLY the indices!"
            },
            6: {
                title: "Level 6: Zero & Negative Indices",
                band: "Ordinary",
                description: "Understand a⁰ = 1 and negative powers.",
                keyPoints: [
                    "a⁰ = 1 (any number to power 0 is 1)",
                    "a⁻ⁿ = 1/aⁿ (flip to a fraction)",
                    "Negative power = reciprocal",
                    "Example: 2⁻³ = 1/2³ = 1/8"
                ],
                examples: [
                    {
                        question: "Simplify: 5⁻²",
                        answer: "5⁻² = 1/5² = 1/25"
                    }
                ],
                tip: "💡 Negative power? Flip it to a fraction!"
            },
            7: {
                title: "Level 7: Fractional Indices",
                band: "Higher",
                description: "Fractional powers mean roots.",
                keyPoints: [
                    "a^(1/2) = √a (square root)",
                    "a^(1/3) = ³√a (cube root)",
                    "a^(1/n) = ⁿ√a (nth root)",
                    "a^(m/n) = (ⁿ√a)ᵐ or ⁿ√(aᵐ)"
                ],
                examples: [
                    {
                        question: "Calculate 16^(1/2)",
                        answer: "16^(1/2) = √16 = 4"
                    }
                ],
                tip: "💡 Fractional index? The bottom number is the root!"
            },
            8: {
                title: "Level 8: Scientific Notation (Large)",
                band: "Higher",
                description: "Write large numbers in scientific notation.",
                keyPoints: [
                    "Format: a × 10ⁿ where 1 ≤ a < 10",
                    "Count digits after first to find exponent",
                    "3,500,000 = 3.5 × 10⁶",
                    "Positive exponent = large number"
                ],
                examples: [
                    {
                        question: "Write 45,000,000 in scientific notation",
                        answer: "4.5 × 10⁷"
                    }
                ],
                tip: "💡 Move the decimal point left, count the moves = exponent!"
            },
            9: {
                title: "Level 9: Scientific Notation (Small)",
                band: "Higher",
                description: "Write small numbers in scientific notation.",
                keyPoints: [
                    "Negative exponent = small number (< 1)",
                    "0.00045 = 4.5 × 10⁻⁴",
                    "Count decimal places to find exponent",
                    "Move decimal right, exponent is negative"
                ],
                examples: [
                    {
                        question: "Write 0.000072 in scientific notation",
                        answer: "7.2 × 10⁻⁵"
                    }
                ],
                tip: "💡 Small number? Move decimal right, use negative exponent!"
            },
            10: {
                title: "Level 10: Calculations in Scientific Notation",
                band: "Mastery",
                description: "Multiply and divide in scientific notation.",
                keyPoints: [
                    "Multiply: multiply mantissas, ADD exponents",
                    "Divide: divide mantissas, SUBTRACT exponents",
                    "Adjust if mantissa ≥ 10 or < 1",
                    "(2 × 10³) × (3 × 10⁴) = 6 × 10⁷"
                ],
                examples: [
                    {
                        question: "(4 × 10⁵) × (2 × 10³)",
                        answer: "8 × 10⁸"
                    }
                ],
                tip: "💡 Multiply/divide the numbers, add/subtract the powers!"
            },
            11: {
                title: "Level 11: Mixed Index Problems",
                band: "Mastery",
                description: "Combine multiple index laws in one problem.",
                keyPoints: [
                    "Apply laws in correct order",
                    "Power of power before multiply/divide",
                    "Watch for negative and fractional indices",
                    "Simplify step by step"
                ],
                examples: [
                    {
                        question: "Simplify: (x³)² × x⁴",
                        answer: "x⁶ × x⁴ = x¹⁰"
                    }
                ],
                tip: "💡 Work step by step: brackets first, then combine!"
            },
            12: {
                title: "Level 12: Problem Solving",
                band: "Mastery",
                description: "Apply indices to real-world problems.",
                keyPoints: [
                    "Population doubling: P × 2ⁿ",
                    "Computing: powers of 2 (bytes, bits)",
                    "Scientific measurements use scientific notation",
                    "Area = side², Volume = side³"
                ],
                examples: [
                    {
                        question: "Bacteria doubles 4 times from 100. Final count?",
                        answer: "100 × 2⁴ = 100 × 16 = 1,600"
                    }
                ],
                tip: "🏆 You've mastered Indices! Powers are everywhere in science and computing."
            }
        };
        
        // Geometry Help Content (12 levels)
        const geometryHelpContent = {
            1: {
                title: "Level 1: Naming Shapes & Properties",
                band: "Foundation",
                description: "Learn to identify and name basic 2D shapes.",
                keyPoints: [
                    "Triangle = 3 sides, Quadrilateral = 4 sides",
                    "Pentagon = 5 sides, Hexagon = 6 sides",
                    "Acute angle < 90°, Right angle = 90°, Obtuse > 90°",
                    "Equilateral = all sides equal, Isosceles = two sides equal"
                ],
                examples: [
                    {
                        question: "How many sides does an octagon have?",
                        answer: "8 sides (oct = 8)"
                    }
                ],
                tip: "💡 Remember: tri = 3, quad = 4, pent = 5, hex = 6, oct = 8!"
            },
            2: {
                title: "Level 2: Angle Sum of Triangle",
                band: "Foundation",
                description: "The angles in any triangle always add up to 180°.",
                keyPoints: [
                    "Angle sum of a triangle = 180°",
                    "To find a missing angle: 180° - other two angles",
                    "Equilateral triangle: all angles = 60°",
                    "Right-angled triangle: one angle = 90°"
                ],
                examples: [
                    {
                        question: "A triangle has angles 56° and 72°. Find the third angle.",
                        answer: "180° - 56° - 72° = 52°"
                    }
                ],
                tip: "💡 Always check your answer: do all three angles add to 180°?"
            },
            3: {
                title: "Level 3: Properties of Quadrilaterals",
                band: "Foundation",
                description: "Learn the properties of squares, rectangles, parallelograms, and more.",
                keyPoints: [
                    "Angle sum of quadrilateral = 360°",
                    "Rectangle: 4 right angles, opposite sides equal",
                    "Parallelogram: opposite angles equal, adjacent angles add to 180°",
                    "Square: 4 equal sides AND 4 right angles"
                ],
                examples: [
                    {
                        question: "In a parallelogram, one angle is 70°. Find the adjacent angle.",
                        answer: "180° - 70° = 110° (adjacent angles are supplementary)"
                    }
                ],
                tip: "💡 A square is a special rectangle AND a special rhombus!"
            },
            4: {
                title: "Level 4: Angles with Parallel Lines",
                band: "Ordinary",
                description: "Corresponding, alternate, and co-interior angles with parallel lines.",
                keyPoints: [
                    "Corresponding angles are EQUAL (F-shape)",
                    "Alternate angles are EQUAL (Z-shape)",
                    "Co-interior angles ADD to 180° (C-shape or U-shape)",
                    "Look for the transversal cutting the parallel lines"
                ],
                examples: [
                    {
                        question: "Parallel lines cut by transversal. One angle is 65°. Find the alternate angle.",
                        answer: "65° (alternate angles are equal)"
                    }
                ],
                tip: "💡 Remember: corresponding (F), alternate (Z), co-interior (C or U)!"
            },
            5: {
                title: "Level 5: Symmetry & Transformations",
                band: "Ordinary",
                description: "Line symmetry, rotational symmetry, and transformations.",
                keyPoints: [
                    "Square: 4 lines of symmetry, order 4 rotational symmetry",
                    "Rectangle: 2 lines of symmetry, order 2 rotational symmetry",
                    "Equilateral triangle: 3 lines of symmetry",
                    "Reflection flips, rotation turns, translation slides"
                ],
                examples: [
                    {
                        question: "How many lines of symmetry does a regular hexagon have?",
                        answer: "6 lines of symmetry"
                    }
                ],
                tip: "💡 Regular shapes have as many lines of symmetry as they have sides!"
            },
            6: {
                title: "Level 6: Basic Constructions",
                band: "Ordinary",
                description: "Construct angles and shapes using compass and ruler only.",
                keyPoints: [
                    "60° angle: use equilateral triangle construction",
                    "Perpendicular bisector: arcs from both endpoints",
                    "Angle bisector: arc from vertex, then equal arcs",
                    "No measuring allowed - only compass and straight edge"
                ],
                examples: [
                    {
                        question: "How do you construct a 60° angle?",
                        answer: "Draw an arc from the vertex, then the same radius arc from where it crosses - this creates an equilateral triangle"
                    }
                ],
                tip: "💡 For constructions, the compass radius often stays the same throughout!"
            },
            7: {
                title: "Level 7: Pythagoras' Theorem",
                band: "Higher",
                description: "Find missing sides in right-angled triangles.",
                keyPoints: [
                    "a² + b² = c² (where c is the hypotenuse)",
                    "Hypotenuse = longest side, opposite the right angle",
                    "To find hypotenuse: √(a² + b²)",
                    "To find a shorter side: √(c² - other side²)"
                ],
                examples: [
                    {
                        question: "Right triangle with sides 3cm and 4cm. Find the hypotenuse.",
                        answer: "√(3² + 4²) = √(9 + 16) = √25 = 5cm"
                    }
                ],
                tip: "💡 Learn the common Pythagorean triples: 3-4-5, 5-12-13, 8-15-17!"
            },
            8: {
                title: "Level 8: Similar Triangles",
                band: "Higher",
                description: "Triangles with equal angles have proportional sides.",
                keyPoints: [
                    "Similar = same shape, different size",
                    "All corresponding angles are equal",
                    "Sides are in the same ratio (scale factor)",
                    "To find missing side: use the scale factor"
                ],
                examples: [
                    {
                        question: "Triangle ABC ~ DEF. |AB| = 4cm, |DE| = 12cm, |BC| = 5cm. Find |EF|.",
                        answer: "Scale factor = 12/4 = 3. |EF| = 5 × 3 = 15cm"
                    }
                ],
                tip: "💡 Find the scale factor first, then multiply or divide to find missing sides!"
            },
            9: {
                title: "Level 9: Scale Drawings",
                band: "Higher",
                description: "Work with maps, plans, and scale diagrams.",
                keyPoints: [
                    "Scale 1:100 means 1cm represents 100cm (1m)",
                    "Drawing to actual: multiply by scale factor",
                    "Actual to drawing: divide by scale factor",
                    "Perimeter scales linearly, area scales by square"
                ],
                examples: [
                    {
                        question: "Scale 1:50. Drawing shows 6cm. What is the actual length?",
                        answer: "6 × 50 = 300cm = 3m"
                    }
                ],
                tip: "💡 Write the scale as 'Drawing : Actual' to help with calculations!"
            },
            10: {
                title: "Level 10: Circle Properties",
                band: "Mastery",
                description: "Circle terminology and important theorems.",
                keyPoints: [
                    "Diameter = 2 × radius",
                    "Angle in a semicircle = 90° (Thales' theorem)",
                    "Tangent meets radius at 90°",
                    "Perpendicular from centre bisects a chord"
                ],
                examples: [
                    {
                        question: "A circle has radius 7cm. What is the diameter?",
                        answer: "Diameter = 2 × 7 = 14cm"
                    }
                ],
                tip: "💡 The angle in a semicircle is ALWAYS 90° - very useful for problem solving!"
            },
            11: {
                title: "Level 11: Advanced Constructions",
                band: "Mastery",
                description: "Divide segments, construct perpendiculars, find triangle centres.",
                keyPoints: [
                    "Divide line into n parts: use parallel lines method",
                    "Circumcentre: where perpendicular bisectors meet",
                    "Incentre: where angle bisectors meet",
                    "Centroid: where medians meet (divides each 2:1)"
                ],
                examples: [
                    {
                        question: "How do you find the centre of the circumcircle?",
                        answer: "Construct perpendicular bisectors of two sides - they meet at the circumcentre"
                    }
                ],
                tip: "💡 The circumcentre is equidistant from all three vertices!"
            },
            12: {
                title: "Level 12: Problem Solving & Proofs",
                band: "Mastery",
                description: "Multi-step geometry problems and justifying answers.",
                keyPoints: [
                    "External angle = sum of non-adjacent interior angles",
                    "AA (Angle-Angle) proves triangles are similar",
                    "SSS, SAS, ASA, RHS prove triangles are congruent",
                    "Always justify your answers with geometric reasons"
                ],
                examples: [
                    {
                        question: "Triangle has interior angles 40° and 65°. Find the exterior angle at the third vertex.",
                        answer: "40° + 65° = 105° (exterior = sum of non-adjacent interior)"
                    }
                ],
                tip: "💡 In proofs, always state the theorem or property you're using!"
            }
        };

        // Number Systems Help Content (12 levels)
        const numberSystemsHelpContent = {
            1: {
                title: "Level 1: Understanding Integers",
                band: "Foundation",
                description: "Learn what integers are and how to classify them.",
                keyPoints: [
                    "Integers include: ..., -3, -2, -1, 0, 1, 2, 3, ...",
                    "Positive integers: greater than 0 (1, 2, 3, ...)",
                    "Negative integers: less than 0 (-1, -2, -3, ...)",
                    "Zero is neither positive nor negative"
                ],
                examples: [
                    {
                        question: "Is -5 a positive or negative integer?",
                        answer: "Negative integer (less than 0)"
                    }
                ],
                tip: "💡 Think of a thermometer: above 0 is positive, below 0 is negative!"
            },
            2: {
                title: "Level 2: Number Line & Ordering",
                band: "Foundation",
                description: "Use the number line to compare and order integers.",
                keyPoints: [
                    "Numbers increase from left to right on the number line",
                    "Numbers further right are larger",
                    "−3 < −1 < 0 < 2 < 5",
                    "Ascending = smallest to largest, Descending = largest to smallest"
                ],
                examples: [
                    {
                        question: "Which is larger: -3 or -7?",
                        answer: "-3 (it's further right on the number line)"
                    }
                ],
                tip: "💡 On the number line, right is greater! -2 is greater than -10."
            },
            3: {
                title: "Level 3: Adding Integers",
                band: "Foundation",
                description: "Add positive and negative numbers.",
                keyPoints: [
                    "Adding two positives: answer is positive",
                    "Adding two negatives: answer is negative (add and keep sign)",
                    "Adding positive and negative: subtract and keep sign of larger",
                    "Adding a negative is like subtracting"
                ],
                examples: [
                    {
                        question: "Calculate: 5 + (-3)",
                        answer: "5 + (-3) = 5 - 3 = 2"
                    }
                ],
                tip: "💡 Same signs: add and keep the sign. Different signs: subtract and keep sign of the larger!"
            },
            4: {
                title: "Level 4: Subtracting Integers",
                band: "Ordinary",
                description: "Subtract positive and negative numbers.",
                keyPoints: [
                    "Subtracting a positive: move left on number line",
                    "Subtracting a negative = adding a positive",
                    "Two negatives together make a plus: 5 - (-3) = 5 + 3 = 8",
                    "Change subtraction to addition of the opposite"
                ],
                examples: [
                    {
                        question: "Calculate: 4 - (-6)",
                        answer: "4 - (-6) = 4 + 6 = 10"
                    }
                ],
                tip: "💡 'Minus a minus is a plus!' Two negatives make a positive."
            },
            5: {
                title: "Level 5: Multiplying Integers",
                band: "Ordinary",
                description: "Multiply positive and negative numbers.",
                keyPoints: [
                    "Positive × Positive = Positive",
                    "Negative × Negative = Positive",
                    "Positive × Negative = Negative",
                    "Negative × Positive = Negative"
                ],
                examples: [
                    {
                        question: "Calculate: (-4) × (-3)",
                        answer: "(-4) × (-3) = 12 (negative × negative = positive)"
                    }
                ],
                tip: "💡 Same signs → Positive result. Different signs → Negative result."
            },
            6: {
                title: "Level 6: Dividing Integers",
                band: "Ordinary",
                description: "Divide positive and negative numbers.",
                keyPoints: [
                    "Same sign rules as multiplication",
                    "Positive ÷ Positive = Positive",
                    "Negative ÷ Negative = Positive",
                    "Different signs = Negative"
                ],
                examples: [
                    {
                        question: "Calculate: (-20) ÷ (-4)",
                        answer: "(-20) ÷ (-4) = 5 (negative ÷ negative = positive)"
                    }
                ],
                tip: "💡 Division follows the same sign rules as multiplication!"
            },
            7: {
                title: "Level 7: Order of Operations (BIMDAS)",
                band: "Higher",
                description: "Apply order of operations with integers.",
                keyPoints: [
                    "B - Brackets first",
                    "I - Indices (powers)",
                    "M/D - Multiplication and Division (left to right)",
                    "A/S - Addition and Subtraction (left to right)"
                ],
                examples: [
                    {
                        question: "Calculate: 3 × 4 + 2",
                        answer: "Multiply first: 12 + 2 = 14"
                    }
                ],
                tip: "💡 BIMDAS tells you the order. Brackets and Indices before Multiply/Divide before Add/Subtract!"
            },
            8: {
                title: "Level 8: Absolute Value",
                band: "Higher",
                description: "Understand and calculate absolute value.",
                keyPoints: [
                    "|x| means the distance from x to 0",
                    "Absolute value is always positive or zero",
                    "|5| = 5 and |-5| = 5",
                    "If |x| = 3, then x = 3 or x = -3"
                ],
                examples: [
                    {
                        question: "What is |-7|?",
                        answer: "|-7| = 7 (distance from -7 to 0)"
                    }
                ],
                tip: "💡 Absolute value = distance from zero. Distance is always positive!"
            },
            9: {
                title: "Level 9: Factors & Multiples",
                band: "Higher",
                description: "Find factors and multiples of numbers.",
                keyPoints: [
                    "Factors divide exactly into a number",
                    "Factors of 12: 1, 2, 3, 4, 6, 12",
                    "Multiples are what you get when you multiply",
                    "Multiples of 5: 5, 10, 15, 20, 25..."
                ],
                examples: [
                    {
                        question: "Is 4 a factor of 20?",
                        answer: "Yes, because 20 ÷ 4 = 5 exactly"
                    }
                ],
                tip: "💡 Factors go INTO a number. Multiples come FROM a number."
            },
            10: {
                title: "Level 10: Prime Numbers",
                band: "Mastery",
                description: "Identify primes and find prime factorization.",
                keyPoints: [
                    "Prime number: exactly 2 factors (1 and itself)",
                    "First primes: 2, 3, 5, 7, 11, 13, 17, 19, 23...",
                    "1 is NOT prime (only 1 factor)",
                    "2 is the only even prime"
                ],
                examples: [
                    {
                        question: "Write 24 as a product of primes",
                        answer: "24 = 2 × 2 × 2 × 3"
                    }
                ],
                tip: "💡 Use a factor tree: keep splitting until all factors are prime!"
            },
            11: {
                title: "Level 11: HCF and LCM",
                band: "Mastery",
                description: "Calculate Highest Common Factor and Lowest Common Multiple.",
                keyPoints: [
                    "HCF: largest number that divides both exactly",
                    "LCM: smallest number both divide into exactly",
                    "HCF × LCM = product of the two numbers",
                    "HCF for equal parts, LCM for when things coincide"
                ],
                examples: [
                    {
                        question: "Find HCF of 12 and 18",
                        answer: "Common factors: 1, 2, 3, 6. HCF = 6"
                    }
                ],
                tip: "💡 HCF = sharing equally. LCM = when do events coincide?"
            },
            12: {
                title: "Level 12: Problem Solving",
                band: "Mastery",
                description: "Apply integer skills to real-world problems.",
                keyPoints: [
                    "Temperature changes can be positive or negative",
                    "Money: profit = positive, loss/debt = negative",
                    "Elevation: above sea level = positive, below = negative",
                    "Check your answer makes sense in context"
                ],
                examples: [
                    {
                        question: "Temp was -3°C, rose by 8°C. New temp?",
                        answer: "-3 + 8 = 5°C"
                    }
                ],
                tip: "🏆 You've mastered Integers! Use these skills in everyday situations."
            }
        };
        
        // Trigonometry Help Content (12 levels)
        const trigonometryHelpContent = {
            1: {
                title: "Level 1: Identifying Sides",
                band: "Foundation",
                description: "Learn to identify opposite, adjacent, and hypotenuse.",
                keyPoints: [
                    "Hypotenuse: longest side, opposite the right angle",
                    "Opposite: side across from the angle (not touching it)",
                    "Adjacent: side next to the angle (not the hypotenuse)",
                    "Sides depend on which angle you're looking at"
                ],
                examples: [
                    {
                        question: "Relative to angle θ, which side is opposite?",
                        answer: "The side across from θ, not touching it"
                    }
                ],
                tip: "💡 The hypotenuse never changes, but opposite and adjacent depend on your reference angle!"
            },
            2: {
                title: "Level 2: SOH CAH TOA",
                band: "Foundation",
                description: "Learn the three trigonometric ratios.",
                keyPoints: [
                    "Sin θ = Opposite / Hypotenuse (SOH)",
                    "Cos θ = Adjacent / Hypotenuse (CAH)",
                    "Tan θ = Opposite / Adjacent (TOA)",
                    "Remember: SOH CAH TOA"
                ],
                examples: [
                    {
                        question: "What is the formula for tan θ?",
                        answer: "Opposite / Adjacent"
                    }
                ],
                tip: "💡 SOH CAH TOA - Some Old Hens Can Always Hide Their Old Age!"
            },
            3: {
                title: "Level 3: Calculator Skills",
                band: "Foundation",
                description: "Use your calculator to find trig values.",
                keyPoints: [
                    "Make sure calculator is in DEGREE mode",
                    "sin, cos, tan buttons give ratios from angles",
                    "sin⁻¹, cos⁻¹, tan⁻¹ give angles from ratios",
                    "Round to 2 decimal places unless told otherwise"
                ],
                examples: [
                    {
                        question: "What is sin(30°)?",
                        answer: "0.5"
                    }
                ],
                tip: "💡 Check your calculator is in DEG mode, not RAD!"
            },
            4: {
                title: "Level 4: Finding Sides",
                band: "Ordinary",
                description: "Use trig ratios to find unknown sides.",
                keyPoints: [
                    "Choose the ratio that uses sides you know/need",
                    "Opp = Hyp × sin θ",
                    "Adj = Hyp × cos θ",
                    "Opp = Adj × tan θ"
                ],
                examples: [
                    {
                        question: "Hyp = 10, θ = 30°. Find opposite.",
                        answer: "Opp = 10 × sin(30°) = 10 × 0.5 = 5"
                    }
                ],
                tip: "💡 Label your triangle first: which side do you know, which do you need?"
            },
            5: {
                title: "Level 5: Finding Angles",
                band: "Ordinary",
                description: "Use inverse trig to find unknown angles.",
                keyPoints: [
                    "Use sin⁻¹ when you know Opp and Hyp",
                    "Use cos⁻¹ when you know Adj and Hyp",
                    "Use tan⁻¹ when you know Opp and Adj",
                    "Answer is always in degrees"
                ],
                examples: [
                    {
                        question: "Opp = 3, Adj = 4. Find angle θ.",
                        answer: "tan θ = 3/4 = 0.75. θ = tan⁻¹(0.75) = 37°"
                    }
                ],
                tip: "💡 The inverse function 'undoes' the trig function to find the angle!"
            },
            6: {
                title: "Level 6: Mixed Problems",
                band: "Ordinary",
                description: "Solve problems requiring multiple steps.",
                keyPoints: [
                    "Read carefully: what do you know, what do you need?",
                    "Choose the right ratio for your information",
                    "You may need to find one thing to find another",
                    "Check your answer makes sense"
                ],
                examples: [
                    {
                        question: "Find both sides of a right triangle with hyp = 10 and angle 40°",
                        answer: "Opp = 10×sin(40°) = 6.4, Adj = 10×cos(40°) = 7.7"
                    }
                ],
                tip: "💡 Draw the triangle, label what you know, then choose your ratio!"
            },
            7: {
                title: "Level 7: Elevation & Depression",
                band: "Higher",
                description: "Solve real-world problems with angles of elevation and depression.",
                keyPoints: [
                    "Angle of elevation: looking UP from horizontal",
                    "Angle of depression: looking DOWN from horizontal",
                    "Both create right triangles",
                    "Angle of depression = angle of elevation (alternate angles)"
                ],
                examples: [
                    {
                        question: "From 50m away, angle of elevation to top is 30°. Find height.",
                        answer: "height = 50 × tan(30°) = 28.9m"
                    }
                ],
                tip: "💡 Draw the horizontal line first, then the angle up (elevation) or down (depression)!"
            },
            8: {
                title: "Level 8: Multi-Step Problems",
                band: "Higher",
                description: "Problems requiring multiple calculations.",
                keyPoints: [
                    "May need Pythagoras first, then trig",
                    "May need to find angle, then use it",
                    "Break complex problems into steps",
                    "Keep track of intermediate answers"
                ],
                examples: [
                    {
                        question: "Find the perimeter of a right triangle with hyp = 13 and angle 30°",
                        answer: "Find both sides first, then add all three"
                    }
                ],
                tip: "💡 Break big problems into smaller steps. Solve one thing at a time!"
            },
            9: {
                title: "Level 9: Pythagoras & Trig Combined",
                band: "Higher",
                description: "Use both Pythagoras' theorem and trigonometry.",
                keyPoints: [
                    "Pythagoras: a² + b² = c²",
                    "Use Pythagoras to find missing sides",
                    "Then use trig to find angles",
                    "Check if sides form a right triangle: a² + b² = c²?"
                ],
                examples: [
                    {
                        question: "Do sides 5, 12, 13 form a right triangle?",
                        answer: "5² + 12² = 25 + 144 = 169 = 13² ✓ Yes!"
                    }
                ],
                tip: "💡 Pythagoras for sides, trig for angles!"
            },
            10: {
                title: "Level 10: Bearings",
                band: "Mastery",
                description: "Three-figure bearings and navigation.",
                keyPoints: [
                    "Bearings measured clockwise from North",
                    "Always written as 3 digits: 045°, 120°, 270°",
                    "Back bearing = bearing + 180° (or -180° if >180°)",
                    "N=000°, E=090°, S=180°, W=270°"
                ],
                examples: [
                    {
                        question: "What bearing is North-East?",
                        answer: "045°"
                    }
                ],
                tip: "💡 Always measure from North, always clockwise, always 3 digits!"
            },
            11: {
                title: "Level 11: Area Formula",
                band: "Mastery",
                description: "Calculate area using ½absinC.",
                keyPoints: [
                    "Area = ½ × a × b × sin(C)",
                    "a and b are two sides, C is the angle BETWEEN them",
                    "Works for any triangle, not just right-angled",
                    "Maximum area when C = 90° (sin 90° = 1)"
                ],
                examples: [
                    {
                        question: "Sides 8cm and 6cm, angle between = 30°. Find area.",
                        answer: "Area = ½ × 8 × 6 × sin(30°) = 24 × 0.5 = 12 cm²"
                    }
                ],
                tip: "💡 The angle MUST be between the two sides you're using!"
            },
            12: {
                title: "Level 12: Problem Solving",
                band: "Mastery",
                description: "Complex real-world applications.",
                keyPoints: [
                    "Draw a diagram for word problems",
                    "Identify the right triangle(s)",
                    "Choose the appropriate formula",
                    "Check your answer is reasonable"
                ],
                examples: [
                    {
                        question: "A 5m ladder leans at 70° to ground. How high up wall?",
                        answer: "height = 5 × sin(70°) = 4.7m"
                    }
                ],
                tip: "🏆 You've mastered Trigonometry! Always draw, label, and check your work."
            }
        };
        
        // Decimals Help Content (12 levels)
        const decimalsHelpContent = {
            1: {
                title: "Level 1: Understanding Place Value",
                band: "Foundation",
                description: "Decimals are numbers with a decimal point that show values less than one. Each digit has a place value - tenths, hundredths, thousandths.",
                keyPoints: [
                    "The <strong>decimal point</strong> separates whole numbers from parts",
                    "<strong>Tenths</strong> (0.1) = first digit after decimal point",
                    "<strong>Hundredths</strong> (0.01) = second digit after decimal point",
                    "Each place is 10× smaller than the one before it"
                ],
                examples: [
                    {
                        question: "In 3.47, what digit is in the tenths place?",
                        steps: [
                            "Find the decimal point: 3<strong>.</strong>47",
                            "The tenths place is the <strong>first digit after</strong> the decimal",
                            "In 3.47, the tenths digit is <strong>4</strong>"
                        ],
                        answer: "The digit 4 is in the tenths place"
                    }
                ],
                tip: "💡 Remember: tenths, hundredths, thousandths - each place is 10× smaller!"
            },
            2: {
                title: "Level 2: Comparing Decimals",
                band: "Foundation",
                description: "To compare decimals, line up the decimal points and compare digit by digit from left to right, just like whole numbers.",
                keyPoints: [
                    "Line up the <strong>decimal points</strong> vertically",
                    "Add zeros to make the same number of decimal places",
                    "Compare from left to right, digit by digit",
                    "The first different digit determines which is larger"
                ],
                examples: [
                    {
                        question: "Which is larger: 0.8 or 0.75?",
                        steps: [
                            "Write with same decimal places: 0.<strong>80</strong> vs 0.<strong>75</strong>",
                            "Compare tenths: 8 vs 7",
                            "8 > 7, so 0.8 > 0.75"
                        ],
                        answer: "0.8 is larger than 0.75"
                    }
                ],
                tip: "💡 Add trailing zeros to compare: 0.8 = 0.80, making it easier to see that 80 > 75!"
            },
            3: {
                title: "Level 3: Adding & Subtracting Decimals",
                band: "Foundation",
                description: "Line up the decimal points, then add or subtract as normal. Keep the decimal point in the same position in your answer.",
                keyPoints: [
                    "<strong>Line up</strong> the decimal points vertically",
                    "Add placeholder zeros if needed",
                    "Add or subtract column by column",
                    "Keep the decimal point in the <strong>same position</strong>"
                ],
                examples: [
                    {
                        question: "Calculate: 3.45 + 2.3",
                        steps: [
                            "Line up: 3.45 + 2.30 (add zero)",
                            "Add: 5 + 0 = 5, 4 + 3 = 7, 3 + 2 = 5",
                            "Result: <strong>5.75</strong>"
                        ],
                        answer: "3.45 + 2.3 = 5.75"
                    }
                ],
                tip: "💡 SEC Exam style! Money problems use decimals - €3.45 + €2.30 = €5.75"
            },
            4: {
                title: "Level 4: Multiplying Decimals by Whole Numbers",
                band: "Ordinary",
                description: "Multiply as if there's no decimal point, then count decimal places in the original number and put the point in the answer.",
                keyPoints: [
                    "Ignore the decimal point and multiply normally",
                    "Count decimal places in the original decimal",
                    "Put the decimal point in the answer (same number of places)",
                    "SEC 2023: '3.4 × 7' is a typical question"
                ],
                examples: [
                    {
                        question: "Calculate: 3.4 × 7 (SEC 2023 OL style)",
                        steps: [
                            "Multiply without decimal: 34 × 7 = <strong>238</strong>",
                            "Count decimal places in 3.4: <strong>1 place</strong>",
                            "Put decimal 1 place from right: <strong>23.8</strong>"
                        ],
                        answer: "3.4 × 7 = 23.8"
                    }
                ],
                tip: "💡 SEC Exam Style! This exact question appeared in 2023 Ordinary Level Paper 1!"
            },
            5: {
                title: "Level 5: Dividing Decimals by Whole Numbers",
                band: "Ordinary",
                description: "Divide as normal, keeping the decimal point directly above in the answer. Add zeros if needed to continue dividing.",
                keyPoints: [
                    "Set up long division with decimal point above",
                    "Divide normally, bringing down digits",
                    "Keep decimal point <strong>aligned</strong> in quotient",
                    "Add zeros after decimal if needed"
                ],
                examples: [
                    {
                        question: "€15.60 shared equally between 4 people. How much each?",
                        steps: [
                            "15.60 ÷ 4",
                            "15 ÷ 4 = 3 remainder 3, then 36 ÷ 4 = 9, then 0 ÷ 4 = 0",
                            "Answer: <strong>€3.90</strong> each"
                        ],
                        answer: "Each person gets €3.90"
                    }
                ],
                tip: "💡 Money problems are common! Always give money answers to 2 decimal places."
            },
            6: {
                title: "Level 6: Rounding Decimals",
                band: "Ordinary",
                description: "Look at the digit AFTER the place you're rounding to. If it's 5 or more, round up. If it's less than 5, round down.",
                keyPoints: [
                    "Identify which place to round to",
                    "Look at the <strong>next digit</strong> (the one after)",
                    "5 or more → round UP",
                    "Less than 5 → round DOWN (keep same)"
                ],
                examples: [
                    {
                        question: "Write down the whole number nearest to 15.8 (SEC 2022 OL)",
                        steps: [
                            "We're rounding to nearest <strong>whole number</strong>",
                            "Look at tenths digit: <strong>8</strong>",
                            "8 ≥ 5, so round UP: 15 → <strong>16</strong>"
                        ],
                        answer: "15.8 rounds to 16"
                    }
                ],
                tip: "💡 SEC Exam Style! 'Nearest whole number', 'to 1 d.p.', 'to the nearest cent' are common."
            },
            7: {
                title: "Level 7: Decimals to Fractions",
                band: "Higher",
                description: "Convert decimals to fractions by putting the decimal over 10, 100, or 1000, then simplify.",
                keyPoints: [
                    "0.1 = 1/10, 0.01 = 1/100, 0.001 = 1/1000",
                    "Count decimal places to know the denominator",
                    "<strong>Simplify</strong> by dividing by common factors",
                    "Common: 0.5 = 1/2, 0.25 = 1/4, 0.75 = 3/4"
                ],
                examples: [
                    {
                        question: "Write 0.75 as a fraction in simplest form.",
                        steps: [
                            "0.75 has 2 decimal places → denominator is 100",
                            "0.75 = 75/100",
                            "Simplify: 75 ÷ 25 = 3, 100 ÷ 25 = 4 → <strong>3/4</strong>"
                        ],
                        answer: "0.75 = 3/4"
                    }
                ],
                tip: "💡 Memorise common conversions: 0.5 = 1/2, 0.25 = 1/4, 0.2 = 1/5, 0.125 = 1/8"
            },
            8: {
                title: "Level 8: Decimals to Percentages",
                band: "Higher",
                description: "To convert a decimal to a percentage, multiply by 100. To convert a percentage to a decimal, divide by 100.",
                keyPoints: [
                    "Decimal → Percentage: <strong>× 100</strong>",
                    "Percentage → Decimal: <strong>÷ 100</strong>",
                    "Moving decimal point: right for %, left for decimal",
                    "0.35 = 35%, 0.07 = 7%, 1.5 = 150%"
                ],
                examples: [
                    {
                        question: "Convert 0.45 to a percentage.",
                        steps: [
                            "Decimal to percentage: multiply by 100",
                            "0.45 × 100 = <strong>45</strong>",
                            "Add the % symbol: <strong>45%</strong>"
                        ],
                        answer: "0.45 = 45%"
                    }
                ],
                tip: "💡 Think of it as moving the decimal point 2 places right (×100) or left (÷100)."
            },
            9: {
                title: "Level 9: Multiplying Decimals by Decimals",
                band: "Higher",
                description: "Multiply without decimals, then count TOTAL decimal places in both numbers and put the point in the answer.",
                keyPoints: [
                    "Ignore decimals and multiply the numbers",
                    "Count decimal places in <strong>BOTH</strong> numbers",
                    "Put decimal point that many places from the right",
                    "Example: 1.2 × 0.3 → 2 places total → 0.36"
                ],
                examples: [
                    {
                        question: "Calculate: 2.5 × 0.4",
                        steps: [
                            "Multiply without decimals: 25 × 4 = 100",
                            "Count decimal places: 2.5 (1) + 0.4 (1) = <strong>2 places</strong>",
                            "Place decimal 2 from right: <strong>1.00</strong> = 1"
                        ],
                        answer: "2.5 × 0.4 = 1.0 (or just 1)"
                    }
                ],
                tip: "💡 Area problems often use this! Length 2.5m × Width 0.4m = 1.0 m²"
            },
            10: {
                title: "Level 10: Dividing Decimals by Decimals",
                band: "Application",
                description: "Make the divisor a whole number by multiplying both numbers by 10, 100, etc. Then divide normally.",
                keyPoints: [
                    "Multiply both numbers to make divisor whole",
                    "0.6 ÷ 0.2 → same as 6 ÷ 2",
                    "1.44 ÷ 0.12 → same as 144 ÷ 12",
                    "This keeps the answer the same!"
                ],
                examples: [
                    {
                        question: "Calculate: 3.6 ÷ 0.4",
                        steps: [
                            "Make 0.4 a whole number: × 10",
                            "Multiply both: 3.6 × 10 = 36, 0.4 × 10 = 4",
                            "Now divide: 36 ÷ 4 = <strong>9</strong>"
                        ],
                        answer: "3.6 ÷ 0.4 = 9"
                    }
                ],
                tip: "💡 'How many 0.4m pieces can be cut from 3.6m?' = 3.6 ÷ 0.4 = 9 pieces"
            },
            11: {
                title: "Level 11: Estimation & Approximation",
                band: "Application",
                description: "Round numbers before calculating to get a quick estimate. This helps check if your exact answer is reasonable.",
                keyPoints: [
                    "Round to easy numbers first (usually 1 s.f.)",
                    "Calculate with rounded values",
                    "Use estimates to <strong>check</strong> exact answers",
                    "If estimate is far from answer, you made an error!"
                ],
                examples: [
                    {
                        question: "Estimate: 4.8 × 6.2",
                        steps: [
                            "Round 4.8 → <strong>5</strong>",
                            "Round 6.2 → <strong>6</strong>",
                            "Estimate: 5 × 6 = <strong>30</strong>",
                            "(Exact answer: 29.76 ✓ Close!)"
                        ],
                        answer: "Estimate is approximately 30"
                    }
                ],
                tip: "💡 Always estimate first! If your calculator says 298.8, you know you made an error."
            },
            12: {
                title: "Level 12: Multi-Step Decimal Problems",
                band: "Mastery",
                description: "Combine all decimal skills to solve real-world problems involving shopping, money, measurements, and more.",
                keyPoints: [
                    "Read the problem carefully - identify operations needed",
                    "Work step by step, showing all working",
                    "Round money to 2 decimal places",
                    "Check your answer is <strong>reasonable</strong>"
                ],
                examples: [
                    {
                        question: "SEC Style: Buy milk (€1.49), bread (€1.89), cheese (€3.49). Pay with €10. Change?",
                        steps: [
                            "Total: €1.49 + €1.89 + €3.49 = <strong>€6.87</strong>",
                            "Change: €10.00 - €6.87",
                            "€10.00 - €6.87 = <strong>€3.13</strong>"
                        ],
                        answer: "Change is €3.13"
                    }
                ],
                tip: "🏆 You've mastered decimals! These skills are essential for everyday money calculations."
            }
        };
        
        // Simplifying Expressions Help Content (12 levels)
        const simplifyingExpressionsHelpContent = {
            1: {
                title: "Level 1: Recognising Like Terms",
                band: "Foundation",
                description: "Like terms have the same variable part. You can only add or subtract like terms together.",
                keyPoints: [
                    "<strong>Like terms</strong> have the same letter (e.g., 3x and 5x)",
                    "3x and 5y are <strong>NOT</strong> like terms - different letters",
                    "2x² and 4x are NOT like terms - different powers"
                ],
                examples: [
                    {
                        question: "Which are like terms: 3x, 5y, 7x?",
                        answer: "3x and 7x are like terms (both have x)"
                    }
                ],
                tip: "💡 Think of variables like different fruits - you can only add apples to apples!"
            },
            2: {
                title: "Level 2: Collecting Like Terms",
                band: "Foundation",
                description: "Add or subtract the coefficients (numbers) of like terms, keeping the variable the same.",
                keyPoints: [
                    "Add the numbers, keep the letter: 3x + 5x = 8x",
                    "For subtraction: 9x - 4x = 5x",
                    "The variable stays the same"
                ],
                examples: [
                    {
                        question: "Simplify: 6a + 3a",
                        steps: ["Both terms have 'a'", "Add coefficients: 6 + 3 = 9"],
                        answer: "9a"
                    }
                ],
                tip: "💡 Just add or subtract the numbers in front!"
            },
            3: {
                title: "Level 3: Two Different Variables",
                band: "Foundation",
                description: "When you have different variables, group and simplify each type separately.",
                keyPoints: [
                    "Group like terms together: (3x + 2x) + (4y + y)",
                    "Simplify each group separately",
                    "SEC style: 5a + 3b - 2a + 7b = 3a + 10b"
                ],
                examples: [
                    {
                        question: "Simplify: 5a + 3b - 2a + 7b",
                        steps: ["Group a terms: 5a - 2a = 3a", "Group b terms: 3b + 7b = 10b"],
                        answer: "3a + 10b"
                    }
                ],
                tip: "💡 SEC 2022 OL Q13(a) style! Keep different letters separate."
            },
            4: {
                title: "Level 4: Multiplying Terms",
                band: "Ordinary",
                description: "When multiplying algebraic terms, multiply the coefficients and add the powers of like variables.",
                keyPoints: [
                    "Multiply coefficients: 3 × 4 = 12",
                    "Same variable: x × x = x²",
                    "Different variables: x × y = xy"
                ],
                examples: [
                    {
                        question: "Simplify: 3x × 4x",
                        steps: ["Multiply numbers: 3 × 4 = 12", "Multiply x × x = x²"],
                        answer: "12x²"
                    }
                ],
                tip: "💡 Remember: x × x = x² (not 2x!)"
            },
            5: {
                title: "Level 5: Expanding Single Brackets",
                band: "Ordinary",
                description: "Multiply everything inside the bracket by the term outside.",
                keyPoints: [
                    "Multiply outside by EACH term inside",
                    "5(2x + 3) = 10x + 15",
                    "Watch the signs: 3(x - 2) = 3x - 6"
                ],
                examples: [
                    {
                        question: "Expand: 3(4x - 2)",
                        steps: ["3 × 4x = 12x", "3 × (-2) = -6"],
                        answer: "12x - 6"
                    }
                ],
                tip: "💡 SEC 2023 style! Multiply the outside number by EVERY term inside."
            },
            6: {
                title: "Level 6: Expand and Simplify",
                band: "Ordinary",
                description: "Expand multiple brackets then collect like terms.",
                keyPoints: [
                    "Expand each bracket first",
                    "Then collect like terms",
                    "2(x + 3) + 3(x + 1) = 2x + 6 + 3x + 3 = 5x + 9"
                ],
                examples: [
                    {
                        question: "Expand and simplify: 3(x + 2) + 2(x + 4)",
                        steps: ["Expand first: 3x + 6", "Expand second: 2x + 8", "Collect: 5x + 14"],
                        answer: "5x + 14"
                    }
                ],
                tip: "💡 Do one bracket at a time, then combine!"
            },
            7: {
                title: "Level 7: Double Brackets (FOIL)",
                band: "Higher",
                description: "Expand (x + a)(x + b) using FOIL: First, Outer, Inner, Last.",
                keyPoints: [
                    "<strong>F</strong>irst: x × x = x²",
                    "<strong>O</strong>uter + <strong>I</strong>nner: gives the x term",
                    "<strong>L</strong>ast: a × b = constant"
                ],
                examples: [
                    {
                        question: "Expand: (x + 3)(x + 2)",
                        steps: ["First: x²", "Outer + Inner: 2x + 3x = 5x", "Last: 3 × 2 = 6"],
                        answer: "x² + 5x + 6"
                    }
                ],
                tip: "💡 SEC 2024 HL style! The middle term = sum of the two numbers."
            },
            8: {
                title: "Level 8: Special Products",
                band: "Higher",
                description: "Perfect squares and difference of squares have special patterns.",
                keyPoints: [
                    "(x + a)² = x² + 2ax + a²",
                    "(x - a)² = x² - 2ax + a²",
                    "(x + a)(x - a) = x² - a² (difference of squares)"
                ],
                examples: [
                    {
                        question: "Expand: (x + 4)²",
                        steps: ["Use (a + b)² = a² + 2ab + b²", "x² + 2(4)x + 4²"],
                        answer: "x² + 8x + 16"
                    }
                ],
                tip: "💡 The middle term is always DOUBLE the number!"
            },
            9: {
                title: "Level 9: Mixed Expanding",
                band: "Higher",
                description: "Combine expanding with other operations and simplifying.",
                keyPoints: [
                    "Expand brackets first",
                    "Then add, subtract, or multiply as needed",
                    "Collect like terms at the end"
                ],
                examples: [
                    {
                        question: "Expand and simplify: (x + 3)(x + 2) + 5",
                        steps: ["Expand: x² + 5x + 6", "Add 5: x² + 5x + 11"],
                        answer: "x² + 5x + 11"
                    }
                ],
                tip: "💡 Always expand first, then simplify!"
            },
            10: {
                title: "Level 10: Factorising - Common Factor",
                band: "Mastery",
                description: "Take out the highest common factor (HCF) from all terms.",
                keyPoints: [
                    "Find the HCF of all coefficients",
                    "Check for common variables",
                    "6x + 12 = 6(x + 2)"
                ],
                examples: [
                    {
                        question: "Factorise: 8x + 12",
                        steps: ["HCF of 8 and 12 is 4", "8x ÷ 4 = 2x", "12 ÷ 4 = 3"],
                        answer: "4(2x + 3)"
                    }
                ],
                tip: "💡 Factorising is the reverse of expanding!"
            },
            11: {
                title: "Level 11: Factorising Quadratics",
                band: "Mastery",
                description: "Factorise x² + bx + c by finding two numbers that multiply to c and add to b.",
                keyPoints: [
                    "Find two numbers that <strong>multiply</strong> to give c",
                    "Those same numbers must <strong>add</strong> to give b",
                    "x² + 5x + 6 = (x + 2)(x + 3) because 2 × 3 = 6 and 2 + 3 = 5"
                ],
                examples: [
                    {
                        question: "Factorise: x² + 7x + 12",
                        steps: ["Need: multiply to 12, add to 7", "Numbers: 3 and 4"],
                        answer: "(x + 3)(x + 4)"
                    }
                ],
                tip: "💡 SEC 2023 HL style! Check by expanding your answer."
            },
            12: {
                title: "Level 12: Complex Expressions",
                band: "Mastery",
                description: "SEC exam-style questions combining multiple skills.",
                keyPoints: [
                    "Difference of squares: x² - 9 = (x + 3)(x - 3)",
                    "Factorise completely by finding ALL common factors",
                    "Always check your answer by expanding"
                ],
                examples: [
                    {
                        question: "Factorise: x² - 25",
                        steps: ["Recognise: x² - 5²", "Difference of squares formula"],
                        answer: "(x + 5)(x - 5)"
                    }
                ],
                tip: "🏆 You've mastered simplifying expressions! These skills are essential for solving equations."
            }
        };
        
        // Expanding and Factorising Help Content (12 levels)
        const expandingFactorisingHelpContent = {
            1: {
                title: "Level 1: Single Brackets (Basic)",
                band: "Foundation",
                description: "Multiply everything inside the bracket by the number outside.",
                keyPoints: [
                    "Multiply the outside by EACH term inside",
                    "3(x + 4) = 3×x + 3×4 = 3x + 12",
                    "Keep the signs the same"
                ],
                examples: [
                    {
                        question: "Expand: 2(x + 5)",
                        answer: "2x + 10"
                    }
                ],
                tip: "💡 The outside number multiplies EVERY term inside the bracket!"
            },
            2: {
                title: "Level 2: Single Brackets (Subtraction)",
                band: "Foundation",
                description: "When there's subtraction inside the bracket, watch your signs carefully.",
                keyPoints: [
                    "3(x - 4) = 3×x + 3×(-4) = 3x - 12",
                    "Positive × negative = negative",
                    "SEC 2022 style: 4(3x - 2)"
                ],
                examples: [
                    {
                        question: "Expand: 5(x - 3)",
                        answer: "5x - 15"
                    }
                ],
                tip: "💡 Multiply each term - the minus sign stays with the number after it!"
            },
            3: {
                title: "Level 3: Negative Multiplier",
                band: "Foundation",
                description: "When the number outside is negative, ALL signs change inside.",
                keyPoints: [
                    "-2(x + 3) = -2x - 6 (both become negative)",
                    "-3(x - 4) = -3x + 12 (negative × negative = positive)",
                    "Two negatives make a positive"
                ],
                examples: [
                    {
                        question: "Expand: -2(x + 5)",
                        answer: "-2x - 10"
                    }
                ],
                tip: "💡 With a negative outside, + becomes - and - becomes +!"
            },
            4: {
                title: "Level 4: Double Brackets (FOIL)",
                band: "Ordinary",
                description: "Expand (x + a)(x + b) using FOIL: First, Outer, Inner, Last.",
                keyPoints: [
                    "<strong>F</strong>irst: x × x = x²",
                    "<strong>O</strong>uter + <strong>I</strong>nner: combine to give middle term",
                    "<strong>L</strong>ast: a × b = constant"
                ],
                examples: [
                    {
                        question: "Expand: (x + 3)(x + 4)",
                        answer: "x² + 7x + 12"
                    }
                ],
                tip: "💡 The middle number = sum of the two numbers, last = product!"
            },
            5: {
                title: "Level 5: Expand and Simplify",
                band: "Ordinary",
                description: "Expand multiple brackets then collect like terms.",
                keyPoints: [
                    "Expand each bracket first",
                    "Then collect like terms",
                    "SEC 2024: 2(x + 3) + 3(x - 1)"
                ],
                examples: [
                    {
                        question: "Expand and simplify: 2(x + 3) + 3(x + 2)",
                        answer: "5x + 12"
                    }
                ],
                tip: "💡 Do one bracket at a time, then add like terms together!"
            },
            6: {
                title: "Level 6: Perfect Squares",
                band: "Ordinary",
                description: "Learn the patterns for (x + a)² and (x - a)².",
                keyPoints: [
                    "(x + a)² = x² + 2ax + a²",
                    "(x - a)² = x² - 2ax + a²",
                    "The middle term is always DOUBLE the number"
                ],
                examples: [
                    {
                        question: "Expand: (x + 5)²",
                        answer: "x² + 10x + 25"
                    }
                ],
                tip: "💡 Remember: middle term = 2 × the number, last term = number squared!"
            },
            7: {
                title: "Level 7: Common Factor",
                band: "Higher",
                description: "Factorise by taking out the highest common factor (HCF).",
                keyPoints: [
                    "Find what divides into ALL terms",
                    "6x + 12 = 6(x + 2)",
                    "x² + 3x = x(x + 3)"
                ],
                examples: [
                    {
                        question: "Factorise: 8x + 12",
                        answer: "4(2x + 3)"
                    }
                ],
                tip: "💡 Factorising is the reverse of expanding - what × what = this?"
            },
            8: {
                title: "Level 8: Quadratic Factorising (Positive)",
                band: "Higher",
                description: "Factorise x² + bx + c where both factors are positive.",
                keyPoints: [
                    "Find two numbers that MULTIPLY to c",
                    "Those same numbers must ADD to b",
                    "x² + 5x + 6 = (x + 2)(x + 3)"
                ],
                examples: [
                    {
                        question: "Factorise: x² + 7x + 12",
                        answer: "(x + 3)(x + 4)"
                    }
                ],
                tip: "💡 SEC 2023 HL style! Check: 3 + 4 = 7 ✓ and 3 × 4 = 12 ✓"
            },
            9: {
                title: "Level 9: Quadratic Factorising (Mixed Signs)",
                band: "Higher",
                description: "Factorise quadratics with negative terms.",
                keyPoints: [
                    "x² - 7x + 12: both factors negative → (x - 3)(x - 4)",
                    "x² + x - 12: factors have different signs → (x + 4)(x - 3)",
                    "The signs tell you the story!"
                ],
                examples: [
                    {
                        question: "Factorise: x² - 5x + 6",
                        answer: "(x - 2)(x - 3)"
                    }
                ],
                tip: "💡 If last term positive: same signs. If negative: different signs!"
            },
            10: {
                title: "Level 10: Difference of Squares",
                band: "Mastery",
                description: "Recognise and factorise x² - a² = (x + a)(x - a).",
                keyPoints: [
                    "x² - 9 = x² - 3² = (x + 3)(x - 3)",
                    "Only works with SUBTRACTION",
                    "Both terms must be perfect squares"
                ],
                examples: [
                    {
                        question: "Factorise: x² - 25",
                        answer: "(x + 5)(x - 5)"
                    }
                ],
                tip: "💡 Spot the pattern: something² - something² = (sum)(difference)"
            },
            11: {
                title: "Level 11: Factorise Fully",
                band: "Mastery",
                description: "Take out ALL common factors, then continue factorising.",
                keyPoints: [
                    "SEC 2022 HL: 3x² - 12x = 3x(x - 4)",
                    "2x² - 8 = 2(x² - 4) = 2(x + 2)(x - 2)",
                    "Always check: can I factorise further?"
                ],
                examples: [
                    {
                        question: "Factorise fully: 2x² - 18",
                        answer: "2(x + 3)(x - 3)"
                    }
                ],
                tip: "💡 'Fully' means take out number factors first, then look for more!"
            },
            12: {
                title: "Level 12: SEC Exam Style",
                band: "Mastery",
                description: "Mixed questions combining expanding and factorising skills.",
                keyPoints: [
                    "Read carefully - expand OR factorise?",
                    "Use (x + a)(x - a) = x² - a² for quick expansion",
                    "Check your answer by expanding/factorising back"
                ],
                examples: [
                    {
                        question: "Expand: (x + 4)(x - 4)",
                        answer: "x² - 16"
                    }
                ],
                tip: "🏆 You've mastered expanding and factorising! These are essential algebra skills."
            }
        };

const wholeNumbersHelpContent = {
    1: {
        title: "Reading Numbers",
        band: "Foundation",
        description: "Learn to read and say numbers up to 10,000. Break big numbers into smaller parts to read them easily.",
        keyPoints: [
            "Read numbers from <strong>left to right</strong>",
            "Say the <strong>thousands</strong> first, then hundreds, then tens and ones",
            "Use commas to help separate thousands: 3,542"
        ],
        examples: [
            {
                question: "How do you read 3,542?",
                steps: [
                    "3 thousands = <strong>three thousand</strong>",
                    "5 hundreds = <strong>five hundred</strong>",
                    "4 tens and 2 ones = <strong>forty-two</strong>",
                    "Together: <strong>three thousand, five hundred and forty-two</strong>"
                ],
                answer: "Three thousand, five hundred and forty-two"
            }
        ],
        tip: "💡 Break big numbers into chunks - thousands, hundreds, tens, ones!"
    },
    2: {
        title: "Place Value",
        band: "Foundation",
        description: "Every digit in a number has a place value. The position tells us how much it's worth.",
        keyPoints: [
            "The <strong>ones</strong> place is on the right",
            "Moving left: ones → tens → hundreds → thousands",
            "A digit's <strong>value</strong> depends on its <strong>position</strong>"
        ],
        examples: [
            {
                question: "In 4,729, what is the value of the 7?",
                steps: [
                    "Find the 7: it's in the <strong>hundreds</strong> place",
                    "Value = 7 × 100 = <strong>700</strong>"
                ],
                answer: "700"
            }
        ],
        tip: "💡 Each place is 10 times bigger than the place to its right!"
    },
    3: {
        title: "Comparing Numbers",
        band: "Foundation",
        description: "Use < (less than), > (greater than), and = (equal to) to compare numbers.",
        keyPoints: [
            "<strong>></strong> means greater than (the bigger number is on the left)",
            "<strong><</strong> means less than (the smaller number is on the left)",
            "Compare from <strong>left to right</strong>, starting with the largest place value"
        ],
        examples: [
            {
                question: "Compare 3,456 and 3,465",
                steps: [
                    "Thousands: both have 3 - <strong>equal</strong>",
                    "Hundreds: both have 4 - <strong>equal</strong>",
                    "Tens: 5 vs 6 - <strong>6 is bigger</strong>",
                    "So 3,456 < 3,465"
                ],
                answer: "3,456 < 3,465"
            }
        ],
        tip: "💡 The hungry crocodile always eats the bigger number! 🐊"
    },
    4: {
        title: "Ordering Numbers",
        band: "Developing",
        description: "Put numbers in order from smallest to largest (ascending) or largest to smallest (descending).",
        keyPoints: [
            "<strong>Ascending</strong> = going UP (smallest first)",
            "<strong>Descending</strong> = going DOWN (largest first)",
            "Compare place values starting from the left"
        ],
        examples: [
            {
                question: "Order 2,345, 2,435, 2,354 in ascending order",
                steps: [
                    "All start with 2 thousand",
                    "Hundreds: 3, 4, 3",
                    "2,345 and 2,354 both have 3 hundreds",
                    "Compare tens: 4 vs 5, so 2,345 < 2,354",
                    "Order: <strong>2,345, 2,354, 2,435</strong>"
                ],
                answer: "2,345, 2,354, 2,435"
            }
        ],
        tip: "💡 Write numbers in a column lined up by place value to compare easily!"
    },
    5: {
        title: "Rounding (10s, 100s)",
        band: "Developing",
        description: "Rounding makes numbers simpler. Look at the digit to the right to decide whether to round up or down.",
        keyPoints: [
            "Look at the digit <strong>to the right</strong> of the place you're rounding to",
            "If it's <strong>5 or more</strong>, round UP",
            "If it's <strong>4 or less</strong>, round DOWN"
        ],
        examples: [
            {
                question: "Round 347 to the nearest 10",
                steps: [
                    "Rounding to tens - look at the ones digit: <strong>7</strong>",
                    "7 ≥ 5, so round UP",
                    "347 → <strong>350</strong>"
                ],
                answer: "350"
            }
        ],
        tip: "💡 5 or more, let it soar! 4 or less, let it rest!"
    },
    6: {
        title: "Rounding (1000s)",
        band: "Developing",
        description: "Round to the nearest thousand by looking at the hundreds digit.",
        keyPoints: [
            "To round to thousands, look at the <strong>hundreds</strong> digit",
            "If hundreds digit is 5-9, round UP to next thousand",
            "If hundreds digit is 0-4, round DOWN"
        ],
        examples: [
            {
                question: "Round 7,621 to the nearest 1,000",
                steps: [
                    "Rounding to thousands - look at hundreds digit: <strong>6</strong>",
                    "6 ≥ 5, so round UP",
                    "7,621 → <strong>8,000</strong>"
                ],
                answer: "8,000"
            }
        ],
        tip: "💡 After rounding to thousands, all digits after become zeros!"
    },
    7: {
        title: "Large Numbers",
        band: "Proficient",
        description: "Work with numbers up to 100,000. The same place value rules apply - just with more digits!",
        keyPoints: [
            "Ten thousands come after thousands: 10,000 = ten thousand",
            "Use commas every 3 digits from the right",
            "Place value pattern continues: ones, tens, hundreds, thousands, ten thousands, hundred thousands"
        ],
        examples: [
            {
                question: "What is the value of 5 in 52,847?",
                steps: [
                    "5 is in the <strong>ten thousands</strong> place",
                    "Value = 5 × 10,000 = <strong>50,000</strong>"
                ],
                answer: "50,000"
            }
        ],
        tip: "💡 Commas are your friends - they make big numbers easier to read!"
    },
    8: {
        title: "Millions",
        band: "Proficient",
        description: "Numbers over a million follow the same patterns. A million is 1,000 thousands!",
        keyPoints: [
            "1,000,000 = one million (1 followed by 6 zeros)",
            "Millions come after hundred thousands",
            "Use commas: millions, thousands, ones groups"
        ],
        examples: [
            {
                question: "How do you read 2,345,678?",
                steps: [
                    "2 million",
                    "345 thousand",
                    "678",
                    "= <strong>two million, three hundred forty-five thousand, six hundred seventy-eight</strong>"
                ],
                answer: "Two million, three hundred forty-five thousand, six hundred seventy-eight"
            }
        ],
        tip: "💡 Group digits in threes: millions | thousands | ones"
    },
    9: {
        title: "Estimation",
        band: "Proficient",
        description: "Estimation gives a quick, approximate answer. Round numbers first, then calculate.",
        keyPoints: [
            "Round each number <strong>before</strong> calculating",
            "Estimation is useful for checking if answers make sense",
            "Choose sensible rounding (to 10s, 100s, or 1000s)"
        ],
        examples: [
            {
                question: "Estimate 387 + 524",
                steps: [
                    "Round 387 → <strong>400</strong>",
                    "Round 524 → <strong>500</strong>",
                    "Estimate: 400 + 500 = <strong>900</strong>"
                ],
                answer: "Approximately 900"
            }
        ],
        tip: "💡 Estimation is your 'sense check' - use it to spot mistakes!"
    },
    10: {
        title: "Number Properties",
        band: "Advanced",
        description: "Learn about special number types: odd, even, factors, and multiples.",
        keyPoints: [
            "<strong>Even</strong> numbers end in 0, 2, 4, 6, 8",
            "<strong>Odd</strong> numbers end in 1, 3, 5, 7, 9",
            "<strong>Factors</strong> divide exactly into a number",
            "<strong>Multiples</strong> are in a number's times table"
        ],
        examples: [
            {
                question: "Find all factors of 12",
                steps: [
                    "1 × 12 = 12 ✓",
                    "2 × 6 = 12 ✓",
                    "3 × 4 = 12 ✓",
                    "Factors: <strong>1, 2, 3, 4, 6, 12</strong>"
                ],
                answer: "1, 2, 3, 4, 6, 12"
            }
        ],
        tip: "💡 Factors come in pairs that multiply to give the number!"
    },
    11: {
        title: "Problem Solving",
        band: "Advanced",
        description: "Apply your number skills to solve multi-step word problems.",
        keyPoints: [
            "Read carefully - <strong>what is the question asking?</strong>",
            "Identify the <strong>numbers</strong> and <strong>operations</strong> needed",
            "Check your answer makes sense"
        ],
        examples: [
            {
                question: "A school has 847 students. 395 are boys. How many are girls?",
                steps: [
                    "Total students: 847",
                    "Boys: 395",
                    "Girls = Total - Boys",
                    "847 - 395 = <strong>452 girls</strong>"
                ],
                answer: "452 girls"
            }
        ],
        tip: "💡 RUCSAC: Read, Understand, Choose operation, Solve, Answer, Check!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You've mastered whole numbers! These questions combine all your skills.",
        keyPoints: [
            "Use <strong>place value</strong> to understand numbers",
            "Apply <strong>rounding</strong> and <strong>estimation</strong> wisely",
            "Think about <strong>number properties</strong> to help solve problems"
        ],
        examples: [
            {
                question: "The population of a town is 45,678. Round to the nearest thousand, then find if this is odd or even.",
                steps: [
                    "Round 45,678 → <strong>46,000</strong>",
                    "46,000 ends in 0",
                    "Answer: <strong>46,000 (even)</strong>"
                ],
                answer: "46,000 (even)"
            }
        ],
        tip: "🏆 Amazing! You're a Whole Numbers Champion!"
    }
};

// ============================================================
// 2. ADDITION & SUBTRACTION HELP CONTENT
// ============================================================
const additionSubtractionHelpContent = {
    1: {
        title: "Adding to 20",
        band: "Foundation",
        description: "Learn to add numbers with totals up to 20. Use counting, fingers, or number lines to help!",
        keyPoints: [
            "<strong>Addition</strong> means putting numbers together",
            "Count on from the bigger number",
            "Learn number bonds to 10 and 20"
        ],
        examples: [
            {
                question: "What is 8 + 5?",
                steps: [
                    "Start with the bigger number: <strong>8</strong>",
                    "Count on 5: 9, 10, 11, 12, 13",
                    "8 + 5 = <strong>13</strong>"
                ],
                answer: "13"
            }
        ],
        tip: "💡 Number bonds to 10: 1+9, 2+8, 3+7, 4+6, 5+5 - learn these by heart!"
    },
    2: {
        title: "Subtracting to 20",
        band: "Foundation",
        description: "Subtraction means taking away. Count back or use number bonds to help.",
        keyPoints: [
            "<strong>Subtraction</strong> means taking away or finding the difference",
            "Count back from the bigger number",
            "Use your addition facts backwards"
        ],
        examples: [
            {
                question: "What is 15 - 7?",
                steps: [
                    "Start at 15",
                    "Count back 7: 14, 13, 12, 11, 10, 9, 8",
                    "15 - 7 = <strong>8</strong>"
                ],
                answer: "8"
            }
        ],
        tip: "💡 If 8 + 7 = 15, then 15 - 7 = 8. Addition and subtraction are opposites!"
    },
    3: {
        title: "Adding 2-Digit Numbers",
        band: "Foundation",
        description: "Add two-digit numbers by adding tens and ones separately.",
        keyPoints: [
            "Line up the numbers by place value",
            "Add the <strong>ones</strong> first",
            "Then add the <strong>tens</strong>"
        ],
        examples: [
            {
                question: "What is 34 + 25?",
                steps: [
                    "Add ones: 4 + 5 = 9",
                    "Add tens: 30 + 20 = 50",
                    "Total: 50 + 9 = <strong>59</strong>"
                ],
                answer: "59"
            }
        ],
        tip: "💡 Partition numbers: 34 = 30 + 4, then add each part!"
    },
    4: {
        title: "Subtracting 2-Digit Numbers",
        band: "Developing",
        description: "Subtract two-digit numbers using column method or partitioning.",
        keyPoints: [
            "Line up digits by place value",
            "Subtract ones first, then tens",
            "If you can't subtract, you might need to <strong>exchange</strong> (borrow)"
        ],
        examples: [
            {
                question: "What is 67 - 24?",
                steps: [
                    "Subtract ones: 7 - 4 = 3",
                    "Subtract tens: 60 - 20 = 40",
                    "Total: 40 + 3 = <strong>43</strong>"
                ],
                answer: "43"
            }
        ],
        tip: "💡 Always check: does your answer + what you subtracted = the start number?"
    },
    5: {
        title: "Adding 3-Digit Numbers",
        band: "Developing",
        description: "Add three-digit numbers using the column method. Remember to carry when needed!",
        keyPoints: [
            "Line up <strong>hundreds, tens, ones</strong>",
            "Add from right to left (ones first)",
            "If a column adds to 10 or more, <strong>carry</strong> to the next column"
        ],
        examples: [
            {
                question: "What is 347 + 285?",
                steps: [
                    "Ones: 7 + 5 = 12. Write 2, carry 1",
                    "Tens: 4 + 8 + 1 = 13. Write 3, carry 1",
                    "Hundreds: 3 + 2 + 1 = 6",
                    "Answer: <strong>632</strong>"
                ],
                answer: "632"
            }
        ],
        tip: "💡 Write the carry digits small above the next column!"
    },
    6: {
        title: "Subtracting 3-Digit Numbers",
        band: "Developing",
        description: "Subtract three-digit numbers. Exchange (borrow) when the top digit is smaller.",
        keyPoints: [
            "Work from right to left",
            "If you can't subtract, <strong>exchange</strong> from the next column",
            "Exchange = borrow 1 ten (or hundred) = 10 ones (or tens)"
        ],
        examples: [
            {
                question: "What is 532 - 178?",
                steps: [
                    "Ones: Can't do 2-8, exchange: 12-8=4",
                    "Tens: 2-7 (after exchange), exchange: 12-7=5",
                    "Hundreds: 4-1=3",
                    "Answer: <strong>354</strong>"
                ],
                answer: "354"
            }
        ],
        tip: "💡 When you exchange, cross out and rewrite the digits to keep track!"
    },
    7: {
        title: "Word Problems (+)",
        band: "Proficient",
        description: "Solve addition word problems. Look for keywords that tell you to add.",
        keyPoints: [
            "Keywords for addition: <strong>total, altogether, sum, combined, in all, plus, more</strong>",
            "Read the problem twice",
            "Write the number sentence before calculating"
        ],
        examples: [
            {
                question: "Aoife has 245 stickers. She gets 178 more. How many does she have now?",
                steps: [
                    "'Gets more' means <strong>add</strong>",
                    "245 + 178 = ?",
                    "245 + 178 = <strong>423 stickers</strong>"
                ],
                answer: "423 stickers"
            }
        ],
        tip: "💡 Circle the numbers and underline the question!"
    },
    8: {
        title: "Word Problems (−)",
        band: "Proficient",
        description: "Solve subtraction word problems. Find the keywords that signal subtraction.",
        keyPoints: [
            "Keywords for subtraction: <strong>left, remaining, difference, fewer, less than, take away</strong>",
            "Draw a picture or bar model if it helps",
            "Check your answer makes sense"
        ],
        examples: [
            {
                question: "A shop had 500 apples. They sold 327. How many are left?",
                steps: [
                    "'How many left' means <strong>subtract</strong>",
                    "500 - 327 = ?",
                    "500 - 327 = <strong>173 apples</strong>"
                ],
                answer: "173 apples"
            }
        ],
        tip: "💡 'How many more' and 'what's the difference' also mean subtract!"
    },
    9: {
        title: "Mixed Operations",
        band: "Proficient",
        description: "Decide whether to add or subtract based on the problem.",
        keyPoints: [
            "Read carefully to decide: add or subtract?",
            "Adding = combining, totalling, increasing",
            "Subtracting = removing, finding difference, decreasing"
        ],
        examples: [
            {
                question: "Cian scored 156 points. Niamh scored 189 points. How many more did Niamh score?",
                steps: [
                    "'How many more' = find the <strong>difference</strong>",
                    "Difference means <strong>subtract</strong>",
                    "189 - 156 = <strong>33 more points</strong>"
                ],
                answer: "33 more points"
            }
        ],
        tip: "💡 Ask yourself: am I putting together or taking apart?"
    },
    10: {
        title: "Multi-Step Problems",
        band: "Advanced",
        description: "Some problems need more than one calculation. Work step by step!",
        keyPoints: [
            "Break the problem into <strong>smaller steps</strong>",
            "Do one calculation at a time",
            "Use the answer from step 1 in step 2"
        ],
        examples: [
            {
                question: "A class has 28 students. 15 are girls. 3 more boys join. How many boys now?",
                steps: [
                    "Step 1: Find original boys: 28 - 15 = 13",
                    "Step 2: Add new boys: 13 + 3 = 16",
                    "Answer: <strong>16 boys</strong>"
                ],
                answer: "16 boys"
            }
        ],
        tip: "💡 Write down each step - don't try to do it all in your head!"
    },
    11: {
        title: "Estimation",
        band: "Advanced",
        description: "Use estimation to check if your answers are sensible.",
        keyPoints: [
            "Round numbers to make calculation easier",
            "Estimate BEFORE you calculate (predict your answer)",
            "If your exact answer is very different from estimate, check again!"
        ],
        examples: [
            {
                question: "Estimate 487 + 312",
                steps: [
                    "Round 487 → 500",
                    "Round 312 → 300",
                    "Estimate: 500 + 300 = <strong>800</strong>",
                    "(Exact answer is 799 - very close! ✓)"
                ],
                answer: "Approximately 800"
            }
        ],
        tip: "💡 Use estimation as a 'sense check' for every calculation!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You've mastered addition and subtraction! Show off all your skills.",
        keyPoints: [
            "Use the <strong>column method</strong> for accuracy",
            "Choose the right operation based on keywords",
            "Always <strong>estimate</strong> first and <strong>check</strong> after"
        ],
        examples: [
            {
                question: "A cinema has 450 seats. Morning show: 287 people. Afternoon: 394 people. How many more in the afternoon?",
                steps: [
                    "'How many more' = subtract",
                    "394 - 287 = <strong>107 more people</strong>"
                ],
                answer: "107 more people"
            }
        ],
        tip: "🏆 Fantastic! You're an Addition & Subtraction Champion!"
    }
};

// ============================================================
// 3. MULTIPLICATION SKILLS HELP CONTENT
// ============================================================
const multiplicationSkillsHelpContent = {
    1: {
        title: "Times Tables (2, 5, 10)",
        band: "Foundation",
        description: "Start with the easiest times tables: 2s, 5s, and 10s. These have simple patterns!",
        keyPoints: [
            "<strong>×2</strong>: double the number (same as adding to itself)",
            "<strong>×5</strong>: ends in 0 or 5",
            "<strong>×10</strong>: just add a 0 to the end"
        ],
        examples: [
            {
                question: "What is 7 × 5?",
                steps: [
                    "Count in 5s: 5, 10, 15, 20, 25, 30, <strong>35</strong>",
                    "Or: 7 × 5 = half of 7 × 10 = half of 70 = <strong>35</strong>"
                ],
                answer: "35"
            }
        ],
        tip: "💡 ×10 is super easy - just add a zero! 7 × 10 = 70"
    },
    2: {
        title: "Times Tables (3, 4)",
        band: "Foundation",
        description: "Learn the 3 and 4 times tables. Look for patterns to help remember them.",
        keyPoints: [
            "<strong>×3</strong>: add the digits of answers - they sum to 3, 6, or 9",
            "<strong>×4</strong>: double, then double again",
            "Practice makes perfect!"
        ],
        examples: [
            {
                question: "What is 8 × 4?",
                steps: [
                    "Double 8: 8 × 2 = 16",
                    "Double again: 16 × 2 = <strong>32</strong>"
                ],
                answer: "32"
            }
        ],
        tip: "💡 ×4 trick: double it twice! 6×4 = 6×2×2 = 12×2 = 24"
    },
    3: {
        title: "Times Tables (6, 7, 8, 9)",
        band: "Foundation",
        description: "Master the trickier times tables. You already know most of these from earlier tables!",
        keyPoints: [
            "If you know 3 × 7, you know 7 × 3 (same answer!)",
            "<strong>×9 trick</strong>: multiply by 10 and subtract once",
            "<strong>×6</strong>: multiply by 3, then double"
        ],
        examples: [
            {
                question: "What is 7 × 9?",
                steps: [
                    "×9 trick: 7 × 10 = 70",
                    "Subtract 7: 70 - 7 = <strong>63</strong>"
                ],
                answer: "63"
            }
        ],
        tip: "💡 9× finger trick: hold up 10 fingers, put down the one you're multiplying by!"
    },
    4: {
        title: "Multiplying by 10, 100",
        band: "Developing",
        description: "Multiplying by 10, 100, or 1000 just moves the digits to the left!",
        keyPoints: [
            "<strong>×10</strong>: digits move 1 place left (add 1 zero)",
            "<strong>×100</strong>: digits move 2 places left (add 2 zeros)",
            "<strong>×1000</strong>: digits move 3 places left (add 3 zeros)"
        ],
        examples: [
            {
                question: "What is 45 × 100?",
                steps: [
                    "×100 = add 2 zeros",
                    "45 × 100 = <strong>4,500</strong>"
                ],
                answer: "4,500"
            }
        ],
        tip: "💡 The number of zeros you add = the number of zeros in what you multiply by!"
    },
    5: {
        title: "2-Digit × 1-Digit",
        band: "Developing",
        description: "Multiply larger numbers by breaking them into parts (partitioning).",
        keyPoints: [
            "Split the 2-digit number: 34 = 30 + 4",
            "Multiply each part separately",
            "Add the results together"
        ],
        examples: [
            {
                question: "What is 34 × 6?",
                steps: [
                    "Split: 34 = 30 + 4",
                    "30 × 6 = 180",
                    "4 × 6 = 24",
                    "Add: 180 + 24 = <strong>204</strong>"
                ],
                answer: "204"
            }
        ],
        tip: "💡 The grid method is great for showing your working!"
    },
    6: {
        title: "2-Digit × 2-Digit",
        band: "Developing",
        description: "Use the grid method or long multiplication for bigger calculations.",
        keyPoints: [
            "Split BOTH numbers",
            "Multiply all 4 parts",
            "Add everything together"
        ],
        examples: [
            {
                question: "What is 23 × 15?",
                steps: [
                    "23 = 20 + 3, 15 = 10 + 5",
                    "20×10=200, 20×5=100, 3×10=30, 3×5=15",
                    "Add: 200+100+30+15 = <strong>345</strong>"
                ],
                answer: "345"
            }
        ],
        tip: "💡 Draw a grid to organise your multiplication!"
    },
    7: {
        title: "Word Problems",
        band: "Proficient",
        description: "Spot when to multiply in word problems. Look for groups of equal amounts.",
        keyPoints: [
            "Keywords: <strong>times, groups of, each, every, per</strong>",
            "If you have equal groups, multiply!",
            "'3 boxes with 24 in each' = 3 × 24"
        ],
        examples: [
            {
                question: "A book has 28 pages. Saoirse reads 5 books. How many pages?",
                steps: [
                    "5 books, each with 28 pages",
                    "5 × 28 = ?",
                    "5 × 28 = <strong>140 pages</strong>"
                ],
                answer: "140 pages"
            }
        ],
        tip: "💡 'Each' and 'every' are multiplication signals!"
    },
    8: {
        title: "Multi-Step Problems",
        band: "Proficient",
        description: "Combine multiplication with other operations.",
        keyPoints: [
            "Read the whole problem first",
            "Plan your steps before calculating",
            "Do one operation at a time"
        ],
        examples: [
            {
                question: "Cinema tickets cost €8 each. A family of 4 buys tickets and €12 of popcorn. Total cost?",
                steps: [
                    "Step 1: Tickets = 4 × €8 = €32",
                    "Step 2: Add popcorn = €32 + €12 = <strong>€44</strong>"
                ],
                answer: "€44"
            }
        ],
        tip: "💡 List the steps you need before you start calculating!"
    },
    9: {
        title: "Estimation",
        band: "Proficient",
        description: "Estimate multiplication answers by rounding first.",
        keyPoints: [
            "Round to <strong>easy numbers</strong> (10s or 100s)",
            "Multiply the rounded numbers",
            "Your estimate should be close to the exact answer"
        ],
        examples: [
            {
                question: "Estimate 48 × 23",
                steps: [
                    "Round: 48 → 50, 23 → 20",
                    "Estimate: 50 × 20 = <strong>1,000</strong>",
                    "(Exact: 1,104 - close! ✓)"
                ],
                answer: "Approximately 1,000"
            }
        ],
        tip: "💡 If your answer is way off from your estimate, check your working!"
    },
    10: {
        title: "3-Digit × 2-Digit",
        band: "Advanced",
        description: "Use long multiplication for larger numbers. Same method, more digits!",
        keyPoints: [
            "Multiply by ones digit first",
            "Multiply by tens digit (remember the zero!)",
            "Add the two rows together"
        ],
        examples: [
            {
                question: "What is 234 × 15?",
                steps: [
                    "234 × 5 = 1,170",
                    "234 × 10 = 2,340",
                    "Add: 1,170 + 2,340 = <strong>3,510</strong>"
                ],
                answer: "3,510"
            }
        ],
        tip: "💡 Keep your columns lined up carefully!"
    },
    11: {
        title: "Problem Solving",
        band: "Advanced",
        description: "Apply multiplication skills to challenging real-world problems.",
        keyPoints: [
            "Identify what you need to find",
            "Choose the right method",
            "Check your answer is reasonable"
        ],
        examples: [
            {
                question: "A school orders 156 books at €12 each. What's the total cost?",
                steps: [
                    "156 × 12 = ?",
                    "156 × 10 = 1,560",
                    "156 × 2 = 312",
                    "Total: 1,560 + 312 = <strong>€1,872</strong>"
                ],
                answer: "€1,872"
            }
        ],
        tip: "💡 Break hard calculations into easier parts!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You're a multiplication master! Put all your skills together.",
        keyPoints: [
            "Know your <strong>times tables</strong> by heart",
            "Use <strong>partitioning</strong> for bigger numbers",
            "<strong>Estimate</strong> to check your answers"
        ],
        examples: [
            {
                question: "A farmer plants 24 rows with 35 apple trees in each row. How many trees?",
                steps: [
                    "24 × 35 = ?",
                    "20×35=700, 4×35=140",
                    "Total: 700 + 140 = <strong>840 trees</strong>"
                ],
                answer: "840 trees"
            }
        ],
        tip: "🏆 Brilliant! You're a Multiplication Champion!"
    }
};

// ============================================================
// 4. DIVISION SKILLS HELP CONTENT
// ============================================================
const divisionSkillsHelpContent = {
    1: {
        title: "Sharing Equally",
        band: "Foundation",
        description: "Division means sharing equally. If you share fairly, everyone gets the same amount!",
        keyPoints: [
            "<strong>Division</strong> = sharing into equal groups",
            "12 ÷ 3 means '12 shared between 3'",
            "Each person gets the same amount"
        ],
        examples: [
            {
                question: "Share 15 sweets equally between 3 friends",
                steps: [
                    "15 ÷ 3 = ?",
                    "Give 1 sweet each: 3 given, 12 left",
                    "Give 1 more each: 6 given, 9 left",
                    "Keep going... each friend gets <strong>5 sweets</strong>"
                ],
                answer: "5 sweets each"
            }
        ],
        tip: "💡 Division is the opposite of multiplication!"
    },
    2: {
        title: "Division Facts",
        band: "Foundation",
        description: "Use your times tables backwards to help with division facts.",
        keyPoints: [
            "If 6 × 4 = 24, then 24 ÷ 4 = 6 AND 24 ÷ 6 = 4",
            "Division and multiplication are <strong>inverse operations</strong>",
            "Fact families: 3, 5, 15 → 3×5=15, 5×3=15, 15÷3=5, 15÷5=3"
        ],
        examples: [
            {
                question: "What is 42 ÷ 7?",
                steps: [
                    "Think: ? × 7 = 42",
                    "From 7 times table: <strong>6</strong> × 7 = 42",
                    "So 42 ÷ 7 = <strong>6</strong>"
                ],
                answer: "6"
            }
        ],
        tip: "💡 Know your times tables and you know your division facts!"
    },
    3: {
        title: "Dividing by 2, 5, 10",
        band: "Foundation",
        description: "These divisions have easy patterns and connect to halving and place value.",
        keyPoints: [
            "<strong>÷2</strong> = halving (split in half)",
            "<strong>÷10</strong> = remove the zero (move digits right)",
            "<strong>÷5</strong> = divide by 10, then double"
        ],
        examples: [
            {
                question: "What is 350 ÷ 10?",
                steps: [
                    "Dividing by 10: digits move 1 place right",
                    "350 → 35",
                    "350 ÷ 10 = <strong>35</strong>"
                ],
                answer: "35"
            }
        ],
        tip: "💡 To divide by 5: divide by 10 first, then double your answer!"
    },
    4: {
        title: "Short Division",
        band: "Developing",
        description: "Use the bus stop method (short division) to divide bigger numbers.",
        keyPoints: [
            "Write the division as a 'bus stop': divisor | dividend",
            "Work from <strong>left to right</strong>",
            "Carry remainders to the next digit"
        ],
        examples: [
            {
                question: "What is 84 ÷ 4?",
                steps: [
                    "4 into 8 = 2 (write 2 above)",
                    "4 into 4 = 1 (write 1 above)",
                    "Answer: <strong>21</strong>"
                ],
                answer: "21"
            }
        ],
        tip: "💡 The 'bus stop' method keeps everything organised!"
    },
    5: {
        title: "Remainders",
        band: "Developing",
        description: "Sometimes division doesn't work out exactly. The leftover is called a remainder.",
        keyPoints: [
            "<strong>Remainder</strong> = what's left over after dividing",
            "Written as 'r' (e.g., 17 ÷ 5 = 3 r 2)",
            "The remainder must be <strong>less than</strong> the divisor"
        ],
        examples: [
            {
                question: "What is 23 ÷ 4?",
                steps: [
                    "4 × 5 = 20 (closest without going over)",
                    "23 - 20 = 3 left over",
                    "Answer: <strong>5 remainder 3</strong> (or 5 r 3)"
                ],
                answer: "5 r 3"
            }
        ],
        tip: "💡 Check: (answer × divisor) + remainder = original number"
    },
    6: {
        title: "Dividing by 10, 100",
        band: "Developing",
        description: "Dividing by 10 or 100 moves digits to the right.",
        keyPoints: [
            "<strong>÷10</strong>: digits move 1 place right",
            "<strong>÷100</strong>: digits move 2 places right",
            "This introduces decimals: 45 ÷ 10 = 4.5"
        ],
        examples: [
            {
                question: "What is 2,500 ÷ 100?",
                steps: [
                    "÷100 = move digits 2 places right",
                    "2,500 → 25",
                    "Answer: <strong>25</strong>"
                ],
                answer: "25"
            }
        ],
        tip: "💡 The number of zeros you 'remove' = zeros in what you divide by!"
    },
    7: {
        title: "Long Division",
        band: "Proficient",
        description: "Long division shows all the steps clearly. Great for bigger numbers!",
        keyPoints: [
            "Divide, Multiply, Subtract, Bring down (DMSB)",
            "Work one digit at a time",
            "Write out all your working"
        ],
        examples: [
            {
                question: "What is 156 ÷ 12?",
                steps: [
                    "12 into 15 = 1, write 1. 1×12=12, 15-12=3",
                    "Bring down 6: 36",
                    "12 into 36 = 3, write 3. 3×12=36, 36-36=0",
                    "Answer: <strong>13</strong>"
                ],
                answer: "13"
            }
        ],
        tip: "💡 Does McDonald's Sell Burgers? Divide, Multiply, Subtract, Bring down!"
    },
    8: {
        title: "Word Problems",
        band: "Proficient",
        description: "Spot when to divide. Look for sharing, grouping, or 'how many in each'.",
        keyPoints: [
            "Keywords: <strong>share, divide, split, per, each, every</strong>",
            "'How many groups?' or 'How many in each group?' = divide",
            "Draw pictures if it helps"
        ],
        examples: [
            {
                question: "144 stickers are shared equally between 8 children. How many each?",
                steps: [
                    "'Shared equally' = divide",
                    "144 ÷ 8 = ?",
                    "Answer: <strong>18 stickers each</strong>"
                ],
                answer: "18 stickers each"
            }
        ],
        tip: "💡 'How many ___ can fit in ___?' signals division!"
    },
    9: {
        title: "Interpreting Remainders",
        band: "Proficient",
        description: "What do you do with the remainder? It depends on the problem!",
        keyPoints: [
            "Sometimes you <strong>round up</strong> (buses needed, containers)",
            "Sometimes you <strong>round down</strong> (complete sets only)",
            "Sometimes you <strong>write the remainder</strong> as a fraction or decimal"
        ],
        examples: [
            {
                question: "33 children need to travel. Each car holds 4. How many cars needed?",
                steps: [
                    "33 ÷ 4 = 8 r 1",
                    "8 cars fit 32 children, 1 left over",
                    "Need 1 more car → <strong>9 cars</strong>"
                ],
                answer: "9 cars (round up)"
            }
        ],
        tip: "💡 Think about what the remainder means in real life!"
    },
    10: {
        title: "Multi-Step Problems",
        band: "Advanced",
        description: "Combine division with other operations to solve complex problems.",
        keyPoints: [
            "Break the problem into steps",
            "Identify which operation for each step",
            "Use the answer from one step in the next"
        ],
        examples: [
            {
                question: "360 apples are packed in boxes of 12, then boxes go on shelves holding 5 boxes. How many shelves?",
                steps: [
                    "Step 1: Boxes = 360 ÷ 12 = 30 boxes",
                    "Step 2: Shelves = 30 ÷ 5 = <strong>6 shelves</strong>"
                ],
                answer: "6 shelves"
            }
        ],
        tip: "💡 Write out each step clearly!"
    },
    11: {
        title: "Problem Solving",
        band: "Advanced",
        description: "Apply division skills to challenging real-world scenarios.",
        keyPoints: [
            "Read carefully to understand what's being asked",
            "Decide: sharing into groups OR how many groups?",
            "Check your answer makes sense"
        ],
        examples: [
            {
                question: "A rope is 225cm long. It's cut into 15cm pieces. How many pieces?",
                steps: [
                    "225 ÷ 15 = ?",
                    "15 × 15 = 225 ✓",
                    "Answer: <strong>15 pieces</strong>"
                ],
                answer: "15 pieces"
            }
        ],
        tip: "💡 Division answers 'how many groups?' or 'how many in each group?'"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You're a division expert! Show off everything you've learned.",
        keyPoints: [
            "Use times tables to help with division facts",
            "Choose short or long division based on the numbers",
            "Think carefully about what to do with remainders"
        ],
        examples: [
            {
                question: "A school orders 1,248 pencils. They come in packs of 24. How many packs?",
                steps: [
                    "1,248 ÷ 24 = ?",
                    "Using long division: <strong>52 packs</strong>"
                ],
                answer: "52 packs"
            }
        ],
        tip: "🏆 Excellent! You're a Division Champion!"
    }
};

// ============================================================
// 5. BASIC FRACTIONS HELP CONTENT
// ============================================================
const basicFractionsHelpContent = {
    1: {
        title: "What is a Fraction?",
        band: "Foundation",
        description: "A fraction shows parts of a whole. It has two numbers: numerator (top) and denominator (bottom).",
        keyPoints: [
            "The <strong>denominator</strong> (bottom) = how many equal parts in total",
            "The <strong>numerator</strong> (top) = how many parts you have",
            "The line in the middle means 'out of' or 'divided by'"
        ],
        examples: [
            {
                question: "What does ¾ mean?",
                steps: [
                    "Denominator = 4 (4 equal parts)",
                    "Numerator = 3 (we have 3 of them)",
                    "¾ = <strong>3 out of 4 parts</strong>"
                ],
                answer: "3 out of 4 equal parts"
            }
        ],
        tip: "💡 Think of a pizza cut into slices - the denominator is total slices!"
    },
    2: {
        title: "Unit Fractions",
        band: "Foundation",
        description: "Unit fractions have 1 as the numerator. They show one equal part of a whole.",
        keyPoints: [
            "<strong>Unit fraction</strong> = numerator is 1",
            "Examples: ½, ⅓, ¼, ⅕, ⅙, etc.",
            "The bigger the denominator, the <strong>smaller</strong> each piece"
        ],
        examples: [
            {
                question: "Which is bigger: ¼ or ⅛?",
                steps: [
                    "¼ = 1 piece when whole is cut into 4",
                    "⅛ = 1 piece when whole is cut into 8",
                    "More pieces = smaller pieces",
                    "So <strong>¼ is bigger</strong>"
                ],
                answer: "¼ is bigger"
            }
        ],
        tip: "💡 More slices = smaller slices! ⅛ < ¼"
    },
    3: {
        title: "Fractions of Shapes",
        band: "Foundation",
        description: "Identify fractions by looking at shaded parts of shapes.",
        keyPoints: [
            "Count <strong>total equal parts</strong> (denominator)",
            "Count <strong>shaded parts</strong> (numerator)",
            "Write as: shaded/total"
        ],
        examples: [
            {
                question: "A rectangle is divided into 5 equal parts. 2 are shaded. What fraction is shaded?",
                steps: [
                    "Total parts = 5 (denominator)",
                    "Shaded parts = 2 (numerator)",
                    "Fraction = <strong>⅖</strong>"
                ],
                answer: "⅖"
            }
        ],
        tip: "💡 Parts MUST be equal for it to be a fraction!"
    },
    4: {
        title: "Equivalent Fractions",
        band: "Developing",
        description: "Equivalent fractions look different but show the same amount. Like ½ and 2/4!",
        keyPoints: [
            "<strong>Equivalent</strong> = equal value",
            "Multiply or divide top AND bottom by the same number",
            "Use fraction walls to see equivalents"
        ],
        examples: [
            {
                question: "Find a fraction equivalent to ⅔",
                steps: [
                    "Multiply top and bottom by 2",
                    "2×2 = 4, 3×2 = 6",
                    "⅔ = <strong>4/6</strong>"
                ],
                answer: "4/6 (or 6/9, 8/12, etc.)"
            }
        ],
        tip: "💡 Whatever you do to the top, do to the bottom!"
    },
    5: {
        title: "Comparing Fractions",
        band: "Developing",
        description: "Compare fractions to see which is larger or smaller.",
        keyPoints: [
            "<strong>Same denominator</strong>: compare numerators (bigger numerator = bigger fraction)",
            "<strong>Same numerator</strong>: compare denominators (bigger denominator = smaller fraction)",
            "<strong>Different both</strong>: find equivalent fractions with same denominator"
        ],
        examples: [
            {
                question: "Which is larger: ⅗ or ⅘?",
                steps: [
                    "Same denominator (5)",
                    "Compare numerators: 4 > 3",
                    "<strong>⅘ is larger</strong>"
                ],
                answer: "⅘"
            }
        ],
        tip: "💡 Same denominator? Just compare the tops!"
    },
    6: {
        title: "Simplifying Fractions",
        band: "Developing",
        description: "Simplify fractions to their lowest terms by dividing top and bottom by common factors.",
        keyPoints: [
            "Find a number that divides <strong>both</strong> numerator and denominator",
            "Keep dividing until you can't anymore",
            "The simplified fraction has the same value"
        ],
        examples: [
            {
                question: "Simplify 6/8",
                steps: [
                    "Both 6 and 8 divide by 2",
                    "6÷2 = 3, 8÷2 = 4",
                    "6/8 = <strong>¾</strong>"
                ],
                answer: "¾"
            }
        ],
        tip: "💡 Try dividing by 2, then 3, then 5... until you can't divide anymore!"
    },
    7: {
        title: "Adding (Same Denominator)",
        band: "Proficient",
        description: "Add fractions with the same denominator by adding the numerators.",
        keyPoints: [
            "Keep the <strong>denominator the same</strong>",
            "<strong>Add the numerators</strong>",
            "Simplify if possible"
        ],
        examples: [
            {
                question: "What is ⅜ + ⅜?",
                steps: [
                    "Same denominator (8) - keep it!",
                    "Add numerators: 3 + 3 = 6",
                    "Answer: <strong>⅝</strong>"
                ],
                answer: "6/8 = ¾"
            }
        ],
        tip: "💡 Same denominator? Add the tops, keep the bottom!"
    },
    8: {
        title: "Subtracting (Same Denominator)",
        band: "Proficient",
        description: "Subtract fractions with the same denominator by subtracting numerators.",
        keyPoints: [
            "Keep the <strong>denominator the same</strong>",
            "<strong>Subtract the numerators</strong>",
            "Simplify if possible"
        ],
        examples: [
            {
                question: "What is ⅚ - ⅔?",
                steps: [
                    "First, make denominators same: ⅔ = 4/6",
                    "⅚ - 4/6 = ?",
                    "Subtract numerators: 5 - 4 = 1",
                    "Answer: <strong>⅙</strong>"
                ],
                answer: "⅙"
            }
        ],
        tip: "💡 Same denominator? Subtract the tops, keep the bottom!"
    },
    9: {
        title: "Fractions of Amounts",
        band: "Proficient",
        description: "Find a fraction of a number by dividing then multiplying.",
        keyPoints: [
            "To find <strong>⅓ of 12</strong>: divide 12 by 3 = 4",
            "To find <strong>⅔ of 12</strong>: find ⅓ (=4), then multiply by 2 = 8",
            "'Of' means multiply!"
        ],
        examples: [
            {
                question: "What is ¾ of 20?",
                steps: [
                    "First find ¼ of 20: 20 ÷ 4 = 5",
                    "Then multiply by 3: 5 × 3 = 15",
                    "¾ of 20 = <strong>15</strong>"
                ],
                answer: "15"
            }
        ],
        tip: "💡 Divide by the bottom, multiply by the top!"
    },
    10: {
        title: "Mixed Numbers",
        band: "Advanced",
        description: "Mixed numbers combine a whole number and a fraction, like 2½.",
        keyPoints: [
            "<strong>Mixed number</strong> = whole number + fraction",
            "<strong>Improper fraction</strong> = numerator ≥ denominator (like 5/2)",
            "You can convert between them"
        ],
        examples: [
            {
                question: "Convert 7/4 to a mixed number",
                steps: [
                    "How many times does 4 go into 7? <strong>1 time</strong>",
                    "Remainder: 7 - 4 = 3",
                    "Answer: <strong>1¾</strong>"
                ],
                answer: "1¾"
            }
        ],
        tip: "💡 Improper → Mixed: divide to get whole number, remainder is new numerator!"
    },
    11: {
        title: "Word Problems",
        band: "Advanced",
        description: "Apply fraction skills to real-world problems.",
        keyPoints: [
            "Read carefully - what fraction operation is needed?",
            "'What fraction?' = write a fraction",
            "'Of' = multiply (find fraction of amount)"
        ],
        examples: [
            {
                question: "Aoife ate ¼ of a pizza. Cian ate ⅜. How much is left?",
                steps: [
                    "Convert ¼ = 2/8",
                    "Eaten: 2/8 + ⅜ = ⅝",
                    "Left: 8/8 - ⅝ = <strong>⅜</strong>"
                ],
                answer: "⅜ of the pizza"
            }
        ],
        tip: "💡 Draw a picture to help visualise the problem!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You've mastered basic fractions! Time for the ultimate challenge.",
        keyPoints: [
            "Understand what fractions represent",
            "Find equivalents and simplify",
            "Add, subtract, and find fractions of amounts"
        ],
        examples: [
            {
                question: "A recipe needs ⅔ cup of flour. You want to make 1½ times the recipe. How much flour?",
                steps: [
                    "1½ = 3/2",
                    "⅔ × 3/2 = (2×3)/(3×2) = 6/6 = 1",
                    "Need: <strong>1 cup of flour</strong>"
                ],
                answer: "1 cup"
            }
        ],
        tip: "🏆 Fantastic! You're a Fractions Champion!"
    }
};

// ============================================================
// 6. BASIC DECIMALS HELP CONTENT
// ============================================================
const basicDecimalsHelpContent = {
    1: {
        title: "Understanding Tenths",
        band: "Foundation",
        description: "Decimals show parts of a whole. The first place after the decimal point is tenths.",
        keyPoints: [
            "<strong>Decimal point</strong> separates whole numbers from parts",
            "First place after decimal = <strong>tenths</strong> (÷10)",
            "0.1 = one tenth = 1/10"
        ],
        examples: [
            {
                question: "What does 0.7 mean?",
                steps: [
                    "0 = zero whole numbers",
                    ".7 = 7 tenths",
                    "0.7 = <strong>seven tenths</strong> = 7/10"
                ],
                answer: "Seven tenths (7/10)"
            }
        ],
        tip: "💡 Think of 1 divided into 10 equal parts - each part is 0.1!"
    },
    2: {
        title: "Decimal Place Value",
        band: "Foundation",
        description: "Every digit in a decimal has a place value, just like whole numbers.",
        keyPoints: [
            "Ones . Tenths Hundredths",
            "Each place is <strong>10 times smaller</strong> as you go right",
            "3.45 = 3 ones + 4 tenths + 5 hundredths"
        ],
        examples: [
            {
                question: "In 2.47, what is the value of the 4?",
                steps: [
                    "4 is in the <strong>tenths</strong> place",
                    "Value = 4 tenths = <strong>0.4</strong>"
                ],
                answer: "0.4 (four tenths)"
            }
        ],
        tip: "💡 Place value chart: ones | tenths | hundredths | thousandths"
    },
    3: {
        title: "Decimals and Money",
        band: "Foundation",
        description: "Money is a great way to understand decimals. €1.50 means 1 euro and 50 cent.",
        keyPoints: [
            "€1 = 100 cent, so 1 cent = €0.01",
            "€3.45 = 3 euros + 45 cent",
            "Money has 2 decimal places (hundredths)"
        ],
        examples: [
            {
                question: "Write 2 euros and 35 cent as a decimal",
                steps: [
                    "Whole euros: 2",
                    "Cent as decimal: 35 cent = 0.35",
                    "Answer: <strong>€2.35</strong>"
                ],
                answer: "€2.35"
            }
        ],
        tip: "💡 Money is always written with 2 decimal places: €5.00, €3.50, €0.99"
    },
    4: {
        title: "Understanding Hundredths",
        band: "Developing",
        description: "The second decimal place is hundredths - one hundred parts of a whole.",
        keyPoints: [
            "Hundredths = second place after decimal point",
            "0.01 = one hundredth = 1/100",
            "0.25 = 25 hundredths = 25/100 = ¼"
        ],
        examples: [
            {
                question: "Write 0.75 as a fraction",
                steps: [
                    "0.75 = 75 hundredths",
                    "= 75/100",
                    "Simplify: = <strong>¾</strong>"
                ],
                answer: "75/100 = ¾"
            }
        ],
        tip: "💡 Hundredths are tiny! 100 of them make 1 whole."
    },
    5: {
        title: "Comparing Decimals",
        band: "Developing",
        description: "Compare decimals by looking at each place value from left to right.",
        keyPoints: [
            "Start comparing from the <strong>left</strong>",
            "Compare ones first, then tenths, then hundredths",
            "Add zeros if needed: 0.5 = 0.50"
        ],
        examples: [
            {
                question: "Which is bigger: 0.45 or 0.5?",
                steps: [
                    "Make same decimal places: 0.5 = 0.50",
                    "Compare: 0.45 vs 0.50",
                    "50 hundredths > 45 hundredths",
                    "<strong>0.5 is bigger</strong>"
                ],
                answer: "0.5"
            }
        ],
        tip: "💡 Line up the decimal points, then compare digit by digit!"
    },
    6: {
        title: "Ordering Decimals",
        band: "Developing",
        description: "Put decimals in order from smallest to largest or largest to smallest.",
        keyPoints: [
            "Make all decimals have the <strong>same number of places</strong>",
            "Compare like whole numbers",
            "Check your order is right!"
        ],
        examples: [
            {
                question: "Order these: 0.4, 0.35, 0.42 (smallest first)",
                steps: [
                    "Make same places: 0.40, 0.35, 0.42",
                    "Compare: 35 < 40 < 42 (hundredths)",
                    "Order: <strong>0.35, 0.4, 0.42</strong>"
                ],
                answer: "0.35, 0.4, 0.42"
            }
        ],
        tip: "💡 Adding zeros after a decimal doesn't change its value: 0.4 = 0.40 = 0.400"
    },
    7: {
        title: "Adding Decimals",
        band: "Proficient",
        description: "Add decimals by lining up the decimal points and adding as normal.",
        keyPoints: [
            "<strong>Line up the decimal points</strong>",
            "Add zeros to make same places if needed",
            "Add column by column, carry if needed"
        ],
        examples: [
            {
                question: "What is 3.45 + 2.8?",
                steps: [
                    "Line up: 3.45",
                    "        + 2.80",
                    "Add: <strong>6.25</strong>"
                ],
                answer: "6.25"
            }
        ],
        tip: "💡 The decimal point in your answer goes directly below the others!"
    },
    8: {
        title: "Subtracting Decimals",
        band: "Proficient",
        description: "Subtract decimals by lining up decimal points, just like addition.",
        keyPoints: [
            "<strong>Line up the decimal points</strong>",
            "Add zeros if needed",
            "Exchange (borrow) if the top digit is smaller"
        ],
        examples: [
            {
                question: "What is 5.2 - 2.75?",
                steps: [
                    "Line up: 5.20",
                    "       - 2.75",
                    "Subtract: <strong>2.45</strong>"
                ],
                answer: "2.45"
            }
        ],
        tip: "💡 5.2 = 5.20 - add that zero so you can subtract hundredths!"
    },
    9: {
        title: "Decimals ↔ Fractions",
        band: "Proficient",
        description: "Convert between decimals and fractions. They're just different ways to write the same thing!",
        keyPoints: [
            "<strong>Decimal → Fraction</strong>: use place value (0.25 = 25/100)",
            "<strong>Fraction → Decimal</strong>: divide numerator by denominator",
            "Learn common ones: ½=0.5, ¼=0.25, ¾=0.75"
        ],
        examples: [
            {
                question: "Write ⅗ as a decimal",
                steps: [
                    "⅗ means 3 ÷ 5",
                    "3 ÷ 5 = <strong>0.6</strong>"
                ],
                answer: "0.6"
            }
        ],
        tip: "💡 Know these: ½=0.5, ¼=0.25, ¾=0.75, ⅕=0.2, ⅒=0.1"
    },
    10: {
        title: "Rounding Decimals",
        band: "Advanced",
        description: "Round decimals to a given number of decimal places.",
        keyPoints: [
            "Look at the digit <strong>after</strong> where you're rounding",
            "5 or more = round up",
            "4 or less = round down"
        ],
        examples: [
            {
                question: "Round 3.47 to 1 decimal place",
                steps: [
                    "Rounding to 1 d.p. - look at hundredths: 7",
                    "7 ≥ 5, so round UP",
                    "3.47 → <strong>3.5</strong>"
                ],
                answer: "3.5"
            }
        ],
        tip: "💡 '1 decimal place' means 1 digit after the point!"
    },
    11: {
        title: "Word Problems",
        band: "Advanced",
        description: "Apply decimal skills to real-world problems, especially money!",
        keyPoints: [
            "Money problems often use decimals",
            "Read carefully - add or subtract?",
            "Line up decimal points for accurate calculation"
        ],
        examples: [
            {
                question: "Niamh has €10. She buys a book for €6.75. How much change?",
                steps: [
                    "€10.00 - €6.75 = ?",
                    "Calculate: <strong>€3.25</strong>"
                ],
                answer: "€3.25"
            }
        ],
        tip: "💡 Always include € and use 2 decimal places for money answers!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You've mastered decimals! Show off all your skills.",
        keyPoints: [
            "Understand decimal place value",
            "Add and subtract with lined-up decimal points",
            "Convert between fractions and decimals"
        ],
        examples: [
            {
                question: "Calculate: 4.5 + ¾ (give answer as decimal)",
                steps: [
                    "Convert ¾ to decimal: 0.75",
                    "Add: 4.5 + 0.75 = 4.50 + 0.75 = <strong>5.25</strong>"
                ],
                answer: "5.25"
            }
        ],
        tip: "🏆 Brilliant! You're a Decimals Champion!"
    }
};

// ============================================================
// 7. BASIC PERCENTAGES HELP CONTENT
// ============================================================
const basicPercentagesHelpContent = {
    1: {
        title: "What is Percent?",
        band: "Foundation",
        description: "Percent means 'out of 100'. The % symbol shows a number as parts of 100.",
        keyPoints: [
            "<strong>Percent</strong> = per hundred (per cent)",
            "100% = the whole thing (all of it)",
            "50% = half, 25% = quarter"
        ],
        examples: [
            {
                question: "What does 75% mean?",
                steps: [
                    "75% = 75 out of 100",
                    "= 75/100",
                    "= <strong>three quarters</strong>"
                ],
                answer: "75 out of 100 (¾)"
            }
        ],
        tip: "💡 Think of a hundred square - 75% means 75 squares shaded!"
    },
    2: {
        title: "50% and Halves",
        band: "Foundation",
        description: "50% is the same as a half. Half of something means dividing by 2.",
        keyPoints: [
            "<strong>50% = ½ = 0.5</strong>",
            "To find 50%, divide by 2",
            "50% of 80 = 80 ÷ 2 = 40"
        ],
        examples: [
            {
                question: "What is 50% of 64?",
                steps: [
                    "50% means half",
                    "Half of 64 = 64 ÷ 2",
                    "= <strong>32</strong>"
                ],
                answer: "32"
            }
        ],
        tip: "💡 50% = half. Just divide by 2!"
    },
    3: {
        title: "25% and Quarters",
        band: "Foundation",
        description: "25% is a quarter. A quarter means dividing by 4.",
        keyPoints: [
            "<strong>25% = ¼ = 0.25</strong>",
            "To find 25%, divide by 4",
            "75% = three quarters (25% × 3)"
        ],
        examples: [
            {
                question: "What is 25% of 80?",
                steps: [
                    "25% = one quarter",
                    "80 ÷ 4 = <strong>20</strong>"
                ],
                answer: "20"
            }
        ],
        tip: "💡 25% = quarter. 50% ÷ 2 also gives 25%!"
    },
    4: {
        title: "10% and Tenths",
        band: "Developing",
        description: "10% is one tenth. Finding 10% is super useful for calculating other percentages!",
        keyPoints: [
            "<strong>10% = 1/10 = 0.1</strong>",
            "To find 10%, divide by 10",
            "Use 10% to find 20%, 30%, 5%, etc."
        ],
        examples: [
            {
                question: "What is 10% of 350?",
                steps: [
                    "10% = divide by 10",
                    "350 ÷ 10 = <strong>35</strong>"
                ],
                answer: "35"
            }
        ],
        tip: "💡 10% = move the decimal point one place left! 350 → 35.0"
    },
    5: {
        title: "Common Percentages",
        band: "Developing",
        description: "Build other percentages from 10%, 25%, and 50%.",
        keyPoints: [
            "20% = 10% × 2",
            "30% = 10% × 3",
            "5% = 10% ÷ 2",
            "75% = 50% + 25%"
        ],
        examples: [
            {
                question: "What is 30% of 60?",
                steps: [
                    "Find 10% first: 60 ÷ 10 = 6",
                    "30% = 10% × 3",
                    "= 6 × 3 = <strong>18</strong>"
                ],
                answer: "18"
            }
        ],
        tip: "💡 Build from 10%! It's your percentage building block."
    },
    6: {
        title: "% ↔ Fractions",
        band: "Developing",
        description: "Convert between percentages and fractions. They're just different ways to show parts.",
        keyPoints: [
            "<strong>% to fraction</strong>: put over 100, then simplify",
            "<strong>Fraction to %</strong>: × 100",
            "Know common ones by heart!"
        ],
        examples: [
            {
                question: "Convert 40% to a fraction",
                steps: [
                    "40% = 40/100",
                    "Simplify: ÷20 each",
                    "= <strong>⅖</strong>"
                ],
                answer: "40/100 = ⅖"
            }
        ],
        tip: "💡 Memorise: 50%=½, 25%=¼, 20%=⅕, 10%=1/10"
    },
    7: {
        title: "% ↔ Decimals",
        band: "Proficient",
        description: "Convert between percentages and decimals quickly.",
        keyPoints: [
            "<strong>% to decimal</strong>: divide by 100 (move point 2 left)",
            "<strong>Decimal to %</strong>: multiply by 100 (move point 2 right)",
            "45% = 0.45, 0.8 = 80%"
        ],
        examples: [
            {
                question: "Convert 0.35 to a percentage",
                steps: [
                    "Decimal to %: × 100",
                    "0.35 × 100 = <strong>35%</strong>"
                ],
                answer: "35%"
            }
        ],
        tip: "💡 % ÷ 100 = decimal. Decimal × 100 = %"
    },
    8: {
        title: "Finding % of Amount",
        band: "Proficient",
        description: "Calculate any percentage of a number using the methods you've learned.",
        keyPoints: [
            "Method 1: Find 10% or 1%, then multiply",
            "Method 2: Convert % to decimal, then multiply",
            "Choose whichever method is easier!"
        ],
        examples: [
            {
                question: "What is 35% of 80?",
                steps: [
                    "Method: Find 10%, then build",
                    "10% of 80 = 8",
                    "30% = 8 × 3 = 24",
                    "5% = 8 ÷ 2 = 4",
                    "35% = 24 + 4 = <strong>28</strong>"
                ],
                answer: "28"
            }
        ],
        tip: "💡 Break percentages into easier parts: 35% = 30% + 5%"
    },
    9: {
        title: "Percentage Problems",
        band: "Proficient",
        description: "Apply percentage skills to real problems like test scores and surveys.",
        keyPoints: [
            "Express as percentage: (part ÷ total) × 100",
            "Read what the question asks for",
            "Check your answer makes sense"
        ],
        examples: [
            {
                question: "Cian scored 18 out of 20 on a test. What percentage?",
                steps: [
                    "Percentage = (18 ÷ 20) × 100",
                    "= 0.9 × 100",
                    "= <strong>90%</strong>"
                ],
                answer: "90%"
            }
        ],
        tip: "💡 (Part ÷ Whole) × 100 = Percentage"
    },
    10: {
        title: "Discounts",
        band: "Advanced",
        description: "Calculate sale prices using percentage discounts.",
        keyPoints: [
            "<strong>Discount</strong> = amount taken off",
            "Sale price = Original price - Discount",
            "Or: Sale price = Original × (100% - discount%)"
        ],
        examples: [
            {
                question: "A €50 jacket has 20% off. What's the sale price?",
                steps: [
                    "Discount = 20% of €50 = €10",
                    "Sale price = €50 - €10 = <strong>€40</strong>"
                ],
                answer: "€40"
            }
        ],
        tip: "💡 20% off = you pay 80%! (100% - 20% = 80%)"
    },
    11: {
        title: "Word Problems",
        band: "Advanced",
        description: "Solve various real-world percentage problems.",
        keyPoints: [
            "Identify: finding %, finding amount, or comparing",
            "Use the method that fits",
            "Show your working clearly"
        ],
        examples: [
            {
                question: "A school has 400 students. 55% are girls. How many boys?",
                steps: [
                    "Girls = 55%, so Boys = 45%",
                    "45% of 400 = ?",
                    "10% = 40, so 45% = 4 × 40 + 20 = <strong>180 boys</strong>"
                ],
                answer: "180 boys"
            }
        ],
        tip: "💡 If you know one percentage, you can find the other (they add to 100%)!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You're a percentage pro! Show everything you've learned.",
        keyPoints: [
            "Convert between %, fractions, and decimals",
            "Find percentages of amounts",
            "Apply to discounts and real problems"
        ],
        examples: [
            {
                question: "A €80 game is reduced by 15%. What's the new price?",
                steps: [
                    "15% of €80: 10% = €8, 5% = €4, 15% = €12",
                    "New price = €80 - €12 = <strong>€68</strong>"
                ],
                answer: "€68"
            }
        ],
        tip: "🏆 Amazing! You're a Percentages Champion!"
    }
};

// ============================================================
// 8. TIME AND CLOCKS HELP CONTENT
// ============================================================
const timeAndClocksHelpContent = {
    1: {
        title: "O'Clock Times",
        band: "Foundation",
        description: "Learn to read o'clock times. The long hand points to 12, the short hand to the hour.",
        keyPoints: [
            "<strong>Short hand</strong> (hour hand) = which hour",
            "<strong>Long hand</strong> (minute hand) = how many minutes",
            "O'clock = long hand on 12"
        ],
        examples: [
            {
                question: "The short hand points to 3, long hand to 12. What time?",
                steps: [
                    "Short hand on 3 = 3 hours",
                    "Long hand on 12 = o'clock",
                    "Time = <strong>3 o'clock</strong>"
                ],
                answer: "3 o'clock (3:00)"
            }
        ],
        tip: "💡 The short hand is shorter because it moves slower (once around = 12 hours)!"
    },
    2: {
        title: "Half Past",
        band: "Foundation",
        description: "Half past means 30 minutes past the hour. The long hand points to 6.",
        keyPoints: [
            "<strong>Half past</strong> = 30 minutes",
            "Long hand points to <strong>6</strong>",
            "Short hand is between two numbers"
        ],
        examples: [
            {
                question: "Long hand on 6, short hand between 4 and 5. What time?",
                steps: [
                    "Long hand on 6 = half past",
                    "Short hand past 4 = hour is 4",
                    "Time = <strong>half past 4</strong> (4:30)"
                ],
                answer: "Half past 4 (4:30)"
            }
        ],
        tip: "💡 At half past, the short hand is halfway between two numbers!"
    },
    3: {
        title: "Quarter Past/To",
        band: "Foundation",
        description: "Quarter past (15 min) and quarter to (45 min) are important clock positions.",
        keyPoints: [
            "<strong>Quarter past</strong> = 15 minutes, long hand on 3",
            "<strong>Quarter to</strong> = 45 minutes, long hand on 9",
            "'To' means towards the NEXT hour"
        ],
        examples: [
            {
                question: "What is quarter to 5?",
                steps: [
                    "Quarter to = 45 minutes",
                    "'To 5' means approaching 5 o'clock",
                    "= <strong>4:45</strong>"
                ],
                answer: "4:45"
            }
        ],
        tip: "💡 Quarter = 15 minutes. There are 4 quarters in an hour (15 × 4 = 60)!"
    },
    4: {
        title: "5-Minute Intervals",
        band: "Developing",
        description: "Each number on the clock represents 5 minutes. Count in 5s!",
        keyPoints: [
            "1 = 5 min, 2 = 10 min, 3 = 15 min...",
            "Count in 5s from 12",
            "12 numbers × 5 minutes = 60 minutes"
        ],
        examples: [
            {
                question: "Long hand on 4, short hand past 7. What time?",
                steps: [
                    "Long hand on 4 = 4 × 5 = 20 minutes",
                    "Short hand past 7 = hour is 7",
                    "Time = <strong>7:20</strong>"
                ],
                answer: "7:20 (twenty past 7)"
            }
        ],
        tip: "💡 The clock numbers are a times-5 table: 1=5, 2=10, 3=15..."
    },
    5: {
        title: "Reading Any Time",
        band: "Developing",
        description: "Read any time by combining hour and minute hands.",
        keyPoints: [
            "Hour = what number the short hand has passed",
            "Minutes = count 5s to where long hand points",
            "Between numbers? Count extra minutes"
        ],
        examples: [
            {
                question: "Long hand between 5 and 6, short hand past 9. What time?",
                steps: [
                    "Long hand: 5 = 25 min, a bit more... ~27 min",
                    "Short hand past 9 = hour is 9",
                    "Time ≈ <strong>9:27</strong>"
                ],
                answer: "Approximately 9:27"
            }
        ],
        tip: "💡 Short hand shows hours, long hand shows minutes. Simple!"
    },
    6: {
        title: "Digital Time",
        band: "Developing",
        description: "Digital clocks show time with numbers: hours:minutes.",
        keyPoints: [
            "Format: <strong>HH:MM</strong> (hours:minutes)",
            "Hours before the colon, minutes after",
            "07:15 = 7:15 = quarter past 7"
        ],
        examples: [
            {
                question: "Write 'twenty to 9' in digital format",
                steps: [
                    "Twenty to 9 = 40 minutes past 8",
                    "= <strong>8:40</strong>"
                ],
                answer: "8:40"
            }
        ],
        tip: "💡 'To' times: subtract from 60 for minutes, use previous hour!"
    },
    7: {
        title: "24-Hour Clock",
        band: "Proficient",
        description: "The 24-hour clock counts from 00:00 to 23:59. Used for timetables!",
        keyPoints: [
            "Morning (AM): same as 12-hour (9am = 09:00)",
            "Afternoon/Evening (PM): add 12 (3pm = 15:00)",
            "Midnight = 00:00, Noon = 12:00"
        ],
        examples: [
            {
                question: "Convert 3:45 PM to 24-hour time",
                steps: [
                    "PM = afternoon, so add 12 to hours",
                    "3 + 12 = 15",
                    "= <strong>15:45</strong>"
                ],
                answer: "15:45"
            }
        ],
        tip: "💡 After 12:59, keep adding: 13:00 (1pm), 14:00 (2pm)..."
    },
    8: {
        title: "Elapsed Time",
        band: "Proficient",
        description: "Calculate how much time has passed between two times.",
        keyPoints: [
            "<strong>Count on</strong> from start time to end time",
            "Count to the next hour, then add remaining",
            "Or subtract start from end"
        ],
        examples: [
            {
                question: "How long from 9:45 to 11:20?",
                steps: [
                    "9:45 to 10:00 = 15 min",
                    "10:00 to 11:00 = 1 hour",
                    "11:00 to 11:20 = 20 min",
                    "Total = <strong>1 hour 35 min</strong>"
                ],
                answer: "1 hour 35 minutes"
            }
        ],
        tip: "💡 Break it into chunks: to the hour, full hours, then remaining minutes!"
    },
    9: {
        title: "Timetables",
        band: "Proficient",
        description: "Read bus, train, and school timetables using 24-hour time.",
        keyPoints: [
            "Timetables often use 24-hour time",
            "Read across rows for one journey",
            "Calculate journey time by finding the difference"
        ],
        examples: [
            {
                question: "A bus leaves at 14:30 and arrives at 15:15. How long is the journey?",
                steps: [
                    "14:30 to 15:00 = 30 min",
                    "15:00 to 15:15 = 15 min",
                    "Total = <strong>45 minutes</strong>"
                ],
                answer: "45 minutes"
            }
        ],
        tip: "💡 Highlight your row in timetables to avoid reading the wrong times!"
    },
    10: {
        title: "Time Calculations",
        band: "Advanced",
        description: "Add and subtract times, dealing with hours and minutes.",
        keyPoints: [
            "60 minutes = 1 hour (carry over when adding)",
            "Borrow from hours when subtracting minutes",
            "Keep hours and minutes aligned"
        ],
        examples: [
            {
                question: "Add: 2 hours 45 min + 1 hour 30 min",
                steps: [
                    "Add minutes: 45 + 30 = 75 min = 1 hr 15 min",
                    "Add hours: 2 + 1 + 1 = 4 hours",
                    "Total = <strong>4 hours 15 min</strong>"
                ],
                answer: "4 hours 15 minutes"
            }
        ],
        tip: "💡 Remember: 60 minutes = 1 hour, not 100!"
    },
    11: {
        title: "Scheduling Problems",
        band: "Advanced",
        description: "Solve real-world scheduling and timing problems.",
        keyPoints: [
            "Start time + Duration = End time",
            "End time - Duration = Start time",
            "End time - Start time = Duration"
        ],
        examples: [
            {
                question: "A film is 1 hr 45 min long. If it ends at 9:30 PM, when did it start?",
                steps: [
                    "Work backwards from 9:30",
                    "9:30 - 45 min = 8:45",
                    "8:45 - 1 hr = <strong>7:45 PM</strong>"
                ],
                answer: "7:45 PM"
            }
        ],
        tip: "💡 Draw a timeline to help visualise the problem!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You're a time-telling expert! Master all aspects of time.",
        keyPoints: [
            "Read analogue and digital clocks confidently",
            "Convert between 12-hour and 24-hour",
            "Calculate elapsed time and solve scheduling problems"
        ],
        examples: [
            {
                question: "A train leaves Dublin at 13:45 and takes 2 hr 35 min. What time does it arrive?",
                steps: [
                    "13:45 + 2 hr = 15:45",
                    "15:45 + 35 min = <strong>16:20</strong>"
                ],
                answer: "16:20 (4:20 PM)"
            }
        ],
        tip: "🏆 Excellent! You're a Time & Clocks Champion!"
    }
};

// ============================================================
// 9. MONEY SKILLS HELP CONTENT
// ============================================================
const moneySkillsHelpContent = {
    1: {
        title: "Coins and Notes",
        band: "Foundation",
        description: "Learn to recognise and know the value of Euro coins and notes.",
        keyPoints: [
            "<strong>Coins</strong>: 1c, 2c, 5c, 10c, 20c, 50c, €1, €2",
            "<strong>Notes</strong>: €5, €10, €20, €50, €100",
            "100 cent = €1"
        ],
        examples: [
            {
                question: "How many 20c coins make €1?",
                steps: [
                    "€1 = 100 cent",
                    "100 ÷ 20 = <strong>5 coins</strong>"
                ],
                answer: "5 coins"
            }
        ],
        tip: "💡 Know your coins: copper (1c, 2c, 5c), gold (10c, 20c, 50c), bi-metal (€1, €2)!"
    },
    2: {
        title: "Counting Money",
        band: "Foundation",
        description: "Count collections of coins and notes to find the total.",
        keyPoints: [
            "Start with the <strong>highest value</strong> coins/notes",
            "Add in order from largest to smallest",
            "Keep a running total"
        ],
        examples: [
            {
                question: "Count: €1, 50c, 20c, 10c, 5c",
                steps: [
                    "€1.00 + 50c = €1.50",
                    "€1.50 + 20c = €1.70",
                    "€1.70 + 10c = €1.80",
                    "€1.80 + 5c = <strong>€1.85</strong>"
                ],
                answer: "€1.85"
            }
        ],
        tip: "💡 Organise coins by value before counting!"
    },
    3: {
        title: "Making Amounts",
        band: "Foundation",
        description: "Use different combinations of coins to make a given amount.",
        keyPoints: [
            "There are often <strong>many ways</strong> to make the same amount",
            "Start with large coins, fill in with smaller ones",
            "Use fewest coins when possible"
        ],
        examples: [
            {
                question: "Make €2.35 using the fewest coins",
                steps: [
                    "€2 coin = €2.00",
                    "Need 35c more",
                    "20c + 10c + 5c = 35c",
                    "Total: <strong>€2 + 20c + 10c + 5c</strong>"
                ],
                answer: "€2 + 20c + 10c + 5c (4 coins)"
            }
        ],
        tip: "💡 Fewest coins = use largest coins possible!"
    },
    4: {
        title: "Adding Money",
        band: "Developing",
        description: "Add amounts of money using the same skills as adding decimals.",
        keyPoints: [
            "<strong>Line up the decimal points</strong>",
            "Add cent first, then euros",
            "Carry over when cent > 99"
        ],
        examples: [
            {
                question: "€3.45 + €2.80 = ?",
                steps: [
                    "Line up: €3.45",
                    "       + €2.80",
                    "45c + 80c = 125c = €1.25",
                    "€3 + €2 + €1 = €6.25",
                    "Answer: <strong>€6.25</strong>"
                ],
                answer: "€6.25"
            }
        ],
        tip: "💡 100c = €1. If cent adds to 100+, carry €1!"
    },
    5: {
        title: "Subtracting Money",
        band: "Developing",
        description: "Subtract money amounts to find the difference or change.",
        keyPoints: [
            "Line up decimal points",
            "Exchange if needed (borrow €1 = 100c)",
            "This is how you calculate change!"
        ],
        examples: [
            {
                question: "€10.00 - €6.75 = ?",
                steps: [
                    "Can't do 0c - 75c, borrow €1",
                    "100c - 75c = 25c",
                    "€9 - €6 = €3",
                    "Answer: <strong>€3.25</strong>"
                ],
                answer: "€3.25"
            }
        ],
        tip: "💡 Need to borrow? €1 becomes 100 cent!"
    },
    6: {
        title: "Giving Change",
        band: "Developing",
        description: "Calculate change from a purchase. This is subtraction!",
        keyPoints: [
            "<strong>Change = Amount paid - Cost</strong>",
            "Count up from cost to amount paid",
            "Or subtract directly"
        ],
        examples: [
            {
                question: "Pay €5 for item costing €3.35. What's the change?",
                steps: [
                    "Change = €5.00 - €3.35",
                    "Count up: €3.35 → €3.40 (5c) → €4 (60c) → €5 (€1)",
                    "5c + 60c + €1 = <strong>€1.65</strong>"
                ],
                answer: "€1.65"
            }
        ],
        tip: "💡 Shopkeepers count up: 'That's €3.35... €4... €5. €1.65 change!'"
    },
    7: {
        title: "Shopping Problems",
        band: "Proficient",
        description: "Solve word problems involving buying multiple items.",
        keyPoints: [
            "List what's being bought",
            "Add all costs together",
            "Calculate change if they pay with larger note"
        ],
        examples: [
            {
                question: "Aoife buys bread (€1.80) and milk (€1.45). She pays with €5. What's her change?",
                steps: [
                    "Total cost: €1.80 + €1.45 = €3.25",
                    "Change: €5.00 - €3.25 = <strong>€1.75</strong>"
                ],
                answer: "€1.75"
            }
        ],
        tip: "💡 Find total cost first, then calculate change!"
    },
    8: {
        title: "Comparing Prices",
        band: "Proficient",
        description: "Compare prices to find which option is cheaper or better value.",
        keyPoints: [
            "Line up prices to compare easily",
            "Sometimes bigger packs are better value",
            "Calculate 'per item' cost for fair comparison"
        ],
        examples: [
            {
                question: "6 apples for €2.40 or 4 apples for €1.80. Which is better value?",
                steps: [
                    "6 for €2.40: €2.40 ÷ 6 = 40c each",
                    "4 for €1.80: €1.80 ÷ 4 = 45c each",
                    "<strong>6 for €2.40 is better value</strong>"
                ],
                answer: "6 for €2.40 (40c each)"
            }
        ],
        tip: "💡 Price per item = Total ÷ Number of items"
    },
    9: {
        title: "Budgeting",
        band: "Proficient",
        description: "Plan spending to stay within a budget.",
        keyPoints: [
            "<strong>Budget</strong> = maximum amount you can spend",
            "Add up costs, check against budget",
            "Don't forget to leave room for essentials!"
        ],
        examples: [
            {
                question: "Cian has €20. Books cost €12.50, lunch €4.75. Can he buy both?",
                steps: [
                    "Total needed: €12.50 + €4.75 = €17.25",
                    "Budget: €20.00",
                    "€17.25 < €20.00 ✓",
                    "<strong>Yes, with €2.75 to spare!</strong>"
                ],
                answer: "Yes (€2.75 left over)"
            }
        ],
        tip: "💡 Always check if total ≤ budget before buying!"
    },
    10: {
        title: "Multi-Step Problems",
        band: "Advanced",
        description: "Solve complex money problems with multiple operations.",
        keyPoints: [
            "Break into steps",
            "Do one calculation at a time",
            "Check your answer makes sense"
        ],
        examples: [
            {
                question: "3 children share €15 equally. Each spends €2.50. How much does each have left?",
                steps: [
                    "Each gets: €15 ÷ 3 = €5",
                    "Each spends: €2.50",
                    "Left: €5.00 - €2.50 = <strong>€2.50 each</strong>"
                ],
                answer: "€2.50 each"
            }
        ],
        tip: "💡 List the steps before calculating!"
    },
    11: {
        title: "Best Value",
        band: "Advanced",
        description: "Analyse deals and special offers to find the best purchase.",
        keyPoints: [
            "Calculate the 'unit price' (price per item)",
            "Watch for 'buy one get one free' (halves unit price!)",
            "Sometimes buying more saves money"
        ],
        examples: [
            {
                question: "Small juice €1.20 (250ml) or Large €2.00 (500ml). Which is better value?",
                steps: [
                    "Small: €1.20 ÷ 250 = 0.48c per ml",
                    "Large: €2.00 ÷ 500 = 0.40c per ml",
                    "<strong>Large is better value</strong>"
                ],
                answer: "Large (cheaper per ml)"
            }
        ],
        tip: "💡 Unit price lets you compare fairly - same amount for same cost!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You're a money master! Apply all your skills to complex problems.",
        keyPoints: [
            "Know your coins and notes",
            "Add, subtract, and calculate change confidently",
            "Compare prices and manage budgets"
        ],
        examples: [
            {
                question: "A family buys 4 cinema tickets at €9.50 each and €8.75 of snacks. They pay with €50. What change?",
                steps: [
                    "Tickets: 4 × €9.50 = €38.00",
                    "Total: €38.00 + €8.75 = €46.75",
                    "Change: €50.00 - €46.75 = <strong>€3.25</strong>"
                ],
                answer: "€3.25"
            }
        ],
        tip: "🏆 Brilliant! You're a Money Skills Champion!"
    }
};

// ============================================================
// 10. MEASUREMENT HELP CONTENT
// ============================================================
const measurementHelpContent = {
    1: {
        title: "Length (cm)",
        band: "Foundation",
        description: "Centimetres (cm) measure shorter lengths. There are 100 cm in 1 metre.",
        keyPoints: [
            "<strong>cm</strong> = centimetre (small lengths)",
            "Your fingernail is about 1 cm wide",
            "A ruler is usually 30 cm long"
        ],
        examples: [
            {
                question: "A pencil is 18 cm long. Is that longer or shorter than a 30 cm ruler?",
                steps: [
                    "18 cm vs 30 cm",
                    "18 < 30",
                    "<strong>Shorter</strong> than the ruler"
                ],
                answer: "Shorter"
            }
        ],
        tip: "💡 Use cm for measuring small things like pencils, books, your hand!"
    },
    2: {
        title: "Length (m, km)",
        band: "Foundation",
        description: "Metres (m) for medium lengths, kilometres (km) for long distances.",
        keyPoints: [
            "<strong>m</strong> = metre (room lengths, heights)",
            "<strong>km</strong> = kilometre (distances between places)",
            "1 km = 1,000 m"
        ],
        examples: [
            {
                question: "Would you measure the length of a football pitch in cm, m, or km?",
                steps: [
                    "A pitch is big but not super far",
                    "cm = too small",
                    "km = too big",
                    "Answer: <strong>metres (m)</strong>"
                ],
                answer: "Metres (about 100m)"
            }
        ],
        tip: "💡 Think: cm for small, m for room-sized, km for map distances!"
    },
    3: {
        title: "Measuring Length",
        band: "Foundation",
        description: "Use rulers and measuring tapes correctly to measure length.",
        keyPoints: [
            "Start measuring from <strong>0</strong>, not the edge of the ruler",
            "Keep the ruler <strong>straight</strong>",
            "Read where the object ends"
        ],
        examples: [
            {
                question: "A line starts at 0 and ends at 7.5 on a ruler. How long is it?",
                steps: [
                    "Start: 0 cm",
                    "End: 7.5 cm",
                    "Length = <strong>7.5 cm</strong>"
                ],
                answer: "7.5 cm"
            }
        ],
        tip: "💡 Always check where 0 is - some rulers have a gap at the start!"
    },
    4: {
        title: "Mass (g, kg)",
        band: "Developing",
        description: "Mass (weight) is measured in grams (g) and kilograms (kg).",
        keyPoints: [
            "<strong>g</strong> = gram (light things)",
            "<strong>kg</strong> = kilogram (heavier things)",
            "1 kg = 1,000 g"
        ],
        examples: [
            {
                question: "A bag of sugar weighs 1 kg. How many grams is that?",
                steps: [
                    "1 kg = 1,000 g",
                    "So 1 kg bag = <strong>1,000 g</strong>"
                ],
                answer: "1,000 g"
            }
        ],
        tip: "💡 A paperclip is about 1g. A bag of sugar is 1kg. A child is about 30kg!"
    },
    5: {
        title: "Capacity (ml, l)",
        band: "Developing",
        description: "Capacity measures how much liquid a container holds.",
        keyPoints: [
            "<strong>ml</strong> = millilitre (small amounts)",
            "<strong>l</strong> = litre (larger amounts)",
            "1 l = 1,000 ml"
        ],
        examples: [
            {
                question: "A medicine spoon holds 5 ml. A bottle holds 100 ml. How many spoonfuls in the bottle?",
                steps: [
                    "100 ml ÷ 5 ml = <strong>20 spoonfuls</strong>"
                ],
                answer: "20 spoonfuls"
            }
        ],
        tip: "💡 A teaspoon ≈ 5ml. A water bottle ≈ 500ml. A big milk carton = 1 litre!"
    },
    6: {
        title: "Comparing Measures",
        band: "Developing",
        description: "Compare measurements to see which is bigger, smaller, or equal.",
        keyPoints: [
            "Make sure units are the <strong>same</strong> before comparing",
            "Convert if necessary",
            "Then compare the numbers"
        ],
        examples: [
            {
                question: "Which is longer: 150 cm or 1.2 m?",
                steps: [
                    "Convert to same unit: 1.2 m = 120 cm",
                    "Compare: 150 cm vs 120 cm",
                    "<strong>150 cm is longer</strong>"
                ],
                answer: "150 cm"
            }
        ],
        tip: "💡 Always convert to the same unit before comparing!"
    },
    7: {
        title: "Converting Length",
        band: "Proficient",
        description: "Convert between cm, m, and km using multiplication and division.",
        keyPoints: [
            "<strong>cm → m</strong>: ÷ 100",
            "<strong>m → cm</strong>: × 100",
            "<strong>m → km</strong>: ÷ 1000, <strong>km → m</strong>: × 1000"
        ],
        examples: [
            {
                question: "Convert 3.5 km to metres",
                steps: [
                    "km to m: multiply by 1,000",
                    "3.5 × 1,000 = <strong>3,500 m</strong>"
                ],
                answer: "3,500 m"
            }
        ],
        tip: "💡 Going to smaller unit? × (number gets bigger). Bigger unit? ÷"
    },
    8: {
        title: "Converting Mass",
        band: "Proficient",
        description: "Convert between grams and kilograms.",
        keyPoints: [
            "<strong>g → kg</strong>: ÷ 1,000",
            "<strong>kg → g</strong>: × 1,000",
            "1.5 kg = 1,500 g"
        ],
        examples: [
            {
                question: "Convert 2,750 g to kg",
                steps: [
                    "g to kg: divide by 1,000",
                    "2,750 ÷ 1,000 = <strong>2.75 kg</strong>"
                ],
                answer: "2.75 kg"
            }
        ],
        tip: "💡 The decimal point moves 3 places when converting g ↔ kg!"
    },
    9: {
        title: "Converting Capacity",
        band: "Proficient",
        description: "Convert between millilitres and litres.",
        keyPoints: [
            "<strong>ml → l</strong>: ÷ 1,000",
            "<strong>l → ml</strong>: × 1,000",
            "0.5 l = 500 ml"
        ],
        examples: [
            {
                question: "A jug holds 1.25 litres. How many ml?",
                steps: [
                    "l to ml: multiply by 1,000",
                    "1.25 × 1,000 = <strong>1,250 ml</strong>"
                ],
                answer: "1,250 ml"
            }
        ],
        tip: "💡 Same as mass: × 1,000 going smaller, ÷ 1,000 going bigger!"
    },
    10: {
        title: "Mixed Conversions",
        band: "Advanced",
        description: "Convert between any metric units for length, mass, and capacity.",
        keyPoints: [
            "Know the conversion factors",
            "Identify: smaller → bigger (÷) or bigger → smaller (×)",
            "Check your answer makes sense"
        ],
        examples: [
            {
                question: "Express 4.2 km + 350 m in metres",
                steps: [
                    "Convert 4.2 km to m: 4.2 × 1,000 = 4,200 m",
                    "Add: 4,200 m + 350 m = <strong>4,550 m</strong>"
                ],
                answer: "4,550 m"
            }
        ],
        tip: "💡 Convert everything to the same unit first, then calculate!"
    },
    11: {
        title: "Word Problems",
        band: "Advanced",
        description: "Apply measurement skills to real-world problems.",
        keyPoints: [
            "Identify what measurement is needed",
            "Choose appropriate units",
            "Convert if necessary"
        ],
        examples: [
            {
                question: "A recipe needs 750ml of milk. You have 2 litres. How much is left after making the recipe?",
                steps: [
                    "2 l = 2,000 ml",
                    "2,000 ml - 750 ml = 1,250 ml",
                    "= <strong>1.25 litres</strong>"
                ],
                answer: "1.25 l (1,250 ml)"
            }
        ],
        tip: "💡 Convert to the same unit, solve, then convert back if needed!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You're a measurement expert! Show your skills across all units.",
        keyPoints: [
            "Know metric prefixes: kilo (1000), centi (1/100), milli (1/1000)",
            "Convert confidently",
            "Apply to real problems"
        ],
        examples: [
            {
                question: "A parcel weighs 2.4 kg. Postage is 15c per 100g. What's the cost?",
                steps: [
                    "2.4 kg = 2,400 g",
                    "2,400 ÷ 100 = 24 lots of 100g",
                    "24 × 15c = 360c = <strong>€3.60</strong>"
                ],
                answer: "€3.60"
            }
        ],
        tip: "🏆 Excellent! You're a Measurement Champion!"
    }
};

// ============================================================
// 11. DATA AND CHARTS HELP CONTENT
// ============================================================
const dataAndChartsHelpContent = {
    1: {
        title: "Tally Charts",
        band: "Foundation",
        description: "Tally charts use marks to count. Every 5th mark crosses the previous 4.",
        keyPoints: [
            "Draw | | | | then cross with fifth: <s>| | | |</s>",
            "Each bundle of 5 makes counting easier",
            "Count in 5s, then add extras"
        ],
        examples: [
            {
                question: "What number does |||| |||| ||| represent?",
                steps: [
                    "Two bundles of 5: 5 + 5 = 10",
                    "Plus 3 more: 10 + 3 = <strong>13</strong>"
                ],
                answer: "13"
            }
        ],
        tip: "💡 The crossing line bundles four marks into a group of 5!"
    },
    2: {
        title: "Pictograms",
        band: "Foundation",
        description: "Pictograms use pictures to represent data. Always check the key!",
        keyPoints: [
            "Each picture represents a number (check the <strong>key</strong>)",
            "Half picture = half the value",
            "Count pictures, then multiply by key value"
        ],
        examples: [
            {
                question: "A pictogram shows 🍎🍎🍎 for Monday. Key: 🍎 = 4 apples. How many apples?",
                steps: [
                    "Count symbols: 3 apples",
                    "Each = 4",
                    "Total: 3 × 4 = <strong>12 apples</strong>"
                ],
                answer: "12 apples"
            }
        ],
        tip: "💡 ALWAYS read the key first - one picture might equal 2, 5, 10..."
    },
    3: {
        title: "Reading Bar Charts",
        band: "Foundation",
        description: "Bar charts use bars to show amounts. Read the height against the scale.",
        keyPoints: [
            "The <strong>scale</strong> (usually on the left) tells you the values",
            "Read where the <strong>top of the bar</strong> lines up",
            "Compare bars to see which is biggest/smallest"
        ],
        examples: [
            {
                question: "A bar chart shows Monday's bar reaching 15. What does this mean?",
                steps: [
                    "Find Monday's bar",
                    "Read across to the scale",
                    "Value = <strong>15</strong>"
                ],
                answer: "15 (of whatever is being measured)"
            }
        ],
        tip: "💡 Check what the scale goes up in: 1s, 2s, 5s, 10s?"
    },
    4: {
        title: "Reading Tables",
        band: "Developing",
        description: "Tables organise data in rows and columns. Find where row and column meet.",
        keyPoints: [
            "<strong>Rows</strong> go across (horizontal)",
            "<strong>Columns</strong> go down (vertical)",
            "Find the cell where row and column intersect"
        ],
        examples: [
            {
                question: "In a table, find the value for 'Blue' (column) and 'Girls' (row)",
                steps: [
                    "Find 'Girls' row",
                    "Find 'Blue' column",
                    "Read the value where they meet"
                ],
                answer: "The value in that cell"
            }
        ],
        tip: "💡 Use your finger to trace along the row and down the column!"
    },
    5: {
        title: "Creating Bar Charts",
        band: "Developing",
        description: "Draw bar charts from data. Remember labels, title, and scale!",
        keyPoints: [
            "Choose an appropriate <strong>scale</strong>",
            "Draw bars of correct height",
            "Add <strong>title</strong>, <strong>labels</strong>, and <strong>scale</strong>"
        ],
        examples: [
            {
                question: "Data: Red=8, Blue=12, Green=6. What scale would you use?",
                steps: [
                    "Highest value: 12",
                    "A scale of 2s works well (0, 2, 4, 6, 8, 10, 12)",
                    "Bars: Red=8, Blue=12, Green=6"
                ],
                answer: "Scale in 2s up to at least 12"
            }
        ],
        tip: "💡 Choose a scale that fits your data and is easy to read!"
    },
    6: {
        title: "Interpreting Data",
        band: "Developing",
        description: "Answer questions about what data shows. Look for patterns and comparisons.",
        keyPoints: [
            "Find <strong>highest</strong> and <strong>lowest</strong> values",
            "Calculate <strong>differences</strong>",
            "Look for <strong>patterns</strong> or trends"
        ],
        examples: [
            {
                question: "Bar chart shows: Mon=15, Tue=10, Wed=20. Which day had most? How many more than Tuesday?",
                steps: [
                    "Most: Wednesday (20)",
                    "Wed - Tue = 20 - 10 = <strong>10 more</strong>"
                ],
                answer: "Wednesday; 10 more than Tuesday"
            }
        ],
        tip: "💡 Read questions carefully - 'how many more' means find the difference!"
    },
    7: {
        title: "Finding Mode",
        band: "Proficient",
        description: "The mode is the most common value - it appears most often.",
        keyPoints: [
            "<strong>Mode</strong> = most frequent value",
            "Count how many times each value appears",
            "There can be more than one mode, or no mode"
        ],
        examples: [
            {
                question: "Find the mode: 3, 5, 5, 7, 5, 8, 7",
                steps: [
                    "3 appears 1 time",
                    "5 appears 3 times ← most",
                    "7 appears 2 times",
                    "8 appears 1 time",
                    "Mode = <strong>5</strong>"
                ],
                answer: "5"
            }
        ],
        tip: "💡 Mode = Most Often Data Entry!"
    },
    8: {
        title: "Finding Mean",
        band: "Proficient",
        description: "The mean is the average. Add all values, then divide by how many.",
        keyPoints: [
            "<strong>Mean = Total ÷ Number of values</strong>",
            "Add up all the values first",
            "Count how many values there are"
        ],
        examples: [
            {
                question: "Find the mean: 4, 6, 8, 10, 12",
                steps: [
                    "Total: 4+6+8+10+12 = 40",
                    "Number of values: 5",
                    "Mean: 40 ÷ 5 = <strong>8</strong>"
                ],
                answer: "8"
            }
        ],
        tip: "💡 Mean = Add them all up, share them all out!"
    },
    9: {
        title: "Comparing Data",
        band: "Proficient",
        description: "Compare two sets of data using mean, mode, range, or charts.",
        keyPoints: [
            "Calculate <strong>same measure</strong> for both sets",
            "Higher mean = higher average",
            "Larger range = more spread out"
        ],
        examples: [
            {
                question: "Class A mean: 65%. Class B mean: 72%. Which class did better on average?",
                steps: [
                    "Compare means: 65% vs 72%",
                    "72% > 65%",
                    "<strong>Class B</strong> did better on average"
                ],
                answer: "Class B"
            }
        ],
        tip: "💡 Make sure you're comparing the same type of measure!"
    },
    10: {
        title: "Data Analysis",
        band: "Advanced",
        description: "Analyse data sets to draw conclusions and answer questions.",
        keyPoints: [
            "Look at <strong>all the statistics</strong> together",
            "Consider what the data is <strong>telling you</strong>",
            "Think about <strong>why</strong> patterns might exist"
        ],
        examples: [
            {
                question: "Test scores: Mean=68, Mode=72, Range=35. What does this tell us?",
                steps: [
                    "Mean (68): average performance",
                    "Mode (72): most common score",
                    "Range (35): scores varied by 35 marks",
                    "Most scored around 72, but there's quite a spread"
                ],
                answer: "Most scored 72, average was 68, with a 35-point spread"
            }
        ],
        tip: "💡 Different statistics tell different parts of the story!"
    },
    11: {
        title: "Survey Problems",
        band: "Advanced",
        description: "Design surveys, collect data, and analyse results.",
        keyPoints: [
            "Ask <strong>clear questions</strong>",
            "Use <strong>categories</strong> that cover all options",
            "Present results clearly"
        ],
        examples: [
            {
                question: "45 students surveyed: 18 walk, 15 by bus, 12 by car. What fraction walk?",
                steps: [
                    "Walkers: 18",
                    "Total: 45",
                    "Fraction: 18/45 = <strong>2/5</strong>"
                ],
                answer: "2/5 (or 40%)"
            }
        ],
        tip: "💡 Survey tip: make sure everyone's answer fits a category!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You're a data expert! Use all your skills to analyse and present information.",
        keyPoints: [
            "Read and create charts confidently",
            "Calculate mean, mode, and range",
            "Draw conclusions from data"
        ],
        examples: [
            {
                question: "Scores: 45, 52, 48, 52, 58, 52, 47. Find mean, mode, range.",
                steps: [
                    "Mean: 354 ÷ 7 = 50.6 (to 1 d.p.)",
                    "Mode: 52 (appears 3 times)",
                    "Range: 58 - 45 = 13"
                ],
                answer: "Mean=50.6, Mode=52, Range=13"
            }
        ],
        tip: "🏆 Fantastic! You're a Data & Charts Champion!"
    }
};

// ============================================================
// 12. NUMBER PATTERNS HELP CONTENT
// ============================================================
const numberPatternsHelpContent = {
    1: {
        title: "Counting Patterns",
        band: "Foundation",
        description: "Spot patterns when counting in 2s, 5s, 10s, and other numbers.",
        keyPoints: [
            "<strong>Count in 2s</strong>: 2, 4, 6, 8, 10... (even numbers)",
            "<strong>Count in 5s</strong>: 5, 10, 15, 20... (ends in 0 or 5)",
            "<strong>Count in 10s</strong>: 10, 20, 30, 40..."
        ],
        examples: [
            {
                question: "What comes next: 5, 10, 15, 20, ?",
                steps: [
                    "Pattern: counting in 5s",
                    "Next: 20 + 5 = <strong>25</strong>"
                ],
                answer: "25"
            }
        ],
        tip: "💡 Look at the gaps between numbers to find the pattern!"
    },
    2: {
        title: "Adding Patterns",
        band: "Foundation",
        description: "Some patterns add the same number each time.",
        keyPoints: [
            "Find the <strong>common difference</strong> (what's being added)",
            "Add this to each term to get the next",
            "Example: +3 each time: 2, 5, 8, 11, 14..."
        ],
        examples: [
            {
                question: "Find the pattern and next two terms: 7, 12, 17, 22, ?, ?",
                steps: [
                    "Difference: 12-7=5, 17-12=5, 22-17=5",
                    "Pattern: +5 each time",
                    "Next: 22+5=27, 27+5=<strong>32</strong>"
                ],
                answer: "27, 32"
            }
        ],
        tip: "💡 Calculate the difference between consecutive terms!"
    },
    3: {
        title: "Subtracting Patterns",
        band: "Foundation",
        description: "Some patterns subtract the same number each time (decreasing).",
        keyPoints: [
            "Numbers get <strong>smaller</strong> each time",
            "Find what's being subtracted",
            "Example: -4 each time: 50, 46, 42, 38..."
        ],
        examples: [
            {
                question: "Find the pattern and next term: 100, 93, 86, 79, ?",
                steps: [
                    "Difference: 93-100=-7, 86-93=-7",
                    "Pattern: -7 each time",
                    "Next: 79-7=<strong>72</strong>"
                ],
                answer: "72"
            }
        ],
        tip: "💡 Decreasing patterns have negative differences!"
    },
    4: {
        title: "Times Table Patterns",
        band: "Developing",
        description: "Times tables create patterns. Recognise them to spot relationships.",
        keyPoints: [
            "×3 pattern: 3, 6, 9, 12, 15...",
            "×4 pattern: 4, 8, 12, 16, 20...",
            "Multiples follow times table patterns"
        ],
        examples: [
            {
                question: "Which times table: 6, 12, 18, 24, 30?",
                steps: [
                    "Check differences: all +6",
                    "These are multiples of 6",
                    "Answer: <strong>6 times table</strong>"
                ],
                answer: "6 times table"
            }
        ],
        tip: "💡 Multiples of a number follow the same pattern as its times table!"
    },
    5: {
        title: "Finding the Rule",
        band: "Developing",
        description: "Express the pattern as a rule in words or as a formula.",
        keyPoints: [
            "Look at <strong>what's happening</strong> to get from one term to the next",
            "Write it as: 'add 3 each time' or 'multiply by 2'",
            "Test your rule on all terms"
        ],
        examples: [
            {
                question: "Find the rule: 4, 9, 14, 19, 24",
                steps: [
                    "9-4=5, 14-9=5, 19-14=5, 24-19=5",
                    "Rule: <strong>Add 5 each time</strong>",
                    "Or: Start at 4, +5"
                ],
                answer: "Add 5 (or +5)"
            }
        ],
        tip: "💡 A rule should work for ALL terms in the sequence!"
    },
    6: {
        title: "Continuing Patterns",
        band: "Developing",
        description: "Use the rule to find more terms in a sequence.",
        keyPoints: [
            "Apply the rule to find next terms",
            "You can find any term if you know the rule",
            "Check by working backwards too"
        ],
        examples: [
            {
                question: "Rule: Start at 3, add 4 each time. Find the first 5 terms.",
                steps: [
                    "1st term: 3",
                    "2nd: 3+4=7",
                    "3rd: 7+4=11",
                    "4th: 11+4=15",
                    "5th: 15+4=<strong>19</strong>"
                ],
                answer: "3, 7, 11, 15, 19"
            }
        ],
        tip: "💡 Keep applying the rule to extend the pattern!"
    },
    7: {
        title: "Shape Patterns",
        band: "Proficient",
        description: "Patterns can involve shapes, where numbers grow in visual ways.",
        keyPoints: [
            "Count objects in each stage",
            "Look for how many are <strong>added</strong> each time",
            "Draw the next stage to check"
        ],
        examples: [
            {
                question: "Triangle pattern: 3, 6, 10, 15... (dots in triangles). What's next?",
                steps: [
                    "Differences: +3, +4, +5",
                    "Pattern in differences: add one more each time",
                    "Next difference: +6",
                    "Next term: 15+6=<strong>21</strong>"
                ],
                answer: "21"
            }
        ],
        tip: "💡 If the differences aren't constant, look for a pattern in the differences!"
    },
    8: {
        title: "Two-Step Patterns",
        band: "Proficient",
        description: "Some patterns need two operations to find the rule.",
        keyPoints: [
            "Position-to-term rules: 'multiply position by 2, add 1'",
            "Example: Position 1→3, 2→5, 3→7 (×2 +1)",
            "Use a table to spot the relationship"
        ],
        examples: [
            {
                question: "Find rule: Position 1=5, 2=8, 3=11, 4=14",
                steps: [
                    "Differences: +3 each time",
                    "When position=1, term=5",
                    "Rule: <strong>3n + 2</strong> (3×position + 2)",
                    "Check: 3×1+2=5 ✓, 3×2+2=8 ✓"
                ],
                answer: "3n + 2 (multiply by 3, add 2)"
            }
        ],
        tip: "💡 The difference gives you the multiplier in 'an + b' rules!"
    },
    9: {
        title: "Missing Numbers",
        band: "Proficient",
        description: "Find missing terms in a sequence by working out the pattern.",
        keyPoints: [
            "Find the rule using the terms you know",
            "Work forwards or backwards to find missing terms",
            "Check your answer fits the pattern"
        ],
        examples: [
            {
                question: "Find the missing number: 8, ?, 20, 26, 32",
                steps: [
                    "Difference from 20 to 26: +6",
                    "Difference from 26 to 32: +6",
                    "Rule: +6",
                    "8 + 6 = <strong>14</strong>"
                ],
                answer: "14"
            }
        ],
        tip: "💡 Use known terms to figure out the pattern, then fill in gaps!"
    },
    10: {
        title: "Complex Patterns",
        band: "Advanced",
        description: "Tackle more challenging sequences with varying differences.",
        keyPoints: [
            "Some sequences have <strong>changing differences</strong>",
            "Look for patterns in the second level of differences",
            "Triangular, square, cube numbers have special patterns"
        ],
        examples: [
            {
                question: "Sequence: 1, 4, 9, 16, 25... What's the pattern?",
                steps: [
                    "These are: 1², 2², 3², 4², 5²",
                    "Pattern: <strong>Square numbers</strong>",
                    "Next: 6² = 36"
                ],
                answer: "Square numbers (n²)"
            }
        ],
        tip: "💡 Recognise special sequences: squares (1,4,9,16), triangles (1,3,6,10), cubes (1,8,27)!"
    },
    11: {
        title: "Pattern Problems",
        band: "Advanced",
        description: "Apply pattern skills to solve real problems.",
        keyPoints: [
            "Set up a table of values",
            "Find the rule",
            "Use the rule to answer the question"
        ],
        examples: [
            {
                question: "A pattern has 5 tiles in row 1, 9 in row 2, 13 in row 3. How many in row 10?",
                steps: [
                    "Pattern: 5, 9, 13... (+4 each time)",
                    "Rule: 4n + 1",
                    "Row 10: 4(10) + 1 = <strong>41 tiles</strong>"
                ],
                answer: "41 tiles"
            }
        ],
        tip: "💡 Find the rule, then substitute any position to find its term!"
    },
    12: {
        title: "Mastery Challenge",
        band: "Advanced",
        description: "You're a pattern master! Apply all your skills.",
        keyPoints: [
            "Identify patterns quickly",
            "Write rules in words or formulas",
            "Find any term in a sequence"
        ],
        examples: [
            {
                question: "Sequence: 2, 6, 12, 20, 30... Find the 10th term.",
                steps: [
                    "Differences: +4, +6, +8, +10 (increasing by 2)",
                    "These are n(n+1): 1×2=2, 2×3=6, 3×4=12...",
                    "10th term: 10×11 = <strong>110</strong>"
                ],
                answer: "110"
            }
        ],
        tip: "🏆 Wonderful! You're a Number Patterns Champion!"
    }
};

// ============================================================
// L1LP STRAND - HELP CONTENT
// 6 Topics × 12 Levels = 72 Help Entries
// ============================================================

// 1. AWARENESS OF ENVIRONMENT HELP CONTENT (LO 2.1-2.7)
const awarenessOfEnvironmentHelpContent = {
    1: {
        title: "Exploring Objects",
        band: "Foundation",
        description: "Discover and explore different objects around you.",
        keyPoints: [
            "Look at objects carefully",
            "Notice colours, shapes, and sizes",
            "Touch and feel different objects"
        ],
        examples: [
            {
                question: "What object is this?",
                answer: "Ball",
                explanation: "Look at the round shape - it's a ball!"
            }
        ],
        tips: "Take your time to look at each picture. What do you see?"
    },
    2: {
        title: "Objects in Motion",
        band: "Foundation",
        description: "Watch how objects move and change.",
        keyPoints: [
            "Some things roll",
            "Some things slide",
            "Things can go fast or slow"
        ],
        examples: [
            {
                question: "Which object can roll?",
                answer: "Ball",
                explanation: "Balls are round - they can roll!"
            }
        ],
        tips: "Think about how things move. Round things roll!"
    },
    3: {
        title: "Showing Preferences",
        band: "Foundation",
        description: "Choose objects you like or prefer.",
        keyPoints: [
            "Everyone has favourites",
            "You can choose what you like",
            "It's okay to have preferences"
        ],
        examples: [
            {
                question: "Which would you pick?",
                answer: "Any choice is correct",
                explanation: "This is about your preference - what YOU like!"
            }
        ],
        tips: "Think about what you enjoy. There's no wrong answer!"
    },
    4: {
        title: "Same or Different",
        band: "Developing",
        description: "Compare objects to find what's the same or different.",
        keyPoints: [
            "Same means matching",
            "Different means not the same",
            "Look at colour, shape, and size"
        ],
        examples: [
            {
                question: "Are these the same?",
                answer: "Yes - they both are red apples",
                explanation: "They match in colour and type!"
            }
        ],
        tips: "Look carefully at each object. What's the same? What's different?"
    },
    5: {
        title: "Matching Objects",
        band: "Developing",
        description: "Find objects that match or go together.",
        keyPoints: [
            "Matching means finding the same",
            "Look for objects that are alike",
            "Pairs go together"
        ],
        examples: [
            {
                question: "Find the matching sock",
                answer: "The blue sock with stripes",
                explanation: "Matching socks look the same!"
            }
        ],
        tips: "Look at the first object. Now find one that looks just like it!"
    },
    6: {
        title: "Sorting by One Thing",
        band: "Developing",
        description: "Sort objects by one attribute like colour or size.",
        keyPoints: [
            "Sort means putting things in groups",
            "You can sort by colour",
            "You can sort by size"
        ],
        examples: [
            {
                question: "Which group does this red apple go in?",
                answer: "With the other red things",
                explanation: "We're sorting by colour, so red things go together!"
            }
        ],
        tips: "Think about what we're sorting by - colour? size? shape?"
    },
    7: {
        title: "Cause and Effect",
        band: "Progressing",
        description: "Understand what happens when we do something.",
        keyPoints: [
            "Actions have results",
            "Push a button, something happens",
            "If... then..."
        ],
        examples: [
            {
                question: "What happens when you press the light switch?",
                answer: "The light turns on",
                explanation: "Pressing the switch causes the light to come on!"
            }
        ],
        tips: "Think: 'If I do this... what will happen?'"
    },
    8: {
        title: "What Happens Next",
        band: "Progressing",
        description: "Predict what will happen next in a sequence.",
        keyPoints: [
            "Things often follow a pattern",
            "We can guess what comes next",
            "Watch for clues"
        ],
        examples: [
            {
                question: "The ball is rolling toward the pins. What happens next?",
                answer: "The pins fall down",
                explanation: "When the ball hits the pins, they fall!"
            }
        ],
        tips: "Look at what's happening. What do you think will happen next?"
    },
    9: {
        title: "Object Permanence",
        band: "Progressing",
        description: "Understand that objects exist even when we can't see them.",
        keyPoints: [
            "Things don't disappear when hidden",
            "We can find hidden objects",
            "Objects are still there under covers"
        ],
        examples: [
            {
                question: "A ball goes under the blanket. Is it still there?",
                answer: "Yes",
                explanation: "The ball is hidden but it didn't disappear!"
            }
        ],
        tips: "Just because you can't see something doesn't mean it's gone!"
    },
    10: {
        title: "Hidden Objects",
        band: "Consolidating",
        description: "Find and remember where hidden objects are.",
        keyPoints: [
            "Remember where things are hidden",
            "Track objects as they move",
            "Find the hidden object"
        ],
        examples: [
            {
                question: "The toy went under the cup. Where is it?",
                answer: "Under the cup",
                explanation: "Watch where objects go to find them!"
            }
        ],
        tips: "Keep your eyes on the object. Where did it go?"
    },
    11: {
        title: "Multi-Attribute Sort",
        band: "Consolidating",
        description: "Sort objects thinking about more than one thing.",
        keyPoints: [
            "Objects can be sorted different ways",
            "Think about colour AND size",
            "Same objects can go in different groups"
        ],
        examples: [
            {
                question: "Sort the big red shapes",
                answer: "Big + Red = Big red shapes group",
                explanation: "We're looking for TWO things: big AND red!"
            }
        ],
        tips: "Check BOTH things before you decide which group!"
    },
    12: {
        title: "Environment Challenge",
        band: "Consolidating",
        description: "Use all your skills to explore and understand your environment.",
        keyPoints: [
            "Use everything you've learned",
            "Look, match, sort, and predict",
            "Be a great observer"
        ],
        examples: [
            {
                question: "Look at this scene. Find the hidden ball, then sort the toys.",
                answer: "Multi-step problem solving",
                explanation: "Use your observation skills to solve problems!"
            }
        ],
        tips: "Take your time. Use all the skills you've learned!"
    }
};

// 2. PATTERN AND SEQUENCE HELP CONTENT (LO 2.8-2.12)
const patternAndSequenceHelpContent = {
    1: {
        title: "Sensory Patterns",
        band: "Foundation",
        description: "Explore patterns through looking, touching, and listening.",
        keyPoints: [
            "Patterns repeat",
            "We can see patterns",
            "We can hear patterns"
        ],
        examples: [
            {
                question: "What pattern do you see? Red, Blue, Red, Blue...",
                answer: "Red, Blue repeating",
                explanation: "The same colours keep coming back in order!"
            }
        ],
        tips: "Look for things that repeat. That's a pattern!"
    },
    2: {
        title: "Patterns Around Us",
        band: "Foundation",
        description: "Find patterns in everyday life.",
        keyPoints: [
            "Patterns are everywhere",
            "Stripes are patterns",
            "Nature has patterns"
        ],
        examples: [
            {
                question: "What pattern is on the zebra?",
                answer: "Black and white stripes",
                explanation: "Zebras have a repeating stripe pattern!"
            }
        ],
        tips: "Look around you. What patterns can you spot?"
    },
    3: {
        title: "AB Patterns",
        band: "Foundation",
        description: "Learn simple AB patterns with two things.",
        keyPoints: [
            "AB means two things take turns",
            "Red Blue Red Blue is AB",
            "Circle Square Circle Square is AB"
        ],
        examples: [
            {
                question: "🔴🔵🔴🔵🔴 What comes next?",
                answer: "Blue (🔵)",
                explanation: "The pattern is Red, Blue, Red, Blue... so Blue is next!"
            }
        ],
        tips: "Find the two things that keep repeating!"
    },
    4: {
        title: "ABB Patterns",
        band: "Developing",
        description: "Learn ABB patterns where one thing repeats.",
        keyPoints: [
            "ABB has three parts",
            "Two of them are the same",
            "Red Blue Blue is ABB"
        ],
        examples: [
            {
                question: "🔴🔵🔵🔴🔵🔵🔴 What comes next?",
                answer: "Blue, Blue (🔵🔵)",
                explanation: "The pattern is Red, Blue, Blue... so two Blues come next!"
            }
        ],
        tips: "Count how many of each you see before it starts again!"
    },
    5: {
        title: "ABC Patterns",
        band: "Developing",
        description: "Learn ABC patterns with three different things.",
        keyPoints: [
            "ABC has three different parts",
            "Each part is different",
            "Red Green Blue is ABC"
        ],
        examples: [
            {
                question: "🔴🟢🔵🔴🟢🔵🔴 What comes next?",
                answer: "Green, Blue (🟢🔵)",
                explanation: "The pattern is Red, Green, Blue... so Green then Blue!"
            }
        ],
        tips: "Find where the pattern starts over!"
    },
    6: {
        title: "What Comes Next",
        band: "Developing",
        description: "Predict the next item in any pattern.",
        keyPoints: [
            "Look at the whole pattern first",
            "Find the repeating part",
            "Work out what's next"
        ],
        examples: [
            {
                question: "🌟⭐🌟⭐🌟 What comes next?",
                answer: "Star (⭐)",
                explanation: "The stars alternate, so a plain star is next!"
            }
        ],
        tips: "Say the pattern out loud. What do you hear coming next?"
    },
    7: {
        title: "Ordering & Sequencing",
        band: "Progressing",
        description: "Put things in the right order.",
        keyPoints: [
            "Some things have an order",
            "First, then, last",
            "Things happen in sequence"
        ],
        examples: [
            {
                question: "Put in order: Put on socks, Put on shoes",
                answer: "Socks first, then shoes",
                explanation: "You need socks on before shoes!"
            }
        ],
        tips: "Think: 'What has to happen first?'"
    },
    8: {
        title: "Daily Routines",
        band: "Progressing",
        description: "Understand the order of daily activities.",
        keyPoints: [
            "Days have routines",
            "Morning, afternoon, evening",
            "Activities happen in order"
        ],
        examples: [
            {
                question: "What comes first: Eat breakfast or Get dressed?",
                answer: "Either could be first - it's your routine!",
                explanation: "Different people have different morning routines."
            }
        ],
        tips: "Think about your day. What do you do first, next, last?"
    },
    9: {
        title: "Copying Patterns",
        band: "Progressing",
        description: "Copy and continue patterns you see.",
        keyPoints: [
            "Look at the pattern carefully",
            "Copy it exactly",
            "Keep the pattern going"
        ],
        examples: [
            {
                question: "Copy this: 🔴🔴🔵🔴🔴🔵",
                answer: "🔴🔴🔵🔴🔴🔵🔴🔴🔵",
                explanation: "Keep adding Red, Red, Blue to continue the pattern!"
            }
        ],
        tips: "Match exactly what you see, then keep going!"
    },
    10: {
        title: "First, Next, Last",
        band: "Consolidating",
        description: "Use words to describe position in a sequence.",
        keyPoints: [
            "First means at the start",
            "Next means coming after",
            "Last means at the end"
        ],
        examples: [
            {
                question: "In 🍎🍌🍊, which is last?",
                answer: "Orange (🍊)",
                explanation: "Orange is at the end, so it's last!"
            }
        ],
        tips: "Point to first, then next, then last!"
    },
    11: {
        title: "Familiar Activities",
        band: "Consolidating",
        description: "Put familiar activities in the right sequence.",
        keyPoints: [
            "Making tea has steps",
            "Getting ready has steps",
            "Stories have beginnings and ends"
        ],
        examples: [
            {
                question: "Order: Pour tea, Boil water, Put in teabag",
                answer: "Boil water → Put in teabag → Pour tea",
                explanation: "You have to boil water first!"
            }
        ],
        tips: "Think about doing this activity. What order makes sense?"
    },
    12: {
        title: "Pattern Challenge",
        band: "Consolidating",
        description: "Use all your pattern skills together.",
        keyPoints: [
            "Patterns can be tricky",
            "Use what you've learned",
            "Take your time"
        ],
        examples: [
            {
                question: "Complex pattern: 🔴🔵🔵🟢🔴🔵🔵🟢🔴 What's next?",
                answer: "Blue, Blue, Green (🔵🔵🟢)",
                explanation: "The pattern is ABBCA - use your skills!"
            }
        ],
        tips: "Break it down step by step. You've got this!"
    }
};

// 3. DEVELOPING NUMBER SENSE HELP CONTENT (LO 2.13-2.17)
const developingNumberSenseHelpContent = {
    1: {
        title: "Counting to 5",
        band: "Foundation",
        description: "Count objects from 1 to 5.",
        keyPoints: [
            "Point to each object as you count",
            "Say the numbers: 1, 2, 3, 4, 5",
            "The last number tells how many"
        ],
        examples: [
            {
                question: "How many apples? 🍎🍎🍎",
                answer: "3",
                explanation: "Count: 1, 2, 3. There are 3 apples!"
            }
        ],
        tips: "Touch each object as you count. Don't skip any!"
    },
    2: {
        title: "Counting to 10",
        band: "Foundation",
        description: "Count objects from 1 to 10.",
        keyPoints: [
            "After 5 comes 6, 7, 8, 9, 10",
            "Count carefully",
            "Check by counting again"
        ],
        examples: [
            {
                question: "How many stars? ⭐⭐⭐⭐⭐⭐⭐",
                answer: "7",
                explanation: "Count: 1, 2, 3, 4, 5, 6, 7. Seven stars!"
            }
        ],
        tips: "If you lose count, start again from 1!"
    },
    3: {
        title: "Recognising Numerals",
        band: "Foundation",
        description: "Recognise written numbers 1 to 10.",
        keyPoints: [
            "Numbers have names and symbols",
            "1 is 'one', 2 is 'two'",
            "Match the numeral to its name"
        ],
        examples: [
            {
                question: "What number is this: 5",
                answer: "Five",
                explanation: "The symbol 5 means five!"
            }
        ],
        tips: "Practice saying the number names as you see them!"
    },
    4: {
        title: "Matching Numbers",
        band: "Developing",
        description: "Match numerals to quantities of objects.",
        keyPoints: [
            "The number tells how many",
            "Count the objects",
            "Find the matching number"
        ],
        examples: [
            {
                question: "Match: 🍎🍎🍎🍎 to a number",
                answer: "4",
                explanation: "Four apples matches the number 4!"
            }
        ],
        tips: "Count first, then look for that number!"
    },
    5: {
        title: "More or Less",
        band: "Developing",
        description: "Compare groups to find which has more or less.",
        keyPoints: [
            "More means a bigger amount",
            "Less means a smaller amount",
            "Count both groups to compare"
        ],
        examples: [
            {
                question: "Which has more: 🍎🍎🍎 or 🍌🍌🍌🍌🍌?",
                answer: "The bananas (5 is more than 3)",
                explanation: "Count each: 3 apples, 5 bananas. 5 is more!"
            }
        ],
        tips: "Count each group and compare the numbers!"
    },
    6: {
        title: "Same Amount",
        band: "Developing",
        description: "Find groups that have the same amount.",
        keyPoints: [
            "Same means equal",
            "Both groups have the same number",
            "Match one-to-one to check"
        ],
        examples: [
            {
                question: "Do these have the same? 🔵🔵🔵 and 🔴🔴🔴",
                answer: "Yes! Both have 3",
                explanation: "Count each: 3 blue, 3 red. Same!"
            }
        ],
        tips: "Pair them up. If nothing's left over, they're the same!"
    },
    7: {
        title: "One More",
        band: "Progressing",
        description: "Find one more than a number.",
        keyPoints: [
            "One more means add 1",
            "The next counting number",
            "4 and one more is 5"
        ],
        examples: [
            {
                question: "There are 3 balls. One more rolls in. How many now?",
                answer: "4",
                explanation: "3 and one more is 4!"
            }
        ],
        tips: "Count what you have, then say the next number!"
    },
    8: {
        title: "One Less",
        band: "Progressing",
        description: "Find one less than a number.",
        keyPoints: [
            "One less means take away 1",
            "Go back one in counting",
            "5 and one less is 4"
        ],
        examples: [
            {
                question: "There are 5 cookies. You eat one. How many left?",
                answer: "4",
                explanation: "5 take away 1 is 4!"
            }
        ],
        tips: "Count what you have, then say the number before!"
    },
    9: {
        title: "Counting to 20",
        band: "Progressing",
        description: "Extend counting to 20.",
        keyPoints: [
            "After 10: 11, 12, 13, 14, 15",
            "Then: 16, 17, 18, 19, 20",
            "Bigger numbers need careful counting"
        ],
        examples: [
            {
                question: "Count the dots to 15",
                answer: "Count carefully: 1, 2, 3... 15",
                explanation: "Take your time with bigger numbers!"
            }
        ],
        tips: "Go slowly and point to each object!"
    },
    10: {
        title: "Simple Combining",
        band: "Consolidating",
        description: "Combine small groups (addition concept).",
        keyPoints: [
            "Put groups together",
            "Count the total",
            "Combining makes more"
        ],
        examples: [
            {
                question: "2 red balls and 3 blue balls. How many altogether?",
                answer: "5",
                explanation: "2 and 3 together make 5!"
            }
        ],
        tips: "Count all of them together!"
    },
    11: {
        title: "Simple Taking Away",
        band: "Consolidating",
        description: "Take away from a group (subtraction concept).",
        keyPoints: [
            "Start with a group",
            "Take some away",
            "Count what's left"
        ],
        examples: [
            {
                question: "5 birds on a fence. 2 fly away. How many left?",
                answer: "3",
                explanation: "5 take away 2 leaves 3!"
            }
        ],
        tips: "Count what you had, cover some up, count what's left!"
    },
    12: {
        title: "Number Challenge",
        band: "Consolidating",
        description: "Use all your number skills together.",
        keyPoints: [
            "Count, compare, combine",
            "Use what you've learned",
            "Numbers are useful!"
        ],
        examples: [
            {
                question: "Multi-step: Count, then add one more",
                answer: "Use your skills step by step",
                explanation: "Break the problem into parts!"
            }
        ],
        tips: "Take it one step at a time. You know how to do this!"
    }
};

// 4. SHAPE AND SPACE HELP CONTENT (LO 2.18-2.21)
const shapeAndSpaceHelpContent = {
    1: {
        title: "Position Words",
        band: "Foundation",
        description: "Learn words that describe where things are.",
        keyPoints: [
            "In means inside",
            "On means on top",
            "Under means below"
        ],
        examples: [
            {
                question: "Where is the cat? (cat on chair)",
                answer: "On the chair",
                explanation: "The cat is sitting on top of the chair!"
            }
        ],
        tips: "Look at where things are. Use in, on, under!"
    },
    2: {
        title: "Movement Words",
        band: "Foundation",
        description: "Learn words that describe how things move.",
        keyPoints: [
            "Up means going higher",
            "Down means going lower",
            "Left and right are directions"
        ],
        examples: [
            {
                question: "The ball goes ___? (ball falling)",
                answer: "Down",
                explanation: "The ball is falling down!"
            }
        ],
        tips: "Watch how things move. Which direction are they going?"
    },
    3: {
        title: "Circle & Square",
        band: "Foundation",
        description: "Recognise circles and squares.",
        keyPoints: [
            "Circles are round with no corners",
            "Squares have 4 equal sides",
            "Squares have 4 corners"
        ],
        examples: [
            {
                question: "Which is the circle? ⚪ ◼️",
                answer: "The round one (⚪)",
                explanation: "Circles are perfectly round!"
            }
        ],
        tips: "Circle = round. Square = 4 equal sides and corners!"
    },
    4: {
        title: "Triangle & Rectangle",
        band: "Developing",
        description: "Recognise triangles and rectangles.",
        keyPoints: [
            "Triangles have 3 sides and 3 corners",
            "Rectangles have 4 sides",
            "Rectangles have 2 long and 2 short sides"
        ],
        examples: [
            {
                question: "Which shape has 3 corners?",
                answer: "Triangle",
                explanation: "Triangles always have exactly 3 corners!"
            }
        ],
        tips: "Count the corners. 3 = triangle, 4 = rectangle or square!"
    },
    5: {
        title: "Shapes Around Us",
        band: "Developing",
        description: "Find shapes in everyday objects.",
        keyPoints: [
            "Windows are often rectangles",
            "Wheels are circles",
            "Roofs can be triangles"
        ],
        examples: [
            {
                question: "What shape is a window?",
                answer: "Rectangle (usually)",
                explanation: "Most windows are rectangle shaped!"
            }
        ],
        tips: "Look around you. What shapes can you spot?"
    },
    6: {
        title: "3D Shapes Intro",
        band: "Developing",
        description: "Meet 3D shapes - shapes you can hold.",
        keyPoints: [
            "3D shapes are solid",
            "You can pick them up",
            "They're not flat like 2D shapes"
        ],
        examples: [
            {
                question: "Is a ball flat or solid?",
                answer: "Solid (3D)",
                explanation: "You can hold a ball - it's 3D!"
            }
        ],
        tips: "Can you hold it in your hand? Then it's probably 3D!"
    },
    7: {
        title: "Ball, Box, Can",
        band: "Progressing",
        description: "Recognise spheres, cubes, and cylinders.",
        keyPoints: [
            "Balls are spheres - round all over",
            "Boxes are cubes - 6 square faces",
            "Cans are cylinders - round with flat ends"
        ],
        examples: [
            {
                question: "What 3D shape is a tin of beans?",
                answer: "Cylinder (can shape)",
                explanation: "Tins are round with flat top and bottom!"
            }
        ],
        tips: "Think: Ball = sphere, Box = cube, Can = cylinder!"
    },
    8: {
        title: "Sorting Shapes",
        band: "Progressing",
        description: "Sort shapes by their properties.",
        keyPoints: [
            "Sort by number of sides",
            "Sort by number of corners",
            "Sort by curved or straight"
        ],
        examples: [
            {
                question: "Sort: shapes with curved edges",
                answer: "Circles, ovals go together",
                explanation: "These shapes have curved sides!"
            }
        ],
        tips: "What property are we sorting by? Look for that!"
    },
    9: {
        title: "Shapes in Life",
        band: "Progressing",
        description: "Connect shapes to real-life objects.",
        keyPoints: [
            "Pizza is often a circle",
            "Door is a rectangle",
            "Tent is a triangle shape"
        ],
        examples: [
            {
                question: "What shape is a slice of pizza?",
                answer: "Triangle",
                explanation: "Pizza slices are triangle shaped!"
            }
        ],
        tips: "Think of real objects. What shapes make them up?"
    },
    10: {
        title: "Sides & Corners",
        band: "Consolidating",
        description: "Count sides and corners on shapes.",
        keyPoints: [
            "Sides are the straight edges",
            "Corners are where sides meet",
            "Triangle: 3 sides, 3 corners"
        ],
        examples: [
            {
                question: "How many sides does a rectangle have?",
                answer: "4",
                explanation: "Count the straight edges - 4 sides!"
            }
        ],
        tips: "Trace around the shape counting each side!"
    },
    11: {
        title: "Describing Shapes",
        band: "Consolidating",
        description: "Use words to describe shapes.",
        keyPoints: [
            "Describe using sides and corners",
            "Describe using size",
            "Compare shapes to each other"
        ],
        examples: [
            {
                question: "Describe a square",
                answer: "4 equal sides, 4 corners",
                explanation: "Squares have equal sides and right angles!"
            }
        ],
        tips: "Think: How many sides? How many corners? What size?"
    },
    12: {
        title: "Shape Challenge",
        band: "Consolidating",
        description: "Use all your shape knowledge together.",
        keyPoints: [
            "Name shapes",
            "Find shapes in real life",
            "Describe and compare shapes"
        ],
        examples: [
            {
                question: "Complex: Find the 3D shape, describe it, and find it in real life",
                answer: "Multi-step shape reasoning",
                explanation: "Use all your shape skills!"
            }
        ],
        tips: "Take it step by step. You're a shape expert now!"
    }
};

// 5. MEASURE AND DATA HELP CONTENT (LO 2.22-2.25)
const measureAndDataHelpContent = {
    1: {
        title: "Big and Small",
        band: "Foundation",
        description: "Compare objects by size.",
        keyPoints: [
            "Big means larger",
            "Small means smaller",
            "Compare by looking"
        ],
        examples: [
            {
                question: "Which is bigger: elephant or mouse?",
                answer: "Elephant",
                explanation: "Elephants are much bigger than mice!"
            }
        ],
        tips: "Look at both objects. Which takes up more space?"
    },
    2: {
        title: "Long and Short",
        band: "Foundation",
        description: "Compare length of objects.",
        keyPoints: [
            "Long means more length",
            "Short means less length",
            "Line up to compare"
        ],
        examples: [
            {
                question: "Which pencil is longer?",
                answer: "The one that reaches further",
                explanation: "Line them up at the start to compare!"
            }
        ],
        tips: "Put things side by side to compare length!"
    },
    3: {
        title: "Heavy and Light",
        band: "Foundation",
        description: "Compare weight of objects.",
        keyPoints: [
            "Heavy means weighs more",
            "Light means weighs less",
            "Size doesn't always mean heavy"
        ],
        examples: [
            {
                question: "Which is heavier: feather or rock?",
                answer: "Rock",
                explanation: "Rocks are much heavier than feathers!"
            }
        ],
        tips: "Imagine holding each one. Which would pull down more?"
    },
    4: {
        title: "Full and Empty",
        band: "Developing",
        description: "Understand full, empty, and in between.",
        keyPoints: [
            "Full means completely filled",
            "Empty means nothing inside",
            "Half full is in between"
        ],
        examples: [
            {
                question: "Is this glass full or empty? (glass with water)",
                answer: "Full / Half full / Empty (depending on image)",
                explanation: "Look at how much is inside!"
            }
        ],
        tips: "Look at how much space is filled up!"
    },
    5: {
        title: "Ordering by Size",
        band: "Developing",
        description: "Put objects in order from smallest to biggest.",
        keyPoints: [
            "Start with smallest",
            "End with biggest",
            "Each one is a bit bigger"
        ],
        examples: [
            {
                question: "Order: big bear, small bear, medium bear",
                answer: "Small → Medium → Big",
                explanation: "Start with smallest and go up in size!"
            }
        ],
        tips: "Find the smallest first, then the next, then the biggest!"
    },
    6: {
        title: "Recognising Coins",
        band: "Developing",
        description: "Know Irish Euro coins by sight.",
        keyPoints: [
            "€2 is big with gold and silver",
            "€1 is gold coloured",
            "Cent coins are copper and smaller"
        ],
        examples: [
            {
                question: "Which coin is €1?",
                answer: "The gold coloured one",
                explanation: "€1 coins are gold and smaller than €2!"
            }
        ],
        tips: "€2 = big gold+silver. €1 = gold. Cents = copper coloured!"
    },
    7: {
        title: "Which Costs More",
        band: "Progressing",
        description: "Compare prices to find which costs more.",
        keyPoints: [
            "More euros means more expensive",
            "Less euros means cheaper",
            "Compare the numbers"
        ],
        examples: [
            {
                question: "Which costs more: €3 or €5?",
                answer: "€5",
                explanation: "5 is more than 3, so €5 costs more!"
            }
        ],
        tips: "Look at the numbers. Bigger number = more expensive!"
    },
    8: {
        title: "Simple Shopping",
        band: "Progressing",
        description: "Use coins in simple shopping scenarios.",
        keyPoints: [
            "Match coins to prices",
            "Use correct coins",
            "Simple buying decisions"
        ],
        examples: [
            {
                question: "You need €2 for a snack. Which coin?",
                answer: "The €2 coin (gold and silver)",
                explanation: "Pick the €2 coin to pay!"
            }
        ],
        tips: "Match your coins to the price. Equal or more!"
    },
    9: {
        title: "Hot and Cold",
        band: "Progressing",
        description: "Understand temperature concepts.",
        keyPoints: [
            "Hot things feel warm/burning",
            "Cold things feel cool/freezing",
            "Weather can be hot or cold"
        ],
        examples: [
            {
                question: "Is ice hot or cold?",
                answer: "Cold",
                explanation: "Ice is frozen water - very cold!"
            }
        ],
        tips: "Think: Would you need a coat (cold) or shorts (hot)?"
    },
    10: {
        title: "Reading Pictographs",
        band: "Consolidating",
        description: "Read simple picture graphs.",
        keyPoints: [
            "Each picture = one thing",
            "Count the pictures",
            "Pictures show amounts"
        ],
        examples: [
            {
                question: "Chart shows 🍎🍎🍎 for Monday. How many apples?",
                answer: "3",
                explanation: "Count the apple pictures - 3!"
            }
        ],
        tips: "Each picture represents one. Count carefully!"
    },
    11: {
        title: "Sorting Data",
        band: "Consolidating",
        description: "Sort and organise information.",
        keyPoints: [
            "Group similar things together",
            "Count each group",
            "Sorting helps us see patterns"
        ],
        examples: [
            {
                question: "Sort fruits: 🍎🍌🍎🍊🍌🍎",
                answer: "Apples: 3, Bananas: 2, Oranges: 1",
                explanation: "Group them, then count each group!"
            }
        ],
        tips: "Make groups first, then count each group!"
    },
    12: {
        title: "Measure Challenge",
        band: "Consolidating",
        description: "Use all your measuring skills together.",
        keyPoints: [
            "Compare sizes and weights",
            "Use coins",
            "Read simple data"
        ],
        examples: [
            {
                question: "Multi-step measuring problem",
                answer: "Use your skills step by step",
                explanation: "Combine comparing, coins, and data!"
            }
        ],
        tips: "Break it into parts. You've learned all of this!"
    }
};

// 6. TIME HELP CONTENT (LO 2.26-2.29)
const l1lpTimeHelpContent = {
    1: {
        title: "Morning & Night",
        band: "Foundation",
        description: "Know the difference between morning and night.",
        keyPoints: [
            "Morning = sun is coming up",
            "Night = dark, stars and moon",
            "We wake up in morning, sleep at night"
        ],
        examples: [
            {
                question: "When do you wake up?",
                answer: "Morning",
                explanation: "We wake up when the sun comes up - morning!"
            }
        ],
        tips: "Sun up = morning. Dark/stars = night!"
    },
    2: {
        title: "Times of Day",
        band: "Foundation",
        description: "Learn morning, afternoon, evening, night.",
        keyPoints: [
            "Morning = before lunch",
            "Afternoon = after lunch",
            "Evening = getting dark",
            "Night = dark, time for sleep"
        ],
        examples: [
            {
                question: "When do we eat dinner?",
                answer: "Evening",
                explanation: "Dinner is usually in the evening!"
            }
        ],
        tips: "Think about meals: Breakfast (morning), Lunch (afternoon), Dinner (evening)!"
    },
    3: {
        title: "Days of the Week",
        band: "Foundation",
        description: "Learn the names of the seven days.",
        keyPoints: [
            "7 days in a week",
            "Monday, Tuesday, Wednesday...",
            "...Thursday, Friday, Saturday, Sunday"
        ],
        examples: [
            {
                question: "What day comes after Monday?",
                answer: "Tuesday",
                explanation: "The days go in order: Monday, Tuesday, Wednesday..."
            }
        ],
        tips: "Learn the days song: Monday, Tuesday, Wednesday..."
    },
    4: {
        title: "Daily Routines",
        band: "Developing",
        description: "Know when daily activities happen.",
        keyPoints: [
            "Breakfast time is morning",
            "School time is during the day",
            "Bedtime is at night"
        ],
        examples: [
            {
                question: "When is breakfast time?",
                answer: "Morning",
                explanation: "We eat breakfast after waking up in the morning!"
            }
        ],
        tips: "Think about YOUR day. When do you do these things?"
    },
    5: {
        title: "Seasons",
        band: "Developing",
        description: "Learn the four seasons of the year.",
        keyPoints: [
            "Spring = flowers, warmer",
            "Summer = hot, sunny",
            "Autumn = leaves fall, cooler",
            "Winter = cold, maybe snow"
        ],
        examples: [
            {
                question: "Which season is coldest?",
                answer: "Winter",
                explanation: "Winter is the coldest season!"
            }
        ],
        tips: "Think about the weather. What do you wear in each season?"
    },
    6: {
        title: "Special Events",
        band: "Developing",
        description: "Know important dates and celebrations.",
        keyPoints: [
            "Birthdays are special days",
            "Christmas is in winter",
            "Halloween is in autumn"
        ],
        examples: [
            {
                question: "When is Halloween?",
                answer: "October (autumn)",
                explanation: "Halloween happens when leaves are falling!"
            }
        ],
        tips: "Think about when you celebrate special days!"
    },
    7: {
        title: "O'Clock Times",
        band: "Progressing",
        description: "Read o'clock times on a clock.",
        keyPoints: [
            "Short hand points to the hour",
            "Long hand points to 12 for o'clock",
            "3 o'clock = short hand on 3, long hand on 12"
        ],
        examples: [
            {
                question: "What time is it? (clock showing 5 o'clock)",
                answer: "5 o'clock",
                explanation: "Short hand on 5, long hand on 12 = 5 o'clock!"
            }
        ],
        tips: "Look at the SHORT hand first. That's the hour!"
    },
    8: {
        title: "Before and After",
        band: "Progressing",
        description: "Understand before and after in time.",
        keyPoints: [
            "Before = happened first",
            "After = happened second",
            "Sequence of events"
        ],
        examples: [
            {
                question: "What comes before lunch?",
                answer: "Morning / Breakfast",
                explanation: "We have morning and breakfast before lunch!"
            }
        ],
        tips: "Before = earlier. After = later!"
    },
    9: {
        title: "Using Timers",
        band: "Progressing",
        description: "Use timers and countdowns.",
        keyPoints: [
            "Timers count time",
            "Sand timers show time passing",
            "Countdown means less and less time"
        ],
        examples: [
            {
                question: "The timer has 5 minutes. Is time running out?",
                answer: "Check if the numbers are going down",
                explanation: "When numbers go down, time is running out!"
            }
        ],
        tips: "Watch the timer. When it reaches zero, time is up!"
    },
    10: {
        title: "Waiting & Turns",
        band: "Consolidating",
        description: "Understand waiting and taking turns.",
        keyPoints: [
            "Sometimes we have to wait",
            "Taking turns means one at a time",
            "First, then next person"
        ],
        examples: [
            {
                question: "There are 2 people before you. When is your turn?",
                answer: "After 2 people go",
                explanation: "Wait for them, then it's your turn!"
            }
        ],
        tips: "Count who's before you. Then you'll know when it's your turn!"
    },
    11: {
        title: "Visual Timetables",
        band: "Consolidating",
        description: "Read and follow visual timetables.",
        keyPoints: [
            "Pictures show activities",
            "Order shows when things happen",
            "Follow left to right or top to bottom"
        ],
        examples: [
            {
                question: "Timetable shows: breakfast → school → lunch. What's after school?",
                answer: "Lunch",
                explanation: "Follow the timetable - lunch comes after school!"
            }
        ],
        tips: "Follow the pictures in order. What comes next?"
    },
    12: {
        title: "Time Challenge",
        band: "Consolidating",
        description: "Use all your time skills together.",
        keyPoints: [
            "Know times of day",
            "Read simple clocks",
            "Follow schedules and sequences"
        ],
        examples: [
            {
                question: "Multi-step time problem",
                answer: "Use your skills step by step",
                explanation: "Combine what you know about time!"
            }
        ],
        tips: "Take it one step at a time. You understand time now!"
    }
};

// ============================================================
// L2LP STRAND - HELP CONTENT (NCCA-Aligned)
// 4 Topics × 12 Levels = 48 Help Entries
// ============================================================

// 1. NUMBER & MONEY HELP CONTENT
const l2NumberAndMoneyHelpContent = {
    1: {
        title: "Numbers in Real Life",
        band: "Foundation",
        description: "Recognise where numbers appear in everyday life.",
        keyPoints: [
            "Numbers are everywhere around us",
            "We see numbers on phones, buses, prices, clocks",
            "Numbers tell us 'how many' or 'how much'"
        ],
        examples: [
            {
                question: "Where might you see numbers at a bus stop?",
                answer: "Bus number, timetable times, route numbers",
                explanation: "Numbers help us catch the right bus!"
            }
        ],
        tips: "Look around you - how many numbers can you spot right now?"
    },
    2: {
        title: "Counting Skills",
        band: "Foundation",
        description: "Count accurately using different methods.",
        keyPoints: [
            "Touch each object as you count",
            "Say each number clearly",
            "Keep track of what you've counted"
        ],
        examples: [
            {
                question: "Count these apples: 🍎🍎🍎🍎🍎",
                answer: "5 apples",
                explanation: "Touch and count: 1, 2, 3, 4, 5!"
            }
        ],
        tips: "Point to each item as you count to avoid counting twice."
    },
    3: {
        title: "Tens and Ones",
        band: "Foundation",
        description: "Understand how two-digit numbers are made of tens and ones.",
        keyPoints: [
            "14 = 1 ten and 4 ones",
            "25 = 2 tens and 5 ones",
            "The first digit tells us how many tens"
        ],
        examples: [
            {
                question: "How many tens and ones in 36?",
                answer: "3 tens and 6 ones",
                explanation: "The 3 is in the tens place, the 6 is in the ones place."
            }
        ],
        tips: "Think of bundles of 10 sticks, plus loose sticks."
    },
    4: {
        title: "Place Value",
        band: "Developing",
        description: "Understand place value for larger numbers.",
        keyPoints: [
            "Tens have 1 zero (10, 20, 30...)",
            "Hundreds have 2 zeros (100, 200, 300...)",
            "Thousands have 3 zeros (1000, 2000, 3000...)"
        ],
        examples: [
            {
                question: "How many zeros in one hundred?",
                answer: "2 zeros (100)",
                explanation: "Hundred = 100 = two zeros after the 1."
            }
        ],
        tips: "Count the zeros: tens=1, hundreds=2, thousands=3."
    },
    5: {
        title: "Estimating Amounts",
        band: "Developing",
        description: "Make sensible guesses about quantities.",
        keyPoints: [
            "Estimate means 'good guess'",
            "Round to nearest 10 or 100",
            "Is it closer to 10 or 20? 50 or 100?"
        ],
        examples: [
            {
                question: "About how many sweets in a jar of 47?",
                answer: "About 50",
                explanation: "47 is close to 50, so we estimate 50."
            }
        ],
        tips: "Think: is it closer to the lower or higher round number?"
    },
    6: {
        title: "Adding & Subtracting",
        band: "Developing",
        description: "Know when to add or subtract and use the symbols.",
        keyPoints: [
            "+ means add or plus (getting more)",
            "- means subtract or minus (taking away)",
            "= means equals (the answer)"
        ],
        examples: [
            {
                question: "You have 8 sweets, you eat 3. Add or subtract?",
                answer: "Subtract: 8 - 3 = 5",
                explanation: "Eating means taking away, so we subtract."
            }
        ],
        tips: "Getting more = add. Taking away = subtract."
    },
    7: {
        title: "Recognising Money",
        band: "Progressing",
        description: "Identify coins and notes and sort them into groups.",
        keyPoints: [
            "Coins: 1c, 2c, 5c, 10c, 20c, 50c, €1, €2",
            "Notes: €5, €10, €20, €50, €100",
            "Sort coins and notes by value"
        ],
        examples: [
            {
                question: "Which is worth more: €2 coin or €5 note?",
                answer: "€5 note",
                explanation: "5 is bigger than 2, so €5 is worth more."
            }
        ],
        tips: "Look at the number on the coin or note to know its value."
    },
    8: {
        title: "Shopping & Transactions",
        band: "Progressing",
        description: "Use money to buy things and understand transactions.",
        keyPoints: [
            "Check the price tag before buying",
            "Give enough money to pay",
            "Wait for your change if you gave too much"
        ],
        examples: [
            {
                question: "Item costs €3. You give €5. What happens?",
                answer: "You get €2 change",
                explanation: "€5 - €3 = €2 change back."
            }
        ],
        tips: "Always count your change to make sure it's correct!"
    },
    9: {
        title: "Totals & Change",
        band: "Progressing",
        description: "Calculate the total cost and check change.",
        keyPoints: [
            "Add all prices to find total",
            "Check your receipt matches what you bought",
            "Count change carefully"
        ],
        examples: [
            {
                question: "Bread €2 + Milk €1 + Apple €1 = ?",
                answer: "€4 total",
                explanation: "Add them up: 2 + 1 + 1 = 4."
            }
        ],
        tips: "Use your fingers or write it down to add up prices."
    },
    10: {
        title: "Estimating & Rounding",
        band: "Consolidating",
        description: "Round prices and estimate bills.",
        keyPoints: [
            "€4.99 rounds to €5",
            "€23 rounds to €20 or €25",
            "Estimate before paying to check you have enough"
        ],
        examples: [
            {
                question: "Items cost €4.99, €2.99, €1.99. Estimate total?",
                answer: "About €10",
                explanation: "€5 + €3 + €2 = €10 (rounded up)."
            }
        ],
        tips: "Round each price to the nearest euro, then add."
    },
    11: {
        title: "Bills & Receipts",
        band: "Consolidating",
        description: "Read and understand bills and receipts.",
        keyPoints: [
            "Receipts show what you bought and the price",
            "Check the total matches your calculation",
            "Keep receipts as proof of purchase"
        ],
        examples: [
            {
                question: "Your receipt shows €15 but you calculated €12. What do you do?",
                answer: "Check again and ask staff if there's a mistake",
                explanation: "Always check receipts - mistakes can happen!"
            }
        ],
        tips: "Read each line of the receipt and check prices."
    },
    12: {
        title: "Digital Payments",
        band: "Consolidating",
        description: "Understand different ways to pay including apps.",
        keyPoints: [
            "Cash, card, and phone payments",
            "Contactless means tap to pay",
            "Apps can transfer money to others"
        ],
        examples: [
            {
                question: "What does 'contactless' mean?",
                answer: "Tap your card or phone to pay without entering a PIN",
                explanation: "Quick payment for small amounts."
            }
        ],
        tips: "Keep your card and phone safe - they can be used to pay!"
    }
};

// 2. TIME & TIMETABLES HELP CONTENT
const l2TimeManagementHelpContent = {
    1: {
        title: "Time Instruments",
        band: "Foundation",
        description: "Recognise different instruments for telling time.",
        keyPoints: [
            "Clocks tell us the time",
            "Watches are clocks you wear",
            "Phones and computers show time too"
        ],
        examples: [
            {
                question: "Name 3 things that show the time.",
                answer: "Clock, watch, phone, computer, microwave",
                explanation: "Many devices show us what time it is!"
            }
        ],
        tips: "Look around - can you spot something showing the time?"
    },
    2: {
        title: "Analogue Clocks",
        band: "Foundation",
        description: "Read time on a clock with hands.",
        keyPoints: [
            "Short hand = hour",
            "Long hand = minutes",
            "The numbers go 1-12 around the clock"
        ],
        examples: [
            {
                question: "Short hand on 3, long hand on 12. What time?",
                answer: "3 o'clock",
                explanation: "Long hand on 12 means 'o'clock'. Short hand shows the hour."
            }
        ],
        tips: "Always look at the short hand first for the hour."
    },
    3: {
        title: "Digital Clocks",
        band: "Foundation",
        description: "Read time on digital displays.",
        keyPoints: [
            "Shows hours : minutes (like 3:00)",
            "Left number = hours",
            "Right number = minutes"
        ],
        examples: [
            {
                question: "The clock shows 9:30. What time is it?",
                answer: "Half past 9 (or 9:30)",
                explanation: "9 hours and 30 minutes."
            }
        ],
        tips: "Digital clocks are easier - just read the numbers!"
    },
    4: {
        title: "12 and 24 Hour Time",
        band: "Developing",
        description: "Understand both time formats.",
        keyPoints: [
            "12-hour: uses a.m. and p.m.",
            "24-hour: goes from 00:00 to 23:59",
            "3 p.m. = 15:00 in 24-hour time"
        ],
        examples: [
            {
                question: "What is 2 p.m. in 24-hour time?",
                answer: "14:00",
                explanation: "Add 12 to afternoon times: 2 + 12 = 14."
            }
        ],
        tips: "For p.m. times, add 12 to get 24-hour time."
    },
    5: {
        title: "Time Language",
        band: "Developing",
        description: "Use words related to time correctly.",
        keyPoints: [
            "Half past = 30 minutes",
            "Quarter past = 15 minutes",
            "Quarter to = 45 minutes (15 to go)"
        ],
        examples: [
            {
                question: "What is 'quarter past 4'?",
                answer: "4:15",
                explanation: "Quarter = 15 minutes past the hour."
            }
        ],
        tips: "Quarter = 15 minutes. Half = 30 minutes."
    },
    6: {
        title: "Units of Time",
        band: "Developing",
        description: "Know how time units relate to each other.",
        keyPoints: [
            "60 seconds = 1 minute",
            "60 minutes = 1 hour",
            "24 hours = 1 day",
            "7 days = 1 week"
        ],
        examples: [
            {
                question: "How many minutes in 2 hours?",
                answer: "120 minutes",
                explanation: "60 + 60 = 120 minutes."
            }
        ],
        tips: "Remember: 60 seconds in a minute, 60 minutes in an hour."
    },
    7: {
        title: "Timelines & Timetables",
        band: "Progressing",
        description: "Read and use timelines and timetables.",
        keyPoints: [
            "Timelines show events in order",
            "Timetables show when things happen",
            "Read across and down to find information"
        ],
        examples: [
            {
                question: "The timetable shows Maths at 9:00. When does it start?",
                answer: "9 o'clock in the morning",
                explanation: "Find the subject and read the time."
            }
        ],
        tips: "Use your finger to follow rows and columns in timetables."
    },
    8: {
        title: "Calculating Time",
        band: "Progressing",
        description: "Work out how long things take.",
        keyPoints: [
            "Count forward to find end time",
            "Count backward to find start time",
            "Subtract to find duration"
        ],
        examples: [
            {
                question: "Film starts at 2:00, ends at 4:00. How long?",
                answer: "2 hours",
                explanation: "From 2 to 4 is 2 hours."
            }
        ],
        tips: "Count on your fingers from start time to end time."
    },
    9: {
        title: "Time Management Skills",
        band: "Progressing",
        description: "Learn to manage your time well.",
        keyPoints: [
            "Plan ahead - know when things start",
            "Allow time to get ready",
            "Don't leave things to the last minute"
        ],
        examples: [
            {
                question: "School starts at 9:00. It takes 20 minutes to get there. When should you leave?",
                answer: "Before 8:40",
                explanation: "Count back 20 minutes from 9:00."
            }
        ],
        tips: "Always give yourself extra time in case of delays!"
    },
    10: {
        title: "Daily Routines",
        band: "Consolidating",
        description: "Understand and plan daily activities.",
        keyPoints: [
            "Routines help us organise our day",
            "Some things happen at the same time each day",
            "Estimate how long activities take"
        ],
        examples: [
            {
                question: "List 3 things you do every morning.",
                answer: "Wake up, eat breakfast, get dressed (examples)",
                explanation: "These are part of your morning routine."
            }
        ],
        tips: "A good routine helps you be on time and less stressed."
    },
    11: {
        title: "Calendars & Planning",
        band: "Consolidating",
        description: "Use calendars for forward planning.",
        keyPoints: [
            "Calendars show days, weeks, and months",
            "Mark important dates and events",
            "Count days until an event"
        ],
        examples: [
            {
                question: "Today is the 10th. The trip is on the 15th. How many days to wait?",
                answer: "5 days",
                explanation: "Count from 10 to 15: 11, 12, 13, 14, 15 = 5 days."
            }
        ],
        tips: "Write important events on a calendar so you don't forget!"
    },
    12: {
        title: "Journey Planning",
        band: "Consolidating",
        description: "Plan journeys using transport timetables.",
        keyPoints: [
            "Check departure and arrival times",
            "Allow time to get to the stop/station",
            "Plan the whole journey including connections"
        ],
        examples: [
            {
                question: "Bus leaves at 10:15, arrives at 10:45. How long is the journey?",
                answer: "30 minutes",
                explanation: "From :15 to :45 is 30 minutes."
            }
        ],
        tips: "Check timetables the day before and have a backup plan."
    }
};

// 3. MEASUREMENT & LOCATION HELP CONTENT
const l2MeasurementLocationHelpContent = {
    1: {
        title: "Comparing Objects",
        band: "Foundation",
        description: "Compare objects by their physical properties.",
        keyPoints: [
            "Compare by length, height, weight",
            "Use words like longer, shorter, heavier, lighter",
            "Hold or lift objects to compare"
        ],
        examples: [
            {
                question: "Which is longer: a pencil or a ruler?",
                answer: "Usually the ruler",
                explanation: "Compare by placing them side by side."
            }
        ],
        tips: "Line things up at one end to compare length fairly."
    },
    2: {
        title: "Measurement Language",
        band: "Foundation",
        description: "Use correct words for measurement.",
        keyPoints: [
            "Length = how long something is",
            "Weight = how heavy something is",
            "Capacity = how much a container holds"
        ],
        examples: [
            {
                question: "What do we measure in litres?",
                answer: "Capacity (liquids)",
                explanation: "Litres measure how much liquid fits in a container."
            }
        ],
        tips: "Length (cm, m), Weight (g, kg), Capacity (ml, L)."
    },
    3: {
        title: "Metric Units",
        band: "Foundation",
        description: "Know the main metric units.",
        keyPoints: [
            "Centimetres (cm) and metres (m) for length",
            "Grams (g) and kilograms (kg) for weight",
            "Millilitres (ml) and litres (L) for capacity"
        ],
        examples: [
            {
                question: "How many centimetres in 1 metre?",
                answer: "100 cm",
                explanation: "1 metre = 100 centimetres."
            }
        ],
        tips: "Small things in cm/g/ml, big things in m/kg/L."
    },
    4: {
        title: "Measuring Length",
        band: "Developing",
        description: "Measure length accurately using rulers and tape measures.",
        keyPoints: [
            "Start at zero on the ruler",
            "Read the number at the end of the object",
            "Use correct units (cm or m)"
        ],
        examples: [
            {
                question: "A book is 25 cm long. How do you know?",
                answer: "Measure with a ruler from one end to the other",
                explanation: "Place ruler at edge, read where it ends."
            }
        ],
        tips: "Always start measuring from 0, not the edge of the ruler."
    },
    5: {
        title: "Comparing Measurements",
        band: "Developing",
        description: "Compare and order objects by measurement.",
        keyPoints: [
            "Measure each object first",
            "Compare the numbers",
            "Order from smallest to largest or vice versa"
        ],
        examples: [
            {
                question: "Order by length: 15cm, 8cm, 23cm",
                answer: "8cm, 15cm, 23cm (shortest to longest)",
                explanation: "Put the smallest number first."
            }
        ],
        tips: "Write down each measurement, then put in order."
    },
    6: {
        title: "Using Measuring Tools",
        band: "Developing",
        description: "Select and use appropriate measuring tools.",
        keyPoints: [
            "Ruler for short lengths",
            "Tape measure for longer lengths",
            "Scales for weight, jugs for capacity"
        ],
        examples: [
            {
                question: "What would you use to measure the length of a room?",
                answer: "Tape measure or metre stick",
                explanation: "A ruler is too short for a room."
            }
        ],
        tips: "Choose the right tool for the job!"
    },
    7: {
        title: "Body in Space",
        band: "Progressing",
        description: "Be aware of your body position and movement.",
        keyPoints: [
            "Know where your body is in space",
            "Move in different directions",
            "Be aware of obstacles around you"
        ],
        examples: [
            {
                question: "Show me how to move forward 3 steps.",
                answer: "Walk 3 steps straight ahead",
                explanation: "Forward means the direction you're facing."
            }
        ],
        tips: "Be aware of what's around you as you move."
    },
    8: {
        title: "Position Words",
        band: "Progressing",
        description: "Use words to describe where things are.",
        keyPoints: [
            "On top of, underneath, inside, outside",
            "Left and right",
            "In front of, behind, beside"
        ],
        examples: [
            {
                question: "The cat is under the table. Where is it?",
                answer: "Underneath/below the table",
                explanation: "Under means below something."
            }
        ],
        tips: "Practice: put an object somewhere and describe its position."
    },
    9: {
        title: "Simple Maps",
        band: "Progressing",
        description: "Draw and use simple maps.",
        keyPoints: [
            "Maps show places from above",
            "Use simple shapes for buildings",
            "Mark important places"
        ],
        examples: [
            {
                question: "Draw a simple map from class to the office.",
                answer: "Show corridor, turns, and the office location",
                explanation: "Include key landmarks to help find the way."
            }
        ],
        tips: "Start with a simple map of somewhere you know well."
    },
    10: {
        title: "Distance on Maps",
        band: "Consolidating",
        description: "Calculate and understand distances on maps.",
        keyPoints: [
            "Maps have a scale (e.g., 1cm = 100m)",
            "Measure with a ruler on the map",
            "Multiply to find real distance"
        ],
        examples: [
            {
                question: "On the map, 2cm = 1km. Two places are 4cm apart. Real distance?",
                answer: "2 km",
                explanation: "4cm ÷ 2 = 2km."
            }
        ],
        tips: "Check the map scale before calculating distances."
    },
    11: {
        title: "Grid References",
        band: "Consolidating",
        description: "Find and give locations on a grid.",
        keyPoints: [
            "Grids have letters across and numbers up",
            "Give letter first, then number (e.g., B3)",
            "Find where the row and column meet"
        ],
        examples: [
            {
                question: "Find square C4 on the grid.",
                answer: "Column C, Row 4",
                explanation: "Go across to C, then up to 4."
            }
        ],
        tips: "Remember: along the corridor first, then up the stairs."
    },
    12: {
        title: "Planning Journeys",
        band: "Consolidating",
        description: "Plan a journey for a day trip or event.",
        keyPoints: [
            "Know where you're starting and finishing",
            "Plan the route and transport",
            "Consider time, distance, and what you need"
        ],
        examples: [
            {
                question: "Plan a trip to town. What do you need to know?",
                answer: "Bus times, route, how long it takes, what to bring",
                explanation: "Good planning makes trips easier!"
            }
        ],
        tips: "Write a checklist: where, when, how, what to bring."
    }
};

// 4. SHAPE, PATTERN & NUMBER HELP CONTENT
const l2ShapePatternNumberHelpContent = {
    1: {
        title: "2D Shapes",
        band: "Foundation",
        description: "Name and describe properties of common 2D shapes.",
        keyPoints: [
            "Circle: round with no corners",
            "Square: 4 equal sides and 4 corners",
            "Rectangle: 4 sides, opposite sides equal",
            "Triangle: 3 sides and 3 corners"
        ],
        examples: [
            {
                question: "How many sides does a triangle have?",
                answer: "3 sides",
                explanation: "Tri- means three, so a triangle has 3 sides."
            }
        ],
        tips: "Count the sides by touching each edge of the shape."
    },
    2: {
        title: "3D Shapes",
        band: "Foundation",
        description: "Name and describe common 3D shapes you can hold.",
        keyPoints: [
            "Cube: 6 square faces (like a dice)",
            "Sphere: completely round (like a ball)",
            "Cylinder: 2 circular ends (like a can)",
            "Cone: pointed end and circular base"
        ],
        examples: [
            {
                question: "What shape is a football?",
                answer: "Sphere",
                explanation: "A football is round in all directions."
            }
        ],
        tips: "2D = flat (draw on paper), 3D = solid (can hold it)."
    },
    3: {
        title: "Simple Patterns",
        band: "Foundation",
        description: "Recognise and describe repeating patterns.",
        keyPoints: [
            "Patterns repeat in a regular way",
            "Look for what comes next",
            "Colours, shapes, or numbers can make patterns"
        ],
        examples: [
            {
                question: "Red, blue, red, blue, red, ___?",
                answer: "Blue",
                explanation: "The pattern alternates red, blue, red, blue..."
            }
        ],
        tips: "Say the pattern out loud to hear what comes next."
    },
    4: {
        title: "Number Patterns",
        band: "Developing",
        description: "Recognise and continue simple number patterns.",
        keyPoints: [
            "Count by 2s: 2, 4, 6, 8, 10...",
            "Count by 5s: 5, 10, 15, 20, 25...",
            "Count by 10s: 10, 20, 30, 40, 50..."
        ],
        examples: [
            {
                question: "What comes next: 5, 10, 15, 20, ___?",
                answer: "25",
                explanation: "The pattern adds 5 each time."
            }
        ],
        tips: "Find the rule: how much is added each time?"
    },
    5: {
        title: "Symmetry",
        band: "Developing",
        description: "Identify shapes and lines with symmetry.",
        keyPoints: [
            "Symmetrical = both halves match exactly",
            "Line of symmetry divides shape into matching parts",
            "Fold test: both sides line up perfectly"
        ],
        examples: [
            {
                question: "Is a square symmetrical?",
                answer: "Yes, it has 4 lines of symmetry",
                explanation: "You can fold a square 4 ways and both halves match."
            }
        ],
        tips: "Imagine folding the shape - would both sides match?"
    },
    6: {
        title: "More 2D Shapes",
        band: "Developing",
        description: "Name and identify pentagon, hexagon, oval, and diamond.",
        keyPoints: [
            "Pentagon: 5 sides (penta = 5)",
            "Hexagon: 6 sides (hexa = 6)",
            "Oval: egg-shaped, no corners",
            "Diamond: 4 sides like a tilted square"
        ],
        examples: [
            {
                question: "How many sides does a hexagon have?",
                answer: "6 sides",
                explanation: "Hexa means six in Greek."
            }
        ],
        tips: "Penta = 5, Hexa = 6 - learn these number prefixes!"
    },
    7: {
        title: "Odd & Even Numbers",
        band: "Progressing",
        description: "Identify and describe odd and even numbers.",
        keyPoints: [
            "Even numbers: 0, 2, 4, 6, 8 (end in these)",
            "Odd numbers: 1, 3, 5, 7, 9 (end in these)",
            "Even numbers can be split into 2 equal groups"
        ],
        examples: [
            {
                question: "Is 17 odd or even?",
                answer: "Odd",
                explanation: "17 ends in 7, so it's odd."
            }
        ],
        tips: "Look at the last digit to tell if a number is odd or even."
    },
    8: {
        title: "Fractions",
        band: "Progressing",
        description: "Understand simple fractions: half, quarter, third.",
        keyPoints: [
            "Half = 1/2 = 2 equal parts",
            "Quarter = 1/4 = 4 equal parts",
            "Third = 1/3 = 3 equal parts"
        ],
        examples: [
            {
                question: "A pizza is cut into 4 equal slices. What is each slice?",
                answer: "A quarter (1/4)",
                explanation: "4 equal parts means each is a quarter."
            }
        ],
        tips: "Equal parts are key - all pieces must be the same size!"
    },
    9: {
        title: "Multiplication Concepts",
        band: "Progressing",
        description: "Understand multiplication as repeated addition.",
        keyPoints: [
            "3 × 4 = 4 + 4 + 4 = 12",
            "× means 'groups of'",
            "Arrays show multiplication visually"
        ],
        examples: [
            {
                question: "What is 3 × 5?",
                answer: "15",
                explanation: "3 groups of 5 = 5 + 5 + 5 = 15"
            }
        ],
        tips: "Draw groups or arrays to see the multiplication."
    },
    10: {
        title: "Division Concepts",
        band: "Consolidating",
        description: "Understand division as equal sharing.",
        keyPoints: [
            "Division = sharing equally",
            "12 ÷ 3 = 4 (12 shared into 3 groups)",
            "Everyone gets the same amount"
        ],
        examples: [
            {
                question: "Share 10 sweets between 2 people. How many each?",
                answer: "5 sweets each",
                explanation: "10 ÷ 2 = 5"
            }
        ],
        tips: "Think of dealing out cards - each pile gets the same."
    },
    11: {
        title: "Number Properties",
        band: "Consolidating",
        description: "Describe properties like factors and multiples.",
        keyPoints: [
            "Multiples: 3, 6, 9, 12... (times table answers)",
            "Factors: numbers that divide exactly",
            "Factors of 12: 1, 2, 3, 4, 6, 12"
        ],
        examples: [
            {
                question: "Is 15 a multiple of 5?",
                answer: "Yes",
                explanation: "15 is in the 5 times table (5 × 3 = 15)"
            }
        ],
        tips: "Use times tables to find multiples quickly."
    },
    12: {
        title: "Problem Solving",
        band: "Consolidating",
        description: "Apply shape, pattern, and number knowledge to real problems.",
        keyPoints: [
            "Read the problem carefully",
            "Decide what maths to use",
            "Check your answer makes sense"
        ],
        examples: [
            {
                question: "3 triangles have how many sides in total?",
                answer: "9 sides",
                explanation: "Each triangle has 3 sides. 3 × 3 = 9"
            }
        ],
        tips: "Draw pictures and break problems into smaller steps."
    }
};

// ========== LC HIGHER LEVEL STRAND HELP CONTENT ==========

const lcHlCalculusDiffHelpContent = {
    1: {
        title: "Power Rule",
        band: "Foundation",
        description: "The fundamental rule for differentiating powers of x. If f(x) = xⁿ, then f'(x) = nxⁿ⁻¹.",
        keyPoints: [
            "Bring the <strong>power down</strong> as a coefficient",
            "<strong>Reduce the power</strong> by 1",
            "Constants differentiate to <strong>zero</strong>"
        ],
        examples: [{
            question: "Differentiate f(x) = 3x⁴",
            steps: ["Bring down power: 4 × 3 = 12", "Reduce power: 4 - 1 = 3", "f'(x) = 12x³"],
            answer: "f'(x) = 12x³"
        }],
        tip: "💡 Remember: d/dx(xⁿ) = nxⁿ⁻¹"
    },
    2: { title: "Chain Rule", band: "Foundation", description: "Differentiate composite functions using the chain rule.", keyPoints: ["Identify the outer and inner functions", "Differentiate outer, keep inner unchanged", "Multiply by derivative of inner"], examples: [{question: "Differentiate (2x + 1)³", answer: "6(2x + 1)²"}], tip: "💡 Chain rule: d/dx[f(g(x))] = f'(g(x)) × g'(x)" },
    3: { title: "Product Rule", band: "Foundation", description: "Differentiate products of two functions.", keyPoints: ["If y = uv, then dy/dx = u(dv/dx) + v(du/dx)", "Differentiate each part separately", "Add the two products"], examples: [{question: "Differentiate x²·sin(x)", answer: "2x·sin(x) + x²·cos(x)"}], tip: "💡 Product rule: (uv)' = u'v + uv'" },
    4: { title: "Quotient Rule", band: "Developing", description: "Differentiate quotients of two functions.", keyPoints: ["If y = u/v, then dy/dx = (v·du/dx - u·dv/dx)/v²", "Bottom stays squared", "Top: bottom times derivative of top minus top times derivative of bottom"], examples: [{question: "Differentiate (x² + 1)/(x - 1)", answer: "(x² - 2x - 1)/(x - 1)²"}], tip: "💡 Remember: 'Low d-high minus high d-low, over low squared'" },
    5: { title: "Trig Differentiation", band: "Developing", description: "Differentiate trigonometric functions.", keyPoints: ["d/dx(sin x) = cos x", "d/dx(cos x) = -sin x", "d/dx(tan x) = sec²x"], examples: [{question: "Differentiate sin(3x)", answer: "3cos(3x)"}], tip: "💡 Use chain rule with trig functions" },
    6: { title: "Exponential & Log", band: "Developing", description: "Differentiate exponential and logarithmic functions.", keyPoints: ["d/dx(eˣ) = eˣ", "d/dx(eᵏˣ) = keᵏˣ", "d/dx(ln x) = 1/x"], examples: [{question: "Differentiate e²ˣ", answer: "2e²ˣ"}], tip: "💡 eˣ is special - it's its own derivative!" },
    7: { title: "Tangents & Normals", band: "Proficient", description: "Find equations of tangent and normal lines to curves.", keyPoints: ["Tangent slope = f'(a) at point (a, f(a))", "Normal slope = -1/f'(a)", "Use y - y₁ = m(x - x₁)"], examples: [{question: "Find tangent to y = x² at x = 2", answer: "y = 4x - 4"}], tip: "💡 Normal is perpendicular to tangent" },
    8: { title: "Related Rates", band: "Proficient", description: "Problems where rates of change are connected.", keyPoints: ["Use chain rule: dA/dt = (dA/dr)(dr/dt)", "Identify what's changing with time", "Set up equation linking quantities"], examples: [{question: "If radius increases at 2cm/s, find rate of area increase when r = 5", answer: "20π cm²/s"}], tip: "💡 Everything changing? Use chain rule with dt" },
    9: { title: "Max/Min Problems", band: "Proficient", description: "Find maximum and minimum values of functions.", keyPoints: ["Set f'(x) = 0 to find turning points", "Use second derivative test: f''(x) > 0 is minimum", "Check endpoints for global max/min"], examples: [{question: "Find minimum of f(x) = x² - 4x + 5", answer: "Minimum value is 1 at x = 2"}], tip: "💡 Second derivative positive = happy face (minimum)" },
    10: { title: "First Principles", band: "Advanced", description: "Derive derivatives from the limit definition.", keyPoints: ["f'(x) = lim(h→0) [f(x+h) - f(x)]/h", "Expand f(x + h) carefully", "Simplify and cancel h before taking limit"], examples: [{question: "Differentiate x² from first principles", answer: "f'(x) = 2x"}], tip: "💡 This proves the rules work - essential for understanding" },
    11: { title: "Applied Optimization", band: "Advanced", description: "Solve real-world optimization problems.", keyPoints: ["Create function from word problem", "Use constraints to reduce to one variable", "Find critical points and verify max/min"], examples: [{question: "Maximize area of rectangle with perimeter 20", answer: "Maximum area = 25 when x = 5"}], tip: "💡 Draw a diagram and label all variables" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style differentiation questions combining all techniques.", keyPoints: ["Read carefully - identify which rule to use", "Check if chain rule is needed", "Verify your answer makes sense"], examples: [{question: "Full differentiation problems", answer: "Various"}], tip: "🏆 You've mastered differentiation - a key LC Higher Level skill!" }
};

const lcHlCalculusIntHelpContent = {
    1: { title: "Basic Integration", band: "Foundation", description: "Integration is the reverse of differentiation.", keyPoints: ["∫xⁿdx = xⁿ⁺¹/(n+1) + C", "Don't forget the constant +C", "Check by differentiating back"], examples: [{question: "∫x³dx", answer: "x⁴/4 + C"}], tip: "💡 Integration is reverse differentiation" },
    2: { title: "Power Rule Integration", band: "Foundation", description: "Apply the power rule for integration systematically.", keyPoints: ["Add 1 to power", "Divide by new power", "Works for negative and fractional powers too"], examples: [{question: "∫3x²dx", answer: "x³ + C"}], tip: "💡 ∫xⁿdx = xⁿ⁺¹/(n+1) + C" },
    3: { title: "Trig Integration", band: "Foundation", description: "Integrate basic trigonometric functions.", keyPoints: ["∫sin x dx = -cos x + C", "∫cos x dx = sin x + C", "∫sec²x dx = tan x + C"], examples: [{question: "∫cos(2x)dx", answer: "sin(2x)/2 + C"}], tip: "💡 Remember the negative sign with sin!" },
    4: { title: "Exponential Integration", band: "Developing", description: "Integrate exponential functions.", keyPoints: ["∫eˣdx = eˣ + C", "∫eᵏˣdx = eᵏˣ/k + C", "∫1/x dx = ln|x| + C"], examples: [{question: "∫e³ˣdx", answer: "e³ˣ/3 + C"}], tip: "💡 Divide by the coefficient of x" },
    5: { title: "Definite Integrals", band: "Developing", description: "Evaluate integrals between limits.", keyPoints: ["∫[a,b] = F(b) - F(a)", "Substitute upper limit first", "No +C needed for definite integrals"], examples: [{question: "∫₀² x²dx", answer: "8/3"}], tip: "💡 Upper minus lower, no constant needed" },
    6: { title: "Area Under Curve", band: "Developing", description: "Use integration to find areas.", keyPoints: ["Area = ∫[a,b] f(x)dx for f(x) ≥ 0", "Below x-axis gives negative value", "Use absolute value for total area"], examples: [{question: "Area under y = x² from 0 to 3", answer: "9 square units"}], tip: "💡 Area below axis? Take absolute value" },
    7: { title: "Area Between Curves", band: "Proficient", description: "Find area between two curves.", keyPoints: ["Area = ∫[a,b] |f(x) - g(x)|dx", "Find intersection points first", "Top curve minus bottom curve"], examples: [{question: "Area between y = x² and y = x", answer: "1/6 square units"}], tip: "💡 Always subtract lower from upper curve" },
    8: { title: "Average Value", band: "Proficient", description: "Find average value of function over interval.", keyPoints: ["Average = (1/(b-a))∫[a,b] f(x)dx", "Divide integral by interval length", "Common in applied contexts"], examples: [{question: "Average of x² on [0,3]", answer: "3"}], tip: "💡 Average = integral ÷ interval width" },
    9: { title: "Applied Integration", band: "Proficient", description: "Solve real-world problems using integration.", keyPoints: ["Distance from velocity", "Work from force", "Total from rate of change"], examples: [{question: "Distance traveled with v(t) = 3t²", answer: "∫v(t)dt = t³"}], tip: "💡 Integration finds total from rate" },
    10: { title: "Optimization Setup", band: "Advanced", description: "Set up optimization problems requiring calculus.", keyPoints: ["Express quantity in terms of one variable", "Use constraints to eliminate variables", "Differentiate and set equal to zero"], examples: [{question: "Maximize volume with fixed surface area", answer: "Set up V(x), find dV/dx = 0"}], tip: "💡 Constraints reduce variables - key skill!" },
    11: { title: "Complex Applications", band: "Advanced", description: "Multi-step integration problems.", keyPoints: ["Combine multiple techniques", "Related rates with integration", "Inflection points and curve analysis"], examples: [{question: "Combining calculus techniques", answer: "Various"}], tip: "💡 Break complex problems into steps" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style integration questions.", keyPoints: ["Identify correct technique", "Show all working clearly", "Check answer by differentiating"], examples: [{question: "Mixed integration problems", answer: "Various"}], tip: "🏆 Integration mastered - essential for Paper 1!" }
};

const lcHlAlgebraHelpContent = {
    1: { title: "Linear Equations", band: "Foundation", description: "Solve equations with one unknown.", keyPoints: ["Collect like terms", "Isolate the variable", "Do same operation to both sides"], examples: [{question: "Solve 3x + 7 = 22", answer: "x = 5"}], tip: "💡 Whatever you do to one side, do to the other" },
    2: { title: "Quadratic Equations", band: "Foundation", description: "Solve ax² + bx + c = 0.", keyPoints: ["Try factorising first", "Use formula: x = (-b ± √(b²-4ac))/2a", "Check solutions by substitution"], examples: [{question: "Solve x² - 5x + 6 = 0", answer: "x = 2 or x = 3"}], tip: "💡 Formula always works when factorising doesn't" },
    3: { title: "Simultaneous (2 var)", band: "Foundation", description: "Solve two equations with two unknowns.", keyPoints: ["Elimination or substitution", "Match coefficients for elimination", "Substitute back to find second variable"], examples: [{question: "3x + y = 10, x - y = 2", answer: "x = 3, y = 1"}], tip: "💡 Substitution good when one variable is 'easy'" },
    4: { title: "Inequalities", band: "Developing", description: "Solve and represent inequalities.", keyPoints: ["Solve like equations", "Flip sign when multiplying by negative", "Show on number line"], examples: [{question: "Solve 2x - 5 < 7", answer: "x < 6"}], tip: "💡 Remember: multiply by negative = flip inequality" },
    5: { title: "Modulus Equations", band: "Developing", description: "Solve equations involving |x|.", keyPoints: ["|x| = a gives x = a or x = -a", "Consider positive and negative cases", "Check solutions satisfy original"], examples: [{question: "Solve |2x - 3| = 7", answer: "x = 5 or x = -2"}], tip: "💡 Modulus = distance from zero (always positive)" },
    6: { title: "Factor Theorem", band: "Developing", description: "If f(a) = 0, then (x - a) is a factor.", keyPoints: ["Test values to find factors", "f(a) = 0 means (x - a) is factor", "Use to factorise cubics"], examples: [{question: "Show (x - 2) is factor of x³ - 8", answer: "f(2) = 8 - 8 = 0 ✓"}], tip: "💡 Try x = ±1, ±2 first for integer roots" },
    7: { title: "Discriminant", band: "Proficient", description: "Use b² - 4ac to analyze quadratic roots.", keyPoints: ["Δ > 0: two real roots", "Δ = 0: one repeated root", "Δ < 0: no real roots (complex)"], examples: [{question: "Nature of roots for x² + 2x + 5 = 0", answer: "Δ = 4 - 20 = -16 < 0, no real roots"}], tip: "💡 Discriminant tells you what type of solutions" },
    8: { title: "Polynomial Division", band: "Proficient", description: "Divide polynomials systematically.", keyPoints: ["Long division or synthetic division", "Divide leading terms first", "Quotient × divisor + remainder = original"], examples: [{question: "Divide x³ + 2x² - x - 2 by (x + 1)", answer: "x² + x - 2"}], tip: "💡 Synthetic division is faster for (x - a) divisors" },
    9: { title: "Indices & Logs", band: "Proficient", description: "Work with exponential and logarithmic expressions.", keyPoints: ["aᵐ × aⁿ = aᵐ⁺ⁿ", "log(ab) = log a + log b", "logₐx = y means aʸ = x"], examples: [{question: "Solve 2ˣ = 16", answer: "x = 4"}], tip: "💡 Logs are inverse of exponentials" },
    10: { title: "Simultaneous (3 var)", band: "Advanced", description: "Solve three equations with three unknowns.", keyPoints: ["Eliminate one variable first", "Reduce to 2 equations in 2 unknowns", "Work systematically"], examples: [{question: "x + y + z = 6, 2x - y + z = 3, x + 2y - z = 5", answer: "x = 2, y = 1, z = 3"}], tip: "💡 Pick the easiest variable to eliminate first" },
    11: { title: "Complex Equations", band: "Advanced", description: "Challenging algebraic equations.", keyPoints: ["Combine multiple techniques", "Systematic approach essential", "Check solutions always"], examples: [{question: "Complex algebraic problems", answer: "Various"}], tip: "💡 Break into smaller steps" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style algebra questions.", keyPoints: ["Read carefully", "Show all working", "Verify answers"], examples: [{question: "Mixed algebra problems", answer: "Various"}], tip: "🏆 Algebra is the foundation of all mathematics!" }
};

const lcHlSequencesHelpContent = {
    1: { title: "Arithmetic Sequences", band: "Foundation", description: "Sequences with constant difference.", keyPoints: ["Common difference d = Tₙ₊₁ - Tₙ", "Tₙ = a + (n-1)d", "a is first term, d is common difference"], examples: [{question: "Find T₁₀ if a = 3, d = 5", answer: "T₁₀ = 3 + 9(5) = 48"}], tip: "💡 Arithmetic = adding same amount each time" },
    2: { title: "Arithmetic Series", band: "Foundation", description: "Sum of arithmetic sequence.", keyPoints: ["Sₙ = n/2(2a + (n-1)d)", "Or Sₙ = n/2(first + last)", "n is number of terms"], examples: [{question: "Sum of 2+5+8+...+29", answer: "S₁₀ = 10/2(2+29) = 155"}], tip: "💡 Pair first and last terms for quick sum" },
    3: { title: "Geometric Sequences", band: "Foundation", description: "Sequences with constant ratio.", keyPoints: ["Common ratio r = Tₙ₊₁/Tₙ", "Tₙ = arⁿ⁻¹", "a is first term, r is common ratio"], examples: [{question: "Find T₅ if a = 2, r = 3", answer: "T₅ = 2(3)⁴ = 162"}], tip: "💡 Geometric = multiplying by same amount" },
    4: { title: "Geometric Series", band: "Developing", description: "Sum of geometric sequence.", keyPoints: ["Sₙ = a(1-rⁿ)/(1-r) for r ≠ 1", "Or Sₙ = a(rⁿ-1)/(r-1)", "Use appropriate formula based on r"], examples: [{question: "Sum 3 + 6 + 12 + 24 + 48", answer: "S₅ = 3(2⁵-1)/(2-1) = 93"}], tip: "💡 Check r < 1 or r > 1 for formula choice" },
    5: { title: "Sum to Infinity", band: "Developing", description: "Sum of infinite geometric series.", keyPoints: ["S∞ = a/(1-r) only when |r| < 1", "Series converges if |r| < 1", "Series diverges if |r| ≥ 1"], examples: [{question: "Sum 1 + 1/2 + 1/4 + ...", answer: "S∞ = 1/(1-0.5) = 2"}], tip: "💡 Only works when |r| < 1!" },
    6: { title: "Sigma Notation", band: "Developing", description: "Use Σ notation for series.", keyPoints: ["Σ(i=1 to n) means add terms from i=1 to n", "Identify pattern in expression", "Can split into separate sums"], examples: [{question: "Σ(i=1 to 5) 2i", answer: "2+4+6+8+10 = 30"}], tip: "💡 Σ just means 'add up'" },
    7: { title: "Applied Arithmetic", band: "Proficient", description: "Real-world arithmetic sequence problems.", keyPoints: ["Identify first term and difference", "Model with Tₙ formula", "Often involves time-based growth"], examples: [{question: "Salary starting €30k, €2k raise/year", answer: "Salary year 10 = 30 + 9(2) = €48k"}], tip: "💡 Look for constant addition = arithmetic" },
    8: { title: "Applied Geometric", band: "Proficient", description: "Real-world geometric sequence problems.", keyPoints: ["Compound interest is geometric", "Drug dosage, depreciation", "Growth/decay models"], examples: [{question: "€1000 at 5% for 10 years", answer: "1000(1.05)¹⁰ = €1628.89"}], tip: "💡 Percentage change = geometric (multiply)" },
    9: { title: "Mixed Problems", band: "Proficient", description: "Combining arithmetic and geometric.", keyPoints: ["Identify which type", "May need both in one problem", "Set up equations from conditions"], examples: [{question: "Mixed sequence problems", answer: "Various"}], tip: "💡 Adding = arithmetic, multiplying = geometric" },
    10: { title: "Recursive Sequences", band: "Advanced", description: "Sequences defined by recurrence relation.", keyPoints: ["Tₙ₊₁ = f(Tₙ)", "Need initial term(s)", "Generate terms step by step"], examples: [{question: "Tₙ₊₁ = 2Tₙ + 1, T₁ = 1", answer: "T₂ = 3, T₃ = 7, T₄ = 15"}], tip: "💡 Each term depends on previous term(s)" },
    11: { title: "Complex Applications", band: "Advanced", description: "Challenging sequence problems.", keyPoints: ["Multi-step problems", "Combining concepts", "Real-world modelling"], examples: [{question: "Complex applications", answer: "Various"}], tip: "💡 Draw diagrams and work systematically" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style sequence questions.", keyPoints: ["All techniques combined", "Applied contexts", "Series and sums"], examples: [{question: "Mixed sequence mastery", answer: "Various"}], tip: "🏆 Sequences appear in many LC contexts!" }
};

const lcHlComplexHelpContent = {
    1: { title: "Complex Operations", band: "Foundation", description: "Add, subtract, multiply complex numbers.", keyPoints: ["Add real to real, imaginary to imaginary", "(a+bi)(c+di) = (ac-bd) + (ad+bc)i", "i² = -1"], examples: [{question: "(3+2i) + (1-4i)", answer: "4 - 2i"}], tip: "💡 Treat i like a variable, but i² = -1" },
    2: { title: "Complex Division", band: "Foundation", description: "Divide complex numbers.", keyPoints: ["Multiply by conjugate of denominator", "Conjugate of a+bi is a-bi", "(a+bi)(a-bi) = a² + b²"], examples: [{question: "(2+3i)/(1-i)", answer: "-1/2 + 5i/2"}], tip: "💡 Conjugate makes denominator real" },
    3: { title: "Argand Diagram", band: "Foundation", description: "Plot complex numbers on Argand plane.", keyPoints: ["x-axis = real, y-axis = imaginary", "a + bi plotted at (a, b)", "Distance from origin = modulus"], examples: [{question: "Plot 3 + 4i", answer: "Point at (3, 4)"}], tip: "💡 Argand diagram = complex number coordinate plane" },
    4: { title: "Modulus & Argument", band: "Developing", description: "Find |z| and arg(z).", keyPoints: ["|z| = √(a² + b²)", "arg(z) = tan⁻¹(b/a)", "Consider quadrant for argument"], examples: [{question: "Find |3+4i|", answer: "|z| = √(9+16) = 5"}], tip: "💡 Modulus = distance, argument = angle" },
    5: { title: "Polar Form", band: "Developing", description: "Express complex numbers in polar form.", keyPoints: ["z = r(cos θ + i sin θ)", "r = |z|, θ = arg(z)", "Also written as r cis θ"], examples: [{question: "Polar form of 1+i", answer: "√2 cis(π/4)"}], tip: "💡 cis θ means cos θ + i sin θ" },
    6: { title: "Polar Multiplication", band: "Developing", description: "Multiply and divide in polar form.", keyPoints: ["z₁z₂: multiply moduli, add arguments", "z₁/z₂: divide moduli, subtract arguments", "Much easier than rectangular!"], examples: [{question: "2 cis(30°) × 3 cis(60°)", answer: "6 cis(90°)"}], tip: "💡 Polar form makes ×÷ easy!" },
    7: { title: "De Moivre Powers", band: "Proficient", description: "Use De Moivre's theorem for powers.", keyPoints: ["[r cis θ]ⁿ = rⁿ cis(nθ)", "Raise modulus to power", "Multiply argument by power"], examples: [{question: "[2 cis(30°)]³", answer: "8 cis(90°) = 8i"}], tip: "💡 De Moivre makes powers easy" },
    8: { title: "Roots of Complex", band: "Proficient", description: "Find nth roots of complex numbers.", keyPoints: ["n roots equally spaced", "Add 360°/n for each root", "All have same modulus"], examples: [{question: "Cube roots of 8", answer: "2, 2cis(120°), 2cis(240°)"}], tip: "💡 nth roots are evenly spaced around circle" },
    9: { title: "Complex Equations", band: "Proficient", description: "Solve equations with complex numbers.", keyPoints: ["Let z = a + bi and substitute", "Equate real and imaginary parts", "Solve simultaneous equations"], examples: [{question: "z² = -4", answer: "z = ±2i"}], tip: "💡 Set real = real, imaginary = imaginary" },
    10: { title: "Identity Proofs", band: "Advanced", description: "Use De Moivre to prove trig identities.", keyPoints: ["Expand [cis θ]ⁿ two ways", "Compare real and imaginary parts", "Derive double/triple angle formulas"], examples: [{question: "Prove cos 2θ = cos²θ - sin²θ", answer: "Use (cis θ)²"}], tip: "💡 De Moivre connects complex to trig" },
    11: { title: "Argand Geometry", band: "Advanced", description: "Geometric interpretation of complex operations.", keyPoints: ["|z - w| = distance between z and w", "Multiplication rotates and scales", "Division reverses rotation"], examples: [{question: "Locus |z - 2| = 3", answer: "Circle centre 2, radius 3"}], tip: "💡 Complex operations have geometric meanings" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style complex number questions.", keyPoints: ["Combine all techniques", "Argand diagram proofs", "Roots and powers"], examples: [{question: "Mixed complex problems", answer: "Various"}], tip: "🏆 Complex numbers - beautiful mathematics!" }
};

const lcHlFunctionsHelpContent = {
    1: { title: "Function Notation", band: "Foundation", description: "Understand and use f(x) notation.", keyPoints: ["f(x) means function of x", "f(2) means substitute x = 2", "Different letters = different functions"], examples: [{question: "If f(x) = 2x + 3, find f(4)", answer: "f(4) = 2(4) + 3 = 11"}], tip: "💡 f(x) is just a machine: input x, get output" },
    2: { title: "Domain & Range", band: "Foundation", description: "Find domain and range of functions.", keyPoints: ["Domain = valid inputs (x values)", "Range = possible outputs (y values)", "Watch for division by zero, negatives under √"], examples: [{question: "Domain of f(x) = 1/(x-2)", answer: "x ≠ 2 or ℝ\\{2}"}], tip: "💡 Domain: what can go in? Range: what comes out?" },
    3: { title: "Composite Functions", band: "Foundation", description: "Combine two functions.", keyPoints: ["f∘g means f(g(x))", "Work from inside out", "Order matters: f∘g ≠ g∘f usually"], examples: [{question: "f(x) = x², g(x) = x+1, find f(g(x))", answer: "(x+1)²"}], tip: "💡 f(g(x)) = put g(x) into f" },
    4: { title: "Inverse Functions", band: "Developing", description: "Find f⁻¹(x).", keyPoints: ["Swap x and y, solve for y", "f⁻¹(f(x)) = x", "Not all functions have inverses"], examples: [{question: "Find inverse of f(x) = 2x + 3", answer: "f⁻¹(x) = (x-3)/2"}], tip: "💡 Inverse undoes what function does" },
    5: { title: "Exponential Functions", band: "Developing", description: "Work with aˣ functions.", keyPoints: ["Always positive for real x", "y = aˣ passes through (0,1)", "Horizontal asymptote at y = 0"], examples: [{question: "Sketch y = 2ˣ", answer: "Curve through (0,1), increasing"}], tip: "💡 Exponentials grow (a>1) or decay (0<a<1)" },
    6: { title: "Logarithmic Functions", band: "Developing", description: "Work with log functions.", keyPoints: ["log_a(x) = y means aʸ = x", "log and exp are inverses", "Domain x > 0 only"], examples: [{question: "Solve log₂(x) = 3", answer: "x = 8"}], tip: "💡 Log asks 'what power?'" },
    7: { title: "Transformations", band: "Proficient", description: "Transform function graphs.", keyPoints: ["f(x) + c: shift up c", "f(x + c): shift left c", "af(x): stretch vertically by a"], examples: [{question: "Describe y = f(x-2) + 3", answer: "Shift right 2, up 3"}], tip: "💡 Inside brackets = horizontal (opposite sign)" },
    8: { title: "Graphing Functions", band: "Proficient", description: "Sketch function graphs accurately.", keyPoints: ["Find intercepts, asymptotes", "Identify key features", "Use calculus for turning points"], examples: [{question: "Key features of rational function", answer: "Asymptotes, intercepts, behavior"}], tip: "💡 Start with intercepts and asymptotes" },
    9: { title: "Piecewise Functions", band: "Proficient", description: "Functions defined in pieces.", keyPoints: ["Different rules for different x-values", "Check continuity at boundaries", "Evaluate carefully at junction points"], examples: [{question: "f(x) = x² if x<0, 2x if x≥0", answer: "Parabola then line"}], tip: "💡 Graph each piece separately, then combine" },
    10: { title: "Exponential Models", band: "Advanced", description: "Model real situations with exponentials.", keyPoints: ["Growth: N = N₀eᵏᵗ, k > 0", "Decay: N = N₀e⁻ᵏᵗ", "Half-life, doubling time"], examples: [{question: "Population doubles every 5 years", answer: "N = N₀(2)^(t/5)"}], tip: "💡 Exponentials model constant % change" },
    11: { title: "Complex Functions", band: "Advanced", description: "Challenging function problems.", keyPoints: ["Combine multiple concepts", "Inverse of composite", "Domain/range of transformed functions"], examples: [{question: "Complex function analysis", answer: "Various"}], tip: "💡 Work step by step, check each stage" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style function questions.", keyPoints: ["All function concepts", "Real-world applications", "Graphical analysis"], examples: [{question: "Mixed function problems", answer: "Various"}], tip: "🏆 Functions are everywhere in maths!" }
};

const lcHlFinancialHelpContent = {
    1: { title: "Compound Interest", band: "Foundation", description: "Calculate compound interest.", keyPoints: ["A = P(1 + r)ⁿ", "P = principal, r = rate, n = periods", "Interest compounds on previous interest"], examples: [{question: "€1000 at 5% for 3 years", answer: "€1000(1.05)³ = €1157.63"}], tip: "💡 Compound = interest on interest" },
    2: { title: "Depreciation", band: "Foundation", description: "Calculate reducing value.", keyPoints: ["V = P(1 - r)ⁿ", "Value decreases over time", "Same formula, subtract rate"], examples: [{question: "€20,000 car, 15% depreciation/year, 4 years", answer: "€20,000(0.85)⁴ = €10,440.31"}], tip: "💡 Depreciation = negative growth" },
    3: { title: "Percentage Change", band: "Foundation", description: "Calculate percentage changes.", keyPoints: ["% change = (new-old)/old × 100", "Increase: multiply by (1 + r)", "Decrease: multiply by (1 - r)"], examples: [{question: "€80 to €100", answer: "(100-80)/80 × 100 = 25% increase"}], tip: "💡 Always divide by original value" },
    4: { title: "Present Value", band: "Developing", description: "Calculate present value of future sum.", keyPoints: ["PV = FV/(1+r)ⁿ", "Discounting reverses compounding", "What's future money worth today?"], examples: [{question: "PV of €5000 in 3 years at 4%", answer: "€5000/(1.04)³ = €4444.98"}], tip: "💡 Present value discounts the future" },
    5: { title: "Future Value", band: "Developing", description: "Calculate future value.", keyPoints: ["FV = PV(1+r)ⁿ", "How much will investment grow to?", "Compounding increases value"], examples: [{question: "€2000 invested at 6% for 5 years", answer: "€2000(1.06)⁵ = €2676.45"}], tip: "💡 Future value = compounding forward" },
    6: { title: "Regular Savings", band: "Developing", description: "Calculate value of regular deposits.", keyPoints: ["Uses geometric series", "FV = P × (rⁿ-1)/(r-1) where r = 1+i", "Each payment grows differently"], examples: [{question: "€100/month at 6% for 2 years", answer: "Geometric series sum"}], tip: "💡 Regular savings = geometric series" },
    7: { title: "Geometric Series", band: "Proficient", description: "Apply series to financial problems.", keyPoints: ["Sum = a(rⁿ-1)/(r-1)", "Identify first term and ratio", "Link to savings/loans"], examples: [{question: "Sum of deposits with interest", answer: "Geometric series formula"}], tip: "💡 Finance problems are often geometric series" },
    8: { title: "Loan Calculations", band: "Proficient", description: "Calculate loan repayments.", keyPoints: ["Present value of payments = loan", "Amortisation formula", "Balance reduces with each payment"], examples: [{question: "Monthly payment on €10,000 loan", answer: "Use loan formula"}], tip: "💡 Loan = present value of all repayments" },
    9: { title: "AER", band: "Proficient", description: "Annual Equivalent Rate.", keyPoints: ["AER = (1 + r/n)ⁿ - 1", "Allows comparison of different rates", "Accounts for compounding frequency"], examples: [{question: "AER for 6% compounded monthly", answer: "(1 + 0.06/12)¹² - 1 = 6.17%"}], tip: "💡 AER = true annual rate with compounding" },
    10: { title: "Mortgage Problems", band: "Advanced", description: "Complex mortgage calculations.", keyPoints: ["Long-term loans with regular payments", "Calculate total interest paid", "Compare different terms"], examples: [{question: "25-year mortgage analysis", answer: "Various calculations"}], tip: "💡 Mortgages combine all financial concepts" },
    11: { title: "Complex Applications", band: "Advanced", description: "Multi-step financial problems.", keyPoints: ["Combine multiple concepts", "Real-world scenarios", "Investment comparison"], examples: [{question: "Compare investment options", answer: "Various"}], tip: "💡 Always identify which formula applies" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style financial maths.", keyPoints: ["All financial concepts", "Applied problems", "Clear working essential"], examples: [{question: "Mixed financial problems", answer: "Various"}], tip: "🏆 Financial maths is very practical!" }
};

const lcHlProofHelpContent = {
    1: { title: "Direct Proof Basics", band: "Foundation", description: "Prove statements directly.", keyPoints: ["Start with given information", "Use logical steps to reach conclusion", "Each step must be justified"], examples: [{question: "Prove sum of two evens is even", answer: "2m + 2n = 2(m+n), which is even"}], tip: "💡 Direct proof: start → logical steps → end" },
    2: { title: "Algebraic Proof", band: "Foundation", description: "Prove algebraic statements.", keyPoints: ["Use algebraic manipulation", "LHS = ... = RHS", "Or transform one side to equal other"], examples: [{question: "Prove (a+b)² = a² + 2ab + b²", answer: "Expand LHS"}], tip: "💡 Work on one side to make it equal the other" },
    3: { title: "Proof Structure", band: "Foundation", description: "Structure proofs correctly.", keyPoints: ["State what you're proving", "Show clear logical steps", "State conclusion clearly"], examples: [{question: "Proper proof format", answer: "Given → Working → Therefore"}], tip: "💡 Clear structure = clear proof" },
    4: { title: "Induction Basics", band: "Developing", description: "Understanding mathematical induction.", keyPoints: ["Step 1: Prove for n = 1 (base case)", "Step 2: Assume true for n = k", "Step 3: Prove true for n = k+1"], examples: [{question: "Induction structure", answer: "Base case + Inductive step"}], tip: "💡 Induction: domino effect for integers" },
    5: { title: "Induction - Series", band: "Developing", description: "Prove series formulas by induction.", keyPoints: ["Prove formula for Σ", "Use P(k) to prove P(k+1)", "Add (k+1)th term to both sides"], examples: [{question: "Prove Σr = n(n+1)/2", answer: "Standard induction proof"}], tip: "💡 Add T_{k+1} to both sides of P(k)" },
    6: { title: "Induction - Divisibility", band: "Developing", description: "Prove divisibility by induction.", keyPoints: ["Show n=1 case", "Express P(k+1) using P(k)", "Factor out the divisor"], examples: [{question: "Prove 3ⁿ - 1 divisible by 2", answer: "Induction with factoring"}], tip: "💡 Write P(k+1) - P(k) or similar" },
    7: { title: "Contradiction Basics", band: "Proficient", description: "Proof by contradiction method.", keyPoints: ["Assume opposite is true", "Derive logical contradiction", "Therefore original must be true"], examples: [{question: "Contradiction structure", answer: "Assume NOT P, derive contradiction"}], tip: "💡 Contradiction: assume false, find impossibility" },
    8: { title: "√2 Irrational", band: "Proficient", description: "Classic proof that √2 is irrational.", keyPoints: ["Assume √2 = p/q in lowest terms", "Show p and q both even (contradiction)", "Therefore √2 cannot be rational"], examples: [{question: "Prove √2 is irrational", answer: "Standard contradiction proof"}], tip: "💡 This proof appears frequently in exams!" },
    9: { title: "Geometric Proofs", band: "Proficient", description: "Prove geometric statements.", keyPoints: ["Use properties and theorems", "Clear diagram essential", "State reasons for each step"], examples: [{question: "Geometric proof", answer: "Using theorems with reasons"}], tip: "💡 Always draw and label diagram" },
    10: { title: "Complex Induction", band: "Advanced", description: "Challenging induction proofs.", keyPoints: ["Multiple base cases possible", "Strong induction if needed", "Complex algebraic manipulation"], examples: [{question: "Advanced induction", answer: "Various techniques"}], tip: "💡 Some proofs need k and k-1 cases" },
    11: { title: "Mixed Proof Types", band: "Advanced", description: "Combining proof techniques.", keyPoints: ["Choose appropriate method", "May need multiple approaches", "Justify method choice"], examples: [{question: "Mixed proof problems", answer: "Various"}], tip: "💡 Direct, induction, or contradiction?" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style proof questions.", keyPoints: ["All proof techniques", "Clear logical structure", "Complete justification"], examples: [{question: "Mixed proof mastery", answer: "Various"}], tip: "🏆 Proof is the heart of mathematics!" }
};

const lcHlProbabilityHelpContent = {
    1: { title: "Basic Probability", band: "Foundation", description: "Fundamental probability concepts.", keyPoints: ["P(A) = favourable/total outcomes", "0 ≤ P(A) ≤ 1", "P(A) + P(not A) = 1"], examples: [{question: "P(head on fair coin)", answer: "1/2"}], tip: "💡 Probability = chance of event happening" },
    2: { title: "Addition Rule", band: "Foundation", description: "Probability of A or B.", keyPoints: ["P(A∪B) = P(A) + P(B) - P(A∩B)", "For mutually exclusive: P(A∪B) = P(A) + P(B)", "Watch for overlap!"], examples: [{question: "P(red or queen) from cards", answer: "Use addition rule with overlap"}], tip: "💡 'Or' means add, but subtract overlap" },
    3: { title: "Multiplication Rule", band: "Foundation", description: "Probability of A and B.", keyPoints: ["P(A∩B) = P(A) × P(B|A)", "For independent: P(A∩B) = P(A) × P(B)", "Order matters for dependent events"], examples: [{question: "P(two reds without replacement)", answer: "P(R₁) × P(R₂|R₁)"}], tip: "💡 'And' means multiply" },
    4: { title: "Conditional Probability", band: "Developing", description: "Probability given an event occurred.", keyPoints: ["P(A|B) = P(A∩B)/P(B)", "Given B happened, what's P(A)?", "Reduces sample space"], examples: [{question: "P(rain|cloudy)", answer: "P(rain and cloudy)/P(cloudy)"}], tip: "💡 P(A|B) = 'P(A given B)'" },
    5: { title: "Tree Diagrams", band: "Developing", description: "Visualize sequential events.", keyPoints: ["Branches show outcomes", "Multiply along branches", "Add across branches for 'or'"], examples: [{question: "Two-stage experiment", answer: "Draw tree, multiply paths"}], tip: "💡 Trees make complex probability clear" },
    6: { title: "Independence", band: "Developing", description: "Test and use independence.", keyPoints: ["Independent if P(A∩B) = P(A)×P(B)", "Equivalently: P(A|B) = P(A)", "One event doesn't affect other"], examples: [{question: "Test if A,B independent", answer: "Check if P(A∩B) = P(A)×P(B)"}], tip: "💡 Independence: one doesn't affect the other" },
    7: { title: "Binomial Distribution", band: "Proficient", description: "Fixed trials, two outcomes.", keyPoints: ["P(X=r) = ⁿCᵣ × pʳ × qⁿ⁻ʳ", "n trials, p = P(success)", "Fixed number of independent trials"], examples: [{question: "P(3 heads in 5 tosses)", answer: "⁵C₃ × (0.5)³ × (0.5)²"}], tip: "💡 Binomial = fixed trials, same probability each" },
    8: { title: "Expected Value", band: "Proficient", description: "Calculate expected value.", keyPoints: ["E(X) = Σ x × P(X=x)", "Long-run average", "Used in decision making"], examples: [{question: "E(X) for dice roll", answer: "E(X) = 1(1/6)+2(1/6)+...+6(1/6) = 3.5"}], tip: "💡 Expected value = weighted average" },
    9: { title: "Bayes' Theorem", band: "Proficient", description: "Reverse conditional probability.", keyPoints: ["P(A|B) = P(B|A)×P(A)/P(B)", "Updates probability with new info", "Use tree diagram to help"], examples: [{question: "Medical test problem", answer: "Apply Bayes' theorem"}], tip: "💡 Bayes reverses the condition" },
    10: { title: "Negative Binomial", band: "Advanced", description: "Trials until kth success.", keyPoints: ["P(kth success on nth trial)", "Different from binomial!", "k-1 successes in first n-1 trials"], examples: [{question: "P(3rd head on 5th toss)", answer: "⁴C₂ × (0.5)² × (0.5)² × 0.5"}], tip: "💡 Last trial must be a success" },
    11: { title: "Complex Applications", band: "Advanced", description: "Multi-step probability problems.", keyPoints: ["Combine multiple concepts", "Real-world scenarios", "Careful probability calculations"], examples: [{question: "Complex probability", answer: "Various"}], tip: "💡 Break into smaller parts" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style probability.", keyPoints: ["All probability concepts", "Expected value applications", "Bayes and binomial"], examples: [{question: "Mixed probability mastery", answer: "Various"}], tip: "🏆 Probability is in every Paper 2!" }
};

const lcHlStatisticsHelpContent = {
    1: { title: "Descriptive Stats", band: "Foundation", description: "Summarize data numerically.", keyPoints: ["Mean = sum/count", "Median = middle value", "Mode = most frequent"], examples: [{question: "Find mean of 3,5,7,8,12", answer: "Mean = 35/5 = 7"}], tip: "💡 Mean, median, mode describe 'typical' value" },
    2: { title: "Mean & Standard Dev", band: "Foundation", description: "Calculate mean and standard deviation.", keyPoints: ["σ = √(Σ(x-x̄)²/n)", "Measures spread from mean", "Higher σ = more spread"], examples: [{question: "Calculate standard deviation", answer: "Use formula with mean"}], tip: "💡 Standard deviation measures spread" },
    3: { title: "Quartiles & IQR", band: "Foundation", description: "Find quartiles and interquartile range.", keyPoints: ["Q1 = 25th percentile", "Q2 = median (50th)", "IQR = Q3 - Q1"], examples: [{question: "Find IQR", answer: "Order data, find Q1 and Q3"}], tip: "💡 IQR measures spread of middle 50%" },
    4: { title: "Normal Distribution", band: "Developing", description: "Work with normal distributions.", keyPoints: ["Bell-shaped, symmetric", "μ = mean, σ = standard deviation", "68-95-99.7 rule"], examples: [{question: "P(X < μ + σ)", answer: "≈ 84%"}], tip: "💡 Normal curve: most data near mean" },
    5: { title: "Z-Scores", band: "Developing", description: "Standardize values.", keyPoints: ["z = (x - μ)/σ", "z tells SDs from mean", "Use tables for probability"], examples: [{question: "Find z for x=72, μ=65, σ=5", answer: "z = (72-65)/5 = 1.4"}], tip: "💡 Z-score: how many SDs from mean" },
    6: { title: "Inverse Normal", band: "Developing", description: "Find values from probabilities.", keyPoints: ["Given P(X < k), find k", "Use tables backwards", "k = μ + zσ"], examples: [{question: "Find top 10% cutoff", answer: "Find z for 0.9, then x = μ + zσ"}], tip: "💡 Inverse: probability → value" },
    7: { title: "Confidence Intervals", band: "Proficient", description: "Estimate population parameters.", keyPoints: ["x̄ ± z(σ/√n) for mean", "p̂ ± z√(p̂(1-p̂)/n) for proportion", "95% CI uses z = 1.96"], examples: [{question: "95% CI for mean", answer: "x̄ ± 1.96(σ/√n)"}], tip: "💡 CI = range likely to contain true value" },
    8: { title: "Hypothesis Testing", band: "Proficient", description: "Test statistical claims.", keyPoints: ["H₀: null hypothesis", "H₁: alternative hypothesis", "Reject H₀ if evidence strong"], examples: [{question: "Test if mean = 50", answer: "Set up H₀: μ = 50, H₁: μ ≠ 50"}], tip: "💡 Hypothesis test: is claim likely true?" },
    9: { title: "P-Values", band: "Proficient", description: "Interpret p-values.", keyPoints: ["p-value = P(data|H₀ true)", "Small p-value → reject H₀", "p < 0.05 typically significant"], examples: [{question: "p-value = 0.03, 5% level", answer: "Reject H₀ (0.03 < 0.05)"}], tip: "💡 p-value < significance level → reject H₀" },
    10: { title: "Sample Size", band: "Advanced", description: "Calculate required sample size.", keyPoints: ["n = (zσ/E)² for margin of error E", "Larger n = more precision", "Cost vs precision trade-off"], examples: [{question: "n for 95% CI, E = 2", answer: "n = (1.96σ/2)²"}], tip: "💡 Bigger sample = smaller margin of error" },
    11: { title: "Two-Tailed Tests", band: "Advanced", description: "Test for difference in either direction.", keyPoints: ["H₁: μ ≠ value (two-tailed)", "Split significance level", "Use |z| for comparison"], examples: [{question: "Two-tailed test at 5%", answer: "Reject if |z| > 1.96"}], tip: "💡 Two-tailed: could be higher OR lower" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style statistics.", keyPoints: ["All statistics concepts", "Hypothesis testing", "Confidence intervals"], examples: [{question: "Mixed statistics mastery", answer: "Various"}], tip: "🏆 Statistics is essential for Paper 2!" }
};

const lcHlCoordGeomHelpContent = {
    1: { title: "Distance & Midpoint", band: "Foundation", description: "Calculate distance and midpoint.", keyPoints: ["d = √[(x₂-x₁)² + (y₂-y₁)²]", "Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2)", "Distance formula from Pythagoras"], examples: [{question: "Distance (1,2) to (4,6)", answer: "√[(3)² + (4)²] = 5"}], tip: "💡 Distance formula = Pythagoras in disguise" },
    2: { title: "Slope & Equations", band: "Foundation", description: "Find slope and write line equations.", keyPoints: ["m = (y₂-y₁)/(x₂-x₁)", "y - y₁ = m(x - x₁)", "y = mx + c form"], examples: [{question: "Line through (1,3) with slope 2", answer: "y - 3 = 2(x - 1) → y = 2x + 1"}], tip: "💡 Slope = rise/run" },
    3: { title: "Parallel & Perpendicular", band: "Foundation", description: "Identify and find parallel/perpendicular lines.", keyPoints: ["Parallel: same slope (m₁ = m₂)", "Perpendicular: m₁ × m₂ = -1", "Negative reciprocal slopes"], examples: [{question: "Perpendicular to y = 2x + 1", answer: "Slope = -1/2"}], tip: "💡 Perpendicular slopes multiply to -1" },
    4: { title: "Line Intersection", band: "Developing", description: "Find where lines meet.", keyPoints: ["Solve equations simultaneously", "Substitute to find x and y", "No solution = parallel lines"], examples: [{question: "2x + y = 7, x - y = 2", answer: "(3, 1)"}], tip: "💡 Intersection = simultaneous equations" },
    5: { title: "Perpendicular Distance", band: "Developing", description: "Distance from point to line.", keyPoints: ["d = |ax₁ + by₁ + c|/√(a² + b²)", "Line in form ax + by + c = 0", "Always positive distance"], examples: [{question: "Distance from (3,4) to 3x + 4y - 5 = 0", answer: "|9+16-5|/5 = 4"}], tip: "💡 Formula in tables - learn to use it" },
    6: { title: "Division of Segment", band: "Developing", description: "Divide segment in given ratio.", keyPoints: ["Point dividing in ratio m:n", "x = (mx₂ + nx₁)/(m+n)", "Similarly for y"], examples: [{question: "Divide (1,2) to (7,8) in ratio 2:1", answer: "(5, 6)"}], tip: "💡 Internal division formula" },
    7: { title: "Circle Equation", band: "Proficient", description: "Equation of circle.", keyPoints: ["(x-h)² + (y-k)² = r²", "Centre (h,k), radius r", "Expand for general form"], examples: [{question: "Circle centre (2,3) radius 5", answer: "(x-2)² + (y-3)² = 25"}], tip: "💡 Complete square to find centre and radius" },
    8: { title: "Tangent to Circle", band: "Proficient", description: "Find tangent to circle.", keyPoints: ["Tangent perpendicular to radius", "Use perpendicular slope", "One touch point only"], examples: [{question: "Tangent at (3,4) on x²+y²=25", answer: "3x + 4y = 25"}], tip: "💡 Tangent ⊥ radius at point of contact" },
    9: { title: "Circle & Line", band: "Proficient", description: "Intersection of circle and line.", keyPoints: ["Substitute line into circle", "Solve quadratic", "Discriminant determines intersection type"], examples: [{question: "Where y = x meets x² + y² = 8", answer: "(2,2) and (-2,-2)"}], tip: "💡 Two points, one point, or no intersection" },
    10: { title: "Touching Circles", band: "Advanced", description: "Circles that touch.", keyPoints: ["Externally: d = r₁ + r₂", "Internally: d = |r₁ - r₂|", "d = distance between centres"], examples: [{question: "Do circles touch?", answer: "Compare d with r₁ ± r₂"}], tip: "💡 Distance between centres = sum or difference of radii" },
    11: { title: "Complex Loci", band: "Advanced", description: "Advanced coordinate geometry.", keyPoints: ["Locus problems", "Combining line and circle", "Geometric properties"], examples: [{question: "Complex coordinate geometry", answer: "Various"}], tip: "💡 Draw diagrams, use all formulas" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style coordinate geometry.", keyPoints: ["All coordinate concepts", "Lines and circles", "Applied problems"], examples: [{question: "Mixed coord geom mastery", answer: "Various"}], tip: "🏆 Coordinate geometry combines algebra and geometry!" }
};

const lcHlTrigonometryHelpContent = {
    1: { title: "Trig Ratios", band: "Foundation", description: "Basic trigonometric ratios.", keyPoints: ["sin θ = opposite/hypotenuse", "cos θ = adjacent/hypotenuse", "tan θ = opposite/adjacent"], examples: [{question: "Find sin 30°", answer: "1/2"}], tip: "💡 SOH CAH TOA" },
    2: { title: "Exact Values", band: "Foundation", description: "Know exact trig values.", keyPoints: ["sin 30° = 1/2, cos 30° = √3/2", "sin 45° = cos 45° = 1/√2", "sin 60° = √3/2, cos 60° = 1/2"], examples: [{question: "cos 60°", answer: "1/2"}], tip: "💡 Learn the 30-45-60 triangle values" },
    3: { title: "Sine Rule", band: "Foundation", description: "Use sine rule in triangles.", keyPoints: ["a/sin A = b/sin B = c/sin C", "Use when you have angle-side pairs", "Two possible solutions sometimes"], examples: [{question: "Find side using sine rule", answer: "a = b × sin A / sin B"}], tip: "💡 Sine rule: sides and opposite angles" },
    4: { title: "Cosine Rule", band: "Developing", description: "Use cosine rule in triangles.", keyPoints: ["a² = b² + c² - 2bc cos A", "Use when no angle-side pair", "Rearrange to find angle"], examples: [{question: "Find side using cosine rule", answer: "a² = b² + c² - 2bc cos A"}], tip: "💡 Cosine rule: two sides and included angle" },
    5: { title: "Area of Triangle", band: "Developing", description: "Calculate triangle area.", keyPoints: ["Area = ½ab sin C", "Need two sides and included angle", "Or use Hero's formula"], examples: [{question: "Area with sides 5,7 and angle 60°", answer: "½ × 5 × 7 × sin 60° = 15.16"}], tip: "💡 Area = ½ × side × side × sin(included angle)" },
    6: { title: "Trig Equations", band: "Developing", description: "Solve trigonometric equations.", keyPoints: ["Find reference angle first", "Consider all quadrants", "Multiple solutions in range"], examples: [{question: "Solve sin x = 0.5, 0° ≤ x ≤ 360°", answer: "x = 30° or 150°"}], tip: "💡 CAST diagram for quadrants" },
    7: { title: "Compound Angles", band: "Proficient", description: "sin(A±B), cos(A±B), tan(A±B).", keyPoints: ["sin(A+B) = sin A cos B + cos A sin B", "cos(A+B) = cos A cos B - sin A sin B", "Signs change for (A-B)"], examples: [{question: "Find sin 75°", answer: "sin(45°+30°) = ..."}], tip: "💡 Compound formulas in tables - use them!" },
    8: { title: "Double Angles", band: "Proficient", description: "sin 2A, cos 2A, tan 2A formulas.", keyPoints: ["sin 2A = 2 sin A cos A", "cos 2A = cos²A - sin²A = 1-2sin²A = 2cos²A-1", "tan 2A = 2tan A/(1-tan²A)"], examples: [{question: "Simplify 2sin x cos x", answer: "sin 2x"}], tip: "💡 Double angle = compound with B = A" },
    9: { title: "3D Trigonometry", band: "Proficient", description: "Apply trig in 3D situations.", keyPoints: ["Draw clear 2D sections", "Identify right triangles", "Angles of elevation/depression"], examples: [{question: "3D trig problem", answer: "Extract 2D triangles"}], tip: "💡 Find the right triangle in 3D" },
    10: { title: "Trig Proofs", band: "Advanced", description: "Prove trigonometric identities.", keyPoints: ["Start with one side", "Use known identities", "Work toward other side"], examples: [{question: "Prove identity", answer: "LHS = ... = RHS"}], tip: "💡 Usually work on more complex side" },
    11: { title: "Complex Applications", band: "Advanced", description: "Challenging trig problems.", keyPoints: ["Combine multiple concepts", "Real-world applications", "Multi-step solutions"], examples: [{question: "Complex trig applications", answer: "Various"}], tip: "💡 Draw diagrams, label clearly" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style trigonometry.", keyPoints: ["All trig concepts", "Proofs and equations", "3D and applied"], examples: [{question: "Mixed trig mastery", answer: "Various"}], tip: "🏆 Trigonometry is huge in Paper 2!" }
};

const lcHlGeometryHelpContent = {
    1: { title: "Basic Constructions", band: "Foundation", description: "Fundamental geometric constructions.", keyPoints: ["Compass and straightedge only", "Perpendicular bisector", "Angle bisector"], examples: [{question: "Construct perpendicular bisector", answer: "Compass arcs from both ends"}], tip: "💡 Constructions are precise - use compass correctly" },
    2: { title: "Triangle Properties", band: "Foundation", description: "Properties of triangles.", keyPoints: ["Angles sum to 180°", "Types: scalene, isosceles, equilateral", "Exterior angle = sum of remote interior"], examples: [{question: "Third angle if two are 50° and 60°", answer: "70°"}], tip: "💡 Triangle angles always sum to 180°" },
    3: { title: "Circle Theorems", band: "Foundation", description: "Key circle theorems.", keyPoints: ["Angle at centre = 2 × angle at circumference", "Angle in semicircle = 90°", "Tangent perpendicular to radius"], examples: [{question: "Angle in semicircle", answer: "90°"}], tip: "💡 Learn the main circle theorems" },
    4: { title: "Congruent Triangles", band: "Developing", description: "Prove triangles congruent.", keyPoints: ["SSS, SAS, ASA, AAS, RHS", "All sides and angles equal", "Give reasons for each step"], examples: [{question: "Prove congruence", answer: "State criterion with reasons"}], tip: "💡 Congruent = exactly the same shape and size" },
    5: { title: "Similar Triangles", band: "Developing", description: "Prove triangles similar.", keyPoints: ["Same angles, proportional sides", "AA similarity criterion", "Ratio of sides equal"], examples: [{question: "Prove similarity", answer: "Show equal angles or proportional sides"}], tip: "💡 Similar = same shape, different size" },
    6: { title: "Enlargement", band: "Developing", description: "Scale factor and enlargement.", keyPoints: ["Scale factor k: lengths × k", "Area × k²", "Volume × k³"], examples: [{question: "Area scale factor", answer: "Linear scale factor squared"}], tip: "💡 Area scales by k², volume by k³" },
    7: { title: "Orthocentre", band: "Proficient", description: "Construct orthocentre.", keyPoints: ["Intersection of altitudes", "Altitude perpendicular to opposite side", "Can be outside triangle"], examples: [{question: "Find orthocentre", answer: "Construct altitudes from 2 vertices"}], tip: "💡 Orthocentre = where altitudes meet" },
    8: { title: "Circumcentre", band: "Proficient", description: "Construct circumcentre.", keyPoints: ["Intersection of perpendicular bisectors", "Equidistant from all vertices", "Centre of circumscribed circle"], examples: [{question: "Find circumcentre", answer: "Construct perpendicular bisectors"}], tip: "💡 Circumcentre = equidistant from vertices" },
    9: { title: "Centroid", band: "Proficient", description: "Construct centroid.", keyPoints: ["Intersection of medians", "Divides median 2:1 from vertex", "Centre of mass"], examples: [{question: "Find centroid", answer: "Construct medians from 2 vertices"}], tip: "💡 Centroid divides median 2:1" },
    10: { title: "Theorem Proofs", band: "Advanced", description: "Prove geometric theorems.", keyPoints: ["Clear logical steps", "State reasons for each step", "Use known results"], examples: [{question: "Prove circle theorem", answer: "Logical proof with reasons"}], tip: "💡 Geometry proofs need clear reasoning" },
    11: { title: "Complex Constructions", band: "Advanced", description: "Advanced construction problems.", keyPoints: ["Multi-step constructions", "Combine basic constructions", "Locus problems"], examples: [{question: "Complex construction", answer: "Various"}], tip: "💡 Break into simpler constructions" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style geometry.", keyPoints: ["All geometry concepts", "Proofs and constructions", "Applied problems"], examples: [{question: "Mixed geometry mastery", answer: "Various"}], tip: "🏆 Geometry requires careful reasoning!" }
};

const lcHlMensurationHelpContent = {
    1: { title: "Area of Shapes", band: "Foundation", description: "Calculate areas of 2D shapes.", keyPoints: ["Rectangle = l × w", "Triangle = ½ × b × h", "Circle = πr²"], examples: [{question: "Area of circle r = 5", answer: "25π ≈ 78.54"}], tip: "💡 Area = 2D space inside shape" },
    2: { title: "Volume - Prisms", band: "Foundation", description: "Calculate volume of prisms.", keyPoints: ["V = area of base × height", "Cuboid = l × w × h", "Cross-section same throughout"], examples: [{question: "Volume cuboid 3×4×5", answer: "60 cubic units"}], tip: "💡 Prism volume = base area × height" },
    3: { title: "Volume - Cylinders", band: "Foundation", description: "Calculate cylinder volume.", keyPoints: ["V = πr²h", "Curved surface = 2πrh", "Total surface = 2πr² + 2πrh"], examples: [{question: "Volume cylinder r=3, h=7", answer: "63π ≈ 197.92"}], tip: "💡 Cylinder = circular prism" },
    4: { title: "Volume - Cones", band: "Developing", description: "Calculate cone volume.", keyPoints: ["V = ⅓πr²h", "Curved surface = πrl (l = slant)", "l² = r² + h²"], examples: [{question: "Volume cone r=3, h=4", answer: "12π ≈ 37.70"}], tip: "💡 Cone volume = ⅓ of cylinder" },
    5: { title: "Volume - Spheres", band: "Developing", description: "Calculate sphere volume.", keyPoints: ["V = ⁴⁄₃πr³", "Surface area = 4πr²", "Hemisphere = half sphere"], examples: [{question: "Volume sphere r=6", answer: "288π ≈ 904.78"}], tip: "💡 Sphere: V = ⁴⁄₃πr³" },
    6: { title: "Surface Area", band: "Developing", description: "Calculate surface areas.", keyPoints: ["Add all faces/surfaces", "Curved + flat surfaces", "Remember all parts"], examples: [{question: "Total surface area", answer: "Sum of all surfaces"}], tip: "💡 Don't forget curved surfaces!" },
    7: { title: "Composite Solids", band: "Proficient", description: "Volume of combined shapes.", keyPoints: ["Break into simple shapes", "Add or subtract volumes", "Watch for internal spaces"], examples: [{question: "Hemisphere on cylinder", answer: "V_cyl + V_hemi"}], tip: "💡 Break complex shapes into simpler ones" },
    8: { title: "Similar Solids", band: "Proficient", description: "Scale factors for similar solids.", keyPoints: ["Linear scale factor = k", "Area scale = k²", "Volume scale = k³"], examples: [{question: "Volume ratio if lengths in ratio 1:2", answer: "1:8"}], tip: "💡 Volume scales by cube of linear factor" },
    9: { title: "Cone Nets", band: "Proficient", description: "Nets of cones.", keyPoints: ["Curved surface becomes sector", "Arc length = circumference of base", "Sector angle = (r/l) × 360°"], examples: [{question: "Sector angle for cone net", answer: "(r/l) × 360°"}], tip: "💡 Net arc length = base circumference" },
    10: { title: "Frustum", band: "Advanced", description: "Volume of truncated cone.", keyPoints: ["V = ⅓πh(R² + Rr + r²)", "Or: large cone - small cone", "Curved surface = π(R+r)l"], examples: [{question: "Frustum volume", answer: "Use frustum formula or subtraction"}], tip: "💡 Frustum = cone with top cut off" },
    11: { title: "Inscribed Solids", band: "Advanced", description: "Solids inside other solids.", keyPoints: ["Use geometry to find dimensions", "Often involves optimization", "Draw clear diagrams"], examples: [{question: "Sphere in cone", answer: "Geometric relationships"}], tip: "💡 Inscribed problems need careful geometry" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style mensuration.", keyPoints: ["All volume/area concepts", "Similar solids", "Complex shapes"], examples: [{question: "Mixed mensuration mastery", answer: "Various"}], tip: "🏆 Mensuration tests spatial thinking!" }
};

const lcHlCountingHelpContent = {
    1: { title: "Counting Principle", band: "Foundation", description: "Fundamental counting principle.", keyPoints: ["If A has m ways, B has n ways", "Total ways = m × n", "Multiply choices at each stage"], examples: [{question: "3 shirts, 4 pants: outfits?", answer: "3 × 4 = 12"}], tip: "💡 Multiply choices at each step" },
    2: { title: "Permutations", band: "Foundation", description: "Arrangements where order matters.", keyPoints: ["nPr = n!/(n-r)!", "Order matters", "n! = n × (n-1) × ... × 1"], examples: [{question: "Arrange 3 from 5 letters", answer: "⁵P₃ = 60"}], tip: "💡 Permutation = arrangement (order matters)" },
    3: { title: "Combinations", band: "Foundation", description: "Selections where order doesn't matter.", keyPoints: ["nCr = n!/[r!(n-r)!]", "Order doesn't matter", "nCr = nPr/r!"], examples: [{question: "Choose 3 from 5", answer: "⁵C₃ = 10"}], tip: "💡 Combination = selection (order doesn't matter)" },
    4: { title: "nPr and nCr", band: "Developing", description: "Apply permutation and combination formulas.", keyPoints: ["Identify if order matters", "Permutation if arranging", "Combination if selecting"], examples: [{question: "Committee of 4 from 10", answer: "¹⁰C₄ = 210"}], tip: "💡 Arranging vs selecting - which is it?" },
    5: { title: "Arrangements", band: "Developing", description: "Arrange objects with conditions.", keyPoints: ["Letters in a word", "Circular arrangements", "Repeated items divide by r!"], examples: [{question: "Arrangements of MISSISSIPPI", answer: "11!/(4!4!2!)"}], tip: "💡 Repeated items: divide by factorial of repeats" },
    6: { title: "Selections", band: "Developing", description: "Select with conditions.", keyPoints: ["At least/at most constraints", "From different groups", "Complementary counting"], examples: [{question: "Select with conditions", answer: "Use combinations"}], tip: "💡 'At least 1' = Total - None" },
    7: { title: "Constrained Counting", band: "Proficient", description: "Counting with restrictions.", keyPoints: ["Items must/must not be together", "Adjacent or separated", "Fix then arrange rest"], examples: [{question: "A and B must be together", answer: "Treat as unit, then arrange"}], tip: "💡 Constraints: fix first, count rest" },
    8: { title: "With Repetition", band: "Proficient", description: "Counting when repetition allowed.", keyPoints: ["n^r for r choices from n items", "Different from without replacement", "PIN codes, passwords"], examples: [{question: "4-digit PIN (0-9)", answer: "10⁴ = 10000"}], tip: "💡 With repetition: n^r" },
    9: { title: "Grid Paths", band: "Proficient", description: "Count paths in a grid.", keyPoints: ["Only right and down moves", "Total moves = m + n", "Choose which are right: (m+n)Cm"], examples: [{question: "3×4 grid paths", answer: "⁷C₃ = 35"}], tip: "💡 Grid path = choosing which moves are right" },
    10: { title: "Complex Constraints", band: "Advanced", description: "Multiple constraints.", keyPoints: ["Combine techniques", "Cases often needed", "Inclusion-exclusion"], examples: [{question: "Complex constraints", answer: "Various"}], tip: "💡 Break into cases for complex constraints" },
    11: { title: "Pairing Problems", band: "Advanced", description: "Count ways to pair items.", keyPoints: ["Match groups", "Derangements", "Systematic approach"], examples: [{question: "Pair 2n people", answer: "(2n-1)!! = (2n-1)(2n-3)...1"}], tip: "💡 Pairing: fix one, count partners" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style counting.", keyPoints: ["All counting techniques", "Word problems", "Complex arrangements"], examples: [{question: "Mixed counting mastery", answer: "Various"}], tip: "🏆 Counting is growing in importance!" }
};

// ========== LC ORDINARY LEVEL STRAND HELP CONTENT ==========

const lcOlCalculusHelpContent = {
    1: { title: "Power Rule Basics", band: "Foundation", description: "Differentiate simple powers of x.", keyPoints: ["If y = xⁿ, then dy/dx = nxⁿ⁻¹", "Bring power down, reduce by 1", "Constant differentiates to 0"], examples: [{question: "y = x⁵", answer: "dy/dx = 5x⁴"}], tip: "💡 Power comes down, subtract 1 from power" },
    2: { title: "Differentiating Polynomials", band: "Foundation", description: "Differentiate expressions with multiple terms.", keyPoints: ["Differentiate each term separately", "Constants multiply through", "Sum of derivatives"], examples: [{question: "y = 3x⁴ - 2x² + 5", answer: "dy/dx = 12x³ - 4x"}], tip: "💡 Term by term, constants stay" },
    3: { title: "Negative Indices", band: "Foundation", description: "Differentiate terms with negative powers.", keyPoints: ["1/x = x⁻¹", "1/x² = x⁻²", "Same rule: nxⁿ⁻¹"], examples: [{question: "y = 1/x³", answer: "y = x⁻³, dy/dx = -3x⁻⁴"}], tip: "💡 Rewrite fractions as negative powers first" },
    4: { title: "Finding Slopes", band: "Developing", description: "Find slope of curve at a point.", keyPoints: ["Substitute x-value into dy/dx", "Slope = f'(x) at that point", "Tangent slope at x = a is f'(a)"], examples: [{question: "y = x² at x = 3", answer: "dy/dx = 2x, slope = 6"}], tip: "💡 Differentiate first, then substitute" },
    5: { title: "Equations of Tangents", band: "Developing", description: "Find equation of tangent line.", keyPoints: ["Find slope using f'(x)", "Use y - y₁ = m(x - x₁)", "Point on curve + slope"], examples: [{question: "Tangent to y = x² at (2,4)", answer: "slope = 4, y - 4 = 4(x - 2)"}], tip: "💡 Need a point AND the slope" },
    6: { title: "Rate of Change", band: "Developing", description: "Apply derivatives to rates.", keyPoints: ["dy/dx = rate of change of y", "Interpret in context", "Units matter"], examples: [{question: "s(t) = t², find speed at t=3", answer: "v = ds/dt = 2t = 6 m/s"}], tip: "💡 Derivative tells how fast something changes" },
    7: { title: "Increasing/Decreasing", band: "Proficient", description: "Determine where function increases/decreases.", keyPoints: ["f'(x) > 0: increasing", "f'(x) < 0: decreasing", "f'(x) = 0: stationary"], examples: [{question: "Where does y = x³ - 3x increase?", answer: "f'(x) > 0 when x < -1 or x > 1"}], tip: "💡 Sign of derivative tells direction" },
    8: { title: "Max & Min Values", band: "Proficient", description: "Find maximum and minimum points.", keyPoints: ["Set f'(x) = 0", "Solve for x (stationary points)", "Substitute back for y-values"], examples: [{question: "Find turning points of y = x³ - 3x", answer: "f'(x) = 3x² - 3 = 0, x = ±1"}], tip: "💡 Turning points where slope = 0" },
    9: { title: "Second Derivative", band: "Proficient", description: "Use f''(x) to classify turning points.", keyPoints: ["f''(x) > 0: minimum", "f''(x) < 0: maximum", "f''(x) = 0: check further"], examples: [{question: "y = x³ - 3x at x = 1", answer: "f''(x) = 6x, f''(1) = 6 > 0: min"}], tip: "💡 Second derivative: + = min, - = max" },
    10: { title: "Applied Max/Min", band: "Advanced", description: "Real-world optimization problems.", keyPoints: ["Define variables", "Create expression to optimize", "Differentiate and solve"], examples: [{question: "Maximize area with 40m fence", answer: "A = x(20-x), max at x = 10"}], tip: "💡 Express what you want to optimize in one variable" },
    11: { title: "Optimisation Problems", band: "Advanced", description: "Complex SEC-style optimization.", keyPoints: ["Often need constraint equation", "Substitute to get one variable", "Find max/min and answer context"], examples: [{question: "Box volume from sheet", answer: "V = x(L-2x)(W-2x)"}], tip: "💡 Read carefully - identify what to maximize/minimize" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style differentiation questions.", keyPoints: ["All differentiation techniques", "Applied problems", "Interpret answers in context"], examples: [{question: "Full LC OL calculus problems", answer: "Various"}], tip: "🏆 Calculus is the highest-mark topic in LC OL!" }
};

const lcOlFinancialHelpContent = {
    1: { title: "VAT Calculations", band: "Foundation", description: "Calculate VAT and prices with/without VAT.", keyPoints: ["VAT added to net price", "Inclusive price × 100/123 = net", "VAT = Gross - Net"], examples: [{question: "Price €100, VAT 23%", answer: "VAT = €23, Total = €123"}], tip: "💡 VAT is always added to the base price" },
    2: { title: "Percentage Increase", band: "Foundation", description: "Increase amounts by a percentage.", keyPoints: ["Multiply by (1 + rate)", "€100 + 15% = €100 × 1.15", "Or calculate % and add"], examples: [{question: "€250 increased by 8%", answer: "€250 × 1.08 = €270"}], tip: "💡 Quick method: multiply by 1.XX" },
    3: { title: "Percentage Decrease", band: "Foundation", description: "Decrease amounts by a percentage.", keyPoints: ["Multiply by (1 - rate)", "€100 - 20% = €100 × 0.80", "Or calculate % and subtract"], examples: [{question: "€400 reduced by 15%", answer: "€400 × 0.85 = €340"}], tip: "💡 Discount: multiply by 0.XX" },
    4: { title: "Profit & Loss", band: "Developing", description: "Calculate profit, loss and percentages.", keyPoints: ["Profit = Selling - Cost", "% Profit = (Profit/Cost) × 100", "Loss if Selling < Cost"], examples: [{question: "Buy €50, sell €65", answer: "Profit = €15, % = 30%"}], tip: "💡 Profit % is based on cost price" },
    5: { title: "Margin & Markup", band: "Developing", description: "Distinguish between margin and markup.", keyPoints: ["Markup % based on cost", "Margin % based on selling price", "Different denominators!"], examples: [{question: "Cost €80, Sell €100", answer: "Markup = 25%, Margin = 20%"}], tip: "💡 Markup = % of cost; Margin = % of selling price" },
    6: { title: "Income Tax Bands", band: "Developing", description: "Calculate tax using Irish tax bands.", keyPoints: ["First €X at lower rate (20%)", "Rest at higher rate (40%)", "Tax credits reduce tax owed"], examples: [{question: "€45,000 income, €40,000 band", answer: "€40k × 20% + €5k × 40%"}], tip: "💡 Split income into bands, then calculate each" },
    7: { title: "Simple Interest", band: "Proficient", description: "Calculate simple interest.", keyPoints: ["I = PRT/100", "P = principal, R = rate, T = time", "Interest same each year"], examples: [{question: "€5000 at 3% for 4 years", answer: "I = 5000 × 3 × 4 / 100 = €600"}], tip: "💡 Simple interest: same amount each year" },
    8: { title: "Compound Interest", band: "Proficient", description: "Calculate compound interest.", keyPoints: ["A = P(1 + r/100)ⁿ", "Interest added to principal", "More frequent = more interest"], examples: [{question: "€4000 at 5% for 3 years", answer: "A = 4000 × 1.05³ = €4630.50"}], tip: "💡 Compound: interest earns interest" },
    9: { title: "Depreciation", band: "Proficient", description: "Calculate reducing value over time.", keyPoints: ["V = P(1 - r/100)ⁿ", "Value decreases each year", "Common for cars, equipment"], examples: [{question: "€20,000 car, 15% p.a., 3 years", answer: "V = 20000 × 0.85³ = €12,282.50"}], tip: "💡 Depreciation uses (1 - rate)" },
    10: { title: "Multi-Year Compound", band: "Advanced", description: "Complex compound interest problems.", keyPoints: ["Different rates per year", "Finding original principal", "Finding time period"], examples: [{question: "After 4 years, €5,520. Rate 5%. Find P", answer: "P = 5520 ÷ 1.05⁴ = €4,540.60"}], tip: "💡 Work backwards by dividing" },
    11: { title: "Complex Tax Problems", band: "Advanced", description: "Multi-step financial calculations.", keyPoints: ["Combine multiple concepts", "Real-world scenarios", "Show all working"], examples: [{question: "Net pay after tax and USC", answer: "Multiple deductions"}], tip: "💡 Break complex problems into steps" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style financial maths.", keyPoints: ["All financial concepts", "Extended problems", "Interpret context"], examples: [{question: "Full LC OL financial problems", answer: "Various"}], tip: "🏆 Financial maths appears every year!" }
};

const lcOlTrigonometryHelpContent = {
    1: { title: "Right Angle Trig", band: "Foundation", description: "Use trig ratios in right triangles.", keyPoints: ["SOH-CAH-TOA", "Identify opposite, adjacent, hypotenuse", "Label from the angle"], examples: [{question: "Find opposite if hyp=10, sin=0.6", answer: "opp = 10 × 0.6 = 6"}], tip: "💡 Label O, A, H from your angle" },
    2: { title: "SOHCAHTOA", band: "Foundation", description: "Apply sin, cos, tan to find sides.", keyPoints: ["Sin = Opp/Hyp", "Cos = Adj/Hyp", "Tan = Opp/Adj"], examples: [{question: "Adj=8, angle=35°, find opp", answer: "tan35° = opp/8, opp = 5.6"}], tip: "💡 Choose the ratio with what you have and want" },
    3: { title: "Finding Angles", band: "Foundation", description: "Use inverse trig to find angles.", keyPoints: ["sin⁻¹, cos⁻¹, tan⁻¹", "Calculator in degree mode", "Check answer makes sense"], examples: [{question: "sin θ = 0.5, find θ", answer: "θ = sin⁻¹(0.5) = 30°"}], tip: "💡 Inverse trig gives the angle" },
    4: { title: "Sine Rule", band: "Developing", description: "Apply sine rule in any triangle.", keyPoints: ["a/sinA = b/sinB = c/sinC", "Use when: angle-side pairs", "Two forms depending on unknown"], examples: [{question: "a=8, A=40°, B=60°, find b", answer: "b/sin60 = 8/sin40, b = 10.8"}], tip: "💡 Sine rule: need angle-opposite side pair" },
    5: { title: "Cosine Rule", band: "Developing", description: "Apply cosine rule.", keyPoints: ["a² = b² + c² - 2bc·cosA", "Use when: SAS or SSS", "Rearrange to find angle"], examples: [{question: "b=7, c=9, A=50°, find a", answer: "a² = 49 + 81 - 126cos50°"}], tip: "💡 Cosine rule: when sine rule won't work" },
    6: { title: "Area Formula ½abSinC", band: "Developing", description: "Calculate area using trigonometry.", keyPoints: ["Area = ½ × a × b × sinC", "Need two sides and included angle", "Angle between the two sides"], examples: [{question: "a=6, b=8, C=45°, find area", answer: "A = ½ × 6 × 8 × sin45° = 16.97"}], tip: "💡 ½absinC when you know two sides and included angle" },
    7: { title: "Two Triangles", band: "Proficient", description: "Solve problems with multiple triangles.", keyPoints: ["Find sides/angles step by step", "Use shared sides", "Draw diagram clearly"], examples: [{question: "Two connected triangles", answer: "Solve first, use result in second"}], tip: "💡 Work through one triangle at a time" },
    8: { title: "Navigation Problems", band: "Proficient", description: "Apply trig to bearings and navigation.", keyPoints: ["Bearings measured from North, clockwise", "Draw North line at each point", "Use angle properties"], examples: [{question: "From A, bearing 045° to B", answer: "Angle = 45° from North"}], tip: "💡 Always draw North line and measure clockwise" },
    9: { title: "Elevation/Depression", band: "Proficient", description: "Angles of elevation and depression.", keyPoints: ["Elevation: looking up from horizontal", "Depression: looking down", "Alternate angles often equal"], examples: [{question: "Tower 50m away, elevation 35°", answer: "height = 50 × tan35°"}], tip: "💡 Elevation up, depression down from horizontal" },
    10: { title: "Combined Triangles", band: "Advanced", description: "Complex multi-triangle problems.", keyPoints: ["Plan your approach", "May need multiple rules", "Keep track of calculations"], examples: [{question: "SEC-style navigation", answer: "Multiple triangles"}], tip: "💡 Label everything clearly in your diagram" },
    11: { title: "Real-World Applications", band: "Advanced", description: "Applied trigonometry in context.", keyPoints: ["Construction, surveying", "Navigation, sport", "Always draw a diagram"], examples: [{question: "Swimming markers problem", answer: "Identify triangles first"}], tip: "💡 Real problems: draw, label, identify triangles" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style trigonometry.", keyPoints: ["All trig techniques", "Extended contexts", "Clear working essential"], examples: [{question: "Full LC OL trig problems", answer: "Various"}], tip: "🏆 Trigonometry is worth 375+ marks over 7 years!" }
};

const lcOlMensurationHelpContent = {
    1: { title: "Volume - Cylinders", band: "Foundation", description: "Calculate volume of cylinders.", keyPoints: ["V = πr²h", "r = radius, h = height", "Remember π ≈ 3.14159"], examples: [{question: "r=5cm, h=10cm", answer: "V = π × 25 × 10 = 785 cm³"}], tip: "💡 Area of circle × height" },
    2: { title: "Surface Area - Cylinders", band: "Foundation", description: "Calculate surface area of cylinders.", keyPoints: ["SA = 2πr² + 2πrh", "Two circles + curved surface", "Curved surface = 2πrh"], examples: [{question: "r=3cm, h=7cm", answer: "SA = 2π(9) + 2π(3)(7) = 188.5 cm²"}], tip: "💡 Two circles + rectangle wrapped around" },
    3: { title: "Volume - Cones", band: "Foundation", description: "Calculate volume of cones.", keyPoints: ["V = ⅓πr²h", "One-third of cylinder", "Same base and height"], examples: [{question: "r=6cm, h=12cm", answer: "V = ⅓π × 36 × 12 = 452.4 cm³"}], tip: "💡 Cone = ⅓ of cylinder with same r and h" },
    4: { title: "Volume - Spheres", band: "Developing", description: "Calculate volume of spheres.", keyPoints: ["V = ⁴⁄₃πr³", "Only need radius", "Common for balls, tanks"], examples: [{question: "r = 9cm", answer: "V = ⁴⁄₃π × 729 = 3053.6 cm³"}], tip: "💡 Sphere volume: 4/3 π r cubed" },
    5: { title: "Surface Area - Cones", band: "Developing", description: "Calculate surface area of cones.", keyPoints: ["SA = πr² + πrl", "l = slant height", "l² = r² + h² (Pythagoras)"], examples: [{question: "r=4cm, h=6cm", answer: "l = √(16+36) = 7.21, SA = π(4)² + π(4)(7.21)"}], tip: "💡 Find slant height first using Pythagoras" },
    6: { title: "Surface Area - Spheres", band: "Developing", description: "Calculate surface area of spheres.", keyPoints: ["SA = 4πr²", "Four times circle area", "Only need radius"], examples: [{question: "r = 5cm", answer: "SA = 4π × 25 = 314.2 cm²"}], tip: "💡 Sphere surface area: 4 π r squared" },
    7: { title: "Composite Solids", band: "Proficient", description: "Volumes of combined shapes.", keyPoints: ["Add volumes of parts", "Or subtract hollow section", "Identify component shapes"], examples: [{question: "Cylinder with hemisphere on top", answer: "V = πr²h + ⅔πr³"}], tip: "💡 Break into shapes you know" },
    8: { title: "Sectors & Arcs", band: "Proficient", description: "Calculate arc length and sector area.", keyPoints: ["Arc = θ/360 × 2πr", "Sector area = θ/360 × πr²", "θ in degrees"], examples: [{question: "r=10cm, θ=72°", answer: "Arc = 72/360 × 2π(10) = 12.57cm"}], tip: "💡 Fraction of the circle = θ/360" },
    9: { title: "Similar Shapes", band: "Proficient", description: "Apply scale factors to similar shapes.", keyPoints: ["Linear: k", "Area: k²", "Volume: k³"], examples: [{question: "Scale factor 2", answer: "Area × 4, Volume × 8"}], tip: "💡 k for length, k² for area, k³ for volume" },
    10: { title: "Scaling Volumes", band: "Advanced", description: "Apply scaling to volume problems.", keyPoints: ["If length × k, volume × k³", "Find k from given dimensions", "Apply to other quantities"], examples: [{question: "Radius doubled", answer: "Volume × 8"}], tip: "💡 Cube the scale factor for volume" },
    11: { title: "Complex Composites", band: "Advanced", description: "Multi-step mensuration problems.", keyPoints: ["Multiple shapes combined", "Surface area with removed parts", "Real-world contexts"], examples: [{question: "Tank with hemispherical ends", answer: "Cylinder + 2 hemispheres"}], tip: "💡 Sketch and label the components" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style mensuration.", keyPoints: ["All mensuration formulae", "Applied contexts", "Careful with units"], examples: [{question: "Full LC OL mensuration", answer: "Various"}], tip: "🏆 Mensuration worth 350 marks - know your formulae!" }
};

const lcOlStatisticsDescHelpContent = {
    1: { title: "Mean & Mode", band: "Foundation", description: "Calculate mean and mode.", keyPoints: ["Mean = sum ÷ count", "Mode = most frequent", "Can have no mode or multiple"], examples: [{question: "2, 4, 4, 6, 8", answer: "Mean = 24/5 = 4.8, Mode = 4"}], tip: "💡 Mean = average, Mode = most common" },
    2: { title: "Median & Range", band: "Foundation", description: "Find median and range.", keyPoints: ["Median = middle value when ordered", "If even count, average middle two", "Range = max - min"], examples: [{question: "1, 3, 5, 7, 9", answer: "Median = 5, Range = 8"}], tip: "💡 Order data first for median" },
    3: { title: "Reading Charts", band: "Foundation", description: "Interpret bar charts, pie charts, line graphs.", keyPoints: ["Read axis labels and scales", "Compare heights/lengths", "Calculate from chart data"], examples: [{question: "Bar chart interpretation", answer: "Read values carefully"}], tip: "💡 Check scales carefully on all axes" },
    4: { title: "Standard Deviation", band: "Developing", description: "Calculate and interpret standard deviation.", keyPoints: ["Measures spread of data", "σ = √[Σ(x-x̄)²/n]", "Low σ = data close to mean"], examples: [{question: "Data: 2, 4, 6, 8", answer: "Mean = 5, σ = √5 ≈ 2.24"}], tip: "💡 Calculator can find σ - understand what it means" },
    5: { title: "Frequency Tables", band: "Developing", description: "Calculate statistics from frequency tables.", keyPoints: ["Mean = Σfx / Σf", "Use midpoints for grouped data", "Cumulative frequency"], examples: [{question: "Grouped data mean", answer: "Use class midpoints × frequency"}], tip: "💡 Multiply values by their frequencies" },
    6: { title: "Histograms", band: "Developing", description: "Interpret and draw histograms.", keyPoints: ["Area represents frequency", "Y-axis = frequency density", "Unequal class widths"], examples: [{question: "Draw histogram", answer: "Frequency density = f/width"}], tip: "💡 Histogram: area = frequency, not height" },
    7: { title: "Quartiles & IQR", band: "Proficient", description: "Calculate quartiles and interquartile range.", keyPoints: ["Q1 = 25%, Q2 = 50%, Q3 = 75%", "IQR = Q3 - Q1", "Measures middle spread"], examples: [{question: "12 data points, find Q1", answer: "Q1 at position (n+1)/4"}], tip: "💡 IQR shows spread of middle 50%" },
    8: { title: "Box Plots", band: "Proficient", description: "Draw and interpret box plots.", keyPoints: ["Min, Q1, Q2, Q3, Max", "Box shows middle 50%", "Whiskers to min/max"], examples: [{question: "Draw box plot", answer: "5-number summary"}], tip: "💡 Box plot = 5-number summary visualized" },
    9: { title: "Comparing Data Sets", band: "Proficient", description: "Use statistics to compare distributions.", keyPoints: ["Compare means for average", "Compare SD for consistency", "Compare ranges for spread"], examples: [{question: "Compare two teams", answer: "Use appropriate measures"}], tip: "💡 Pick relevant statistics for the context" },
    10: { title: "Outliers", band: "Advanced", description: "Identify and handle outliers.", keyPoints: ["Outside Q1 - 1.5×IQR or Q3 + 1.5×IQR", "May affect mean greatly", "Consider excluding or investigating"], examples: [{question: "Is 95 an outlier?", answer: "Calculate boundaries"}], tip: "💡 Outliers can significantly affect the mean" },
    11: { title: "Data Interpretation", band: "Advanced", description: "Interpret statistics in context.", keyPoints: ["What do values mean?", "Draw valid conclusions", "Recognise limitations"], examples: [{question: "Interpret findings", answer: "Relate to context"}], tip: "💡 Statistics must be interpreted in context" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style descriptive statistics.", keyPoints: ["All statistical measures", "Tables and charts", "Interpretation and comparison"], examples: [{question: "Full LC OL statistics", answer: "Various"}], tip: "🏆 Statistics worth 330+ marks - show all working!" }
};

const lcOlProbabilityHelpContent = {
    1: { title: "Basic Probability", band: "Foundation", description: "Understand probability basics.", keyPoints: ["P(event) = favourable/total", "0 ≤ P ≤ 1", "P(certain) = 1, P(impossible) = 0"], examples: [{question: "Die showing 6", answer: "P(6) = 1/6"}], tip: "💡 Probability = what you want / total outcomes" },
    2: { title: "Sample Spaces", band: "Foundation", description: "List all possible outcomes.", keyPoints: ["Sample space = all outcomes", "Use systematic listing", "Two-way tables help"], examples: [{question: "Two coins", answer: "HH, HT, TH, TT - 4 outcomes"}], tip: "💡 List systematically to not miss any" },
    3: { title: "Addition Rule", band: "Foundation", description: "P(A or B) for events.", keyPoints: ["P(A or B) = P(A) + P(B) if mutually exclusive", "Mutually exclusive = can't both happen", "Otherwise subtract overlap"], examples: [{question: "P(1 or 2) on die", answer: "1/6 + 1/6 = 2/6 = 1/3"}], tip: "💡 'Or' often means add (if no overlap)" },
    4: { title: "Multiplication Rule", band: "Developing", description: "P(A and B) for events.", keyPoints: ["P(A and B) = P(A) × P(B) if independent", "Independent = one doesn't affect other", "Tree diagrams help"], examples: [{question: "Two heads in a row", answer: "½ × ½ = ¼"}], tip: "💡 'And' usually means multiply" },
    5: { title: "Tree Diagrams", band: "Developing", description: "Use tree diagrams for multi-stage events.", keyPoints: ["Branches show choices", "Multiply along branches", "Add for different paths to same outcome"], examples: [{question: "Two draws from bag", answer: "Draw tree, multiply along paths"}], tip: "💡 Multiply along, add across" },
    6: { title: "Counting Principle", band: "Developing", description: "Count outcomes systematically.", keyPoints: ["Multiply choices at each stage", "Permutations if order matters", "Combinations if order doesn't"], examples: [{question: "3 shirts, 4 pants", answer: "3 × 4 = 12 outfits"}], tip: "💡 If A has m ways, B has n ways: m × n total" },
    7: { title: "Without Replacement", band: "Proficient", description: "Probability when items not replaced.", keyPoints: ["Second probability changes", "Total decreases by 1", "Favourable may decrease too"], examples: [{question: "2 red from 3R, 2B without replacement", answer: "3/5 × 2/4 = 6/20 = 3/10"}], tip: "💡 Without replacement: numbers change!" },
    8: { title: "Conditional Probability", band: "Proficient", description: "Probability given another event occurred.", keyPoints: ["P(A|B) = P(A given B happened)", "Reduced sample space", "Focus on when B happens"], examples: [{question: "P(6 | even)", answer: "Given even: 2,4,6. P(6) = 1/3"}], tip: "💡 'Given' means work in reduced sample" },
    9: { title: "Expected Value", band: "Proficient", description: "Calculate expected value.", keyPoints: ["E(X) = Σ x × P(x)", "Long-run average", "Used in games, decisions"], examples: [{question: "Win €5 with P=0.3, lose €2 with P=0.7", answer: "E = 5(0.3) + (-2)(0.7) = 0.10"}], tip: "💡 Expected value = sum of (outcome × probability)" },
    10: { title: "Geometric Probability", band: "Advanced", description: "First success on nth trial.", keyPoints: ["P(first success on trial n) = (1-p)^(n-1) × p", "Keep failing then succeed", "e.g., first win on 3rd game"], examples: [{question: "P(win) = 0.22, first win on 3rd", answer: "0.78² × 0.22 = 0.134"}], tip: "💡 Fail, fail, ..., then succeed" },
    11: { title: "Complex Tree Diagrams", band: "Advanced", description: "Multi-stage probability problems.", keyPoints: ["Three or more stages", "Conditional probabilities change", "Careful with branches"], examples: [{question: "Three draws, mixed replacement", answer: "Extended tree diagram"}], tip: "💡 Take it stage by stage" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style probability.", keyPoints: ["All probability concepts", "Real-world contexts", "Extended calculations"], examples: [{question: "Full LC OL probability", answer: "Various"}], tip: "🏆 Probability worth 295+ marks - always draw diagrams!" }
};

const lcOlAppliedMeasureHelpContent = {
    1: { title: "Unit Conversions", band: "Foundation", description: "Convert between units.", keyPoints: ["km, m, cm, mm", "kg, g, mg", "L, mL, cm³"], examples: [{question: "2.5 km to m", answer: "2.5 × 1000 = 2500 m"}], tip: "💡 Know your conversion factors" },
    2: { title: "Area Calculations", band: "Foundation", description: "Calculate areas of basic shapes.", keyPoints: ["Rectangle = l × w", "Triangle = ½ × b × h", "Circle = πr²"], examples: [{question: "Rectangle 8m × 5m", answer: "Area = 40 m²"}], tip: "💡 Always include correct units (m², cm²)" },
    3: { title: "Perimeter", band: "Foundation", description: "Calculate perimeter of shapes.", keyPoints: ["Sum of all sides", "Circle circumference = 2πr", "Add all outer edges"], examples: [{question: "Rectangle 6m × 4m", answer: "P = 2(6) + 2(4) = 20m"}], tip: "💡 Perimeter = distance around the edge" },
    4: { title: "Trapezoidal Rule", band: "Developing", description: "Estimate area under a curve.", keyPoints: ["A ≈ h/2[first + last + 2(middle terms)]", "h = strip width", "More strips = better estimate"], examples: [{question: "Estimate area with 4 strips", answer: "Use formula with y-values"}], tip: "💡 h/2 × [first + last + 2×middles]" },
    5: { title: "Scale Factors", band: "Developing", description: "Work with maps and scale drawings.", keyPoints: ["Scale like 1:50000", "Multiply/divide by scale", "Units must match"], examples: [{question: "Map 1:25000, 4cm = ?", answer: "4 × 25000 = 100000cm = 1km"}], tip: "💡 Scale tells real:map ratio" },
    6: { title: "Proportion Problems", band: "Developing", description: "Solve direct and inverse proportion.", keyPoints: ["Direct: y = kx", "Inverse: y = k/x", "Find k first"], examples: [{question: "y ∝ x, y=12 when x=3, find y when x=5", answer: "k = 4, y = 20"}], tip: "💡 Find the constant k first" },
    7: { title: "Speed/Distance/Time", band: "Proficient", description: "Apply speed-distance-time relationships.", keyPoints: ["Speed = Distance/Time", "Distance = Speed × Time", "Time = Distance/Speed"], examples: [{question: "240km in 3 hours", answer: "Speed = 80 km/h"}], tip: "💡 Triangle: D on top, S×T on bottom" },
    8: { title: "Work Rate Problems", band: "Proficient", description: "Calculate combined work rates.", keyPoints: ["Rate = 1/time to complete", "Add rates for combined work", "Time = 1/combined rate"], examples: [{question: "A does job in 6h, B in 4h, together?", answer: "1/6 + 1/4 = 5/12, time = 12/5 = 2.4h"}], tip: "💡 Add rates, not times" },
    9: { title: "Combined Rates", band: "Proficient", description: "Complex rate problems.", keyPoints: ["Multiple workers", "Different speeds", "Find individual rates first"], examples: [{question: "3 people working together", answer: "Add all three rates"}], tip: "💡 Work with rates, convert to times at end" },
    10: { title: "LCM Applications", band: "Advanced", description: "Use LCM in practical problems.", keyPoints: ["When will events coincide?", "Find LCM of time periods", "Cycling problems"], examples: [{question: "Two cleaners: every 6 and 8 weeks", answer: "LCM(6,8) = 24 weeks"}], tip: "💡 LCM for 'when together again'" },
    11: { title: "Complex Conversions", band: "Advanced", description: "Multi-step unit conversions.", keyPoints: ["Convert step by step", "Speed units: km/h to m/s", "Area/volume unit conversions"], examples: [{question: "72 km/h to m/s", answer: "72 × 1000/3600 = 20 m/s"}], tip: "💡 km/h to m/s: divide by 3.6" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style applied measure.", keyPoints: ["All measurement concepts", "Real-world contexts", "Multiple steps"], examples: [{question: "Full LC OL applied measure", answer: "Various"}], tip: "🏆 Applied measure appears every year!" }
};

const lcOlSequencesHelpContent = {
    1: { title: "Number Patterns", band: "Foundation", description: "Recognize and continue patterns.", keyPoints: ["Find the rule", "Add/subtract patterns", "Multiply/divide patterns"], examples: [{question: "2, 5, 8, 11, ...", answer: "Add 3 each time, next = 14"}], tip: "💡 Look at differences between terms" },
    2: { title: "Arithmetic Sequences", band: "Foundation", description: "Understand arithmetic sequences.", keyPoints: ["Common difference d", "Same amount added each time", "Linear patterns"], examples: [{question: "3, 7, 11, 15, ...", answer: "a = 3, d = 4"}], tip: "💡 Arithmetic = constant difference" },
    3: { title: "Finding Tₙ", band: "Foundation", description: "Find any term in a sequence.", keyPoints: ["Tₙ = a + (n-1)d", "a = first term", "d = common difference"], examples: [{question: "a=5, d=3, find T₁₀", answer: "T₁₀ = 5 + 9(3) = 32"}], tip: "💡 Remember: (n-1) not n!" },
    4: { title: "Tₙ = a + (n-1)d", band: "Developing", description: "Apply the nth term formula.", keyPoints: ["Sub values into formula", "Can find a, d, or n", "Rearrange as needed"], examples: [{question: "T₁ = 7, T₅ = 23, find d", answer: "23 = 7 + 4d, d = 4"}], tip: "💡 Set up equation with what you know" },
    5: { title: "Finding n", band: "Developing", description: "Find position of a term.", keyPoints: ["Set Tₙ = value", "Solve for n", "n must be positive integer"], examples: [{question: "When does 4n + 1 = 97?", answer: "4n = 96, n = 24"}], tip: "💡 Substitute and solve for n" },
    6: { title: "Arithmetic Series Sₙ", band: "Developing", description: "Sum of arithmetic sequence terms.", keyPoints: ["Sₙ = sum of first n terms", "Sₙ = n/2[2a + (n-1)d]", "Or Sₙ = n/2[a + l]"], examples: [{question: "Sum first 10 terms: 2, 5, 8...", answer: "S₁₀ = 10/2[4 + 27] = 155"}], tip: "💡 Two formulas - use the easier one" },
    7: { title: "Sₙ Formula", band: "Proficient", description: "Apply series formula fluently.", keyPoints: ["Sₙ = n/2[2a + (n-1)d]", "Sₙ = n/2[first + last]", "Can find unknowns"], examples: [{question: "S₂₀ = 630, a = 3, find d", answer: "630 = 10[6 + 19d], d = 3"}], tip: "💡 Substitute known values, solve for unknown" },
    8: { title: "Quadratic Patterns", band: "Proficient", description: "Patterns with Tₙ = an² + bn + c.", keyPoints: ["Second differences constant", "Use simultaneous equations", "Or pattern method"], examples: [{question: "1, 4, 9, 16, ...", answer: "Tₙ = n² (square numbers)"}], tip: "💡 Quadratic if second difference is constant" },
    9: { title: "Pattern Problems", band: "Proficient", description: "Patterns in visual/context problems.", keyPoints: ["Dots, matches, shapes", "Find formula from pattern", "Verify with examples"], examples: [{question: "Triangle numbers: 1, 3, 6, 10...", answer: "Tₙ = n(n+1)/2"}], tip: "💡 Draw extra examples to spot the pattern" },
    10: { title: "Finding Formula from Pattern", band: "Advanced", description: "Derive formula from sequence.", keyPoints: ["Check constant difference", "If not, try second difference", "Test formula works"], examples: [{question: "Find formula for 2, 6, 12, 20...", answer: "Second diff = 2, Tₙ = n² + n"}], tip: "💡 Test your formula with known terms" },
    11: { title: "Applied Sequences", band: "Advanced", description: "Real-world sequence applications.", keyPoints: ["Savings, growth patterns", "Stadium seating", "Building patterns"], examples: [{question: "Stadium rows: 20, 24, 28...", answer: "Arithmetic, find total seats"}], tip: "💡 Set up the sequence from the context" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style sequences.", keyPoints: ["All sequence concepts", "Pattern recognition", "Formula derivation"], examples: [{question: "Full LC OL sequences", answer: "Various"}], tip: "🏆 Sequences worth 295+ marks - practice formula derivation!" }
};

const lcOlAlgebraHelpContent = {
    1: { title: "Linear Equations", band: "Foundation", description: "Solve equations like ax + b = c.", keyPoints: ["Get x terms on one side", "Numbers on the other", "Inverse operations"], examples: [{question: "3x + 5 = 17", answer: "3x = 12, x = 4"}], tip: "💡 Undo operations in reverse order" },
    2: { title: "Substitution", band: "Foundation", description: "Substitute values into expressions.", keyPoints: ["Replace variable with value", "Follow BIMDAS", "Careful with negatives"], examples: [{question: "Find 2x² - 3x when x = 4", answer: "2(16) - 3(4) = 32 - 12 = 20"}], tip: "💡 Use brackets when substituting" },
    3: { title: "Transposing Formulae", band: "Foundation", description: "Rearrange formulae to change subject.", keyPoints: ["Do same to both sides", "Isolate the new subject", "Undo operations"], examples: [{question: "Make r subject: A = πr²", answer: "r² = A/π, r = √(A/π)"}], tip: "💡 Treat formula like an equation" },
    4: { title: "Simultaneous (Linear)", band: "Developing", description: "Solve two equations with two unknowns.", keyPoints: ["Elimination or substitution", "Make coefficients equal", "Solve for one, then other"], examples: [{question: "2x + y = 7, x - y = 2", answer: "Add: 3x = 9, x = 3, y = 1"}], tip: "💡 Elimination: add or subtract equations" },
    5: { title: "Quadratic Equations", band: "Developing", description: "Solve ax² + bx + c = 0.", keyPoints: ["Factorising", "Using the formula", "x = [-b ± √(b²-4ac)] / 2a"], examples: [{question: "x² + 5x + 6 = 0", answer: "(x+2)(x+3) = 0, x = -2 or -3"}], tip: "💡 Try factorising first, formula if stuck" },
    6: { title: "Using the Formula", band: "Developing", description: "Apply the quadratic formula.", keyPoints: ["x = [-b ± √(b²-4ac)] / 2a", "Substitute carefully", "Two solutions usually"], examples: [{question: "2x² + 3x - 5 = 0", answer: "a=2, b=3, c=-5, apply formula"}], tip: "💡 Write out a, b, c before substituting" },
    7: { title: "Linear + Quadratic", band: "Proficient", description: "Solve systems with line and curve.", keyPoints: ["Substitute linear into quadratic", "Solve resulting quadratic", "Find both unknowns"], examples: [{question: "y = x + 1, y = x²", answer: "x + 1 = x², solve x² - x - 1 = 0"}], tip: "💡 Substitute to eliminate y (or x)" },
    8: { title: "Inequalities", band: "Proficient", description: "Solve linear inequalities.", keyPoints: ["Same as equations usually", "Flip sign if multiply by negative", "Graph on number line"], examples: [{question: "3x - 2 < 7", answer: "3x < 9, x < 3"}], tip: "💡 Remember to flip if ×/÷ by negative" },
    9: { title: "Forming Equations", band: "Proficient", description: "Create equations from word problems.", keyPoints: ["Define variables", "Translate words to algebra", "Solve and check"], examples: [{question: "Sum is 15, difference is 3", answer: "x + y = 15, x - y = 3"}], tip: "💡 Define what x represents clearly" },
    10: { title: "Word Problems", band: "Advanced", description: "Complex algebraic word problems.", keyPoints: ["Read carefully", "Identify relationships", "Set up and solve"], examples: [{question: "Age problems", answer: "Set up equations from information"}], tip: "💡 Draw a diagram if it helps" },
    11: { title: "Complex Simultaneous", band: "Advanced", description: "Challenging simultaneous equations.", keyPoints: ["May need substitution then quadratic", "Fractional equations", "Three unknowns occasionally"], examples: [{question: "Non-linear systems", answer: "Careful algebraic manipulation"}], tip: "💡 Take it step by step" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style algebra.", keyPoints: ["All equation types", "Word problems", "Full working required"], examples: [{question: "Full LC OL algebra", answer: "Various"}], tip: "🏆 Algebra worth 265+ marks - show all working!" }
};

const lcOlFunctionsHelpContent = {
    1: { title: "Function Notation", band: "Foundation", description: "Understand f(x) notation.", keyPoints: ["f(x) means 'function of x'", "f(3) means substitute x = 3", "Same as y = expression"], examples: [{question: "f(x) = 2x + 1, find f(4)", answer: "f(4) = 2(4) + 1 = 9"}], tip: "💡 f(x) is just another name for y" },
    2: { title: "Evaluating f(x)", band: "Foundation", description: "Calculate function values.", keyPoints: ["Substitute given value", "Follow order of operations", "Can find f(a) for any a"], examples: [{question: "f(x) = x² - 3, find f(-2)", answer: "f(-2) = 4 - 3 = 1"}], tip: "💡 Replace every x with the given value" },
    3: { title: "Linear Graphs", band: "Foundation", description: "Plot and interpret y = mx + c.", keyPoints: ["m = slope (gradient)", "c = y-intercept", "Straight line graph"], examples: [{question: "y = 2x - 3", answer: "Slope 2, crosses y at -3"}], tip: "💡 Plot y-intercept, use slope to find more points" },
    4: { title: "Quadratic Graphs", band: "Developing", description: "Sketch and interpret parabolas.", keyPoints: ["y = ax² + bx + c", "a > 0: smile, a < 0: frown", "Vertex at x = -b/2a"], examples: [{question: "y = x² - 4x + 3", answer: "U-shape, vertex at x = 2"}], tip: "💡 Find roots, y-intercept, and vertex" },
    5: { title: "Roots from Graphs", band: "Developing", description: "Find solutions graphically.", keyPoints: ["Roots where graph crosses x-axis", "f(x) = 0 at roots", "Read x-coordinates"], examples: [{question: "Where does y = x² - 4 = 0?", answer: "x = -2 and x = 2 (from graph)"}], tip: "💡 Roots = x-intercepts = solutions" },
    6: { title: "Sketching Parabolas", band: "Developing", description: "Draw quadratic graphs from equation.", keyPoints: ["Find y-intercept (x = 0)", "Find x-intercepts (y = 0)", "Find vertex"], examples: [{question: "Sketch y = x² - 2x - 3", answer: "Roots at -1, 3; vertex at (1, -4)"}], tip: "💡 5-point method: y-int, 2 roots, vertex, symmetry" },
    7: { title: "Graph Transformations", band: "Proficient", description: "Translate and reflect graphs.", keyPoints: ["f(x) + k: up k", "f(x + k): left k", "Common exam topic"], examples: [{question: "y = f(x) + 3", answer: "Graph moved up 3 units"}], tip: "💡 +k outside = vertical, +k inside = opposite horizontal" },
    8: { title: "Exponential Graphs", band: "Proficient", description: "Understand exponential functions.", keyPoints: ["y = aˣ grows/decays", "Always positive", "y-intercept = 1 for y = aˣ"], examples: [{question: "y = 2ˣ", answer: "Increasing, passes through (0,1)"}], tip: "💡 Exponential: gets very big very fast" },
    9: { title: "Interpreting Graphs", band: "Proficient", description: "Extract information from function graphs.", keyPoints: ["Maximum/minimum values", "Increasing/decreasing intervals", "Rate of change"], examples: [{question: "When is f(x) > 0?", answer: "Where graph is above x-axis"}], tip: "💡 Graph tells you everything about the function" },
    10: { title: "Growth/Decay Models", band: "Advanced", description: "Apply exponential models.", keyPoints: ["P(t) = P₀ × aᵗ", "a > 1: growth, a < 1: decay", "Often population, value"], examples: [{question: "Bacteria doubles every hour", answer: "P(t) = P₀ × 2ᵗ"}], tip: "💡 Identify initial value and growth factor" },
    11: { title: "Real-World Functions", band: "Advanced", description: "Functions in context.", keyPoints: ["Interpret parameters", "Domain restrictions", "Practical meaning"], examples: [{question: "Profit function P(x)", answer: "Find break-even, max profit"}], tip: "💡 What do the numbers actually mean?" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style functions.", keyPoints: ["All function concepts", "Graph interpretation", "Modeling applications"], examples: [{question: "Full LC OL functions", answer: "Various"}], tip: "🏆 Functions worth 240+ marks - practice graph sketching!" }
};

const lcOlStatisticsInfHelpContent = {
    1: { title: "Sampling Basics", band: "Foundation", description: "Understand sampling concepts.", keyPoints: ["Population vs sample", "Why we sample", "Representative samples"], examples: [{question: "Why sample 100 from 10000?", answer: "Time, cost, practicality"}], tip: "💡 Sample should represent the population" },
    2: { title: "Types of Sampling", band: "Foundation", description: "Know sampling methods.", keyPoints: ["Simple random sampling", "Stratified sampling", "Systematic sampling"], examples: [{question: "Stratified sample", answer: "Proportion from each group"}], tip: "💡 Random = every member has equal chance" },
    3: { title: "Bias in Sampling", band: "Foundation", description: "Recognize and avoid bias.", keyPoints: ["Selection bias", "Response bias", "Non-response bias"], examples: [{question: "Phone survey during work hours", answer: "Misses employed people - bias"}], tip: "💡 Bias = systematic error in results" },
    4: { title: "Normal Distribution", band: "Developing", description: "Understand the normal curve.", keyPoints: ["Bell-shaped, symmetric", "Mean = median = mode", "68-95-99.7 rule"], examples: [{question: "68% within", answer: "One standard deviation of mean"}], tip: "💡 Normal curve: most data near the middle" },
    5: { title: "Z-Scores", band: "Developing", description: "Standardize using z-scores.", keyPoints: ["z = (x - μ) / σ", "How many SDs from mean", "Use tables for probability"], examples: [{question: "μ = 50, σ = 10, x = 65", answer: "z = (65-50)/10 = 1.5"}], tip: "💡 Z-score tells how unusual a value is" },
    6: { title: "Using Tables", band: "Developing", description: "Read standard normal tables.", keyPoints: ["Tables give P(Z < z)", "Area to the left", "Use symmetry for negative z"], examples: [{question: "P(Z < 1.5)", answer: "Look up 1.5 → 0.9332"}], tip: "💡 Tables formula booklet - know how to use them" },
    7: { title: "Margin of Error", band: "Proficient", description: "Calculate margin of error.", keyPoints: ["MoE = 1/√n approx", "Or MoE = z × √[p(1-p)/n]", "Larger n = smaller margin"], examples: [{question: "n = 400", answer: "MoE ≈ 1/√400 = 0.05 = 5%"}], tip: "💡 1/√n gives quick estimate of MoE" },
    8: { title: "Confidence Intervals", band: "Proficient", description: "Construct confidence intervals.", keyPoints: ["CI = estimate ± margin", "95% uses z = 1.96", "Interpret in context"], examples: [{question: "p̂ = 0.6, MoE = 0.04", answer: "95% CI: (0.56, 0.64)"}], tip: "💡 CI = best estimate ± margin of error" },
    9: { title: "Sample Proportion", band: "Proficient", description: "Work with sample proportions.", keyPoints: ["p̂ = x/n", "Standard error = √[p(1-p)/n]", "Distribution approximately normal"], examples: [{question: "35 out of 100 said yes", answer: "p̂ = 0.35"}], tip: "💡 Sample proportion estimates population proportion" },
    10: { title: "Hypothesis Testing", band: "Advanced", description: "Basic hypothesis testing.", keyPoints: ["Null hypothesis H₀", "Test if sample unusual", "Compare proportions"], examples: [{question: "Test if proportion changed", answer: "Compare sample to claimed value"}], tip: "💡 Is the difference real or just chance?" },
    11: { title: "Comparing Proportions", band: "Advanced", description: "Compare two sample proportions.", keyPoints: ["Non-overlapping CIs suggest difference", "Overlapping may still differ", "Consider practical significance"], examples: [{question: "2024 vs 2023 proportions", answer: "Compare confidence intervals"}], tip: "💡 Check if confidence intervals overlap" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style inferential statistics.", keyPoints: ["All inference concepts", "Interpret in context", "Show all working"], examples: [{question: "Full LC OL statistics inference", answer: "Various"}], tip: "🏆 Inferential stats worth 210+ marks - growing importance!" }
};

const lcOlCoordLinesHelpContent = {
    1: { title: "Distance Formula", band: "Foundation", description: "Find distance between points.", keyPoints: ["|AB| = √[(x₂-x₁)² + (y₂-y₁)²]", "Based on Pythagoras", "Always positive"], examples: [{question: "(1, 2) to (4, 6)", answer: "|AB| = √(9 + 16) = 5"}], tip: "💡 Distance formula = Pythagoras in disguise" },
    2: { title: "Midpoint Formula", band: "Foundation", description: "Find midpoint of a segment.", keyPoints: ["M = ((x₁+x₂)/2, (y₁+y₂)/2)", "Average of coordinates", "Point exactly in middle"], examples: [{question: "Midpoint of (2, 4) and (6, 8)", answer: "M = (4, 6)"}], tip: "💡 Add and divide by 2 for each coordinate" },
    3: { title: "Slope Calculation", band: "Foundation", description: "Calculate slope of a line.", keyPoints: ["m = (y₂-y₁)/(x₂-x₁)", "Rise over run", "Positive up, negative down"], examples: [{question: "Slope through (1, 2) and (3, 8)", answer: "m = 6/2 = 3"}], tip: "💡 Slope = change in y / change in x" },
    4: { title: "Equation y = mx + c", band: "Developing", description: "Write equation of a line.", keyPoints: ["m = slope, c = y-intercept", "Or use y - y₁ = m(x - x₁)", "Rearrange to form needed"], examples: [{question: "Slope 2, through (1, 5)", answer: "y - 5 = 2(x - 1), y = 2x + 3"}], tip: "💡 Point-slope form often easier to start" },
    5: { title: "Parallel Lines", band: "Developing", description: "Identify parallel lines.", keyPoints: ["Same slope means parallel", "Never intersect", "m₁ = m₂"], examples: [{question: "y = 3x + 1 and y = 3x - 4", answer: "Both slope 3, so parallel"}], tip: "💡 Parallel = same slope" },
    6: { title: "Perpendicular Lines", band: "Developing", description: "Identify perpendicular lines.", keyPoints: ["Slopes multiply to -1", "m₁ × m₂ = -1", "Negative reciprocals"], examples: [{question: "Line slope 2, perpendicular slope", answer: "-1/2 (negative reciprocal)"}], tip: "💡 Perpendicular: flip and negate" },
    7: { title: "Perpendicular Distance", band: "Proficient", description: "Distance from point to line.", keyPoints: ["d = |ax₁ + by₁ + c| / √(a² + b²)", "Line in form ax + by + c = 0", "Take absolute value"], examples: [{question: "Distance from (3, 4) to 3x + 4y - 5 = 0", answer: "d = |9 + 16 - 5|/5 = 4"}], tip: "💡 Put line in ax + by + c = 0 form first" },
    8: { title: "Intersection Points", band: "Proficient", description: "Find where lines meet.", keyPoints: ["Solve simultaneously", "Sub y from one into other", "Or use elimination"], examples: [{question: "y = 2x + 1 and y = -x + 7", answer: "2x + 1 = -x + 7, x = 2, y = 5"}], tip: "💡 Set equations equal and solve" },
    9: { title: "Dividing Segments", band: "Proficient", description: "Divide segment in given ratio.", keyPoints: ["Internal division formula", "Ratio m:n", "Weighted average"], examples: [{question: "Divide (1, 2) to (7, 8) in ratio 2:1", answer: "Point = (5, 6)"}], tip: "💡 Closer to which end depends on ratio" },
    10: { title: "Area of Triangle", band: "Advanced", description: "Find area from coordinates.", keyPoints: ["A = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)|", "Or base × height ÷ 2", "Shoelace formula"], examples: [{question: "Triangle vertices known", answer: "Apply area formula"}], tip: "💡 Use formula or find base and height" },
    11: { title: "Applied Problems", band: "Advanced", description: "Coordinate geometry in context.", keyPoints: ["Real-world applications", "Combine multiple concepts", "Clear diagram helps"], examples: [{question: "GPS coordinates problem", answer: "Apply appropriate formulae"}], tip: "💡 Draw diagram, label all points" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style coordinate geometry.", keyPoints: ["All coordinate geometry concepts", "Lines formulae", "Extended problems"], examples: [{question: "Full LC OL coord geometry lines", answer: "Various"}], tip: "🏆 Coord geometry lines worth 200 marks - know all formulae!" }
};

const lcOlCoordCirclesHelpContent = {
    1: { title: "Circle Equation", band: "Foundation", description: "Standard form of circle equation.", keyPoints: ["(x-h)² + (y-k)² = r²", "(h, k) = centre", "r = radius"], examples: [{question: "Centre (3, 4), radius 5", answer: "(x-3)² + (y-4)² = 25"}], tip: "💡 Signs flip: centre (3,4) gives (x-3) and (y-4)" },
    2: { title: "Centre & Radius", band: "Foundation", description: "Extract centre and radius from equation.", keyPoints: ["Read off (h, k) from equation", "r = √(number on right)", "Watch negative signs"], examples: [{question: "(x+2)² + (y-1)² = 16", answer: "Centre (-2, 1), radius 4"}], tip: "💡 (x+2) means h = -2" },
    3: { title: "Point on Circle", band: "Foundation", description: "Check if point lies on circle.", keyPoints: ["Substitute point into equation", "If LHS = RHS, point is on circle", "If <, inside; if >, outside"], examples: [{question: "Is (3, 4) on x² + y² = 25?", answer: "9 + 16 = 25 ✓ Yes!"}], tip: "💡 Sub in and check if equation balances" },
    4: { title: "General Form", band: "Developing", description: "Circle in general form.", keyPoints: ["x² + y² + 2gx + 2fy + c = 0", "Centre = (-g, -f)", "r = √(g² + f² - c)"], examples: [{question: "x² + y² - 6x + 4y - 12 = 0", answer: "g=-3, f=2, centre (3,-2)"}], tip: "💡 g and f have opposite signs to centre" },
    5: { title: "Converting Forms", band: "Developing", description: "Convert between circle forms.", keyPoints: ["Expand standard to get general", "Complete square to get standard", "Same circle, different forms"], examples: [{question: "x² + y² - 4x + 6y - 3 = 0", answer: "Complete square: (x-2)² + (y+3)² = 16"}], tip: "💡 Completing the square reveals centre" },
    6: { title: "Tangent to Circle", band: "Developing", description: "Line touching circle at one point.", keyPoints: ["Tangent perpendicular to radius", "At point of contact", "Use perpendicular slopes"], examples: [{question: "Tangent at (3, 4) to x² + y² = 25", answer: "Radius slope = 4/3, tangent slope = -3/4"}], tip: "💡 Tangent ⊥ radius at contact point" },
    7: { title: "Line & Circle", band: "Proficient", description: "Find where line meets circle.", keyPoints: ["Substitute line into circle equation", "Solve resulting quadratic", "0, 1, or 2 solutions"], examples: [{question: "y = x + 1 and x² + y² = 5", answer: "Sub: x² + (x+1)² = 5, solve"}], tip: "💡 2 points = intersects, 1 = tangent, 0 = misses" },
    8: { title: "External/Internal Points", band: "Proficient", description: "Determine point's position relative to circle.", keyPoints: ["Substitute into circle equation", "< r²: inside circle", "> r²: outside circle"], examples: [{question: "Is (1, 1) inside x² + y² = 9?", answer: "1 + 1 = 2 < 9, so inside"}], tip: "💡 Compare distance² to r²" },
    9: { title: "Tangent from Point", band: "Proficient", description: "Find tangent from external point.", keyPoints: ["Two tangents from external point", "Use perpendicular distance = r", "Or geometric approach"], examples: [{question: "Tangents from (5, 0) to x² + y² = 9", answer: "Distance formula and algebra"}], tip: "💡 Tangent length² = distance² - r²" },
    10: { title: "Touching Circles", band: "Advanced", description: "Circles that touch each other.", keyPoints: ["External touch: d = r₁ + r₂", "Internal touch: d = |r₁ - r₂|", "d = distance between centres"], examples: [{question: "When do circles touch?", answer: "Centre distance = sum or difference of radii"}], tip: "💡 Compare distance between centres to radii" },
    11: { title: "Circle Problems", band: "Advanced", description: "Complex circle problems.", keyPoints: ["Combine multiple concepts", "Find equations from conditions", "Real-world contexts"], examples: [{question: "Circle through 3 points", answer: "Set up 3 equations, solve"}], tip: "💡 Draw diagram, label everything" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style circle coordinate geometry.", keyPoints: ["All circle concepts", "Extended problems", "Show clear working"], examples: [{question: "Full LC OL coord circles", answer: "Various"}], tip: "🏆 Circle coord geom worth 200 marks!" }
};

const lcOlComplexHelpContent = {
    1: { title: "Introduction to i", band: "Foundation", description: "Understand the imaginary unit.", keyPoints: ["i = √(-1)", "i² = -1", "Allows √ of negatives"], examples: [{question: "√(-9)", answer: "√9 × √(-1) = 3i"}], tip: "💡 i² = -1 is the key fact" },
    2: { title: "Adding Complex", band: "Foundation", description: "Add complex numbers.", keyPoints: ["Add real parts together", "Add imaginary parts together", "(a + bi) + (c + di) = (a+c) + (b+d)i"], examples: [{question: "(3 + 2i) + (1 + 4i)", answer: "4 + 6i"}], tip: "💡 Real with real, imaginary with imaginary" },
    3: { title: "Subtracting Complex", band: "Foundation", description: "Subtract complex numbers.", keyPoints: ["Subtract real parts", "Subtract imaginary parts", "Watch negative signs"], examples: [{question: "(5 + 3i) - (2 + i)", answer: "3 + 2i"}], tip: "💡 Distribute the minus sign carefully" },
    4: { title: "Multiplying Complex", band: "Developing", description: "Multiply complex numbers.", keyPoints: ["FOIL method", "Remember i² = -1", "Simplify result"], examples: [{question: "(2 + 3i)(1 + i)", answer: "2 + 2i + 3i + 3i² = -1 + 5i"}], tip: "💡 FOIL then use i² = -1" },
    5: { title: "Conjugates", band: "Developing", description: "Find and use conjugates.", keyPoints: ["Conjugate of a + bi is a - bi", "Change sign of imaginary part", "z × z̄ = |z|²"], examples: [{question: "Conjugate of 3 - 4i", answer: "3 + 4i"}], tip: "💡 Flip the sign of the imaginary part" },
    6: { title: "Dividing Complex", band: "Developing", description: "Divide complex numbers.", keyPoints: ["Multiply by conjugate of denominator", "Top and bottom", "Simplify result"], examples: [{question: "(3 + i)/(1 - i)", answer: "Multiply by (1+i)/(1+i)"}], tip: "💡 Multiply top and bottom by conjugate of bottom" },
    7: { title: "Argand Diagram", band: "Proficient", description: "Plot complex numbers.", keyPoints: ["x-axis = Real", "y-axis = Imaginary", "Plot like coordinates"], examples: [{question: "Plot 3 + 2i", answer: "Point at (3, 2)"}], tip: "💡 Real along, imaginary up" },
    8: { title: "Modulus", band: "Proficient", description: "Find modulus of complex number.", keyPoints: ["|z| = √(a² + b²)", "Distance from origin", "Always positive"], examples: [{question: "|3 + 4i|", answer: "√(9 + 16) = 5"}], tip: "💡 Pythagoras from origin to point" },
    9: { title: "Solving Equations", band: "Proficient", description: "Solve equations with complex numbers.", keyPoints: ["Equate real and imaginary parts", "Use conjugate roots theorem", "Careful algebra"], examples: [{question: "(x + yi)(2 - i) = 7 + i", answer: "Expand, equate parts, solve"}], tip: "💡 Matching real and imaginary gives two equations" },
    10: { title: "Quadratic with Complex", band: "Advanced", description: "Solve quadratics with complex roots.", keyPoints: ["When discriminant < 0", "Roots are conjugates", "Use formula: (-b ± √(b²-4ac))/2a"], examples: [{question: "x² + 2x + 5 = 0", answer: "x = (-2 ± √(-16))/2 = -1 ± 2i"}], tip: "💡 Negative discriminant → complex roots" },
    11: { title: "Plotting & Interpreting", band: "Advanced", description: "Interpret Argand diagram features.", keyPoints: ["Addition = vector addition", "Modulus = distance", "Conjugate = reflection in x-axis"], examples: [{question: "What does |z - w| represent?", answer: "Distance between z and w"}], tip: "💡 Argand diagram gives geometric insight" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style complex numbers.", keyPoints: ["All complex number concepts", "Division in a + bi form", "Argand diagram work"], examples: [{question: "Full LC OL complex numbers", answer: "Various"}], tip: "🏆 Complex numbers worth 200 marks at OL!" }
};

const lcOlGeometryHelpContent = {
    1: { title: "Angle Properties", band: "Foundation", description: "Basic angle relationships.", keyPoints: ["Angles on line = 180°", "Angles at point = 360°", "Vertically opposite equal"], examples: [{question: "Angle x if x + 130° on a line", answer: "x = 50°"}], tip: "💡 Know the basic angle facts" },
    2: { title: "Triangle Properties", band: "Foundation", description: "Angle sum and types of triangles.", keyPoints: ["Angles sum to 180°", "Isosceles: 2 equal angles", "Equilateral: all 60°"], examples: [{question: "Triangle with 40°, 60°, find third", answer: "180 - 100 = 80°"}], tip: "💡 Triangle angles always add to 180°" },
    3: { title: "Parallel Lines", band: "Foundation", description: "Angles with parallel lines.", keyPoints: ["Alternate angles equal", "Corresponding angles equal", "Co-interior sum to 180°"], examples: [{question: "Alternate angles", answer: "Z-shape = equal"}], tip: "💡 F = corresponding, Z = alternate" },
    4: { title: "Constructions - Basics", band: "Developing", description: "Use compass and straight edge.", keyPoints: ["Compass for circles/arcs", "Ruler for straight lines", "No measuring angles"], examples: [{question: "Construct equilateral triangle", answer: "Two compass arcs, same radius"}], tip: "💡 Practice constructions - they appear every year" },
    5: { title: "Perpendicular Bisector", band: "Developing", description: "Construct perpendicular bisector.", keyPoints: ["Cuts line in half at 90°", "Equal arcs from both ends", "All points equidistant from endpoints"], examples: [{question: "Construct ⊥ bisector of AB", answer: "Arc from A, arc from B, join intersections"}], tip: "💡 Arcs same radius, cross above and below" },
    6: { title: "Angle Bisector", band: "Developing", description: "Construct angle bisector.", keyPoints: ["Divides angle in half", "Arc from vertex, then from arc points", "All points equidistant from arms"], examples: [{question: "Bisect angle of 80°", answer: "Arc from vertex, two equal arcs, join to vertex"}], tip: "💡 Creates two equal angles" },
    7: { title: "Enlargement", band: "Proficient", description: "Enlarge shapes from centre.", keyPoints: ["Scale factor k", "Distances from centre × k", "Angles unchanged"], examples: [{question: "Enlarge by factor 2 from O", answer: "All distances from O doubled"}], tip: "💡 Measure from centre, multiply, plot" },
    8: { title: "Centre of Enlargement", band: "Proficient", description: "Find centre of enlargement.", keyPoints: ["Join corresponding points", "Lines intersect at centre", "Work backwards from image"], examples: [{question: "Find centre from shape and image", answer: "Extend lines through corresponding points"}], tip: "💡 Corresponding points lie on lines through centre" },
    9: { title: "Incentre/Circumcentre", band: "Proficient", description: "Construct triangle centres.", keyPoints: ["Incentre: angle bisectors meet", "Circumcentre: ⊥ bisectors meet", "Both involve constructions"], examples: [{question: "Construct incentre", answer: "Bisect all three angles, they meet at incentre"}], tip: "💡 Incentre inside, circumcentre may be outside" },
    10: { title: "Centroid Construction", band: "Advanced", description: "Construct centroid of triangle.", keyPoints: ["Medians meet at centroid", "Median: vertex to midpoint of opposite side", "Centroid divides median 2:1"], examples: [{question: "Construct centroid", answer: "Find midpoints, draw medians, they meet at centroid"}], tip: "💡 Centroid = centre of mass (balancing point)" },
    11: { title: "Congruence Proofs", band: "Advanced", description: "Prove triangles congruent.", keyPoints: ["SSS, SAS, ASA, RHS", "State criteria used", "Give reasons for each step"], examples: [{question: "Prove △ABD ≅ △ACD", answer: "Show 3 matching parts with reasons"}], tip: "💡 State the congruence criterion clearly" },
    12: { title: "Mastery Challenge", band: "Advanced", description: "SEC exam-style geometry.", keyPoints: ["All geometry concepts", "Constructions with explanation", "Clear reasoning"], examples: [{question: "Full LC OL geometry", answer: "Various"}], tip: "🏆 Geometry/constructions appear every year - practice!" }
};

// ============================================================

        
        // Combined help content lookup - MUST be after all HelpContent definitions
        function getHelpContent(topic, level) {
            // Numeracy Strand
            if (topic === 'whole_numbers') {
                return wholeNumbersHelpContent[level];
            } else if (topic === 'addition_subtraction') {
                return additionSubtractionHelpContent[level];
            } else if (topic === 'multiplication_skills') {
                return multiplicationSkillsHelpContent[level];
            } else if (topic === 'division_skills') {
                return divisionSkillsHelpContent[level];
            } else if (topic === 'basic_fractions') {
                return basicFractionsHelpContent[level];
            } else if (topic === 'basic_decimals') {
                return basicDecimalsHelpContent[level];
            } else if (topic === 'basic_percentages') {
                return basicPercentagesHelpContent[level];
            } else if (topic === 'time_and_clocks') {
                return timeAndClocksHelpContent[level];
            } else if (topic === 'money_skills') {
                return moneySkillsHelpContent[level];
            } else if (topic === 'measurement') {
                return measurementHelpContent[level];
            } else if (topic === 'data_and_charts') {
                return dataAndChartsHelpContent[level];
            } else if (topic === 'number_patterns') {
                return numberPatternsHelpContent[level];
            // L1LP Strand
            } else if (topic === 'awareness_of_environment') {
                return awarenessOfEnvironmentHelpContent[level];
            } else if (topic === 'pattern_and_sequence') {
                return patternAndSequenceHelpContent[level];
            } else if (topic === 'developing_number_sense') {
                return developingNumberSenseHelpContent[level];
            } else if (topic === 'shape_and_space') {
                return shapeAndSpaceHelpContent[level];
            } else if (topic === 'measure_and_data') {
                return measureAndDataHelpContent[level];
            } else if (topic === 'time') {
                return l1lpTimeHelpContent[level];
            // L2LP Strand (NCCA-aligned)
            } else if (topic === 'l2_number_and_money') {
                return l2NumberAndMoneyHelpContent[level];
            } else if (topic === 'l2_time_management') {
                return l2TimeManagementHelpContent[level];
            } else if (topic === 'l2_measurement_location') {
                return l2MeasurementLocationHelpContent[level];
            } else if (topic === 'l2_shape_pattern_number') {
                return l2ShapePatternNumberHelpContent[level];
            // JC Exam Topics
            } else if (topic === 'arithmetic') {
                return arithmeticHelpContent[level];
            } else if (topic === 'fractions') {
                return adaptiveHelpContent[level];
            } else if (topic === 'percentages') {
                return percentagesHelpContent[level];
            } else if (topic === 'decimals') {
                return decimalsHelpContent[level];
            } else if (topic === 'ratio') {
                return ratioHelpContent[level];
            } else if (topic === 'sets') {
                return setsHelpContent[level];
            } else if (topic === 'descriptive_statistics') {
                return descriptiveStatisticsHelpContent[level];
            } else if (topic === 'patterns') {
                return patternsHelpContent[level];
            } else if (topic === 'functions') {
                return functionsHelpContent[level];
            } else if (topic === 'area_perimeter_volume') {
                return areaHelpContent[level];
            } else if (topic === 'solving_equations') {
                return solvingEquationsHelpContent[level];
            } else if (topic === 'simultaneous_equations') {
                return simultaneousEquationsHelpContent[level];
            } else if (topic === 'linear_inequalities') {
                return linearInequalitiesHelpContent[level];
            } else if (topic === 'introductory_algebra') {
                return introductoryAlgebraHelpContent[level];
            } else if (topic === 'applied_arithmetic') {
                return appliedArithmeticHelpContent[level];
            } else if (topic === 'currency') {
                return currencyHelpContent[level];
            } else if (topic === 'speed_distance_time') {
                return speedDistanceTimeHelpContent[level];
            } else if (topic === 'probability') {
                return probabilityHelpContent[level];
            } else if (topic === 'coordinate_geometry') {
                return coordinateGeometryHelpContent[level];
            } else if (topic === 'trigonometry') {
                return trigonometryHelpContent[level];
            } else if (topic === 'number_systems') {
                return numberSystemsHelpContent[level];
            } else if (topic === 'indices') {
                return indicesHelpContent[level];
            } else if (topic === 'geometry') {
                return geometryHelpContent[level];
            } else if (topic === 'simplifying_expressions') {
                return simplifyingExpressionsHelpContent[level];
            } else if (topic === 'expanding_factorising') {
                return expandingFactorisingHelpContent[level];
            // LC Higher Level Strand
            } else if (topic === 'lc_hl_calculus_diff') {
                return lcHlCalculusDiffHelpContent[level];
            } else if (topic === 'lc_hl_calculus_int') {
                return lcHlCalculusIntHelpContent[level];
            } else if (topic === 'lc_hl_algebra') {
                return lcHlAlgebraHelpContent[level];
            } else if (topic === 'lc_hl_sequences') {
                return lcHlSequencesHelpContent[level];
            } else if (topic === 'lc_hl_complex') {
                return lcHlComplexHelpContent[level];
            } else if (topic === 'lc_hl_functions') {
                return lcHlFunctionsHelpContent[level];
            } else if (topic === 'lc_hl_financial') {
                return lcHlFinancialHelpContent[level];
            } else if (topic === 'lc_hl_proof') {
                return lcHlProofHelpContent[level];
            } else if (topic === 'lc_hl_probability') {
                return lcHlProbabilityHelpContent[level];
            } else if (topic === 'lc_hl_statistics') {
                return lcHlStatisticsHelpContent[level];
            } else if (topic === 'lc_hl_coord_geom') {
                return lcHlCoordGeomHelpContent[level];
            } else if (topic === 'lc_hl_trigonometry') {
                return lcHlTrigonometryHelpContent[level];
            } else if (topic === 'lc_hl_geometry') {
                return lcHlGeometryHelpContent[level];
            } else if (topic === 'lc_hl_mensuration') {
                return lcHlMensurationHelpContent[level];
            } else if (topic === 'lc_hl_counting') {
                return lcHlCountingHelpContent[level];
            // LC Ordinary Level Strand
            } else if (topic === 'lc_ol_calculus') {
                return lcOlCalculusHelpContent[level];
            } else if (topic === 'lc_ol_financial') {
                return lcOlFinancialHelpContent[level];
            } else if (topic === 'lc_ol_trigonometry') {
                return lcOlTrigonometryHelpContent[level];
            } else if (topic === 'lc_ol_mensuration') {
                return lcOlMensurationHelpContent[level];
            } else if (topic === 'lc_ol_statistics_desc') {
                return lcOlStatisticsDescHelpContent[level];
            } else if (topic === 'lc_ol_probability') {
                return lcOlProbabilityHelpContent[level];
            } else if (topic === 'lc_ol_applied_measure') {
                return lcOlAppliedMeasureHelpContent[level];
            } else if (topic === 'lc_ol_sequences') {
                return lcOlSequencesHelpContent[level];
            } else if (topic === 'lc_ol_algebra') {
                return lcOlAlgebraHelpContent[level];
            } else if (topic === 'lc_ol_functions') {
                return lcOlFunctionsHelpContent[level];
            } else if (topic === 'lc_ol_statistics_inf') {
                return lcOlStatisticsInfHelpContent[level];
            } else if (topic === 'lc_ol_coord_lines') {
                return lcOlCoordLinesHelpContent[level];
            } else if (topic === 'lc_ol_coord_circles') {
                return lcOlCoordCirclesHelpContent[level];
            } else if (topic === 'lc_ol_complex') {
                return lcOlComplexHelpContent[level];
            } else if (topic === 'lc_ol_geometry') {
                return lcOlGeometryHelpContent[level];
            }
            // Default to fractions if topic not found
            return adaptiveHelpContent[level];
        }
        
        // Show help for current level
        function showAdaptiveHelp() {
            const level = adaptiveState.currentLevel || 1;
            const topic = adaptiveState.topic || 'fractions';
            const content = getHelpContent(topic, level);
            
            if (!content) return;
            
            // Stop the pulse animation when help is viewed
            const helpBtn = document.getElementById('adaptiveHelpBtn');
            if (helpBtn) helpBtn.classList.remove('help-btn-pulse');
            
            // Update header
            document.getElementById('helpLevelNumber').textContent = level;
            document.getElementById('helpLevelBand').textContent = content.band;
            document.getElementById('helpLevelTitle').textContent = content.title;
            
            // Build body content
            let html = `
                <div class="help-section">
                    <h3><i class="fas fa-info-circle"></i> What You'll Learn</h3>
                    <p>${content.description}</p>
                    <ul style="margin-top: 10px; padding-left: 20px; color: #4b5563;">
                        ${content.keyPoints.map(p => `<li style="margin: 8px 0; line-height: 1.5;">${p}</li>`).join('')}
                    </ul>
                </div>
                
                <div class="help-section">
                    <h3><i class="fas fa-pencil-alt"></i> Worked Example${content.examples.length > 1 ? 's' : ''}</h3>
            `;
            
            content.examples.forEach((ex, idx) => {
                html += `
                    <div class="worked-example">
                        <div class="example-question">${content.examples.length > 1 ? `Example ${idx + 1}: ` : ''}${ex.question}</div>
                        ${ex.visual ? `<div class="example-visual">${ex.visual}</div>` : ''}
                        ${ex.steps && ex.steps.length > 0 ? `
                        <div style="margin-top: 12px;">
                            ${ex.steps.map((step, i) => `
                                <div class="step">
                                    <span class="step-number">${i + 1}</span>
                                    <span>${step}</span>
                                </div>
                            `).join('')}
                        </div>
                        ` : ''}
                        <div class="answer">
                            <i class="fas fa-check-circle"></i>
                            ${ex.answer}
                        </div>
                    </div>
                `;
            });
            
            html += `
                </div>
                
                <div class="help-tip">
                    <span class="help-tip-icon">💡</span>
                    <span class="help-tip-text"><strong>Tip:</strong> ${content.tip}</span>
                </div>
                
                <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">
                    <button onclick="openTopicTutorial(); hideAdaptiveHelp();" style="background: linear-gradient(135deg, #ef4444, #dc2626); border: none; color: white; padding: 12px 24px; border-radius: 25px; cursor: pointer; font-size: 1rem; font-weight: 600; transition: all 0.2s; display: flex; align-items: center; gap: 8px; box-shadow: 0 4px 15px rgba(239, 68, 68, 0.3);">
                        <i class="fab fa-youtube"></i> Watch Video Tutorial
                    </button>
                    <button class="help-got-it-btn" onclick="hideAdaptiveHelp()">
                        <i class="fas fa-thumbs-up"></i> Got it! Let's go
                    </button>
                </div>
            `;
            
            document.getElementById('helpBodyContent').innerHTML = html;
            document.getElementById('adaptiveHelpModal').classList.add('show');
            
            // Mark that we've shown help for this level/topic combination
            if (level === 1 && adaptiveState.topic) {
                const helpKey = `adaptiveHelpShown_${adaptiveState.topic}_L1`;
                localStorage.setItem(helpKey, 'true');
            }
        }
        
        // Hide help modal
        function hideAdaptiveHelp() {
            document.getElementById('adaptiveHelpModal').classList.remove('show');
        }
        
        // Topic video URLs mapping (must match the one in renderStrands)
        const globalTopicVideoUrls = {
            'fractions': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5A3lQJK26JqkPC2HZPOb3-W',
            'percentages': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5A3lQJK26JqkPC2HZPOb3-W',
            'decimals': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5A3lQJK26JqkPC2HZPOb3-W',
            'ratio': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5A3EpPzrcebR5Y8q8K25hTl',
            'sets': 'https://www.khanacademy.org/math/statistics-probability/probability-library#basic-set-ops',
            'descriptive_statistics': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5D5BS80FWHE_mH6ZTtGU3iQ',
            'patterns': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5BGNGW5eVKndzk4BCdJE6kP',
            'functions': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5CGGxg3mH3nMpPnuEzW-jXh',
            'area_perimeter_volume': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5DtydLCjMby6JhKZmh-cbvh',
            'solving_equations': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5DMdiBiiGeTIkaht6MBhhnC',
            'simultaneous_equations': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5BflvNTYTtJski5eASSVFVt',
            'linear_inequalities': 'https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:inequalities-systems-graphs',
            'introductory_algebra': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5BTbgTCHTkwxUqfvg6MvNuJ',
            'applied_arithmetic': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5D4-Axux8PcJmZXB0Yv2gi1',
            'currency': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5D4-Axux8PcJmZXB0Yv2gi1',
            'speed_distance_time': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5A3EpPzrcebR5Y8q8K25hTl',
            'probability': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5ANrjJ0EEMzvxVKmnPNVYvf',
            'coordinate_geometry': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5Dao4OjSGe8msbPBQ0y74Lr',
            'trigonometry': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5DdtHcMLtodrdN7nr79GJIJ',
            'number_systems': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5CyhzaViGUSFc164691gd0G',
            'indices': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5CWmVgY_VVRmh_r_MJgE1uo',
            'geometry': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5AtD-gkOyQMtLjR2TPMrJkQ',
            'simplifying_expressions': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5BTbgTCHTkwxUqfvg6MvNuJ',
            'expanding_factorising': 'https://www.youtube.com/playlist?list=PL5KkMZvBpo5ATGZobbZgt78rXma1cidQB'
        };
        
        // Open tutorial video for current topic
        function openTopicTutorial() {
            const topic = adaptiveState.topic || 'fractions';
            const videoUrl = globalTopicVideoUrls[topic];
            
            if (videoUrl) {
                // Open in new tab
                window.open(videoUrl, '_blank');
            } else {
                // Fallback - search YouTube
                const searchTerm = topic.replace(/_/g, ' ');
                window.open(`https://www.youtube.com/results?search_query=eddie+woo+${encodeURIComponent(searchTerm)}`, '_blank');
            }
        }
        
        // Check if should auto-show help for Level 1
        function checkAutoShowHelp() {
            const helpBtn = document.getElementById('adaptiveHelpBtn');
            
            // At Level 1: add pulse animation to draw attention
            if (adaptiveState.currentLevel === 1) {
                if (helpBtn) helpBtn.classList.add('help-btn-pulse');
                
                // Auto-show help if never shown before for this topic
                const helpKey = `adaptiveHelpShown_${adaptiveState.topic}_L1`;
                if (!localStorage.getItem(helpKey)) {
                    setTimeout(() => {
                        showAdaptiveHelp();
                        localStorage.setItem(helpKey, 'true');
                    }, 800); // Delay so question loads first
                }
            } else {
                // Remove pulse for higher levels
                if (helpBtn) helpBtn.classList.remove('help-btn-pulse');
            }
        }
        
        // Update help button pulse based on level changes
        function updateHelpButtonState() {
            const helpBtn = document.getElementById('adaptiveHelpBtn');
            if (helpBtn) {
                if (adaptiveState.currentLevel === 1) {
                    helpBtn.classList.add('help-btn-pulse');
                } else {
                    helpBtn.classList.remove('help-btn-pulse');
                }
            }
        }
        
        function updateAdaptiveProgress() {
            const level = adaptiveState.currentLevel;
            const points = adaptiveState.currentPoints;
            const pointsRequired = getPointsRequired(level);
            const band = getAdaptiveBand(level);
            const bandNames = { beginner: 'Beginner', intermediate: 'Intermediate', advanced: 'Advanced', mastery: 'Mastery', application: 'Application', linked: 'Linked' };
            
            document.getElementById('adaptiveTopicTitle').textContent = adaptiveState.topicTitle;
            document.getElementById('adaptiveLevelNumber').textContent = level;
            document.getElementById('adaptiveLevelBand').textContent = bandNames[band] || band;
            
            if (level >= 12) {
                document.getElementById('adaptiveProgressText').innerHTML = '🏆 Complete Mastery! <button onclick="finishAdaptiveTopic()" style="margin-left: 10px; padding: 4px 12px; background: #10b981; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 0.85rem;">Finish Topic</button>';
                document.getElementById('adaptiveProgressBar').style.width = '100%';
            } else if (level >= 10) {
                const nextLevel = level + 1;
                document.getElementById('adaptiveProgressText').textContent = `🎯 ${points}/${pointsRequired} to Level ${nextLevel}`;
                document.getElementById('adaptiveProgressBar').style.width = `${(points / pointsRequired) * 100}%`;
            } else {
                const nextLevel = level + 1;
                document.getElementById('adaptiveProgressText').textContent = `${points}/${pointsRequired} to Level ${nextLevel}`;
                document.getElementById('adaptiveProgressBar').style.width = `${(points / pointsRequired) * 100}%`;
            }
            
            // Update Level Progress Pie Chart
            updateLevelProgressPie(level);
        }
        
        // Update the level progress pie chart (shows levels 1-12 completion)
        function updateLevelProgressPie(currentLevel) {
            const circle = document.getElementById('levelProgressCircle');
            const pieText = document.getElementById('levelPieText');
            const pieSubtext = document.getElementById('levelPieSubtext');
            
            if (!circle) return;
            
            // Calculate percentage (level 1 = 8.33%, level 12 = 100%)
            const percentage = (currentLevel / 12) * 100;
            
            // SVG circle dasharray for progress
            // circumference = 2 * PI * r = 2 * 3.14159 * 15.9 ≈ 100
            circle.setAttribute('stroke-dasharray', `${percentage} 100`);
            
            // Update text
            if (pieText) pieText.textContent = currentLevel;
            
            // Update subtext based on level
            if (pieSubtext) {
                if (currentLevel === 1) {
                    pieSubtext.textContent = 'Just started';
                } else if (currentLevel <= 3) {
                    pieSubtext.textContent = 'Beginner';
                } else if (currentLevel <= 6) {
                    pieSubtext.textContent = 'Intermediate';
                } else if (currentLevel <= 9) {
                    pieSubtext.textContent = 'Advanced';
                } else if (currentLevel <= 11) {
                    pieSubtext.textContent = 'Almost there!';
                } else {
                    pieSubtext.textContent = '🏆 Mastered!';
                }
            }
        }
        
        // Show/hide the top Next Question button
        function showTopNextButton(show) {
            const btn = document.getElementById('topNextQuestionBtn');
            if (btn) {
                btn.style.display = show ? 'block' : 'none';
            }
        }
        
        // Show/hide Dino Bonus notification in top bar
        function showDinoBonusNotification(show) {
            const notification = document.getElementById('dinoBonusNotification');
            if (notification) {
                notification.style.display = show ? 'block' : 'none';
            }
        }
        
        async function loadAdaptiveQuestion() {
            // Hide the top Next button when loading new question
            showTopNextButton(false);
            
            // Hide Dino Bonus notification (will show again if still available)
            showDinoBonusNotification(false);
            
            const questionContent = document.getElementById('adaptiveQuestionContent');
            questionContent.innerHTML = `
                <div style="text-align: center; padding: 40px;">
                    <i class="fas fa-spinner fa-spin" style="font-size: 2rem; color: #8b5cf6;"></i>
                    <p style="margin-top: 15px; color: #6b7280;">Loading question...</p>
                </div>
            `;
            
            try {
                // Build URL with excluded question IDs to prevent repeats
                let url = `/api/adaptive/question/${adaptiveState.topic}/${adaptiveState.currentLevel}`;
                if (adaptiveState.shownQuestionIds.length > 0) {
                    url += `?exclude=${adaptiveState.shownQuestionIds.join(',')}`;
                }
                
                console.log('🔍 Fetching adaptive question:', url);
                
                const response = await fetch(url);
                const question = await response.json();
                
                console.log('📦 API Response:', question);
                
                // Check for error response
                if (question.error) {
                    console.error('❌ API Error:', question.error);
                    questionContent.innerHTML = `
                        <div style="text-align: center; padding: 40px; color: #ef4444;">
                            <i class="fas fa-exclamation-triangle" style="font-size: 2rem;"></i>
                            <p style="margin-top: 15px;">No questions available for this level.</p>
                            <p style="color: #666; font-size: 0.9rem;">${question.error}</p>
                            <button onclick="loadAdaptiveQuestion()" style="margin-top: 15px; padding: 10px 20px; background: #8b5cf6; color: white; border: none; border-radius: 8px; cursor: pointer;">
                                Try Again
                            </button>
                        </div>
                    `;
                    return;
                }
                
                // Validate question has required fields
                if (!question.question_text || !question.option_a) {
                    console.error('❌ Invalid question data:', question);
                    questionContent.innerHTML = `
                        <div style="text-align: center; padding: 40px; color: #ef4444;">
                            <i class="fas fa-exclamation-triangle" style="font-size: 2rem;"></i>
                            <p style="margin-top: 15px;">Question data is invalid.</p>
                            <button onclick="loadAdaptiveQuestion()" style="margin-top: 15px; padding: 10px 20px; background: #8b5cf6; color: white; border: none; border-radius: 8px; cursor: pointer;">
                                Try Again
                            </button>
                        </div>
                    `;
                    return;
                }
                
                // Track this question to avoid repeats
                if (question.id) {
                    adaptiveState.shownQuestionIds.push(question.id);
                }
                
                adaptiveState.questionStartTime = Date.now();
                displayAdaptiveQuestion(question);
            } catch (error) {
                console.error('Error loading adaptive question:', error);
                questionContent.innerHTML = `
                    <div style="text-align: center; padding: 40px; color: #ef4444;">
                        <i class="fas fa-exclamation-triangle" style="font-size: 2rem;"></i>
                        <p style="margin-top: 15px;">Error loading question. Please try again.</p>
                        <button onclick="loadAdaptiveQuestion()" style="margin-top: 15px; padding: 10px 20px; background: #8b5cf6; color: white; border: none; border-radius: 8px; cursor: pointer;">
                            Retry
                        </button>
                    </div>
                `;
            }
        }
        
        function displayAdaptiveQuestion(question) {
            const questionContent = document.getElementById('adaptiveQuestionContent');
            
            // Store current question for flagging
            adaptiveState.currentQuestion = question;
            
            // Check for visual question (SVG) - V2.92 increased size for frequency tables/stem-leaf diagrams
            const visualHtml = question.image_svg ? `<div style="margin: 20px 0; text-align: center; overflow: visible;"><div style="max-width: 320px; margin: 0 auto; overflow: visible;">${question.image_svg}</div></div>` : '';
            
            questionContent.innerHTML = `
                <div class="adaptive-question">
                    <h3 style="font-size: 1.2rem; color: #1f2937; margin-bottom: 20px; line-height: 1.5;">${question.question_text}</h3>
                    ${visualHtml}
                    <div class="adaptive-options" style="display: grid; gap: 12px; margin-top: 20px;">
                        <button class="adaptive-option-btn" onclick="submitAdaptiveAnswerBeta('A', '${question.correct_answer}')" style="padding: 15px 20px; border: 2px solid #e5e7eb; border-radius: 12px; background: white; text-align: left; cursor: pointer; font-size: 1rem; transition: all 0.2s;">
                            <span style="font-weight: 600; color: #8b5cf6; margin-right: 10px;">A.</span> ${question.option_a}
                        </button>
                        <button class="adaptive-option-btn" onclick="submitAdaptiveAnswerBeta('B', '${question.correct_answer}')" style="padding: 15px 20px; border: 2px solid #e5e7eb; border-radius: 12px; background: white; text-align: left; cursor: pointer; font-size: 1rem; transition: all 0.2s;">
                            <span style="font-weight: 600; color: #8b5cf6; margin-right: 10px;">B.</span> ${question.option_b}
                        </button>
                        <button class="adaptive-option-btn" onclick="submitAdaptiveAnswerBeta('C', '${question.correct_answer}')" style="padding: 15px 20px; border: 2px solid #e5e7eb; border-radius: 12px; background: white; text-align: left; cursor: pointer; font-size: 1rem; transition: all 0.2s;">
                            <span style="font-weight: 600; color: #8b5cf6; margin-right: 10px;">C.</span> ${question.option_c}
                        </button>
                        <button class="adaptive-option-btn" onclick="submitAdaptiveAnswerBeta('D', '${question.correct_answer}')" style="padding: 15px 20px; border: 2px solid #e5e7eb; border-radius: 12px; background: white; text-align: left; cursor: pointer; font-size: 1rem; transition: all 0.2s;">
                            <span style="font-weight: 600; color: #8b5cf6; margin-right: 10px;">D.</span> ${question.option_d}
                        </button>
                    </div>
                    <!-- Report Question Button -->
                    <div style="margin-top: 20px; text-align: center;">
                        <button onclick="showAdaptiveFlagModal()" style="background: none; border: none; color: #9ca3af; font-size: 0.85rem; cursor: pointer; padding: 8px 16px; transition: color 0.2s;" onmouseover="this.style.color='#ef4444'" onmouseout="this.style.color='#9ca3af'">
                            <i class="fas fa-flag" style="margin-right: 6px;"></i>Report an issue with this question
                        </button>
                    </div>
                </div>
            `;
            
            // Add hover effects
            document.querySelectorAll('.adaptive-option-btn').forEach(btn => {
                btn.onmouseenter = () => { btn.style.borderColor = '#8b5cf6'; btn.style.background = '#f5f3ff'; };
                btn.onmouseleave = () => { btn.style.borderColor = '#e5e7eb'; btn.style.background = 'white'; };
            });
        }
        
        // ==================== ADAPTIVE QUESTION FLAGGING ====================
        
        function showAdaptiveFlagModal() {
            const question = adaptiveState.currentQuestion;
            if (!question) {
                alert('No question to report');
                return;
            }
            
            // Use the existing flag modal but with adaptive handler
            document.getElementById('flagQuestionText').textContent = question.question_text;
            document.getElementById('flagQuestionModal').classList.remove('hidden');
            document.getElementById('flagQuestionModal').classList.add('flex');
            document.getElementById('flagForm').reset();
            
            // Mark that we're flagging an adaptive question
            window.currentAdaptiveFlagQuestion = question;
        }
        
        async function submitAdaptiveAnswerBeta(selected, correct) {
            const timeTaken = (Date.now() - adaptiveState.questionStartTime) / 1000;
            
            // Normalize correct answer to uppercase letter
            // Database might store: 0/1/2/3, 'a'/'b'/'c'/'d', or 'A'/'B'/'C'/'D'
            let normalizedCorrect = correct;
            if (typeof correct === 'number' || /^[0-3]$/.test(correct)) {
                const index = parseInt(correct);
                normalizedCorrect = ['A', 'B', 'C', 'D'][index];
            } else if (typeof correct === 'string') {
                normalizedCorrect = correct.toUpperCase();
            }
            
            console.log('Answer check:', { selected, correct, normalizedCorrect });
            
            const isCorrect = selected === normalizedCorrect;
            const fastThreshold = getFastThreshold(adaptiveState.currentLevel);
            const isFast = timeTaken < fastThreshold;
            
            // Update stats
            adaptiveState.questionsAnswered++;
            
            // Track clock challenge questions (Rev 3.0)
            if (adaptiveState.clockMode) {
                adaptiveState.clockQuestionsAnswered++;
            }
            
            // Disable buttons
            document.querySelectorAll('.adaptive-option-btn').forEach(btn => {
                btn.disabled = true;
                btn.style.cursor = 'default';
            });
            
            // Show correct/incorrect styling
            document.querySelectorAll('.adaptive-option-btn').forEach(btn => {
                const optionLetter = btn.textContent.trim().charAt(0);
                if (optionLetter === normalizedCorrect) {
                    btn.style.background = '#dcfce7';
                    btn.style.borderColor = '#22c55e';
                }
                if (optionLetter === selected && !isCorrect) {
                    btn.style.background = '#fee2e2';
                    btn.style.borderColor = '#ef4444';
                }
            });
            
            // Calculate LEVEL progression points (for leveling up)
            let levelPointsEarned = 0;
            
            // Calculate REAL points to award (for Prize Shop)
            let realPointsEarned = 0;
            const band = getAdaptiveBand(adaptiveState.currentLevel);
            const pointConfig = ADAPTIVE_POINTS[band] || ADAPTIVE_POINTS.beginner;
            
            if (isCorrect) {
                // Level progression points
                levelPointsEarned = isFast ? 2 : 1;
                adaptiveState.currentPoints += levelPointsEarned;
                
                // Real points to award
                realPointsEarned = pointConfig.base;
                if (isFast) {
                    realPointsEarned += pointConfig.fast;
                }
                
                // Update session streak
                adaptiveState.sessionStreak++;
                adaptiveState.correctAnswers++;
                adaptiveState.sessionPointsEarned += realPointsEarned;
                
                // Track clock challenge correct answer (Rev 3.0)
                if (adaptiveState.clockMode) {
                    adaptiveState.clockQuestionsCorrect++;
                }
                
                // Play correct sound
                if (typeof playSound === 'function') {
                    playSound('correct');
                }
                
                // Streak milestone sounds
                if (typeof playSound === 'function') {
                    if (adaptiveState.sessionStreak === 3) playSound('streak3');
                    else if (adaptiveState.sessionStreak === 5) playSound('streak5');
                    else if (adaptiveState.sessionStreak === 10) playSound('streak10');
                }
                
                // Who Am I - reveal tile (check BOTH global and adaptiveState for compatibility)
                const whoAmIActive = whoAmIEnabled || adaptiveState.whoAmIEnabled;
                console.log('🎭 ADAPTIVE: Checking Who Am I reveal...');
                console.log('   - global whoAmIEnabled:', whoAmIEnabled);
                console.log('   - adaptiveState.whoAmIEnabled:', adaptiveState.whoAmIEnabled);
                console.log('   - typeof onCorrectAnswer:', typeof onCorrectAnswer);
                
                if (whoAmIActive && typeof onCorrectAnswer === 'function') {
                    console.log('🎭 ADAPTIVE: Calling onCorrectAnswer()');
                    onCorrectAnswer();
                } else {
                    console.log('🎭 ADAPTIVE: NOT calling onCorrectAnswer (disabled or function missing)');
                }
                
                // Award real points to user account and update header display
                try {
                    const pointsResponse = await fetch('/api/award-points', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            points: realPointsEarned,
                            source: 'adaptive_quiz',
                            topic: adaptiveState.topic,
                            level: adaptiveState.currentLevel
                        })
                    });
                    
                    // Update header points display in real-time (Rev 2.92 fix)
                    if (pointsResponse.ok) {
                        const pointsData = await pointsResponse.json();
                        if (pointsData.total_points !== undefined) {
                            const statPointsEl = document.getElementById('stat-points');
                            if (statPointsEl) {
                                statPointsEl.textContent = pointsData.total_points;
                                // Brief highlight animation
                                statPointsEl.style.transition = 'transform 0.2s, color 0.2s';
                                statPointsEl.style.transform = 'scale(1.2)';
                                statPointsEl.style.color = '#22c55e';
                                setTimeout(() => {
                                    statPointsEl.style.transform = 'scale(1)';
                                    statPointsEl.style.color = '';
                                }, 300);
                            }
                        }
                    }
                } catch (error) {
                    console.log('Could not award points:', error);
                }
                
            } else {
                // Wrong answer
                adaptiveState.currentPoints = 0; // Reset level progress
                adaptiveState.sessionStreak = 0; // Reset streak
                
                // Clock Challenge penalty (Rev 3.0)
                if (adaptiveState.clockMode) {
                    applyClockPenalty();
                }
                
                // Play incorrect sound
                if (typeof playSound === 'function') {
                    playSound('incorrect');
                }
            }
            
            // Update streak display
            updateAdaptiveStreakDisplay();
            
            // Update points display
            document.getElementById('adaptiveSessionPoints').textContent = adaptiveState.sessionPointsEarned;
            
            // Check for level up
            const pointsRequired = getPointsRequired(adaptiveState.currentLevel);
            let leveledUp = false;
            
            if (isCorrect && adaptiveState.currentPoints >= pointsRequired && adaptiveState.currentLevel < 12) {
                const previousLevel = adaptiveState.currentLevel; // Store before incrementing
                adaptiveState.currentLevel++;
                adaptiveState.currentPoints = 0;
                leveledUp = true;
                
                console.log('📈 Level up! Previous:', previousLevel, 'New:', adaptiveState.currentLevel);
                
                // Update help button (remove pulse when leaving Level 1)
                updateHelpButtonState();
                
                // Clock Challenge: Success if leveled up while in clock mode! (Rev 3.0)
                if (adaptiveState.clockMode) {
                    // They completed the level in clock mode!
                    clockSuccess();
                    return; // Don't show normal feedback, clockSuccess handles it
                }
                
                // Unlock Clock Challenge for the level just completed (Rev 3.0.8)
                // This re-enables Clock Challenge if they previously timed out
                if (previousLevel >= 6 && previousLevel <= 10) {
                    unlockClockChallenge(previousLevel);
                }
                
                // First time reaching Level 6 - show intro modal (Rev 3.0)
                if (adaptiveState.currentLevel === 6) {
                    checkAndShowClockIntro();
                }
            }
            
            // Save progress to server
            try {
                await fetch('/api/adaptive/save-progress', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        topic: adaptiveState.topic,
                        current_level: adaptiveState.currentLevel,
                        current_points: adaptiveState.currentPoints
                    })
                });
            } catch (error) {
                console.log('Could not save progress:', error);
            }
            
            // Show feedback
            showAdaptiveFeedbackBeta(isCorrect, isFast, levelPointsEarned, realPointsEarned, leveledUp, timeTaken);
            
            // Update progress display
            updateAdaptiveProgress();
            
            // Check for Dino Bonus unlock (after streak of 5)
            if (isCorrect && adaptiveState.sessionStreak === 5) {
                checkAdaptiveDinoBonusUnlock();
            }
        }
        
        // Update adaptive streak display with visual styling
        function updateAdaptiveStreakDisplay() {
            const streak = adaptiveState.sessionStreak;
            const display = document.getElementById('adaptiveStreakDisplay');
            const countEl = document.getElementById('adaptiveStreakCount');
            
            if (!display || !countEl) return;
            
            countEl.textContent = streak;
            
            // Remove all streak classes
            display.classList.remove('streak-cold', 'streak-warming', 'streak-hot', 'streak-fire', 'streak-legendary');
            
            // Add appropriate class based on streak
            if (streak === 0) {
                display.classList.add('streak-cold');
                display.style.background = 'rgba(255,255,255,0.1)';
            } else if (streak < 3) {
                display.classList.add('streak-warming');
                display.style.background = 'rgba(251,191,36,0.3)';
            } else if (streak < 5) {
                display.classList.add('streak-hot');
                display.style.background = 'rgba(249,115,22,0.4)';
            } else if (streak < 10) {
                display.classList.add('streak-fire');
                display.style.background = 'rgba(239,68,68,0.5)';
            } else {
                display.classList.add('streak-legendary');
                display.style.background = 'linear-gradient(90deg, rgba(239,68,68,0.6), rgba(168,85,247,0.6))';
            }
        }
        
        // Check for Dino Bonus unlock
        function checkAdaptiveDinoBonusUnlock() {
            const dinoBonusUnlock = document.getElementById('adaptive-dino-bonus-unlock');
            if (dinoBonusUnlock && typeof startBonusQuestion === 'function') {
                // Store info for bonus submission
                window.bonusQuizInfo = {
                    topic: adaptiveState.topic,
                    score: 100 // Treat streak of 5 as 100%
                };
                dinoBonusUnlock.style.display = 'block';
                
                // Show the notification in the top bar
                showDinoBonusNotification(true);
                
                console.log('🦕 Dino Bonus unlocked for 5 streak!');
            }
        }
        
        function showAdaptiveFeedbackBeta(isCorrect, isFast, levelPointsEarned, realPointsEarned, leveledUp, timeTaken) {
            // Show the top Next button for easy access
            showTopNextButton(true);
            
            // Show Dino Bonus notification if bonus card is visible
            const dinoBonusCard = document.getElementById('adaptive-dino-bonus-unlock');
            if (dinoBonusCard && dinoBonusCard.style.display !== 'none') {
                showDinoBonusNotification(true);
            }
            
            const feedback = document.getElementById('adaptiveFeedbackBeta');
            feedback.classList.remove('hidden');
            
            const streakMsg = adaptiveState.sessionStreak > 1 ? 
                `<span style="color: #f97316;">🔥 ${adaptiveState.sessionStreak} streak!</span>` : '';
            
            // Check if just reached Level 12 (Topic Mastery!)
            if (leveledUp && adaptiveState.currentLevel === 12) {
                feedback.style.background = 'linear-gradient(135deg, #fef3c7, #fbbf24, #f59e0b)';
                feedback.innerHTML = `
                    <div style="font-size: 4rem; margin-bottom: 15px;">🏆</div>
                    <h3 style="color: #92400e; font-size: 1.8rem; margin-bottom: 10px; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">TOPIC MASTERED!</h3>
                    <p style="color: #a16207; font-size: 1.2rem; margin-bottom: 5px;">Congratulations! You've completed all 12 levels!</p>
                    <p style="color: #16a34a; font-size: 1rem; margin-top: 10px;">💰 +${realPointsEarned} points ${streakMsg}</p>
                    <p style="color: #6b7280; font-size: 0.9rem; margin-top: 15px;">You can continue practicing or return to topics.</p>
                    <div style="display: flex; gap: 10px; justify-content: center; margin-top: 20px; flex-wrap: wrap;">
                        <button onclick="finishAdaptiveTopic()" style="padding: 12px 25px; background: #10b981; color: white; border: none; border-radius: 8px; cursor: pointer; font-size: 1rem; font-weight: 600;">
                            <i class="fas fa-check"></i> Finish Topic
                        </button>
                        <button onclick="continueAdaptiveQuizBeta()" style="padding: 12px 25px; background: #8b5cf6; color: white; border: none; border-radius: 8px; cursor: pointer; font-size: 1rem; font-weight: 600;">
                            Keep Practicing <i class="fas fa-arrow-right"></i>
                        </button>
                    </div>
                `;
            } else if (leveledUp) {
                // Check if clock challenge should be offered (L6-10, not currently in clock mode)
                const clockEligible = adaptiveState.currentLevel >= 6 && adaptiveState.currentLevel <= 10 && !adaptiveState.clockMode;
                console.log('🎉 Level Up! Current level:', adaptiveState.currentLevel, 'clockEligible:', clockEligible, 'clockMode:', adaptiveState.clockMode);
                
                feedback.style.background = 'linear-gradient(135deg, #fef3c7, #fde68a)';
                
                if (clockEligible) {
                    // Level 6-10: Offer clock challenge option (Rev 3.0)
                    feedback.innerHTML = `
                        <div style="font-size: 3rem; margin-bottom: 10px;">🎉</div>
                        <h3 style="color: #92400e; font-size: 1.5rem; margin-bottom: 10px;">LEVEL UP!</h3>
                        <p style="color: #a16207; font-size: 1.1rem;">You've reached Level ${adaptiveState.currentLevel}!</p>
                        <p style="color: #16a34a; font-size: 1rem; margin-top: 10px;">💰 +${realPointsEarned} points ${streakMsg}</p>
                        <div style="margin-top: 20px; display: flex; flex-direction: column; gap: 10px; align-items: center;">
                            <button onclick="offerClockChallenge()" style="padding: 12px 25px; background: linear-gradient(135deg, #1e1b4b, #312e81); color: white; border: none; border-radius: 8px; cursor: pointer; font-size: 1rem; font-weight: 600; display: flex; align-items: center; gap: 8px;">
                                ⏱️ Try Clock Challenge
                            </button>
                            <button onclick="continueAdaptiveQuizBeta()" style="padding: 10px 20px; background: rgba(139,92,246,0.2); color: #7c3aed; border: 2px solid #8b5cf6; border-radius: 8px; cursor: pointer; font-size: 0.9rem;">
                                Continue Normal Mode <i class="fas fa-arrow-right"></i>
                            </button>
                        </div>
                    `;
                } else {
                    // Standard level-up (L1-5 or L11-12)
                    feedback.innerHTML = `
                        <div style="font-size: 3rem; margin-bottom: 10px;">🎉</div>
                        <h3 style="color: #92400e; font-size: 1.5rem; margin-bottom: 10px;">LEVEL UP!</h3>
                        <p style="color: #a16207; font-size: 1.1rem;">You've reached Level ${adaptiveState.currentLevel}!</p>
                        <p style="color: #16a34a; font-size: 1rem; margin-top: 10px;">💰 +${realPointsEarned} points ${streakMsg}</p>
                        <button onclick="continueAdaptiveQuizBeta()" style="margin-top: 20px; padding: 12px 30px; background: #8b5cf6; color: white; border: none; border-radius: 8px; cursor: pointer; font-size: 1rem; font-weight: 600;">
                            Continue <i class="fas fa-arrow-right"></i>
                        </button>
                    `;
                }
            } else if (isCorrect) {
                const speedMsg = isFast ? 
                    `<span style="color: #f59e0b;"><i class="fas fa-bolt"></i> Speed Bonus!</span>` : '';
                const explanationHtml = adaptiveState.currentQuestion?.explanation ? 
                    `<div style="margin-top: 15px; padding: 12px 15px; background: rgba(255,255,255,0.7); border-radius: 10px; text-align: left; border-left: 4px solid #22c55e;">
                        <div style="font-weight: 600; color: #166534; font-size: 0.85rem; margin-bottom: 5px;"><i class="fas fa-lightbulb"></i> Explanation</div>
                        <div style="color: #374151; font-size: 0.9rem; line-height: 1.5;">${adaptiveState.currentQuestion.explanation}</div>
                    </div>` : '';
                feedback.style.background = 'linear-gradient(135deg, #dcfce7, #bbf7d0)';
                feedback.innerHTML = `
                    <div style="font-size: 2rem; margin-bottom: 10px;">✓</div>
                    <h3 style="color: #166534; font-size: 1.2rem; margin-bottom: 5px;">Correct!</h3>
                    <p style="color: #16a34a; font-size: 1rem;">💰 +${realPointsEarned} points ${speedMsg}</p>
                    <p style="color: #6b7280; font-size: 0.85rem; margin-top: 5px;">
                        +${levelPointsEarned} level progress • ${timeTaken.toFixed(1)}s ${streakMsg}
                    </p>
                    ${explanationHtml}
                    <button onclick="continueAdaptiveQuizBeta()" style="margin-top: 15px; padding: 10px 25px; background: #22c55e; color: white; border: none; border-radius: 8px; cursor: pointer; font-size: 0.95rem;">
                        Next Question <i class="fas fa-arrow-right"></i>
                    </button>
                `;
            } else {
                // Find the correct answer text
                const correctIndex = adaptiveState.currentQuestion?.correct_answer;
                const correctOptions = ['option_a', 'option_b', 'option_c', 'option_d'];
                const correctLetter = ['A', 'B', 'C', 'D'][correctIndex] || '?';
                const correctText = adaptiveState.currentQuestion?.[correctOptions[correctIndex]] || '';
                
                const explanationHtml = adaptiveState.currentQuestion?.explanation ? 
                    `<div style="margin-top: 15px; padding: 12px 15px; background: rgba(255,255,255,0.7); border-radius: 10px; text-align: left; border-left: 4px solid #f59e0b;">
                        <div style="font-weight: 600; color: #166534; font-size: 0.85rem; margin-bottom: 5px;">✓ Correct Answer: ${correctLetter}. ${correctText}</div>
                        <div style="font-weight: 600; color: #92400e; font-size: 0.85rem; margin-top: 10px; margin-bottom: 5px;"><i class="fas fa-lightbulb"></i> Explanation</div>
                        <div style="color: #374151; font-size: 0.9rem; line-height: 1.5;">${adaptiveState.currentQuestion.explanation}</div>
                    </div>` : 
                    `<div style="margin-top: 10px; padding: 10px 15px; background: rgba(255,255,255,0.5); border-radius: 8px;">
                        <div style="color: #166534; font-size: 0.9rem;">✓ Correct Answer: ${correctLetter}. ${correctText}</div>
                    </div>`;
                
                feedback.style.background = 'linear-gradient(135deg, #fee2e2, #fecaca)';
                feedback.innerHTML = `
                    <div style="font-size: 2rem; margin-bottom: 10px;">✗</div>
                    <h3 style="color: #991b1b; font-size: 1.2rem; margin-bottom: 5px;">Not quite</h3>
                    <p style="color: #b91c1c; font-size: 0.95rem;">Progress reset - keep going!</p>
                    ${explanationHtml}
                    <button onclick="continueAdaptiveQuizBeta()" style="margin-top: 15px; padding: 10px 25px; background: #8b5cf6; color: white; border: none; border-radius: 8px; cursor: pointer; font-size: 0.95rem;">
                        Try Again <i class="fas fa-arrow-right"></i>
                    </button>
                `;
            }
        }
        
        function continueAdaptiveQuizBeta() {
            document.getElementById('adaptiveFeedbackBeta').classList.add('hidden');
            loadAdaptiveQuestion();
        }
        
        async function exitAdaptiveQuizBeta() {
            // Stop clock challenge if active (Rev 3.0)
            if (adaptiveState.clockMode) {
                stopClockTimer();
                hideClockTimerUI();
                // Complete as timeout since they're exiting
                completeClockChallenge(false);
                adaptiveState.clockMode = false;
                adaptiveState.clockSessionId = null;
            }
            
            // Save progress before exiting
            try {
                await fetch('/api/adaptive/save-progress', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        topic: adaptiveState.topic,
                        current_level: adaptiveState.currentLevel,
                        current_points: adaptiveState.currentPoints
                    })
                });
            } catch (error) {
                console.log('Could not save progress:', error);
            }
            
            // Check if user came from passport and should return there
            const returnToPassport = sessionStorage.getItem('returnToPassport');
            if (returnToPassport === 'true') {
                sessionStorage.removeItem('returnToPassport');
                console.log('🎫 Returning to passport...');
                window.location.href = '/passport?synced=true';
                return;
            }
            
            // Update the topic card to reflect new level (Rev 2.92 fix)
            updateTopicCardLevel(adaptiveState.topic, adaptiveState.currentLevel);
            
            // Refresh stats panel to show updated points (Rev 2.93 fix)
            refreshStatsPanel();
            
            adaptiveState.active = false;
            document.getElementById('adaptiveQuizScreenBeta').classList.add('hidden');
            document.getElementById('topicScreen').classList.remove('hidden');
        }
        
        // Helper function to update topic card level display (Rev 2.92)
        function updateTopicCardLevel(topic, level) {
            const topicCard = document.querySelector(`.unified-topic-card[data-topic="${topic}"]`);
            if (!topicCard) return;
            
            const levelText = topicCard.querySelector('.unified-level-text');
            const levelFill = topicCard.querySelector('.unified-level-fill');
            
            if (levelText) {
                if (level >= 12) {
                    levelText.textContent = '✓ Level 12';
                    levelText.classList.add('mastered');
                } else {
                    levelText.textContent = `Level ${level} of 12`;
                    levelText.classList.remove('mastered');
                }
            }
            
            if (levelFill) {
                const percent = Math.round((level / 12) * 100);
                levelFill.style.width = `${percent}%`;
                if (level >= 12) {
                    levelFill.classList.add('mastered');
                } else {
                    levelFill.classList.remove('mastered');
                }
            }
            
            console.log(`📊 Updated topic card for ${topic} to Level ${level}`);
        }
        
        // Helper function to refresh stats panel after quiz (Rev 2.93)
        async function refreshStatsPanel() {
            try {
                // Use correct endpoint (Rev 2.99 fix - was /api/badges, now /api/student/badges)
                const badgesResponse = await fetch('/api/student/badges');
                if (badgesResponse.ok) {
                    const badgesData = await badgesResponse.json();
                    
                    const statPointsEl = document.getElementById('stat-points');
                    const statLevelEl = document.getElementById('stat-level');
                    
                    if (statPointsEl && badgesData.total_points !== undefined) {
                        statPointsEl.textContent = badgesData.total_points;
                        // Brief highlight animation
                        statPointsEl.style.transition = 'transform 0.3s, color 0.3s';
                        statPointsEl.style.transform = 'scale(1.15)';
                        statPointsEl.style.color = '#22c55e';
                        setTimeout(() => {
                            statPointsEl.style.transform = 'scale(1)';
                            statPointsEl.style.color = '';
                        }, 400);
                    }
                    
                    if (statLevelEl && badgesData.level !== undefined) {
                        statLevelEl.textContent = badgesData.level;
                    }
                    
                    console.log('📊 Stats panel refreshed - Points:', badgesData.total_points, 'Level:', badgesData.level);
                }
            } catch (error) {
                console.log('Could not refresh stats panel:', error);
            }
        }
        
        // Finish topic with celebration (called when completing Level 12)
        async function finishAdaptiveTopic() {
            // Save final progress
            try {
                await fetch('/api/adaptive/save-progress', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        topic: adaptiveState.topic,
                        current_level: adaptiveState.currentLevel,
                        current_points: adaptiveState.currentPoints
                    })
                });
            } catch (error) {
                console.log('Could not save progress:', error);
            }
            
            // Update the topic card to reflect mastery (Rev 2.92 fix)
            updateTopicCardLevel(adaptiveState.topic, adaptiveState.currentLevel);
            
            // Refresh stats panel to show updated points (Rev 2.93 fix)
            refreshStatsPanel();
            
            adaptiveState.active = false;
            document.getElementById('adaptiveQuizScreenBeta').classList.add('hidden');
            document.getElementById('topicScreen').classList.remove('hidden');
            
            // Show a brief celebration toast
            showToast(`🏆 ${adaptiveState.topicTitle} Mastered! Great work!`, 'success', 4000);
        }
        
        async function confirmAdaptiveResetBeta() {
            if (confirm(`Are you sure? This will reset your ${adaptiveState.topicTitle} progress back to Level 1.`)) {
                // Call API to reset progress
                try {
                    await fetch('/api/adaptive/reset-progress', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ topic: adaptiveState.topic })
                    });
                } catch (error) {
                    console.log('Could not reset progress on server:', error);
                }
                
                adaptiveState.currentLevel = 1;
                adaptiveState.currentPoints = 0;
                adaptiveState.shownQuestionIds = []; // Clear shown questions
                currentStreak = 0;
                adaptiveState.sessionStreak = 0;
                document.getElementById('adaptiveStreakCount').textContent = '0';
                updateAdaptiveProgress();
                loadAdaptiveQuestion();
                
                // Update the topic card to reflect reset (Rev 2.92 fix)
                updateTopicCardLevel(adaptiveState.topic, 1);
                
                // Clear the help shown flag so it shows again after reset
                const helpKey = `adaptiveHelpShown_${adaptiveState.topic}_L1`;
                localStorage.removeItem(helpKey);
                
                // Show help popup after reset to Level 1
                setTimeout(() => {
                    showAdaptiveHelp();
                }, 600);
            }
        }
        // ===== END ADAPTIVE QUIZ SYSTEM =====

        async function startQuiz(difficulty) {
            currentDifficulty = difficulty;
            currentQuestionIndex = 0;
            score = 0;
            answered = false;
            startTime = Date.now();

            // Reset milestone tracking for new quiz
            consecutiveCorrect = 0;
            maxConsecutiveCorrect = 0;
            questionsAnsweredInQuiz = 0;
            shownMilestones.clear();
            totalMilestonePoints = 0;  // Reset milestone points
            
            // Reset streak tracking
            currentStreak = 0;
            hintUsedThisQuestion = false;
            
            // Reset hot streak display
            updateHotStreakDisplay(0);
            
            // RESET DINO BONUS: Hide any lingering Dino bonus UI from previous topic
            const dinoBonusUnlock = document.getElementById('dino-bonus-unlock');
            if (dinoBonusUnlock) {
                dinoBonusUnlock.style.display = 'none';
            }
            // Also reset adaptive Dino bonus if present
            const adaptiveDinoBonusUnlock = document.getElementById('adaptive-dino-bonus-unlock');
            if (adaptiveDinoBonusUnlock) {
                adaptiveDinoBonusUnlock.style.display = 'none';
            }
            if (typeof showDinoBonusNotification === 'function') {
                showDinoBonusNotification(false);
            }
            
            console.log('✅ Milestone and streak tracking reset for new quiz');
            
            // AVATAR: Store points before quiz for unlock detection (if function exists)
            if (typeof getPointsBeforeQuiz === 'function') {
                getPointsBeforeQuiz(); // Don't await - let it run in background
            }

            document.getElementById('difficultyScreen').classList.add('hidden');
            document.getElementById('loadingScreen').classList.remove('hidden');

            try {
                const response = await fetch(`/api/questions/${currentTopic}/${difficulty}`);
                questions = await response.json();

                document.getElementById('loadingScreen').classList.add('hidden');
                document.getElementById('quizScreen').classList.remove('hidden');
                
                // ===== ACTIVATE COMPACT QUIZ MODE =====
                document.body.classList.add('quiz-active');
                
                // Update compact header
                const topicDisplay = currentTopic.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
                document.getElementById('compactTopicTitle').textContent = topicDisplay;
                document.getElementById('compactQuestionBadge').textContent = `Q1/${questions.length}`;
                document.getElementById('compactScoreBadge').textContent = `Score: 0/${questions.length}`;
                document.getElementById('compactProgressBar').style.width = '0%';

                // Initialize calculator for quiz
                if (typeof initCalculator === 'function') {
                    initCalculator();
                }

                document.getElementById('quizTopicTitle').textContent = currentTopic.charAt(0).toUpperCase() + currentTopic.slice(1);
                document.getElementById('total').textContent = questions.length;
                document.getElementById('totalQuestions').textContent = questions.length;
                
                // Render avatar in quiz header (compact)
                const quizHeaderAvatar = document.getElementById('quiz-header-avatar');
                if (quizHeaderAvatar && typeof AvatarRenderer !== 'undefined' && window.currentAvatarConfig) {
                    AvatarRenderer.render(quizHeaderAvatar, window.currentAvatarConfig, 'small');
                }

                // Initialize tutorial system for ALL topics (shows splash screen on first visit, help button on subsequent)
                const tutorialTopics = [
                    'introductory_algebra', 'solving_equations', 'simplifying_expressions',
                    'expanding_factorising', 'functions', 'patterns', 'arithmetic',
                    'bodmas', 'fractions', 'decimals', 'multiplication_division',
                    'number_systems', 'surds', 'complex_numbers_intro', 'complex_numbers_expanded',
                    'descriptive_statistics', 'probability', 'sets'
                ];
                
                if (tutorialTopics.includes(currentTopic)) {
                    initTutorial(currentTopic, difficulty);
                }

                showQuestion();
                
                // WHO AM I: Enable for ALL topics (backend will check if images exist)
                whoAmIEnabled = true;  // Changed from checking specific topic
                if (whoAmIEnabled && typeof initializeWhoAmI === 'function') {
                    // Show the container
                    const container = document.getElementById('who-am-i-container');
                    if (container) {
                        container.style.display = 'block';
                        
                        // Create quiz attempt and initialize
                        fetch('/api/create-quiz-attempt', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({
                                topic: currentTopic,
                                difficulty: currentDifficulty
                            })
                        })
                        .then(response => response.json())
                        .then(data => {
                            if (data.quiz_attempt_id) {
                                currentQuizAttemptId = data.quiz_attempt_id;
                                initializeWhoAmI(currentTopic, currentDifficulty, currentQuizAttemptId);
                                console.log('✅ Who Am I initialized for quiz attempt:', currentQuizAttemptId);
                            }
                        })
                        .catch(error => console.error('Error creating quiz attempt:', error));
                    }
                } else {
                    // Hide container for non-Who Am I topics
                    const container = document.getElementById('who-am-i-container');
                    if (container) {
                        container.style.display = 'none';
                    }
                }
                
            } catch (error) {
                console.error('Error loading questions:', error);
                alert('Error loading questions. Please try again.');
                backToDifficulty();
            }
        }

        // Streak tracking for bonus points (currentStreak defined in Day 1 features above)
        // let currentStreak = 0;  // REMOVED - duplicate declaration
        let hintUsedThisQuestion = false;
        let currentHintPenalty = 50;

        function showQuestion() {
            const question = questions[currentQuestionIndex];
            answered = false;
            hintUsedThisQuestion = false;
            
            // ===== AUTO-SCROLL TO TOP =====
            window.scrollTo({ top: 0, behavior: 'smooth' });
            
            // ===== UPDATE COMPACT HEADER =====
            document.getElementById('compactQuestionBadge').textContent = `Q${currentQuestionIndex + 1}/${questions.length}`;
            document.getElementById('compactScoreBadge').textContent = `Score: ${score}/${questions.length}`;
            const progress = ((currentQuestionIndex + 1) / questions.length) * 100;
            document.getElementById('compactProgressBar').style.width = progress + '%';
            
            // Update streak badge in header (use new hot streak display)
            const streakBadge = document.getElementById('compactStreakBadge');
            if (streakBadge) {
                if (currentStreak >= 3) {
                    const multiplier = getStreakMultiplier();
                    streakBadge.innerHTML = `🔥 ${multiplier}x`;
                    streakBadge.classList.add('visible');
                } else {
                    streakBadge.classList.remove('visible');
                }
            }
            // Also update the new hot streak display
            if (typeof updateHotStreakDisplay === 'function') {
                updateHotStreakDisplay(currentStreak);
            }

            document.getElementById('questionText').innerHTML = question.question;
            document.getElementById('currentQuestion').textContent = currentQuestionIndex + 1;
            document.getElementById('score').textContent = score;

            document.getElementById('progressBar').style.width = progress + '%';

            // Handle question image
            const imageContainer = document.getElementById('questionImageContainer');
            const imageEl = document.getElementById('questionImage');
            const captionEl = document.getElementById('questionImageCaption');
            
            if (question.image_url) {
                imageEl.src = question.image_url;
                imageContainer.classList.remove('hidden');
                if (question.image_caption) {
                    captionEl.textContent = question.image_caption;
                    captionEl.classList.remove('hidden');
                } else {
                    captionEl.classList.add('hidden');
                }
            } else {
                imageContainer.classList.add('hidden');
            }

            // Handle hint - update compact header hint button
            const hintContainer = document.getElementById('hintContainer');
            const hintTextEl = document.getElementById('hintText');
            const compactHintBtn = document.getElementById('compactHintBtn');
            
            if (question.hint_text) {
                hintContainer.classList.remove('hidden');
                hintTextEl.classList.add('hidden');
                currentHintPenalty = question.hint_penalty || 50;
                document.getElementById('hintContent').textContent = question.hint_text;
                // Show hint button in compact header
                if (compactHintBtn) {
                    compactHintBtn.style.display = 'flex';
                    compactHintBtn.classList.remove('hint-used');
                    compactHintBtn.title = `Show Hint (-${currentHintPenalty}% points)`;
                }
            } else {
                hintContainer.classList.add('hidden');
                // Hide hint button in compact header
                if (compactHintBtn) {
                    compactHintBtn.style.display = 'none';
                }
            }

            // Update streak display (for compatibility)
            updateStreakDisplay();

            const optionsContainer = document.getElementById('optionsContainer');
            optionsContainer.innerHTML = '';

            // Add number line ONLY for arithmetic questions (addition/subtraction)
            // Do NOT show number line for complex numbers or other topics
            if (currentTopic === 'arithmetic') {
                const numberLineHtml = generateBlankNumberLine(question.question);
                if (numberLineHtml) {
                    const numberLineDiv = document.createElement('div');
                    numberLineDiv.innerHTML = numberLineHtml;
                    optionsContainer.appendChild(numberLineDiv);
                }
            }

            // Add answer options
            question.options.forEach((option, index) => {
                const button = document.createElement('button');
                button.className = 'w-full p-4 rounded-xl text-left text-lg font-medium transition-all bg-gray-50 hover:bg-purple-50 border-2 border-gray-200 hover:border-purple-300 text-gray-800';
                button.textContent = option;
                button.onclick = () => handleAnswer(index);
                optionsContainer.appendChild(button);
            });

            // Add flag button
            const flagButton = document.createElement('button');
            flagButton.className = 'w-full mt-4 p-3 rounded-lg text-center text-sm font-medium bg-gray-100 hover:bg-gray-200 text-gray-700 transition-all';
            flagButton.innerHTML = '<i class="fas fa-flag mr-2"></i>Report an issue with this question';
            flagButton.onclick = () => showFlagQuestionModal(question.id);
            optionsContainer.appendChild(flagButton);

            // ===== HIDE FEEDBACK ROW =====
            document.getElementById('feedbackNextRow').classList.add('hidden');
            document.getElementById('explanationSection').classList.add('hidden');
            document.getElementById('feedbackContainer').classList.add('hidden');
            document.getElementById('nextButton').classList.add('hidden');
        }

        // ==================== HINT SYSTEM ====================
        function showHint() {
            if (hintUsedThisQuestion) return;
            hintUsedThisQuestion = true;
            
            document.getElementById('hintText').classList.remove('hidden');
            
            // Update compact header hint button
            const compactHintBtn = document.getElementById('compactHintBtn');
            if (compactHintBtn) {
                compactHintBtn.classList.add('hint-used');
                compactHintBtn.title = 'Hint shown';
            }
        }

        // ==================== STREAK DISPLAY ====================
        function updateStreakDisplay() {
            const streakDisplay = document.getElementById('streakDisplay');
            const streakEmoji = document.getElementById('streakEmoji');
            const streakText = document.getElementById('streakText');
            const streakMultiplier = document.getElementById('streakMultiplier');
            
            if (currentStreak >= 3) {
                streakDisplay.classList.remove('hidden');
                
                // Set emoji based on streak length
                if (currentStreak >= 10) {
                    streakEmoji.textContent = '🌟';
                } else if (currentStreak >= 7) {
                    streakEmoji.textContent = '💥';
                } else if (currentStreak >= 5) {
                    streakEmoji.textContent = '🔥🔥';
                } else {
                    streakEmoji.textContent = '🔥';
                }
                
                streakText.textContent = `${currentStreak} in a row!`;
                
                // Calculate and display multiplier
                const multiplier = getStreakMultiplier();
                streakMultiplier.textContent = `${multiplier}x`;
            } else {
                streakDisplay.classList.add('hidden');
            }
        }

        function getStreakMultiplier() {
            if (currentStreak >= 10) return 2.5;
            if (currentStreak >= 7) return 2.0;
            if (currentStreak >= 5) return 1.75;
            if (currentStreak >= 3) return 1.5;
            return 1.0;
        }

        function calculateQuestionPoints(isCorrect) {
            if (!isCorrect) return 0;
            
            let basePoints = 10; // Base points per correct answer
            
            // Apply hint penalty
            if (hintUsedThisQuestion) {
                basePoints = Math.floor(basePoints * (1 - currentHintPenalty / 100));
            }
            
            // Apply streak multiplier
            const multiplier = getStreakMultiplier();
            const totalPoints = Math.floor(basePoints * multiplier);
            
            return totalPoints;
        }

        function handleAnswer(selectedIndex) {
            if (answered) return;
            answered = true;

            const question = questions[currentQuestionIndex];
            const correct = selectedIndex === question.correct;

            // Track answer for milestone detection
            questionsAnsweredInQuiz++;
            
            // Update streak tracking
            if (correct) {
                currentStreak++;
                consecutiveCorrect++;
                maxConsecutiveCorrect = Math.max(maxConsecutiveCorrect, consecutiveCorrect);
                console.log(`✅ Correct! Streak: ${currentStreak}, Multiplier: ${getStreakMultiplier()}x`);
                
                // Play correct sound
                playSound('correct');
                
                // Update hot streak display
                updateHotStreakDisplay(currentStreak);
                
                // Check for "10 in a Row" milestone
                if (consecutiveCorrect === 10 && !shownMilestones.has('ten_streak')) {
                    shownMilestones.add('ten_streak');
                    setTimeout(() => {
                        showAchievementPopup({
                            icon: '🔥',
                            title: '10 in a Row!',
                            description: "Incredible! You've answered 10 questions correctly in a row!",
                            points: 50
                        });
                    }, 800);
                }
            } else {
                currentStreak = 0; // Reset streak on wrong answer
                consecutiveCorrect = 0;
                console.log(`❌ Incorrect. Streak reset.`);
                
                // Play incorrect sound
                playSound('incorrect');
                
                // Update hot streak display
                updateHotStreakDisplay(0);
            }

            // Check for "20 Questions Completed" milestone
            if (questionsAnsweredInQuiz === 20 && !shownMilestones.has('twenty_questions')) {
                shownMilestones.add('twenty_questions');
                setTimeout(() => {
                    showAchievementPopup({
                        icon: '🎯',
                        title: '20 Questions!',
                        description: "You've answered 20 questions! Keep up the excellent work!",
                        points: 30
                    });
                }, 800);
            }

            if (correct) {
                score++;
                document.getElementById('score').textContent = score;
                
                // WHO AM I: Reveal tile on correct answer
                if (whoAmIEnabled && typeof onCorrectAnswer === 'function') {
                    onCorrectAnswer();
                }
            }

            const allChildren = document.getElementById('optionsContainer').children;

            // CRITICAL FIX: Find the offset by checking if first child is number line
            // Number line div doesn't have onclick, buttons do
            let buttonOffset = 0;
            if (allChildren.length > 0 && !allChildren[0].onclick) {
                buttonOffset = 1; // First child is number line, so buttons start at index 1
            }

            // Calculate where option buttons end (before flag button)
            // There are always 4 option buttons, plus potentially 1 number line at start
            const optionButtonCount = 4;
            const optionButtonsEnd = buttonOffset + optionButtonCount;

            // Now loop through actual option buttons only (NOT the flag button at the end)
            for (let i = buttonOffset; i < optionButtonsEnd; i++) {
                const button = allChildren[i];
                const optionIndex = i - buttonOffset; // Convert container index to option index

                button.disabled = true;

                if (optionIndex === question.correct) {
                    button.className = 'w-full p-4 rounded-xl text-left text-lg font-medium bg-green-100 border-2 border-green-500 text-green-800';
                    button.innerHTML += ' <i class="fas fa-check float-right text-green-600"></i>';
                } else if (optionIndex === selectedIndex && !correct) {
                    button.className = 'w-full p-4 rounded-xl text-left text-lg font-medium bg-red-100 border-2 border-red-500 text-red-800';
                    button.innerHTML += ' <i class="fas fa-times float-right text-red-600"></i>';
                } else if (button.onclick) { // Only style actual option buttons
                    button.className = 'w-full p-4 rounded-xl text-left text-lg font-medium bg-gray-100 text-gray-600';
                }
            }

            // Keep the flag button enabled and clickable (it's the last child)
            // No need to disable it - students should be able to report issues after seeing the answer

            // Generate solution number line for arithmetic questions
            let solutionNumberLine = '';
            if (currentTopic === 'arithmetic') {
                solutionNumberLine = generateSolutionNumberLine(question.question) || '';
            }

            // Calculate bonus text for streak
            let streakBonus = '';
            if (correct && currentStreak >= 3) {
                const multiplier = getStreakMultiplier();
                streakBonus = `🔥 ${multiplier}x streak!`;
            }
            
            // Show hint penalty if used
            let hintPenalty = '';
            if (correct && hintUsedThisQuestion) {
                hintPenalty = `💡 -${currentHintPenalty}%`;
            }

            // ===== SHOW INLINE FEEDBACK ROW =====
            const feedbackRow = document.getElementById('feedbackNextRow');
            const feedbackInline = document.getElementById('feedbackInline');
            const feedbackIcon = feedbackInline.querySelector('.feedback-icon');
            const feedbackText = document.getElementById('feedbackText');
            const feedbackStreak = document.getElementById('feedbackStreak');
            
            // Update inline feedback
            if (correct) {
                feedbackInline.className = 'feedback-inline correct';
                feedbackIcon.textContent = '✅';
                feedbackText.className = 'feedback-text correct';
                feedbackText.textContent = 'Correct!';
            } else {
                feedbackInline.className = 'feedback-inline incorrect';
                feedbackIcon.textContent = '📖';
                feedbackText.className = 'feedback-text incorrect';
                feedbackText.textContent = 'Let\'s learn!';
            }
            
            // Show streak/hint info
            let bonusInfo = [streakBonus, hintPenalty].filter(x => x).join(' ');
            feedbackStreak.textContent = bonusInfo;
            
            feedbackRow.classList.remove('hidden');
            
            // ===== SHOW EXPLANATION SECTION =====
            const explanationSection = document.getElementById('explanationSection');
            const explanationContent = document.getElementById('explanationContent');
            
            if (question.explanation || solutionNumberLine) {
                explanationContent.innerHTML = `
                    <p>${question.explanation || ''}</p>
                    ${solutionNumberLine}
                `;
                explanationSection.classList.remove('hidden');
                // Auto-expand if incorrect
                if (!correct) {
                    explanationContent.classList.remove('hidden');
                    document.getElementById('explanationArrow').classList.add('fa-chevron-up');
                    document.getElementById('explanationArrow').classList.remove('fa-chevron-down');
                } else {
                    explanationContent.classList.add('hidden');
                    document.getElementById('explanationArrow').classList.remove('fa-chevron-up');
                    document.getElementById('explanationArrow').classList.add('fa-chevron-down');
                }
            } else {
                explanationSection.classList.add('hidden');
            }
            
            // Update compact header with new score
            document.getElementById('compactScoreBadge').textContent = `Score: ${score}/${questions.length}`;
            
            // Update streak badge (with null check for new UI)
            const streakBadge = document.getElementById('compactStreakBadge');
            if (streakBadge) {
                if (currentStreak >= 3) {
                    const multiplier = getStreakMultiplier();
                    streakBadge.innerHTML = `🔥 ${multiplier}x`;
                    streakBadge.classList.add('visible');
                } else {
                    streakBadge.classList.remove('visible');
                }
            }

            // Legacy feedback (hidden but kept for compatibility)
            const feedback = document.getElementById('feedbackContainer');
            feedback.innerHTML = '';
            document.getElementById('nextButton').classList.add('hidden');
        }
        
        // Toggle explanation visibility
        function toggleExplanation() {
            const content = document.getElementById('explanationContent');
            const arrow = document.getElementById('explanationArrow');
            content.classList.toggle('hidden');
            arrow.classList.toggle('fa-chevron-down');
            arrow.classList.toggle('fa-chevron-up');
        }

        function nextQuestion() {
            currentQuestionIndex++;
            if (currentQuestionIndex < questions.length) {
                showQuestion();
            } else {
                submitAndShowResults();
            }
        }

        function showGuestResultModal(score, total, percentage) {
            const performanceMessages = {
                100: { emoji: '🏆', title: 'Perfect Score!', message: 'Outstanding! You got every question right!' },
                90: { emoji: '⭐', title: 'Excellent Work!', message: 'You scored 90% or higher - fantastic!' },
                70: { emoji: '👍', title: 'Good Job!', message: 'You\'re doing well! Keep practicing!' },
                50: { emoji: '💪', title: 'Keep Trying!', message: 'You\'re learning! Practice makes perfect!' },
                0: { emoji: '📚', title: 'Room to Grow', message: 'Don\'t give up! Every expert was once a beginner.' }
            };

            const messageKey = Object.keys(performanceMessages)
                .map(Number)
                .reverse()
                .find(threshold => percentage >= threshold) || 0;
            
            const performance = performanceMessages[messageKey];

            const modal = document.createElement('div');
            modal.className = 'guest-result-overlay';
            modal.innerHTML = `
                <div class="guest-result-modal">
                    <div style="text-align: center;">
                        <div style="font-size: 64px; margin-bottom: 16px;">${performance.emoji}</div>
                        <h2>${performance.title}</h2>
                        <div class="score-display">${percentage}%</div>
                        <div class="message">${performance.message}</div>
                        <div class="message">You got <strong>${score} out of ${total}</strong> questions correct!</div>
                    </div>

                    <div class="benefits">
                        <h3>🌟 Create a free account to:</h3>
                        <ul>
                            <li>Save your quiz scores and progress</li>
                            <li>Earn badges and achievements</li>
                            <li>Track your learning journey</li>
                            <li>Compete on leaderboards</li>
                            <li>Get detailed performance analytics</li>
                        </ul>
                    </div>

                    <div class="button-group">
                        <a href="/register" class="primary-btn">Create Free Account</a>
                        <button onclick="closeGuestModal()" class="secondary-btn">Continue as Guest</button>
                    </div>
                </div>
            `;

            document.body.appendChild(modal);
            
            // Close modal when clicking outside
            modal.addEventListener('click', (e) => {
                if (e.target === modal) {
                    closeGuestModal();
                }
            });
        }

        function closeGuestModal() {
            const modal = document.querySelector('.guest-result-overlay');
            if (modal) {
                modal.remove();
            }
            backToTopics();
        }

        async function submitAndShowResults() {
            const percentage = Math.round((score / questions.length) * 100);
            const timeTaken = Math.floor((Date.now() - startTime) / 1000);

            // Check for quiz completion milestones (FOR ALL USERS including guests)
            const milestones = [];

            // Perfect Score
            if (percentage === 100 && !shownMilestones.has('perfect_score')) {
                milestones.push({
                    icon: '💯',
                    title: 'Perfect Score!',
                    description: 'Flawless! You got every single question correct!',
                    points: 100
                });
                shownMilestones.add('perfect_score');
            }

            // First Quiz (always show for first quiz of session)
            if (!shownMilestones.has('first_quiz')) {
                milestones.push({
                    icon: '🌟',
                    title: 'First Quiz Complete!',
                    description: 'Congratulations on completing your first quiz!',
                    points: 25
                });
                shownMilestones.add('first_quiz');
            }

            // Quick Learner (under 5 minutes with 80%+)
            const timeInMinutes = timeTaken / 60;
            if (timeInMinutes < 5 && percentage >= 80 && !shownMilestones.has('quick_learner')) {
                milestones.push({
                    icon: '⚡',
                    title: 'Quick Learner!',
                    description: 'Amazing! You completed this quiz in under 5 minutes with a great score!',
                    points: 40
                });
                shownMilestones.add('quick_learner');
            }

            // Show milestones if any were earned (with delays between multiple milestones)
            if (milestones.length > 0) {
                console.log('🎉 Quiz completion milestones earned:', milestones);
                for (let i = 0; i < milestones.length; i++) {
                    setTimeout(() => {
                        showAchievementPopup(milestones[i]);
                    }, i * 2500); // Show each milestone 2.5 seconds apart
                }
            }

            // WHO AM I: Get bonus points if enabled
            let whoAmIBonus = 0;
            if (whoAmIEnabled && typeof getWhoAmIBonusPoints === 'function') {
                whoAmIBonus = getWhoAmIBonusPoints();
                console.log('🎯 Who Am I bonus points to submit:', whoAmIBonus);
            }

            // Submit to backend
            try {
                console.log('📤 Submitting quiz with data:', {
                    topic: currentTopic,
                    difficulty: currentDifficulty,
                    score: score,
                    total_questions: questions.length,
                    percentage: percentage,
                    time_taken: timeTaken,
                    quiz_attempt_id: currentQuizAttemptId,
                    who_am_i_bonus: whoAmIBonus,
                    milestone_points: totalMilestonePoints  // Include milestone points!
                });
                
                const response = await fetch('/api/submit-quiz', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        topic: currentTopic,
                        difficulty: currentDifficulty,
                        score: score,
                        total_questions: questions.length,
                        percentage: percentage,
                        time_taken: timeTaken,
                        quiz_attempt_id: currentQuizAttemptId,
                        who_am_i_bonus: whoAmIBonus,
                        milestone_points: totalMilestonePoints  // Include milestone points!
                    })
                });

                console.log('📥 Submit quiz response status:', response.status);
                const result = await response.json();
                console.log('📥 Submit quiz result:', result);
                
                // Check if user is a guest
                if (result.is_guest || result.prompt_register) {
                    console.log('⚠️ User is guest - showing guest modal');
                    // Show guest modal with registration prompt
                    showGuestResultModal(score, questions.length, percentage);
                    return;
                }
                
                console.log('✅ Quiz submitted for registered user');
                
                // ✨ NEW: Show milestone celebration if badges were earned
                if (result.newly_earned_badges && result.newly_earned_badges.length > 0) {
                    console.log('🎉 Badges earned:', result.newly_earned_badges);
                    // Show milestone modal BEFORE results screen
                    showMilestoneModal(result.newly_earned_badges);
                    
                    // Wait a moment for user to see the celebration
                    // The user will click "Continue" to proceed
                } else {
                    console.log('No new badges earned this time');
                }
                
                // Regular user - reload progress and show results
                await loadProgress();
                await loadBadgeWidget();
                
            } catch (error) {
                console.error('Error submitting quiz:', error);
            }

            showResults(percentage);
        }

        function showResults(percentage) {
            // ===== DEACTIVATE QUIZ MODE =====
            document.body.classList.remove('quiz-active');
            
            document.getElementById('quizScreen').classList.add('hidden');
            document.getElementById('resultsScreen').classList.remove('hidden');

            document.getElementById('percentage').textContent = percentage + '%';
            document.getElementById('scoreText').textContent = `You scored ${score} out of ${questions.length}`;

            const messageEl = document.getElementById('performanceMessage');
            if (percentage === 100) {
                messageEl.className = 'text-xl text-green-600 font-semibold mb-6';
                messageEl.textContent = '🌟 Perfect score! Amazing work!';
            } else if (percentage >= 80) {
                messageEl.className = 'text-xl text-blue-600 font-semibold mb-6';
                messageEl.textContent = '🎉 Great job! You\'re really getting it!';
            } else if (percentage >= 60) {
                messageEl.className = 'text-xl text-orange-600 font-semibold mb-6';
                messageEl.textContent = '👍 Good effort! Keep practicing!';
            } else {
                messageEl.className = 'text-xl text-red-600 font-semibold mb-6';
                messageEl.textContent = '💪 Keep trying! Practice makes perfect!';
            }
            
            // WHO AM I: Show bonus if earned
            if (whoAmIEnabled && typeof getWhoAmIBonusPoints === 'function') {
                const whoAmIBonus = getWhoAmIBonusPoints();
                if (whoAmIBonus > 0) {
                    const bonusDisplay = document.getElementById('who-am-i-bonus-display');
                    const bonusPoints = document.getElementById('bonus-points-display');
                    if (bonusDisplay && bonusPoints) {
                        bonusPoints.textContent = whoAmIBonus;
                        bonusDisplay.style.display = 'block';
                    }
                }
            }
            
            // AVATAR: Check for new item unlocks after a delay to let points update
            if (typeof checkForNewUnlocks === 'function') {
                setTimeout(() => {
                    // Fetch updated points and check for unlocks
                    fetch('/api/avatar/inventory')
                        .then(r => r.json())
                        .then(data => {
                            if (data.points !== undefined) {
                                checkForNewUnlocks(data.points);
                            }
                        })
                        .catch(e => console.log('Could not check unlocks:', e));
                }, 1000); // Wait 1 second for points to update
            }
            
            // AVATAR: Hide the unlock banner initially (will show if items unlocked)
            const unlockBanner = document.getElementById('new-unlock-banner');
            if (unlockBanner) {
                unlockBanner.classList.add('hidden');
            }
            
            // DINO BONUS: Show unlock for 85%+ scores
            const dinoBonusUnlock = document.getElementById('dino-bonus-unlock');
            if (dinoBonusUnlock) {
                if (percentage >= 85) {
                    dinoBonusUnlock.style.display = 'block';
                    // Store quiz info for bonus submission
                    window.bonusQuizInfo = {
                        topic: currentTopic,
                        score: percentage
                    };
                } else {
                    dinoBonusUnlock.style.display = 'none';
                }
            }
        }
        
        // ==================== DINO BONUS QUESTION FUNCTIONS ====================
        
        let currentBonusQuestion = null;
        let bonusAnswered = false;
        
        function skipBonusQuestion() {
            const dinoBonusUnlock = document.getElementById('dino-bonus-unlock');
            if (dinoBonusUnlock) {
                dinoBonusUnlock.style.display = 'none';
            }
        }
        
        async function startBonusQuestion() {
            // Hide the unlock card
            const dinoBonusUnlock = document.getElementById('dino-bonus-unlock');
            if (dinoBonusUnlock) {
                dinoBonusUnlock.style.display = 'none';
            }
            
            // Show modal
            const modal = document.getElementById('bonusQuestionModal');
            modal.classList.add('visible');
            
            // Reset state
            bonusAnswered = false;
            document.getElementById('bonusResult').style.display = 'none';
            document.getElementById('bonusFooter').style.display = 'none';
            document.getElementById('bonusImage').style.display = 'none';
            document.getElementById('bonusImageLoading').style.display = 'block';
            document.getElementById('bonusOptions').innerHTML = '<p class="text-center text-gray-500">Loading options...</p>';
            
            // Fetch random bonus question
            try {
                const response = await fetch('/api/bonus-question/random?category=dinosaurs');
                if (!response.ok) {
                    throw new Error('No bonus questions available');
                }
                
                currentBonusQuestion = await response.json();
                
                // Load image
                const img = document.getElementById('bonusImage');
                img.onload = function() {
                    document.getElementById('bonusImageLoading').style.display = 'none';
                    img.style.display = 'block';
                };
                img.onerror = function() {
                    document.getElementById('bonusImageLoading').innerHTML = '<p class="text-red-400">Image failed to load</p>';
                };
                img.src = currentBonusQuestion.image_url;
                
                // Render options
                const optionsContainer = document.getElementById('bonusOptions');
                optionsContainer.innerHTML = '';
                
                currentBonusQuestion.options.forEach((option, index) => {
                    const btn = document.createElement('button');
                    btn.className = 'bonus-option-btn';
                    btn.textContent = option;
                    btn.onclick = () => selectBonusAnswer(option, btn);
                    optionsContainer.appendChild(btn);
                });
                
            } catch (error) {
                console.error('Error loading bonus question:', error);
                document.getElementById('bonusOptions').innerHTML = `
                    <p class="text-center text-red-500">
                        <i class="fas fa-exclamation-circle mr-2"></i>
                        Could not load bonus question. Please try again later.
                    </p>
                `;
            }
        }
        
        async function selectBonusAnswer(selectedAnswer, btnElement) {
            if (bonusAnswered) return;
            bonusAnswered = true;
            
            // Disable all buttons
            document.querySelectorAll('.bonus-option-btn').forEach(btn => {
                btn.disabled = true;
            });
            
            // Submit answer
            try {
                const response = await fetch('/api/bonus-question/submit', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        question_id: currentBonusQuestion.id,
                        selected_answer: selectedAnswer,
                        quiz_topic: window.bonusQuizInfo?.topic || currentTopic,
                        quiz_score: window.bonusQuizInfo?.score || 0
                    })
                });
                
                const result = await response.json();
                
                // Highlight correct/incorrect
                document.querySelectorAll('.bonus-option-btn').forEach(btn => {
                    if (btn.textContent === result.correct_answer) {
                        btn.classList.add('reveal-correct');
                    }
                    if (btn.textContent === selectedAnswer) {
                        if (result.correct) {
                            btn.classList.add('correct');
                        } else {
                            btn.classList.add('incorrect');
                        }
                    }
                });
                
                // Show result
                const resultDiv = document.getElementById('bonusResult');
                resultDiv.className = 'bonus-result ' + (result.correct ? 'correct' : 'incorrect');
                
                if (result.correct) {
                    resultDiv.innerHTML = `
                        <h3>🎉 Correct!</h3>
                        <div class="points-earned">+${result.points_earned} points!</div>
                        <div class="fun-fact">
                            <div class="fun-fact-label">🦕 Did You Know?</div>
                            <div class="fun-fact-text">${result.fun_fact || 'Amazing work!'}</div>
                        </div>
                    `;
                    
                    // Refresh stats panel to show updated points (Rev 2.99 fix)
                    if (typeof loadBadgeWidget === 'function') {
                        loadBadgeWidget();
                    } else if (typeof refreshStatsPanel === 'function') {
                        refreshStatsPanel();
                    }
                } else {
                    resultDiv.innerHTML = `
                        <h3>Not quite!</h3>
                        <p style="color: #4b5563; margin-bottom: 8px;">The correct answer was <strong>${result.correct_answer}</strong></p>
                        <div class="fun-fact">
                            <div class="fun-fact-label">🦕 Did You Know?</div>
                            <div class="fun-fact-text">${result.fun_fact || 'Better luck next time!'}</div>
                        </div>
                    `;
                }
                
                resultDiv.style.display = 'block';
                document.getElementById('bonusFooter').style.display = 'block';
                
            } catch (error) {
                console.error('Error submitting bonus answer:', error);
                alert('Error submitting answer. Please try again.');
                bonusAnswered = false;
                document.querySelectorAll('.bonus-option-btn').forEach(btn => {
                    btn.disabled = false;
                });
            }
        }
        
        function closeBonusOnOverlay(event) {
            if (event.target.id === 'bonusQuestionModal' && bonusAnswered) {
                closeBonusModal();
            }
        }
        
        function closeBonusModal() {
            document.getElementById('bonusQuestionModal').classList.remove('visible');
            currentBonusQuestion = null;
        }

        // ==================== DINO ARCHIVE FUNCTIONS ====================
        
        async function openDinoArchive() {
            const modal = document.getElementById('dinoArchiveModal');
            const body = document.getElementById('dinoArchiveBody');
            
            modal.classList.add('visible');
            body.innerHTML = `
                <div class="dino-archive-empty">
                    <i class="fas fa-spinner fa-spin"></i>
                    <p>Loading your archive...</p>
                </div>
            `;
            
            try {
                const response = await fetch('/api/bonus-question/archive');
                const data = await response.json();
                
                // Update stats
                document.getElementById('archiveTotalCount').textContent = data.total || 0;
                document.getElementById('archiveCorrectCount').textContent = data.correct || 0;
                const accuracy = data.total > 0 ? Math.round((data.correct / data.total) * 100) : 0;
                document.getElementById('archiveAccuracy').textContent = accuracy + '%';
                
                if (!data.attempts || data.attempts.length === 0) {
                    body.innerHTML = `
                        <div class="dino-archive-empty">
                            <i class="fas fa-egg"></i>
                            <h3 style="margin-bottom: 10px; color: #374151;">No Dinosaurs Yet!</h3>
                            <p>Complete quizzes with 80%+ score to unlock Dino Challenges.</p>
                            <p style="margin-top: 10px;">Your discovered dinosaurs will appear here.</p>
                        </div>
                    `;
                    return;
                }
                
                // Render archive cards
                body.innerHTML = `
                    <div class="dino-archive-grid">
                        ${data.attempts.map(attempt => `
                            <div class="dino-archive-card ${attempt.is_correct ? 'correct' : 'incorrect'}">
                                <div class="dino-archive-card-image-wrapper">
                                    ${attempt.image_url ? `
                                        <img src="${attempt.image_url}" alt="${attempt.correct_answer}" class="dino-archive-card-image" 
                                             onerror="this.style.display='none'; this.parentElement.innerHTML='<div class=\\'dino-placeholder\\'><span>🦕</span><small>${attempt.correct_answer}</small></div>';">
                                    ` : `
                                        <div class="dino-placeholder"><span>🦕</span><small>${attempt.correct_answer}</small></div>
                                    `}
                                </div>
                                <div class="dino-archive-card-body">
                                    <div class="dino-archive-card-answer">
                                        ${attempt.is_correct ? '<i class="fas fa-check-circle"></i>' : '<i class="fas fa-times-circle"></i>'}
                                        ${attempt.correct_answer}
                                    </div>
                                    <div class="dino-archive-card-meta">
                                        ${attempt.era_or_region ? `<span>${attempt.era_or_region}</span> • ` : ''}
                                        <span>${formatArchiveDate(attempt.attempted_at)}</span>
                                        ${attempt.quiz_topic ? ` • <span>${formatTopicName(attempt.quiz_topic)}</span>` : ''}
                                    </div>
                                    ${attempt.fun_fact ? `
                                        <div class="dino-archive-card-fact">
                                            <strong>🦴 Fun Fact:</strong> ${attempt.fun_fact}
                                        </div>
                                    ` : ''}
                                    ${!attempt.is_correct ? `
                                        <div class="dino-archive-card-your-answer">
                                            Your answer: ${attempt.selected_answer}
                                        </div>
                                    ` : ''}
                                </div>
                            </div>
                        `).join('')}
                    </div>
                `;
                
            } catch (error) {
                console.error('Error loading archive:', error);
                body.innerHTML = `
                    <div class="dino-archive-empty">
                        <i class="fas fa-exclamation-triangle" style="color: #ef4444;"></i>
                        <p>Error loading archive. Please try again.</p>
                    </div>
                `;
            }
        }
        
        function closeDinoArchive() {
            document.getElementById('dinoArchiveModal').classList.remove('visible');
        }
        
        function closeDinoArchiveOnOverlay(event) {
            if (event.target.id === 'dinoArchiveModal') {
                closeDinoArchive();
            }
        }
        
        function formatArchiveDate(dateString) {
            if (!dateString) return '';
            const date = new Date(dateString);
            const now = new Date();
            const diffMs = now - date;
            const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));
            
            if (diffDays === 0) return 'Today';
            if (diffDays === 1) return 'Yesterday';
            if (diffDays < 7) return `${diffDays} days ago`;
            if (diffDays < 30) return `${Math.floor(diffDays / 7)} weeks ago`;
            
            return date.toLocaleDateString('en-IE', { day: 'numeric', month: 'short' });
        }
        
        function formatTopicName(topic) {
            if (!topic) return '';
            return topic.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
        }
        
        // ==================== END DINO ARCHIVE ====================

        function retryQuiz() {
            document.getElementById('resultsScreen').classList.add('hidden');
            startQuiz(currentDifficulty);
        }

        async function backToTopics() {
            document.getElementById('difficultyScreen').classList.add('hidden');
            document.getElementById('resultsScreen').classList.add('hidden');
            document.getElementById('quizScreen').classList.add('hidden');
            document.getElementById('topicScreen').classList.remove('hidden');
            
            // Refresh mastery data AND progress after quiz completion
            await loadMasteryData();
            await loadTopics(); // Rebuild topic cards with updated mastery
            loadProgress();
        }

        function backToDifficulty() {
            // Refresh mastery data before showing difficulty screen
            refreshAndShowDifficulty();
        }
        
        async function refreshAndShowDifficulty() {
            // ===== DEACTIVATE QUIZ MODE =====
            document.body.classList.remove('quiz-active');
            
            await loadMasteryData(); // Get updated mastery after quiz
            document.getElementById('quizScreen').classList.add('hidden');
            document.getElementById('resultsScreen').classList.add('hidden');
            // Re-render difficulty buttons with updated mastery
            selectTopic(currentTopic, document.getElementById('selectedTopicTitle').textContent);
        }

        async function logout() {
            try {
                await fetch('/api/logout', { method: 'POST' });
                window.location.href = '/';
            } catch (error) {
                console.error('Error logging out:', error);
            }
        }

        // ==================== MOBILE MENU ====================
        
        function toggleMobileMenu() {
            const menu = document.getElementById('mobileMenu');
            const icon = document.getElementById('mobileMenuIcon');
            
            menu.classList.toggle('show');
            
            if (menu.classList.contains('show')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        }
        
        // Close mobile menu when clicking outside
        document.addEventListener('click', function(e) {
            const menu = document.getElementById('mobileMenu');
            const menuBtn = document.getElementById('mobileMenuBtn');
            
            if (menu && menuBtn && !menu.contains(e.target) && !menuBtn.contains(e.target)) {
                if (menu.classList.contains('show')) {
                    menu.classList.remove('show');
                    document.getElementById('mobileMenuIcon').classList.remove('fa-times');
                    document.getElementById('mobileMenuIcon').classList.add('fa-bars');
                }
            }
        });

        // ==================== PWA BACK BUTTON HANDLING ====================
        
        // Handle back button in PWA to prevent hanging
        window.addEventListener('popstate', function(event) {
            // If we're on a quiz screen, go back to topic selection
            const quizScreen = document.getElementById('quizScreen');
            const difficultyScreen = document.getElementById('difficultyScreen');
            const resultsScreen = document.getElementById('resultsScreen');
            const adaptiveContainer = document.getElementById('adaptiveQuizContainer');
            
            if (quizScreen && !quizScreen.classList.contains('hidden')) {
                // In a quiz - go back to difficulty selection
                event.preventDefault();
                backToTopics();
                history.pushState(null, '', window.location.pathname);
            } else if (difficultyScreen && !difficultyScreen.classList.contains('hidden')) {
                // In difficulty selection - go back to topics
                event.preventDefault();
                backToTopics();
                history.pushState(null, '', window.location.pathname);
            } else if (resultsScreen && !resultsScreen.classList.contains('hidden')) {
                // In results - go back to topics
                event.preventDefault();
                backToTopics();
                history.pushState(null, '', window.location.pathname);
            } else if (adaptiveContainer && !adaptiveContainer.classList.contains('hidden')) {
                // In adaptive quiz - go back to topics
                event.preventDefault();
                exitAdaptiveQuiz();
                history.pushState(null, '', window.location.pathname);
            }
        });
        
        // Push initial state so we have something to go back to
        if (window.history && window.history.pushState) {
            history.pushState(null, '', window.location.pathname);
        }

        // ==================== QUESTION FLAGGING ====================

        let currentFlagQuestionId = null;

        function showFlagQuestionModal(questionId) {
            currentFlagQuestionId = questionId;
            const question = questions[currentQuestionIndex];

            document.getElementById('flagQuestionText').textContent = question.question;
            document.getElementById('flagQuestionModal').classList.remove('hidden');
            document.getElementById('flagQuestionModal').classList.add('flex');

            document.getElementById('flagForm').reset();
            // Clear adaptive flag marker when showing for standard question
            window.currentAdaptiveFlagQuestion = null;
        }

        function hideFlagModal() {
            document.getElementById('flagQuestionModal').classList.add('hidden');
            document.getElementById('flagQuestionModal').classList.remove('flex');
            currentFlagQuestionId = null;
            window.currentAdaptiveFlagQuestion = null;
        }

        document.addEventListener('DOMContentLoaded', function() {
            const flagForm = document.getElementById('flagForm');
            if (flagForm) {
                flagForm.addEventListener('submit', async function(e) {
                    e.preventDefault();

                    const flagType = document.getElementById('flagType').value;
                    const description = document.getElementById('flagDescription').value;

                    if (!flagType || !description.trim()) {
                        alert('Please fill in all fields');
                        return;
                    }

                    try {
                        let response;
                        
                        // Check if this is an adaptive question flag
                        if (window.currentAdaptiveFlagQuestion) {
                            const question = window.currentAdaptiveFlagQuestion;
                            response = await fetch('/api/student/flag-adaptive-question', {
                                method: 'POST',
                                headers: {'Content-Type': 'application/json'},
                                body: JSON.stringify({
                                    question_id: question.id,
                                    topic: adaptiveState ? adaptiveState.topic : '',
                                    flag_type: flagType,
                                    description: description,
                                    question_text: question.question_text
                                })
                            });
                        } else {
                            // Standard question flag
                            response = await fetch('/api/student/flag-question', {
                                method: 'POST',
                                headers: {'Content-Type': 'application/json'},
                                body: JSON.stringify({
                                    question_id: currentFlagQuestionId,
                                    flag_type: flagType,
                                    description: description
                                })
                            });
                        }

                        const data = await response.json();

                        if (response.ok) {
                            alert('Thank you! Your report has been submitted to the administrator.');
                            hideFlagModal();
                        } else {
                            alert(data.error || 'Failed to submit report');
                        }
                    } catch (error) {
                        console.error('Error submitting flag:', error);
                        alert('Error submitting report. Please try again.');
                    }
                });
            }
        });
        
        // ==================== CALCULATOR FUNCTIONS ====================
        
        let calcExpression = '';
        let calcCurrentValue = '0';
        let calcLastResult = null;
        let calcIsOpen = false;
        
        // Initialize calculator state from session preference
        function initCalculator() {
            const keepOpen = localStorage.getItem('calcKeepOpen') === 'true';
            const checkbox = document.getElementById('calcKeepOpen');
            if (checkbox) {
                checkbox.checked = keepOpen;
            }
        }
        
        function toggleCalculator() {
            const overlay = document.getElementById('calculatorOverlay');
            const calcBtn = document.getElementById('compactCalcBtn');
            
            if (overlay.classList.contains('visible')) {
                hideCalculator();
            } else {
                showCalculator();
            }
        }
        
        function showCalculator() {
            const overlay = document.getElementById('calculatorOverlay');
            const calcBtn = document.getElementById('compactCalcBtn');
            
            overlay.classList.add('visible');
            if (calcBtn) calcBtn.classList.add('active');
            calcIsOpen = true;
        }
        
        function hideCalculator() {
            const overlay = document.getElementById('calculatorOverlay');
            const calcBtn = document.getElementById('compactCalcBtn');
            const keepOpen = document.getElementById('calcKeepOpen');
            
            // Don't hide if "keep open" is checked (unless forced)
            if (keepOpen && keepOpen.checked) return;
            
            overlay.classList.remove('visible');
            if (calcBtn) calcBtn.classList.remove('active');
            calcIsOpen = false;
        }
        
        function closeCalculatorOnOverlay(event) {
            // Only close if clicking on the overlay background
            if (event.target.id === 'calculatorOverlay') {
                const keepOpen = document.getElementById('calcKeepOpen');
                if (!keepOpen || !keepOpen.checked) {
                    hideCalculator();
                }
            }
        }
        
        // ========== CALCULATOR DRAG FUNCTIONALITY ==========
        let calcDragActive = false;
        let calcDragStartX = 0;
        let calcDragStartY = 0;
        let calcInitialLeft = 0;
        let calcInitialTop = 0;
        
        function initCalculatorDrag() {
            const header = document.getElementById('calculatorHeader');
            const container = document.getElementById('calculatorContainer');
            
            if (!header || !container) return;
            
            // Mouse events
            header.addEventListener('mousedown', startCalcDrag);
            document.addEventListener('mousemove', doCalcDrag);
            document.addEventListener('mouseup', stopCalcDrag);
            
            // Touch events for mobile
            header.addEventListener('touchstart', startCalcDragTouch, { passive: false });
            document.addEventListener('touchmove', doCalcDragTouch, { passive: false });
            document.addEventListener('touchend', stopCalcDrag);
        }
        
        function startCalcDrag(e) {
            // Don't drag if clicking the close button
            if (e.target.closest('.calculator-close')) return;
            
            const container = document.getElementById('calculatorContainer');
            calcDragActive = true;
            calcDragStartX = e.clientX;
            calcDragStartY = e.clientY;
            
            const rect = container.getBoundingClientRect();
            calcInitialLeft = rect.left;
            calcInitialTop = rect.top;
            
            container.style.transition = 'none';
        }
        
        function startCalcDragTouch(e) {
            if (e.target.closest('.calculator-close')) return;
            
            const touch = e.touches[0];
            const container = document.getElementById('calculatorContainer');
            calcDragActive = true;
            calcDragStartX = touch.clientX;
            calcDragStartY = touch.clientY;
            
            const rect = container.getBoundingClientRect();
            calcInitialLeft = rect.left;
            calcInitialTop = rect.top;
            
            container.style.transition = 'none';
            e.preventDefault();
        }
        
        function doCalcDrag(e) {
            if (!calcDragActive) return;
            
            const container = document.getElementById('calculatorContainer');
            const deltaX = e.clientX - calcDragStartX;
            const deltaY = e.clientY - calcDragStartY;
            
            let newLeft = calcInitialLeft + deltaX;
            let newTop = calcInitialTop + deltaY;
            
            // Keep calculator within viewport bounds
            const maxLeft = window.innerWidth - container.offsetWidth - 10;
            const maxTop = window.innerHeight - container.offsetHeight - 10;
            
            newLeft = Math.max(10, Math.min(newLeft, maxLeft));
            newTop = Math.max(10, Math.min(newTop, maxTop));
            
            container.style.left = newLeft + 'px';
            container.style.top = newTop + 'px';
            container.style.right = 'auto';
        }
        
        function doCalcDragTouch(e) {
            if (!calcDragActive) return;
            
            const touch = e.touches[0];
            const container = document.getElementById('calculatorContainer');
            const deltaX = touch.clientX - calcDragStartX;
            const deltaY = touch.clientY - calcDragStartY;
            
            let newLeft = calcInitialLeft + deltaX;
            let newTop = calcInitialTop + deltaY;
            
            // Keep calculator within viewport bounds
            const maxLeft = window.innerWidth - container.offsetWidth - 10;
            const maxTop = window.innerHeight - container.offsetHeight - 10;
            
            newLeft = Math.max(10, Math.min(newLeft, maxLeft));
            newTop = Math.max(10, Math.min(newTop, maxTop));
            
            container.style.left = newLeft + 'px';
            container.style.top = newTop + 'px';
            container.style.right = 'auto';
            
            e.preventDefault();
        }
        
        function stopCalcDrag() {
            if (calcDragActive) {
                const container = document.getElementById('calculatorContainer');
                container.style.transition = '';
            }
            calcDragActive = false;
        }
        
        // Initialize drag on page load
        document.addEventListener('DOMContentLoaded', initCalculatorDrag);
        // ========== END CALCULATOR DRAG ==========
        
        function saveCalcPreference() {
            const keepOpen = document.getElementById('calcKeepOpen').checked;
            localStorage.setItem('calcKeepOpen', keepOpen);
            
            if (keepOpen && !calcIsOpen) {
                showCalculator();
            }
        }
        
        function updateCalcDisplay() {
            document.getElementById('calcExpression').textContent = calcExpression;
            document.getElementById('calcResult').textContent = calcCurrentValue;
        }
        
        function calcInput(value) {
            if (calcCurrentValue === '0' && value !== '.') {
                calcCurrentValue = value;
            } else if (calcCurrentValue === 'Error') {
                calcCurrentValue = value;
                calcExpression = '';
            } else {
                calcCurrentValue += value;
            }
            updateCalcDisplay();
        }
        
        function calcClear() {
            calcExpression = '';
            calcCurrentValue = '0';
            calcLastResult = null;
            updateCalcDisplay();
        }
        
        function calcBackspace() {
            if (calcCurrentValue.length > 1) {
                calcCurrentValue = calcCurrentValue.slice(0, -1);
            } else {
                calcCurrentValue = '0';
            }
            updateCalcDisplay();
        }
        
        function calcEquals() {
            try {
                // Store expression for display
                calcExpression = calcCurrentValue;
                
                // Convert display operators to JavaScript operators
                let expression = calcCurrentValue
                    .replace(/×/g, '*')
                    .replace(/÷/g, '/')
                    .replace(/−/g, '-')
                    .replace(/π/g, Math.PI.toString());
                
                // Evaluate safely
                let result = Function('"use strict"; return (' + expression + ')')();
                
                // Format result
                if (isNaN(result) || !isFinite(result)) {
                    calcCurrentValue = 'Error';
                } else {
                    // Round to reasonable precision
                    if (Number.isInteger(result)) {
                        calcCurrentValue = result.toString();
                    } else {
                        calcCurrentValue = parseFloat(result.toPrecision(10)).toString();
                    }
                    calcLastResult = result;
                }
            } catch (e) {
                calcCurrentValue = 'Error';
            }
            updateCalcDisplay();
        }
        
        function calcSquare() {
            try {
                let val = parseFloat(calcCurrentValue.replace(/×/g, '*').replace(/÷/g, '/').replace(/−/g, '-'));
                if (!isNaN(val)) {
                    calcExpression = `(${calcCurrentValue})²`;
                    calcCurrentValue = (val * val).toString();
                    updateCalcDisplay();
                }
            } catch (e) {
                calcCurrentValue = 'Error';
                updateCalcDisplay();
            }
        }
        
        function calcSquareRoot() {
            try {
                let val = parseFloat(calcCurrentValue);
                if (!isNaN(val) && val >= 0) {
                    calcExpression = `√(${calcCurrentValue})`;
                    let result = Math.sqrt(val);
                    calcCurrentValue = Number.isInteger(result) ? result.toString() : parseFloat(result.toPrecision(10)).toString();
                    updateCalcDisplay();
                } else {
                    calcCurrentValue = 'Error';
                    updateCalcDisplay();
                }
            } catch (e) {
                calcCurrentValue = 'Error';
                updateCalcDisplay();
            }
        }
        
        function calcPi() {
            if (calcCurrentValue === '0' || calcCurrentValue === 'Error') {
                calcCurrentValue = 'π';
            } else {
                calcCurrentValue += 'π';
            }
            updateCalcDisplay();
        }
        
        function calcNegate() {
            if (calcCurrentValue !== '0' && calcCurrentValue !== 'Error') {
                if (calcCurrentValue.startsWith('-')) {
                    calcCurrentValue = calcCurrentValue.slice(1);
                } else {
                    calcCurrentValue = '-' + calcCurrentValue;
                }
                updateCalcDisplay();
            }
        }
        
        // Keyboard support for calculator
        document.addEventListener('keydown', function(e) {
            // Only handle if calculator is open
            if (!calcIsOpen) return;
            
            // Prevent interference with other inputs
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
            
            const key = e.key;
            
            if (/[0-9]/.test(key)) {
                calcInput(key);
            } else if (key === '.') {
                calcInput('.');
            } else if (key === '+') {
                calcInput('+');
            } else if (key === '-') {
                calcInput('-');
            } else if (key === '*') {
                calcInput('×');
            } else if (key === '/') {
                e.preventDefault(); // Prevent browser search
                calcInput('÷');
            } else if (key === 'Enter' || key === '=') {
                e.preventDefault();
                calcEquals();
            } else if (key === 'Escape') {
                hideCalculator();
            } else if (key === 'Backspace') {
                e.preventDefault();
                calcBackspace();
            } else if (key === 'c' || key === 'C') {
                calcClear();
            } else if (key === '(') {
                calcInput('(');
            } else if (key === ')') {
                calcInput(')');
            }
        });
        
        // Initialize calculator when quiz starts
        const originalStartQuiz = window.startQuiz;
        if (typeof originalStartQuiz === 'function') {
            window.startQuiz = function(...args) {
                initCalculator();
                return originalStartQuiz.apply(this, args);
            };
        } else {
            // If startQuiz not defined yet, init on DOM ready
            document.addEventListener('DOMContentLoaded', initCalculator);
        }
