from abc import ABC, abstractmethod
from .models import LogEvent

class LogAnalyzer(ABC):
    @abstractmethod
    async def analyze(self, event:LogEvent):
        """ Analyze a log event. """