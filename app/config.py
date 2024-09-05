import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:example@postgres/postgres"

settings = Settings()