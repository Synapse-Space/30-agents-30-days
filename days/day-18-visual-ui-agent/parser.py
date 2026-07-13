from shared_core.vision import VisionResult 

class VisionParser:
    def parse(self,response):
        return VisionResult.model_validate_json(response)
        