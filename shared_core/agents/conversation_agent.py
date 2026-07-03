from shared_core.conversation import (ConversationManager)

from .base_agent import BaseAgent 

class ConversationAgent(BaseAgent):
    def __init__(self,system_prompt:str):
        super().__init__(system_prompt)

        self.conversation=(
            ConversationManager()
        )
    
    def user(self,text:str):
        self.conversation.add_user_message(text)
    
    def assistant(self, text:str):
        self.conversation.add_assistant_message(text)

    @property
    def messages(self):
        return self.conversation.messages()
        