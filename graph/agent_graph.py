from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph, END
from agents.planner import planner_node
from agents.executor import executor_node

class AgentState(TypedDict):
    user_input: str
    plan: List[str]
    tool_results: Dict
    final_answer: str

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_node)
    graph.add_node("executor", executor_node)

    graph.set_entry_point("planner")
    graph.add_edge("planner", "executor")
    graph.add_edge("executor", END)

    return graph.compile()
