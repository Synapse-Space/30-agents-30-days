from .registry import ToolRegistry


class ToolExecuter:
    def __init__(self, registry: ToolRegistry):
        self.registry=registry


    def execute(self, tool_name:str, arguments:dict):
        tool=self.registry.get(
            tool_name
        )

        if tool is None:
            raise ValueError(f"Tool {tool_name} not found")

        return tool.execute(**arguments)