document.addEventListener('DOMContentLoaded', function () {
    const closeButton = document.querySelector('.button-close-navbar');
    const navbar = document.querySelector('.nav-bar');
    const chatbot = document.querySelector('.chatbot');

    closeButton.addEventListener('click', function () {
        // Start sliding navbar out
        navbar.classList.add('slide-out');

        // Immediately expand chatbot (width will animate)
        chatbot.classList.add('full-width');

        // After 400ms (same as transition), hide navbar from layout
        setTimeout(() => {
            navbar.classList.add('hidden');
        }, 400);
    });
});
