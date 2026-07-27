from shared_core.orchestration import WorkflowEngine, Supervisor, WorkflowPlanner, AgentRegistry

from .base_agent import BaseAgent

class SolutionArchtectAgent(BaseAgent):
    def __init__(self, system_prompt, memory_manger):
        super().__init__(system_prompt, memory_manger)
        self.registry=AgentRegistry()

        self.supervisor=Supervisor(planner=None, registry=self.registry)

        self.workflow=WorkflowEngine(self.supervisor)