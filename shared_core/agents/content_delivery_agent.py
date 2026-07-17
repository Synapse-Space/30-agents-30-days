from shared_core.publishing import MarkdownFormatter, ContentValidator, PublishState, CMSClient 

from .workflow_agent import WorkflowAutomationAgent
class ContentDeliveryAgent(WorkflowAutomationAgent):
    def __init__(self, system_prompt, memory_manager):
        super().__init__(system_prompt, memory_manager)
        self.formatter = MarkdownFormatter()

        self.validator = ContentValidator()

        self.state = PublishState()

        self.cms = CMSClient()