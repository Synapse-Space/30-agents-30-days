class KnowledgeException(Exception):
    """Base knowledge exception."""


class EmbeddingError(KnowledgeException,):
    """Embedding failed."""

class UnsupportedDocumentException(KnowledgeException):
    pass