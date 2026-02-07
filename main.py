#main.py

import json
from agent import Agent
from planner import build_prompt
from llm import call_llm

agent = Agent("Explain what an AI agent is")

while True:
    context = agent.get_context()
    prompt = build_prompt(context)

    llm_output = call_llm(prompt)

    print("\nLLM OUTPUT:\n", llm_output)

    try:
        data = json.loads(llm_output)
    except:
        print("Invalid JSON, retrying...")
        continue

    agent.add_observation(f"Thought: {data['thought']}")

    if data["action"] == "finish":
        print("\nFINAL ANSWER:\n", data["final_answer"])
        break

