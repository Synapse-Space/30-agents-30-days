from shared_core.context import (ContextManager)

from .base_agent import BaseAgent

class StatefulAgent(BaseAgent):
    def __init__(self, system_prompt: str):
        super().__init__(system_prompt)

        self.context_manager=(ContextManager())

    def load_context(self, session_id=None):
        return self.context_manager.load_context(session_id)
    
    def save_context(self,context):
        self.context_manager.save_context(context)

        