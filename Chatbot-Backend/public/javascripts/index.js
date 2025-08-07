document.addEventListener('DOMContentLoaded', function () {
    const header = document.querySelector('.header');
    const navbar = document.querySelector('.navbar');
    const chatbot = document.querySelector('.chatbot');
    const closeButton = document.querySelector('.button-close-navbar');
    const arrow = closeButton.querySelector('.arrow-left');
    const searchEngineContainer = document.querySelector('.search-engine-container');

    let menuOpen = false;

    closeButton.addEventListener('click', function () {
        if (!menuOpen) {
            // Close the menu
            header.classList.add('full-width');
            navbar.classList.add('inactive');
            if (!searchEngineContainer.classList.contains('active')) {
                chatbot.style.left = '0'
                chatbot.style.width = '100vw'
            } else {
                chatbot.style.left = '0'
                chatbot.style.width = '78vw'
            }
            arrow.classList.add('rotate-180');
            menuOpen = true;
        } else {
            // Open the menu
            header.classList.remove('full-width');
            navbar.classList.remove('inactive');
            if (!searchEngineContainer.classList.contains('active')) {
                chatbot.style.left = '18vw'
                chatbot.style.width = '82vw'
            } else {
                chatbot.style.left = '18vw'
                chatbot.style.width = '60vw'
            }
            arrow.classList.remove('rotate-180');
            menuOpen = false;
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.chatbox');
    const textarea = form.querySelector('textarea');
    const button = form.querySelector('button');

    form.addEventListener('submit', function (e) {
        if (!textarea.value.trim()) {
            e.preventDefault(); // stop submission
        }
    });

    // Update button cursor based on textarea input
    textarea.addEventListener('input', function () {
        if (textarea.value.trim()) {
            button.classList.add('button-valid')
        } else {
            button.classList.remove('button-valid')
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const searchEngineContainer = document.querySelector('.search-engine-container');
    const filtersButton = document.querySelector('.button-chat-filters img');
    const chatbot = document.querySelector('.chatbot');
    const navbar = document.querySelector('.navbar');

    let filtersOpen = false;

    filtersButton.addEventListener('click', function () {
        if (!filtersOpen) {
            // Open the filters tab
            searchEngineContainer.classList.add('active');
            filtersButton.classList.add('active')
            if (!navbar.classList.contains('inactive')) {
                chatbot.style.left = '18vw'
                chatbot.style.width = '60vw'
            } else {
                chatbot.style.left = '0vw'
                chatbot.style.width = '78vw'
            }
            filtersOpen = true;
        } else {
            // Close the filters tab
            searchEngineContainer.classList.remove('active');
            filtersButton.classList.remove('active')
            if (!navbar.classList.contains('inactive')) {
                chatbot.style.left = '18vw'
                chatbot.style.width = '82vw'
            } else {
                chatbot.style.left = '0'
                chatbot.style.width = '100vw'
            }
            filtersOpen = false;
        }
    });
});