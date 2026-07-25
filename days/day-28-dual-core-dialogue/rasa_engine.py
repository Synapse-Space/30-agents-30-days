from shared_core.dialogue import RasaEngine, DialogueResponse, DialogueEngine

class EnterpriseRasaEngine(RasaEngine):
    def respond(self, message, state):
        if state.active_form=="account":
            return DialogueResponse(
                response="Please enter your full name.",
                engine=DialogueEngine.RASA,
                metadata={
                    "form":"account"
                }
            )
        return DialogueResponse(
            response="Welcome, How can I help you today?",
            engine=DialogueEngine.RASA,
        )
        