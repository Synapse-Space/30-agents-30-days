from models import ExtractedMemory

from prompts import SYSTEM_PROMPT

class MemoryExtractor:
    def __init__(self,llm):
        self.llm=llm

    def extract(self,text:str)->ExtractedMemory:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ]
        response = self.llm.structured(messages=messages, schema=ExtractedMemory)
        return ExtractedMemory.model_validate_json(response)
        