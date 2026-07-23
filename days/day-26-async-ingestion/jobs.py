import uuid 

def create_job(file_path):
    return {
        "id":str(uuid.uuid4()),
        "topic":"document.ingest",
        "data":{"file":file_path}
    }