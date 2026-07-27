from shared_core.agents import SolutionArchitectAgent
from planner import EnterprisePlanner
from registry import EnterpriseRegistry
from supervisor import EnterpriseSupervisor
from workflow import EnterpriseWorkflow

class EnterpriseArchitect(SolutionArchitectAgent):
    def __init__(self, memory_manager=None):
        super().__init__("Enterprise Architect", memory_manager)
        registry = EnterpriseRegistry()
        registry.load_defaults()
        supervisor = EnterpriseSupervisor(EnterprisePlanner(), registry)
        self.workflow = EnterpriseWorkflow(supervisor)

    async def solve(self, objective):
        return await self.workflow.run(objective)

    def run(self, objective, *args, **kwargs):
        import asyncio
        return asyncio.run(self.solve(objective))
