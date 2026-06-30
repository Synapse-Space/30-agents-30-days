from  typing import Literal
from pydantic import BaseModel
from pydantic import Field

class EmailResponse(BaseModel):
    intent: Literal[
        "support",
        "sales",
        "spam",
        "general"
    ]=Field(
        description="Intent of the email."
    )

    priority:Literal[
        "low",
        "medium",
        "high",
    ]

    sentiment: Literal[
        "positive",
        "neutral",
        "negative",
    ]
    summary:str 
    draft_response:str