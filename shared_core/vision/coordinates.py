from .models import BoundingBox

class CoordinateCalculator:
    @staticmethod
    def center(box: BoundingBox):
        return (  box.x + box.width // 2,

            box.y + box.height // 2,
            )

    @staticmethod
    def top_left(box:BoundingBox):
        return (box.x,box.y)

    @staticmethod
    def bottom_right(box:BoundingBox):
        return (box.x + box.width, box.y + box.height)
