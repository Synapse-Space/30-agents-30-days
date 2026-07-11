from shared_core.browser import BrowserSession 

from .browser_agent import BrowserAgent 

class AuthenticatedBrowserAgent(BaseAgent):
    def __init__(self, system_prompt, memory_manager):
        super().__init__(system_prompt,memory_manager)

    def open_authenticated_browser(self, headless=True,storage_state="storage_state.json"):
        return BrowserSession(headless=headless,storage_state=storage_state)