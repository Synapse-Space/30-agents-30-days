from shared_core.graph import GraphNode 

class CriticNode(GraphNode):
    def __init__(self,llm):
        self.llm=llm 
    
    def run(self,state):
        prompt=f""" Evaluate this answer,
        Return:
        Score (0-1)
        Feedback
        Answer:
        {state.answer}
        """
        review=self.llm.invoke(prompt)
        state.score=review.score 
        state.feedback=review.feedback 
        return state 
        