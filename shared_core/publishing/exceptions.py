class PublishingException(Exception):
    """Base publishing exception."""

class PublishFailed(PublishingException):
    """when publishing fails"""
    