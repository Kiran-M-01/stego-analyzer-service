from flask import Blueprint, jsonify

analyze_bp = Blueprint("analyze", __name__)


@analyze_bp.route("/health", methods=["GET"])
def health():
    return jsonify(
        {
            "status": "healthy",
            "service": "Stego Analyzer Service",
            "version": "1.0.0"
        }
    )