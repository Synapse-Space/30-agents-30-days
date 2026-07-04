from dataclasses import dataclass

@dataclass(slots=True)
class TransitionResult:
    success:bool
    current_state:str
    next_state:str|None
    message:str

