"""Unit tests for the service endpoints."""

import unittest
from prometheus_client import REGISTRY, generate_latest
from src.service import app, health_status


class ServiceTestCase(unittest.TestCase):
    """Test case for the service endpoints."""

    def setUp(self):
        """Set up the test client and enable testing mode."""
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        """Reset the health status after each test."""
        health_status.custom_health_status = True

    def test_health(self):
        """Test the /health endpoint."""
        response = self.app.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "running"})

    def test_custom_health(self):
        """Test the /custom-health endpoint."""
        response = self.app.get("/custom-health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "custom health is good"})

    def test_toggle_health(self):
        """Test the /toggle-health endpoint."""
        response = self.app.post("/toggle-health")
        self.assertEqual(response.status_code, 200)
        self.assertIn("CUSTOM_HEALTH_STATUS set to", response.json["status"])

        # Verify that the custom health status has been toggled
        response = self.app.get("/custom-health")
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {"status": "custom health is bad"})

        # Toggle back to the original state
        response = self.app.post("/toggle-health")
        self.assertEqual(response.status_code, 200)
        self.assertIn("CUSTOM_HEALTH_STATUS set to", response.json["status"])

        response = self.app.get("/custom-health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "custom health is good"})

    def test_get_status(self):
        """Test the get_status method of HealthStatus."""
        self.assertTrue(health_status.get_status())
        health_status.toggle()
        self.assertFalse(health_status.get_status())

    def test_metrics(self):
        """Test the /metrics endpoint."""
        response = self.app.get("/metrics")
        self.assertEqual(response.status_code, 200)
        metrics_data = generate_latest()
        self.assertEqual(response.data, metrics_data)

    def test_request_count_increments(self):
        """Test that the request count increments with each request."""
        initial_count = REGISTRY.get_sample_value("request_count_total") or 0

        # Make a request to increment the count
        self.app.get("/health")
        new_count = REGISTRY.get_sample_value("request_count_total")
        self.assertEqual(new_count, initial_count + 1)

        # Make another request to increment the count again
        self.app.get("/health")
        new_count = REGISTRY.get_sample_value("request_count_total")
        self.assertEqual(new_count, initial_count + 2)


if __name__ == "__main__":
    unittest.main()
