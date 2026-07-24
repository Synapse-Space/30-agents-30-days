from celery import Celery 

celery= Celery("self_healing_worker", broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",)

celery.conf.update(

    task_serializer="json",

    result_serializer="json",

    accept_content=["json"],

    task_track_started=True,

    worker_prefetch_multiplier=1,

)