from langgraph.graph import StateGraph, START, END 

from state import ResearchState 

def build_graph(market, technology,trends,report):
    graph=StateGraph(ResearchState)
    graph.add_node("technology", technology.run)
    graph.add_node("market", market.run)
    graph.add_node("trends", trends.run)
    graph.add_node("report", report.run)

    graph.add_edge(START,"market")
    graph.add_edge(START,"technology")
    graph.add_edge(START,"trends")

    #converge
    graph.add_edge("market","report")
    graph.add_edge("technology","report")
    graph.add_edge("trends","report")

    graph.add_edge("report",END)

    return graph.compile()