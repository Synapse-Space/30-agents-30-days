from datetime import datetime 
from shared_core.monitoring import AnomalyDetector, MonitoringResult, Alert, Severity

class RuleBasedDetector(AnomalyDetector):
    KEYWORDS = {
        "failed login": Severity.WARNING,
        "unauthorized": Severity.HIGH,
        "500": Severity.HIGH,
        "memory leak": Severity.CRITICAL,
        "cpu spike": Severity.CRITICAL,
    }

    async def detect(self, event):
        text = event.message.lower()
        for keyword, severity in self.KEYWORDS.items():
            if keyword in text:
                return MonitoringResult(
                    anomaly=True,
                    alert=Alert(
                        severity=severity,
                        title="System Anomaly Detected",
                        description=event.message,
                        source=event.source,
                        timestamp=datetime.utcnow()
                    )
                )
        return MonitoringResult(anomaly=False)