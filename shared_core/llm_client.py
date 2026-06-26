""" 
LLM Wrapper

Default: Ollama

Alternatives: OpenAI, Gemini

"""
import os
from ollama import chat

class LLMClient:
    def __init__(
        self,
        model="qwen3-8b"
    );
        self.model=model
    
    def invoke(self,messages):
        response=chat(
            model=self.model,
            messages=messages
        )
        return response["message"]["content"]

# ---------------------------------------
# OpenAI
# ---------------------------------------

# from openai import OpenAI
#
# class LLMClient:
#
#     def __init__(self):
#         self.client = OpenAI(
#             api_key=os.getenv("OPENAI_API_KEY")
#         )
#
#     def invoke(self, messages):
#
#         response = self.client.chat.completions.create(
#             model="gpt-4.1",
#             messages=messages
#         )
#
#         return response.choices[0].message.content


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