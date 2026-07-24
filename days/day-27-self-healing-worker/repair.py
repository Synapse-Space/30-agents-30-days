from shared_core.automation import models
from langchain_ollama import ChatOllama 
from shared_core.recovery import RepairEngine, RepairSuggestion

class OllamaRepairEngine(RepairEngine):
    def __init__(self):
        self.llm=ChatOllama(model="llama3.1:8b")

    def repair(self, error, payload):
        prompt=f"""A background task failed Error: {error.message} Payload: {payload} Return corrected JSON only."""

        fixed=self.llm.invoke(prompt).content 

        return RepairSuggestion(fixed_input={"raw":fixed},explanation="LLM repaired payload.", retry=True)