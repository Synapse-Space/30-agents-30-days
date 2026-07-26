import json 
import websockets 
from datetime import datetime

from shared_core.monitoring import LogEvent, LogStream

class WebSocketLogStream(LogStream):
    def __init__(self, url:str):
        self.url = url
        
        self.connection=None 

    async def connect(self):
        self.connection=await websockets.connect(self.url)

    async def receive(self):
        raw=await self.connection.recv()
        data=json.loads(raw)
        return LogEvent(
            timestamp=datetime.fromisoformat(data["timestamp"]),
            source=data["source"],
            message=data["message"],
            metadata=data.get("metadata",{})
        )