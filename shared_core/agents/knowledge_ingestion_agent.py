from shared_core.knowledge import DocumentLoader, TextChunker, Embedder, VectorRepository, KnowledgePipeline

from .parallel_research_agent import ParallelResearchAgent 


class KnowledgeIngestionAgent(ParallelResearchAgent):
    def __init__(self, system_prompt, memory_manager):
        super().__init__(system_prompt, memory_manager)
        self.loader=DocumentLoader()
        self.chunker=TextChunker()
        self.embedder=Embedder()
        self.repository=VectorRepository()
        self.pipeline=KnowledgePipeline(
            self.loader,
            self.chunker,
            self.embedder,
            self.repository
        )
