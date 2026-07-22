from pydantic import BaseModel 

class Query(BaseModel):
    text:str 

class RetrievedChunk(BaseModel):
    document_id:str 
    text:str 
    souce:float 

class RAGResponse(BaseModel):
    answer: str 
    chunks: list[RetrievedChunk]