from dataclasses import dataclass

@dataclass(slots=True)
class Rule:
    route_name: str
    keywords: list[str]
    