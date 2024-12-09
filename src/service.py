"""Service module providing health check endpoints."""

import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    """Return the health status of the service."""
    return jsonify({"status": "running"}), 200


@app.route("/custom-health", methods=["GET"])
def custom_health():
    """Return the custom health status based on the CUSTOM_HEALTH environment variable."""
    custom_health_status = os.getenv("CUSTOM_HEALTH", "true").lower()
    if custom_health_status == "true":
        return jsonify({"status": "custom health is good"}), 200
    return jsonify({"status": "custom health is bad"}), 500


if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=8080)
