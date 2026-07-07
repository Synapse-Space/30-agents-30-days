from faq_matcher import FAQMatcher

class FAQEngine:
    def __init__(self,):
        self.matcher=FAQMatcher()

    def answer(self, question:str):
        return self.matcher.match(question)
        