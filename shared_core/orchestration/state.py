from pydantic import BaseModel, Field


class WorkflowState(BaseModel):

    workflow_id: str

    objective: str

    tasks: list = Field(default_factory=list)

    context: dict = Field(default_factory=dict)

    outputs: dict = Field(default_factory=dict)

    metadata: dict = Field(default_factory=dict)