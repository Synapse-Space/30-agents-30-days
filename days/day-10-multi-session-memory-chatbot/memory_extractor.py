from models import ExtractedMemory

class MemoryExtractor:
    def __init__(self,llm):
        self.llm=llm

    def extract(self,text:str)->ExtractedMemory:
        return self.llm.generate_structured_output(prompt=text,output_model=ExtractedMemory)
        