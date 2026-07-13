from shared_core.vision import CoordinateCalculator

class VisualPlanner:
    def choose(self,vision_result,instruction):
        best=max(vision_result.elements,key=lambda e:e.confidence)

        x,y=CoordinateCalculator.center(best.bounding_box)

        return {
            "element":best,
            "coordinates":(x,y)
        }