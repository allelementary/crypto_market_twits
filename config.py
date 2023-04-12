import os

from pydantic import BaseSettings


class Config(BaseSettings):
    API_ID: str = os.environ.get("API_ID")
    API_HASH: str = os.environ.get("API_HASH")
    TARGET_CHANNEL: str = os.environ.get("TARGET_CHANNEL")
    DESTINATION_CHANNEL: str = os.environ.get("DESTINATION_CHANNEL")

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


config = Config(_env_file='.env')
