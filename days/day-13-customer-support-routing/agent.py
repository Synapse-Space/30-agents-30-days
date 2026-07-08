"""
Customer Support Agent
"""

from shared_core.agents import SupportAgent

from prompts import (
    NORMAL_PROMPT,
    EMPATHY_PROMPT,
)

from escalation import EscalationEngine
from mock_ticket_service import MockTicketService


class CustomerSupportAgent(SupportAgent):

    def __init__(
        self,
        memory_manager,
    ):

        super().__init__(
            NORMAL_PROMPT,
            memory_manager,
        )

        self.escalation = EscalationEngine()

        self.ticket_service = MockTicketService()

    def respond(
        self,
        user_message: str,
    ):

        emotion = self.emotions.analyze(
            user_message
        )

        escalation = self.escalation.evaluate(
            emotion
        )

        if escalation.escalate:

            ticket = self.ticket_service.create_ticket(
                user_message,
                escalation.priority.value,
            )

            prompt = f"""
{EMPATHY_PROMPT}

Customer Message:
{user_message}

Respond with empathy.
"""

            response = self.generate(prompt)

            return {

                "emotion": emotion,

                "ticket": ticket,

                "response": response,

            }

        prompt = f"""
{NORMAL_PROMPT}

Customer Message:
{user_message}
"""

        response = self.generate(prompt)

        return {

            "emotion": emotion,

            "ticket": None,

            "response": response,

        }