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

    confidence: float=Field(
        ge=0,
        le=1,
        description="Confidence score between 0 and 1."
    )

    draft_response:str