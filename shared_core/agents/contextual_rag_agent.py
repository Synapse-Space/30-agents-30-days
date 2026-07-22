from shared_core.rag import DocumentSummarizer, Contextualizer, Retriever, AnswerGenerator, ContextualRAGPipeline

from .knowledge_ingestion_agent import KnowledgeIngestionAgent

class ContextualRAGAgent(KnowledgeIngestionAgent):
    def __init__(self, system_prompt,memory_manager):
        super().__init__(

            system_prompt,

            memory_manager,

        )

        self.summarizer = DocumentSummarizer()

        self.contextualizer = Contextualizer()

        self.retriever = Retriever()

        self.generator = AnswerGenerator()

        self.pipeline = ContextualRAGPipeline(

            self.summarizer,

            self.contextualizer,

            self.retriever,

            self.generator,

        )