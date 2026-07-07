from collections import defaultdict
from .tokenizer import Tokenizer 

class KeywordIndex:
    def __init__(self):
        self.tokenizer=Tokenizer()
        self.index=defaultdict(list)

    def build(self, chunks):
        for chunk in chunks:
            tokens=self.tokenizer.tokenize(chunk.text)

            for token in tokens:
                self.index[token].append(chunks)
                