from enum import Enum 

from pydantic import BaseModel 

class TeamStatus(str, Enum):
    RUNNING="running"
    COMPLETED="completed"
    FAILED="failed"

class WorkerResult(BaseModel):
    worker:str 
    output:str 
    success:bool=True

class TeamResult(BaseModel):
    status: TeamStatus
    completed_workers:int 
    report:str 

    