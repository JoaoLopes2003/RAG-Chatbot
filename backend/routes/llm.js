var express = require('express');
var axios = require('axios');
var router = express.Router();

var VECTOR_DB_URL = process.env.VECTOR_DB_HOST;
var LLM_URL = process.env.LLM_HOST;

/* POST LLM answer. */
router.post('/', async function(req, res, next) {
    if (!req.body || !req.body.prompt) {
        return res.status(400).json({
            error: 'Bad Request',
            message: 'Missing required field: prompt'
        });
    }

    // Try to get documents from Search Engine
    try {
        console.log('Sending request to search engine...');
        const searchResponse = await axios.post(
            `${VECTOR_DB_URL}/search`,
            { query: req.body.prompt },
            { headers: { 'Content-Type': 'application/json' } }
        );
        console.log('Received response from search engine:', searchResponse.status);

        // Add documents only if search succeeded
        req.body.documents = searchResponse.data.response;
    } catch (error) {
        console.warn('Search engine failed, continuing without documents.', {
            message: error.message,
            status: error.response?.status
        });
        // Do not add documents field, just continue to LLM
    }

    // Call LLM service
    try {
        console.log('Sending request to LLM service...');
        const llmResponse = await axios.post(
            `${LLM_URL}/llm`,
            req.body,
            { headers: { 'Content-Type': 'application/json' } }
        );
        console.log('Received response from LLM service:', llmResponse.status);
        res.json(llmResponse.data);
    } catch (error) {
        console.error('LLM service error:', {
            message: error.message,
            code: error.code,
            response: error.response?.data,
            status: error.response?.status
        });

        if (error.response) {
            res.status(error.response.status).json({
                error: 'LLM service error',
                message: error.response.data || error.message
            });
        } else if (error.request) {
            res.status(503).json({
                error: 'Service unavailable',
                message: 'Unable to connect to LLM service'
            });
        } else {
            res.status(500).json({
                error: 'Internal server error',
                message: error.message
            });
        }
    }
});

module.exports = router;