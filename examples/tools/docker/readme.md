# Dockerized Python Application with Massive API Client

This Docker setup provides a ready-to-use environment for running Python scripts that utilize the `massive-api-client` for financial data processing. It encapsulates the Python environment and the `massive-api-client` library in a Docker container, making it easy to deploy and run the application consistently across any system with Docker installed. This approach is particularly useful for developers looking to integrate Massive's financial data APIs into their applications without worrying about environment inconsistencies.

### Prerequisites

- [Docker](https://www.docker.com/) installed on your machine
- [Massive.com](https://massive.com/) account and API key

### Setup and Configuration

1. Clone the repository or download the Dockerfile and your Python script into a directory.
2. Use Docker's `--env` flag when running the container to set the `MASSIVE_API_KEY` environment variable dynamically, or replace `<your_api_key>` in the Dockerfile with your Massive API key (not recommended for production or shared environments).
3. Ensure your Python script (e.g., `app.py`) is in the same directory as the Dockerfile.

### Building the Docker Image

Any modifications to the Python script will require rebuilding the Docker image to reflect the changes in the containerized environment. Use the docker build command each time your script is updated to ensure the latest version is used in your Docker container.

Navigate to the directory containing your Dockerfile and execute the following command to build your Docker image:

```
docker build -t massive-client-app .
```

This command creates a Docker image named `massive-client-app` based on the instructions in your Dockerfile.

### Running the Docker Container

Run your Docker container using the following command:

```
docker run --env MASSIVE_API_KEY="<your_api_key>" massive-client-app
```

Replace `<your_api_key>` with your actual Massive API key. This command starts a Docker container based on the `massive-client-app` image, sets the `MASSIVE_API_KEY` environment variable to your provided API key, and runs your Python script inside the container.

### Additional Notes

- The Docker setup provided here is a very basic example. Depending on your specific requirements, you might need to customize the Dockerfile, such as adding volume mounts for persistent data or exposing ports for network communication.
- For more details on using the Massive API and the `massive-api-client` library, please refer to the [Massive documentation](https://massive.com/docs), the [massive-com/client-python](https://github.com/massive-com/client-python) repo, or the [massive-api-client documentation](https://massive-api-client.readthedocs.io/en/latest/).