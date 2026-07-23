import asyncio
from shared_core.jobs import JobQueue 

class AsyncJobQueue(JobQueue):
    def __init__(self, tracker, worker=None):
        self.tracker = tracker
        self.worker = worker

    def set_worker(self, worker):
        self.worker = worker

    async def publish(self, topic, payload):
        self.tracker.create(payload)
        if self.worker:
            asyncio.create_task(self.worker.process(payload))
        return payload.get("id") if isinstance(payload, dict) else payload.id
