from enum import Enum 
from pydantic import BaseModel

class Emotion(str, Enum):
    HAPPY="happy"
    SAD="sad"
    ANGRY="angry"
    FEAR="fear"
    SURPRISE="surprise"
    DISGUST="disgust"
    NEUTRAL="neutral"
    FRUSTRATED="frustrated"
    INTERESTED="interested"
    TIRED="tired"
    CONFUSED="confused"
    


class EmotionResult(BaseModel):
    emotion: Emotion
    score:float
    confidence: float
    matched_keywords:list[str]
    