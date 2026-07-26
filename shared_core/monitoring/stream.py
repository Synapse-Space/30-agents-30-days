from abc import ABC, abstractmethod
from .models import LogEvent


class LogStream(ABC):
    @abstractmethod
    async def connect(self):
        """connect to log source"""
        
    @abstractmethod
    async def receive(self) -> LogEvent:
        """Receive next log even"""