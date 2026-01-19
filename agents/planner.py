from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

def planner_node(state):
    prompt = f"""
You are a planning agent.
Break the task into clear executable steps.

Task: {state['user_input']}
"""
    plan = llm.invoke(prompt).content.split("\n")
    return {"plan": plan}
