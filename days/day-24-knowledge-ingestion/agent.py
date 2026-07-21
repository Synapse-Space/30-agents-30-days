from shared_core.agents import KnowledgeIngestionAgent

from embedder import LocalEmbedder 

from database import PgVectorRepository 

from pipeline import LocalKnowledgePipeline 

from prompts import SYSTEM_PROMPT 

from report import build_summary

class LocalEmbeddingAgent(KnowledgeIngestionAgent):
    def __init__(self, memory_manager):
        super().__init__(SYSTEM_PROMPT, memory_manager)

        self.embedder=LocalEmbedder()
        self.repository=PgVectorRepository()
        self.repository=PgVectorRepository(
            "postgresql://postgres:postgres@localhost:5432/ai_agents"
        )
        self.pipeline=LocalKnowledgePipeline(self.loader,self.chunker,self.embedder,self.repository)

    def ingest(self, filepath):
        total=self.pipeline.ingest(filepath)
        summary=self.generate(build_summary(filepath,total))

        return {
            "chunks":total,
            "summary":summary,
        }