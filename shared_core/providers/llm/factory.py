from shared_core.config import config
from .ollama_client import OllamaClient
# from .openai_client import OpenAIClient
# from .gemini_client import GeminiClient

class LLMFactory:
    @staticmethod
    def create():
        provider=config.LLM_PROVIDER.lower()

        if provider=="ollama":
            return OllamaClient()
        # elif provider == "openai":
        #     return OpenAIClient()
        # elif provider == "gemini":
        #     return GeminiClient()
        else:
            raise ValueError(f"Unknown LLM provider: {provider}")

   
        