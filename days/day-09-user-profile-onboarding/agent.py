from shared_core.agents import (
    WorkflowAgent,
)

from models import UserProfile

from workflow import (
    OnboardingWorkflow,
)

from prompts import (
    SYSTEM_PROMPT,
)

class OnboardingAgent(WorkflowAgent):
    def __init__(self):
        super().__init__(SYSTEM_PROMPT)
        self.workflow=(OnboardingWorkflow())
        self.profile=(UserProfile())

    def current_prompt(self):
        return (self.workflow.machine.state().prompt)

    def run(self, *args, **kwargs):
        pass

    
    def process(self,user_input:str):
        state=(self.workflow.machine.state())

        result=(
            self.workflow.machine.process(user_input)
        )

        if not result.success:
            return {
                "success": False,
                "message": result.message,
                "next_prompt":(
                    state.prompt
                )
            }
        
        if state.name == "name":

            self.profile.full_name = (
                user_input
            )

        elif state.name == "email":

            self.profile.email = (
                user_input
            )

        elif state.name == "phone":

            self.profile.phone = (
                user_input
            )

        elif state.name == "country":

            self.profile.country = (
                user_input
            )
        
        next_state=(self.workflow.machine.state())

        if next_state.terminal:
            self.profile.completed=True
            return {
                 "success": True,

                "completed": True,

                "profile": (
                    self.profile
                ),
            }
        
        return {

            "success": True,

            "completed": False,

            "next_prompt": (
                next_state.prompt
            ),

        }


