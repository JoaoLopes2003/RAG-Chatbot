var express = require('express');
var axios = require('axios');
var router = express.Router();

var BACKEND_HOST = process.env.BACKEND_HOST;

/* GET home page. */
router.get('/', function(req, res, next) {
    res.render('index', { currentPage: 'Chatbot' });
});

/* POST LLM answer. */
router.post('/llm', async function(req, res, next) {
    
    // Check if the request is valid
    if (!req.body || !req.body.prompt) {
        return res.status(400).json({
            error: 'Bad Request',
            message: 'Missing required field: prompt'
        });
    }

    try {
        console.log('Sending request to search engine...');
        const llmResponse = await axios.post(
            `${BACKEND_HOST}/llm`,
            req.body,
            { headers: { 'Content-Type': 'application/json' } }
        );
        console.log('Received response from the backend:', llmResponse.status);
        res.json(llmResponse.data)
    } catch (error) {
        // Internal error setting up request
        res.status(500).json({
            error: 'Internal Server Error',
            message: error.message
        });
    }
});

module.exports = router;
