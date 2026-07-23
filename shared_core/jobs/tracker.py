from .models import JobStatus 

class JobTracker:
    def __init__(self):
        self.jobs={}

    def create(self, job):
        self.jobs[job.id]=job.status 

    def update(self, job_id, status):
        self.jobs[job_id]=status 

    def get(self,job_id):
        return self.jobs.get(job_id) 