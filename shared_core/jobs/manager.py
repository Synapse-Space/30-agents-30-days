class JobManager:
    def __init__(self, queue, tracker):
        self.queue=queue 
        self.tracker=tracker 

    def submit(self,job):
        self.tracker.create(job)
        self.queue.publish(job)

        return job.id