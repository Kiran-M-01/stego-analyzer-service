from flask import Blueprint, jsonify, request

from utils.validators import allowed_file
from utils.image_loader import ImageLoader
from analyzer.report import ReportAnalyzer
import time

analyze_bp = Blueprint("analyze", __name__)


@analyze_bp.route("/health", methods=["GET"])
def health():
    return jsonify(
        {
            "status": "healthy",
            "service": "Stego Analyzer Service",
            "version": "1.0.0",
            "author": "Kiran",
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
        
        start = time.perf_counter()

        image, metadata = ImageLoader.load_image(file)

        report = ReportAnalyzer.analyze(image)

        processing_time = round(
            time.perf_counter() - start,
            3
        )

        return jsonify(
            {
                "status": "success",
                "message": "Image analyzed successfully.",
                "processing_time_seconds": processing_time,
                "metadata": metadata,
                "analysis": report,
            }
        )
        


    except Exception as e:

        return jsonify(
            {
                "status": "error",
                "message": "Failed to analyze image.",
                "message": str(e),
            }
        ), 500