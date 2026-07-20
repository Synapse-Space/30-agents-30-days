from typing import TypedDict, List, Any, Annotated
import operator

class TeamState(TypedDict):
    query: str
    results: Annotated[List[Any], operator.add]
    completed: Annotated[int, operator.add]
    expected_workers: int