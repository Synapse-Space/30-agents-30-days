from rapidfuzz import fuzz
from shared_core.routing import (BaseMatcher, Route, RouteResult)
from faq_repository import FAQRepository

class FAQMatcher(BaseMatcher):
    def __init__(self, threshold=80):
        self.threshold=threshold

        self.repository=FAQRepository()
    
    def match(self, text:str)->RouteResult:
        best_score=0
        best_faq=None
        for faq in self.repository.get_all():
            score=fuzz.token_sort_ratio(text.lower(),faq.question.lower())
            if score>best_score:
                best_score=score
                best_faq=faq

        if ( best_faq and best_score >=self.threshold):
            return RouteResult(
                matched=True,
                confidence= best_score/100.0,
                route=Route(
                    name="faq",
                    handler="faq"
                ),
                message=best_faq.answer 
            )
        
        return RouteResult(

            matched=False,

            confidence=0,

            route=None,

            message="",

        )