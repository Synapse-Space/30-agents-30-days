from .lexicon import POSITIVE, NEGATIVE, ESCALATION

from .utils import tokenize

class EmotionScorer:
    def score(self,text:str):
        tokens=tokenize(text)
        positive=[]
        negative=[]
        escalation=[]
        for token in tokens:
            if token in POSITIVE:
                positive.append(token)
            if token in NEGATIVE:
                negative.append(token)
            if token in ESCALATION:
                escalation.append(token)
            
        return {
            "positive":positive,
            "negative":negative,
            "escalation":escalation
        }
        