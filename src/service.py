"""Service module providing health check endpoints."""

from flask import Flask, jsonify
from prometheus_client import generate_latest, Counter

app = Flask(__name__)


class HealthStatus:
    """Class to manage the custom health status."""

    def __init__(self):
        """Initialize the HealthStatus with default value."""
        self.custom_health_status = True

    def toggle(self):
        """Toggle the custom health status and return the new status."""
        self.custom_health_status = not self.custom_health_status
        return self.custom_health_status

    def get_status(self):
        """Return the current custom health status."""
        return self.custom_health_status


health_status = HealthStatus()


class RequestCounter:
    """Class to manage the request count."""

    def __init__(self):
        """Initialize the RequestCounter with a Prometheus counter."""
        self.counter = Counter("request_count", "Total number of requests")

    def increment(self):
        """Increment the request count."""
        self.counter.inc()

    def get_metrics(self):
        """Return the current Prometheus metrics."""
        return generate_latest()


request_counter = RequestCounter()


@app.before_request
def before_request():
    """Increment the request count before each request."""
    request_counter.increment()


@app.route("/health", methods=["GET"])
def health():
    """Return the health status of the service."""
    return jsonify({"status": "running"}), 200


@app.route("/custom-health", methods=["GET"])
def custom_health():
    """Return the custom health status based on the internal CUSTOM_HEALTH_STATUS variable."""
    if health_status.get_status():
        return jsonify({"status": "custom health is good"}), 200
    return jsonify({"status": "custom health is bad"}), 500


@app.route("/toggle-health", methods=["POST"])
def toggle_health():
    """Toggle the internal CUSTOM_HEALTH_STATUS variable."""
    status = health_status.toggle()
    return (
        jsonify({"status": f"CUSTOM_HEALTH_STATUS set to {status}"}),
        200,
    )


@app.route("/metrics", methods=["GET"])
def metrics():
    """Return Prometheus metrics."""
    return request_counter.get_metrics(), 200


if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=8080)
