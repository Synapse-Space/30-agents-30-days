from langchain_ollama import ChatOllama 
from shared_core.rag import DocumentSummarizer

class localDocumentSummarizer(DocumentSummarizer):
    def __init__(self):
        self.llm=ChatOllama(model="llama3.1:8b")

    def summarize(self, document):
        prompt=f"""Summarize the following document in 5 concise bullet points.
        Document:
        {document.content}
        """
        return self.llm.invoke(prompt).content 
        