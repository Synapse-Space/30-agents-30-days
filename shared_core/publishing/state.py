from .models import PublishStatus


class PublishState:

    def __init__(self):

        self.status = PublishStatus.DRAFT

    def publish(self):

        self.status = PublishStatus.PUBLISHED

    def fail(self):

        self.status = PublishStatus.FAILED