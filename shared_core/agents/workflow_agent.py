from shared_core.workflow import Workflow
from .conversation_agent import (ConversationAgent)

class WorkflowAgent(ConversationAgent):
    def __init__(self,system_prompt:str):
        super().__init__(system_prompt)

        self.workflow=Workflow()