from shared_core.agents import ContextualRAGAgent
from shared_core.rag import AnswerGenerator
from langchain_ollama import ChatOllama

from summarizer import LocalDocumentSummarizer
from retriever import ContextualRetriever
from pipeline import LocalContextualPipeline
from prompts import SYSTEM_PROMPT
from report import build_summary


class LocalAnswerGenerator(AnswerGenerator):
    def __init__(self):
        self.llm = ChatOllama(model="llama3.1:latest")

    def generate(self, query, context=None):
        if context:
            prompt = f"Context:\n{context}\n\nQuestion:\n{query}\n\nAnswer using ONLY the provided context."
        else:
            prompt = query
        return self.llm.invoke(prompt).content


class AnthropicStyleRAGAgent(ContextualRAGAgent):
    def __init__(self, memory_manger):
        super().__init__(SYSTEM_PROMPT, memory_manger)

        self.summarizer = LocalDocumentSummarizer()
        self.retriever = ContextualRetriever()
        self.generator = LocalAnswerGenerator()
        self.pipeline = LocalContextualPipeline(self.retriever, self.generator)

    def ask(self, question):
        answer, chunks = self.pipeline.answer(question)
        explanation = self.generate(build_summary(question, chunks))

        return {
            "answer": answer,
            "sources": len(chunks),
            "reasoning": explanation,
        }

    def run(self, question, *args, **kwargs):
        return self.ask(question)

    def generate(self, prompt: str):
        return self.generator.generate(prompt)
