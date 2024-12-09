# REST Test Service

This is a simple Python REST API service built using Flask. It provides two endpoints:

- `/health`: Returns a 200 status code whenever the service is running.
- `/custom-health`: Returns a 200 status code if the environment variable `CUSTOM_HEALTH` is not set or set to `true`, and a 500 status code otherwise.

## Running Locally

1. **Create a virtual environment**:

   ```sh
   python -m venv venv
   ```

2. **Activate the virtual environment**:

   - On **Windows**:
     ```sh
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```sh
     source venv/bin/activate
     ```

3. **Install the dependencies**:

   ```sh
   pip install -r src/requirements.txt
   ```

4. **Run the service**:
   ```sh
   python src/service.py
   ```

The service will start running on `http://0.0.0.0:5000`.

## Running with Docker

1. **Build the Docker image**:

   ```sh
   docker build -t rest-test-service .
   ```

2. **Run the Docker container**:
   ```sh
   docker run -p 8080:8080 rest-test-service
   ```

The service will be available on `http://localhost:8080`.

## Running tests locally

## Endpoints

- **GET /health**

  - Returns: `{"status": "running"}` with a 200 status code.

- **GET /custom-health**
  - Returns: `{"status": "custom health is good"}` with a 200 status code if `CUSTOM_HEALTH` is not set or set to `true`.
  - Returns: `{"status": "custom health is bad"}` with a 500 status code if `CUSTOM_HEALTH` is set to `false`.

## Linting

To lint your project locally using GitHub Super-Linter, follow these steps:

1. Ensure you have Docker installed on your machine.
2. Run the following command to lint your project: `docker-compose -f docker-compose-lint.yml run --rm lint`
3. To lint and automatically fix issues, run: `docker-compose -f docker-compose-lint.yml run --rm fix`

## Running Tests

To run the tests, use the following command: `pytest`
