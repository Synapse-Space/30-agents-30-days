from pathlib import Path 
from pydantic import BaseModel


class FunctionInfo(BaseModel):
    name:str
    line:int
    arguments:list[str]
    has_docstring:bool
    has_return_annotation: bool 
    decorators:list[str]


class ClassInfo(BaseModel):
    name:str
    line:int
    methods:list[str]
    has_docstring:bool


class ModuleInfo(BaseModel):
    path:str
    imports:list[str]
    functions:list[FunctionInfo]
    classes:list[ClassInfo]