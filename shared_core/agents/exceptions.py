"""
Common Agent Exceptions
"""


class AgentException(Exception):
    """Base exception for all agents."""


class ValidationFailure(AgentException):
    """Raised when output validation fails."""


class MaxRetriesExceeded(AgentException):
    """Raised when retry limit is reached."""