class RecoveryPipeline:
    def __init__(self,analyzer,repair_engine,retry_policy):
        self.analyzer=analyzer
        self.repair_engine=repair_engine
        self.retry_policy=retry_policy

    