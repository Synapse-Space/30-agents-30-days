from shared_core.graph import GraphNode 

class WriterNode(GraphNode):
    def __init__(self,llm):
        self.llm=llm 

    def run(self,state):
        prompt=f"""User Request:
        {state.prompt}
        Previous Feedback:
        {state.feedback}
        Write the best possible answer.
        """
        response=self.llm.invoke(prompt)
        state.answer=response 
        state.iteration+=1
        return state 
        