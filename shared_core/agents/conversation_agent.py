from shared_core.conversation import (ConversationManager)

from .base_agent import BaseAgent 

from shared_core.json_parser import JSONParser
from shared_core.validator import Validator

class ConversationAgent(BaseAgent):
    def __init__(self,system_prompt:str):
        super().__init__(system_prompt)
        self.conversation = ConversationManager()
        # Add system prompt to our custom conversation manager
        self.conversation.memory.history.add("system", system_prompt)
    
    def user(self,text:str):
        self.conversation.add_user_message(text)
    
    def assistant(self, text:str):
        self.conversation.add_assistant_message(text)

    def generate_structured_output(self, text: str, schema):
        # Convert ChatMessage objects to dicts for the LLM
        msgs = [
            {"role": m.role, "content": m.content} 
            for m in self.conversation.messages()
        ]
        response = self.llm.structured(msgs, schema)
        json_data = JSONParser.parse(response)
        return Validator.validate(json_data, schema)
        