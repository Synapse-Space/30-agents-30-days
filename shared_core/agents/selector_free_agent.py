from shared_core.automation import ActionExecutor, ActionPlanner, ActionVerifier 

from .vision_browser_agent import VisionBrowserAgent 

class SelectorFreeAgent(VisionBrowserAgent):
    def __init__(self,system_prompt, memory_manger):
        super().__init__(system_prompt,memory_manger)
        self.executor = ActionExecutor()

        self.planner = ActionPlanner()

        self.verifier = ActionVerifier()


