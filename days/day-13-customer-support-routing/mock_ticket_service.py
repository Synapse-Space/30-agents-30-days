from datetime import datetime
from uuid import uuid4

class MockTicketService:
    def create_ticket(self, message: str, priority:str):

        return {
            "ticket_id": str(uuid4()),
            "priority":priority,
            "created_at":datetime.now().isoformat(),
            "message":message,
            "status":"OPEN"
        }