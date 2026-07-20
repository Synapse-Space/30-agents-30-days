class MultiAgentException(Exception):
    """Base multi-agent exception."""


class WorkerExecutionError(
    MultiAgentException,
):
    """Worker execution failed."""