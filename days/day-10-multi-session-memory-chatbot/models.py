from pydantic import BaseModel

class ExtractedMemory(BaseModel):
    should_remember: bool
    key: str | None=None
    value: str | None=None
    response: str
    