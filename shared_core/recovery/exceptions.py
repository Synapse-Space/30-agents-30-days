class RecoveryException(Exception):
    """Base recovery exception."""


class RetryLimitExceeded(
    RecoveryException,
):
    """Retry limit exceeded."""