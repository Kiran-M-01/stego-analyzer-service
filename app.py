from flask import Flask
from config import Config
from routes.analyze import analyze_bp
from flask import Flask, render_template, request

from utils.image_loader import ImageLoader
from analyzer.report import ReportAnalyzer
from utils.validators import allowed_file


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(analyze_bp)

    return app


app = create_app()
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze-web", methods=["GET", "POST"])
def analyze_web():

    if request.method == "GET":
        return render_template("index.html")

    if "image" not in request.files:
        return render_template(
            "index.html",
            error="No image uploaded."
        )

    file = request.files["image"]

    if file.filename == "":
        return render_template(
            "index.html",
            error="No file selected."
        )

    if not allowed_file(file.filename):
        return render_template(
            "index.html",
            error="Unsupported file format."
        )

    image, metadata = ImageLoader.load_image(file)

    report = ReportAnalyzer.analyze(image)

    return render_template(
        "index.html",
        metadata=metadata,
        analysis=report
    )



if __name__ == "__main__":
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )