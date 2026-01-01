/**
 * AgentMath Sound Effects Module
 * Audio feedback for correct/incorrect answers and streaks
 * Rev 3.0.11 - 2025-12-12
 */

// =====================================================
// SOUND EFFECTS SYSTEM
// =====================================================

let soundEnabled = localStorage.getItem('agentmath_sound') !== 'false'; // Default ON

// Sound effect URLs (using Web Audio API for reliability)
const soundEffects = {
    correct: null,
    incorrect: null,
    streak3: null,
    streak5: null,
    streak10: null,
    levelUp: null
};

// Initialize audio context and sounds
let audioContext = null;

function initSoundSystem() {
    try {
        audioContext = new (window.AudioContext || window.webkitAudioContext)();
        console.log('🔊 Sound system initialized');
    } catch (e) {
        console.log('⚠️ Web Audio API not supported');
    }
}

function playSound(type) {
    if (!soundEnabled || !audioContext) return;
    
    // Resume audio context if suspended (required for some browsers)
    if (audioContext.state === 'suspended') {
        audioContext.resume();
    }
    
    const oscillator = audioContext.createOscillator();
    const gainNode = audioContext.createGain();
    oscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);
    
    const now = audioContext.currentTime;
    
    switch(type) {
        case 'correct':
            // Pleasant ascending two-note chime
            oscillator.type = 'sine';
            oscillator.frequency.setValueAtTime(523.25, now); // C5
            oscillator.frequency.setValueAtTime(659.25, now + 0.1); // E5
            gainNode.gain.setValueAtTime(0.3, now);
            gainNode.gain.exponentialDecayToValueAtTime(0.01, now + 0.3);
            oscillator.start(now);
            oscillator.stop(now + 0.3);
            break;
            
        case 'incorrect':
            // Low buzz
            oscillator.type = 'sawtooth';
            oscillator.frequency.setValueAtTime(150, now);
            gainNode.gain.setValueAtTime(0.2, now);
            gainNode.gain.exponentialDecayToValueAtTime(0.01, now + 0.2);
            oscillator.start(now);
            oscillator.stop(now + 0.2);
            break;
            
        case 'streak3':
            // Three ascending notes
            playArpeggio([523.25, 587.33, 659.25], 0.1, 0.4);
            break;
            
        case 'streak5':
            // Five ascending notes (pentatonic feel)
            playArpeggio([523.25, 587.33, 659.25, 783.99, 880], 0.08, 0.5);
            break;
            
        case 'streak10':
            // Celebratory fanfare
            playArpeggio([523.25, 659.25, 783.99, 1046.5], 0.12, 0.6);
            break;
            
        case 'levelUp':
            // Triumphant ascending arpeggio
            playArpeggio([523.25, 659.25, 783.99, 1046.5, 1318.5], 0.1, 0.7);
            break;
    }
}

function playArpeggio(frequencies, noteLength, totalDuration) {
    if (!audioContext) return;
    
    frequencies.forEach((freq, index) => {
        const osc = audioContext.createOscillator();
        const gain = audioContext.createGain();
        osc.connect(gain);
        gain.connect(audioContext.destination);
        
        osc.type = 'sine';
        const startTime = audioContext.currentTime + (index * noteLength);
        osc.frequency.setValueAtTime(freq, startTime);
        gain.gain.setValueAtTime(0.2, startTime);
        gain.gain.exponentialDecayToValueAtTime(0.01, startTime + noteLength + 0.1);
        
        osc.start(startTime);
        osc.stop(startTime + noteLength + 0.1);
    });
}

function toggleSoundEffects() {
    soundEnabled = !soundEnabled;
    localStorage.setItem('agentmath_sound', soundEnabled);
    updateSoundToggleUI();
    
    // Play a test sound when turning on
    if (soundEnabled) {
        playSound('correct');
    }
}

function updateSoundToggleUI() {
    const toggleBtn = document.getElementById('soundToggleBtn');
    if (toggleBtn) {
        toggleBtn.innerHTML = soundEnabled ? 
            '<i class="fas fa-volume-up"></i>' : 
            '<i class="fas fa-volume-mute"></i>';
        toggleBtn.title = soundEnabled ? 'Sound On (click to mute)' : 'Sound Off (click to unmute)';
        toggleBtn.style.opacity = soundEnabled ? '1' : '0.5';
    }
}

// =====================================================
// END SOUND EFFECTS MODULE
// =====================================================

console.log('🔊 Sound effects module loaded');
