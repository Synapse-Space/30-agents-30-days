from enum import Enum 

from pydantic import BaseModel

class UIElementType(str, Enum):
    BUTTON="button"
    INPUT="input"
    LINK="link"
    IMAGE="image"
    TEXT="text"
    UNKNOWN="unknown"

class BoundingBox(BaseModel):
    x:int 
    y:int 
    width:int 
    height:int 

class UIElement(BaseModel):
    label:str 
    element_type:UIElementType
    bounding_box:BoundingBox
    confidence:float

class VisionResult(BaseModel):
    elements:list[UIElement]