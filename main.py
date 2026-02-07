#main.py

import json
from agent import Agent
from planner import build_prompt
from llm import call_llm
import tools

# 1. Load data
tools.load_csv("data/sample.csv")

agent = Agent("Clean this dataset and make it ready for machine learning")

while True:
    prompt = build_prompt(agent.context())

    llm_output = call_llm(prompt)
    print("\nLLM:\n", llm_output)

    try:
        data = json.loads(llm_output)
    except:
        agent.observe("LLM returned invalid JSON.")
        continue

    agent.observe(f"Thought: {data['thought']}")

    action = data["action"]
    params = data.get("params", {})

    # 2. Execute tool
    if action == "describe_dataframe":
        result = tools.describe_dataframe()

    elif action == "clean_column":
        result = tools.clean_column(**params)

    elif action == "save_report":
        result = tools.save_report(**params)

    elif action == "finish":
        print("\nFINAL ANSWER:\n", data["final_answer"])
        break

    else:
        result = "Unknown action"

    # 3. Store observation
    agent.observe(f"Action: {action}, Result: {result}")

