# Translation Service

## Overview

The Translation Service is a microservice designed to handle text translation tasks. It allows to translate text from Romanian to English and vice versa. The service is built using FastAPI and leverages gemini for translation.

## Setup Instructions

If the user wants to only run the translation service, follow these steps:

1. Navigate to the `translation_service` directory:
   ```bash
   cd translation_service
   ```

2. Run the docker-compose command to start the service:
   ```bash
    docker-compose up
    ```

3. The translation service will be accessible at `http://localhost:3004`.

4. To stop the service, use:
   ```bash
   docker-compose down
   ```

## Technologies Used

The Translation Service utilizes the following technologies:

- **FastAPI** as the web framework;
- **Uvicorn** as the ASGI server;
- **python-dotenv** for environment variable management;
- **Pydantic** for data validation;
- **Google Generative AI** for AI functionalities;

## Project Structure

The project structure is organized as follows:

```
translation_service/
├── app/
│   ├── routes/             # API route definitions
│   ├── schemas/            # Pydantic models for request and response validation
│   ├── services/           # Business logic and service implementations
│   ├── main.py             # Entry point for the FastAPI application
├── Dockerfile              # Dockerfile for building the service image
├── requirements.txt        # Python dependencies
├── README.md               # This file
```

## Environment Variables

The translation service uses environment variables for configuration. You can set these variables in a `.env` file in the `translation_service` directory if you intend to run the service independently. (if running as part of the full application stack, the main `.env` file in the root directory will be used).

The following environment variables are used:
- `API_KEY`: Your Gemini API key for translation services.

## API Endpoints

The Translation Service exposes the following API endpoints:
- `POST /query_translator`: Translates text from Romanian to English or vice versa.

### Request

- **Method**: POST
- **Request Body**:
    - `query` (string): The text to be translated.
    - `origin` (string): The source language code (e.g., "ro" for Romanian, "en" for English).
    - `target` (string): The target language code (e.g., "en" for English, "ro" for Romanian).

### Response

- **Content**: A JSON object containing the translated text.
```json
{
    "response": "Translated text"
}
```

## Important Notes

It's important to note the following:

- The service architecture was designed to be extensible, allowing for the addition of more languages in the future.
- The accurate translation relly on an in-context learning approach, where we concatenate the user query with a predefined prompt that provides context for the translation task (a series of input-output pairs where the second line is the translation of the first). You can find the examples in the file `translation_examples.py` inside the folder `services`.