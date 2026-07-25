from shared_core.dialogue import DialogueRouter, DialogueEngine 

class HybridRouter(DialogueRouter):
    BUSINESS_KEYWORDS = {
        "open account",
        "bank account",
        "open a bank account",
        "account",
        "loan",
        "kyc",
        "apply"
    }

    def route(self, message, state):
        text = message.lower()

        # Check explicit business keywords or phrases
        if any(keyword in text for keyword in self.BUSINESS_KEYWORDS) or ("open" in text and "account" in text):
            return DialogueEngine.RASA 

        # If currently inside an active Rasa business form
        if getattr(state, "active_form", None):
            # If user asks an off-topic / conceptual question during the form
            if any(phrase in text for phrase in ["what is", "explain", "difference", "why", "how", "what are"]):
                return DialogueEngine.LANGGRAPH
            
            return DialogueEngine.RASA 
        
        # Default fallback to LangGraph for general Q&A
        return DialogueEngine.LANGGRAPH