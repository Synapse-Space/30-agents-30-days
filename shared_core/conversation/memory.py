from pydantic import BaseModel, Field
from .history import ConverastionHistory

class ConverastionMemory(BaseModel):
    history: ConverastionHistory=Field(default_factory=ConverastionHistory)
    metadata: dict=Field(default_factory=dict)


    