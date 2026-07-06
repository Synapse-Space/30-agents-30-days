from .matcher import BaseMatcher 
from .result import RouteResult


class Router:
    def __init__(self):
        self.matchers: list[BaseMatcher]=[]
    
    def register_matcher(self, matcher:BaseMatcher):
        self.matchers.append(matcher)

    
    def route(self,text:str)->RouteResult:
        best_result=None
        for matcher in self.matchers:
            result=matcher.match(text)
            if not result.matched:
                continue

            if best_result is None:
                best_result=result

            elif result.confidence > best_result.confidence:
                best_result=result

        
        if best_result:
            return best_result
        
        return RouteResult(
            matched=False,
            route=None,
            confidence=0.0,
            message="No matching Route"
        )
