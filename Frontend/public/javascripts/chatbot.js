class ChatBot {
    constructor() {
        this.form = document.getElementById('chatForm');
        this.textarea = document.getElementById('message');
        this.sendButton = document.getElementById('sendButton');
        this.chatContainer = document.querySelector('.chat-container');
        this.history = [];
        
        this.initializeEventListeners();

        this.converter = new showdown.Converter({
            tables: true,
            emoji: true,
            disableForced4SpacesIndentedSublists: true,
            tasklists: true,
            ghCodeBlocks: true,
            simplifiedAutoLink: true,
            openLinksInNewWindow: true,
            strikethrough: true,
            moreStyling: true
        })
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

        // Update button cursor based on textarea input
        this.textarea.addEventListener('input', () => {
            if (this.textarea.value.trim()) {
                this.sendButton.classList.add('button-valid')
            } else {
                this.sendButton.classList.remove('button-valid')
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
        this.sendButton.classList.remove('button-valid')

        if (this.history.length < 2) {
            this.hideGreetingText()
            this.initiateMessagesContainer()
        }

        const messagesContainer = document.querySelector('.messages-container')

        this.addUserMessage(message)

        // Add a loading animation
        const loader = document.createElement("div");
        loader.classList.add("message-container-assistant");
        loader.innerHTML = `
            <img src="/images/icon-chatbot-2.svg" alt="Chatbot Icon">
            <div class="loader"></div>
        `;
        messagesContainer.appendChild(loader);
        
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

            this.addChatbotMessage(data.response)
            
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

    hideGreetingText() {
        const chatGreeting = document.getElementById('chatGreeting');
        chatGreeting.style.display = "none"
    }

    initiateMessagesContainer() {
        const messagesContainer = document.createElement("div");
        messagesContainer.classList.add("messages-container");
        this.chatContainer.prepend(messagesContainer)
    }

    // Adding the user message to the DOM
    addUserMessage(content) {
        const messagesContainer = document.querySelector('.messages-container')

        const userMessage = document.createElement("div")
        userMessage.classList.add("message-container-user");

        userMessage.innerHTML = `
            <div class="message-wrapper-user">
                <span>${content}</span>
            </div>
            <img src="/images/icon-user.svg" alt="User Icon">
        `;
        messagesContainer.appendChild(userMessage)
    }

    // Adding the chatbot message to the DOM
    addChatbotMessage(content) {
        const messagesContainer = document.querySelector('.messages-container')

        const chatbotMessage = messagesContainer.lastElementChild
        chatbotMessage.querySelector(".loader").remove()
        console.log(content)

        // Parse markdown to HTML
        const htmlContent = this.converter.makeHtml(content);

        chatbotMessage.innerHTML += `
            <div class="message-wrapper-assistant">
                ${htmlContent}
            </div>
        `;
    }
}

// Initialize chatbot when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new ChatBot();
});