from shared_core.multi_agent import TeamState, Supervisor, ResultAggregator, MultiAgentBuilder

from .reflective_reasoning_agent import ReflectionReasoningAgent 

class ParallelResearchAgent(ReflectionReasoningAgent):
    def __init__(self, system_prompt, memory_manager):
        super().__init__(system_prompt, memory_manager)

        self.state=TeamState()
        self.supervisor=Supervisor()
        self.aggregator=ResultAggregator()
        self.team=MultiAgentBuilder()
