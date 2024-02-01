# Dockerized Python Application with Polygon API Client

This Docker setup provides a ready-to-use environment for running Python scripts that utilize the `polygon-api-client` for financial data processing. It encapsulates the Python environment and the `polygon-api-client` library in a Docker container, making it easy to deploy and run the application consistently across any system with Docker installed. This approach is particularly useful for developers looking to integrate Polygon's financial data APIs into their applications without worrying about environment inconsistencies.

### Prerequisites

- [Docker](https://www.docker.com/) installed on your machine
- [Polygon.io](https://polygon.io/) account and API key

### Setup and Configuration

1. Clone the repository or download the Dockerfile and your Python script into a directory.
2. Use Docker's `--env` flag when running the container to set the `POLYGON_API_KEY` environment variable dynamically, or replace `<your_api_key>` in the Dockerfile with your Polygon API key (not recommended for production or shared environments).
3. Ensure your Python script (e.g., `app.py`) is in the same directory as the Dockerfile.

### Building the Docker Image

Any modifications to the Python script will require rebuilding the Docker image to reflect the changes in the containerized environment. Use the docker build command each time your script is updated to ensure the latest version is used in your Docker container.

Navigate to the directory containing your Dockerfile and execute the following command to build your Docker image:

```
docker build -t polygon-client-app .
```

This command creates a Docker image named `polygon-client-app` based on the instructions in your Dockerfile.

### Running the Docker Container

Run your Docker container using the following command:

```
docker run --env POLYGON_API_KEY="<your_api_key>" polygon-client-app
```

Replace `<your_api_key>` with your actual Polygon API key. This command starts a Docker container based on the `polygon-client-app` image, sets the `POLYGON_API_KEY` environment variable to your provided API key, and runs your Python script inside the container.

### Additional Notes

- The Docker setup provided here is a very basic example. Depending on your specific requirements, you might need to customize the Dockerfile, such as adding volume mounts for persistent data or exposing ports for network communication.
- For more details on using the Polygon API and the `polygon-api-client` library, please refer to the [Polygon documentation](https://polygon.io/docs), the [polygon-io/client-python](https://github.com/polygon-io/client-python) repo, or the [polygon-api-client documentation](https://polygon-api-client.readthedocs.io/en/latest/).