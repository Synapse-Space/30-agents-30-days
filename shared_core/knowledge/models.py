from dataclasses import dataclass, field
from uuid import uuid4

@dataclass(slots=True)
class Document:
    id:str=field(
        default_factory=lambda: str(uuid4())

    )
    name: str=""
    path: str=""
    content: str=""

@dataclass(slots=True)
class Chunk:
    id:str=firld(default_factory=lambda:str(uuid4()))
    document_id:str=""
    chunk_number:int=0
    text:str=""
    