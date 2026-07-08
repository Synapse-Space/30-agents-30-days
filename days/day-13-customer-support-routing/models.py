from enum import Enum 
from pydantic import BaseModel 

class TicketPriority(str, Enum):
    LOW="LOW"
    MEDIUM="MEDIUM"
    HIGH="HIGH"


class EscalationResult(BaseModel):
    escalate:bool
    priority: TicketPriority
    reason: str
    
