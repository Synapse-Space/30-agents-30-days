from datetime import datetime 
from enum import Enum 
from pydantic import BaseModel 

class JobStatus(str, Enum):
    PENDING = "pending"   
    RUNNING="running"
    RETRYING="retrying"
    SUCCESS="success"
    FAILED="failed"

class ErrorContext(BaseModel):
    exception_type:str 
    message:str 
    traceback:str 

class RecoveryJob(BaseModel):
    job_id:str 
    attempts:int=0
    max_attempts:int=3
    status: JobStatus=JobStatus.PENDING
    created_at:datetime=datetime.utcnow()

class RepairSuggestion(BaseModel):
    fixed_input:dict 
    explanation:str 
    retry: bool=True 
    
