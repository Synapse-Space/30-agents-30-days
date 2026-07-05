from models import ExtractedMemory

class MemoryExtractor:
    def __init__(self,llm):
        self.llm=llm

    def extract(self,text:str)->ExtractedMemory:
        response = self.llm.structured(messages=[{"role": "user", "content": text}], schema=ExtractedMemory)
        return ExtractedMemory.model_validate_json(response)
        