# Use a lightweight Python base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory for the application
WORKDIR /home/app

# Install necessary dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

# Copy the Python script into the container
COPY scripts/scripts.py ./scripts.py

# Create the output directory
RUN mkdir -p /home/data/output

# Set environment variable for data directory
ENV DATA_DIR=/home/data/

# Set the entrypoint to execute the script
ENTRYPOINT ["python", "scripts.py"]
