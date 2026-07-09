from shared_core.code_analysis import CodeAnalyzer
from .knowledge_agent import KnowledgeAgent 

class CodeReviewAgent(KnowledgeAgent):
    def __init__(self, system_prompt,memory_manager):
        super().__init__(system_prompt,memory_manager)
        self.analyzer=CodeAnalyzer()

    
    def inspect(self, file_path:str):
        return self.analyzer.analyze(file_path)