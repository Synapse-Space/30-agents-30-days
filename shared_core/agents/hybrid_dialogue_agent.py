from shared_core.dialogue import ConversationState, DialoguePipeline, DialogueRouter, RasaEngine, LangGraphEngine
from .conversation_agent import ConversationAgent

class HybridDialogueAgent(ConversationAgent):
    def __init__(self, system_prompt, memory_manager=None):
        super().__init__(system_prompt)

        self.state = ConversationState(session_id="default-session")
        self.router = DialogueRouter()
        self.pipeline = DialoguePipeline(
            self.router,
            RasaEngine(),
            LangGraphEngine()
        )