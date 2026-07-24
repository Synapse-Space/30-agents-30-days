
from shared_core.recovery import (
    ErrorAnalyzer,
    RepairEngine,
    RetryPolicy,
    RecoveryPipeline,
)

from .async_document_ingestion_agent import (
    AsyncDocumentIngestionAgent,
)


class SelfHealingWorkerAgent(
    AsyncDocumentIngestionAgent
):

    def __init__(
        self,
        system_prompt,
        memory_manager,
    ):

        super().__init__(
            system_prompt,
            memory_manager,
        )

        self.analyzer = ErrorAnalyzer()

        self.repair_engine = RepairEngine()

        self.retry_policy = RetryPolicy()

        self.pipeline = RecoveryPipeline(
            self.analyzer,
            self.repair_engine,
            self.retry_policy,
        )