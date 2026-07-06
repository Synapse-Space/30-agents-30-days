from dataclasses import dataclass

@dataclass(slots=True)
class RouteResult:
    matched:bool
    route:Route | None
    confidence:float 
    message:str 
