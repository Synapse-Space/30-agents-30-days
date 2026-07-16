class WorkflowQueue:
    def __init__(self):
        self.steps=[]

    def load(self, steps):
        self.steps.extend(steps)

    def next(self):
        if not self.steps:
            return None

        return self.steps.pop(0)
    
    def empty(self):
        return len(self.steps)==0

    def empty(self):
        return len(self.steps)==0