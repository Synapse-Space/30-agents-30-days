class KnowledgePipeline:
    def __init__(self,loader,chunker,embedder,repository):
        self.loader=loader
        self.chunker=chunker
        self.embedder=embedder
        self.repository=repository