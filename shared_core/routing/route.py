from dataclasses import dataclass 

@dataclass(slots=True)
class Route:
    name:str
    handler:str
    decription:str=""
    confidence_threshold:float=0.75