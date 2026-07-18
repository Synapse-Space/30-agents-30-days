from shared_core.graph import GraphNode 

class WriterNode(GraphNode):
    def __init__(self,llm):
        self.llm=llm 

    def run(self,state):
        prompt=f"""User Request:
        {state.get('prompt', '')}
        Previous Feedback:
        {state.get('feedback', '')}
        Write the best possible answer.
        """
        response=self.llm.invoke(prompt)
        return {"answer": response.content, "iteration": state.get("iteration", 0) + 1}
        