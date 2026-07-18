from shared_core.agents import ReflectionReasoningAgent
from writer import WriterNode
from critic import CriticNode
from graph import build_graph

from prompts import WRITER_PROMPT,CRITIC_PROMPT
from report import build_summary

class ReflectionGraphAgent(ReflectionReasoningAgent):
    def __init__(self,llm,memory_manager):
        super().__init__(WRITER_PROMPT, memory_manager)

        self.writer=WriterNode(llm)
        self.critic=CriticNode(llm)
        self.graph=build_graph(self.writer, self.critic,self.controller)

    def reflect(self, prompt):
        initial_state = {"prompt": prompt, "answer": "", "feedback": "", "score": 0.0, "iteration": 0, "max_iterations": 5}
        state=self.graph.invoke(initial_state)

        explanation=self.generate(build_summary(state))

        return {
            "answer": state.get("answer", ""),
            "score": state.get("score", 0.0),
            "iterations": state.get("iteration", 0),
            "reasoning": explanation
        }

    def run(self, prompt):
        return self.reflect(prompt)

    def generate(self, prompt: str):
        response = self.llm.chat(messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]