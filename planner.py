#planner.py

def build_prompt(context):
    return f"""
You are an autonomous AI agent.

Your goal is:
{context}

Decide what to do next.

You MUST reply in JSON with this format:
{{
  "thought": "...",
  "action": "think or finish",
  "final_answer": "only if action is finish"
}}
"""

