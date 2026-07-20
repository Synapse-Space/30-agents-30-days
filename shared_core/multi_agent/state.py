from typing import TypedDict, List, Any

class TeamState(TypedDict):
    query: str
    results: List[Any]
    completed: int
    expected_workers: int
        