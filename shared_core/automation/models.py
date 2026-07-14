from enum import Enum 
from pydantic import BaseModel 

class ActionType(str,Enum):
    CLICK="click"
    DOUBLE_CLICK="double_click"
    RIGHT_CLICK="right_click"
    HOVER="hover"


class ActionResult(str,Enum):
    SUCCESS="success"
    FAILED="failed"
    

class MousePoint(BaseModel):

    x: int

    y: int


class AutomationAction(BaseModel):

    action: ActionType

    target: str

    point: MousePoint


class AutomationResponse(BaseModel):

    result: ActionResult

    message: str