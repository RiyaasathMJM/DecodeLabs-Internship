/**
 * DecodeLabs - Project 1
 * Rule-Based AI Chatbot - Frontend Controller
 */

// ============================================
// DOM REFERENCES
// ============================================
const messagesContainer = document.getElementById('messagesContainer');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const statsModal = document.getElementById('statsModal');

// ============================================
// STATE
// ============================================
let messageCounter = 0;
let isProcessing = false;

// ============================================
// CORE FUNCTIONS
// ============================================

/**
 * Send message to chatbot API
 */
async function sendMessage() {
    // Prevent double sends
    if (isProcessing) return;

    const message = userInput.value.trim();
    if (!message) {
        userInput.focus();
        return;
    }

    // Clear input
    userInput.value = '';

    // Display user message
    addMessageToChat(message, 'user');

    // Set processing state
    isProcessing = true;
    sendBtn.disabled = true;

    // Show typing indicator
    const typingId = showTypingIndicator();

    try {
        // Send to Flask backend
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({ message: message })
        });

        // Handle errors
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.response || 'Network response was not ok');
        }

        const data = await response.json();

        // Remove typing indicator
        removeTypingIndicator(typingId);

        // Display bot response
        const messageType = data.type || 'normal';
        addMessageToChat(data.response, 'bot');

        // If exit message, update UI
        if (messageType === 'exit') {
            userInput.placeholder = 'Chat ended. Refresh to start new conversation...';
            userInput.disabled = true;
            sendBtn.disabled = true;

            // Re-enable after delay
            setTimeout(() => {
                userInput.disabled = false;
                userInput.placeholder = 'Start a new conversation...';
                sendBtn.disabled = false;
                userInput.focus();
            }, 2000);
        }

    } catch (error) {
        console.error('Chat Error:', error);
        removeTypingIndicator(typingId);
        addMessageToChat('Sorry, there was an error. Please try again.', 'bot');
    } finally {
        isProcessing = false;
        sendBtn.disabled = false;
        userInput.focus();
    }
}

/**
 * Add message to chat display
 */
function addMessageToChat(text, sender) {
    messageCounter++;

    const wrapper = document.createElement('div');
    wrapper.className = `message-wrapper ${sender}`;
    wrapper.id = `msg-${messageCounter}`;

    // Avatar
    const avatar = document.createElement('div');
    avatar.className = 'message-avatar';
    avatar.textContent = sender === 'user' ? '👤' : '🤖';

    // Message body
    const body = document.createElement('div');
    body.className = 'message-body';

    // Bubble
    const bubble = document.createElement('div');
    bubble.className = 'message-bubble';

    // Bot header
    if (sender === 'bot') {
        const header = document.createElement('div');
        header.className = 'message-header';
        header.textContent = 'DecodeLabs Chatbot';
        bubble.appendChild(header);
    }

    // Message text (support for basic HTML formatting)
    const textDiv = document.createElement('div');
    textDiv.className = 'message-text';
    textDiv.innerHTML = formatMessage(text);

    bubble.appendChild(textDiv);

    // Timestamp
    const time = document.createElement('span');
    time.className = 'message-time';
    time.textContent = new Date().toLocaleTimeString('en-US', {
        hour: '2-digit',
        minute: '2-digit',
        hour12: true
    });

    body.appendChild(bubble);
    body.appendChild(time);

    wrapper.appendChild(avatar);
    wrapper.appendChild(body);

    messagesContainer.appendChild(wrapper);

    // Smooth scroll to bottom
    scrollToBottom();
}

/**
 * Format message text
 */
function formatMessage(text) {
    // Escape HTML first
    let formatted = text
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');

    // Line breaks
    formatted = formatted.replace(/\n/g, '<br>');

    // Bold text
    formatted = formatted.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');

    // Code
    formatted = formatted.replace(/`(.+?)`/g, '<code>$1</code>');

    // Highlight specific terms
    const highlights = [
        'deterministic', 'O\\(1\\)', 'hash map', 'white box',
        'IPO', 'rule-based'
    ];

    highlights.forEach(term => {
        const regex = new RegExp(`(${term})`, 'gi');
        formatted = formatted.replace(regex, '<strong style="color: #a29bfe;">$1</strong>');
    });

    return formatted;
}

/**
 * Send quick message from sidebar
 */
function sendQuickMessage(message) {
    userInput.value = message;
    sendMessage();
}

/**
 * Handle keyboard events
 */
function handleKeyDown(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
}

/**
 * Reset conversation
 */
async function resetConversation() {
    try {
        const response = await fetch('/api/reset', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });

        if (response.ok) {
            // Clear messages
            messagesContainer.innerHTML = '';
            messageCounter = 0;

            // Add welcome message back
            addMessageToChat(
                'Conversation reset! I\'m ready for new inputs. Try "hello" or "help" to start.',
                'bot'
            );

            // Reset input
            userInput.value = '';
            userInput.disabled = false;
            userInput.placeholder = 'Type your message... (e.g., hello, what is AI?, bye)';
            userInput.focus();

            sendBtn.disabled = false;

            console.log('✅ Chat reset successfully');
        }
    } catch (error) {
        console.error('Reset Error:', error);
    }
}

/**
 * Show statistics modal
 */
async function showStats() {
    statsModal.style.display = 'flex';

    try {
        const [statsRes, historyRes] = await Promise.all([
            fetch('/api/stats'),
            fetch('/api/history')
        ]);

        const stats = await statsRes.json();
        const history = await historyRes.json();

        const statsContent = document.getElementById('statsContent');
        statsContent.innerHTML = `
            <div style="display: grid; gap: 16px;">
                <div style="background: var(--bg-dark); padding: 16px; border-radius: 8px;">
                    <strong>📈 Performance Metrics</strong><br><br>
                    Total Interactions: <span style="color: #a29bfe;">${stats.total_interactions || 0}</span><br>
                    Fallback Count: <span style="color: #ffa726;">${stats.fallback_count || 0}</span><br>
                    Match Efficiency: <span style="color: #00d68f;">${stats.efficiency || '100%'}</span><br>
                    Active Sessions: <span style="color: #40c4ff;">${stats.active_sessions || 1}</span>
                </div>
                <div style="background: var(--bg-dark); padding: 16px; border-radius: 8px;">
                    <strong>🏗️ Architecture</strong><br><br>
                    Type: Deterministic (White Box)<br>
                    Data Structure: Hash Map / Dictionary<br>
                    Lookup Time: O(1) Constant<br>
                    Pattern: IPO Model<br>
                    Fallback: Atomic .get() method
                </div>
            </div>
        `;
    } catch (error) {
        console.error('Stats Error:', error);
        document.getElementById('statsContent').innerHTML = 'Failed to load stats.';
    }
}

/**
 * Close modal
 */
function closeModal() {
    statsModal.style.display = 'none';
}

// Close modal on background click
statsModal.addEventListener('click', function(e) {
    if (e.target === statsModal) {
        closeModal();
    }
});

// Close modal on Escape key
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && statsModal.style.display === 'flex') {
        closeModal();
    }
});

/**
 * Show typing indicator
 */
function showTypingIndicator() {
    const typingId = `typing-${Date.now()}`;

    const wrapper = document.createElement('div');
    wrapper.className = 'message-wrapper bot';
    wrapper.id = typingId;

    const avatar = document.createElement('div');
    avatar.className = 'message-avatar';
    avatar.textContent = '🤖';

    const body = document.createElement('div');
    body.className = 'message-body';

    const bubble = document.createElement('div');
    bubble.className = 'message-bubble';
    bubble.innerHTML = `
        <div class="typing-indicator">
            <span class="typing-dot"></span>
            <span class="typing-dot"></span>
            <span class="typing-dot"></span>
        </div>
    `;

    body.appendChild(bubble);
    wrapper.appendChild(avatar);
    wrapper.appendChild(body);

    messagesContainer.appendChild(wrapper);
    scrollToBottom();

    return typingId;
}

/**
 * Remove typing indicator
 */
function removeTypingIndicator(typingId) {
    const element = document.getElementById(typingId);
    if (element) {
        element.remove();
    }
}

/**
 * Smooth scroll to bottom
 */
function scrollToBottom() {
    messagesContainer.scrollTo({
        top: messagesContainer.scrollHeight,
        behavior: 'smooth'
    });
}

// ============================================
// INITIALIZATION
// ============================================
document.addEventListener('DOMContentLoaded', function() {
    console.log('🤖 DecodeLabs Chatbot Initialized');
    console.log('📋 Project 1: Rule-Based AI');
    console.log('🏗️ Architecture: Deterministic | Hash Map | O(1)');
    console.log('✅ Ready for input');

    // Focus input on load
    userInput.focus();

    // Load bot info
    fetch('/api/info')
        .then(res => res.json())
        .then(data => {
            console.log('📊 Bot Info:', data);
            const intentCount = document.getElementById('intent-count');
            if (intentCount && data.intents_count) {
                intentCount.textContent = `${data.intents_count}+`;
            }
        })
        .catch(err => console.error('Failed to load bot info:', err));
});

// Log on page unload
window.addEventListener('beforeunload', () => {
    console.log('👋 Chatbot session ended');
});