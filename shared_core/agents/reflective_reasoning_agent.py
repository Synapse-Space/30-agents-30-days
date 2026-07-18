from shared_core.graph import GraphState, ReflectionController, GraphBuilder 

from .content_delivery_agent import ContentDeliveryAgent 

class ReflectionReasoningAgent(ContentDeliveryAgent):
    def __init__(self, system_prompt, memory_manager):
        super().__init__(system_prompt, memory_manager)

        self.state=GraphState()
        self.controller=ReflectionController()
        self.graph=GraphBuilder()
        