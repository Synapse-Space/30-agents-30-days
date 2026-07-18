class GraphException(Exception):
    """Base graph exception."""


class NodeExecutionError(
    GraphException,
):
    """Node execution failed."""
    