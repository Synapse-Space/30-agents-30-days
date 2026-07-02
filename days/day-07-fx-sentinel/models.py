from pydantic import BaseModel

class WatchRule(BaseModel):
    base:str
    target:str
    threshold:float
    direction:str #above or below
    