from alerts import AlertManager 

class EnterpriseMonitoringPipeline:
    def __init__(self, stream, detector, analyzer, metrics):
        self.stream=stream 
        self.detector=detector 
        self.analyzer=analyzer
        self.metrics=metrics 
        self.alerts=AlertManager() 

    async def monitor(self):
        await self.stream.connect() 

        while True:
            event = await self.stream.receive()
            self.metrics.record_event(event.source)
            result=await self.detector.detect(event)

            if result.anomaly:
                analysis=await self.analyzer.analyze(event)
                self.metrics.record_alert() 

                await self.alerts.publish(result.alert)

                print()
                print(analysis)