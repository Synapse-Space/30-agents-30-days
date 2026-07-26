import asyncio
import json 
from datetime import datetime
import websockets 

from shared_core.monitoring import LogEvent, LogStream

class WebSocketLogStream(LogStream):
    def __init__(self, url: str):
        self.url = url
        self.connection = None 
        self.use_mock = False
        self._mock_logs = [
            {"source": "auth-service", "message": "User admin logged in successfully"},
            {"source": "gateway-api", "message": "GET /api/v1/health 200 OK"},
            {"source": "auth-service", "message": "Failed login attempt for user root from 192.168.1.50"},
            {"source": "payment-service", "message": "POST /api/v1/checkout 200 OK"},
            {"source": "user-service", "message": "Unauthorized access attempt to /admin/settings"},
            {"source": "order-service", "message": "Database connection lost: HTTP 500 Server Error"},
            {"source": "auth-service", "message": "Failed login attempt for user admin from 10.0.0.1"},
            {"source": "worker-node-1", "message": "Critical memory leak detected in worker process #4021"},
            {"source": "gateway-api", "message": "Critical cpu spike detected: node load 99.4%"},
        ]
        self._mock_idx = 0

    async def connect(self):
        try:
            self.connection = await asyncio.wait_for(websockets.connect(self.url), timeout=1.5)
            self.use_mock = False
        except Exception:
            self.use_mock = True

    async def receive(self):
        if not self.use_mock and self.connection:
            raw = await self.connection.recv()
            data = json.loads(raw)
            return LogEvent(
                timestamp=datetime.fromisoformat(data["timestamp"]),
                source=data["source"],
                message=data["message"],
                metadata=data.get("metadata", {})
            )
        else:
            await asyncio.sleep(1.2)
            log = self._mock_logs[self._mock_idx % len(self._mock_logs)]
            self._mock_idx += 1
            return LogEvent(
                timestamp=datetime.utcnow(),
                source=log["source"],
                message=log["message"],
                metadata={"synthetic": True}
            )