import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    GOOGLE_TOKEN_ENDPOINT: str = "https://oauth2.googleapis.com/token"
    GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET: str = os.getenv("GOOGLE_CLIENT_SECRET")
    REDIRECT_URI: str = "http://localhost:8000/callback"

    MONGO_DB_URI: str = os.getenv("MONGO_DB_FAST_CHAT_URI")


settings = Settings()
