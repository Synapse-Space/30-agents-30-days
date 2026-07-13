from pathlib import Path 
from .models import VisionResult

class VisionDetector:
    def detect(self, image: Path, instruction:str)->VisionResult:
        raise NotImplementedError

        