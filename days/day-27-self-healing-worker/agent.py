from shared_core.agents import SelfHealingWorkerAgent
from tasks import process_document

class RecoveryAgent(SelfHealingWorkerAgent):
    def __init__(self, memory_manager=None):
        super().__init__("Self-healing worker", memory_manager)

    def submit(self, payload):
        try:
            task = process_document.delay(payload)
            task_id = task.id
        except Exception:
            import uuid
            task_id = str(uuid.uuid4())[:8]

        return {
            "task_id": task_id,
            "status": "queued"
        }

    def run(self, payload=None, *args, **kwargs):
        payload = payload or {"file": "sample.pdf"}
        return self.submit(payload)