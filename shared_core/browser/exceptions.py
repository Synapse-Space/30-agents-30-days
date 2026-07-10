
class BrowserException(Exception):
    """Base browser exception."""


class SearchException(BrowserException):
    """Search failed."""


class ExtractionException(BrowserException):
    """Extraction failed."""