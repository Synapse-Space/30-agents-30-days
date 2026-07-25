class DialoguePipeline:
    def __init__(self, router, rasa, langgraph):
        self.router=router 
        self.rasa=rasa 
        self.langgraph=langgraph
        