from shared_core.monitoring import (
    MetricsCollector,
)

from .self_healing_worker_agent import (
    SelfHealingWorkerAgent,
)


class DistributedLogMonitoringAgent(
    SelfHealingWorkerAgent
):

    def __init__(
        self,
        system_prompt,
        memory_manager=None,
    ):

        super().__init__(
            system_prompt,
            memory_manager,
        )

        self.metrics = MetricsCollector()

    def run(
        self,
        *args,
        **kwargs,
    ):

        pass
