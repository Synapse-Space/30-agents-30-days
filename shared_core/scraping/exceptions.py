
class ScrapingException(Exception):
    """Base scraping exception."""


class ExtractionException(
    ScrapingException,
):
    """Extraction failed."""