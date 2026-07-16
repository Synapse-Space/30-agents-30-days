
from shared_core.workflow import (

    WorkflowPlanner,

    WorkflowExecutor,

    WorkflowValidator,

    WorkflowQueue,

    WorkflowState,

)

from .selector_free_agent import (

    SelectorFreeAgent,

)


class WorkflowAutomationAgent(

    SelectorFreeAgent

):

    def __init__(

        self,

        system_prompt,

        memory_manager,

    ):

        super().__init__(

            system_prompt,

            memory_manager,

        )

        self.state = WorkflowState()

        self.queue = WorkflowQueue()

        self.planner = WorkflowPlanner()

        self.executor = WorkflowExecutor()

        self.validator = WorkflowValidator()