class ResultAggregator:
    def build(self, state):
        return "\n\n".join(state.results)