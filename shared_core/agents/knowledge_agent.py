from shared_core.knowledge import (

    DocumentLoader,

    ParagraphSplitter,

    Chunker,

    KeywordIndex,

    KeywordRetriever,

)
from .guardrail_agent import GuardrailAgent 

class KnowledgeAgent(GuardrailAgent):
    def __init__(self, system_prompt, memory_manager):
        super().__init__(system_prompt, memory_manager)
        self.loader=DocumentLoader()
        self.splitter=ParagraphSplitter()
        self.chunker=Chunker()
        self.index=KeywordIndex()
        self.retriever=KeywordRetriever(self.index)
    
    def load_documents(self, folder):
        documents = self.loader.load_directory(folder)
        all_chunks=[]

        for document in documents:
            paragraphs=self.splitter.split(document.content)

            chunks=self.chunker.chunk(document,paragraphs)

            all_chunks.extend(chunks)

        self.index.build(all_chunks)
        
        return len(all_chunks)

    def search(self,question):
        return self.retriever.retrieve(question)
        