from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field

class Memory(BaseModel):

    id:str=Field(
        default_factory=lambda:str(uuid4())
    )

    user_id:str
    key:str
    value:str
    created_at:datetime=Field(
        default_factory=datetime.now
    )