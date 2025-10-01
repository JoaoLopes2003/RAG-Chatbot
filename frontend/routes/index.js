var express = require('express');
var axios = require('axios');
var path = require('path');
var router = express.Router();

var BACKEND_HOST = process.env.BACKEND_ENTRYPOINT || 'http://localhost:3007';

/* GET home page. */
router.get('/', function(req, res, next) {
    res.render('index', { currentPage: 'Chatbot' });
});

/* Answer a client prompt */
router.post('/answerprompt', async function(req, res, next) {
    console.log('Proxying /answerprompt request to backend with data:', req.body);

    try {
        const response = await axios.post(
            `${BACKEND_HOST}/answerprompt`,
            req.body,
            {
                timeout: 300000 // 2.5 minutes
            }
        );

        // If the backend responds successfully, forward its response (data and status)
        res.status(response.status).json(response.data);

    } catch (error) {
        // If anything goes wrong during the proxy request, handle the error gracefully.
        console.error("Error proxying /answerprompt:", error.message);

        if (error.response) {
            res.status(error.response.status).send(error.response.data);
        } else if (error.request) {
            res.status(503).send("The backend chatbot service is unavailable.");
        } else {
            res.status(500).send("An internal server error occurred while processing the request.");
        }
    }
});

/* Download a specific file from the server. */
router.get('/getfile/:filepath(*)', async function(req, res, next) {
    const filepath = req.params.filepath;

    try {
        const response = await axios({
            method: 'GET',
            url: `${BACKEND_HOST}/getfile`,
            params: {
                filename: filepath
            },
            responseType: 'stream'
        });

        res.set(response.headers);
        res.setHeader('Content-Disposition', `attachment; filename="${path.basename(filepath)}"`);
        response.data.pipe(res);

    } catch (error) {
        console.error("Error proxying /getfile:", error.message);

        if (error.response) {
            // The backend responded with an error. We must handle its response carefully.
            res.status(error.response.status);

            // FIX: Check if the error data is a stream. If so, pipe it.
            // Otherwise, send it normally. This prevents the circular JSON error.
            if (error.response.data && typeof error.response.data.pipe === 'function') {
                error.response.data.pipe(res);
            } else {
                res.send(error.response.data);
            }
        } else if (error.request) {
            res.status(503).send("The backend file service is unavailable.");
        } else {
            res.status(500).send("An internal server error occurred.");
        }
    }
});

/* GET all files from server. */
router.get('/getallfiles', async function(req, res, next) {

    try {
        const response = await axios.get(`${BACKEND_HOST}/getallfiles`);
        
        const responseData = response.data;
        if (responseData && responseData.filenames) {
            
            for (const folderName in responseData.filenames) {
                const files = responseData.filenames[folderName];
                
                // Sort the array of files alphabetically
                if (Array.isArray(files)) {
                    files.sort();
                }
            }
        }

        res.json(responseData);

    } catch (error) {
        console.error("Error proxying /getallfiles:", error.message);
        if (error.response) {
            res.status(error.response.status).send(error.response.data);
        } else if (error.request) {
            res.status(503).send("The backend file service is unavailable.");
        } else {
            res.status(500).send("An internal server error occurred.");
        }
    }
});

/* Upload new file to the server. */
router.post('/uploadfile', async function(req, res, next) {
    try {

        const response = await axios.post(
            `${BACKEND_HOST}/uploadfile`,
            req,
            {
                headers: {
                    'Content-Type': req.headers['content-type']
                },
                timeout: 300000 // 5 minutes
            }
        );

        // The backend returns 201 Created on success.
        res.status(response.status).json(response.data);

    } catch (error) {
        console.error("Error proxying /uploadfile:", error.message);
        if (error.response) {
            res.status(error.response.status).send(error.response.data);
        } else if (error.request) {
            res.status(503).send("The backend file processing service is unavailable.");
        } else {
            res.status(500).send("An internal server error occurred.");
        }
    }
});

/* Update a file in the server. */
router.post('/updatefile', async function(req, res, next) {
    try {

        const response = await axios.post(
            `${BACKEND_HOST}/updatefile`,
            req,
            {
                headers: {
                    'Content-Type': req.headers['content-type']
                },
                timeout: 300000 // 5 minutes
            }
        );

        // The backend returns a status code (e.g., 201 Created).
        // Forward the status and any data from the backend back to the client.
        res.status(response.status).json(response.data);

    } catch (error) {
        console.error("Error proxying /updatefile:", error.message);
        if (error.response) {
            // The backend responded with an error
            res.status(error.response.status).send(error.response.data);
        } else if (error.request) {
            // No response was received from the backend
            res.status(503).send("The backend file processing service is unavailable.");
        } else {
            // Another error occurred
            res.status(500).send("An internal server error occurred.");
        }
    }
});

/* Delete a file from the server. */
router.post('/deletefile', async function(req, res, next) {
    try {

        await new Promise(resolve => setTimeout(resolve, 5000));
        
        const { filename, folder } = req.body;

        const payload = {
            filename: filename,
            folder: folder
        };

        const response = await axios.post(`${BACKEND_HOST}/deletefile`, payload);

        // The backend returns 204 No Content on success.
        res.sendStatus(response.status);

    } catch (error) {
        console.error("Error proxying /deletefile:", error.message);
        if (error.response) {
            res.status(error.response.status).send(error.response.data);
        } else if (error.request) {
            res.status(503).send("The backend file service is unavailable.");
        } else {
            res.status(500).send("An internal server error occurred.");
        }
    }
});

module.exports = router;