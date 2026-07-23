
from shared_core.agents import (AsyncDocumentIngestionAgent,)

from queue import (PgBossQueue,)

from worker import (IngestionWorker,)

from pipeline import (AsyncPipeline,)

from report import (build_summary,)


class BackgroundIngestionAgent(

    AsyncDocumentIngestionAgent

):

    def __init__(

        self,

        memory_manager,

        boss,

        tracker,

        knowledge_pipeline,

    ):

        super().__init__(

            "Async ingestion",

            memory_manager,

        )

        self.queue = PgBossQueue(
            boss
        )

        self.pipeline = AsyncPipeline(
            knowledge_pipeline
        )

        self.worker = IngestionWorker(

            self.pipeline,

            tracker,

        )

    async def submit(

        self,

        filepath,

    ):

        job = {

            "id": "generated-at-runtime",

            "topic": "document.ingest",

            "data": {

                "file": filepath,

            },

        }

        await self.queue.publish(

            job["topic"],

            job,

        )

        return {

            "job_id": job["id"],

            "summary": build_summary(

                job["id"]

            ),

        }