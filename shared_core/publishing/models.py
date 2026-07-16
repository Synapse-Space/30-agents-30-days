from enum import Enum 
from pydantic import BaseModel 

class PublishStatus(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    FAILED= "failed"


class ContentType(str, Enum):
    BLOG="blog"
    ARTICLE="article"
    DOCUMENTATION="documentation"


class ContentDraft(BaseModel):
    title:str 
    body:str 
    content_type:ContentType 


class PublishResult(BaseModel):
    status: PublishStatus 
    preview_url: str| None = None 
    message: str