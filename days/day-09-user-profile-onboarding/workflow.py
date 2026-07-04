"""
Onboarding workflow.
"""

from shared_core.workflow import (

    Workflow,

    WorkflowState,

)

from validators import (

    validate_name,

    validate_email,

    validate_phone,

    validate_country,

)


class OnboardingWorkflow(
    Workflow
):

    def __init__(self):

        super().__init__()

        self.machine.add_state(

            WorkflowState(

                name="name",

                prompt="What is your full name?",

                validator=validate_name,

                error_message=(
                    "Please enter your full name."
                ),

                next_state="email",

            )

        )

        self.machine.add_state(

            WorkflowState(

                name="email",

                prompt="What is your email address?",

                validator=validate_email,

                error_message=(
                    "Invalid email address."
                ),

                next_state="phone",

            )

        )

        self.machine.add_state(

            WorkflowState(

                name="phone",

                prompt="What is your phone number?",

                validator=validate_phone,

                error_message=(
                    "Invalid phone number."
                ),

                next_state="country",

            )

        )

        self.machine.add_state(

            WorkflowState(

                name="country",

                prompt="Which country are you from?",

                validator=validate_country,

                error_message=(
                    "Unsupported country."
                ),

                next_state="completed",

            )

        )

        self.machine.add_state(

            WorkflowState(

                name="completed",

                prompt="Profile completed.",

                terminal=True,

            )

        )

        self.start("name")