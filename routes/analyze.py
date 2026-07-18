from flask import Blueprint, jsonify, request

from utils.validators import allowed_file
from utils.image_loader import ImageLoader
from analyzer.report import ReportAnalyzer

analyze_bp = Blueprint("analyze", __name__)


@analyze_bp.route("/health", methods=["GET"])
def health():
    return jsonify(
        {
            "status": "healthy",
            "service": "Stego Analyzer Service",
            "version": "1.0.0",
        }
    )


@analyze_bp.route("/analyze", methods=["POST"])
def analyze():

    if "image" not in request.files:
        return jsonify(
            {
                "status": "error",
                "message": "No image uploaded."
            }
        ), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify(
            {
                "status": "error",
                "message": "No file selected."
            }
        ), 400

    if not allowed_file(file.filename):
        return jsonify(
            {
                "status": "error",
                "message": "Unsupported file format."
            }
        ), 400

    try:

        image, metadata = ImageLoader.load_image(file)

        report = ReportAnalyzer.analyze(image)

        return jsonify(
            {
                "status": "success",
                "metadata": metadata,
                "analysis": report,
            }
        )

    except Exception as e:

        return jsonify(
            {
                "status": "error",
                "message": str(e),
            }
        ), 500