from shared_core.agents import (
    ContentDeliveryAgent,
)

from adapter import CMSAdapter
from workflow import PublishingWorkflow
from extractor import PreviewExtractor
from prompts import SYSTEM_PROMPT
from report import build_summary


class CMSPublishingAgent(ContentDeliveryAgent):
    def __init__(self,memory_manager):
        super().__init__(SYSTEM_PROMPT, memory_manager)
        self.adapter=CMSAdapter()
        self.workflow = PublishingWorkflow()
        self.extractor = PreviewExtractor()

    def publish(self,page,draft):
        draft.body=self.formatter.format(draft.body)

        self.validator.validate(draft)

        self.cms.login("admin","password")

        self.workflow.run(

            self.adapter,

            page,

            draft,

        )

        self.state.publish()

        metadata = self.extractor.extract(

            page,

        )

        result = {

            "status": self.state.status.value,

            "preview_url": metadata["preview_url"],

        }

        explanation = self.generate(

            build_summary(result)

        )

        return {

            "publish": result,

            "reasoning": explanation,

        }

    def run(self, page, draft):
        return self.publish(page, draft)

    def generate(self, prompt: str):
        response = self.llm.chat(messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]