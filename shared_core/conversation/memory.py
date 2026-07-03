from pydantic import BaseModel, Field
from .history import ConversationHistory

class ConversationMemory(BaseModel):
    history: ConversationHistory=Field(default_factory=ConversationHistory)
    metadata: dict=Field(default_factory=dict)


    