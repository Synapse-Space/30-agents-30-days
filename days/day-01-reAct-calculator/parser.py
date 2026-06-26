from dataclasses import dataclass
import re
from typing import Optional

@dataclass
class AgentResponse:
    thought:Optional[str]=None
    action:Optional[str]=None
    action_input:Optional[str]=None
    final_answer:Optional[str]=None

class ReActParser:
    THOUGHT_PATTERN=re.compile(
        r"Thought:\s*(.*?)(?=\n[A-Z][a-zA-Z]*:|$)",
        re.DOTALL
    )
    ACTION_PATTERN=re.compile(
        r"Action:\s*(.*)"
    )
    ACTION_INPUT_PATTERN=re.compile(
        r"Action Input:\s*(.*)"
    )
    FINAL_ANSWER_PATTERN=re.compile(
        r"Final Answer:\s*(.*)",
        re.DOTALL
    )
    @classmethod
    def parse(cls, text: str) -> AgentResponse:

        thought = cls.THOUGHT_PATTERN.search(text)
        action = cls.ACTION_PATTERN.search(text)
        action_input = cls.ACTION_INPUT_PATTERN.search(text)
        final = cls.FINAL_ANSWER_PATTERN.search(text)

        return AgentResponse(
            thought=thought.group(1).strip() if thought else None,
            action=action.group(1).strip() if action else None,
            action_input=action_input.group(1).strip() if action_input else None,
            final_answer=final.group(1).strip() if final else None,
        )