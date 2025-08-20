FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy installation files
COPY requirements.txt /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the .env file
COPY .env /app

# Copy the .env file
COPY documents_json/ /app/documents_json/

# Copy the rest of the application files
COPY app/ /app

# Expose the port your app runs on
EXPOSE 3003

# Start FastAPI app on port 3003
CMD ["python", "-u", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3003"]