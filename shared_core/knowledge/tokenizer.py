import re

from .stopwords import STOPWORDS


class Tokenizer:

    def tokenize(

        self,

        text: str,

    ) -> list[str]:

        tokens = re.findall(

            r"[a-zA-Z0-9]+",

            text.lower(),

        )

        return [

            token

            for token in tokens

            if token not in STOPWORDS

        ]