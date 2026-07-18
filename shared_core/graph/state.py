from typing import TypedDict

class GraphState(TypedDict):
    prompt: str
    answer: str
    feedback: str
    score: float
    iteration: int
    max_iterations: int