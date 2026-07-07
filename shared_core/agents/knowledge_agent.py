from shared_core.knowledge import (DocumentLoader,ParagraphSplitter,Chunker)

from .gaurdrail_agent import GaurdrailAgent 

class KnowledgeAgent(GaurdrailAgent):
    def __init__(self, system_prompt, memory_manager):
        super().__init__(system_prompt, memory_manager)
        self.loader=DocumentLoader()
        self.splitter=ParagraphSplitter()
        self.chunker=Chunker()
    
    def load_documents(self, folder:str):
        documents = self.loader.load_directory(folder)
        all_chunks=[]

        for document in documents:
            paragraphs=self.splitter.split(document.content)

            chunks=self.chunker.chunk(document,paragraphs)

            all_chunks.extend(chunks)
        
        return all_chunks
        