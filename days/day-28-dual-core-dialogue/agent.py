
from shared_core.agents import (
    HybridDialogueAgent,
)

from rasa_engine import (
    EnterpriseRasaEngine,
)

from langgraph_engine import (
    EnterpriseLangGraph,
)

from router import (
    HybridRouter,
)

from pipeline import (
    EnterprisePipeline,
)


class EnterpriseAssistant(

    HybridDialogueAgent

):

    def __init__(

        self,

        memory_manager,

    ):

        super().__init__(

            "Hybrid assistant",

            memory_manager,

        )

        self.pipeline = EnterprisePipeline(

            HybridRouter(),

            EnterpriseRasaEngine(),

            EnterpriseLangGraph(),

        )

    def chat(

        self,

        message,

    ):

        return self.pipeline.respond(

            message,

            self.state,

        )