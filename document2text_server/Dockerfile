FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy installation files
COPY requirements.txt /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the .env file
COPY .env /app

# Copy the rest of the application files
COPY app/ /app

# Expose the port your app runs on
EXPOSE 3004

# Start the application
# If it's a FastAPI app, use uvicorn
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3004"]

# If it's just a regular Python script, use:
CMD ["python", "main.py"]