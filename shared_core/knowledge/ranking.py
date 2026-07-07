
from dataclasses import dataclass


@dataclass(slots=True)
class SearchResult:

    chunk: object

    score: int


class KeywordRanker:

    def score(

        self,

        query_tokens,

        chunk_tokens,

    ):

        return len(

            set(query_tokens)

            &

            set(chunk_tokens)

        )