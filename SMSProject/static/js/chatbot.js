// Chatbot JavaScript Functionality

class ChatBot {
    constructor() {
        this.chatWidget = document.getElementById('chatbotWidget');
        this.chatToggle = document.getElementById('chatbotToggle');
        this.chatMessages = document.getElementById('chatMessages');
        this.chatInput = document.getElementById('chatInput');
        this.sendBtn = document.getElementById('sendBtn');
        this.minimizeBtn = document.getElementById('minimizeBtn');
        this.notificationBadge = document.getElementById('notificationBadge');
        
        this.isMinimized = false;
        this.isLoading = false;
        
        this.init();
    }

    init() {
        // Event listeners
        this.sendBtn.addEventListener('click', () => this.sendMessage());
        this.chatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.sendMessage();
            }
        });
        this.minimizeBtn.addEventListener('click', () => this.toggleMinimize());
        this.chatToggle.addEventListener('click', () => this.toggleChat());
        
        // Welcome message
        this.addBotMessage('Hello! 👋 I\'m your AI Assistant. How can I help you today?');
        this.setBadge(1);
    }

    toggleChat() {
        if (this.chatWidget.style.display === 'none') {
            this.chatWidget.style.display = 'flex';
            this.chatToggle.classList.add('hidden');
            this.setBadge(0);
        } else {
            this.chatWidget.style.display = 'none';
            this.chatToggle.classList.remove('hidden');
        }
    }

    toggleMinimize() {
        this.isMinimized = !this.isMinimized;
        this.chatWidget.classList.toggle('minimized');
        this.minimizeBtn.innerHTML = this.isMinimized ? 
            '<i class="fas fa-plus"></i>' : 
            '<i class="fas fa-minus"></i>';
    }

    async sendMessage() {
        const message = this.chatInput.value.trim();
        
        if (!message || this.isLoading) {
            return;
        }

        // Clear input
        this.chatInput.value = '';
        this.chatInput.focus();

        // Add user message
        this.addUserMessage(message);

        // Show typing indicator
        this.showTypingIndicator();
        this.isLoading = true;

        try {
            const response = await fetch('/chatbot/api/response/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.getCookie('csrftoken')
                },
                body: JSON.stringify({ message: message })
            });

            const data = await response.json();

            // Remove typing indicator
            this.removeTypingIndicator();

            if (data.success) {
                this.addBotMessage(data.response);
            } else {
                this.addBotMessage('Sorry, I encountered an error: ' + data.error);
            }
        } catch (error) {
            this.removeTypingIndicator();
            this.addBotMessage('Sorry, I couldn\'t process your message. Please try again.');
            console.error('Error:', error);
        } finally {
            this.isLoading = false;
        }
    }

    addUserMessage(message) {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'message user';
        messageDiv.innerHTML = `
            <div class="message-content">
                ${this.escapeHtml(message)}
            </div>
        `;
        this.chatMessages.appendChild(messageDiv);
        this.scrollToBottom();
    }

    addBotMessage(message) {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'message bot';
        
        // Parse and format message (handle markdown-like formatting)
        const formattedMessage = this.formatMessage(message);
        
        messageDiv.innerHTML = `
            <div class="message-content">
                ${formattedMessage}
            </div>
        `;
        this.chatMessages.appendChild(messageDiv);
        this.scrollToBottom();
    }

    formatMessage(message) {
        // Escape HTML
        let formatted = this.escapeHtml(message);
        
        // Convert URLs to links
        formatted = formatted.replace(
            /https?:\/\/[^\s]+/g,
            url => `<a href="${url}" target="_blank" rel="noopener">${url}</a>`
        );
        
        // Convert line breaks
        formatted = formatted.replace(/\n/g, '<br>');
        
        // Bold text between **
        formatted = formatted.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
        
        // Italic text between *
        formatted = formatted.replace(/\*(.+?)\*/g, '<em>$1</em>');
        
        return formatted;
    }

    escapeHtml(text) {
        const map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        };
        return text.replace(/[&<>"']/g, m => map[m]);
    }

    showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot typing-message';
        typingDiv.innerHTML = `
            <div class="typing-indicator">
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
            </div>
        `;
        this.chatMessages.appendChild(typingDiv);
        this.scrollToBottom();
    }

    removeTypingIndicator() {
        const typingMessage = this.chatMessages.querySelector('.typing-message');
        if (typingMessage) {
            typingMessage.remove();
        }
    }

    scrollToBottom() {
        setTimeout(() => {
            this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
        }, 0);
    }

    setBadge(count) {
        this.notificationBadge.textContent = count;
        if (count === 0) {
            this.notificationBadge.style.display = 'none';
        } else {
            this.notificationBadge.style.display = 'flex';
        }
    }

    getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
}

// Initialize chatbot when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new ChatBot();
});
