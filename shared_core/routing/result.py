from dataclasses import dataclass
from .route import Route

@dataclass(slots=True)
class RouteResult:
    matched:bool
    route:Route | None
    confidence:float 
    message:str 
