
from shared_core.agents import (
    AuthenticatedBrowserAgent,
)

from prompts import SYSTEM_PROMPT
from extractor import ProfileExtractor
from metrics import MetricsAnalyzer
from report import build_prompt


class ProfileAnalyzerAgent(

    AuthenticatedBrowserAgent

):

    def __init__(
        self,
        memory_manager,
    ):

        super().__init__(
            SYSTEM_PROMPT,
            memory_manager,
        )

        self.extractor = ProfileExtractor()

        self.metrics = MetricsAnalyzer()

    def analyze_profile(
        self,
        profile_url: str,
    ):

        with self.open_authenticated_browser() as page:

            page.goto(
                profile_url,
                wait_until="networkidle",
            )

            profile = self.extractor.extract(
                page
            )

        metrics = self.metrics.analyze(
            profile
        )

        prompt = build_prompt(
            profile,
            metrics,
        )

        summary = self.generate(
            prompt
        )

        return {

            "profile": profile,

            "metrics": metrics,

            "summary": summary,

        }