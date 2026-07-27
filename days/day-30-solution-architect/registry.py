from shared_core.orchestration import AgentRegistry

class EnterpriseRegistry(AgentRegistry):
    def load_defaults(self):
        self.register("research", "ResearchAgent")
        self.register("rag", "ContextualRagAgent")
        self.register("vision", "VisionAgent")
        self.register("browser", "PlaywrightAgent")
        self.register("reporter", "ReportAgent")
        self.register("publisher", "PublishingAgent")
        self.register("monitor", "MonitoringAgent")
        self.register("recovery", "RecoveryAgent")
        