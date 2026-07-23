class JobException(Exception):
    """Base job exception."""


class JobFailed(
    JobException,
):
    """Background job failed."""