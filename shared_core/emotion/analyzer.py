from .models import Emotion, EmotionResult
from .scorer import EmotionScorer

class EmotionAnalyer:
    def __init__(self):
        self.scorer=EmotionScorer()
        
    def analyze(self, text:str)->EmotionResult:
        result=self.scorer.score(text)
        positives=len(result["positive"])
        negatives=len(result["negative"])
        escalations=len(result["escalation"])

        total=positives+negatives+1

        confidence=max(positives,negatives, escalations)/total

        if escalations:
            return EmotionResult(
                emotion=Emotion.ANGRY,
                score=1.0,
                confidence=confidence,
                matched_keywords=result["escalation"]
            )
        
        if negatives >=4:
            return EmotionResult(
                emotion=Emotion.ANGRY,
                score=0.95,
                confidence=confidence,
                matched_keywords=result["negative"]
            )
        
        if negatives>=2:
            return EmotionResult(
                emotion=Emotion.FRUSTRATED,
                score=0.75,
                confidence=confidence,
                matched_keywords=result["negative"]
            )
        
        if positives>=2:
            return EmotionResult(
                emotion=Emotion.HAPPY,
                score=0.2,
                confidence=confidence,
                matched_keywords=result["positive"]
            )
        
        return EmotionResult(
            emotion=Emotion.NEUTRAL,
            score=0.5,
            confidence=0.5,
            matched_keywords=[]
        )
        
        