class MonitoringPipeline:

    def __init__(

        self,

        stream,

        detector,

        analyzer,

        metrics,

    ):

        self.stream = stream

        self.detector = detector

        self.analyzer = analyzer

        self.metrics = metrics