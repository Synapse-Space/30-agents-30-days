class ContextualRAGPipeline:

    def __init__(

        self,

        summarizer,

        contextualizer,

        retriever,

        generator,

    ):

        self.summarizer = summarizer

        self.contextualizer = contextualizer

        self.retriever = retriever

        self.generator = generator