from shared_core.agents import SolutionArchtectAgent
from planner import EnterprisePlanner
from registry import EnterpriseRegistry
from supervisor import EnterpriseSupervisor
from workflow import EnterpriseWorkflow

class EnterpriseArchitect(SolutionArchtectAgent):
    def __init__(self, memory_manger):
        super().__init__("Enterprise Architect", memory_manger)
        registry=EnterpriseRegistry()
        registry.load_defaults()
        supervisor=EnterpriseSupervisor(EnterprisePlanner(), registry)
        self.workflow=EnterpriseWorkflow(supervisor)

    async def solve(self, objective):
        return await self.workflow.run(objective)
