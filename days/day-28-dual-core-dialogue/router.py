from shared_core.dialogue import DialogueRouter, DialogueEngine 

class HybridRouter(DialogueRouter):
    QUESTION_PATTERNS = [
        "what is", "explain", "difference", "why", "how do", "how does", 
        "what are", "tell me about", "can you explain", "i am asking"
    ]
    FORM_INTENTS = [
        "open account", "open a bank account", "open bank account", 
        "apply for loan", "apply loan", "start kyc"
    ]

    def route(self, message, state):
        text = message.lower().strip()

        # 1. First check if message is a conceptual question or explanation request
        if any(pattern in text for pattern in self.QUESTION_PATTERNS) or text.endswith("?"):
            # Exclude explicit form trigger phrases like "how to open a bank account"
            if not any(intent in text for intent in self.FORM_INTENTS):
                return DialogueEngine.LANGGRAPH

        # 2. Check if user explicitly wants to start a business form workflow
        if any(intent in text for intent in self.FORM_INTENTS) or (("open" in text or "apply" in text) and "account" in text):
            return DialogueEngine.RASA

        # 3. If currently inside an active Rasa form, route to RASA for slot collection
        if getattr(state, "active_form", None):
            return DialogueEngine.RASA 

        # 4. Check general business keywords
        if any(k in text for k in ["account", "loan", "kyc", "apply"]):
            return DialogueEngine.RASA

        # 5. Default fallback to LangGraph for reasoning
        return DialogueEngine.LANGGRAPH