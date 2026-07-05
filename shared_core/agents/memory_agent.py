from shared_core.memory import MemoryManager

from .conversation_agent import ConversationAgent 

class MemoryAgent(ConversationAgent):
    def __init__(self, system_prompt, memory_manager):
        super().__init__(system_prompt)
        self.memory=(memory_manager)


    
