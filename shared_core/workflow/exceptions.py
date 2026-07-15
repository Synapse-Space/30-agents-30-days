class WorkflowException(Exception):
    """Base workflow exception."""


class ValidationException(
    WorkflowException,
):
    """Workflow validation failed."""