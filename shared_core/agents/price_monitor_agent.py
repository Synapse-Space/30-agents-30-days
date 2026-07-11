from shared_core.scraping import HydrationManager, ProductExtractor, SnapshotManager

from .browser_agent import BrowserAgent 

class PriceMonitorAgent(BrowserAgent):
    def __init__(self, system_prompt, memory_manager):
        super().__init__(system_prompt, memory_manager)
        self.extractor=ProductExtractor()
        self.snapshots=SnapshotManager()
        self.hydration_manager=HydrationManager()
