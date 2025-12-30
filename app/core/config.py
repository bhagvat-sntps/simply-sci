# This file contains app configuration/Envs settings.

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PORT: int = 8000
    HOST: str = "0.0.0.0"  
    debug: bool = True
    API_TOKEN: str = None

    class Config:
        env_file = ".env"

settings = Settings()