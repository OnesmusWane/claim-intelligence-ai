import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Claim Intelligence AI"
    API_VERSION: str = "0.1.0"
    DEBUG: bool = True

    # Add DB or AI configs later
    DATABASE_URL: str = "postgresql://user:pass@localhost:5432/claims"

settings = Settings()