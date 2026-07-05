from pydantic import BaseModel

class ExtractedMemory(BaseModel):
    should_remember: bool
    key: str
    value: str
    response: str
    