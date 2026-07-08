from shared_core.emotion import Emotion 

from models import EscalationResult,TicketPriority

class EscalationEngine:
    def evaluate(self, emotion_result)->EscalationResult:
        if emotion_result.emotion==Emotion.ANGRY:
            return EscalationResult(
                escalate=True,
                priority=TicketPriority.HIGH,
                reason="user seems extremely frustrated."
            )

        if emotion_result.emotion==Emotion.FRUSTRATED:
            return EscalationResult(
                escalate=True,
                priority=TicketPriority.MEDIUM,
                reason="Customer Frustration Detected"
            )
        
        return EscalationResult(
            escalate=False,
            priority=TicketPriority.LOW,
            reason="Normal user interaction"
        )