from shared_core.jobs import Worker

class IngestionWorker(Worker):
    def __init__(self, pipeline,tracker):
        self.pipeline=pipeline 
        self.tracker=tracker 

    async def run(self,job):
        await self.tracker.update(job.id,"processing")

        self.pipeline.ingest(job.data["file"])

        await self.tracker.update(job.id, "completed")