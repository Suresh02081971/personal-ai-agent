from tools.git_tools import git_status
from tools.fs_tools import read_file

def executor_node(state):
    results = {}

    for step in state["plan"]:
        if "git status" in step.lower():
            results["git_status"] = git_status()

    final_answer = "Task completed.\n\n" + "\n".join(
        f"{k}: {v}" for k, v in results.items()
    )

    return {
        "tool_results": results,
        "final_answer": final_answer
    }
