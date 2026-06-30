from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass(slots=True)
class Config:

    LLM_PROVIDER: str = os.getenv(
        "LLM_PROVIDER",
        "ollama",
    )

    OLLAMA_HOST: str = os.getenv(
        "OLLAMA_HOST",
        "http://localhost:11434",
    )

    OLLAMA_MODEL: str = os.getenv(
        "OLLAMA_MODEL",
        "qwen3:8b",
    )

    OPENAI_API_KEY: str = os.getenv(
        "OPENAI_API_KEY",
        "",
    )

    OPENAI_MODEL: str = os.getenv(
        "OPENAI_MODEL",
        "gpt-4.1",
    )

    GEMINI_API_KEY: str = os.getenv(
        "GEMINI_API_KEY",
        "",
    )

    GEMINI_MODEL: str = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.5-pro",
    )

    WEATHER_GEOCODE_URL: str = (
        "https://geocoding-api.open-meteo.com/v1/search"
    )

    WEATHER_API_URL: str = (
        "https://api.open-meteo.com/v1/forecast"
    )


config = Config()