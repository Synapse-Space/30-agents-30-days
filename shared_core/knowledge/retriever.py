from .ranking import (

    SearchResult,

    KeywordRanker,

)

from .tokenizer import Tokenizer


class KeywordRetriever:

    def __init__(

        self,

        index,

    ):

        self.index = index

        self.tokenizer = Tokenizer()

        self.ranker = KeywordRanker()

    def retrieve(

        self,

        query,

        top_k=3,

    ):

        query_tokens = self.tokenizer.tokenize(

            query

        )

        candidates = {}

        for token in query_tokens:

            for chunk in self.index.index.get(

                token,

                [],

            ):

                candidates[chunk.id] = chunk

        results = []

        for chunk in candidates.values():

            score = self.ranker.score(

                query_tokens,

                self.tokenizer.tokenize(

                    chunk.text

                ),

            )

            results.append(

                SearchResult(

                    chunk,

                    score,

                )

            )

        results.sort(

            key=lambda x: x.score,

            reverse=True,

        )

        return results[:top_k]