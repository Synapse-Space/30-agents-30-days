from .machine import WorkflowMachine

class Workflow: 
    def __init__(self):
        self.machine=WorkflowMachine()

    def start(self, initial_state: str):
        self.machine.start(initial_state)