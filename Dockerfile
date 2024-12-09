# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY src/requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY src/ .

# Set the user to 1000
USER 1000

# Expose the port the app runs on
EXPOSE 8080

# Add a healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s CMD curl -f http://localhost:8080/health || exit 1

# Define the command to run the application
CMD ["python", "service.py"]