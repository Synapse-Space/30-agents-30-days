"""
Shared Agent Framework

Every agent in the project should inherit from BaseAgent.

Example:
    from shared_core.agents import BaseAgent
"""

from .base_agent import BaseAgent
from .structured_agent import StructuredAgent

__all__ = [
    "BaseAgent",
    "StructuredAgent"
]