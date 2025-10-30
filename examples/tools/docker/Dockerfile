# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir massive

# Set the environment variable for the Massive API key
# Note: Replace "<your_api_key>" with your actual API key or use Docker's --env flag when running the container to set it dynamically
# Warning: Not recommended for production or shared environments
ENV MASSIVE_API_KEY=<your_api_key>

# Run the script when the container launches
CMD ["python", "./app.py"]
