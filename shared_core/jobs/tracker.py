from .models import JobStatus 

class JobTracker:
    def __init__(self):
        self.jobs = {}

    def create(self, job):
        if hasattr(job, "id"):
            job_id = job.id
            status = job.status
            data = getattr(job, "payload", {}) or getattr(job, "data", {})
        elif isinstance(job, dict):
            job_id = job.get("id")
            status = job.get("status", JobStatus.QUEUED)
            data = job.get("data", {})
        else:
            job_id = str(job)
            status = JobStatus.QUEUED
            data = {}

        if hasattr(status, "value"):
            status = status.value

        self.jobs[job_id] = {
            "id": job_id,
            "status": str(status),
            "data": data,
            "chunks": None,
            "error": None,
        }

    def update(self, job_id, status, chunks=None, error=None):
        if hasattr(status, "value"):
            status = status.value
        if job_id in self.jobs:
            self.jobs[job_id]["status"] = str(status)
            if chunks is not None:
                self.jobs[job_id]["chunks"] = chunks
            if error is not None:
                self.jobs[job_id]["error"] = error
        else:
            self.jobs[job_id] = {
                "id": job_id,
                "status": str(status),
                "chunks": chunks,
                "error": error,
            }

    def get(self, job_id):
        return self.jobs.get(job_id)

    def list_all(self):
        return list(self.jobs.values())