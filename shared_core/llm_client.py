""" 
LLM Wrapper

Default: Ollama

Alternatives: OpenAI, Gemini

"""
import json

from ollama import Client

from shared_core.config import config


class LLMClient:

    def __init__(self):

        self.client = Client()

        self.model = config.OLLAMA_MODEL

    def chat(
        self,
        messages,
        tools=None,
        format=None,
    ):

        return self.client.chat(
            model=self.model,
            messages=messages,
            tools=tools,
            format=format,
        )

    def structured(
        self,
        messages,
        schema,
    ):
        """
        Ask the model to return JSON matching
        a Pydantic schema.
        """

        response = self.chat(
            messages=messages,
            format=schema.model_json_schema(),
        )

        return response["message"]["content"]

# from openai import OpenAI
#
# class LLMClient:
#
#     def __init__(self):
#         self.client = OpenAI()
#
#     def structured(
#         self,
#         messages,
#         schema,
#     ):
#
#         response = self.client.responses.parse(
#             model="gpt-4.1",
#             input=messages,
#             text_format=schema,
#         )
#
#         return response.output_parsed

# ---------------------------------------
# Gemini
# ---------------------------------------

# import google.generativeai as genai
#
# class LLMClient:
#
#     def __init__(self):
#
#         genai.configure(
#             api_key=os.getenv("GOOGLE_API_KEY")
#         )
#
#         self.model = genai.GenerativeModel(
#             "gemini-2.5-pro"
#         )
#
#     def invoke(self, messages):
#
#         prompt = "\n".join(
#             f"{m['role']}: {m['content']}"
#             for m in messages
#         )
#
#         return self.model.generate_content(
#             prompt
#         ).text