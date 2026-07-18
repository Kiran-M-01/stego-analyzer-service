import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 5000))
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"

    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB

    UPLOAD_FOLDER = "uploads"

    ALLOWED_EXTENSIONS = {
        "png",
        "jpg",
        "jpeg"
    }