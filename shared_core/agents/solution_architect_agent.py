from shared_core.orchestration import WorkflowEngine, Supervisor, WorkflowPlanner, AgentRegistry
from .base_agent import BaseAgent

class SolutionArchitectAgent(BaseAgent):
    def __init__(self, system_prompt: str = "Solution Architect Agent", memory_manager=None):
        super().__init__(system_prompt)
        self.registry = AgentRegistry()
        self.supervisor = Supervisor(planner=None, registry=self.registry)
        self.workflow = WorkflowEngine(self.supervisor)

    def run(self, objective, *args, **kwargs):
        import asyncio
        return asyncio.run(self.solve(objective))

    async def solve(self, objective):
        return await self.workflow.run(objective)

# Alias to support both SolutionArchitectAgent and SolutionArchtectAgent
SolutionArchtectAgent = SolutionArchitectAgent