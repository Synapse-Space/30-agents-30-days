from abc import abstractmethod
from typing import Type

from pydantic import BaseModel

from shared_core.agents import BaseAgent
from shared_core.json_parser import JSONParser
from shared_core.validator import Validator

class StructuredAgent(BaseAgent):
    MAX_RETRIES=3

    def __init__(self, system_prompt:str):
        super().__init__(system_prompt)

    @property
    @abstractmethod
    def schema(self) -> Type[BaseModel]:
        """Every child agent must define output schema"""

    def generate(self):
        response=self.structured(self.schema)

        self.add_assistant_message(response)

        json_data=JSONParser.parse(response)

        validated=Validator.validate(json_data,self.schema)

        return validated
    
    def run(self, user_input:str):
        self.clear_history()
        self.add_user_message(user_input)

        last_error=None

        for attempt in range(1, self.MAX_RETRIES+1):
            try:
                self.logger.info(
                    "Attempt %s/%s",
                    attempt,
                    self.MAX_RETRIES,
                )

                return self.generate()

            except Exception as exc:
                last_error =exc
                self.logger.warning(exc)
                self.add_user_message(
                    f"""
Previous response failed validation.

Error:

{exc}

Return ONLY valid JSON.
"""
                )

        raise RuntimeError(last_error)