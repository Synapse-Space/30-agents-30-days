import shared_core.agents.selector_free_agent
from shared_core.jobs import JobManager, JobTracker, JobQueue

from .contextual_rag_agent import ContextualRAGAgent

class AsyncDocumentIngestionAgent(ContextualRAGAgent):
    def __init__(self, system_prompt, memory_manager):
        super().__init__(system_prompt, memory_manager)

        self.queue=JobQueue() 
        self.tracker=JobTracker() 
        self.manager=JobManager(self.queue,self.tracker) 