class ChatBot {
    constructor() {
        this.form = document.getElementById('chatForm');
        this.textarea = document.getElementById('message');
        this.sendButton = document.getElementById('sendButton');
        this.chatContainer = document.querySelector('.chat-container');
        this.messagesContainer = null;
        this.regenerateMessageContainer = null
        this.firstMessage = true
        this.resendMessage = false
        this.lastMessage = ''
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

        let message = this.textarea.value.trim();
        if (this.resendMessage && this.lastMessage) {
            this.resendMessage = false
            message = this.lastMessage
        } else if (!this.textarea.value.trim()) {
            return;
        } else {
            this.lastMessage = message
        }

        // Remove the regenerateMessageContainer in case there was an error before
        this.checkErrorMessage()
        
        // Disable input while sending
        this.setInputState(false);
        
        // Clear textarea
        this.textarea.value = '';
        this.sendButton.classList.remove('button-valid')

        if (this.history.length < 2 && this.firstMessage) {
            this.firstMessage = false
            this.removeGreetingText()
            this.initiateMessagesContainer()
            this.setupHeightListener();
        }

        const messagesContainer = document.querySelector('.messages-container')

        this.addUserMessage(message)

        // Add a loading animation
        const loader = document.createElement("div");
        loader.classList.add("message-container-assistant-1");
        loader.innerHTML = `
            <div class="message-container-assistant-2">
                <img src="/images/icon-chatbot-2.svg" alt="Chatbot Icon">
                <div class="loader"></div>
            </div>
        `;
        messagesContainer.appendChild(loader);

        this.onChatboxResize(this.form.getBoundingClientRect().height)
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
        
        try {
            // Send request to server
            const response = await fetch('http://localhost:3001/llm', {
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
            this.addChatbotErrorMessage()
            console.error('Error sending message:', error);
        } finally {

            // Add again the chatbot filter and update the scroll bar position
            if (!this.regenerateMessageContainer) {
                this.onChatboxResize(this.form.getBoundingClientRect().height)
            } else {
                this.onChatboxResize(this.form.getBoundingClientRect().height + this.regenerateMessageContainer.getBoundingClientRect().height + 20)
            }
            messagesContainer.scrollTop = messagesContainer.scrollHeight;

            // Update the fade effect
            this.hideFade()

            // Hide loading and re-enable input
            this.setInputState(true);
            this.textarea.focus();
        }
    }

    setInputState(enabled) {
        this.textarea.disabled = !enabled;
    }

    removeGreetingText() {
        const chatGreeting = document.getElementById('chatGreeting').remove()
    }

    initiateMessagesContainer() {
        // create messages container
        const messagesContainer = document.createElement("div");
        messagesContainer.classList.add("messages-container");

        // Calculate the height of the chatbox
        const chatboxHeight = this.form.offsetHeight;
        messagesContainer.innerHTML = `<div class="chatbox-filler" style="min-height: ${chatboxHeight}px"></div>`;
        this.chatContainer.prepend(messagesContainer);
        this.messagesContainer = messagesContainer;

        // Add the fade effect at the top of the chat container
        const fade = document.createElement("div");
        fade.className = "fade-top";
        this.chatContainer.appendChild(fade);
        this.fadeTop = fade;

        // initial place and keep updated on resize
        this.positionFade();
        window.addEventListener('resize', () => this.positionFade());
        this.messagesContainer.addEventListener('scroll', () => this.hideFade());
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
        const loaderEl = messagesContainer.querySelector(".loader")
        const chatbotMessage = loaderEl.parentElement
        loaderEl.remove()

        console.log(content)
        // Parse markdown to HTML
        const htmlContent = this.converter.makeHtml(content);

        chatbotMessage.innerHTML += `
            <div class="message-wrapper-assistant">
                ${htmlContent}
            </div>
        `;

        // Add the option icons refering to this message
        const messageContainer =  chatbotMessage.parentElement
        messageContainer.innerHTML += `
            <div class="message-container-assistant-3">
                <img src="/images/icon-copy-text.svg" alt="Copy Icon" class="copy-option">
                <div class="copy-option-activated">
                    <span>&#x2714;</span>
                </div>
            </div>
        `

        // Add an event listener that links this button to the respective message
        const copyOption = messageContainer.querySelector('.copy-option')
        copyOption.addEventListener('click', (event) => { 
            // Convert the html text to plain text 
            const text = this.copyMessageChatbot(messageContainer.querySelector('.message-wrapper-assistant').innerHTML); 
            
            navigator.clipboard.writeText(text).then(() => { 
                // Update the icon to show the user the content has been copied successfully 
                const checkIconEL = messageContainer.querySelector('.message-container-assistant-3 .copy-option-activated');
                const copyIcon = event.target;
                
                if (checkIconEL) { 
                    checkIconEL.style.display = 'flex';
                } 
                copyIcon.style.display = 'none';

                // Sleep for 3 seconds and hide check icon and show copy icon again 
                setTimeout(() => { 
                    if (checkIconEL) { 
                        checkIconEL.style.display = 'none'; 
                    } 
                    copyIcon.style.display = 'block'; 
                }, 3000); 
            }).catch(err => { 
                console.error('Failed to copy text: ', err); 
            }); 
        });

        // Add an event listener also to the success copy button, so that the user can also copy when the copy button is hidden
        const checkIconEL = messageContainer.querySelector('.message-container-assistant-3 .copy-option-activated')
        checkIconEL.addEventListener('click', () => {
            // Convert the html text to plain text 
            const text = this.copyMessageChatbot(messageContainer.querySelector('.message-wrapper-assistant').innerHTML); 
            navigator.clipboard.writeText(text)
        });

        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    addChatbotErrorMessage() {
        const messagesContainer = document.querySelector('.messages-container')
        const loaderEl = messagesContainer.querySelector(".loader")
        const chatbotMessage = loaderEl.parentElement
        loaderEl.remove()
        
        // Parse markdown to HTML
        const error = "Something went wrong. If this issue persists please contact us."
        console.log(error)

        chatbotMessage.innerHTML += `
            <div class="message-wrapper-assistant-error">
                <span>${error}</span>
            </div>
        `;

        this.addRegenerateResponseButton()

        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    addRegenerateResponseButton() {
        const regenerateResponseEL = document.createElement("div");
        regenerateResponseEL.classList.add("regenerate-response-container");
        this.regenerateMessageContainer = regenerateResponseEL

        // Determine the correct position for the element
        const chatHeight = this.form.getBoundingClientRect().height;
        regenerateResponseEL.style.bottom = `${chatHeight}px`;

        regenerateResponseEL.innerHTML = `
            <span>There was an error generating a response</span>
            <div class="regenerate-response-button">
                <span>&#10226;</span><span>Regenerate Response</span>
            </div>
        `;

        // Add event listener for the regenerate button
        const regenerateButton = regenerateResponseEL.querySelector('.regenerate-response-button');
        regenerateButton.addEventListener('click', () => {
            this.regenerateMessage();
        });

        this.chatContainer.appendChild(regenerateResponseEL)
    }

    regenerateMessage() {
        this.resendMessage = true
        this.sendMessage()
    }

    checkErrorMessage() {
        if (this.regenerateMessageContainer) {
            this.regenerateMessageContainer.remove()
            this.regenerateMessageContainer = null

            // Remove the last two messages in the DOM
            this.history = this.history.slice(0, -2)
            this.reloadLastRequest()
        }
    }

    // Handling height changes in the form div
    setupHeightListener() {
        const resizeObserver = new ResizeObserver(entries => {
            for (let entry of entries) {
                const height = this.form.getBoundingClientRect().height;
                this.onChatboxResize(height);
            }
        });
        
        resizeObserver.observe(this.form);
        resizeObserver.observe(this.messagesContainer);
    }

    removeChatbotFilter() {
        const OldChatboxFiller = this.chatContainer.querySelector('.chatbox-filler');

        if (OldChatboxFiller) {
            // Remove the old filler
            OldChatboxFiller.remove();
        }
    }

    addChatbotFilter (newHeight) {
        // Create the new filler
        const newChatboxFiller = document.createElement("div");
        newChatboxFiller.classList.add("chatbox-filler");
        newChatboxFiller.style.minHeight = `${newHeight}px`;

        // Add the new filler to the DOM
        this.messagesContainer.appendChild(newChatboxFiller);
    }

    onChatboxResize(newHeight) {
        this.removeChatbotFilter()
        this.addChatbotFilter(newHeight)
    }

    positionFade() {
        const chatRect = this.chatContainer.getBoundingClientRect();
        const msgRect  = this.messagesContainer.getBoundingClientRect();

        // compute coordinates relative to chatContainer
        this.fadeTop.style.top  = `${msgRect.top - chatRect.top}px`;
        this.fadeTop.style.left = `${msgRect.left - chatRect.left}px`;
        this.fadeTop.style.width = `${msgRect.width}px`;
    }

    hideFade() {
        if (this.messagesContainer.scrollTop < 40) {
            this.fadeTop.style.display = "none"
        } else {
            this.fadeTop.style.display = "block"
        }
    }

    reloadLastRequest() {
        this.removeChatbotFilter()
        this.messagesContainer.lastElementChild.remove()
        this.messagesContainer.lastElementChild.remove()
    }

    copyMessageChatbot(html) {
        let text = html;
        text = text.replace(/\n/gi, "");
        text = text.replace(/<style([\s\S]*?)<\/style>/gi, "");
        text = text.replace(/<script([\s\S]*?)<\/script>/gi, "");
        text = text.replace(/<a.*?href="(.*?)[\?\"].*?>(.*?)<\/a.*?>/gi, " $2 $1 ");
        text = text.replace(/<\/div>/gi, "\n\n");
        text = text.replace(/<\/li>/gi, "\n");
        text = text.replace(/<li.*?>/gi, "  *  ");
        text = text.replace(/<\/ul>/gi, "\n\n");
        text = text.replace(/<\/p>/gi, "\n\n");
        text = text.replace(/<br\s*[\/]?>/gi, "\n");
        text = text.replace(/<[^>]+>/gi, "");
        text = text.replace(/^\s*/gim, "");
        text = text.replace(/ ,/gi, ",");
        text = text.replace(/ +/gi, " ");
        text = text.replace(/\n+/gi, "\n\n");
        return text;
    }
}

// Initialize chatbot when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new ChatBot();
});