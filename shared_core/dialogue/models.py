from enum import Enum 
from typing import Dict, Any 
from pydantic import BaseModel, Field

class DialogueEngine(str, Enum):
    RASA = "rasa"
    LANGGRAPH = "langgraph"
    
class DialogueRequest(BaseModel):
    session_id: str 
    message: str 

class DialogueResponse(BaseModel):
    response: str 
    engine: DialogueEngine 
    metadata: Dict[str, Any] = Field(default_factory=dict)