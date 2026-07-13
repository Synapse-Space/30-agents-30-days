from shared_core.agents import (

    VisionBrowserAgent,

)

from detector import (

    OllamaVisionDetector,

)

from parser import (

    VisionParser,

)

from planner import (

    VisualPlanner,

)

from prompts import (

    SYSTEM_PROMPT,

)

from report import (

    explain,

)

class VisualUIAgent(VisionBrowserAgent):
    def __init__(self,memory_manager):
        super().__init__(SYSTEM_PROMPT,memory_manager)

        self.detector=OllamaVisionDetector()
        self.planner=VisualPlanner()
    
    def locate(self,page,instruction):
        image=self.screenshots.capture(page)
        raw=self.detector.detect(image,instruction,SYSTEM_PROMPT)

        result=self.parser.parse(raw)

        plan=self.planner.choose(result,instruction)

        explanation=self.generate(
            explain(plan["element"])
        )

        return {
            "target":plan,
            "reasoning":explanation
        }