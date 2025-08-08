class ChatBot {
    constructor() {
        this.form = document.getElementById('chatForm');
        this.textarea = document.getElementById('message');
        this.sendButton = document.getElementById('sendButton');
        this.history = [];
        
        this.initializeEventListeners();
    }
    
    initializeEventListeners() {
        // Form submission
        this.form.addEventListener('submit', (e) => {
            e.preventDefault();
            this.sendMessage();
        });
        
        // Enter key to send (Shift+Enter for new line)
        this.textarea.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });
    }
    
    async sendMessage() {
        const message = this.textarea.value.trim();
        if (!message) return;
        
        // Disable input while sending
        this.setInputState(false);
        
        // Clear textarea
        this.textarea.value = '';
        
        try {
            // Send request to server
            const response = await fetch('http://localhost:3002/llm', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    prompt: message,
                    history: this.history
                })
            });
            
            if (!response.ok) {
                throw new Error(`Server error: ${response.status} ${response.statusText}`);
            }
            
            const data = await response.json();
            
            // Update history
            this.history.push(
                { role: 'user', content: message },
                { role: 'assistant', content: data.response }
            );
            
        } catch (error) {
            console.error('Error sending message:', error);
        } finally {
            // Hide loading and re-enable input
            this.setInputState(true);
            this.textarea.focus();
        }
    }

    setInputState(enabled) {
        this.textarea.disabled = !enabled;
    }
}

// Initialize chatbot when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new ChatBot();
});