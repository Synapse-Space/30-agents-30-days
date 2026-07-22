from shared_core.knowledge import chunker
class LocalContextualPipeline:
    def __init__(self,retriever,generator):
        self.retriever=retriever 
        self.generator=generator

    def answer(self, query):
        chunks=self.retriever.search(query)
        context="\n\n".join(chunk.text for chunk in chunks)

        answer=self.generator.generate(query,context)

        return answer,chunks 