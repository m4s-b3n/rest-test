from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "running"}), 200


@app.route('/custom-health', methods=['GET'])
def custom_health():
    custom_health_status = os.getenv('CUSTOM_HEALTH', 'true').lower()
    if custom_health_status == 'true':
        return jsonify({"status": "custom health is good"}), 200
    else:
        return jsonify({"status": "custom health is bad"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
