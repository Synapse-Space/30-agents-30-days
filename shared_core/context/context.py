from dataclasses import dataclass, field
from typing import Any

@dataclass(slots=True)
class AgentContext:
    session_id: str
    state: dict[str, Any]=field(
        default_factory=dict
    )
    metadata: dict[str, Any]=field(
        default_factory=dict
    )