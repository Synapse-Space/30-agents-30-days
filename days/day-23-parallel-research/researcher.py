from shared_core.multi_agent import Worker 
from prompts import MARKET_PROMPT, TECH_PROMPT, TRENDS_PROMPT

class MarketResearcher(Worker):
    def __init__(self,llm):
        self.llm=llm

    def run(self,state):
        response=self.llm.invoke(f"{state.get('query', '')}\n\n{MARKET_PROMPT}")
        return {"market": response.content, "completed": 1}


class TechnologyResearcher(Worker):
    def __init__(self,llm):
        self.llm=llm

    def run(self,state):
        response=self.llm.invoke(f"{state.get('query', '')}\n\n{TECH_PROMPT}")
        return {"technology": response.content, "completed": 1}


class TrendsResearcher(Worker):
    def __init__(self,llm):
        self.llm=llm

    def run(self,state):
        response=self.llm.invoke(f"{state.get('query', '')}\n\n{TRENDS_PROMPT}")
        return {"trends": response.content, "completed": 1}