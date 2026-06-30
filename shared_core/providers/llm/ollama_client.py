from ollama import Client
from shared_core.config import config
from .base import BaseLLM

class OllamaClient(BaseLLM):
    def __init(self):
        self.client=Client(
            host=config.OLLAMA_HOST
        )
        self.model=config.OLLAMA_MODEL

    def chat(
        self,
        messages,
        tools=None
        ,format=None
    ):
        return self.client.chat(
            model=self.model,
            messages=messages,
            tools=tools,
            format=format,
        )
    
    def structured( self,messages, schema):
        response=self.chat(messages,format=schema.model_json_schema())

        return response["message"]["content"]