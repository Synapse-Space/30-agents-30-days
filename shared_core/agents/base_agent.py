from abc import ABC, abstractmethod
from shared_core.llm_client import LLMClient
from shared_core.logger import logger

class BaseAgent(ABC):
    def __init__(self):
        self.logger=logger
        self.llm=LLMClient()
        self.messages=[]

    def add_system_prompt(self, prompt:str):
        self.messages.append({"role":"system","content":prompt})

    def add_user_message(self,message:str):
        self.messages.append({"role":"user","content":message})

    def add_assistant_message(self,message:str):
        self.messages.append({"role":"assistant","content":message})

    def clear_chat(self):
        system_prompt=self.messages[0]
        self.messages=[system_prompt]
    
    @abstractmethod
    def run(self, user_input:str):
        """
        Every agent implements this.
        """
        ...