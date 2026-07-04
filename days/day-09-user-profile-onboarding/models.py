from pydantic import BaseModel

class UserProfile(BaseModel):
    full_name: str | None=None
    email: str | None=None
    phone: str | None=None
    country: str | None=None
    completed: bool=False
    
