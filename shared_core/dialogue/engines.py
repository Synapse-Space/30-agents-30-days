class DialogueEngineBase:
    def respond(self,message,state):
        raise NotImplementedError 

    
class RasaEngine(DialogueEngineBase):
    pass 


class LangGraphEngine(DialogueEngineBase):
    pass