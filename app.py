from flask import Flask
from config import Config
from routes.analyze import analyze_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(analyze_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )