from agents.memory import save_memory

# At the end of executor_node()
save_memory(state["user_input"])
