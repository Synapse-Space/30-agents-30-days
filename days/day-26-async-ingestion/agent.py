import uuid
from shared_core.agents import AsyncDocumentIngestionAgent
from job_queue import AsyncJobQueue
from worker import IngestionWorker
from pipeline import AsyncPipeline
from report import build_summary

class BackgroundIngestionAgent(AsyncDocumentIngestionAgent):
    def __init__(self, memory_manager, tracker, knowledge_pipeline):
        super().__init__("Async ingestion", memory_manager)

        self.tracker = tracker
        self.pipeline = AsyncPipeline(knowledge_pipeline)
        self.worker = IngestionWorker(self.pipeline, self.tracker)
        self.queue = AsyncJobQueue(self.tracker, self.worker)

    async def submit(self, filepath):
        job_id = str(uuid.uuid4())[:8]
        job = {
            "id": job_id,
            "topic": "document.ingest",
            "data": {
                "file": filepath,
            },
            "status": "queued",
        }

        await self.queue.publish(job["topic"], job)

        return {
            "job_id": job_id,
            "status": "queued",
            "summary": build_summary(job_id),
        }

    def get_status(self, job_id):
        return self.tracker.get(job_id)

    def list_jobs(self):
        return self.tracker.list_all()

    def run(self, filepath):
        import asyncio
        return asyncio.run(self.submit(filepath))