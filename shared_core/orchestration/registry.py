class AgentRegistry:
    def __init__(self):
        self.agents={}

    def register(self,name,agent):
        self._agents[name]=agent 

    def get(self,name):
        return self._agents[name]
    
    def list_agents(self):
        return list(self._agents.keys())