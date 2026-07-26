from langchain_ollama import ChatOllama 
from shared_core.monitoring import LogAnalyzer

class OllamaLogAnalyzer(LogAnalyzer):
    def __init__(self):
        self.llm=ChatOllama(model="llama3.1:latest")

    async def analyze(self,event):
        prompt=f"""Analyze this server log.
        Log: {event.message}
        Return :
        -Summary
        -Security Risk
        -Root Cause
        -Recommended Action
        """

        return self.llm.invoke(prompt).content