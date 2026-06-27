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
        tools=None
    ):

        response = self.client.chat(
            model=self.model,
            messages=messages,
            tools=tools
        )

        return response


# from openai import OpenAI
#
# class LLMClient:
#
#     def __init__(self):
#
#         self.client = OpenAI()
#
#     def chat(
#         self,
#         messages,
#         tools=None
#     ):
#
#         return self.client.chat.completions.create(
#             model="gpt-4.1",
#             messages=messages,
#             tools=tools
#         )

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