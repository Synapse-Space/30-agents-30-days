import json
from shared_core.vision import VisionResult

class VisionParser:
    def parse(self, response):
        try:
            data = json.loads(response)
        except json.JSONDecodeError:
            # Fallback if Ollama didn't return valid JSON
            return VisionResult(elements=[])
            
        if "results" in data and "elements" not in data:
            data["elements"] = data.pop("results")
            
        if "elements" not in data:
            data["elements"] = []
            
        return VisionResult.model_validate(data)