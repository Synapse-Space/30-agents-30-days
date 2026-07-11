
class BrowserException(Exception):
    """Base browser exception."""


class SearchException(BrowserException):
    """Search failed."""


class ExtractionException(BrowserException):
    """Extraction failed."""

class AuthenticationException(Exception):
    """Base authentication exception."""


class SessionExpiredException(
    AuthenticationException,
):
    """Stored session is no longer valid."""