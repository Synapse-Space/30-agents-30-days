from shared_core.dialogue import DialogueEngine 

class EnterprisePipeline:
    def __init__(self, router, rasa, langgraph):
        self.router=router 
        self.rasa=rasa 
        self.langgraph=langgraph 

    def respond(self, message, state):
        engine=self.router.route(message,state)

        if engine==DialogueEngine.RASA:
            state.current_engine="rasa"

            return self.rasa.respond(message,state)