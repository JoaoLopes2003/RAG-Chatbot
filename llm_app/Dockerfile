FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy files
COPY app/ /app
COPY requirements.txt .
COPY .env /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start FastAPI app on port 3002
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3002"]