from shared_core.vision import (
    CoordinateCalculator,
)


class TargetPlanner:

    def choose(
        self,
        result,
    ):

        if not result.elements:
            return None

        ranked = sorted(
            result.elements,
            key=lambda e: e.confidence,
            reverse=True,
        )

        best = ranked[0]

        x, y = CoordinateCalculator.center(
            best.bounding_box
        )

        return {

            "element": best,

            "coordinates": (x, y),

            "alternatives": ranked[1:],

        }