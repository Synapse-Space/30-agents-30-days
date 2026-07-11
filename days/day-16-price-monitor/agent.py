
from shared_core.agents import (
    PriceMonitorAgent,
)

from detector import PriceDetector
from alerts import AlertEngine
from prompts import SYSTEM_PROMPT
from report import build_summary_prompt


class DynamicPriceMonitorAgent(

    PriceMonitorAgent

):

    def __init__(
        self,
        memory_manager,
    ):

        super().__init__(
            SYSTEM_PROMPT,
            memory_manager,
        )

        self.detector = PriceDetector()

        self.alerts = AlertEngine()

    def monitor(
        self,
        previous_snapshots,
        current_snapshots,
    ):

        changes = self.detector.compare(

            previous_snapshots,

            current_snapshots,

        )

        alerts = self.alerts.generate(
            changes
        )

        prompt = build_summary_prompt(
            changes
        )

        summary = self.generate(
            prompt
        )

        return {

            "changes": changes,

            "alerts": alerts,

            "summary": summary,

        }

    def run(self, previous_snapshots, current_snapshots):
        return self.monitor(previous_snapshots, current_snapshots)

    def generate(self, prompt: str):
        response = self.llm.chat(messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]