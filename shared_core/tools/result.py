from dataclasses import dataclass 
from typing import Any 

@dataclass(slots=True)
class ToolResult:
    success: bool
    message: str
    data: Any=None
    