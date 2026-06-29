from pydantic import BaseModel
from pydantic import Field

class SQLQuery(BaseModel):
    sql:str=Field(
        description="A single read-only SQL query."
    )

    explanation:str=Field(
        description="Brief explanation of the SQL query."
    )