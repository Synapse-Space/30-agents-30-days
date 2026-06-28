from typing import Optional

from pydantic import BaseModel, EmailStr, Field

class ContactInformation(BaseModel):
    name:str=Field(
        description="Full name of the sender."
    )

    company: Optional[str]=Field(
        default=None,
        description="Company name."

    )

    email:EmailStr
    phone:Optional[str]=None
    meeting_date: Optional[str]=Field(
        default=None,
        description="ISO Date (YYYY-MM-DD)"
    )
    
    meeting_time:Optional[str]=Field(
        default=None,
        description="24-hour format HH:MM"
    )

    purpose: Optional[str]=Field(
        default=None,
        description="Purpose of the email."
    )