from shared_core.agents import ReflectiveReasoningAgent
from writer import WriterNode
from critic import CriticNode
from graph import build_graph

from prompts import WRITER_PROMPT,CRITIC_PROMPT
from report import build_summary

class ReflectionGraphAgent(ReflectiveReasoningAgent):
    def __init__(self,llm,memory_manager):
        super().__init__(WRITER_PROMPT, memory_manager)

        self.writer=WriterNode(llm)
        self.critic=CriticNode(llm)
        self.graph=build_graph(self.writer, self.critic,self.controller)

    def reflect(self, prompt):
        self.state.prompt=prompt 
        state=self.graph.invoke(self.state)

        explanation=self.generate(build_summary(state))

        return {
            "answer": state.answer,
            "score": state.score,
            "iterations":state.iteration,
            "reasoning":explanation
        }