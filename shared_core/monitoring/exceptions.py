class MonitoringException(
    Exception,
):
    """Base monitoring exception."""


class StreamDisconnected(
    MonitoringException,
):
    """Stream disconnected."""