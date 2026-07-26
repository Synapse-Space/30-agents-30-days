from collections import defaultdict

class MetricsCollector:
    def __init__(self):
        self.events=0
        self.alerts=0
        self.sources=defaultdict(int)

    def record_event(self, source:str):
        self.events+=1
        self.sources[source]+=1
    
    def record_alert(self):
        self.alerts+=1

    def summary(self):
        return {
            "events":self.events,
            "alerts":self.alerts,
            "sources":dict(self.sources)
        }