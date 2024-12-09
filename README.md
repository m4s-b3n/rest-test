# REST Test Service

This is a simple Python REST API service built using Flask. It provides three endpoints:

- `/health`: Returns a 200 status code whenever the service is running.
- `/custom-health`: Returns a 200 status code if the internal variable `custom_health_status` is `True`, and a 500 status code otherwise.
- `/toggle-health`: Toggles the internal variable `custom_health_status` between `True` and `False`.

Simply run the service using Docker:

```sh
docker run -p 8080:8080 ghcr.io/m4s-b3n/rest-test:1.1.0
```

You can run and test the service using `curl` commands:

1. **Test the `/health` endpoint**:

   ```sh
   curl -X GET http://localhost:8080/health
   ```

2. **Test the `/custom-health` endpoint**:

   ```sh
   curl -X GET http://localhost:8080/custom-health
   ```

3. **Toggle the result using the `/toggle-health` endpoint**:

   ```sh
   curl -X POST http://localhost:8080/toggle-health
   ```

## Endpoints

- **GET /health**

  - Returns: `{"status": "running"}` with a 200 status code.

- **GET /custom-health**

  - Returns: `{"status": "custom health is good"}` with a 200 status code if `custom_health_status` is `True`.
  - Returns: `{"status": "custom health is bad"}` with a 500 status code if `custom_health_status` is `False`.

- **POST /toggle-health**
  - Toggles the internal variable `custom_health_status` between `True` and `False`.
  - Returns: `{"status": "custom health toggled"}` with a 200 status code.

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

1. **Activate the virtual environment** (if not already activated):

   - On **Windows**:
     ```sh
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```sh
     source venv/bin/activate
     ```

2. **Install the dependencies** (if not already installed):

   ```sh
   pip install -r src/requirements.txt
   ```

3. **Install the test dependencies**:

   ```sh
   pip install -r test/requirements.txt
   ```

4. **Run the tests**:

   ```sh
   pytest
   ```

## Linting Locally

To lint your project locally using GitHub Super-Linter, follow these steps:

1. **Ensure you have Docker installed on your machine**

2. **Lint your project**

   ```sh
   docker-compose -f docker-compose-lint.yml run --rm lint
   ```

3. **Lint and automatically fix issues**
   ```sh
   docker-compose -f docker-compose-lint.yml run --rm fix
   ```
