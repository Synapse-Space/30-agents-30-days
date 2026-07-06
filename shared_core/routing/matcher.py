from abc import ABC 
from abc import abstractmethod

from .result import RouteResult

class BaseMatcher(ABC):

    @abstractmethod
    def match(self,text:str)-> RouteResult:
        pass