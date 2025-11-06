# routes/health.py
# Simple health probe for demos & readiness checks.

from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Server is running"}), 200
