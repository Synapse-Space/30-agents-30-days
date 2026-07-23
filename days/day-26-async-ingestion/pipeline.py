from shared_core.knowledge import EmbeddedChunk

class LocalKnowledgePipeline:
    def __init__(self, loader, chunker, embedder, repository):
        self.loader = loader
        self.chunker = chunker
        self.embedder = embedder
        self.repository = repository
    
    def ingest(self, filepath):
        document = self.loader.load(filepath)
        chunks = self.chunker.chunk(document)

        for chunk in chunks:
            embedding = self.embedder.embed(chunk.text)
            self.repository.save(
                EmbeddedChunk(
                    document_id=chunk.document_id,
                    index=chunk.index,
                    text=chunk.text,
                    embedding=embedding,
                )
            )

        return len(chunks)


class AsyncPipeline:
    def __init__(self, knowledge_pipeline):
        self.pipeline = knowledge_pipeline

    def ingest(self, file):
        return self.pipeline.ingest(file)