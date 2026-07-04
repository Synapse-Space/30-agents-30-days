from dataclasses import dataclass 
from typing import Callable

@dataclass(slots=True)
class WorkflowState:
    name: str
    prompt: str
    validator: Callable[[str],bool] | None = None 
    error_message: str="Invalid Input."
    next_state:str|None=None
    terminal: bool=False
    