"""Service module providing health check endpoints."""

from flask import Flask, jsonify

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


if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=8080)
