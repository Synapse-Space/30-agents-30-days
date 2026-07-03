from pydantic import BaseModel, Field
from .message import ChatMessage

class ConversationHistory(BaseModel):
    messages:list[ChatMessage]=Field(default_factory=list)

    def add(self,role:str, content:str):
        self.messages.append(ChatMessage(role=role, content=content))

    def clear(self):
        if not self.messages:
            return None

        return self.messages[-1]
        