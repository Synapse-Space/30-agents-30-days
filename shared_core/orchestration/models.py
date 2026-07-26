from pygments.lexer import default
from enum import Enum 
from datetime import datetime
from pydantic import BaseModel, Field

class TaskStatus(str, Enum):
    PENDING="pending"
    RUNNING="running"
    COMPLETED="completed"
    FAILED="failed"

class WorkflowTask(BaseModel):
    id:str 
    name:str 
    agent:str 
    status: TaskStatus=TaskStatus.PENDING
    dependencies:list[str]=Field(default_factory=list)


class WorkflowResult(BaseModel):
    workflow_id:str 
    status:TaskStatus
    completed_tasks:int 
    created_at:datetime=Field(default_factory=datetime.utcnow)
    