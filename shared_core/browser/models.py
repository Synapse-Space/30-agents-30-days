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
    