import uuid 

from shared_core.orchestration import WorkflowPlanner, WorkflowTask

class EnterprisePlanner(WorkflowPlanner):
    def plan(self, objective):
        return [
            WorkflowTask(
                id=str(uuid.uuid4()),
                name="Research",
                agent="research"
            ),
            WorkflowTask(
                id=str(uuid.uuid4()),
                name="RAG Analysis",
                agent="rag",
            ),

            WorkflowTask(
                id=str(uuid.uuid4()),
                name="Generate Report",
                agent="report",
                dependencies=["Research"],
            ),

            WorkflowTask(
                id=str(uuid.uuid4()),
                name="Publish",
                agent="publisher",
                dependencies=["Generate Report"],
            ),
        ]
