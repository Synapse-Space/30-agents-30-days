from fastapi import APIRouter,UploadFile 

from jobs import create_job

router=APIRouter()

@router.post("/upload")

async def upload(file:UploadFile):
    job=create_job(file.filename)

    await queue.publish(job["topic"],job)
    return {
        "job_id":job["id"],
        "status":"queued"
    }