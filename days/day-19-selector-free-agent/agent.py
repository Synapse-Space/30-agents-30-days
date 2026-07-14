from shared_core.agents import (
    SelectorFreeAgent,
)

from detector import ComputerUseDetector
from parser import VisionParser
from planner import TargetPlanner
from recovery import RecoveryManager
from prompts import SYSTEM_PROMPT
from report import build_reasoning


class VisualInteractionAgent(
    SelectorFreeAgent
):

    def __init__(
        self,
        memory_manager,
    ):

        super().__init__(
            SYSTEM_PROMPT,
            memory_manager,
        )

        self.detector = ComputerUseDetector()
        self.parser = VisionParser()
        self.planner = TargetPlanner()
        self.recovery = RecoveryManager()

    def interact(
        self,
        page,
        instruction,
    ):

        image = self.screenshots.capture(page)

        raw = self.detector.detect(
            image,
            instruction,
            SYSTEM_PROMPT,
        )

        parsed = self.parser.parse(raw)

        plan = self.planner.choose(parsed)

        action = self.planner.build(
            plan["element"].label,
            plan["coordinates"],
        )

        previous_url = page.url

        self.executor.execute(
            page,
            action,
        )

        success = self.verifier.page_changed(
            page,
            previous_url,
        )

        if not success:

            alternative = self.recovery.next_candidate(
                plan
            )

            if alternative:

                # Retry logic could build and execute
                # another action here.
                pass

        explanation = self.generate(
            build_reasoning(
                plan["element"]
            )
        )

        return {

            "success": success,

            "target": plan,

            "reasoning": explanation,

        }

    def run(self, page, instruction):
        return self.interact(page, instruction)

    def generate(self, prompt: str):
        response = self.llm.chat(messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]