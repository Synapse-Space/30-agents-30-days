from shared_core.browser import (BrowserSession, SearchEngine)

from .knowledge_agent import KnowledgeAgent 

class BrowserAgent(KnowledgeAgent):
    def __init__(self,system_prompt,memory_manager):
        super().__init__(system_prompt,memory_manager)
        self.search_engine=SearchEngine()

    def open_browser(self, headless=True):
        return BrowserSession(headless=headless)