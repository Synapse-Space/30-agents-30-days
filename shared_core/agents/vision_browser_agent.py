from shared_core.vision import (

    ScreenshotManager,

    VisionDetector,

)

from .authenticated_browser_agent import (

    AuthenticatedBrowserAgent,

)


class VisionBrowserAgent(AuthenticatedBrowserAgent):
    def __init__(

        self,

        system_prompt,

        memory_manager,

    ):

        super().__init__(

            system_prompt,

            memory_manager,

        )

        self.screenshots = ScreenshotManager()

        self.detector = VisionDetector()