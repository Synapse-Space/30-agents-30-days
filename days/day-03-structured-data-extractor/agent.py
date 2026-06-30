from pydantic import ValidationError
from shared_core.agents import BaseAgent
from shared_core.json_parser import JSONParser
from shared_core.validator import Validator

from shared_core.prompts.extractor import SYSTEM_PROMPT
from schemas import ContactInformation

class StructuredExtractorAgent(BaseAgent):
    MAX_RETRIES=3
    def __init__(self):
        super().__init__(SYSTEM_PROMPT)
    def extract(self):
        response =self.structured(ContactInformation)
        self.logger.info("LLM Response:\n%s", response)
        self.add_assistant_message(response)
        json_data=JSONParser.parse(response)
        validated=Validator.validate(
            json_data,ContactInformation
        )

        return validated
    
    def run(self, email:str)->ContactInformation:
        self.clear_history()
        self.add_user_message(email)
        last_error=None
        for attempt in range(1, self.MAX_RETRIES+1):
            try:
                self.logger.info(
                    "Extraction Attempt %s/%s",
                    attempt,
                    self.MAX_RETRIES
                )

                return self.extract()

            except (
                ValueError,
                ValidationError,
            ) as exc:

                last_error = exc

                self.logger.warning(exc)

                # Give feedback to the LLM
                self.add_user_message(
                    f"""
Your previous response was invalid.

Error:
{exc}

Return ONLY valid JSON matching
the schema.

Do not explain.
"""
                )

        raise RuntimeError(
            f"Extraction failed after "
            f"{self.MAX_RETRIES} attempts.\n\n"
            f"{last_error}"
        )

    