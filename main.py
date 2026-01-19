import sys
from graph.agent_graph import build_graph

def main():
    agent = build_graph()

    user_input = " ".join(sys.argv[1:])
    if not user_input:
        print("Usage: python main.py \"your task here\"")
        return

    result = agent.invoke({
        "user_input": user_input,
        "plan": [],
        "tool_results": {},
        "final_answer": ""
    })

    print("\n=== FINAL ANSWER ===\n")
    print(result["final_answer"])

if __name__ == "__main__":
    main()
