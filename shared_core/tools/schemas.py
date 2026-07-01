from pydantic import BaseModel

class EmptyArgs(BaseModel):
    """
    Schema for tools that require no arguments.
    """

    pass