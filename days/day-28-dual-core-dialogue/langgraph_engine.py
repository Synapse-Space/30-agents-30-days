from langchain_ollama import ChatOllama
from shared_core.dialogue import LangGraphEngine, DialogueEngine, DialogueResponse

class EnterpriseLangGraph(LangGraphEngine):
    def __init__(self):
        self.llm = ChatOllama(model="llama3.1:latest")

    def respond(self, message, state):
        prompt_messages = []
        prompt_messages.append({
            "role": "system", 
            "content": "You are the reasoning core of an enterprise banking system. Answer user questions clearly and concisely."
        })

        # Include recent history from state if present
        if hasattr(state, "history") and isinstance(state.history, list):
            for turn in state.history[-6:]:
                if isinstance(turn, dict):
                    prompt_messages.append(turn)

        prompt_messages.append({"role": "user", "content": message})

        answer = self.llm.invoke(prompt_messages).content

        # Update history
        if hasattr(state, "history") and isinstance(state.history, list):
            state.history.append({"role": "user", "content": message})
            state.history.append({"role": "assistant", "content": answer})

        return DialogueResponse(response=answer, engine=DialogueEngine.LANGGRAPH)