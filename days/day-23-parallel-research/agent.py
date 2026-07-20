from shared_core.agents import ParallelResearchAgent 

from researcher import MarketResearcher, TechnologyResearcher, TrendsResearcher
from report import ExecutiveReportGenerator
from graph import build_graph 
from state import ResearchState 

class ResearchTeamAgent(ParallelResearchAgent):
    def __init__(self, llm, memory_manger):
        super().__init__("Parallel research supervisor", memory_manger)

        self.market=MarketResearcher(llm)
        self.technology=TechnologyResearcher(llm)
        self.trends=TrendsResearcher(llm)

        self.report=ExecutiveReportGenerator(llm)

        self.graph=build_graph(

            self.market,
            self.technology,
            self.trends,
            self.report
        )
        
    
    def research(self, query):
        state=ResearchState()
        state.query=query
        result=self.graph.invoke(state)
        return {
            "report":result.executive_report,
            "completed_workers": result.completed 
        }