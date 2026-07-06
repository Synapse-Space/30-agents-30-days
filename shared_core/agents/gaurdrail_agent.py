from shared_core.routing import Router
from .memory_agent import MemoryAgent 

class GaurdrailAgent(MemoryAgent):
    def __init__(self,system_prompt,memory_manager):
        super().__init__(system_prompt,memory_manager)

        self.router = Router()

    