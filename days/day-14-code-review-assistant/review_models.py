from enum import Enum 
from pydantic import BaseModel

class Severity(str, Enum):
    INFO="INFO"
    WARNING="WARNING"
    ERROR="ERROR"

class ReviewFinding(BaseModel):
    rule:str
    severity:Severity
    message:str 
    line:int 

class ReviewReport(BaseModel):
    findings:list[ReviewFinding]
    score:int
    