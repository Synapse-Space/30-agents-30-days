from typing import Callable

class ToolRegistry:
    def __init__(self):
        self.tools={}

    def register(
        self,
        name:str,
        func:Callable
    ):

        self.tools[name]=func
    
    def execute(
        self, 
        tool_name:str,
        **kwargs
    ):
        if tool_name not in self.tools:
            raise ValueError(f"Tool '{tool_name}' not found.")

        return self.tools[tool_name](**kwargs)

