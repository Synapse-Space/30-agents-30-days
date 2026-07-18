from shared_core.graph import GraphNode 

from pydantic import BaseModel, Field

class Review(BaseModel):
    score: float = Field(description="Score between 0.0 and 1.0")
    feedback: str = Field(description="Feedback on the answer")

class CriticNode(GraphNode):
    def __init__(self,llm):
        self.llm=llm 
    
    def run(self,state):
        prompt=f""" Evaluate this answer,
        Return:
        Score (0-1)
        Feedback
        Answer:
        {state.get('answer', '')}
        """
        llm_with_structure = self.llm.with_structured_output(Review)
        review = llm_with_structure.invoke(prompt)
        return {"score": review.score, "feedback": review.feedback}
        