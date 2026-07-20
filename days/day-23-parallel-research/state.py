from shared_core.multi_agent import TeamState

class ResearchState(TeamState):
    def __init__(self):
        super().__init__()
        self.market=""
        self.technology=""
        self.trends=""
        self.executive_report=""
        