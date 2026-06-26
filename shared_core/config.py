from dataclasses import dataclasses
import os

@dataclass
class Config:
    OLLAMA_MODEL:str=os.getenv(
        "OLLAMA_MODEL",
        "qwen3:8b"
    )

config=Config()