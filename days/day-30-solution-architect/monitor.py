class WorkflowMonitor:

    def __init__(self):

        self.completed = 0

        self.failed = 0

    def success(self):

        self.completed += 1

    def failure(self):

        self.failed += 1

    def report(self):

        return {

            "completed": self.completed,

            "failed": self.failed,

        }