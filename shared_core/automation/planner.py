from .models import AutomationAction,ActionType,MousePoint

class ActionPlanner:
    def build(self,label,coordinates):
        return AutomationAction(
            action=ActionType.CLICL,
            target=label,
            point=MousePoint(x=coordinates[0],y=coordinates[1])
        )

        