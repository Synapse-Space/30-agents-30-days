from langgraph.graph import StateGraph, END

from shared_core.graph import GraphState 

def build_graph(writer,critic,controller):
    graph=StateGraph(GraphState)

    graph.add_node("writer", writer.run)
    graph.add_node("critic", critic.run)
    graph.set_entry_point("writer")

    graph.add_edge("writer", "critic")
    graph.add_conditional_adges("critic", controller.next,{"writer":"writer", "finish":END})

    return graph.compile()
    