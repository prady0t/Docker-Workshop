# Use the Alpine Linux base image
FROM alpine:latest

# Set the working directory
WORKDIR /app

# Install necessary packages
RUN apk add --no-cache python3 py3-pip

# Copy the application files into the container
COPY . /app

# Install Flask and dependencies

RUN pip3 install Flask
# Expose the port the app runs on
EXPOSE 8000

# Specify the default command to run when the container starts
CMD ["python3", "app.py"]

