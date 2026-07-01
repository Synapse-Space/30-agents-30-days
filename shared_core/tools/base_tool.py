from abc import ABC 
from abc import abstractmethod
from .result import ToolResult

class BaseTool(ABC):
    name:str=""
    description:str=""
    parameters: dict={}

    @abstractmethod
    def execute(self, **kwargs)->ToolResult:
        pass

    def schema(self):
        return {
            "type":"function",
            "function":{
                "name":self.name,
                "description":self.description,
                "parameters":self.parameters
            }
        }