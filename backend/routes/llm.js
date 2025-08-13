var express = require('express');
var axios = require('axios')
var router = express.Router();

/* POST LLM answer. */
router.post('/', function(req, res, next) {

    // Validate request body
    if (!req.body || !req.body.prompt) {
        return res.status(400).json({
            error: 'Bad Request',
            message: 'Missing required field: prompt'
        });
    }

    console.log('Sending request to LLM service...'); // Debug log

    axios.post('http://localhost:3002/llm', req.body, {
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(answer => {
        console.log('Received response from LLM service:', answer.status);
        res.json(answer.data);
    })
    .catch(error => {
        // Handle errors properly
        console.error('Error details:', {
            message: error.message,
            code: error.code,
            response: error.response?.data,
            status: error.response?.status
        });
        
        // Send appropriate error response
        if (error.response) {
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            res.status(error.response.status).json({
                error: 'LLM service error',
                message: error.response.data || error.message
            });
        } else if (error.request) {
            // The request was made but no response was received
            res.status(503).json({
                error: 'Service unavailable',
                message: 'Unable to connect to LLM service'
            });
        } else {
            // Something happened in setting up the request that triggered an Error
            res.status(500).json({
                error: 'Internal server error',
                message: error.message
            });
        }
    });
});

module.exports = router;
