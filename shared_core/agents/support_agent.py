from shared_core.emotion import EmotionAnalyzer

from .knowledge_agent import KnowledgeAgent 

class SupportAgent(KnowledgeAgent):
    def __init__(self,system_prompt,memory_manager):
        super().__init__(system_prompt,memory_manager)
        self.emotion_analyzer=EmotionAnalyzer()
