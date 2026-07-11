from enum import Enum 
from pydantic import BaseModel


class BrowserState(str, Enum):
    CLOSED="closed"
    OPEN="open"

class SearchResult(BaseModel):
    title:str
    url:str
    snippet:str=""

class PageContent(BaseModel):
    url:str
    title:str
    markdown:str
    
class SessionState(str, Enum):
    VALID="valid"
    EXPIRED="expired"
    TERMINATED="terminated"
    UNKNOWN="unknown"

class BrowserSessionInfo(BaseModel):
    storage_state:str
    state:SessionState

class ProfileMetric(BaseModel):
    name:str
    value:str

    