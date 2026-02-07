#planner.py

def build_prompt(context):
    return f"""
You are an autonomous Data Scientist agent.

Your goal:
{context}

You have these tools:
- describe_dataframe()
- clean_column(column, strategy)
- save_report(path)

Strategies for cleaning:
- "drop"
- "mean"
- "median"
- "mode"

Decide the next best action.

You MUST reply in JSON with one of these actions:
- describe_dataframe
- clean_column
- save_report
- finish

Format:
{{
  "thought": "...",
  "action": "...",
  "params": {{}}
}}

If action is finish, also include:
"final_answer": "..."
"""

