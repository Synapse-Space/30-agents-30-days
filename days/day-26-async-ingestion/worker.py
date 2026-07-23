import asyncio
from shared_core.jobs import Worker

class IngestionWorker(Worker):
    def __init__(self, pipeline, tracker):
        self.pipeline = pipeline 
        self.tracker = tracker 

    async def process(self, job):
        file_path = job.get("data", {}).get("file") if isinstance(job, dict) else job.data.get("file")
        job_id = job.get("id") if isinstance(job, dict) else job.id

        self.tracker.update(job_id, "processing")
        try:
            chunks = await asyncio.to_thread(self.pipeline.ingest, file_path)
            self.tracker.update(job_id, "completed", chunks=chunks)
        except Exception as exc:
            self.tracker.update(job_id, "failed", error=str(exc))

    async def run(self, job):
        await self.process(job)