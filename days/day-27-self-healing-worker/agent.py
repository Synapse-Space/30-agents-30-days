from shared_core.agents import SelfHealingWorkerAgent
from tasks import process_document

class RecoveryAgent(SelfHealingWorkerAgent):
    def submit(self, payload):
        task=process_document.delay(payload)

        return {
            "task_id":task.id,
            "status":"queued"
        }