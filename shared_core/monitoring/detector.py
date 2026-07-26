from abc import ABC, abstractmethod

from .models import LogEvent, MonitoringResult

class AnomalyDetector(ABC):
    @abstractmethod
    async def detect(self, event: LogEvent) -> MonitoringResult:
        """Detect anomalies."""