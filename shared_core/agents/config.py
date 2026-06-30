from dataclasses import dataclass
from typing import Type

from  pydantic import BaseModel

@dataclass(slots=True)
class AgentConfig:
    name:str
    description:str
    system_prompt:str
    output_schema:Type[BaseModel]
    temperature:float=0.2
    max_retries:int=3 
    