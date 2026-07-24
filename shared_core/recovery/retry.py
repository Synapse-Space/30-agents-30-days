class RetryPolicy:
    def __init__(self,max_attempts=3):
        self.max_attempts=max_attempts

    def should_retry(self, attempts):
        return attempts<self.max_attempts