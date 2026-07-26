class WorkflowException(
    Exception,
):
    """Base workflow exception."""


class AgentNotFound(
    WorkflowException,
):
    """Unknown agent."""