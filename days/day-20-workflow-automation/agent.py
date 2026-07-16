from shared_core.agents import WorkflowAutomationAgent

from mapper import FieldMapper
from workflow import WorkflowController
from validator import FormValidator
from recovery import WorkflowRecovery
from prompts import SYSTEM_PROMPT
from report import build_summary

class FormWorkflowAgent(WorkflowAutomationAgent):
    def __init__(self,memory_manager):
        super().__init__(SYSTEM_PROMPT,memory_manager)
        self.mapper=FieldMapper()
        self.controller=WorkflowController()
        self.validator=FormValidator()
        self.recovery=WorkflowRecovery()

    def process(self,page,csv_row):
        mapped = self.mapper.map(csv_row)

        fields = list(mapped.keys())

        steps = self.planner.build(fields)

        self.queue.load(steps)

        self.state.start()

        self.controller.run(

            self.queue,

            self.executor,

            self.validator,

            page,

        )

        self.state.complete()

        result = {

            "status": self.state.status.value,

            "completed_steps": len(steps),

        }

        explanation = self.generate(

            build_summary(result)

        )

        return {

            "workflow": result,

        }

    def run(self, page, csv_row):
        return self.process(page, csv_row)

    def generate(self, prompt: str):
        response = self.llm.chat(messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]