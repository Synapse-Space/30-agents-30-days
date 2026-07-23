class AsyncPipeline:

    def __init__(

        self,

        knowledge_pipeline,

    ):

        self.pipeline = knowledge_pipeline

    def ingest(

        self,

        file,

    ):

        return self.pipeline.ingest(
            file
        )