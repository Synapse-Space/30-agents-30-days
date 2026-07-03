from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

class ChatMessage(BaseModel):
    role:Literal["system","user","assistant","tool"]
    content: str
    timestamp: datetime=Field(
        default_factory=datetime.utcnow
    )

    