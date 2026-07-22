from shared_core.agents import ContextualRAGAgent

from summarizer import LocalDocumentSummarizer

from retriever import ContextualRetriever

from pipeline import LocalContextualPipeline

from prompts import SYSTEM_PROMPT

from report import build_summary

class AnthropicStyleRAGAgent(ContextualRAGAgent):
    def __init__(self, memory_manger):
        super().__init__(SYSTEM_PROMPT,memory_manger)

        self.summarizer=LocalDocumentSummarizer()
        self.retriever =ContextualRetriever()
        self.pipeline=LocalContextualPipeline(self.summarizer, self.generator)

    def ask(self, question):
        answer,chunks=self.pipeline.answer(question)
        explanation=self.generate(build_summary(question,chunks))

        return {
            "answer": answer,

            "sources": len(chunks),

            "reasoning": explanation,
        }
