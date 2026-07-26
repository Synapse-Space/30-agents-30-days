from shared_core.agents import (
    DistributedLogMonitoringAgent,
)

from websocket import (
    WebSocketLogStream,
)

from detector import (
    RuleBasedDetector,
)

from analyzer import (
    OllamaLogAnalyzer,
)

from pipeline import (
    EnterpriseMonitoringPipeline,
)

from shared_core.monitoring import (
    MetricsCollector,
)


class EnterpriseMonitoringAgent(
    DistributedLogMonitoringAgent
):

    def __init__(

        self,

        websocket_url,

        memory_manager,

    ):

        super().__init__(

            "Monitoring Agent",

            memory_manager,

        )

        self.pipeline = EnterpriseMonitoringPipeline(

            WebSocketLogStream(
                websocket_url
            ),

            RuleBasedDetector(),

            OllamaLogAnalyzer(),

            MetricsCollector(),

        )

    async def start(self):

        await self.pipeline.monitor()