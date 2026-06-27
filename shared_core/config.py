from dataclasses import dataclasses
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    OLLAMA_MODEL:str=os.getenv(
        "OLLAMA_MODEL",
        "qwen3:8b"
    )

    WEATHER_GEOCODE_URL: str = (
        "https://geocoding-api.open-meteo.com/v1/search"
    )

    WEATHER_API_URL: str = (
        "https://api.open-meteo.com/v1/forecast"
    )

config=Config()