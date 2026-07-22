class RAGException(Exception):
    """Base RAG exception."""


class RetrievalError(
    RAGException,
):
    """Semantic retrieval failed."""