from .models import BoundingBox

def area(box:BoundingBox):
    return box.width*box.height

def overlaps(a:BoundingBox,b:BoundingBox):
    return not (
        a.x + a.width < b.x

        or

        b.x + b.width < a.x

        or

        a.y + a.height < b.y

        or

        b.y + b.height < a.y

    )