
from .models import WorkflowStatus


class WorkflowState:

    def __init__(self):

        self.status = WorkflowStatus.PENDING

        self.current_step = 0

    def start(self):

        self.status = WorkflowStatus.RUNNING

    def next(self):

        self.current_step += 1

    def complete(self):

        self.status = WorkflowStatus.COMPLETED

    def fail(self):

        self.status = WorkflowStatus.FAILED