from langchain_ollama import ChatOllama

from shared_core.dialogue import LangGraphEngine, DialogueEngine, DialogueResponse

class EnterpriseLangGraph(LangGraphEngine):
    def __init__(self):
        self.llm=ChatOllama(model="llama3.1:latest")

    
    def respond(self, message,state):
        answer=self.llm.invoke(message).content 

        return DialogueResponse(response=answer, engine=DialogueEngine.LANGGRAPH)