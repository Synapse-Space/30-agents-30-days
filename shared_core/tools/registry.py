
from typing import Dict

from .base_tool import BaseTool


class ToolRegistry:

    def __init__(self):

        self.tools: Dict[
            str,
            BaseTool,
        ] = {}

    def register(
        self,
        tool: BaseTool,
    ):

        self.tools[
            tool.name
        ] = tool

    def get(
        self,
        name: str,
    ):

        return self.tools.get(name)

    def schemas(self):

        return [

            tool.schema()

            for tool in self.tools.values()

        ]

    def list_tools(self):

        return list(
            self.tools.keys()
        )