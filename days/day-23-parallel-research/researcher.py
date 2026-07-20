from shared_core.multi_agent import Worker 

class MarketResearcher(Worker):
    def __init__(self,llm):
        self.llm=llm

    def run(self,state):
        state.market=self.llm.invoke(f"{state.query}\n\n{MARKET_PROMPT}")

        state.completed+=1
        return state 


class TechnologyResearcher(Worker):
    def __init__(self,llm):
        self.llm=llm

    def run(self,state):
        state.technology=self.llm.invoke(f"{state.query}\n\n{TECHNOLOGY_PROMPT}")

        state.completed+=1
        return state 


class TrendsResearcher(Worker):
    def __init__(self,llm):
        self.llm=llm

    def run(self,state):
        state.trends=self.llm.invoke(f"{state.query}\n\n{TRENDS_PROMPT}")

        state.completed+=1
        return state 