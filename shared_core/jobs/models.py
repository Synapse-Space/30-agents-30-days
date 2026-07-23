from enum import Enum 
from pydantic import BaseModel 

class JobStatus(str, Enum):
    QUEUED="queued"
    PROCESSING="processing"
    COMPLETED="completed"
    FAILED="failed"

class Job(BaseModel):
    id:str 
    type:str 
    payload:dict 
    status: JobStatus=JobStatus.QUEUED


class JobResult(BaseModel):
    job_id:str 
    status: JobStatus 
    message:str