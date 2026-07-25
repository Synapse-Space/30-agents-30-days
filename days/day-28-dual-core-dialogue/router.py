from shared_core.dialogue import DialogueRouter, DialogueEngine 

class HybridRouter(DialogueRouter):
    BUSINESS_KEYWORDS={
        "open account",
        "loan",
        "kyc",
        "apply"
    }

    def route(self, message,state):
        text=message.lower()
        if any(keyword in text for keyword in self.BUSINESS_KEYWORDS):
            return DialogueEngine.RASA 

        if state.active_form:
            if any(phrase in text for phrase in ["what is", "explain", "difference", "why", "how"]):
                return DialogueEngine.LANGGRAPH
            
            return DialogueEngine.RASA 
        
        return DialogueEngine.LANGGRAPH