"""
Base Agent

Provides common functionality shared across all AI agents.

Features:
---------
✓ Conversation Management
✓ Logger
✓ LLM Client
✓ Retry Mechanism
✓ Chat Reset
✓ Helper Methods

Every future agent should inherit from this class.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from shared_core.providers.llm import LLMFactory
from shared_core.logger import logger


class BaseAgent(ABC):
    """
    Base class for all AI Agents.
    """

    MAX_RETRIES = 3

    def __init__(self, system_prompt: str | None = None):

        self.logger = logger

        self.llm = LLMFactory.create()

        self.messages: list[dict[str, Any]] = []

        if system_prompt:
            self.set_system_prompt(system_prompt)

    # ---------------------------------------------------------
    # Conversation Helpers
    # ---------------------------------------------------------

    def set_system_prompt(
        self,
        prompt: str,
    ) -> None:
        """
        Sets the system prompt.

        This replaces any existing system prompt.
        """

        if (
            self.messages
            and self.messages[0]["role"] == "system"
        ):

            self.messages[0]["content"] = prompt

        else:

            self.messages.insert(
                0,
                {
                    "role": "system",
                    "content": prompt,
                },
            )

    def add_user_message(
        self,
        message: str,
    ) -> None:

        self.messages.append(
            {
                "role": "user",
                "content": message,
            }
        )

    def add_assistant_message(
        self,
        message: str,
    ) -> None:

        self.messages.append(
            {
                "role": "assistant",
                "content": message,
            }
        )

    def add_tool_message(
        self,
        tool_name: str,
        content: str,
    ) -> None:
        """
        Used for Tool Calling (Day 2+)
        """

        self.messages.append(
            {
                "role": "tool",
                "name": tool_name,
                "content": content,
            }
        )

    # ---------------------------------------------------------
    # Chat Management
    # ---------------------------------------------------------

    def clear_history(self) -> None:
        """
        Clears conversation while preserving
        the system prompt.
        """

        if (
            self.messages
            and self.messages[0]["role"] == "system"
        ):

            self.messages = [self.messages[0]]

        else:

            self.messages = []

    @property
    def history(self):

        return self.messages

    # ---------------------------------------------------------
    # Retry Helper
    # ---------------------------------------------------------

    def retry(
        self,
        func,
        *args,
        **kwargs,
    ):
        """
        Retries a callable if it raises an exception.
        """

        last_exception = None

        for attempt in range(
            1,
            self.MAX_RETRIES + 1,
        ):

            try:

                return func(
                    *args,
                    **kwargs,
                )

            except Exception as exc:

                last_exception = exc

                self.logger.warning(
                    "Attempt %s/%s failed: %s",
                    attempt,
                    self.MAX_RETRIES,
                    exc,
                )

        raise last_exception

    # ---------------------------------------------------------
    # LLM Wrappers
    # ---------------------------------------------------------

    def chat(
        self,
        tools=None,
    ):
        """
        Simple chat completion.
        """

        return self.llm.chat(
            messages=self.messages,
            tools=tools,
        )

    def structured(
        self,
        schema,
    ):
        """
        Structured output.
        """

        return self.llm.structured(
            self.messages,
            schema,
        )

    # ---------------------------------------------------------
    # Abstract Entry Point
    # ---------------------------------------------------------

    @abstractmethod
    def run(
        self,
        *args,
        **kwargs,
    ):
        """
        Every agent must implement this.
        """
        raise NotImplementedError