"""Unit tests for the service endpoints."""

import os
import unittest
from src.service import app


class ServiceTestCase(unittest.TestCase):
    """Test case for the service endpoints."""

    def setUp(self):
        """Set up the test client and enable testing mode."""
        self.app = app.test_client()
        self.app.testing = True

    def test_health(self):
        """Test the /health endpoint."""
        response = self.app.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "running"})

    def test_custom_health_default(self):
        """Test the /custom-health endpoint with default environment variable."""
        response = self.app.get("/custom-health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "custom health is good"})

    def test_custom_health_true(self):
        """Test the /custom-health endpoint with CUSTOM_HEALTH set to 'true'."""
        os.environ["CUSTOM_HEALTH"] = "true"
        response = self.app.get("/custom-health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "custom health is good"})

    def test_custom_health_false(self):
        """Test the /custom-health endpoint with CUSTOM_HEALTH set to 'false'."""
        os.environ["CUSTOM_HEALTH"] = "false"
        response = self.app.get("/custom-health")
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {"status": "custom health is bad"})


if __name__ == "__main__":
    unittest.main()
