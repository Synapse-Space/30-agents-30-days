from celery_app import celery 

from worker import SelfHealingWorker 

from repair import OllamaRepairEngine 

from shared_core.recovery import ErrorAnalyzer, RetryPolicy

worker=SelfHealingWorker(
    ErrorAnalyzer(),
    OllamaRepairEngine(),
    RetryPolicy()
)

def embedding_task(payload):
    if "document" not in payload:
        raise ValueError(
            "Missing document field."
        )
    return {
        "status":"completed"
    }


@celery.task 
def process_document(payload):
    return worker.execute(embedding_task, payload)