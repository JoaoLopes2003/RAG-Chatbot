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
            if (!searchEngineContainer.classList.contains('active-2')) {
                chatbot.style.left = '0'
                chatbot.style.width = '100vw'
            } else {
                chatbot.style.left = '0'
                chatbot.style.width = '78vw'
                searchEngineContainer.classList.remove('active-2')
                searchEngineContainer.classList.add('active-1')
            }
            arrow.classList.add('rotate-180');
            menuOpen = true;
        } else {
            // Open the menu
            header.classList.remove('full-width');
            navbar.classList.remove('inactive');
            if (!searchEngineContainer.classList.contains('active-1')) {
                chatbot.style.left = '18vw'
                chatbot.style.width = '82vw'
            } else {
                chatbot.style.left = '18vw'
                chatbot.style.width = '60vw'
                searchEngineContainer.classList.remove('active-1')
                searchEngineContainer.classList.add('active-2')
            }
            arrow.classList.remove('rotate-180');
            menuOpen = false;
        }
    });

    // FILTERS/SEARCH ENGINE PANEL TOGGLE LOGIC
    const filtersButton = document.querySelector('.button-chat-filters img');
    let filtersOpen = false;

    filtersButton.addEventListener('click', function () {
        if (!filtersOpen) {
            // Open the filters tab
            filtersButton.classList.add('active')
            if (!navbar.classList.contains('inactive')) {
                searchEngineContainer.classList.add('active-2')
                chatbot.style.left = '18vw'
                chatbot.style.width = '60vw'
            } else {
                searchEngineContainer.classList.add('active-1')
                chatbot.style.left = '0vw'
                chatbot.style.width = '78vw'
            }
            filtersOpen = true;
        } else {
            // Close the filters tab
            searchEngineContainer.classList.remove('active-1');
            searchEngineContainer.classList.remove('active-2')
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

    const tabButtons = document.querySelectorAll('.search-engine-options-container .search-engine-options');
    const contentPanes = document.querySelectorAll('.search-engine-options-content-container [data-pane]');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const targetTab = button.dataset.tab;

            // Deactivate all other buttons and panes first
            tabButtons.forEach(btn => btn.classList.remove('active'));
            contentPanes.forEach(pane => pane.classList.remove('active'));

            // Activate the clicked button
            button.classList.add('active');

            // Activate the corresponding content pane
            const targetPane = document.querySelector(`.search-engine-options-content-container [data-pane="${targetTab}"]`);
            if (targetPane) {
                targetPane.classList.add('active');
            }
        });
    });
});