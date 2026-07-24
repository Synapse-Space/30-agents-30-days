from shared_core.recovery import (RetryLimitExceeded)

class SelfHealingWorker:
    def __init__(self, analyzer, repair_engine, retry_policy):
        self.analyzer = analyzer

        self.repair_engine = repair_engine

        self.retry_policy = retry_policy
    
    
    def execute(self, task, payload, attempts=0):
        try:
            return task(payload)
        
        except Exception as exc:
            error =self.analyzer.analyze(exc)
            if not self.retry_policy.should_retry(attempts):
                raise RetryLimitExceeded() 

            repair=self.repair_engine.repair(error, payload)

            return self.execute(task, repair.fixed_input, attempts+1)