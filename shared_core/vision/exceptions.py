class VisionException(Exception):
    """Base vision exception."""


class DetectionException(
    VisionException,
):
    """UI detection failed."""