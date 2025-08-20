# Use the official Node.js runtime as the base image
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json
COPY package.json /app

# Install all dependencies
RUN npm i

# Copy the rest of the application code
COPY . /app

# Expose port 3001
EXPOSE 3001

# Run the app in dev mode
CMD ["npm", "run", "dev"]