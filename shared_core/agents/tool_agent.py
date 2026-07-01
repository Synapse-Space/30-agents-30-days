from shared_core.agents.base_agent import BaseAgent 
from shared_core.tools.result import ToolResult
from shared_core.tools.executer import ToolExecuter

class ToolAgent(BaseAgent):
    def __init__(self, system_prompt:str):
        super().__init__(system_prompt)
        self.registry=ToolRegistry()
        self.executor=ToolExecuter(self.registry)

        
    def register_tool(self,tool):
        self.registry.register(tool)

    def available_tools(self):
        return self.registry.schemas()
