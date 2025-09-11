var express = require('express');
var axios = require('axios');
var path = require('path');
var router = express.Router();

var BACKEND_HOST = process.env.BACKEND_HOST || 'http://localhost:3007';

/* GET home page. */
router.get('/', function(req, res, next) {
    res.render('index', { currentPage: 'Chatbot' });
});

/* Download a specific file from the server. */
router.get('/getfile/:filepath(*)', async function(req, res, next) {
    // The (*) in the route path allows for slashes in the filename
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

        // Extract just the filename (e.g., "file.pdf") from the full path ("folder/file.pdf")
        const cleanFilename = path.basename(filepath);

        // First, set all the headers from the backend response (like Content-Type, Content-Length)
        res.set(response.headers);

        // Explicitly set the Content-Disposition header to the correct filename
        res.setHeader('Content-Disposition', `attachment; filename="${cleanFilename}"`);

        // Pipe the file stream from the backend directly to the client's response.
        response.data.pipe(res);

    } catch (error) {
        console.error("Error proxying /getfile:", error.message);
        // Handle errors from the backend service
        if (error.response) {
            res.status(error.response.status).send(error.response.data);
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