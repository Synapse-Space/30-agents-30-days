from enum import Enum
from pydantic import BaseModel 

class WorkflowStatus(str, Enum):

    PENDING = "pending"

    RUNNING = "running"

    COMPLETED = "completed"

    FAILED = "failed"


class StepType(str, Enum):

    INPUT = "input"

    CLICK = "click"

    VALIDATE = "validate"

    SUBMIT = "submit"


class WorkflowStep(BaseModel):

    id: int

    name: str

    action: StepType

    payload: dict = {}


class WorkflowResult(BaseModel):

    status: WorkflowStatus

    completed_steps: int

    message: str
