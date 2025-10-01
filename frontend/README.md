# Frontend Service

## Overview

This directory contains the frontend service for the application, built using html, css, and javascript. The frontend service provides a user interface for interacting with the backend services.

## Setup Instructions

If the user wants to run the frontend service solo, they can follow these steps:

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
    ```

2. Run the docker-compose command to start the service:
   ```bash
   docker-compose up
   ```

3. The frontend service will be accessible at `http://localhost:3001`.

4. To stop the service, use `CTRL+C` in the terminal where the service is running.

## Technologies Used

The frontend server is built using the following technologies:

- **Node.js**;
- **Express.js**;
- **Pug** as the templating engine;
- **Axios** for making HTTP requests to the backend services.
- **dotenv** for managing environment variables.
- **morgan** for logging HTTP requests.
- **nodemon** for development to automatically restart the server on file changes.

## Project Structure

The project structure is as follows:

```
frontend/
├── bin/
│   └── www                # Entry point for the Express application
├── public/                # Static files (CSS, JS, images)
├── routes/                # Route definitions
├── views/                 # Pug templates
├── app.js                 # Main application file
├── package.json           # Project metadata and dependencies
├── README.md              # This file
```

## Environment Variables

The frontend service uses environment variables for configuration. You can set these variables in a `.env` file in the `frontend` directory if you intend to run the service solo. (if running as part of the full application, the main `.env` file in the root directory will be used).

The following environment variables are used:
- `API_KEY`: API key for the Gemini translation service.

Here is an example `.env` file:

```
API_KEY=your_api_key_here
```

## API Endpoints

The frontend service provides the following API endpoints:
- `GET /`: Renders the main page of the application.
- `POST /answerprompt`: Proxies a prompt to the backend chatbot service and returns the response.
- `GET /getfile/:filepath`: Proxies a request to download a specific file
- `GET /getallfiles`: Proxies a request to get a list of all files from the backend service.
- `POST /uploadfile`: Proxies a request to upload a new file to the backend service.
- `POST /updatefile`: Proxies a request to update an existing file in the backend service.
- `POST /deletefile`: Proxies a request to delete a file from the backend service.

## API Documentation

In relation to the API endpoints details, you can find more information by checking the other services README files, since the frontend service mainly acts as a proxy to the backend services. You can quickly access them by clicking here:

## Implemented Features

At the moment the frontend service implements the following features:
- Complete and user friendly interface for interacting with the backend services.
- It allows the common user to easily use the chatbot without worrying about the technical details of the backend services.
- View the sources used by the chatbot to generate the retrieved response.
- Smooth handling of errors and loading states, allowing to resend a prompt if something goes wrong.
- For the experienced user it allows to:
    - Upload, update, delete and download files from the backend service.
    - Select specific source files to be used by the chatbot when answering a prompt.
    - Select how many files the chatbot should retrieve from the vector database when answering a prompt.
    - Select the input and output language for the chatbot.
    - Select the chunking method to consider when doing the similarity search in the vector database.
    - Select if we want to use complete documents or only chunks in the retrieval process.