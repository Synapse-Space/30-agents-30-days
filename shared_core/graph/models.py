from enum import Enum 
from pydantic import BaseModel 

class GraphStatus(str, Enum):
    RUNNING="running"
    FINISHED="finished"
    FAILED="failed"

class ReflectionResult(BaseModel):
    score:float
    feedback:str 
    approved:bool 

class GraphResult(BaseModel):
    status: GraphStatus 
    iterations: int 
    output: str 

