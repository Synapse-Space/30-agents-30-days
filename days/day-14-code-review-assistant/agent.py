from shared_core.agents import CodeReviewAgent

from prompts import SYSTEM_PROMPT
from rules import RuleEngine
from report import build_review_prompt

class PythonCodeReviewAgent(CodeReviewAgent):
    def __init__(self,memory_manager):
        super().__init__(SYSTEM_PROMPT,memory_manager)
        self.rules=RuleEngine()

    def review(self,file_path):
        module=self.inspect(file_path)
        report=self.rules.evaluate(module)
        prompt=build_review_prompt(report)
        explanation=self.generate(prompt)

        return {
            "module": module,

            "report": report,

            "review": explanation,
        }

    def run(self, file_path: str):
        return self.review(file_path)

    def generate(self, prompt: str):
        response = self.llm.chat(messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]