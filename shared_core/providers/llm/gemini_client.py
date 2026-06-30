from openai import OpenAI

from shared_core.config import config

from .base import BaseLLM


class OpenAIClient(BaseLLM):

    def __init__(self):

        self.client = OpenAI(
            api_key=config.OPENAI_API_KEY
        )

    def chat(
        self,
        messages,
        tools=None,
        format=None,
    ):

        return self.client.responses.create(
            model=config.OPENAI_MODEL,
            input=messages,
            tools=tools,
        )

    def structured(
        self,
        messages,
        schema,
    ):

        response = self.client.responses.parse(
            model=config.OPENAI_MODEL,
            input=messages,
            text_format=schema,
        )

        return response.output_parsed
