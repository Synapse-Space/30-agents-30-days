from .models import (
    DialogueEngine,
)


class DialogueRouter:

    def route(
        self,
        message: str,
        state,
    ) -> DialogueEngine:
        """
        Decide which engine
        should handle the message.
        """

        raise NotImplementedError