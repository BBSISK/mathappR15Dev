/**
 * Reactive Learning Engine - Passport Integration
 * ================================================
 * This module provides dynamic learning path adjustments based on quiz performance.
 * 
 * Usage:
 * 1. Include this script in student_passport.html
 * 2. Call ReactiveLearning.recordAnswer() after each question
 * 3. Call ReactiveLearning.analyzeAndRecommend() after quiz completion
 * 4. The UI will show recommendations automatically
 * 
 * Revision: 1.0 - 2025-12-19
 */

const ReactiveLearning = {
    // Current session tracking
    sessionId: null,
    currentTopic: null,
    questionCount: 0,
    
    // Thresholds (should match backend)
    thresholds: {
        minQuestionsForAnalysis: 5,
        strugglingAccuracy: 50,
        excellingAccuracy: 85
    },
    
    /**
     * Start a new quiz session for tracking
     */
    startSession: function(topic) {
        this.sessionId = 'session_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
        this.currentTopic = topic.toLowerCase().replace(/ /g, '_');
        this.questionCount = 0;
        console.log(`📊 Reactive Learning: Started session ${this.sessionId} for ${topic}`);
        return this.sessionId;
    },
    
    /**
     * Record a single answer for analysis
     * Call this after each question is answered
     */
    recordAnswer: async function(isCorrect, timeTakenSeconds, level) {
        if (!this.sessionId || !this.currentTopic) {
            console.warn('ReactiveLearning: No active session. Call startSession() first.');
            return;
        }
        
        this.questionCount++;
        
        try {
            const response = await fetch('/api/passport/record-performance', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    topic: this.currentTopic,
                    level: level || 1,
                    is_correct: isCorrect,
                    time_taken_seconds: timeTakenSeconds || 0,
                    question_number: this.questionCount,
                    session_id: this.sessionId
                })
            });
            
            const data = await response.json();
            if (!data.success) {
                console.warn('ReactiveLearning: Failed to record answer', data);
            }
        } catch (error) {
            console.error('ReactiveLearning: Error recording answer', error);
        }
    },
    
    /**
     * Analyze performance and get recommendation
     * Call this after quiz completion
     */
    analyzeAndRecommend: async function(topic) {
        const topicKey = (topic || this.currentTopic).toLowerCase().replace(/ /g, '_');
        
        try {
            const response = await fetch(`/api/passport/analyze-performance/${topicKey}`);
            const data = await response.json();
            
            console.log('📊 Reactive Learning Analysis:', data);
            
            if (data.has_recommendation && data.recommendation) {
                // Show recommendation UI
                this.showRecommendationModal(topicKey, data);
            }
            
            return data;
        } catch (error) {
            console.error('ReactiveLearning: Error analyzing performance', error);
            return null;
        }
    },
    
    /**
     * Show recommendation modal to user
     */
    showRecommendationModal: function(topic, analysisData) {
        const rec = analysisData.recommendation;
        
        // Remove any existing modal
        const existing = document.getElementById('reactive-learning-modal');
        if (existing) existing.remove();
        
        // Determine colors based on recommendation type
        let bgGradient, borderColor, buttonColor;
        if (rec.type === 'level_up') {
            bgGradient = 'linear-gradient(135deg, #10b981, #059669)';
            borderColor = '#10b981';
            buttonColor = '#059669';
        } else if (rec.type === 'level_down') {
            bgGradient = 'linear-gradient(135deg, #f59e0b, #d97706)';
            borderColor = '#f59e0b';
            buttonColor = '#d97706';
        } else {
            bgGradient = 'linear-gradient(135deg, #6366f1, #4f46e5)';
            borderColor = '#6366f1';
            buttonColor = '#4f46e5';
        }
        
        const modal = document.createElement('div');
        modal.id = 'reactive-learning-modal';
        modal.innerHTML = `
            <div style="
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(0,0,0,0.7);
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 10000;
                animation: fadeIn 0.3s ease;
            ">
                <div style="
                    background: white;
                    border-radius: 20px;
                    max-width: 420px;
                    width: 90%;
                    overflow: hidden;
                    box-shadow: 0 25px 50px rgba(0,0,0,0.3);
                    animation: slideUp 0.3s ease;
                ">
                    <!-- Header -->
                    <div style="
                        background: ${bgGradient};
                        padding: 25px;
                        text-align: center;
                        color: white;
                    ">
                        <div style="font-size: 48px; margin-bottom: 10px;">${rec.emoji}</div>
                        <h2 style="margin: 0; font-size: 24px; font-weight: bold;">
                            ${rec.type === 'level_up' ? 'You\'re Excelling!' : 
                              rec.type === 'level_down' ? 'Let\'s Strengthen Foundations' : 
                              'Keep Going!'}
                        </h2>
                    </div>
                    
                    <!-- Content -->
                    <div style="padding: 25px;">
                        <!-- Stats -->
                        <div style="
                            display: flex;
                            justify-content: space-around;
                            margin-bottom: 20px;
                            padding: 15px;
                            background: #f8fafc;
                            border-radius: 12px;
                        ">
                            <div style="text-align: center;">
                                <div style="font-size: 28px; font-weight: bold; color: ${borderColor};">
                                    ${analysisData.accuracy}%
                                </div>
                                <div style="font-size: 12px; color: #64748b;">Accuracy</div>
                            </div>
                            <div style="text-align: center;">
                                <div style="font-size: 28px; font-weight: bold; color: ${borderColor};">
                                    ${analysisData.questions_analyzed}
                                </div>
                                <div style="font-size: 12px; color: #64748b;">Questions</div>
                            </div>
                            <div style="text-align: center;">
                                <div style="font-size: 28px; font-weight: bold; color: ${borderColor};">
                                    L${analysisData.current_level}
                                </div>
                                <div style="font-size: 12px; color: #64748b;">Current</div>
                            </div>
                        </div>
                        
                        <!-- Message -->
                        <p style="
                            color: #475569;
                            font-size: 15px;
                            line-height: 1.6;
                            margin-bottom: 15px;
                            text-align: center;
                        ">
                            ${rec.reason}
                        </p>
                        
                        <!-- Encouragement -->
                        <p style="
                            color: #64748b;
                            font-size: 13px;
                            font-style: italic;
                            text-align: center;
                            margin-bottom: 20px;
                        ">
                            "${rec.encouragement}"
                        </p>
                        
                        <!-- Confidence indicator -->
                        <div style="margin-bottom: 20px;">
                            <div style="
                                display: flex;
                                justify-content: space-between;
                                font-size: 12px;
                                color: #64748b;
                                margin-bottom: 5px;
                            ">
                                <span>Confidence</span>
                                <span>${Math.round(rec.confidence * 100)}%</span>
                            </div>
                            <div style="
                                height: 6px;
                                background: #e2e8f0;
                                border-radius: 3px;
                                overflow: hidden;
                            ">
                                <div style="
                                    height: 100%;
                                    width: ${rec.confidence * 100}%;
                                    background: ${borderColor};
                                    border-radius: 3px;
                                    transition: width 0.5s ease;
                                "></div>
                            </div>
                        </div>
                        
                        <!-- Buttons -->
                        <div style="display: flex; gap: 10px;">
                            ${rec.type !== 'stay' ? `
                                <button onclick="ReactiveLearning.applyRecommendation('${topic}', ${rec.recommended_level})" style="
                                    flex: 1;
                                    padding: 14px 20px;
                                    background: ${buttonColor};
                                    color: white;
                                    border: none;
                                    border-radius: 10px;
                                    font-size: 15px;
                                    font-weight: 600;
                                    cursor: pointer;
                                    transition: transform 0.2s, opacity 0.2s;
                                " onmouseover="this.style.opacity='0.9'" onmouseout="this.style.opacity='1'">
                                    ${rec.action_text}
                                </button>
                                <button onclick="ReactiveLearning.dismissRecommendation('${topic}')" style="
                                    padding: 14px 20px;
                                    background: #f1f5f9;
                                    color: #64748b;
                                    border: none;
                                    border-radius: 10px;
                                    font-size: 15px;
                                    font-weight: 600;
                                    cursor: pointer;
                                    transition: background 0.2s;
                                " onmouseover="this.style.background='#e2e8f0'" onmouseout="this.style.background='#f1f5f9'">
                                    Stay at L${analysisData.current_level}
                                </button>
                            ` : `
                                <button onclick="ReactiveLearning.closeModal()" style="
                                    flex: 1;
                                    padding: 14px 20px;
                                    background: ${buttonColor};
                                    color: white;
                                    border: none;
                                    border-radius: 10px;
                                    font-size: 15px;
                                    font-weight: 600;
                                    cursor: pointer;
                                ">
                                    ${rec.action_text}
                                </button>
                            `}
                        </div>
                    </div>
                </div>
            </div>
            
            <style>
                @keyframes fadeIn {
                    from { opacity: 0; }
                    to { opacity: 1; }
                }
                @keyframes slideUp {
                    from { transform: translateY(30px); opacity: 0; }
                    to { transform: translateY(0); opacity: 1; }
                }
            </style>
        `;
        
        document.body.appendChild(modal);
    },
    
    /**
     * Apply the recommendation - change level
     */
    applyRecommendation: async function(topic, newLevel) {
        try {
            const response = await fetch('/api/passport/apply-recommendation', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    topic: topic,
                    new_level: newLevel,
                    reason: 'reactive_adjustment'
                })
            });
            
            const data = await response.json();
            
            if (data.success) {
                this.closeModal();
                this.showSuccessToast(`Level adjusted to ${newLevel}! 🎯`);
                
                // Update passport UI if function exists
                if (typeof updatePassportDestination === 'function') {
                    updatePassportDestination(topic, newLevel);
                }
                
                // Refresh passport itinerary if function exists
                if (typeof refreshItinerary === 'function') {
                    refreshItinerary();
                }
            } else {
                alert('Failed to apply recommendation: ' + (data.error || 'Unknown error'));
            }
        } catch (error) {
            console.error('Error applying recommendation:', error);
            alert('Error applying recommendation. Please try again.');
        }
    },
    
    /**
     * Dismiss recommendation without applying
     */
    dismissRecommendation: async function(topic) {
        try {
            await fetch('/api/passport/dismiss-recommendation', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic: topic })
            });
        } catch (error) {
            console.warn('Error dismissing recommendation:', error);
        }
        
        this.closeModal();
        this.showSuccessToast('Staying at current level 👍');
    },
    
    /**
     * Close the modal
     */
    closeModal: function() {
        const modal = document.getElementById('reactive-learning-modal');
        if (modal) {
            modal.style.opacity = '0';
            setTimeout(() => modal.remove(), 200);
        }
    },
    
    /**
     * Show a success toast notification
     */
    showSuccessToast: function(message) {
        const toast = document.createElement('div');
        toast.style.cssText = `
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            background: #10b981;
            color: white;
            padding: 15px 30px;
            border-radius: 50px;
            font-weight: 600;
            box-shadow: 0 10px 30px rgba(16, 185, 129, 0.3);
            z-index: 10001;
            animation: toastIn 0.3s ease, toastOut 0.3s ease 2.7s;
        `;
        toast.innerHTML = message;
        
        const style = document.createElement('style');
        style.textContent = `
            @keyframes toastIn { from { opacity: 0; transform: translateX(-50%) translateY(20px); } }
            @keyframes toastOut { to { opacity: 0; transform: translateX(-50%) translateY(-20px); } }
        `;
        document.head.appendChild(style);
        
        document.body.appendChild(toast);
        setTimeout(() => toast.remove(), 3000);
    },
    
    /**
     * Get all pending recommendations
     */
    getPendingRecommendations: async function() {
        try {
            const response = await fetch('/api/passport/get-recommendations');
            const data = await response.json();
            return data.recommendations || [];
        } catch (error) {
            console.error('Error getting recommendations:', error);
            return [];
        }
    },
    
    /**
     * Check for pending recommendations and show badge
     * Call this on passport page load
     */
    checkPendingRecommendations: async function() {
        const recommendations = await this.getPendingRecommendations();
        
        if (recommendations.length > 0) {
            console.log(`📊 Found ${recommendations.length} pending recommendation(s)`);
            
            // Add badge to passport if element exists
            const badge = document.getElementById('recommendations-badge');
            if (badge) {
                badge.textContent = recommendations.length;
                badge.style.display = 'flex';
            }
            
            // Show first recommendation if on passport page
            if (window.location.pathname.includes('passport')) {
                const first = recommendations[0];
                // Could auto-show or just highlight the destination
                this.highlightDestination(first.topic, first.recommendation_type);
            }
        }
        
        return recommendations;
    },
    
    /**
     * Highlight a destination with a recommendation
     */
    highlightDestination: function(topic, type) {
        const destinations = document.querySelectorAll('.destination-card, .itinerary-item');
        destinations.forEach(dest => {
            if (dest.dataset.topic === topic || dest.textContent.toLowerCase().includes(topic.replace('_', ' '))) {
                dest.style.boxShadow = type === 'level_up' 
                    ? '0 0 0 3px #10b981, 0 0 20px rgba(16, 185, 129, 0.3)'
                    : '0 0 0 3px #f59e0b, 0 0 20px rgba(245, 158, 11, 0.3)';
                dest.style.animation = 'pulse 2s infinite';
            }
        });
    },
    
    /**
     * Get performance summary for a topic
     */
    getPerformanceSummary: async function(topic) {
        const topicKey = topic.toLowerCase().replace(/ /g, '_');
        
        try {
            const response = await fetch(`/api/passport/performance-summary/${topicKey}`);
            return await response.json();
        } catch (error) {
            console.error('Error getting performance summary:', error);
            return null;
        }
    }
};

// Auto-initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    // Check for pending recommendations
    if (window.location.pathname.includes('passport')) {
        ReactiveLearning.checkPendingRecommendations();
    }
});

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ReactiveLearning;
}
