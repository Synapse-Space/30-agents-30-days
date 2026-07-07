from pydantic import BaseModel 

class FAQ(BaseModel):
    question:str
    answer:str
    

class UnknownQuestion(BaseModel):
    question:str
