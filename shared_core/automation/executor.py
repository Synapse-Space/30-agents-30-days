from .mouse import MouseController
from .models import AutomationAction 

class ActionExecutor:
    def __init__(self):
        self.mouse=MouseController()

    def execute(self,page,action:AutomationAction):
        if action.action.value=="click":
            self.mouse.click(page,action.point)

        elif action.action.value=="hover":
            self.mouse.hover(page,action.point)