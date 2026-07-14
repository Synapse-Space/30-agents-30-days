class AutomationException(Exception):
    """Base automation exception."""


class VerificationFailed(
    AutomationException,
):
    """Action verification failed."""