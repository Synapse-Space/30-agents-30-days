"""
Generic workflow engine.
"""

from .state import WorkflowState
from .transition import TransitionResult


class WorkflowMachine:

    def __init__(self):

        self.states: dict[str, WorkflowState] = {}

        self.current_state: str | None = None

    def add_state(
        self,
        state: WorkflowState,
    ):

        self.states[state.name] = state

    def start(
        self,
        state_name: str,
    ):

        self.current_state = state_name

    def state(self):

        return self.states[
            self.current_state
        ]

    def process(
        self,
        value: str,
    ) -> TransitionResult:

        state = self.state()

        if state.validator:

            if not state.validator(
                value
            ):

                return TransitionResult(

                    success=False,

                    current_state=state.name,

                    next_state=state.name,

                    message=state.error_message,

                )

        previous = state.name

        self.current_state = (
            state.next_state
        )

        return TransitionResult(

            success=True,

            current_state=previous,

            next_state=self.current_state,

            message="Accepted",

        )