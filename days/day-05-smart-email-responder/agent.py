from shared_core.agents import ( StructuredAgent, AgentConfig)
from shared_core.prompts import EMAIL_SYSTEM_PROMPT

import os 


from schemas import EmailResponse 

class EmailAssistantAgent(StructuredAgent):
    config = AgentConfig(
        name="Email Assistant",
        description="Classifies emails and drafts replies.",
        system_prompt=EMAIL_SYSTEM_PROMPT,
        output_schema=EmailResponse,
        temperature=0.2,
        max_retries=3
    )

    @property
    def schema(self):
        return self.config.output_schema

    def __init__(self):
        super().__init__(self.config.system_prompt)

    def process(self,email:str)->EmailResponse:
        
        return self.run(email)