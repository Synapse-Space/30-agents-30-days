from enum import Enum 
from pydantic import BaseModel

class PriceStatus(str, Enum):
    INCREASED="INCREASED"
    DECREASED="DECREASED"
    UNCHANGED="UNCHANGED"


class PriceChange(BaseModel):
    title:str
    previous:float
    current:float
    difference:float
    percentage:float
    status:PrinceStatus

    