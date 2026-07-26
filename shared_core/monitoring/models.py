from datetime import timedelta
from datetime import datetime 
from enum import Enum 
from typing import Any 
from pydantic import BaseModel, Field

class Severity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    HIGH = "high"
    CRITICAL = "critical"

class LogEvent(BaseModel):
    timestamp: datetime 
    source: str 
    message: str 
    metadata: dict[str, Any] = Field(default_factory=dict)

class Alert(BaseModel):
    severity: Severity
    title: str 
    description: str 
    source: str 
    timestamp: datetime

class MonitoringResult(BaseModel):
    anomaly: bool 
    alert: Alert | None = None