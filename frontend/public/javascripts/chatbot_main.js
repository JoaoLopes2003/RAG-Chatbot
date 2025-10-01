import Settings from './settings.js';
import ChatBot from './chatbot.js';
import Sources from './sources_tab.js';

// Single entrypoint for the chatbot
document.addEventListener('DOMContentLoaded', async () => {
    // 1. Initialize the Settings object first and wait for it to be ready
    //    (since it fetches documents from the server).
    const appSettings = await Settings.create();
    const sourceTabs = new Sources();
    console.log("Settings class is fully initialized and ready to use.");

    // 2. Initialize the ChatBot and pass the appSettings instance to it.
    const chatBot = new ChatBot(appSettings, sourceTabs);
    console.log("ChatBot class is initialized and connected to settings and sources.");
});