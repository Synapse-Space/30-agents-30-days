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

    def run(self, filepath):
        return self.ingest(filepath)

    def generate(self, prompt: str):
        from langchain_ollama import ChatOllama
        llm = ChatOllama(model="llama3.1:latest")
        response = llm.invoke(prompt)
        return response.content