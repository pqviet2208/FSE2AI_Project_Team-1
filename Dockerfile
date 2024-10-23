# Use Python 3.9 as the base image
FROM python:3.9-slim

# Set environment variables to avoid issues with buffer or input output handling
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update && apt install -y  make git curl ca-certificates build-essential

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements.txt first to leverage Docker's caching mechanism
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the project files into the container
COPY . .

# Run the pipeline using the main Makefile
CMD ["make", "run"]
